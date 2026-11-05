const fs = require('fs');
const vm = require('vm');
const path = require('path');
const dir = '/home/cgslinde/DrillRoom/DrillRoom';

const dummyElem = {
    onclick: null, oninput: null, onchange: null, addEventListener: () => {},
    style: {}, classList: { add: () => {}, remove: () => {}, contains: () => false, toggle: () => {} },
    innerHTML: '', textContent: '', appendChild: () => {}, querySelector: () => dummyElem, querySelectorAll: () => [dummyElem],
    dataset: {}, value: '30'
};
const store = {};
const sandbox = {
    console: console, clearInterval: () => {}, setInterval: () => 1, timerId: 1,
    $: (id) => dummyElem,
    document: { getElementById: (id) => dummyElem, querySelector: (sel) => dummyElem, querySelectorAll: (sel) => [dummyElem], createElement: (tag) => ({ ...dummyElem }), addEventListener: () => {}, body: dummyElem },
    localStorage: { getItem: (k) => store[k] || null, setItem: (k, v) => { store[k] = String(v); }, removeItem: (k) => { delete store[k]; } },
    view: () => {}, tick: () => {}, flash: () => {}, paintHome: () => {},
    rawToScaled: (pct) => ({ score: Math.round(118 + (pct/100)*14), ptile: '50th' })
};
sandbox.window = sandbox; sandbox.global = sandbox; sandbox.globalThis = sandbox;
const context = vm.createContext(sandbox);

const html = fs.readFileSync(path.join(dir, 'DrillRoom.html'), 'utf8');
const scriptMatches = [...html.matchAll(/<script src=['"](.*?)['"]><\/script>/g)].map(m => m[1]);
for (const scriptFile of scriptMatches) {
    if (scriptFile === 'gemini_analysis.js') continue;
    const filePath = path.join(dir, scriptFile);
    const code = fs.readFileSync(filePath, 'utf8');
    try { vm.runInContext(code, context); } catch (e) { console.error(e); }
}

// Implement and test the functions in context
const codeToInject = `
function getQuestionArchetype(q, sec) {
  const text = ((q.q || "") + " " + ((q.ch || []).join(" "))).toLowerCase();
  if (sec === "CARS") {
    if (text.includes("main idea") || text.includes("central thesis") || text.includes("primary purpose") || text.includes("author's primary") || text.includes("best summarizes") || text.includes("title for the passage") || text.includes("overarching")) {
      return "Main Idea & Global Reasoning";
    }
    if (text.includes("attitude") || text.includes("tone") || text.includes("feel towards") || text.includes("perspective") || text.includes("author would most likely view") || text.includes("sentiment") || text.includes("author's reaction")) {
      return "Author Attitude & Tone";
    }
    if (text.includes("if ") || text.includes("suppose that") || text.includes("which of the following, if true") || text.includes("new discovery") || text.includes("scenario") || text.includes("apply to") || text.includes("analogous")) {
      return "Reasoning Beyond the Text";
    }
    if (text.includes("infer") || text.includes("implies") || text.includes("implicit") || text.includes("suggests") || text.includes("assumption") || text.includes("presupposes") || text.includes("unspoken")) {
      return "Inference & Implicit Assumption";
    }
    return "Foundations of Comprehension";
  } else {
    if (text.includes("calculate") || text.includes("value") || text.includes("approximate") || text.includes("molar") || text.includes("wavelength") || text.includes("energy") || text.includes("joules") || text.includes("current") || text.includes("velocity") || text.includes("ph of") || text.includes("half-life") || text.includes("concentration") || text.includes("ratio of") || text.includes("frequency") || text.includes("power") || text.includes("force")) {
      return "Calculation & Quantitative";
    }
    if (text.includes("figure") || text.includes("table") || text.includes("graph") || text.includes("data") || text.includes("plot") || text.includes("trend") || text.includes("shown in") || (text.includes("increase") && text.includes("decrease") && text.includes("rate"))) {
      return "Data Interpretation & Graphs";
    }
    if (text.includes("experiment") || text.includes("control") || text.includes("hypothesis") || text.includes("independent variable") || text.includes("dependent variable") || text.includes("assay") || text.includes("purification") || text.includes("gel") || text.includes("western blot") || text.includes("pcr") || text.includes("mutant") || text.includes("knockout")) {
      return "Experimental Design & Hypothesis";
    }
    if (text.includes("mechanism") || text.includes("pathway") || text.includes("inhibit") || text.includes("activate") || text.includes("enzyme") || text.includes("catalyze") || text.includes("substrate") || text.includes("receptor") || text.includes("cascade") || text.includes("allosteric") || text.includes("cleavage") || text.includes("metabolism") || text.includes("phosphorylation")) {
      return "Mechanism & Biochemical Logic";
    }
    return "Discrete Recall & Scientific Principle";
  }
}
window.getQuestionArchetype = getQuestionArchetype;

function parseExamNum(e) {
  const match = (e.suite || e.id || "").match(/exam(\\d+)/i);
  if (match) return parseInt(match[1]);
  const num = parseInt((e.suite || "").replace(/\\D/g, ""));
  return isNaN(num) ? 999 : num;
}

function getSortedSubjectPool(secKey) {
  const pool = PRACTICE_EXAMS.filter(e => e.sec === secKey && !e.isHalf);
  pool.sort((a, b) => {
    const na = parseExamNum(a);
    const nb = parseExamNum(b);
    if (na !== nb) return na - nb;
    return b.duration - a.duration;
  });
  return pool;
}

function getSubjectPassageQueue(secKey) {
  const peKey = "drillroom_pe_v1";
  let peData;
  try { peData = JSON.parse(localStorage.getItem(peKey)) || {}; } catch (e) { peData = {}; }

  const pool = getSortedSubjectPool(secKey);
  const queue = [];

  for (const ex of pool) {
    const r = peData[ex.id];
    if (r && r.done) continue;
    const completedSets = (r && Array.isArray(r.completedSets)) ? r.completedSets : [];
    for (let setIdx = 0; setIdx < ex.sets.length; setIdx++) {
      if (!completedSets.includes(setIdx)) {
        queue.push({
          exam: ex,
          examId: ex.id,
          setIndex: setIdx,
          set: ex.sets[setIdx]
        });
      }
    }
  }

  if (queue.length === 0) {
    for (const ex of pool) {
      for (let setIdx = 0; setIdx < ex.sets.length; setIdx++) {
        queue.push({
          exam: ex,
          examId: ex.id,
          setIndex: setIdx,
          set: ex.sets[setIdx],
          isReviewCycle: true
        });
      }
    }
  }

  return queue;
}

function getContinuousPassagePlan(secKey, targetPassages, selectedExamId) {
  const peKey = "drillroom_pe_v1";
  let peData;
  try { peData = JSON.parse(localStorage.getItem(peKey)) || {}; } catch (e) { peData = {}; }

  const fullQueue = getSubjectPassageQueue(secKey);
  const pool = getSortedSubjectPool(secKey);
  let pCount = Math.max(1, targetPassages || 1);

  let chosenQueueItems = [];

  if (selectedExamId && selectedExamId !== "auto") {
    const specificExam = pool.find(e => e.id === selectedExamId);
    if (specificExam) {
      const fromSpecific = fullQueue.filter(item => item.examId === selectedExamId);
      chosenQueueItems.push(...fromSpecific.slice(0, pCount));

      if (chosenQueueItems.length < pCount) {
        const remainingNeeded = pCount - chosenQueueItems.length;
        const others = fullQueue.filter(item => item.examId !== selectedExamId);
        chosenQueueItems.push(...others.slice(0, remainingNeeded));
      }
    }
  }

  if (chosenQueueItems.length === 0) {
    chosenQueueItems = fullQueue.slice(0, pCount);
  }

  const sets = chosenQueueItems.map(item => ({
    ...item.set,
    _sourceExamId: item.examId,
    _sourceSetIndex: item.setIndex,
    qs: [...item.set.qs]
  }));

  const sourceBreakdownMap = {};
  chosenQueueItems.forEach(item => {
    if (!sourceBreakdownMap[item.examId]) {
      sourceBreakdownMap[item.examId] = {
        examId: item.examId,
        label: item.exam.label,
        duration: item.exam.duration,
        setIndices: []
      };
    }
    sourceBreakdownMap[item.examId].setIndices.push(item.setIndex);
  });
  const sourceBreakdown = Object.values(sourceBreakdownMap);

  const totalQs = sets.reduce((sum, s) => sum + (s && s.qs ? s.qs.length : 0), 0);
  const secPerQ = secKey === "CARS" ? 101.8 : 96.6;
  const estMinutes = Math.max(2, Math.round((totalQs * secPerQ) / 60));

  return {
    sets,
    sourceBreakdown,
    totalPassages: sets.length,
    totalQs,
    estMinutes,
    isCombining: sourceBreakdown.length > 1,
    primaryExam: chosenQueueItems[0]?.exam || pool[0]
  };
}
`;

vm.runInContext(codeToInject, context);

// Test continuous queue:
// Suppose cars90 has 8 of its 9 sets completed, leaving only 1 set (set 8).
const peData = { cars90: { completedSets: [0, 1, 2, 3, 4, 5, 6, 7], done: false } };
context.localStorage.setItem('drillroom_pe_v1', JSON.stringify(peData));

const plan = context.getContinuousPassagePlan('CARS', 3, 'auto');
console.log('Continuous plan combining banks?:', plan.isCombining);
console.log('Source breakdown:', plan.sourceBreakdown);
if (!plan.isCombining) throw new Error('Expected plan to combine leftover bank from cars90 with cars60');
if (plan.sourceBreakdown[0].examId !== 'cars90' || plan.sourceBreakdown[0].setIndices.length !== 1) {
    throw new Error('Expected 1 set from cars90');
}
if (plan.sourceBreakdown[1].examId !== 'cars60' || plan.sourceBreakdown[1].setIndices.length !== 2) {
    throw new Error('Expected 2 sets from cars60');
}
console.log('>>> CONTINUOUS QUEUE COMBINATION TEST PASSED! <<<');

const gradingCode = `
function gradePracticeExam() {
  if (!E || !E._isPracticeExam) return;

  clearInterval(timerId);
  $("paused").classList.add("hide");
  $("tPause").classList.remove("on");

  const qs = E.s.qs;
  const n = qs.length;
  let right = 0, lucky = 0, shaky = 0;

  qs.forEach((q, k) => {
    const ok = E.ans[k] === q.a;
    if (ok) right++;
    if (ok && E.conf[k] === "guess") lucky++;
    if (ok && E.conf[k] === "two") shaky++;
  });

  const solid = right - lucky - shaky;
  const pct = Math.round(right / n * 100);
  const { score, ptile } = rawToScaled(pct);
  const pe = E._peRef;

  const peKey = "drillroom_pe_v1";
  let peData;
  try { peData = JSON.parse(localStorage.getItem(peKey)) || {}; } catch (e) { peData = {}; }

  const timeUsed = pe.exam.duration * 60 - E.left;

  // Process set completion across source breakdown
  if (pe.exam._sourceBreakdown && Array.isArray(pe.exam._sourceBreakdown)) {
    pe.exam._sourceBreakdown.forEach(src => {
      if (!peData[src.examId]) peData[src.examId] = { completedSets: [], done: false };
      const cSets = new Set(peData[src.examId].completedSets || []);
      src.setIndices.forEach(idx => cSets.add(idx));
      peData[src.examId].completedSets = Array.from(cSets);

      const srcExam = PRACTICE_EXAMS.find(e => e.id === src.examId);
      if (srcExam && peData[src.examId].completedSets.length >= srcExam.sets.length) {
        peData[src.examId].done = true;
        peData[src.examId].completedViaAdaptive = true;
        peData[src.examId].scaledScore = score;
        peData[src.examId].pct = pct;
      }
    });
  } else {
    if (!peData[pe.exam.id]) peData[pe.exam.id] = {};
    peData[pe.exam.id].done = true;
  }

  // Archetypes & Telemetry
  const archetypesMap = {};
  qs.forEach((q, idx) => {
    const arch = getQuestionArchetype(q, pe.exam.sec);
    if (!archetypesMap[arch]) archetypesMap[arch] = { name: arch, total: 0, right: 0, totalSecs: 0 };
    archetypesMap[arch].total++;
    if (E.ans[idx] === q.a) archetypesMap[arch].right++;
    archetypesMap[arch].totalSecs += (PE._qTimes[idx] || 0);
  });
  const archetypeList = Object.values(archetypesMap).map(a => ({
    ...a,
    avgSecs: Math.round(a.totalSecs / a.total),
    acc: Math.round((a.right / a.total) * 100)
  }));

  const timeSinkQuestions = qs.map((q, idx) => ({
    number: idx + 1,
    seconds: PE._qTimes[idx] || 0,
    isCorrect: E.ans[idx] === q.a,
    archetype: getQuestionArchetype(q, pe.exam.sec),
    conf: E.conf[idx] || "unrated"
  })).filter(x => x.seconds >= 110);

  const histId = "att_" + Date.now();
  const reviewData = {
    id: histId,
    examId: pe.exam.id,
    sec: pe.exam.sec,
    duration: pe.exam.duration,
    suiteTitle: pe.exam.suiteTitle,
    label: pe.exam.label,
    scaledScore: score,
    rawScore: right,
    totalQs: n,
    pct: pct,
    percentile: ptile,
    solid: solid,
    lucky: lucky,
    shaky: shaky,
    timeUsed: timeUsed,
    ts: Date.now(),
    _isAdaptive: !!pe.exam._isAdaptive,
    isHalf: !!pe.exam.isHalf,
    qs: qs.map((q, k) => ({
      q: q.q,
      ch: [...q.ch],
      a: q.a,
      e: q.e || "",
      why: q.why || null,
      d: !!q.d,
      ans: E.ans[k],
      conf: E.conf[k] || "-",
      time: PE._qTimes[k] || 0,
      archetype: getQuestionArchetype(q, pe.exam.sec),
      passage: q._passage || null,
      topic: q._topic || "",
      setIdx: q._setIdx
    })),
    passageStats: Object.entries(PE._passageReadState || {}).map(([sIdx, p]) => ({
      pIndex: parseInt(sIdx) + 1,
      wordCount: p.wordCount || 0,
      readSec: p.elapsedSec || 0,
      wpm: Math.round((p.wordCount / Math.max(1, p.elapsedSec)) * 60)
    })),
    telemetry: {
      qTimes: [...PE._qTimes],
      passageReadState: { ...PE._passageReadState },
      answerChangeAudit: {
        totalChanges: PE._answerChanges.length,
        rightToWrong: PE._answerChanges.filter(c => c.wasCorrect && !c.nowCorrect).length,
        wrongToRight: PE._answerChanges.filter(c => !c.wasCorrect && c.nowCorrect).length
      },
      archetypeStats: archetypeList,
      timeSinkQuestions: timeSinkQuestions
    }
  };

  peData[pe.exam.id] = {
    ...peData[pe.exam.id],
    done: true,
    scaledScore: score,
    rawScore: right,
    total: n,
    pct: pct,
    lastReview: reviewData
  };

  try { localStorage.setItem(peKey, JSON.stringify(peData)); } catch(e){}

  addHistoryEntry({
    id: histId,
    examId: pe.exam.id,
    sec: pe.exam.sec,
    duration: pe.exam.duration,
    type: "adaptive",
    label: pe.exam.label,
    scaledScore: score,
    rawScore: right,
    totalQs: n,
    pct: pct,
    percentile: ptile,
    solid: solid,
    lucky: lucky,
    shaky: shaky,
    timeUsed: timeUsed,
    ts: Date.now(),
    includedInAverage: true,
    reviewData: reviewData
  });
}
`;

vm.runInContext(gradingCode, context);

// Simulate the adaptive study section with plan
const studyExam = {
  id: 'study_test_comb',
  sec: 'CARS',
  suiteTitle: 'Adaptive Study',
  label: 'CARS Study (3 Passages)',
  duration: 30,
  sets: plan.sets,
  _isAdaptive: true,
  _sourceBreakdown: plan.sourceBreakdown
};

context.beginPracticeExam(studyExam); context.PE._qTimes = Array(context.PE.questions.length).fill(0); context.PE._answerChanges = [];
console.log('Active exam sets count:', context.PE.exam.sets.length);
console.log('Active questions count:', context.PE.questions.length);

// Answer all questions
context.PE.questions.forEach((q, idx) => {
  context.E.ans[idx] = q.a;
  context.E.conf[idx] = 'sure';
  context.PE._qTimes[idx] = 75; // 75 seconds per question
});
// Set passage read state
context.PE._passageReadState = {
  0: { reading: false, done: true, elapsedSec: 150, wordCount: 620 },
  1: { reading: false, done: true, elapsedSec: 160, wordCount: 590 },
  2: { reading: false, done: true, elapsedSec: 140, wordCount: 580 }
};

context.gradePracticeExam();

const updatedPeData = JSON.parse(context.localStorage.getItem('drillroom_pe_v1'));
console.log('cars90 status after session (should be done=true):', updatedPeData.cars90?.done);
console.log('cars90 completedSets length:', updatedPeData.cars90?.completedSets?.length);
console.log('cars60 status after session:', updatedPeData.cars60?.done);
console.log('cars60 completedSets:', updatedPeData.cars60?.completedSets);

if (!updatedPeData.cars90?.done) throw new Error('cars90 should be 100% completed!');
if (updatedPeData.cars90.completedSets.length !== 9) throw new Error('cars90 should have all 9 sets marked complete!');
if (updatedPeData.cars60.completedSets.length !== 2) throw new Error('cars60 should have 2 sets marked complete!');

const hist = context.getHistory();
console.log('History entries count:', hist.length);
console.log('Has reviewData attached?:', !!hist[0].reviewData);
console.log('PassageStats in reviewData:', hist[0].reviewData.passageStats);
console.log('ArchetypeStats in reviewData:', hist[0].reviewData.telemetry.archetypeStats);

console.log('>>> COMPLETE ADAPTIVE STUDY & REVIEW PACKET TEST PASSED! <<<');
