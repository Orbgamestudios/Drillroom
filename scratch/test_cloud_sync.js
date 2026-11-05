/**
 * scratch/test_cloud_sync.js
 * Verification of Cloud Sync & User Account System (Username + 4-Digit PIN)
 * for multi-computer persistence.
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

console.log('=== TEST SUITE: Cloud Sync & Account System (Username + 4-Digit PIN) ===\n');

// Mock browser DOM environment
const elements = {};
function createMockElement(id = '') {
  return {
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
    querySelector() { return null; },
    querySelectorAll() { return []; },
    addEventListener() {},
    setAttribute() {},
    getAttribute() { return null; }
  };
}

function $(id) {
  if (!elements[id]) elements[id] = createMockElement(id);
  return elements[id];
}

let mockStorage = {};
const mockWorkerStore = new Map();

// Mock fetch that routes to our Worker logic
const ctx = {
  window: { addEventListener: () => {} },
  document: {
    getElementById: $,
    addEventListener() {},
    createElement: (tag) => createMockElement(tag),
    body: createMockElement('body'),
    head: createMockElement('head'),
    querySelectorAll: () => []
  },
  localStorage: {
    getItem: (k) => mockStorage[k] || null,
    setItem: (k, v) => { mockStorage[k] = String(v); },
    removeItem: (k) => { delete mockStorage[k]; },
    clear: () => { mockStorage = {}; }
  },
  fetch: null, // assigned below to worker
  $: $,
  console: console,
  setTimeout: (fn, ms) => setTimeout(fn, ms),
  clearTimeout: (id) => clearTimeout(id),
  confirm: () => true,
  alert: () => {}
};
ctx.global = ctx;
ctx.globalThis = ctx;
ctx.window = ctx;
vm.createContext(ctx);

(async () => {
  // Load Worker module
  const workerModule = await import('../worker/index.js');
  const worker = workerModule.default;

  // Route fetch directly to Worker
  ctx.fetch = async (url, opts = {}) => {
    const parsed = new URL(url);
    const req = new Request('http://localhost' + parsed.pathname, opts);
    return await worker.fetch(req, {});
  };

  // Run cloud_sync.js in sandbox
  const syncCode = fs.readFileSync(path.join(__dirname, '../cloud_sync.js'), 'utf8');
  vm.runInContext(syncCode, ctx);

  console.log('1. Verifying DrillRoomCloud API exposure:');
  assert(typeof ctx.DrillRoomCloud === 'object', 'DrillRoomCloud object is globally exposed');
  assert(typeof ctx.DrillRoomCloud.registerAccount === 'function', 'registerAccount function exists');
  assert(typeof ctx.DrillRoomCloud.loginAccount === 'function', 'loginAccount function exists');
  assert(typeof ctx.DrillRoomCloud.syncProgress === 'function', 'syncProgress function exists');
  assert(typeof ctx.DrillRoomCloud.showCloudSyncModal === 'function', 'showCloudSyncModal function exists');

  console.log('\n2. Testing Account Registration:');
  const regBadUser = await ctx.DrillRoomCloud.registerAccount('a', '1234');
  assert(!regBadUser.ok, 'Rejects username shorter than 3 characters');

  const regBadPin = await ctx.DrillRoomCloud.registerAccount('mcat_student', '123');
  assert(!regBadPin.ok, 'Rejects PIN that is not exactly 4 digits');

  const regBadPinAlpha = await ctx.DrillRoomCloud.registerAccount('mcat_student', 'abcd');
  assert(!regBadPinAlpha.ok, 'Rejects PIN with non-digit characters');

  const regSuccess = await ctx.DrillRoomCloud.registerAccount('mcat_student', '5678');
  assert(regSuccess.ok, `Registration successful for mcat_student (${regSuccess.message})`);

  const session = ctx.DrillRoomCloud.getSession();
  assert(session.username === 'mcat_student', 'Session username is mcat_student');
  assert(session.token && session.token.startsWith('mcat_student.'), 'Session token is created and prefixed with username');

  console.log('\n3. Testing Multi-Computer Sync Flow:');
  // Machine A: User completes CARS 90m Passage 1 and 2
  mockStorage['drillroom_pe_v1'] = JSON.stringify({
    completedPassageFingerprints: ['p:cars90_p1', 'p:cars90_p2'],
    cars90: { done: false, completedSets: [0, 1], score: 12, scaledScore: 124 }
  });
  mockStorage['drillroom_history_v1'] = JSON.stringify([
    { id: 'attempt_machine_A', examId: 'cars90_h1', scaledScore: 124, ts: 1000 }
  ]);

  const syncMachineA = await ctx.DrillRoomCloud.syncProgress(true);
  assert(syncMachineA.ok, 'Machine A synced progress to cloud successfully');

  // Now simulate Machine B (new browser / different computer):
  // User on Machine B clears local storage (new computer with nothing done yet)
  mockStorage = {};
  assert(!ctx.DrillRoomCloud.getSession().username, 'Machine B starts completely clean and logged out');

  // User on Machine B logs in with username and PIN
  const loginMachineB = await ctx.DrillRoomCloud.loginAccount('mcat_student', '5678');
  assert(loginMachineB.ok, 'Machine B logged in with username and 4-digit PIN');

  // Verify Machine B received Machine A progress immediately on login
  const peDataB = JSON.parse(mockStorage['drillroom_pe_v1'] || '{}');
  const historyB = JSON.parse(mockStorage['drillroom_history_v1'] || '[]');

  assert(peDataB.completedPassageFingerprints?.includes('p:cars90_p1'), 'Machine B received Passage 1 completion');
  assert(peDataB.completedPassageFingerprints?.includes('p:cars90_p2'), 'Machine B received Passage 2 completion');
  assert(peDataB.cars90?.completedSets?.length === 2, 'Machine B has completedSets [0, 1]');
  assert(historyB.some(h => h.id === 'attempt_machine_A'), 'Machine B received history attempt from Machine A');

  // Now Machine B completes Passage 3 on their computer
  peDataB.completedPassageFingerprints.push('p:cars90_p3');
  peDataB.cars90.completedSets.push(2);
  peDataB.cars90.score = 18;
  peDataB.cars90.scaledScore = 127;
  mockStorage['drillroom_pe_v1'] = JSON.stringify(peDataB);

  historyB.push({ id: 'attempt_machine_B', examId: 'cars90_h2', scaledScore: 127, ts: 2000 });
  mockStorage['drillroom_history_v1'] = JSON.stringify(historyB);

  // Machine B syncs to cloud
  const syncMachineB = await ctx.DrillRoomCloud.syncProgress(true);
  assert(syncMachineB.ok, 'Machine B synced newly completed passage to cloud');

  // Now back to Machine A: User clicks "Sync Now"
  // Setup Machine A state back
  mockStorage = {
    'drillroom_sync_username': 'mcat_student',
    'drillroom_sync_token': session.token,
    'drillroom_pe_v1': JSON.stringify({
      completedPassageFingerprints: ['p:cars90_p1', 'p:cars90_p2'],
      cars90: { done: false, completedSets: [0, 1], score: 12, scaledScore: 124 }
    }),
    'drillroom_history_v1': JSON.stringify([
      { id: 'attempt_machine_A', examId: 'cars90_h1', scaledScore: 124, ts: 1000 }
    ])
  };

  const syncBackToA = await ctx.DrillRoomCloud.syncProgress(true);
  assert(syncBackToA.ok, 'Machine A pulled down updates from Machine B');

  const peDataFinalA = JSON.parse(mockStorage['drillroom_pe_v1'] || '{}');
  const historyFinalA = JSON.parse(mockStorage['drillroom_history_v1'] || '[]');

  assert(peDataFinalA.completedPassageFingerprints?.length === 3, `Machine A has all 3 passages completed (got ${peDataFinalA.completedPassageFingerprints?.length})`);
  assert(peDataFinalA.cars90?.completedSets?.length === 3, 'Machine A has sets 0, 1, and 2 completed');
  assert(peDataFinalA.cars90?.scaledScore === 127, 'Machine A updated to higher scaled score 127');
  assert(historyFinalA.length === 2, 'Machine A history has attempts from both Machine A and Machine B');

  console.log('\n4. Testing Modal Rendering:');
  ctx.DrillRoomCloud.showCloudSyncModal();
  const modal = elements['cloudSyncModal'];
  assert(modal && !modal.classList.contains('hide'), 'Cloud Sync modal rendered and visible');

  console.log(`\n==================================================`);
  console.log(`TEST RESULTS: ${testsPassed} passed, ${testsFailed} failed`);
  console.log(`==================================================`);

  if (testsFailed > 0) {
    process.exit(1);
  }
})().catch(err => {
  console.error('Test execution failed:', err);
  process.exit(1);
});
