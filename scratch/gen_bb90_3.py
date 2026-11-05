"""
gen_bb90_3.py
Builds Exam 3 B/B from modular passage scripts in scratch/bb_passages/.
"""
import json
import os
import re
import sys

sys.path.append("/home/cgslinde/DrillRoom/DrillRoom/scratch/bb_passages")

from p1 import p1_data
from p2 import p2_data
from p3 import p3_data
from p4 import p4_data
from p5 import p5_data
from p6 import p6_data
from p7 import p7_data
from discretes import bb_discretes_data

passages = [
    p1_data,
    p2_data,
    p3_data,
    p4_data,
    p5_data,
    p6_data,
    p7_data,
    bb_discretes_data
]

total_qs = 0
parity_violations = []

for idx, p in enumerate(passages):
    p_id = p["id"]
    qs = p["qs"]
    total_qs += len(qs)
    
    if p_id != "exam_bb90_3_disc":
        assert "<table class=\"tbl\">" in p["passage"], f"Missing table in {p_id}"
        p_texts = re.findall(r"<p>(.*?)</p>", p["passage"], re.DOTALL)
        prose = re.sub(r"<[^>]+>", " ", " ".join(p_texts))
        words = prose.split()
        print(f"[{idx+1}] {p_id}: {len(qs)} questions, prose words: {len(words)}")
        assert 230 <= len(words) <= 380, f"Prose word count out of range in {p_id}: {len(words)}"
    else:
        print(f"[{idx+1}] {p_id}: {len(qs)} discrete questions")

    for q_idx, q in enumerate(qs):
        ch = q["ch"]
        a = q["a"]
        e = q["e"]
        
        assert len(ch) == 4, f"Question {q_idx+1} in {p_id} does not have 4 choices"
        assert a in [0, 1, 2, 3], f"Question {q_idx+1} in {p_id} has invalid answer index {a}"
        assert "Distractor Traps:" in e, f"Question {q_idx+1} in {p_id} missing Distractor Traps in explanation"
        
        if p_id == "exam_bb90_3_disc":
            assert q.get("d") is True, f"Question {q_idx+1} in discretes missing d: True"
        
        lengths = [len(c) for c in ch]
        avg_len = sum(lengths) / 4.0
        diff_from_avg = [abs(l - avg_len) / avg_len for l in lengths]
        max_diff = max(diff_from_avg)
        
        if max_diff > 0.20:
            parity_violations.append((p_id, q_idx + 1, lengths, max_diff))

assert total_qs == 52, f"Expected 52 questions, found {total_qs}"
assert len(parity_violations) == 0, f"Parity violations found: {parity_violations}"

js_output_path = "/home/cgslinde/DrillRoom/DrillRoom/exam_bb90_3.js"
js_content = "/* ---- exam_bb90_3.js ---- */\n/* Full 90-minute Biochem/Bio Practice Exam 3: 7 passages (42 Qs) + 10 discrete Qs = 52 Qs */\nconst EXAM_BB90_3 = " + json.dumps(passages, indent=2) + ";\n"

with open(js_output_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"All 52 questions verified and successfully generated {js_output_path} ({os.path.getsize(js_output_path)} bytes)")
