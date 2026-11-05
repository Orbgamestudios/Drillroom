import json
import os
import re
import sys

sys.path.append("/home/cgslinde/DrillRoom/DrillRoom/scratch/bb4")

from p1 import p1_data
from p2 import p2_data
from p3 import p3_data
from p4 import p4_data
from p5 import p5_data
from p6 import p6_data
from p7 import p7_data
from discretes import bb_discretes_data
from validator import validate_section, count_words

sections = [
    p1_data,
    p2_data,
    p3_data,
    p4_data,
    p5_data,
    p6_data,
    p7_data,
    bb_discretes_data
]

letters = ['A', 'B', 'C', 'D']
ans_counts = {0: 0, 1: 0, 2: 0, 3: 0}
all_errors = []
total_qs = 0

for s_idx, sec in enumerate(sections):
    is_disc = (sec["id"] == "exam_bb90_4_disc")
    wc, errs = validate_section(sec, is_discrete=is_disc)
    all_errors.extend(errs)
    
    qs = sec["qs"]
    total_qs += len(qs)
    
    if not is_disc:
        print(f"Passage {s_idx+1} ({sec['id']}): {len(qs)} Qs, prose word count: {wc}")
    else:
        print(f"Discrete set ({sec['id']}): {len(qs)} Qs")
        
    for q_idx, q in enumerate(qs, 1):
        a = q["a"]
        ans_counts[a] += 1
        
        # Check distractor trap bullets
        e = q["e"]
        bullets = re.findall(r"&bull;\s*([A-D])", e)
        expected_distractors = [letters[i] for i in range(4) if i != a]
        if bullets != expected_distractors:
            all_errors.append(f"{sec['id']} Q{q_idx}: distractor bullets {bullets} do not match expected {expected_distractors}")
            
        # Check ratio max/min
        lengths = [len(c) for c in q["ch"]]
        ratio = max(lengths) / min(lengths)
        if ratio > 1.25:
            all_errors.append(f"{sec['id']} Q{q_idx}: ratio max/min {ratio:.2f} > 1.25 (lengths: {lengths})")

print(f"\nTotal Questions: {total_qs}")
print(f"Answer distribution: A: {ans_counts[0]}, B: {ans_counts[1]}, C: {ans_counts[2]}, D: {ans_counts[3]}")

if total_qs != 52:
    all_errors.append(f"Total questions is {total_qs}, expected 52")

for i, count in ans_counts.items():
    if count != 13:
        all_errors.append(f"Answer choice {letters[i]} has {count} occurrences, expected exactly 13")

if all_errors:
    print(f"\nFAILED with {len(all_errors)} errors:")
    for err in all_errors:
        print(f" - {err}")
    sys.exit(1)
else:
    print("\nALL 52 QUESTIONS PASSED VALIDATION WITH ZERO ERRORS!")

# Write exam_bb90_4.js
output_path = "/home/cgslinde/DrillRoom/DrillRoom/exam_bb90_4.js"
header = "/* ---- exam_bb90_4.js ---- */\n/* Full 90-minute Biochem/Bio Practice Exam 4: 7 passages (42 Qs) + 10 discrete Qs = 52 Qs */\nconst EXAM_BB90_4 = "
json_str = json.dumps(sections, indent=2, ensure_ascii=False)
full_js = header + json_str + ";\n"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_js)

print(f"Successfully generated {output_path} ({os.path.getsize(output_path):,} bytes)")
