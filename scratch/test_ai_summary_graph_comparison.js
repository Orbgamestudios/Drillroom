const assert = require("assert");
const fs = require("fs");
const vm = require("vm");

console.log("=== Testing AI Summary Comparison with Previous Sessions & Important Graphs ===");

const codeCharts = fs.readFileSync("/home/cgslinde/DrillRoom/DrillRoom/performance_charts.js", "utf8");
const codeGemini = fs.readFileSync("/home/cgslinde/DrillRoom/DrillRoom/gemini_analysis.js", "utf8");

function setupContext() {
  const mockStorage = {
    drillroom_history_v1: JSON.stringify([
      {
        id: "att_prior_1",
        examId: "exam_cars_1",
        sec: "CARS",
        suiteTitle: "CARS Diagnostic 1",
        label: "CARS Full Section 1",
        duration: 90,
        scaledScore: 126,
        pct: 72,
        solid: 18,
        ts: Date.now() - 86400000 * 5,
        reviewData: {
          passageStats: [
            { pIndex: 1, setIdx: 0, wordCount: 550, readSec: 210, wpm: 157 },
            { pIndex: 2, setIdx: 1, wordCount: 580, readSec: 250, wpm: 139 },
            { pIndex: 3, setIdx: 2, wordCount: 540, readSec: 260, wpm: 125 }
          ],
          qs: Array.from({ length: 15 }, () => ({ time: 68, ans: 0, a: 0, conf: "sure" }))
        }
      },
      {
        id: "att_prior_2",
        examId: "exam_cars_2",
        sec: "CARS",
        suiteTitle: "CARS Diagnostic 2",
        label: "CARS Full Section 2",
        duration: 90,
        scaledScore: 129,
        pct: 80,
        solid: 22,
        ts: Date.now() - 86400000 * 2,
        reviewData: {
          passageStats: [
            { pIndex: 1, setIdx: 0, wordCount: 560, readSec: 180, wpm: 187 },
            { pIndex: 2, setIdx: 1, wordCount: 570, readSec: 210, wpm: 163 },
            { pIndex: 3, setIdx: 2, wordCount: 530, readSec: 225, wpm: 141 }
          ],
          qs: Array.from({ length: 15 }, () => ({ time: 55, ans: 0, a: 0, conf: "sure" }))
        }
      }
    ])
  };

  const sandbox = {
    console: console,
    localStorage: {
      getItem: (k) => mockStorage[k] || null,
      setItem: (k, v) => { mockStorage[k] = v; }
    },
    window: {},
    document: {
      createElement: () => ({ style: {}, appendChild: () => {}, querySelector: () => null }),
      querySelector: () => null,
      getElementById: () => null
    }
  };
  sandbox.window = sandbox;
  sandbox.globalThis = sandbox;

  vm.createContext(sandbox);
  vm.runInContext(codeCharts, sandbox);
  vm.runInContext(codeGemini, sandbox);
  return sandbox;
}

const sb = setupContext();

// Current completed exam
const mockCurrentExam = {
  examId: "att_current_3",
  title: "CARS High-Yield Adaptive Study",
  sec: "CARS",
  duration: 50,
  modeName: "Adaptive Study",
  scaledScore: 131,
  percentile: "96th",
  right: 17,
  wrong: 1,
  total: 18,
  pct: 94,
  solid: 15,
  lucky: 1,
  shaky: 1,
  avgQSec: 46,
  passageStats: [
    { pIndex: 1, setIdx: 0, wordCount: 585, readSec: 161, wpm: 218 },
    { pIndex: 2, setIdx: 1, wordCount: 580, readSec: 180, wpm: 193 },
    { pIndex: 3, setIdx: 2, wordCount: 508, readSec: 175, wpm: 174 }
  ],
  qs: [
    { q: "Test stem", ch: ["A", "B", "C", "D"], a: 0, _passage: "Text...", _topic: "Philosophy", archetype: "Reasoning Beyond" }
  ],
  userAnswers: [0],
  confidences: ["sure"],
  qTimes: [46]
};

// 1. Verify extractHistoricalTrajectory
console.log("\n--- TEST 1: extractHistoricalTrajectory() ---");
const hist = sb.extractHistoricalTrajectory(mockCurrentExam);
assert(hist, "Historical trajectory must not be null when prior sessions exist");
assert.strictEqual(hist.priorCount, 2, "Must identify 2 prior sessions");
assert.strictEqual(hist.subject, "CARS");
console.log(`  Identified ${hist.priorCount} prior CARS sessions with baseline score ${hist.baseline.scaledScore}/132`);
assert(hist.baseline.scaledScore >= 127 && hist.baseline.scaledScore <= 128);
console.log("  [PASSED] extractHistoricalTrajectory() correctly calculated multi-session baseline metrics.");

// 2. Verify buildDiagnosticPrompt() formatting
console.log("\n--- TEST 2: buildDiagnosticPrompt() with Multi-Session Comparison ---");
const prompt = sb.buildDiagnosticPrompt(mockCurrentExam);

assert(prompt.includes("4 CORE PERFORMANCE TELEMETRY GRAPHS (EMBEDDED DIRECTLY IN REPORT):"), "Must include comparative section header");
assert(prompt.includes("Score Trajectory Graph"), "Must reference Score Trajectory Graph");
assert(prompt.includes("Reading Speed Graph") || prompt.includes("Passage Reading Speed Graph"), "Must reference Reading Speed Graph");
assert(prompt.includes("Fatigue Delta Graph"), "Must reference Fatigue Delta Graph");
assert(prompt.includes("Fatigue Reduction Trend Graph") || prompt.includes("Fatigue Reduction & Multi-Session Stamina Trend"), "Must reference Fatigue Reduction Trend Graph");
assert(prompt.includes("Trajectory vs Previous Sessions:"), "Executive Summary must require Trajectory vs Previous Sessions callout");
assert(prompt.includes("# 1. Visual Graph Diagnostics: What the 4 Key Graphs Reveal"), "Must include dedicated Section 1 for visual graph diagnostics");
assert(prompt.includes("### Graph 1: Score Trajectory & MCAT Target Analysis"), "Must include Graph 1 subhead");
assert(prompt.includes("### Graph 3: Passage Reading Speed (WPM) vs Comprehension Analysis"), "Must include Graph 3 subhead");
assert(prompt.includes("### Graph 4: Fatigue Reduction & Multi-Session Stamina Trend"), "Must include Graph 4 subhead");
console.log("  [PASSED] Diagnostic prompt contains comprehensive historical graph comparison table and instructions.");

// 3. Verify renderMarkdown() turns graph mentions into clickable pills and mounts embedded charts
console.log("\n--- TEST 3: renderMarkdown() Graph Pill Links & Embedded Chart Mount ---");
const mockAIOutput = `
# 1. Visual Graph Diagnostics: What the 4 Key Graphs Reveal
Your stamina curve is consolidating on the [Session Fatigue Delta Graph].
Meanwhile, your analytical reading pace on the [Reading Speed Graph] accelerated by +23 WPM compared to your baseline sessions.
Cross-reference your progress on the [Score Trajectory Graph].
`;

const renderedHtml = sb.renderGeminiMarkdown(mockAIOutput);
assert(renderedHtml.includes('id="peEmbeddedGraphsMount"'), "Must mount peEmbeddedGraphsMount directly before Section 1");
assert(renderedHtml.includes("jumpToPerformanceChart('avgSessionFatigueDelta')"), "Must render clickable pill for Session Fatigue Delta Graph");
assert(renderedHtml.includes("jumpToPerformanceChart('avgPassageWpm')"), "Must render clickable pill for Reading Speed Graph");
assert(renderedHtml.includes("jumpToPerformanceChart('scaledScore')"), "Must render clickable pill for Score Trajectory Graph");
console.log("  [PASSED] renderGeminiMarkdown() mounts embedded charts and converts graph names into interactive pills.");

// 4. Verify jumpToPerformanceChart
console.log("\n--- TEST 4: jumpToPerformanceChart() state updates ---");
sb.jumpToPerformanceChart("avgSessionFatigueDelta");
assert.strictEqual(sb.chartState.yMetric, "avgSessionFatigueDelta");
assert.strictEqual(sb.chartState.xAxisMode, "sessions");
console.log("  [PASSED] jumpToPerformanceChart() pre-selects the requested metric and switches axis mode.");

console.log("\n>>> ALL AI SUMMARY GRAPH COMPARISON TESTS PASSED 100% <<<");
