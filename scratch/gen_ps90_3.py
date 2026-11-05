#!/usr/bin/env python3
"""
Generation script for MCAT P/S Exam 3 (exam_ps90_3.js).
Assembles 7 passages (6 Qs each = 42 Qs) + 10 standalone discretes = 52 Qs.
Enforces strict schema validation, AAMC Distractor Architecture, and +/-20% choice length parity.
"""

import sys
import os
import json
import re

# Add scratch to sys.path
sys.path.insert(0, '/home/cgslinde/DrillRoom/DrillRoom/scratch')

from exam3_src.p1 import p1_data
from exam3_src.p2 import p2_data
from exam3_src.p3 import p3_data
from exam3_src.p4 import p4_data
from exam3_src.p5 import p5_data
from exam3_src.p6 import p6_data
from exam3_src.p7 import p7_data
from exam3_src.disc import disc_data

sections = [
    p1_data,
    p2_data,
    p3_data,
    p4_data,
    p5_data,
    p6_data,
    p7_data,
    disc_data
]

print("=== Running Comprehensive Validation ===")
assert len(sections) == 8, f"Expected 8 sections, found {len(sections)}"

total_questions = 0
answer_counts = {0: 0, 1: 0, 2: 0, 3: 0}
q_num = 1

for s_idx, sec in enumerate(sections):
    is_disc = (s_idx == 7)
    sec_id = sec["id"]
    print(f"\nValidating Section {s_idx + 1}: {sec_id} ({sec['topic']})")
    
    assert sec["sec"] == "P/S", f"sec must be P/S in {sec_id}"
    assert sec["label"] == "Psychological, Social, and Biological Foundations of Behavior"
    assert sec["examId"] == "ps90_3"
    
    if not is_disc:
        expected_id = f"exam_ps90_3_p{s_idx + 1}"
        assert sec_id == expected_id, f"Expected {expected_id}, got {sec_id}"
        assert sec["sheet"] == s_idx + 1, f"Expected sheet {s_idx + 1}, got {sec['sheet']}"
        assert "<table class=\"tbl\">" in sec["passage"], f"Passage {s_idx+1} missing HTML table"
        assert "<div class=\"ttl\">" in sec["passage"]
        
        # Word count check of passage paragraph prose
        paras = re.findall(r'<p>(.*?)</p>', sec["passage"], re.DOTALL)
        para_text = ' '.join(paras)
        clean = re.sub(r'<[^>]+>', ' ', para_text)
        words = clean.split()
        print(f"  Passage paragraph prose word count: {len(words)} words")
        assert 250 <= len(words) <= 360, f"Passage {s_idx+1} word count {len(words)} out of expected ~250-350 range"
        assert len(sec["qs"]) == 6, f"Passage {s_idx+1} must have 6 questions"
    else:
        assert sec_id == "exam_ps90_3_disc"
        assert sec["sheet"] is None
        assert sec["passage"] == ""
        assert len(sec["qs"]) == 10, f"Discretes must have 10 questions"

    for q_idx, q_obj in enumerate(sec["qs"]):
        current_q_num = q_num
        q_num += 1
        total_questions += 1
        
        # Validate discrete flag
        if is_disc:
            assert q_obj.get("d") is True, f"Q{current_q_num} must have d: True"
        else:
            assert "d" not in q_obj, f"Q{current_q_num} should not have d flag"
            
        # Validate question text
        assert isinstance(q_obj["q"], str) and len(q_obj["q"].strip()) > 10
        
        # Validate choices
        ch = q_obj["ch"]
        assert len(ch) == 4, f"Q{current_q_num} must have exactly 4 choices"
        for c in ch:
            assert isinstance(c, str) and len(c.strip()) > 0
            
        # Validate answer key
        a = q_obj["a"]
        assert a in (0, 1, 2, 3), f"Q{current_q_num} invalid answer index: {a}"
        answer_counts[a] += 1
        
        # Validate length parity (+/- 20% from mean)
        lens = [len(c) for c in ch]
        mean_l = sum(lens) / 4.0
        max_diff = max(abs(l - mean_l) for l in lens)
        ratio = max_diff / mean_l
        if ratio > 0.20:
            print(f"  ERROR: Q{current_q_num} parity failed! ratio={ratio*100:.1f}%, lens={lens}")
            for ci, c in enumerate(ch):
                print(f"    [{ci}] ({len(c)} chars): {c}")
            sys.exit(1)
        else:
            print(f"  Q{current_q_num} (key={chr(65+a)}): lens={lens}, mean={mean_l:.1f}, parity_dev={ratio*100:.1f}%")
            
        # Validate explanation
        e = q_obj["e"]
        assert e.startswith("<strong>"), f"Q{current_q_num} explanation should start with <strong>"
        assert "Distractor Traps:" in e, f"Q{current_q_num} explanation missing Distractor Traps:"
        assert "&bull;" in e, f"Q{current_q_num} explanation missing bullet points in traps"

print(f"\nTotal questions validated: {total_questions}")
assert total_questions == 52, f"Expected 52 questions, found {total_questions}"

print("\nAnswer Distribution:")
for k, count in sorted(answer_counts.items()):
    pct = (count / total_questions) * 100
    print(f"  Choice {chr(65+k)} ({k}): {count} ({pct:.1f}%)")
    assert count == 13, f"Choice {chr(65+k)} count is {count}, expected exactly 13!"

print("\nAll programmatic validations PASSED successfully!")

# Format output file
output_path = "/home/cgslinde/DrillRoom/DrillRoom/exam_ps90_3.js"
print(f"\nWriting production JS file to {output_path}...")

json_text = json.dumps(sections, indent=2, ensure_ascii=False)
header = """/* ---- exam_ps90_3.js ---- */
/* Full 90-minute Psych/Soc Practice Exam 3: 7 passages (42 Qs) + 10 discrete Qs = 52 Qs */
const EXAM_PS90_3 = """

full_content = header + json_text + ";\n"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_content)

file_size = os.path.getsize(output_path)
print(f"Successfully wrote {output_path} ({file_size:,} bytes).")
