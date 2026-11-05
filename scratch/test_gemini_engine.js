// Mock localStorage and window
const store = {};
global.localStorage = {
  getItem: k => store[k] || null,
  setItem: (k, v) => { store[k] = String(v); },
  removeItem: k => { delete store[k]; }
};

global.window = {
  addEventListener: () => {},
  E: null
};
global.document = {
  getElementById: id => null,
  body: { appendChild: () => {} }
};

// Load gemini_analysis.js
require('/home/cgslinde/DrillRoom/DrillRoom/gemini_analysis.js');

console.log("Functions exported to window:", Object.keys(global.window));

// Test Markdown formatting
const mdSample = `
# 1. 📊 Executive Diagnostic
- High-yield **content gap** in amino acids.
- You chose *inverted* relationship.

| Question | Trap Type | Principle |
| --- | --- | --- |
| Q4 | Buzzword Trap | Henderson-Hasselbalch |
| Q12 | Opposite | Le Chatelier |

> [!TIP]
> Always check for the negative control before interpreting delta changes.

\`\`\`
Km increases = affinity decreases
\`\`\`
`;

// Test rendering markdown
// We can test by calling through the module or invoking renderMarkdown
console.log("Gemini Engine module loaded successfully!");
