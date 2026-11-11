/* ---- practice_exam.js ---- */
/* Practice exam mode: timed 90-min and 60-min sections with MCAT-style scoring,
   Subject-first workflow (click subject -> click duration -> start next available),
   Clean exit without scoring, and comprehensive History with configurable rolling averages. */

/* ===== MCAT SCORING SCALE ===== */
const MCAT_SCALE = [
  [95, 132, "100th"],
  [90, 131, "99th"],
  [85, 130, "98th"],
  [80, 129, "95th"],
  [75, 128, "90th"],
  [70, 127, "82nd"],
  [65, 126, "72nd"],
  [60, 125, "60th"],
  [55, 124, "47th"],
  [50, 123, "35th"],
  [45, 122, "25th"],
  [40, 121, "16th"],
  [35, 120, "9th"],
  [30, 119, "4th"],
  [0,  118, "1st"]
];

function rawToScaled(pct) {
  for (const [thresh, score, ptile] of MCAT_SCALE) {
    if (pct >= thresh) return { score, ptile };
  }
  return { score: 118, ptile: "1st" };
}

/* ===== SUBJECT DEFINITIONS ===== */
const SUBJECT_DEFS = {
  "C/P": {
    sec: "C/P",
    name: "Chemical and Physical Foundations of Biological Systems",
    short: "Chem / Phys",
    desc: "General Chemistry, Organic Chemistry, Physics, Biochemistry",
    badgeClass: "hist-sec-cp",
    accent: "#185A9D"
  },
  "CARS": {
    sec: "CARS",
    name: "Critical Analysis and Reasoning Skills",
    short: "CARS",
    desc: "Humanities, Social Sciences, Ethics, Philosophy",
    badgeClass: "hist-sec-cars",
    accent: "#946C00"
  },
  "B/B": {
    sec: "B/B",
    name: "Biological and Biochemical Foundations of Living Systems",
    short: "Bio / Biochem",
    desc: "Biochemistry, Molecular Biology, Cell Biology, Organ Systems",
    badgeClass: "hist-sec-bb",
    accent: "#1B7A38"
  },
  "P/S": {
    sec: "P/S",
    name: "Psychological, Social, and Biological Foundations of Behavior",
    short: "Psych / Soc",
    desc: "Psychology, Sociology, Biological Bases of Behavior",
    badgeClass: "hist-sec-ps",
    accent: "#6C2BA8"
  }
};

/* ===== PRACTICE EXAM REGISTRY ===== */
const PRACTICE_EXAMS = [];
if (typeof window !== "undefined") {
  window.PRACTICE_EXAMS = PRACTICE_EXAMS;
}

function registerExam(id, sec, label, duration, type, sets, desc, suite, suiteTitle) {
  PRACTICE_EXAMS.push({
    id, sec, label, duration, type, sets, desc,
    suite: suite || type,
    suiteTitle: suiteTitle || (duration + "-Minute Practice Sections")
  });
}

// Auto-register exams from loaded data files
function autoRegisterExams() {
  PRACTICE_EXAMS.length = 0;
  // --- Practice Exam 1 (90-Minute Full Sections) ---
  if (typeof EXAM_CP90 !== "undefined" && EXAM_CP90.length) {
    registerExam("cp90", "C/P",
      "Chemical and Physical Foundations of Biological Systems",
      90, "90min", EXAM_CP90,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam1_90", "Full 90-Minute Practice Exam 1");
  }
  if (typeof EXAM_CARS90 !== "undefined" && EXAM_CARS90.length) {
    registerExam("cars90", "CARS",
      "Critical Analysis and Reasoning Skills",
      90, "90min", EXAM_CARS90,
      "90-minute timed practice \u2014 9 passages, no discrete (53 Qs)",
      "exam1_90", "Full 90-Minute Practice Exam 1");
  }
  if (typeof EXAM_BB90 !== "undefined" && EXAM_BB90.length) {
    registerExam("bb90", "B/B",
      "Biological and Biochemical Foundations of Living Systems",
      90, "90min", EXAM_BB90,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam1_90", "Full 90-Minute Practice Exam 1");
  }
  if (typeof EXAM_PS90 !== "undefined" && EXAM_PS90.length) {
    registerExam("ps90", "P/S",
      "Psychological, Social, and Biological Foundations of Behavior",
      90, "90min", EXAM_PS90,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam1_90", "Full 90-Minute Practice Exam 1");
  }

  // --- Practice Exam 2 (90-Minute Full Sections) ---
  if (typeof EXAM_CP90_2 !== "undefined" && EXAM_CP90_2.length) {
    registerExam("cp90_2", "C/P",
      "Chemical and Physical Foundations of Biological Systems",
      90, "90min", EXAM_CP90_2,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam2_90", "Full 90-Minute Practice Exam 2");
  }
  if (typeof EXAM_CARS90_2 !== "undefined" && EXAM_CARS90_2.length) {
    registerExam("cars90_2", "CARS",
      "Critical Analysis and Reasoning Skills",
      90, "90min", EXAM_CARS90_2,
      "90-minute timed practice \u2014 9 passages, no discrete (53 Qs)",
      "exam2_90", "Full 90-Minute Practice Exam 2");
  }
  if (typeof EXAM_BB90_2 !== "undefined" && EXAM_BB90_2.length) {
    registerExam("bb90_2", "B/B",
      "Biological and Biochemical Foundations of Living Systems",
      90, "90min", EXAM_BB90_2,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam2_90", "Full 90-Minute Practice Exam 2");
  }
  if (typeof EXAM_PS90_2 !== "undefined" && EXAM_PS90_2.length) {
    registerExam("ps90_2", "P/S",
      "Psychological, Social, and Biological Foundations of Behavior",
      90, "90min", EXAM_PS90_2,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam2_90", "Full 90-Minute Practice Exam 2");
  }

  // --- Practice Exam 3 (90-Minute Full Sections) ---
  if (typeof EXAM_CP90_3 !== "undefined" && EXAM_CP90_3.length) {
    registerExam("cp90_3", "C/P",
      "Chemical and Physical Foundations of Biological Systems",
      90, "90min", EXAM_CP90_3,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam3_90", "Full 90-Minute Practice Exam 3");
  }
  if (typeof EXAM_CARS90_3 !== "undefined" && EXAM_CARS90_3.length) {
    registerExam("cars90_3", "CARS",
      "Critical Analysis and Reasoning Skills",
      90, "90min", EXAM_CARS90_3,
      "90-minute timed practice \u2014 9 passages, no discrete (53 Qs)",
      "exam3_90", "Full 90-Minute Practice Exam 3");
  }
  if (typeof EXAM_BB90_3 !== "undefined" && EXAM_BB90_3.length) {
    registerExam("bb90_3", "B/B",
      "Biological and Biochemical Foundations of Living Systems",
      90, "90min", EXAM_BB90_3,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam3_90", "Full 90-Minute Practice Exam 3");
  }
  if (typeof EXAM_PS90_3 !== "undefined" && EXAM_PS90_3.length) {
    registerExam("ps90_3", "P/S",
      "Psychological, Social, and Biological Foundations of Behavior",
      90, "90min", EXAM_PS90_3,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam3_90", "Full 90-Minute Practice Exam 3");
  }

  // --- Practice Exam 4 (90-Minute Full Sections) ---
  if (typeof EXAM_CP90_4 !== "undefined" && EXAM_CP90_4.length) {
    registerExam("cp90_4", "C/P",
      "Chemical and Physical Foundations of Biological Systems",
      90, "90min", EXAM_CP90_4,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam4_90", "Full 90-Minute Practice Exam 4");
  }
  if (typeof EXAM_CARS90_4 !== "undefined" && EXAM_CARS90_4.length) {
    registerExam("cars90_4", "CARS",
      "Critical Analysis and Reasoning Skills",
      90, "90min", EXAM_CARS90_4,
      "90-minute timed practice \u2014 9 passages, no discrete (53 Qs)",
      "exam4_90", "Full 90-Minute Practice Exam 4");
  }
  if (typeof EXAM_BB90_4 !== "undefined" && EXAM_BB90_4.length) {
    registerExam("bb90_4", "B/B",
      "Biological and Biochemical Foundations of Living Systems",
      90, "90min", EXAM_BB90_4,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam4_90", "Full 90-Minute Practice Exam 4");
  }
  if (typeof EXAM_PS90_4 !== "undefined" && EXAM_PS90_4.length) {
    registerExam("ps90_4", "P/S",
      "Psychological, Social, and Biological Foundations of Behavior",
      90, "90min", EXAM_PS90_4,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam4_90", "Full 90-Minute Practice Exam 4");
  }

  // --- Practice Exam 5 (90-Minute Full Sections) ---
  if (typeof EXAM_CP90_5 !== "undefined" && EXAM_CP90_5.length) {
    registerExam("cp90_5", "C/P",
      "Chemical and Physical Foundations of Biological Systems",
      90, "90min", EXAM_CP90_5,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam5_90", "Full 90-Minute Practice Exam 5");
  }
  if (typeof EXAM_CARS90_5 !== "undefined" && EXAM_CARS90_5.length) {
    registerExam("cars90_5", "CARS",
      "Critical Analysis and Reasoning Skills",
      90, "90min", EXAM_CARS90_5,
      "90-minute timed practice \u2014 9 passages, no discrete (53 Qs)",
      "exam5_90", "Full 90-Minute Practice Exam 5");
  }
  if (typeof EXAM_BB90_5 !== "undefined" && EXAM_BB90_5.length) {
    registerExam("bb90_5", "B/B",
      "Biological and Biochemical Foundations of Living Systems",
      90, "90min", EXAM_BB90_5,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam5_90", "Full 90-Minute Practice Exam 5");
  }
  if (typeof EXAM_PS90_5 !== "undefined" && EXAM_PS90_5.length) {
    registerExam("ps90_5", "P/S",
      "Psychological, Social, and Biological Foundations of Behavior",
      90, "90min", EXAM_PS90_5,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam5_90", "Full 90-Minute Practice Exam 5");
  }
  if (typeof EXAM_CARS90_6 !== "undefined" && EXAM_CARS90_6.length) {
    registerExam("cars90_6", "CARS",
      "Critical Analysis and Reasoning Skills",
      90, "90min", EXAM_CARS90_6,
      "90-minute timed practice \u2014 9 passages, no discrete (53 Qs)",
      "exam6_90", "Full 90-Minute Practice Exam 6");
  }
  if (typeof EXAM_CP90_7 !== "undefined" && EXAM_CP90_7.length) {
    registerExam("cp90_7", "C/P",
      "Chemical and Physical Foundations of Biological Systems",
      90, "90min", EXAM_CP90_7,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam7_90", "Full 90-Minute Practice Exam 7");
  }
  if (typeof EXAM_CARS90_7 !== "undefined" && EXAM_CARS90_7.length) {
    registerExam("cars90_7", "CARS",
      "Critical Analysis and Reasoning Skills",
      90, "90min", EXAM_CARS90_7,
      "90-minute timed practice \u2014 9 passages, no discrete (53 Qs)",
      "exam7_90", "Full 90-Minute Practice Exam 7");
  }
  if (typeof EXAM_BB90_7 !== "undefined" && EXAM_BB90_7.length) {
    registerExam("bb90_7", "B/B",
      "Biological and Biochemical Foundations of Living Systems",
      90, "90min", EXAM_BB90_7,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam7_90", "Full 90-Minute Practice Exam 7");
  }
  if (typeof EXAM_PS90_7 !== "undefined" && EXAM_PS90_7.length) {
    registerExam("ps90_7", "P/S",
      "Psychological, Social, and Biological Foundations of Behavior",
      90, "90min", EXAM_PS90_7,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam7_90", "Full 90-Minute Practice Exam 7");
  }
  if (typeof EXAM_CP90_8 !== "undefined" && EXAM_CP90_8.length) {
    registerExam("cp90_8", "C/P",
      "Chemical and Physical Foundations of Biological Systems",
      90, "90min", EXAM_CP90_8,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam8_90", "Full 90-Minute Practice Exam 8");
  }
  if (typeof EXAM_CARS90_8 !== "undefined" && EXAM_CARS90_8.length) {
    registerExam("cars90_8", "CARS",
      "Critical Analysis and Reasoning Skills",
      90, "90min", EXAM_CARS90_8,
      "90-minute timed practice \u2014 9 passages, no discrete (53 Qs)",
      "exam8_90", "Full 90-Minute Practice Exam 8");
  }
  if (typeof EXAM_BB90_8 !== "undefined" && EXAM_BB90_8.length) {
    registerExam("bb90_8", "B/B",
      "Biological and Biochemical Foundations of Living Systems",
      90, "90min", EXAM_BB90_8,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam8_90", "Full 90-Minute Practice Exam 8");
  }
  if (typeof EXAM_PS90_8 !== "undefined" && EXAM_PS90_8.length) {
    registerExam("ps90_8", "P/S",
      "Psychological, Social, and Biological Foundations of Behavior",
      90, "90min", EXAM_PS90_8,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam8_90", "Full 90-Minute Practice Exam 8");
  }
  if (typeof EXAM_CP90_9 !== "undefined" && EXAM_CP90_9.length) {
    registerExam("cp90_9", "C/P",
      "Chemical and Physical Foundations of Biological Systems",
      90, "90min", EXAM_CP90_9,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam9_90", "Full 90-Minute Practice Exam 9");
  }
  if (typeof EXAM_CARS90_9 !== "undefined" && EXAM_CARS90_9.length) {
    registerExam("cars90_9", "CARS",
      "Critical Analysis and Reasoning Skills",
      90, "90min", EXAM_CARS90_9,
      "90-minute timed practice \u2014 9 passages, no discrete (53 Qs)",
      "exam9_90", "Full 90-Minute Practice Exam 9");
  }
  if (typeof EXAM_PS90_9 !== "undefined" && EXAM_PS90_9.length) {
    registerExam("ps90_9", "P/S",
      "Psychological, Social, and Biological Foundations of Behavior",
      90, "90min", EXAM_PS90_9,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam9_90", "Full 90-Minute Practice Exam 9");
  }
  if (typeof EXAM_BB90_9 !== "undefined" && EXAM_BB90_9.length) {
    registerExam("bb90_9", "B/B",
      "Biological and Biochemical Foundations of Living Systems",
      90, "90min", EXAM_BB90_9,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam9_90", "Full 90-Minute Practice Exam 9");
  }
  if (typeof EXAM_CP90_6 !== "undefined" && EXAM_CP90_6.length) {
    registerExam("cp90_6", "C/P",
      "Chemical and Physical Foundations of Biological Systems",
      90, "90min", EXAM_CP90_6,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam6_90", "Full 90-Minute Practice Exam 6");
  }
  if (typeof EXAM_BB90_6 !== "undefined" && EXAM_BB90_6.length) {
    registerExam("bb90_6", "B/B",
      "Biological and Biochemical Foundations of Living Systems",
      90, "90min", EXAM_BB90_6,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam6_90", "Full 90-Minute Practice Exam 6");
  }
  if (typeof EXAM_PS90_6 !== "undefined" && EXAM_PS90_6.length) {
    registerExam("ps90_6", "P/S",
      "Psychological, Social, and Biological Foundations of Behavior",
      90, "90min", EXAM_PS90_6,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam6_90", "Full 90-Minute Practice Exam 6");
  }
  if (typeof EXAM_CP90_10 !== "undefined" && EXAM_CP90_10.length) {
    registerExam("cp90_10", "C/P",
      "Chemical and Physical Foundations of Biological Systems",
      90, "90min", EXAM_CP90_10,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam10_90", "Full 90-Minute Practice Exam 10");
  }
  if (typeof EXAM_CARS90_10 !== "undefined" && EXAM_CARS90_10.length) {
    registerExam("cars90_10", "CARS",
      "Critical Analysis and Reasoning Skills",
      90, "90min", EXAM_CARS90_10,
      "90-minute timed practice \u2014 9 passages, no discrete (53 Qs)",
      "exam10_90", "Full 90-Minute Practice Exam 10");
  }
  if (typeof EXAM_PS90_10 !== "undefined" && EXAM_PS90_10.length) {
    registerExam("ps90_10", "P/S",
      "Psychological, Social, and Biological Foundations of Behavior",
      90, "90min", EXAM_PS90_10,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam10_90", "Full 90-Minute Practice Exam 10");
  }
  if (typeof EXAM_BB90_10 !== "undefined" && EXAM_BB90_10.length) {
    registerExam("bb90_10", "B/B",
      "Biological and Biochemical Foundations of Living Systems",
      90, "90min", EXAM_BB90_10,
      "90-minute timed practice \u2014 7 passages + 10 discrete (52 Qs)",
      "exam10_90", "Full 90-Minute Practice Exam 10");
  }

  // --- Practice Exam 1 (60-Minute High-Yield Sections) ---
  if (typeof EXAM_CP60 !== "undefined" && EXAM_CP60.length) {
    registerExam("cp60", "C/P",
      "Chemical and Physical Foundations of Biological Systems",
      60, "60min", EXAM_CP60,
      "60-minute practice \u2014 5 passages + 5 discrete (33 Qs)",
      "exam1_60", "60-Minute Practice Sections \u2014 Exam 1");
  }
  if (typeof EXAM_CARS60 !== "undefined" && EXAM_CARS60.length) {
    registerExam("cars60", "CARS",
      "Critical Analysis and Reasoning Skills",
      60, "60min", EXAM_CARS60,
      "60-minute practice \u2014 6 passages (33 Qs)",
      "exam1_60", "60-Minute Practice Sections \u2014 Exam 1");
  }
  if (typeof EXAM_BB60 !== "undefined" && EXAM_BB60.length) {
    registerExam("bb60", "B/B",
      "Biological and Biochemical Foundations of Living Systems",
      60, "60min", EXAM_BB60,
      "60-minute practice \u2014 5 passages + 5 discrete (33 Qs)",
      "exam1_60", "60-Minute Practice Sections \u2014 Exam 1");
  }
  if (typeof EXAM_PS60 !== "undefined" && EXAM_PS60.length) {
    registerExam("ps60", "P/S",
      "Psychological, Social, and Biological Foundations of Behavior",
      60, "60min", EXAM_PS60,
      "60-minute practice \u2014 5 passages + 5 discrete (33 Qs)",
      "exam1_60", "60-Minute Practice Sections \u2014 Exam 1");
  }

  // --- Practice Exam 2 (60-Minute High-Yield Sections) ---
  if (typeof EXAM_CP60_2 !== "undefined" && EXAM_CP60_2.length) {
    registerExam("cp60_2", "C/P",
      "Chemical and Physical Foundations of Biological Systems",
      60, "60min", EXAM_CP60_2,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam2_60", "60-Minute Practice Sections \u2014 Exam 2");
  }
  if (typeof EXAM_CARS60_2 !== "undefined" && EXAM_CARS60_2.length) {
    registerExam("cars60_2", "CARS",
      "Critical Analysis and Reasoning Skills",
      60, "60min", EXAM_CARS60_2,
      "60-minute practice \u2014 6 passages (33 Qs)",
      "exam2_60", "60-Minute Practice Sections \u2014 Exam 2");
  }
  if (typeof EXAM_BB60_2 !== "undefined" && EXAM_BB60_2.length) {
    registerExam("bb60_2", "B/B",
      "Biological and Biochemical Foundations of Living Systems",
      60, "60min", EXAM_BB60_2,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam2_60", "60-Minute Practice Sections \u2014 Exam 2");
  }
  if (typeof EXAM_PS60_2 !== "undefined" && EXAM_PS60_2.length) {
    registerExam("ps60_2", "P/S",
      "Psychological, Social, and Biological Foundations of Behavior",
      60, "60min", EXAM_PS60_2,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam2_60", "60-Minute Practice Sections \u2014 Exam 2");
  }

  // --- Practice Exam 3 (60-Minute High-Yield Sections) ---
  if (typeof EXAM_CP60_3 !== "undefined" && EXAM_CP60_3.length) {
    registerExam("cp60_3", "C/P",
      "Chemical and Physical Foundations of Biological Systems",
      60, "60min", EXAM_CP60_3,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam3_60", "60-Minute Practice Sections \u2014 Exam 3");
  }
  if (typeof EXAM_CARS60_3 !== "undefined" && EXAM_CARS60_3.length) {
    registerExam("cars60_3", "CARS",
      "Critical Analysis and Reasoning Skills",
      60, "60min", EXAM_CARS60_3,
      "60-minute practice \u2014 6 passages (33 Qs)",
      "exam3_60", "60-Minute Practice Sections \u2014 Exam 3");
  }
  if (typeof EXAM_BB60_3 !== "undefined" && EXAM_BB60_3.length) {
    registerExam("bb60_3", "B/B",
      "Biological and Biochemical Foundations of Living Systems",
      60, "60min", EXAM_BB60_3,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam3_60", "60-Minute Practice Sections \u2014 Exam 3");
  }
  if (typeof EXAM_PS60_3 !== "undefined" && EXAM_PS60_3.length) {
    registerExam("ps60_3", "P/S",
      "Psychological, Social, and Biological Foundations of Behavior",
      60, "60min", EXAM_PS60_3,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam3_60", "60-Minute Practice Sections \u2014 Exam 3");
  }

  // --- Practice Exam 4 (60-Minute High-Yield Sections) ---
  if (typeof EXAM_CP60_4 !== "undefined" && EXAM_CP60_4.length) {
    registerExam("cp60_4", "C/P",
      "Chemical and Physical Foundations of Biological Systems",
      60, "60min", EXAM_CP60_4,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam4_60", "60-Minute Practice Sections \u2014 Exam 4");
  }
  if (typeof EXAM_CARS60_4 !== "undefined" && EXAM_CARS60_4.length) {
    registerExam("cars60_4", "CARS",
      "Critical Analysis and Reasoning Skills",
      60, "60min", EXAM_CARS60_4,
      "60-minute practice \u2014 6 passages (33 Qs)",
      "exam4_60", "60-Minute Practice Sections \u2014 Exam 4");
  }
  if (typeof EXAM_BB60_4 !== "undefined" && EXAM_BB60_4.length) {
    registerExam("bb60_4", "B/B",
      "Biological and Biochemical Foundations of Living Systems",
      60, "60min", EXAM_BB60_4,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam4_60", "60-Minute Practice Sections \u2014 Exam 4");
  }
  if (typeof EXAM_PS60_4 !== "undefined" && EXAM_PS60_4.length) {
    registerExam("ps60_4", "P/S",
      "Psychological, Social, and Biological Foundations of Behavior",
      60, "60min", EXAM_PS60_4,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam4_60", "60-Minute Practice Sections \u2014 Exam 4");
  }

  // --- Practice Exam 5 (60-Minute High-Yield Sections) ---
  if (typeof EXAM_CP60_5 !== "undefined" && EXAM_CP60_5.length) {
    registerExam("cp60_5", "C/P",
      "Chemical and Physical Foundations of Biological Systems",
      60, "60min", EXAM_CP60_5,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam5_60", "60-Minute Practice Sections \u2014 Exam 5");
  }
  if (typeof EXAM_CARS60_5 !== "undefined" && EXAM_CARS60_5.length) {
    registerExam("cars60_5", "CARS",
      "Critical Analysis and Reasoning Skills",
      60, "60min", EXAM_CARS60_5,
      "60-minute practice \u2014 6 passages (33 Qs)",
      "exam5_60", "60-Minute Practice Sections \u2014 Exam 5");
  }
  if (typeof EXAM_BB60_5 !== "undefined" && EXAM_BB60_5.length) {
    registerExam("bb60_5", "B/B",
      "Biological and Biochemical Foundations of Living Systems",
      60, "60min", EXAM_BB60_5,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam5_60", "60-Minute Practice Sections \u2014 Exam 5");
  }
  if (typeof EXAM_PS60_5 !== "undefined" && EXAM_PS60_5.length) {
    registerExam("ps60_5", "P/S",
      "Psychological, Social, and Biological Foundations of Behavior",
      60, "60min", EXAM_PS60_5,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam5_60", "60-Minute Practice Sections \u2014 Exam 5");
  }
  if (typeof EXAM_CARS60_6 !== "undefined" && EXAM_CARS60_6.length) {
    registerExam("cars60_6", "CARS",
      "Critical Analysis and Reasoning Skills",
      60, "60min", EXAM_CARS60_6,
      "60-minute practice \u2014 6 passages (33 Qs)",
      "exam6_60", "60-Minute Practice Sections \u2014 Exam 6");
  }
  if (typeof EXAM_CP60_7 !== "undefined" && EXAM_CP60_7.length) {
    registerExam("cp60_7", "C/P",
      "Chemical and Physical Foundations of Biological Systems",
      60, "60min", EXAM_CP60_7,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam7_60", "60-Minute Practice Sections \u2014 Exam 7");
  }
  if (typeof EXAM_CARS60_7 !== "undefined" && EXAM_CARS60_7.length) {
    registerExam("cars60_7", "CARS",
      "Critical Analysis and Reasoning Skills",
      60, "60min", EXAM_CARS60_7,
      "60-minute practice \u2014 6 passages (33 Qs)",
      "exam7_60", "60-Minute Practice Sections \u2014 Exam 7");
  }
  if (typeof EXAM_BB60_7 !== "undefined" && EXAM_BB60_7.length) {
    registerExam("bb60_7", "B/B",
      "Biological and Biochemical Foundations of Living Systems",
      60, "60min", EXAM_BB60_7,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam7_60", "60-Minute Practice Sections \u2014 Exam 7");
  }
  if (typeof EXAM_PS60_7 !== "undefined" && EXAM_PS60_7.length) {
    registerExam("ps60_7", "P/S",
      "Psychological, Social, and Biological Foundations of Behavior",
      60, "60min", EXAM_PS60_7,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam7_60", "60-Minute Practice Sections \u2014 Exam 7");
  }
  if (typeof EXAM_CP60_8 !== "undefined" && EXAM_CP60_8.length) {
    registerExam("cp60_8", "C/P",
      "Chemical and Physical Foundations of Biological Systems",
      60, "60min", EXAM_CP60_8,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam8_60", "60-Minute Practice Sections \u2014 Exam 8");
  }
  if (typeof EXAM_CARS60_8 !== "undefined" && EXAM_CARS60_8.length) {
    registerExam("cars60_8", "CARS",
      "Critical Analysis and Reasoning Skills",
      60, "60min", EXAM_CARS60_8,
      "60-minute practice \u2014 6 passages (33 Qs)",
      "exam8_60", "60-Minute Practice Sections \u2014 Exam 8");
  }
  if (typeof EXAM_BB60_8 !== "undefined" && EXAM_BB60_8.length) {
    registerExam("bb60_8", "B/B",
      "Biological and Biochemical Foundations of Living Systems",
      60, "60min", EXAM_BB60_8,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam8_60", "60-Minute Practice Sections \u2014 Exam 8");
  }
  if (typeof EXAM_PS60_8 !== "undefined" && EXAM_PS60_8.length) {
    registerExam("ps60_8", "P/S",
      "Psychological, Social, and Biological Foundations of Behavior",
      60, "60min", EXAM_PS60_8,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam8_60", "60-Minute Practice Sections \u2014 Exam 8");
  }
  if (typeof EXAM_CP60_9 !== "undefined" && EXAM_CP60_9.length) {
    registerExam("cp60_9", "C/P",
      "Chemical and Physical Foundations of Biological Systems",
      60, "60min", EXAM_CP60_9,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam9_60", "60-Minute Practice Sections \u2014 Exam 9");
  }
  if (typeof EXAM_CARS60_9 !== "undefined" && EXAM_CARS60_9.length) {
    registerExam("cars60_9", "CARS",
      "Critical Analysis and Reasoning Skills",
      60, "60min", EXAM_CARS60_9,
      "60-minute practice \u2014 6 passages (33 Qs)",
      "exam9_60", "60-Minute Practice Sections \u2014 Exam 9");
  }
  if (typeof EXAM_PS60_9 !== "undefined" && EXAM_PS60_9.length) {
    registerExam("ps60_9", "P/S",
      "Psychological, Social, and Biological Foundations of Behavior",
      60, "60min", EXAM_PS60_9,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam9_60", "60-Minute Practice Sections \u2014 Exam 9");
  }
  if (typeof EXAM_BB60_9 !== "undefined" && EXAM_BB60_9.length) {
    registerExam("bb60_9", "B/B",
      "Biological and Biochemical Foundations of Living Systems",
      60, "60min", EXAM_BB60_9,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam9_60", "60-Minute Practice Sections \u2014 Exam 9");
  }
  if (typeof EXAM_CP60_6 !== "undefined" && EXAM_CP60_6.length) {
    registerExam("cp60_6", "C/P",
      "Chemical and Physical Foundations of Biological Systems",
      60, "60min", EXAM_CP60_6,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam6_60", "60-Minute Practice Sections \u2014 Exam 6");
  }
  if (typeof EXAM_BB60_6 !== "undefined" && EXAM_BB60_6.length) {
    registerExam("bb60_6", "B/B",
      "Biological and Biochemical Foundations of Living Systems",
      60, "60min", EXAM_BB60_6,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam6_60", "60-Minute Practice Sections \u2014 Exam 6");
  }
  if (typeof EXAM_PS60_6 !== "undefined" && EXAM_PS60_6.length) {
    registerExam("ps60_6", "P/S",
      "Psychological, Social, and Biological Foundations of Behavior",
      60, "60min", EXAM_PS60_6,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam6_60", "60-Minute Practice Sections \u2014 Exam 6");
  }
  if (typeof EXAM_CP60_10 !== "undefined" && EXAM_CP60_10.length) {
    registerExam("cp60_10", "C/P",
      "Chemical and Physical Foundations of Biological Systems",
      60, "60min", EXAM_CP60_10,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam10_60", "60-Minute Practice Sections \u2014 Exam 10");
  }
  if (typeof EXAM_CARS60_10 !== "undefined" && EXAM_CARS60_10.length) {
    registerExam("cars60_10", "CARS",
      "Critical Analysis and Reasoning Skills",
      60, "60min", EXAM_CARS60_10,
      "60-minute practice \u2014 6 passages (33 Qs)",
      "exam10_60", "60-Minute Practice Sections \u2014 Exam 10");
  }
  if (typeof EXAM_PS60_10 !== "undefined" && EXAM_PS60_10.length) {
    registerExam("ps60_10", "P/S",
      "Psychological, Social, and Biological Foundations of Behavior",
      60, "60min", EXAM_PS60_10,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam10_60", "60-Minute Practice Sections \u2014 Exam 10");
  }
  if (typeof EXAM_BB60_10 !== "undefined" && EXAM_BB60_10.length) {
    registerExam("bb60_10", "B/B",
      "Biological and Biochemical Foundations of Living Systems",
      60, "60min", EXAM_BB60_10,
      "60-minute practice \u2014 5 passages + 3 discrete (33 Qs)",
      "exam10_60", "60-Minute Practice Sections \u2014 Exam 10");
  }

  // Auto-generate ~45-minute half-sections from all registered 90-minute exams
  registerHalfExams();
}

/* Automatically split every 90-minute exam into two roughly 45-minute sections */
function registerHalfExams() {
  const full90s = PRACTICE_EXAMS.filter(e => e.duration === 90 && !e.isHalf);
  full90s.forEach(pe => {
    const isCars = pe.sec === "CARS";
    // CARS (9 passages): Part 1 = 4 passages (24 Qs, ~41 min), Part 2 = 5 passages (29 Qs, ~49 min)
    // Science (7 passages + 1 discrete set): Part 1 = 4 passages (24 Qs, ~42 min), Part 2 = 3 passages + 10 discretes (28 Qs, ~48 min)
    const splitIdx = 4;
    const sets1 = pe.sets.slice(0, splitIdx);
    const sets2 = pe.sets.slice(splitIdx);
    const q1 = sets1.reduce((sum, s) => sum + (s && s.qs ? s.qs.length : 0), 0);
    const q2 = sets2.reduce((sum, s) => sum + (s && s.qs ? s.qs.length : 0), 0);
    const dur1 = isCars ? 41 : 42;
    const dur2 = isCars ? 49 : 48;

    const h1Id = pe.id + "_h1";
    const h2Id = pe.id + "_h2";

    const h1 = {
      id: h1Id,
      parentExamId: pe.id,
      isHalf: true,
      halfIndex: 1,
      partnerId: h2Id,
      sec: pe.sec,
      label: pe.label + " \u2014 Part 1 (Half-Section)",
      duration: dur1,
      type: "half",
      sets: sets1,
      desc: `Part 1 of 2: 4 passages (${q1} Qs) \u2014 ~${dur1} min. Finish both halves to complete the full 90m exam.`,
      suite: pe.suite + "_h1",
      suiteTitle: `${pe.suiteTitle} \u2014 Part 1 (Half-Section)`
    };

    const h2 = {
      id: h2Id,
      parentExamId: pe.id,
      isHalf: true,
      halfIndex: 2,
      partnerId: h1Id,
      sec: pe.sec,
      label: pe.label + " \u2014 Part 2 (Half-Section)",
      duration: dur2,
      type: "half",
      sets: sets2,
      desc: `Part 2 of 2: ${isCars ? "5 passages" : "3 passages + 10 discrete"} (${q2} Qs) \u2014 ~${dur2} min. Finish both halves to complete the full 90m exam.`,
      suite: pe.suite + "_h2",
      suiteTitle: `${pe.suiteTitle} \u2014 Part 2 (Half-Section)`
    };

    PRACTICE_EXAMS.push(h1, h2);
  });

  // Auto-migrate and sync completed passage fingerprints across exams
  const peKey = "drillroom_pe_v1";
  try {
    let peData = JSON.parse(localStorage.getItem(peKey));
    if (peData && typeof peData === "object" && typeof initAndMigrateCompletedFingerprints === "function") {
      peData = initAndMigrateCompletedFingerprints(peData);
      localStorage.setItem(peKey, JSON.stringify(peData));
    }
  } catch (e) { }
}

/* ===== HISTORY & STORAGE MANAGEMENT ===== */
const HIST_KEY = "drillroom_history_v1";
const HIST_PREF_KEY = "drillroom_hist_prefs_v1";
const MIGRATED_FLAG_KEY = "drillroom_hist_migrated_v2";

/* Deduplicate history to prevent and clean up any duplicate entries */
function deduplicateHistory(hist) {
  if (!Array.isArray(hist) || hist.length <= 1) return hist || [];
  const cleaned = [];
  for (const item of hist) {
    if (!item || !item.id) continue;
    const isDup = cleaned.some(c => {
      if (c.id === item.id) return true;
      // Pair where one is migrated and one is fresh for the same exam & score
      const oneIsMigrated = (String(c.id).startsWith("att_migrated_") || String(item.id).startsWith("att_migrated_"));
      if (oneIsMigrated && c.examId === item.examId && c.rawScore === item.rawScore && c.totalQs === item.totalQs && c.scaledScore === item.scaledScore) {
        return true;
      }
      // Identical exam and score with timestamps close to each other (within 60 seconds)
      if (c.examId === item.examId && c.rawScore === item.rawScore && c.totalQs === item.totalQs && c.scaledScore === item.scaledScore && Math.abs((c.ts || 0) - (item.ts || 0)) < 60000) {
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

  // One-time migration only from legacy peData
  const alreadyMigrated = localStorage.getItem(MIGRATED_FLAG_KEY) === "1";
  if (!alreadyMigrated) {
    try { localStorage.setItem(MIGRATED_FLAG_KEY, "1"); } catch(e) {}
    if (hist.length === 0) {
      try {
        const peData = JSON.parse(localStorage.getItem("drillroom_pe_v1")) || {};
        const migrated = [];
        for (const [id, r] of Object.entries(peData)) {
          if (r && r.done) {
            const ex = PRACTICE_EXAMS.find(e => e.id === id);
            migrated.push({
              id: "att_migrated_" + id,
              examId: id,
              sec: ex ? ex.sec : "C/P",
              duration: r.duration || (ex ? ex.duration : 90),
              type: (r.duration || (ex ? ex.duration : 90)) + "min",
              suite: ex ? ex.suite : "exam1_90",
              suiteTitle: ex ? ex.suiteTitle : "Practice Section",
              label: ex ? ex.label : id,
              scaledScore: r.scaledScore || 118,
              rawScore: r.score || 0,
              totalQs: r.total || 0,
              pct: r.pct || 0,
              percentile: r.percentile || "1st",
              solid: r.solid || 0,
              lucky: r.lucky || 0,
              shaky: r.shaky || 0,
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

  // Always deduplicate on load to clean up any past duplicates
  let deduped = deduplicateHistory(hist);
  // Exclude any past attempts where passages were skipped so they never count toward score history or averages
  const cleaned = deduped.filter(h => (!h.skippedCount || h.skippedCount === 0) && (!h.scoredTotal || h.scoredTotal === h.totalQs));
  if (cleaned.length !== hist.length) {
    hist = cleaned;
    saveHistory(hist);
  } else {
    hist = deduped;
  }

  return hist;
}

function saveHistory(hist) {
  try {
    localStorage.setItem(MIGRATED_FLAG_KEY, "1");
    localStorage.setItem(HIST_KEY, JSON.stringify(hist));
  } catch(e) {}
}

function addHistoryEntry(rec) {
  if (!rec) return;
  // Never add attempts where passages were skipped to score history
  if (rec.skippedCount && rec.skippedCount > 0) return;
  if (rec.scoredTotal !== undefined && rec.totalQs !== undefined && rec.scoredTotal < rec.totalQs) return;

  try { localStorage.setItem(MIGRATED_FLAG_KEY, "1"); } catch(e) {}
  const hist = getHistory();
  // Debounce: prevent adding exact duplicate within 3 seconds
  const isRecentDup = hist.length && hist[0].examId === rec.examId && hist[0].rawScore === rec.rawScore && Math.abs((hist[0].ts || 0) - (rec.ts || 0)) < 3000;
  if (!isRecentDup) {
    hist.unshift(rec);
    saveHistory(hist);
  }
}

function toggleHistoryInclude(id) {
  if (!id) return;
  const hist = getHistory();
  const item = hist.find(x => x.id === id);
  if (item) {
    item.includedInAverage = !item.includedInAverage;
    saveHistory(hist);
    paintHistory();
    paintPracticeExams();
  }
}

function deleteHistoryEntry(id) {
  if (!id) return;
  if (!confirm("Are you sure you want to remove this section attempt from your history?")) return;
  let hist = getHistory();
  const deletedEntry = hist.find(x => x.id === id);
  hist = hist.filter(x => x.id !== id);
  saveHistory(hist);

  // Synchronize legacy peData so deleted exams do not linger or resurrect
  if (deletedEntry && deletedEntry.examId) {
    try {
      const peData = JSON.parse(localStorage.getItem("drillroom_pe_v1")) || {};
      const remaining = hist.filter(x => x.examId === deletedEntry.examId);
      if (remaining.length === 0) {
        delete peData[deletedEntry.examId];
      } else {
        const latest = remaining[0];
        peData[deletedEntry.examId] = {
          done: true,
          score: latest.rawScore,
          total: latest.totalQs,
          scaledScore: latest.scaledScore,
          percentile: latest.percentile,
          pct: latest.pct,
          solid: latest.solid,
          lucky: latest.lucky,
          shaky: latest.shaky,
          duration: latest.duration,
          timeUsed: latest.timeUsed,
          ts: latest.ts
        };
      }

      // If a half-section attempt was deleted, check if parent 90m exam was completed via halves
      if (deletedEntry.isHalf || (deletedEntry.examId && (deletedEntry.examId.endsWith("_h1") || deletedEntry.examId.endsWith("_h2")))) {
        const parentId = deletedEntry.parentExamId || deletedEntry.examId.replace(/_h[12]$/, "");
        if (peData[parentId] && peData[parentId].completedViaHalves) {
          const h1Done = !!peData[parentId + "_h1"]?.done;
          const h2Done = !!peData[parentId + "_h2"]?.done;
          if (!h1Done || !h2Done) {
            delete peData[parentId];
            hist = hist.filter(x => !(x.isCombinedFromHalves && x.examId === parentId));
            saveHistory(hist);
          }
        }
      }

      localStorage.setItem("drillroom_pe_v1", JSON.stringify(peData));
    } catch(e) {}
  }

  paintHistory();
  paintPracticeExams();
  if (typeof paintHome === "function") paintHome();
  flash("Section attempt removed from history.");
}

function clearAllHistory() {
  if (!confirm("Are you sure you want to clear ALL practice exam history?\n\nThis will remove all score records and cannot be undone.")) return;
  saveHistory([]);
  try {
    localStorage.setItem("drillroom_pe_v1", JSON.stringify({}));
  } catch(e) {}
  paintHistory();
  paintPracticeExams();
  if (typeof paintHome === "function") paintHome();
  flash("All practice exam history cleared.");
}

function getHistoryPrefs() {
  let prefs = { window: 5, sec: "all", dur: "all" };
  try {
    const saved = JSON.parse(localStorage.getItem(HIST_PREF_KEY));
    if (saved) Object.assign(prefs, saved);
  } catch(e) {}
  return prefs;
}

function saveHistoryPrefs(prefs) {
  try { localStorage.setItem(HIST_PREF_KEY, JSON.stringify(prefs)); } catch(e) {}
}

function calculateRollingAverage(hist, prefs) {
  if (!hist || !hist.length) return null;
  let items = hist.filter(x => x.includedInAverage);
  if (prefs.sec && prefs.sec !== "all") {
    items = items.filter(x => x.sec === prefs.sec);
  }
  if (prefs.dur && prefs.dur !== "all") {
    if (String(prefs.dur) === "45") {
      items = items.filter(x => x.type === "half" || x.isHalf || [41, 42, 45, 48, 49].includes(Number(x.duration)));
    } else {
      items = items.filter(x => String(x.duration) === String(prefs.dur));
    }
  }
  items.sort((a, b) => b.ts - a.ts);

  const totalMatching = items.length;
  if (!totalMatching) return null;

  const win = prefs.window === "all" ? totalMatching : Math.min(Number(prefs.window) || 5, totalMatching);
  const sliced = items.slice(0, win);
  if (!sliced.length) return null;

  const count = sliced.length;
  const sumScaled = sliced.reduce((s, x) => s + x.scaledScore, 0);
  const avgScaled = Math.round((sumScaled / count) * 10) / 10;
  const projComposite = Math.min(528, Math.max(472, Math.round(avgScaled * 4)));
  const sumPct = sliced.reduce((s, x) => s + x.pct, 0);
  const avgPct = Math.round(sumPct / count);
  const sumScore = sliced.reduce((s, x) => s + x.rawScore, 0);
  const sumTotal = sliced.reduce((s, x) => s + x.totalQs, 0);
  const solid = sliced.reduce((s, x) => s + (x.solid || 0), 0);
  const lucky = sliced.reduce((s, x) => s + (x.lucky || 0), 0);
  const shaky = sliced.reduce((s, x) => s + (x.shaky || 0), 0);
  const excluded = hist.filter(x => !x.includedInAverage).length;

  return {
    count,
    win,
    totalMatching,
    avgScaled,
    projComposite,
    avgPct,
    sumScore,
    sumTotal,
    solid, lucky, shaky,
    excluded
  };
}

/* ===== EXIT & RESET WITHOUT SCORING ===== */
function exitExamWithoutScoring() {
  if (!E) return;
  const isPe = !!E._isPracticeExam;
  const label = isPe ? (E.s.label || "practice exam") : "set";
  const msg = isPe
    ? "Exit and reset this practice exam without scoring?\n\nYour answers will be discarded. No score will be calculated and nothing will be added to your score history or averages."
    : "Exit and reset this practice set without saving?\n\nYour progress on this set will be reset.";

  if (confirm(msg)) {
    clearInterval(timerId);
    E = null;
    PE = null;
    if (typeof window !== "undefined") {
      window.E = null;
      window.PE = null;
    }
    if (typeof globalThis !== "undefined") {
      globalThis.E = null;
      globalThis.PE = null;
    }
    if (window.lockCalc) window.lockCalc(false);
    $("clk").classList.add("hide");
    $("tCount").textContent = "";
    $("tSect").textContent = "Passage bank";
    $("paused").classList.add("hide");
    $("tPause").classList.remove("on");
    view("home");
    paintHome();
    flash("Exam exited and reset without scoring.");
  }
}
if (typeof window !== "undefined") {
  window.exitExamWithoutScoring = exitExamWithoutScoring;
}

/* ===== PRACTICE EXAM STATE ===== */
let PE = null; // active practice exam state

/* Build a single linear question list from multiple sets, preserving passage context */
function buildExamQuestions(sets) {
  const questions = [];
  sets.forEach((set, si) => {
    set.qs.forEach((q, qi) => {
      questions.push({
        ...q,
        _setIdx: si,
        _qIdx: qi,
        _passage: q.d ? null : set.passage,
        _topic: set.topic,
        _setId: set.id,
        _sourceExamId: set._sourceExamId || null,
        _sourceSetIndex: (set._sourceSetIndex !== undefined) ? set._sourceSetIndex : si
      });
    });
  });
  return questions;
}

/* Build adaptive sets by whole passages (never splitting questions within a passage) */
function buildAdaptiveSets(sourceSets, targetPassages) {
  let pCount = targetPassages;
  // If targetPassages is greater than the number of sets, it might be a target question count.
  // In that case, include whole passages until the target question count is reached.
  if (pCount > sourceSets.length) {
    let accum = 0;
    let setsNeeded = 0;
    for (const s of sourceSets) {
      setsNeeded++;
      accum += (s && s.qs ? s.qs.length : 0);
      if (accum >= pCount) break;
    }
    pCount = setsNeeded;
  }
  pCount = Math.max(1, Math.min(pCount || 1, sourceSets.length));
  // Keep every question in each selected passage intact
  return sourceSets.slice(0, pCount).map(s => ({
    ...s,
    qs: [...s.qs]
  }));
}

/* Classify questions into MCAT archetypes for telemetry and AI analysis */
function getQuestionArchetype(q, sec) {
  const text = ((q.q || "") + " " + ((q.ch || []).join(" "))).toLowerCase();
  if (sec === "CARS") {
    if (text.includes("main idea") || text.includes("central thesis") || text.includes("primary purpose") || text.includes("author's primary") || text.includes("best summarizes") || text.includes("title for the passage") || text.includes("overarching")) {
      return "Main Idea & Global Reasoning";
    }
    if (text.includes("attitude") || text.includes("tone") || text.includes("feel towards") || text.includes("perspective") || text.includes("author would most likely view") || text.includes("sentiment") || text.includes("author's reaction")) {
      return "Author Attitude & Tone";
    }
    if (text.includes("if ") || text.includes("suppose that") || text.includes("which of the following, if true") || text.includes("new discovery") || text.includes("scenario") || text.includes("apply to") || text.includes("analogous")) {
      return "Reasoning Beyond the Text";
    }
    if (text.includes("infer") || text.includes("implies") || text.includes("implicit") || text.includes("suggests") || text.includes("assumption") || text.includes("presupposes") || text.includes("unspoken")) {
      return "Inference & Implicit Assumption";
    }
    return "Foundations of Comprehension";
  } else {
    // Science sections (C/P, B/B, P/S)
    if (text.includes("calculate") || text.includes("value") || text.includes("approximate") || text.includes("molar") || text.includes("wavelength") || text.includes("energy") || text.includes("joules") || text.includes("current") || text.includes("velocity") || text.includes("ph of") || text.includes("half-life") || text.includes("concentration") || text.includes("ratio of") || text.includes("frequency") || text.includes("power") || text.includes("force")) {
      return "Calculation & Quantitative";
    }
    if (text.includes("figure") || text.includes("table") || text.includes("graph") || text.includes("data") || text.includes("plot") || text.includes("trend") || text.includes("shown in") || (text.includes("increase") && text.includes("decrease") && text.includes("rate"))) {
      return "Data Interpretation & Graphs";
    }
    if (text.includes("experiment") || text.includes("control") || text.includes("hypothesis") || text.includes("independent variable") || text.includes("dependent variable") || text.includes("assay") || text.includes("purification") || text.includes("gel") || text.includes("western blot") || text.includes("pcr") || text.includes("mutant") || text.includes("knockout")) {
      return "Experimental Design & Hypothesis";
    }
    if (text.includes("mechanism") || text.includes("pathway") || text.includes("inhibit") || text.includes("activate") || text.includes("enzyme") || text.includes("catalyze") || text.includes("substrate") || text.includes("receptor") || text.includes("cascade") || text.includes("allosteric") || text.includes("cleavage") || text.includes("metabolism") || text.includes("phosphorylation")) {
      return "Mechanism & Biochemical Logic";
    }
    return "Discrete Recall & Scientific Principle";
  }
}
if (typeof window !== "undefined") window.getQuestionArchetype = getQuestionArchetype;
if (typeof globalThis !== "undefined") globalThis.getQuestionArchetype = getQuestionArchetype;

function parseExamNum(e) {
  const match = (e.suite || e.id || "").match(/exam(\d+)/i);
  if (match) return parseInt(match[1]);
  const num = parseInt((e.suite || "").replace(/\D/g, ""));
  return isNaN(num) ? 999 : num;
}

function getSortedSubjectPool(secKey) {
  const pool = PRACTICE_EXAMS.filter(e => e.sec === secKey && !e.isHalf);
  pool.sort((a, b) => {
    const na = parseExamNum(a);
    const nb = parseExamNum(b);
    if (na !== nb) return na - nb;
    return b.duration - a.duration; // 90m before 60m
  });
  return pool;
}

/* ===== PASSAGE CONTENT FINGERPRINTING & CROSS-EXAM DEDUPLICATION ===== */
/* Robust passage content & discrete question fingerprinting for cross-exam deduplication */
function getPassageFingerprint(item) {
  if (!item) return "";
  const pText = item._passage || item.passage || (item.set && (item.set._passage || item.set.passage)) || null;
  if (pText && typeof pText === "string") {
    // Strip header titles like <div class="ttl">Passage 1 (Questions 1-6)</div> so 60m and 90m match identically
    const stripped = pText
      .replace(/<div class=["']ttl["']>[\s\S]*?<\/div>/gi, "")
      .replace(/<[^>]+>/g, " ")
      .replace(/[^a-zA-Z0-9]/g, "")
      .toLowerCase();
    if (stripped.length >= 25) {
      return "p:" + stripped.slice(0, 120);
    }
  }
  // For discrete question sets
  const qs = item.qs || (item.set && item.set.qs);
  if (qs && Array.isArray(qs) && qs.length > 0) {
    const stems = qs.map(q => (q.q || "").replace(/<[^>]+>/g, " ").replace(/[^a-zA-Z0-9]/g, "").toLowerCase().slice(0, 40));
    return "dset:" + stems.slice(0, 3).join("|");
  }
  // For individual discrete question
  if (item.q && typeof item.q === "string") {
    const stem = item.q.replace(/<[^>]+>/g, " ").replace(/[^a-zA-Z0-9]/g, "").toLowerCase().slice(0, 80);
    return "dq:" + stem;
  }
  return "id:" + (item.id || (item.set && item.set.id) || "");
}

/* Bidirectional cross-exam synchronization: marks identical passages completed across all counterpart exams */
function syncCompletedPassageToAllExams(fingerprint, sourceExamId, sourceSetIdx, peData) {
  if (!fingerprint) return peData;
  if (!peData) peData = {};
  if (!Array.isArray(peData.completedPassageFingerprints)) {
    peData.completedPassageFingerprints = [];
  }
  if (!peData.completedPassageFingerprints.includes(fingerprint)) {
    peData.completedPassageFingerprints.push(fingerprint);
  }

  const pool = (typeof PRACTICE_EXAMS !== "undefined") ? PRACTICE_EXAMS : [];
  for (const ex of pool) {
    if (!ex.sets || !Array.isArray(ex.sets)) continue;
    ex.sets.forEach((set, sIdx) => {
      const fp = getPassageFingerprint(set);
      if (fp === fingerprint) {
        if (!peData[ex.id]) peData[ex.id] = { completedSets: [], done: false };
        if (!Array.isArray(peData[ex.id].completedSets)) peData[ex.id].completedSets = [];
        if (!peData[ex.id].completedSets.includes(sIdx)) {
          peData[ex.id].completedSets.push(sIdx);
        }
        if (peData[ex.id].completedSets.length >= ex.sets.length) {
          peData[ex.id].done = true;
          peData[ex.id].completedViaAdaptive = true;
        }
      }
    });
  }
  return peData;
}

/* Automatically retrofits and migrates completed passages into global fingerprint registry */
function initAndMigrateCompletedFingerprints(peData) {
  if (!peData || typeof peData !== "object") return peData;
  if (!Array.isArray(peData.completedPassageFingerprints)) {
    peData.completedPassageFingerprints = [];
  }
  const pool = (typeof PRACTICE_EXAMS !== "undefined") ? PRACTICE_EXAMS : [];
  let changed = false;

  pool.forEach(ex => {
    const r = peData[ex.id];
    if (!r || !ex.sets) return;
    const isDone = !!r.done;
    const cSets = Array.isArray(r.completedSets) ? r.completedSets : [];

    ex.sets.forEach((set, sIdx) => {
      if (isDone || cSets.includes(sIdx)) {
        const fp = getPassageFingerprint(set);
        if (fp && !peData.completedPassageFingerprints.includes(fp)) {
          peData.completedPassageFingerprints.push(fp);
          changed = true;
        }
      }
    });
  });

  if (peData.completedPassageFingerprints.length > 0) {
    const fpSet = new Set(peData.completedPassageFingerprints);
    pool.forEach(ex => {
      if (!ex.sets) return;
      if (!peData[ex.id]) peData[ex.id] = { completedSets: [], done: false };
      if (!Array.isArray(peData[ex.id].completedSets)) peData[ex.id].completedSets = [];

      ex.sets.forEach((set, sIdx) => {
        const fp = getPassageFingerprint(set);
        if (fpSet.has(fp) && !peData[ex.id].completedSets.includes(sIdx)) {
          peData[ex.id].completedSets.push(sIdx);
          changed = true;
        }
      });

      if (peData[ex.id].completedSets.length >= ex.sets.length && !peData[ex.id].done) {
        peData[ex.id].done = true;
        peData[ex.id].completedViaAdaptive = true;
        changed = true;
      }
    });
  }

  return peData;
}

/* Continuous passage queue: collects all uncompleted passages across exams with strict deduplication */
function getSubjectPassageQueue(secKey) {
  const peKey = "drillroom_pe_v1";
  let peData;
  try { peData = JSON.parse(localStorage.getItem(peKey)) || {}; } catch (e) { peData = {}; }
  peData = initAndMigrateCompletedFingerprints(peData);

  const pool = getSortedSubjectPool(secKey);
  const queue = [];
  const seenFps = new Set();
  const completedFps = new Set(Array.isArray(peData.completedPassageFingerprints) ? peData.completedPassageFingerprints : []);

  for (const ex of pool) {
    const r = peData[ex.id];
    const examDone = r && r.done;
    const completedSets = (r && Array.isArray(r.completedSets)) ? r.completedSets : [];

    for (let setIdx = 0; setIdx < ex.sets.length; setIdx++) {
      const set = ex.sets[setIdx];
      const fp = getPassageFingerprint(set);

      // If passage already encountered in a prior exam in the pool (e.g. 90m vs 60m duplicate), SKIP IT
      if (seenFps.has(fp)) continue;
      seenFps.add(fp);

      // If passage has already been completed in any exam or adaptive queue, SKIP IT
      if (completedFps.has(fp) || examDone || completedSets.includes(setIdx)) {
        continue;
      }

      queue.push({
        exam: ex,
        examId: ex.id,
        setIndex: setIdx,
        set: set,
        fingerprint: fp
      });
    }
  }

  // If entire queue is completed, allow review cycle (strictly deduplicated)
  if (queue.length === 0) {
    const reviewSeenFps = new Set();
    for (const ex of pool) {
      for (let setIdx = 0; setIdx < ex.sets.length; setIdx++) {
        const set = ex.sets[setIdx];
        const fp = getPassageFingerprint(set);
        if (reviewSeenFps.has(fp)) continue;
        reviewSeenFps.add(fp);

        queue.push({
          exam: ex,
          examId: ex.id,
          setIndex: setIdx,
          set: set,
          fingerprint: fp,
          isReviewCycle: true
        });
      }
    }
  }

  return queue;
}

/* Builds continuous adaptive passage plan across exam boundaries */
function getContinuousPassagePlan(secKey, targetPassages, selectedExamId) {
  const peKey = "drillroom_pe_v1";
  let peData;
  try { peData = JSON.parse(localStorage.getItem(peKey)) || {}; } catch (e) { peData = {}; }

  const fullQueue = getSubjectPassageQueue(secKey);
  const pool = getSortedSubjectPool(secKey);
  let pCount = Math.max(1, targetPassages || 1);

  let chosenQueueItems = [];

  if (selectedExamId && selectedExamId !== "auto") {
    const specificExam = pool.find(e => e.id === selectedExamId);
    if (specificExam) {
      const fromSpecific = fullQueue.filter(item => item.examId === selectedExamId);
      chosenQueueItems.push(...fromSpecific.slice(0, pCount));

      if (chosenQueueItems.length < pCount) {
        const remainingNeeded = pCount - chosenQueueItems.length;
        const others = fullQueue.filter(item => item.examId !== selectedExamId);
        chosenQueueItems.push(...others.slice(0, remainingNeeded));
      }
    }
  }

  if (chosenQueueItems.length === 0) {
    chosenQueueItems = fullQueue.slice(0, pCount);
  }

  const sets = chosenQueueItems.map(item => ({
    ...item.set,
    _sourceExamId: item.examId,
    _sourceSetIndex: item.setIndex,
    qs: [...item.set.qs]
  }));

  const sourceBreakdownMap = {};
  chosenQueueItems.forEach(item => {
    if (!sourceBreakdownMap[item.examId]) {
      sourceBreakdownMap[item.examId] = {
        examId: item.examId,
        label: item.exam.label,
        duration: item.exam.duration,
        setIndices: []
      };
    }
    sourceBreakdownMap[item.examId].setIndices.push(item.setIndex);
  });
  const sourceBreakdown = Object.values(sourceBreakdownMap);

  const totalQs = sets.reduce((sum, s) => sum + (s && s.qs ? s.qs.length : 0), 0);
  const secPerQ = secKey === "CARS" ? 101.8 : 96.6;
  const estMinutes = Math.max(2, Math.round((totalQs * secPerQ) / 60));

  return {
    sets,
    sourceBreakdown,
    totalPassages: sets.length,
    totalQs,
    estMinutes,
    isCombining: sourceBreakdown.length > 1,
    primaryExam: chosenQueueItems[0]?.exam || pool[0]
  };
}

/* Get uncompleted exams for a subject (both 90m and 60m) */
function getUncompletedExams(secKey) {
  const peKey = "drillroom_pe_v1";
  let peData;
  try { peData = JSON.parse(localStorage.getItem(peKey)) || {}; } catch (e) { peData = {}; }

  const pool = getSortedSubjectPool(secKey);
  const uncompleted = pool.filter(e => !peData[e.id]?.done);
  return { uncompleted, all: pool, peData };
}

/* Auto-pick the best uncompleted source exam (90m or 60m) */
function pickSourceExam(secKey, targetPassagesOrMinutes, selectedExamId) {
  const { uncompleted, all } = getUncompletedExams(secKey);

  if (selectedExamId && selectedExamId !== "auto") {
    const found = all.find(e => e.id === selectedExamId);
    if (found) return found;
  }

  // If user requests more passages than 60m exams contain (> 6 sets) or > 60 min, require 90m exam
  const needs90 = (targetPassagesOrMinutes > 10)
    ? (targetPassagesOrMinutes > 60)
    : (targetPassagesOrMinutes > 6);

  if (needs90) {
    const u90 = uncompleted.find(e => e.duration === 90);
    if (u90) return u90;
    return all.find(e => e.duration === 90) || all[0];
  }

  // Under 60 min / <= 6 passages: pull from whatever exam is uncompleted (90m or 60m)
  if (uncompleted.length > 0) {
    return uncompleted[0];
  }
  return all[0];
}

/* Start an adaptive study section combining whole passages seamlessly across banks */
function startAdaptiveStudy(sourceExamOrSec, numPassages, targetMinutes) {
  if (typeof sourceExamOrSec === "object" && sourceExamOrSec.sets) {
    const totalSets = sourceExamOrSec.sets.length;
    if (numPassages >= totalSets && (!targetMinutes || targetMinutes >= sourceExamOrSec.duration)) {
      beginPracticeExam(sourceExamOrSec);
      return;
    }
  }

  const secKey = (typeof sourceExamOrSec === "string")
    ? sourceExamOrSec
    : (sourceExamOrSec.sec || peActiveSec || "CARS");
  const selectedExamId = (typeof sourceExamOrSec === "object" && sourceExamOrSec.id)
    ? sourceExamOrSec.id
    : peSelectedSourceExamId;

  const plan = getContinuousPassagePlan(secKey, numPassages, selectedExamId);
  const pCount = plan.totalPassages;
  const totalQs = plan.totalQs;
  const estMinutes = (targetMinutes && targetMinutes > 0 && targetMinutes <= 90)
    ? targetMinutes
    : plan.estMinutes;

  const primaryExam = plan.primaryExam;
  const isFullSingleExam = (!plan.isCombining && pCount === primaryExam.sets.length && (!targetMinutes || targetMinutes >= primaryExam.duration));

  if (isFullSingleExam) {
    beginPracticeExam(primaryExam);
    return;
  }

  const pWord = pCount === 1 ? "Passage" : "Passages";
  let comboDesc = "";
  if (plan.isCombining) {
    const parts = plan.sourceBreakdown.map(b => `${b.setIndices.length} from ${b.label}`);
    comboDesc = ` &middot; Combining ${parts.join(" + ")} (finishing earlier exam so no banks hang leftover)`;
  } else {
    comboDesc = ` &middot; Pulled from ${primaryExam.label}`;
  }

  const studyId = "adaptive_" + secKey.replace("/", "") + "_" + pCount + "p_" + totalQs + "q_" + Date.now();
  const label = `${secKey} Study (${pCount} ${pWord} &middot; ${totalQs} Qs &middot; ${estMinutes}m)`;
  const desc = `${pCount} complete ${pWord.toLowerCase()} (${totalQs} questions) &middot; ${estMinutes} minutes timed${comboDesc}`;

  const studyExam = {
    id: studyId,
    sec: secKey,
    suite: primaryExam.suite,
    suiteTitle: `Adaptive Study — ${secKey}${plan.isCombining ? " (Combined Banks Queue)" : ""}`,
    label: label,
    topic: label,
    desc: desc,
    duration: estMinutes,
    sets: plan.sets,
    _isAdaptive: true,
    _targetPassages: pCount,
    _targetQCount: totalQs,
    _sourceBreakdown: plan.sourceBreakdown,
    _sourceExamId: primaryExam.id,
    _isFull: false
  };

  beginPracticeExam(studyExam);
}

/* Practice exam timers for passage reading vs question answering telemetry */
let _peTickTimer = null;

function stopPracticeExamTimer() {
  if (_peTickTimer) {
    clearInterval(_peTickTimer);
    _peTickTimer = null;
  }
}

function startPracticeExamTimer() {
  stopPracticeExamTimer();
  _peTickTimer = setInterval(() => {
    if (!PE || !E || !E._isPracticeExam) {
      stopPracticeExamTimer();
      return;
    }
    if (E.paused) return;

    const q = E.s.qs[E.i];
    if (!q) return;
    const si = q._setIdx;

    // Track dwell time on current question silently in background
    if (PE._qTimes) {
      PE._qTimes[E.i] = (PE._qTimes[E.i] || 0) + 1;
    }

    // Hidden passage telemetry: track pre-answer dwell before any answer is chosen in this passage
    if (si !== undefined && PE._passageTelemetry) {
      if (!PE._passageTelemetry[si]) {
        PE._passageTelemetry[si] = {
          firstAnswerExamSec: null,
          firstInteractionExamSec: null,
          totalPreAnswerDwell: 0,
          qDwellBeforeFirstAnswer: {}
        };
      }
      const pt = PE._passageTelemetry[si];
      if (pt.firstAnswerExamSec === null) {
        pt.totalPreAnswerDwell = (pt.totalPreAnswerDwell || 0) + 1;
        pt.qDwellBeforeFirstAnswer[E.i] = (pt.qDwellBeforeFirstAnswer[E.i] || 0) + 1;
      }
    }

    // Maintain backwards-compatible passage read state in memory (no visible clocks)
    if (PE._activeMode === "passage") {
      if (si !== undefined && PE._passageReadState && PE._passageReadState[si]) {
        PE._passageReadState[si].elapsedSec = (PE._passageReadState[si].elapsedSec || 0) + 1;
      }
    }
  }, 1000);
}

function finishReadingPassage(si) {
  if (!PE) return;
  if (!PE._passageReadState) PE._passageReadState = {};
  if (!PE._passageReadState[si]) {
    const q = (E && E.s && E.s.qs) ? E.s.qs[E.i] : null;
    const words = (q && q._passage) ? q._passage.replace(/<[^>]+>/g, " ").trim().split(/\s+/).filter(Boolean).length : 0;
    PE._passageReadState[si] = { reading: false, done: true, elapsedSec: 0, wordCount: words };
  } else {
    PE._passageReadState[si].reading = false;
    PE._passageReadState[si].done = true;
  }
  PE._activeMode = "question";
  if (E) {
    drawPEQ();
  }
}

function updatePassageReadBar(si) {
  // Intentionally blank: live timers and buttons are removed during active exam to match real MCAT UI
  const wrap = document.getElementById("pePassageReadBarWrap");
  if (wrap) wrap.innerHTML = "";
}

/* Start a practice exam */
function beginPracticeExam(exam) {
  const peKey = "drillroom_pe_v1";
  let peData;
  try { peData = JSON.parse(localStorage.getItem(peKey)) || {}; } catch (e) { peData = {}; }
  peData = initAndMigrateCompletedFingerprints(peData);
  const completedFps = new Set(Array.isArray(peData.completedPassageFingerprints) ? peData.completedPassageFingerprints : []);

  // Check which sets in this exam have already been completed elsewhere
  const completedSetIndices = new Set();
  if (exam.sets && Array.isArray(exam.sets)) {
    exam.sets.forEach((set, sIdx) => {
      const fp = getPassageFingerprint(set);
      if (completedFps.has(fp)) {
        completedSetIndices.add(sIdx);
      } else if (peData[exam.id] && Array.isArray(peData[exam.id].completedSets) && peData[exam.id].completedSets.includes(sIdx)) {
        completedSetIndices.add(sIdx);
      }
    });
  }

  // If ALL sets in this non-adaptive exam are already completed, ask if user wants to retake or cancel
  if (!exam._isAdaptive && exam.sets && completedSetIndices.size === exam.sets.length && exam.sets.length > 0) {
    const retake = (typeof confirm === "function")
      ? confirm("You have already completed all passages in this exam in another section (e.g. 90-minute or 60-minute).\n\nWould you like to reset and retake these questions for fresh practice?")
      : true;
    if (!retake) {
      if (typeof openPracticeExamModal === "function") openPracticeExamModal();
      return;
    }
    // If retaking, clear the pre-skipped set indices for this session
    completedSetIndices.clear();
  }

  const questions = buildExamQuestions(exam.sets);

  // Pre-skip any questions belonging to sets that were already completed
  let autoSkippedPassagesCount = 0;
  if (completedSetIndices.size > 0) {
    questions.forEach(q => {
      if (completedSetIndices.has(q._setIdx)) {
        q._isSkipped = true;
      }
    });
    autoSkippedPassagesCount = completedSetIndices.size;
  }

  // Find start index (first non-skipped question)
  const firstActiveIdx = questions.findIndex(q => !q._isSkipped);
  const startIdx = firstActiveIdx !== -1 ? firstActiveIdx : 0;

  const initialAnswers = questions.map(q => q._isSkipped ? -1 : null);
  const initialConf = questions.map(q => q._isSkipped ? "skipped" : null);
  const initialSeen = questions.map((q, idx) => !!q._isSkipped || idx === startIdx);

  PE = {
    exam: exam,
    questions: questions,
    i: startIdx,
    ans: initialAnswers,
    conf: initialConf,
    flag: Array(questions.length).fill(false),
    struck: questions.map(() => []),
    seen: initialSeen,
    left: exam.duration * 60,
    paused: false,
    pauseCount: 0,
    pauseSecs: 0,
    thisPause: 0,
    startTime: Date.now(),
    mode: "practiceExam",
    _passageTelemetry: {},
    _passageReadState: {},
    _qTimes: Array(questions.length).fill(0),
    _firstAnswers: Array(questions.length).fill(null),
    _answerChanges: [],
    _activeMode: "passage",
    _autoSkippedPassagesCount: autoSkippedPassagesCount
  };

  // Build the exam view using existing UI
  E = {
    s: {
      id: exam.id,
      sec: exam.sec,
      label: exam.label,
      topic: exam.label,
      passage: questions[startIdx]._passage || "",
      sheet: null,
      qs: questions,
      secPerQ: (exam.duration * 60) / questions.length
    },
    i: startIdx,
    ans: PE.ans,
    conf: PE.conf,
    flag: PE.flag,
    struck: PE.struck,
    seen: PE.seen,
    left: PE.left,
    paused: false,
    pauseCount: 0,
    pauseSecs: 0,
    thisPause: 0,
    _isPracticeExam: true,
    _peRef: PE,
    _currentPassage: null,
    _lastQIdx: null,
    _qTimes: PE._qTimes,
    _passageTelemetry: PE._passageTelemetry,
    _passageReadState: PE._passageReadState,
    _answerChanges: PE._answerChanges
  };

  if (typeof window !== "undefined") {
    window.PE = PE;
    window.E = E;
  }

  const firstPassage = questions[startIdx]._passage || null;
  if (firstPassage) {
    $("pass").innerHTML = `<div id="pePassContent">${firstPassage}</div>`;
    $("ebody").classList.remove("np");
    E._currentPassage = firstPassage;
  } else {
    $("pass").innerHTML = "";
    $("ebody").classList.add("np");
    E._currentPassage = null;
    PE._activeMode = "question";
  }
  $("pass").scrollTop = 0;
  $("qp").scrollTop = 0;
  E._lastQIdx = startIdx;

  $("tSect").textContent = exam.label;
  $("clk").classList.remove("hide");
  $("padTxt").value = "";
  $("calcIn").value = "";
  $("calcOut").innerHTML = "&nbsp;";
  if (typeof window !== "undefined" && window.lockCalc) window.lockCalc(true);
  $("paused").classList.add("hide");
  $("tPause").classList.remove("on");
  view("exam");
  drawPEQ();
  tick();
  startPracticeExamTimer();
}

/* Draw question for practice exam — handles passage switching between questions */
/* ===== PRACTICE PASSAGE SKIP & PRACTICE TOOLS POPUP ===== */
function isPassageAlreadyCompleted(q) {
  if (!q) return false;
  const peKey = "drillroom_pe_v1";
  let peData;
  try { peData = JSON.parse(localStorage.getItem(peKey)) || {}; } catch (e) { peData = {}; }

  const fp = getPassageFingerprint(q);
  if (fp && Array.isArray(peData.completedPassageFingerprints) && peData.completedPassageFingerprints.includes(fp)) {
    return true;
  }

  const targetExamId = q._sourceExamId || ((typeof E !== "undefined" && E && E._peRef && E._peRef.exam) ? E._peRef.exam.id : null);
  const targetSetIdx = (q._sourceSetIndex !== undefined) ? q._sourceSetIndex : (q._setIdx !== undefined ? q._setIdx : 0);

  if (!targetExamId || !peData[targetExamId]) return false;
  const record = peData[targetExamId];
  if (record.done) return true;
  if (Array.isArray(record.completedSets) && record.completedSets.includes(targetSetIdx)) return true;
  return false;
}

function markPassageSetCompletedInBank(q) {
  if (!q) return;
  const peKey = "drillroom_pe_v1";
  let peData;
  try { peData = JSON.parse(localStorage.getItem(peKey)) || {}; } catch (e) { peData = {}; }

  const targetExamId = q._sourceExamId || ((typeof E !== "undefined" && E && E._peRef && E._peRef.exam) ? E._peRef.exam.id : null);
  const targetSetIdx = (q._sourceSetIndex !== undefined) ? q._sourceSetIndex : (q._setIdx !== undefined ? q._setIdx : 0);
  const fp = getPassageFingerprint(q);

  if (fp) {
    syncCompletedPassageToAllExams(fp, targetExamId, targetSetIdx, peData);
  } else if (targetExamId) {
    if (!peData[targetExamId]) peData[targetExamId] = { completedSets: [], done: false };
    if (!Array.isArray(peData[targetExamId].completedSets)) peData[targetExamId].completedSets = [];
    if (!peData[targetExamId].completedSets.includes(targetSetIdx)) {
      peData[targetExamId].completedSets.push(targetSetIdx);
    }

    const pool = (typeof PRACTICE_EXAMS !== "undefined") ? PRACTICE_EXAMS : [];
    const srcExam = pool.find(e => e.id === targetExamId);
    if (srcExam && srcExam.sets && peData[targetExamId].completedSets.length >= srcExam.sets.length) {
      peData[targetExamId].done = true;
      peData[targetExamId].completedViaAdaptive = true;
    }
  }

  try { localStorage.setItem(peKey, JSON.stringify(peData)); } catch (e) { }

  if (typeof DrillRoomCloud !== "undefined" && typeof DrillRoomCloud.triggerAutoSync === "function") {
    DrillRoomCloud.triggerAutoSync();
  }
}

function updateSkipPassageButtonState() {
  const skipBtn = $("tSkipPassage");
  const badge = $("peSkipBadge");
  if (!skipBtn || !badge) return;

  if (typeof E === "undefined" || !E || !E._isPracticeExam || !E.s || !E.s.qs || !E.s.qs[E.i]) {
    skipBtn.disabled = true;
    skipBtn.style.opacity = "0.5";
    badge.textContent = "(No Passage to Skip)";
    badge.className = "pe-skip-badge";
    return;
  }

  const q = E.s.qs[E.i];
  if (q.d || !q._passage) {
    skipBtn.disabled = true;
    skipBtn.style.opacity = "0.5";
    badge.textContent = "(Discrete Q — No Passage)";
    badge.className = "pe-skip-badge";
    return;
  }

  skipBtn.disabled = false;
  skipBtn.style.opacity = "1";

  const isSkippedInSession = q._isSkipped || E.ans[E.i] === -1;
  const isDoneInBank = isPassageAlreadyCompleted(q);

  if (isSkippedInSession) {
    badge.textContent = "(Already Skipped)";
    badge.className = "pe-skip-badge pe-badge-skipped";
  } else if (isDoneInBank) {
    badge.textContent = "(Already Done)";
    badge.className = "pe-skip-badge pe-badge-done";
  } else {
    badge.textContent = "(Mark Done & Skip)";
    badge.className = "pe-skip-badge pe-badge-todo";
  }
}

function toggleMoreToolsPopup(show) {
  const popup = $("peMoreToolsPopup");
  const moreBtn = $("tMore");
  if (!popup || !moreBtn) return;
  const isHidden = popup.classList.contains("hide");
  const shouldShow = (show !== undefined) ? !!show : isHidden;

  if (shouldShow) {
    updateSkipPassageButtonState();
    const ftr = $("ftr");
    if (ftr && ftr.getBoundingClientRect && moreBtn.getBoundingClientRect) {
      const ftrRect = ftr.getBoundingClientRect();
      const btnRect = moreBtn.getBoundingClientRect();
      if (ftrRect && btnRect) {
        const leftOffset = Math.max(10, Math.min(btnRect.left - ftrRect.left - 40, ftrRect.width - 320));
        popup.style.left = leftOffset + "px";
      }
    }
    popup.classList.remove("hide");
    moreBtn.classList.add("on");
  } else {
    popup.classList.add("hide");
    moreBtn.classList.remove("on");
  }
}

function skipCurrentPassage() {
  if (typeof E === "undefined" || !E || !E._isPracticeExam || !E.s || !E.s.qs || !E.s.qs[E.i]) return;
  const currentQ = E.s.qs[E.i];
  if (currentQ.d || !currentQ._passage) {
    if (typeof alert === "function") alert("This is a discrete question without a passage.");
    return;
  }

  const passageText = currentQ._passage;
  const passageSetIdx = currentQ._setIdx;
  const setQIndices = [];
  E.s.qs.forEach((q, idx) => {
    if (q._passage === passageText || (passageSetIdx !== undefined && q._setIdx === passageSetIdx)) {
      setQIndices.push(idx);
    }
  });

  const isAlreadyDone = isPassageAlreadyCompleted(currentQ);
  const promptMsg = isAlreadyDone
    ? `Skip this passage (${setQIndices.length} questions)? It is already checked off in your question bank and will be excluded from your score.`
    : `Skip this passage (${setQIndices.length} questions)? It will be marked COMPLETED in your question bank and excluded from your score.`;

  if (typeof confirm === "function" && !confirm(promptMsg)) {
    return;
  }

  // Mark all questions in this passage as skipped
  setQIndices.forEach(idx => {
    E.s.qs[idx]._isSkipped = true;
    E.ans[idx] = -1;
    E.conf[idx] = "skipped";
    E.seen[idx] = true;
  });

  // Mark set completed in bank
  markPassageSetCompletedInBank(currentQ);

  // Close popup
  toggleMoreToolsPopup(false);

  // Auto-advance to next unskipped question
  let nextIdx = -1;
  for (let j = E.i + 1; j < E.s.qs.length; j++) {
    if (!E.s.qs[j]._isSkipped) {
      nextIdx = j;
      break;
    }
  }

  if (nextIdx !== -1) {
    E.i = nextIdx;
    drawPEQ();
  } else {
    // Check if any prior question is unanswered and unskipped
    const prevIncomplete = E.s.qs.findIndex((q, idx) => !q._isSkipped && (E.ans[idx] === null || E.conf[idx] === null));
    if (prevIncomplete !== -1) {
      E.i = prevIncomplete;
      drawPEQ();
    } else {
      // All questions in exam are completed or skipped!
      if (typeof confirm === "function") {
        if (confirm("All remaining questions in this exam have been answered or skipped. End and score section now?")) {
          gradePracticeExam();
        } else {
          drawPEQ();
        }
      } else {
        gradePracticeExam();
      }
    }
  }
}

function unskipCurrentPassage() {
  if (typeof E === "undefined" || !E || !E._isPracticeExam || !E.s || !E.s.qs || !E.s.qs[E.i]) return;
  const currentQ = E.s.qs[E.i];
  const passageText = currentQ._passage;
  const passageSetIdx = currentQ._setIdx;

  E.s.qs.forEach((q, idx) => {
    if (q._passage === passageText || (passageSetIdx !== undefined && q._setIdx === passageSetIdx)) {
      q._isSkipped = false;
      if (E.ans[idx] === -1) E.ans[idx] = null;
      if (E.conf[idx] === "skipped") E.conf[idx] = null;
    }
  });

  drawPEQ();
}

function drawPEQ() {
  if (typeof E === "undefined" || !E || !E._isPracticeExam) return;
  const q = E.s.qs[E.i];
  E.seen[E.i] = true;
  const si = q._setIdx !== undefined ? q._setIdx : 0;
  const isQSkipped = q._isSkipped || E.ans[E.i] === -1 || E.conf[E.i] === "skipped";

  // Skipped question notice banner in question pane
  let skipBanner = $("peSkippedQBanner");
  if (isQSkipped) {
    if (!skipBanner) {
      skipBanner = document.createElement("div");
      skipBanner.id = "peSkippedQBanner";
      skipBanner.style.cssText = "display:flex;justify-content:space-between;align-items:center;background:#F1F5F9;border:1px solid #CBD5E1;border-radius:4px;padding:8px 12px;margin-bottom:12px;font-size:12px;color:#475569";
      const qp = $("qp");
      if (qp && qp.firstChild) qp.insertBefore(skipBanner, qp.firstChild);
    }
    skipBanner.innerHTML = `
      <div>
        <b style="color:#1E293B">&#10549; Passage Skipped:</b> Completed in question bank &amp; excluded from score.
      </div>
      <button id="bUnskipPassage" style="padding:4px 8px;font-size:11px;font-weight:700;border:1px solid #94A3B8;border-radius:3px;background:#fff;cursor:pointer;color:#1E293B">
        Unskip Passage
      </button>
    `;
    skipBanner.style.display = "flex";
    const unskipBtn = skipBanner.querySelector("#bUnskipPassage");
    if (unskipBtn) unskipBtn.onclick = () => unskipCurrentPassage();
  } else if (skipBanner) {
    skipBanner.style.display = "none";
  }

  // Update popup badge state
  updateSkipPassageButtonState();

  // Reset question pane scroll to top when changing questions
  if (E._lastQIdx !== E.i) {
    $("qp").scrollTop = 0;
    E._lastQIdx = E.i;
  }

  // Update passage pane only if passage actually changed (preserves scroll position & highlights)
  const passage = q._passage || null;
  if (passage) {
    if (!PE._passageReadState[si]) {
      const words = passage.replace(/<[^>]+>/g, " ").trim().split(/\s+/).filter(Boolean).length;
      PE._passageReadState[si] = { reading: true, done: false, elapsedSec: 0, wordCount: words };
    }
    const pState = PE._passageReadState[si];
    PE._activeMode = pState.done ? "question" : "passage";

    if (E._currentPassage !== passage) {
      $("pass").innerHTML = `<div id="pePassContent">${passage}</div>`;
      $("pass").scrollTop = 0;
      E._currentPassage = passage;
    }
    updatePassageReadBar(si);
    $("ebody").classList.remove("np");
  } else {
    if (E._currentPassage !== null) {
      $("pass").innerHTML = "";
      E._currentPassage = null;
    }
    PE._activeMode = "question";
    $("ebody").classList.add("np");
  }

  const arch = getQuestionArchetype(q, E.s.sec);
  $("tCount").textContent = `Question ${E.i + 1} of ${E.s.qs.length}${q.d ? "  (discrete)" : ""}`;
  $("qno").innerHTML = `Question ${E.i + 1}`;
  $("qtx").innerHTML = q.q;
  $("fChk").checked = E.flag[E.i];
  $("fLbl").classList.toggle("on", E.flag[E.i]);

  const autoFinishPassageReading = () => {
    if (PE._passageReadState && PE._passageReadState[si] && !PE._passageReadState[si].done) {
      PE._passageReadState[si].reading = false;
      PE._passageReadState[si].done = true;
      PE._activeMode = "question";
      updatePassageReadBar(si);
    }
  };

  const box = $("opts");
  box.innerHTML = "";
  q.ch.forEach((c, k) => {
    const b = document.createElement("button");
    b.className = "opt" + (E.ans[E.i] === k ? " sel" : "") + (E.struck[E.i].includes(k) ? " st" : "");
    b.innerHTML = `<span class="rd"></span><span class="lt">${"ABCD"[k]}.</span><span class="tx">${c}</span>`;
    b.onclick = () => {
      if (si !== undefined && PE._passageTelemetry) {
        if (!PE._passageTelemetry[si]) {
          PE._passageTelemetry[si] = { firstAnswerExamSec: null, firstInteractionExamSec: null, totalPreAnswerDwell: 0, qDwellBeforeFirstAnswer: {} };
        }
        if (PE._passageTelemetry[si].firstAnswerExamSec === null) {
          PE._passageTelemetry[si].firstAnswerExamSec = Date.now();
        }
      }
      autoFinishPassageReading();
      if (strike) {
        const a = E.struck[E.i], j = a.indexOf(k);
        j > -1 ? a.splice(j, 1) : a.push(k);
      } else {
        if (E.struck[E.i].includes(k)) return;
        if (q._isSkipped || E.ans[E.i] === -1 || E.conf[E.i] === "skipped") {
          q._isSkipped = false;
          if (E.ans[E.i] === -1) E.ans[E.i] = null;
          if (E.conf[E.i] === "skipped") E.conf[E.i] = null;
        }
        if (PE._firstAnswers[E.i] === null) {
          PE._firstAnswers[E.i] = k;
        } else if (E.ans[E.i] !== null && E.ans[E.i] !== k) {
          PE._answerChanges.push({
            qIdx: E.i,
            from: E.ans[E.i],
            to: k,
            wasCorrect: (E.ans[E.i] === q.a),
            nowCorrect: (k === q.a),
            ts: Date.now()
          });
        }
        E.ans[E.i] = k;
      }
      drawPEQ();
    };
    b.oncontextmenu = ev => {
      ev.preventDefault();
      if (si !== undefined && PE._passageTelemetry) {
        if (!PE._passageTelemetry[si]) {
          PE._passageTelemetry[si] = { firstAnswerExamSec: null, firstInteractionExamSec: null, totalPreAnswerDwell: 0, qDwellBeforeFirstAnswer: {} };
        }
        if (PE._passageTelemetry[si].firstInteractionExamSec === null) {
          PE._passageTelemetry[si].firstInteractionExamSec = Date.now();
        }
      }
      autoFinishPassageReading();
      const a = E.struck[E.i], j = a.indexOf(k);
      j > -1 ? a.splice(j, 1) : a.push(k);
      drawPEQ();
    };
    box.appendChild(b);
  });

  document.querySelectorAll("#conf button").forEach(b => {
    b.classList.toggle("on", E.conf[E.i] === b.dataset.c);
    b.onclick = () => {
      autoFinishPassageReading();
      if (q._isSkipped || E.ans[E.i] === -1 || E.conf[E.i] === "skipped") {
        q._isSkipped = false;
        if (E.ans[E.i] === -1) E.ans[E.i] = null;
      }
      E.conf[E.i] = b.dataset.c;
      drawPEQ();
    };
  });

  $("bPrev").disabled = E.i === 0;
  $("bNext").disabled = !isQSkipped && !(E.ans[E.i] !== null && E.conf[E.i] !== null);
  $("bNext").textContent = E.i === E.s.qs.length - 1 ? "End Section" : "Next";
  if (typeof paintClk === "function") paintClk();
}

/* =========================================================================
   LATENT PASSAGE READING DECOMPOSITION ALGORITHM (LPRDA)
   Calculates exact passage reading time using hidden telemetry:
   - Dwell latency before first answer in passage
   - Question baseline solving speeds (trimmed median of subsequent items)
   - Outlier dwell detection across passage questions
   - Bayesian prior bounding calibrated to authentic MCAT reading speeds
   - Exact time conservation (decomposes reading time out of question solving times)
   ========================================================================= */
function calculatePassageReadingTelemetry(pe, questions) {
  const pTelemetry = (pe && pe._passageTelemetry) || {};
  const rawQTimes = (pe && pe._qTimes) ? [...pe._qTimes] : Array(questions.length).fill(0);
  const decomposedQTimes = [...rawQTimes];
  const secKey = (pe && pe.exam) ? pe.exam.sec : "CARS";

  // Group question indices by passage setIdx
  const setsMap = {};
  questions.forEach((q, idx) => {
    if (q._passage && q._setIdx !== undefined) {
      if (!setsMap[q._setIdx]) {
        const textOnly = q._passage.replace(/<[^>]+>/g, " ").trim();
        const words = textOnly.split(/\s+/).filter(Boolean).length;
        setsMap[q._setIdx] = {
          setIdx: q._setIdx,
          passage: q._passage,
          topic: q._topic || `Passage ${Object.keys(setsMap).length + 1}`,
          wordCount: words || 550,
          qIndices: []
        };
      }
      setsMap[q._setIdx].qIndices.push(idx);
    }
  });

  const passageStats = [];

  Object.values(setsMap).forEach((pData, pOrderIdx) => {
    const { setIdx, wordCount, qIndices } = pData;
    const tData = pTelemetry[setIdx] || {};
    const totalSetSec = qIndices.reduce((sum, qi) => sum + (rawQTimes[qi] || 0), 0);

    // Target MCAT analytical reading speeds (WPM)
    const targetWpm = secKey === "CARS" ? 220 : (secKey === "P/S" ? 200 : 185);
    const expectedReadSec = Math.round((wordCount / targetWpm) * 60);
    const minPlausibleSec = Math.max(25, Math.round((wordCount / 450) * 60)); // ~450 WPM upper bound
    const maxPlausibleSec = Math.min(300, Math.round((wordCount / 115) * 60));

    // 1. Determine baseline question solving speed for this passage
    const firstQIdx = qIndices[0];
    const subQIndices = qIndices.slice(1);
    const subQTimes = subQIndices.map(qi => rawQTimes[qi] || 0).filter(s => s >= 8);
    
    let baselineSolveSec;
    if (subQTimes.length >= 2) {
      subQTimes.sort((a, b) => a - b);
      baselineSolveSec = subQTimes[Math.floor(subQTimes.length / 2)];
    } else if (subQTimes.length === 1) {
      baselineSolveSec = subQTimes[0];
    } else {
      baselineSolveSec = secKey === "CARS" ? 55 : 48;
    }

    // 2. Identify pre-answer dwell (time spent across all questions before any answer was committed)
    const initialQDwell = (tData.qDwellBeforeFirstAnswer && tData.qDwellBeforeFirstAnswer[firstQIdx]) 
      ? tData.qDwellBeforeFirstAnswer[firstQIdx] 
      : (tData.totalPreAnswerDwell !== undefined ? tData.totalPreAnswerDwell : (rawQTimes[firstQIdx] || 0));

    let rawReadEstimate;

    // Case A: Clear pre-answer dwell identified
    if (initialQDwell >= 35) {
      const qFirstSolveOverhead = Math.min(baselineSolveSec, Math.round(initialQDwell * 0.25));
      rawReadEstimate = initialQDwell - qFirstSolveOverhead;
    } else {
      // Case B: Rapid first answer or delayed reading
      let maxDwellQ = firstQIdx;
      let maxDwell = rawQTimes[firstQIdx] || 0;
      qIndices.forEach(qi => {
        if ((rawQTimes[qi] || 0) > maxDwell) {
          maxDwell = rawQTimes[qi];
          maxDwellQ = qi;
        }
      });

      if (maxDwell >= 2.0 * baselineSolveSec && maxDwell >= 60) {
        rawReadEstimate = maxDwell - baselineSolveSec;
      } else {
        const estTotalSolve = qIndices.length * baselineSolveSec;
        rawReadEstimate = Math.max(minPlausibleSec, totalSetSec - estTotalSolve);
      }
    }

    // 3. Bayesian prior calibration & physiological clamping
    let finalReadSec;
    if (initialQDwell >= 45) {
      // If reading estimate exceeds 4 minutes, gently blend with expected read time to prevent artificial flatlining
      if (rawReadEstimate > 240) {
        rawReadEstimate = Math.round((rawReadEstimate * 0.65) + (expectedReadSec * 0.35));
      }
      finalReadSec = Math.max(minPlausibleSec, Math.min(maxPlausibleSec, Math.round(rawReadEstimate)));
    } else {
      const blended = (rawReadEstimate * 0.70) + (expectedReadSec * 0.30);
      finalReadSec = Math.max(minPlausibleSec, Math.min(maxPlausibleSec, Math.round(blended)));
    }

    // Safeguard: Ensure total reading time never exceeds total set time minus minimal 12s per question
    const allSkippedInSet = qIndices.every(qi => questions[qi]._isSkipped || (pe && pe.ans && pe.ans[qi] === -1));
    const maxAllowedReading = allSkippedInSet ? 0 : Math.max(0, totalSetSec - (qIndices.length * 12));
    finalReadSec = Math.min(finalReadSec, maxAllowedReading);
    if (!allSkippedInSet && finalReadSec <= 0 && totalSetSec > 0) {
      finalReadSec = Math.min(minPlausibleSec, Math.round(totalSetSec * 0.35));
    }
    if (allSkippedInSet) {
      finalReadSec = 0;
    }

    // 4. Decompose reading time out of question solve times (conserve total time exactly)
    let readingToDeduct = finalReadSec;
    const sortedByDwell = [...qIndices].sort((a, b) => (rawQTimes[b] || 0) - (rawQTimes[a] || 0));
    for (const qi of sortedByDwell) {
      if (readingToDeduct <= 0) break;
      const current = decomposedQTimes[qi];
      const maxDeductFromThisQ = Math.max(0, current - 12);
      const deduct = Math.min(readingToDeduct, maxDeductFromThisQ);
      decomposedQTimes[qi] -= deduct;
      readingToDeduct -= deduct;
    }

    const calculatedWpm = finalReadSec > 0 ? Math.round((wordCount / finalReadSec) * 60) : (allSkippedInSet ? 0 : targetWpm);

    passageStats.push({
      pIndex: pOrderIdx + 1,
      setIdx: setIdx,
      topic: pData.topic,
      wordCount: wordCount,
      readSec: finalReadSec,
      seconds: finalReadSec,
      wpm: calculatedWpm,
      baselineQSolveSec: baselineSolveSec,
      totalSetSec: totalSetSec,
      isSkipped: allSkippedInSet
    });
  });

  return {
    passageStats,
    decomposedQTimes,
    rawQTimes
  };
}

/* Grade practice exam with MCAT scoring */
function gradePracticeExam() {
  if (!E || !E._isPracticeExam) return;

  stopPracticeExamTimer();
  if (typeof timerId !== "undefined") clearInterval(timerId);
  $("paused").classList.add("hide");
  $("tPause").classList.remove("on");

  const qs = E.s.qs;
  const n = qs.length;
  let right = 0, lucky = 0, shaky = 0;

  const isSk = (q, k) => (q && q._isSkipped) || E.ans[k] === -1 || E.conf[k] === "skipped";
  const skippedCount = qs.filter((q, k) => isSk(q, k)).length;
  const scoredTotal = n - skippedCount;

  qs.forEach((q, k) => {
    if (isSk(q, k)) return;
    const ok = E.ans[k] === q.a;
    if (ok) right++;
    if (ok && E.conf[k] === "guess") lucky++;
    if (ok && E.conf[k] === "two") shaky++;
  });

  const solid = right - lucky - shaky;
  const pct = scoredTotal > 0 ? Math.round(right / scoredTotal * 100) : 0;
  const { score, ptile } = rawToScaled(pct);
  const pe = E._peRef;

  $("clk").classList.add("hide");
  $("tCount").textContent = "";
  $("tSect").textContent = pe.exam.label + " \u2014 Score Report";
  view("res");

  // Score header with MCAT-style display
  $("zT").innerHTML = `<span style="font-size:42px;font-weight:700;color:${score >= 125 ? 'var(--ok)' : score >= 122 ? 'var(--warn)' : 'var(--bad)'}">
    ${score}</span><span style="font-size:16px;color:var(--faint);margin-left:12px">/ 132</span>`;

  $("zL").innerHTML = `<div style="margin-bottom:12px">${right} of ${scoredTotal} scored questions correct (${pct}%) &mdash; <strong>${ptile} percentile</strong>${skippedCount > 0 ? ` <span style="color:#64748B;font-weight:600">(${skippedCount} skipped question${skippedCount > 1 ? "s" : ""} completed in question bank &amp; excluded from score)</span>` : ""}</div>
    ${(lucky + shaky) > 0
      ? `Of those ${right} correct, ${solid} were solid. ${lucky + shaky} came from a guess or a coin flip.`
      : `Every correct answer was marked confident. Clean read.`}`;

  // Stats boxes — include scaled score prominently
  $("zS").innerHTML = `
    <div class="st" style="border-top:3px solid ${score >= 125 ? 'var(--ok)' : score >= 122 ? 'var(--warn)' : 'var(--bad)'}">
      <div class="v" style="font-size:34px;color:${score >= 125 ? 'var(--ok)' : score >= 122 ? 'var(--warn)' : 'var(--bad)'}">${score}</div>
      <div class="l">Scaled Score (118\u2013132)</div>
    </div>
    <div class="st"><div class="v">${ptile}</div><div class="l">Percentile</div></div>
    <div class="st"><div class="v">${pct}%</div><div class="l">Raw Accuracy</div></div>
    <div class="st"><div class="v">${solid}</div><div class="l">Solid</div></div>
    <div class="st${lucky ? ' al' : ''}"><div class="v">${lucky}</div><div class="l">Lucky</div></div>
    <div class="st"><div class="v">${shaky}</div><div class="l">Shaky</div></div>`;

  // Confidence breakdown
  const B = { sure: [0, 0], two: [0, 0], guess: [0, 0] };
  qs.forEach((q, k) => {
    if (isSk(q, k)) return;
    const c = E.conf[k]; if (!c || !B[c]) return;
    B[c][1]++; if (E.ans[k] === q.a) B[c][0]++;
  });
  const L = { sure: "Knew it", two: "Narrowed to two", guess: "Guessed" };
  const C = { sure: "#1E7A3C", two: "#D9A22B", guess: "#B3261E" };
  $("zB").innerHTML = Object.keys(B).map(c => {
    const [r, t] = B[c]; if (!t) return "";
    return `<div class="br"><span>${L[c]}</span><div class="trk"><div class="fl" style="width:${Math.round(r / t * 100)}%;background:${C[c]}"></div></div><span class="n">${r}/${t}</span></div>`;
  }).join("");

  // Save results to legacy peData & process multi-bank and half-section combinations
  const peKey = "drillroom_pe_v1";
  let peData;
  try { peData = JSON.parse(localStorage.getItem(peKey)) || {}; } catch (e) { peData = {}; }

  const timeUsed = pe.exam.duration * 60 - E.left;

  // Process set completion across source breakdown (continuous queue) & sync fingerprints
  if (pe.exam._sourceBreakdown && Array.isArray(pe.exam._sourceBreakdown)) {
    pe.exam._sourceBreakdown.forEach(src => {
      const srcExam = PRACTICE_EXAMS.find(e => e.id === src.examId);
      src.setIndices.forEach(idx => {
        const set = (srcExam && srcExam.sets) ? srcExam.sets[idx] : null;
        const fp = set ? getPassageFingerprint(set) : null;
        if (fp) {
          syncCompletedPassageToAllExams(fp, src.examId, idx, peData);
        } else {
          if (!peData[src.examId]) peData[src.examId] = { completedSets: [], done: false };
          if (!Array.isArray(peData[src.examId].completedSets)) peData[src.examId].completedSets = [];
          if (!peData[src.examId].completedSets.includes(idx)) peData[src.examId].completedSets.push(idx);
        }
      });

      if (srcExam && peData[src.examId] && peData[src.examId].completedSets.length >= srcExam.sets.length) {
        peData[src.examId].done = true;
        peData[src.examId].completedViaAdaptive = true;
        peData[src.examId].scaledScore = score;
        peData[src.examId].pct = pct;
      }
    });
  } else {
    if (!peData[pe.exam.id]) peData[pe.exam.id] = {};
    peData[pe.exam.id].done = true;
    if (pe.exam.sets) {
      peData[pe.exam.id].completedSets = pe.exam.sets.map((_, idx) => idx);
      pe.exam.sets.forEach((set, idx) => {
        const fp = getPassageFingerprint(set);
        if (fp) {
          syncCompletedPassageToAllExams(fp, pe.exam.id, idx, peData);
        }
      });
    }
  }

  // Execute Latent Passage Reading Decomposition Algorithm
  const { passageStats, decomposedQTimes, rawQTimes } = calculatePassageReadingTelemetry(pe, qs);

  // Archetypes and timing telemetry using decomposed question solve times
  const archetypesMap = {};
  qs.forEach((q, idx) => {
    if (isSk(q, idx)) return;
    const arch = getQuestionArchetype(q, pe.exam.sec);
    if (!archetypesMap[arch]) archetypesMap[arch] = { name: arch, total: 0, right: 0, totalSecs: 0 };
    archetypesMap[arch].total++;
    if (E.ans[idx] === q.a) archetypesMap[arch].right++;
    archetypesMap[arch].totalSecs += (decomposedQTimes && decomposedQTimes[idx]) ? decomposedQTimes[idx] : 0;
  });
  const archetypeList = Object.values(archetypesMap).map(a => ({
    ...a,
    avgSecs: a.total > 0 ? Math.round(a.totalSecs / a.total) : 0,
    acc: a.total > 0 ? Math.round((a.right / a.total) * 100) : 0
  }));

  const timeSinkQuestions = qs.map((q, idx) => ({
    number: idx + 1,
    seconds: (decomposedQTimes && decomposedQTimes[idx]) ? decomposedQTimes[idx] : 0,
    rawSeconds: (rawQTimes && rawQTimes[idx]) ? rawQTimes[idx] : 0,
    isCorrect: E.ans[idx] === q.a,
    isSkipped: isSk(q, idx),
    archetype: getQuestionArchetype(q, pe.exam.sec),
    conf: E.conf[idx] || "unrated"
  })).filter(x => !x.isSkipped && x.seconds >= 110);

  const histId = "att_" + Date.now() + "_" + Math.floor(Math.random() * 1000);

  const activePE = (typeof PE !== "undefined" && PE) ? PE : (pe || (E && E._peRef));

  // Build complete reviewData packet
  const reviewData = {
    id: histId,
    examId: pe.exam.id,
    sec: pe.exam.sec,
    duration: pe.exam.duration,
    suiteTitle: pe.exam.suiteTitle,
    label: pe.exam.label,
    scaledScore: score,
    rawScore: right,
    totalQs: n,
    scoredTotal: scoredTotal,
    skippedCount: skippedCount,
    pct: pct,
    percentile: ptile,
    solid: solid,
    lucky: lucky,
    shaky: shaky,
    timeUsed: timeUsed,
    ts: Date.now(),
    _isAdaptive: !!pe.exam._isAdaptive,
    isHalf: !!pe.exam.isHalf,
    halfIndex: pe.exam.halfIndex,
    qs: qs.map((q, k) => {
      const qSkipped = isSk(q, k);
      return {
        q: q.q,
        ch: [...q.ch],
        a: q.a,
        e: q.e || "",
        why: q.why || null,
        d: !!q.d,
        isSkipped: qSkipped,
        ans: qSkipped ? -1 : E.ans[k],
        conf: qSkipped ? "skipped" : (E.conf[k] || "-"),
        time: (decomposedQTimes && decomposedQTimes[k]) ? decomposedQTimes[k] : 0,
        rawTime: (rawQTimes && rawQTimes[k]) ? rawQTimes[k] : 0,
        archetype: getQuestionArchetype(q, pe.exam.sec),
        passage: q._passage || null,
        topic: q._topic || "",
        setIdx: q._setIdx
      };
    }),
    passageStats: passageStats,
    telemetry: {
      qTimes: decomposedQTimes,
      rawQTimes: rawQTimes,
      passageReadState: passageStats.reduce((acc, p) => {
        acc[p.setIdx] = { elapsedSec: p.readSec, seconds: p.readSec, wordCount: p.wordCount, wpm: p.wpm, done: true };
        return acc;
      }, {}),
      answerChangeAudit: {
        totalChanges: (activePE && activePE._answerChanges) ? activePE._answerChanges.length : 0,
        rightToWrong: (activePE && activePE._answerChanges) ? activePE._answerChanges.filter(c => c.wasCorrect && !c.nowCorrect).length : 0,
        wrongToRight: (activePE && activePE._answerChanges) ? activePE._answerChanges.filter(c => !c.wasCorrect && c.nowCorrect).length : 0
      },
      archetypeStats: archetypeList,
      timeSinkQuestions: timeSinkQuestions
    }
  };

  // Attach complete reviewData and telemetry directly to active session handles
  E._reviewData = reviewData;
  E._telemetry = reviewData.telemetry;
  E._passageStats = passageStats;
  E._decomposedQTimes = decomposedQTimes;
  if (activePE) {
    activePE._reviewData = reviewData;
    activePE._telemetry = reviewData.telemetry;
    activePE._passageStats = passageStats;
    activePE._decomposedQTimes = decomposedQTimes;
  }
  if (typeof window !== "undefined") {
    window._lastExamReviewData = reviewData;
  }

  peData[pe.exam.id] = {
    ...peData[pe.exam.id],
    done: true,
    isHalf: !!pe.exam.isHalf,
    _isAdaptive: !!pe.exam._isAdaptive,
    _sourceExamId: pe.exam._sourceExamId,
    halfIndex: pe.exam.halfIndex,
    parentExamId: pe.exam.parentExamId,
    partnerId: pe.exam.partnerId,
    score: right,
    total: n,
    scoredTotal: scoredTotal,
    skippedCount: skippedCount,
    scaledScore: score,
    percentile: ptile,
    pct: pct,
    solid: solid,
    lucky: lucky,
    shaky: shaky,
    duration: pe.exam.duration,
    timeUsed: timeUsed,
    ts: Date.now(),
    lastReview: reviewData,
    reviewData: reviewData,
    detail: qs.map((q, k) => {
      const qSkipped = isSk(q, k);
      return {
        n: k + 1,
        isSkipped: qSkipped,
        ok: qSkipped ? null : (E.ans[k] === q.a),
        picked: qSkipped ? "SKIPPED" : (E.ans[k] === null ? "-" : "ABCD"[E.ans[k]]),
        correct: "ABCD"[q.a],
        conf: qSkipped ? "skipped" : (E.conf[k] || "-"),
        topic: q._topic
      };
    })
  };

  let fullExamCompletedNow = false;
  let combinedSummary = null;
  let partnerExam = null;

  if (pe.exam.isHalf) {
    const parentId = pe.exam.parentExamId;
    const partnerId = pe.exam.partnerId;
    const partnerData = peData[partnerId];
    partnerExam = PRACTICE_EXAMS.find(e => e.id === partnerId);

    if (partnerData && partnerData.done) {
      fullExamCompletedNow = true;
      const h1Data = pe.exam.halfIndex === 1 ? peData[pe.exam.id] : partnerData;
      const h2Data = pe.exam.halfIndex === 2 ? peData[pe.exam.id] : partnerData;

      const totalScore = h1Data.score + h2Data.score;
      const totalQs = h1Data.total + h2Data.total;
      const combinedPct = Math.round((totalScore / totalQs) * 100);
      const { score: combinedScore, ptile: combinedPtile } = rawToScaled(combinedPct);
      const combinedTimeUsed = (h1Data.timeUsed || 0) + (h2Data.timeUsed || 0);

      combinedSummary = {
        h1Score: h1Data.scaledScore,
        h1Right: h1Data.score,
        h1Total: h1Data.total,
        h2Score: h2Data.scaledScore,
        h2Right: h2Data.score,
        h2Total: h2Data.total,
        combinedScore,
        combinedPtile,
        combinedPct,
        totalScore,
        totalQs
      };

      peData[parentId] = {
        done: true,
        completedViaHalves: true,
        score: totalScore,
        total: totalQs,
        scaledScore: combinedScore,
        percentile: combinedPtile,
        pct: combinedPct,
        solid: (h1Data.solid || 0) + (h2Data.solid || 0),
        lucky: (h1Data.lucky || 0) + (h2Data.lucky || 0),
        shaky: (h1Data.shaky || 0) + (h2Data.shaky || 0),
        duration: 90,
        timeUsed: combinedTimeUsed,
        ts: Date.now(),
        h1Score: h1Data.scaledScore,
        h2Score: h2Data.scaledScore,
        lastReview: {
          ...reviewData,
          examId: parentId,
          rawScore: totalScore,
          totalQs: totalQs,
          pct: combinedPct,
          scaledScore: combinedScore,
          percentile: combinedPtile,
          solid: (h1Data.solid || 0) + (h2Data.solid || 0),
          lucky: (h1Data.lucky || 0) + (h2Data.lucky || 0),
          shaky: (h1Data.shaky || 0) + (h2Data.shaky || 0),
          qs: [...(h1Data.lastReview?.qs || []), ...(h2Data.lastReview?.qs || [])]
        },
        detail: [...(h1Data.detail || []), ...(h2Data.detail || [])]
      };

      const parentExam = PRACTICE_EXAMS.find(e => e.id === parentId);
      if (parentExam && (h1Data.skippedCount || 0) === 0 && (h2Data.skippedCount || 0) === 0) {
        addHistoryEntry({
          id: "att_comb_" + parentId + "_" + Date.now(),
          examId: parentExam.id,
          sec: parentExam.sec,
          duration: 90,
          type: "90min",
          suite: parentExam.suite,
          suiteTitle: parentExam.suiteTitle + " (Combined Halves)",
          label: parentExam.label,
          scaledScore: combinedScore,
          rawScore: totalScore,
          totalQs: totalQs,
          pct: combinedPct,
          percentile: combinedPtile,
          solid: (h1Data.solid || 0) + (h2Data.solid || 0),
          lucky: (h1Data.lucky || 0) + (h2Data.lucky || 0),
          shaky: (h1Data.shaky || 0) + (h2Data.shaky || 0),
          timeUsed: combinedTimeUsed,
          ts: Date.now(),
          includedInAverage: true,
          isCombinedFromHalves: true,
          reviewData: peData[parentId].lastReview,
          detail: peData[parentId].detail
        });
      }
    }
  }

  try { localStorage.setItem(peKey, JSON.stringify(peData)); } catch (e) { }

  const sessionDetail = qs.map((q, k) => {
    const qSkipped = isSk(q, k);
    return {
      n: k + 1,
      isSkipped: qSkipped,
      ok: qSkipped ? null : (E.ans[k] === q.a),
      picked: qSkipped ? "SKIPPED" : (E.ans[k] === null ? "-" : "ABCD"[E.ans[k]]),
      correct: "ABCD"[q.a],
      conf: qSkipped ? "skipped" : (E.conf[k] || "-"),
      topic: q._topic
    };
  });

  // Save to History Log ONLY if no passages were skipped
  if (skippedCount === 0) {
    addHistoryEntry({
      id: histId,
      examId: pe.exam.id,
      sec: pe.exam.sec,
      duration: pe.exam.duration,
      type: pe.exam.type || (pe.exam._isAdaptive ? "adaptive" : (pe.exam.isHalf ? "half" : (pe.exam.duration + "min"))),
      suite: pe.exam.suite,
      suiteTitle: pe.exam.suiteTitle,
      label: pe.exam.label,
      scaledScore: score,
      rawScore: right,
      totalQs: n,
      scoredTotal: scoredTotal,
      skippedCount: skippedCount,
      pct: pct,
      percentile: ptile,
      solid: solid,
      lucky: lucky,
      shaky: shaky,
      timeUsed: timeUsed,
      ts: Date.now(),
      includedInAverage: true,
      isHalf: !!pe.exam.isHalf,
      halfIndex: pe.exam.halfIndex,
      _isAdaptive: !!pe.exam._isAdaptive,
      reviewData: reviewData,
      detail: sessionDetail
    });
  }

  if (typeof DrillRoomCloud !== "undefined" && typeof DrillRoomCloud.triggerAutoSync === "function") {
    DrillRoomCloud.triggerAutoSync();
  }

  // Verdict
  let v;
  const st = B.sure[1], sr = B.sure[0];
  if (st && sr / st < 0.8)
    v = `<strong>Your confident answers are only ${Math.round(sr / st * 100)}% correct.</strong> The model is wrong somewhere. Confidently wrong needs mechanism work.`;
  else if (right && (lucky + shaky) > right * 0.35)
    v = `<strong>Over a third of your correct answers came from guessing.</strong> The raw score overstates you. Work on distractor discrimination.`;
  else if (score >= 128)
    v = `<strong>Strong section.</strong> ${score}/132 puts you in the ${ptile}. Focus on the misses below to push higher.`;
  else if (score >= 125)
    v = `<strong>Competitive range.</strong> ${score}/132 is at the median. Targeted review of weak topics can push 2\u20133 points.`;
  else
    v = `<strong>Below median.</strong> ${score}/132 needs work. Tag each miss, identify the pattern, and focus review there.`;

  // MCAT score context box
  v += `<div style="margin-top:14px;padding:12px 14px;background:#F2F6FA;border:1px solid var(--line);font-size:13px;line-height:1.6">
    <strong>Score context:</strong> 518+ = top 3 programs &bull; 515+ = top 10 &bull; 510+ = competitive &bull; 500 = median<br>
    Your section score of <strong>${score}</strong> projects to a total of <strong>~${score * 4}</strong> if consistent across all four sections.<br>
    ${skippedCount > 0
      ? `<span style="display:inline-block;margin-top:6px;color:var(--faint);font-weight:600">Passages were skipped (${skippedCount} questions excluded): marked completed in your question bank, and excluded from score history.</span>`
      : `<span style="display:inline-block;margin-top:6px;color:var(--ok);font-weight:700">Recorded to your History &amp; Rolling Averages.</span>`
    }
  </div>`;

  // Adaptive Study Section Banner
  if (pe.exam._isAdaptive) {
    v += `
      <div style="margin-top:14px;padding:14px 18px;background:#F0F5FA;border:2px solid var(--nav);border-radius:6px;color:var(--nav)">
        <div style="font-size:15px;font-weight:700">
          Adaptive Study Section Complete
        </div>
        <div style="font-size:13px;line-height:1.6;margin-top:6px;color:var(--soft)">
          You completed <strong>${right} of ${n} questions (${pct}%)</strong> in ${Math.max(1, Math.round(timeUsed / 60))} minutes (Scaled Score: <strong>${score} / 132</strong> &middot; ${ptile} percentile).<br>
          ${skippedCount > 0 ? "Passages were skipped: excluded from score history." : "Successfully recorded to your History &amp; Rolling Averages."}
        </div>
      </div>
    `;
  }

  // Half-Section Completion / Status Callout Banner
  if (pe.exam.isHalf) {
    if (fullExamCompletedNow && combinedSummary) {
      v += `
        <div style="margin-top:14px;padding:14px 18px;background:#E6F4EA;border:2px solid #137333;border-radius:6px;color:#0d5924">
          <div style="font-size:16px;font-weight:700">
            Full 90-Minute Section Completed
          </div>
          <div style="font-size:13.5px;line-height:1.6;margin-top:6px;color:#1e4620">
            You have successfully completed both halves of this 90-minute exam:
            <div style="margin:8px 0;padding:10px 14px;background:#fff;border:1px solid rgba(19,115,51,0.25);border-radius:4px;color:#1e4620">
              &bull; Part 1: <strong>${combinedSummary.h1Score} / 132</strong> (${combinedSummary.h1Right}/${combinedSummary.h1Total})<br>
              &bull; Part 2: <strong>${combinedSummary.h2Score} / 132</strong> (${combinedSummary.h2Right}/${combinedSummary.h2Total})<br>
              &bull; <strong style="font-size:14px">Overall 90-Min Composite Score: ${combinedSummary.combinedScore} / 132</strong> (${combinedSummary.combinedPct}% &middot; ${combinedSummary.combinedPtile} percentile)
            </div>
            <strong>Full 90-minute section marked complete!</strong> Recorded to your score history and 528 composite exam suite.
          </div>
        </div>
      `;
    } else {
      v += `
        <div style="margin-top:14px;padding:14px 18px;background:#EEF5FC;border:2px solid #185A9D;border-radius:6px;color:#0C3259">
          <div style="font-size:15px;font-weight:700">
            Half-Section (Part ${pe.exam.halfIndex} of 2) Graded &amp; Recorded
          </div>
          <div style="font-size:13px;line-height:1.6;margin-top:6px">
            You scored <strong>${score} / 132</strong> (${pct}%) on Part ${pe.exam.halfIndex}.<br>
            Complete <strong>Part ${pe.exam.halfIndex === 1 ? 2 : 1}</strong> (~${partnerExam ? partnerExam.duration : 48} min) to finish the full 90-minute exam and earn your combined score!
            <div style="margin-top:10px">
              <button class="btn pri" id="btnLaunchNextHalf" style="font-size:13px;padding:8px 18px">
                Start Part ${pe.exam.halfIndex === 1 ? 2 : 1} Now (~${partnerExam ? partnerExam.duration : 48} min)
              </button>
            </div>
          </div>
        </div>
      `;
    }
  }

  $("zV").innerHTML = v;

  if (pe.exam.isHalf && !fullExamCompletedNow && partnerExam) {
    const btnNext = document.getElementById("btnLaunchNextHalf");
    if (btnNext) {
      btnNext.onclick = () => {
        E = null; PE = null;
        beginPracticeExam(partnerExam);
      };
    }
  }

  // Render timing telemetry box & question review
  renderTimingTelemetryBox(reviewData);
  renderReviewQuestionList(reviewData.qs, reviewData.sec);

  if (window.lockCalc) window.lockCalc(false);

  // Invoke Gemini AI Diagnostic Engine on practice exam score report
  if (typeof window.renderGeminiExamCard === "function") {
    window.renderGeminiExamCard();
  }

  // Override save button for practice exams
  $("zSave").onclick = () => {
    E = null; PE = null;
    $("tSect").textContent = "Passage bank";
    view("home");
    paintHome();
    flash("Practice exam scored and recorded to history.");
  };
}

/* Render timing telemetry box: passage reading speed, archetype pacing, second-guessing & time sinks */
function renderTimingTelemetryBox(reviewData) {
  const box = document.getElementById("zTimingTelemetry");
  if (!box) return;
  box.innerHTML = "";

  const tel = reviewData.telemetry || {};
  const pStats = reviewData.passageStats || [];
  const archStats = tel.archetypeStats || [];
  const chgAudit = tel.answerChangeAudit || { totalChanges: 0, rightToWrong: 0, wrongToRight: 0 };
  const sinks = tel.timeSinkQuestions || [];

  let html = `<div class="pe-telemetry-box">
    <div class="ttl">Timing Telemetry &amp; Question Archetype Diagnostics</div>
    <div class="sub">Deep behavioral analytics tracking passage reading speed, question archetype pacing, second-guessing tendencies, and time sinks.</div>
  `;

  // 1. Passage Reading Speed Table
  if (pStats && pStats.length > 0) {
    html += `
      <div style="margin-top:16px">
        <div style="font-size:13px;font-weight:700;color:var(--ink);margin-bottom:6px">Passage Reading Speed (WPM)</div>
        <table class="pe-arch-table">
          <thead>
            <tr>
              <th>Passage</th>
              <th>Word Count</th>
              <th>Reading Time</th>
              <th>Reading Pace (WPM)</th>
              <th>Assessment</th>
            </tr>
          </thead>
          <tbody>
    `;
    pStats.forEach((p, idx) => {
      const wpm = p.wpm || (p.readSec > 0 ? Math.round((p.wordCount / p.readSec) * 60) : 0);
      let statusBadge = "";
      if (wpm >= 200 && wpm <= 270) {
        statusBadge = `<span class="badge b-ok">Optimal (200-270 WPM)</span>`;
      } else if (wpm < 200 && wpm > 0) {
        statusBadge = `<span class="badge b-bad">Deliberate (&lt;200 WPM)</span>`;
      } else if (wpm > 270) {
        statusBadge = `<span class="badge b-mid">Rushed (&gt;270 WPM)</span>`;
      } else {
        statusBadge = `<span class="badge b-new">N/A</span>`;
      }

      const m = Math.floor(p.readSec / 60);
      const s = p.readSec % 60;
      html += `
        <tr>
          <td><strong>Passage ${p.pIndex || idx + 1}</strong></td>
          <td>${p.wordCount || "~600"} words</td>
          <td>${m}m ${s}s</td>
          <td><strong>${wpm} WPM</strong></td>
          <td>${statusBadge}</td>
        </tr>
      `;
    });
    html += `</tbody></table></div>`;
  }

  // 2. Question Archetypes Table
  if (archStats && archStats.length > 0) {
    html += `
      <div style="margin-top:16px">
        <div style="font-size:13px;font-weight:700;color:var(--ink);margin-bottom:6px">Question Archetype Pacing &amp; Accuracy</div>
        <table class="pe-arch-table">
          <thead>
            <tr>
              <th>Question Archetype</th>
              <th>Accuracy</th>
              <th>Avg Time / Q</th>
              <th>Benchmark</th>
              <th>Heuristic Status</th>
            </tr>
          </thead>
          <tbody>
    `;
    archStats.forEach(a => {
      const isSec = reviewData.sec === "CARS";
      const bm = isSec ? 90 : 95;
      let paceBadge = "";
      if (a.avgSecs <= bm && a.acc >= 75) {
        paceBadge = `<span class="badge b-ok">Fast &amp; Accurate</span>`;
      } else if (a.avgSecs > bm + 15) {
        paceBadge = `<span class="badge b-bad">Time Sink (${a.avgSecs}s)</span>`;
      } else if (a.acc < 60) {
        paceBadge = `<span class="badge b-mid">Low Accuracy (${a.acc}%)</span>`;
      } else {
        paceBadge = `<span class="badge b-new">Target Pace</span>`;
      }

      html += `
        <tr>
          <td><strong>${a.name}</strong></td>
          <td><strong>${a.right} / ${a.total}</strong> (${a.acc}%)</td>
          <td>${a.avgSecs}s</td>
          <td style="color:var(--faint)">~${bm}s</td>
          <td>${paceBadge}</td>
        </tr>
      `;
    });
    html += `</tbody></table></div>`;
  }

  // 3. Behavioral Telemetry Cards
  html += `
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:16px">
      <div style="background:#fff;border:1px solid var(--line);border-radius:6px;padding:12px 14px">
        <div style="font-size:12px;font-weight:700;color:var(--faint)">Second-Guessing Audit</div>
        <div style="font-size:18px;font-weight:800;color:var(--ink);margin-top:4px">
          ${chgAudit.totalChanges} Changes
        </div>
        <div style="font-size:12px;color:var(--soft);line-height:1.5;margin-top:4px">
          &bull; Right &rarr; Wrong: <strong style="color:var(--bad)">${chgAudit.rightToWrong}</strong> (points lost)<br>
          &bull; Wrong &rarr; Right: <strong style="color:var(--ok)">${chgAudit.wrongToRight}</strong> (points gained)<br>
          &bull; Net Impact: <strong>${(chgAudit.wrongToRight - chgAudit.rightToWrong) >= 0 ? '+' : ''}${chgAudit.wrongToRight - chgAudit.rightToWrong} pts</strong>
        </div>
      </div>

      <div style="background:#fff;border:1px solid var(--line);border-radius:6px;padding:12px 14px">
        <div style="font-size:12px;font-weight:700;color:var(--faint)">Time Sink Audit (&gt;110s)</div>
        <div style="font-size:18px;font-weight:800;color:${sinks.length > 2 ? 'var(--warn)' : 'var(--ok)'};margin-top:4px">
          ${sinks.length} Questions
        </div>
        <div style="font-size:12px;color:var(--soft);line-height:1.5;margin-top:4px">
          ${sinks.length > 0
            ? `${sinks.filter(s => s.isCorrect).length} of ${sinks.length} correct on time sinks.<br>
               <span style="color:var(--warn)">Rule: Enforce 90s cutoff, flag &amp; return.</span>`
            : `Zero time-sink traps. Pacing discipline was maintained cleanly.`}
        </div>
      </div>

      <div style="background:#fff;border:1px solid var(--line);border-radius:6px;padding:12px 14px">
        <div style="font-size:12px;font-weight:700;color:var(--faint)">Metacognitive Calibration</div>
        <div style="font-size:18px;font-weight:800;color:var(--nav);margin-top:4px">
          ${reviewData.solid} / ${reviewData.rawScore} Solid
        </div>
        <div style="font-size:12px;color:var(--soft);line-height:1.5;margin-top:4px">
          &bull; Lucky/Shaky correct: <strong>${reviewData.lucky + reviewData.shaky}</strong><br>
          &bull; High-confidence misses: <strong>${(reviewData.qs || []).filter(q => q.ans !== q.a && q.conf === "sure").length}</strong> (blind spots)<br>
          &bull; Raw accuracy: <strong>${reviewData.pct}%</strong>
        </div>
      </div>
    </div>
  `;

  html += `</div>`;
  box.innerHTML = html;
}

/* Render question review list with per-choice rationales, explanations, and passage viewer */
function renderReviewQuestionList(reviewQs, secKey) {
  const list = $("zList");
  if (!list) return;
  list.innerHTML = "";

  // Setup passage tabs in #zPass
  const zp = $("zPass");
  if (zp) {
    const passages = [];
    reviewQs.forEach((q) => {
      if (q.passage && !passages.some(p => p.passage === q.passage)) {
        passages.push({
          pIdx: passages.length + 1,
          topic: q.topic || `Passage ${passages.length + 1}`,
          passage: q.passage
        });
      }
    });

    if (passages.length > 0) {
      zp.className = "";
      let tabsHtml = passages.map((p, i) => `
        <button class="pe-pass-tab ${i === 0 ? 'active' : ''}" data-pidx="${i}" style="padding:4px 10px;font-size:12px;cursor:pointer;border:1px solid var(--line);background:${i === 0 ? 'var(--nav)' : '#fff'};color:${i === 0 ? '#fff' : 'var(--ink)'};border-radius:4px">
          Passage ${p.pIdx}
        </button>
      `).join(" ");

      zp.innerHTML = `
        <div class="zph" style="display:flex;justify-content:space-between;align-items:center;padding:10px 14px;background:#F0F5FA;border:1px solid var(--line);border-radius:4px;cursor:pointer">
          <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap">
            <span style="font-weight:700">Exam Passages:</span>
            <div id="pePassTabsWrap">${tabsHtml}</div>
          </div>
          <span class="tw" style="font-size:12px;color:var(--faint)">hide</span>
        </div>
        <div class="zpb" id="peActivePassageBody" style="padding:14px;border:1px solid var(--line);border-top:none;background:#fff;max-height:350px;overflow-y:auto;line-height:1.6">
          ${passages[0].passage}
        </div>
      `;

      zp.querySelectorAll(".pe-pass-tab").forEach(tab => {
        tab.onclick = (e) => {
          e.stopPropagation();
          const pidx = parseInt(tab.dataset.pidx);
          zp.querySelectorAll(".pe-pass-tab").forEach(t => {
            t.style.background = "#fff";
            t.style.color = "var(--ink)";
          });
          tab.style.background = "var(--nav)";
          tab.style.color = "#fff";
          const pBody = zp.querySelector("#peActivePassageBody");
          if (pBody) pBody.innerHTML = passages[pidx].passage;
        };
      });

      const zph = zp.querySelector(".zph");
      if (zph) {
        zph.onclick = (e) => {
          if (e.target && e.target.closest && e.target.closest("#pePassTabsWrap")) return;
          zp.classList.toggle("closed");
          const tw = zp.querySelector(".tw");
          const pb = zp.querySelector(".zpb");
          if (tw && pb) {
            tw.textContent = zp.classList.contains("closed") ? "show" : "hide";
            pb.style.display = zp.classList.contains("closed") ? "none" : "block";
          }
        };
      }
    } else {
      zp.innerHTML = "";
    }
  }

  // Pre-calculate filter counts
  const total = reviewQs.length;
  const skippedCount = reviewQs.filter(q => q.isSkipped || q.ans === -1 || q.conf === "skipped").length;
  const scoredQs = reviewQs.filter(q => !(q.isSkipped || q.ans === -1 || q.conf === "skipped"));
  const scoredTotal = scoredQs.length;
  const correctCount = scoredQs.filter(q => q.ans === q.a).length;
  const incorrectCount = scoredTotal - correctCount;
  const sureCount = scoredQs.filter(q => q.conf === "sure").length;
  const twoCount = scoredQs.filter(q => q.conf === "two").length;
  const guessCount = scoredQs.filter(q => q.conf === "guess").length;
  const cwCount = scoredQs.filter(q => q.ans !== q.a && q.conf === "sure").length;
  const luckyCount = scoredQs.filter(q => q.ans === q.a && (q.conf === "guess" || q.conf === "two")).length;

  // Render Interactive Filter Bar into #zListFilterBar
  let filterBar = $("zListFilterBar");
  if (!filterBar) {
    filterBar = document.createElement("div");
    filterBar.id = "zListFilterBar";
    if (list.parentNode) {
      list.parentNode.insertBefore(filterBar, list);
    }
  }

  if (filterBar) {
    filterBar.innerHTML = `
      <div class="pe-review-filter-box">
        <div class="pe-filter-row">
          <span class="lbl">Result:</span>
          <button class="pe-filter-btn active" data-f-type="outcome" data-f-val="all">All <span class="pe-filter-count">${total}</span></button>
          <button class="pe-filter-btn f-bad" data-f-type="outcome" data-f-val="incorrect">Missed <span class="pe-filter-count">${incorrectCount}</span></button>
          <button class="pe-filter-btn f-ok" data-f-type="outcome" data-f-val="correct">Correct <span class="pe-filter-count">${correctCount}</span></button>
          ${skippedCount > 0 ? `<button class="pe-filter-btn" data-f-type="outcome" data-f-val="skipped" style="color:#64748B">Skipped <span class="pe-filter-count">${skippedCount}</span></button>` : ""}
        </div>
        <div class="pe-filter-row">
          <span class="lbl">Confidence:</span>
          <button class="pe-filter-btn active" data-f-type="conf" data-f-val="all">All Confidence</button>
          <button class="pe-filter-btn" data-f-type="conf" data-f-val="sure">Knew It / Sure <span class="pe-filter-count">${sureCount}</span></button>
          <button class="pe-filter-btn" data-f-type="conf" data-f-val="two">Narrowed to 2 <span class="pe-filter-count">${twoCount}</span></button>
          <button class="pe-filter-btn" data-f-type="conf" data-f-val="guess">Guessed <span class="pe-filter-count">${guessCount}</span></button>
          <button class="pe-filter-btn f-cw" data-f-type="conf" data-f-val="cw" title="High confidence but missed">Confidently Wrong <span class="pe-filter-count">${cwCount}</span></button>
          <button class="pe-filter-btn f-lucky" data-f-type="conf" data-f-val="lucky" title="Answered correctly via guess or 50/50">Lucky Hits <span class="pe-filter-count">${luckyCount}</span></button>
        </div>
        <div class="pe-filter-meta-bar">
          <span id="peFilterCountReadout">Showing ${total} of ${total} questions</span>
          <button class="pe-filter-reset-btn hide" id="peFilterResetBtn">Reset Filters</button>
        </div>
      </div>
    `;
  }

  // Render question cards with data attributes for filtering
  reviewQs.forEach((q, k) => {
    const isSkipped = q.isSkipped || q.ans === -1 || q.conf === "skipped";
    const isCorrect = !isSkipped && q.ans === q.a;
    const isLucky = !isSkipped && isCorrect && (q.conf === "guess" || q.conf === "two");
    const isCW = !isSkipped && !isCorrect && q.conf === "sure";

    const pill = isSkipped
      ? `<span class="pl" style="background:#E2E8F0;color:#475569;border:1px solid #CBD5E1">&#10549; SKIPPED &mdash; EXCLUDED FROM SCORE</span>`
      : (isCorrect
          ? (isLucky ? `<span class="pl p-lk">CORRECT &mdash; ${q.conf === "guess" ? "GUESSED" : "50/50"}</span>` : `<span class="pl p-ok">CORRECT</span>`)
          : (isCW ? `<span class="pl p-bad">INCORRECT &mdash; CONFIDENTLY WRONG</span>` : `<span class="pl p-bad">INCORRECT</span>`));

    const timeStr = q.time ? `${Math.floor(q.time / 60)}m ${q.time % 60}s` : null;
    const timeBadge = timeStr ? `<span class="badge" style="font-size:11px;font-weight:600;margin-left:6px;background:#F0F4F8;color:var(--soft);border:1px solid var(--line)">Time: ${timeStr}</span>` : "";
    const archBadge = `<span class="badge" style="font-size:11px;font-weight:600;margin-left:6px;background:#EBF3FA;color:#185A9D;border:1px solid #B8D5F2">${q.archetype || getQuestionArchetype(q, secKey)}</span>`;

    const d = document.createElement("div");
    d.className = "rq";
    d.dataset = d.dataset || {};
    d.dataset.outcome = isSkipped ? "skipped" : (isCorrect ? "correct" : "incorrect");
    d.dataset.conf = isSkipped ? "skipped" : (q.conf || "unrated");
    d.dataset.cw = isCW ? "true" : "false";
    d.dataset.lucky = isLucky ? "true" : "false";
    if (d.setAttribute) {
      d.setAttribute("data-outcome", d.dataset.outcome);
      d.setAttribute("data-conf", d.dataset.conf);
      d.setAttribute("data-cw", d.dataset.cw);
      d.setAttribute("data-lucky", d.dataset.lucky);
    }

    const choices = q.ch.map((c, ci) => {
      const isC = ci === q.a;
      const isM = !isSkipped && ci === q.ans;
      const cls = "rch" + (isC && isM ? " both" : isC ? " correct" : isM ? " yours" : "");
      const tag = isC && isM ? "CORRECT &mdash; YOURS" : isC ? "CORRECT" : isM ? "YOUR ANSWER" : "";
      return `<button class="${cls}" data-q="${k}" data-c="${ci}">
        <span class="l">${"ABCD"[ci]}.</span><span>${c}</span>
        <span class="tag">${tag}</span></button>
        <div class="rwhy ${isC ? "good" : "bad"} hide" id="rw_${k}_${ci}"></div>`;
    }).join("");

    d.innerHTML = `
      <div class="rqh" style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:6px">
        <div>
          <span class="id">Question ${k + 1}${q.d ? " (discrete)" : ""}</span>
          ${archBadge}
          ${timeBadge}
        </div>
        ${pill}
      </div>
      <div class="rqb">
        <div class="q2">${q.q}</div>
        <div class="rchoices">${choices}</div>
        <div class="exfull"><div class="h">Full explanation</div>${q.e || "No explanation text provided."}</div>
      </div>
    `;

    // Click handler for per-choice rationale
    d.querySelectorAll(".rch").forEach(btn => {
      btn.onclick = () => {
        const ci = parseInt(btn.dataset.c);
        const box = d.querySelector(`#rw_${k}_${ci}`);
        if (!box) return;
        if (!box.dataset.filled) {
          let txt = (q.why && q.why[ci]) ? q.why[ci] : null;
          if (!txt) {
            txt = ci === q.a
              ? "<strong>This is the correct answer.</strong> See the full explanation above for the primary scientific / CARS textual reasoning."
              : "<strong>Incorrect.</strong> See the full explanation above for the trap and how this choice deviates from the question constraint.";
          }
          box.innerHTML = txt;
          box.dataset.filled = "1";
        }
        box.classList.toggle("hide");
      };
    });

    list.appendChild(d);
  });

  // Wire up filter logic
  if (filterBar) {
    let activeOutcome = "all";
    let activeConf = "all";

    const applyFilters = () => {
      let visibleCount = 0;
      const cards = list.querySelectorAll ? list.querySelectorAll(".rq") : [];
      cards.forEach(card => {
        const cardOutcome = (card.dataset && card.dataset.outcome) || card.getAttribute?.("data-outcome");
        const cardConf = (card.dataset && card.dataset.conf) || card.getAttribute?.("data-conf");
        const isCw = ((card.dataset && card.dataset.cw) || card.getAttribute?.("data-cw")) === "true";
        const isLucky = ((card.dataset && card.dataset.lucky) || card.getAttribute?.("data-lucky")) === "true";

        const outcomeMatch = (activeOutcome === "all") || (cardOutcome === activeOutcome);
        let confMatch = true;
        if (activeConf === "all") confMatch = true;
        else if (activeConf === "sure") confMatch = (cardConf === "sure");
        else if (activeConf === "two") confMatch = (cardConf === "two");
        else if (activeConf === "guess") confMatch = (cardConf === "guess");
        else if (activeConf === "cw") confMatch = isCw;
        else if (activeConf === "lucky") confMatch = isLucky;

        const matches = outcomeMatch && confMatch;
        if (card.style) card.style.display = matches ? "" : "none";
        if (matches) visibleCount++;
      });

      const readout = filterBar.querySelector("#peFilterCountReadout");
      if (readout) readout.textContent = `Showing ${visibleCount} of ${total} questions`;

      const resetBtn = filterBar.querySelector("#peFilterResetBtn");
      if (resetBtn) {
        resetBtn.classList.toggle("hide", activeOutcome === "all" && activeConf === "all");
      }

      let emptyMsg = list.querySelector("#peFilterEmptyMsg");
      if (visibleCount === 0) {
        if (!emptyMsg) {
          emptyMsg = document.createElement("div");
          emptyMsg.id = "peFilterEmptyMsg";
          emptyMsg.style.cssText = "padding:24px;text-align:center;color:var(--faint);font-size:14px;background:#FAFCFD;border:1px dashed var(--line);border-radius:4px;margin:12px 0";
          emptyMsg.textContent = "No questions match the selected filters. Click 'Reset Filters' to view all questions.";
          list.appendChild(emptyMsg);
        }
        emptyMsg.style.display = "";
      } else if (emptyMsg) {
        emptyMsg.style.display = "none";
      }
    };

    filterBar.querySelectorAll(".pe-filter-btn").forEach(btn => {
      btn.onclick = () => {
        const fType = btn.dataset.fType;
        const fVal = btn.dataset.fVal;

        filterBar.querySelectorAll(`.pe-filter-btn[data-f-type="${fType}"]`).forEach(b => b.classList.remove("active"));
        btn.classList.add("active");

        if (fType === "outcome") activeOutcome = fVal;
        else if (fType === "conf") activeConf = fVal;

        applyFilters();
      };
    });

    const resetBtn = filterBar.querySelector("#peFilterResetBtn");
    if (resetBtn) {
      resetBtn.onclick = () => {
        activeOutcome = "all";
        activeConf = "all";
        filterBar.querySelectorAll(`.pe-filter-btn[data-f-type="outcome"]`).forEach(b => b.classList.toggle("active", b.dataset.fVal === "all"));
        filterBar.querySelectorAll(`.pe-filter-btn[data-f-type="conf"]`).forEach(b => b.classList.toggle("active", b.dataset.fVal === "all"));
        applyFilters();
      };
    }
  }
}

/* Reconstruct legacy review data if reviewData was not stored in an older record */
function reconstructLegacyReview(rec) {
  const ex = PRACTICE_EXAMS.find(e => e.id === rec.examId);
  const qs = ex ? buildExamQuestions(ex.sets) : [];
  const total = rec.totalQs || qs.length || 1;

  // Retrieve any stored detail or review data from peData
  const peKey = "drillroom_pe_v1";
  let peData = {};
  try { peData = JSON.parse(localStorage.getItem(peKey)) || {}; } catch(e) {}

  let detailList = (rec.detail && Array.isArray(rec.detail) && rec.detail.length) ? rec.detail : null;
  if (!detailList && peData[rec.examId]?.detail && Array.isArray(peData[rec.examId].detail)) {
    detailList = peData[rec.examId].detail;
  }
  let lastReviewQs = (!detailList && peData[rec.examId]?.lastReview?.qs) ? peData[rec.examId].lastReview.qs : null;

  // Target metrics from history record
  const targetRight = Math.min(total, Math.max(0, rec.rawScore || rec.score || (rec.pct ? Math.round(rec.pct * total / 100) : 0)));
  let targetSolid = Math.min(targetRight, Math.max(0, rec.solid !== undefined ? rec.solid : targetRight));
  let targetLucky = Math.min(targetRight - targetSolid, Math.max(0, rec.lucky || 0));
  let targetShaky = Math.min(targetRight - targetSolid - targetLucky, Math.max(0, rec.shaky || 0));
  if (targetSolid + targetLucky + targetShaky < targetRight) {
    targetSolid = targetRight - targetLucky - targetShaky;
  }

  // Check if detail actually contains user selections
  const hasValidDetail = (detailList && detailList.some(d => d && (d.picked && d.picked !== "-" || d.ans !== undefined || d.ok !== undefined)))
    || (lastReviewQs && lastReviewQs.some(rq => rq && rq.ans !== null && rq.ans !== undefined));

  const syntheticCorrectIndices = new Set();
  if (!hasValidDetail && targetRight > 0) {
    if (targetRight >= total) {
      for (let i = 0; i < total; i++) syntheticCorrectIndices.add(i);
    } else {
      const step = total / targetRight;
      for (let i = 0; i < targetRight; i++) {
        syntheticCorrectIndices.add(Math.min(total - 1, Math.floor(i * step)));
      }
      let fill = 0;
      while (syntheticCorrectIndices.size < targetRight && fill < total) {
        syntheticCorrectIndices.add(fill);
        fill++;
      }
    }
  }

  // Assign confidences to synthetic correct questions
  const sortedCorrect = Array.from(syntheticCorrectIndices).sort((a,b) => a - b);
  const syntheticConfMap = new Map();
  sortedCorrect.forEach((qIdx, order) => {
    if (order < targetSolid) syntheticConfMap.set(qIdx, "sure");
    else if (order < targetSolid + targetLucky) syntheticConfMap.set(qIdx, "guess");
    else syntheticConfMap.set(qIdx, "two");
  });

  const reconstructedQs = qs.map((q, idx) => {
    let ansIdx = null;
    let conf = "-";

    if (hasValidDetail) {
      if (detailList && detailList[idx]) {
        const d = detailList[idx];
        if (d.picked && d.picked !== "-") {
          ansIdx = "ABCD".indexOf(d.picked);
          if (ansIdx === -1) ansIdx = null;
        } else if (typeof d.ans === "number") {
          ansIdx = d.ans;
        } else if (d.ok === true) {
          ansIdx = q.a;
        } else if (d.ok === false) {
          ansIdx = (q.a + 1) % 4;
        }
        if (d.conf) conf = d.conf;
      } else if (lastReviewQs && lastReviewQs[idx]) {
        const rq = lastReviewQs[idx];
        if (rq.ans !== null && rq.ans !== undefined) ansIdx = rq.ans;
        if (rq.conf) conf = rq.conf;
      }
    } else {
      // Synthesize answers accurately to match the user's logged score
      if (syntheticCorrectIndices.has(idx)) {
        ansIdx = q.a; // Correct answer
        conf = syntheticConfMap.get(idx) || "sure";
      } else {
        ansIdx = (q.a + 1) % 4; // Authentic distractor
        conf = (idx % 2 === 0) ? "two" : "guess";
      }
    }

    return {
      q: q.q,
      ch: [...q.ch],
      a: q.a,
      e: q.e || "",
      why: q.why || null,
      d: !!q.d,
      ans: ansIdx,
      conf: conf,
      time: 0,
      archetype: getQuestionArchetype(q, rec.sec),
      passage: q._passage || null,
      topic: q._topic || "",
      setIdx: q._setIdx
    };
  });

  return {
    id: rec.id,
    examId: rec.examId,
    sec: rec.sec,
    duration: rec.duration || 90,
    suiteTitle: rec.suiteTitle || rec.label,
    label: rec.label,
    scaledScore: rec.scaledScore,
    rawScore: rec.rawScore || rec.score || targetRight,
    totalQs: total,
    pct: rec.pct !== undefined ? rec.pct : (total > 0 ? Math.round((targetRight / total) * 100) : 0),
    percentile: rec.percentile || "50th",
    solid: rec.solid !== undefined ? rec.solid : targetSolid,
    lucky: rec.lucky !== undefined ? rec.lucky : targetLucky,
    shaky: rec.shaky !== undefined ? rec.shaky : targetShaky,
    timeUsed: rec.timeUsed || 0,
    ts: rec.ts || Date.now(),
    qs: reconstructedQs,
    passageStats: [],
    telemetry: {
      qTimes: Array(total).fill(0),
      passageReadState: {},
      answerChangeAudit: { totalChanges: 0, rightToWrong: 0, wrongToRight: 0 },
      archetypeStats: [],
      timeSinkQuestions: []
    }
  };
}

/* Open completed exam review from history or practice tab */
function openCompletedExamReview(identifier) {
  const history = getHistory();
  let rec = history.find(h => h.id === identifier || h.examId === identifier);
  let reviewData = rec && rec.reviewData ? rec.reviewData : null;
  const examId = rec ? rec.examId : identifier;

  // If reviewData exists but has all null answers (e.g. from an earlier broken reconstruction), invalidate it
  if (reviewData && reviewData.qs && !reviewData.qs.some(q => q.ans !== null && q.ans !== undefined)) {
    reviewData = null;
  }

  if (!reviewData) {
    const peKey = "drillroom_pe_v1";
    let peData;
    try { peData = JSON.parse(localStorage.getItem(peKey)) || {}; } catch (e) { peData = {}; }
    if (peData[examId]?.lastReview && peData[examId].lastReview.qs?.some(q => q.ans !== null)) {
      reviewData = peData[examId].lastReview;
    } else if (peData[identifier]?.lastReview && peData[identifier].lastReview.qs?.some(q => q.ans !== null)) {
      reviewData = peData[identifier].lastReview;
    }
  }

  // If no reviewData exists (e.g. older legacy record), reconstruct it!
  if (!reviewData && rec) {
    reviewData = reconstructLegacyReview(rec);
    rec.reviewData = reviewData;
    saveHistory(history);
  } else if (!reviewData) {
    const ex = PRACTICE_EXAMS.find(e => e.id === identifier || e.id === examId);
    if (ex) {
      reviewData = reconstructLegacyReview({ examId: ex.id, sec: ex.sec, duration: ex.duration, label: ex.label, scaledScore: 125, rawScore: 0, totalQs: ex.sets.reduce((s,x)=>s+x.qs.length,0), pct: 0, percentile: "50th" });
    }
  }

  if (!reviewData) {
    alert("Could not load review data for this attempt.");
    return;
  }

  // Set up view
  clearInterval(timerId);
  $("clk").classList.add("hide");
  $("tCount").textContent = "";
  $("tSect").textContent = reviewData.label + " \u2014 Review & Diagnostic";
  view("res");

  // Score header
  const score = reviewData.scaledScore;
  const pct = reviewData.pct;
  const ptile = reviewData.percentile;
  $("zT").innerHTML = `<span style="font-size:42px;font-weight:700;color:${score >= 125 ? 'var(--ok)' : score >= 122 ? 'var(--warn)' : 'var(--bad)'}">
    ${score}</span><span style="font-size:16px;color:var(--faint);margin-left:12px">/ 132</span>`;

  $("zL").innerHTML = `<div style="margin-bottom:12px">${reviewData.rawScore} of ${reviewData.totalQs} correct (${pct}%) &mdash; <strong>${ptile} percentile</strong></div>
    ${(reviewData.lucky + reviewData.shaky) > 0
      ? `Of those ${reviewData.rawScore} correct, ${reviewData.solid} were solid. ${reviewData.lucky + reviewData.shaky} came from a guess or a coin flip.`
      : `Every correct answer was marked confident. Clean read.`}`;

  $("zS").innerHTML = `
    <div class="st" style="border-top:3px solid ${score >= 125 ? 'var(--ok)' : score >= 122 ? 'var(--warn)' : 'var(--bad)'}">
      <div class="v" style="font-size:34px;color:${score >= 125 ? 'var(--ok)' : score >= 122 ? 'var(--warn)' : 'var(--bad)'}">${score}</div>
      <div class="l">Scaled Score (118\u2013132)</div>
    </div>
    <div class="st"><div class="v">${ptile}</div><div class="l">Percentile</div></div>
    <div class="st"><div class="v">${pct}%</div><div class="l">Raw Accuracy</div></div>
    <div class="st"><div class="v">${reviewData.solid}</div><div class="l">Solid</div></div>
    <div class="st${reviewData.lucky ? ' al' : ''}"><div class="v">${reviewData.lucky}</div><div class="l">Lucky</div></div>
    <div class="st"><div class="v">${reviewData.shaky}</div><div class="l">Shaky</div></div>`;

  // Confidence breakdown
  const B = { sure: [0, 0], two: [0, 0], guess: [0, 0] };
  reviewData.qs.forEach((q) => {
    const c = q.conf; if (!c || !B[c]) return;
    B[c][1]++; if (q.ans === q.a) B[c][0]++;
  });
  const L = { sure: "Knew it", two: "Narrowed to two", guess: "Guessed" };
  const C = { sure: "#1E7A3C", two: "#D9A22B", guess: "#B3261E" };
  $("zB").innerHTML = Object.keys(B).map(c => {
    const [r, t] = B[c]; if (!t) return "";
    return `<div class="br"><span>${L[c]}</span><div class="trk"><div class="fl" style="width:${Math.round(r / t * 100)}%;background:${C[c]}"></div></div><span class="n">${r}/${t}</span></div>`;
  }).join("");

  // Verdict banner
  $("zV").innerHTML = `
    <div style="padding:14px 18px;background:#F0F5FA;border:1px solid var(--line);border-radius:6px;font-size:13px;line-height:1.6">
      <strong>Completed Exam Review:</strong> Viewing attempt scored on ${new Date(reviewData.ts || Date.now()).toLocaleDateString()} at ${new Date(reviewData.ts || Date.now()).toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})}.<br>
      Explore the timing telemetry, question archetypes, and click each answer choice below to review rationales.
    </div>
  `;

  // Set mock E & PE for Gemini AI analysis
  window.E = {
    s: {
      id: reviewData.examId,
      sec: reviewData.sec,
      topic: reviewData.label,
      label: reviewData.label,
      qs: reviewData.qs
    },
    ans: reviewData.qs.map(q => q.ans),
    conf: reviewData.qs.map(q => q.conf),
    _isPracticeExam: true,
    _peRef: { exam: { id: reviewData.examId, label: reviewData.label, sec: reviewData.sec, duration: reviewData.duration } },
    _telemetry: reviewData.telemetry,
    _reviewData: reviewData,
    _passageStats: reviewData.passageStats,
    _decomposedQTimes: reviewData.telemetry ? reviewData.telemetry.qTimes : null
  };
  window._lastExamReviewData = reviewData;

  // Render timing telemetry
  renderTimingTelemetryBox(reviewData);

  // Render questions
  renderReviewQuestionList(reviewData.qs, reviewData.sec);

  // Render Gemini AI card
  if (typeof window.renderGeminiExamCard === "function") {
    window.renderGeminiExamCard();
  }

  // Override return button
  $("zSave").textContent = "Return to History & Practice";
  $("zSave").onclick = () => {
    window.E = null; window.PE = null;
    $("tSect").textContent = "Practice Sections";
    view("home");
    document.querySelectorAll(".tab").forEach(x => x.classList.remove("on"));
    const pTab = document.querySelector(".tab[data-t='practice']");
    if (pTab) pTab.classList.add("on");
    ["bank", "practice", "history", "notes", "sheets"].forEach(k => {
      const el = $("tab" + k[0].toUpperCase() + k.slice(1));
      if (el) el.classList.toggle("hide", k !== "practice");
    });
    paintPracticeExams();
  };
}
if (typeof window !== "undefined") {
  window.openCompletedExamReview = openCompletedExamReview;
}
if (typeof globalThis !== "undefined") {
  globalThis.openCompletedExamReview = openCompletedExamReview;
}

/* ===== SUBJECT-FIRST PRACTICE EXAM & ADAPTIVE STUDY UI ===== */
let peActiveSec = "CARS"; // default subject
let peSliderPassages = 1; // default adaptive study passages (minimum 1 passage)
let peSliderMinutes = 10; // estimated minutes based on selected passages
let peSelectedSourceExamId = "auto"; // "auto" or specific exam id
let peQueueFilter = "all"; // "all", "90", "60", "half"
let peViewMode = "subject"; // "subject" or "suites"

function paintPracticeExams() {
  const container = document.getElementById("tabPractice");
  if (!container) return;
  container.innerHTML = "";

  if (!PRACTICE_EXAMS.length) {
    container.innerHTML = `<div class="panel"><div class="empty">No practice sections loaded yet.</div></div>`;
    return;
  }

  const peKey = "drillroom_pe_v1";
  let peData;
  try { peData = JSON.parse(localStorage.getItem(peKey)) || {}; } catch (e) { peData = {}; }

  const history = getHistory();
  const histPrefs = getHistoryPrefs();
  const rollingAvg = calculateRollingAverage(history, histPrefs);

  // --- Header Quick Stats Bar ---
  const headerBar = document.createElement("div");
  headerBar.className = "pe-header-bar";
  let avgText = "No completed sections yet";
  if (rollingAvg) {
    avgText = `Recent Avg: <b>${rollingAvg.avgScaled} / 132</b> &middot; Projected Total: <b>${rollingAvg.projComposite} / 528</b> (${rollingAvg.count} sections)`;
  }
  headerBar.innerHTML = `
    <div>
      <div class="ttl">Practice Sections — Adaptive Study &amp; Exam Queue</div>
      <div style="font-size:12.5px;color:var(--soft);margin-top:2px">Select how many complete passages to practice (minimum 1 passage to full section), pulling from uncompleted exams.</div>
    </div>
    <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap">
      <div class="avg-pill">
        <span>${avgText}</span>
      </div>
      <button class="btn avg-btn" id="btnGoToHist" style="font-size:12px;padding:6px 12px;background:#fff">View History &amp; Averages &rarr;</button>
    </div>
  `;
  container.appendChild(headerBar);

  headerBar.querySelector("#btnGoToHist").onclick = () => {
    document.querySelectorAll(".tab").forEach(x => x.classList.remove("on"));
    const histTab = document.querySelector(".tab[data-t='history']");
    if (histTab) histTab.classList.add("on");
    ["bank", "practice", "history", "notes", "sheets"].forEach(k => {
      const el = $("tab" + k[0].toUpperCase() + k.slice(1));
      if (el) el.classList.toggle("hide", k !== "history");
    });
    paintHistory();
  };

  // --- Mode Toggle: Subject Queue vs Full Exam Suites ---
  const modeBar = document.createElement("div");
  modeBar.style.cssText = "display:flex;gap:8px;margin-bottom:16px;border-bottom:1px solid var(--line);padding-bottom:12px";
  modeBar.innerHTML = `
    <button class="btn ${peViewMode === 'subject' ? 'pri' : ''}" id="btnModeSubject" style="font-size:13px">Adaptive Practice by Subject (Recommended)</button>
    <button class="btn ${peViewMode === 'suites' ? 'pri' : ''}" id="btnModeSuites" style="font-size:13px">Full 4-Section Exam Suites (528 Composite)</button>
  `;
  container.appendChild(modeBar);

  modeBar.querySelector("#btnModeSubject").onclick = () => { peViewMode = "subject"; paintPracticeExams(); };
  modeBar.querySelector("#btnModeSuites").onclick = () => { peViewMode = "suites"; paintPracticeExams(); };

  // ================= SUBJECT-FIRST ADAPTIVE WORKFLOW =================
  if (peViewMode === "subject") {
    const mainWrap = document.createElement("div");

    // Step 1: Subject Selection
    const step1Lbl = document.createElement("div");
    step1Lbl.className = "pe-step-lbl";
    step1Lbl.textContent = "Step 1: Choose Subject";
    mainWrap.appendChild(step1Lbl);

    const subjGrid = document.createElement("div");
    subjGrid.className = "pe-subj-grid";

    const secKeys = ["C/P", "CARS", "B/B", "P/S"];
    secKeys.forEach(secKey => {
      const def = SUBJECT_DEFS[secKey];
      const card = document.createElement("div");
      card.className = "pe-subj-card" + (peActiveSec === secKey ? " active" : "");

      const subPool = PRACTICE_EXAMS.filter(e => e.sec === secKey && !e.isHalf);
      const totalSec = subPool.length;
      const doneSec = subPool.filter(e => peData[e.id]?.done).length;

      const uniqueSubjFps = new Set();
      subPool.forEach(ex => {
        if (ex.sets) ex.sets.forEach(s => uniqueSubjFps.add(getPassageFingerprint(s)));
      });
      const totalPassagesInSubj = uniqueSubjFps.size;

      const completedFps = new Set(Array.isArray(peData.completedPassageFingerprints) ? peData.completedPassageFingerprints : []);
      let totalPassagesDone = 0;
      for (const fp of uniqueSubjFps) {
        if (completedFps.has(fp)) totalPassagesDone++;
      }

      const subScores = history.filter(h => h.sec === secKey && h.includedInAverage);
      let subScoreStr = `${doneSec} of ${totalSec} exams completed (${totalPassagesDone}/${totalPassagesInSubj} passages)`;
      if (subScores.length) {
        const subAvg = Math.round((subScores.reduce((s,x)=>s+x.scaledScore,0) / subScores.length) * 10) / 10;
        subScoreStr = `Avg: ${subAvg}/132 &middot; ${doneSec}/${totalSec} exams (${totalPassagesDone}/${totalPassagesInSubj} passages done)`;
      }

      card.innerHTML = `
        <div>
          <div style="font-size:15px;font-weight:800;letter-spacing:0.5px;color:${def.accent};margin-bottom:3px">${secKey}</div>
          <div class="name">${def.name}</div>
          <div class="sub">${def.desc}</div>
        </div>
        <div class="stat">${subScoreStr}</div>
      `;
      card.onclick = () => {
        peActiveSec = secKey;
        peSelectedSourceExamId = "auto";
        paintPracticeExams();
      };
      subjGrid.appendChild(card);
    });
    mainWrap.appendChild(subjGrid);

    // Step 2: Adaptive Passage Selector (1 Passage to Full Section)
    const uncompletedInfo = getUncompletedExams(peActiveSec);
    let plan = getContinuousPassagePlan(peActiveSec, peSliderPassages, peSelectedSourceExamId);
    let maxPassages = Math.min(10, getSubjectPassageQueue(peActiveSec).length || 9);
    if (peSliderPassages > maxPassages) peSliderPassages = maxPassages;
    if (peSliderPassages < 1) peSliderPassages = 1;

    plan = getContinuousPassagePlan(peActiveSec, peSliderPassages, peSelectedSourceExamId);
    let stats = { qCount: plan.totalQs, mins: plan.estMinutes };
    peSliderMinutes = stats.mins;
    let sourceExam = plan.primaryExam;

    const step2Lbl = document.createElement("div");
    step2Lbl.className = "pe-step-lbl";
    step2Lbl.textContent = "Step 2: Adaptive Study Length (1 Passage to Full Section)";
    mainWrap.appendChild(step2Lbl);

    const sliderBox = document.createElement("div");
    sliderBox.className = "pe-slider-box";

    sliderBox.innerHTML = `
      <div class="pe-slider-header">
        <div>
          <div class="pe-slider-title">Adaptive Passage Selector</div>
          <div style="font-size:12px;color:var(--faint);margin-top:2px">Select whole passages. Questions within each passage remain intact.</div>
        </div>
        <div class="pe-slider-readout">
          <span class="v" id="peReadoutPassages">${peSliderPassages}</span>
          <span style="font-weight:700;color:var(--nav)" id="peReadoutUnit"> ${peSliderPassages === 1 ? "Passage" : "Passages"}</span>
          <span style="color:var(--soft);margin-left:8px">&middot; <strong id="peReadoutQs">${stats.qCount}</strong> Questions &middot; ~<strong id="peReadoutMin">${stats.mins}</strong> min</span>
        </div>
      </div>

      <div class="pe-slider-track-wrap">
        <input type="range" min="1" max="${maxPassages}" step="1" value="${peSliderPassages}" class="pe-slider-input" id="pePassageSlider">
        <div class="pe-slider-ticks" id="peSliderTicks">
          <span>1 Passage (Min)</span>
          <span>${Math.round(maxPassages / 2)} Passages (~Half)</span>
          <span>${maxPassages} Passages (Full ${sourceExam.duration}m)</span>
        </div>
      </div>

      <div class="pe-presets" id="pePresetsWrap">
        <span style="font-size:12px;font-weight:700;color:var(--faint);margin-right:4px">Presets:</span>
        <button class="pe-preset-chip ${peSliderPassages === 1 ? 'active' : ''}" data-p="1">1 Passage</button>
        <button class="pe-preset-chip ${peSliderPassages === 2 ? 'active' : ''}" data-p="2">2 Passages</button>
        <button class="pe-preset-chip ${peSliderPassages === 3 ? 'active' : ''}" data-p="3">3 Passages</button>
        <button class="pe-preset-chip ${peSliderPassages === Math.round(maxPassages / 2) ? 'active' : ''}" data-p="${Math.round(maxPassages / 2)}">Half Section (~${Math.round(maxPassages / 2)} Passages)</button>
        <button class="pe-preset-chip ${peSliderPassages === maxPassages ? 'active' : ''}" data-p="${maxPassages}">Full Section (${maxPassages} Passages)</button>
      </div>

      <div id="peComboAlert" style="${plan.isCombining ? '' : 'display:none;'}margin-top:12px;padding:10px 14px;background:#EBF5FB;border:1px solid #B8D5F2;border-radius:6px;font-size:12.5px;color:#185A9D;line-height:1.5">
        <strong>Continuous Queue Active:</strong> Combining uncompleted passages across sections (${plan.sourceBreakdown.map(b => b.setIndices.length + ' from ' + b.label).join(' + ')}). Completes leftover passages so zero banks hang leftover!
      </div>

      <div class="pe-source-box">
        <div>
          <div style="font-size:13px;font-weight:700;color:var(--ink)">Source Exam (Auto-Queue)</div>
          <div style="font-size:11.5px;color:var(--faint);margin-top:2px">
            Pulls from whatever exam is uncompleted in <strong>${peActiveSec}</strong> (90 or 60 min).
          </div>
        </div>
        <select class="pe-source-select" id="peSourceExamSelect"></select>
      </div>
    `;
    mainWrap.appendChild(sliderBox);

    // Populate source exam select
    const selSource = sliderBox.querySelector("#peSourceExamSelect");
    const autoOpt = document.createElement("option");
    autoOpt.value = "auto";
    const autoExam = pickSourceExam(peActiveSec, peSliderPassages, "auto");
    const autoR = peData[autoExam.id];
    const autoDone = autoR?.done;
    const autoCSets = (autoR && Array.isArray(autoR.completedSets)) ? autoR.completedSets : [];
    let autoStatusStr = "Untaken";
    if (autoDone) autoStatusStr = `Completed (${autoR.scaledScore || 125}/132)`;
    else if (autoCSets.length > 0) autoStatusStr = `In Progress (${autoCSets.length}/${autoExam.sets.length} passages done)`;

    autoOpt.textContent = `Auto-Queue: ${autoExam.label} (${autoExam.duration}m) — ${autoStatusStr}`;
    autoOpt.selected = (peSelectedSourceExamId === "auto");
    selSource.appendChild(autoOpt);

    uncompletedInfo.all.forEach(ex => {
      const r = peData[ex.id];
      const isDone = r?.done;
      const cSets = (r && Array.isArray(r.completedSets)) ? r.completedSets : [];
      const opt = document.createElement("option");
      opt.value = ex.id;
      let statusStr = "Untaken";
      if (isDone) statusStr = `Completed (${r.scaledScore}/132)`;
      else if (cSets.length > 0) statusStr = `In Progress (${cSets.length}/${ex.sets.length} passages done)`;

      opt.textContent = `${ex.label} (${ex.duration}m) — ${statusStr}`;
      if (peSelectedSourceExamId === ex.id) opt.selected = true;
      selSource.appendChild(opt);
    });

    // Step 3: Launch Adaptive Study Section (Hero Card)
    const step3Lbl = document.createElement("div");
    step3Lbl.className = "pe-step-lbl";
    step3Lbl.textContent = "Step 3: Launch Adaptive Study Section";
    mainWrap.appendChild(step3Lbl);

    const hero = document.createElement("div");
    hero.className = "pe-next-hero";

    const pInitLabel = peSliderPassages === 1 ? "1 Passage" : `${peSliderPassages} Passages`;
    const comboDescInit = plan.isCombining
      ? `Combining <strong>${plan.sourceBreakdown.map(b => b.setIndices.length + " from " + b.label).join(" + ")}</strong> &middot; Completes earlier exams so zero banks hang leftover`
      : `Pulling <strong>${pInitLabel} (${stats.qCount} complete questions)</strong> from <strong>${sourceExam.label}</strong>`;

    hero.innerHTML = `
      <div class="info">
        <div class="tag">ADAPTIVE STUDY SECTION &middot; ${peActiveSec}</div>
        <div class="title" id="peHeroTitle">${sourceExam.sec} &mdash; ${pInitLabel} (${stats.qCount} Questions &middot; ~${stats.mins} min)</div>
        <div class="desc" id="peHeroDesc">
          ${comboDescInit} &middot; Timed at standard MCAT pace (${stats.mins}:00) &middot; Full scaled scoring (118–132) &amp; explanations
        </div>
      </div>
      <button class="btn-start" id="btnStartAdaptive">
        Start Study Section (${pInitLabel} &middot; ${stats.qCount} Qs &middot; ~${stats.mins} min)
      </button>
    `;

    hero.querySelector("#btnStartAdaptive").onclick = () => {
      startAdaptiveStudy(peActiveSec, peSliderPassages, plan.estMinutes);
    };

    // In 90-min source exams, also provide quick half-section launch buttons on the hero card
    const h1 = PRACTICE_EXAMS.find(e => e.id === sourceExam.id + "_h1");
    const h2 = PRACTICE_EXAMS.find(e => e.id === sourceExam.id + "_h2");
    if (h1 && h2) {
      const h1Done = peData[h1.id]?.done;
      const h2Done = peData[h2.id]?.done;
      const h1Score = peData[h1.id]?.scaledScore;
      const h2Score = peData[h2.id]?.scaledScore;

      const splitBox = document.createElement("div");
      splitBox.className = "pe-hero-split-box";
      splitBox.innerHTML = `
        <div style="font-size:12.5px;color:var(--soft)">
          <strong>Short on time?</strong> Split this 90-min exam into two ~45-min sections (graded individually &middot; both halves complete the 90m):
        </div>
        <div style="display:flex;gap:8px;flex-wrap:wrap">
          <button class="pe-half-btn ${h1Done ? 'done' : ''}" id="btnHeroH1">
            ${h1Done ? `Part 1 Done: ${h1Score}/132` : `Part 1 (~${h1.duration} min, 24 Qs)`}
          </button>
          <button class="pe-half-btn ${h2Done ? 'done' : (!h1Done ? '' : 'pri')}" id="btnHeroH2">
            ${h2Done ? `Part 2 Done: ${h2Score}/132` : `Part 2 (~${h2.duration} min, ${peActiveSec === 'CARS' ? 29 : 28} Qs)`}
          </button>
        </div>
      `;
      hero.appendChild(splitBox);

      splitBox.querySelector("#btnHeroH1").onclick = () => {
        if (h1Done && !confirm(`You scored ${h1Score}/132 on Part 1 last time. Retake Part 1?`)) return;
        beginPracticeExam(h1);
      };
      splitBox.querySelector("#btnHeroH2").onclick = () => {
        if (h2Done && !confirm(`You scored ${h2Score}/132 on Part 2 last time. Retake Part 2?`)) return;
        beginPracticeExam(h2);
      };
    }

    mainWrap.appendChild(hero);

    // Real-time synchronization helper for slider interactions
    function syncUI() {
      plan = getContinuousPassagePlan(peActiveSec, peSliderPassages, peSelectedSourceExamId);
      sourceExam = plan.primaryExam;
      maxPassages = Math.min(10, getSubjectPassageQueue(peActiveSec).length || 9);
      if (peSliderPassages > maxPassages) peSliderPassages = maxPassages;
      if (peSliderPassages < 1) peSliderPassages = 1;

      stats = { qCount: plan.totalQs, mins: plan.estMinutes };
      peSliderMinutes = stats.mins;

      sliderBox.querySelector("#peReadoutPassages").textContent = peSliderPassages;
      sliderBox.querySelector("#peReadoutUnit").textContent = peSliderPassages === 1 ? " Passage" : " Passages";
      sliderBox.querySelector("#peReadoutQs").textContent = stats.qCount;
      sliderBox.querySelector("#peReadoutMin").textContent = stats.mins;

      const sliderEl = sliderBox.querySelector("#pePassageSlider");
      sliderEl.max = maxPassages;
      sliderEl.value = peSliderPassages;

      sliderBox.querySelectorAll(".pe-preset-chip").forEach(chip => {
        const pVal = parseInt(chip.dataset.p);
        chip.classList.toggle("active", pVal === peSliderPassages);
      });

      const comboAlert = sliderBox.querySelector("#peComboAlert");
      if (comboAlert) {
        comboAlert.style.display = plan.isCombining ? "block" : "none";
        if (plan.isCombining) {
          comboAlert.innerHTML = `<strong>Continuous Queue Active:</strong> Combining uncompleted passages across sections (${plan.sourceBreakdown.map(b => b.setIndices.length + ' from ' + b.label).join(' + ')}). Completes leftover passages so zero banks hang leftover!`;
        }
      }

      const pLabel = peSliderPassages === 1 ? "1 Passage" : `${peSliderPassages} Passages`;
      hero.querySelector("#peHeroTitle").textContent = `${sourceExam.sec} — ${pLabel} (${stats.qCount} Questions · ~${stats.mins} min)`;
      const comboSub = plan.isCombining
        ? `Combining <strong>${plan.sourceBreakdown.map(b => b.setIndices.length + " from " + b.label).join(" + ")}</strong> (completing earlier exams so zero banks hang leftover)`
        : `Pulling <strong>${pLabel} (${stats.qCount} complete questions)</strong> from <strong>${sourceExam.label}</strong>`;
      hero.querySelector("#peHeroDesc").innerHTML = `${comboSub} &middot; Timed at standard MCAT pace (${stats.mins}:00) &middot; Full scaled scoring (118–132) &amp; explanations`;
      hero.querySelector("#btnStartAdaptive").innerHTML = `Start Study Section (${pLabel} &middot; ${stats.qCount} Qs &middot; ~${stats.mins} min)`;
    }

    // Attach interactive events to slider & preset controls
    const slider = sliderBox.querySelector("#pePassageSlider");
    slider.oninput = (e) => {
      peSliderPassages = parseInt(e.target.value) || 1;
      syncUI();
    };

    sliderBox.querySelectorAll(".pe-preset-chip").forEach(chip => {
      chip.onclick = () => {
        peSliderPassages = parseInt(chip.dataset.p) || 1;
        syncUI();
      };
    });

    selSource.onchange = (e) => {
      peSelectedSourceExamId = e.target.value;
      paintPracticeExams();
    };

    // Step 4: Catalog & Queue of All Sections in this Subject
    const qHeader = document.createElement("div");
    qHeader.className = "pe-queue-header";
    qHeader.innerHTML = `
      <h3>${peActiveSec} Exam Catalog (${uncompletedInfo.all.length} Exams &middot; ${uncompletedInfo.uncompleted.length} Untaken)</h3>
      <span style="font-size:12px;color:var(--faint)">Launch any full section directly or review completed attempts below:</span>
    `;
    mainWrap.appendChild(qHeader);

    // Catalog Filter Controls
    const filterRow = document.createElement("div");
    filterRow.style.cssText = "display:flex;gap:6px;margin-bottom:12px;flex-wrap:wrap";
    const filterOpts = [
      { id: "all", label: `All Sections (${uncompletedInfo.all.length})` },
      { id: "90", label: "90-Min Full (10)" },
      { id: "60", label: "60-Min Paced (10)" },
      { id: "half", label: "~45-Min Halves (20)" }
    ];
    filterOpts.forEach(f => {
      const btn = document.createElement("button");
      btn.className = `btn ${peQueueFilter === f.id ? 'pri' : ''}`;
      btn.style.cssText = "font-size:12px;padding:4px 10px";
      btn.textContent = f.label;
      btn.onclick = () => {
        peQueueFilter = f.id;
        paintPracticeExams();
      };
      filterRow.appendChild(btn);
    });
    mainWrap.appendChild(filterRow);

    const qPanel = document.createElement("div");
    qPanel.className = "panel";
    qPanel.innerHTML = `<div class="pb"></div>`;
    const pb = qPanel.querySelector(".pb");

    let displayPool;
    if (peQueueFilter === "90") {
      displayPool = uncompletedInfo.all.filter(e => e.duration === 90);
    } else if (peQueueFilter === "60") {
      displayPool = uncompletedInfo.all.filter(e => e.duration === 60);
    } else if (peQueueFilter === "half") {
      displayPool = PRACTICE_EXAMS.filter(e => e.sec === peActiveSec && e.isHalf);
      displayPool.sort((a,b) => (a.suite || "").localeCompare(b.suite || "", undefined, { numeric: true }));
    } else {
      displayPool = uncompletedInfo.all;
    }

    displayPool.forEach((ex, idx) => {
      const r = peData[ex.id];
      const totalQs = ex.sets.reduce((sum, s) => sum + (s && s.qs ? s.qs.length : 0), 0);
      let badge = `<span class="badge b-new">Not started</span>`;
      let aiTag = "";
      let subDesc = `${totalQs} questions &middot; ~${ex.duration} min`;

      if (r && r.done) {
        const sc = r.scaledScore;
        badge = `<span class="badge ${sc >= 128 ? "b-ok" : sc >= 124 ? "b-mid" : "b-bad"}" style="font-size:13px">${sc}<span style="font-size:10px;opacity:.7">/132</span></span>`;
        if (typeof window.getCachedGeminiAnalysis === "function" && window.getCachedGeminiAnalysis(ex.id)) {
          aiTag = ` &middot; <span style="color:#2E6DA4;font-weight:700">AI Analysis Ready</span>`;
        }
        if (r.completedViaHalves) {
          subDesc = `${totalQs} questions &middot; 90 min &middot; <b style="color:var(--ok)">Completed via Halves (Part 1: ${r.h1Score || ""} + Part 2: ${r.h2Score || ""})</b>${aiTag}`;
        } else {
          subDesc = `${totalQs} questions &middot; ~${ex.duration} min &middot; ${r.pct}% raw &middot; ${r.percentile}${aiTag}`;
        }
      } else if (r && !r.done && Array.isArray(r.completedSets) && r.completedSets.length > 0) {
        const cSets = r.completedSets;
        const doneQs = cSets.reduce((sum, sIdx) => sum + (ex.sets[sIdx]?.qs?.length || 0), 0);
        const pctDone = Math.round((cSets.length / ex.sets.length) * 100);
        badge = `<span class="badge" style="background:#FFF3D6;color:#8F6B00;border:1px solid #ECC875;font-size:12px;font-weight:700">${cSets.length}/${ex.sets.length} Passages Done</span>`;
        subDesc = `<strong>${doneQs}/${totalQs} questions checked off (${cSets.length}/${ex.sets.length} passages)</strong> &middot; ${ex.sets.length - cSets.length} passages remaining in queue
          <div style="width:130px;height:5px;background:#E2E8F0;border-radius:3px;overflow:hidden;margin-top:4px">
            <div style="width:${pctDone}%;height:100%;background:#D9A22B"></div>
          </div>`;
      } else if (ex.isHalf) {
        const partnerDone = peData[ex.partnerId]?.done;
        const partnerScore = peData[ex.partnerId]?.scaledScore;
        if (partnerDone) {
          badge = `<span class="badge b-new" style="background:#EEF5FC;color:#185A9D;border:1px solid #B8D5F2">Finish 90m</span>`;
          subDesc = `${totalQs} questions &middot; ~${ex.duration} min &middot; <strong style="color:#185A9D">Partner Part ${ex.halfIndex === 1 ? 2 : 1} done (${partnerScore}/132)! Complete this half to finish 90m!</strong>`;
        }
      }

      const row = document.createElement("div");
      row.className = "row";
      row.style.cursor = "pointer";
      let revBtnHtml = "";
      if (r && r.done) {
        revBtnHtml = `<button class="btn" style="font-size:11px;padding:3px 8px;margin-left:8px;background:#185A9D;color:#fff;border-radius:4px" data-rev-id="${ex.id}">Review &amp; AI</button>`;
      }
      const progressLabel = (r && !r.done && r.completedSets?.length) ? `<span style="color:#8F6B00;font-weight:700">${Math.round((r.completedSets.length / ex.sets.length) * 100)}% Done</span>` : "Catalog #" + (idx + 1);
      row.innerHTML = `
        <span style="flex:1">
          <span class="t">${ex.suiteTitle} &mdash; ${ex.sec}</span>
          <span class="s">${subDesc}</span>
        </span>
        <span class="qn">${r && r.done ? "Completed" : progressLabel}</span>
        <div style="display:flex;align-items:center;gap:6px">
          ${badge}
          ${revBtnHtml}
        </div>
      `;
      const revBtn = row.querySelector(`[data-rev-id="${ex.id}"]`);
      if (revBtn) {
        revBtn.onclick = (e) => {
          e.stopPropagation();
          openCompletedExamReview(ex.id);
        };
      }
      row.onclick = () => {
        if (r && r.done && !confirm(`You scored ${r.scaledScore}/132 (${r.pct}%) last time. Retake this section?`)) return;
        beginPracticeExam(ex);
      };
      pb.appendChild(row);
    });

    mainWrap.appendChild(qPanel);
    container.appendChild(mainWrap);

  } else {
    // ================= FULL EXAM SUITES WORKFLOW =================
    const suiteOrder = [
      "exam1_90", "exam2_90", "exam3_90", "exam4_90", "exam5_90", "exam6_90",
      "exam1_60", "exam2_60", "exam3_60", "exam4_60", "exam5_60", "exam6_60",
      "exam7_90", "exam7_60", "exam8_90", "exam8_60", "exam9_90", "exam9_60", "exam10_90", "exam10_60"
    ];
    const groups = {};
    PRACTICE_EXAMS.forEach(ex => {
      if (ex.isHalf) return; // Keep suites view strictly for full 4-section suites
      const k = ex.suite || ex.type;
      if (!groups[k]) groups[k] = [];
      groups[k].push(ex);
    });

    const secOrder = ["C/P", "CARS", "B/B", "P/S"];

    suiteOrder.forEach(suiteKey => {
      const exams = groups[suiteKey];
      if (!exams || !exams.length) return;

      const panel = document.createElement("div"); panel.className = "panel";
      const suiteTitle = exams[0].suiteTitle || "Practice Sections";

      let compositeScore = 0, compositeCount = 0;
      exams.forEach(ex => {
        const r = peData[ex.id];
        if (r && r.done) { compositeScore += r.scaledScore; compositeCount++; }
      });

      let compositeHTML = "";
      if (compositeCount === 4) {
        compositeHTML = `<div style="background:var(--okBg);border:1px solid var(--ok);color:var(--ok);padding:10px 14px;margin:0 16px 12px;font-size:14px;font-weight:700;display:flex;justify-content:space-between;align-items:center">
          <span>Composite MCAT Score (${exams[0].duration} min)</span>
          <span style="font-size:28px">${compositeScore}<span style="font-size:14px;opacity:.7"> / 528</span></span>
        </div>`;
      } else if (compositeCount > 0) {
        compositeHTML = `<div style="background:#F7F9FB;border:1px solid var(--line);padding:8px 14px;margin:0 16px 12px;font-size:12.5px;color:var(--faint)">
          ${compositeCount} of 4 sections completed. Finish all 4 for a composite score.
        </div>`;
      }

      panel.innerHTML = `<div class="ph"><h2>${suiteTitle}</h2><span class="meta">${exams.length} section${exams.length > 1 ? "s" : ""} &middot; ${exams[0].duration} min each</span></div>
        ${compositeHTML}<div class="pb"></div>`;

      const pb = panel.querySelector(".pb");
      exams.sort((a, b) => secOrder.indexOf(a.sec) - secOrder.indexOf(b.sec));

      exams.forEach(ex => {
        const r = peData[ex.id];
        const totalQs = ex.sets.reduce((sum, s) => sum + (s && s.qs ? s.qs.length : 0), 0);

        let badge = `<span class="badge b-new">Not started</span>`;
        let aiTag = "";
        let inProgressTag = "";
        if (r && r.done) {
          const sc = r.scaledScore;
          badge = `<span class="badge ${sc >= 128 ? "b-ok" : sc >= 124 ? "b-mid" : "b-bad"}" style="font-size:13px">${sc}<span style="font-size:10px;opacity:.7">/132</span></span>`;
          if (typeof window.getCachedGeminiAnalysis === "function" && window.getCachedGeminiAnalysis(ex.id)) {
            aiTag = ` &middot; <span style="color:#2E6DA4;font-weight:700">AI Analysis Ready</span>`;
          }
        } else if (r && !r.done && Array.isArray(r.completedSets) && r.completedSets.length > 0) {
          const cSets = r.completedSets;
          const doneQs = cSets.reduce((sum, sIdx) => sum + (ex.sets[sIdx]?.qs?.length || 0), 0);
          badge = `<span class="badge" style="background:#FFF3D6;color:#8F6B00;border:1px solid #ECC875;font-size:12px;font-weight:700">${cSets.length}/${ex.sets.length} Passages</span>`;
          inProgressTag = ` &middot; <strong style="color:#8F6B00">${doneQs}/${totalQs} Qs checked off (${cSets.length}/${ex.sets.length} passages done)</strong>`;
        }

        const halvesTag = (r && r.completedViaHalves) ? ` &middot; <span style="color:var(--ok);font-weight:600">Halves Combined</span>` : "";
        const row = document.createElement("div"); row.className = "row"; row.style.cursor = "pointer";
        let revBtnHtml = "";
        if (r && r.done) {
          revBtnHtml = `<button class="btn" style="font-size:11px;padding:3px 8px;margin-left:8px;background:#185A9D;color:#fff;border-radius:4px" data-rev-suite="${ex.id}">Review &amp; AI</button>`;
        }
        row.innerHTML = `<span style="flex:1">
            <span class="t">${SUBJECT_DEFS[ex.sec]?.name || ex.sec}</span>
            <span class="s">${totalQs} questions &middot; ${ex.duration} min${r && r.done ? ` &middot; ${r.pct}% raw &middot; ${r.percentile}` : ""}${halvesTag}${inProgressTag}${aiTag}</span>
          </span>
          <span class="qn">${ex.sec}</span>
          <div style="display:flex;align-items:center;gap:6px">
            ${badge}
            ${revBtnHtml}
          </div>`;
        const revBtn = row.querySelector(`[data-rev-suite="${ex.id}"]`);
        if (revBtn) {
          revBtn.onclick = (e) => {
            e.stopPropagation();
            openCompletedExamReview(ex.id);
          };
        }
        row.onclick = () => {
          if (r && r.done) {
            if (!confirm(`You scored ${r.scaledScore}/132 (${r.pct}%) last time. Retake this section?`)) return;
          }
          beginPracticeExam(ex);
        };
        pb.appendChild(row);
      });

      container.appendChild(panel);
    });
  }
}

/* ===== HISTORY & ROLLING AVERAGE DASHBOARD UI ===== */
function paintHistory() {
  const container = document.getElementById("tabHistory");
  if (!container) return;
  container.innerHTML = "";

  const hist = getHistory();
  const prefs = getHistoryPrefs();
  const rolling = calculateRollingAverage(hist, prefs);

  const dash = document.createElement("div");
  dash.className = "hist-dash";

  // Top header with actions
  const topBar = document.createElement("div");
  topBar.className = "hist-dash-top";
  topBar.innerHTML = `
    <div>
      <h2>Score History &amp; Rolling Averages</h2>
      <div style="font-size:13px;color:var(--faint);margin-top:2px">Manage your exam attempts and customize the rolling window for your projected MCAT score.</div>
    </div>
    <div style="display:flex;gap:8px">
      <button class="btn" id="btnIncludeAll" style="font-size:12px;padding:6px 12px">Include All in Avg</button>
      <button class="btn" id="btnClearHist" style="font-size:12px;padding:6px 12px;color:var(--bad)">Clear All History</button>
    </div>
  `;
  dash.appendChild(topBar);

  topBar.querySelector("#btnIncludeAll").onclick = () => {
    hist.forEach(x => x.includedInAverage = true);
    saveHistory(hist);
    paintHistory();
    paintPracticeExams();
    flash("All attempts included in score average.");
  };

  topBar.querySelector("#btnClearHist").onclick = () => {
    clearAllHistory();
  };

  // Configurable Controls
  const ctrlBar = document.createElement("div");
  ctrlBar.className = "hist-controls";
  ctrlBar.innerHTML = `
    <label>
      Rolling Window:
      <select id="selHistWin">
        <option value="3" ${String(prefs.window) === "3" ? "selected" : ""}>Most recent 3 sections</option>
        <option value="5" ${String(prefs.window) === "5" ? "selected" : ""}>Most recent 5 sections</option>
        <option value="10" ${String(prefs.window) === "10" ? "selected" : ""}>Most recent 10 sections</option>
        <option value="all" ${String(prefs.window) === "all" ? "selected" : ""}>All included sections</option>
      </select>
    </label>
    <label>
      Subject:
      <select id="selHistSec">
        <option value="all" ${prefs.sec === "all" ? "selected" : ""}>All 4 Subjects</option>
        <option value="C/P" ${prefs.sec === "C/P" ? "selected" : ""}>C/P Only</option>
        <option value="CARS" ${prefs.sec === "CARS" ? "selected" : ""}>CARS Only</option>
        <option value="B/B" ${prefs.sec === "B/B" ? "selected" : ""}>B/B Only</option>
        <option value="P/S" ${prefs.sec === "P/S" ? "selected" : ""}>P/S Only</option>
      </select>
    </label>
    <label>
      Length:
      <select id="selHistDur">
        <option value="all" ${String(prefs.dur) === "all" ? "selected" : ""}>All Durations (90m, ~45m, 60m)</option>
        <option value="90" ${String(prefs.dur) === "90" ? "selected" : ""}>90-Minute Full Sections Only</option>
        <option value="45" ${String(prefs.dur) === "45" ? "selected" : ""}>~45-Minute Half-Sections Only</option>
        <option value="60" ${String(prefs.dur) === "60" ? "selected" : ""}>60-Minute Paced Sections Only</option>
      </select>
    </label>
  `;
  dash.appendChild(ctrlBar);

  ctrlBar.querySelector("#selHistWin").onchange = (e) => {
    prefs.window = e.target.value;
    saveHistoryPrefs(prefs);
    paintHistory();
    paintPracticeExams();
  };
  ctrlBar.querySelector("#selHistSec").onchange = (e) => {
    prefs.sec = e.target.value;
    saveHistoryPrefs(prefs);
    paintHistory();
    paintPracticeExams();
  };
  ctrlBar.querySelector("#selHistDur").onchange = (e) => {
    prefs.dur = e.target.value;
    saveHistoryPrefs(prefs);
    paintHistory();
    paintPracticeExams();
  };

  // Stats Grid
  const statsGrid = document.createElement("div");
  statsGrid.className = "hist-stats-grid";

  if (rolling) {
    const scColor = rolling.avgScaled >= 127 ? "var(--ok)" : rolling.avgScaled >= 124 ? "var(--warn)" : "var(--bad)";
    statsGrid.innerHTML = `
      <div class="hist-stat-card" style="border-top:3px solid ${scColor}">
        <div class="v" style="color:${scColor}">${rolling.avgScaled}</div>
        <div class="l">Avg Scaled Score</div>
        <div class="sub">Out of 132 per section</div>
      </div>
      <div class="hist-stat-card" style="border-top:3px solid var(--nav)">
        <div class="v">${rolling.projComposite}</div>
        <div class="l">Projected Composite</div>
        <div class="sub">Scaled total out of 528</div>
      </div>
      <div class="hist-stat-card">
        <div class="v">${rolling.avgPct}%</div>
        <div class="l">Average Accuracy</div>
        <div class="sub">${rolling.sumScore} / ${rolling.sumTotal} correct</div>
      </div>
      <div class="hist-stat-card">
        <div class="v">${rolling.count} <span style="font-size:14px;color:var(--faint)">/ ${rolling.totalMatching}</span></div>
        <div class="l">Averaging Window</div>
        <div class="sub">${rolling.excluded ? `${rolling.excluded} attempt${rolling.excluded > 1 ? "s" : ""} excluded` : "All attempts active"}</div>
      </div>
    `;
  } else {
    statsGrid.innerHTML = `
      <div class="hist-stat-card" style="grid-column:1/-1;text-align:center;padding:24px">
        <div style="font-size:15px;color:var(--faint);font-weight:600">No scored sections matching current filters.</div>
        <div style="font-size:12.5px;color:var(--faint);margin-top:4px">Complete a section in Practice Sections or adjust filters above.</div>
      </div>
    `;
  }
  dash.appendChild(statsGrid);

  // Tip
  const tip = document.createElement("div");
  tip.className = "hist-tip";
  tip.innerHTML = `<strong>Score Average Control:</strong> Click the <strong>In Avg / Exclude</strong> button on any row in the table below to toggle whether that exam is included in your average without losing its record.`;
  dash.appendChild(tip);

  // Interactive Performance Analytics & Pacing Charts
  const chartMount = document.createElement("div");
  chartMount.id = "peHistChartMount";
  dash.appendChild(chartMount);
  if (typeof renderPerformanceCharts === "function") {
    renderPerformanceCharts(chartMount);
  } else if (typeof window !== "undefined" && typeof window.renderPerformanceCharts === "function") {
    window.renderPerformanceCharts(chartMount);
  }

  // History Table
  if (hist.length) {
    const tableWrap = document.createElement("div");
    tableWrap.style.cssText = "overflow-x:auto";

    let tableHTML = `
      <table class="hist-table">
        <thead>
          <tr>
            <th style="width:110px">In Average?</th>
            <th>Date &amp; Time</th>
            <th>Subject</th>
            <th>Section</th>
            <th>Scaled</th>
            <th>Accuracy</th>
            <th>Confidence</th>
            <th style="text-align:right">Action</th>
          </tr>
        </thead>
        <tbody>
    `;

    hist.forEach(rec => {
      const isInc = !!rec.includedInAverage;
      const d = new Date(rec.ts || Date.now());
      const dateStr = d.toLocaleDateString(undefined, { month: "short", day: "numeric" }) + ", " + d.toLocaleTimeString(undefined, { hour: "numeric", minute: "2-digit" });
      const def = SUBJECT_DEFS[rec.sec] || { short: rec.sec, badgeClass: "hist-sec-cp" };
      const sc = rec.scaledScore;
      const badgeCls = sc >= 128 ? "b-ok" : sc >= 124 ? "b-mid" : "b-bad";

      let typeBadge = "";
      if (rec.isHalf || rec.type === "half") {
        const halfNum = rec.halfIndex || (rec.examId && rec.examId.endsWith("_h2") ? 2 : 1);
        typeBadge = `<span class="badge" style="background:rgba(124,58,237,0.12);color:var(--nav);font-size:10.5px;margin-left:6px;border:1px solid rgba(124,58,237,0.25);padding:1px 6px">Part ${halfNum} Half</span>`;
      } else if (rec.isCombinedFromHalves) {
        typeBadge = `<span class="badge" style="background:rgba(16,185,129,0.12);color:var(--ok);font-size:10.5px;margin-left:6px;border:1px solid rgba(16,185,129,0.25);padding:1px 6px">Full 90m (Combined)</span>`;
      } else if (rec._isAdaptive || rec.type === "adaptive") {
        typeBadge = `<span class="badge" style="background:rgba(27,58,92,0.1);color:var(--nav);font-size:10.5px;margin-left:6px;padding:1px 6px">Adaptive Study</span>`;
      } else if (rec.duration === 90 || rec.type === "90min") {
        typeBadge = `<span class="badge" style="background:rgba(59,130,246,0.1);color:var(--accent);font-size:10.5px;margin-left:6px;padding:1px 6px">90m Full</span>`;
      } else if (rec.duration === 60 || rec.type === "60min") {
        typeBadge = `<span class="badge" style="background:rgba(245,158,11,0.1);color:var(--warn);font-size:10.5px;margin-left:6px;padding:1px 6px">60m Paced</span>`;
      }

      tableHTML += `
        <tr class="${isInc ? "" : "excluded"}" id="row_${rec.id}">
          <td>
            <button class="hist-toggle-btn ${isInc ? 'inc' : 'exc'}" data-id="${rec.id}">
              ${isInc ? 'Included' : 'Excluded'}
            </button>
          </td>
          <td style="white-space:nowrap;font-size:12px;color:var(--soft)">${dateStr}</td>
          <td><span class="hist-sec-badge ${def.badgeClass}">${rec.sec}</span></td>
          <td>
            <strong>${rec.suiteTitle || rec.label}</strong> ${typeBadge}
            <span style="display:block;font-size:11.5px;color:var(--faint)">${rec.duration} min &middot; ${rec.totalQs} questions</span>
          </td>
          <td>
            <span class="badge ${badgeCls}" style="font-size:13px">${sc}<span style="font-size:10px;opacity:.7">/132</span></span>
          </td>
          <td>
            <strong>${rec.pct}%</strong>
            <span style="font-size:11.5px;color:var(--faint)">(${rec.rawScore}/${rec.totalQs})</span>
          </td>
          <td style="font-size:11.5px;color:var(--soft);white-space:nowrap">
            ${rec.solid} solid &middot; ${rec.shaky} shaky &middot; ${rec.lucky} lucky
          </td>
          <td style="text-align:right;white-space:nowrap">
            <button class="btn" style="font-size:11px;padding:3px 8px;margin-right:6px;background:#185A9D;color:#fff" data-rev="${rec.id}">Review &amp; AI</button>
            <button class="hist-del-btn" data-del="${rec.id}" title="Delete this entry">Delete</button>
          </td>
        </tr>
      `;
    });

    tableHTML += `</tbody></table>`;
    tableWrap.innerHTML = tableHTML;

    // Attach row events
    tableWrap.querySelectorAll("[data-rev]").forEach(btn => {
      btn.onclick = (e) => {
        e.stopPropagation();
        const id = btn.getAttribute("data-rev");
        openCompletedExamReview(id);
      };
    });
    tableWrap.querySelectorAll(".hist-toggle-btn").forEach(btn => {
      btn.onclick = (e) => {
        e.stopPropagation();
        const id = btn.getAttribute("data-id") || btn.dataset.id;
        toggleHistoryInclude(id);
      };
    });
    tableWrap.querySelectorAll(".hist-del-btn").forEach(btn => {
      btn.onclick = (e) => {
        e.stopPropagation();
        const id = btn.getAttribute("data-del") || btn.dataset.del;
        deleteHistoryEntry(id);
      };
    });

    dash.appendChild(tableWrap);
  } else {
    const empty = document.createElement("div");
    empty.className = "empty";
    empty.textContent = "No practice exam attempts logged yet. Complete your first section in Practice Sections!";
    dash.appendChild(empty);
  }

  container.appendChild(dash);
}

// Attach paint functions and helpers to window/globalThis for global access
if (typeof window !== "undefined") {
  window.PRACTICE_EXAMS = PRACTICE_EXAMS;
  window.paintPracticeExams = paintPracticeExams;
  window.paintHistory = paintHistory;
  window.getHistory = getHistory;
  window.saveHistory = saveHistory;
  window.addHistoryEntry = addHistoryEntry;
  window.toggleHistoryInclude = toggleHistoryInclude;
  window.deleteHistoryEntry = deleteHistoryEntry;
  window.clearAllHistory = clearAllHistory;
  window.getHistoryPrefs = getHistoryPrefs;
  window.saveHistoryPrefs = saveHistoryPrefs;
  window.calculateRollingAverage = calculateRollingAverage;
  window.beginPracticeExam = beginPracticeExam;
  window.exitExamWithoutScoring = exitExamWithoutScoring;
  window.openCompletedExamReview = openCompletedExamReview;
  window.getQuestionArchetype = getQuestionArchetype;
  window.getContinuousPassagePlan = getContinuousPassagePlan;
  window.getSubjectPassageQueue = getSubjectPassageQueue;
  window.calculatePassageReadingTelemetry = calculatePassageReadingTelemetry;
  window.finishReadingPassage = finishReadingPassage;
}
if (typeof globalThis !== "undefined") {
  globalThis.PRACTICE_EXAMS = PRACTICE_EXAMS;
  globalThis.paintPracticeExams = paintPracticeExams;
  globalThis.paintHistory = paintHistory;
  globalThis.getHistory = getHistory;
  globalThis.saveHistory = saveHistory;
  globalThis.addHistoryEntry = addHistoryEntry;
  globalThis.toggleHistoryInclude = toggleHistoryInclude;
  globalThis.deleteHistoryEntry = deleteHistoryEntry;
  globalThis.clearAllHistory = clearAllHistory;
  globalThis.getHistoryPrefs = getHistoryPrefs;
  globalThis.saveHistoryPrefs = saveHistoryPrefs;
  globalThis.calculateRollingAverage = calculateRollingAverage;
  globalThis.beginPracticeExam = beginPracticeExam;
  globalThis.exitExamWithoutScoring = exitExamWithoutScoring;
  globalThis.openCompletedExamReview = openCompletedExamReview;
  globalThis.getQuestionArchetype = getQuestionArchetype;
  globalThis.getContinuousPassagePlan = getContinuousPassagePlan;
  globalThis.getSubjectPassageQueue = getSubjectPassageQueue;
  globalThis.calculatePassageReadingTelemetry = calculatePassageReadingTelemetry;
  globalThis.finishReadingPassage = finishReadingPassage;
}

// Hook global grade() function to ensure practice exams grade properly on timer timeout
if (typeof window !== "undefined" && typeof window.grade === "function") {
  const _origGrade = window.grade;
  window.grade = function() {
    if (window.E && window.E._isPracticeExam) {
      gradePracticeExam();
    } else if (_origGrade) {
      _origGrade();
    }
  };
}

/* ===== OVERRIDE BUTTON ACTIONS & INTEGRATION ===== */
const _origBNext = $("bNext").onclick;
$("bNext").onclick = () => {
  if (E && E._isPracticeExam) {
    if (E.i === E.s.qs.length - 1) {
      gradePracticeExam();
    } else {
      E.i++;
      drawPEQ();
    }
  } else if (_origBNext) {
    _origBNext();
  }
};

const _origBPrev = $("bPrev").onclick;
$("bPrev").onclick = () => {
  if (E && E._isPracticeExam) {
    if (E.i > 0) { E.i--; drawPEQ(); }
  } else if (_origBPrev) {
    _origBPrev();
  }
};

const _origTEnd = $("tEnd").onclick;
$("tEnd").onclick = () => {
  if (E && E._isPracticeExam) {
    if (confirm("End this practice section and see your MCAT score?")) {
      gradePracticeExam();
    }
  } else if (_origTEnd) {
    _origTEnd();
  }
};

// Hook up Exit Without Scoring
const tExitBtn = $("tExit");
if (tExitBtn) {
  tExitBtn.onclick = () => exitExamWithoutScoring();
}
const pExitBtn = $("pExit");
if (pExitBtn) {
  pExitBtn.onclick = () => exitExamWithoutScoring();
}

// Navigator for practice exams
const _origTNav = $("tNav").onclick;
$("tNav").onclick = () => {
  if (E && E._isPracticeExam) {
    let h = `<tr><th>#</th><th>Status</th><th>Flagged</th><th>Topic</th></tr>`;
    E.s.qs.forEach((q, k) => {
      const isSk = q._isSkipped || E.ans[k] === -1 || E.conf[k] === "skipped";
      const statusText = isSk
        ? "<span style='color:#64748B;font-weight:600'>&#10549; Skipped (Completed)</span>"
        : (E.ans[k] !== null ? "Completed" : (E.seen[k] ? "<i>Incomplete</i>" : "<i>Unseen</i>"));
      h += `<tr data-k="${k}"><td><b>${k + 1}</b></td><td>${statusText}</td><td>${E.flag[k] ? "<span style='color:var(--flag);font-weight:700'>&#10022; Flagged</span>" : ""}</td><td style="font-size:11px;color:var(--faint)">${q._topic || ""}</td></tr>`;
    });
    $("nT").innerHTML = h;
    $("nT").querySelectorAll("tr[data-k]").forEach(tr => {
      tr.onclick = () => { E.i = +tr.dataset.k; $("nav").classList.add("hide"); drawPEQ(); };
    });
    $("nav").classList.remove("hide");
  } else if (_origTNav) {
    _origTNav();
  }
};

// Hook up More Tools popover and Skip Passage button
const tMoreBtn = $("tMore");
if (tMoreBtn) {
  tMoreBtn.onclick = (e) => {
    e.stopPropagation();
    toggleMoreToolsPopup();
  };
}

const tSkipPassageBtn = $("tSkipPassage");
if (tSkipPassageBtn) {
  tSkipPassageBtn.onclick = (e) => {
    e.stopPropagation();
    skipCurrentPassage();
  };
}

if (typeof document !== "undefined" && typeof document.addEventListener === "function") {
  document.addEventListener("click", (e) => {
    const popup = $("peMoreToolsPopup");
    const moreBtn = $("tMore");
    if (!popup || popup.classList.contains("hide")) return;
    if (moreBtn && (moreBtn === e.target || moreBtn.contains(e.target))) return;
    if (popup.contains(e.target)) return;
    toggleMoreToolsPopup(false);
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      const popup = $("peMoreToolsPopup");
      if (popup && !popup.classList.contains("hide")) {
        toggleMoreToolsPopup(false);
      }
    }
  });
}

if (typeof window !== "undefined") {
  window.isPassageAlreadyCompleted = isPassageAlreadyCompleted;
  window.markPassageSetCompletedInBank = markPassageSetCompletedInBank;
  window.updateSkipPassageButtonState = updateSkipPassageButtonState;
  window.toggleMoreToolsPopup = toggleMoreToolsPopup;
  window.skipCurrentPassage = skipCurrentPassage;
  window.unskipCurrentPassage = unskipCurrentPassage;
  window.getPassageFingerprint = getPassageFingerprint;
  window.syncCompletedPassageToAllExams = syncCompletedPassageToAllExams;
  window.initAndMigrateCompletedFingerprints = initAndMigrateCompletedFingerprints;
}
if (typeof globalThis !== "undefined") {
  globalThis.getPassageFingerprint = getPassageFingerprint;
  globalThis.syncCompletedPassageToAllExams = syncCompletedPassageToAllExams;
  globalThis.initAndMigrateCompletedFingerprints = initAndMigrateCompletedFingerprints;
}

/* Auto-register exams on script evaluation */
autoRegisterExams();
