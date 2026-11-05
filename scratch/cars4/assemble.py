#!/usr/bin/env python3
import json
import os
import sys

SCRATCH_DIR = "/home/cgslinde/DrillRoom/DrillRoom/scratch/cars4"
sys.path.insert(0, SCRATCH_DIR)

from validate import validate_passage, count_words
from passages.p1 import passage_data as p1
from passages.p2 import passage_data as p2
from passages.p3 import passage_data as p3
from passages.p4 import passage_data as p4
from passages.p5 import passage_data as p5
from passages.p6 import passage_data as p6
from passages.p7 import passage_data as p7
from passages.p8 import passage_data as p8
from passages.p9 import passage_data as p9

passages = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
expected_q_counts = [6, 6, 6, 6, 6, 6, 6, 6, 5]

def main():
    print("=" * 65)
    print("VALIDATING & ASSEMBLING EXAM 4 (CARS 90-MIN, 9 PASSAGES, 53 Qs)")
    print("=" * 65)
    
    total_errors = []
    total_qs = 0
    answer_dist = {0: 0, 1: 0, 2: 0, 3: 0}
    letters = ['A', 'B', 'C', 'D']
    
    for idx, p in enumerate(passages, 1):
        expected_qs = expected_q_counts[idx - 1]
        wc, errs = validate_passage(p, expected_q_count=expected_qs)
        total_errors.extend(errs)
        n_qs = len(p["qs"])
        total_qs += n_qs
        q_ans = [letters[q["a"]] for q in p["qs"]]
        print(f"Passage {idx} ({p['id']}): {wc} words, {n_qs} Qs, Ans: {q_ans} - Topic: {p['topic']}")
        for q in p["qs"]:
            answer_dist[q["a"]] += 1
            
    print("-" * 65)
    print(f"Total Passages: {len(passages)}")
    print(f"Total Questions: {total_qs} (Target: 53)")
    print(f"Answer Key Distribution: A={answer_dist[0]}, B={answer_dist[1]}, C={answer_dist[2]}, D={answer_dist[3]}")
    print(f"Target Distribution:     A=13, B=13, C=14, D=13")
    
    if total_qs != 53:
        total_errors.append(f"Total questions error: expected 53, got {total_qs}")
        
    expected_dist = {0: 13, 1: 13, 2: 14, 3: 13}
    if answer_dist != expected_dist:
        total_errors.append(f"Answer distribution mismatch: expected {expected_dist}, got {answer_dist}")
        
    if total_errors:
        print("\nERRORS DETECTED:")
        for err in total_errors:
            print("  [ERROR]", err)
        sys.exit(1)
        
    print("\nAll validation checks PASSED perfectly!")
    
    # Write to exam_cars90_4.js
    output_js_path = "/home/cgslinde/DrillRoom/DrillRoom/exam_cars90_4.js"
    js_content = "/* ---- exam_cars90_4.js ---- */\n/* Full 90-minute CARS Practice Exam 4: 9 passages (53 Qs) */\nconst EXAM_CARS90_4 = "
    js_content += json.dumps(passages, indent=2, ensure_ascii=False)
    js_content += ";\n"
    
    with open(output_js_path, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"Successfully generated {output_js_path} ({os.path.getsize(output_js_path)} bytes)")

if __name__ == "__main__":
    main()
