const assert = require("assert");
const fs = require("fs");
const vm = require("vm");

console.log("=== Comprehensive Metric Scope Isolation & Cross-Axis Testing ===");

const code = fs.readFileSync("/home/cgslinde/DrillRoom/DrillRoom/performance_charts.js", "utf8");

function setupContext() {
  const mockStorage = {
    drillroom_history_v1: JSON.stringify([
      {
        id: "att_cars_adaptive_1",
        examId: "adaptive_cars_5p",
        sec: "CARS",
        suiteTitle: "Adaptive Study — CARS",
        label: "CARS Study (5 Passages)",
        duration: 50,
        scaledScore: 132,
        pct: 100,
        solid: 25,
        ts: Date.now() - 3600000,
        reviewData: {
          passageStats: [
            { pIndex: 1, setIdx: 0, topic: "Passage 1", wordCount: 585, readSec: 161, wpm: 218, acc: 100, avgQSec: 45 },
            { pIndex: 2, setIdx: 1, topic: "Passage 2", wordCount: 580, readSec: 233, wpm: 149, acc: 100, avgQSec: 52 },
            { pIndex: 3, setIdx: 2, topic: "Edmund Burke & Kant — The Aesthetic Sublime", wordCount: 610, readSec: 185, wpm: 198, acc: 100, avgQSec: 48 },
            { pIndex: 4, setIdx: 3, topic: "Passage 4", wordCount: 540, readSec: 170, wpm: 191, acc: 100, avgQSec: 50 },
            { pIndex: 5, setIdx: 4, topic: "Passage 5", wordCount: 575, readSec: 165, wpm: 209, acc: 100, avgQSec: 46 }
          ],
          qs: Array.from({ length: 25 }, (_, i) => ({
            setIdx: Math.floor(i / 5),
            time: 48,
            ans: 0,
            a: 0,
            conf: "sure"
          }))
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
      createElement: () => ({ style: {}, appendChild: () => {}, querySelector: () => null })
    }
  };
  sandbox.window = sandbox;
  sandbox.globalThis = sandbox;

  vm.createContext(sandbox);
  vm.runInContext(code, sandbox);
  return sandbox;
}

// Test 1: User switches from questions_single to passages_single with passageWpm
console.log("\n--- TEST 1: Switching from Question mode to Single-Section Passages with WPM ---");
const sb = setupContext();
sb.chartState.xAxisMode = "questions_single";
sb.chartState.withinX = "question";
sb.chartState.withinY = "qTime";
sb.chartState.yMetric = "passageWpm"; // Dropdown visibly showing passageWpm

sb.chartState.xAxisMode = "passages_single";
const ds1 = sb.getActiveChartDataset();
assert.strictEqual(ds1.metricDef.id, "passageWpm");
assert.strictEqual(ds1.points.length, 5);
assert.strictEqual(JSON.stringify(ds1.points.map(p => p.val)), JSON.stringify([218, 149, 198, 191, 209]));
assert.strictEqual(ds1.points[2].label, "Passage 3 (Edmund Burke & Kant — The Aesthetic Sublime)");
console.log("✓ Test 1 Passed: Points accurately evaluate to [218, 149, 198, 191, 209] WPM, not 0s!");

// Test 2: If yMetric was qTime when switching to passages_single, falls back safely to passageReadSec
console.log("\n--- TEST 2: qTime falls back to passage metric in passages_single ---");
sb.chartState.yMetric = "qTime";
sb.chartState.withinY = "qTime";
sb.chartState.xAxisMode = "passages_single";
const ds2 = sb.getActiveChartDataset();
assert(ds2.metricDef.scope === "within_passage");
assert.strictEqual(ds2.metricDef.id, "passageReadSec");
assert.strictEqual(JSON.stringify(ds2.points.map(p => p.val)), JSON.stringify([161, 233, 185, 170, 165]));
console.log("✓ Test 2 Passed: qTime cleanly fell back to passageReadSec:", ds2.points.map(p => p.val));

// Test 3: Switching to sessions with passageWpm maps cleanly to avgPassageWpm
console.log("\n--- TEST 3: Switching to Sessions mode maps passage metrics to session metrics ---");
sb.chartState.yMetric = "passageWpm";
sb.chartState.xAxisMode = "sessions";
const ds3 = sb.getActiveChartDataset();
assert.strictEqual(ds3.metricDef.id, "avgPassageWpm");
assert.strictEqual(ds3.metricDef.scope, "across");
console.log("✓ Test 3 Passed: passageWpm mapped to avgPassageWpm across sessions");

// Test 4: Switching from sessions (scaledScore) to passages_single defaults safely to a passage metric
console.log("\n--- TEST 4: scaledScore falls back to valid passage metric in passages_single ---");
sb.chartState.yMetric = "scaledScore";
sb.chartState.withinY = null;
sb.chartState.xAxisMode = "passages_single";
const ds4 = sb.getActiveChartDataset();
assert(ds4.metricDef.scope === "within_passage");
assert.strictEqual(ds4.metricDef.id, "passageWpm");
assert.strictEqual(JSON.stringify(ds4.points.map(p => p.val)), JSON.stringify([218, 149, 198, 191, 209]));
console.log("✓ Test 4 Passed: scaledScore fell back to passageWpm for passages_single");

// Test 5: passages_all with qTime falls back safely to passageReadSec
console.log("\n--- TEST 5: passages_all falls back safely if non-passage metric present ---");
sb.chartState.yMetric = "qTime";
sb.chartState.xAxisMode = "passages_all";
const ds5 = sb.getActiveChartDataset();
assert.strictEqual(ds5.metricDef.id, "passageReadSec");
assert.strictEqual(JSON.stringify(ds5.points.map(p => p.val)), JSON.stringify([161, 233, 185, 170, 165]));
console.log("✓ Test 5 Passed: passages_all safely evaluated passageReadSec");

console.log("\n>>> ALL SCOPE & AXIS ISOLATION TESTS PASSED 100% <<<");
