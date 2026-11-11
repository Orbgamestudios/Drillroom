// Test Gemini API Model Auto-Discovery and Fallback
const assert = require("assert");

console.log("=== Testing Gemini API Model Discovery and Fallback ===");

const DEFAULT_MODEL = "gemini-1.5-flash";
const SUPPORTED_MODELS = [
  { id: "gemini-1.5-flash", name: "Gemini 1.5 Flash (Recommended — Universally Available & Fast)" },
  { id: "gemini-2.0-flash", name: "Gemini 2.0 Flash (Fast & Modern)" },
  { id: "gemini-1.5-flash-8b", name: "Gemini 1.5 Flash-8B (Lightweight)" },
  { id: "gemini-1.5-pro",   name: "Gemini 1.5 Pro (Deep Cognitive Reasoning — Requires Pro access)" }
];

let mockLocalStorage = {};

function getApiKey() { return "AIzaSyFakeKeyTest123"; }
function getModel() {
  const m = mockLocalStorage["drillroom_gemini_model"];
  if (m && m !== "gemini-3.8-flash" && m !== "gemini-3.8-pro" && m !== "gemini-3.8" && m !== "gemini-2.5-flash") {
    return m;
  }
  return DEFAULT_MODEL;
}

// Simulated mock fetch
async function mockFetch(url, options) {
  if (url.includes("/models?key=")) {
    // ListModels endpoint
    return {
      ok: true,
      json: async () => ({
        models: [
          { name: "models/gemini-1.5-flash", supportedGenerationMethods: ["generateContent"], displayName: "Gemini 1.5 Flash" },
          { name: "models/gemini-1.5-flash-8b", supportedGenerationMethods: ["generateContent"], displayName: "Gemini 1.5 Flash 8B" }
        ]
      })
    };
  }

  if (url.includes("gemini-1.5-pro:generateContent")) {
    return {
      ok: false,
      status: 404,
      json: async () => ({
        error: {
          code: 404,
          status: "NOT_FOUND",
          message: "models/gemini-1.5-pro is not found for API version v1beta, or is not supported for generateContent. Call ModelService.ListModels to see the list of available models and their supported methods."
        }
      })
    };
  }

  if (url.includes("gemini-1.5-flash:generateContent")) {
    return {
      ok: true,
      status: 200,
      json: async () => ({
        candidates: [{
          content: { parts: [{ text: "# Executive Summary\nAnalysis generated successfully!" }] }
        }]
      })
    };
  }

  return { ok: false, status: 404, json: async () => ({ error: { message: "Not found" } }) };
}

async function fetchAvailableModels(apiKey) {
  if (!apiKey) return [];
  try {
    const res = await mockFetch(`https://generativelanguage.googleapis.com/v1beta/models?key=${apiKey}`);
    if (!res.ok) return [];
    const data = await res.json();
    if (!data.models || !Array.isArray(data.models)) return [];
    return data.models
      .filter(m => m.supportedGenerationMethods && m.supportedGenerationMethods.includes("generateContent"))
      .map(m => {
        const id = m.name.replace(/^models\//, "");
        return { id, name: m.displayName ? `${m.displayName} (${id})` : id };
      });
  } catch (e) {
    return [];
  }
}

async function callGeminiAPI(prompt, apiKey, requestedModel) {
  if (!apiKey) throw new Error("Missing Gemini API Key. Please enter your key first.");

  let cleanModel = (requestedModel || getModel()).replace(/^models\//, "").trim();
  if (cleanModel === "gemini-2.5-flash" || cleanModel.startsWith("gemini-3.8")) {
    cleanModel = DEFAULT_MODEL;
  }

  let modelsToTry = [
    cleanModel,
    "gemini-1.5-flash",
    "gemini-2.0-flash",
    "gemini-1.5-flash-8b",
    "gemini-1.5-pro"
  ].filter((v, i, a) => v && a.indexOf(v) === i);

  let lastError = null;

  for (let i = 0; i < modelsToTry.length; i++) {
    const model = modelsToTry[i];
    try {
      const endpoint = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${encodeURIComponent(apiKey)}`;
      const payload = {
        contents: [{ parts: [{ text: String(prompt) }] }]
      };

      const res = await mockFetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      const data = await res.json();

      if (!res.ok) {
        const errMsg = data.error?.message || `HTTP ${res.status}`;
        if (data.error?.status === "NOT_FOUND" || errMsg.toLowerCase().includes("not found") || errMsg.toLowerCase().includes("not supported")) {
          lastError = new Error(`Model ${model} not available: ${errMsg}`);
          if (i === 0) {
            try {
              const detected = await fetchAvailableModels(apiKey);
              if (detected && detected.length > 0) {
                detected.forEach(d => {
                  if (!modelsToTry.includes(d.id)) {
                    modelsToTry.push(d.id);
                  }
                });
              }
            } catch (e) {}
          }
          continue;
        }
        throw new Error(errMsg);
      }

      const cand = data.candidates?.[0];
      const text = cand?.content?.parts?.[0]?.text;
      if (!text) {
        throw new Error("Gemini returned an empty response candidate.");
      }

      mockLocalStorage["drillroom_gemini_model"] = model;
      return { text, modelUsed: model };
    } catch (err) {
      lastError = err;
    }
  }

  throw lastError || new Error("Failed to communicate with the Gemini API.");
}

async function run() {
  // Scenario 1: User had stored "gemini-1.5-pro", but 1.5 Pro is not available on their key
  mockLocalStorage["drillroom_gemini_model"] = "gemini-1.5-pro";
  console.log("Testing with initial model = gemini-1.5-pro (which will return 404)...");
  
  const res = await callGeminiAPI("Generate summary", "fake_key");
  console.log("Call result:", res);

  assert.strictEqual(res.modelUsed, "gemini-1.5-flash");
  assert(res.text.includes("Analysis generated successfully!"));
  assert.strictEqual(mockLocalStorage["drillroom_gemini_model"], "gemini-1.5-flash");
  console.log("✓ Successfully discovered and fell back to gemini-1.5-flash and cached working model!");
  console.log("All Gemini fallback tests PASSED!");
}

run();
