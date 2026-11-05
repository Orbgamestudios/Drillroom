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
        print(f"Error: {filepath} does not exist yet.", file=sys.stderr)
        return None
    with open(filepath) as f:
        text = f.read()
    raw = text[text.find('['):text.rfind(']')+1]
    return json.loads(raw)

def assemble():
    print("Loading 90-min Exam 3 files...")
    cp90_3 = load_exam("/home/cgslinde/DrillRoom/DrillRoom/exam_cp90_3.js")
    bb90_3 = load_exam("/home/cgslinde/DrillRoom/DrillRoom/exam_bb90_3.js")
    cars90_3 = load_exam("/home/cgslinde/DrillRoom/DrillRoom/exam_cars90_3.js")
    ps90_3 = load_exam("/home/cgslinde/DrillRoom/DrillRoom/exam_ps90_3.js")

    if not (cp90_3 and bb90_3 and cars90_3 and ps90_3):
        print("Not all 90-min Exam 3 files are ready.", file=sys.stderr)
        return False

    # 1. EXAM_CP60_3 (5 Passages + 3 Discretes = 33 Questions)
    print("Assembling EXAM_CP60_3...")
    exam_cp60_3 = []
    q_counter = 1
    for p_idx in range(1, 6): # Passages 1 to 5
        src_p = cp90_3[p_idx - 1]
        n_qs = len(src_p["qs"])
        q_start = q_counter
        q_end = q_counter + n_qs - 1
        q_counter += n_qs
        
        clean_p = {
            "id": f"exam_cp60_3_p{p_idx}",
            "sec": "C/P",
            "topic": src_p["topic"],
            "sheet": p_idx,
            "label": "Chemical and Physical Foundations of Biological Systems",
            "examId": "cp60_3",
            "passage": renumber_passage(src_p["passage"], p_idx, q_start, q_end),
            "qs": src_p["qs"]
        }
        exam_cp60_3.append(clean_p)

    # 3 discretes from cp90_3 discretes
    cp_disc_src = cp90_3[7]["qs"][:3]
    exam_cp60_3.append({
        "id": "exam_cp60_3_disc",
        "sec": "C/P",
        "topic": "C/P Standalone Discrete Questions",
        "sheet": None,
        "label": "Chemical and Physical Foundations of Biological Systems",
        "examId": "cp60_3",
        "passage": "",
        "qs": cp_disc_src
    })
    total_cp = sum(len(s["qs"]) for s in exam_cp60_3)

    # 2. EXAM_BB60_3 (5 Passages + 3 Discretes = 33 Questions)
    print("Assembling EXAM_BB60_3...")
    exam_bb60_3 = []
    q_counter = 1
    for p_idx in range(1, 6): # Passages 1 to 5
        src_p = bb90_3[p_idx - 1]
        n_qs = len(src_p["qs"])
        q_start = q_counter
        q_end = q_counter + n_qs - 1
        q_counter += n_qs
        
        clean_p = {
            "id": f"exam_bb60_3_p{p_idx}",
            "sec": "B/B",
            "topic": src_p["topic"],
            "sheet": p_idx,
            "label": "Biological and Biochemical Foundations of Living Systems",
            "examId": "bb60_3",
            "passage": renumber_passage(src_p["passage"], p_idx, q_start, q_end),
            "qs": src_p["qs"]
        }
        exam_bb60_3.append(clean_p)

    bb_disc_src = bb90_3[7]["qs"][:3]
    exam_bb60_3.append({
        "id": "exam_bb60_3_disc",
        "sec": "B/B",
        "topic": "B/B Standalone Discrete Questions",
        "sheet": None,
        "label": "Biological and Biochemical Foundations of Living Systems",
        "examId": "bb60_3",
        "passage": "",
        "qs": bb_disc_src
    })
    total_bb = sum(len(s["qs"]) for s in exam_bb60_3)

    # 3. EXAM_CARS60_3 (Passages 1 to 5 + 3 Qs of Passage 6 = 33 Questions)
    print("Assembling EXAM_CARS60_3...")
    exam_cars60_3 = []
    q_counter = 1
    for p_idx in range(1, 6): # Passages 1 to 5
        src_p = cars90_3[p_idx - 1]
        n_qs = len(src_p["qs"])
        q_start = q_counter
        q_end = q_counter + n_qs - 1
        q_counter += n_qs
        
        clean_p = {
            "id": f"exam_cars60_3_p{p_idx}",
            "sec": "CARS",
            "topic": src_p["topic"],
            "sheet": None,
            "label": "Critical Analysis and Reasoning Skills",
            "examId": "cars60_3",
            "passage": renumber_passage(src_p["passage"], p_idx, q_start, q_end),
            "qs": src_p["qs"]
        }
        exam_cars60_3.append(clean_p)

    src_p6 = cars90_3[5]
    p6_qs = src_p6["qs"][:3]
    q_start = q_counter
    q_end = q_counter + len(p6_qs) - 1
    exam_cars60_3.append({
        "id": "exam_cars60_3_p6",
        "sec": "CARS",
        "topic": src_p6["topic"],
        "sheet": None,
        "label": "Critical Analysis and Reasoning Skills",
        "examId": "cars60_3",
        "passage": renumber_passage(src_p6["passage"], 6, q_start, q_end),
        "qs": p6_qs
    })
    total_cars = sum(len(s["qs"]) for s in exam_cars60_3)

    # 4. EXAM_PS60_3 (5 Passages + 3 Discretes = 33 Questions)
    print("Assembling EXAM_PS60_3...")
    exam_ps60_3 = []
    q_counter = 1
    for p_idx in range(1, 6): # Passages 1 to 5
        src_p = ps90_3[p_idx - 1]
        n_qs = len(src_p["qs"])
        q_start = q_counter
        q_end = q_counter + n_qs - 1
        q_counter += n_qs
        
        clean_p = {
            "id": f"exam_ps60_3_p{p_idx}",
            "sec": "P/S",
            "topic": src_p["topic"],
            "sheet": p_idx,
            "label": "Psychological, Social, and Biological Foundations of Behavior",
            "examId": "ps60_3",
            "passage": renumber_passage(src_p["passage"], p_idx, q_start, q_end),
            "qs": src_p["qs"]
        }
        exam_ps60_3.append(clean_p)

    ps_disc_src = ps90_3[7]["qs"][:3]
    exam_ps60_3.append({
        "id": "exam_ps60_3_disc",
        "sec": "P/S",
        "topic": "P/S Standalone Discrete Questions",
        "sheet": None,
        "label": "Psychological, Social, and Biological Foundations of Behavior",
        "examId": "ps60_3",
        "passage": "",
        "qs": ps_disc_src
    })
    total_ps = sum(len(s["qs"]) for s in exam_ps60_3)

    js_out = f"""/* ---- exam_60min_3.js ---- */
/* 60-minute practice sections for Exam 3 across all 4 MCAT subjects.
   CP60_3: {total_cp} Qs | BB60_3: {total_bb} Qs | CARS60_3: {total_cars} Qs | PS60_3: {total_ps} Qs */

const EXAM_CP60_3 = {json.dumps(exam_cp60_3, indent=2)};

const EXAM_BB60_3 = {json.dumps(exam_bb60_3, indent=2)};

const EXAM_CARS60_3 = {json.dumps(exam_cars60_3, indent=2)};

const EXAM_PS60_3 = {json.dumps(exam_ps60_3, indent=2)};
"""

    out_path = "/home/cgslinde/DrillRoom/DrillRoom/exam_60min_3.js"
    with open(out_path, "w") as f:
        f.write(js_out)
    print(f"Successfully generated {out_path} ({total_cp} CP, {total_bb} BB, {total_cars} CARS, {total_ps} PS)!")
    return True

if __name__ == "__main__":
    assemble()
