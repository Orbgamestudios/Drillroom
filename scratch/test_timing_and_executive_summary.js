const assert = require("assert");
const fs = require("fs");
const path = require("path");
const vm = require("vm");

console.log("=== TEST SUITE: Latent Timing Decomposition & Executive Summary Architecture ===");

const practiceExamCode = fs.readFileSync(path.join(__dirname, "../practice_exam.js"), "utf8");
const geminiAnalysisCode = fs.readFileSync(path.join(__dirname, "../gemini_analysis.js"), "utf8");

// Mock browser environment
const mockStorage = {};
const mockLocalStorage = {
  getItem: (k) => (k in mockStorage ? mockStorage[k] : null),
  setItem: (k, v) => { mockStorage[k] = String(v); },
  removeItem: (k) => { delete mockStorage[k]; }
};

const sandbox = {
  console,
  localStorage: mockLocalStorage,
  window: { addEventListener: () => {} },
  document: {
    getElementById: () => null,
    querySelectorAll: () => [],
    createElement: () => ({
      style: {},
      classList: { add: () => {}, remove: () => {} },
      appendChild: () => {},
      querySelectorAll: () => [],
      querySelector: () => null
    }),
    body: { appendChild: () => {} }
  },
  $: () => ({
    style: {},
    classList: { add: () => {}, remove: () => {}, contains: () => false, toggle: () => {} },
    textContent: "",
    innerHTML: "",
    appendChild: () => {},
    querySelectorAll: () => [],
    querySelector: () => null
  }),
  view: () => {},
  rawToScaled: (pct) => ({ score: 131, ptile: "99th" }),
  getQuestionArchetype: (q, sec) => {
    if (q && q.archetype) return q.archetype;
    return "Foundations of Comprehension";
  },
  stopPracticeExamTimer: () => {},
  setInterval: () => 123,
  clearInterval: () => {},
  clearHighlightsOnPassageChange: () => {},
  saveHighlightsForActiveQuestion: () => {},
  loadHighlightsForActiveQuestion: () => {},
  PRACTICE_EXAMS: [],
  addEventListener: () => {}
};

sandbox.window = sandbox;
sandbox.globalThis = sandbox;

vm.createContext(sandbox);
vm.runInContext(practiceExamCode, sandbox);
vm.runInContext(geminiAnalysisCode, sandbox);

// -------------------------------------------------------------
// TEST 1: Simulate the exact 3-passage CARS exam scenario
// -------------------------------------------------------------
console.log("\n--- TEST 1: Practice Exam Grading & Telemetry Attachment ---");

// Passage 1: 585 words, 6 questions (Q1 - Q6). First question has 215s dwell (reading + solve)
// Passage 2: 580 words, 6 questions (Q7 - Q12). First question has 287s dwell (reading + solve)
// Passage 3: 508 words, 6 questions (Q13 - Q18). First question has 265s dwell (reading + solve)
const p1Text = Array(585).fill("word").join(" ");
const p2Text = Array(580).fill("analysis").join(" ");
const p3Text = Array(508).fill("concept").join(" ");

const questions = [];
// Passage 1: Q1 to Q6
for (let i = 0; i < 6; i++) {
  questions.push({
    q: `Passage 1 Question ${i + 1}`,
    ch: ["Option A", "Option B", "Option C", "Option D"],
    a: 0,
    e: "Official rationale",
    _passage: p1Text,
    _setIdx: 0,
    _topic: "Passage 1",
    archetype: i === 0 ? "Foundations of Comprehension" : "Foundations of Comprehension"
  });
}
// Passage 2: Q7 to Q12
for (let i = 0; i < 6; i++) {
  questions.push({
    q: `Passage 2 Question ${i + 7}`,
    ch: ["Option A", "Option B", "Option C", "Option D"],
    a: 1,
    e: "Official rationale",
    _passage: p2Text,
    _setIdx: 1,
    _topic: "Passage 2",
    archetype: i === 0 ? "Inference & Implicit Assumption" : "Foundations of Comprehension"
  });
}
// Passage 3: Q13 to Q18
for (let i = 0; i < 6; i++) {
  questions.push({
    q: `Passage 3 Question ${i + 13}`,
    ch: ["Option A", "Option B", "Option C", "Option D"],
    a: 2,
    e: "Official rationale",
    _passage: p3Text,
    _setIdx: 2,
    _topic: "Passage 3",
    archetype: i === 4 ? "Inference & Implicit Assumption" : "Reasoning Beyond the Text"
  });
}

// Set up raw question dwell times
// Q1 = 215s (161s reading + 54s solve)
// Q2-Q6 = 54s each
// Q7 = 287s (233s reading + 54s solve)
// Q8-Q12 = 54s each
// Q13 = 269s (215s reading + 54s solve)
// Q14-Q18 = ~30-55s each
const rawQTimes = [
  215, 54, 54, 54, 54, 54,
  287, 54, 54, 54, 54, 54,
  269, 30, 30, 25, 55, 25
];

const mockExam = {
  id: "cars_diagnostic_test",
  sec: "CARS",
  duration: 60,
  label: "CARS Diagnostic Section"
};

sandbox.PE = {
  exam: mockExam,
  questions: questions,
  _qTimes: [...rawQTimes],
  _passageTelemetry: {
    0: { totalPreAnswerDwell: 215 },
    1: { totalPreAnswerDwell: 287 },
    2: { totalPreAnswerDwell: 269 }
  },
  _passageReadState: {},
  _answerChanges: [
    { wasCorrect: false, nowCorrect: true },
    { wasCorrect: false, nowCorrect: true },
    { wasCorrect: true, nowCorrect: false }
  ]
};

sandbox.E = {
  s: { id: mockExam.id, qs: questions, sec: "CARS", topic: mockExam.label },
  ans: questions.map((q, idx) => (idx === 16 ? 0 : q.a)), // Q17 is wrong (index 16)
  conf: questions.map((q, idx) => (idx === 16 ? "sure" : (idx === 9 ? "two" : "sure"))),
  left: 600,
  _isPracticeExam: true,
  _peRef: sandbox.PE
};

vm.runInContext("E = window.E; PE = window.PE;", sandbox);

// Run gradePracticeExam
sandbox.gradePracticeExam();

assert(sandbox.E._reviewData, "E._reviewData must be attached to active session");
assert(sandbox.E._telemetry, "E._telemetry must be attached to active session");
assert(sandbox.E._passageStats, "E._passageStats must be attached to active session");
assert(sandbox.E._decomposedQTimes, "E._decomposedQTimes must be attached to active session");
assert(sandbox.window._lastExamReviewData, "window._lastExamReviewData must be set");
console.log("  [PASSED] Session handles successfully attached reviewData, telemetry, and passageStats.");

const rev = sandbox.E._reviewData;
assert(rev.passageStats.length === 3, `Expected 3 passage stats, got ${rev.passageStats.length}`);

// Check that passage reading times are isolated
const p1Stat = rev.passageStats[0];
const p2Stat = rev.passageStats[1];
const p3Stat = rev.passageStats[2];
console.log(`  Passage 1: ${p1Stat.wordCount} words, ${p1Stat.readSec}s, ${p1Stat.wpm} WPM`);
console.log(`  Passage 2: ${p2Stat.wordCount} words, ${p2Stat.readSec}s, ${p2Stat.wpm} WPM`);
console.log(`  Passage 3: ${p3Stat.wordCount} words, ${p3Stat.readSec}s, ${p3Stat.wpm} WPM`);

assert(p1Stat.wpm >= 190 && p1Stat.wpm <= 240, `Passage 1 WPM expected ~208-218, got ${p1Stat.wpm}`);
assert(p2Stat.wpm >= 135 && p2Stat.wpm <= 165, `Passage 2 WPM expected ~149, got ${p2Stat.wpm}`);
assert(p3Stat.wpm >= 120 && p3Stat.wpm <= 160, `Passage 3 WPM expected ~128-142, got ${p3Stat.wpm}`);

// Check decomposed question times: Q1 (raw 215) and Q7 (raw 287) must be decoupled
const decQTimes = sandbox.E._decomposedQTimes;
console.log(`  Q1 Pure Answering Time: ${decQTimes[0]}s (Raw was ${rawQTimes[0]}s)`);
console.log(`  Q7 Pure Answering Time: ${decQTimes[6]}s (Raw was ${rawQTimes[6]}s)`);

assert(decQTimes[0] <= 80, `Q1 net solve time should be ~54-75s, got ${decQTimes[0]}s`);
assert(decQTimes[6] <= 80, `Q7 net solve time should be ~54-75s, got ${decQTimes[6]}s`);
assert(decQTimes[0] !== rawQTimes[0], "Q1 net solve time must NOT equal raw dwell time");
assert(decQTimes[6] !== rawQTimes[6], "Q7 net solve time must NOT equal raw dwell time");
console.log("  [PASSED] Latent passage reading time successfully deducted from first questions.");

// -------------------------------------------------------------
// TEST 2: extractCurrentExamInfo() verification
// -------------------------------------------------------------
console.log("\n--- TEST 2: extractCurrentExamInfo() Consistency ---");

const info = sandbox.extractCurrentExamInfo();
assert(info, "extractCurrentExamInfo() must return info object");
assert.strictEqual(info.scaledScore, 131, `Expected scaled score 131, got ${info.scaledScore}`);
assert.strictEqual(info.qTimes[0], decQTimes[0], "info.qTimes[0] must equal decomposed solve time");
assert.strictEqual(info.qTimes[6], decQTimes[6], "info.qTimes[6] must equal decomposed solve time");

console.log(`  Net Average Question Answering Time: ${info.avgQSec}s`);
assert(info.avgQSec >= 40 && info.avgQSec <= 70, `avgQSec expected ~45-60s, got ${info.avgQSec}`);

// Verify time sink questions: ZERO questions should be flagged >= 110s!
console.log(`  Time-sink questions count (>110s pure solve): ${info.timeSinkQuestions.length}`);
assert.strictEqual(info.timeSinkQuestions.length, 0, "No questions should be falsely flagged as time-sinks!");
console.log("  [PASSED] extractCurrentExamInfo() uses decomposed times and flags 0 false time-sinks.");

// -------------------------------------------------------------
// TEST 3: buildDiagnosticPrompt() verification
// -------------------------------------------------------------
console.log("\n--- TEST 3: buildDiagnosticPrompt() Structure & Prompt Formatting ---");

const prompt = sandbox.buildDiagnosticPrompt(info);

// 1. Executive Summary directive check
assert(prompt.includes("# Executive Summary: What You Most Need to Work On"), "Prompt must instruct AI to start with Executive Summary");
assert(prompt.includes("CRITICAL REQUIREMENT: The student wants an immediate, high-yield summary right at the top"), "Prompt must emphasize rapid read summary");
assert(prompt.includes("Quick Priority Punch List"), "Prompt must require Quick Priority Punch List");

// 2. Timing telemetry and WPM consistency check
assert(prompt.includes("Passage Reading Telemetry & Speed (WPM):"), "Prompt must include Passage Reading Telemetry block");
assert(prompt.includes(`Passage 1:** Reading Time: **${Math.floor(p1Stat.readSec / 60)}m`), "Prompt must include exact Passage 1 reading time");
assert(prompt.includes(`${p1Stat.wpm} WPM`), "Prompt must include exact Passage 1 WPM");
assert(prompt.includes(`${p2Stat.wpm} WPM`), "Prompt must include exact Passage 2 WPM");
assert(prompt.includes(`${p3Stat.wpm} WPM`), "Prompt must include exact Passage 3 WPM");

// 3. Question Answering decoupling note
assert(prompt.includes("CRITICAL PACING CONTEXT FOR EVALUATION:"), "Prompt must include CRITICAL PACING CONTEXT note");
assert(prompt.includes("The Question Answering Times and Archetype averages listed below reflect PURE question-answering time"), "Prompt must explicitly clarify pure question answering time");
assert(!prompt.includes("Time Spent on Question: 287 seconds"), "Prompt must NOT state Q7 took 287s");
assert(!prompt.includes("Time Spent on Question: 215 seconds"), "Prompt must NOT state Q1 took 215s");
console.log("  [PASSED] Diagnostic prompt contains Executive Summary instructions and pure timing telemetry.");

// -------------------------------------------------------------
// TEST 4: Markdown Renderer & Executive Summary Card Hook
// -------------------------------------------------------------
console.log("\n--- TEST 4: renderMarkdown() Executive Summary Card Hook ---");

const sampleAIOutput = `
# Executive Summary: What You Most Need to Work On
> [!IMPORTANT]
> **Priority Focus / #1 Blindspot:** You are committing to Confidently Wrong answers on Inference questions by over-extrapolating unstated author assumptions.
> 
> **Pacing Reality:** Your question solving speed is exceptional (54s/Q) and passage reading is methodical (166 WPM avg). Pacing is completely sound; do not rush.
> 
> **#1 Rule for Your Next Section:** Demand explicit textual proof before selecting any inference choice.

### Quick Priority Punch List
- **What Dropped Points:** Question 17 was missed with high confidence due to choosing an extreme distractor.
- **What Succeeded:** Flawless 100% accuracy on Foundations of Comprehension with zero lucky guesses.
- **Immediate Action Item:** Drill 10 Inference & Implicit Assumption questions with strict textual cross-referencing.

---

# 1. Executive Score Diagnostic & Metacognitive Calibration
Your score of 131/132 is 99th percentile.
`;

const renderedHtml = sandbox.renderGeminiMarkdown(sampleAIOutput);

assert(renderedHtml.includes('class="gemini-exec-summary-card"'), "Rendered HTML must contain gemini-exec-summary-card container");
assert(renderedHtml.includes('READ FIRST'), "Executive summary card must contain READ FIRST badge");
assert(renderedHtml.includes('HIGH PRIORITY:'), "Executive summary card must format [!IMPORTANT] alert");
assert(renderedHtml.includes('Quick Priority Punch List'), "Executive summary card must contain Quick Priority Punch List");
assert(renderedHtml.includes('<h2 style='), "Section 1 must render as a standard h2 header");

// Ensure executive summary card closes properly before section 1
const execCardIdx = renderedHtml.indexOf('class="gemini-exec-summary-card"');
const closeDivIdx = renderedHtml.indexOf('</div>', execCardIdx + 30);
const sec1Idx = renderedHtml.indexOf('Executive Score Diagnostic');
assert(closeDivIdx > execCardIdx && closeDivIdx < sec1Idx, "gemini-exec-summary-card must close before Section 1");
console.log("  [PASSED] renderMarkdown() cleanly encapsulates Executive Summary into high-impact callout card.");

// -------------------------------------------------------------
// TEST 5: Emoji Audit Verification
// -------------------------------------------------------------
console.log("\n--- TEST 5: Clean AAMC Interface (Zero Emojis) ---");
const geminiCode = fs.readFileSync(path.join(__dirname, "../gemini_analysis.js"), "utf8");
const forbiddenSymbols = ["✓", "✕", "⚠", "☘", "↷", "📊", "🎯", "💡", "✗"];
forbiddenSymbols.forEach(sym => {
  assert(!geminiCode.includes(`"${sym}`) && !geminiCode.includes(`'${sym}`) && !geminiCode.includes(`>${sym}`), `Forbidden emoji '${sym}' must not be in UI strings`);
});
console.log("  [PASSED] Zero emojis verified across gemini_analysis.js.");

console.log("\n=======================================================");
console.log(">>> ALL TIMING & EXECUTIVE SUMMARY TESTS PASSED 100% <<<");
console.log("=======================================================\n");
