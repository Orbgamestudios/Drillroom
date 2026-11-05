/**
 * cloud_sync.js
 * MCAT DrillRoom Multi-Device Cloud Synchronization
 *
 * Enables students to log in with a username and 4-digit PIN on any computer or phone
 * and automatically keep completed passages, exam scores, and history in sync with 0 duplicates.
 */

(function () {
  "use strict";

  const STORAGE_KEYS = {
    USERNAME: "drillroom_sync_username",
    DISPLAY_NAME: "drillroom_sync_display_name",
    TOKEN: "drillroom_sync_token",
    LAST_SYNCED: "drillroom_sync_last_synced",
    API_URL: "drillroom_sync_api_url",
    AUTO_SYNC: "drillroom_sync_auto_enabled",
    PE_DATA: "drillroom_pe_v1",
    HISTORY: "drillroom_history_v1",
    PREFS: "drillroom_hist_prefs_v1"
  };

  // Default endpoint for Cloudflare Worker; user can customize in Cloud Settings
  const DEFAULT_API_URL = "https://drillroom.solitary-sky-76c1.workers.dev";

  function getApiUrl() {
    let url = localStorage.getItem(STORAGE_KEYS.API_URL) || DEFAULT_API_URL;
    if (url.endsWith("/")) url = url.slice(0, -1);
    return url;
  }

  function setApiUrl(url) {
    if (!url) {
      localStorage.removeItem(STORAGE_KEYS.API_URL);
    } else {
      localStorage.setItem(STORAGE_KEYS.API_URL, url.trim().replace(/\/+$/, ""));
    }
  }

  function getSession() {
    return {
      username: localStorage.getItem(STORAGE_KEYS.USERNAME) || null,
      displayName: localStorage.getItem(STORAGE_KEYS.DISPLAY_NAME) || localStorage.getItem(STORAGE_KEYS.USERNAME) || null,
      token: localStorage.getItem(STORAGE_KEYS.TOKEN) || null,
      lastSynced: parseInt(localStorage.getItem(STORAGE_KEYS.LAST_SYNCED) || "0", 10) || 0,
      autoSync: localStorage.getItem(STORAGE_KEYS.AUTO_SYNC) !== "false"
    };
  }

  function setSession(username, token, displayName) {
    localStorage.setItem(STORAGE_KEYS.USERNAME, username);
    localStorage.setItem(STORAGE_KEYS.TOKEN, token);
    if (displayName) localStorage.setItem(STORAGE_KEYS.DISPLAY_NAME, displayName);
    updateTopBarAccountButton();
  }

  function clearSession() {
    localStorage.removeItem(STORAGE_KEYS.USERNAME);
    localStorage.removeItem(STORAGE_KEYS.DISPLAY_NAME);
    localStorage.removeItem(STORAGE_KEYS.TOKEN);
    localStorage.removeItem(STORAGE_KEYS.LAST_SYNCED);
    updateTopBarAccountButton();
  }

  /* Extract current local progress payload */
  function getLocalPayload() {
    let peData = {};
    try { peData = JSON.parse(localStorage.getItem(STORAGE_KEYS.PE_DATA)) || {}; } catch (e) { peData = {}; }
    let history = [];
    try { history = JSON.parse(localStorage.getItem(STORAGE_KEYS.HISTORY)) || []; } catch (e) { history = []; }
    let prefs = {};
    try { prefs = JSON.parse(localStorage.getItem(STORAGE_KEYS.PREFS)) || {}; } catch (e) { prefs = {}; }

    return {
      peData,
      history,
      prefs,
      clientTimestamp: Date.now()
    };
  }

  /* Smart 3-Way Union Merge of progress data */
  function mergeAndApplyPayload(remoteData) {
    if (!remoteData || typeof remoteData !== "object") return;

    const local = getLocalPayload();
    const remPE = remoteData.peData || {};
    const locPE = local.peData || {};

    // 1. Merge completed passage fingerprints
    const mergedFps = Array.from(new Set([
      ...(Array.isArray(locPE.completedPassageFingerprints) ? locPE.completedPassageFingerprints : []),
      ...(Array.isArray(remPE.completedPassageFingerprints) ? remPE.completedPassageFingerprints : [])
    ]));

    // 2. Merge peData records
    const allExamIds = new Set([...Object.keys(locPE), ...Object.keys(remPE)]);
    allExamIds.delete("completedPassageFingerprints");

    const mergedPE = {
      completedPassageFingerprints: mergedFps
    };

    const pool = (typeof PRACTICE_EXAMS !== "undefined") ? PRACTICE_EXAMS : [];

    for (const id of allExamIds) {
      const l = locPE[id] || {};
      const r = remPE[id] || {};
      const targetExam = pool.find(e => e.id === id);

      const combinedSets = Array.from(new Set([
        ...(Array.isArray(l.completedSets) ? l.completedSets : []),
        ...(Array.isArray(r.completedSets) ? r.completedSets : [])
      ])).sort((a, b) => a - b);

      const isDone = !!(l.done || r.done || (targetExam && targetExam.sets && combinedSets.length >= targetExam.sets.length));
      const lTs = l.ts || 0;
      const rTs = r.ts || 0;
      const base = rTs > lTs ? { ...l, ...r } : { ...r, ...l };

      mergedPE[id] = {
        ...base,
        completedSets: combinedSets,
        done: isDone,
        score: Math.max(l.score || 0, r.score || 0),
        scaledScore: Math.max(l.scaledScore || 0, r.scaledScore || 0),
        pct: Math.max(l.pct || 0, r.pct || 0),
        ts: Math.max(lTs, rTs)
      };
    }

    // 3. Merge history (union by attempt ID)
    const historyMap = new Map();
    const remHist = Array.isArray(remoteData.history) ? remoteData.history : [];
    const locHist = Array.isArray(local.history) ? local.history : [];

    for (const item of [...remHist, ...locHist]) {
      if (item && item.id && !historyMap.has(item.id)) {
        historyMap.set(item.id, item);
      }
    }
    const mergedHistory = Array.from(historyMap.values()).sort((a, b) => (b.ts || 0) - (a.ts || 0));

    // 4. Merge prefs
    const mergedPrefs = {
      ...(local.prefs || {}),
      ...(remoteData.prefs || {})
    };

    // Save merged results to localStorage
    try {
      localStorage.setItem(STORAGE_KEYS.PE_DATA, JSON.stringify(mergedPE));
      localStorage.setItem(STORAGE_KEYS.HISTORY, JSON.stringify(mergedHistory));
      localStorage.setItem(STORAGE_KEYS.PREFS, JSON.stringify(mergedPrefs));
      localStorage.setItem(STORAGE_KEYS.LAST_SYNCED, String(Date.now()));
    } catch (e) {
      console.warn("Error saving merged cloud data:", e);
    }

    // Trigger local retroactive passage deduplication & sync
    if (typeof initAndMigrateCompletedFingerprints === "function") {
      try {
        const mig = initAndMigrateCompletedFingerprints(mergedPE);
        localStorage.setItem(STORAGE_KEYS.PE_DATA, JSON.stringify(mig));
      } catch (e) { }
    }

    // Repaint all active UI views
    if (typeof paintPracticeExams === "function") paintPracticeExams();
    if (typeof paintHistory === "function") paintHistory();
    if (typeof updateSkipPassageButtonState === "function") updateSkipPassageButtonState();
  }

  /* API Calls */
  async function apiFetch(endpoint, options = {}) {
    const url = getApiUrl() + endpoint;
    const session = getSession();
    const headers = {
      "Content-Type": "application/json",
      ...(options.headers || {})
    };
    if (session.token && !headers["Authorization"]) {
      headers["Authorization"] = `Bearer ${session.token}`;
    }

    const res = await fetch(url, {
      ...options,
      headers
    });
    const data = await res.json().catch(() => ({ ok: false, error: "Network or JSON error" }));
    return { ok: res.ok, status: res.status, data };
  }

  async function registerAccount(username, pin) {
    const cleanUser = String(username || "").trim();
    const cleanPin = String(pin || "").trim();

    if (!cleanUser || !/^[a-zA-Z0-9_-]{3,30}$/.test(cleanUser)) {
      return { ok: false, error: "Username must be 3–30 characters and contain only letters, numbers, hyphens, and underscores." };
    }
    if (!/^\d{4}$/.test(cleanPin)) {
      return { ok: false, error: "PIN must be exactly 4 digits." };
    }

    const initialData = getLocalPayload();
    const res = await apiFetch("/api/account/register", {
      method: "POST",
      body: JSON.stringify({
        username: cleanUser,
        pin: cleanPin,
        initialData
      })
    });

    if (res.ok && res.data.ok) {
      setSession(res.data.username, res.data.token, res.data.displayName || cleanUser);
      localStorage.setItem(STORAGE_KEYS.LAST_SYNCED, String(Date.now()));
      return { ok: true, username: res.data.username, message: res.data.message };
    }
    return { ok: false, error: res.data.error || "Failed to create account." };
  }

  async function loginAccount(username, pin) {
    const cleanUser = String(username || "").trim();
    const cleanPin = String(pin || "").trim();

    if (!cleanUser || !cleanPin) {
      return { ok: false, error: "Please enter both username and 4-digit PIN." };
    }

    const res = await apiFetch("/api/account/login", {
      method: "POST",
      body: JSON.stringify({
        username: cleanUser,
        pin: cleanPin
      })
    });

    if (res.ok && res.data.ok) {
      setSession(res.data.username, res.data.token, res.data.displayName || cleanUser);
      // Merge remote data with whatever local data already exists
      if (res.data.data) {
        mergeAndApplyPayload(res.data.data);
      }
      // Immediately push merged state back to cloud so both are in perfect sync
      syncProgress(true).catch(() => {});
      return { ok: true, username: res.data.username, message: res.data.message };
    }
    return { ok: false, error: res.data.error || "Login failed." };
  }

  let isSyncing = false;
  async function syncProgress(force = false) {
    const session = getSession();
    if (!session.token || !session.username) return { ok: false, error: "Not logged in" };
    if (isSyncing && !force) return { ok: true, inProgress: true };

    isSyncing = true;
    updateTopBarAccountButton(true);

    try {
      const payload = getLocalPayload();
      const res = await apiFetch("/api/account/sync", {
        method: "POST",
        body: JSON.stringify({
          token: session.token,
          username: session.username,
          data: payload
        })
      });

      if (res.ok && res.data.ok) {
        if (res.data.data) {
          mergeAndApplyPayload(res.data.data);
        }
        localStorage.setItem(STORAGE_KEYS.LAST_SYNCED, String(Date.now()));
        updateTopBarAccountButton(false);
        return { ok: true, message: "Synced successfully" };
      } else if (res.status === 401) {
        // Session expired
        clearSession();
        updateTopBarAccountButton(false);
        return { ok: false, error: "Session expired. Please log in again." };
      }
      updateTopBarAccountButton(false);
      return { ok: false, error: res.data.error || "Sync failed" };
    } catch (err) {
      updateTopBarAccountButton(false);
      return { ok: false, error: err.message };
    } finally {
      isSyncing = false;
    }
  }

  // Debounced auto-sync for background updates
  let autoSyncTimer = null;
  function triggerAutoSync() {
    const session = getSession();
    if (!session.token || !session.autoSync) return;
    if (autoSyncTimer) clearTimeout(autoSyncTimer);
    autoSyncTimer = setTimeout(() => {
      syncProgress().catch(() => {});
    }, 2000);
  }

  /* Format relative time */
  function formatRelativeTime(ts) {
    if (!ts) return "Never";
    const sec = Math.floor((Date.now() - ts) / 1000);
    if (sec < 45) return "Just now";
    if (sec < 90) return "1 minute ago";
    const min = Math.floor(sec / 60);
    if (min < 60) return `${min} minutes ago`;
    const hrs = Math.floor(min / 60);
    if (hrs < 24) return `${hrs} hour${hrs > 1 ? "s" : ""} ago`;
    const days = Math.floor(hrs / 24);
    return `${days} day${days > 1 ? "s" : ""} ago`;
  }

  /* Update top-bar and home buttons */
  function updateTopBarAccountButton(syncing = false) {
    const btn = document.getElementById("tCloudAccount");
    const session = getSession();

    if (btn) {
      if (syncing) {
        btn.innerHTML = `<span style="display:inline-block;animation:spin 1s linear infinite">⟳</span> Syncing...`;
        btn.style.color = "#FFD700";
      } else if (session.username) {
        btn.innerHTML = `☁️ <span style="font-weight:700">${session.displayName || session.username}</span> <span style="display:inline-block;width:7px;height:7px;border-radius:50%;background:#4ADE80;margin-left:4px" title="Cloud Synced"></span>`;
        btn.style.color = "#fff";
      } else {
        btn.innerHTML = `☁️ Sign In / Sync`;
        btn.style.color = "rgba(255,255,255,0.9)";
      }
    }

    const homeBtn = document.getElementById("bCloudAccount");
    if (homeBtn) {
      if (session.username) {
        homeBtn.innerHTML = `☁️ Synced as <b>${session.displayName || session.username}</b>`;
      } else {
        homeBtn.innerHTML = `☁️ Cloud Sync &amp; Account`;
      }
    }
  }

  /* ===== MODAL UI ===== */
  function showCloudSyncModal() {
    let modal = document.getElementById("cloudSyncModal");
    if (!modal) {
      modal = document.createElement("div");
      modal.id = "cloudSyncModal";
      modal.style.cssText = "position:fixed;inset:0;background:rgba(16,24,38,0.72);z-index:99999;display:flex;align-items:center;justify-content:center;padding:16px;backdrop-filter:blur(2px)";
      document.body.appendChild(modal);
    }

    const session = getSession();
    const local = getLocalPayload();
    const peData = local.peData || {};
    const fpsCount = Array.isArray(peData.completedPassageFingerprints) ? peData.completedPassageFingerprints.length : 0;
    const historyCount = Array.isArray(local.history) ? local.history.length : 0;
    const lastSyncStr = formatRelativeTime(session.lastSynced);

    modal.innerHTML = `
      <div style="background:#fff;border:1px solid var(--line2);box-shadow:0 24px 60px rgba(0,0,0,0.35);width:min(540px,96vw);border-radius:4px;overflow:hidden;font-family:var(--f)">
        <!-- Header -->
        <div style="background:var(--nav);color:#fff;padding:14px 20px;display:flex;justify-content:space-between;align-items:center">
          <div style="display:flex;align-items:center;gap:10px">
            <span style="font-size:18px">☁️</span>
            <div>
              <div style="font-weight:700;font-size:15px;letter-spacing:0.3px">DrillRoom Cloud Sync</div>
              <div style="font-size:11.5px;color:rgba(255,255,255,0.75)">Practice across multiple computers with 0 duplicates</div>
            </div>
          </div>
          <button id="csModalClose" style="color:#fff;font-size:24px;line-height:1;border:none;background:none;cursor:pointer;opacity:0.85">&times;</button>
        </div>

        <div style="padding:22px">
          ${session.username ? `
            <!-- LOGGED IN VIEW -->
            <div style="background:#F0FDF4;border:1px solid #BBF7D0;border-radius:4px;padding:14px 16px;margin-bottom:18px;display:flex;justify-content:space-between;align-items:center">
              <div>
                <div style="font-size:11.5px;text-transform:uppercase;letter-spacing:0.05em;color:#166534;font-weight:700">Connected Account</div>
                <div style="font-size:18px;font-weight:800;color:#14532D;margin-top:2px">${session.displayName || session.username}</div>
                <div style="font-size:12px;color:#15803D;margin-top:2px">
                  <span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:#22C55E;margin-right:4px"></span>
                  Last synced: <span id="csLastSyncText">${lastSyncStr}</span>
                </div>
              </div>
              <button class="btn pri" id="csSyncNowBtn" style="padding:9px 16px;display:flex;align-items:center;gap:6px">
                <span id="csSyncSpinner" style="display:inline-block">🔄</span> Sync Now
              </button>
            </div>

            <!-- Stats Bar -->
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:18px">
              <div style="background:#F8FAFC;border:1px solid #E2E8F0;padding:10px 14px;border-radius:3px">
                <div style="font-size:11px;color:var(--faint);text-transform:uppercase;font-weight:700">Completed Passages</div>
                <div style="font-size:20px;font-weight:700;color:var(--nav);margin-top:2px">${fpsCount} <span style="font-size:12px;font-weight:400;color:var(--faint)">/ 324 unique</span></div>
              </div>
              <div style="background:#F8FAFC;border:1px solid #E2E8F0;padding:10px 14px;border-radius:3px">
                <div style="font-size:11px;color:var(--faint);text-transform:uppercase;font-weight:700">Exam Attempts</div>
                <div style="font-size:20px;font-weight:700;color:var(--nav);margin-top:2px">${historyCount}</div>
              </div>
            </div>

            <div style="margin-bottom:18px">
              <label style="display:flex;align-items:center;gap:8px;font-size:13px;cursor:pointer">
                <input type="checkbox" id="csAutoSyncChk" ${session.autoSync ? "checked" : ""} />
                <span><b>Automatic Sync:</b> Instantly sync when finishing exams or skipping passages</span>
              </label>
            </div>

            <div id="csStatusMsg" style="min-height:20px;font-size:12.5px;margin-bottom:16px"></div>

            <div style="border-top:1px solid #E2E8F0;padding-top:14px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px">
              <button class="btn" id="csLogoutBtn" style="color:var(--bad)">Sign Out</button>
              <div style="display:flex;gap:8px">
                <button class="btn" id="csToggleAdvancedBtn" style="font-size:12px">⚙️ Cloud Server</button>
              </div>
            </div>
          ` : `
            <!-- LOGGED OUT VIEW -->
            <div style="display:flex;border-bottom:2px solid #E2E8F0;margin-bottom:18px">
              <button id="csTabLogin" class="tab on" style="flex:1;padding:10px;text-align:center;font-weight:700;font-size:14px;border-bottom:3px solid var(--nav)">Log In</button>
              <button id="csTabRegister" class="tab" style="flex:1;padding:10px;text-align:center;font-weight:600;font-size:14px;color:var(--faint)">Create Account</button>
            </div>

            <p id="csFormSub" style="font-size:12.5px;color:var(--soft);margin-bottom:16px;line-height:1.4">
              Log in to sync your completed passages and MCAT exam scores to this computer.
            </p>

            <div style="margin-bottom:14px">
              <label style="display:block;font-size:12.5px;font-weight:700;margin-bottom:5px">Username</label>
              <input type="text" id="csUsernameInput" placeholder="e.g. orbgames" autocomplete="username"
                     style="width:100%;padding:9px 12px;border:1px solid var(--line2);border-radius:3px;font-size:14px" />
              <div style="font-size:11px;color:var(--faint);margin-top:3px">Letters, numbers, hyphens, and underscores (3–30 chars).</div>
            </div>

            <div style="margin-bottom:18px">
              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:5px">
                <label style="font-size:12.5px;font-weight:700">4-Digit PIN</label>
                <button type="button" id="csTogglePin" style="font-size:11.5px;color:var(--selBd);cursor:pointer">Show</button>
              </div>
              <input type="password" id="csPinInput" maxlength="4" placeholder="••••" autocomplete="current-password" inputmode="numeric"
                     style="width:100%;padding:9px 12px;border:1px solid var(--line2);border-radius:3px;font-size:18px;letter-spacing:6px;font-family:monospace" />
              <div style="font-size:11px;color:var(--faint);margin-top:3px">Your easy-to-remember 4-digit PIN (e.g. 1234).</div>
            </div>

            <div id="csStatusMsg" style="min-height:22px;font-size:12.5px;margin-bottom:16px"></div>

            <div style="display:flex;justify-content:space-between;align-items:center;gap:10px">
              <button class="btn" id="csToggleAdvancedBtn" style="font-size:12px">⚙️ Cloud Server</button>
              <button class="btn pri" id="csSubmitBtn" style="padding:10px 22px;font-size:13.5px">Log In &amp; Sync</button>
            </div>
          `}

          <!-- Advanced Server Settings (Collapsible) -->
          <div id="csAdvancedWrap" class="hide" style="margin-top:16px;padding:12px;background:#F8FAFC;border:1px solid #E2E8F0;border-radius:4px">
            <div style="font-size:12px;font-weight:700;margin-bottom:6px">Cloudflare Worker API Endpoint:</div>
            <input type="text" id="csApiUrlInput" value="${getApiUrl()}" placeholder="https://drillroom-sync.yourname.workers.dev"
                   style="width:100%;padding:7px 10px;font-family:monospace;font-size:12px;border:1px solid var(--line);border-radius:2px;margin-bottom:8px" />
            <div style="display:flex;justify-content:space-between;align-items:center">
              <div style="font-size:11px;color:var(--faint)">Default: Cloudflare Workers KV API</div>
              <button class="btn" id="csSaveApiUrlBtn" style="font-size:11.5px;padding:3px 9px">Save Endpoint</button>
            </div>
          </div>

          <!-- Offline / Manual Backup -->
          <div style="margin-top:18px;border-top:1px dashed #CBD5E1;padding-top:12px;display:flex;justify-content:space-between;align-items:center">
            <span style="font-size:11.5px;color:var(--faint)">Offline File Backup:</span>
            <div style="display:flex;gap:6px">
              <button class="btn" id="csExportFileBtn" style="font-size:11px;padding:3px 8px" title="Export complete progress as a JSON file">⬇ Export JSON</button>
              <button class="btn" id="csImportFileBtn" style="font-size:11px;padding:3px 8px" title="Import JSON backup from another device">⬆ Import JSON</button>
              <input type="file" id="csFileInput" accept=".json" class="hide" />
            </div>
          </div>
        </div>
      </div>
    `;

    modal.classList.remove("hide");

    // Close Button
    const closeBtn = document.getElementById("csModalClose");
    if (closeBtn) closeBtn.onclick = () => modal.classList.add("hide");

    // Mask/Unmask PIN
    const togglePinBtn = document.getElementById("csTogglePin");
    const pinInput = document.getElementById("csPinInput");
    if (togglePinBtn && pinInput) {
      togglePinBtn.onclick = () => {
        if (pinInput.type === "password") {
          pinInput.type = "text";
          togglePinBtn.textContent = "Hide";
        } else {
          pinInput.type = "password";
          togglePinBtn.textContent = "Show";
        }
      };
    }

    // Toggle Advanced Server Settings
    const advBtn = document.getElementById("csToggleAdvancedBtn");
    const advWrap = document.getElementById("csAdvancedWrap");
    if (advBtn && advWrap) {
      advBtn.onclick = () => {
        advWrap.classList.toggle("hide");
      };
    }

    // Save Custom API URL
    const saveApiBtn = document.getElementById("csSaveApiUrlBtn");
    const apiInput = document.getElementById("csApiUrlInput");
    if (saveApiBtn && apiInput) {
      saveApiBtn.onclick = () => {
        setApiUrl(apiInput.value);
        const status = document.getElementById("csStatusMsg");
        if (status) status.innerHTML = `<span style="color:var(--ok)">✓ Server endpoint saved: <code>${getApiUrl()}</code></span>`;
      };
    }

    // Offline Export/Import
    const expBtn = document.getElementById("csExportFileBtn");
    if (expBtn) {
      expBtn.onclick = () => {
        const payload = getLocalPayload();
        const blob = new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" });
        const a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = `drillroom-backup-${Date.now()}.json`;
        a.click();
        URL.revokeObjectURL(a.href);
      };
    }

    const impBtn = document.getElementById("csImportFileBtn");
    const fileInput = document.getElementById("csFileInput");
    if (impBtn && fileInput) {
      impBtn.onclick = () => fileInput.click();
      fileInput.onchange = (e) => {
        const file = e.target.files && e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (re) => {
          try {
            const data = JSON.parse(re.target.result);
            mergeAndApplyPayload(data);
            const status = document.getElementById("csStatusMsg");
            if (status) status.innerHTML = `<span style="color:var(--ok);font-weight:700">✓ Successfully imported and merged progress!</span>`;
            setTimeout(() => showCloudSyncModal(), 1200);
          } catch (err) {
            alert("Invalid JSON file: " + err.message);
          }
        };
        reader.readAsText(file);
      };
    }

    // Auto-sync Checkbox
    const autoSyncChk = document.getElementById("csAutoSyncChk");
    if (autoSyncChk) {
      autoSyncChk.onchange = () => {
        localStorage.setItem(STORAGE_KEYS.AUTO_SYNC, autoSyncChk.checked ? "true" : "false");
      };
    }

    // Sync Now Button (when logged in)
    const syncNowBtn = document.getElementById("csSyncNowBtn");
    if (syncNowBtn) {
      syncNowBtn.onclick = async () => {
        const status = document.getElementById("csStatusMsg");
        const spinner = document.getElementById("csSyncSpinner");
        if (spinner) spinner.style.animation = "spin 1s linear infinite";
        if (status) status.innerHTML = `<span style="color:var(--selBd)">Syncing completed passages and scores with Cloudflare...</span>`;

        const res = await syncProgress(true);
        if (spinner) spinner.style.animation = "none";

        if (res.ok) {
          if (status) status.innerHTML = `<span style="color:var(--ok);font-weight:700">✓ Up to date! Synchronized across all computers.</span>`;
          const lastText = document.getElementById("csLastSyncText");
          if (lastText) lastText.textContent = "Just now";
        } else {
          if (status) status.innerHTML = `<span style="color:var(--bad)">✗ Sync error: ${res.error || "Unknown"}</span>`;
        }
      };
    }

    // Sign Out Button
    const logoutBtn = document.getElementById("csLogoutBtn");
    if (logoutBtn) {
      logoutBtn.onclick = async () => {
        if (confirm("Sign out of Cloud Sync? Your progress remains safely stored on this computer.")) {
          await apiFetch("/api/account/logout", { method: "POST" }).catch(() => {});
          clearSession();
          showCloudSyncModal();
        }
      };
    }

    // Tab Toggle: Log In vs Create Account
    let isRegisterMode = false;
    const tabLogin = document.getElementById("csTabLogin");
    const tabRegister = document.getElementById("csTabRegister");
    const submitBtn = document.getElementById("csSubmitBtn");
    const formSub = document.getElementById("csFormSub");

    function setMode(register) {
      isRegisterMode = register;
      if (register) {
        tabRegister.classList.add("on");
        tabRegister.style.borderBottom = "3px solid var(--nav)";
        tabRegister.style.color = "var(--nav)";
        tabLogin.classList.remove("on");
        tabLogin.style.borderBottom = "none";
        tabLogin.style.color = "var(--faint)";
        submitBtn.textContent = "Create Account & Sync";
        if (formSub) formSub.textContent = "Create a username and 4-digit PIN. Your completed progress on this computer will be saved to the cloud.";
      } else {
        tabLogin.classList.add("on");
        tabLogin.style.borderBottom = "3px solid var(--nav)";
        tabLogin.style.color = "var(--nav)";
        tabRegister.classList.remove("on");
        tabRegister.style.borderBottom = "none";
        tabRegister.style.color = "var(--faint)";
        submitBtn.textContent = "Log In & Sync";
        if (formSub) formSub.textContent = "Log in to sync your completed passages and MCAT exam scores to this computer.";
      }
    }

    if (tabLogin && tabRegister) {
      tabLogin.onclick = () => setMode(false);
      tabRegister.onclick = () => setMode(true);
    }

    // Submit Log In or Register
    if (submitBtn) {
      submitBtn.onclick = async () => {
        const usernameEl = document.getElementById("csUsernameInput");
        const pinEl = document.getElementById("csPinInput");
        const status = document.getElementById("csStatusMsg");

        const u = usernameEl ? usernameEl.value.trim() : "";
        const p = pinEl ? pinEl.value.trim() : "";

        if (!u) {
          if (status) status.innerHTML = `<span style="color:var(--bad)">Please enter a username.</span>`;
          return;
        }
        if (!p || p.length !== 4) {
          if (status) status.innerHTML = `<span style="color:var(--bad)">PIN must be exactly 4 digits.</span>`;
          return;
        }

        submitBtn.disabled = true;
        submitBtn.style.opacity = "0.6";
        if (status) status.innerHTML = `<span style="color:var(--selBd)">Connecting to Cloudflare...</span>`;

        let res;
        if (isRegisterMode) {
          res = await registerAccount(u, p);
        } else {
          res = await loginAccount(u, p);
        }

        submitBtn.disabled = false;
        submitBtn.style.opacity = "1";

        if (res.ok) {
          if (status) status.innerHTML = `<span style="color:var(--ok);font-weight:700">✓ ${res.message || "Success!"}</span>`;
          setTimeout(() => {
            showCloudSyncModal();
          }, 600);
        } else {
          if (status) status.innerHTML = `<span style="color:var(--bad)">✗ ${res.error || "Authentication failed."}</span>`;
        }
      };
    }
  }

  // Hook background auto-sync when page loads if user is logged in
  if (typeof window !== "undefined" && typeof window.addEventListener === "function") {
    window.addEventListener("DOMContentLoaded", () => {
      // Inject spinner CSS rule if not present
      if (typeof document !== "undefined") {
        if (!document.getElementById("csSpinStyle")) {
          const st = document.createElement("style");
          st.id = "csSpinStyle";
          st.innerHTML = "@keyframes spin { 100% { transform: rotate(360deg); } }";
          if (document.head) document.head.appendChild(st);
        }

        updateTopBarAccountButton();

        // Hook buttons
        const topBtn = document.getElementById("tCloudAccount");
        if (topBtn) topBtn.onclick = () => showCloudSyncModal();

        const homeBtn = document.getElementById("bCloudAccount");
        if (homeBtn) homeBtn.onclick = () => showCloudSyncModal();

        // Silent background sync on load
        const session = getSession();
        if (session.token && session.autoSync) {
          setTimeout(() => {
            syncProgress().catch(() => {});
          }, 1000);
        }
      }
    });
  }

  // Expose API globally
  window.DrillRoomCloud = {
    getSession,
    registerAccount,
    loginAccount,
    syncProgress,
    clearSession,
    triggerAutoSync,
    showCloudSyncModal,
    getLocalPayload,
    mergeAndApplyPayload,
    getApiUrl,
    setApiUrl
  };

  if (typeof globalThis !== "undefined") {
    globalThis.DrillRoomCloud = window.DrillRoomCloud;
  }
})();
