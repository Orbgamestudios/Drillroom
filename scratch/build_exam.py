#!/usr/bin/env python3
"""
Build script to compile exam_cp90_3.js from modular passage files.
"""
import os
import sys
import json
import re

# Add scratch/cp_passages to python path
cur_dir = os.path.dirname(os.path.abspath(__file__))
passages_dir = os.path.join(cur_dir, "cp_passages")
sys.path.insert(0, passages_dir)

from p1 import passage_data as p1
from p2 import passage_data as p2
from p3 import passage_data as p3
from p4 import passage_data as p4
from p5 import passage_data as p5
from p6 import passage_data as p6
from p7 import passage_data as p7
from discretes import discrete_data as disc

def main():
    passages = [p1, p2, p3, p4, p5, p6, p7, disc]
    
    # Validation checks
    assert len(passages) == 8, f"Expected 8 passage sets, got {len(passages)}"
    
    total_qs = 0
    total_passage_qs = 0
    total_disc_qs = 0
    
    for idx, p in enumerate(passages[:7]):
        assert p["sec"] == "C/P"
        assert p["label"] == "Chemical and Physical Foundations of Biological Systems"
        assert p["examId"] == "cp90_3"
        assert p["sheet"] == idx + 1, f"Expected sheet {idx+1}, got {p['sheet']}"
        assert p["id"] == f"exam_cp90_3_p{idx+1}"
        assert "<table class=\"tbl\">" in p["passage"], f"Passage {idx+1} missing table"
        
        # Word count
        clean = re.sub(r'<[^>]+>', ' ', p["passage"])
        wc = len(clean.split())
        print(f"Passage {idx+1} word count: {wc}")
        assert 200 <= wc <= 400, f"Passage {idx+1} word count out of bounds: {wc}"
        
        # Questions
        assert len(p["qs"]) == 6, f"Passage {idx+1} has {len(p['qs'])} questions (expected 6)"
        for q_idx, q in enumerate(p["qs"]):
            total_qs += 1
            total_passage_qs += 1
            assert len(q["ch"]) == 4, f"P{idx+1} Q{q_idx+1} does not have 4 choices"
            assert q["a"] in [0, 1, 2, 3], f"P{idx+1} Q{q_idx+1} invalid answer index"
            assert "Distractor Traps:" in q["e"], f"P{idx+1} Q{q_idx+1} missing Distractor Traps"
            lens = [len(c) for c in q["ch"]]
            avg = sum(lens) / 4.0
            max_dev = max(abs(l - avg) / avg for l in lens)
            assert max_dev <= 0.25, f"P{idx+1} Q{q_idx+1} length parity failed: {max_dev:.2%}"

    # Discretes
    assert disc["sec"] == "C/P"
    assert disc["label"] == "Chemical and Physical Foundations of Biological Systems"
    assert disc["examId"] == "cp90_3"
    assert disc["sheet"] is None
    assert disc["id"] == "exam_cp90_3_disc"
    assert len(disc["qs"]) == 10, f"Discretes has {len(disc['qs'])} questions (expected 10)"
    
    for q_idx, q in enumerate(disc["qs"]):
        total_qs += 1
        total_disc_qs += 1
        assert len(q["ch"]) == 4, f"Discrete Q{q_idx+1} does not have 4 choices"
        assert q["a"] in [0, 1, 2, 3], f"Discrete Q{q_idx+1} invalid answer index"
        assert q.get("d") is True, f"Discrete Q{q_idx+1} missing d: True"
        assert "Distractor Traps:" in q["e"], f"Discrete Q{q_idx+1} missing Distractor Traps"
        lens = [len(c) for c in q["ch"]]
        avg = sum(lens) / 4.0
        max_dev = max(abs(l - avg) / avg for l in lens)
        assert max_dev <= 0.25, f"Discrete Q{q_idx+1} length parity failed: {max_dev:.2%}"

    print(f"Total questions validated: {total_qs} (Passage: {total_passage_qs}, Discretes: {total_disc_qs})")
    assert total_qs == 52, f"Expected 52 total questions, got {total_qs}"

    # Export to exam_cp90_3.js
    output_path = "/home/cgslinde/DrillRoom/DrillRoom/exam_cp90_3.js"
    js_content = "/* ---- exam_cp90_3.js ---- */\n"
    js_content += "/* Full 90-minute Chem/Phys Practice Exam 3: 7 passages (42 Qs) + 10 discrete Qs = 52 Qs */\n"
    js_content += "const EXAM_CP90_3 = "
    js_content += json.dumps(passages, indent=2, ensure_ascii=False)
    js_content += ";\n"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    
    print(f"Wrote {len(js_content)} characters to {output_path}")

if __name__ == "__main__":
    main()
