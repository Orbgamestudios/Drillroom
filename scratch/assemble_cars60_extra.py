import json
import re
import os
import sys

def renumber_passage(passage_html, p_num, q_start, q_end):
    new_header = f'<div class="ttl">Passage {p_num} (Questions {q_start}&ndash;{q_end})</div>'
    if '<div class="ttl">' in passage_html:
        return re.sub(r'<div class="ttl">.*?</div>', new_header, passage_html, count=1)
    else:
        return new_header + "\n" + passage_html

def load_exam(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath) as f:
        text = f.read()
    raw = text[text.find('['):text.rfind(']')+1]
    return json.loads(raw)

def build_cars60(exam_num):
    src_file = f"/home/cgslinde/DrillRoom/DrillRoom/exam_cars90_{exam_num}.js"
    out_file = f"/home/cgslinde/DrillRoom/DrillRoom/exam_cars60_{exam_num}.js"
    
    cars90 = load_exam(src_file)
    if not cars90 or len(cars90) < 6:
        print(f"Cannot build cars60_{exam_num}: {src_file} not ready or insufficient passages.", file=sys.stderr)
        return False

    exam_cars60 = []
    q_counter = 1

    # Passages 1 to 5 (6 Qs each = 30 Qs)
    for p_idx in range(1, 6):
        src_p = cars90[p_idx - 1]
        n_qs = len(src_p["qs"])
        q_start = q_counter
        q_end = q_counter + n_qs - 1
        q_counter += n_qs
        
        clean_p = {
            "id": f"exam_cars60_{exam_num}_p{p_idx}",
            "sec": "CARS",
            "topic": src_p["topic"],
            "sheet": None,
            "label": "Critical Analysis and Reasoning Skills",
            "examId": f"cars60_{exam_num}",
            "passage": renumber_passage(src_p["passage"], p_idx, q_start, q_end),
            "qs": src_p["qs"]
        }
        exam_cars60.append(clean_p)

    # Passage 6 (first 3 questions = 3 Qs)
    src_p6 = cars90[5]
    p6_qs = src_p6["qs"][:3]
    q_start = q_counter
    q_end = q_counter + len(p6_qs) - 1
    exam_cars60.append({
        "id": f"exam_cars60_{exam_num}_p6",
        "sec": "CARS",
        "topic": src_p6["topic"],
        "sheet": None,
        "label": "Critical Analysis and Reasoning Skills",
        "examId": f"cars60_{exam_num}",
        "passage": renumber_passage(src_p6["passage"], 6, q_start, q_end),
        "qs": p6_qs
    })

    total_qs = sum(len(s["qs"]) for s in exam_cars60)
    assert total_qs == 33, f"Expected 33 questions, got {total_qs}"

    js_out = f"""/* ---- exam_cars60_{exam_num}.js ---- */
/* 60-minute CARS Practice Exam {exam_num}: 6 passages (33 Qs) */

const EXAM_CARS60_{exam_num} = {json.dumps(exam_cars60, indent=2)};
"""

    with open(out_file, "w") as f:
        f.write(js_out)
    print(f"Successfully generated {out_file} (33 questions across 6 passages)!")
    return True

def main():
    nums = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else [4, 5, 6, 7, 8, 9]
    for num in nums:
        build_cars60(num)

if __name__ == "__main__":
    main()
