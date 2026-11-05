const fs = require('fs');
const vm = require('vm');
const path = require('path');

const dir = '/home/cgslinde/DrillRoom/DrillRoom';

const memoryStorage = {};
const dummyElem = {
    onclick: null,
    addEventListener: () => {},
    style: {},
    classList: { add: () => {}, remove: () => {}, contains: () => false, toggle: () => {} },
    innerHTML: '',
    appendChild: () => {},
    querySelector: () => dummyElem,
    querySelectorAll: () => []
};

const sandbox = {
    console: console,
    $: (id) => dummyElem,
    document: {
        getElementById: (id) => dummyElem,
        querySelector: (sel) => dummyElem,
        querySelectorAll: (sel) => [],
        createElement: (tag) => ({ ...dummyElem }),
        addEventListener: () => {},
        body: dummyElem,
    },
    localStorage: {
        getItem: (k) => memoryStorage[k] || null,
        setItem: (k, v) => { memoryStorage[k] = String(v); },
        removeItem: (k) => { delete memoryStorage[k]; },
        clear: () => { Object.keys(memoryStorage).forEach(k => delete memoryStorage[k]); }
    },
    confirm: () => true,
    alert: () => {},
    flash: () => {},
    triggerConfetti: () => {},
    renderGeminiAnalysisBanner: () => {},
    clearInterval: () => {},
    setInterval: () => 123,
    view: () => {},
    paintHome: () => {},
    post: () => {},
    tick: () => {},
    strike: false,
    hl: false,
    timerId: null
};
sandbox.window = sandbox;
sandbox.global = sandbox;

const context = vm.createContext(sandbox);

// Load all scripts from DrillRoom.html
const html = fs.readFileSync(path.join(dir, 'DrillRoom.html'), 'utf8');
const scriptMatches = [...html.matchAll(/<script src=["'](.*?)["']><\/script>/g)].map(m => m[1]);

for (const scriptFile of scriptMatches) {
    if (scriptFile === 'gemini_analysis.js') continue;
    const filePath = path.join(dir, scriptFile);
    const code = fs.readFileSync(filePath, 'utf8');
    vm.runInContext(code, context, { filename: scriptFile });
}

// Auto-register exams
sandbox.autoRegisterExams();

const exams = sandbox.PRACTICE_EXAMS;
const h1 = exams.find(e => e.id === 'cp90_h1');
const h2 = exams.find(e => e.id === 'cp90_h2');
const parent = exams.find(e => e.id === 'cp90');

if (!h1 || !h2 || !parent) {
    console.error('Failed to find cp90_h1, cp90_h2, or cp90');
    process.exit(1);
}

console.log(`Testing Part 1: ${h1.id} (${h1.duration} min, ${h1.sets.reduce((s,x)=>s+x.qs.length, 0)} Qs)`);
console.log(`Testing Part 2: ${h2.id} (${h2.duration} min, ${h2.sets.reduce((s,x)=>s+x.qs.length, 0)} Qs)`);
console.log(`Parent: ${parent.id} (${parent.duration} min, ${parent.sets.reduce((s,x)=>s+x.qs.length, 0)} Qs)`);

// 1. Simulate taking Part 1 (cp90_h1)
sandbox.beginPracticeExam(h1);
const qs1 = sandbox.E.s.qs;
console.log(`Part 1 questions loaded: ${qs1.length}`);

// Answer 20 correct out of 24
for (let i = 0; i < qs1.length; i++) {
    sandbox.E.ans[i] = (i < 20) ? qs1[i].a : ((qs1[i].a + 1) % 4);
    sandbox.E.conf[i] = 'sure';
}

// Grade Part 1
sandbox.gradePracticeExam();

let peData = JSON.parse(memoryStorage['drillroom_pe_v1'] || '{}');
let hist = sandbox.getHistory();

console.log('\n--- AFTER GRADING PART 1 ---');
console.log(`peData['cp90_h1']:`, peData['cp90_h1'] ? {
    done: peData['cp90_h1'].done,
    score: peData['cp90_h1'].score,
    total: peData['cp90_h1'].total,
    scaledScore: peData['cp90_h1'].scaledScore,
    pct: peData['cp90_h1'].pct
} : 'MISSING');

console.log(`peData['cp90'] (Parent should NOT be done yet):`, peData['cp90'] ? peData['cp90'] : 'NOT SET (CORRECT)');
console.log(`History entries: ${hist.length}`);
const h1Hist = hist.find(x => x.examId === 'cp90_h1');
console.log(`Part 1 in history:`, h1Hist ? `Scaled: ${h1Hist.scaledScore}, ${h1Hist.rawScore}/${h1Hist.totalQs} (${h1Hist.pct}%)` : 'MISSING');

if (!peData['cp90_h1']?.done || peData['cp90']?.done || !h1Hist) {
    console.error('Part 1 grading assertions failed!');
    process.exit(1);
}

// 2. Simulate taking Part 2 (cp90_h2)
sandbox.beginPracticeExam(h2);
const qs2 = sandbox.E.s.qs;
console.log(`\nPart 2 questions loaded: ${qs2.length}`);

// Answer 22 correct out of 28
for (let i = 0; i < qs2.length; i++) {
    sandbox.E.ans[i] = (i < 22) ? qs2[i].a : ((qs2[i].a + 1) % 4);
    sandbox.E.conf[i] = 'sure';
}

// Grade Part 2
sandbox.gradePracticeExam();

peData = JSON.parse(memoryStorage['drillroom_pe_v1'] || '{}');
hist = sandbox.getHistory();

console.log('\n--- AFTER GRADING PART 2 ---');
console.log(`peData['cp90_h2']:`, peData['cp90_h2'] ? {
    done: peData['cp90_h2'].done,
    score: peData['cp90_h2'].score,
    total: peData['cp90_h2'].total,
    scaledScore: peData['cp90_h2'].scaledScore,
    pct: peData['cp90_h2'].pct
} : 'MISSING');

console.log(`peData['cp90'] (Parent should now be DONE via halves):`, peData['cp90'] ? {
    done: peData['cp90'].done,
    completedViaHalves: peData['cp90'].completedViaHalves,
    score: peData['cp90'].score,
    total: peData['cp90'].total,
    scaledScore: peData['cp90'].scaledScore,
    pct: peData['cp90'].pct
} : 'MISSING');

console.log(`Total history entries: ${hist.length}`);
const combHist = hist.find(x => x.isCombinedFromHalves && x.examId === 'cp90');
console.log(`Combined 90m in history:`, combHist ? `Scaled: ${combHist.scaledScore}, ${combHist.rawScore}/${combHist.totalQs} (${combHist.pct}%)` : 'MISSING');

// Assertions
if (!peData['cp90_h2']?.done) {
    console.error('Part 2 not marked done in peData!');
    process.exit(1);
}
if (!peData['cp90']?.done || !peData['cp90']?.completedViaHalves) {
    console.error('Parent exam cp90 was NOT marked done via halves!');
    process.exit(1);
}
if (peData['cp90'].score !== (20 + 22) || peData['cp90'].total !== 52) {
    console.error(`Parent score mismatch: got ${peData['cp90'].score}/${peData['cp90'].total}, expected 42/52`);
    process.exit(1);
}
if (!combHist) {
    console.error('Combined 90m history entry missing!');
    process.exit(1);
}

// 3. Test rolling averages for both 45m and 90m filters
const roll45 = sandbox.calculateRollingAverage(hist, { dur: '45', sec: 'all', window: '5' });
console.log('\n--- ROLLING AVERAGE FILTER FOR 45m ---');
console.log(`45m Count: ${roll45?.count}, AvgScaled: ${roll45?.avgScaled}, Accuracy: ${roll45?.avgPct}%`);

const roll90 = sandbox.calculateRollingAverage(hist, { dur: '90', sec: 'all', window: '5' });
console.log('\n--- ROLLING AVERAGE FILTER FOR 90m ---');
console.log(`90m Count: ${roll90?.count}, AvgScaled: ${roll90?.avgScaled}, Accuracy: ${roll90?.avgPct}%`);

if (!roll45 || roll45.count !== 2) {
    console.error('Rolling avg for 45m should have 2 attempts!');
    process.exit(1);
}
if (!roll90 || roll90.count !== 1) {
    console.error('Rolling avg for 90m should have 1 combined attempt!');
    process.exit(1);
}

// 4. Test deleting Part 1 removes parent completion
console.log('\n--- TESTING DELETION OF PART 1 ---');
sandbox.deleteHistoryEntry(h1Hist.id);
peData = JSON.parse(memoryStorage['drillroom_pe_v1'] || '{}');
hist = sandbox.getHistory();

console.log(`Part 1 in peData after deletion:`, peData['cp90_h1'] ? 'PRESENT (ERROR)' : 'REMOVED (CORRECT)');
console.log(`Parent cp90 in peData after deletion:`, peData['cp90'] ? 'STILL PRESENT (ERROR)' : 'CLEARED (CORRECT)');
console.log(`Combined cp90 in history:`, hist.some(x => x.isCombinedFromHalves && x.examId === 'cp90') ? 'PRESENT (ERROR)' : 'CLEARED (CORRECT)');

if (peData['cp90_h1'] || peData['cp90'] || hist.some(x => x.isCombinedFromHalves && x.examId === 'cp90')) {
    console.error('Deletion cascading failed!');
    process.exit(1);
}

// 5. Test CARS half-sections (cars90_h1 & cars90_h2)
console.log('\n--- TESTING CARS 90 HALF-SECTIONS ---');
const carsH1 = exams.find(e => e.id === 'cars90_h1');
const carsH2 = exams.find(e => e.id === 'cars90_h2');
const carsParent = exams.find(e => e.id === 'cars90');

sandbox.beginPracticeExam(carsH1);
for (let i = 0; i < sandbox.E.s.qs.length; i++) {
    sandbox.E.ans[i] = sandbox.E.s.qs[i].a; // 100%
    sandbox.E.conf[i] = 'sure';
}
sandbox.gradePracticeExam();

sandbox.beginPracticeExam(carsH2);
for (let i = 0; i < sandbox.E.s.qs.length; i++) {
    sandbox.E.ans[i] = sandbox.E.s.qs[i].a; // 100%
    sandbox.E.conf[i] = 'sure';
}
sandbox.gradePracticeExam();

peData = JSON.parse(memoryStorage['drillroom_pe_v1'] || '{}');
console.log('cars90 parent completion:', peData['cars90'] ? {
    done: peData['cars90'].done,
    completedViaHalves: peData['cars90'].completedViaHalves,
    score: peData['cars90'].score,
    total: peData['cars90'].total,
    scaledScore: peData['cars90'].scaledScore
} : 'MISSING');

if (!peData['cars90']?.done || peData['cars90'].total !== 53 || peData['cars90'].score !== 53 || peData['cars90'].scaledScore !== 132) {
    console.error('CARS half-section combination failed!');
    process.exit(1);
}

console.log('\n>>> ALL HALF-SECTION GRADING & INTEGRATION TESTS PASSED WITH 100% ACCURACY! <<<');
