const fs = require('fs');
const vm = require('vm');
const path = require('path');

const dir = '/home/cgslinde/DrillRoom/DrillRoom';

const dummyElem = {
    onclick: null,
    oninput: null,
    onchange: null,
    addEventListener: () => {},
    style: {},
    classList: { add: () => {}, remove: () => {}, contains: () => false, toggle: () => {} },
    innerHTML: '',
    textContent: '',
    appendChild: () => {},
    querySelector: () => dummyElem,
    querySelectorAll: () => [dummyElem],
    dataset: {},
    value: '30'
};

const store = {};
const sandbox = {
    console: console,
    clearInterval: () => {},
    setInterval: () => 1,
    timerId: 1,
    $: (id) => dummyElem,
    document: {
        getElementById: (id) => dummyElem,
        querySelector: (sel) => dummyElem,
        querySelectorAll: (sel) => [dummyElem],
        createElement: (tag) => ({ ...dummyElem }),
        addEventListener: () => {},
        body: dummyElem,
    },
    localStorage: {
        getItem: (k) => store[k] || null,
        setItem: (k, v) => { store[k] = String(v); },
        removeItem: (k) => { delete store[k]; },
    },
    view: () => {},
    tick: () => {},
    flash: () => {},
    paintHome: () => {},
    rawToScaled: (pct) => ({ score: Math.round(118 + (pct/100)*14), ptile: '50th' })
};
sandbox.window = sandbox;
sandbox.global = sandbox;
sandbox.globalThis = sandbox;

const context = vm.createContext(sandbox);

// Read script tags from DrillRoom.html
const html = fs.readFileSync(path.join(dir, 'DrillRoom.html'), 'utf8');
const scriptMatches = [...html.matchAll(/<script src=["'](.*?)["']><\/script>/g)].map(m => m[1]);

for (const scriptFile of scriptMatches) {
    if (scriptFile === 'gemini_analysis.js') continue;
    const filePath = path.join(dir, scriptFile);
    const code = fs.readFileSync(filePath, 'utf8');
    try {
        vm.runInContext(code, context);
    } catch (e) {
        console.error(`Error executing ${scriptFile}:`, e);
    }
}

// 1. Verify getUncompletedExams
const { uncompleted, all } = context.getUncompletedExams('CARS');
console.log('Total CARS exams in all:', all.length, 'uncompleted:', uncompleted.length);
if (all.length !== 20 || uncompleted.length !== 20) {
    throw new Error(`Expected 20 CARS exams, got ${all.length}`);
}

// 2. Verify pickSourceExam
const pickedShort = context.pickSourceExam('CARS', 3, 'auto'); // 3 passages
console.log('Picked for 3 passages:', pickedShort.id, pickedShort.duration);
if (pickedShort.duration !== 90 && pickedShort.duration !== 60) throw new Error('Invalid picked exam duration');

const pickedLong = context.pickSourceExam('CARS', 8, 'auto'); // 8 passages requires 90m
console.log('Picked for 8 passages:', pickedLong.id, pickedLong.duration);
if (pickedLong.duration !== 90) throw new Error('Expected 90m exam for 8 passage session');

// 3. Test startAdaptiveStudy with 1 whole passage (minimum 1 passage, all questions intact)
console.log('\n--- Testing 1-Passage Adaptive Study (Min 1 Passage) ---');
const p1Qs = pickedShort.sets[0].qs.length;
context.startAdaptiveStudy(pickedShort, 1);
const PE = context.PE;
const E = context.E;
if (!PE || !E) throw new Error('PE/E not initialized');
console.log(`Active exam questions count for 1 passage: ${PE.questions.length} (Expected intact passage: ${p1Qs})`);
if (PE.questions.length !== p1Qs) throw new Error(`Expected all ${p1Qs} questions from Passage 1 intact, got ${PE.questions.length}`);
if (!PE.questions[0]._passage) throw new Error('Expected passage preserved for CARS Passage 1');

// Grade the 1-passage study
for (let i = 0; i < p1Qs; i++) {
    E.ans[i] = E.s.qs[i].a; // correct answer
    E.conf[i] = 'sure';
}
context.gradePracticeExam();

const hist1 = context.getHistory();
console.log('History entries after 1 Passage:', hist1.length);
const latest1 = hist1[0];
console.log('Latest history entry:', latest1.label, 'Score:', latest1.scaledScore, 'Qs:', latest1.totalQs);
if (latest1.totalQs !== p1Qs || latest1.type !== 'adaptive') throw new Error('Expected adaptive history entry with complete passage');

// Check peData: source exam must NOT be marked done after partial study!
const peData1 = JSON.parse(store['drillroom_pe_v1'] || '{}');
console.log(`Source exam ${pickedShort.id} done status:`, peData1[pickedShort.id]?.done);
if (peData1[pickedShort.id]?.done) throw new Error('Source exam should NOT be marked done after 1 passage!');

// 4. Test 2-Passage Adaptive Study (Both passages intact)
console.log('\n--- Testing 2-Passage Adaptive Study ---');
const p2ExpectedQs = pickedShort.sets[0].qs.length + pickedShort.sets[1].qs.length;
context.startAdaptiveStudy(pickedShort, 2);
console.log(`Active questions count for 2 passages: ${context.PE.questions.length} (Expected: ${p2ExpectedQs})`);
if (context.PE.questions.length !== p2ExpectedQs) throw new Error(`Expected intact passages totaling ${p2ExpectedQs} questions, got ${context.PE.questions.length}`);

for (let i = 0; i < p2ExpectedQs; i++) {
    context.E.ans[i] = context.E.s.qs[i].a;
    context.E.conf[i] = 'sure';
}
context.gradePracticeExam();
const hist2 = context.getHistory();
console.log('History entries after 2 Passages:', hist2.length);
console.log('Latest entry:', hist2[0].label, 'Score:', hist2[0].scaledScore, 'TotalQs:', hist2[0].totalQs);
if (hist2[0].totalQs !== p2ExpectedQs) throw new Error('Expected full questions from both passages in history');

// 5. Test Full Exam (All passages completed)
console.log('\n--- Testing Full Exam (All Passages) ---');
const allQs = pickedLong.sets.reduce((sum, s) => sum + s.qs.length, 0);
context.startAdaptiveStudy(pickedLong, pickedLong.sets.length);
console.log('Full exam questions count:', context.PE.questions.length, 'Expected:', allQs);
if (context.PE.questions.length !== allQs) throw new Error(`Expected ${allQs} questions for full exam`);
for (let i = 0; i < allQs; i++) {
    context.E.ans[i] = context.E.s.qs[i].a;
    context.E.conf[i] = 'sure';
}
context.gradePracticeExam();
const peDataFull = JSON.parse(store['drillroom_pe_v1'] || '{}');
console.log(`Source exam ${pickedLong.id} done status after full section:`, peDataFull[pickedLong.id]?.done);
if (!peDataFull[pickedLong.id]?.done) throw new Error('Source exam SHOULD be marked done after full section!');

// 6. Test that after cars90 is completed, pickSourceExam automatically advances to next uncompleted exam!
const nextPick = context.pickSourceExam('CARS', 3, 'auto');
console.log('Next picked exam after completion:', nextPick.id);
if (nextPick.id === pickedLong.id) throw new Error('Should have picked next uncompleted exam!');

// 7. Test Science adaptive study with whole passages
console.log('\n--- Testing C/P Science Adaptive Study with 1 Passage ---');
const cpExam = context.pickSourceExam('C/P', 1, 'auto');
const cpP1Qs = cpExam.sets[0].qs.length;
context.startAdaptiveStudy(cpExam, 1);
console.log(`C/P 1-passage questions count: ${context.PE.questions.length} (Expected: ${cpP1Qs})`);
if (context.PE.questions.length !== cpP1Qs) throw new Error(`Expected ${cpP1Qs} questions in C/P study`);
for (let i = 0; i < cpP1Qs; i++) {
    context.E.ans[i] = context.E.s.qs[i].a;
    context.E.conf[i] = 'sure';
}
context.gradePracticeExam();
const hist3 = context.getHistory();
console.log('Latest entry C/P:', hist3[0].label, 'Score:', hist3[0].scaledScore);

console.log('\n>>> ALL ADAPTIVE STUDY SIMULATION TESTS PASSED WITH 100% SUCCESS! <<<');
