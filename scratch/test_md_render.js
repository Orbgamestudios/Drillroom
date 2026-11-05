const store = {};
global.localStorage = { getItem: k => store[k] || null, setItem: (k,v) => { store[k]=v; }, removeItem: k => { delete store[k]; } };
global.window = { addEventListener: () => {} };
global.document = { getElementById: () => null, body: { appendChild: () => {} } };

require('/home/cgslinde/DrillRoom/DrillRoom/gemini_analysis.js');

const sample = `# 1. 📊 Executive Score Diagnostic
- Scaled score of **126/132** (72nd percentile).
- **Solid:** 28 | **Lucky:** 4 | **Shaky:** 5 | **Misses:** 15

| Category | Count | Focus |
| --- | --- | --- |
| Content Gap | 6 | Amino Acid Chemistry |
| Distractor Trap | 5 | Opposite Direction |

> [!TIP]
> Always rephrase the stem in 3 words before reading choices.

\`\`\`
Delta G = Delta H - T * Delta S
\`\`\`
`;

const html = window.renderGeminiMarkdown(sample);
console.log("HTML Output:\n", html);
assert = require('assert');
assert(html.includes('<h2'), 'Should contain h2 header');
assert(html.includes('<strong>126/132</strong>'), 'Should format bold');
assert(html.includes('<table'), 'Should contain table');
assert(html.includes('TIP:'), 'Should render tip alert');
assert(html.includes('<pre'), 'Should render code block');
console.log("\nALL MARKDOWN TESTS PASSED!");
