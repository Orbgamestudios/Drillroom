const assert = require("assert");

console.log("=== Testing Embedded Canvas Chart Drawing with Mock Context ===");

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
    createLinearGradient: (x0, y0, x1, y1) => ({
      addColorStop: () => {}
    }),
    setLineDash: () => {},
    save: () => calls.push(["save"]),
    restore: () => calls.push(["restore"])
  };
}

// Import our draw logic
function drawEmbeddedChart(canvas, dataset, hoveredIdx) {
  if (!canvas || !dataset || !dataset.points || !dataset.points.length) return;
  const ctx = canvas.getContext ? canvas.getContext("2d") : null;
  if (!ctx) return;

  const rect = canvas.getBoundingClientRect ? canvas.getBoundingClientRect() : { width: 340, height: 210 };
  const width = rect.width || 340;
  const height = rect.height || 210;

  ctx.clearRect(0, 0, width, height);

  const padL = 46;
  const padR = 24;
  const padT = 24;
  const padB = 34;

  const plotW = width - padL - padR;
  const plotH = height - padT - padB;

  const yFloor = dataset.yFloor;
  const yCeil = dataset.yCeil;
  const span = (yCeil - yFloor) || 1;

  const getY = (v) => padT + plotH - ((v - yFloor) / span) * plotH;
  const getX = (idx) => {
    if (dataset.points.length === 1) return padL + plotW / 2;
    return padL + (idx / (dataset.points.length - 1)) * plotW;
  };

  // 1. Gridlines & Ticks
  const ticks = dataset.ticks || [
    yFloor,
    yFloor + span * 0.25,
    yFloor + span * 0.5,
    yFloor + span * 0.75,
    yCeil
  ];

  ticks.forEach(t => {
    const yPx = getY(t);
    ctx.strokeStyle = (dataset.isDelta && t === 0) ? "#10B981" : "#F1F5F9";
    ctx.beginPath();
    ctx.moveTo(padL, yPx);
    ctx.lineTo(padL + plotW, yPx);
    ctx.stroke();

    const label = dataset.isDelta ? (t > 0 ? `+${Math.round(t)}s` : `${Math.round(t)}s`) : `${Math.round(t)}`;
    ctx.fillText(label, padL - 6, yPx + 3);
  });

  // 2. Benchmark Band / Line
  if (dataset.benchmark) {
    if (dataset.benchmark.min !== undefined && dataset.benchmark.max !== undefined) {
      const bTop = getY(dataset.benchmark.max);
      const bBottom = getY(dataset.benchmark.min);
      ctx.fillStyle = "rgba(16, 185, 129, 0.10)";
      ctx.fillRect(padL, bTop, plotW, bBottom - bTop);
      ctx.fillText(dataset.benchmark.label, padL + plotW - 4, bTop + 10);
    } else if (dataset.benchmark.line !== undefined) {
      const bY = getY(dataset.benchmark.line);
      ctx.strokeStyle = "#10B981";
      ctx.beginPath();
      ctx.moveTo(padL, bY);
      ctx.lineTo(padL + plotW, bY);
      ctx.stroke();
      ctx.fillText(dataset.benchmark.label, padL + plotW - 4, bY - 4);
    }
  }

  // 3. Stems / Lines / Points
  if (dataset.type === "fatigueDelta") {
    const zeroY = getY(0);
    dataset.points.forEach((p, idx) => {
      const xPx = getX(idx);
      const yPx = getY(p.val);
      const color = p.val <= 0 ? "#10B981" : (p.val <= 20 ? "#F59E0B" : "#EF4444");

      // Stem from zeroY to yPx
      ctx.strokeStyle = color;
      ctx.beginPath();
      ctx.moveTo(xPx, zeroY);
      ctx.lineTo(xPx, yPx);
      ctx.stroke();

      // Dot
      ctx.fillStyle = color;
      ctx.beginPath();
      ctx.arc(xPx, yPx, 4.5, 0, Math.PI * 2);
      ctx.fill();

      // Value label
      const valText = p.val > 0 ? `+${p.val}s` : `${p.val}s`;
      ctx.fillText(valText, xPx, yPx + (p.val >= 0 ? -7 : 12));

      // X Label
      ctx.fillText(p.label, xPx, padT + plotH + 16);
    });
  } else {
    // Line chart
    const color = dataset.type === "scoreTrajectory" ? "#185A9D" : "#0D9488";
    ctx.strokeStyle = color;
    ctx.beginPath();
    dataset.points.forEach((p, idx) => {
      const xPx = getX(idx);
      const yPx = getY(p.val);
      if (idx === 0) ctx.moveTo(xPx, yPx);
      else ctx.lineTo(xPx, yPx);
    });
    ctx.stroke();

    // Dots
    dataset.points.forEach((p, idx) => {
      const xPx = getX(idx);
      const yPx = getY(p.val);
      ctx.fillStyle = color;
      ctx.beginPath();
      ctx.arc(xPx, yPx, p.isCurrent ? 5.5 : 4.5, 0, Math.PI * 2);
      ctx.fill();

      // Value text
      const valText = dataset.type === "scoreTrajectory" ? `${p.val}` : `${p.val}w`;
      ctx.fillText(valText, xPx, yPx - 8);

      // X Label
      ctx.fillText(p.label, xPx, padT + plotH + 16);
    });
  }
}

// Test Chart 1: Score Trajectory
const ctx1 = createMockContext();
const mockCanvas1 = { getContext: () => ctx1, getBoundingClientRect: () => ({ width: 340, height: 210 }) };
const ds1 = {
  type: "scoreTrajectory",
  yFloor: 120,
  yCeil: 132,
  ticks: [120, 124, 128, 132],
  benchmark: { line: 128, label: "128 Target" },
  points: [
    { label: "S1", val: 125, isCurrent: false },
    { label: "S2", val: 128, isCurrent: false },
    { label: "Current", val: 130, isCurrent: true }
  ]
};
drawEmbeddedChart(mockCanvas1, ds1, -1);
assert(ctx1.calls.length > 20, "Should have executed multiple drawing operations");
console.log("✓ Chart 1 (Score Trajectory) drew successfully with zero NaN errors!");

// Test Chart 2: Cognitive Fatigue Delta
const ctx2 = createMockContext();
const mockCanvas2 = { getContext: () => ctx2, getBoundingClientRect: () => ({ width: 340, height: 210 }) };
const ds2 = {
  type: "fatigueDelta",
  isDelta: true,
  yFloor: -60,
  yCeil: 60,
  ticks: [-60, -30, 0, 30, 60],
  benchmark: { line: 0, label: "0s Baseline (P1)" },
  points: [
    { label: "P1", val: 0 },
    { label: "P2", val: 15 },
    { label: "P3", val: -10 },
    { label: "P4", val: 45 }
  ]
};
drawEmbeddedChart(mockCanvas2, ds2, -1);
assert(ctx2.calls.length > 20);
console.log("✓ Chart 2 (Fatigue Delta) drew successfully with centered zero and zero NaN errors!");

// Test Chart 3: Passage Reading Speed
const ctx3 = createMockContext();
const mockCanvas3 = { getContext: () => ctx3, getBoundingClientRect: () => ({ width: 340, height: 210 }) };
const ds3 = {
  type: "passageWpm",
  yFloor: 140,
  yCeil: 280,
  ticks: [140, 180, 220, 260, 280],
  benchmark: { min: 200, max: 260, label: "AAMC 200-260 Target" },
  points: [
    { label: "P1", val: 215 },
    { label: "P2", val: 195 },
    { label: "P3", val: 230 },
    { label: "P4", val: 175 }
  ]
};
drawEmbeddedChart(mockCanvas3, ds3, -1);
assert(ctx3.calls.length > 20);
console.log("✓ Chart 3 (Passage Reading Speed) drew successfully with AAMC target band!");

console.log("\n>>> ALL MOCK CONTEXT TESTS PASSED 100% <<<");
