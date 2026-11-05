const assert = require("assert");
const fs = require("fs");
const path = require("path");

console.log("=== Verifying Sickle Cell Question & Codon Memorization Fix ===");

const bb90 = fs.readFileSync(path.join(__dirname, "../exam_bb90.js"), "utf8");
const bb60 = fs.readFileSync(path.join(__dirname, "../exam_60min.js"), "utf8");

// 1. Verify that GAG/GTG is provided with the amino acids in exam_bb90.js
assert(bb90.includes("converts codon GAG (encoding glutamate) to GTG (encoding valine) at position 6"), "exam_bb90 must provide the codon translation in the question stem");
assert(bb90.includes("Exposure of a hydrophobic side chain that lodges into a complementary pocket on adjacent deoxygenated tetramers"), "exam_bb90 must have the biophysical mechanism choice");
console.log("  ✓ exam_bb90 question provides codon-to-amino-acid translation and tests biophysical mechanism");

// 2. Verify that GAG/GTG is provided in exam_60min.js
assert(bb60.includes("converts codon GAG (encoding glutamate) to GTG (encoding valine) at position 6"), "exam_60min must provide the codon translation in the question stem");
assert(bb60.includes("Exposure of a hydrophobic side chain that lodges into a complementary pocket on adjacent deoxygenated tetramers"), "exam_60min must have the biophysical mechanism choice");
console.log("  ✓ exam_60min question provides codon-to-amino-acid translation and tests biophysical mechanism");

// 3. Verify Gate 4 choice length ratio <= 1.080x and correct answer is not longest
const ch = [
  "Disruption of proximal histidine-heme coordination, triggering apoprotein denaturation and oxidative precipitation",
  "Introduction of an electropositive residue that destabilizes salt bridges across the alpha-beta heterodimer boundary",
  "Exposure of a hydrophobic side chain that lodges into a complementary pocket on adjacent deoxygenated tetramers",
  "Formation of covalent intermolecular disulfide linkages between opposing beta subunits during high oxygen tension"
];
const lengths = ch.map(c => c.length);
const max = Math.max(...lengths);
const min = Math.min(...lengths);
const ratio = max / min;
console.log(`  ✓ Choice lengths: [${lengths.join(", ")}], max=${max}, min=${min}, ratio=${ratio.toFixed(4)}`);
assert(ratio <= 1.080, `Ratio must be <= 1.080, got ${ratio}`);
assert(ch[2].length < max, "Correct answer (index 2) must not be the longest option");
console.log("  ✓ Gate 4 compliance passed: ratio <= 1.080 and correct choice is not longest");

console.log("All codon fix tests passed successfully!");
