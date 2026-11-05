import json
import re

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

print("Loading 90-min Exam 2 files...")
cp90_2 = load_exam("/home/cgslinde/DrillRoom/DrillRoom/exam_cp90_2.js")
bb90_2 = load_exam("/home/cgslinde/DrillRoom/DrillRoom/exam_bb90_2.js")
cars90_2 = load_exam("/home/cgslinde/DrillRoom/DrillRoom/exam_cars90_2.js")
ps90_2 = load_exam("/home/cgslinde/DrillRoom/DrillRoom/exam_ps90_2.js")

# ==============================================================================
# 1. EXAM_CP60_2 (5 Passages + 3 Discretes = 33 Questions)
# ==============================================================================
print("Assembling EXAM_CP60_2...")
exam_cp60_2 = []
q_counter = 1
for p_idx in range(1, 6): # Passages 1 to 5
    src_p = cp90_2[p_idx - 1]
    n_qs = len(src_p["qs"])
    q_start = q_counter
    q_end = q_counter + n_qs - 1
    q_counter += n_qs
    
    clean_p = {
        "id": f"exam_cp60_2_p{p_idx}",
        "sec": "C/P",
        "topic": src_p["topic"],
        "sheet": p_idx,
        "label": "Chemical and Physical Foundations of Biological Systems",
        "examId": "cp60_2",
        "passage": renumber_passage(src_p["passage"], p_idx, q_start, q_end),
        "qs": src_p["qs"]
    }
    exam_cp60_2.append(clean_p)

# Add 3 discretes from cp90_2 discretes (first 3 discretes: Calorimetry, Osmotic pressure, Capacitance)
cp_disc_src = cp90_2[7]["qs"][:3]
exam_cp60_2.append({
    "id": "exam_cp60_2_disc",
    "sec": "C/P",
    "topic": "C/P Standalone Discrete Questions",
    "sheet": None,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_2",
    "passage": "",
    "qs": cp_disc_src
})

total_cp60_2_qs = sum(len(s["qs"]) for s in exam_cp60_2)
print(f"EXAM_CP60_2 assembled: {len(exam_cp60_2)} sets, {total_cp60_2_qs} questions")

# ==============================================================================
# 2. EXAM_BB60_2 (5 Passages + 3 Discretes = 33 Questions)
# ==============================================================================
print("Assembling EXAM_BB60_2...")
exam_bb60_2 = []
q_counter = 1
for p_idx in range(1, 6): # Passages 1 to 5
    src_p = bb90_2[p_idx - 1]
    n_qs = len(src_p["qs"])
    q_start = q_counter
    q_end = q_counter + n_qs - 1
    q_counter += n_qs
    
    clean_p = {
        "id": f"exam_bb60_2_p{p_idx}",
        "sec": "B/B",
        "topic": src_p["topic"],
        "sheet": p_idx,
        "label": "Biological and Biochemical Foundations of Living Systems",
        "examId": "bb60_2",
        "passage": renumber_passage(src_p["passage"], p_idx, q_start, q_end),
        "qs": src_p["qs"]
    }
    exam_bb60_2.append(clean_p)

bb_disc_src = bb90_2[7]["qs"][:3]
exam_bb60_2.append({
    "id": "exam_bb60_2_disc",
    "sec": "B/B",
    "topic": "B/B Standalone Discrete Questions",
    "sheet": None,
    "label": "Biological and Biochemical Foundations of Living Systems",
    "examId": "bb60_2",
    "passage": "",
    "qs": bb_disc_src
})

total_bb60_2_qs = sum(len(s["qs"]) for s in exam_bb60_2)
print(f"EXAM_BB60_2 assembled: {len(exam_bb60_2)} sets, {total_bb60_2_qs} questions")

# ==============================================================================
# 3. EXAM_CARS60_2 (Passages 1 to 6 = 33 Questions: 5 full + 1 with 3 Qs, or 6 passages)
# Let's take Passages 1 to 5 (6 Qs each = 30 Qs) + first 3 Qs of Passage 6 = 33 Questions
# ==============================================================================
print("Assembling EXAM_CARS60_2...")
exam_cars60_2 = []
q_counter = 1
for p_idx in range(1, 6): # Passages 1 to 5
    src_p = cars90_2[p_idx - 1]
    n_qs = len(src_p["qs"])
    q_start = q_counter
    q_end = q_counter + n_qs - 1
    q_counter += n_qs
    
    clean_p = {
        "id": f"exam_cars60_2_p{p_idx}",
        "sec": "CARS",
        "topic": src_p["topic"],
        "sheet": None,
        "label": "Critical Analysis and Reasoning Skills",
        "examId": "cars60_2",
        "passage": renumber_passage(src_p["passage"], p_idx, q_start, q_end),
        "qs": src_p["qs"]
    }
    exam_cars60_2.append(clean_p)

# Passage 6 (take first 3 questions for exactly 33 questions)
src_p6 = cars90_2[5]
p6_qs = src_p6["qs"][:3]
q_start = q_counter
q_end = q_counter + len(p6_qs) - 1
exam_cars60_2.append({
    "id": "exam_cars60_2_p6",
    "sec": "CARS",
    "topic": src_p6["topic"],
    "sheet": None,
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars60_2",
    "passage": renumber_passage(src_p6["passage"], 6, q_start, q_end),
    "qs": p6_qs
})

total_cars60_2_qs = sum(len(s["qs"]) for s in exam_cars60_2)
print(f"EXAM_CARS60_2 assembled: {len(exam_cars60_2)} sets, {total_cars60_2_qs} questions")

# ==============================================================================
# 4. EXAM_PS60_2 (5 Passages + 3 Discretes = 33 Questions)
# ==============================================================================
print("Assembling EXAM_PS60_2...")
exam_ps60_2 = []
q_counter = 1
for p_idx in range(1, 6): # Passages 1 to 5
    src_p = ps90_2[p_idx - 1]
    n_qs = len(src_p["qs"])
    q_start = q_counter
    q_end = q_counter + n_qs - 1
    q_counter += n_qs
    
    clean_p = {
        "id": f"exam_ps60_2_p{p_idx}",
        "sec": "P/S",
        "topic": src_p["topic"],
        "sheet": p_idx,
        "label": "Psychological, Social, and Biological Foundations of Behavior",
        "examId": "ps60_2",
        "passage": renumber_passage(src_p["passage"], p_idx, q_start, q_end),
        "qs": src_p["qs"]
    }
    exam_ps60_2.append(clean_p)

ps_disc_src = ps90_2[7]["qs"][:3]
exam_ps60_2.append({
    "id": "exam_ps60_2_disc",
    "sec": "P/S",
    "topic": "P/S Standalone Discrete Questions",
    "sheet": None,
    "label": "Psychological, Social, and Biological Foundations of Behavior",
    "examId": "ps60_2",
    "passage": "",
    "qs": ps_disc_src
})

total_ps60_2_qs = sum(len(s["qs"]) for s in exam_ps60_2)
print(f"EXAM_PS60_2 assembled: {len(exam_ps60_2)} sets, {total_ps60_2_qs} questions")

# ==============================================================================
# Write to /home/cgslinde/DrillRoom/DrillRoom/exam_60min_2.js
# ==============================================================================
js_out = f"""/* ---- exam_60min_2.js ---- */
/* 60-minute practice sections for Exam 2 across all 4 MCAT subjects.
   CP60_2: {total_cp60_2_qs} Qs | BB60_2: {total_bb60_2_qs} Qs | CARS60_2: {total_cars60_2_qs} Qs | PS60_2: {total_ps60_2_qs} Qs */

const EXAM_CP60_2 = {json.dumps(exam_cp60_2, indent=2)};

const EXAM_BB60_2 = {json.dumps(exam_bb60_2, indent=2)};

const EXAM_CARS60_2 = {json.dumps(exam_cars60_2, indent=2)};

const EXAM_PS60_2 = {json.dumps(exam_ps60_2, indent=2)};
"""

with open("/home/cgslinde/DrillRoom/DrillRoom/exam_60min_2.js", "w") as f:
    f.write(js_out)

print("exam_60min_2.js generated and written successfully!")
