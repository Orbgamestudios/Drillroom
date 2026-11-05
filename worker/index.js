/**
 * DrillRoom Cloudflare Worker - Multi-Device Cloud Sync
 *
 * Cloudflare Worker providing user accounts with a username and 4-digit PIN,
 * and seamless cross-device synchronization for MCAT DrillRoom using Cloudflare KV.
 *
 * Supported Routes:
 *   GET  /api/health           - Health check and status
 *   POST /api/account/register - Register with username and 4-digit PIN
 *   POST /api/account/login    - Log in with username and 4-digit PIN -> returns session token + data
 *   POST /api/account/sync     - 3-way union merge of completed passages, exams, and history
 *   GET  /api/account/data     - Fetch current saved progress
 *   POST /api/account/logout   - Invalidate session token
 */

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization",
  "Access-Control-Max-Age": "86400"
};

function jsonResponse(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      "Content-Type": "application/json",
      ...CORS_HEADERS
    }
  });
}

function hex(bytes) {
  return [...new Uint8Array(bytes)].map(b => b.toString(16).padStart(2, "0")).join("");
}

function randomHex(length = 16) {
  const bytes = new Uint8Array(length);
  crypto.getRandomValues(bytes);
  return hex(bytes);
}

function constantTimeEqual(a, b) {
  if (typeof a !== "string" || typeof b !== "string") return false;
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) {
    diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  }
  return diff === 0;
}

async function hashPin(username, pin, salt) {
  const enc = new TextEncoder();
  const input = `${username.toLowerCase()}:${pin}:${salt}`;
  const key = await crypto.subtle.importKey(
    "raw",
    enc.encode(input),
    "PBKDF2",
    false,
    ["deriveBits"]
  );
  const bits = await crypto.subtle.deriveBits(
    {
      name: "PBKDF2",
      hash: "SHA-256",
      salt: enc.encode(salt),
      iterations: 100000
    },
    key,
    256
  );
  return hex(bits);
}

async function hashToken(token) {
  const enc = new TextEncoder();
  const digest = await crypto.subtle.digest("SHA-256", enc.encode(token));
  return hex(digest);
}

// In-memory fallback if KV binding is not present (for local testing/dev)
const memoryStore = new Map();

class StorageAdapter {
  constructor(env) {
    this.kv = env && env.DRILLROOM_KV;
  }

  async get(key) {
    if (this.kv) {
      return await this.kv.get(key, "json");
    }
    const val = memoryStore.get(key);
    return val ? JSON.parse(val) : null;
  }

  async put(key, value, options) {
    if (this.kv) {
      return await this.kv.put(key, JSON.stringify(value), options);
    }
    memoryStore.set(key, JSON.stringify(value));
  }

  async delete(key) {
    if (this.kv) {
      return await this.kv.delete(key);
    }
    memoryStore.delete(key);
  }
}

/**
 * Robust 3-Way Union Merge for DrillRoom Progress
 * Ensures zero progress is lost when student works on multiple devices.
 */
function mergeProgressData(local, remote) {
  const loc = local || {};
  const rem = remote || {};

  // 1. Merge completed passage fingerprints (union)
  const fpSet = new Set();
  const locFps = Array.isArray(loc.peData?.completedPassageFingerprints) ? loc.peData.completedPassageFingerprints : [];
  const remFps = Array.isArray(rem.peData?.completedPassageFingerprints) ? rem.peData.completedPassageFingerprints : [];
  locFps.forEach(f => fpSet.add(f));
  remFps.forEach(f => fpSet.add(f));
  const mergedFps = Array.from(fpSet);

  // 2. Merge peData (exams, sets, scores)
  const locPE = loc.peData || {};
  const remPE = rem.peData || {};
  const allExamIds = new Set([...Object.keys(locPE), ...Object.keys(remPE)]);
  allExamIds.delete("completedPassageFingerprints");

  const mergedPE = {
    completedPassageFingerprints: mergedFps
  };

  for (const id of allExamIds) {
    const lRecord = locPE[id] || {};
    const rRecord = remPE[id] || {};

    // Combine completed sets (union)
    const setIndices = new Set();
    if (Array.isArray(lRecord.completedSets)) lRecord.completedSets.forEach(s => setIndices.add(s));
    if (Array.isArray(rRecord.completedSets)) rRecord.completedSets.forEach(s => setIndices.add(s));
    const mergedSets = Array.from(setIndices).sort((a, b) => a - b);

    const isDone = !!(lRecord.done || rRecord.done);

    // Pick highest score or most recent review
    const lTs = lRecord.ts || 0;
    const rTs = rRecord.ts || 0;
    const preferRemote = rTs > lTs;

    const baseRecord = preferRemote ? { ...lRecord, ...rRecord } : { ...rRecord, ...lRecord };
    mergedPE[id] = {
      ...baseRecord,
      completedSets: mergedSets,
      done: isDone,
      score: Math.max(lRecord.score || 0, rRecord.score || 0),
      scaledScore: Math.max(lRecord.scaledScore || 0, rRecord.scaledScore || 0),
      pct: Math.max(lRecord.pct || 0, rRecord.pct || 0),
      ts: Math.max(lTs, rTs)
    };
  }

  // 3. Merge history attempts (keyed by attempt id)
  const historyMap = new Map();
  const locHist = Array.isArray(loc.history) ? loc.history : [];
  const remHist = Array.isArray(rem.history) ? rem.history : [];

  for (const item of [...remHist, ...locHist]) {
    if (item && item.id) {
      if (!historyMap.has(item.id)) {
        historyMap.set(item.id, item);
      }
    }
  }
  const mergedHistory = Array.from(historyMap.values()).sort((a, b) => (b.ts || 0) - (a.ts || 0));

  // 4. Merge preferences
  const mergedPrefs = {
    ...(rem.prefs || {}),
    ...(loc.prefs || {})
  };

  return {
    peData: mergedPE,
    history: mergedHistory,
    prefs: mergedPrefs,
    updatedAt: Date.now()
  };
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const store = new StorageAdapter(env);

    // Handle CORS preflight
    if (request.method === "OPTIONS") {
      return new Response(null, {
        status: 204,
        headers: CORS_HEADERS
      });
    }

    // Health check
    if (url.pathname === "/api/health" || url.pathname === "/health") {
      return jsonResponse({
        ok: true,
        service: "DrillRoom Cloud Sync",
        version: "1.0.0",
        timestamp: Date.now()
      });
    }

    // Helper to get auth token from header or body
    async function getAuthSession(req, bodyToken) {
      const authHeader = req.headers.get("Authorization");
      let token = bodyToken;
      if (authHeader && authHeader.startsWith("Bearer ")) {
        token = authHeader.slice(7).trim();
      }
      if (!token || typeof token !== "string") return null;

      const tHash = await hashToken(token);
      const session = await store.get(`session:${tHash}`);
      if (!session || !session.username || session.expires < Date.now()) {
        return null;
      }
      return { token, ...session };
    }

    // Route: Register (Username + 4-digit PIN)
    if (url.pathname === "/api/account/register" && request.method === "POST") {
      try {
        const body = await request.json();
        const rawUser = String(body.username || "").trim();
        const pin = String(body.pin || "").trim();

        if (!/^[a-zA-Z0-9_-]{3,30}$/.test(rawUser)) {
          return jsonResponse({
            ok: false,
            error: "Username must be 3–30 characters and contain only letters, numbers, hyphens, and underscores."
          }, 400);
        }

        if (!/^\d{4}$/.test(pin)) {
          return jsonResponse({
            ok: false,
            error: "PIN must be exactly 4 digits (0-9)."
          }, 400);
        }

        const normUser = rawUser.toLowerCase();
        const existing = await store.get(`user:${normUser}`);
        if (existing) {
          return jsonResponse({
            ok: false,
            error: `The username "${rawUser}" is already taken. Please pick another username or log in.`
          }, 409);
        }

        const salt = randomHex(16);
        const pinHash = await hashPin(normUser, pin, salt);
        const userRecord = {
          username: normUser,
          displayName: rawUser,
          salt,
          pinHash,
          createdAt: Date.now(),
          updatedAt: Date.now()
        };

        // Create 365-day session token
        const rawToken = `${normUser}.${randomHex(32)}`;
        const tHash = await hashToken(rawToken);
        const expires = Date.now() + 365 * 24 * 60 * 60 * 1000;

        await store.put(`user:${normUser}`, userRecord);
        await store.put(`session:${tHash}`, { username: normUser, expires });

        // Save initial client data if provided
        let initialData = body.initialData || { peData: {}, history: [], prefs: {} };
        initialData.updatedAt = Date.now();
        await store.put(`data:${normUser}`, initialData);

        return jsonResponse({
          ok: true,
          username: normUser,
          displayName: rawUser,
          token: rawToken,
          message: "Account created successfully."
        });
      } catch (err) {
        return jsonResponse({ ok: false, error: "Registration failed: " + err.message }, 500);
      }
    }

    // Route: Login (Username + 4-digit PIN)
    if (url.pathname === "/api/account/login" && request.method === "POST") {
      try {
        const body = await request.json();
        const rawUser = String(body.username || "").trim();
        const pin = String(body.pin || "").trim();

        if (!rawUser || !pin) {
          return jsonResponse({ ok: false, error: "Please enter both username and 4-digit PIN." }, 400);
        }

        const normUser = rawUser.toLowerCase();
        const userRecord = await store.get(`user:${normUser}`);

        const authFailedMsg = "Incorrect username or 4-digit PIN.";
        if (!userRecord || !userRecord.salt || !userRecord.pinHash) {
          return jsonResponse({ ok: false, error: authFailedMsg }, 401);
        }

        const checkHash = await hashPin(normUser, pin, userRecord.salt);
        if (!constantTimeEqual(checkHash, userRecord.pinHash)) {
          return jsonResponse({ ok: false, error: authFailedMsg }, 401);
        }

        // Issue new session
        const rawToken = `${normUser}.${randomHex(32)}`;
        const tHash = await hashToken(rawToken);
        const expires = Date.now() + 365 * 24 * 60 * 60 * 1000;
        await store.put(`session:${tHash}`, { username: normUser, expires });

        // Fetch user data
        const savedData = await store.get(`data:${normUser}`) || { peData: {}, history: [], prefs: {} };

        return jsonResponse({
          ok: true,
          username: normUser,
          displayName: userRecord.displayName || rawUser,
          token: rawToken,
          data: savedData,
          message: "Logged in successfully."
        });
      } catch (err) {
        return jsonResponse({ ok: false, error: "Login failed: " + err.message }, 500);
      }
    }

    // Route: Sync (Bidirectional 3-Way Union Merge)
    if (url.pathname === "/api/account/sync" && request.method === "POST") {
      try {
        const body = await request.json();
        const session = await getAuthSession(request, body.token);
        if (!session) {
          return jsonResponse({ ok: false, error: "Session expired or invalid. Please log in again." }, 401);
        }

        const normUser = session.username;
        const clientData = body.data || {};
        const remoteData = await store.get(`data:${normUser}`) || { peData: {}, history: [], prefs: {} };

        // Perform union merge so no progress on either machine is ever lost
        const merged = mergeProgressData(clientData, remoteData);
        await store.put(`data:${normUser}`, merged);

        return jsonResponse({
          ok: true,
          username: normUser,
          data: merged,
          updatedAt: merged.updatedAt,
          message: "Data synchronized successfully."
        });
      } catch (err) {
        return jsonResponse({ ok: false, error: "Sync failed: " + err.message }, 500);
      }
    }

    // Route: Fetch Data
    if (url.pathname === "/api/account/data" && request.method === "GET") {
      const session = await getAuthSession(request);
      if (!session) {
        return jsonResponse({ ok: false, error: "Session expired or invalid." }, 401);
      }
      const data = await store.get(`data:${session.username}`) || { peData: {}, history: [], prefs: {} };
      return jsonResponse({
        ok: true,
        username: session.username,
        data
      });
    }

    // Route: Logout
    if (url.pathname === "/api/account/logout" && request.method === "POST") {
      try {
        const body = await request.json();
        const session = await getAuthSession(request, body.token);
        if (session) {
          const tHash = await hashToken(session.token);
          await store.delete(`session:${tHash}`);
        }
        return jsonResponse({ ok: true, message: "Logged out successfully." });
      } catch (e) {
        return jsonResponse({ ok: true });
      }
    }

    return jsonResponse({ ok: false, error: "Not Found" }, 404);
  }
};
