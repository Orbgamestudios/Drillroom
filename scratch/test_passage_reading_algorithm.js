/**
 * scratch/test_passage_reading_algorithm.js
 * Comprehensive verification of the Latent Passage Reading Decomposition Algorithm
 * and real-MCAT clean interface (zero visible timers / buttons during exam).
 */

const fs = require('fs');
const vm = require('vm');

const elements = {};
function createMockElement(id = '') {
  const el = {
    id: id,
    className: '',
    classList: {
      _classes: new Set(),
      add(c) { this._classes.add(c); },
      remove(c) { this._classes.delete(c); },
      toggle(c, f) {
        if (f === undefined) f = !this._classes.has(c);
        f ? this._classes.add(c) : this._classes.delete(c);
        return f;
      },
      contains(c) { return this._classes.has(c); }
    },
    style: {},
    children: [],
    dataset: {},
    appendChild(child) { this.children.push(child); return child; },
    insertBefore(newChild, refChild) {
      const idx = this.children.indexOf(refChild);
      if (idx >= 0) this.children.splice(idx, 0, newChild);
      else this.children.push(newChild);
      return newChild;
    },
    querySelector(sel) {
      if (sel.startsWith('#')) return elements[sel.slice(1)] || null;
      if (sel.startsWith('.')) {
        const cls = sel.slice(1);
        const findIn = (node) => {
          if (node.classList && node.classList.contains(cls)) return node;
          for (const ch of (node.children || [])) {
            const found = findIn(ch);
            if (found) return found;
          }
          return null;
        };
        return findIn(this);
      }
      return createMockElement();
    },
    querySelectorAll(sel) {
      const results = [];
      if (sel.startsWith('.')) {
        const cls = sel.slice(1);
        const search = (node) => {
          if (node.classList && node.classList.contains(cls)) results.push(node);
          for (const ch of (node.children || [])) search(ch);
        };
        search(this);
      }
      return results;
    },
    addEventListener() {},
    dispatchEvent() {},
    scrollTop: 0,
    get innerHTML() { return this._html || ''; },
    set innerHTML(val) { this._html = val; this.children = []; },
    textContent: '',
    value: '',
    disabled: false,
    checked: false
  };
  if (id) elements[id] = el;
  return el;
}

const standardIds = [
  'pass', 'qp', 'ebody', 'tSect', 'tCount', 'qno', 'qtx', 'fChk', 'fLbl', 'opts',
  'conf', 'bPrev', 'bNext', 'clk', 'padTxt', 'calcIn', 'calcOut', 'paused', 'tPause',
  'res', 'zT', 'zL', 'zS', 'zB', 'zV', 'zPass', 'zTimingTelemetry', 'zGeminiAnalysis', 'zList', 'zSave',
  'tabPractice', 'tabHistory', 'nT', 'nav', 'pePassageReadBarWrap'
];
standardIds.forEach(id => createMockElement(id));

const store = {};
const sandbox = {
  console: console,
  window: null,
  clearInterval: () => {},
  setInterval: () => 1,
  timerId: 1,
  strike: false,
  $: (id) => elements[id] || (elements[id] = createMockElement(id)),
  document: {
    getElementById: (id) => elements[id] || (elements[id] = createMockElement(id)),
    querySelector: (sel) => {
      if (sel.startsWith('#')) return elements[sel.slice(1)] || (elements[sel.slice(1)] = createMockElement(sel.slice(1)));
      return createMockElement();
    },
    querySelectorAll: () => [createMockElement()],
    createElement: (tag) => {
      const el = createMockElement();
      el.tagName = tag.toUpperCase();
      return el;
    },
    addEventListener: () => {},
    body: createMockElement('body')
  },
  localStorage: {
    getItem: (k) => store[k] || null,
    setItem: (k, v) => { store[k] = String(v); },
    removeItem: (k) => { delete store[k]; }
  },
  view: () => {},
  tick: () => {},
  flash: (m) => console.log('FLASH:', m),
  getQuestionArchetype: (q) => "Reasoning Within the Text"
};

sandbox.window = sandbox;
const context = vm.createContext(sandbox);

// Load practice_exam.js
const code = fs.readFileSync('/home/cgslinde/DrillRoom/DrillRoom/practice_exam.js', 'utf8');
vm.runInContext(code, context);

console.log('=== TEST 1: Clean Real-MCAT UI Verification (No Buttons / Visible Timers) ===');
const mockPassageText = "<div class='ttl'>Passage 1</div><p>" + "word ".repeat(580) + "</p>";
const mockQuestions = [
  { q: "What is the primary thesis?", ch: ["Choice A", "Choice B", "Choice C", "Choice D"], a: 0, _passage: mockPassageText, _setIdx: 0, _topic: "Philosophy of Art" },
  { q: "The author implies that...", ch: ["Choice A", "Choice B", "Choice C", "Choice D"], a: 1, _passage: mockPassageText, _setIdx: 0, _topic: "Philosophy of Art" },
  { q: "Which finding would weaken?", ch: ["Choice A", "Choice B", "Choice C", "Choice D"], a: 2, _passage: mockPassageText, _setIdx: 0, _topic: "Philosophy of Art" },
  { q: "According to paragraph 3...", ch: ["Choice A", "Choice B", "Choice C", "Choice D"], a: 3, _passage: mockPassageText, _setIdx: 0, _topic: "Philosophy of Art" },
  { q: "The term pseudo-individuality means...", ch: ["Choice A", "Choice B", "Choice C", "Choice D"], a: 0, _passage: mockPassageText, _setIdx: 0, _topic: "Philosophy of Art" },
  { q: "The author's tone is best described as...", ch: ["Choice A", "Choice B", "Choice C", "Choice D"], a: 2, _passage: mockPassageText, _setIdx: 0, _topic: "Philosophy of Art" }
];

const mockExam = {
  id: "test_cars_clean",
  sec: "CARS",
  duration: 90,
  label: "Critical Analysis and Reasoning Skills",
  suiteTitle: "Test Suite",
  sets: [{
    id: "set_1",
    sec: "CARS",
    topic: "Philosophy of Art",
    passage: mockPassageText,
    qs: mockQuestions
  }]
};

context.beginPracticeExam(mockExam);
const passHTML = elements['pass'].innerHTML;
const qnoHTML = elements['qno'].innerHTML;

console.log("Passage pane HTML contains 'btnDoneReading'?:", passHTML.includes('btnDoneReading'));
console.log("Passage pane HTML contains 'Done Reading Passage'?:", passHTML.includes('Done Reading Passage'));
console.log("Passage pane HTML contains 'pePassClock'?:", passHTML.includes('pePassClock'));
console.log("Question header contains 'peQTimer'?:", qnoHTML.includes('peQTimer'));
console.log("Question header contains 'Time on this Q'?:", qnoHTML.includes('Time on this Q'));
console.log("Question header textContent strictly 'Question 1'?:", qnoHTML.trim() === 'Question 1');

if (passHTML.includes('btnDoneReading') || passHTML.includes('Done Reading Passage') || passHTML.includes('pePassClock')) {
  throw new Error("FAIL: Active passage pane still contains visible button or clock!");
}
if (qnoHTML.includes('peQTimer') || qnoHTML.includes('Time on this Q')) {
  throw new Error("FAIL: Question header still contains live question timer!");
}
console.log(">>> TEST 1 PASSED: Real-MCAT clean interface verified! <<<\n");


console.log('=== TEST 2: Latent Passage Reading Decomposition Algorithm (LPRDA) ===');
// Scenario 1: Standard Examinee Flow (600 words)
// Spends 220s on Q1 (reading passage + solving Q1).
// Spends ~60s on Q2, 55s on Q3, 65s on Q4, 50s on Q5, 70s on Q6.
const PE = context.PE;
PE._qTimes = [220, 60, 55, 65, 50, 70]; // Total = 520s
PE._passageTelemetry = {
  0: {
    firstAnswerExamSec: 1000 + 220,
    totalPreAnswerDwell: 220,
    qDwellBeforeFirstAnswer: { 0: 220 }
  }
};

const result1 = context.calculatePassageReadingTelemetry(PE, PE.questions);
const pStat1 = result1.passageStats[0];

console.log("Scenario 1 Calculated Passage Reading Time:", `${Math.floor(pStat1.readSec / 60)}m ${pStat1.readSec % 60}s (${pStat1.readSec}s)`);
console.log("Scenario 1 Calculated Reading Speed:", `${pStat1.wpm} WPM`);
console.log("Scenario 1 Decomposed Question Solve Times:", result1.decomposedQTimes);

// Verification:
// Baseline solve for other questions is median(60, 55, 65, 50, 70) = 60s.
// Overhead on Q1 is 60s, so raw reading estimate is 220 - 60 = 160s.
// Clamped to plausible range: 160s (~218 WPM, right in the optimal 200-270 WPM zone).
if (pStat1.readSec < 140 || pStat1.readSec > 180) {
  throw new Error(`FAIL: Expected readSec between 140s and 180s, got ${pStat1.readSec}s`);
}
if (pStat1.wpm < 200 || pStat1.wpm > 260) {
  throw new Error(`FAIL: Expected WPM in optimal MCAT range (200-260), got ${pStat1.wpm}`);
}
if (result1.decomposedQTimes[0] < 50 || result1.decomposedQTimes[0] > 70) {
  throw new Error(`FAIL: Q1 decomposed solve time should be ~60s, got ${result1.decomposedQTimes[0]}s`);
}

// Time conservation check
const rawTotal1 = PE._qTimes.reduce((a, b) => a + b, 0);
const decomposedTotal1 = pStat1.readSec + result1.decomposedQTimes.reduce((a, b) => a + b, 0);
console.log(`Time Conservation Check: Raw (${rawTotal1}s) == Decomposed + Read (${decomposedTotal1}s):`, rawTotal1 === decomposedTotal1);
if (rawTotal1 !== decomposedTotal1) {
  throw new Error(`FAIL: Total time not conserved! Raw=${rawTotal1}, Decomposed=${decomposedTotal1}`);
}
console.log(">>> Scenario 1 PASSED: Clean 2m 40s reading time isolated and Q1 solve normalized! <<<\n");


console.log('=== TEST 3: Question-First Skimmer Scenario ===');
// Examinee flips Q1 (10s), Q2 (15s), reads on Q2 for 160s before selecting first answer
PE._qTimes = [55, 195, 50, 55, 60, 50]; // Total = 465s
PE._passageTelemetry = {
  0: {
    firstAnswerExamSec: 1000 + 200,
    totalPreAnswerDwell: 185, // 10s on Q1 + 175s on Q2 before answer
    qDwellBeforeFirstAnswer: { 0: 10, 1: 175 }
  }
};

const result2 = context.calculatePassageReadingTelemetry(PE, PE.questions);
const pStat2 = result2.passageStats[0];

console.log("Scenario 2 Calculated Reading Time:", `${Math.floor(pStat2.readSec / 60)}m ${pStat2.readSec % 60}s (${pStat2.readSec}s)`);
console.log("Scenario 2 Decomposed Question Solve Times:", result2.decomposedQTimes);
const rawTotal2 = PE._qTimes.reduce((a, b) => a + b, 0);
const decomposedTotal2 = pStat2.readSec + result2.decomposedQTimes.reduce((a, b) => a + b, 0);
console.log(`Time Conservation Check: Raw (${rawTotal2}s) == Decomposed + Read (${decomposedTotal2}s):`, rawTotal2 === decomposedTotal2);

if (rawTotal2 !== decomposedTotal2) {
  throw new Error(`FAIL: Total time not conserved in Scenario 2!`);
}
console.log(">>> Scenario 2 PASSED: Question-first preview accounted for and conserved! <<<\n");


console.log('=== TEST 4: Exam Grading & Telemetry Box Integration ===');
// Set answers and confidences
PE.questions.forEach((q, idx) => {
  context.E.ans[idx] = q.a;
  context.E.conf[idx] = "sure";
});

context.gradePracticeExam();

const hist = context.getHistory();
const latestReview = hist[0].reviewData;
console.log("Graded scaled score:", hist[0].scaledScore);
console.log("Passage stats recorded count:", latestReview.passageStats.length);
console.log("First passage recorded reading time:", latestReview.passageStats[0].readSec + "s");
console.log("First passage recorded WPM:", latestReview.passageStats[0].wpm + " WPM");

if (!latestReview.passageStats || latestReview.passageStats.length !== 1) {
  throw new Error("FAIL: Expected passageStats in reviewData");
}
if (!latestReview.telemetry.qTimes || latestReview.telemetry.qTimes[0] > 100) {
  throw new Error("FAIL: Q1 time in telemetry should be decomposed question solve time, not raw time with reading overhead!");
}

// Render Telemetry Box
context.renderTimingTelemetryBox(latestReview);
const telBoxHTML = elements['zTimingTelemetry'].innerHTML;
console.log("Telemetry box contains 'Passage Reading Speed (WPM)'?:", telBoxHTML.includes("Passage Reading Speed (WPM)"));
console.log("Telemetry box contains WPM row with Optimal assessment?:", telBoxHTML.includes("Optimal (200-270 WPM)"));

if (!telBoxHTML.includes("Passage Reading Speed (WPM)") || !telBoxHTML.includes("Optimal (200-270 WPM)")) {
  throw new Error("FAIL: Timing telemetry box did not render passage reading table or optimal assessment");
}

console.log(">>> TEST 4 PASSED: Review telemetry and AI data packets verified! <<<\n");

console.log("==================================================================");
console.log(">>> ALL LATENT PASSAGE READING & CLEAN-MCAT TESTS PASSED 100%! <<<");
console.log("==================================================================");
