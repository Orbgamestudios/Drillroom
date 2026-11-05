#!/usr/bin/env python3
import json
import os
import sys

# Ensure drillroom directory is on sys.path
BASE_DIR = "/home/cgslinde/DrillRoom/DrillRoom"
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from scratch.test_helpers import validate_passage_obj, count_words
from scratch.passages.p1_kant import passage_data as p1
from scratch.passages.p2_utilitarianism import passage_data as p2
from scratch.passages.p3_sartre import passage_data as p3
from scratch.passages.p4_pragmatism import passage_data as p4
from scratch.passages.p5_brain_in_vat import passage_data as p5
from scratch.passages.p6_kuhn import passage_data as p6
from scratch.passages.p7_popper import passage_data as p7
from scratch.passages.p8_hard_problem import passage_data as p8
from scratch.passages.p9_epistemic_injustice import passage_data as p9

passages = [p1, p2, p3, p4, p5, p6, p7, p8, p9]

def main():
    print("=" * 60)
    print("GENERATING EXAM 3 (CARS 90-MIN, 9 PASSAGES, 53 QUESTIONS)")
    print("=" * 60)
    
    total_errors = []
    total_qs = 0
    answer_dist = {0: 0, 1: 0, 2: 0, 3: 0}
    letters = ['A', 'B', 'C', 'D']
    
    for i, p in enumerate(passages, 1):
        wc, errs = validate_passage_obj(p)
        total_errors.extend(errs)
        n_qs = len(p["qs"])
        total_qs += n_qs
        print(f"Passage {i} ({p['id']}): {wc} words, {n_qs} questions - Topic: {p['topic']}")
        for q in p["qs"]:
            answer_dist[q["a"]] += 1
            
    print("-" * 60)
    print(f"Total Passages: {len(passages)}")
    print(f"Total Questions: {total_qs}")
    print(f"Answer Key Distribution: A={answer_dist[0]}, B={answer_dist[1]}, C={answer_dist[2]}, D={answer_dist[3]}")
    
    expected_q_counts = [6, 6, 6, 6, 6, 6, 6, 6, 5]
    actual_q_counts = [len(p["qs"]) for p in passages]
    if actual_q_counts != expected_q_counts:
        total_errors.append(f"Question distribution error: expected {expected_q_counts}, got {actual_q_counts}")
        
    if total_qs != 53:
        total_errors.append(f"Total questions error: expected 53, got {total_qs}")
        
    if total_errors:
        print("\nERRORS ENCOUNTERED:")
        for err in total_errors:
            print("  [ERROR]", err)
        sys.exit(1)
        
    print("\nAll passage and question validations PASSED!")
    
    # Write to exam_cars90_3.js
    output_js_path = os.path.join(BASE_DIR, "exam_cars90_3.js")
    js_content = "/* ---- exam_cars90_3.js ---- */\n/* Full 90-minute CARS Practice Exam 3: 9 passages (53 Qs) */\nconst EXAM_CARS90_3 = "
    js_content += json.dumps(passages, indent=2, ensure_ascii=False)
    js_content += ";\n"
    
    with open(output_js_path, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"Successfully generated {output_js_path} ({os.path.getsize(output_js_path)} bytes)")

if __name__ == "__main__":
    main()
