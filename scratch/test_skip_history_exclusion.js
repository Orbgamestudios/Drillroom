const assert = require("assert");
const fs = require("fs");
const path = require("path");
const vm = require("vm");

console.log("=== TEST SUITE: Skipped Passage History Exclusion, Clean MCAT Styling & Website Icons ===");

const html = fs.readFileSync(path.join(__dirname, "../index.html"), "utf8");
const practiceExamCode = fs.readFileSync(path.join(__dirname, "../practice_exam.js"), "utf8");

// 1. Verify Website Icons exist on disk and are linked in index.html and DrillRoom.html
assert(fs.existsSync(path.join(__dirname, "../favicon.ico")), "favicon.ico must exist");
assert(fs.existsSync(path.join(__dirname, "../favicon.svg")), "favicon.svg must exist");
assert(fs.existsSync(path.join(__dirname, "../favicon-32x32.png")), "favicon-32x32.png must exist");
assert(fs.existsSync(path.join(__dirname, "../apple-touch-icon.png")), "apple-touch-icon.png must exist");
console.log("  ✓ All icon files (SVG, ICO, PNGs) exist on disk");

assert(html.includes('rel="icon" type="image/svg+xml" href="favicon.svg"'), "SVG favicon linked");
assert(html.includes('rel="icon" type="image/x-icon" href="favicon.ico"'), "ICO favicon linked");
assert(html.includes('rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png"'), "Apple touch icon linked");
assert(html.includes('<img src="favicon.svg" alt="DrillRoom"'), "Header contains DrillRoom brand icon");
console.log("  ✓ Icon tags properly linked in HTML head and top bar");

// 2. Verify "A guess that lands right is a gap, not a point" is completely removed
assert(!html.includes("A guess that lands right is a gap, not a point"), "The 'guess that lands right is a gap, not a point' text must be completely removed");
assert(!html.includes("Required. A guess that lands right"), "Notice below confidence options is removed");
console.log("  ✓ Notice below Know It / Guess section is removed");

// 3. Verify emojis are removed from buttons and UI
assert(!html.includes("☁️ Cloud Sync"), "Cloud emoji removed from top bar button");
assert(!html.includes("☁️ Cloud Sync &amp; Account"), "Cloud emoji removed from home button");
const cloudSyncCode = fs.readFileSync(path.join(__dirname, "../cloud_sync.js"), "utf8");
assert(!cloudSyncCode.includes("☁️ Sign In / Sync"), "Cloud emoji removed from cloud_sync.js buttons");
assert(!cloudSyncCode.includes("⚙️ Cloud Server"), "Gear emoji removed from cloud_sync.js buttons");
assert(!practiceExamCode.includes("☘ Lucky Hits"), "Clover emoji removed from practice exam filters");
assert(!practiceExamCode.includes("⚠ Confident"), "Warning emoji removed from practice exam filters");
assert(!practiceExamCode.includes("✓ Correct"), "Check emoji removed from practice exam filters");
assert(!practiceExamCode.includes("✕ Missed"), "Cross emoji removed from practice exam filters");
console.log("  ✓ All emojis removed from UI, buttons, and filters");

// 4. Verify that skipped passages do NOT count in history
const mockStorage = {};
const mockLocalStorage = {
  getItem: (k) => (k in mockStorage ? mockStorage[k] : null),
  setItem: (k, v) => { mockStorage[k] = String(v); },
  removeItem: (k) => { delete mockStorage[k]; }
};

const sandbox = {
  console,
  localStorage: mockLocalStorage,
  window: {},
  document: {
    getElementById: () => null,
    querySelectorAll: () => [],
    createElement: () => ({ style: {}, classList: { add: ()=>{}, remove: ()=>{} }, appendChild: ()=>{}, querySelectorAll: () => [], querySelector: () => null })
  },
  $: () => ({ style: {}, classList: { add: ()=>{}, remove: ()=>{}, contains: ()=>false, toggle: ()=>{} }, textContent: "", innerHTML: "", appendChild: ()=>{}, querySelectorAll: () => [], querySelector: () => null }),
  tick: () => {},
  view: () => {},
  rawToScaled: () => ({ score: 130, ptile: "98th" }),
  getQuestionArchetype: () => "Data Interpretation",
  stopPracticeExamTimer: () => {},
  setInterval: () => 123,
  clearInterval: () => {},
  clearHighlightsOnPassageChange: () => {},
  saveHighlightsForActiveQuestion: () => {},
  loadHighlightsForActiveQuestion: () => {},
  PRACTICE_EXAMS: [
    {
      id: "test_exam",
      sec: "CARS",
      duration: 60,
      suite: "exam1_60",
      suiteTitle: "CARS Practice 1",
      label: "CARS 1",
      sets: [{ id: "set1", qs: [{}, {}] }]
    }
  ]
};
vm.createContext(sandbox);
vm.runInContext(practiceExamCode, sandbox);

// Set up past history with 1 normal full attempt and 1 dirty attempt that had skipped passages
mockStorage["drillroom_history_v1"] = JSON.stringify([
  {
    id: "legit_attempt",
    examId: "test_exam",
    rawScore: 50,
    totalQs: 50,
    scoredTotal: 50,
    skippedCount: 0,
    scaledScore: 130
  },
  {
    id: "bad_skipped_attempt",
    examId: "test_exam",
    rawScore: 10,
    totalQs: 50,
    scoredTotal: 10,
    skippedCount: 40,
    scaledScore: 118
  }
]);

// getHistory() must automatically clean out the bad skipped attempt!
const hist = sandbox.getHistory();
assert.strictEqual(hist.length, 1, `getHistory() should purge skipped attempts, expected 1 item, got ${hist.length}`);
assert.strictEqual(hist[0].id, "legit_attempt", "Only legitimate un-skipped exam remains");
console.log("  ✓ getHistory() automatically purges any attempts with skipped passages");

// Verify addHistoryEntry rejects any attempt with skippedCount > 0
sandbox.addHistoryEntry({
  id: "new_skipped_attempt",
  examId: "test_exam",
  rawScore: 5,
  totalQs: 50,
  scoredTotal: 5,
  skippedCount: 45,
  scaledScore: 130
});
const histAfter = sandbox.getHistory();
assert.strictEqual(histAfter.length, 1, "addHistoryEntry must NOT save an attempt with skippedCount > 0");
console.log("  ✓ addHistoryEntry rejects attempts with skippedCount > 0");

// Verify gradePracticeExam with skipped questions does NOT add to history
const testExam = {
  id: "cars_test_1",
  sec: "CARS",
  duration: 60,
  suiteTitle: "Diagnostic Suite",
  label: "CARS Section 1",
  sets: [
    { id: "p1", topic: "Philosophy", passage: "Passage 1 content", qs: [{ q: "Q1", ch: ["A","B","C","D"], a: 0 }, { q: "Q2", ch: ["A","B","C","D"], a: 1 }] },
    { id: "p2", topic: "History", passage: "Passage 2 content", qs: [{ q: "Q3", ch: ["A","B","C","D"], a: 2 }, { q: "Q4", ch: ["A","B","C","D"], a: 3 }] }
  ]
};
sandbox.registerExam(testExam.id, testExam.sec, testExam.label, testExam.duration, "60min", testExam.sets, "desc", "diag", testExam.suiteTitle);
sandbox.beginPracticeExam(testExam);

// Skip passage 1 (questions 0 and 1)
sandbox.E.s.qs[0]._isSkipped = true;
sandbox.E.s.qs[1]._isSkipped = true;
sandbox.E.ans[0] = -1;
sandbox.E.ans[1] = -1;
sandbox.E.conf[0] = "skipped";
sandbox.E.conf[1] = "skipped";
// Answer passage 2 correctly
sandbox.E.ans[2] = 2;
sandbox.E.conf[2] = "sure";
sandbox.E.ans[3] = 3;
sandbox.E.conf[3] = "sure";

const histBeforeGrading = sandbox.getHistory().length;
sandbox.gradePracticeExam();
const histAfterGrading = sandbox.getHistory().length;

assert.strictEqual(histAfterGrading, histBeforeGrading, "gradePracticeExam with skipped passages must NOT add an entry to history");
console.log("  ✓ gradePracticeExam with skipped passages does not add to score history");

console.log("\nAll tests passed successfully!");
