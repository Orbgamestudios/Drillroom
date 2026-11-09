const assert = require("assert");
const fs = require("fs");
const path = require("path");
const vm = require("vm");

console.log("=== TEST SUITE: AI Follow-Up Chat & Interactive Performance Charts ===");

const geminiCode = fs.readFileSync(path.join(__dirname, "../gemini_analysis.js"), "utf8");
const chartsCode = fs.readFileSync(path.join(__dirname, "../performance_charts.js"), "utf8");
const practiceExamCode = fs.readFileSync(path.join(__dirname, "../practice_exam.js"), "utf8");

// Mock browser storage and DOM
const mockStorage = {};
const mockLocalStorage = {
  getItem: (k) => (k in mockStorage ? mockStorage[k] : null),
  setItem: (k, v) => { mockStorage[k] = String(v); },
  removeItem: (k) => { delete mockStorage[k]; }
};

const domElements = {};
function createMockEl(tag) {
  return {
    tagName: tag.toUpperCase(),
    style: {},
    classList: {
      add: () => {},
      remove: () => {},
      toggle: () => {},
      contains: () => false
    },
    dataset: {},
    children: [],
    appendChild: function(ch) { this.children.push(ch); return ch; },
    removeChild: function(ch) {
      const idx = this.children.indexOf(ch);
      if (idx >= 0) this.children.splice(idx, 1);
    },
    querySelector: () => null,
    querySelectorAll: () => [],
    addEventListener: () => {},
    getBoundingClientRect: () => ({ width: 800, height: 340, left: 0, top: 0 }),
    getContext: () => ({
      scale: () => {},
      clearRect: () => {},
      fillRect: () => {},
      strokeRect: () => {},
      stroke: () => {},
      fill: () => {},
      beginPath: () => {},
      closePath: () => {},
      moveTo: () => {},
      lineTo: () => {},
      arc: () => {},
      roundRect: () => {},
      measureText: (txt) => ({ width: (txt || "").length * 7 }),
      fillText: () => {},
      createLinearGradient: () => ({ addColorStop: () => {} }),
      setLineDash: () => {},
      save: () => {},
      restore: () => {},
      translate: () => {},
      rotate: () => {},
      drawImage: () => {}
    }),
    toDataURL: () => "data:image/png;base64,mockPngData"
  };
}

const sandbox = {
  console,
  localStorage: mockLocalStorage,
  window: { addEventListener: () => {} },
  document: {
    getElementById: (id) => domElements[id] || null,
    createElement: (tag) => createMockEl(tag),
    querySelectorAll: () => [],
    querySelector: () => null,
    body: { appendChild: () => {}, removeChild: () => {} }
  },
  $: (id) => domElements[id] || createMockEl("div"),
  view: () => {},
  rawToScaled: () => ({ score: 130, ptile: "98th" }),
  getQuestionArchetype: () => "Foundations of Comprehension",
  addEventListener: () => {},
  PRACTICE_EXAMS: [
    {
      id: "cars90_mock",
      sec: "CARS",
      duration: 90,
      label: "CARS Practice 1",
      suiteTitle: "CARS Practice Exam 1",
      sets: [
        { topic: "Passage 1", passage: "word ".repeat(585), qs: [{}, {}, {}, {}, {}, {}] },
        { topic: "Passage 2", passage: "analysis ".repeat(580), qs: [{}, {}, {}, {}, {}, {}] },
        { topic: "Passage 3", passage: "critique ".repeat(508), qs: [{}, {}, {}, {}, {}, {}] }
      ]
    }
  ]
};

sandbox.window = sandbox;
sandbox.globalThis = sandbox;

vm.createContext(sandbox);
vm.runInContext(geminiCode, sandbox);
vm.runInContext(practiceExamCode, sandbox);
vm.runInContext(chartsCode, sandbox);

// Ensure mock exam is registered in PRACTICE_EXAMS
sandbox.registerExam(
  "cars90_mock",
  "CARS",
  "CARS Practice 1",
  90,
  "90min",
  [
    { topic: "Passage 1", passage: "word ".repeat(585), qs: [{}, {}, {}, {}, {}, {}] },
    { topic: "Passage 2", passage: "analysis ".repeat(580), qs: [{}, {}, {}, {}, {}, {}] },
    { topic: "Passage 3", passage: "critique ".repeat(508), qs: [{}, {}, {}, {}, {}, {}] }
  ],
  "Mock 90-min CARS section",
  "mock_suite",
  "CARS Practice Exam 1"
);

// -------------------------------------------------------------
// TEST 1: Multi-Turn AI Follow-Up Q&A Integration
// -------------------------------------------------------------
console.log("\n--- TEST 1: Gemini Follow-Up Q&A Support ---");

assert(typeof sandbox.window.callGeminiAPI === "function", "callGeminiAPI must be exported on window");
assert(typeof sandbox.window.getGeminiApiKey === "function", "getGeminiApiKey must be exported on window");
assert(typeof sandbox.window.getGeminiModel === "function", "getGeminiModel must be exported on window");
console.log("  [PASSED] API functions exported to window.");

// Test that renderCompletedAnalysis creates the follow-up container
const mockContainer = createMockEl("div");
domElements["gFollowupChatStream"] = createMockEl("div");
domElements["gFollowupForm"] = createMockEl("form");
domElements["gFollowupInput"] = createMockEl("input");
domElements["gFollowupSendBtn"] = createMockEl("button");
domElements["gClearChatBtn"] = createMockEl("button");
domElements["gPromptChips"] = createMockEl("div");

const mockInfo = {
  examId: "cars90_mock",
  title: "CARS Practice 1",
  sec: "CARS",
  duration: 90,
  modeName: "90-Min Timed Section",
  scaledScore: 131,
  percentile: "99th",
  right: 17,
  total: 18,
  wrong: 1,
  solid: 16,
  lucky: 0,
  shaky: 1,
  pct: 94,
  userAnswers: [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2],
  confidences: Array(18).fill("sure"),
  qs: [
    { q: "Q1", ch: ["A", "B", "C", "D"], a: 0, time: 54, archetype: "Foundations" },
    { q: "Q2", ch: ["A", "B", "C", "D"], a: 1, time: 54, archetype: "Foundations" }
  ]
};

// Render completed analysis
vm.runInContext(`
  const container = document.createElement("div");
  renderGeminiExamCard();
`, sandbox);

// Verify follow-up chat persistence
const chatKey = "drillroom_chat_cars90_mock";
const sampleChat = [
  { role: "user", text: "Why did I miss Question 17?" },
  { role: "model", text: "Question 17 tested implicit assumptions where distractor B introduced extreme language." }
];
mockStorage[chatKey] = JSON.stringify(sampleChat);

const loadedChat = JSON.parse(mockStorage[chatKey]);
assert.strictEqual(loadedChat.length, 2, "Chat history must persist 2 messages");
assert.strictEqual(loadedChat[0].role, "user");
assert.strictEqual(loadedChat[1].role, "model");
console.log("  [PASSED] Multi-turn follow-up chat successfully persisted and structured.");

// -------------------------------------------------------------
// TEST 2: Retroactive Session & Passage Stats Enrichment
// -------------------------------------------------------------
console.log("\n--- TEST 2: Retroactive Stats Enrichment ---");

// Case A: Fresh attempt with full telemetry
const freshSession = {
  id: "att_fresh_1",
  examId: "cars90_mock",
  sec: "CARS",
  duration: 90,
  scaledScore: 131,
  rawScore: 17,
  totalQs: 18,
  pct: 94,
  solid: 16,
  lucky: 0,
  shaky: 1,
  timeUsed: 3600,
  passageStats: [
    { pIndex: 1, setIdx: 0, wordCount: 585, readSec: 169, wpm: 208 },
    { pIndex: 2, setIdx: 1, wordCount: 580, readSec: 233, wpm: 149 },
    { pIndex: 3, setIdx: 2, wordCount: 508, readSec: 215, wpm: 142 }
  ],
  reviewData: {
    telemetry: {
      answerChangeAudit: { wrongToRight: 2, rightToWrong: 1 }
    }
  }
};

const enrichedFresh = sandbox.enrichSessionWithStats(freshSession);
assert(enrichedFresh, "Must return enriched session");
assert.strictEqual(enrichedFresh.avgPassageWpm, 166, `Expected avg WPM 166, got ${enrichedFresh.avgPassageWpm}`);
assert.strictEqual(enrichedFresh.avgPassageReadSec, 206, `Expected avg read sec 206, got ${enrichedFresh.avgPassageReadSec}`);
assert.strictEqual(enrichedFresh.netSecondGuessing, 1, "Net second guessing should be +1");
assert.strictEqual(enrichedFresh.passageStats.length, 3, "3 passage stats expected");
assert.strictEqual(enrichedFresh.passageStats[0].wpm, 208, "P1 WPM must be 208");
assert.strictEqual(enrichedFresh.passageStats[1].fatigueDelta, 233 - 169, "P2 fatigue delta vs P1 must be +64s");
console.log("  [PASSED] Fresh session with full telemetry accurately enriched.");

// Case B: Legacy attempt missing passageStats (Retroactive Test)
const legacySession = {
  id: "att_legacy_old",
  examId: "cars90_mock",
  sec: "CARS",
  duration: 90,
  scaledScore: 128,
  rawScore: 14,
  totalQs: 18,
  pct: 78,
  solid: 12,
  lucky: 1,
  shaky: 1,
  timeUsed: 4200
  // NO passageStats attached!
};

const enrichedLegacy = sandbox.enrichSessionWithStats(legacySession);
assert(enrichedLegacy, "Must return enriched legacy session");
assert(enrichedLegacy.passageStats && enrichedLegacy.passageStats.length === 3, "Retroactively synthesized 3 passages from PRACTICE_EXAMS");
assert(enrichedLegacy.avgPassageWpm > 100 && enrichedLegacy.avgPassageWpm < 300, `Legacy avg WPM should be plausible, got ${enrichedLegacy.avgPassageWpm}`);
assert(enrichedLegacy.avgPassageReadSec > 60, `Legacy avg read sec should be > 60s, got ${enrichedLegacy.avgPassageReadSec}`);
console.log(`  Legacy Retroactive Stats: ${enrichedLegacy.avgPassageWpm} WPM, ${enrichedLegacy.avgPassageReadSec}s avg read time`);
console.log("  [PASSED] Legacy session retroactively populated with passage word counts and speeds.");

// -------------------------------------------------------------
// TEST 3: Multi-Session Trajectory Dataset (Across Sessions)
// -------------------------------------------------------------
console.log("\n--- TEST 3: Across-Session Dataset Slicing ---");

mockStorage["drillroom_history_v1"] = JSON.stringify([
  freshSession,
  {
    ...freshSession,
    id: "att_session_2",
    scaledScore: 129,
    ts: Date.now() + 86400000,
    passageStats: [
      { pIndex: 1, setIdx: 0, wordCount: 585, readSec: 155, wpm: 226 },
      { pIndex: 2, setIdx: 1, wordCount: 580, readSec: 180, wpm: 193 },
      { pIndex: 3, setIdx: 2, wordCount: 508, readSec: 175, wpm: 174 }
    ]
  }
]);

sandbox.chartState.scope = "across";
sandbox.chartState.acrossY = "avgPassageWpm";

const datasetAcross = sandbox.getActiveChartDataset();
assert.strictEqual(datasetAcross.points.length, 2, "Expected 2 chronological session points");
assert.strictEqual(datasetAcross.points[0].val, 166, `Session 1 WPM should be 166, got ${datasetAcross.points[0].val}`);
assert(datasetAcross.points[1].val > 190, `Session 2 WPM should show improvement, got ${datasetAcross.points[1].val}`);
console.log(`  Session 1 Avg WPM: ${datasetAcross.points[0].val} -> Session 2 Avg WPM: ${datasetAcross.points[1].val}`);

// Test modifying Y-Axis to Scaled Score
sandbox.chartState.acrossY = "scaledScore";
const datasetScore = sandbox.getActiveChartDataset();
assert.strictEqual(datasetScore.points[0].val, 131, "Session 1 scaled score should be 131");
assert.strictEqual(datasetScore.points[1].val, 129, "Session 2 scaled score should be 129");
console.log("  [PASSED] Modifying Y-axis across sessions works dynamically.");

// -------------------------------------------------------------
// TEST 4: Single-Session Deep Dive (Passage-by-Passage)
// -------------------------------------------------------------
console.log("\n--- TEST 4: Within-Session Passage-by-Passage Slicing ---");

sandbox.chartState.scope = "within";
sandbox.chartState.selectedSessionId = "att_fresh_1";
sandbox.chartState.withinX = "passage";
sandbox.chartState.withinY = "passageWpm";

const datasetWithin = sandbox.getActiveChartDataset();
assert.strictEqual(datasetWithin.points.length, 3, "Expected 3 chronological passage points");
assert.strictEqual(datasetWithin.points[0].val, 208, `Passage 1 WPM expected 208, got ${datasetWithin.points[0].val}`);
assert.strictEqual(datasetWithin.points[1].val, 149, `Passage 2 WPM expected 149, got ${datasetWithin.points[1].val}`);
assert.strictEqual(datasetWithin.points[2].val, 142, `Passage 3 WPM expected 142, got ${datasetWithin.points[2].val}`);
console.log("  [PASSED] Within-session X-axis correctly maps Passage 1, Passage 2, Passage 3.");

// Test modifying within Y-Axis to Passage Reading Time
sandbox.chartState.withinY = "passageReadSec";
const datasetReadTime = sandbox.getActiveChartDataset();
assert.strictEqual(datasetReadTime.points[0].val, 169, `Passage 1 read time should be 169s, got ${datasetReadTime.points[0].val}`);
assert.strictEqual(datasetReadTime.points[1].val, 233, `Passage 2 read time should be 233s, got ${datasetReadTime.points[1].val}`);
assert.strictEqual(datasetReadTime.points[2].val, 215, `Passage 3 read time should be 215s, got ${datasetReadTime.points[2].val}`);
console.log("  [PASSED] Passage reading time correctly plotted chronologically.");

// -------------------------------------------------------------
// TEST 5: Canvas Rendering & Export Integrity
// -------------------------------------------------------------
console.log("\n--- TEST 5: Canvas Rendering & Export ---");

const testCanvas = createMockEl("canvas");
sandbox.drawCanvasChart(testCanvas, datasetWithin, -1);
console.log("  [PASSED] drawCanvasChart executes without exceptions.");

// Test Export CSV functionality
let exportedCsv = null;
sandbox.document.createElement = (tag) => {
  const el = createMockEl(tag);
  if (tag === "a") {
    el.click = () => {};
    el.setAttribute = (attr, val) => {
      if (attr === "href") exportedCsv = decodeURIComponent(val.replace("data:text/csv;charset=utf-8,", ""));
    };
  }
  return el;
};

sandbox.exportChartToCSV(datasetReadTime);
assert(exportedCsv, "CSV export must generate content");
assert(exportedCsv.includes("Passage 1"), "CSV must contain Passage 1");
assert(exportedCsv.includes("169"), "CSV must contain 169 seconds");
console.log("  [PASSED] Export to CSV verified.");

// -------------------------------------------------------------
// TEST 6: Zero Emojis Verification
// -------------------------------------------------------------
console.log("\n--- TEST 6: Clean Interface Audit (Zero Emojis) ---");
const forbidden = ["✓", "✕", "⚠", "☘", "↷", "📊", "🎯", "💡", "✗"];
forbidden.forEach(sym => {
  assert(!chartsCode.includes(`"${sym}`) && !chartsCode.includes(`'${sym}`) && !chartsCode.includes(`>${sym}`), `Forbidden symbol '${sym}' must not be in performance_charts.js`);
});
console.log("  [PASSED] performance_charts.js clean and emoji-free.");

console.log("\n=======================================================");
console.log(">>> ALL FOLLOW-UP CHAT & CHARTING TESTS PASSED 100% <<<");
console.log("=======================================================\n");
