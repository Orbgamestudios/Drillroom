import re
import json
import copy
import subprocess

from p1 import passage_data as p1
from p2 import passage_data as p2
from p3 import passage_data as p3
from p4 import passage_data as p4
from p5 import passage_data as p5
from p6 import passage_data as p6
from p7 import passage_data as p7
from discretes import discrete_data as disc

def count_words(html_text):
    # remove ttl
    text = re.sub(r'<div class="ttl">.*?</div>', '', html_text, flags=re.DOTALL)
    # remove table
    text = re.sub(r'<table.*?</table>', '', text, flags=re.DOTALL)
    # remove other html tags
    text = re.sub(r'<.*?>', ' ', text)
    words = text.split()
    return len(words)

def validate_questions(questions, exam_name):
    letters = ["A", "B", "C", "D"]
    counts = {0: 0, 1: 0, 2: 0, 3: 0}
    
    for i, q in enumerate(questions):
        q_idx = i + 1
        ch = q["ch"]
        ans = q["a"]
        exp = q["e"]
        
        # 4 choices
        assert len(ch) == 4, f"{exam_name} Q{q_idx}: choices length is not 4"
        assert ans in [0, 1, 2, 3], f"{exam_name} Q{q_idx}: answer index invalid: {ans}"
        counts[ans] += 1
        
        # Length parity: max / min <= 1.25
        lens = [len(c) for c in ch]
        max_l = max(lens)
        min_l = min(lens)
        ratio = max_l / min_l
        if ratio > 1.25:
            raise AssertionError(f"{exam_name} Q{q_idx} failed length parity: max={max_l}, min={min_l}, ratio={ratio:.3f}\nChoices: {lens}\n{ch}")
        
        # Explanation format
        assert exp.startswith("<strong>"), f"{exam_name} Q{q_idx} explanation must start with <strong>"
        assert "<em>Distractor Traps:</em><br>" in exp, f"{exam_name} Q{q_idx} explanation missing Distractor Traps header"
        
        # Check bullets
        traps_part = exp.split("<em>Distractor Traps:</em><br>")[1]
        bullets = re.findall(r'&bull;\s+([A-D])\s+', traps_part)
        assert len(bullets) == 3, f"{exam_name} Q{q_idx} must have exactly 3 distractor bullets, found {len(bullets)}: {bullets}"
        
        expected_incorrect = [letters[k] for k in range(4) if k != ans]
        assert bullets == expected_incorrect, f"{exam_name} Q{q_idx} distractor bullets {bullets} do not match expected {expected_incorrect}"
        
    return counts

def main():
    passages_90 = [p1, p2, p3, p4, p5, p6, p7]
    
    # 1. Check passages
    for i, p in enumerate(passages_90):
        p_num = i + 1
        words = count_words(p["passage"])
        print(f"Passage {p_num} prose word count: {words}")
        assert 200 <= words <= 380, f"Passage {p_num} word count out of bounds: {words}"
        assert len(p["qs"]) == 6, f"Passage {p_num} must have exactly 6 questions"
    
    assert len(disc["qs"]) == 10, "Discrete set must have exactly 10 questions"
    
    # Collect all questions for 90m
    all_qs_90 = []
    for p in passages_90:
        all_qs_90.extend(p["qs"])
    all_qs_90.extend(disc["qs"])
    
    assert len(all_qs_90) == 52, f"Total 90m questions must be 52, got {len(all_qs_90)}"
    
    # Validate 90m questions
    counts_90 = validate_questions(all_qs_90, "90-minute Exam")
    print(f"90m Answer Distribution: A={counts_90[0]}, B={counts_90[1]}, C={counts_90[2]}, D={counts_90[3]}")
    assert counts_90[0] == 13, f"A count != 13: {counts_90[0]}"
    assert counts_90[1] == 13, f"B count != 13: {counts_90[1]}"
    assert counts_90[2] == 13, f"C count != 13: {counts_90[2]}"
    assert counts_90[3] == 13, f"D count != 13: {counts_90[3]}"
    
    # Build 60m exam
    passages_60 = []
    for i in range(5):
        p_copy = copy.deepcopy(passages_90[i])
        p_copy["id"] = f"exam_bb60_7_p{i+1}"
        p_copy["examId"] = "bb60_7"
        passages_60.append(p_copy)
    
    disc_60 = copy.deepcopy(disc)
    disc_60["id"] = "exam_bb60_7_disc"
    disc_60["examId"] = "bb60_7"
    disc_60["sheet"] = 8
    disc_60["passage"] = "<div class=\"ttl\">Item Set (Questions 31&ndash;33)</div>\n<p><strong>Directions:</strong> Questions 31&ndash;33 are standalone questions that are not based on a passage. Select the single best answer to each question.</p>"
    disc_60["qs"] = copy.deepcopy(disc["qs"][:3])
    
    all_qs_60 = []
    for p in passages_60:
        all_qs_60.extend(p["qs"])
    all_qs_60.extend(disc_60["qs"])
    
    assert len(all_qs_60) == 33, f"Total 60m questions must be 33, got {len(all_qs_60)}"
    
    counts_60 = validate_questions(all_qs_60, "60-minute Exam")
    print(f"60m Answer Distribution: A={counts_60[0]}, B={counts_60[1]}, C={counts_60[2]}, D={counts_60[3]}")
    assert counts_60[0] == 8, f"60m A count != 8: {counts_60[0]}"
    assert counts_60[1] == 8, f"60m B count != 8: {counts_60[1]}"
    assert counts_60[2] == 9, f"60m C count != 9: {counts_60[2]}"
    assert counts_60[3] == 8, f"60m D count != 8: {counts_60[3]}"
    
    # 2. Write out exam_bb90_7.js
    exam_bb90_7_data = passages_90 + [disc]
    js_content_90 = (
        "/* ---- exam_bb90_7.js ---- */\n"
        "/* Full 90-minute Biochem/Bio Practice Exam 7: 7 passages (42 Qs) + 10 discrete Qs = 52 Qs */\n"
        "const EXAM_BB90_7 = " + json.dumps(exam_bb90_7_data, indent=2) + ";\n\n"
        "if (typeof window !== 'undefined') {\n"
        "  window.EXAM_BB90_7 = EXAM_BB90_7;\n"
        "}\n"
        "if (typeof globalThis !== 'undefined') {\n"
        "  globalThis.EXAM_BB90_7 = EXAM_BB90_7;\n"
        "}\n"
    )
    
    bb90_path = "/home/cgslinde/DrillRoom/DrillRoom/exam_bb90_7.js"
    with open(bb90_path, "w", encoding="utf-8") as f:
        f.write(js_content_90)
    print(f"Wrote {bb90_path}")
    
    # 3. Write out exam_bb60_7.js
    exam_bb60_7_data = passages_60 + [disc_60]
    js_content_60 = (
        "/* ---- exam_bb60_7.js ---- */\n"
        "/* 60-minute Biochem/Bio Practice Exam 7: 5 passages (30 Qs) + 3 discrete Qs = 33 Qs */\n"
        "const EXAM_BB60_7 = " + json.dumps(exam_bb60_7_data, indent=2) + ";\n\n"
        "if (typeof window !== 'undefined') {\n"
        "  window.EXAM_BB60_7 = EXAM_BB60_7;\n"
        "}\n"
        "if (typeof globalThis !== 'undefined') {\n"
        "  globalThis.EXAM_BB60_7 = EXAM_BB60_7;\n"
        "}\n"
    )
    
    bb60_path = "/home/cgslinde/DrillRoom/DrillRoom/exam_bb60_7.js"
    with open(bb60_path, "w", encoding="utf-8") as f:
        f.write(js_content_60)
    print(f"Wrote {bb60_path}")
    
    # 4. Check with node
    for pth in [bb90_path, bb60_path]:
        res = subprocess.run(["/home/cgslinde/node-v24.22.0-linux-x64/bin/node", "-c", pth], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"Node syntax check failed for {pth}:")
            print(res.stderr)
            exit(1)
        else:
            print(f"Node syntax check PASSED for {pth}")

if __name__ == "__main__":
    main()
