/**
 * scratch/test_cross_exam_deduplication.js
 * Verification of Cross-Exam Deduplication and Bidirectional Synchronization
 * between 90-minute, 60-minute, and half-section practice exams.
 */

const fs = require('fs');
const vm = require('vm');
const path = require('path');

let testsPassed = 0;
let testsFailed = 0;

function assert(cond, msg) {
  if (cond) {
    console.log(`  ✓ ${msg}`);
    testsPassed++;
  } else {
    console.error(`  ✗ FAIL: ${msg}`);
    testsFailed++;
  }
}

console.log('=== TEST SUITE: Cross-Exam Passage Deduplication & Sync ===\n');

// Set up mock DOM and storage environment
const elements = {};
function createMockElement(id = '') {
  return {
    id: id,
    className: '',
    classList: {
      _classes: new Set(),
      add(c) { this._classes.add(c); },
      remove(c) { this._classes.delete(c); },
      toggle(c, f) {
        if (f === undefined) f = !this._classes.has(c);
        f ? this._classes.add(c) : this._classes.delete(c);
        return f;
      },
      contains(c) { return this._classes.has(c); }
    },
    style: {},
    children: [],
    dataset: {},
    appendChild(child) { this.children.push(child); return child; },
    insertBefore(newChild) { this.children.unshift(newChild); return newChild; },
    querySelector() { return null; },
    querySelectorAll() { return []; },
    addEventListener() {},
    setAttribute() {},
    getAttribute() { return null; },
    getBoundingClientRect() { return { top: 0, bottom: 0, left: 0, right: 0, width: 800, height: 600 }; }
  };
}

function $(id) {
  if (!elements[id]) elements[id] = createMockElement(id);
  return elements[id];
}

let mockStorage = {};
const ctx = {
  window: {},
  document: {
    getElementById: $,
    addEventListener() {},
    createElement: (tag) => createMockElement(tag),
    body: createMockElement('body'),
    querySelectorAll: () => []
  },
  localStorage: {
    getItem: (k) => mockStorage[k] || null,
    setItem: (k, v) => { mockStorage[k] = String(v); },
    removeItem: (k) => { delete mockStorage[k]; },
    clear: () => { mockStorage = {}; }
  },
  $: $,
  console: console,
  setTimeout: () => 0,
  clearTimeout: () => {},
  setInterval: () => 0,
  clearInterval: () => {},
  confirm: () => true,
  alert: () => {},
  view: () => {},
  tick: () => {}
};
ctx.global = ctx;
ctx.globalThis = ctx;
ctx.window = ctx;
vm.createContext(ctx);

// Load all exam files and practice_exam.js
const htmlContent = fs.readFileSync(path.join(__dirname, '../DrillRoom.html'), 'utf8');
const scriptMatches = [...htmlContent.matchAll(/<script src="([^"]+)"><\/script>/g)].map(m => m[1]);

for (const s of scriptMatches) {
  if (s.startsWith('exam_') || s === 'practice_exam.js') {
    const code = fs.readFileSync(path.join(__dirname, '../' + s), 'utf8');
    vm.runInContext(code, ctx);
  }
}
ctx.autoRegisterExams();

console.log('1. Verifying Passage Fingerprinting Consistency:');
const cars90 = ctx.PRACTICE_EXAMS.find(e => e.id === 'cars90');
const cars60 = ctx.PRACTICE_EXAMS.find(e => e.id === 'cars60');
const cp90 = ctx.PRACTICE_EXAMS.find(e => e.id === 'cp90');
const cp60 = ctx.PRACTICE_EXAMS.find(e => e.id === 'cp60');

assert(cars90 && cars60, 'Both cars90 and cars60 are registered');
assert(cp90 && cp60, 'Both cp90 and cp60 are registered');

// Test that all 6 shared passages in CARS60 match CARS90 exactly
for (let i = 0; i < cars60.sets.length; i++) {
  const fp60 = ctx.getPassageFingerprint(cars60.sets[i]);
  const fp90 = ctx.getPassageFingerprint(cars90.sets[i]);
  assert(fp60 === fp90 && fp60.startsWith('p:'), `CARS Passage ${i + 1} fingerprint matches between 60m and 90m`);
}

// Test that CP60 passages match CP90 passages
for (let i = 0; i < 5; i++) {
  const fp60 = ctx.getPassageFingerprint(cp60.sets[i]);
  const fp90 = ctx.getPassageFingerprint(cp90.sets[i]);
  assert(fp60 === fp90 && fp60.startsWith('p:'), `CP Passage ${i + 1} fingerprint matches between 60m and 90m`);
}

// Test discrete set fingerprint
const fp_cp60_disc = ctx.getPassageFingerprint(cp60.sets[5]);
const fp_cp90_disc = ctx.getPassageFingerprint(cp90.sets[7]);
assert(fp_cp60_disc === fp_cp90_disc && fp_cp60_disc.startsWith('dset:'), 'CP Discrete question sets share fingerprint between 60m and 90m');

console.log('\n2. Verifying getSubjectPassageQueue Deduplication (Fresh State):');
mockStorage = {};

for (const sec of ['CARS', 'C/P', 'B/B', 'P/S']) {
  const q = ctx.getSubjectPassageQueue(sec);
  const seenFps = new Set();
  let duplicateCount = 0;
  q.forEach(item => {
    if (seenFps.has(item.fingerprint)) duplicateCount++;
    seenFps.add(item.fingerprint);
  });
  assert(duplicateCount === 0, `${sec} queue contains 0 duplicate passages (total: ${q.length} unique sets)`);
}

console.log('\n3. Verifying Bidirectional Synchronization (Completing 60m Exam):');
mockStorage = {};
let peData = {};

// Complete all sets of CARS60
cars60.sets.forEach((set, sIdx) => {
  const fp = ctx.getPassageFingerprint(set);
  ctx.syncCompletedPassageToAllExams(fp, 'cars60', sIdx, peData);
});
mockStorage['drillroom_pe_v1'] = JSON.stringify(peData);

assert(peData['cars60'] && peData['cars60'].done === true, 'CARS60 marked done in peData');
assert(peData['cars90'] && peData['cars90'].done === false, 'CARS90 NOT marked done (has 3 fresh passages remaining)');
assert(peData['cars90'].completedSets.length === 6, 'CARS90 has exactly 6 completedSets cross-registered');
assert(peData['cars90_h1'] && peData['cars90_h1'].done === true, 'CARS90 Half 1 marked done (all 4 passages were in CARS60)');

// Check queue after CARS60 completion
const qCARSAfter60 = ctx.getSubjectPassageQueue('CARS');
const cars60Fps = new Set(cars60.sets.map(s => ctx.getPassageFingerprint(s)));
const hasAnyCars60 = qCARSAfter60.some(item => cars60Fps.has(item.fingerprint));
assert(!hasAnyCars60, 'getSubjectPassageQueue(CARS) contains ZERO passages that were completed in CARS60');
assert(qCARSAfter60.length === 90 - 6, `CARS queue decremented by exactly 6 sets (expected 84, got ${qCARSAfter60.length})`);

console.log('\n4. Verifying Direct Exam Launch with Completed Sets (Auto-Skip):');
// Now launch CARS90 directly. Sets 0-5 should be pre-skipped, starting at Passage 7 (Q37, index 36)
ctx.beginPracticeExam(cars90);

assert(ctx.E.s.id === 'cars90', 'Active exam is cars90');
assert(ctx.E.i === 36, `Active question auto-advanced to Question 37 (idx 36) (got idx ${ctx.E.i})`);
const skippedInExam = ctx.E.s.qs.filter(q => q._isSkipped).length;
assert(skippedInExam === 36, `Exactly 36 questions (Passages 1-6 in 90m) are pre-skipped (got ${skippedInExam})`);
assert(ctx.PE._autoSkippedPassagesCount === 6, 'PE._autoSkippedPassagesCount is 6');

// Verify that navigator reflects skipped status
let navHtml = '';
ctx.E.s.qs.forEach((q, k) => {
  const isSk = q._isSkipped || ctx.E.ans[k] === -1 || ctx.E.conf[k] === 'skipped';
  if (isSk) navHtml += `Q${k + 1}: Skipped; `;
});
assert(navHtml.includes('Q1: Skipped') && navHtml.includes('Q36: Skipped'), 'Navigator marks questions 1-36 as skipped');
assert(!navHtml.includes('Q37: Skipped'), 'Question 37 is not skipped');

console.log('\n5. Verifying Grade Practice Exam with Auto-Skipped Sets:');
// Answer the remaining 17 questions (Qs 37-53, indices 36-52)
for (let idx = 36; idx < ctx.E.s.qs.length; idx++) {
  ctx.E.ans[idx] = ctx.E.s.qs[idx].a; // Answer correctly
  ctx.E.conf[idx] = 'sure';
}
ctx.gradePracticeExam();

const cars90Data = JSON.parse(mockStorage['drillroom_pe_v1'])['cars90'];
assert(cars90Data && cars90Data.done === true, 'CARS90 marked done after completion');
assert(cars90Data.scoredTotal === 17, `Scored total is 17 (excluded 36 skipped questions, got ${cars90Data.scoredTotal})`);
assert(cars90Data.score === 17, `Raw score is 17 (got ${cars90Data.score})`);
assert(cars90Data.pct === 100, `Raw accuracy is 100% (got ${cars90Data.pct}%)`);

console.log('\n6. Verifying Completing Full 90m Syncs Counterpart 60m Exam:');
mockStorage = {};
peData = {};
cars90.sets.forEach((set, sIdx) => {
  const fp = ctx.getPassageFingerprint(set);
  ctx.syncCompletedPassageToAllExams(fp, 'cars90', sIdx, peData);
});
assert(peData['cars90'].done === true, 'cars90 marked done');
assert(peData['cars60'].done === true, 'cars60 marked done automatically');
assert(peData['cars90_h1'].done === true, 'cars90_h1 marked done automatically');
assert(peData['cars90_h2'].done === true, 'cars90_h2 marked done automatically');

console.log('\n7. Verifying Migration of Legacy Storage:');
const legacyData = {
  cp90: { done: true, completedSets: [0, 1, 2, 3, 4, 5, 6, 7] }
};
const migrated = ctx.initAndMigrateCompletedFingerprints(legacyData);
assert(migrated.completedPassageFingerprints.length === 8, '8 passage fingerprints extracted from legacy cp90');
assert(migrated.cp60 && migrated.cp60.done === true, 'cp60 automatically marked done via legacy migration');
assert(migrated.cp90_h1 && migrated.cp90_h1.done === true, 'cp90_h1 automatically marked done via legacy migration');
assert(migrated.cp90_h2 && migrated.cp90_h2.done === true, 'cp90_h2 automatically marked done via legacy migration');

console.log(`\n==================================================`);
console.log(`TEST RESULTS: ${testsPassed} passed, ${testsFailed} failed`);
console.log(`==================================================`);

if (testsFailed > 0) {
  process.exit(1);
}
