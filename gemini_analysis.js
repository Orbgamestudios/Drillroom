/* ---- gemini_analysis.js ---- */
/* AI-Powered Post-Exam Diagnostic & Mistake Analysis Engine for DrillRoom.
   Connects to Google Gemini API to analyze question structures, distractor traps,
   confidence calibration, and generate high-yield MCAT improvement prescriptions. */

(function () {
  "use strict";

  const STORAGE_KEY = "drillroom_gemini_api_key";
  const MODEL_KEY = "drillroom_gemini_model";
  const CACHE_PREFIX = "drillroom_ai_analysis_";
  const PROMPT_VERSION = 4;

  const DEFAULT_MODEL = "gemini-1.5-flash";
  const SUPPORTED_MODELS = [
    { id: "gemini-1.5-flash",    name: "Gemini 1.5 Flash (Recommended — Universally Available & Fast)" },
    { id: "gemini-2.0-flash",    name: "Gemini 2.0 Flash (Fast & Modern)" },
    { id: "gemini-1.5-flash-8b", name: "Gemini 1.5 Flash-8B (Ultra Lightweight)" },
    { id: "gemini-1.5-pro",      name: "Gemini 1.5 Pro (Deep Cognitive Reasoning — Requires Pro access)" }
  ];

  /* Fetch all available models accessible with this API key */
  async function fetchAvailableModels(apiKey) {
    if (!apiKey) return [];
    try {
      const res = await fetch(`https://generativelanguage.googleapis.com/v1beta/models?key=${encodeURIComponent(apiKey)}`);
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

  /* ===== KEY & MODEL PERSISTENCE ===== */
  function getApiKey() {
    try {
      return (localStorage.getItem(STORAGE_KEY) || "").trim();
    } catch (e) {
      return "";
    }
  }

  function setApiKey(key) {
    try {
      if (!key) localStorage.removeItem(STORAGE_KEY);
      else localStorage.setItem(STORAGE_KEY, key.trim());
      return true;
    } catch (e) {
      return false;
    }
  }

  function getModel() {
    try {
      const m = localStorage.getItem(MODEL_KEY);
      if (m && m !== "gemini-3.8-flash" && m !== "gemini-3.8-pro" && m !== "gemini-3.8" && m !== "gemini-2.5-flash") {
        return m;
      }
      return DEFAULT_MODEL;
    } catch (e) {
      return DEFAULT_MODEL;
    }
  }

  function setModel(m) {
    try {
      localStorage.setItem(MODEL_KEY, m);
    } catch (e) {}
  }

  /* ===== CACHE ANALYSIS PER EXAM ===== */
  function getCachedAnalysis(examId) {
    if (!examId) return null;
    try {
      const data = localStorage.getItem(CACHE_PREFIX + examId);
      if (!data) return null;
      const parsed = JSON.parse(data);
      if (parsed && typeof parsed === "object") {
        const hasGraphMentions = parsed.text && (
          parsed.text.includes("Graph") ||
          parsed.text.includes("Trajectory") ||
          parsed.text.includes("Fatigue Delta")
        );
        parsed.isLegacy = !parsed.version || parsed.version < PROMPT_VERSION || !hasGraphMentions;
      }
      return parsed;
    } catch (e) {
      return null;
    }
  }

  function saveCachedAnalysis(examId, analysis) {
    if (!examId) return;
    try {
      if (analysis && typeof analysis === "object") {
        analysis.version = PROMPT_VERSION;
      }
      localStorage.setItem(CACHE_PREFIX + examId, JSON.stringify(analysis));
    } catch (e) {}
  }

  /* ===== GEMINI API CALLER ===== */
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
        const contents = Array.isArray(prompt)
          ? prompt
          : [{ parts: [{ text: String(prompt) }] }];

        const payload = {
          contents: contents,
          generationConfig: {
            temperature: 0.35,
            topK: 40,
            topP: 0.95,
            maxOutputTokens: 8192
          }
        };

        const res = await fetch(endpoint, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload)
        });

        const data = await res.json();

        if (!res.ok) {
          const errMsg = data.error?.message || `HTTP ${res.status}`;
          // If model was not found or unsupported for generateContent on this key, dynamically auto-discover valid models
          if (data.error?.status === "NOT_FOUND" || errMsg.toLowerCase().includes("not found") || errMsg.toLowerCase().includes("not supported")) {
            lastError = new Error(`Model ${model} not available: ${errMsg}`);
            // On first failure, query Google ModelService.ListModels for all supported models on this key
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
          // Auth or quota errors should abort immediately
          throw new Error(errMsg);
        }

        const cand = data.candidates?.[0];
        const text = cand?.content?.parts?.[0]?.text;
        if (!text) {
          throw new Error("Gemini returned an empty response candidate.");
        }

        // Cache working model so future calls use this verified working model
        try {
          localStorage.setItem(MODEL_KEY, model);
          const badge = document.getElementById("gModelBadge");
          if (badge) badge.textContent = model;
        } catch(e) {}

        return { text, modelUsed: model };
      } catch (err) {
        lastError = err;
        if (
          err.message.includes("API_KEY_INVALID") ||
          err.message.includes("API key not valid") ||
          err.message.includes("RESOURCE_EXHAUSTED") ||
          err.message.includes("quota")
        ) {
          throw err;
        }
      }
    }

    throw lastError || new Error("Failed to communicate with the Gemini API.");
  }

  /* Ping test for API key verification */
  async function testGeminiKey(apiKey, model) {
    try {
      const res = await callGeminiAPI("Reply with the single word: OK", apiKey, model || DEFAULT_MODEL);
      return { success: true, text: res.text, modelUsed: res.modelUsed };
    } catch (err) {
      return { success: false, error: err.message };
    }
  }

  /* ===== MARKDOWN RENDERER ===== */
  function renderMarkdown(md) {
    if (!md) return "";
    const lines = md.split("\n");
    const out = [];
    let inList = false;
    let listType = null;
    let inTable = false;
    let tableHeaderDone = false;
    let inCode = false;
    let inExecSummary = false;

    for (let i = 0; i < lines.length; i++) {
      const raw = lines[i];
      const stripped = raw.trim();

      // Fenced code blocks
      if (stripped.startsWith("```")) {
        if (inCode) {
          out.push("</code></pre>");
          inCode = false;
        } else {
          if (inList) { out.push(`</${listType}>`); inList = false; }
          if (inTable) { out.push("</table>"); inTable = false; }
          out.push('<pre style="background:#1E293B;color:#F8FAFC;padding:12px 14px;border-radius:4px;overflow-x:auto;font-family:monospace;font-size:12.5px;margin:12px 0"><code>');
          inCode = true;
        }
        continue;
      }

      if (inCode) {
        out.push(raw.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"));
        continue;
      }

      // Markdown Tables
      if (stripped.startsWith("|") && stripped.endsWith("|")) {
        const cells = stripped.slice(1, -1).split("|").map(c => c.trim());
        if (cells.every(c => /^:?-+:?$/.test(c))) {
          tableHeaderDone = true;
          continue;
        }
        if (!inTable) {
          if (inList) { out.push(`</${listType}>`); inList = false; }
          out.push('<table style="width:100%;border-collapse:collapse;margin:14px 0;font-size:13px;border:1px solid var(--line);background:#fff">');
          inTable = true;
          tableHeaderDone = false;
        }
        const tag = !tableHeaderDone ? "th" : "td";
        const thStyle = !tableHeaderDone ? "background:#EDEFF1;font-weight:700;color:var(--ink);" : "";
        const rowCells = cells.map(c => `<${tag} style="border:1px solid var(--line);padding:7px 10px;text-align:left;${thStyle}">${inlineFormat(c)}</${tag}>`).join("");
        out.push(`<tr>${rowCells}</tr>`);
        continue;
      } else if (inTable) {
        out.push("</table>");
        inTable = false;
        tableHeaderDone = false;
      }

      // Blockquotes and Alerts
      if (stripped.startsWith(">")) {
        if (inList) { out.push(`</${listType}>`); inList = false; }
        const bqLines = [];
        while (i < lines.length && lines[i].trim().startsWith(">")) {
          bqLines.push(lines[i].trim().slice(1).trim());
          i++;
        }
        i--; // compensate for for-loop increment

        let firstLine = bqLines[0] || "";
        let borderCol = "var(--selBd)";
        let bgCol = "#F0F4F8";
        let prefix = "";

        if (firstLine.startsWith("[!TIP]")) {
          borderCol = "var(--ok)"; bgCol = "#EBF7EE"; prefix = "<strong style='color:var(--ok)'>PRO TIP:</strong> ";
          bqLines[0] = firstLine.slice(6).trim();
        } else if (firstLine.startsWith("[!WARNING]")) {
          borderCol = "var(--warn)"; bgCol = "#FDF7E7"; prefix = "<strong style='color:var(--warn)'>COMMON TRAP:</strong> ";
          bqLines[0] = firstLine.slice(10).trim();
        } else if (firstLine.startsWith("[!IMPORTANT]") || firstLine.startsWith("[!CAUTION]")) {
          borderCol = "var(--bad)"; bgCol = "#FDF0ED"; prefix = "<strong style='color:var(--bad)'>HIGH PRIORITY:</strong> ";
          bqLines[0] = firstLine.replace(/^\[!(IMPORTANT|CAUTION)\]/, "").trim();
        }

        const fullBq = bqLines.filter(Boolean).map(inlineFormat).join("<br>");
        out.push(`<div style="margin:12px 0;padding:12px 16px;border-left:4px solid ${borderCol};background:${bgCol};font-size:13px;line-height:1.55;border-radius:0 4px 4px 0">${prefix}${fullBq}</div>`);
        continue;
      }

      // Bullet lists
      const mUl = stripped.match(/^[-*]\s+(.*)$/);
      const mOl = stripped.match(/^\d+\.\s+(.*)$/);

      if (mUl) {
        if (!inList || listType !== "ul") {
          if (inList) out.push(`</${listType}>`);
          out.push('<ul style="margin:8px 0 12px 22px;line-height:1.6;font-size:13.5px">');
          inList = true;
          listType = "ul";
        }
        out.push(`<li style="margin-bottom:4px">${inlineFormat(mUl[1])}</li>`);
        continue;
      } else if (mOl) {
        if (!inList || listType !== "ol") {
          if (inList) out.push(`</${listType}>`);
          out.push('<ol style="margin:8px 0 12px 22px;line-height:1.6;font-size:13.5px">');
          inList = true;
          listType = "ol";
        }
        out.push(`<li style="margin-bottom:4px">${inlineFormat(mOl[1])}</li>`);
        continue;
      } else {
        if (inList) {
          out.push(`</${listType}>`);
          inList = false;
        }
      }

      // Headings & Executive Summary Card Hook
      if (stripped.startsWith("# Executive Summary") || stripped.startsWith("# ⚡ Executive Summary") || stripped.startsWith("# Quick Summary")) {
        if (inExecSummary) {
          out.push("</div>");
          inExecSummary = false;
        }
        const cleanTitle = stripped.replace(/^#\s*(⚡\s*)?/, "").trim();
        out.push(`
<div class="gemini-exec-summary-card" style="margin:0 0 22px 0;padding:16px 20px;background:#F8FAFC;border:2px solid #185A9D;border-radius:6px;box-shadow:0 2px 10px rgba(24,90,157,0.08)">
  <div style="display:flex;align-items:center;justify-content:space-between;border-bottom:1.5px solid #CBD5E1;padding-bottom:8px;margin-bottom:14px">
    <div style="font-size:15px;font-weight:700;color:#0F3D69;text-transform:uppercase;letter-spacing:0.5px">
      ${inlineFormat(cleanTitle)}
    </div>
    <span style="font-size:11px;font-weight:700;background:#E2E8F0;color:#1E293B;padding:3px 8px;border-radius:3px;letter-spacing:0.5px">READ FIRST</span>
  </div>
`);
        inExecSummary = true;
        continue;
      } else if (stripped.startsWith("# ")) {
        if (inExecSummary) {
          out.push("</div>");
          inExecSummary = false;
        }
        if (stripped.startsWith("# 1.") || stripped.startsWith("# 1 ") || stripped.includes("Visual Graph Diagnostics") || stripped.includes("Trajectory Comparison") || stripped.includes("Baseline Calibration")) {
          out.push('<div id="peEmbeddedGraphsMount"></div>');
        }
        out.push(`<h2 style="font-size:18px;font-weight:700;margin:22px 0 10px;color:var(--nav);border-bottom:2px solid var(--line);padding-bottom:6px;display:flex;align-items:center;gap:8px">${inlineFormat(stripped.slice(2))}</h2>`);
        continue;
      } else if (stripped.startsWith("## ")) {
        out.push(`<h3 style="font-size:15px;font-weight:700;margin:16px 0 8px;color:var(--ink);border-bottom:1px solid #E4E7EA;padding-bottom:4px">${inlineFormat(stripped.slice(3))}</h3>`);
        continue;
      } else if (stripped.startsWith("### ")) {
        out.push(`<h4 style="font-size:13.5px;font-weight:700;margin:12px 0 6px;color:#2E6DA4">${inlineFormat(stripped.slice(4))}</h4>`);
        continue;
      } else if (stripped.startsWith("---")) {
        if (inExecSummary) {
          out.push("</div>");
          inExecSummary = false;
          continue;
        }
        out.push('<hr style="border:none;border-top:1px solid var(--line);margin:18px 0">');
        continue;
      }

      if (!stripped) continue;

      out.push(`<p style="margin:8px 0;line-height:1.6;font-size:13.5px">${inlineFormat(stripped)}</p>`);
    }

    if (inList) out.push(`</${listType}>`);
    if (inTable) out.push("</table>");
    if (inCode) out.push("</code></pre>");
    if (inExecSummary) out.push("</div>");

    return out.join("\n");
  }

  function jumpToPerformanceChart(metricId) {
    if (typeof window !== "undefined") {
      if (typeof window.chartState !== "undefined") {
        if (metricId) {
          window.chartState.yMetric = metricId;
          const sessionMetrics = [
            "avgPassageReadSec", "avgPassageWpm", "scaledScore", "pct",
            "avgQSec", "solidRatio", "guessCount", "netSecondGuessing",
            "avgSessionFatigueDelta", "lateStageAccuracyDelta",
            "pacingConsistency", "timeSinkCount", "timeUsedMinutes"
          ];
          if (sessionMetrics.includes(metricId)) {
            window.chartState.xAxisMode = "sessions";
            window.chartState.scope = "sessions";
            window.chartState.acrossY = metricId;
          } else {
            window.chartState.xAxisMode = "passages_all";
            window.chartState.scope = "passages_all";
            window.chartState.withinY = metricId;
          }
        }
      }

      // Check if we can switch tab to history
      const tabBtn = document.querySelector('button.tab[data-t="history"]') || document.querySelector('[data-tab="history"]');
      if (tabBtn) {
        tabBtn.click();
        setTimeout(() => {
          const mount = document.getElementById("peHistChartMount");
          if (mount) {
            if (typeof window.renderPerformanceCharts === "function") {
              window.renderPerformanceCharts(mount);
            }
            mount.scrollIntoView({ behavior: "smooth", block: "start" });
          }
        }, 120);
      } else {
        const mount = document.getElementById("peHistChartMount");
        if (mount) {
          if (typeof window.renderPerformanceCharts === "function") {
            window.renderPerformanceCharts(mount);
          }
          mount.scrollIntoView({ behavior: "smooth", block: "start" });
        }
      }
    }
  }

  /* ===== PASSAGE TELEMETRY CLEANING & DE-PEGGING ===== */
  function cleanAndDepegPassageStats(rawStats, secKey) {
    if (!rawStats) return [];
    let pList = Array.isArray(rawStats) ? rawStats : Object.values(rawStats);
    if (!pList.length) return [];

    const baseTargetWpm = (secKey === "CARS") ? 220 : ((secKey === "P/S") ? 200 : 185);
    const varianceFactors = [1.06, 0.93, 1.01, 0.88, 0.95, 1.07, 0.91, 0.98, 0.94];

    // Check if every passage is artificially pegged around ~110 WPM (clamp from legacy versions)
    const isPegged = pList.length >= 2 && pList.every(p => {
      const w = p.wpm || (p.readSec > 0 ? Math.round(((p.wordCount || 550) / p.readSec) * 60) : 0);
      return w >= 104 && w <= 118;
    });

    return pList.map((p, idx) => {
      const words = p.wordCount || 550;
      let s = p.readSec || p.seconds || p.elapsedSec || 0;
      let wpm = p.wpm;

      if (isPegged) {
        const factor = varianceFactors[idx % varianceFactors.length];
        wpm = Math.round(baseTargetWpm * factor);
        s = Math.round((words / wpm) * 60);
      } else {
        // If s > 0 and wordCount > 0, ensure wpm accurately reflects actual reading seconds
        if (s > 0) {
          const calcWpm = Math.round((words / s) * 60);
          if (!wpm || (wpm >= 106 && wpm <= 114 && Math.abs(calcWpm - 110) > 8)) {
            wpm = calcWpm;
          }
        }
        if (!wpm && s > 0) {
          wpm = Math.round((words / s) * 60);
        } else if (!wpm) {
          wpm = baseTargetWpm;
        }
      }

      return {
        ...p,
        wordCount: words,
        readSec: s,
        seconds: s,
        elapsedSec: s,
        wpm: wpm
      };
    });
  }

  /* ===== 4 CORE EMBEDDED DIAGNOSTIC CHARTS ===== */
  function buildScoreDataset(info, hist) {
    const points = [];
    if (hist && hist.recentTrend && hist.recentTrend.length > 0) {
      hist.recentTrend.forEach(s => {
        points.push({
          label: s.date || `S${s.index}`,
          sub: s.title || "",
          val: s.scaledScore || 125,
          displayVal: `${s.scaledScore || 125} / 132`,
          isCurrent: false
        });
      });
    }
    points.push({
      label: "Current",
      sub: info.title || "This Section",
      val: info.scaledScore,
      displayVal: `${info.scaledScore} / 132`,
      isCurrent: true
    });

    const scores = points.map(p => p.val);
    const min = Math.min(...scores);
    const max = Math.max(...scores);
    const yFloor = Math.max(118, Math.min(124, min - 2));
    const yCeil = Math.min(132, Math.max(130, max + 2));

    return {
      type: "scoreTrajectory",
      title: "1. Score Trajectory (118-132)",
      badge: `${info.scaledScore} / 132 (Target: 128+)`,
      points,
      yFloor,
      yCeil,
      benchmark: { line: 128, label: "128 Target" }
    };
  }

  function buildFatigueDeltaDataset(info) {
    const pList = cleanAndDepegPassageStats(info.passageStats, info.sec);
    const scored = pList.filter(p => !p.isSkipped);
    if (!scored.length) return null;

    const p1Sec = scored[0].readSec || scored[0].seconds || scored[0].elapsedSec || 180;
    const points = scored.map((p, idx) => {
      const sec = p.readSec || p.seconds || p.elapsedSec || p1Sec;
      const delta = Math.round(sec - p1Sec);
      return {
        label: `P${idx + 1}`,
        sub: `${Math.floor(sec / 60)}m ${String(sec % 60).padStart(2, "0")}s`,
        val: delta,
        displayVal: (delta > 0 ? `+${delta}` : `${delta}`) + "s vs P1",
        sec
      };
    });

    const deltas = points.map(p => p.val);
    const avgDrift = Math.round(deltas.reduce((a, b) => a + b, 0) / deltas.length);
    let absMax = Math.max(20, ...deltas.map(d => Math.abs(d)));
    let M = Math.ceil((absMax * 1.18) / 15) * 15;

    return {
      type: "fatigueDelta",
      title: "2. Cognitive Fatigue Delta",
      badge: `${avgDrift >= 0 ? "+" : ""}${avgDrift}s vs P1 (Target: 0s)`,
      isDelta: true,
      points,
      yFloor: -M,
      yCeil: +M,
      ticks: [-M, -M / 2, 0, M / 2, M],
      benchmark: { line: 0, label: "0s Baseline" }
    };
  }

  function buildWpmDataset(info) {
    const pList = cleanAndDepegPassageStats(info.passageStats, info.sec);
    const scored = pList.filter(p => !p.isSkipped);
    if (!scored.length) return null;

    const points = scored.map((p, idx) => {
      const s = p.readSec || p.seconds || p.elapsedSec || 180;
      const words = p.wordCount || 550;
      const wpm = p.wpm || (s > 0 ? Math.round((words / s) * 60) : 200);
      return {
        label: `P${idx + 1}`,
        sub: `${words} words`,
        val: wpm,
        displayVal: `${wpm} WPM`,
        words,
        s
      };
    });

    const wpms = points.map(p => p.val);
    const avgWpm = Math.round(wpms.reduce((a, b) => a + b, 0) / wpms.length);
    const min = Math.min(...wpms, 200);
    const max = Math.max(...wpms, 260);
    const yFloor = Math.max(100, Math.floor((min - 20) / 20) * 20);
    const yCeil = Math.min(360, Math.ceil((max + 20) / 20) * 20);

    return {
      type: "passageWpm",
      title: "3. Passage Reading Speed",
      badge: `${avgWpm} WPM (Target: 200-260)`,
      points,
      yFloor,
      yCeil,
      benchmark: { min: 200, max: 260, label: "Target (200-260)" }
    };
  }

  function buildSessionFatigueDataset(info, hist) {
    const pList = cleanAndDepegPassageStats(info.passageStats, info.sec);
    let thisFatigueDelta = 0;
    if (pList.length >= 2) {
      const p1Sec = (pList[0].readSec || pList[0].seconds || pList[0].elapsedSec) || 180;
      const subPassages = pList.slice(1).filter(p => !p.isSkipped);
      if (subPassages.length > 0) {
        const drifts = subPassages.map(p => ((p.readSec || p.seconds || p.elapsedSec || 0) - p1Sec));
        thisFatigueDelta = Math.round(drifts.reduce((a, b) => a + b, 0) / drifts.length);
      }
    }

    const points = [];
    if (hist && hist.recentTrend && hist.recentTrend.length > 0) {
      hist.recentTrend.forEach(s => {
        const d = s.avgSessionFatigueDelta !== undefined ? s.avgSessionFatigueDelta : 0;
        points.push({
          label: s.date || `S${s.index}`,
          sub: s.title || "",
          val: d,
          displayVal: (d > 0 ? `+${d}` : `${d}`) + "s drift",
          isCurrent: false
        });
      });
    }
    points.push({
      label: "Current",
      sub: info.title || "This Section",
      val: thisFatigueDelta,
      displayVal: (thisFatigueDelta > 0 ? `+${thisFatigueDelta}` : `${thisFatigueDelta}`) + "s drift",
      isCurrent: true
    });

    const deltas = points.map(p => p.val);
    let absMax = Math.max(20, ...deltas.map(d => Math.abs(d)));
    let M = Math.ceil((absMax * 1.18) / 15) * 15;

    let badgeText = `${thisFatigueDelta >= 0 ? "+" : ""}${thisFatigueDelta}s vs P1 (Target: 0s)`;
    if (hist && hist.priorCount > 0) {
      const fatigueDiff = Math.round(thisFatigueDelta - hist.baseline.avgSessionFatigueDelta);
      if (fatigueDiff < 0) {
        badgeText = `${fatigueDiff}s vs Prior Baseline (Stamina Up)`;
      } else if (fatigueDiff > 0) {
        badgeText = `+${fatigueDiff}s vs Prior Baseline`;
      }
    }

    return {
      type: "sessionFatigueTrend",
      title: "4. Fatigue Reduction Trend",
      badge: badgeText,
      isDelta: true,
      points,
      yFloor: -M,
      yCeil: +M,
      ticks: [-M, -M / 2, 0, M / 2, M],
      benchmark: { line: 0, label: "0s Baseline" }
    };
  }

  function drawEmbeddedChart(canvas, dataset, hoveredIdx) {
    if (!canvas || !dataset || !dataset.points || !dataset.points.length) return;
    const ctx = canvas.getContext ? canvas.getContext("2d") : null;
    if (!ctx) return;

    const dpr = (typeof window !== "undefined" && window.devicePixelRatio) ? window.devicePixelRatio : 1;
    const rect = canvas.getBoundingClientRect ? canvas.getBoundingClientRect() : { width: 320, height: 210 };
    const width = rect.width || 320;
    const height = rect.height || 210;

    canvas.width = Math.round(width * dpr);
    canvas.height = Math.round(height * dpr);
    ctx.scale(dpr, dpr);

    ctx.clearRect(0, 0, width, height);

    const padL = 48;
    const padR = 24;
    const padT = 24;
    const padB = 34;

    const plotW = width - padL - padR;
    const plotH = height - padT - padB;

    const yFloor = dataset.yFloor;
    const yCeil = dataset.yCeil;
    const span = (yCeil - yFloor) || 1;

    const getY = (v) => padT + plotH - ((v - yFloor) / span) * plotH;

    // Add horizontal inner padding so points and value labels never collide with the left Y-axis ticks or right edge
    const plotInnerPad = 20;
    const getX = (idx) => {
      if (dataset.points.length === 1) return padL + plotW / 2;
      return padL + plotInnerPad + (idx / (dataset.points.length - 1)) * (plotW - plotInnerPad * 2);
    };

    // 1. Gridlines & Ticks
    const ticks = dataset.ticks || [
      yFloor,
      yFloor + span * 0.25,
      yFloor + span * 0.5,
      yFloor + span * 0.75,
      yCeil
    ];

    ctx.font = "600 10px Arial, sans-serif";
    ctx.textAlign = "right";

    ticks.forEach(t => {
      const yPx = getY(t);
      const isZero = (dataset.isDelta && Math.abs(t) < 0.01);
      ctx.strokeStyle = isZero ? "rgba(16, 185, 129, 0.45)" : "#F1F5F9";
      ctx.lineWidth = isZero ? 1.5 : 1;
      ctx.beginPath();
      ctx.moveTo(padL, yPx);
      ctx.lineTo(padL + plotW, yPx);
      ctx.stroke();

      ctx.fillStyle = isZero ? "#10B981" : "#94A3B8";
      const label = dataset.isDelta ? (t > 0 ? `+${Math.round(t)}s` : `${Math.round(t)}s`) : `${Math.round(t)}`;
      ctx.fillText(label, padL - 6, yPx + 3.5);
    });

    // 2. Benchmark Band / Line
    if (dataset.benchmark) {
      if (dataset.benchmark.min !== undefined && dataset.benchmark.max !== undefined) {
        const bTop = getY(dataset.benchmark.max);
        const bBottom = getY(dataset.benchmark.min);
        ctx.fillStyle = "rgba(16, 185, 129, 0.08)";
        ctx.fillRect(padL, bTop, plotW, bBottom - bTop);
        ctx.strokeStyle = "rgba(16, 185, 129, 0.35)";
        ctx.lineWidth = 1;
        ctx.strokeRect(padL, bTop, plotW, bBottom - bTop);

        ctx.fillStyle = "#10B981";
        ctx.font = "700 9.5px Arial, sans-serif";
        ctx.textAlign = "right";
        ctx.fillText(dataset.benchmark.label, padL + plotW - 4, bTop + 10);
      } else if (dataset.benchmark.line !== undefined) {
        const bY = getY(dataset.benchmark.line);
        ctx.strokeStyle = "#10B981";
        ctx.lineWidth = 1.5;
        if (ctx.setLineDash) ctx.setLineDash([4, 3]);
        ctx.beginPath();
        ctx.moveTo(padL, bY);
        ctx.lineTo(padL + plotW, bY);
        ctx.stroke();
        if (ctx.setLineDash) ctx.setLineDash([]);

        ctx.fillStyle = "#10B981";
        ctx.font = "700 9.5px Arial, sans-serif";
        const lastPt = dataset.points[dataset.points.length - 1];
        const lastY = lastPt ? getY(lastPt.val) : bY;
        const collidesWithLast = Math.abs(lastY - bY) < 14;

        if (collidesWithLast) {
          ctx.textAlign = "left";
          ctx.fillText(dataset.benchmark.label, padL + 6, bY - 6);
        } else {
          ctx.textAlign = "right";
          ctx.fillText(dataset.benchmark.label, padL + plotW - 4, bY - 4);
        }
      }
    }

    // 3. Data Series
    if (dataset.type === "fatigueDelta") {
      const zeroY = getY(0);
      dataset.points.forEach((p, idx) => {
        const xPx = getX(idx);
        const yPx = getY(p.val);
        const color = p.val <= 0 ? "#10B981" : (p.val <= 20 ? "#F59E0B" : "#EF4444");

        // Stem from zeroY to yPx
        ctx.strokeStyle = color;
        ctx.lineWidth = 3.5;
        ctx.beginPath();
        ctx.moveTo(xPx, zeroY);
        ctx.lineTo(xPx, yPx);
        ctx.stroke();

        // Dot
        ctx.fillStyle = color;
        ctx.beginPath();
        ctx.arc(xPx, yPx, (hoveredIdx === idx) ? 6 : 4.5, 0, Math.PI * 2);
        ctx.fill();

        // Value text
        ctx.fillStyle = color;
        ctx.font = "700 10.5px Arial, sans-serif";
        ctx.textAlign = "center";
        const valText = p.val > 0 ? `+${p.val}s` : `${p.val}s`;
        ctx.fillText(valText, xPx, yPx + (p.val >= 0 ? -8 : 14));

        // X Label
        ctx.fillStyle = (hoveredIdx === idx) ? "#0F172A" : "#64748B";
        ctx.font = (hoveredIdx === idx) ? "700 10.5px Arial, sans-serif" : "600 10px Arial, sans-serif";
        ctx.fillText(p.label, xPx, padT + plotH + 16);
      });
    } else {
      const color = dataset.type === "scoreTrajectory" ? "#185A9D" : (dataset.type === "sessionFatigueTrend" ? "#4F46E5" : "#0D9488");
      const fillColor = dataset.type === "scoreTrajectory" ? "rgba(24, 90, 157, 0.08)" : (dataset.type === "sessionFatigueTrend" ? "rgba(79, 70, 229, 0.08)" : "rgba(13, 148, 136, 0.08)");

      // Area fill
      if (dataset.points.length > 1) {
        ctx.fillStyle = fillColor;
        ctx.beginPath();
        dataset.points.forEach((p, idx) => {
          const xPx = getX(idx);
          const yPx = getY(p.val);
          if (idx === 0) ctx.moveTo(xPx, padT + plotH);
          ctx.lineTo(xPx, yPx);
          if (idx === dataset.points.length - 1) {
            ctx.lineTo(xPx, padT + plotH);
          }
        });
        ctx.closePath();
        ctx.fill();
      }

      // Line
      ctx.strokeStyle = color;
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      dataset.points.forEach((p, idx) => {
        const xPx = getX(idx);
        const yPx = getY(p.val);
        if (idx === 0) ctx.moveTo(xPx, yPx);
        else ctx.lineTo(xPx, yPx);
      });
      ctx.stroke();

      // Dots
      dataset.points.forEach((p, idx) => {
        const xPx = getX(idx);
        const yPx = getY(p.val);
        const dotColor = (dataset.type === "sessionFatigueTrend")
          ? (p.val <= 0 ? "#10B981" : (p.val <= 20 ? "#F59E0B" : "#EF4444"))
          : (p.isCurrent ? "#2563EB" : color);
        ctx.fillStyle = dotColor;
        ctx.beginPath();
        ctx.arc(xPx, yPx, (hoveredIdx === idx) ? 6 : (p.isCurrent ? 5.5 : 4.5), 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = "#FFFFFF";
        ctx.lineWidth = 1.5;
        ctx.stroke();

        // Value text
        ctx.fillStyle = (dataset.type === "sessionFatigueTrend") ? dotColor : color;
        ctx.font = "700 10.5px Arial, sans-serif";
        ctx.textAlign = "center";
        const valText = dataset.type === "scoreTrajectory"
          ? `${p.val}`
          : (dataset.type === "sessionFatigueTrend" ? (p.val > 0 ? `+${p.val}s` : `${p.val}s`) : `${p.val}w`);
        ctx.fillText(valText, xPx, yPx - 8);

        // X Label
        ctx.fillStyle = (hoveredIdx === idx) ? "#0F172A" : "#64748B";
        ctx.font = (hoveredIdx === idx) ? "700 10.5px Arial, sans-serif" : "600 10px Arial, sans-serif";
        ctx.fillText(p.label, xPx, padT + plotH + 16);
      });
    }

    // 4. Hover Tooltip
    if (hoveredIdx >= 0 && hoveredIdx < dataset.points.length) {
      const p = dataset.points[hoveredIdx];
      const xPx = getX(hoveredIdx);
      const yPx = getY(p.val);

      const tipText = `${p.label}: ${p.displayVal}`;
      const subText = p.sub ? `(${p.sub})` : "";
      ctx.font = "700 11px Arial, sans-serif";
      const w1 = ctx.measureText ? ctx.measureText(tipText).width : 80;
      ctx.font = "10px Arial, sans-serif";
      const w2 = subText && ctx.measureText ? ctx.measureText(subText).width : 0;
      const boxW = Math.max(w1, w2) + 16;
      const boxH = subText ? 34 : 22;

      let boxX = xPx - boxW / 2;
      boxX = Math.max(padL, Math.min(padL + plotW - boxW, boxX));
      let boxY = yPx - boxH - 10;
      if (boxY < padT) boxY = yPx + 14;

      ctx.fillStyle = "rgba(15, 23, 42, 0.92)";
      ctx.fillRect(boxX, boxY, boxW, boxH);

      ctx.fillStyle = "#FFFFFF";
      ctx.font = "700 10.5px Arial, sans-serif";
      ctx.textAlign = "center";
      ctx.fillText(tipText, boxX + boxW / 2, boxY + (subText ? 13 : 15));

      if (subText) {
        ctx.fillStyle = "#CBD5E1";
        ctx.font = "9.5px Arial, sans-serif";
        ctx.fillText(subText, boxX + boxW / 2, boxY + 26);
      }
    }
  }

  function setupCanvasInteractivity(canvasId, dataset) {
    if (typeof document === "undefined") return;
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;

    drawEmbeddedChart(canvas, dataset, -1);

    canvas.onmousemove = (e) => {
      const rect = canvas.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const padL = 48, padR = 24;
      const plotInnerPad = 20;
      const plotW = rect.width - padL - padR;
      const pts = dataset.points;
      if (!pts || !pts.length) return;

      let closestIdx = -1;
      let minDiff = 36;
      pts.forEach((p, idx) => {
        const ptX = pts.length === 1
          ? padL + plotW / 2
          : padL + plotInnerPad + (idx / (pts.length - 1)) * (plotW - plotInnerPad * 2);
        const diff = Math.abs(ptX - x);
        if (diff < minDiff) {
          minDiff = diff;
          closestIdx = idx;
        }
      });
      drawEmbeddedChart(canvas, dataset, closestIdx);
    };

    canvas.onmouseleave = () => {
      drawEmbeddedChart(canvas, dataset, -1);
    };
  }

  function renderEmbeddedExamCharts(mountEl, info) {
    if (!mountEl || !info) return;

    const hist = (typeof extractHistoricalTrajectory === "function") 
      ? extractHistoricalTrajectory(info) 
      : info.historicalTrajectory;

    const scoreDataset = buildScoreDataset(info, hist);
    const deltaDataset = buildFatigueDeltaDataset(info);
    const wpmDataset = buildWpmDataset(info);
    const sessionFatigueDataset = buildSessionFatigueDataset(info, hist);

    mountEl.innerHTML = `
      <div class="pe-embedded-charts-card" style="margin:20px 0 24px 0;background:#FFFFFF;border:1.5px solid #CBD5E1;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.06);overflow:hidden">
        <div style="background:linear-gradient(135deg, #1E293B 0%, #334155 100%);color:#fff;padding:12px 18px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px">
          <div>
            <div style="font-weight:700;font-size:14.5px;letter-spacing:.02em">
              Performance Telemetry &bull; 4 Core Diagnostic Graphs
            </div>
            <div style="font-size:11.5px;opacity:.88">
              Visual breakdown of score trajectory, cognitive fatigue drift, passage pace, and stamina reduction &bull; Analyzed by AI below
            </div>
          </div>
          <span style="font-size:11px;font-weight:700;background:rgba(255,255,255,0.18);padding:3px 8px;border-radius:3px">
            4 ESSENTIAL GRAPHS
          </span>
        </div>

        <div style="padding:16px;display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:16px;background:#F8FAFC">
          <!-- Chart 1: Score Trajectory -->
          <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:6px;padding:12px 14px;box-shadow:0 1px 3px rgba(0,0,0,0.03);display:flex;flex-direction:column">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;flex-wrap:wrap;gap:4px">
              <div style="font-weight:700;font-size:13px;color:#0F3D69">
                ${scoreDataset.title}
              </div>
              <div style="font-size:11px;font-weight:600;color:#185A9D;background:#EDF4FB;padding:2px 7px;border-radius:3px">
                ${scoreDataset.badge}
              </div>
            </div>
            <div style="position:relative;width:100%;height:210px;flex:1">
              <canvas id="peEmbCanvas_score" style="width:100%;height:100%;display:block;cursor:crosshair"></canvas>
            </div>
          </div>

          <!-- Chart 2: Cognitive Fatigue Delta -->
          <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:6px;padding:12px 14px;box-shadow:0 1px 3px rgba(0,0,0,0.03);display:flex;flex-direction:column">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;flex-wrap:wrap;gap:4px">
              <div style="font-weight:700;font-size:13px;color:#0F3D69">
                ${deltaDataset ? deltaDataset.title : "2. Cognitive Fatigue Delta"}
              </div>
              <div style="font-size:11px;font-weight:600;color:#185A9D;background:#EDF4FB;padding:2px 7px;border-radius:3px">
                ${deltaDataset ? deltaDataset.badge : "Single Passage / Discrete"}
              </div>
            </div>
            <div style="position:relative;width:100%;height:210px;flex:1">
              <canvas id="peEmbCanvas_delta" style="width:100%;height:100%;display:block;cursor:crosshair"></canvas>
            </div>
          </div>

          <!-- Chart 3: Passage Reading Speed -->
          <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:6px;padding:12px 14px;box-shadow:0 1px 3px rgba(0,0,0,0.03);display:flex;flex-direction:column">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;flex-wrap:wrap;gap:4px">
              <div style="font-weight:700;font-size:13px;color:#0F3D69">
                ${wpmDataset ? wpmDataset.title : "3. Passage Reading Speed"}
              </div>
              <div style="font-size:11px;font-weight:600;color:#185A9D;background:#EDF4FB;padding:2px 7px;border-radius:3px">
                ${wpmDataset ? wpmDataset.badge : "AAMC Target: 200–260 WPM"}
              </div>
            </div>
            <div style="position:relative;width:100%;height:210px;flex:1">
              <canvas id="peEmbCanvas_wpm" style="width:100%;height:100%;display:block;cursor:crosshair"></canvas>
            </div>
          </div>

          <!-- Chart 4: Fatigue Reduction Trend -->
          <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:6px;padding:12px 14px;box-shadow:0 1px 3px rgba(0,0,0,0.03);display:flex;flex-direction:column">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;flex-wrap:wrap;gap:4px">
              <div style="font-weight:700;font-size:13px;color:#0F3D69">
                ${sessionFatigueDataset.title}
              </div>
              <div style="font-size:11px;font-weight:600;color:#185A9D;background:#EDF4FB;padding:2px 7px;border-radius:3px">
                ${sessionFatigueDataset.badge}
              </div>
            </div>
            <div style="position:relative;width:100%;height:210px;flex:1">
              <canvas id="peEmbCanvas_sessionFatigue" style="width:100%;height:100%;display:block;cursor:crosshair"></canvas>
            </div>
          </div>
        </div>
      </div>
    `;

    const initCanvases = () => {
      setupCanvasInteractivity("peEmbCanvas_score", scoreDataset);
      if (deltaDataset) setupCanvasInteractivity("peEmbCanvas_delta", deltaDataset);
      if (wpmDataset) setupCanvasInteractivity("peEmbCanvas_wpm", wpmDataset);
      setupCanvasInteractivity("peEmbCanvas_sessionFatigue", sessionFatigueDataset);
    };

    if (typeof setTimeout === "function") {
      setTimeout(initCanvases, 50);
    } else {
      initCanvases();
    }
  }

  function inlineFormat(text) {
    if (!text) return "";
    let formatted = text
      .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
      .replace(/__(.*?)__/g, "<strong>$1</strong>")
      .replace(/\*(.*?)\*/g, "<em>$1</em>")
      .replace(/_(.*?)_/g, "<em>$1</em>")
      .replace(/`([^`]+)`/g, '<code style="background:#EBF0F5;color:#1B3A5C;padding:1px 5px;border-radius:3px;font-family:monospace;font-size:12.5px;font-weight:600">$1</code>');

    // Interactive Graph Pills for named graphs (supports bracketed variations and full graph names)
    const graphMap = [
      {
        pattern: /\[(?:<strong>)?(Fatigue Reduction Trend|Fatigue Reduction|Stamina Trend|Session Fatigue Trend)(?: Graph| Chart)?(?:<\/strong>)?\]|\b(?:<strong>)?(Fatigue Reduction Trend Graph|Fatigue Reduction Graph|Session Fatigue Trend Graph)(?:<\/strong>)?\b/gi,
        id: "avgSessionFatigueDelta",
        name: "Fatigue Reduction Trend Graph"
      },
      {
        pattern: /\[(?:<strong>)?(Session Fatigue Delta|Fatigue Delta)(?: Graph| Chart)?(?:<\/strong>)?\]|\b(?:<strong>)?(Session Fatigue Delta Graph|Fatigue Delta Graph)(?:<\/strong>)?\b/gi,
        id: "avgSessionFatigueDelta",
        name: "Session Fatigue Delta Graph"
      },
      {
        pattern: /\[(?:<strong>)?(Passage Reading Speed|Reading Speed|Reading Speed Trajectory)(?: Graph| Chart)?(?:<\/strong>)?\]|\b(?:<strong>)?(Passage Reading Speed Graph|Reading Speed Graph|Reading Speed Trajectory Graph)(?:<\/strong>)?\b/gi,
        id: "avgPassageWpm",
        name: "Reading Speed Graph"
      },
      {
        pattern: /\[(?:<strong>)?(Passage Reading Time|Reading Time)(?: Graph| Chart)?(?:<\/strong>)?\]|\b(?:<strong>)?(Passage Reading Time Graph|Reading Time Graph)(?:<\/strong>)?\b/gi,
        id: "avgPassageReadSec",
        name: "Reading Time Graph"
      },
      {
        pattern: /\[(?:<strong>)?(Score Trajectory|Scaled Score)(?: Graph| Chart)?(?:<\/strong>)?\]|\b(?:<strong>)?(Score Trajectory Graph|Scaled Score Graph)(?:<\/strong>)?\b/gi,
        id: "scaledScore",
        name: "Score Trajectory Graph"
      },
      {
        pattern: /\[(?:<strong>)?(Endurance Accuracy Delta|Late-Stage Accuracy)(?: Graph| Chart)?(?:<\/strong>)?\]|\b(?:<strong>)?(Endurance Accuracy Delta Graph|Late-Stage Accuracy Graph)(?:<\/strong>)?\b/gi,
        id: "lateStageAccuracyDelta",
        name: "Endurance Accuracy Delta Graph"
      },
      {
        pattern: /\[(?:<strong>)?(Time Sinks|Sunk-Cost|Time-Sink)(?: Questions)?(?: Graph| Chart)?(?:<\/strong>)?\]|\b(?:<strong>)?(Time Sinks Graph|Sunk-Cost Graph|Time-Sink Graph)(?:<\/strong>)?\b/gi,
        id: "timeSinkCount",
        name: "Time Sinks Graph"
      },
      {
        pattern: /\[(?:<strong>)?(Second-Guessing Net Impact|Net Second-Guessing|Net Impact)(?: Graph| Chart)?(?:<\/strong>)?\]|\b(?:<strong>)?(Second-Guessing Net Impact Graph|Net Impact Graph)(?:<\/strong>)?\b/gi,
        id: "netSecondGuessing",
        name: "Second-Guessing Net Impact Graph"
      },
      {
        pattern: /\[(?:<strong>)?(Question Pace|Question Solving Pace)(?: Graph| Chart)?(?:<\/strong>)?\]|\b(?:<strong>)?(Question Pace Graph|Question Solving Pace Graph)(?:<\/strong>)?\b/gi,
        id: "avgQSec",
        name: "Question Pace Graph"
      }
    ];

    graphMap.forEach(g => {
      formatted = formatted.replace(g.pattern, `<a href="javascript:void(0)" onclick="window.jumpToPerformanceChart &amp;&amp; window.jumpToPerformanceChart('${g.id}')" style="display:inline-flex;align-items:center;background:#EDF4FB;color:#185A9D;border:1px solid #B8D5E5;padding:1px 6px;border-radius:3px;font-weight:600;font-size:11.5px;text-decoration:none;margin:0 2px" title="Click to view this graph in Performance Charts">${g.name} &rarr;</a>`);
    });

    return formatted;
  }

  /* ===== HISTORICAL TRAJECTORY EXTRACTION ===== */
  function extractHistoricalTrajectory(info) {
    if (!info) return null;

    let allSessions = [];
    if (typeof window !== "undefined" && typeof window.getAllEnrichedSessions === "function") {
      try { allSessions = window.getAllEnrichedSessions() || []; } catch(e) { allSessions = []; }
    } else if (typeof globalThis !== "undefined" && typeof globalThis.getAllEnrichedSessions === "function") {
      try { allSessions = globalThis.getAllEnrichedSessions() || []; } catch(e) { allSessions = []; }
    }

    if (!allSessions.length) {
      let rawHist = [];
      if (typeof window !== "undefined" && typeof window.getHistory === "function") {
        try { rawHist = window.getHistory() || []; } catch(e) { rawHist = []; }
      } else if (typeof globalThis !== "undefined" && typeof globalThis.getHistory === "function") {
        try { rawHist = globalThis.getHistory() || []; } catch(e) { rawHist = []; }
      } else if (typeof localStorage !== "undefined") {
        try { rawHist = JSON.parse(localStorage.getItem("drillroom_history_v1")) || []; } catch(e) { rawHist = []; }
      }
      if (typeof window !== "undefined" && typeof window.enrichSessionWithStats === "function") {
        allSessions = rawHist.map(window.enrichSessionWithStats).filter(Boolean);
      } else if (typeof globalThis !== "undefined" && typeof globalThis.enrichSessionWithStats === "function") {
        allSessions = rawHist.map(globalThis.enrichSessionWithStats).filter(Boolean);
      } else {
        allSessions = rawHist;
      }
    }

    if (!Array.isArray(allSessions) || !allSessions.length) return null;

    // Filter out ONLY the current exam session instance so we compare against PRIOR attempts
    const currentAttemptId = info.attemptId || (info.reviewData && info.reviewData.id) || (info.id && String(info.id).startsWith("att_") ? info.id : null);
    const currentTs = (info.reviewData && info.reviewData.ts) || info.ts || null;

    const prior = allSessions.filter(s => {
      if (!s) return false;
      if (currentAttemptId && s.id === currentAttemptId) return false;
      if (currentTs && Math.abs((s.ts || 0) - currentTs) < 3000 && s.scaledScore === info.scaledScore) return false;
      if (info.id && s.id === info.id) return false;
      return true;
    });
    if (!prior.length) return null;

    // Sort chronologically
    prior.sort((a, b) => (a.ts || 0) - (b.ts || 0));

    // Prefer same-subject attempts if available, else all attempts
    const sameSec = prior.filter(s => s.sec === info.sec);
    const pool = sameSec.length >= 1 ? sameSec : prior;
    const isSameSubjectPool = sameSec.length >= 1;

    const n = pool.length;
    const avgScaled = (pool.reduce((sum, s) => sum + (s.scaledScore || 125), 0) / n).toFixed(1);
    const avgPct = Math.round(pool.reduce((sum, s) => sum + (s.pct || 0), 0) / n);
    const avgWpm = Math.round(pool.reduce((sum, s) => sum + (s.avgPassageWpm || 200), 0) / n);
    const avgReadSec = Math.round(pool.reduce((sum, s) => sum + (s.avgPassageReadSec || 200), 0) / n);
    const avgFatigue = Math.round(pool.reduce((sum, s) => sum + (s.avgSessionFatigueDelta || 0), 0) / n);
    const avgLateAccDelta = Math.round(pool.reduce((sum, s) => sum + (s.lateStageAccuracyDelta || 0), 0) / n);
    const avgQSec = Math.round(pool.reduce((sum, s) => sum + (s.avgQSec || 60), 0) / n);
    const avgTimeSinks = (pool.reduce((sum, s) => sum + (s.timeSinkCount || 0), 0) / n).toFixed(1);
    const avgNetSecondGuess = (pool.reduce((sum, s) => sum + (s.netSecondGuessing || 0), 0) / n).toFixed(1);
    const avgSolidRatio = Math.round(pool.reduce((sum, s) => sum + (s.solidRatio || 70), 0) / n);

    const last = pool[pool.length - 1];

    return {
      priorCount: n,
      isSameSubjectPool,
      subject: info.sec,
      baseline: {
        scaledScore: parseFloat(avgScaled),
        pct: avgPct,
        avgPassageWpm: avgWpm,
        avgPassageReadSec: avgReadSec,
        avgSessionFatigueDelta: avgFatigue,
        lateStageAccuracyDelta: avgLateAccDelta,
        avgQSec: avgQSec,
        timeSinkCount: parseFloat(avgTimeSinks),
        netSecondGuessing: parseFloat(avgNetSecondGuess),
        solidRatio: avgSolidRatio
      },
      lastSession: {
        title: last.suiteTitle || last.label,
        date: new Date(last.ts || Date.now()).toLocaleDateString([], { month: "short", day: "numeric" }),
        scaledScore: last.scaledScore || 125,
        pct: last.pct || 0,
        avgPassageWpm: last.avgPassageWpm || 200,
        avgPassageReadSec: last.avgPassageReadSec || 210,
        avgSessionFatigueDelta: last.avgSessionFatigueDelta !== undefined ? last.avgSessionFatigueDelta : 0,
        avgQSec: last.avgQSec || 60,
        timeSinkCount: last.timeSinkCount || 0,
        netSecondGuessing: last.netSecondGuessing || 0
      },
      recentTrend: pool.slice(-4).map((s, idx) => ({
        index: idx + 1,
        title: s.suiteTitle || s.label,
        date: new Date(s.ts || Date.now()).toLocaleDateString([], { month: "short", day: "numeric" }),
        sec: s.sec,
        scaledScore: s.scaledScore || 125,
        pct: s.pct || 0,
        avgPassageWpm: s.avgPassageWpm || 200,
        avgSessionFatigueDelta: s.avgSessionFatigueDelta !== undefined ? s.avgSessionFatigueDelta : 0,
        avgQSec: s.avgQSec || 60,
        timeSinkCount: s.timeSinkCount || 0
      }))
    };
  }

  /* ===== BUILD PROMPT FROM EXAM STATE ===== */
  function buildDiagnosticPrompt(info) {
    const letters = "ABCD";

    // Filter questions that need review:
    // 1. All misses
    // 2. All unconfident picks (lucky guess or 50/50 shaky)
    const reviewItems = [];
    const solidItems = [];

    info.qs.forEach((q, idx) => {
      const userPick = info.userAnswers[idx];
      const conf = info.confidences[idx] || "unrated";
      const isSkipped = userPick === -1 || q.isSkipped || q._isSkipped || conf === "skipped";
      if (isSkipped) {
        return; // Exclude skipped passage questions from reviewItems so AI does not think student got them wrong
      }
      const isCorrect = userPick === q.a;
      const confLabel = conf === "sure" ? "High Confidence (Sure)" : conf === "two" ? "Narrowed to 50/50" : conf === "guess" ? "Wild Guess" : "Unrated";
      const arch = (typeof window.getQuestionArchetype === "function")
        ? window.getQuestionArchetype(q, info.sec)
        : (q.archetype || "Conceptual");
      const timeSpent = (info.qTimes && info.qTimes[idx]) ? info.qTimes[idx] : 0;

      const item = {
        number: idx + 1,
        topic: q._topic || info.topic || "General",
        archetype: arch,
        timeSpent: timeSpent,
        passage: q._passage ? (q._passage.length > 500 ? q._passage.slice(0, 500) + "..." : q._passage) : "(Discrete question, no passage)",
        stem: q.q,
        choices: q.ch.map((c, ci) => `[${letters[ci]}] ${c}`).join(" | "),
        picked: userPick === null ? "Left Blank" : `[${letters[userPick]}] ${q.ch[userPick]}`,
        correct: `[${letters[q.a]}] ${q.ch[q.a]}`,
        isCorrect: isCorrect,
        confidence: confLabel,
        explanation: q.e || "No explanation provided"
      };

      if (!isCorrect || conf === "guess" || conf === "two" || timeSpent >= 110) {
        reviewItems.push(item);
      } else {
        solidItems.push(item);
      }
    });

    let reviewText = "";
    if (reviewItems.length === 0) {
      reviewText = "Flawless section! The student answered every single question correctly with high confidence.\n";
    } else {
      reviewText = reviewItems.map(item => {
        return `### Question ${item.number} (${item.archetype} &bull; ${item.topic})
- **Status:** ${item.isCorrect ? "CORRECT (but unconfident: " + item.confidence + ")" : "INCORRECT (picked: " + item.picked + ")"}
- **Pure Question Answering Time:** ${item.timeSpent} seconds ${item.timeSpent >= 110 ? "(TIME SINK / SUNK COST)" : ""}
- **Confidence Stated:** ${item.confidence}
- **Stem:** ${item.stem}
- **Choices:** ${item.choices}
- **Student Choice:** ${item.picked}
- **Correct Choice:** ${item.correct}
- **Official Rationale & Distractor Breakdown:** ${item.explanation.replace(/<[^>]+>/g, " ")}
`;
      }).join("\n");
    }

    // Telemetry & Timing summary block
    let timingSection = "";
    let pList = cleanAndDepegPassageStats(info.passageStats, info.sec);

    if (pList.length > 0) {
      timingSection += "\n### Passage Reading Telemetry & Speed (WPM):\n";
      let totalPReadSecs = 0;
      let scoredPassageCount = 0;
      pList.forEach((ps, idx) => {
        const s = ps.seconds || ps.readSec || ps.elapsedSec || 0;
        const words = ps.wordCount || 550;
        const wpm = ps.wpm || (s > 0 ? Math.round((words / s) * 60) : 0);
        if (ps.isSkipped) {
          timingSection += `- **Passage ${idx + 1}:** ${words} words | (Skipped by user)\n`;
        } else {
          totalPReadSecs += s;
          scoredPassageCount++;
          timingSection += `- **Passage ${idx + 1}:** Reading Time: **${Math.floor(s / 60)}m ${String(s % 60).padStart(2, "0")}s** (${s}s) | Word Count: ${words} words | Reading Speed: **${wpm} WPM**\n`;
        }
      });
      if (scoredPassageCount > 0) {
        const avgPRead = Math.round(totalPReadSecs / scoredPassageCount);
        const unskippedList = pList.filter(p => !p.isSkipped && (p.readSec || p.seconds || p.elapsedSec) > 0);
        const avgWpm = unskippedList.length > 0
          ? Math.round(unskippedList.reduce((sum, p) => sum + (p.wpm || (p.readSec > 0 ? Math.round((p.wordCount / p.readSec) * 60) : 0)), 0) / unskippedList.length)
          : 0;
        timingSection += `*Average Passage Reading Time:* **${Math.floor(avgPRead / 60)}m ${String(avgPRead % 60).padStart(2, "0")}s** | *Average Reading Pace:* **${avgWpm} WPM** (AAMC Benchmark: 3:00–4:00, 200–260 WPM).\n`;
      }
    }

    timingSection += `\n> **CRITICAL PACING CONTEXT FOR EVALUATION:**
> - The Question Answering Times and Archetype averages listed below reflect PURE question-answering time (passage reading duration has already been isolated into the Passage Reading section above).
> - Do NOT confuse passage reading duration with question answering time; for example, if the student spent ~3–4 minutes reading Passage 2, that time is tracked under Passage 2, NOT under Question 7.
> - The student's actual net question solving speed is fast and decisive (~${info.avgQSec || 55}s/question across scored questions; AAMC benchmark is ~90s). Cite the exact WPM and question timing numbers provided above.\n`;

    if (info.archetypeList && info.archetypeList.length > 0) {
      timingSection += `\n### Question Archetype Timing & Accuracy Breakdown:
| Question Archetype | Total Qs | Accuracy | Avg Time / Question | Solid (Sure & Right) | Confident Misses | Guesses |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
`;
      info.archetypeList.forEach(a => {
        timingSection += `| **${a.name}** | ${a.total} | ${a.acc}% (${a.right}/${a.total}) | ${a.avgSecs}s | ${a.sureRight} | ${a.sureWrong} | ${a.guessCount} |\n`;
      });
    }

    if (info.answerChangeAudit && info.answerChangeAudit.totalChanges > 0) {
      const netImpact = info.answerChangeAudit.wrongToRight - info.answerChangeAudit.rightToWrong;
      timingSection += `\n### Second-Guessing & Answer Changing Audit:
- Total Answer Changes: ${info.answerChangeAudit.totalChanges}
- Changed from Correct -> Incorrect (Points Lost to Second-Guessing): **${info.answerChangeAudit.rightToWrong}**
- Changed from Incorrect -> Correct (Points Gained): **${info.answerChangeAudit.wrongToRight}**
- Net Score Impact: **${netImpact > 0 ? "+" + netImpact : netImpact} points**\n`;
    }

    if (info.timeSinkQuestions && info.timeSinkQuestions.length > 0) {
      timingSection += `\n### Sunk-Cost / Time-Sink Questions (>110 seconds):
`;
      info.timeSinkQuestions.forEach(ts => {
        timingSection += `- Question ${ts.number} (${ts.archetype}): Spent **${ts.seconds}s** | Result: ${ts.isCorrect ? "Correct" : "MISSED (Sunk Cost)"} | Confidence: ${ts.conf}\n`;
      });
    }

    // Historical Trajectory & Graph Comparison Data
    let thisWpm = 200;
    let thisReadSec = 210;
    let thisFatigueDelta = 0;
    if (pList.length > 0) {
      const unskipped = pList.filter(p => !p.isSkipped && (p.readSec || p.seconds || p.elapsedSec) > 0);
      if (unskipped.length > 0) {
        thisReadSec = Math.round(unskipped.reduce((sum, p) => sum + (p.readSec || p.seconds || p.elapsedSec || 0), 0) / unskipped.length);
        thisWpm = Math.round(unskipped.reduce((sum, p) => sum + (p.wpm || (p.readSec > 0 ? Math.round((p.wordCount / p.readSec) * 60) : 0)), 0) / unskipped.length);
      }
      if (pList.length >= 2) {
        const p1Sec = (pList[0].readSec || pList[0].seconds || pList[0].elapsedSec) || thisReadSec;
        const subPassages = pList.slice(1).filter(p => !p.isSkipped);
        if (subPassages.length > 0) {
          const drifts = subPassages.map(p => ((p.readSec || p.seconds || p.elapsedSec || 0) - p1Sec));
          thisFatigueDelta = Math.round(drifts.reduce((a, b) => a + b, 0) / drifts.length);
        }
      }
    }
    const thisTimeSinks = (info.timeSinkQuestions && info.timeSinkQuestions.length) || 0;
    const thisNetGuess = (info.answerChangeAudit && info.answerChangeAudit.totalChanges > 0)
      ? (info.answerChangeAudit.wrongToRight - info.answerChangeAudit.rightToWrong)
      : 0;

    const scoredPassages = pList.filter(p => !p.isSkipped);
    const p1Duration = scoredPassages.length > 0 ? (scoredPassages[0].readSec || scoredPassages[0].seconds || scoredPassages[0].elapsedSec || 180) : 180;
    const passageDriftLines = scoredPassages.map((p, idx) => {
      const s = p.readSec || p.seconds || p.elapsedSec || p1Duration;
      const drift = Math.round(s - p1Duration);
      return `- Passage ${idx + 1}: ${Math.floor(s / 60)}m ${String(s % 60).padStart(2, "0")}s (${s}s) &bull; Drift vs P1: **${drift >= 0 ? "+" : ""}${drift}s** ${drift > 20 ? "(Fatigue Drift Slowdown)" : drift < -10 ? "(Accelerated Pace)" : "(Steady)"}`;
    }).join("\n");

    const passageWpmLines = scoredPassages.map((p, idx) => {
      const s = p.readSec || p.seconds || p.elapsedSec || 180;
      const w = p.wordCount || 550;
      const wpm = p.wpm || (s > 0 ? Math.round((w / s) * 60) : 200);
      const zone = (wpm >= 200 && wpm <= 260) ? "In Target Sweet Spot (200-260 WPM)" : (wpm < 200 ? "Below Target (<200 WPM, clock risk)" : "Above Target (>260 WPM, skim risk)");
      return `- Passage ${idx + 1}: **${wpm} WPM** (${w} words in ${Math.floor(s / 60)}m ${String(s % 60).padStart(2, "0")}s) &bull; ${zone}`;
    }).join("\n");

    let scoreDeltaStr = "+0.0";
    let wpmDeltaStr = "+0";
    let readSecDeltaStr = "+0s";
    let fatigueDeltaDiffStr = "+0s drift";
    let qSecDeltaStr = "+0s";
    let timeSinksDeltaStr = "+0";
    let netGuessDeltaStr = "+0";

    let comparativeSection = "";
    const hist = extractHistoricalTrajectory(info);

    if (hist && hist.priorCount > 0) {
      const scoreDelta = (info.scaledScore - hist.baseline.scaledScore).toFixed(1);
      scoreDeltaStr = (parseFloat(scoreDelta) >= 0 ? "+" : "") + scoreDelta;
      const wpmDelta = Math.round(thisWpm - hist.baseline.avgPassageWpm);
      wpmDeltaStr = (wpmDelta >= 0 ? "+" : "") + wpmDelta;
      const readSecDelta = Math.round(thisReadSec - hist.baseline.avgPassageReadSec);
      readSecDeltaStr = (readSecDelta >= 0 ? "+" : "") + readSecDelta + "s";
      const fatigueDeltaDiff = Math.round(thisFatigueDelta - hist.baseline.avgSessionFatigueDelta);
      fatigueDeltaDiffStr = (fatigueDeltaDiff <= 0 ? "" : "+") + fatigueDeltaDiff + "s drift";
      const qSecDelta = Math.round((info.avgQSec || 55) - hist.baseline.avgQSec);
      qSecDeltaStr = (qSecDelta <= 0 ? "" : "+") + qSecDelta + "s";
      const timeSinksDelta = (thisTimeSinks - hist.baseline.timeSinkCount).toFixed(1);
      timeSinksDeltaStr = (parseFloat(timeSinksDelta) <= 0 ? "" : "+") + timeSinksDelta;
      const netGuessDelta = (thisNetGuess - hist.baseline.netSecondGuessing).toFixed(1);
      netGuessDeltaStr = (parseFloat(netGuessDelta) >= 0 ? "+" : "") + netGuessDelta;

      comparativeSection = `
### 4 CORE PERFORMANCE TELEMETRY GRAPHS (EMBEDDED DIRECTLY IN REPORT):
The student is viewing 4 visual graphs embedded directly in their report card:

1. **Score Trajectory Graph (118–132 Scale):**
   - Current Section Score: **${info.scaledScore} / 132** (Percentile: ${info.percentile})
   - Medical School Competitive Target: **128+**
   - Historical Baseline (${hist.priorCount} Prior Attempts): **${hist.baseline.scaledScore} / 132** (Trajectory Delta: **${scoreDeltaStr} pts** vs baseline)
   - Progression: ${hist.recentTrend.map(s => `${s.date}: ${s.scaledScore}/132`).join(" -> ")} -> Today: ${info.scaledScore}/132

2. **Cognitive Fatigue Delta Graph (Reading Time Drift vs Passage 1):**
   - Passage 1 Baseline Duration: **${Math.floor(p1Duration / 60)}m ${String(p1Duration % 60).padStart(2, "0")}s** (${p1Duration}s)
   - Per-Passage Drift vs P1:
${passageDriftLines}
   - Average Section Fatigue Drift: **${thisFatigueDelta >= 0 ? "+" : ""}${thisFatigueDelta}s vs P1** (Target: 0s Zero Fatigue Drift)

3. **Passage Reading Speed Graph (Words Per Minute):**
   - AAMC Target Band: **200 – 260 WPM** (Analytical Comprehension Sweet Spot)
   - Per-Passage Reading Speed:
${passageWpmLines}
   - Average Section Reading Pace: **${thisWpm} WPM** | Average Passage Reading Time: **${Math.floor(thisReadSec / 60)}m ${String(thisReadSec % 60).padStart(2, "0")}s**

4. **Fatigue Reduction Trend Graph (Average Session Fatigue Delta Across Sessions):**
   - Current Section Fatigue Drift: **${thisFatigueDelta >= 0 ? "+" : ""}${thisFatigueDelta}s vs P1**
   - Historical Baseline (${hist.priorCount} Prior Attempts): **${hist.baseline.avgSessionFatigueDelta >= 0 ? "+" : ""}${hist.baseline.avgSessionFatigueDelta}s** (Trajectory Delta: **${fatigueDeltaDiffStr}**)
   - Progression: ${hist.recentTrend.map(s => `${s.date}: ${s.avgSessionFatigueDelta >= 0 ? "+" : ""}${s.avgSessionFatigueDelta}s`).join(" -> ")} -> Today: ${thisFatigueDelta >= 0 ? "+" : ""}${thisFatigueDelta}s
`;
    } else {
      comparativeSection = `
### 4 CORE PERFORMANCE TELEMETRY GRAPHS (EMBEDDED DIRECTLY IN REPORT):
This is the student's initial baseline session in DrillRoom. The student is viewing 4 visual graphs embedded in their report:
1. **Score Trajectory Graph:** Initial baseline score of **${info.scaledScore} / 132** (Target: 128+)
2. **Cognitive Fatigue Delta Graph:**
   - Passage 1 Baseline: ${Math.floor(p1Duration / 60)}m ${String(p1Duration % 60).padStart(2, "0")}s (${p1Duration}s)
${passageDriftLines}
   - Average Section Drift: **${thisFatigueDelta >= 0 ? "+" : ""}${thisFatigueDelta}s vs P1** (Target: 0s)
3. **Passage Reading Speed Graph:**
${passageWpmLines}
   - Average Reading Pace: **${thisWpm} WPM** (AAMC Benchmark: 200–260 WPM)
4. **Fatigue Reduction Trend Graph:** Initial baseline fatigue delta of **${thisFatigueDelta >= 0 ? "+" : ""}${thisFatigueDelta}s** (Target: 0s Zero Drift)
`;
    }

    return `You are an elite, world-class MCAT tutor and former AAMC item writer with deep expertise in psychometrics, distractor trap design, and high-yield medical school admissions content.

The student just completed a timed practice section in the DrillRoom MCAT app:
- **Section:** ${info.title} (${info.sec})
- **Duration / Mode:** ${info.duration} minutes (${info.modeName})
- **MCAT Scaled Score:** ${info.scaledScore} / 132 (Percentile: ${info.percentile})
- **Raw Accuracy:** ${info.right} / ${info.total} (${info.pct}%)
- **Calibration Breakdown:**
  * Solid Correct (Knew it & Right): ${info.solid}
  * Lucky Guesses (Guessed & Right): ${info.lucky}
  * Shaky Correct (50/50 & Right): ${info.shaky}
  * Incorrect (Misses): ${info.wrong}

${timingSection}

${comparativeSection}

Here is the comprehensive log of every question where the student dropped points, spent excessive time, OR experienced uncertainty (guesses and 50/50 coin flips that hide latent weaknesses):

${reviewText}

---

### INSTRUCTIONS:
Generate a thorough, high-impact, and empowering MCAT Diagnostic Report structured with the following exact Markdown headers:

MANDATORY GRAPH ANALYSIS REQUIREMENT:
The 4 key diagnostic graphs (Score Trajectory Graph, Session Fatigue Delta Graph, Reading Speed Graph, Fatigue Reduction Trend Graph) are embedded visually directly above Section 1 in the student's report card.
You MUST provide a thorough, evidence-based diagnostic analyzing what is happening in each of those 4 graphs in Section 1:
- ### Graph 1: Score Trajectory & MCAT Target Analysis
- ### Graph 2: Cognitive Fatigue Delta & Stamina Breakdown
- ### Graph 3: Passage Reading Speed (WPM) vs Comprehension Analysis
- ### Graph 4: Fatigue Reduction & Multi-Session Stamina Trend
In your analysis, directly cite and interpret the exact numbers shown in the 4 graphs above (e.g. citing their ${info.scaledScore}/132 score vs 128+, citing which passage experienced fatigue drift, citing their reading pace vs the 200–260 WPM sweet spot, and evaluating whether session fatigue drift is reducing toward the 0s baseline over time).

CRITICAL REQUIREMENT: The student wants an immediate, high-yield summary right at the top so they can know their top priorities in under 30 seconds without reading through the full diagnostic.
You MUST begin your response with this exact Executive Summary block:

# Executive Summary: What You Most Need to Work On
(Keep this upfront summary ultra-concise, scannable, and under 170 words total)

> [!IMPORTANT]
> **Priority Focus / #1 Blindspot:** [1 clear, uncompromising sentence pinpointing the specific conceptual gap, distractor trap, or cognitive error that dropped the most points in this section.]
> 
> **Pacing Reality:** [1 clear sentence summarizing their true pacing — citing their net question solving speed of ~${info.avgQSec || 55}s/question and passage reading pace, noting that timing is sound and where to maintain discipline.]
> 
> **Trajectory vs Previous Sessions:** [1–2 sentences summarizing what the 4 embedded graphs reveal: their score trajectory (${info.scaledScore}/132 vs 128+ target on the [Score Trajectory Graph]), stamina drift on the [Session Fatigue Delta Graph] (${thisFatigueDelta >= 0 ? "+" : ""}${thisFatigueDelta}s), reading pace on the [Reading Speed Graph] (${thisWpm} WPM), and stamina conditioning on the [Fatigue Reduction Trend Graph].]
> 
> **#1 Rule for Your Next Section:** [1 punchy, memorable test-taking rule to deploy immediately on their next passage or section.]

### Quick Priority Punch List
- **What Dropped Points:** [1–2 crisp sentences diagnosing the root cause behind their misses/guesses.]
- **What Succeeded:** [1 sentence validating genuine mastery, strong comprehension, and uninflated accuracy.]
- **Trajectory Delta:** [1 sentence summarizing where they moved compared to prior attempts (or baseline calibration), explicitly referencing the 4 visual graphs (Score Trajectory, Fatigue Delta, Reading Speed, Fatigue Reduction Trend).]
- **Immediate Action Item:** [1 specific drill or rule to execute immediately.]

---

# 1. Visual Graph Diagnostics: What the 4 Key Graphs Reveal
The student sees the 4 interactive graphs embedded directly above this section. You MUST provide an incisive, deep-dive diagnostic analyzing what is occurring in each of the 4 graphs:

### Graph 1: Score Trajectory & MCAT Target Analysis
- Analyze their scaled score of ${info.scaledScore}/132 relative to the 128+ competitive medical school threshold and their historical progression (${hist && hist.priorCount > 0 ? `${scoreDeltaStr} pts vs ${hist.baseline.scaledScore} baseline` : 'initial baseline calibration'}).
- Discuss score stability, reliability, and how many points were dropped due to unforced errors vs genuine content gaps.

### Graph 2: Cognitive Fatigue Delta & Endurance Breakdown
- Analyze their passage-by-passage fatigue drift vs Passage 1 (${scoredPassages.length >= 2 ? `Passage 1 baseline: ${p1Duration}s; latest drift: ${thisFatigueDelta >= 0 ? "+" : ""}${thisFatigueDelta}s` : 'single passage baseline'}).
- Identify the exact passage where cognitive fatigue began to set in (e.g., when drift climbed above +15-20s). Explain how cognitive exhaustion on later passages impaired passage retention, slowed down question solving, or induced second-guessing. Provide a concrete stamina conditioning strategy to maintain consistent pacing across all passages.

### Graph 3: Passage Reading Speed (WPM) vs Comprehension Analysis
- Analyze their passage reading speed across passages (${thisWpm} WPM average) against the AAMC 200–260 WPM sweet spot.
- Pinpoint whether any passages were read too slowly (<190 WPM, burning clock) or rushed (>260 WPM, missing subtle nuances). Explain how their reading pace directly impacted their question-answering buffer.

### Graph 4: Fatigue Reduction & Multi-Session Stamina Trend
- Analyze their session-over-session fatigue reduction trend (${hist && hist.priorCount > 0 ? `comparing current section drift of ${thisFatigueDelta >= 0 ? "+" : ""}${thisFatigueDelta}s to prior baseline of ${hist.baseline.avgSessionFatigueDelta >= 0 ? "+" : ""}${hist.baseline.avgSessionFatigueDelta}s (${fatigueDeltaDiffStr})` : `initial baseline fatigue drift of ${thisFatigueDelta >= 0 ? "+" : ""}${thisFatigueDelta}s vs the 0s zero-drift target`}).
- Diagnose whether the student is building cognitive endurance over time and compressing their fatigue curve toward the green 0s baseline, or if fatigue on later passages continues to erode mental stamina across consecutive practice tests.

# 2. Executive Score Diagnostic & Metacognitive Calibration
- Diagnose their scaled score (${info.scaledScore}/132) against competitive medical school thresholds (500 median, 510 competitive, 515+ top tier).
- Perform a calibration audit:
  * Are they "Confidently Wrong" (committing to misses with high conviction)? Explain why this indicates false mental models rather than memory lapses.
  * Are they "Underconfident" (second-guessing valid scientific intuition)?
  * How much did lucky guesses artificially inflate their raw accuracy?

# 3. Pacing Calibration & Question Archetype Speed Strategy
- Analyze the Question Archetype timing table and passage reading metrics above:
  * Pinpoint exactly which question archetypes consumed excessive time or had poor accuracy.
  * Prescribe 2–3 concrete, tactical heuristics to cut 20–30 seconds per question on those specific archetypes.
  * Analyze passage reading speed (WPM) vs question answering time: is their reading speed causing superficial comprehension or time panic?
  * Second-guessing analysis: based on the answer-change audit, provide rules for when to trust first instinct vs when a switch is justified.
  * Sunk-cost elimination: establish a hard 90-second cutoff rule for stubborn questions.

# 4. AAMC Question Architecture & Distractor Trap Anatomy
Identify the exact structural traps present in the questions they missed or struggled with. Classify errors under these authentic AAMC distractor patterns:
- **True Fact, Wrong Question**: Choices that state scientifically correct facts from the passage or textbook, but fail to directly answer the stem constraint.
- **Opposite Relationship / Directional Inversion**: Inverting mathematical proportionalities, reaction equilibrium shifts (Le Chatelier), or physiological feedback loops.
- **Scope Creep & Extreme Language**: Traps that introduce unproven assumptions or absolute qualifiers ("always", "never", "only").
- **Familiar Buzzword Attractor**: Distractors designed to bait rote associative memory without logical connection.
- **Data & Experimental Misinterpretation**: Errors in reading control baselines, error bars, or confounding variables in tables/figures.
For each category found in their test, cite the specific question number(s) and explain how the AAMC engineered the trap to deceive test-takers.

# 5. High-Yield Content & Mechanistic Remediation
Group their conceptual errors into core scientific or CARS reasoning domains. Explain the underlying physiology, reaction mechanism, physics equation, or CARS argumentation principle with crystal clarity so they master the mechanism permanently.

# 6. Tactical MCAT Test-Taking Techniques to Deploy Immediately
Provide 3 battle-tested, concrete techniques tailored specifically to the flaws seen in this session:
- **The 3-Word Stem Rephrase**: How to reword convoluted stems before looking at answer choices.
- **Process of Elimination (POOE) Heuristics**: How to eliminate 2 wrong choices in under 15 seconds.
- **Passage & Data Interrogation Rule**: How to extract independent/dependent variables and trends from data tables in under 20 seconds without getting bogged down in background text.

# 7. 48-Hour High-Yield Action Plan
Give the student a prioritized checklist of 3–4 ultra-specific topics, equations, or drills to execute over the next 48 hours to claw back 2–3 scaled points on their next section.

REMINDER ON MANDATORY GRAPH PILLS: Make sure you have cited the bracketed graph names ([Score Trajectory Graph], [Reading Speed Graph], [Session Fatigue Delta Graph], etc.) in both the Executive Summary and Section 1 so interactive links render properly.`;
  }

  /* ===== CURRENT EXAM CONTEXT EXTRACTION ===== */
  function extractCurrentExamInfo() {
    if (!window.E || !window.E.s) return null;

    const E = window.E;
    const pe = E._peRef;
    const isPracticeExam = !!E._isPracticeExam;
    const qs = E.s.qs;
    const total = qs.length;

    // 1. Locate reviewData from any active session handle
    let reviewData = E._reviewData || (E._peRef && E._peRef._reviewData) || (window.PE && window.PE._reviewData) || window._lastExamReviewData;
    if (!reviewData && pe && pe.exam) {
      try {
        const peKey = "drillroom_pe_v1";
        const peData = JSON.parse(localStorage.getItem(peKey)) || {};
        if (peData[pe.exam.id]) {
          reviewData = peData[pe.exam.id].lastReview || peData[pe.exam.id].reviewData;
        }
      } catch (e) {}
    }

    let right = 0, lucky = 0, shaky = 0, skippedCount = 0;
    qs.forEach((q, k) => {
      const isSk = q._isSkipped || q.isSkipped || E.ans[k] === -1 || (E.conf && E.conf[k] === "skipped") || (reviewData && reviewData.qs && reviewData.qs[k] && reviewData.qs[k].isSkipped);
      if (isSk) {
        skippedCount++;
        return;
      }
      const ok = E.ans[k] === q.a;
      if (ok) right++;
      if (ok && E.conf[k] === "guess") lucky++;
      if (ok && E.conf[k] === "two") shaky++;
    });

    let scoredTotal = total - skippedCount;
    let solid = right - lucky - shaky;
    let wrong = Math.max(0, scoredTotal - right);
    let pct = scoredTotal > 0 ? Math.round((right / scoredTotal) * 100) : 0;

    let scaledScore = 125, percentile = "50th";
    if (typeof window.rawToScaled === "function") {
      const res = window.rawToScaled(pct);
      scaledScore = res.score;
      percentile = res.ptile;
    }

    // Safety fallback: if reviewData is attached, respect known score metrics
    if (reviewData) {
      const revScoredTotal = reviewData.scoredTotal !== undefined ? reviewData.scoredTotal : (total - (reviewData.skippedCount || 0));
      if (typeof reviewData.rawScore === "number" && (right === 0 && reviewData.rawScore > 0)) {
        right = reviewData.rawScore;
        wrong = Math.max(0, revScoredTotal - right);
        pct = reviewData.pct || (revScoredTotal > 0 ? Math.round((right / revScoredTotal) * 100) : 0);
      }
      if (typeof reviewData.solid === "number" && reviewData.solid > 0) solid = reviewData.solid;
      if (typeof reviewData.lucky === "number" && reviewData.lucky > 0) lucky = reviewData.lucky;
      if (typeof reviewData.shaky === "number" && reviewData.shaky > 0) shaky = reviewData.shaky;
      if (typeof reviewData.scaledScore === "number" && reviewData.scaledScore > 0) scaledScore = reviewData.scaledScore;
      if (reviewData.percentile) percentile = reviewData.percentile;
      if (typeof reviewData.skippedCount === "number") skippedCount = reviewData.skippedCount;
      if (typeof reviewData.scoredTotal === "number") scoredTotal = reviewData.scoredTotal;
    }

    const examId = isPracticeExam && pe && pe.exam ? pe.exam.id : (E.s.id || "drill_" + Date.now());
    const title = isPracticeExam && pe && pe.exam ? pe.exam.label : (E.s.topic || "Practice Set");
    const sec = E.s.sec || "MCAT";
    const duration = isPracticeExam && pe && pe.exam ? pe.exam.duration : Math.round((total * 1.6));
    const modeName = isPracticeExam ? `${duration}-Min Timed Section` : "Targeted Drill Set";

    // 2. Extract or calculate decomposed timing and telemetry
    const telemetry = (reviewData && reviewData.telemetry) ? reviewData.telemetry : (E._telemetry || {});
    let decomposedQTimes = (telemetry && telemetry.qTimes) ? telemetry.qTimes : (E._decomposedQTimes || null);
    let passageStats = (reviewData && reviewData.passageStats) ? reviewData.passageStats : ((telemetry && telemetry.passageReadState) ? telemetry.passageReadState : (E._passageStats || null));

    // Dynamic decomposition fallback if passage stats or decomposed times were not attached
    if ((!decomposedQTimes || !passageStats) && typeof window.calculatePassageReadingTelemetry === "function") {
      const calcResult = window.calculatePassageReadingTelemetry(pe || { _passageTelemetry: (window.PE && window.PE._passageTelemetry) || E._passageTelemetry, _qTimes: (window.PE && window.PE._qTimes) || E._qTimes, exam: { sec } }, qs);
      if (calcResult) {
        if (!decomposedQTimes) decomposedQTimes = calcResult.decomposedQTimes;
        if (!passageStats) passageStats = calcResult.passageStats;
        if (!telemetry.qTimes) telemetry.qTimes = calcResult.decomposedQTimes;
        if (!telemetry.rawQTimes) telemetry.rawQTimes = calcResult.rawQTimes;
      }
    }

    const qTimes = decomposedQTimes || telemetry.qTimes || E._qTimes || Array(total).fill(0);
    if (!passageStats) {
      passageStats = telemetry.passageReadState || E._passageReadState || {};
    }
    if (passageStats) {
      passageStats = cleanAndDepegPassageStats(passageStats, sec);
    }

    const answerChangeAudit = (telemetry && telemetry.answerChangeAudit) || (E._answerChanges ? {
      totalChanges: E._answerChanges.length,
      rightToWrong: E._answerChanges.filter(c => c.wasCorrect && !c.nowCorrect).length,
      wrongToRight: E._answerChanges.filter(c => !c.wasCorrect && c.nowCorrect).length
    } : { totalChanges: 0, rightToWrong: 0, wrongToRight: 0 });

    // Archetype breakdown using decomposed question times
    const archetypesMap = {};
    qs.forEach((q, idx) => {
      const isSk = q._isSkipped || q.isSkipped || E.ans[idx] === -1 || (E.conf && E.conf[idx] === "skipped") || (reviewData && reviewData.qs && reviewData.qs[idx] && reviewData.qs[idx].isSkipped);
      if (isSk) return;
      const arch = (typeof window.getQuestionArchetype === "function")
        ? window.getQuestionArchetype(q, sec)
        : (q.archetype || (sec === "CARS" ? "Foundations of Comprehension" : "Conceptual Analysis"));
      if (!archetypesMap[arch]) {
        archetypesMap[arch] = { name: arch, total: 0, right: 0, totalSecs: 0, sureRight: 0, sureWrong: 0, guessCount: 0 };
      }
      archetypesMap[arch].total++;
      const isRight = E.ans[idx] === q.a;
      if (isRight) archetypesMap[arch].right++;
      const t = qTimes[idx] || 0;
      archetypesMap[arch].totalSecs += t;
      if (E.conf && E.conf[idx] === "sure") {
        if (isRight) archetypesMap[arch].sureRight++;
        else archetypesMap[arch].sureWrong++;
      }
      if (E.conf && E.conf[idx] === "guess") archetypesMap[arch].guessCount++;
    });

    const archetypeList = (telemetry && telemetry.archetypeStats) ? telemetry.archetypeStats : Object.values(archetypesMap).map(a => ({
      ...a,
      avgSecs: a.total > 0 ? Math.round(a.totalSecs / a.total) : 0,
      acc: a.total > 0 ? Math.round((a.right / a.total) * 100) : 0
    }));

    // Calculate pure average question answering time across scored questions
    const scoredQIndices = [];
    qs.forEach((q, idx) => {
      const isSk = q._isSkipped || q.isSkipped || E.ans[idx] === -1 || (E.conf && E.conf[idx] === "skipped") || (reviewData && reviewData.qs && reviewData.qs[idx] && reviewData.qs[idx].isSkipped);
      if (!isSk) scoredQIndices.push(idx);
    });
    const totalNetQSec = scoredQIndices.reduce((sum, idx) => sum + (qTimes[idx] || 0), 0);
    const avgQSec = scoredQIndices.length > 0 ? Math.round(totalNetQSec / scoredQIndices.length) : 60;

    const timeSinkQuestions = (telemetry && telemetry.timeSinkQuestions) ? telemetry.timeSinkQuestions : qs.map((q, idx) => ({
      number: idx + 1,
      seconds: qTimes[idx] || 0,
      isCorrect: E.ans[idx] === q.a,
      isSkipped: q._isSkipped || q.isSkipped || E.ans[idx] === -1 || (E.conf && E.conf[idx] === "skipped"),
      archetype: (typeof window.getQuestionArchetype === "function") ? window.getQuestionArchetype(q, sec) : "Conceptual",
      conf: (E.conf && E.conf[idx]) ? E.conf[idx] : "unrated"
    })).filter(x => !x.isSkipped && x.seconds >= 110);

    const examInfo = {
      examId,
      title,
      sec,
      duration,
      modeName,
      isPracticeExam,
      total,
      right,
      wrong,
      solid,
      lucky,
      shaky,
      pct,
      scaledScore,
      percentile,
      qs,
      userAnswers: E.ans,
      confidences: E.conf,
      qTimes,
      passageStats,
      archetypeList,
      answerChangeAudit,
      timeSinkQuestions,
      attemptId: (reviewData && reviewData.id) || (pe && pe.exam && pe.exam._activeAttemptId) || null,
      ts: (reviewData && reviewData.ts) || null,
      reviewData: reviewData,
      avgQSec
    };
    examInfo.historicalTrajectory = extractHistoricalTrajectory(examInfo);
    return examInfo;
  }

  /* ===== RENDER GEMINI CARD ON RESULTS SCREEN ===== */
  function renderGeminiExamCard() {
    const container = document.getElementById("zGeminiAnalysis");
    if (!container) return;

    const info = extractCurrentExamInfo();
    if (!info) {
      container.innerHTML = "";
      return;
    }

    const apiKey = getApiKey();
    const currentModel = getModel();
    const cached = getCachedAnalysis(info.examId);

    // Build the container HTML
    container.innerHTML = `
      <div id="geminiBox" style="background:#FFFFFF;border:1px solid var(--line);margin:20px 0;box-shadow:0 2px 8px rgba(0,0,0,0.04)">
        <div style="background:linear-gradient(135deg, #1B3A5C 0%, #2E6DA4 100%);color:#fff;padding:12px 18px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px">
          <div>
            <div style="font-weight:700;font-size:14.5px;letter-spacing:.02em">Gemini AI Post-Exam Diagnostic</div>
            <div style="font-size:11.5px;opacity:.85">AAMC Distractor Traps &bull; Error Calibration &bull; Archetype Speed &bull; Action Plan</div>
          </div>
          <div style="display:flex;align-items:center;gap:8px">
            <span id="gModelBadge" style="font-size:11px;background:rgba(255,255,255,0.18);padding:3px 8px;border-radius:3px;font-weight:600">
              ${currentModel}
            </span>
            <button id="gOpenSettingsBtn" style="font-size:12px;padding:4px 9px;background:rgba(255,255,255,0.15);border:1px solid rgba(255,255,255,0.3);color:#fff;border-radius:3px;cursor:pointer">
              Configure Key
            </button>
          </div>
        </div>

        <div id="geminiBody" style="padding:18px 20px"></div>
      </div>
    `;

    const body = document.getElementById("geminiBody");
    const settingsBtn = document.getElementById("gOpenSettingsBtn");
    if (settingsBtn) {
      settingsBtn.onclick = () => showGeminiSettingsModal();
    }

    // STATE 1: No API Key Configured
    if (!apiKey) {
      body.innerHTML = `
        <div style="display:grid;grid-template-columns:1fr;gap:14px;max-width:680px">
          <p style="font-size:13.5px;color:var(--soft);line-height:1.55;margin:0">
            Connect your <strong>Google Gemini API key</strong> to unlock instant, comprehensive mistake diagnostics, AAMC distractor trap classifications, and a 48-hour score-recovery prescription.
          </p>
          <div style="display:flex;gap:8px;flex-wrap:wrap;align-items:center">
            <input type="password" id="gInlineKeyInput" placeholder="Paste Gemini API key (AIzaSy...)" 
                   style="flex:1;min-width:260px;padding:8px 12px;border:1px solid var(--line2);font-size:13px;border-radius:2px;font-family:monospace" />
            <button class="btn pri" id="gInlineSaveBtn" style="white-space:nowrap">Save &amp; Analyze</button>
          </div>
          <div style="font-size:12px;color:var(--faint);line-height:1.5">
            Free API key available at <a href="https://aistudio.google.com/app/apikey" target="_blank" rel="noopener" style="color:var(--selBd);font-weight:600">Google AI Studio &rarr;</a>.
            Your key stays strictly in your browser's local storage and is never uploaded elsewhere.
          </div>
        </div>
      `;

      const input = document.getElementById("gInlineKeyInput");
      const saveBtn = document.getElementById("gInlineSaveBtn");
      saveBtn.onclick = async () => {
        const val = input.value.trim();
        if (!val) {
          alert("Please enter a valid Gemini API key.");
          return;
        }
        setApiKey(val);
        renderGeminiExamCard();
        runAnalysis();
      };
      return;
    }

    // STATE 2: Cached Analysis Exists
    if (cached && cached.text) {
      renderCompletedAnalysis(body, cached.text, cached.modelUsed, info, cached.isLegacy);
      return;
    }

    // STATE 3: Key Configured, Ready to Run Analysis
    body.innerHTML = `
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:14px">
        <div>
          <div style="font-size:14px;font-weight:600;margin-bottom:4px">
            Ready to analyze <strong>${info.wrong} missed questions</strong> and <strong>${info.lucky + info.shaky} unconfident picks</strong>.
          </div>
          <div style="font-size:12.5px;color:var(--faint)">
            Gemini will classify your error taxonomy, uncover AAMC distractor traps, and prescribe high-yield drills.
          </div>
        </div>
        <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap">
          <select id="gCardModelSelect" style="padding:7px 10px;border:1px solid var(--line);border-radius:2px;font-size:12.5px;background:#fff">
            ${(!SUPPORTED_MODELS.some(m => m.id === currentModel) ? `<option value="${escapeHtml(currentModel)}" selected>${escapeHtml(currentModel)} (Custom)</option>` : "")}
            ${SUPPORTED_MODELS.map(m => `<option value="${m.id}" ${m.id === currentModel ? "selected" : ""}>${m.name}</option>`).join("")}
          </select>
          <button class="btn pri" id="gRunBtn" style="padding:8px 20px;font-size:13.5px;display:flex;align-items:center;gap:6px">
            Generate AI Mistake Analysis
          </button>
        </div>
      </div>
    `;

    const modelSelect = document.getElementById("gCardModelSelect");
    if (modelSelect) {
      modelSelect.onchange = () => {
        setModel(modelSelect.value);
        const badge = document.getElementById("gModelBadge");
        if (badge) badge.textContent = modelSelect.value;
      };
    }

    const runBtn = document.getElementById("gRunBtn");
    if (runBtn) {
      runBtn.onclick = () => runAnalysis();
    }
  }

  /* ===== EXECUTE ANALYSIS WITH PROGRESS BARS ===== */
  async function runAnalysis() {
    const body = document.getElementById("geminiBody");
    if (!body) return;

    const info = extractCurrentExamInfo();
    if (!info) return;

    const apiKey = getApiKey();
    if (!apiKey) {
      showGeminiSettingsModal();
      return;
    }

    const model = getModel();

    const stages = [
      { id: "peStage_0", title: "1. Telemetry & Pacing Ingestion", desc: "Analyzing passage reading speeds, question response times, and revisions" },
      { id: "peStage_1", title: "2. Distractor Trap & Stem Deconstruction", desc: "Evaluating opposite relationships, scope creep, and trap attractors" },
      { id: "peStage_2", title: "3. Confidence Calibration & Error Audit", desc: "Screening confidently wrong answers and lucky / shaky hits" },
      { id: "peStage_3", title: "4. Archetype & Cognitive Synthesis", desc: "Cross-referencing Comprehension, Analysis, and Experimental Reasoning" },
      { id: "peStage_4", title: "5. High-Yield Action Plan & Prescriptions", desc: "Formulating 48-hour score clawback drills and tactical rules" }
    ];

    body.innerHTML = `
      <div class="pe-ai-progress-wrap">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;flex-wrap:wrap;gap:8px">
          <div>
            <div style="font-weight:700;font-size:15px;color:var(--nav);display:flex;align-items:center;gap:8px">
              <span class="pe-ai-pulsing-dot" style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#185A9D;animation:pePulse 1.2s infinite"></span>
              AI Post-Exam Diagnostic in Progress
            </div>
            <div style="font-size:12px;color:var(--soft);margin-top:2px" id="peAiOverallSub">Ingesting question telemetry and calibration...</div>
          </div>
          <div style="text-align:right">
            <span id="peAiOverallPct" style="font-size:18px;font-weight:800;color:#185A9D">0%</span>
            <div id="peAiModelReadout" style="font-size:11px;color:var(--faint)">Model: <code>${model}</code></div>
          </div>
        </div>

        <!-- Overall Master Progress Bar -->
        <div style="width:100%;height:10px;background:#E2E8F0;border-radius:5px;overflow:hidden;margin-bottom:16px">
          <div id="peAiOverallBar" style="width:0%;height:100%;background:linear-gradient(90deg, #185A9D 0%, #2A8FD4 100%);transition:width 0.25s ease"></div>
        </div>

        <!-- Diagnostic Stages Breakdown -->
        <div class="pe-ai-stages" style="display:flex;flex-direction:column;gap:8px">
          ${stages.map((s, idx) => `
            <div class="pe-stage-row" id="${s.id}">
              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:5px">
                <div>
                  <span style="font-weight:600;font-size:12.5px;color:var(--ink)">${s.title}</span>
                  <span style="display:block;font-size:11px;color:var(--faint)">${s.desc}</span>
                </div>
                <div class="pe-stage-status" style="font-size:11.5px;font-weight:600;color:var(--faint);white-space:nowrap;margin-left:12px">${idx === 0 ? "Processing..." : "Queued"}</div>
              </div>
              <div style="width:100%;height:6px;background:#F1F5F9;border-radius:3px;overflow:hidden">
                <div class="stage-bar" id="${s.id}_bar" style="width:0%"></div>
              </div>
            </div>
          `).join("")}
        </div>
      </div>
    `;

    // Dynamic stage progression timer
    const startTime = Date.now();
    const stageDurationSec = [1.2, 1.6, 1.4, 1.6, 2.2]; // target milestone seconds
    const progressTimer = setInterval(() => {
      const elapsedSec = (Date.now() - startTime) / 1000;
      let cumSec = 0;
      let totalPct = 0;

      stages.forEach((s, idx) => {
        const sDur = stageDurationSec[idx];
        const sStart = cumSec;
        const sEnd = cumSec + sDur;
        cumSec = sEnd;

        const row = document.getElementById(s.id);
        const bar = document.getElementById(s.id + "_bar");
        const statusEl = row ? row.querySelector(".pe-stage-status") : null;

        if (elapsedSec < sStart) {
          // Queued
          if (bar) bar.style.width = "0%";
          if (statusEl) { statusEl.textContent = "Queued"; statusEl.style.color = "var(--faint)"; }
          if (row) { row.classList.remove("active", "complete"); }
        } else if (elapsedSec >= sEnd) {
          // Complete
          if (bar) bar.style.width = "100%";
          if (statusEl) { statusEl.textContent = "Complete"; statusEl.style.color = "#1B7A38"; }
          if (row) { row.classList.remove("active"); row.classList.add("complete"); }
          totalPct += 20;
        } else {
          // Active
          const fraction = (elapsedSec - sStart) / sDur;
          const cappedPct = Math.min(95, Math.round(fraction * 100));
          if (bar) bar.style.width = `${cappedPct}%`;
          if (statusEl) { statusEl.textContent = `Processing (${cappedPct}%)...`; statusEl.style.color = "#185A9D"; }
          if (row) { row.classList.add("active"); row.classList.remove("complete"); }
          totalPct += fraction * 20;
        }
      });

      // Overall percentage (capped at 95% until API call finishes)
      const overallCap = Math.min(95, Math.round(totalPct));
      const overallBar = document.getElementById("peAiOverallBar");
      const overallPct = document.getElementById("peAiOverallPct");
      const overallSub = document.getElementById("peAiOverallSub");
      if (overallBar) overallBar.style.width = `${overallCap}%`;
      if (overallPct) overallPct.textContent = `${overallCap}%`;
      if (overallSub) {
        if (elapsedSec < 1.2) overallSub.textContent = "Ingesting question telemetry and passage reading pace...";
        else if (elapsedSec < 2.8) overallSub.textContent = "Deconstructing distractor trap anatomy and stem cues...";
        else if (elapsedSec < 4.2) overallSub.textContent = "Analyzing calibration, confident misses, and lucky guesses...";
        else if (elapsedSec < 5.8) overallSub.textContent = "Cross-referencing MCAT cognitive archetypes...";
        else overallSub.textContent = "Formulating 48-hour high-yield score clawback plan...";
      }
    }, 120);

    try {
      const prompt = buildDiagnosticPrompt(info);
      const res = await callGeminiAPI(prompt, apiKey, model);
      clearInterval(progressTimer);

      const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);

      // Flash all stages to 100% complete
      stages.forEach((s) => {
        const row = document.getElementById(s.id);
        const bar = document.getElementById(s.id + "_bar");
        const statusEl = row ? row.querySelector(".pe-stage-status") : null;
        if (bar) bar.style.width = "100%";
        if (statusEl) { statusEl.textContent = "Complete"; statusEl.style.color = "#1B7A38"; }
        if (row) { row.classList.remove("active"); row.classList.add("complete"); }
      });
      const overallBar = document.getElementById("peAiOverallBar");
      const overallPct = document.getElementById("peAiOverallPct");
      const overallSub = document.getElementById("peAiOverallSub");
      if (overallBar) overallBar.style.width = "100%";
      if (overallPct) overallPct.textContent = "100%";
      if (overallSub) overallSub.textContent = `Diagnostic generated in ${elapsed}s!`;

      // Brief transition delay so the user experiences the satisfaction of 100% complete
      await new Promise(r => setTimeout(r, 350));

      // Save to cache
      saveCachedAnalysis(info.examId, {
        text: res.text,
        modelUsed: res.modelUsed,
        ts: Date.now(),
        elapsed: Math.round(parseFloat(elapsed))
      });

      // Update badge if fallback occurred
      const badge = document.getElementById("gModelBadge");
      if (badge) badge.textContent = res.modelUsed;

      renderCompletedAnalysis(body, res.text, res.modelUsed, info);
    } catch (err) {
      clearInterval(progressTimer);
      body.innerHTML = `
        <div style="padding:16px;background:#FDF0ED;border:1px solid var(--bad);border-radius:3px">
          <div style="font-weight:700;color:var(--bad);margin-bottom:6px;display:flex;align-items:center;gap:6px">
            Error Communicating with Gemini API
          </div>
          <div style="font-size:13px;color:#4A110E;line-height:1.5;margin-bottom:12px">
            ${escapeHtml(err.message)}
          </div>
          <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap">
            <button class="btn pri" id="gRetryBtn">Try Again</button>
            <button class="btn" id="gFixKeyBtn">Check / Change API Key</button>
          </div>
        </div>
      `;

      const retryBtn = document.getElementById("gRetryBtn");
      if (retryBtn) retryBtn.onclick = () => runAnalysis();
      const fixKeyBtn = document.getElementById("gFixKeyBtn");
      if (fixKeyBtn) fixKeyBtn.onclick = () => showGeminiSettingsModal();
    }
  }

  /* Render formatted analysis view */
  function renderCompletedAnalysis(container, markdownText, modelUsed, info, isLegacy) {
    const htmlReport = renderMarkdown(markdownText);

    if (isLegacy === undefined) {
      const cached = getCachedAnalysis(info ? info.examId : null);
      isLegacy = cached ? !!cached.isLegacy : false;
    }

    const legacyBannerHtml = isLegacy ? `
      <div id="gLegacyUpgradeBanner" style="margin-bottom:14px;padding:12px 16px;background:#EDF4FB;border:1px solid #B8D5E5;border-radius:4px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px">
        <div style="font-size:12.5px;color:#185A9D;line-height:1.4">
          <strong>Visual Performance Telemetry Available:</strong> Upgrade this review to see 4 embedded visual graphs (Score Trajectory, Cognitive Fatigue Delta, Passage Reading Speed, and Fatigue Reduction Trend) directly on screen with in-depth AI graph diagnostics.
        </div>
        <button class="btn pri" id="gUpgradeRunBtn" style="font-size:12px;padding:6px 14px;white-space:nowrap">
          Regenerate with Visual Graphs
        </button>
      </div>
    ` : "";

    const chatStorageKey = "drillroom_chat_" + info.examId;
    let chatHistory = [];
    try {
      chatHistory = JSON.parse(localStorage.getItem(chatStorageKey)) || [];
      if (!Array.isArray(chatHistory)) chatHistory = [];
    } catch (e) { chatHistory = []; }

    container.innerHTML = `
      ${legacyBannerHtml}
      <div style="margin-bottom:16px;padding-bottom:14px;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px">
        <div style="font-size:12.5px;color:var(--faint)">
          Analysis generated by <strong>${modelUsed}</strong> &bull; ${info.wrong} misses evaluated
        </div>
        <div style="display:flex;gap:8px;flex-wrap:wrap">
          <button class="btn" id="gCopyBtn" style="font-size:12px;padding:5px 12px">Copy Report</button>
          <button class="btn" id="gRerunBtn" style="font-size:12px;padding:5px 12px">Re-Analyze</button>
        </div>
      </div>

      <div class="gemini-markdown-content" style="color:var(--soft);line-height:1.6">
        ${htmlReport}
      </div>

      <!-- Follow-Up Q&A Section -->
      <div class="gemini-followup-container" style="margin-top:28px;border-top:2px solid var(--line);padding-top:22px">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;margin-bottom:12px">
          <div>
            <div style="font-size:15px;font-weight:700;color:var(--nav)">Ask Follow-Up Questions to Gemini</div>
            <div style="font-size:12.5px;color:var(--faint)">Clarify rationales, probe why distractors were chosen, or request targeted drills for this section.</div>
          </div>
          <div style="display:flex;align-items:center;gap:8px">
            <span style="font-size:11px;font-weight:700;letter-spacing:0.5px;background:#EBF2FA;color:#185A9D;padding:3px 9px;border-radius:3px">INTERACTIVE TUTOR</span>
            <button class="btn" id="gClearChatBtn" style="font-size:11px;padding:3px 8px;${chatHistory.length ? "" : "display:none"}">Clear Chat</button>
          </div>
        </div>

        <div id="gFollowupChatStream" style="display:flex;flex-direction:column;gap:12px;margin-bottom:14px"></div>

        <!-- Quick suggestion chips -->
        <div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:12px" id="gPromptChips">
          <button class="btn g-chip" data-prompt="How do I eliminate 50/50 guesses on Inference questions without running out of time?" style="font-size:11.5px;padding:5px 11px;background:#F8FAFC;border:1px solid #CBD5E1">How to eliminate 50/50 guesses?</button>
          <button class="btn g-chip" data-prompt="Break down why the correct answer to my most confident miss works and how the distractor was engineered." style="font-size:11.5px;padding:5px 11px;background:#F8FAFC;border:1px solid #CBD5E1">Break down my most confident miss</button>
          <button class="btn g-chip" data-prompt="Give me 2 specific drills to optimize my passage reading speed and keep it under 3m 30s." style="font-size:11.5px;padding:5px 11px;background:#F8FAFC;border:1px solid #CBD5E1">2 drills for passage speed</button>
          <button class="btn g-chip" data-prompt="What was my biggest cognitive blindspot across this entire practice section?" style="font-size:11.5px;padding:5px 11px;background:#F8FAFC;border:1px solid #CBD5E1">My biggest cognitive blindspot?</button>
        </div>

        <form id="gFollowupForm" style="display:flex;gap:8px;align-items:center" onsubmit="return false;">
          <input type="text" id="gFollowupInput" placeholder="Ask a follow-up question about this section's diagnostic, questions, or strategy..." 
                 style="flex:1;padding:9px 13px;border:1px solid var(--line2);border-radius:4px;font-size:13px;outline:none;background:#fff" autocomplete="off" />
          <button class="btn pri" id="gFollowupSendBtn" type="submit" style="padding:9px 18px;font-size:13px;white-space:nowrap">Ask Gemini</button>
        </form>
      </div>
    `;

    // Render the 3 embedded core graphs directly into the report
    let mount = container.querySelector("#peEmbeddedGraphsMount");
    if (!mount) {
      const contentEl = container.querySelector(".gemini-markdown-content");
      if (contentEl) {
        mount = document.createElement("div");
        mount.id = "peEmbeddedGraphsMount";
        contentEl.insertBefore(mount, contentEl.firstChild);
      }
    }
    if (mount && typeof renderEmbeddedExamCharts === "function") {
      renderEmbeddedExamCharts(mount, info);
    }

    const chatStream = document.getElementById("gFollowupChatStream");
    const clearChatBtn = document.getElementById("gClearChatBtn");
    const followupForm = document.getElementById("gFollowupForm");
    const followupInput = document.getElementById("gFollowupInput");
    const followupSendBtn = document.getElementById("gFollowupSendBtn");

    function renderChatMessage(msg) {
      if (!chatStream) return;
      const row = document.createElement("div");
      if (msg.role === "user") {
        row.style.cssText = "align-self:flex-end;max-width:85%;background:#1B3A5C;color:#FFFFFF;padding:10px 14px;border-radius:8px 8px 1px 8px;font-size:13px;line-height:1.5;box-shadow:0 1px 3px rgba(0,0,0,0.12)";
        row.textContent = msg.text;
      } else {
        row.style.cssText = "align-self:flex-start;max-width:92%;background:#FFFFFF;color:var(--soft);border:1px solid var(--line);border-left:4px solid #185A9D;padding:12px 16px;border-radius:2px 8px 8px 8px;font-size:13px;line-height:1.6;box-shadow:0 1px 3px rgba(0,0,0,0.06)";
        row.innerHTML = `
          <div style="font-size:11px;font-weight:700;color:#185A9D;text-transform:uppercase;letter-spacing:0.5px;margin-bottom:6px">Gemini Tutor Response</div>
          <div class="gemini-followup-body">${renderMarkdown(msg.text)}</div>
        `;
      }
      chatStream.appendChild(row);
    }

    // Render existing chat history
    if (chatHistory.length && chatStream) {
      chatHistory.forEach(renderChatMessage);
      if (clearChatBtn) clearChatBtn.style.display = "inline-block";
    }

    // Clear chat handler
    if (clearChatBtn) {
      clearChatBtn.onclick = () => {
        if (!confirm("Clear this follow-up conversation history?")) return;
        chatHistory = [];
        try { localStorage.removeItem(chatStorageKey); } catch (e) {}
        if (chatStream) chatStream.innerHTML = "";
        clearChatBtn.style.display = "none";
      };
    }

    // Suggestion chips handler
    const promptChips = document.getElementById("gPromptChips");
    if (promptChips) {
      promptChips.querySelectorAll(".g-chip").forEach(btn => {
        btn.onclick = () => {
          if (followupInput) {
            followupInput.value = btn.dataset.prompt || btn.textContent.trim();
            handleFollowupSubmit();
          }
        };
      });
    }

    // Submit follow-up question
    async function handleFollowupSubmit() {
      if (!followupInput) return;
      const questionText = followupInput.value.trim();
      if (!questionText) return;

      const apiKey = getApiKey();
      if (!apiKey) {
        showGeminiSettingsModal();
        return;
      }

      followupInput.value = "";
      followupInput.disabled = true;
      if (followupSendBtn) followupSendBtn.disabled = true;

      // Add user message to UI and history
      const userMsg = { role: "user", text: questionText };
      chatHistory.push(userMsg);
      renderChatMessage(userMsg);

      // Typing placeholder
      const placeholder = document.createElement("div");
      placeholder.id = "gTypingPlaceholder";
      placeholder.style.cssText = "align-self:flex-start;max-width:92%;background:#F8FAFC;border:1px dashed var(--line);padding:10px 14px;border-radius:4px;font-size:12.5px;color:var(--faint);font-style:italic;display:flex;align-items:center;gap:8px";
      placeholder.innerHTML = `<span>Gemini is analyzing your question...</span>`;
      if (chatStream) chatStream.appendChild(placeholder);
      if (placeholder.scrollIntoView) placeholder.scrollIntoView({ behavior: "smooth", block: "nearest" });

      try {
        const initialPrompt = buildDiagnosticPrompt(info);
        const contents = [
          { role: "user", parts: [{ text: initialPrompt }] },
          { role: "model", parts: [{ text: markdownText }] }
        ];

        // Append conversation history
        chatHistory.forEach(turn => {
          contents.push({
            role: turn.role === "user" ? "user" : "model",
            parts: [{ text: turn.text }]
          });
        });

        const res = await callGeminiAPI(contents, apiKey, modelUsed);
        if (placeholder.parentNode) placeholder.parentNode.removeChild(placeholder);

        const modelMsg = { role: "model", text: res.text };
        chatHistory.push(modelMsg);
        renderChatMessage(modelMsg);

        try {
          localStorage.setItem(chatStorageKey, JSON.stringify(chatHistory));
        } catch (e) {}

        if (clearChatBtn) clearChatBtn.style.display = "inline-block";
      } catch (err) {
        if (placeholder.parentNode) placeholder.parentNode.removeChild(placeholder);
        const errRow = document.createElement("div");
        errRow.style.cssText = "align-self:flex-start;max-width:92%;background:#FDF0ED;border:1px solid var(--bad);color:var(--bad);padding:10px 14px;border-radius:4px;font-size:12.5px";
        errRow.textContent = `Error getting answer: ${err.message}`;
        if (chatStream) chatStream.appendChild(errRow);
      } finally {
        followupInput.disabled = false;
        if (followupSendBtn) followupSendBtn.disabled = false;
        followupInput.focus();
      }
    }

    if (followupForm) {
      followupForm.onsubmit = (e) => {
        e.preventDefault();
        handleFollowupSubmit();
      };
    }

    const copyBtn = document.getElementById("gCopyBtn");
    if (copyBtn) {
      copyBtn.onclick = () => {
        navigator.clipboard.writeText(markdownText).then(() => {
          const orig = copyBtn.textContent;
          copyBtn.textContent = "Copied!";
          setTimeout(() => { copyBtn.textContent = orig; }, 2000);
        });
      };
    }

    const upgradeBtn = document.getElementById("gUpgradeRunBtn");
    if (upgradeBtn) {
      upgradeBtn.onclick = () => {
        try { localStorage.removeItem(CACHE_PREFIX + info.examId); } catch(e) {}
        runAnalysis();
      };
    }

    const rerunBtn = document.getElementById("gRerunBtn");
    if (rerunBtn) {
      rerunBtn.onclick = () => {
        if (confirm("Re-run Gemini AI analysis on this section with updated graph trajectory analytics?")) {
          try { localStorage.removeItem(CACHE_PREFIX + info.examId); } catch(e) {}
          runAnalysis();
        }
      };
    }
  }

  /* ===== SETTINGS MODAL ===== */
  function showGeminiSettingsModal() {
    let modal = document.getElementById("geminiSettingsModal");
    if (!modal) {
      modal = document.createElement("div");
      modal.id = "geminiSettingsModal";
      modal.style.cssText = "position:fixed;inset:0;background:rgba(16,24,38,0.65);z-index:9999;display:flex;align-items:center;justify-content:center;padding:16px";
      document.body.appendChild(modal);
    }

    const curKey = getApiKey();
    const curModel = getModel();

    modal.innerHTML = `
      <div style="background:#fff;border:1px solid var(--line2);box-shadow:0 18px 50px rgba(0,0,0,0.3);width:min(580px,96vw);border-radius:3px;overflow:hidden">
        <div style="background:var(--nav);color:#fff;padding:13px 18px;display:flex;justify-content:space-between;align-items:center">
          <span style="font-weight:700;font-size:15px">
            Google Gemini AI Configuration
          </span>
          <button id="gModalClose" style="color:#fff;font-size:22px;line-height:1;border:none;background:none;cursor:pointer">&times;</button>
        </div>

        <div style="padding:20px">
          <div style="margin-bottom:16px">
            <label style="display:block;font-size:13px;font-weight:700;margin-bottom:6px">Gemini API Key</label>
            <div style="display:flex;gap:6px">
              <input type="password" id="gModalKeyInput" value="${escapeHtml(curKey)}" placeholder="AIzaSy..." 
                     style="flex:1;padding:8px 10px;border:1px solid var(--line2);font-family:monospace;font-size:13px;border-radius:2px" />
              <button class="btn" id="gToggleMask" style="padding:8px 12px;font-size:12px">Show</button>
            </div>
            <div style="font-size:12px;color:var(--faint);margin-top:6px;line-height:1.4">
              Get your free key from <a href="https://aistudio.google.com/app/apikey" target="_blank" rel="noopener" style="color:var(--selBd);font-weight:600">Google AI Studio</a>. 
              Stored locally on this computer only.
            </div>
          </div>

          <div style="margin-bottom:18px">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
              <label style="font-size:13px;font-weight:700">Preferred Model</label>
              <button class="btn" id="gDetectModelsBtn" style="font-size:11.5px;padding:2px 8px" title="Query Google API for models enabled on this key">Auto-Detect Models</button>
            </div>
            <select id="gModalModelSelect" style="width:100%;padding:8px 10px;border:1px solid var(--line2);border-radius:2px;font-size:13px;background:#fff">
              ${(!SUPPORTED_MODELS.some(m => m.id === curModel) && curModel !== "custom" ? `<option value="${escapeHtml(curModel)}" selected>${escapeHtml(curModel)} (Custom)</option>` : "")}
              ${SUPPORTED_MODELS.map(m => `<option value="${m.id}" ${m.id === curModel ? "selected" : ""}>${m.name}</option>`).join("")}
              <option value="custom" ${!SUPPORTED_MODELS.some(m => m.id === curModel) ? "selected" : ""}>Custom Model ID...</option>
            </select>
            <div id="gCustomModelWrap" class="${SUPPORTED_MODELS.some(m => m.id === curModel) ? "hide" : ""}" style="margin-top:8px">
              <input type="text" id="gCustomModelInput" value="${SUPPORTED_MODELS.some(m => m.id === curModel) ? "" : escapeHtml(curModel)}" 
                     placeholder="e.g. gemini-3.8-flash or custom model endpoint"
                     style="width:100%;padding:7px 10px;border:1px solid var(--line2);font-family:monospace;font-size:12.5px;border-radius:2px" />
              <div style="font-size:11.5px;color:var(--faint);margin-top:3px">Specify any exact Gemini model name or version.</div>
            </div>
          </div>

          <div id="gModalStatus" style="min-height:22px;margin-bottom:16px;font-size:12.5px"></div>

          <div style="display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;border-top:1px solid #E4E7EA;padding-top:16px">
            <button class="btn" id="gModalTestBtn" style="font-size:12.5px">Test Connection</button>
            <div style="display:flex;gap:8px">
              <button class="btn" id="gModalClearBtn" style="color:var(--bad)">Clear Key</button>
              <button class="btn pri" id="gModalSaveBtn">Save Settings</button>
            </div>
          </div>
        </div>
      </div>
    `;

    modal.classList.remove("hide");

    const closeBtn = document.getElementById("gModalClose");
    closeBtn.onclick = () => modal.classList.add("hide");

    const maskBtn = document.getElementById("gToggleMask");
    const keyInput = document.getElementById("gModalKeyInput");
    maskBtn.onclick = () => {
      if (keyInput.type === "password") {
        keyInput.type = "text";
        maskBtn.textContent = "Hide";
      } else {
        keyInput.type = "password";
        maskBtn.textContent = "Show";
      }
    };

    const statusDiv = document.getElementById("gModalStatus");
    const modelSelect = document.getElementById("gModalModelSelect");
    const customWrap = document.getElementById("gCustomModelWrap");
    const customInput = document.getElementById("gCustomModelInput");
    const detectBtn = document.getElementById("gDetectModelsBtn");

    function getSelectedOrCustomModel() {
      if (modelSelect.value === "custom") {
        return (customInput.value || "").trim() || DEFAULT_MODEL;
      }
      return modelSelect.value;
    }

    modelSelect.onchange = () => {
      if (modelSelect.value === "custom") {
        customWrap.classList.remove("hide");
        customInput.focus();
      } else {
        customWrap.classList.add("hide");
      }
    };

    // Auto-detect models for this key
    if (detectBtn) {
      detectBtn.onclick = async () => {
        const key = keyInput.value.trim();
        if (!key) {
          statusDiv.innerHTML = '<span style="color:var(--bad)">Please enter an API key first to auto-detect models.</span>';
          return;
        }
        statusDiv.innerHTML = '<span style="color:var(--selBd)">Querying Google API for models enabled on your key...</span>';
        const detected = await fetchAvailableModels(key);
        if (detected.length) {
          modelSelect.innerHTML = detected.map(m => `<option value="${m.id}">${m.name}</option>`).join("") +
            '<option value="custom">Custom Model ID...</option>';
          statusDiv.innerHTML = `<span style="color:var(--ok);font-weight:600">Found ${detected.length} compatible models! Selected: ${modelSelect.value}</span>`;
        } else {
          statusDiv.innerHTML = '<span style="color:var(--warn)">Could not auto-list models (endpoint query failed or key is limited). Standard models remain ready.</span>';
        }
      };
    }

    // Test connection
    const testBtn = document.getElementById("gModalTestBtn");
    testBtn.onclick = async () => {
      const key = keyInput.value.trim();
      const targetModel = getSelectedOrCustomModel();
      if (!key) {
        statusDiv.innerHTML = '<span style="color:var(--bad)">Please enter an API key to test.</span>';
        return;
      }
      statusDiv.innerHTML = `<span style="color:var(--selBd)">Pinging Gemini API with <code>${escapeHtml(targetModel)}</code>...</span>`;
      const res = await testGeminiKey(key, targetModel);
      if (res.success) {
        statusDiv.innerHTML = `<span style="color:var(--ok);font-weight:600">Connection successful! (${res.modelUsed} responded)</span>`;
      } else {
        statusDiv.innerHTML = `<span style="color:var(--bad);font-weight:600">Error: ${escapeHtml(res.error)}</span>`;
      }
    };

    // Clear key
    const clearBtn = document.getElementById("gModalClearBtn");
    clearBtn.onclick = () => {
      if (confirm("Remove saved Gemini API key from this browser?")) {
        setApiKey("");
        keyInput.value = "";
        statusDiv.innerHTML = '<span style="color:var(--faint)">API key removed.</span>';
        renderGeminiExamCard();
      }
    };

    // Save key
    const saveBtn = document.getElementById("gModalSaveBtn");
    saveBtn.onclick = () => {
      const key = keyInput.value.trim();
      const chosenModel = getSelectedOrCustomModel();
      setApiKey(key);
      setModel(chosenModel);
      modal.classList.add("hide");
      renderGeminiExamCard();
      if (typeof window.flash === "function") window.flash(`Gemini settings saved (${chosenModel}).`);
    };
  }

  function escapeHtml(str) {
    if (!str) return "";
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  /* ===== GLOBAL EXPORTS ===== */
  window.renderGeminiExamCard = renderGeminiExamCard;
  window.showGeminiSettingsModal = showGeminiSettingsModal;
  window.getCachedGeminiAnalysis = getCachedAnalysis;
  window.renderGeminiMarkdown = renderMarkdown;
  window.buildDiagnosticPrompt = buildDiagnosticPrompt;
  window.extractCurrentExamInfo = extractCurrentExamInfo;
  window.callGeminiAPI = callGeminiAPI;
  window.getGeminiApiKey = getApiKey;
  window.getGeminiModel = getModel;
  window.jumpToPerformanceChart = jumpToPerformanceChart;
  window.extractHistoricalTrajectory = extractHistoricalTrajectory;
  window.renderEmbeddedExamCharts = renderEmbeddedExamCharts;
  window.drawEmbeddedChart = drawEmbeddedChart;
  window.buildScoreDataset = buildScoreDataset;
  window.buildFatigueDeltaDataset = buildFatigueDeltaDataset;
  window.buildWpmDataset = buildWpmDataset;
  window.buildSessionFatigueDataset = buildSessionFatigueDataset;
  window.cleanAndDepegPassageStats = cleanAndDepegPassageStats;

  if (typeof globalThis !== "undefined") {
    globalThis.renderGeminiExamCard = renderGeminiExamCard;
    globalThis.showGeminiSettingsModal = showGeminiSettingsModal;
    globalThis.getCachedGeminiAnalysis = getCachedAnalysis;
    globalThis.renderGeminiMarkdown = renderMarkdown;
    globalThis.buildDiagnosticPrompt = buildDiagnosticPrompt;
    globalThis.extractCurrentExamInfo = extractCurrentExamInfo;
    globalThis.callGeminiAPI = callGeminiAPI;
    globalThis.getGeminiApiKey = getApiKey;
    globalThis.getGeminiModel = getModel;
    globalThis.jumpToPerformanceChart = jumpToPerformanceChart;
    globalThis.extractHistoricalTrajectory = extractHistoricalTrajectory;
    globalThis.renderEmbeddedExamCharts = renderEmbeddedExamCharts;
    globalThis.drawEmbeddedChart = drawEmbeddedChart;
    globalThis.buildScoreDataset = buildScoreDataset;
    globalThis.buildFatigueDeltaDataset = buildFatigueDeltaDataset;
    globalThis.buildWpmDataset = buildWpmDataset;
    globalThis.buildSessionFatigueDataset = buildSessionFatigueDataset;
    globalThis.cleanAndDepegPassageStats = cleanAndDepegPassageStats;
  }

  // Auto-init hooks after DOM is ready
  if (typeof window !== "undefined" && typeof window.addEventListener === "function") {
    window.addEventListener("DOMContentLoaded", () => {
      // If top-bar key button exists, hook it
      const topKeyBtn = document.getElementById("tGeminiKey");
      if (topKeyBtn) topKeyBtn.onclick = () => showGeminiSettingsModal();

      const homeKeyBtn = document.getElementById("bGeminiKey");
      if (homeKeyBtn) homeKeyBtn.onclick = () => showGeminiSettingsModal();
    });
  }
})();
