#!/usr/bin/env python3
"""
assemble_cp5.py
Assembles exam_cp90_5.js from modular passage and discrete files,
verifying all MCAT C/P section specifications.
"""

import json
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from validator import validate_section, count_words
import p1
import p2
import p3
import p4
import p5
import p6
import p7
import discretes

def assemble():
    passages = [
        p1.passage_data,
        p2.passage_data,
        p3.passage_data,
        p4.passage_data,
        p5.passage_data,
        p6.passage_data,
        p7.passage_data
    ]
    discrete = discretes.discrete_data

    all_sections = passages + [discrete]

    # Validate each section
    total_errors = []
    total_qs = 0
    ans_counts = {0: 0, 1: 0, 2: 0, 3: 0}
    letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}

    print("=== Validating Individual Sections ===")
    for idx, p_obj in enumerate(passages, 1):
        wc, errs = validate_section(p_obj, is_discrete=False)
        print(f"Passage {idx} ({p_obj['id']}): {len(p_obj['qs'])} Qs, {wc} prose words")
        if errs:
            total_errors.extend(errs)
        total_qs += len(p_obj['qs'])
        for q in p_obj['qs']:
            ans_counts[q['a']] += 1

    wc_disc, errs_disc = validate_section(discrete, is_discrete=True)
    print(f"Discrete ({discrete['id']}): {len(discrete['qs'])} Qs")
    if errs_disc:
        total_errors.extend(errs_disc)
    total_qs += len(discrete['qs'])
    for q in discrete['qs']:
        ans_counts[q['a']] += 1

    print("\n=== Section & Question Audit ===")
    print(f"Total Sections: {len(all_sections)} (7 Passages + 1 Discrete Set)")
    print(f"Total Questions: {total_qs} (Target: 52)")
    if total_qs != 52:
        total_errors.append(f"Total questions is {total_qs}, expected 52!")

    print("\n=== Answer Key Distribution ===")
    for k in sorted(ans_counts.keys()):
        print(f"Choice {letters[k]}: {ans_counts[k]} (Target: 13)")
        if ans_counts[k] != 13:
            total_errors.append(f"Choice {letters[k]} has count {ans_counts[k]}, expected exactly 13!")

    # Check distractor trap bullets
    print("\n=== Distractor Traps Bullet Count Audit ===")
    q_global_idx = 1
    for s_idx, sec in enumerate(all_sections):
        pid = sec['id']
        for q_idx, q in enumerate(sec['qs'], 1):
            exp = q.get('e', '')
            bullets = [line.strip() for line in exp.split('<br>') if line.strip().startswith('&bull;')]
            if len(bullets) != 3:
                total_errors.append(f"{pid} Q{q_idx} (Global Q{q_global_idx}): expected 3 &bull; bullets, found {len(bullets)}")
            q_global_idx += 1

    if total_errors:
        print("\nERRORS FOUND:")
        for e in total_errors:
            print(" -", e)
        sys.exit(1)

    print("\nAll automated validation checks passed with 100% compliance!")

    # Format JavaScript output
    js_content = "/* ---- exam_cp90_5.js ---- */\n"
    js_content += "/* Full 90-minute Chem/Physical Practice Exam 5: 7 passages (42 Qs) + 10 discrete Qs = 52 Qs */\n"
    js_content += "const EXAM_CP90_5 = "
    js_content += json.dumps(all_sections, indent=2, ensure_ascii=False)
    js_content += ";\n"

    dest_path = "/home/cgslinde/DrillRoom/DrillRoom/exam_cp90_5.js"
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(js_content)

    print(f"\nSuccessfully wrote production-ready exam to: {dest_path}")
    print(f"File size: {os.path.getsize(dest_path):,} bytes")

if __name__ == "__main__":
    assemble()
