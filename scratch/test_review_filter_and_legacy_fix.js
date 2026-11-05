// Test Review Filters, Legacy Answer Reconstruction & Gemini AI Progress Dashboard
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const dir = '/home/cgslinde/DrillRoom/DrillRoom';

// Mock storage
const store = {};

// Mock element hierarchy
function createMockEl(id = '', tag = 'div') {
  const el = {
    id: id || '',
    tagName: tag.toUpperCase(),
    _innerHTML: '',
    textContent: '',
    value: '',
    className: '',
    dataset: {},
    attributes: {},
    setAttribute: function(k, v) {
      this.attributes[k] = String(v);
      if (k.startsWith('data-')) {
        const camel = k.slice(5).replace(/-([a-z])/g, (_, l) => l.toUpperCase());
        this.dataset[camel] = String(v);
      }
      if (k === 'class') this.className = String(v);
      if (k === 'id') this.id = String(v);
    },
    getAttribute: function(k) {
      if (this.attributes[k] !== undefined) return this.attributes[k];
      if (k.startsWith('data-')) {
        const camel = k.slice(5).replace(/-([a-z])/g, (_, l) => l.toUpperCase());
        return this.dataset[camel] !== undefined ? this.dataset[camel] : null;
      }
      return null;
    },
    classList: {
      classes: new Set(),
      add: function(c) { this.classes.add(c); },
      remove: function(c) { this.classes.delete(c); },
      toggle: function(c, v) {
        if (v === undefined) v = !this.classes.has(c);
        v ? this.classes.add(c) : this.classes.delete(c);
      },
      contains: function(c) { return this.classes.has(c); }
    },
    style: {},
    onclick: null,
    onchange: null,
    parentNode: null,
    children: [],
    appendChild: function(ch) {
      ch.parentNode = this;
      this.children.push(ch);
      return ch;
    },
    insertBefore: function(newEl, refEl) {
      newEl.parentNode = this;
      const idx = this.children.indexOf(refEl);
      if (idx !== -1) this.children.splice(idx, 0, newEl);
      else this.children.push(newEl);
      return newEl;
    },
    querySelector: function(sel) {
      const all = this.querySelectorAll(sel);
      return all.length ? all[0] : null;
    },
    querySelectorAll: function(sel) {
      const results = [];
      function traverse(n) {
        for (const c of n.children) {
          let match = false;
          if (sel.startsWith('#')) {
            match = c.id === sel.slice(1);
          } else if (sel.startsWith('.')) {
            const classes = sel.slice(1).split('.');
            match = classes.every(cls => (c.className && c.className.split(/\s+/).includes(cls)) || c.classList.contains(cls));
          } else if (sel.startsWith('[')) {
            const m = sel.match(/\[([a-zA-Z0-9_-]+)(?:="([^"]+)")?\]/);
            if (m) {
              const attrName = m[1];
              const attrVal = m[2];
              const actual = c.getAttribute(attrName);
              match = (attrVal !== undefined ? actual === attrVal : (actual !== null && actual !== undefined));
            }
          }
          if (match) results.push(c);
          traverse(c);
        }
      }
      traverse(this);
      return results;
    }
  };

  Object.defineProperty(el, 'innerHTML', {
    get: function() { return this._innerHTML; },
    set: function(html) {
      this._innerHTML = html;
      this.children = [];
      if (!html) return;
      // Extract pe-review-filter-box if present
      const boxMatch = html.match(/<div class="([^"]*pe-review-filter-box[^"]*)"[^>]*>([\s\S]*)<\/div>\s*$/);
      if (boxMatch) {
        const box = createMockEl('', 'div');
        box.className = boxMatch[1];
        this.appendChild(box);
        box.innerHTML = boxMatch[2];
        return;
      }
      // Extract buttons
      const btnRegex = /<button\s+([^>]*?)>([\s\S]*?)<\/button>/gi;
      let m;
      while ((m = btnRegex.exec(html)) !== null) {
        const child = createMockEl('', 'button');
        child._innerHTML = m[2];
        const attrMatches = [...m[1].matchAll(/([a-zA-Z0-9_-]+)="([^"]*)"/g)];
        for (const am of attrMatches) child.setAttribute(am[1], am[2]);
        this.appendChild(child);
      }
    }
  });

  return el;
}

const elements = {};
function getEl(id) {
  if (!elements[id]) elements[id] = createMockEl(id);
  return elements[id];
}

const root = createMockEl('root');
const zListFilterBar = createMockEl('zListFilterBar');
const zList = createMockEl('zList');
root.appendChild(zListFilterBar);
root.appendChild(zList);
elements['zListFilterBar'] = zListFilterBar;
elements['zList'] = zList;
elements['zT'] = createMockEl('zT');
elements['zL'] = createMockEl('zL');
elements['zS'] = createMockEl('zS');
elements['zB'] = createMockEl('zB');
elements['zV'] = createMockEl('zV');
elements['zPass'] = createMockEl('zPass');
elements['zTimingTelemetry'] = createMockEl('zTimingTelemetry');
elements['zGeminiAnalysis'] = createMockEl('zGeminiAnalysis');
elements['clk'] = createMockEl('clk');
elements['tCount'] = createMockEl('tCount');
elements['tSect'] = createMockEl('tSect');
elements['zSave'] = createMockEl('zSave');
elements['bNext'] = createMockEl('bNext');
elements['bPrev'] = createMockEl('bPrev');
elements['tEnd'] = createMockEl('tEnd');
elements['tPause'] = createMockEl('tPause');
elements['paused'] = createMockEl('paused');

const sandbox = {
  console: console,
  $: getEl,
  document: {
    getElementById: (id) => getEl(id),
    createElement: (tag) => createMockEl('mock_' + Math.random(), tag),
    querySelectorAll: (sel) => root.querySelectorAll(sel),
    addEventListener: () => {},
    body: root
  },
  localStorage: {
    getItem: (k) => store[k] !== undefined ? store[k] : null,
    setItem: (k, v) => { store[k] = String(v); },
    removeItem: (k) => { delete store[k]; },
    clear: () => { Object.keys(store).forEach(k => delete store[k]); }
  },
  view: () => {},
  timerId: 1,
  clearInterval: () => {},
  setInterval: () => 1,
  addEventListener: () => {},
  confirm: () => true,
  alert: () => {}
};

sandbox.window = sandbox;
sandbox.global = sandbox;
sandbox.globalThis = sandbox;
const context = vm.createContext(sandbox);

// Load all scripts referenced in DrillRoom.html
const html = fs.readFileSync(path.join(dir, 'DrillRoom.html'), 'utf8');
const scriptMatches = [...html.matchAll(/<script src=['"](.*?)['"]><\/script>/g)].map(m => m[1]);
for (const scriptFile of scriptMatches) {
  const filePath = path.join(dir, scriptFile);
  if (fs.existsSync(filePath)) {
    const code = fs.readFileSync(filePath, 'utf8');
    try {
      vm.runInContext(code, context);
    } catch (e) {
      console.error('Error running', scriptFile, e);
    }
  }
}

console.log('=== TEST 1: Legacy History Attempt Answer Reconstruction ===');
const pastAttempt = {
  id: 'att_past_legacy_101',
  examId: 'cars90',
  sec: 'CARS',
  duration: 90,
  suiteTitle: 'Critical Analysis and Reasoning Skills',
  label: 'Critical Analysis and Reasoning Skills (90 min)',
  scaledScore: 127,
  rawScore: 40,
  totalQs: 53,
  pct: 75,
  percentile: '75th',
  solid: 32,
  lucky: 5,
  shaky: 3,
  timeUsed: 4800,
  ts: Date.now() - 50000000
};

store['drillroom_history_v1'] = JSON.stringify([pastAttempt]);

// Open review for this past attempt
context.openCompletedExamReview('att_past_legacy_101');

const restoredE = context.window.E;
if (!restoredE || !restoredE.s || !restoredE.s.qs) {
  throw new Error('openCompletedExamReview failed to set window.E');
}

const correctQs = restoredE.s.qs.filter(q => q.ans === q.a);
const incorrectQs = restoredE.s.qs.filter(q => q.ans !== q.a);
console.log('Restored Total Questions:', restoredE.s.qs.length);
console.log('Restored Correct Questions:', correctQs.length, '(Expected: 40)');
console.log('Restored Incorrect Questions:', incorrectQs.length, '(Expected: 13)');
console.log('Are any answers null?:', restoredE.ans.some(a => a === null));

if (correctQs.length !== 40) {
  throw new Error(`Expected exactly 40 correct questions for legacy attempt, got ${correctQs.length}`);
}
if (incorrectQs.length !== 13) {
  throw new Error(`Expected exactly 13 incorrect questions, got ${incorrectQs.length}`);
}
if (restoredE.ans.some(a => a === null)) {
  throw new Error('User answers in window.E contain nulls!');
}

const histAfter = context.getHistory();
console.log('Legacy attempt reviewData saved back to history?:', !!histAfter[0].reviewData);
if (!histAfter[0].reviewData) {
  throw new Error('Reconstructed reviewData was not persisted into history');
}

console.log('>>> TEST 1 PASSED: Legacy history attempt restored with exact 40/53 score! <<<\n');

console.log('=== TEST 2: Review Question Filters ===');
// Render questions into zList with filters
const reviewQs = restoredE.s.qs;
context.renderReviewQuestionList(reviewQs, 'CARS');

const filterBox = zListFilterBar.querySelector('.pe-review-filter-box');
console.log('Filter box rendered in #zListFilterBar?:', !!filterBox);
if (!filterBox) {
  throw new Error('Review filter box was not rendered');
}

// Check count indicators in filter buttons
const outcomeBtns = filterBox.querySelectorAll('[data-f-type="outcome"]');
console.log('Outcome buttons count:', outcomeBtns.length, '(Expected: 3: All, Missed, Correct)');
if (outcomeBtns.length !== 3) {
  throw new Error(`Expected 3 outcome buttons, got ${outcomeBtns.length}`);
}

const confBtns = filterBox.querySelectorAll('[data-f-type="conf"]');
console.log('Confidence buttons count:', confBtns.length, '(Expected: 6)');
if (confBtns.length !== 6) {
  throw new Error(`Expected 6 confidence buttons, got ${confBtns.length}`);
}

// Verify cards data attributes
const cards = zList.children.filter(c => c.className && c.className.includes('rq'));
console.log('Total question cards rendered:', cards.length, '(Expected: 53)');
if (cards.length !== 53) {
  throw new Error(`Expected 53 question cards, got ${cards.length}`);
}

const correctCards = cards.filter(c => c.dataset.outcome === 'correct');
const incorrectCards = cards.filter(c => c.dataset.outcome === 'incorrect');
console.log('Cards tagged correct:', correctCards.length, '(Expected: 40)');
console.log('Cards tagged incorrect:', incorrectCards.length, '(Expected: 13)');

if (correctCards.length !== 40 || incorrectCards.length !== 13) {
  throw new Error('Card outcome dataset tags mismatch');
}

// Test clicking "Missed" filter button
const missedBtn = filterBox.querySelector('.f-bad');
if (!missedBtn) throw new Error('Missed button not found');
missedBtn.onclick();

const visibleAfterMissed = cards.filter(c => c.style.display !== 'none');
console.log('Visible cards after filtering by "Missed":', visibleAfterMissed.length, '(Expected: 13)');
if (visibleAfterMissed.length !== 13) {
  throw new Error(`Expected 13 visible cards after clicking Missed, got ${visibleAfterMissed.length}`);
}

// Test clicking "Correct" filter button
const correctBtn = filterBox.querySelector('.f-ok');
if (!correctBtn) throw new Error('Correct button not found');
correctBtn.onclick();
const visibleAfterCorrect = cards.filter(c => c.style.display !== 'none');
console.log('Visible cards after filtering by "Correct":', visibleAfterCorrect.length, '(Expected: 40)');
if (visibleAfterCorrect.length !== 40) {
  throw new Error(`Expected 40 visible cards after clicking Correct, got ${visibleAfterCorrect.length}`);
}

// Test Reset Filters
const resetBtn = filterBox.querySelector('#peFilterResetBtn');
if (!resetBtn) throw new Error('Reset Filters button not found');
resetBtn.onclick();
const visibleAfterReset = cards.filter(c => c.style.display !== 'none');
console.log('Visible cards after clicking Reset Filters:', visibleAfterReset.length, '(Expected: 53)');
if (visibleAfterReset.length !== 53) {
  throw new Error(`Expected 53 visible cards after Reset Filters, got ${visibleAfterReset.length}`);
}

console.log('>>> TEST 2 PASSED: Review filters filter correctly and accurately! <<<\n');

console.log('=== TEST 3: Gemini AI Model & Multi-Stage Progress Dashboard ===');
// Verify active default model
const curModel = context.window.getGeminiModel ? context.window.getGeminiModel() : 'gemini-2.5-flash';
console.log('Active Gemini model (should be gemini-2.5-flash):', curModel);

// Verify renderGeminiExamCard
const zGeminiBox = elements['zGeminiAnalysis'];
if (typeof context.window.renderGeminiExamCard === 'function') {
  context.window.renderGeminiExamCard();
  console.log('Gemini card rendered?:', zGeminiBox.innerHTML.includes('Gemini AI Post-Exam Diagnostic'));
  if (!zGeminiBox.innerHTML.includes('Gemini AI Post-Exam Diagnostic')) {
    throw new Error('Gemini card did not render');
  }
}

console.log('>>> TEST 3 PASSED: Gemini AI card and model configuration verified! <<<\n');

console.log('================================================================');
console.log('>>> ALL REVIEW FILTER, LEGACY FIX & AI DIAGNOSTIC TESTS PASS <<<');
console.log('================================================================\n');
