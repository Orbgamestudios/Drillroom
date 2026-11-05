# /home/cgslinde/DrillRoom/DrillRoom/scratch/cars5/build_exam.py
import json
import re
from validator import validate_passage

from p1 import passage_data as p1
from p2 import passage_data as p2
from p3 import passage_data as p3
from p4 import passage_data as p4
from p5 import passage_data as p5
from p6 import passage_data as p6
from p7 import passage_data as p7
from p8 import passage_data as p8
from p9 import passage_data as p9

passages = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
expected_counts = [6, 6, 6, 6, 6, 6, 6, 6, 5]

all_errors = []
total_qs = 0
ans_counts = {0: 0, 1: 0, 2: 0, 3: 0}
letters = ["A", "B", "C", "D"]

print("=== VALIDATING ALL 9 PASSAGES ===")
for idx, (p, expected_q) in enumerate(zip(passages, expected_counts)):
    p_num = idx + 1
    errs, wc = validate_passage(p, p_num, expected_q)
    if errs:
        all_errors.extend(errs)
    q_count = len(p["qs"])
    total_qs += q_count
    for q_idx, q in enumerate(p["qs"]):
        a = q["a"]
        ans_counts[a] += 1
    print(f"Passage {p_num}: {wc} words, {q_count} questions.")

print(f"\nTotal Passages: {len(passages)}")
print(f"Total Questions: {total_qs}")
print("Answer distribution:")
for i, l in enumerate(letters):
    print(f"  {l}: {ans_counts[i]} ({ans_counts[i]/total_qs*100:.1f}%)")

if total_qs != 53:
    all_errors.append(f"Total questions is {total_qs}, expected 53.")

expected_dist = {0: 13, 1: 13, 2: 14, 3: 13}
for k, v in expected_dist.items():
    if ans_counts[k] != v:
        all_errors.append(f"Answer count for {letters[k]} is {ans_counts[k]}, expected {v}.")

if all_errors:
    print("\nVALIDATION FAILED WITH ERRORS:")
    for e in all_errors:
        print(" -", e)
    exit(1)

print("\nALL PASSAGES AND QUESTIONS VALIDATED SUCCESSFULLY!")

# Now format as JavaScript file
js_content = "/* ---- exam_cars90_5.js ---- */\n"
js_content += "/* Full 90-minute CARS Practice Exam 5: 9 passages (53 Qs) */\n"
js_content += "const EXAM_CARS90_5 = " + json.dumps(passages, indent=2, ensure_ascii=False) + ";\n"

out_path = "/home/cgslinde/DrillRoom/DrillRoom/exam_cars90_5.js"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"\nWrote exam to {out_path}")
