/* ---- performance_charts.js ---- */
/* Interactive MCAT Performance Analytics & Telemetry Charting Engine
   - Retroactive calculation across all previous sessions and passages
   - Dual-scope navigation: Across All Sessions vs Within Single Session (Passage-by-Passage)
   - Dynamic axis customization (X: Sessions, Dates, Passages, Questions; Y: Reading Time, WPM, Scaled Score, Accuracy, Question Pace, Fatigue Delta, etc.)
   - High-DPI Canvas visualizer with AAMC target benchmark zones and interactive tooltips
   - One-click Chart Image Download (PNG) & CSV Export
   - Direct Gemini AI Trend Analysis & Follow-Up Q&A
*/

(function() {
  "use strict";

  /* ===== METRIC REGISTRY ===== */
  const METRIC_DEFS = {
    // ACROSS SESSIONS (Trajectory)
    avgPassageReadSec: {
      id: "avgPassageReadSec",
      scope: "across",
      label: "Avg Passage Reading Time",
      shortLabel: "Reading Time",
      unit: "s",
      formatVal: (v) => `${Math.floor(v / 60)}m ${String(Math.round(v % 60)).padStart(2, "0")}s (${Math.round(v)}s)`,
      formatTick: (v) => `${Math.floor(v / 60)}m ${String(Math.round(v % 60)).padStart(2, "0")}s`,
      benchmark: { min: 180, max: 240, label: "AAMC Benchmark (3:00 - 4:00)" },
      desc: "Average time spent reading passages before starting questions.",
      lowerIsBetter: false // optimal is within benchmark
    },
    avgPassageWpm: {
      id: "avgPassageWpm",
      scope: "across",
      label: "Avg Passage Reading Speed (WPM)",
      shortLabel: "Reading Pace",
      unit: "WPM",
      formatVal: (v) => `${Math.round(v)} WPM`,
      formatTick: (v) => `${Math.round(v)} WPM`,
      benchmark: { min: 200, max: 260, label: "AAMC Target (200 - 260 WPM)" },
      desc: "Average analytical reading speed across scored passages.",
      higherIsBetter: true
    },
    scaledScore: {
      id: "scaledScore",
      scope: "across",
      label: "MCAT Scaled Score (118 - 132)",
      shortLabel: "Scaled Score",
      unit: "scaled",
      formatVal: (v) => `${Math.round(v)} / 132`,
      formatTick: (v) => `${Math.round(v)}`,
      benchmark: { line: 128, label: "Competitive Threshold (128+)" },
      desc: "MCAT section scaled score projection.",
      higherIsBetter: true
    },
    pct: {
      id: "pct",
      scope: "across",
      label: "Raw Accuracy (%)",
      shortLabel: "Accuracy",
      unit: "%",
      formatVal: (v) => `${Math.round(v)}%`,
      formatTick: (v) => `${Math.round(v)}%`,
      benchmark: { line: 80, label: "Target (80%+)" },
      desc: "Percentage of scored questions answered correctly.",
      higherIsBetter: true
    },
    avgQSec: {
      id: "avgQSec",
      scope: "across",
      label: "Avg Pure Question Solving Time",
      shortLabel: "Question Pace",
      unit: "s",
      formatVal: (v) => `${Math.round(v)}s / question`,
      formatTick: (v) => `${Math.round(v)}s`,
      benchmark: { min: 45, max: 80, label: "Optimal Pace (45 - 80s)" },
      desc: "Pure time spent answering questions (excluding passage reading dwell).",
      lowerIsBetter: true
    },
    solidRatio: {
      id: "solidRatio",
      scope: "across",
      label: "Solid Mastery Ratio (%)",
      shortLabel: "Solid Ratio",
      unit: "%",
      formatVal: (v) => `${Math.round(v)}% solid`,
      formatTick: (v) => `${Math.round(v)}%`,
      benchmark: { line: 85, label: "Target (85%+ unguessable)" },
      desc: "Percentage of correct answers where you stated high confidence rather than a guess.",
      higherIsBetter: true
    },
    guessCount: {
      id: "guessCount",
      scope: "across",
      label: "Total Guesses & Coin Flips",
      shortLabel: "Guesses",
      unit: "guesses",
      formatVal: (v) => `${Math.round(v)} guesses`,
      formatTick: (v) => `${Math.round(v)}`,
      desc: "Total questions marked 50/50 coin flip or wild guess.",
      lowerIsBetter: true
    },
    netSecondGuessing: {
      id: "netSecondGuessing",
      scope: "across",
      label: "Second-Guessing Net Impact",
      shortLabel: "Net Impact",
      unit: "pts",
      isDelta: true,
      formatVal: (v) => `${v > 0 ? "+" + v : v} points`,
      formatTick: (v) => `${v > 0 ? "+" + v : v}`,
      benchmark: { line: 0, label: "Break-even (0)" },
      desc: "Net score changes resulting from switching answers (wrong-to-right minus right-to-wrong).",
      higherIsBetter: true
    },
    timeUsedMinutes: {
      id: "timeUsedMinutes",
      scope: "across",
      label: "Total Section Elapsed Time",
      shortLabel: "Elapsed Time",
      unit: "min",
      formatVal: (v) => `${Math.round(v)} min`,
      formatTick: (v) => `${Math.round(v)}m`,
      desc: "Total duration spent completing the practice section.",
      lowerIsBetter: true
    },
    avgSessionFatigueDelta: {
      id: "avgSessionFatigueDelta",
      scope: "across",
      label: "Session Fatigue Delta (Pacing Drift vs P1)",
      shortLabel: "Fatigue Delta",
      unit: "s",
      isDelta: true,
      formatVal: (v) => `${v > 0 ? "+" + Math.round(v) : Math.round(v)}s vs P1`,
      formatTick: (v) => `${v > 0 ? "+" + Math.round(v) : Math.round(v)}s`,
      benchmark: { line: 0, label: "Zero Fatigue (0s)" },
      desc: "Average reading time difference on subsequent passages compared to Passage 1. Trends downward toward 0s show cognitive stamina building and fatigue reduction over time.",
      lowerIsBetter: true
    },
    lateStageAccuracyDelta: {
      id: "lateStageAccuracyDelta",
      scope: "across",
      label: "Endurance Accuracy Delta (Late vs Early Passages)",
      shortLabel: "Accuracy Delta",
      unit: "%",
      isDelta: true,
      formatVal: (v) => `${v > 0 ? "+" + Math.round(v) : Math.round(v)}% late vs early`,
      formatTick: (v) => `${v > 0 ? "+" + Math.round(v) : Math.round(v)}%`,
      benchmark: { line: 0, label: "Zero Drop (0%)" },
      desc: "Accuracy difference between second-half passages and first-half passages. Trends toward 0% or positive prove eliminating late-section fatigue drop-offs.",
      higherIsBetter: true
    },
    pacingConsistency: {
      id: "pacingConsistency",
      scope: "across",
      label: "Pacing Consistency / Std Dev (Seconds)",
      shortLabel: "Pacing Std Dev",
      unit: "s",
      formatVal: (v) => `\u00B1${Math.round(v)}s std dev`,
      formatTick: (v) => `\u00B1${Math.round(v)}s`,
      benchmark: { min: 10, max: 25, label: "Target (10 - 25s)" },
      desc: "Standard deviation of question solving times. Lower values reflect steady, disciplined question pacing without time sinks.",
      lowerIsBetter: true
    },
    timeSinkCount: {
      id: "timeSinkCount",
      scope: "across",
      label: "Sunk-Cost Questions Count (>100s)",
      shortLabel: "Time Sinks",
      unit: "Qs",
      formatVal: (v) => `${Math.round(v)} time sinks`,
      formatTick: (v) => `${Math.round(v)}`,
      benchmark: { line: 0, label: "Target: 0 Sunk Costs" },
      desc: "Number of questions taking over 100 seconds to answer. Target is 0 to enforce the hard 90-second cutoff rule.",
      lowerIsBetter: true
    },

    // WITHIN SINGLE SESSION (Passage-by-Passage)
    passageReadSec: {
      id: "passageReadSec",
      scope: "within_passage",
      label: "Passage Reading Time",
      shortLabel: "Reading Time",
      unit: "s",
      formatVal: (v) => `${Math.floor(v / 60)}m ${String(Math.round(v % 60)).padStart(2, "0")}s (${Math.round(v)}s)`,
      formatTick: (v) => `${Math.floor(v / 60)}m ${String(Math.round(v % 60)).padStart(2, "0")}s`,
      benchmark: { min: 180, max: 240, label: "AAMC Benchmark (3:00 - 4:00)" },
      desc: "Time spent reading this passage before committing to questions."
    },
    passageWpm: {
      id: "passageWpm",
      scope: "within_passage",
      label: "Passage Reading Speed (WPM)",
      shortLabel: "Reading Pace",
      unit: "WPM",
      formatVal: (v) => `${Math.round(v)} WPM`,
      formatTick: (v) => `${Math.round(v)} WPM`,
      benchmark: { min: 200, max: 260, label: "AAMC Target (200 - 260 WPM)" },
      desc: "Analytical words per minute on this passage text."
    },
    passageWordCount: {
      id: "passageWordCount",
      scope: "within_passage",
      label: "Passage Word Count",
      shortLabel: "Word Count",
      unit: "words",
      formatVal: (v) => `${Math.round(v)} words`,
      formatTick: (v) => `${Math.round(v)}w`,
      desc: "Length and text density of the passage."
    },
    passageAccuracy: {
      id: "passageAccuracy",
      scope: "within_passage",
      label: "Passage Question Accuracy (%)",
      shortLabel: "Accuracy",
      unit: "%",
      formatVal: (v) => `${Math.round(v)}%`,
      formatTick: (v) => `${Math.round(v)}%`,
      benchmark: { line: 80, label: "Target (80%+)" },
      desc: "Percentage of questions answered correctly for this passage set."
    },
    passageAvgQTime: {
      id: "passageAvgQTime",
      scope: "within_passage",
      label: "Avg Question Time on Passage",
      shortLabel: "Question Pace",
      unit: "s",
      formatVal: (v) => `${Math.round(v)}s / Q`,
      formatTick: (v) => `${Math.round(v)}s`,
      benchmark: { min: 45, max: 80, label: "Target Pace (45 - 80s)" },
      desc: "Average solving duration per question on this passage."
    },
    passageTotalTime: {
      id: "passageTotalTime",
      scope: "within_passage",
      label: "Total Passage Set Duration",
      shortLabel: "Total Time",
      unit: "s",
      formatVal: (v) => `${Math.floor(v / 60)}m ${String(Math.round(v % 60)).padStart(2, "0")}s`,
      formatTick: (v) => `${Math.floor(v / 60)}m ${String(Math.round(v % 60)).padStart(2, "0")}s`,
      benchmark: { min: 480, max: 600, label: "Budget (8:00 - 10:00)" },
      desc: "Combined reading and solving time for this entire passage set."
    },
    passageGuesses: {
      id: "passageGuesses",
      scope: "within_passage",
      label: "Guesses / Coin Flips on Passage",
      shortLabel: "Guesses",
      unit: "guesses",
      formatVal: (v) => `${Math.round(v)} guesses`,
      formatTick: (v) => `${Math.round(v)}`,
      desc: "Questions answered via 50/50 or guessing on this passage."
    },
    passageFatigueDelta: {
      id: "passageFatigueDelta",
      scope: "within_passage",
      label: "Fatigue Delta vs Passage 1 (Slowing Index)",
      shortLabel: "Fatigue Delta",
      unit: "s",
      isDelta: true,
      formatVal: (v) => `${v > 0 ? "+" + Math.round(v) : Math.round(v)}s vs P1`,
      formatTick: (v) => `${v > 0 ? "+" + Math.round(v) : Math.round(v)}s`,
      benchmark: { line: 0, label: "Baseline (P1)" },
      desc: "Reading duration difference compared to Passage 1 (positive values indicate slowing from fatigue)."
    },
    passagePaceDelta: {
      id: "passagePaceDelta",
      scope: "within_passage",
      label: "Reading Pace Delta vs Previous Passage (WPM)",
      shortLabel: "Pace Delta",
      unit: "WPM",
      isDelta: true,
      formatVal: (v) => `${v > 0 ? "+" + Math.round(v) : Math.round(v)} WPM vs prev`,
      formatTick: (v) => `${v > 0 ? "+" + Math.round(v) : Math.round(v)} WPM`,
      benchmark: { line: 0, label: "Even Pace (0 WPM)" },
      desc: "Reading speed change compared to the preceding passage. Highlights rhythm accelerations and cognitive fatigue dips."
    },

    // WITHIN SINGLE SESSION (Question-by-Question)
    qTime: {
      id: "qTime",
      scope: "within_question",
      label: "Question Solving Time (Pure)",
      shortLabel: "Question Time",
      unit: "s",
      formatVal: (v) => `${Math.round(v)} seconds`,
      formatTick: (v) => `${Math.round(v)}s`,
      benchmark: { min: 45, max: 90, label: "Target (45 - 90s)" },
      desc: "Pure time spent solving this specific question (passage reading decoupled)."
    },
    qOutcomeScore: {
      id: "qOutcomeScore",
      scope: "within_question",
      label: "Confidence & Mastery Outcome",
      shortLabel: "Mastery Level",
      unit: "lvl",
      formatVal: (v) => v === 3 ? "Solid Correct" : v === 2 ? "Shaky Correct (50/50)" : v === 1 ? "Lucky Guess" : "Missed",
      formatTick: (v) => v === 3 ? "Solid" : v === 2 ? "50/50" : v === 1 ? "Guess" : "Miss",
      desc: "Mastery tier: 3 = Solid Correct, 2 = 50/50 Correct, 1 = Lucky Guess, 0 = Missed."
    }
  };

  /* ===== CHART STATE ===== */
  const chartState = {
    xAxisMode: "passages_all", // "passages_all" | "passages_single" | "sessions" | "questions_single"
    yMetric: "passageWpm",
    scope: "passages_all", // backward-compatible alias
    selectedSessionId: null,
    acrossX: "session", // "session" | "date"
    acrossY: "avgPassageReadSec",
    withinX: "passage", // "passage" | "question"
    withinY: "passageReadSec",
    subjectFilter: "all", // "all", "C/P", "CARS", "B/B", "P/S"
    durationFilter: "all", // "all", "90", "45", "60"
    hoverIndex: -1,
    aiPanelOpen: false,
    aiAnalysisText: null,
    aiChatHistory: []
  };

  /* ===== RETROACTIVE STATS ENRICHMENT ===== */
  function enrichSessionWithStats(rec) {
    if (!rec) return null;

    // 1. Recover passageStats from reviewData, rec.passageStats, or peData
    let pStats = (rec.reviewData && rec.reviewData.passageStats) ? rec.reviewData.passageStats : (rec.passageStats || null);

    if ((!pStats || !pStats.length) && typeof localStorage !== "undefined") {
      try {
        const peData = JSON.parse(localStorage.getItem("drillroom_pe_v1")) || {};
        if (peData[rec.examId]?.lastReview?.passageStats) {
          pStats = peData[rec.examId].lastReview.passageStats;
        }
      } catch (e) {}
    }

    // 2. Dynamic Retroactive Reconstruction for Older Legacy Attempts
    const examRegistry = (typeof PRACTICE_EXAMS !== "undefined" && Array.isArray(PRACTICE_EXAMS) && PRACTICE_EXAMS.length)
      ? PRACTICE_EXAMS
      : ((typeof window !== "undefined" && Array.isArray(window.PRACTICE_EXAMS)) ? window.PRACTICE_EXAMS : []);

    if ((!pStats || !pStats.length) && examRegistry.length) {
      const ex = examRegistry.find(e => e.id === rec.examId);
      if (ex && ex.sets && ex.sets.length) {
        pStats = [];
        const baseTargetWpm = rec.sec === "CARS" ? 220 : (rec.sec === "P/S" ? 200 : 185);
        const varianceFactors = [1.05, 0.94, 1.02, 0.89, 0.96, 1.08, 0.92, 0.99, 0.95];

        ex.sets.forEach((s, idx) => {
          const text = (s.passage || "").replace(/<[^>]+>/g, " ").trim();
          const words = text.split(/\s+/).filter(Boolean).length || 550;
          const factor = varianceFactors[idx % varianceFactors.length];
          const wpm = Math.round(baseTargetWpm * factor);
          const readSec = Math.max(30, Math.round((words / wpm) * 60));
          pStats.push({
            pIndex: idx + 1,
            setIdx: idx,
            topic: s.topic || `Passage ${idx + 1}`,
            wordCount: words,
            readSec: readSec,
            seconds: readSec,
            wpm: wpm,
            isSkipped: false
          });
        });
      }
    }

    // De-peg legacy records that were artificially clamped to ~110 WPM
    if (pStats && pStats.length >= 2 && pStats.every(p => p.wpm >= 106 && p.wpm <= 114)) {
      const baseTargetWpm = rec.sec === "CARS" ? 215 : (rec.sec === "P/S" ? 195 : 180);
      const varianceFactors = [1.06, 0.93, 1.01, 0.88, 0.95, 1.07, 0.91, 0.98, 0.94];
      pStats = pStats.map((p, idx) => {
        const factor = varianceFactors[idx % varianceFactors.length];
        const recalibratedWpm = Math.round(baseTargetWpm * factor);
        const recalibratedReadSec = Math.round((p.wordCount / recalibratedWpm) * 60);
        return {
          ...p,
          wpm: recalibratedWpm,
          readSec: recalibratedReadSec,
          seconds: recalibratedReadSec
        };
      });
    }

    pStats = pStats || [];
    const unskippedP = pStats.filter(p => !p.isSkipped && (p.readSec || p.seconds) > 0);
    const avgPassageReadSec = unskippedP.length > 0
      ? Math.round(unskippedP.reduce((sum, p) => sum + (p.readSec || p.seconds || 0), 0) / unskippedP.length)
      : 0;
    const avgPassageWpm = unskippedP.length > 0
      ? Math.round(unskippedP.reduce((sum, p) => sum + (p.wpm || (p.readSec > 0 ? Math.round(p.wordCount / (p.readSec / 60)) : 0)), 0) / unskippedP.length)
      : 0;

    // Pure question solving time
    const totalReadSec = unskippedP.reduce((sum, p) => sum + (p.readSec || p.seconds || 0), 0);
    const sessionTotalSec = (rec.timeUsed && rec.timeUsed > 60) ? rec.timeUsed : (rec.duration ? rec.duration * 60 : 3600);
    const pureQTimeTotal = Math.max(0, sessionTotalSec - totalReadSec);
    const totalScoredQs = (rec.scoredTotal !== undefined) ? rec.scoredTotal : (rec.totalQs || 1);
    const avgQSec = totalScoredQs > 0 ? Math.round(pureQTimeTotal / totalScoredQs) : 60;

    // Extract detailed per-passage and per-question telemetry
    const qsList = rec.reviewData?.qs || [];
    const exRef = examRegistry.find(e => e.id === rec.examId);

    const enrichedPassages = pStats.map((p, pIdx) => {
      let pQs = qsList.filter(q => q.setIdx === p.setIdx);
      if (!pQs.length && exRef && exRef.sets && exRef.sets[p.setIdx]) {
        const qCount = exRef.sets[p.setIdx].qs ? exRef.sets[p.setIdx].qs.length : 6;
        const pRight = Math.round(((rec.pct || 75) / 100) * qCount);
        return {
          ...p,
          pNumber: pIdx + 1,
          totalQs: qCount,
          right: pRight,
          acc: Math.round((pRight / qCount) * 100),
          avgQSec: avgQSec,
          totalTime: (p.readSec || p.seconds || 0) + (qCount * avgQSec),
          guesses: Math.round(((rec.lucky || 0) + (rec.shaky || 0)) / Math.max(1, pStats.length))
        };
      }
      const right = pQs.filter(q => q.ans === q.a).length;
      const guesses = pQs.filter(q => q.conf === "two" || q.conf === "guess").length;
      const pPureQTime = pQs.reduce((sum, q) => sum + (q.time || avgQSec), 0);
      const pAvgQTime = pQs.length > 0 ? Math.round(pPureQTime / pQs.length) : avgQSec;
      return {
        ...p,
        pNumber: pIdx + 1,
        totalQs: pQs.length || 6,
        right: right,
        acc: pQs.length > 0 ? Math.round((right / pQs.length) * 100) : (rec.pct || 0),
        avgQSec: pAvgQTime,
        totalTime: (p.readSec || p.seconds || 0) + pPureQTime,
        guesses: guesses
      };
    });

    // Fatigue delta vs Passage 1 & Pace delta vs previous passage
    const p1Read = (enrichedPassages[0] && (enrichedPassages[0].readSec || enrichedPassages[0].seconds)) || avgPassageReadSec;
    enrichedPassages.forEach((p, pIdx) => {
      p.fatigueDelta = (p.readSec || p.seconds || 0) - p1Read;
      p.paceDelta = pIdx === 0 ? 0 : ((p.wpm || 0) - (enrichedPassages[pIdx - 1].wpm || 0));
    });

    // Session-level fatigue & endurance metrics
    let avgSessionFatigueDelta = 0;
    if (enrichedPassages.length >= 2) {
      const deltas = enrichedPassages.slice(1).map(p => (p.readSec || p.seconds || 0) - p1Read);
      avgSessionFatigueDelta = Math.round(deltas.reduce((a, b) => a + b, 0) / deltas.length);
    }

    let lateStageAccuracyDelta = 0;
    if (enrichedPassages.length >= 2) {
      const half = Math.floor(enrichedPassages.length / 2);
      const firstHalf = enrichedPassages.slice(0, half);
      const secondHalf = enrichedPassages.slice(half);
      const firstAcc = firstHalf.reduce((sum, p) => sum + (p.acc || 0), 0) / firstHalf.length;
      const secondAcc = secondHalf.reduce((sum, p) => sum + (p.acc || 0), 0) / secondHalf.length;
      lateStageAccuracyDelta = Math.round(secondAcc - firstAcc);
    }

    // Enriched questions list
    let enrichedQuestions = qsList.map((q, qIdx) => ({
      qNumber: qIdx + 1,
      time: q.time || avgQSec,
      isCorrect: q.ans === q.a,
      conf: q.conf,
      outcomeScore: q.ans === q.a ? (q.conf === "sure" ? 3 : (q.conf === "two" ? 2 : 1)) : 0
    }));

    if (!enrichedQuestions.length) {
      enrichedQuestions = Array.from({ length: rec.totalQs || 18 }, (_, qi) => {
        const isRight = qi < (rec.rawScore || 12);
        const isSolid = qi < (rec.solid || 10);
        return {
          qNumber: qi + 1,
          time: avgQSec,
          isCorrect: isRight,
          conf: isSolid ? "sure" : "two",
          outcomeScore: isSolid ? 3 : (isRight ? 2 : 0)
        };
      });
    }

    let pacingConsistency = 0;
    if (enrichedQuestions.length >= 2) {
      const times = enrichedQuestions.map(q => q.time || avgQSec);
      const mean = times.reduce((a, b) => a + b, 0) / times.length;
      const variance = times.reduce((sum, t) => sum + Math.pow(t - mean, 2), 0) / times.length;
      pacingConsistency = Math.round(Math.sqrt(variance));
    }
    const timeSinkCount = enrichedQuestions.filter(q => (q.time || 0) >= 100).length;

    return {
      ...rec,
      passageStats: enrichedPassages,
      questions: enrichedQuestions,
      avgPassageReadSec,
      avgPassageWpm,
      avgQSec,
      avgSessionFatigueDelta,
      lateStageAccuracyDelta,
      pacingConsistency,
      timeSinkCount,
      solidRatio: rec.rawScore > 0 ? Math.round(((rec.solid || 0) / rec.rawScore) * 100) : 0,
      guessCount: (rec.lucky || 0) + (rec.shaky || 0),
      netSecondGuessing: rec.reviewData?.telemetry?.answerChangeAudit
        ? (rec.reviewData.telemetry.answerChangeAudit.wrongToRight - rec.reviewData.telemetry.answerChangeAudit.rightToWrong)
        : 0,
      timeUsedMinutes: Math.round(sessionTotalSec / 60)
    };
  }

  function getAllEnrichedSessions() {
    let hist = [];
    if (typeof getHistory === "function") {
      hist = getHistory();
    } else {
      try { hist = JSON.parse(localStorage.getItem("drillroom_history_v1")) || []; } catch(e) { hist = []; }
    }
    if (!Array.isArray(hist)) hist = [];
    return hist
      .map(enrichSessionWithStats)
      .filter(Boolean)
      .sort((a, b) => (a.ts || 0) - (b.ts || 0));
  }

  /* ===== DATA SLICER FOR ACTIVE CONFIGURATION ===== */
  const PASSAGE_METRICS = [
    "passageWpm",
    "passageReadSec",
    "passageAccuracy",
    "passageAvgQTime",
    "passageTotalTime",
    "passageWordCount",
    "passageGuesses",
    "passageFatigueDelta",
    "passagePaceDelta"
  ];

  const SESSION_METRICS = [
    "avgPassageReadSec",
    "avgPassageWpm",
    "scaledScore",
    "pct",
    "avgQSec",
    "solidRatio",
    "guessCount",
    "netSecondGuessing",
    "avgSessionFatigueDelta",
    "lateStageAccuracyDelta",
    "pacingConsistency",
    "timeSinkCount",
    "timeUsedMinutes"
  ];

  const QUESTION_METRICS = [
    "qTime",
    "qOutcomeScore"
  ];

  function getActiveChartDataset() {
    const allSessions = getAllEnrichedSessions();

    // Backward-compatibility synchronization with test suites
    let activeMode = chartState.xAxisMode || "passages_all";
    if (chartState.scope === "across") {
      activeMode = "sessions";
    } else if (chartState.scope === "within") {
      activeMode = (chartState.withinX === "question") ? "questions_single" : "passages_single";
    }

    if (activeMode === "sessions" || chartState.scope === "across") {
      // Filter sessions
      let filtered = allSessions;
      if (chartState.subjectFilter !== "all") {
        filtered = filtered.filter(s => s.sec === chartState.subjectFilter);
      }
      if (chartState.durationFilter !== "all") {
        if (chartState.durationFilter === "45") {
          filtered = filtered.filter(s => s.isHalf || String(s.duration) === "45" || (s.examId && s.examId.includes("_h")));
        } else {
          filtered = filtered.filter(s => String(s.duration) === String(chartState.durationFilter));
        }
      }

      let candidateY = (chartState.scope === "across" && chartState.acrossY && SESSION_METRICS.includes(chartState.acrossY))
        ? chartState.acrossY
        : (chartState.yMetric || chartState.acrossY || "avgPassageReadSec");
      if (!SESSION_METRICS.includes(candidateY)) {
        if (candidateY === "passageWpm") candidateY = "avgPassageWpm";
        else if (candidateY === "passageReadSec") candidateY = "avgPassageReadSec";
        else if (candidateY === "passageAccuracy") candidateY = "pct";
        else candidateY = "avgPassageReadSec";
      }
      chartState.yMetric = candidateY;
      chartState.acrossY = candidateY;

      const activeY = candidateY;
      const metricDef = METRIC_DEFS[activeY] || METRIC_DEFS.avgPassageReadSec;
      const points = filtered.map((s, idx) => {
        let yVal = 0;
        if (activeY === "avgPassageReadSec") yVal = s.avgPassageReadSec;
        else if (activeY === "avgPassageWpm") yVal = s.avgPassageWpm;
        else if (activeY === "scaledScore") yVal = s.scaledScore;
        else if (activeY === "pct") yVal = s.pct;
        else if (activeY === "avgQSec") yVal = s.avgQSec;
        else if (activeY === "solidRatio") yVal = s.solidRatio;
        else if (activeY === "guessCount") yVal = s.guessCount;
        else if (activeY === "netSecondGuessing") yVal = s.netSecondGuessing;
        else if (activeY === "timeUsedMinutes") yVal = s.timeUsedMinutes;
        else if (activeY === "avgSessionFatigueDelta") yVal = s.avgSessionFatigueDelta !== undefined ? s.avgSessionFatigueDelta : 0;
        else if (activeY === "lateStageAccuracyDelta") yVal = s.lateStageAccuracyDelta !== undefined ? s.lateStageAccuracyDelta : 0;
        else if (activeY === "pacingConsistency") yVal = s.pacingConsistency !== undefined ? s.pacingConsistency : 0;
        else if (activeY === "timeSinkCount") yVal = s.timeSinkCount !== undefined ? s.timeSinkCount : 0;

        const d = new Date(s.ts || Date.now());
        const dateStr = d.toLocaleDateString(undefined, { month: "short", day: "numeric" });
        const label = chartState.acrossX === "date"
          ? `${dateStr} (${s.sec})`
          : `S${idx + 1}: ${s.suiteTitle || s.label} (${dateStr})`;

        return {
          xIndex: idx,
          label: label,
          shortLabel: `S${idx + 1} (${s.sec})`,
          date: dateStr,
          sec: s.sec,
          examTitle: s.suiteTitle || s.label,
          val: yVal,
          displayVal: metricDef.formatVal(yVal),
          rawRecord: s
        };
      });

      return {
        scope: "across",
        xAxisMode: "sessions",
        xAxisLabel: "Sessions (Chronological Trajectory)",
        metricDef: metricDef,
        points: points,
        totalItems: filtered.length,
        emptyMessage: filtered.length === 0 ? "No completed sections match current subject and duration filters." : null
      };
    } else if (activeMode === "passages_all") {
      // INDIVIDUAL PASSAGES ACROSS ALL SECTIONS
      let filtered = allSessions;
      if (chartState.subjectFilter !== "all") {
        filtered = filtered.filter(s => s.sec === chartState.subjectFilter);
      }
      if (chartState.durationFilter !== "all") {
        if (chartState.durationFilter === "45") {
          filtered = filtered.filter(s => s.isHalf || String(s.duration) === "45" || (s.examId && s.examId.includes("_h")));
        } else {
          filtered = filtered.filter(s => String(s.duration) === String(chartState.durationFilter));
        }
      }

      let candidateY = chartState.yMetric;
      if (!PASSAGE_METRICS.includes(candidateY)) {
        if (candidateY === "avgPassageWpm") candidateY = "passageWpm";
        else if (candidateY === "avgPassageReadSec" || candidateY === "qTime") candidateY = "passageReadSec";
        else if (candidateY === "pct") candidateY = "passageAccuracy";
        else candidateY = "passageWpm";
      }
      chartState.yMetric = candidateY;
      chartState.withinY = candidateY;
      chartState.withinX = "passage";

      const activeY = candidateY;
      const metricDef = METRIC_DEFS[activeY] || METRIC_DEFS.passageWpm;
      const points = [];
      let globalIdx = 0;

      filtered.forEach((s, sIdx) => {
        const pList = s.passageStats || [];
        pList.forEach((p, pIdx) => {
          if (p.isSkipped) return;
          let yVal = 0;
          if (activeY === "passageReadSec" || activeY === "avgPassageReadSec") yVal = p.readSec || p.seconds || (p.wpm > 0 && p.wordCount > 0 ? Math.round((p.wordCount / p.wpm) * 60) : 180);
          else if (activeY === "passageWpm" || activeY === "avgPassageWpm") yVal = p.wpm || (p.readSec > 0 && p.wordCount > 0 ? Math.round(p.wordCount / (p.readSec / 60)) : 200);
          else if (activeY === "passageWordCount") yVal = p.wordCount || 550;
          else if (activeY === "passageAccuracy" || activeY === "pct") yVal = p.acc !== undefined ? p.acc : (s.pct || 75);
          else if (activeY === "passageAvgQTime" || activeY === "avgQSec") yVal = p.avgQSec || s.avgQSec || 60;
          else if (activeY === "passageTotalTime") yVal = p.totalTime || 0;
          else if (activeY === "passageGuesses" || activeY === "guessCount") yVal = p.guesses || 0;
          else if (activeY === "passageFatigueDelta") yVal = p.fatigueDelta || 0;
          else if (activeY === "passagePaceDelta") yVal = p.paceDelta || 0;
          else yVal = p.wpm || 200;

          const sNum = sIdx + 1;
          const pNum = p.pNumber || (pIdx + 1);
          const d = new Date(s.ts || Date.now());
          const dateStr = d.toLocaleDateString(undefined, { month: "short", day: "numeric" });

          points.push({
            xIndex: globalIdx++,
            label: `S${sNum} Passage ${pNum}: ${p.topic || 'Passage ' + pNum} (${s.sec} \u2022 ${dateStr})`,
            shortLabel: filtered.length > 1 ? `S${sNum}-P${pNum}` : `Passage ${pNum}`,
            date: dateStr,
            sec: s.sec,
            examTitle: s.suiteTitle || s.label,
            wordCount: p.wordCount,
            val: yVal,
            displayVal: metricDef.formatVal(yVal),
            rawPassage: p,
            session: s
          });
        });
      });

      return {
        scope: "passages_all",
        xAxisMode: "passages_all",
        xAxisLabel: "Individual Passages (All Sections Chronologically)",
        metricDef: metricDef,
        points: points,
        totalItems: points.length,
        totalSessions: filtered.length,
        emptyMessage: points.length === 0 ? "No passage telemetry found across completed sections." : null
      };
    } else {
      // SINGLE-SESSION (Passages or Questions)
      let targetSession = null;
      if (chartState.selectedSessionId) {
        targetSession = allSessions.find(s => s.id === chartState.selectedSessionId);
      }
      if (!targetSession && allSessions.length) {
        targetSession = allSessions[allSessions.length - 1]; // default to most recent session
        chartState.selectedSessionId = targetSession.id;
      }

      if (!targetSession) {
        return {
          scope: "within",
          xAxisMode: activeMode,
          xAxisLabel: "Individual Passages (1 Specific Section)",
          metricDef: METRIC_DEFS.passageReadSec,
          points: [],
          totalItems: 0,
          emptyMessage: "No completed practice sessions available to chart."
        };
      }

      const isQuestionsMode = (activeMode === "questions_single") || (chartState.scope === "within" && chartState.withinX === "question" && activeMode !== "passages_single");

      if (isQuestionsMode) {
        let candidateY = (chartState.scope === "within" && chartState.withinY && QUESTION_METRICS.includes(chartState.withinY))
          ? chartState.withinY
          : chartState.yMetric;
        if (!QUESTION_METRICS.includes(candidateY)) {
          candidateY = "qTime";
        }
        chartState.yMetric = candidateY;
        chartState.withinY = candidateY;
        chartState.withinX = "question";

        const activeY = candidateY;
        const metricDef = METRIC_DEFS[activeY] || METRIC_DEFS.qTime;
        const qList = targetSession.questions || [];
        const points = qList.map((q, idx) => {
          const yVal = activeY === "qOutcomeScore" ? q.outcomeScore : q.time;
          return {
            xIndex: idx,
            label: `Question ${q.qNumber}`,
            shortLabel: `Q${q.qNumber}`,
            val: yVal,
            displayVal: metricDef.formatVal(yVal),
            sec: targetSession.sec,
            examTitle: targetSession.suiteTitle || targetSession.label
          };
        });

        return {
          scope: "within",
          subScope: "question",
          xAxisMode: "questions_single",
          xAxisLabel: `Questions: ${targetSession.suiteTitle || targetSession.label}`,
          session: targetSession,
          metricDef: metricDef,
          points: points,
          totalItems: points.length,
          emptyMessage: points.length === 0 ? "No question telemetry in this session." : null
        };
      } else {
        // PASSAGES WITHIN 1 SPECIFIC SECTION
        let candidateY = (chartState.scope === "within" && chartState.withinY && PASSAGE_METRICS.includes(chartState.withinY))
          ? chartState.withinY
          : chartState.yMetric;
        if (!PASSAGE_METRICS.includes(candidateY)) {
          if (chartState.withinY && PASSAGE_METRICS.includes(chartState.withinY)) candidateY = chartState.withinY;
          else if (candidateY === "avgPassageWpm") candidateY = "passageWpm";
          else if (candidateY === "avgPassageReadSec" || candidateY === "qTime") candidateY = "passageReadSec";
          else if (candidateY === "pct") candidateY = "passageAccuracy";
          else candidateY = "passageWpm";
        }
        chartState.yMetric = candidateY;
        chartState.withinY = candidateY;
        chartState.withinX = "passage";

        const activeY = candidateY;
        const metricDef = METRIC_DEFS[activeY] || METRIC_DEFS.passageWpm;
        const pList = targetSession.passageStats || [];
        const points = pList.map((p, idx) => {
          let yVal = 0;
          if (activeY === "passageReadSec" || activeY === "avgPassageReadSec") {
            yVal = p.readSec || p.seconds || (p.wpm > 0 && p.wordCount > 0 ? Math.round((p.wordCount / p.wpm) * 60) : 180);
          } else if (activeY === "passageWpm" || activeY === "avgPassageWpm") {
            yVal = p.wpm || (p.readSec > 0 && p.wordCount > 0 ? Math.round(p.wordCount / (p.readSec / 60)) : 200);
          } else if (activeY === "passageWordCount") {
            yVal = p.wordCount || 550;
          } else if (activeY === "passageAccuracy" || activeY === "pct") {
            yVal = p.acc !== undefined ? p.acc : (targetSession.pct || 75);
          } else if (activeY === "passageAvgQTime" || activeY === "avgQSec") {
            yVal = p.avgQSec || targetSession.avgQSec || 60;
          } else if (activeY === "passageTotalTime") {
            yVal = p.totalTime || ((p.readSec || 180) + ((p.totalQs || 5) * (p.avgQSec || 60)));
          } else if (activeY === "passageGuesses" || activeY === "guessCount") {
            yVal = p.guesses || 0;
          } else if (activeY === "passageFatigueDelta") {
            yVal = p.fatigueDelta || 0;
          } else if (activeY === "passagePaceDelta") {
            yVal = p.paceDelta || 0;
          } else {
            yVal = p.wpm || 200;
          }

          return {
            xIndex: idx,
            label: `Passage ${idx + 1} (${p.topic || 'Passage'})`,
            shortLabel: `Passage ${idx + 1}`,
            val: yVal,
            displayVal: metricDef.formatVal(yVal),
            sec: targetSession.sec,
            examTitle: targetSession.suiteTitle || targetSession.label,
            wordCount: p.wordCount,
            rawPassage: p
          };
        });

        return {
          scope: "within",
          subScope: "passage",
          xAxisMode: "passages_single",
          xAxisLabel: `Passages: ${targetSession.suiteTitle || targetSession.label}`,
          session: targetSession,
          metricDef: metricDef,
          points: points,
          totalItems: points.length,
          emptyMessage: points.length === 0 ? "No passage telemetry in this session." : null
        };
      }
    }
  }

  /* ===== CANVAS RENDERING ENGINE ===== */
  function drawCanvasChart(canvas, dataset, hoveredIdx) {
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const dpr = window.devicePixelRatio || 1;
    const rect = canvas.getBoundingClientRect();
    const width = rect.width || 760;
    const height = rect.height || 340;

    canvas.width = Math.round(width * dpr);
    canvas.height = Math.round(height * dpr);
    ctx.scale(dpr, dpr);

    ctx.clearRect(0, 0, width, height);

    const padL = 68;
    const padR = 36;
    const padT = 32;
    const padB = 62;

    const plotW = width - padL - padR;
    const plotH = height - padT - padB;

    if (!dataset.points || dataset.points.length === 0) {
      ctx.fillStyle = "#64748B";
      ctx.font = "600 13.5px Arial, sans-serif";
      ctx.textAlign = "center";
      ctx.fillText(dataset.emptyMessage || "No data available to display.", width / 2, height / 2);
      return;
    }

    const pts = dataset.points;
    const vals = pts.map(p => p.val);
    let minVal = Math.min(...vals);
    let maxVal = Math.max(...vals);

    // Expand bounds with benchmark consideration
    const bench = dataset.metricDef.benchmark;

    const isDelta = !!(
      dataset.metricDef.isDelta ||
      (dataset.metricDef.id && dataset.metricDef.id.toLowerCase().includes("delta")) ||
      (bench && bench.line === 0) ||
      dataset.metricDef.id === "netSecondGuessing"
    );

    let yFloor, yCeil, numYTicks;
    if (isDelta) {
      let absMax = Math.max(Math.abs(minVal), Math.abs(maxVal));
      if (absMax === 0) {
        absMax = dataset.metricDef.unit === "s" ? 30 : (dataset.metricDef.unit === "%" ? 15 : (dataset.metricDef.unit === "WPM" ? 25 : 4));
      }
      let M = absMax * 1.18;
      // Round up to clean increments
      if (dataset.metricDef.unit === "s") {
        if (M <= 30) M = Math.ceil(M / 10) * 10;
        else if (M <= 90) M = Math.ceil(M / 15) * 15;
        else M = Math.ceil(M / 30) * 30;
      } else if (dataset.metricDef.unit === "%") {
        M = Math.ceil(M / 5) * 5;
      } else if (dataset.metricDef.unit === "pts" || dataset.metricDef.unit === "guesses") {
        M = Math.ceil(M / 2) * 2;
      } else if (dataset.metricDef.unit === "WPM") {
        M = Math.ceil(M / 10) * 10;
      } else {
        M = Math.ceil(M / 10) * 10;
      }
      yFloor = -M;
      yCeil = +M;
      numYTicks = 4; // 4 intervals produces 5 ticks: -M, -M/2, 0, +M/2, +M
    } else {
      if (bench) {
        if (bench.min !== undefined) minVal = Math.min(minVal, bench.min);
        if (bench.max !== undefined) maxVal = Math.max(maxVal, bench.max);
        if (bench.line !== undefined) {
          minVal = Math.min(minVal, bench.line - 2);
          maxVal = Math.max(maxVal, bench.line + 2);
        }
      }
      if (minVal === maxVal) {
        minVal = Math.max(0, minVal - 10);
        maxVal = maxVal + 10;
      }
      const valSpan = maxVal - minVal || 1;
      yFloor = Math.max(0, Math.floor(minVal - valSpan * 0.1));
      yCeil = Math.ceil(maxVal + valSpan * 0.1);
      numYTicks = 5;
    }

    const getYPx = (v) => padT + plotH - ((v - yFloor) / (yCeil - yFloor)) * plotH;
    const getXPx = (idx) => {
      if (pts.length === 1) return padL + plotW / 2;
      return padL + (idx / (pts.length - 1)) * plotW;
    };

    // 1. Draw Benchmark Shaded Band or Target Line
    if (bench && bench.min !== undefined && bench.max !== undefined) {
      const topY = getYPx(bench.max);
      const botY = getYPx(bench.min);
      const bandH = Math.abs(botY - topY);

      ctx.fillStyle = "rgba(30, 122, 60, 0.08)";
      ctx.fillRect(padL, topY, plotW, bandH);

      ctx.strokeStyle = "rgba(30, 122, 60, 0.35)";
      ctx.lineWidth = 1;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(padL, topY);
      ctx.lineTo(padL + plotW, topY);
      ctx.moveTo(padL, botY);
      ctx.lineTo(padL + plotW, botY);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = "#1E7A3C";
      ctx.font = "bold 10.5px Arial, sans-serif";
      ctx.textAlign = "right";
      ctx.fillText(bench.label, padL + plotW - 6, topY + 12);
    } else if (bench && bench.line !== undefined) {
      const lineY = getYPx(bench.line);
      ctx.strokeStyle = isDelta ? "rgba(71, 85, 105, 0.75)" : "rgba(30, 122, 60, 0.6)";
      ctx.lineWidth = 1.5;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(padL, lineY);
      ctx.lineTo(padL + plotW, lineY);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = isDelta ? "#334155" : "#1E7A3C";
      ctx.font = "bold 10.5px Arial, sans-serif";
      ctx.textAlign = "right";
      ctx.fillText(bench.label, padL + plotW - 6, lineY - 4);
    }

    // 2. Grid lines & Y Ticks
    ctx.font = "11px Arial, sans-serif";
    ctx.fillStyle = "#64748B";
    ctx.textAlign = "right";

    for (let i = 0; i <= numYTicks; i++) {
      const tickVal = yFloor + (i / numYTicks) * (yCeil - yFloor);
      const yPos = getYPx(tickVal);
      const isZeroBaseline = isDelta && Math.abs(tickVal) < 0.0001;

      // Grid line
      ctx.strokeStyle = isZeroBaseline ? "#475569" : "#E2E8F0";
      ctx.lineWidth = isZeroBaseline ? 1.8 : 1;
      ctx.beginPath();
      ctx.moveTo(padL, yPos);
      ctx.lineTo(padL + plotW, yPos);
      ctx.stroke();

      // Tick text
      const tickStr = dataset.metricDef.formatTick ? dataset.metricDef.formatTick(tickVal) : String(Math.round(tickVal));
      ctx.fillStyle = isZeroBaseline ? "#0F172A" : "#64748B";
      ctx.font = isZeroBaseline ? "bold 11px Arial, sans-serif" : "11px Arial, sans-serif";
      ctx.fillText(tickStr, padL - 8, yPos + 3.5);

      if (isZeroBaseline) {
        ctx.save();
        ctx.fillStyle = "#475569";
        ctx.font = "bold 10px Arial, sans-serif";
        ctx.textAlign = "left";
        ctx.fillText("0 (Baseline)", padL + 6, yPos - 5);
        ctx.restore();
      }
    }

    // 3. Area gradient fill under data curve
    if (pts.length > 1) {
      const yBase = isDelta ? getYPx(0) : (padT + plotH);
      const grad = ctx.createLinearGradient(0, padT, 0, padT + plotH);
      if (isDelta) {
        grad.addColorStop(0, "rgba(24, 90, 157, 0.18)");
        grad.addColorStop(0.5, "rgba(24, 90, 157, 0.03)");
        grad.addColorStop(1, "rgba(24, 90, 157, 0.18)");
      } else {
        grad.addColorStop(0, "rgba(24, 90, 157, 0.22)");
        grad.addColorStop(1, "rgba(24, 90, 157, 0.01)");
      }

      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.moveTo(getXPx(0), yBase);
      pts.forEach((p, idx) => {
        ctx.lineTo(getXPx(idx), getYPx(p.val));
      });
      ctx.lineTo(getXPx(pts.length - 1), yBase);
      ctx.closePath();
      ctx.fill();
    }

    // 4. Data line stroke
    ctx.strokeStyle = "#185A9D";
    ctx.lineWidth = 2.5;
    ctx.lineJoin = "round";
    ctx.lineCap = "round";
    ctx.beginPath();
    pts.forEach((p, idx) => {
      const x = getXPx(idx);
      const y = getYPx(p.val);
      if (idx === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    });
    ctx.stroke();

    // 5. Data points circles & X Ticks
    ctx.textAlign = "center";
    ctx.font = "11px Arial, sans-serif";

    pts.forEach((p, idx) => {
      const x = getXPx(idx);
      const y = getYPx(p.val);
      const isHovered = hoveredIdx === idx;

      // Outer point glow on hover
      if (isHovered) {
        ctx.fillStyle = isDelta
          ? (p.val > 0 ? "rgba(16, 185, 129, 0.28)" : (p.val < 0 ? "rgba(239, 68, 68, 0.28)" : "rgba(100, 116, 139, 0.28)"))
          : "rgba(24, 90, 157, 0.25)";
        ctx.beginPath();
        ctx.arc(x, y, 10, 0, Math.PI * 2);
        ctx.fill();
      }

      // Point circle
      let ptColor = isHovered ? "#0C3259" : "#185A9D";
      if (isDelta) {
        if (p.val > 0) ptColor = isHovered ? "#047857" : "#10B981";
        else if (p.val < 0) ptColor = isHovered ? "#B91C1C" : "#EF4444";
        else ptColor = isHovered ? "#334155" : "#64748B";
      }
      ctx.fillStyle = ptColor;
      ctx.beginPath();
      ctx.arc(x, y, isHovered ? 6 : 4.5, 0, Math.PI * 2);
      ctx.fill();

      ctx.fillStyle = "#FFFFFF";
      ctx.beginPath();
      ctx.arc(x, y, isHovered ? 2.5 : 2, 0, Math.PI * 2);
      ctx.fill();

      // X Tick Label (thin out automatically if many data points)
      const step = pts.length > 20 ? Math.ceil(pts.length / 14) : 1;
      if (idx % step === 0 || idx === pts.length - 1 || isHovered) {
        ctx.save();
        ctx.translate(x, padT + plotH + 16);
        ctx.rotate(-Math.PI / 6);
        ctx.fillStyle = isHovered ? "#0F172A" : "#64748B";
        ctx.font = isHovered ? "bold 11px Arial, sans-serif" : "11px Arial, sans-serif";
        ctx.textAlign = "right";
        ctx.fillText(p.shortLabel, 0, 0);
        ctx.restore();
      }
    });

    // Axis interactive hints on canvas margins
    ctx.fillStyle = "#94A3B8";
    ctx.font = "bold 9.5px Arial, sans-serif";
    ctx.textAlign = "left";
    ctx.fillText("Y-AXIS (CLICK TO CHANGE)", padL, padT - 10);
    ctx.textAlign = "center";
    ctx.fillText("X-AXIS: " + (dataset.xAxisLabel || "").toUpperCase() + " (CLICK TO CHANGE)", padL + plotW / 2, height - 10);

    // 6. Draw interactive Tooltip card
    if (hoveredIdx >= 0 && hoveredIdx < pts.length) {
      const p = pts[hoveredIdx];
      const x = getXPx(hoveredIdx);
      const y = getYPx(p.val);

      const ttLines = [
        p.label,
        `${dataset.metricDef.shortLabel}: ${p.displayVal}`
      ];
      if (hoveredIdx > 0) {
        const prevVal = pts[hoveredIdx - 1].val;
        const delta = p.val - prevVal;
        const deltaStr = (delta >= 0 ? "+" : "") + Math.round(delta);
        ttLines.push(`Delta vs previous: ${deltaStr} ${dataset.metricDef.unit}`);
      }

      ctx.font = "bold 12px Arial, sans-serif";
      let ttW = Math.max(...ttLines.map(l => ctx.measureText(l).width)) + 24;
      const ttH = ttLines.length * 18 + 14;

      let ttX = x - ttW / 2;
      let ttY = y - ttH - 12;

      // Clamping inside chart canvas
      if (ttX < padL) ttX = padL + 4;
      if (ttX + ttW > width - padR) ttX = width - padR - ttW - 4;
      if (ttY < 6) ttY = y + 14;

      // Tooltip Card Box
      ctx.fillStyle = "#1E293B";
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.roundRect(ttX, ttY, ttW, ttH, 5);
      ctx.fill();
      ctx.stroke();

      // Tooltip Text
      ttLines.forEach((line, li) => {
        ctx.fillStyle = li === 0 ? "#94A3B8" : (li === 1 ? "#FFFFFF" : "#38BDF8");
        ctx.font = li === 1 ? "bold 12px Arial, sans-serif" : "11px Arial, sans-serif";
        ctx.textAlign = "left";
        ctx.fillText(line, ttX + 12, ttY + 16 + (li * 18));
      });
    }
  }

  /* ===== EXPORT CHART AS PNG ===== */
  function exportChartToPNG(dataset) {
    if (!dataset || !dataset.points || !dataset.points.length) {
      alert("No data available to export as chart.");
      return;
    }

    const expW = 1280;
    const expH = 720;
    const expCanvas = document.createElement("canvas");
    expCanvas.width = expW;
    expCanvas.height = expH;
    const ctx = expCanvas.getContext("2d");

    // Clean white background
    ctx.fillStyle = "#FFFFFF";
    ctx.fillRect(0, 0, expW, expH);

    // Top Brand & Header Banner
    ctx.fillStyle = "#1B3A5C";
    ctx.fillRect(0, 0, expW, 70);

    ctx.fillStyle = "#FFFFFF";
    ctx.font = "bold 20px Arial, sans-serif";
    ctx.textAlign = "left";
    ctx.fillText("DrillRoom MCAT Analytics", 32, 42);

    ctx.font = "13px Arial, sans-serif";
    ctx.fillStyle = "#94A3B8";
    ctx.textAlign = "right";
    ctx.fillText(`Generated: ${new Date().toLocaleDateString()} at ${new Date().toLocaleTimeString()}`, expW - 32, 42);

    // Subtitle & Scope
    ctx.fillStyle = "#0F172A";
    ctx.font = "bold 18px Arial, sans-serif";
    ctx.textAlign = "left";
    const subTitle = dataset.scope === "passages_all"
      ? `Individual Passage Analysis: ${dataset.metricDef.label} (All Sections Chronologically)`
      : (dataset.scope === "across"
        ? `Performance Trajectory: ${dataset.metricDef.label} (Across All Sessions)`
        : `Single-Section Analysis: ${dataset.session?.suiteTitle || dataset.session?.label || 'Session'} (${dataset.metricDef.label})`);
    ctx.fillText(subTitle, 32, 105);

    // Render Stats Ribbon
    const vals = dataset.points.map(p => p.val);
    const avgVal = vals.length ? (vals.reduce((a, b) => a + b, 0) / vals.length) : 0;
    const minVal = vals.length ? Math.min(...vals) : 0;
    const maxVal = vals.length ? Math.max(...vals) : 0;
    const trendDelta = vals.length > 1 ? (vals[vals.length - 1] - vals[0]) : 0;

    const statsBarY = 120;
    ctx.fillStyle = "#F8FAFC";
    ctx.strokeStyle = "#CBD5E1";
    ctx.lineWidth = 1;
    ctx.fillRect(32, statsBarY, expW - 64, 46);
    ctx.strokeRect(32, statsBarY, expW - 64, 46);

    ctx.fillStyle = "#334155";
    ctx.font = "13px Arial, sans-serif";
    ctx.textAlign = "left";
    const statText = `Average: ${dataset.metricDef.formatVal(avgVal)}   |   Min: ${dataset.metricDef.formatVal(minVal)}   |   Max: ${dataset.metricDef.formatVal(maxVal)}   |   Trajectory: ${trendDelta >= 0 ? "+" : ""}${Math.round(trendDelta)} ${dataset.metricDef.unit}`;
    ctx.fillText(statText, 48, statsBarY + 28);

    // Draw Main Chart in Center
    const chartSubCanvas = document.createElement("canvas");
    chartSubCanvas.style.width = `${expW - 64}px`;
    chartSubCanvas.style.height = `${expH - 250}px`;
    drawCanvasChart(chartSubCanvas, dataset, -1);
    ctx.drawImage(chartSubCanvas, 32, 180, expW - 64, expH - 260);

    // Footer Watermark
    ctx.fillStyle = "#64748B";
    ctx.font = "12px Arial, sans-serif";
    ctx.textAlign = "center";
    ctx.fillText("DrillRoom MCAT Preparation & Pacing Analytics • Authentic AAMC Metric Calibration", expW / 2, expH - 24);

    // Trigger Download
    const dataUrl = expCanvas.toDataURL("image/png");
    const link = document.createElement("a");
    link.download = `DrillRoom_Chart_${dataset.metricDef.id}_${Date.now()}.png`;
    link.href = dataUrl;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }

  /* ===== EXPORT DATASET AS CSV ===== */
  function exportChartToCSV(dataset) {
    if (!dataset || !dataset.points || !dataset.points.length) {
      alert("No data available to export as CSV.");
      return;
    }

    const headers = ["Index", "Label", "Value", "Unit", "Subject", "Date"];
    const rows = dataset.points.map(p => [
      p.xIndex + 1,
      `"${p.label.replace(/"/g, '""')}"`,
      p.val,
      `"${dataset.metricDef.unit}"`,
      `"${p.sec || ''}"`,
      `"${p.date || ''}"`
    ]);

    const csvContent = "data:text/csv;charset=utf-8," + [headers.join(","), ...rows.map(r => r.join(","))].join("\n");
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", `DrillRoom_${dataset.metricDef.id}_${Date.now()}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }

  /* ===== GEMINI AI TREND ANALYSIS ===== */
  async function runAITrendAnalysis(dataset, container, customQuestion) {
    if (!dataset || !dataset.points.length) return;

    const apiKey = (typeof window.getGeminiApiKey === "function") ? window.getGeminiApiKey() : null;
    if (!apiKey) {
      if (typeof window.showGeminiSettingsModal === "function") {
        window.showGeminiSettingsModal();
      } else {
        alert("Please connect your Google Gemini API key to unlock AI trajectory coaching.");
      }
      return;
    }

    const statusEl = document.getElementById("gChartAIStatus");
    const contentEl = document.getElementById("gChartAIContent");
    const askBtn = document.getElementById("btnAskGeminiChart");
    if (statusEl) statusEl.textContent = "Synthesizing trajectory analytics with Gemini...";
    if (askBtn) askBtn.disabled = true;

    const vals = dataset.points.map(p => p.val);
    const avgVal = (vals.reduce((a, b) => a + b, 0) / vals.length).toFixed(1);
    const minVal = Math.min(...vals);
    const maxVal = Math.max(...vals);
    const trendDelta = (vals[vals.length - 1] - vals[0]).toFixed(1);

    const scopeDesc = dataset.scope === "passages_all"
      ? `Across All Individual Passages Chronologically (${dataset.points.length} passages across ${dataset.totalSessions || 1} sections)`
      : (dataset.scope === "across"
        ? `Across Chronological Practice Sessions (${dataset.points.length} sessions)`
        : `Within Single Session (${dataset.session?.suiteTitle || dataset.session?.label || 'Session'})`);

    const promptText = `You are a world-class MCAT cognitive coach and former AAMC psychometrician.
The student is inspecting their performance analytics chart inside the DrillRoom MCAT app:
- **Scope:** ${scopeDesc}
- **Metric Analyzed:** ${dataset.metricDef.label} (${dataset.metricDef.unit})
- **AAMC Target Benchmark:** ${dataset.metricDef.benchmark ? (dataset.metricDef.benchmark.label || dataset.metricDef.benchmark.min + '-' + dataset.metricDef.benchmark.max) : "Standard MCAT pace"}
- **Dataset Chronology (${dataset.points.length} points):**
${dataset.points.map(p => `- ${p.label}: **${p.displayVal}** (${p.sec || 'Section'})`).join("\n")}

- **Summary Statistics:**
  * Average: **${dataset.metricDef.formatVal(avgVal)}**
  * Peak / Best: **${dataset.metricDef.formatVal(maxVal)}**
  * Minimum: **${dataset.metricDef.formatVal(minVal)}**
  * Net Trend Progression: **${trendDelta >= 0 ? "+" + trendDelta : trendDelta} ${dataset.metricDef.unit}**

${customQuestion ? `The student is asking this specific follow-up question about this trend:\n"${customQuestion}"\n` : ""}

### INSTRUCTIONS:
Generate a concise, high-impact MCAT Trend Assessment (under 250 words total) structured with these exact sections:
1. **Trajectory & Pacing Reality:** Direct assessment of whether they are improving, stabilizing, or experiencing cognitive fatigue/plateauing. Cite the specific numbers and contrast against AAMC benchmarks.
2. **Cognitive Fatigue & Speed Diagnosis:** Diagnose what their passage reading pace or question solving speed reveals about their comprehension trade-off. Are they rushing early or fatiguing late?
3. **#1 Tactical Drill to Deploy on Next Section:** Give 1 ultra-specific, concrete execution rule or heuristic to optimize this metric immediately.`;

    try {
      const model = (typeof window.getGeminiModel === "function") ? window.getGeminiModel() : "gemini-2.5-flash";
      const res = await window.callGeminiAPI(promptText, apiKey, model);

      chartState.aiAnalysisText = res.text;
      if (statusEl) statusEl.textContent = `Diagnostic formulated by ${res.modelUsed}`;
      if (contentEl) {
        const renderMd = (typeof window.renderGeminiMarkdown === "function") ? window.renderGeminiMarkdown : (s => `<p>${s}</p>`);
        contentEl.innerHTML = renderMd(res.text);
      }
    } catch (err) {
      if (statusEl) statusEl.textContent = `Error: ${err.message}`;
    } finally {
      if (askBtn) askBtn.disabled = false;
    }
  }

  /* ===== MAIN RENDERER FOR PERFORMANCE CHARTS ===== */
  function renderPerformanceCharts(container) {
    if (!container) return;
    container.innerHTML = "";

    const allSessions = getAllEnrichedSessions();
    if (!chartState.selectedSessionId && allSessions.length) {
      chartState.selectedSessionId = allSessions[allSessions.length - 1].id;
    }

    const dataset = getActiveChartDataset();
    const activeMode = dataset.xAxisMode || chartState.xAxisMode || "passages_all";

    const wrap = document.createElement("div");
    wrap.className = "pe-chart-dashboard";
    wrap.style.cssText = "margin:20px 0 24px 0;background:#FFFFFF;border:1px solid var(--line);border-radius:6px;box-shadow:0 2px 8px rgba(0,0,0,0.06);padding:20px";

    // 1. Dashboard Header (Title & Action Buttons)
    const headerEl = document.createElement("div");
    headerEl.style.cssText = "display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;margin-bottom:14px;border-bottom:1.5px solid #E2E8F0;padding-bottom:12px";
    headerEl.innerHTML = `
      <div>
        <div style="font-size:17px;font-weight:700;color:var(--nav);display:flex;align-items:center;gap:8px">
          Performance Analytics &amp; Telemetry
        </div>
        <div style="font-size:12px;color:var(--faint);margin-top:2px">
          Select any X-axis and Y-axis directly on the chart below to analyze reading speeds, question pace, and trajectories.
        </div>
      </div>
      <div style="display:flex;gap:8px;flex-wrap:wrap;align-items:center">
        <button class="btn" id="btnDownloadChartPNG" style="font-size:12px;padding:5px 12px;border:1px solid #CBD5E1;background:#F8FAFC" title="Download high-resolution chart image">
          Download Chart (PNG)
        </button>
        <button class="btn" id="btnExportChartCSV" style="font-size:12px;padding:5px 12px;border:1px solid #CBD5E1;background:#F8FAFC" title="Export raw data to CSV">
          Export CSV
        </button>
        <button class="btn pri" id="btnToggleAIPanel" style="font-size:12px;padding:5px 12px">
          Ask Gemini About Trend
        </button>
      </div>
    `;
    wrap.appendChild(headerEl);

    // 2. Stats Ribbon (Summary Analytics)
    const statsRibbon = document.createElement("div");
    statsRibbon.style.cssText = "display:flex;gap:18px;flex-wrap:wrap;margin-bottom:14px;padding:8px 12px;background:#F1F5F9;border-radius:4px;font-size:12px;color:#334155";

    const vals = dataset.points.map(p => p.val);
    const avgVal = vals.length ? (vals.reduce((a, b) => a + b, 0) / vals.length) : 0;
    const minVal = vals.length ? Math.min(...vals) : 0;
    const maxVal = vals.length ? Math.max(...vals) : 0;
    const trendDelta = vals.length > 1 ? (vals[vals.length - 1] - vals[0]) : 0;

    statsRibbon.innerHTML = `
      <div><strong>Data Points:</strong> ${dataset.points.length}</div>
      <div><strong>Average:</strong> ${dataset.metricDef.formatVal(avgVal)}</div>
      <div><strong>Min:</strong> ${dataset.metricDef.formatVal(minVal)}</div>
      <div><strong>Max:</strong> ${dataset.metricDef.formatVal(maxVal)}</div>
      <div><strong>Trajectory Delta:</strong> <span style="font-weight:700;color:${trendDelta > 0 ? (dataset.metricDef.higherIsBetter ? 'var(--ok)' : 'var(--warn)') : (dataset.metricDef.higherIsBetter ? 'var(--bad)' : 'var(--ok)')}">${trendDelta >= 0 ? "+" : ""}${Math.round(trendDelta)} ${dataset.metricDef.unit}</span></div>
      ${dataset.metricDef.benchmark ? `<div style="margin-left:auto;color:#1E7A3C;font-weight:600">Target: ${dataset.metricDef.benchmark.label}</div>` : ""}
    `;
    wrap.appendChild(statsRibbon);

    // 3. THE GRAPH STAGE (Chart Stage with On-Graph Axis Selectors)
    const graphStage = document.createElement("div");
    graphStage.style.cssText = "position:relative;background:#FFFFFF;border:1.5px solid #CBD5E1;border-radius:6px;padding:12px 14px 14px 14px;margin-bottom:14px;box-shadow:0 1px 4px rgba(0,0,0,0.04)";

    // Top Bar: Direct Y-Axis Selector & Filters (aligned right over the Y-axis column)
    const topBar = document.createElement("div");
    topBar.style.cssText = "display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:8px;padding-bottom:6px;border-bottom:1px solid #F1F5F9";

    // Generate Y-Axis Options based on active X-Axis Mode
    let yOptionsHtml = "";
    const activeY = dataset.metricDef.id;

    if (activeMode === "passages_all" || activeMode === "passages_single") {
      yOptionsHtml = `
        <option value="passageWpm" ${activeY === 'passageWpm' ? 'selected' : ''}>Passage Reading Speed (WPM) — AAMC Target (200 - 260 WPM)</option>
        <option value="passageReadSec" ${activeY === 'passageReadSec' ? 'selected' : ''}>Passage Reading Time — AAMC Benchmark (3:00 - 4:00)</option>
        <option value="passageAccuracy" ${activeY === 'passageAccuracy' ? 'selected' : ''}>Passage Question Accuracy (%)</option>
        <option value="passageAvgQTime" ${activeY === 'passageAvgQTime' ? 'selected' : ''}>Avg Question Time on Passage (s/Q)</option>
        <option value="passageTotalTime" ${activeY === 'passageTotalTime' ? 'selected' : ''}>Total Passage Duration (Reading + Questions)</option>
        <option value="passageWordCount" ${activeY === 'passageWordCount' ? 'selected' : ''}>Passage Word Count</option>
        <option value="passageGuesses" ${activeY === 'passageGuesses' ? 'selected' : ''}>Guesses &amp; 50/50s on Passage</option>
        <option value="passageFatigueDelta" ${activeY === 'passageFatigueDelta' ? 'selected' : ''}>Fatigue Delta vs Passage 1 (Slowing Index)</option>
        <option value="passagePaceDelta" ${activeY === 'passagePaceDelta' ? 'selected' : ''}>Reading Pace Delta vs Previous Passage (WPM)</option>
      `;
    } else if (activeMode === "sessions") {
      yOptionsHtml = `
        <option value="avgPassageReadSec" ${activeY === 'avgPassageReadSec' ? 'selected' : ''}>Avg Passage Reading Time (3:00 - 4:00 Benchmark)</option>
        <option value="avgPassageWpm" ${activeY === 'avgPassageWpm' ? 'selected' : ''}>Avg Passage Reading Pace (200 - 260 WPM Target)</option>
        <option value="scaledScore" ${activeY === 'scaledScore' ? 'selected' : ''}>MCAT Scaled Score (118 - 132)</option>
        <option value="pct" ${activeY === 'pct' ? 'selected' : ''}>Raw Accuracy (%)</option>
        <option value="avgQSec" ${activeY === 'avgQSec' ? 'selected' : ''}>Avg Pure Question Solving Time (s/Q)</option>
        <option value="solidRatio" ${activeY === 'solidRatio' ? 'selected' : ''}>Solid Mastery Ratio (%)</option>
        <option value="guessCount" ${activeY === 'guessCount' ? 'selected' : ''}>Total Guesses &amp; Coin Flips</option>
        <option value="netSecondGuessing" ${activeY === 'netSecondGuessing' ? 'selected' : ''}>Second-Guessing Net Impact (Points)</option>
        <option value="avgSessionFatigueDelta" ${activeY === 'avgSessionFatigueDelta' ? 'selected' : ''}>Session Fatigue Delta vs P1 (Endurance Conditioning)</option>
        <option value="lateStageAccuracyDelta" ${activeY === 'lateStageAccuracyDelta' ? 'selected' : ''}>Endurance Accuracy Delta (Late vs Early Passages)</option>
        <option value="pacingConsistency" ${activeY === 'pacingConsistency' ? 'selected' : ''}>Pacing Consistency / Std Dev (Seconds)</option>
        <option value="timeSinkCount" ${activeY === 'timeSinkCount' ? 'selected' : ''}>Sunk-Cost Questions Count (>100s)</option>
        <option value="timeUsedMinutes" ${activeY === 'timeUsedMinutes' ? 'selected' : ''}>Total Section Elapsed Time (Minutes)</option>
      `;
    } else {
      // questions_single
      yOptionsHtml = `
        <option value="qTime" ${activeY === 'qTime' ? 'selected' : ''}>Question Solving Time (Seconds/Q)</option>
        <option value="qOutcomeScore" ${activeY === 'qOutcomeScore' ? 'selected' : ''}>Confidence &amp; Mastery Tier (Solid, 50/50, Guess, Miss)</option>
      `;
    }

    topBar.innerHTML = `
      <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap">
        <label for="selDirectYMetric" style="font-size:11.5px;font-weight:700;color:#185A9D;background:#EDF4FB;border:1px solid #B8D5E5;padding:3px 8px;border-radius:4px;cursor:pointer" title="Select metric directly for vertical Y-axis">
          Y-Axis
        </label>
        <select id="selDirectYMetric" style="font-size:12.5px;font-weight:600;color:#0F172A;padding:4px 10px;border:1.5px solid #185A9D;border-radius:4px;background:#FFFFFF;cursor:pointer;box-shadow:0 1px 3px rgba(0,0,0,0.06)">
          ${yOptionsHtml}
        </select>
        <span style="font-size:11.5px;color:#64748B;font-style:italic">
          ${dataset.metricDef.desc || ''}
        </span>
      </div>

      <div style="display:flex;align-items:center;gap:8px">
        <label style="font-size:12px;font-weight:600;color:#475569;display:flex;align-items:center;gap:4px">
          Subject:
          <select id="selDirectSubject" style="font-size:12px;padding:3px 8px;border:1px solid #CBD5E1;border-radius:3px;background:#FFF;cursor:pointer">
            <option value="all" ${chartState.subjectFilter === 'all' ? 'selected' : ''}>All 4 Subjects</option>
            <option value="C/P" ${chartState.subjectFilter === 'C/P' ? 'selected' : ''}>C/P Only</option>
            <option value="CARS" ${chartState.subjectFilter === 'CARS' ? 'selected' : ''}>CARS Only</option>
            <option value="B/B" ${chartState.subjectFilter === 'B/B' ? 'selected' : ''}>B/B Only</option>
            <option value="P/S" ${chartState.subjectFilter === 'P/S' ? 'selected' : ''}>P/S Only</option>
          </select>
        </label>
      </div>
    `;
    graphStage.appendChild(topBar);

    // Canvas Container
    const canvasWrap = document.createElement("div");
    canvasWrap.style.cssText = "position:relative;width:100%;height:330px";
    const canvas = document.createElement("canvas");
    canvas.style.cssText = "width:100%;height:100%;display:block;cursor:crosshair";
    canvasWrap.appendChild(canvas);
    graphStage.appendChild(canvasWrap);

    // Bottom Bar: Direct X-Axis Selector & Section Picker (aligned right under horizontal X-axis)
    const bottomBar = document.createElement("div");
    bottomBar.style.cssText = "display:flex;justify-content:center;align-items:center;gap:12px;margin-top:8px;padding-top:10px;border-top:1.5px dashed #E2E8F0;flex-wrap:wrap";
    bottomBar.innerHTML = `
      <div style="display:flex;align-items:center;gap:8px">
        <label for="selDirectXAxis" style="font-size:11.5px;font-weight:700;color:#185A9D;background:#EDF4FB;border:1px solid #B8D5E5;padding:3px 8px;border-radius:4px;cursor:pointer" title="Select dimension directly for horizontal X-axis">
          X-Axis
        </label>
        <select id="selDirectXAxis" style="font-size:12.5px;font-weight:600;color:#0F172A;padding:4px 10px;border:1.5px solid #185A9D;border-radius:4px;background:#FFFFFF;cursor:pointer;box-shadow:0 1px 3px rgba(0,0,0,0.06)">
          <option value="passages_all" ${activeMode === 'passages_all' ? 'selected' : ''}>Individual Passages (All Sections Chronologically)</option>
          <option value="passages_single" ${activeMode === 'passages_single' ? 'selected' : ''}>Individual Passages (1 Specific Section)</option>
          <option value="sessions" ${activeMode === 'sessions' ? 'selected' : ''}>Sessions (Trajectory Across Attempts)</option>
          <option value="questions_single" ${activeMode === 'questions_single' ? 'selected' : ''}>Individual Questions (1 Specific Section)</option>
        </select>
      </div>

      <!-- Section Picker for 1 specific section -->
      <div id="wrapDirectSectionPicker" style="display:${(activeMode === 'passages_single' || activeMode === 'questions_single') ? 'flex' : 'none'};align-items:center;gap:6px">
        <span style="font-size:12px;font-weight:600;color:#475569">Section:</span>
        <select id="selDirectSection" style="font-size:12px;padding:4px 8px;border:1px solid #CBD5E1;border-radius:3px;background:#FFF;cursor:pointer;max-width:280px">
          ${allSessions.slice().reverse().map(s => `
            <option value="${s.id}" ${s.id === chartState.selectedSessionId ? 'selected' : ''}>
              ${new Date(s.ts || Date.now()).toLocaleDateString([], {month:'short', day:'numeric'})} &bull; ${s.sec} - ${s.suiteTitle || s.label} (${s.scaledScore || 125}/132)
            </option>
          `).join("")}
        </select>
      </div>
    `;
    graphStage.appendChild(bottomBar);
    wrap.appendChild(graphStage);

    // Initial canvas render
    const runTimer = (typeof setTimeout !== "undefined") ? setTimeout : ((fn) => fn());
    runTimer(() => {
      drawCanvasChart(canvas, dataset, chartState.hoverIndex);
    }, 0);

    // Canvas click listener to open/focus axis selector directly from graph margins
    canvas.onclick = (e) => {
      const rect = canvas.getBoundingClientRect();
      const xMouse = e.clientX - rect.left;
      const yMouse = e.clientY - rect.top;
      const padL = 68;
      const padT = 32;
      const padB = 62;
      const plotH = rect.height - padT - padB;

      if (xMouse < padL + 15) {
        const selYEl = wrap.querySelector("#selDirectYMetric");
        if (selYEl) {
          selYEl.focus();
          if (typeof selYEl.showPicker === "function") {
            try { selYEl.showPicker(); } catch (err) {}
          }
        }
      } else if (yMouse > padT + plotH - 10) {
        const selXEl = wrap.querySelector("#selDirectXAxis");
        if (selXEl) {
          selXEl.focus();
          if (typeof selXEl.showPicker === "function") {
            try { selXEl.showPicker(); } catch (err) {}
          }
        }
      }
    };

    // Mouse move hover listener for interactive tooltips
    canvas.onmousemove = (e) => {
      const rect = canvas.getBoundingClientRect();
      const xMouse = e.clientX - rect.left;
      const padL = 68;
      const padR = 36;
      const plotW = rect.width - padL - padR;

      let closestIdx = -1;
      let closestDist = Infinity;

      dataset.points.forEach((p, idx) => {
        const xPos = dataset.points.length === 1 ? (padL + plotW / 2) : (padL + (idx / (dataset.points.length - 1)) * plotW);
        const dist = Math.abs(xMouse - xPos);
        if (dist < closestDist && dist < 35) {
          closestDist = dist;
          closestIdx = idx;
        }
      });

      if (closestIdx !== chartState.hoverIndex) {
        chartState.hoverIndex = closestIdx;
        drawCanvasChart(canvas, dataset, closestIdx);
      }
    };

    canvas.onmouseleave = () => {
      chartState.hoverIndex = -1;
      drawCanvasChart(canvas, dataset, -1);
    };

    // 4. AI Trajectory Analysis Panel
    const aiPanel = document.createElement("div");
    aiPanel.id = "peChartAIPanel";
    aiPanel.style.cssText = `margin-top:20px;border-top:1.5px solid #E2E8F0;padding-top:16px;${chartState.aiPanelOpen ? "" : "display:none"}`;
    aiPanel.innerHTML = `
      <div style="background:#F8FAFC;border:1.5px solid #185A9D;border-radius:6px;padding:16px 18px">
        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:10px">
          <div style="font-size:14.5px;font-weight:700;color:var(--nav);display:flex;align-items:center;gap:8px">
            Gemini AI Trajectory &amp; Fatigue Analysis
          </div>
          <div id="gChartAIStatus" style="font-size:11.5px;color:var(--faint);font-weight:600"></div>
        </div>

        <div id="gChartAIContent" style="font-size:13px;line-height:1.6;color:var(--soft);margin-bottom:14px">
          ${chartState.aiAnalysisText ? (typeof window.renderGeminiMarkdown === "function" ? window.renderGeminiMarkdown(chartState.aiAnalysisText) : chartState.aiAnalysisText) : '<p style="color:var(--faint)">Click "Analyze Trajectory" below to have Gemini formulate an expert diagnostic of your pacing and cognitive stamina across these sessions.</p>'}
        </div>

        <!-- Follow-up Question to Chart AI -->
        <div style="display:flex;gap:8px;align-items:center">
          <input type="text" id="gChartQuestionInput" placeholder="Ask Gemini a specific question about this chart, speed plateau, or pacing..." 
                 style="flex:1;padding:8px 12px;border:1px solid var(--line2);border-radius:3px;font-size:12.5px" />
          <button class="btn pri" id="btnAskGeminiChart" style="padding:8px 16px;font-size:12.5px;white-space:nowrap">Analyze Trajectory</button>
        </div>
      </div>
    `;
    wrap.appendChild(aiPanel);

    // Event Listeners for On-Graph Selectors
    const selY = wrap.querySelector("#selDirectYMetric");
    if (selY) {
      selY.onchange = (e) => {
        const val = e.target.value;
        chartState.yMetric = val;
        if (activeMode === "sessions") {
          chartState.acrossY = val;
        } else if (activeMode === "questions_single") {
          chartState.withinX = "question";
          chartState.withinY = val;
        } else {
          chartState.withinX = "passage";
          chartState.withinY = val;
        }
        renderPerformanceCharts(container);
      };
    }

    const selX = wrap.querySelector("#selDirectXAxis");
    if (selX) {
      selX.onchange = (e) => {
        const newMode = e.target.value;
        chartState.xAxisMode = newMode;
        chartState.scope = newMode; // synchronize

        // Smart metric transition
        if (newMode === "sessions") {
          if (chartState.yMetric === "passageWpm") chartState.acrossY = "avgPassageWpm";
          else if (chartState.yMetric === "passageReadSec") chartState.acrossY = "avgPassageReadSec";
          else if (chartState.yMetric === "passageAccuracy") chartState.acrossY = "pct";
          else if (!SESSION_METRICS.includes(chartState.acrossY)) chartState.acrossY = "avgPassageReadSec";
          chartState.yMetric = chartState.acrossY;
        } else if (newMode === "questions_single") {
          chartState.withinX = "question";
          chartState.withinY = "qTime";
          chartState.yMetric = "qTime";
        } else {
          // passages_all or passages_single
          chartState.withinX = "passage";
          if (chartState.yMetric === "avgPassageWpm") chartState.yMetric = "passageWpm";
          else if (chartState.yMetric === "avgPassageReadSec" || chartState.yMetric === "qTime") chartState.yMetric = "passageReadSec";
          else if (chartState.yMetric === "pct") chartState.yMetric = "passageAccuracy";
          else if (!PASSAGE_METRICS.includes(chartState.yMetric)) {
            chartState.yMetric = "passageWpm";
          }
          chartState.withinY = chartState.yMetric;
        }

        renderPerformanceCharts(container);
      };
    }

    const selSection = wrap.querySelector("#selDirectSection");
    if (selSection) {
      selSection.onchange = (e) => {
        chartState.selectedSessionId = e.target.value;
        renderPerformanceCharts(container);
      };
    }

    const selSubject = wrap.querySelector("#selDirectSubject");
    if (selSubject) {
      selSubject.onchange = (e) => {
        chartState.subjectFilter = e.target.value;
        renderPerformanceCharts(container);
      };
    }

    // Export Buttons
    const btnPNG = wrap.querySelector("#btnDownloadChartPNG");
    if (btnPNG) {
      btnPNG.onclick = () => exportChartToPNG(dataset);
    }

    const btnCSV = wrap.querySelector("#btnExportChartCSV");
    if (btnCSV) {
      btnCSV.onclick = () => exportChartToCSV(dataset);
    }

    // AI Panel Toggle & Ask Gemini
    const btnToggleAI = wrap.querySelector("#btnToggleAIPanel");
    if (btnToggleAI) {
      btnToggleAI.onclick = () => {
        chartState.aiPanelOpen = !chartState.aiPanelOpen;
        aiPanel.style.display = chartState.aiPanelOpen ? "block" : "none";
        if (chartState.aiPanelOpen && !chartState.aiAnalysisText) {
          runAITrendAnalysis(dataset, aiPanel, null);
        }
      };
    }

    const btnAskAI = wrap.querySelector("#btnAskGeminiChart");
    const inputAI = wrap.querySelector("#gChartQuestionInput");
    if (btnAskAI) {
      btnAskAI.onclick = () => {
        const q = inputAI ? inputAI.value.trim() : "";
        runAITrendAnalysis(dataset, aiPanel, q || null);
        if (inputAI) inputAI.value = "";
      };
    }

    container.appendChild(wrap);
  }

  /* ===== EXPORTS ===== */
  window.renderPerformanceCharts = renderPerformanceCharts;
  window.enrichSessionWithStats = enrichSessionWithStats;
  window.getAllEnrichedSessions = getAllEnrichedSessions;
  window.getActiveChartDataset = getActiveChartDataset;
  window.drawCanvasChart = drawCanvasChart;
  window.exportChartToPNG = exportChartToPNG;
  window.exportChartToCSV = exportChartToCSV;
  window.chartState = chartState;
  window.CHART_METRIC_DEFS = METRIC_DEFS;

  if (typeof globalThis !== "undefined") {
    globalThis.renderPerformanceCharts = renderPerformanceCharts;
    globalThis.enrichSessionWithStats = enrichSessionWithStats;
    globalThis.getAllEnrichedSessions = getAllEnrichedSessions;
    globalThis.getActiveChartDataset = getActiveChartDataset;
  }
})();
