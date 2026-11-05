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
        print(f"Error: {filepath} does not exist.", file=sys.stderr)
        return None
    with open(filepath) as f:
        text = f.read()
    raw = text[text.find('['):text.rfind(']')+1]
    return json.loads(raw)

def build_science60(sec_code, sec_name, label, exam_num):
    # sec_code: 'cp', 'bb', 'ps'
    # sec_name: 'C/P', 'B/B', 'P/S'
    src_file = f"/home/cgslinde/DrillRoom/DrillRoom/exam_{sec_code}90_{exam_num}.js"
    out_file = f"/home/cgslinde/DrillRoom/DrillRoom/exam_{sec_code}60_{exam_num}.js"
    
    data90 = load_exam(src_file)
    if not data90 or len(data90) < 8:
        print(f"Cannot build {sec_code}60_{exam_num}: {src_file} invalid or incomplete.", file=sys.stderr)
        return False

    exam60 = []
    q_counter = 1

    # Passages 1 to 5 (6 Qs each = 30 Qs)
    for p_idx in range(1, 6):
        src_p = data90[p_idx - 1]
        n_qs = len(src_p["qs"])
        q_start = q_counter
        q_end = q_counter + n_qs - 1
        q_counter += n_qs
        clean_p = {
            "id": f"exam_{sec_code}60_{exam_num}_p{p_idx}",
            "sec": sec_name,
            "topic": src_p["topic"],
            "sheet": p_idx if sec_code == "cp" else None,
            "label": label,
            "examId": f"{sec_code}60_{exam_num}",
            "passage": renumber_passage(src_p["passage"], p_idx, q_start, q_end),
            "qs": src_p["qs"]
        }
        exam60.append(clean_p)

    # Discrete set (3 Qs)
    disc_src = data90[7]["qs"][:3]
    exam60.append({
        "id": f"exam_{sec_code}60_{exam_num}_disc",
        "sec": sec_name,
        "topic": f"{sec_name} Standalone Discrete Questions",
        "sheet": None,
        "label": label,
        "examId": f"{sec_code}60_{exam_num}",
        "passage": "",
        "qs": disc_src
    })

    total_qs = sum(len(s["qs"]) for s in exam60)
    assert total_qs == 33, f"Expected 33 questions, got {total_qs}"

    var_name = f"EXAM_{sec_code.upper()}60_{exam_num}"
    js_out = f"""/* ---- exam_{sec_code}60_{exam_num}.js ---- */
/* 60-minute {sec_name} Practice Exam {exam_num}: 5 passages + 3 discrete (33 Qs) */

const {var_name} = {json.dumps(exam60, indent=2)};
"""

    with open(out_file, "w") as f:
        f.write(js_out)
    print(f"Successfully generated {out_file} (33 questions across 6 sets)!")
    return True

def main():
    nums = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else [4, 5]
    configs = [
        ("cp", "C/P", "Chemical and Physical Foundations of Biological Systems"),
        ("bb", "B/B", "Biological and Biochemical Foundations of Living Systems"),
        ("ps", "P/S", "Psychological, Social, and Biological Foundations of Behavior")
    ]
    for num in nums:
        for sec_code, sec_name, label in configs:
            src = f"/home/cgslinde/DrillRoom/DrillRoom/exam_{sec_code}90_{num}.js"
            if os.path.exists(src):
                build_science60(sec_code, sec_name, label, num)

if __name__ == "__main__":
    main()
