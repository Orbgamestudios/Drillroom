import json, re

def renumber_passage(passage_html, p_num, q_start, q_end):
    new_header = f'<div class="ttl">Passage {p_num} (Questions {q_start}&ndash;{q_end})</div>'
    if '<div class="ttl">' in passage_html:
        return re.sub(r'<div class="ttl">.*?</div>', new_header, passage_html, count=1)
    else:
        return new_header + "\n" + passage_html

def load_exam(filepath):
    with open(filepath) as f:
        text = f.read()
    raw = text[text.find('['):text.rfind(']')+1]
    return json.loads(raw)

print("Loading upgraded 90-min Suite 1 files...")
cp90 = load_exam("/home/cgslinde/DrillRoom/DrillRoom/exam_cp90.js")
bb90 = load_exam("/home/cgslinde/DrillRoom/DrillRoom/exam_bb90.js")
cars90 = load_exam("/home/cgslinde/DrillRoom/DrillRoom/exam_cars90.js")
ps90 = load_exam("/home/cgslinde/DrillRoom/DrillRoom/exam_ps90.js")

# ==============================================================================
# 1. EXAM_CP60 (5 Passages [30 Qs] + 3 Discretes = 33 Qs)
# ==============================================================================
print("Assembling EXAM_CP60...")
exam_cp60 = []
q_counter = 1
for p_idx in range(1, 6): # Passages 1 to 5
    src_p = cp90[p_idx - 1]
    n_qs = len(src_p["qs"])
    q_start = q_counter
    q_end = q_counter + n_qs - 1
    q_counter += n_qs
    
    clean_p = {
        "id": f"exam_cp60_p{p_idx}",
        "sec": "C/P",
        "topic": src_p["topic"],
        "sheet": p_idx,
        "label": "Chemical and Physical Foundations of Biological Systems",
        "examId": "cp60",
        "passage": renumber_passage(src_p["passage"], p_idx, q_start, q_end),
        "qs": src_p["qs"]
    }
    exam_cp60.append(clean_p)

# Discretes: first 3 from cp90
cp_disc_src = cp90[7]["qs"][:3]
exam_cp60.append({
    "id": "exam_cp60_disc",
    "sec": "C/P",
    "topic": "C/P Standalone Discrete Questions",
    "sheet": None,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60",
    "passage": "",
    "qs": cp_disc_src
})

# ==============================================================================
# 2. EXAM_BB60 (5 Passages [30 Qs] + 3 Discretes = 33 Qs)
# ==============================================================================
print("Assembling EXAM_BB60...")
exam_bb60 = []
q_counter = 1
for p_idx in range(1, 6): # Passages 1 to 5
    src_p = bb90[p_idx - 1]
    n_qs = len(src_p["qs"])
    q_start = q_counter
    q_end = q_counter + n_qs - 1
    q_counter += n_qs
    
    clean_p = {
        "id": f"exam_bb60_p{p_idx}",
        "sec": "B/B",
        "topic": src_p["topic"],
        "sheet": p_idx,
        "label": "Biological and Biochemical Foundations of Living Systems",
        "examId": "bb60",
        "passage": renumber_passage(src_p["passage"], p_idx, q_start, q_end),
        "qs": src_p["qs"]
    }
    exam_bb60.append(clean_p)

bb_disc_src = bb90[7]["qs"][:3]
exam_bb60.append({
    "id": "exam_bb60_disc",
    "sec": "B/B",
    "topic": "B/B Standalone Discrete Questions",
    "sheet": None,
    "label": "Biological and Biochemical Foundations of Living Systems",
    "examId": "bb60",
    "passage": "",
    "qs": bb_disc_src
})

# ==============================================================================
# 3. EXAM_CARS60 (6 Passages = 33 Qs: Passages 1-5 [30 Qs] + first 3 Qs of Passage 6)
# ==============================================================================
print("Assembling EXAM_CARS60...")
exam_cars60 = []
q_counter = 1
for p_idx in range(1, 6): # Passages 1 to 5
    src_p = cars90[p_idx - 1]
    n_qs = len(src_p["qs"])
    q_start = q_counter
    q_end = q_counter + n_qs - 1
    q_counter += n_qs
    
    clean_p = {
        "id": f"exam_cars60_p{p_idx}",
        "sec": "CARS",
        "topic": src_p["topic"],
        "sheet": p_idx,
        "label": "Critical Analysis and Reasoning Skills",
        "examId": "cars60",
        "passage": renumber_passage(src_p["passage"], p_idx, q_start, q_end),
        "qs": src_p["qs"]
    }
    exam_cars60.append(clean_p)

# Passage 6 (take first 3 Qs to reach exactly 33 Qs)
src_p6 = cars90[5]
p6_qs = src_p6["qs"][:3]
q_start = q_counter
q_end = q_counter + len(p6_qs) - 1
exam_cars60.append({
    "id": "exam_cars60_p6",
    "sec": "CARS",
    "topic": src_p6["topic"],
    "sheet": 6,
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars60",
    "passage": renumber_passage(src_p6["passage"], 6, q_start, q_end),
    "qs": p6_qs
})

# ==============================================================================
# 4. EXAM_PS60 (5 Passages [30 Qs] + 3 Discretes = 33 Qs)
# ==============================================================================
print("Assembling EXAM_PS60...")
exam_ps60 = []
q_counter = 1
for p_idx in range(1, 6): # Passages 1 to 5
    src_p = ps90[p_idx - 1]
    n_qs = len(src_p["qs"])
    q_start = q_counter
    q_end = q_counter + n_qs - 1
    q_counter += n_qs
    
    clean_p = {
        "id": f"exam_ps60_p{p_idx}",
        "sec": "P/S",
        "topic": src_p["topic"],
        "sheet": p_idx,
        "label": "Psychological, Social, and Biological Foundations of Behavior",
        "examId": "ps60",
        "passage": renumber_passage(src_p["passage"], p_idx, q_start, q_end),
        "qs": src_p["qs"]
    }
    exam_ps60.append(clean_p)

ps_disc_src = ps90[7]["qs"][:3]
exam_ps60.append({
    "id": "exam_ps60_disc",
    "sec": "P/S",
    "topic": "P/S Standalone Discrete Questions",
    "sheet": None,
    "label": "Psychological, Social, and Biological Foundations of Behavior",
    "examId": "ps60",
    "passage": "",
    "qs": ps_disc_src
})

# Build output JS
js_out = f"""/* ---- exam_60min.js ---- */
/* 60-minute practice sections for all 4 MCAT subjects (Suite 1).
   CP60: 33 Qs | BB60: 33 Qs | CARS60: 33 Qs | PS60: 33 Qs
   Fully upgraded to 5-Gate Review Protocol (5/5 Crucible Standard). */

const EXAM_CP60 = {json.dumps(exam_cp60, indent=2)};

const EXAM_BB60 = {json.dumps(exam_bb60, indent=2)};

const EXAM_CARS60 = {json.dumps(exam_cars60, indent=2)};

const EXAM_PS60 = {json.dumps(exam_ps60, indent=2)};
"""

with open("/home/cgslinde/DrillRoom/DrillRoom/exam_60min.js", "w") as f:
    f.write(js_out)

print("exam_60min.js successfully synchronized and written!")
