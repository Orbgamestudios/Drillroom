// Test duplicate prevention and deletion bug fix
const fs = require('fs');

const storage = {};
global.localStorage = {
  getItem: (k) => storage[k] !== undefined ? storage[k] : null,
  setItem: (k, v) => { storage[k] = String(v); },
  removeItem: (k) => { delete storage[k]; }
};

global.$ = (id) => ({
  id,
  classList: { add: ()=>{}, remove: ()=>{}, toggle: ()=>{} },
  onclick: null,
  querySelector: () => ({ onclick: null }),
  querySelectorAll: () => []
});
global.document = {
  getElementById: (id) => global.$(id),
  createElement: () => global.$('el'),
  querySelectorAll: () => []
};
global.window = {};
global.confirm = () => true;
global.flash = (m) => console.log('FLASH:', m);

// Load the updated logic
const HIST_KEY = "drillroom_history_v1";
const MIGRATED_FLAG_KEY = "drillroom_hist_migrated_v2";

function deduplicateHistory(hist) {
  if (!Array.isArray(hist) || hist.length <= 1) return hist || [];
  const cleaned = [];
  for (const item of hist) {
    if (!item || !item.id) continue;
    const isDup = cleaned.some(c => {
      if (c.id === item.id) return true;
      const oneIsMigrated = (c.id.startsWith("att_migrated_") || item.id.startsWith("att_migrated_"));
      if (oneIsMigrated && c.examId === item.examId && c.rawScore === item.rawScore && c.totalQs === item.totalQs && c.scaledScore === item.scaledScore) {
        return true;
      }
      if (c.examId === item.examId && c.rawScore === item.rawScore && c.totalQs === item.totalQs && c.scaledScore === item.scaledScore && Math.abs((c.ts || 0) - (item.ts || 0)) < 30000) {
        return true;
      }
      return false;
    });
    if (!isDup) cleaned.push(item);
  }
  return cleaned;
}

function getHistory() {
  let hist = [];
  try { hist = JSON.parse(localStorage.getItem(HIST_KEY)) || []; } catch(e) { hist = []; }
  if (!Array.isArray(hist)) hist = [];

  const alreadyMigrated = localStorage.getItem(MIGRATED_FLAG_KEY) === "1";
  if (!alreadyMigrated) {
    localStorage.setItem(MIGRATED_FLAG_KEY, "1");
    if (hist.length === 0) {
      try {
        const peData = JSON.parse(localStorage.getItem("drillroom_pe_v1")) || {};
        const migrated = [];
        for (const [id, r] of Object.entries(peData)) {
          if (r && r.done) {
            migrated.push({
              id: "att_migrated_" + id,
              examId: id,
              sec: "CARS",
              duration: 90,
              type: "90min",
              suiteTitle: "Full 90-Minute Practice Exam 1",
              scaledScore: r.scaledScore || 118,
              rawScore: r.score || 0,
              totalQs: r.total || 0,
              pct: r.pct || 0,
              percentile: r.percentile || "1st",
              solid: r.solid || 0, lucky: r.lucky || 0, shaky: r.shaky || 0,
              timeUsed: r.timeUsed || 0,
              ts: r.ts || (Date.now() - 3600000),
              includedInAverage: true
            });
          }
        }
        if (migrated.length) {
          migrated.sort((a,b) => b.ts - a.ts);
          hist = migrated;
          saveHistory(hist);
        }
      } catch(e) {}
    }
  }

  const deduped = deduplicateHistory(hist);
  if (deduped.length !== hist.length) {
    hist = deduped;
    saveHistory(hist);
  }
  return hist;
}

function saveHistory(hist) {
  try { localStorage.setItem(HIST_KEY, JSON.stringify(hist)); } catch(e) {}
}

function deleteHistoryEntry(id) {
  if (!id) return;
  let hist = getHistory();
  const deletedEntry = hist.find(x => x.id === id);
  hist = hist.filter(x => x.id !== id);
  saveHistory(hist);

  if (deletedEntry && deletedEntry.examId) {
    try {
      const peData = JSON.parse(localStorage.getItem("drillroom_pe_v1")) || {};
      const remaining = hist.filter(x => x.examId === deletedEntry.examId);
      if (remaining.length === 0) {
        delete peData[deletedEntry.examId];
      }
      localStorage.setItem("drillroom_pe_v1", JSON.stringify(peData));
    } catch(e) {}
  }
}

// SCENARIO 1: Simulate the exact bug the user experienced
console.log('--- SCENARIO 1: User has duplicate copies in storage ---');
// In peData:
storage["drillroom_pe_v1"] = JSON.stringify({
  cars90: { done: true, score: 45, total: 53, scaledScore: 129, pct: 85, ts: 1000 }
});
// In history: user had both copies
storage[HIST_KEY] = JSON.stringify([
  { id: "att_migrated_cars90", examId: "cars90", rawScore: 45, totalQs: 53, scaledScore: 129, ts: 1000, includedInAverage: true },
  { id: "att_1729600000_123", examId: "cars90", rawScore: 45, totalQs: 53, scaledScore: 129, ts: 1005, includedInAverage: true }
]);

console.log('Raw storage before getHistory:', JSON.parse(storage[HIST_KEY]).length, 'items');
let h = getHistory();
console.log('After getHistory with auto-deduplication:', h.length, 'item (duplicate removed automatically!)');
if (h.length !== 1) throw new Error('Expected 1 item after deduplication, got ' + h.length);

console.log('--- SCENARIO 2: Deleting the remaining entry ---');
console.log('Deleting entry with id:', h[0].id);
deleteHistoryEntry(h[0].id);

h = getHistory();
console.log('History after delete:', h.length, 'items');
if (h.length !== 0) throw new Error('Expected 0 items after delete, but got ' + h.length + ' (it resurrected!)');

const peAfter = JSON.parse(storage["drillroom_pe_v1"]);
console.log('peData after delete:', peAfter);
if (peAfter.cars90 !== undefined) throw new Error('Expected peData.cars90 to be deleted');

console.log('ALL TESTS PASSED! The duplicate was removed and deleting cannot resurrect it.');
