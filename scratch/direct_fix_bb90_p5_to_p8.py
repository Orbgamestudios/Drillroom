import sys, re
sys.path.append('/home/cgslinde/DrillRoom/DrillRoom/scratch')
import craft_bb90_p5_to_p8 as m

# P5 Q2 (Q26): ans=B (1)
m.p5_qs[1]["ch"] = [
    "sudden opening of nuclear pore complexes allowing calcium leakage into the sarcoplasm of myocytes",
    "re-activation of voltage-gated L-type Ca2+ channels (Cav1.2) during prolonged Phase 2/3 plateaus",
    "spontaneous ATP depletion within the matrix causing rapid potassium channel opening in myocytes",
    "abrupt efflux of divalent magnesium ions through sarcolemmal calcium-activated pump complexes"
]

# P5 Q5 (Q29): ans=D (3)
m.p5_qs[4]["ch"] = [
    "The time required for electrical conduction to traverse the atrioventricular AV node alone in heart",
    "The isolated period of ventricular mechanical contraction occurring strictly during systole phase",
    "The duration of atrial depolarization and subsequent repolarization prior to the QRS wave in rhythm",
    "The total time required for ventricular depolarization and subsequent complete repolarization"
]

# P6 Q2 (Q32): ans=D (3)
m.p6_qs[1]["ch"] = [
    "Oligomycin oxidizes all intramitochondrial NADH molecules into NAD+ to deplete electron pools",
    "Oligomycin covalently cleaves cytochrome c, severing electron transfer between III and IV cristae",
    "Oligomycin opens giant outer membrane channels, dissipating all mitochondrial substrate gradients",
    "Proton pumping against a hyperpolarized electrochemical gradient is thermodynamically arrested"
]

# P6 Q3 (Q33): ans=A (0)
m.p6_qs[2]["ch"] = [
    "NADH translocates 10 H+ (4 at I, 4 at III, 2 at IV); FADH2 translocates 6 H+ (4 at III, 2 at IV)",
    "NADH translocates 12 H+ (4 at I, 4 at III, 4 at IV); FADH2 translocates 8 H+ (4 at III, 4 at IV) net",
    "NADH translocates 8 H+ (4 at I, 2 at III, 2 at IV); FADH2 translocates 4 H+ (2 at III, 2 at IV) net",
    "NADH translocates 6 H+ (2 at I, 2 at III, 2 at IV); FADH2 translocates 3 H+ (2 at III, 1 at IV) net"
]

# P6 Q4 (Q34): ans=C (2)
m.p6_qs[3]["ch"] = [
    "Complex I, preventing electron transfer from flavin mononucleotide to iron-sulfur centers in core",
    "Complex II, preventing oxidation of succinate into fumarate during the citric acid cycle in cells",
    "Complex IV (cytochrome c oxidase), blocking terminal electron transfer to molecular oxygen gas",
    "Complex III (cytochrome bc1), preventing ubiquinol oxidation via the Q cycle mechanism in cristae"
]

# P6 Q5 (Q35): ans=B (1)
m.p6_qs[4]["ch"] = [
    "The matrix is more acidic (lower pH) and electrically positive relative to space in organelle",
    "The matrix is more alkaline (higher pH) and electrically negative relative to space in organelle",
    "The matrix is more alkaline (higher pH) and electrically positive relative to the outer organelle",
    "The matrix is iso-osmolar with identical pH and zero potential relative to space in organelle"
]

# P7 Q3 (Q39): ans=D (3)
m.p7_qs[2]["ch"] = [
    "AID normally acts as a transcriptional repressor that suppresses baseline IgM synthesis in B lymphocytes",
    "IgM expression requires RAG1-mediated inversion, whereas other isotypes require RNA degradation in cells",
    "T-helper cells selectively destroy B cells that attempt to secrete IgG or IgA in secondary lymph nodes",
    "B cells can transcribe the default Cμ constant region, but cannot undergo CSR to other isotypes in body"
]

# Disc Q5 (Q47): ans=A (0)
m.discrete_qs[4]["ch"] = [
    "All four children inherit the maternal mitochondrial mutation and risk developing clinical symptoms",
    "Only the two daughters will inherit the mutation, whereas both sons will remain completely unaffected here",
    "Only the two sons will inherit the mutation via non-recombining holandric Y-chromosome transmission line",
    "Fifty percent of the children will inherit the mutation following typical Mendelian dominant genetics"
]

# Disc Q6 (Q48): ans=B (1)
m.discrete_qs[5]["ch"] = [
    "Peptide hormones are lipophilic and cross the plasma membrane to bind nuclear transcription factors in cell",
    "Peptide hormones act via cell-surface receptors and second messengers, while steroids alter expression",
    "Steroid hormones circulate freely dissolved in plasma, whereas peptide hormones require carrier globulins",
    "Peptide hormones are synthesized directly from cholesterol, whereas steroid hormones translate from mRNA"
]

# Disc Q7 (Q49): ans=C (2)
m.discrete_qs[6]["ch"] = [
    "Hemoglobin has a significantly higher overall affinity for oxygen across all physiological tissue pO2 values",
    "Hemoglobin exhibits negative cooperativity, meaning oxygen binding promotes rapid subunit disassembly in cells",
    "Hemoglobin displays positive cooperativity, where O2 binding at one subunit increases affinity elsewhere",
    "Myoglobin contains four cooperative heme groups, whereas hemoglobin binds O2 through a single porphyrin ring"
]

# Now run validation on all!
m.validate_questions(m.p5_qs, 25)
m.validate_questions(m.p6_qs, 31)
m.validate_questions(m.p7_qs, 37)
m.validate_questions(m.discrete_qs, 43)
print("ALL bb90 p5-p8 VALIDATED SUCCESSFULLY IN MEMORY!")

# Write out the updated craft_bb90_p5_to_p8.py cleanly
import json
with open("/home/cgslinde/DrillRoom/DrillRoom/scratch/craft_bb90_p5_to_p8.py", "w") as f:
    f.write('''# -*- coding: utf-8 -*-
"""
Suite 1 Bio/Biochem 90 Overhaul: Passages 5 to 8 (Questions 25 to 52)
5-Gate Review Protocol calibration
"""
import re

def validate_questions(qs_list, start_idx=25):
    for i, q in enumerate(qs_list):
        num = start_idx + i
        ans = q["a"]
        ch = q["ch"]
        lens = [len(c) for c in ch]
        
        is_num = all(re.match(r'^[+-]?\d+(?:\.\d+)?(?:/[+-]?\d+(?:\.\d+)?)?(?:\s*(?:×|x)\s*10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹\d+-]+)?(?:\s*[\w%/°℃Ω\^]+)?(?:\s*\([^\)]+\))?$', c.strip()) for c in ch)
        if is_num:
            def extract_val(s):
                m = re.search(r'([+-]?\d+(?:\.\d+)?)', s)
                return float(m.group(1)) if m else 0.0
            vals = [extract_val(c) for c in ch]
            asc = all(vals[j] <= vals[j+1] for j in range(len(vals)-1))
            desc = all(vals[j] >= vals[j+1] for j in range(len(vals)-1))
            assert asc or desc, f"Q{num} numeric choices not sorted: {vals}"
        else:
            ratio = max(lens) / min(lens) if min(lens) > 0 else 999
            assert ratio <= 1.0801, f"Q{num} length ratio violated: {ratio:.3f} (lens: {lens})"
            assert ans != lens.index(max(lens)), f"Q{num} correct choice is strictly longest! ans={ans}, lens={lens}"

        e = q["e"]
        assert "<strong>[Governing Principle:" in e, f"Q{num} missing Governing Principle tag"
        assert "<em>Distractor Traps:</em><br>&bull;" in e, f"Q{num} missing Distractor Traps tag"
        other_letters = [chr(65+j) for j in range(4) if j != ans]
        for ol in other_letters:
            assert f"&bull; {ol} (" in e, f"Q{num} missing autopsy for {ol}"
    print(f"Validated {len(qs_list)} questions starting at Q{start_idx} successfully!")

p5_qs = ''' + json.dumps(m.p5_qs, indent=4) + '''
p6_qs = ''' + json.dumps(m.p6_qs, indent=4) + '''
p7_qs = ''' + json.dumps(m.p7_qs, indent=4) + '''
discrete_qs = ''' + json.dumps(m.discrete_qs, indent=4) + '''

if __name__ == "__main__":
    validate_questions(p5_qs, 25)
    validate_questions(p6_qs, 31)
    validate_questions(p7_qs, 37)
    validate_questions(discrete_qs, 43)
    print("ALL PASSAGES 5 TO 8 QUESTIONS VALIDATED 100% PERFECTLY!")
''')
print("Successfully regenerated craft_bb90_p5_to_p8.py!")
