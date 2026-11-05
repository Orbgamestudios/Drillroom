#!/usr/bin/env python3
import json
import os
import sys

SCRATCH_DIR = "/home/cgslinde/DrillRoom/DrillRoom/scratch/ps4"
sys.path.insert(0, SCRATCH_DIR)

from validator import validate_section, count_words
from passages.p1 import passage_data as p1
from passages.p2 import passage_data as p2
from passages.p3 import passage_data as p3
from passages.p4 import passage_data as p4
from passages.p5 import passage_data as p5
from passages.p6 import passage_data as p6
from passages.p7 import passage_data as p7
from passages.disc import passage_data as disc

passages = [p1, p2, p3, p4, p5, p6, p7]

def main():
    print("=" * 65)
    print("VALIDATING & ASSEMBLING EXAM 4 (P/S 90-MIN, 7 PASSAGES + 10 DISCRETE Qs = 52 Qs)")
    print("=" * 65)
    
    total_errors = []
    total_qs = 0
    answer_dist = {0: 0, 1: 0, 2: 0, 3: 0}
    letters = ['A', 'B', 'C', 'D']
    
    # Validate 7 passages
    for idx, p in enumerate(passages, 1):
        wc, errs = validate_section(p, is_discrete=False)
        total_errors.extend(errs)
        n_qs = len(p["qs"])
        total_qs += n_qs
        q_ans = [letters[q["a"]] for q in p["qs"]]
        print(f"Passage {idx} ({p['id']}): {wc} words, {n_qs} Qs, Ans: {q_ans} - Topic: {p['topic']}")
        
        # Word count check: strict MCAT requirement 200 - 380 words
        if not (200 <= wc <= 380):
            total_errors.append(f"Passage {idx} word count {wc} outside 200-380 words")
            
        for q_idx, q in enumerate(p["qs"], 1):
            answer_dist[q["a"]] += 1
            # Check 3 distractor bullets
            e = q.get("e", "")
            bullets = [b for b in e.split("&bull;") if b.strip()]
            if len(bullets) != 4: # First part is intro, then 3 bullets after split
                # Let's count count of "&bull;"
                b_count = e.count("&bull;")
                if b_count != 3:
                    total_errors.append(f"Passage {idx} Q{q_idx}: expected exactly 3 distractor bullets, found {b_count}")
                    
    # Validate discrete set
    wc_d, errs_d = validate_section(disc, is_discrete=True)
    total_errors.extend(errs_d)
    n_qs_d = len(disc["qs"])
    total_qs += n_qs_d
    q_ans_d = [letters[q["a"]] for q in disc["qs"]]
    print(f"Discrete ({disc['id']}): {n_qs_d} Qs, Ans: {q_ans_d} - Topic: {disc['topic']}")
    for q_idx, q in enumerate(disc["qs"], 1):
        answer_dist[q["a"]] += 1
        b_count = q.get("e", "").count("&bull;")
        if b_count != 3:
            total_errors.append(f"Discrete Q{q_idx}: expected exactly 3 distractor bullets, found {b_count}")
            
    print("-" * 65)
    print(f"Total Sections: {len(passages)} passages + 1 discrete set")
    print(f"Total Questions: {total_qs} (Target: 52)")
    print(f"Answer Key Distribution: A={answer_dist[0]}, B={answer_dist[1]}, C={answer_dist[2]}, D={answer_dist[3]}")
    print(f"Target Distribution:     A=13, B=13, C=13, D=13")
    
    if total_qs != 52:
        total_errors.append(f"Total questions error: expected 52, got {total_qs}")
        
    expected_dist = {0: 13, 1: 13, 2: 13, 3: 13}
    if answer_dist != expected_dist:
        total_errors.append(f"Answer distribution mismatch: expected {expected_dist}, got {answer_dist}")
        
    if total_errors:
        print("\nERRORS DETECTED:")
        for err in total_errors:
            print("  [ERROR]", err)
        sys.exit(1)
        
    print("\nAll validation checks PASSED perfectly!")
    
    all_sections = passages + [disc]
    output_js_path = "/home/cgslinde/DrillRoom/DrillRoom/exam_ps90_4.js"
    js_content = "/* ---- exam_ps90_4.js ---- */\n/* Full 90-minute Psych/Soc Practice Exam 4: 7 passages (42 Qs) + 10 discrete Qs = 52 Qs */\nconst EXAM_PS90_4 = "
    js_content += json.dumps(all_sections, indent=2, ensure_ascii=False)
    js_content += ";\n"
    
    with open(output_js_path, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"Successfully generated {output_js_path} ({os.path.getsize(output_js_path)} bytes)")

if __name__ == "__main__":
    main()
