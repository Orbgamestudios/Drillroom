const fs = require('fs');
const vm = require('vm');
const path = require('path');
const dir = '/home/cgslinde/DrillRoom/DrillRoom';

const elements = {};
function createMockElement(id) {
  const el = {
    id: id || '',
    tagName: 'DIV',
    style: {},
    classList: {
      _classes: new Set(),
      add(c) { this._classes.add(c); },
      remove(c) { this._classes.delete(c); },
      toggle(c, force) {
        if (force === undefined) {
          if (this._classes.has(c)) this._classes.delete(c);
          else this._classes.add(c);
        } else if (force) this._classes.add(c);
        else this._classes.delete(c);
      },
      contains(c) { return this._classes.has(c); }
    },
    dataset: {},
    children: [],
    appendChild(child) { this.children.push(child); return child; },
    removeChild(child) {
      const idx = this.children.indexOf(child);
      if (idx > -1) this.children.splice(idx, 1);
      return child;
    },
    querySelector(sel) {
      if (sel.startsWith('#')) {
        const targetId = sel.slice(1);
        return elements[targetId] || (elements[targetId] = createMockElement(targetId));
      }
      return createMockElement('sub_' + Math.random());
    },
    querySelectorAll(sel) {
      return [this.querySelector(sel)];
    },
    addEventListener(ev, fn) {},
    dispatchEvent(ev) {},
    scrollTop: 0,
    get innerHTML() { return this._html || ''; }, set innerHTML(val) { this._html = val; this.children = []; },
    textContent: '',
    value: '',
    disabled: false,
    checked: false
  };
  if (id) elements[id] = el;
  return el;
}

// Pre-create standard IDs
const standardIds = [
  'pass', 'qp', 'ebody', 'tSect', 'tCount', 'qno', 'qtx', 'fChk', 'fLbl', 'opts',
  'conf', 'bPrev', 'bNext', 'clk', 'padTxt', 'calcIn', 'calcOut', 'paused', 'tPause',
  'res', 'zT', 'zL', 'zS', 'zB', 'zV', 'zPass', 'zTimingTelemetry', 'zGeminiAnalysis', 'zList', 'zSave',
  'tabPractice', 'tabHistory', 'nT', 'nav'
];
standardIds.forEach(id => createMockElement(id));

const store = {};
const sandbox = {
  console: console,
  clearInterval: () => {},
  setInterval: () => 1,
  timerId: 1,
  strike: false,
  $: (id) => elements[id] || (elements[id] = createMockElement(id)),
  document: {
    getElementById: (id) => elements[id] || (elements[id] = createMockElement(id)),
    querySelector: (sel) => {
      if (sel.startsWith('#')) return elements[sel.slice(1)] || (elements[sel.slice(1)] = createMockElement(sel.slice(1)));
      return createMockElement();
    },
    querySelectorAll: () => [createMockElement()],
    createElement: (tag) => {
      const el = createMockElement();
      el.tagName = tag.toUpperCase();
      return el;
    },
    addEventListener: () => {},
    body: createMockElement('body')
  },
  localStorage: {
    getItem: (k) => store[k] || null,
    setItem: (k, v) => { store[k] = String(v); },
    removeItem: (k) => { delete store[k]; }
  },
  view: () => {},
  tick: () => {},
  flash: (m) => console.log('FLASH:', m),
  paintHome: () => {},
  rawToScaled: (pct) => ({ score: Math.round(118 + (pct/100)*14), ptile: '50th' })
};
sandbox.window = sandbox; sandbox.window.addEventListener = () => {};
sandbox.global = sandbox;
sandbox.globalThis = sandbox;

const context = vm.createContext(sandbox);

// Load all script files in order
const html = fs.readFileSync(path.join(dir, 'DrillRoom.html'), 'utf8');
const scriptMatches = [...html.matchAll(/<script src=['"](.*?)['"]><\/script>/g)].map(m => m[1]);
for (const scriptFile of scriptMatches) {
  const filePath = path.join(dir, scriptFile);
  const code = fs.readFileSync(filePath, 'utf8');
  try {
    vm.runInContext(code, context);
  } catch (e) {
    console.error('Error in ' + scriptFile, e);
  }
}

console.log('\n--- 1. Testing Continuous Passage Queue & Multi-Bank Combining ---');
// Setup: cars90 has 8 of 9 sets completed, 1 set remaining
store['drillroom_pe_v1'] = JSON.stringify({
  cars90: { completedSets: [0, 1, 2, 3, 4, 5, 6, 7], done: false }
});

const plan = context.getContinuousPassagePlan('CARS', 3, 'auto');
console.log('Is combining multiple banks?:', plan.isCombining);
console.log('Total passages planned:', plan.totalPassages);
console.log('Source breakdown:', plan.sourceBreakdown.map(b => b.examId + ' (' + b.setIndices.length + ' sets)'));

if (!plan.isCombining) throw new Error('Expected continuous queue to combine leftover cars90 with cars60');
if (plan.sourceBreakdown[0].examId !== 'cars90' || plan.sourceBreakdown[0].setIndices.length !== 1) {
  throw new Error('Expected 1 set from cars90');
}
if (plan.sourceBreakdown[1].examId !== 'cars60' || plan.sourceBreakdown[1].setIndices.length !== 2) {
  throw new Error('Expected 2 sets from cars60');
}

console.log('\n--- 2. Testing Adaptive Study Session Launch with Timing Telemetry ---');
context.startAdaptiveStudy('CARS', 3, plan.estMinutes);
const PE = context.PE;
const E = context.E;
if (!PE || !E) throw new Error('Exam state not initialized');
console.log('Session total questions:', PE.questions.length);
console.log('Session passage read mode active?:', PE._activeMode);
if (PE._activeMode !== 'passage') throw new Error('Session should start in passage reading mode');

// Simulate reading passage 0 for 145 seconds
PE._passageReadState[0] = { reading: true, done: false, elapsedSec: 145, wordCount: 610 };
// Click Done Reading Passage button
context.finishReadingPassage(0);
console.log('Passage 0 read status after clicking Done Reading:', PE._passageReadState[0].done);
console.log('Active mode after finishing reading:', PE._activeMode);
if (!PE._passageReadState[0].done || PE._activeMode !== 'question') {
  throw new Error('Should transition to question answering mode');
}

// Test smart auto-transition on Question 6 (which is in passage 1):
// Jump to Question 6
E.i = 6;
const q6SetIdx = E.s.qs[6]._setIdx;
console.log('Question 6 is in passage set index:', q6SetIdx);
context.drawPEQ();
console.log('Passage 1 reading state initially done?:', PE._passageReadState[q6SetIdx]?.done);

// Simulate user clicking an answer choice directly without clicking "Done Reading" button:
const optBtn = elements['opts'].children[0] || { onclick: null };
// Draw sets up opt buttons:
const optClick = elements['opts'].children[1]?.onclick;
if (optClick) optClick();
console.log('Passage 1 reading state after selecting an answer (smart auto-finish):', PE._passageReadState[q6SetIdx]?.done);
if (!PE._passageReadState[q6SetIdx]?.done) {
  throw new Error('Selecting an answer should auto-finish passage reading');
}

// Test second-guessing tracking
E.i = 0;
// First answer was choice 0
PE._firstAnswers[0] = 0;
E.ans[0] = 0;
// Now user changes answer to choice 1
elements['opts'].children[1]?.onclick();
console.log('Answer changes recorded:', PE._answerChanges.length);
if (PE._answerChanges.length !== 1) throw new Error('Expected 1 answer change recorded');

console.log('\n--- 3. Testing Exam Grading & Zero Leftovers Completion ---');
// Fill in all answers
PE.questions.forEach((q, idx) => {
  E.ans[idx] = q.a;
  E.conf[idx] = 'sure';
  PE._qTimes[idx] = 80;
});
PE._passageReadState = {
  0: { reading: false, done: true, elapsedSec: 145, wordCount: 610 },
  1: { reading: false, done: true, elapsedSec: 155, wordCount: 590 },
  2: { reading: false, done: true, elapsedSec: 140, wordCount: 580 }
};

context.gradePracticeExam();

const updatedPeData = JSON.parse(store['drillroom_pe_v1'] || '{}');
console.log('cars90 100% completed status (zero leftovers):', updatedPeData.cars90?.done);
console.log('cars90 total completed sets:', updatedPeData.cars90?.completedSets?.length, '/ 9');
console.log('cars60 sets completed from this session:', updatedPeData.cars60?.completedSets);

if (!updatedPeData.cars90?.done) throw new Error('cars90 should be marked 100% done!');
if (updatedPeData.cars90.completedSets.length !== 9) throw new Error('cars90 should have 9 completed sets');
if (updatedPeData.cars60.completedSets.length !== 2) throw new Error('cars60 should have 2 sets completed');

console.log('\n--- 4. Testing Telemetry Rendering & Review Packet ---');
const timingHtml = elements['zTimingTelemetry'].innerHTML;
console.log('Telemetry box rendered?:', timingHtml.includes('pe-telemetry-box'));
console.log('Passage reading table included?:', timingHtml.includes('Passage Reading Speed'));
console.log('Question archetypes table included?:', timingHtml.includes('Question Archetype Pacing'));
console.log('Second-guessing audit included?:', timingHtml.includes('Second-Guessing Audit'));

if (!timingHtml.includes('pe-telemetry-box') || !timingHtml.includes('Passage Reading Speed')) {
  throw new Error('Telemetry box not properly rendered in #zTimingTelemetry');
}

const listChildren = elements['zList'].children.length;
console.log('Total review questions rendered in #zList:', listChildren);
if (listChildren !== PE.questions.length) {
  throw new Error('Expected all questions rendered in review list');
}

console.log('\n--- 5. Testing openCompletedExamReview from History ---');
const hist = context.getHistory();
console.log('History entries count:', hist.length);
const attemptId = hist[0].id;

// Clear DOM elements
elements['zT'].innerHTML = '';
elements['zTimingTelemetry'].innerHTML = '';
elements['zList'].children = [];

// Re-open review
context.openCompletedExamReview(attemptId);
console.log('Score rendered on re-review:', elements['zT'].innerHTML.includes('132'));
console.log('Timing telemetry restored on re-review:', elements['zTimingTelemetry'].innerHTML.includes('Timing Telemetry'));
console.log('Questions restored on re-review:', elements['zList'].children.length);

if (!elements['zT'].innerHTML.includes('132') || elements['zList'].children.length !== PE.questions.length) {
  throw new Error('openCompletedExamReview failed to restore exam review state');
}

console.log('\n--- 6. Testing Legacy Review Reconstruction (Previous Attempts) ---');
// Create a mock legacy record without reviewData
const legacyRec = {
  id: 'legacy_test_01',
  examId: 'cars60',
  sec: 'CARS',
  duration: 60,
  label: 'Critical Analysis and Reasoning Skills (60 min)',
  scaledScore: 126,
  rawScore: 22,
  totalQs: 30,
  pct: 73,
  percentile: '65th',
  solid: 18,
  lucky: 2,
  shaky: 2,
  timeUsed: 3400,
  ts: Date.now() - 100000
};
hist.push(legacyRec);
context.saveHistory(hist);

// Open review for legacy record
context.openCompletedExamReview('legacy_test_01');
console.log('Legacy review questions restored:', elements['zList'].children.length);
if (elements['zList'].children.length === 0) {
  throw new Error('Legacy review reconstruction failed');
}

console.log('\n--- 7. Testing UI Paint (Practice & History Tabs with Review Buttons) ---');
context.paintPracticeExams();
function serializeEl(el) { let s = el.innerHTML || ''; for(const c of el.children) s += serializeEl(c); return s; }
const practiceHtml = serializeEl(elements['tabPractice']);
console.log('Adaptive slider rendered in tabPractice?:', practiceHtml.includes('pe-slider-box'));
console.log('Continuous queue alert present?:', practiceHtml.includes('peComboAlert'));

context.paintHistory();
const historyHtml = serializeEl(elements['tabHistory']);
console.log('Review & AI button rendered in history rows?:', historyHtml.includes('Review &amp; AI'));
if (!historyHtml.includes('Review &amp; AI')) {
  throw new Error('Review & AI button missing from history table');
}

console.log('\n========================================================');
console.log('>>> ALL VERIFICATION TESTS PASSED WITH 100% SUCCESS! <<<');
console.log('========================================================\n');
