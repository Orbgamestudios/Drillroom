const fs = require('fs');
const vm = require('vm');
const path = require('path');

const dir = '/home/cgslinde/DrillRoom/DrillRoom';

// Create a sandbox window/global context with DOM stubs
const dummyElem = {
    onclick: null,
    addEventListener: () => {},
    style: {},
    classList: { add: () => {}, remove: () => {}, contains: () => false },
    innerHTML: '',
    appendChild: () => {},
};

const sandbox = {
    console: console,
    $: (id) => dummyElem,
    document: {
        getElementById: (id) => dummyElem,
        querySelector: (sel) => dummyElem,
        querySelectorAll: (sel) => [],
        createElement: (tag) => dummyElem,
        addEventListener: () => {},
        body: dummyElem,
    },
    localStorage: {
        getItem: () => null,
        setItem: () => {},
        removeItem: () => {},
    },
};
sandbox.window = sandbox;
sandbox.global = sandbox;

const context = vm.createContext(sandbox);

// Read script tags from DrillRoom.html
const html = fs.readFileSync(path.join(dir, 'DrillRoom.html'), 'utf8');
const scriptMatches = [...html.matchAll(/<script src=["'](.*?)["']><\/script>/g)].map(m => m[1]);

console.log(`Found ${scriptMatches.length} script tags in DrillRoom.html`);

// Execute each script in context
for (const scriptFile of scriptMatches) {
    if (scriptFile === 'gemini_analysis.js') continue;
    const filePath = path.join(dir, scriptFile);
    const code = fs.readFileSync(filePath, 'utf8');
    try {
        vm.runInContext(code, context, { filename: scriptFile });
    } catch (err) {
        console.error(`Error loading ${scriptFile}:`, err);
        process.exit(1);
    }
}

// Call autoRegisterExams
if (typeof sandbox.autoRegisterExams === 'function') {
    sandbox.autoRegisterExams();
} else {
    console.error('autoRegisterExams is not a function');
    process.exit(1);
}

const exams = sandbox.PRACTICE_EXAMS;
console.log(`\nSuccessfully registered ${exams.length} practice exams in PRACTICE_EXAMS!`);

const subjects = ['C/P', 'CARS', 'B/B', 'P/S'];
let allPassed = true;

const standardExams = exams.filter(e => !e.isHalf);
const halfExams = exams.filter(e => e.isHalf);

const full90s = standardExams.filter(e => e.duration === 90);
const full60s = standardExams.filter(e => e.duration === 60);

console.log(`Standard Full/Paced Exams: ${standardExams.length} (${full90s.length} 90m + ${full60s.length} 60m)`);
console.log(`Half-Section Exams: ${halfExams.length} (Expected ${full90s.length * 2}: ${full90s.length} Part 1 + ${full90s.length} Part 2)`);

if (standardExams.length < 56) {
    console.error(`[FAIL] Expected at least 56 standard exams, got ${standardExams.length}`);
    allPassed = false;
}
if (halfExams.length !== full90s.length * 2) {
    console.error(`[FAIL] Expected ${full90s.length * 2} half exams, got ${halfExams.length}`);
    allPassed = false;
}

// Validate standard exams
const summary = {};
for (const sec of subjects) {
    summary[sec] = { 90: [], 60: [] };
}

for (const exam of standardExams) {
    const sec = exam.sec;
    const dur = exam.duration;
    
    let qCount = 0;
    const keyDist = { A: 0, B: 0, C: 0, D: 0 };
    for (const set of exam.sets) {
        if (!set.qs) continue;
        for (const q of set.qs) {
            qCount++;
            const letter = ['A', 'B', 'C', 'D'][q.a];
            if (letter) keyDist[letter]++;
            if (!q.ch || q.ch.length !== 4) {
                console.error(`[FAIL] Exam ${exam.id} Q has ${q.ch ? q.ch.length : 0} choices!`);
                allPassed = false;
            }
            if (q.a === undefined || q.a < 0 || q.a > 3) {
                console.error(`[FAIL] Exam ${exam.id} Q has invalid answer index: ${q.a}`);
                allPassed = false;
            }
        }
    }
    summary[sec][dur].push({ id: exam.id, title: exam.label || exam.title, qCount, keyDist });
}

console.log('\n--- STANDARD EXAM REGISTRATION & QUESTION COUNTS ---');
for (const sec of subjects) {
    console.log(`\n### Subject: ${sec}`);
    for (const dur of [90, 60]) {
        console.log(`  Duration: ${dur} min (${summary[sec][dur].length} exams)`);
        for (const e of summary[sec][dur]) {
            console.log(`    - ${e.id.padEnd(12)}: ${e.qCount} Qs | Keys: A=${String(e.keyDist.A).padStart(2)} B=${String(e.keyDist.B).padStart(2)} C=${String(e.keyDist.C).padStart(2)} D=${String(e.keyDist.D).padStart(2)}`);
        }
    }
}

// Validate half-sections pairing and consistency
console.log('\n--- VERIFYING 45-MIN HALF-SECTION EXAMS ---');
for (const parent of full90s) {
    const h1 = halfExams.find(e => e.id === parent.id + '_h1');
    const h2 = halfExams.find(e => e.id === parent.id + '_h2');
    if (!h1 || !h2) {
        console.error(`[FAIL] Missing half-sections for parent ${parent.id}: h1=${!!h1}, h2=${!!h2}`);
        allPassed = false;
        continue;
    }
    const q1 = h1.sets.reduce((s, set) => s + (set.qs ? set.qs.length : 0), 0);
    const q2 = h2.sets.reduce((s, set) => s + (set.qs ? set.qs.length : 0), 0);
    const parentQ = parent.sets.reduce((s, set) => s + (set.qs ? set.qs.length : 0), 0);
    const isCars = parent.sec === 'CARS';

    const expectedQ1 = 24;
    const expectedQ2 = isCars ? 29 : 28;
    const expectedDur1 = isCars ? 41 : 42;
    const expectedDur2 = isCars ? 49 : 48;

    if (q1 !== expectedQ1 || q2 !== expectedQ2 || (q1 + q2) !== parentQ) {
        console.error(`[FAIL] Parent ${parent.id} split mismatch: Q1=${q1} (exp ${expectedQ1}), Q2=${q2} (exp ${expectedQ2}), Sum=${q1+q2} (parent ${parentQ})`);
        allPassed = false;
    }
    if (h1.duration !== expectedDur1 || h2.duration !== expectedDur2) {
        console.error(`[FAIL] Parent ${parent.id} duration mismatch: Dur1=${h1.duration} (exp ${expectedDur1}), Dur2=${h2.duration} (exp ${expectedDur2})`);
        allPassed = false;
    }
    if (h1.partnerId !== h2.id || h2.partnerId !== h1.id) {
        console.error(`[FAIL] Partner ID mismatch for ${parent.id}: h1.partner=${h1.partnerId}, h2.partner=${h2.partnerId}`);
        allPassed = false;
    }
}

console.log(`Validated all ${full90s.length} 90-min parent exams have perfectly paired, correctly timed halves!`);

if (allPassed && exams.length === standardExams.length + halfExams.length) {
    console.log(`\n>>> ALL ${exams.length} EXAMS (${standardExams.length} STANDARD + ${halfExams.length} HALF-SECTIONS) VALIDATED SUCCESSFULLY! <<<`);
} else {
    console.error(`\n>>> VALIDATION FAILED! (Total exams: ${exams.length}) <<<`);
    process.exit(1);
}
