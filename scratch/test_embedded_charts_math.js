const assert = require("assert");
const fs = require("fs");
const vm = require("vm");

console.log("=== Testing Embedded Canvas Chart Drawing with Real Logic & Mock Context ===");

const codeCharts = fs.readFileSync("/home/cgslinde/DrillRoom/DrillRoom/performance_charts.js", "utf8");
const codeGemini = fs.readFileSync("/home/cgslinde/DrillRoom/DrillRoom/gemini_analysis.js", "utf8");

function createMockContext() {
  const calls = [];
  return {
    calls,
    scale: (sx, sy) => calls.push(["scale", sx, sy]),
    clearRect: (x, y, w, h) => calls.push(["clearRect", x, y, w, h]),
    beginPath: () => calls.push(["beginPath"]),
    moveTo: (x, y) => {
      assert(!isNaN(x) && !isNaN(y), "moveTo coordinates must not be NaN");
      calls.push(["moveTo", x, y]);
    },
    lineTo: (x, y) => {
      assert(!isNaN(x) && !isNaN(y), "lineTo coordinates must not be NaN");
      calls.push(["lineTo", x, y]);
    },
    stroke: () => calls.push(["stroke"]),
    fill: () => calls.push(["fill"]),
    closePath: () => calls.push(["closePath"]),
    arc: (x, y, r, sa, ea) => {
      assert(!isNaN(x) && !isNaN(y) && !isNaN(r), "arc coordinates must not be NaN");
      calls.push(["arc", x, y, r, sa, ea]);
    },
    fillText: (text, x, y) => {
      assert(!isNaN(x) && !isNaN(y), "fillText coordinates must not be NaN");
      calls.push(["fillText", text, x, y]);
    },
    fillRect: (x, y, w, h) => {
      assert(!isNaN(x) && !isNaN(y) && !isNaN(w) && !isNaN(h), "fillRect coordinates must not be NaN");
      calls.push(["fillRect", x, y, w, h]);
    },
    strokeRect: (x, y, w, h) => {
      assert(!isNaN(x) && !isNaN(y) && !isNaN(w) && !isNaN(h), "strokeRect coordinates must not be NaN");
      calls.push(["strokeRect", x, y, w, h]);
    },
    measureText: (text) => ({ width: (text || "").length * 6 }),
    createLinearGradient: () => ({
      addColorStop: () => {}
    }),
    setLineDash: () => {},
    save: () => calls.push(["save"]),
    restore: () => calls.push(["restore"])
  };
}

function setupSandbox() {
  const sandbox = {
    console: console,
    localStorage: {
      getItem: () => null,
      setItem: () => {},
      removeItem: () => {}
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
  return sandbox;
}

const sb = setupSandbox();

// -------------------------------------------------------------------
// TEST 1: Score Trajectory Dataset & Label Anti-Collision
// -------------------------------------------------------------------
console.log("\n--- TEST 1: Score Trajectory & Axis Collision Avoidance ---");
const mockExam1 = {
  examId: "pe_cars_1",
  title: "CARS Practice 1",
  sec: "CARS",
  scaledScore: 131,
  passageStats: []
};
const mockHist1 = {
  priorCount: 2,
  baseline: { scaledScore: 128 },
  recentTrend: [
    { index: 1, scaledScore: 126, date: "Nov 4" },
    { index: 2, scaledScore: 129, date: "Nov 8" }
  ]
};

const dsScore = sb.buildScoreDataset(mockExam1, mockHist1);
assert.strictEqual(dsScore.type, "scoreTrajectory");
assert.strictEqual(dsScore.points.length, 3);
assert.strictEqual(dsScore.points[2].val, 131);
assert.strictEqual(dsScore.points[2].label, "Current");

const ctx1 = createMockContext();
const canvas1 = {
  getContext: () => ctx1,
  getBoundingClientRect: () => ({ width: 340, height: 210 })
};
sb.drawEmbeddedChart(canvas1, dsScore, -1);
assert(ctx1.calls.length > 25, "Canvas drawing operations must occur");

// Check that no point is placed directly on padL (48px)
const dotArcs1 = ctx1.calls.filter(c => c[0] === "arc");
assert.strictEqual(dotArcs1.length, 3);
const firstPointX = dotArcs1[0][1];
assert(firstPointX > 48, `First point X (${firstPointX}) must be strictly > padL (48) to avoid collision with Y-axis tick label!`);
console.log(`✓ Test 1 Passed: Score Trajectory rendered with inner padding (x0 = ${firstPointX}px > padL 48px), preventing '132131' collision!`);

// -------------------------------------------------------------------
// TEST 2: Cognitive Fatigue Delta with 0s Baseline Collision Avoidance
// -------------------------------------------------------------------
console.log("\n--- TEST 2: Cognitive Fatigue Delta & Baseline Collision Avoidance ---");
const mockExam2 = {
  examId: "pe_cars_2",
  title: "CARS Practice 2",
  sec: "CARS",
  scaledScore: 130,
  passageStats: [
    { pIndex: 1, wordCount: 520, readSec: 180, wpm: 173 },
    { pIndex: 2, wordCount: 540, readSec: 205, wpm: 158 },
    { pIndex: 3, wordCount: 510, readSec: 165, wpm: 185 },
    { pIndex: 4, wordCount: 550, readSec: 210, wpm: 157 },
    { pIndex: 5, wordCount: 530, readSec: 180, wpm: 177 } // Delta = 0 at the end!
  ]
};

const dsFatigue = sb.buildFatigueDeltaDataset(mockExam2);
assert.strictEqual(dsFatigue.type, "fatigueDelta");
assert.strictEqual(dsFatigue.isDelta, true);
assert.strictEqual(dsFatigue.points.length, 5);
assert.strictEqual(dsFatigue.points[0].val, 0); // P1 is 0s
assert.strictEqual(dsFatigue.points[4].val, 0); // P5 is 0s, directly at baseline!

const ctx2 = createMockContext();
const canvas2 = {
  getContext: () => ctx2,
  getBoundingClientRect: () => ({ width: 340, height: 210 })
};
sb.drawEmbeddedChart(canvas2, dsFatigue, -1);

// Find text draw for benchmark label "0s Baseline"
const baselineLabelCalls = ctx2.calls.filter(c => c[0] === "fillText" && c[1] === "0s Baseline");
assert.strictEqual(baselineLabelCalls.length, 1);
const bX = baselineLabelCalls[0][2];
// Because P5 is at 0s (baseline line), collision avoidance should have switched alignment or shifted X
assert(bX < 100 || bX > 200, "Benchmark label must have collision-safe positioning");
console.log("✓ Test 2 Passed: Cognitive Fatigue Delta rendered with centered zero and collision avoidance!");

// -------------------------------------------------------------------
// TEST 3: Passage Reading Speed & De-pegged WPM
// -------------------------------------------------------------------
console.log("\n--- TEST 3: Passage Reading Speed with De-pegged WPM ---");
const mockExamPegged = {
  examId: "pe_cars_3",
  title: "CARS Pegged Test",
  sec: "CARS",
  scaledScore: 129,
  passageStats: [
    { pIndex: 1, wordCount: 550, readSec: 300, wpm: 110 },
    { pIndex: 2, wordCount: 550, readSec: 300, wpm: 110 },
    { pIndex: 3, wordCount: 550, readSec: 300, wpm: 110 },
    { pIndex: 4, wordCount: 550, readSec: 300, wpm: 110 },
    { pIndex: 5, wordCount: 550, readSec: 300, wpm: 110 }
  ]
};

const dsWpm = sb.buildWpmDataset(mockExamPegged);
assert.strictEqual(dsWpm.type, "passageWpm");
assert.strictEqual(dsWpm.points.length, 5);
// Ensure de-pegging occurred!
const all110 = dsWpm.points.every(p => p.val === 110);
assert(!all110, "Passages must NOT all be pegged at 110 WPM!");
const avgWpm = Math.round(dsWpm.points.reduce((a, b) => a + b.val, 0) / dsWpm.points.length);
assert(avgWpm >= 170 && avgWpm <= 240, `Avg WPM should be in realistic range [170, 240], got ${avgWpm}`);

const ctx3 = createMockContext();
const canvas3 = {
  getContext: () => ctx3,
  getBoundingClientRect: () => ({ width: 340, height: 210 })
};
sb.drawEmbeddedChart(canvas3, dsWpm, -1);
assert(ctx3.calls.length > 25);
console.log(`✓ Test 3 Passed: Passage Reading Speed successfully de-pegged (realistic avg ${avgWpm} WPM)!`);

// -------------------------------------------------------------------
// TEST 4: Graph 4 (Fatigue Reduction Trend Across Sessions)
// -------------------------------------------------------------------
console.log("\n--- TEST 4: Fatigue Reduction Trend (Graph 4) ---");
const mockExamHist = {
  examId: "pe_cars_current",
  title: "CARS Exam 4",
  sec: "CARS",
  scaledScore: 130,
  passageStats: [
    { pIndex: 1, wordCount: 520, readSec: 180, wpm: 173 },
    { pIndex: 2, wordCount: 540, readSec: 189, wpm: 171 },
    { pIndex: 3, wordCount: 510, readSec: 185, wpm: 165 },
    { pIndex: 4, wordCount: 530, readSec: 192, wpm: 166 }
  ]
};
const mockHistTrend = {
  priorCount: 3,
  baseline: { scaledScore: 127, avgSessionFatigueDelta: 24 },
  recentTrend: [
    { index: 1, avgSessionFatigueDelta: 28, date: "Oct 20", title: "CARS Diagnostic" },
    { index: 2, avgSessionFatigueDelta: 22, date: "Oct 28", title: "CARS Practice 1" },
    { index: 3, avgSessionFatigueDelta: 16, date: "Nov 5", title: "CARS Practice 2" }
  ]
};

const dsSessionFatigue = sb.buildSessionFatigueDataset(mockExamHist, mockHistTrend);
assert.strictEqual(dsSessionFatigue.type, "sessionFatigueTrend");
assert.strictEqual(dsSessionFatigue.title, "4. Fatigue Reduction Trend");
assert.strictEqual(dsSessionFatigue.isDelta, true);
assert.strictEqual(dsSessionFatigue.points.length, 4); // 3 prior + 1 current
assert.strictEqual(dsSessionFatigue.points[0].val, 28);
assert.strictEqual(dsSessionFatigue.points[1].val, 22);
assert.strictEqual(dsSessionFatigue.points[2].val, 16);
assert(dsSessionFatigue.points[3].isCurrent, "Last point must be current session");
console.log(`  Current session fatigue drift: ${dsSessionFatigue.points[3].val}s (vs Oct 20 baseline 28s)`);
assert(dsSessionFatigue.badge.includes("Stamina Up") || dsSessionFatigue.badge.includes("vs Prior Baseline"));

const ctx4 = createMockContext();
const canvas4 = {
  getContext: () => ctx4,
  getBoundingClientRect: () => ({ width: 340, height: 210 })
};
sb.drawEmbeddedChart(canvas4, dsSessionFatigue, -1);
assert(ctx4.calls.length > 30, "Graph 4 must render lines, dots, and area fill");
console.log("✓ Test 4 Passed: 4. Fatigue Reduction Trend graph drew successfully with multi-session stamina trajectory!");

console.log("\n>>> ALL EMBEDDED CHARTS MATH & RENDERING TESTS PASSED 100% <<<");
