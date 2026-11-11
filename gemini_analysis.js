/* ---- gemini_analysis.js ---- */
/* AI-Powered Post-Exam Diagnostic & Mistake Analysis Engine for DrillRoom.
   Connects to Google Gemini API to analyze question structures, distractor traps,
   confidence calibration, and generate high-yield MCAT improvement prescriptions. */

(function () {
  "use strict";

  const STORAGE_KEY = "drillroom_gemini_api_key";
  const MODEL_KEY = "drillroom_gemini_model";
  const CACHE_PREFIX = "drillroom_ai_analysis_";

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
      return data ? JSON.parse(data) : null;
    } catch (e) {
      return null;
    }
  }

  function saveCachedAnalysis(examId, analysis) {
    if (!examId) return;
    try {
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

  function inlineFormat(text) {
    if (!text) return "";
    return text
      .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
      .replace(/__(.*?)__/g, "<strong>$1</strong>")
      .replace(/\*(.*?)\*/g, "<em>$1</em>")
      .replace(/_(.*?)_/g, "<em>$1</em>")
      .replace(/`([^`]+)`/g, '<code style="background:#EBF0F5;color:#1B3A5C;padding:1px 5px;border-radius:3px;font-family:monospace;font-size:12.5px;font-weight:600">$1</code>');
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
    let pList = [];
    if (Array.isArray(info.passageStats)) {
      pList = info.passageStats;
    } else if (info.passageStats && typeof info.passageStats === "object") {
      pList = Object.values(info.passageStats);
    }

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

Here is the comprehensive log of every question where the student dropped points, spent excessive time, OR experienced uncertainty (guesses and 50/50 coin flips that hide latent weaknesses):

${reviewText}

---

### INSTRUCTIONS:
Generate a thorough, high-impact, and empowering MCAT Diagnostic Report structured with the following exact Markdown headers:

CRITICAL REQUIREMENT: The student wants an immediate, high-yield summary right at the top so they can know their top priorities in under 30 seconds without reading through the full diagnostic.
You MUST begin your response with this exact Executive Summary block:

# Executive Summary: What You Most Need to Work On
(Keep this upfront summary ultra-concise, scannable, and under 150 words total)

> [!IMPORTANT]
> **Priority Focus / #1 Blindspot:** [1 clear, uncompromising sentence pinpointing the specific conceptual gap, distractor trap, or cognitive error that dropped the most points in this section.]
> 
> **Pacing Reality:** [1 clear sentence summarizing their true pacing — citing their net question solving speed of ~${info.avgQSec || 55}s/question and passage reading pace, noting that timing is sound and where to maintain discipline.]
> 
> **#1 Rule for Your Next Section:** [1 punchy, memorable test-taking rule to deploy immediately on their next passage or section.]

### Quick Priority Punch List
- **What Dropped Points:** [1–2 crisp sentences diagnosing the root cause behind their misses/guesses.]
- **What Succeeded:** [1 sentence validating genuine mastery, strong comprehension, and uninflated accuracy.]
- **Immediate Action Item:** [1 specific drill or rule to execute immediately.]

---

# 1. Executive Score Diagnostic & Metacognitive Calibration
- Diagnose their scaled score (${info.scaledScore}/132) against competitive medical school thresholds (500 median, 510 competitive, 515+ top tier).
- Perform a calibration audit:
  * Are they "Confidently Wrong" (committing to misses with high conviction)? Explain why this indicates false mental models rather than memory lapses.
  * Are they "Underconfident" (second-guessing valid scientific intuition)?
  * How much did lucky guesses artificially inflate their raw accuracy?

# 2. Pacing Calibration & Question Archetype Speed Strategy
- Analyze the Question Archetype timing table and passage reading metrics above:
  * Pinpoint exactly which question archetypes consumed excessive time or had poor accuracy.
  * Prescribe 2–3 concrete, tactical heuristics to cut 20–30 seconds per question on those specific archetypes.
  * Analyze passage reading speed (WPM) vs question answering time: is their reading speed causing superficial comprehension or time panic?
  * Second-guessing analysis: based on the answer-change audit, provide rules for when to trust first instinct vs when a switch is justified.
  * Sunk-cost elimination: establish a hard 90-second cutoff rule for stubborn questions.

# 3. AAMC Question Architecture & Distractor Trap Anatomy
Identify the exact structural traps present in the questions they missed or struggled with. Classify errors under these authentic AAMC distractor patterns:
- **True Fact, Wrong Question**: Choices that state scientifically correct facts from the passage or textbook, but fail to directly answer the stem constraint.
- **Opposite Relationship / Directional Inversion**: Inverting mathematical proportionalities, reaction equilibrium shifts (Le Chatelier), or physiological feedback loops.
- **Scope Creep & Extreme Language**: Traps that introduce unproven assumptions or absolute qualifiers ("always", "never", "only").
- **Familiar Buzzword Attractor**: Distractors designed to bait rote associative memory without logical connection.
- **Data & Experimental Misinterpretation**: Errors in reading control baselines, error bars, or confounding variables in tables/figures.
For each category found in their test, cite the specific question number(s) and explain how the AAMC engineered the trap to deceive test-takers.

# 4. High-Yield Content & Mechanistic Remediation
Group their conceptual errors into core scientific or CARS reasoning domains. Explain the underlying physiology, reaction mechanism, physics equation, or CARS argumentation principle with crystal clarity so they master the mechanism permanently.

# 5. Tactical MCAT Test-Taking Techniques to Deploy Immediately
Provide 3 battle-tested, concrete techniques tailored specifically to the flaws seen in this session:
- **The 3-Word Stem Rephrase**: How to reword convoluted stems before looking at answer choices.
- **Process of Elimination (POOE) Heuristics**: How to eliminate 2 wrong choices in under 15 seconds.
- **Passage & Data Interrogation Rule**: How to extract independent/dependent variables and trends from data tables in under 20 seconds without getting bogged down in background text.

# 6. 48-Hour High-Yield Action Plan
Give the student a prioritized checklist of 3–4 ultra-specific topics, equations, or drills to execute over the next 48 hours to claw back 2–3 scaled points on their next section.`;
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

    return {
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
      avgQSec
    };
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
      renderCompletedAnalysis(body, cached.text, cached.modelUsed, info);
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
  function renderCompletedAnalysis(container, markdownText, modelUsed, info) {
    const htmlReport = renderMarkdown(markdownText);

    const chatStorageKey = "drillroom_chat_" + info.examId;
    let chatHistory = [];
    try {
      chatHistory = JSON.parse(localStorage.getItem(chatStorageKey)) || [];
      if (!Array.isArray(chatHistory)) chatHistory = [];
    } catch (e) { chatHistory = []; }

    container.innerHTML = `
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

    const rerunBtn = document.getElementById("gRerunBtn");
    if (rerunBtn) {
      rerunBtn.onclick = () => {
        if (confirm("Re-run Gemini AI analysis on this section?")) {
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

  // Auto-init hooks after DOM is ready
  window.addEventListener("DOMContentLoaded", () => {
    // If top-bar key button exists, hook it
    const topKeyBtn = document.getElementById("tGeminiKey");
    if (topKeyBtn) topKeyBtn.onclick = () => showGeminiSettingsModal();

    const homeKeyBtn = document.getElementById("bGeminiKey");
    if (homeKeyBtn) homeKeyBtn.onclick = () => showGeminiSettingsModal();
  });
})();
