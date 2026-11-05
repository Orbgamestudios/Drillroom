const storage = {
  drillroom_pe_v1: JSON.stringify({
    cars90: { done: true, score: 45, total: 53, scaledScore: 129, pct: 85, ts: 1000 }
  }),
  drillroom_history_v1: JSON.stringify([
    { id: 'att_migrated_cars90', examId: 'cars90', rawScore: 45, totalQs: 53, scaledScore: 129, ts: 1000, includedInAverage: true },
    { id: 'att_1729600000_123', examId: 'cars90', rawScore: 45, totalQs: 53, scaledScore: 129, ts: 1005, includedInAverage: true }
  ])
};

global.localStorage = {
  getItem: (k) => storage[k] !== undefined ? storage[k] : null,
  setItem: (k, v) => { storage[k] = String(v); },
  removeItem: (k) => { delete storage[k]; }
};

const mockEl = {
  classList: { add: ()=>{}, remove: ()=>{}, toggle: ()=>{} },
  onclick: null,
  style: {},
  appendChild: () => {},
  querySelector: () => mockEl,
  querySelectorAll: () => []
};

global.$ = () => mockEl;
global.document = {
  getElementById: () => mockEl,
  createElement: () => mockEl,
  querySelectorAll: () => []
};
global.window = {};
global.confirm = () => true;
global.flash = (m) => {};

// Mock exam globals
global.EXAM_CP90 = [1]; global.EXAM_CARS90 = [1]; global.EXAM_BB90 = [1]; global.EXAM_PS90 = [1];
global.EXAM_CP90_2 = [1]; global.EXAM_CARS90_2 = [1]; global.EXAM_BB90_2 = [1]; global.EXAM_PS90_2 = [1];
global.EXAM_CP60 = [1]; global.EXAM_CARS60 = [1]; global.EXAM_BB60 = [1]; global.EXAM_PS60 = [1];
global.EXAM_CP60_2 = [1]; global.EXAM_CARS60_2 = [1]; global.EXAM_BB60_2 = [1]; global.EXAM_PS60_2 = [1];

require('/home/cgslinde/DrillRoom/DrillRoom/practice_exam.js');

console.log('1. Loading history through practice_exam.js:');
let h = globalThis.getHistory();
console.log('History count (should be 1 due to auto-dedup):', h.length);
if (h.length !== 1) throw new Error('Expected 1, got ' + h.length);

console.log('2. Deleting the single remaining entry:');
globalThis.deleteHistoryEntry(h[0].id);

h = globalThis.getHistory();
console.log('History count after deletion (should be 0):', h.length);
if (h.length !== 0) throw new Error('Expected 0, got ' + h.length + ' (resurrected!)');

const peAfter = JSON.parse(storage['drillroom_pe_v1']);
console.log('peData after deletion (should be {}):', peAfter);
if (Object.keys(peAfter).length !== 0) throw new Error('Expected empty peData');

console.log('INTEGRATION TEST PASSED: The exact bug reported by user is completely resolved!');
