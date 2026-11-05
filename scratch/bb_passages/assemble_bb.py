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

print("=== STARTING FULL EXAM AUDIT & ASSEMBLY ===")

total_qs = 0
ans_dist = {0: 0, 1: 0, 2: 0, 3: 0}
all_passed = True

for idx, p in enumerate(passages):
    pid = p["id"]
    qs = p["qs"]
    total_qs += len(qs)
    
    if pid != "exam_bb90_3_disc":
        assert p.get("sheet") == idx + 1, f"Sheet number mismatch for {pid}: {p.get('sheet')}"
        assert "<table class=\"tbl\">" in p["passage"], f"Missing HTML table in {pid}"
        p_texts = re.findall(r"<p>(.*?)</p>", p["passage"], re.DOTALL)
        prose = re.sub(r"<[^>]+>", " ", " ".join(p_texts))
        words = prose.split()
        print(f"[{idx+1}] {pid}: {len(qs)} questions, prose word count: {len(words)}")
        assert 230 <= len(words) <= 380, f"Prose word count outside 230-380 in {pid}: {len(words)}"
    else:
        assert p.get("sheet") is None, f"Discrete block sheet must be None"
        print(f"[{idx+1}] {pid}: {len(qs)} discrete questions")
    
    for q_idx, q in enumerate(qs):
        ch = q["ch"]
        a = q["a"]
        e = q["e"]
        
        assert len(ch) == 4, f"{pid} Q{q_idx+1} does not have 4 choices"
        assert a in [0, 1, 2, 3], f"{pid} Q{q_idx+1} invalid answer {a}"
        ans_dist[a] += 1
        
        assert "Distractor Traps:" in e, f"{pid} Q{q_idx+1} missing Distractor Traps"
        assert "<strong>" in e, f"{pid} Q{q_idx+1} missing <strong> topic rationale"
        
        if pid == "exam_bb90_3_disc":
            assert q.get("d") is True, f"{pid} Q{q_idx+1} missing d: True"
        
        lengths = [len(c) for c in ch]
        avg_l = sum(lengths) / 4.0
        diffs = [abs(l - avg_l) / avg_l for l in lengths]
        max_diff = max(diffs)
        
        if max_diff > 0.20:
            print(f"FAIL: {pid} Q{q_idx+1} length parity failed: max_diff={max_diff:.1%}, lengths={lengths}")
            all_passed = False

assert total_qs == 52, f"Total questions expected 52, found {total_qs}"
assert all_passed, "Some questions failed parity checks!"

print(f"\nAll 52 questions passed structural and length parity audits!")
print(f"Answer Key Distribution:")
for key in sorted(ans_dist.keys()):
    letter = chr(ord('A') + key)
    count = ans_dist[key]
    pct = count / total_qs * 100
    print(f"  Choice {letter} ({key}): {count} questions ({pct:.1f}%)")

# Write out exam_bb90_3.js
js_output = "/home/cgslinde/DrillRoom/DrillRoom/exam_bb90_3.js"
js_text = "/* ---- exam_bb90_3.js ---- */\n/* Full 90-minute Biochem/Bio Practice Exam 3: 7 passages (42 Qs) + 10 discrete Qs = 52 Qs */\nconst EXAM_BB90_3 = " + json.dumps(passages, indent=2) + ";\n"

with open(js_output, "w", encoding="utf-8") as f:
    f.write(js_text)

print(f"\nSuccessfully wrote production-ready exam to: {js_output}")
print(f"File size: {os.path.getsize(js_output)} bytes")
