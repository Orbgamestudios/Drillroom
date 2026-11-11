// Scratch test for clock pacing color logic and Gemini model fallback
const assert = require("assert");

console.log("=== Running Clock Pacing & Gemini Model Tests ===");

// 1. Clock Pacing Math Simulation
function computePacingDelta(E) {
  const qs = E.s.qs;
  const N = qs.length;

  let totalSec = E._totalSec;
  if (!totalSec) {
    if (E.s.secPerQ) totalSec = Math.round(E.s.secPerQ * N);
    else if (E._peRef && E._peRef.exam && E._peRef.exam.duration) totalSec = E._peRef.exam.duration * 60;
    else if (E._origLeft) totalSec = E._origLeft;
    else totalSec = (E.left || 5400);
    E._totalSec = totalSec;
  }

  const secPerQ = (E.s.secPerQ && E.s.secPerQ > 0) ? E.s.secPerQ : (totalSec / N);

  let answeredCount = 0;
  let activeTotal = 0;
  for (let j = 0; j < N; j++) {
    const q = qs[j];
    const isSk = q && (q._isSkipped || (E.ans && E.ans[j] === -1));
    if (!isSk) {
      activeTotal++;
      if (E.ans && E.ans[j] !== null && E.ans[j] !== undefined && E.ans[j] !== -1) {
        answeredCount++;
      }
    }
  }
  if (activeTotal === 0) activeTotal = N;

  const remainingToAnswer = Math.max(0, activeTotal - answeredCount);
  const timeRemaining = Math.max(0, E.left);

  const currIdx = (typeof E.i === "number" && E.i >= 0 && E.i < N) ? E.i : 0;
  const currIsAnswered = (E.ans && E.ans[currIdx] !== null && E.ans[currIdx] !== undefined && E.ans[currIdx] !== -1);

  let deltaSec = 0;
  if (currIsAnswered || remainingToAnswer === 0) {
    const timeNeeded = remainingToAnswer * secPerQ;
    deltaSec = timeRemaining - timeNeeded;
  } else {
    const targetStart = remainingToAnswer * secPerQ;
    const targetEnd = (remainingToAnswer - 1) * secPerQ;
    if (timeRemaining > targetStart) {
      deltaSec = timeRemaining - targetStart;
    } else if (timeRemaining < targetEnd) {
      deltaSec = timeRemaining - targetEnd;
    } else {
      deltaSec = 0;
    }
  }

  return { deltaSec, remainingToAnswer, answeredCount, totalSec, secPerQ };
}

function getClockStyle(deltaSec) {
  if (Math.abs(deltaSec) <= 15) {
    return {
      color: "#FFFFFF",
      background: "rgba(255, 255, 255, 0.12)",
      borderColor: "rgba(255, 255, 255, 0.22)",
      title: "Pacing: On schedule",
      status: "neutral"
    };
  }

  if (deltaSec > 15) {
    const t = Math.min(1, (deltaSec - 15) / 285);
    const r = Math.round(255 - t * (255 - 74));
    const g = Math.round(255 - t * (255 - 222));
    const b = Math.round(255 - t * (255 - 128));
    const bgA = (0.12 + 0.20 * t).toFixed(2);
    const bdA = (0.25 + 0.40 * t).toFixed(2);

    const aheadSec = Math.round(deltaSec);
    const mAhead = Math.floor(aheadSec / 60);
    const sAhead = aheadSec % 60;
    const title = mAhead > 0 ? `Pacing: ${mAhead}m ${sAhead}s ahead of schedule` : `Pacing: ${sAhead}s ahead of schedule`;

    return {
      color: `rgb(${r}, ${g}, ${b})`,
      background: `rgba(34, 197, 94, ${bgA})`,
      borderColor: `rgba(74, 222, 128, ${bdA})`,
      title,
      status: "ahead",
      t
    };
  } else {
    const behindSec = Math.round(Math.abs(deltaSec));
    const t = Math.min(1, (behindSec - 15) / 285);

    let r, g, b;
    if (t < 0.35) {
      const p = t / 0.35;
      r = Math.round(255 - p * (255 - 251));
      g = Math.round(255 - p * (255 - 146));
      b = Math.round(255 - p * (255 - 60));
    } else if (t < 0.70) {
      const p = (t - 0.35) / 0.35;
      r = Math.round(251 - p * (251 - 248));
      g = Math.round(146 - p * (146 - 113));
      b = Math.round(60 + p * (113 - 60));
    } else {
      const p = (t - 0.70) / 0.30;
      r = Math.round(248 - p * (248 - 239));
      g = Math.round(113 - p * (113 - 68));
      b = Math.round(113 - p * (113 - 68));
    }

    const bgA = (0.12 + 0.22 * t).toFixed(2);
    const bdA = (0.28 + 0.45 * t).toFixed(2);

    const mBehind = Math.floor(behindSec / 60);
    const sBehind = behindSec % 60;
    const title = mBehind > 0 ? `Pacing: ${mBehind}m ${sBehind}s behind schedule` : `Pacing: ${sBehind}s behind schedule`;

    return {
      color: `rgb(${r}, ${g}, ${b})`,
      background: `rgba(239, 68, 68, ${bgA})`,
      borderColor: `rgba(248, 113, 113, ${bdA})`,
      title,
      status: "behind",
      t
    };
  }
}

// Test Case 1: Start of 90m exam (53 questions, 5400s)
const exam1 = {
  s: { qs: Array(53).fill({ q: "Stem", ch: ["A","B","C","D"], a: 0 }), secPerQ: 5400 / 53 },
  i: 0,
  ans: Array(53).fill(null),
  left: 5400
};
let p1 = computePacingDelta(exam1);
let s1 = getClockStyle(p1.deltaSec);
assert.strictEqual(s1.status, "neutral");
assert.strictEqual(s1.title, "Pacing: On schedule");
console.log("✓ Test 1 Passed: Exam Start -> Neutral");

// Test Case 2: 40 seconds into Question 1 (unanswered, well within 101.88s budget)
exam1.left = 5400 - 40;
let p2 = computePacingDelta(exam1);
let s2 = getClockStyle(p2.deltaSec);
assert.strictEqual(s2.status, "neutral");
assert.strictEqual(s2.title, "Pacing: On schedule");
console.log("✓ Test 2 Passed: 40s on Q1 -> Still Neutral (within question budget)");

// Test Case 3: Answered Q1 at 40s (now on Q2, 61s ahead)
exam1.ans[0] = 0;
exam1.i = 1;
exam1.left = 5400 - 40; // 5360s left
let p3 = computePacingDelta(exam1);
let s3 = getClockStyle(p3.deltaSec);
assert.strictEqual(s3.status, "ahead");
assert(p3.deltaSec > 60);
assert(s3.title.includes("ahead of schedule"));
console.log(`✓ Test 3 Passed: Q1 answered in 40s -> Ahead by ${Math.round(p3.deltaSec)}s (${s3.color})`);

// Test Case 4: Answered 10 questions in 500s (budget was 1018s -> ~518s ahead, saturated green)
exam1.ans = Array(10).fill(0).concat(Array(43).fill(null));
exam1.i = 10;
exam1.left = 5400 - 500; // 4900s left
let p4 = computePacingDelta(exam1);
let s4 = getClockStyle(p4.deltaSec);
assert.strictEqual(s4.status, "ahead");
assert.strictEqual(s4.t, 1.0); // max green
assert.strictEqual(s4.color, "rgb(74, 222, 128)");
console.log("✓ Test 4 Passed: 10 Qs rapid -> Full Emerald Green (rgb(74, 222, 128))");

// Test Case 5: Bogged down on Q1 (spent 200s on Q1 without answering -> 200 - 101.88 = 98s behind)
const exam2 = {
  s: { qs: Array(53).fill({ q: "Stem", ch: ["A","B","C","D"], a: 0 }), secPerQ: 5400 / 53 },
  i: 0,
  ans: Array(53).fill(null),
  left: 5400 - 200 // 5200s left, but targetEnd was 5298s -> behind by ~98s
};
let p5 = computePacingDelta(exam2);
let s5 = getClockStyle(p5.deltaSec);
assert.strictEqual(s5.status, "behind");
assert(p5.deltaSec < -90);
assert(s5.title.includes("behind schedule"));
console.log(`✓ Test 5 Passed: 200s on Q1 -> Behind by ${Math.round(Math.abs(p5.deltaSec))}s (${s5.color})`);

// Test Case 6: Severely behind (5 questions done, but spent 40 minutes = 2400s; should have taken ~509s -> ~1891s behind)
const exam3 = {
  s: { qs: Array(53).fill({ q: "Stem", ch: ["A","B","C","D"], a: 0 }), secPerQ: 5400 / 53 },
  i: 5,
  ans: Array(5).fill(0).concat(Array(48).fill(null)),
  left: 5400 - 2400 // 3000s left
};
let p6 = computePacingDelta(exam3);
let s6 = getClockStyle(p6.deltaSec);
assert.strictEqual(s6.status, "behind");
assert.strictEqual(s6.t, 1.0); // max red
assert.strictEqual(s6.color, "rgb(239, 68, 68)");
console.log("✓ Test 6 Passed: Major time sink -> Urgent Crimson (rgb(239, 68, 68))");

// Test Case 7: Verify Zero Emojis in all titles
[s1, s2, s3, s4, s5, s6].forEach((st, idx) => {
  const hasEmoji = /[\uD800-\uDBFF][\uDC00-\uDFFF]|\p{Emoji_Presentation}/gu.test(st.title);
  assert.strictEqual(hasEmoji, false, `Emoji found in test case ${idx + 1}`);
});
console.log("✓ Test 7 Passed: Zero emojis verified in all tooltips");

console.log("All clock tests PASSED successfully!");
