// Test Delta Graph Formatting and 0-in-the-middle calculations
const assert = require("assert");

console.log("=== Testing Delta Graph Center-Zero Calculation ===");

function computeYAxisBounds(vals, metricDef) {
  let minVal = Math.min(...vals);
  let maxVal = Math.max(...vals);

  const bench = metricDef.benchmark;
  if (bench) {
    if (bench.min !== undefined) minVal = Math.min(minVal, bench.min);
    if (bench.max !== undefined) maxVal = Math.max(maxVal, bench.max);
    if (bench.line !== undefined) {
      minVal = Math.min(minVal, bench.line);
      maxVal = Math.max(maxVal, bench.line);
    }
  }

  const isDelta = !!(
    metricDef.isDelta ||
    metricDef.id.toLowerCase().includes("delta") ||
    (bench && bench.line === 0) ||
    metricDef.id === "netSecondGuessing"
  );

  if (isDelta) {
    // Symmetrical range around 0
    let absMax = Math.max(Math.abs(minVal), Math.abs(maxVal));
    if (absMax === 0) absMax = metricDef.unit === "s" ? 30 : (metricDef.unit === "%" ? 15 : 5);
    
    // Add 15% breathing room
    let M = absMax * 1.15;

    // Round up to clean increments
    if (metricDef.unit === "s") {
      if (M <= 30) M = Math.ceil(M / 10) * 10;
      else if (M <= 90) M = Math.ceil(M / 15) * 15;
      else M = Math.ceil(M / 30) * 30;
    } else if (metricDef.unit === "%") {
      M = Math.ceil(M / 5) * 5;
    } else if (metricDef.unit === "pts" || metricDef.unit === "guesses") {
      M = Math.ceil(M / 2) * 2;
    } else {
      M = Math.ceil(M / 10) * 10;
    }

    const yFloor = -M;
    const yCeil = +M;
    const numYTicks = 4; // 4 intervals gives 5 ticks: -M, -M/2, 0, +M/2, +M
    const ticks = [];
    for (let i = 0; i <= numYTicks; i++) {
      ticks.push(yFloor + (i / numYTicks) * (yCeil - yFloor));
    }

    return { isDelta, yFloor, yCeil, M, ticks };
  } else {
    // Standard non-delta bounds
    if (minVal === maxVal) {
      minVal = Math.max(0, minVal - 10);
      maxVal = maxVal + 10;
    }
    const valSpan = maxVal - minVal || 1;
    const yFloor = Math.max(0, Math.floor(minVal - valSpan * 0.1));
    const yCeil = Math.ceil(maxVal + valSpan * 0.1);
    const numYTicks = 5;
    const ticks = [];
    for (let i = 0; i <= numYTicks; i++) {
      ticks.push(yFloor + (i / numYTicks) * (yCeil - yFloor));
    }
    return { isDelta, yFloor, yCeil, ticks };
  }
}

// Test Case 1: passageFatigueDelta with mixed positive and negative values
const metric1 = {
  id: "passageFatigueDelta",
  unit: "s",
  benchmark: { line: 0, label: "Baseline (P1)" },
  isDelta: true
};
const vals1 = [0, -22, +15, +48, -10];
const r1 = computeYAxisBounds(vals1, metric1);

assert.strictEqual(r1.isDelta, true);
assert.strictEqual(r1.yFloor, -r1.yCeil, "yFloor must equal -yCeil for 0 to be dead-center");
assert.strictEqual(r1.ticks[2], 0, "Middle tick (index 2 of 5) must be exactly 0");
console.log("✓ Test 1 Passed: Fatigue Delta has symmetric bounds [", r1.yFloor, ",", r1.yCeil, "] with 0 in middle tick:", r1.ticks);

// Test Case 2: netSecondGuessing (-2 to +3 points)
const metric2 = {
  id: "netSecondGuessing",
  unit: "pts",
  benchmark: { line: 0, label: "Break-even (0)" },
  isDelta: true
};
const vals2 = [+1, -2, +3, 0];
const r2 = computeYAxisBounds(vals2, metric2);
assert.strictEqual(r2.isDelta, true);
assert.strictEqual(r2.yFloor, -r2.yCeil);
assert.strictEqual(r2.ticks[2], 0);
console.log("✓ Test 2 Passed: Second Guessing Net Impact has symmetric bounds [", r2.yFloor, ",", r2.yCeil, "] with 0 in middle tick:", r2.ticks);

// Test Case 3: avgSessionFatigueDelta (Session fatigue trend)
const metric3 = {
  id: "avgSessionFatigueDelta",
  unit: "s",
  benchmark: { line: 0, label: "Zero Fatigue (0s)" },
  isDelta: true
};
const vals3 = [+55, +40, +18, -5];
const r3 = computeYAxisBounds(vals3, metric3);
assert.strictEqual(r3.isDelta, true);
assert.strictEqual(r3.yFloor, -r3.yCeil);
assert.strictEqual(r3.ticks[2], 0);
console.log("✓ Test 3 Passed: Session Fatigue Delta has symmetric bounds [", r3.yFloor, ",", r3.yCeil, "] with 0 in middle tick:", r3.ticks);

// Test Case 4: Non-delta metric (e.g. passageWpm) remains non-delta
const metric4 = {
  id: "passageWpm",
  unit: "WPM",
  benchmark: { min: 200, max: 260 }
};
const vals4 = [180, 215, 230, 195];
const r4 = computeYAxisBounds(vals4, metric4);
assert.strictEqual(r4.isDelta, false);
assert(r4.yFloor >= 0);
console.log("✓ Test 4 Passed: Regular non-delta metric preserves standard positive floor:", r4.yFloor);

console.log("All Delta Chart Math tests PASSED successfully!");
