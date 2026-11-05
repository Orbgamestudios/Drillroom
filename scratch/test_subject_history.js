// Automated Test for Subject-First Practice, Exit Without Scoring, and History with Configurable Rolling Averages
const fs = require('fs');

// Mock localStorage
const storage = {};
global.localStorage = {
  getItem: (k) => storage[k] || null,
  setItem: (k, v) => { storage[k] = String(v); },
  removeItem: (k) => { delete storage[k]; }
};

// Mock DOM elements
const elements = {};
function getEl(id) {
  if (!elements[id]) {
    elements[id] = {
      id,
      innerHTML: '',
      textContent: '',
      value: '',
      className: '',
      classList: {
        add: function(c) { this.classes = this.classes || new Set(); this.classes.add(c); },
        remove: function(c) { this.classes = this.classes || new Set(); this.classes.delete(c); },
        toggle: function(c, v) {
          this.classes = this.classes || new Set();
          if (v === undefined) v = !this.classes.has(c);
          v ? this.classes.add(c) : this.classes.delete(c);
        },
        contains: function(c) { return this.classes ? this.classes.has(c) : false; }
      },
      style: {},
      onclick: null,
      onchange: null,
      children: [],
      appendChild: function(ch) { this.children.push(ch); return ch; },
      querySelector: function(sel) {
        return this.children.find(c => (sel.startsWith('#') && c.id === sel.slice(1)) || (sel.startsWith('.') && c.className && c.className.includes(sel.slice(1)))) || getEl('mock_' + Math.random());
      },
      querySelectorAll: function() { return []; }
    };
  }
  return elements[id];
}

global.$ = getEl;
global.document = {
  getElementById: (id) => getEl(id),
  createElement: (tag) => getEl('mock_el_' + Math.random()),
  querySelectorAll: () => []
};
global.window = {
  lockCalc: () => {}
};
global.confirm = () => true;
global.flash = (m) => console.log('FLASH:', m);
global.view = (v) => console.log('VIEW SWITCHED TO:', v);
global.paintHome = () => {};
global.tick = () => {};
global.timerId = 123;
global.clearInterval = (id) => console.log('TIMER CLEARED:', id);

// Mock exam definitions
global.EXAM_CP90 = [{ id: "set_cp1", topic: "CP Topic 1", passage: "CP Pass 1", qs: [{ q: "Q1", ch: ["A","B","C","D"], a: 0 }] }];
global.EXAM_CARS90 = [{ id: "set_cars1", topic: "CARS Topic 1", passage: "CARS Pass 1", qs: [{ q: "Q1", ch: ["A","B","C","D"], a: 1 }] }];
global.EXAM_BB90 = [{ id: "set_bb1", topic: "BB Topic 1", passage: "BB Pass 1", qs: [{ q: "Q1", ch: ["A","B","C","D"], a: 2 }] }];
global.EXAM_PS90 = [{ id: "set_ps1", topic: "PS Topic 1", passage: "PS Pass 1", qs: [{ q: "Q1", ch: ["A","B","C","D"], a: 3 }] }];

global.EXAM_CP90_2 = [{ id: "set_cp2", topic: "CP Topic 2", passage: "CP Pass 2", qs: [{ q: "Q1", ch: ["A","B","C","D"], a: 0 }] }];
global.EXAM_CARS90_2 = [{ id: "set_cars2", topic: "CARS Topic 2", passage: "CARS Pass 2", qs: [{ q: "Q1", ch: ["A","B","C","D"], a: 1 }] }];
global.EXAM_BB90_2 = [{ id: "set_bb2", topic: "BB Topic 2", passage: "BB Pass 2", qs: [{ q: "Q1", ch: ["A","B","C","D"], a: 2 }] }];
global.EXAM_PS90_2 = [{ id: "set_ps2", topic: "PS Topic 2", passage: "PS Pass 2", qs: [{ q: "Q1", ch: ["A","B","C","D"], a: 3 }] }];

global.EXAM_CP60 = [{ id: "set_cp60", topic: "CP60", qs: [{ q: "Q1", ch: ["A","B","C","D"], a: 0 }] }];
global.EXAM_CARS60 = [{ id: "set_cars60", topic: "CARS60", qs: [{ q: "Q1", ch: ["A","B","C","D"], a: 1 }] }];
global.EXAM_BB60 = [{ id: "set_bb60", topic: "BB60", qs: [{ q: "Q1", ch: ["A","B","C","D"], a: 2 }] }];
global.EXAM_PS60 = [{ id: "set_ps60", topic: "PS60", qs: [{ q: "Q1", ch: ["A","B","C","D"], a: 3 }] }];

global.EXAM_CP60_2 = [{ id: "set_cp60_2", topic: "CP60 2", qs: [{ q: "Q1", ch: ["A","B","C","D"], a: 0 }] }];
global.EXAM_CARS60_2 = [{ id: "set_cars60_2", topic: "CARS60 2", qs: [{ q: "Q1", ch: ["A","B","C","D"], a: 1 }] }];
global.EXAM_BB60_2 = [{ id: "set_bb60_2", topic: "BB60 2", qs: [{ q: "Q1", ch: ["A","B","C","D"], a: 2 }] }];
global.EXAM_PS60_2 = [{ id: "set_ps60_2", topic: "PS60 2", qs: [{ q: "Q1", ch: ["A","B","C","D"], a: 3 }] }];

// Load practice_exam.js
require('/home/cgslinde/DrillRoom/DrillRoom/practice_exam.js');

console.log('=== TEST 1: PRACTICE_EXAMS REGISTRY ===');
console.log('Exams registered:', PRACTICE_EXAMS.length);
if (PRACTICE_EXAMS.length !== 16) throw new Error('Expected 16 registered exams, got ' + PRACTICE_EXAMS.length);
console.log('Test 1 Passed: 16 exams registered across 4 suites and 4 subjects.');

console.log('\n=== TEST 2: HISTORY STORAGE & AVERAGE CALCULATION ===');
// Add test history records
const sampleHistory = [
  { id: "att_1", examId: "cars90", sec: "CARS", duration: 90, scaledScore: 130, rawScore: 48, totalQs: 53, pct: 91, ts: 1000, includedInAverage: true },
  { id: "att_2", examId: "cp90", sec: "C/P", duration: 90, scaledScore: 128, rawScore: 44, totalQs: 52, pct: 85, ts: 2000, includedInAverage: true },
  { id: "att_3", examId: "bb90", sec: "B/B", duration: 90, scaledScore: 129, rawScore: 45, totalQs: 52, pct: 87, ts: 3000, includedInAverage: true },
  { id: "att_4", examId: "ps90", sec: "P/S", duration: 90, scaledScore: 131, rawScore: 49, totalQs: 52, pct: 94, ts: 4000, includedInAverage: true },
  { id: "att_5", examId: "cars60", sec: "CARS", duration: 60, scaledScore: 126, rawScore: 26, totalQs: 33, pct: 79, ts: 5000, includedInAverage: true },
  { id: "att_6", examId: "cp60", sec: "C/P", duration: 60, scaledScore: 120, rawScore: 18, totalQs: 33, pct: 55, ts: 6000, includedInAverage: false } // EXCLUDED!
];
saveHistory(sampleHistory);

const h = getHistory();
console.log('History items loaded:', h.length);
if (h.length !== 6) throw new Error('Expected 6 history items');

// Calculate rolling average with window = 3
const avg3 = calculateRollingAverage(h, { window: 3, sec: "all", dur: "all" });
console.log('Avg 3 recent included:', avg3);
// Included items sorted by ts desc: att_5 (ts 5000, 126), att_4 (ts 4000, 131), att_3 (ts 3000, 129)
// (att_6 is ts 6000 but excluded!)
// Average of 126, 131, 129 = 386 / 3 = 128.7
if (avg3.count !== 3) throw new Error('Expected 3 items in window');
if (avg3.avgScaled !== 128.7) throw new Error('Expected avg 128.7, got ' + avg3.avgScaled);
if (avg3.projComposite !== 515) throw new Error('Expected projected 515, got ' + avg3.projComposite);
if (avg3.excluded !== 1) throw new Error('Expected 1 excluded, got ' + avg3.excluded);
console.log('Test 2 Passed: Window 3 calculation and excluded item omission verified!');

console.log('\n=== TEST 3: TOGGLING INCLUSION IN AVERAGE ===');
// Toggle att_6 to included
toggleHistoryInclude("att_6");
const hAfterToggle = getHistory();
const item6 = hAfterToggle.find(x => x.id === "att_6");
if (!item6.includedInAverage) throw new Error('Expected att_6 to be included');

const avgWith6 = calculateRollingAverage(hAfterToggle, { window: 3, sec: "all", dur: "all" });
// Now the 3 most recent are att_6 (120), att_5 (126), att_4 (131). Average = (120+126+131)/3 = 125.7
console.log('Avg after including att_6:', avgWith6.avgScaled, 'Projected composite:', avgWith6.projComposite);
if (avgWith6.avgScaled !== 125.7) throw new Error('Expected avg 125.7, got ' + avgWith6.avgScaled);

// Toggle att_6 back to excluded
toggleHistoryInclude("att_6");
const avgReExcluded = calculateRollingAverage(getHistory(), { window: 3, sec: "all", dur: "all" });
if (avgReExcluded.avgScaled !== 128.7) throw new Error('Expected avg back to 128.7');
console.log('Test 3 Passed: Toggle include/exclude dynamically alters score average.');

console.log('\n=== TEST 4: SUBJECT FILTER IN AVERAGE ===');
const carsOnly = calculateRollingAverage(getHistory(), { window: "all", sec: "CARS", dur: "all" });
// CARS included: att_5 (126) and att_1 (130). Avg = 128.0
console.log('CARS average:', carsOnly.avgScaled, 'count:', carsOnly.count);
if (carsOnly.count !== 2) throw new Error('Expected 2 CARS items');
if (carsOnly.avgScaled !== 128.0) throw new Error('Expected 128.0');
console.log('Test 4 Passed: Subject filter accurately isolates subject performance.');

console.log('\n=== TEST 5: EXIT EXAM WITHOUT SCORING ===');
// Start an exam session
const testExam = PRACTICE_EXAMS[0];
beginPracticeExam(testExam);
console.log('Exam started. Active state E:', !!global.E, 'PE:', !!global.PE);

// Simulate answer choice on Q0
global.E.ans[0] = 0;
global.E.conf[0] = "sure";

// Exit exam without scoring
exitExamWithoutScoring();

console.log('After exitExamWithoutScoring: E is', global.E, 'PE is', global.PE);
if (global.E !== null || global.PE !== null) throw new Error('Expected E and PE to be null after exit');

// Check that no new history item was added
const hAfterExit = getHistory();
if (hAfterExit.length !== 6) throw new Error('History should not have changed after exiting without scoring');
console.log('Test 5 Passed: Exam cleanly exited without scoring, history unchanged.');

console.log('\nALL 5 TEST SUITES PASSED PERFECTLY!');
