const assert = require("assert");

function inlineFormat(text) {
  if (!text) return "";
  let formatted = text
    .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
    .replace(/__(.*?)__/g, "<strong>$1</strong>")
    .replace(/\*(.*?)\*/g, "<em>$1</em>")
    .replace(/_(.*?)_/g, "<em>$1</em>")
    .replace(/`([^`]+)`/g, '<code style="background:#EBF0F5;color:#1B3A5C;padding:1px 5px;border-radius:3px;font-family:monospace;font-size:12.5px;font-weight:600">$1</code>');

  const graphMap = [
    { pattern: /\[?(Session Fatigue Delta Graph|Fatigue Delta Graph)\]?/gi, id: "avgSessionFatigueDelta", name: "Session Fatigue Delta Graph" },
    { pattern: /\[?(Passage Reading Speed Graph|Reading Speed Graph|Reading Speed Trajectory Graph)\]?/gi, id: "avgPassageWpm", name: "Reading Speed Graph" },
    { pattern: /\[?(Passage Reading Time Graph|Reading Time Graph)\]?/gi, id: "avgPassageReadSec", name: "Reading Time Graph" },
    { pattern: /\[?(Score Trajectory Graph|Scaled Score Graph)\]?/gi, id: "scaledScore", name: "Score Trajectory Graph" },
    { pattern: /\[?(Endurance Accuracy Delta Graph|Late-Stage Accuracy Graph)\]?/gi, id: "lateStageAccuracyDelta", name: "Endurance Accuracy Delta Graph" },
    { pattern: /\[?(Time Sinks Graph|Sunk-Cost Graph|Time-Sink Graph)\]?/gi, id: "timeSinkCount", name: "Time Sinks Graph" },
    { pattern: /\[?(Second-Guessing Net Impact Graph|Net Impact Graph)\]?/gi, id: "netSecondGuessing", name: "Second-Guessing Net Impact Graph" },
    { pattern: /\[?(Question Pace Graph|Question Solving Pace Graph)\]?/gi, id: "avgQSec", name: "Question Pace Graph" }
  ];

  graphMap.forEach(g => {
    formatted = formatted.replace(g.pattern, `<a href="javascript:void(0)" onclick="window.jumpToPerformanceChart &amp;&amp; window.jumpToPerformanceChart('${g.id}')" style="display:inline-flex;align-items:center;background:#EDF4FB;color:#185A9D;border:1px solid #B8D5E5;padding:1px 6px;border-radius:3px;font-weight:600;font-size:11.5px;text-decoration:none;margin:0 2px" title="Click to view this graph in Performance Charts">${g.name} &rarr;</a>`);
  });

  return formatted;
}

const input1 = "Your stamina is improving on the **Session Fatigue Delta Graph**, while reading speed holds steady on the Reading Speed Graph.";
const output1 = inlineFormat(input1);
console.log("Output 1:\n", output1);
assert(output1.includes("window.jumpToPerformanceChart('avgSessionFatigueDelta')"));
assert(output1.includes("window.jumpToPerformanceChart('avgPassageWpm')"));
console.log("✓ Graph pill formatting test passed!");
