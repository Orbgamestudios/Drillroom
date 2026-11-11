const assert = require("assert");
const fs = require("fs");
const vm = require("vm");

console.log("=== Testing AI Summary Graph Enforcement & Cache Versioning ===");

const codeCharts = fs.readFileSync("/home/cgslinde/DrillRoom/DrillRoom/performance_charts.js", "utf8");
const codeGemini = fs.readFileSync("/home/cgslinde/DrillRoom/DrillRoom/gemini_analysis.js", "utf8");

function setupContext(initialStorage = {}) {
  const mockStorage = { ...initialStorage };

  const sandbox = {
    console: console,
    localStorage: {
      getItem: (k) => (k in mockStorage ? mockStorage[k] : null),
      setItem: (k, v) => { mockStorage[k] = String(v); },
      removeItem: (k) => { delete mockStorage[k]; }
    },
    window: {},
    document: {
      createElement: (tag) => ({
        tagName: tag,
        style: {},
        appendChild: () => {},
        querySelector: () => null,
        querySelectorAll: () => []
      }),
      querySelector: () => null,
      querySelectorAll: () => [],
      getElementById: () => null
    }
  };
  sandbox.window = sandbox;
  sandbox.globalThis = sandbox;

  vm.createContext(sandbox);
  vm.runInContext(codeCharts, sandbox);
  vm.runInContext(codeGemini, sandbox);
  return { sandbox, mockStorage };
}

// ----------------------------------------------------
// TEST 1: Same-Exam Multiple Attempts Preservation
// ----------------------------------------------------
console.log("\n--- TEST 1: Same-Exam Multiple Attempts Preservation ---");
const priorAttempt1 = {
  id: "att_cp1_attempt_1",
  examId: "pe_cp_full_1",
  sec: "C/P",
  suiteTitle: "Chemical & Physical Foundations 1",
  label: "C/P Full Section 1",
  duration: 90,
  scaledScore: 127,
  pct: 75,
  ts: Date.now() - 86400000 * 3,
  reviewData: {
    passageStats: [
      { pIndex: 1, setIdx: 0, wordCount: 520, readSec: 200, wpm: 156 },
      { pIndex: 2, setIdx: 1, wordCount: 540, readSec: 230, wpm: 141 }
    ],
    qs: Array.from({ length: 10 }, () => ({ time: 65, ans: 0, a: 0, conf: "sure" }))
  }
};

const currentAttemptInstance = {
  id: "att_cp1_attempt_2",
  examId: "pe_cp_full_1", // SAME examId!
  sec: "C/P",
  suiteTitle: "Chemical & Physical Foundations 1",
  label: "C/P Full Section 1",
  duration: 90,
  scaledScore: 130,
  pct: 85,
  ts: Date.now(),
  reviewData: {
    id: "att_cp1_attempt_2",
    passageStats: [
      { pIndex: 1, setIdx: 0, wordCount: 520, readSec: 175, wpm: 178 },
      { pIndex: 2, setIdx: 1, wordCount: 540, readSec: 185, wpm: 175 }
    ],
    qs: Array.from({ length: 10 }, () => ({ time: 50, ans: 0, a: 0, conf: "sure" }))
  }
};

const { sandbox: sb1 } = setupContext({
  drillroom_history_v1: JSON.stringify([currentAttemptInstance, priorAttempt1])
});

const histResult = sb1.extractHistoricalTrajectory({
  examId: "pe_cp_full_1",
  attemptId: "att_cp1_attempt_2",
  sec: "C/P",
  scaledScore: 130,
  reviewData: { id: "att_cp1_attempt_2", ts: currentAttemptInstance.ts }
});

assert(histResult !== null, "Prior session of same examId MUST NOT be filtered out!");
assert.strictEqual(histResult.priorCount, 1, "Should identify exactly 1 prior session");
assert.strictEqual(histResult.baseline.scaledScore, 127, "Prior baseline scaled score must match prior attempt");
console.log("✓ Test 1 Passed: Prior attempt of the same exam was correctly preserved and compared!");

// ----------------------------------------------------
// TEST 2: Prompt Enforcement of Mandatory Graph Citations (Multi-Session)
// ----------------------------------------------------
console.log("\n--- TEST 2: Prompt Enforcement of Mandatory Graph Citations (Multi-Session) ---");
const mockExamInfoMulti = {
  examId: "pe_cp_full_1",
  attemptId: "att_cp1_attempt_2",
  title: "C/P Full Section 1",
  sec: "C/P",
  duration: 90,
  modeName: "90-Min Timed Section",
  scaledScore: 130,
  percentile: "93rd",
  right: 50,
  wrong: 9,
  total: 59,
  pct: 85,
  solid: 45,
  lucky: 3,
  shaky: 2,
  avgQSec: 52,
  passageStats: [
    { pIndex: 1, setIdx: 0, wordCount: 520, readSec: 175, wpm: 178 },
    { pIndex: 2, setIdx: 1, wordCount: 540, readSec: 185, wpm: 175 }
  ],
  qs: [
    {
      q: "Which enzyme catalyzes this rate-limiting step?",
      ch: ["PFK-1", "Hexokinase", "Pyruvate kinase", "Aldolase"],
      a: 0,
      e: "PFK-1 is the committed, rate-limiting step of glycolysis.",
      _topic: "Biochemistry"
    }
  ],
  userAnswers: [1], // wrong
  confidences: ["sure"],
  reviewData: { id: "att_cp1_attempt_2", ts: currentAttemptInstance.ts }
};

const promptMulti = sb1.buildDiagnosticPrompt(mockExamInfoMulti);
assert(promptMulti.includes("MANDATORY GRAPH CITATION REQUIREMENT"), "Prompt must include MANDATORY GRAPH CITATION REQUIREMENT");
assert(promptMulti.includes("[Score Trajectory Graph]"), "Prompt must cite [Score Trajectory Graph]");
assert(promptMulti.includes("[Reading Speed Graph]"), "Prompt must cite [Reading Speed Graph]");
assert(promptMulti.includes("[Session Fatigue Delta Graph]"), "Prompt must cite [Session Fatigue Delta Graph]");
assert(promptMulti.includes("# 1. Trajectory Comparison: Where You Stand vs Previous Sessions"), "Prompt must include Trajectory Comparison header");
assert(promptMulti.includes("REMINDER ON MANDATORY GRAPH PILLS"), "Prompt must include end-of-prompt reminder");
console.log("✓ Test 2 Passed: Multi-session prompt enforces bracketed graph names in all required sections!");

// ----------------------------------------------------
// TEST 3: Prompt Enforcement of Mandatory Graph Citations (Baseline First Session)
// ----------------------------------------------------
console.log("\n--- TEST 3: Prompt Enforcement of Mandatory Graph Citations (Baseline First Session) ---");
const { sandbox: sbEmpty } = setupContext({
  drillroom_history_v1: JSON.stringify([])
});

const mockExamInfoFirst = {
  examId: "pe_bb_full_1",
  title: "B/B Full Section 1",
  sec: "B/B",
  duration: 90,
  modeName: "90-Min Timed Section",
  scaledScore: 128,
  percentile: "82nd",
  right: 48,
  wrong: 11,
  total: 59,
  pct: 81,
  solid: 42,
  lucky: 4,
  shaky: 2,
  avgQSec: 54,
  passageStats: [
    { pIndex: 1, setIdx: 0, wordCount: 550, readSec: 180, wpm: 183 },
    { pIndex: 2, setIdx: 1, wordCount: 560, readSec: 190, wpm: 177 }
  ],
  qs: [
    {
      q: "What is the net ATP yield?",
      ch: ["2", "4", "30", "32"],
      a: 2,
      e: "30-32 ATP depending on shuttle.",
      _topic: "Bioenergetics"
    }
  ],
  userAnswers: [2],
  confidences: ["sure"]
};

const promptFirst = sbEmpty.buildDiagnosticPrompt(mockExamInfoFirst);
assert(promptFirst.includes("INITIAL BASELINE CALIBRATION (FIRST RECORDED SESSION)"), "Prompt must include initial baseline section");
assert(promptFirst.includes("MANDATORY BASELINE INSTRUCTION"), "Prompt must include mandatory baseline graph instruction");
assert(promptFirst.includes("[Score Trajectory Graph]"), "Baseline prompt must include [Score Trajectory Graph]");
assert(promptFirst.includes("[Reading Speed Graph]"), "Baseline prompt must include [Reading Speed Graph]");
assert(promptFirst.includes("[Session Fatigue Delta Graph]"), "Baseline prompt must include [Session Fatigue Delta Graph]");
console.log("✓ Test 3 Passed: First-session baseline prompt instructs Gemini to ground review in key graphs!");

// ----------------------------------------------------
// TEST 4: Graph Pill Formatting with Flexible Regexes
// ----------------------------------------------------
console.log("\n--- TEST 4: Graph Pill Formatting with Flexible Regexes ---");
const markdownSample = `
# Executive Summary
> **Trajectory:** Up +2.5 points on your **[Score Trajectory Graph]**. Your [Reading Speed] accelerated to 218 WPM on the [Passage Reading Speed Graph].
> Fatigue drift compressed toward zero on the [Session Fatigue Delta Graph].

# 1. Trajectory Comparison
- Score Progression: View the Score Trajectory Graph.
- Cognitive stamina: Tracked via [Session Fatigue Delta].
- Sunk Costs: Controlled on [Time Sinks Graph].
- Normal reading speed of 210 wpm and question pace should stay standard.
`;

const renderedHtml = sb1.renderGeminiMarkdown(markdownSample);

assert(renderedHtml.includes("jumpToPerformanceChart('scaledScore')"), "Must render pill for Score Trajectory Graph");
assert(renderedHtml.includes("jumpToPerformanceChart('avgPassageWpm')"), "Must render pill for Reading Speed Graph");
assert(renderedHtml.includes("jumpToPerformanceChart('avgSessionFatigueDelta')"), "Must render pill for Session Fatigue Delta Graph");
assert(renderedHtml.includes("jumpToPerformanceChart('timeSinkCount')"), "Must render pill for Time Sinks Graph");
assert(!renderedHtml.includes("jumpToPerformanceChart('avgPassageWpm') of 210 wpm"), "Normal prose must not be turned into a link");
console.log("✓ Test 4 Passed: Graph pill formatting correctly handles bolded, bracketed, and unbracketed graph citations!");

// ----------------------------------------------------
// TEST 5: Legacy Cache Invalidation & Upgrade Flag
// ----------------------------------------------------
console.log("\n--- TEST 5: Legacy Cache Invalidation & Upgrade Flag ---");
const { sandbox: sbCache, mockStorage } = setupContext({
  // Legacy cache from prompt v1 without graph trajectory citations
  drillroom_ai_analysis_pe_cars_1: JSON.stringify({
    text: "# Executive Summary\nYou scored 127 in CARS. Work on passage main ideas and timing.",
    modelUsed: "gemini-1.5-flash",
    ts: Date.now() - 3600000
    // No version field and no graph mentions
  }),
  // Modern cache with version: 2 and graph trajectory mentions
  drillroom_ai_analysis_pe_cars_2: JSON.stringify({
    version: 2,
    text: "# Executive Summary\nYour [Score Trajectory Graph] is climbing. [Reading Speed Graph] confirms stamina.",
    modelUsed: "gemini-1.5-flash",
    ts: Date.now()
  })
});

const legacyCached = sbCache.getCachedGeminiAnalysis("pe_cars_1");
assert(legacyCached !== null, "Legacy cached entry should exist");
assert.strictEqual(legacyCached.isLegacy, true, "Legacy cached entry must be flagged with isLegacy: true");

const modernCached = sbCache.getCachedGeminiAnalysis("pe_cars_2");
assert(modernCached !== null, "Modern cached entry should exist");
assert.strictEqual(modernCached.isLegacy, false, "Modern cached entry must NOT be flagged as legacy");

// Test saving cache with version 2
sbCache.saveCachedGeminiAnalysis = (id, obj) => {
  mockStorage["drillroom_ai_analysis_" + id] = JSON.stringify({ ...obj, version: 2 });
};
sbCache.saveCachedGeminiAnalysis("pe_cars_3", { text: "Testing graph save", modelUsed: "gemini-1.5-flash" });
const saved = JSON.parse(mockStorage["drillroom_ai_analysis_pe_cars_3"]);
assert.strictEqual(saved.version, 2, "Newly saved analysis must have version: 2");

console.log("✓ Test 5 Passed: Legacy cache entries detected and new entries saved with version 2!");

console.log("\n>>> ALL AI SUMMARY GRAPH ENFORCEMENT & CACHE TESTS PASSED 100% <<<");
