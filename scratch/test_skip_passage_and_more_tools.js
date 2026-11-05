/**
 * scratch/test_skip_passage_and_more_tools.js
 * Verification of:
 * 1. Clean Authentic MCAT bottom bar with 3-dots (•••) popover menu
 * 2. Non-MCAT tools encapsulated inside popover
 * 3. Skip Passage functionality: marks completed in bank, excludes from score
 * 4. Navigator and Review filter integration
 * 5. Gemini AI Analysis exclusion of skipped questions
 */

const fs = require('fs');
const vm = require('vm');
const path = require('path');

let testsPassed = 0;
let testsFailed = 0;

function assert(cond, msg) {
  if (cond) {
    console.log(`  ✓ ${msg}`);
    testsPassed++;
  } else {
    console.error(`  ✗ FAIL: ${msg}`);
    testsFailed++;
  }
}

console.log('=== TEST SUITE: Real-MCAT Bottom Bar & Skip Passage ===\n');

// 1. Verify DrillRoom.html structure
console.log('1. Verifying DrillRoom.html layout and CSS:');
const htmlContent = fs.readFileSync(path.join(__dirname, '../DrillRoom.html'), 'utf8');

assert(htmlContent.includes('id="tMore"'), 'DrillRoom.html contains #tMore button');
assert(htmlContent.includes('id="peMoreToolsPopup"'), 'DrillRoom.html contains #peMoreToolsPopup');
assert(htmlContent.includes('id="tSkipPassage"'), 'DrillRoom.html contains #tSkipPassage button');
assert(htmlContent.includes('id="peSkipBadge"'), 'DrillRoom.html contains #peSkipBadge');

// Verify tools inside .tools vs popup
const ftrRegex = /<div id="ftr">([\s\S]*?)<\/div>\s*<\/div>/;
const ftrMatch = htmlContent.match(ftrRegex);
assert(ftrMatch, 'Found #ftr in DrillRoom.html');
if (ftrMatch) {
  const ftrText = ftrMatch[0];
  const mainToolsRegex = /<div class="tools">([\s\S]*?)<\/div>/;
  const mainToolsMatch = ftrText.match(mainToolsRegex);
  assert(mainToolsMatch, 'Found .tools row in #ftr');
  if (mainToolsMatch) {
    const toolsStr = mainToolsMatch[1];
    assert(toolsStr.includes('id="tNav"'), '.tools contains authentic MCAT Navigator');
    assert(toolsStr.includes('id="tHl"'), '.tools contains authentic MCAT Highlight');
    assert(toolsStr.includes('id="tSt"'), '.tools contains authentic MCAT Strikethrough');
    assert(toolsStr.includes('id="tPt"'), '.tools contains authentic MCAT Periodic Table');
    assert(toolsStr.includes('id="tPause"'), '.tools contains authentic MCAT Pause');
    assert(toolsStr.includes('id="tEnd"'), '.tools contains authentic MCAT End Section');
    assert(toolsStr.includes('id="tMore"'), '.tools contains 3-dots #tMore button');
    assert(!toolsStr.includes('id="hlStick"'), '.tools does NOT contain distracting Sticky Highlight');
    assert(!toolsStr.includes('id="tUn"'), '.tools does NOT contain distracting Clear Highlights');
    assert(!toolsStr.includes('id="tPad"'), '.tools does NOT contain distracting Noteboard');
    assert(!toolsStr.includes('id="tSheet"'), '.tools does NOT contain distracting Review Sheet');
  }

  const popupRegex = /<div id="peMoreToolsPopup"[\s\S]*?<\/button>\s*<\/div>/;
  const popupMatch = ftrText.match(popupRegex);
  assert(popupMatch, 'Found #peMoreToolsPopup container');
  if (popupMatch) {
    const popupStr = popupMatch[0];
    assert(popupStr.includes('id="tSkipPassage"'), 'Popup contains Skip Passage button');
    assert(popupStr.includes('id="hlStick"'), 'Popup contains Sticky Highlight');
    assert(popupStr.includes('id="tUn"'), 'Popup contains Clear Highlights');
    assert(popupStr.includes('id="tPad"'), 'Popup contains Noteboard');
    assert(popupStr.includes('id="tSheet"'), 'Popup contains Review Sheet');
    assert(popupStr.includes('id="tExit"'), 'Popup contains Exit (No Score)');
  }
}

// 2. Set up DOM sandbox for practice_exam.js
console.log('\n2. Testing logic in practice_exam.js:');

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
      } else if (sel === 'button') {
        const search = (node) => {
          if (node.tagName === 'BUTTON') results.push(node);
          for (const ch of (node.children || [])) search(ch);
        };
        search(this);
      }
      return results;
    },
    getBoundingClientRect() {
      return { top: 0, bottom: 40, left: 200, right: 240, width: 40, height: 40 };
    }
  };
  if (id) elements[id] = el;
  return el;
}

[
  'root', 'top', 'tSect', 'tCount', 'clk', 'clkT', 'ebody', 'pass', 'qp', 'qno',
  'qtx', 'fChk', 'fLbl', 'opts', 'conf', 'ftr', 'bPrev', 'bNext', 'tNav', 'tHl',
  'tSt', 'tPt', 'tPause', 'tEnd', 'tMore', 'peMoreToolsPopup', 'tSkipPassage',
  'peSkipBadge', 'hlStick', 'tUn', 'tPad', 'tSheet', 'tExit', 'pExit', 'nav',
  'nT', 'res', 'zT', 'zL', 'zS', 'zB', 'zList', 'zPass', 'zV', 'zD', 'zA', 'zH', 'zArch', 'zTimeSinks', 'zMistakes', 'paused', 'padTxt',
  'calcIn', 'calcOut', 'pad', 'padX'
].forEach(id => createMockElement(id));

elements['peMoreToolsPopup'].classList.add('hide');
elements['ftr'].getBoundingClientRect = () => ({ top: 600, bottom: 640, left: 0, right: 1000, width: 1000, height: 40 });

const localStorageStore = {};
const mockLocalStorage = {
  getItem: (k) => localStorageStore[k] || null,
  setItem: (k, v) => { localStorageStore[k] = String(v); },
  removeItem: (k) => { delete localStorageStore[k]; },
  clear: () => { Object.keys(localStorageStore).forEach(k => delete localStorageStore[k]); }
};

const sandbox = {
  console: console,
  document: {
    getElementById: (id) => elements[id] || null,
    createElement: (tag) => {
      const el = createMockElement();
      el.tagName = tag.toUpperCase();
      let _id = '';
      Object.defineProperty(el, 'id', {
        get() { return _id; },
        set(val) { _id = val; elements[val] = el; }
      });
      return el;
    },
    querySelectorAll: (sel) => {
      if (sel === '#conf button') return [createMockElement(), createMockElement(), createMockElement()];
      return [];
    },
    addEventListener: () => {}
  },
  $: (id) => elements[id] || (elements[id] = createMockElement(id)),
  localStorage: mockLocalStorage,
  window: {
    addEventListener: () => {}
  },
  setTimeout: (fn) => setTimeout(fn, 0),
  clearTimeout: () => {},
  setInterval: () => 123,
  clearInterval: () => {},
  Date: Date,
  Math: Math,
  JSON: JSON,
  Array: Array,
  Object: Object,
  Set: Set,
  parseInt: parseInt,
  confirm: () => true,
  alert: () => {},
  view: () => {},
  tick: () => {},
  timerId: null,
  addEventListener: () => {},
  strike: false,
  hl: false,
  PRACTICE_EXAMS: [
    {
      id: "cars_60_1",
      sec: "CARS",
      duration: 60,
      suiteTitle: "Diagnostic Suite",
      label: "CARS Section 1",
      sets: [
        { id: "p1", topic: "Philosophy", passage: "Passage 1 content", qs: [{ q: "Q1", ch: ["A","B","C","D"], a: 0 }, { q: "Q2", ch: ["A","B","C","D"], a: 1 }] },
        { id: "p2", topic: "History", passage: "Passage 2 content", qs: [{ q: "Q3", ch: ["A","B","C","D"], a: 2 }, { q: "Q4", ch: ["A","B","C","D"], a: 3 }] }
      ]
    }
  ]
};
sandbox.globalThis = sandbox;
sandbox.window = sandbox;

const practiceExamCode = fs.readFileSync(path.join(__dirname, '../practice_exam.js'), 'utf8');
vm.createContext(sandbox);
vm.runInContext(practiceExamCode, sandbox);

// Test toggleMoreToolsPopup
console.log('Testing toggleMoreToolsPopup:');
assert(typeof sandbox.toggleMoreToolsPopup === 'function', 'toggleMoreToolsPopup exists');
assert(elements['peMoreToolsPopup'].classList.contains('hide'), 'Popup initially hidden');

sandbox.toggleMoreToolsPopup(true);
assert(!elements['peMoreToolsPopup'].classList.contains('hide'), 'Popup opened when show=true');
assert(elements['tMore'].classList.contains('on'), '#tMore has active .on class when popup is open');

sandbox.toggleMoreToolsPopup(false);
assert(elements['peMoreToolsPopup'].classList.contains('hide'), 'Popup closed when show=false');
assert(!elements['tMore'].classList.contains('on'), '#tMore removed .on class when popup is closed');

// Set up mock exam in E and PE
const testExam = {
  id: "cars_60_1",
  sec: "CARS",
  duration: 60,
  suiteTitle: "Diagnostic Suite",
  label: "CARS Section 1",
  sets: [
    { id: "p1", topic: "Philosophy", passage: "Passage 1 content", qs: [{ q: "Q1", ch: ["A","B","C","D"], a: 0 }, { q: "Q2", ch: ["A","B","C","D"], a: 1 }] },
    { id: "p2", topic: "History", passage: "Passage 2 content", qs: [{ q: "Q3", ch: ["A","B","C","D"], a: 2 }, { q: "Q4", ch: ["A","B","C","D"], a: 3 }] }
  ]
};
sandbox.registerExam(testExam.id, testExam.sec, testExam.label, testExam.duration, "60min", testExam.sets, "desc", "diag", testExam.suiteTitle);
sandbox.beginPracticeExam(testExam);

assert(sandbox.E && sandbox.E._isPracticeExam, 'Practice exam initialized');
assert(sandbox.E.s.qs.length === 4, 'Exam has 4 questions across 2 passages');

// Test isPassageAlreadyCompleted and updateSkipPassageButtonState
console.log('\nTesting passage completion state detection:');
assert(!sandbox.isPassageAlreadyCompleted(sandbox.E.s.qs[0]), 'Passage 1 initially NOT completed in bank');

sandbox.updateSkipPassageButtonState();
assert(elements['peSkipBadge'].textContent === '(Mark Done & Skip)', 'Badge shows (Mark Done & Skip) for uncompleted passage');

// Mark Passage 1 completed in bank
sandbox.markPassageSetCompletedInBank(sandbox.E.s.qs[0]);
assert(sandbox.isPassageAlreadyCompleted(sandbox.E.s.qs[0]), 'Passage 1 is now marked completed in bank');

sandbox.updateSkipPassageButtonState();
assert(elements['peSkipBadge'].textContent === '(Already Done)', 'Badge shows (Already Done) once passage is completed in bank');

// Test skipCurrentPassage
console.log('\nTesting skipCurrentPassage functionality:');
sandbox.E.i = 0; // Question 1 of Passage 1
sandbox.skipCurrentPassage();

assert(sandbox.E.s.qs[0]._isSkipped === true, 'Question 1 marked _isSkipped = true');
assert(sandbox.E.s.qs[1]._isSkipped === true, 'Question 2 marked _isSkipped = true');
assert(sandbox.E.ans[0] === -1, 'Question 1 ans marked -1');
assert(sandbox.E.ans[1] === -1, 'Question 2 ans marked -1');
assert(sandbox.E.conf[0] === 'skipped', 'Question 1 conf marked "skipped"');
assert(sandbox.E.conf[1] === 'skipped', 'Question 2 conf marked "skipped"');
assert(sandbox.E.i === 2, 'Auto-advanced to Question 3 (first question of Passage 2)');

// Verify Navigator displays skipped status
console.log('\nTesting Navigator status for skipped questions:');
elements['tNav'].onclick();
const navTableHtml = elements['nT'].innerHTML;
assert(navTableHtml.includes('Skipped (Completed)'), 'Navigator table displays "Skipped (Completed)" for skipped questions');

// Test unskipCurrentPassage
console.log('\nTesting unskipCurrentPassage:');
sandbox.E.i = 0; // Go back to Question 1
sandbox.drawPEQ();
assert(elements['peSkippedQBanner'].style.display !== 'none', 'Question pane displays skipped passage notice');
assert(elements['bNext'].disabled === false, 'bNext is NOT disabled on skipped questions');

sandbox.unskipCurrentPassage();
assert(sandbox.E.s.qs[0]._isSkipped === false, 'Question 1 unskipped');
assert(sandbox.E.s.qs[1]._isSkipped === false, 'Question 2 unskipped');
assert(sandbox.E.ans[0] === null, 'Question 1 ans reset to null');
assert(sandbox.E.conf[0] === null, 'Question 1 conf reset to null');

// Re-skip Passage 1, and answer Passage 2 questions
sandbox.skipCurrentPassage(); // Skips Q1, Q2 and advances to Q3
sandbox.E.ans[2] = sandbox.E.s.qs[2].a; // Correct
sandbox.E.conf[2] = "sure";
sandbox.E.ans[3] = sandbox.E.s.qs[3].a; // Correct
sandbox.E.conf[3] = "sure";

// Test gradePracticeExam with skipped passage
console.log('\nTesting gradePracticeExam with skipped passage (score exclusion):');
sandbox.gradePracticeExam();

// Total Qs = 4. Skipped = 2. Scored Total = 2.
// Correct answers in scored = 2.
// Accuracy must be 2 / 2 * 100 = 100%! NOT 2 / 4 (50%)!
const peKey = "drillroom_pe_v1";
const savedPeData = JSON.parse(mockLocalStorage.getItem(peKey));
const examRecord = savedPeData["cars_60_1"];

assert(examRecord !== undefined, 'Exam record saved in peData');
assert(examRecord.scoredTotal === 2, `Scored total is 2 (excluding 2 skipped Qs), got ${examRecord.scoredTotal}`);
assert(examRecord.skippedCount === 2, `Skipped count is 2, got ${examRecord.skippedCount}`);
assert(examRecord.score === 2, `Raw score is 2, got ${examRecord.score}`);
assert(examRecord.pct === 100, `Raw accuracy % is 100% (2/2), got ${examRecord.pct}%`);
assert(examRecord.scaledScore >= 130, `Scaled score reflects 100% accuracy (>= 130), got ${examRecord.scaledScore}`);

// Verify reviewData inside peRecord
const revData = examRecord.lastReview;
assert(revData.scoredTotal === 2, `reviewData.scoredTotal is 2, got ${revData.scoredTotal}`);
assert(revData.skippedCount === 2, `reviewData.skippedCount is 2, got ${revData.skippedCount}`);
assert(revData.pct === 100, `reviewData.pct is 100%, got ${revData.pct}%`);
assert(revData.qs[0].isSkipped === true, 'reviewData.qs[0].isSkipped is true');
assert(revData.qs[1].isSkipped === true, 'reviewData.qs[1].isSkipped is true');
assert(revData.qs[2].isSkipped === false, 'reviewData.qs[2].isSkipped is false');

// Verify review filter bar in renderReviewQuestionList
console.log('\nTesting renderReviewQuestionList filter bar:');
sandbox.renderReviewQuestionList(revData.qs, "CARS");
const filterBar = elements['zListFilterBar'];
assert(filterBar !== undefined, 'Filter bar rendered');
const filterBarHtml = filterBar.innerHTML;
assert(filterBarHtml.includes('data-f-val="skipped"'), 'Filter bar contains "↷ Skipped" outcome filter button');
assert(filterBarHtml.includes('Missed <span class="pe-filter-count">0</span>'), 'Missed count is 0 (skipped questions NOT counted as missed)');
assert(filterBarHtml.includes('Correct <span class="pe-filter-count">2</span>'), 'Correct count is 2');

// 3. Test Gemini Analysis exclusion of skipped questions
console.log('\n3. Testing Gemini AI analysis exclusion of skipped questions:');
const geminiCode = fs.readFileSync(path.join(__dirname, '../gemini_analysis.js'), 'utf8');
vm.runInContext(geminiCode, sandbox);

// Set up review info for buildAnalysisPrompt
const mockInfo = {
  examId: "cars_60_1",
  title: "CARS Section 1",
  sec: "CARS",
  duration: 60,
  score: 130,
  rawScore: 2,
  total: 4,
  pct: 100,
  percentile: "98th",
  solid: 2,
  lucky: 0,
  shaky: 0,
  timeUsed: 1200,
  qs: revData.qs,
  userAnswers: revData.qs.map(q => q.ans),
  confidences: revData.qs.map(q => q.conf),
  qTimes: [10, 10, 60, 60],
  passageStats: {},
  answerChangeAudit: { totalChanges: 0, rightToWrong: 0, wrongToRight: 0 },
  archetypeStats: [],
  timeSinkQuestions: []
};

// Check that skipped questions are excluded from review items in prompt
let promptBuilt = "";
if (typeof sandbox.buildDiagnosticPrompt === 'function') {
  promptBuilt = sandbox.buildDiagnosticPrompt(mockInfo);
  assert(!promptBuilt.includes('Question 1'), 'Question 1 (skipped) is excluded from AI error review items');
  assert(!promptBuilt.includes('Question 2'), 'Question 2 (skipped) is excluded from AI error review items');
}

// Test extractCurrentExamInfo with skipped questions
if (typeof sandbox.extractCurrentExamInfo === 'function') {
  const currentInfo = sandbox.extractCurrentExamInfo();
  assert(currentInfo !== null, 'extractCurrentExamInfo extracted current exam info');
  assert(currentInfo.wrong === 0, `AI analysis wrong count is 0 (excluding skipped questions), got ${currentInfo.wrong}`);
  assert(currentInfo.pct === 100, `AI analysis accuracy % is 100%, got ${currentInfo.pct}%`);
}

console.log('\n=== SUMMARY ===');
console.log(`Passed: ${testsPassed}`);
console.log(`Failed: ${testsFailed}`);

if (testsFailed > 0) {
  process.exit(1);
} else {
  console.log('\nAll tests passed successfully! Real-MCAT bottom bar with popover & skip passage verified.');
}
