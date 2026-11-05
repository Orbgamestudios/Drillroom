import re, json, sys

with open("/home/cgslinde/DrillRoom/DrillRoom/DrillRoom.html") as f:
    html = f.read()

scripts = re.findall(r"<script>(.*?)</script>", html, re.DOTALL)

# Import JSObjectParser
sys.path.append("/home/cgslinde/DrillRoom/DrillRoom/scratch")
from parse_cars import JSObjectParser, parse_set_at

# Helper to find set across all scripts in DrillRoom.html
def find_set(sid):
    for i, s in enumerate(scripts):
        if f'"{sid}"' in s or f"'{sid}'" in s:
            try:
                obj = parse_set_at(s, sid)
                return obj
            except Exception as e:
                pass
    raise ValueError(f"Could not find {sid} in any script block")

# Helper to load JSON/JS array from exam files
def load_exam_file(filepath):
    with open(filepath) as f:
        text = f.read()
    raw = text[text.find('['):text.rfind(']')+1]
    return json.loads(raw)

# Helper to update passage header
def renumber_passage(passage_html, p_num, q_start, q_end):
    new_header = f'<div class="ttl">Passage {p_num} (Questions {q_start}&ndash;{q_end})</div>'
    if '<div class="ttl">' in passage_html:
        return re.sub(r'<div class="ttl">.*?</div>', new_header, passage_html, count=1)
    else:
        return new_header + "\n" + passage_html

print("Loading base exam files...")
cp90 = load_exam_file("/home/cgslinde/DrillRoom/DrillRoom/exam_cp90.js")
bb90 = load_exam_file("/home/cgslinde/DrillRoom/DrillRoom/exam_bb90.js")
ps90 = load_exam_file("/home/cgslinde/DrillRoom/DrillRoom/exam_ps90.js")

# ==============================================================================
# 1. EXAM_CP60 (5 Passages + 5 Discretes)
# ==============================================================================
print("Assembling EXAM_CP60...")
# Passages from DrillRoom: cp_acid (take first 5 Qs), cp_kin (first 5 Qs), cp_phys (6 Qs)
s_cp_acid = find_set("cp_acid")
s_cp_acid["qs"] = s_cp_acid["qs"][:5]

s_cp_kin = find_set("cp_kin")
s_cp_kin["qs"] = s_cp_kin["qs"][:5]

s_cp_phys = find_set("cp_phys")
s_cp_phys["qs"] = s_cp_phys["qs"][:6]

# Passages from cp90: Passage 4 (6 Qs) and Passage 7 (6 Qs)
s_cp_p4 = cp90[3] # electrochemical cells
s_cp_p7 = cp90[6] # cisplatin kinetics

# Discretes: 5 Qs from cp90 discretes
cp_discretes = {
    "id": "exam_cp60_disc",
    "sec": "C/P",
    "topic": "C/P Standalone Discrete Questions",
    "sheet": None,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60",
    "passage": "",
    "qs": cp90[7]["qs"][:5]
}

cp60_raw_passages = [
    (s_cp_acid, "Acid-base equilibria and physiologic buffers"),
    (s_cp_kin, "Reaction kinetics, catalysis, and thermodynamics"),
    (s_cp_phys, "Fluids and electrical circuit dynamics"),
    (s_cp_p4, s_cp_p4["topic"]),
    (s_cp_p7, s_cp_p7["topic"]),
]

exam_cp60 = []
q_counter = 1
for p_idx, (p_set, topic) in enumerate(cp60_raw_passages, 1):
    n_qs = len(p_set["qs"])
    q_start = q_counter
    q_end = q_counter + n_qs - 1
    q_counter += n_qs
    
    clean_p = {
        "id": f"exam_cp60_p{p_idx}",
        "sec": "C/P",
        "topic": topic,
        "sheet": p_set.get("sheet", p_idx),
        "label": "Chemical and Physical Foundations of Biological Systems",
        "examId": "cp60",
        "passage": renumber_passage(p_set["passage"], p_idx, q_start, q_end),
        "qs": p_set["qs"]
    }
    exam_cp60.append(clean_p)

exam_cp60.append(cp_discretes)
total_cp60_qs = sum(len(s["qs"]) for s in exam_cp60)
print(f"EXAM_CP60 assembled: {len(exam_cp60)} sets, {total_cp60_qs} questions")

# ==============================================================================
# 2. EXAM_BB60 (5 Passages + 5 Discretes)
# ==============================================================================
print("Assembling EXAM_BB60...")
s_bb_renal = find_set("bb_renal")
s_bb_cv = find_set("bb_cv")
s_bb_resp = find_set("bb_resp")
s_bb_enz = find_set("bb_enz")
s_bb_enz["qs"] = s_bb_enz["qs"][:5] # keep 5 passage Qs
s_bb_endo = find_set("bb_endo")
s_bb_endo["qs"] = s_bb_endo["qs"][:5] # keep 5 passage Qs

bb_discretes = {
    "id": "exam_bb60_disc",
    "sec": "B/B",
    "topic": "B/B Standalone Discrete Questions",
    "sheet": None,
    "label": "Biological and Biochemical Foundations of Living Systems",
    "examId": "bb60",
    "passage": "",
    "qs": bb90[7]["qs"][:5]
}

bb60_raw_passages = [
    (s_bb_renal, "Renal concentrating mechanism and tubular transport"),
    (s_bb_cv, "Cardiovascular pressure, flow, and vascular resistance"),
    (s_bb_resp, "Respiratory gas exchange and hemoglobin dynamics"),
    (s_bb_enz, "Enzyme kinetics and reversible inhibition mechanisms"),
    (s_bb_endo, "Endocrine feedback loops and hormone regulation"),
]

exam_bb60 = []
q_counter = 1
for p_idx, (p_set, topic) in enumerate(bb60_raw_passages, 1):
    n_qs = len(p_set["qs"])
    q_start = q_counter
    q_end = q_counter + n_qs - 1
    q_counter += n_qs
    
    clean_p = {
        "id": f"exam_bb60_p{p_idx}",
        "sec": "B/B",
        "topic": topic,
        "sheet": p_set.get("sheet", p_idx),
        "label": "Biological and Biochemical Foundations of Living Systems",
        "examId": "bb60",
        "passage": renumber_passage(p_set["passage"], p_idx, q_start, q_end),
        "qs": p_set["qs"]
    }
    exam_bb60.append(clean_p)

exam_bb60.append(bb_discretes)
total_bb60_qs = sum(len(s["qs"]) for s in exam_bb60)
print(f"EXAM_BB60 assembled: {len(exam_bb60)} sets, {total_bb60_qs} questions")

# ==============================================================================
# 3. EXAM_CARS60 (6 Passages = ~32 Questions)
# ==============================================================================
print("Assembling EXAM_CARS60...")
s_cars_1 = find_set("cars_1")
s_cars_2 = find_set("cars_2")
s_cars_3 = find_set("cars_3")
s_cars_boas = find_set("cars_boas")
s_cars_pater = find_set("cars_pater")
s_cars_puritan = find_set("aamc_puritan_society")

cars60_raw_passages = [
    (s_cars_1, s_cars_1.get("topic", "Philosophy of history")),
    (s_cars_2, s_cars_2.get("topic", "Aesthetics — the problem of the copy")),
    (s_cars_3, s_cars_3.get("topic", "Social science — the measurement of poverty")),
    (s_cars_boas, s_cars_boas.get("topic", "Boas — inferring aptitude from achievement")),
    (s_cars_pater, s_cars_pater.get("topic", "Pater — aesthetic criticism")),
    (s_cars_puritan, s_cars_puritan.get("topic", "Puritan society and individualism")),
]

exam_cars60 = []
q_counter = 1
for p_idx, (p_set, topic) in enumerate(cars60_raw_passages, 1):
    n_qs = len(p_set["qs"])
    q_start = q_counter
    q_end = q_counter + n_qs - 1
    q_counter += n_qs
    
    clean_p = {
        "id": f"exam_cars60_p{p_idx}",
        "sec": "CARS",
        "topic": topic,
        "sheet": p_set.get("sheet", None),
        "label": "Critical Analysis and Reasoning Skills",
        "examId": "cars60",
        "passage": renumber_passage(p_set["passage"], p_idx, q_start, q_end),
        "qs": p_set["qs"]
    }
    exam_cars60.append(clean_p)

total_cars60_qs = sum(len(s["qs"]) for s in exam_cars60)
print(f"EXAM_CARS60 assembled: {len(exam_cars60)} sets, {total_cars60_qs} questions")

# ==============================================================================
# 4. EXAM_PS60 (5 Passages + 5 Discretes)
# ==============================================================================
print("Assembling EXAM_PS60...")
s_ps_social = find_set("ps_social")
s_ps_learn = find_set("ps_learn")
s_ps_disorders = find_set("ps_disorders")
s_ps_p2 = ps90[1] # Stereotype threat & cortisol
s_ps_p3 = ps90[2] # Fundamental cause theory & weathering

ps_discretes = {
    "id": "exam_ps60_disc",
    "sec": "P/S",
    "topic": "P/S Standalone Discrete Questions",
    "sheet": None,
    "label": "Psychological, Social, and Biological Foundations of Behavior",
    "examId": "ps60",
    "passage": "",
    "qs": ps90[7]["qs"][:5]
}

ps60_raw_passages = [
    (s_ps_social, "Social psychology — helping behavior and attribution"),
    (s_ps_learn, "Learning, memory formation, and conditioning"),
    (s_ps_disorders, "Psychological disorders and biological bases"),
    (s_ps_p2, s_ps_p2["topic"]),
    (s_ps_p3, s_ps_p3["topic"]),
]

exam_ps60 = []
q_counter = 1
for p_idx, (p_set, topic) in enumerate(ps60_raw_passages, 1):
    n_qs = len(p_set["qs"])
    q_start = q_counter
    q_end = q_counter + n_qs - 1
    q_counter += n_qs
    
    clean_p = {
        "id": f"exam_ps60_p{p_idx}",
        "sec": "P/S",
        "topic": topic,
        "sheet": p_set.get("sheet", p_idx),
        "label": "Psychological, Social, and Biological Foundations of Behavior",
        "examId": "ps60",
        "passage": renumber_passage(p_set["passage"], p_idx, q_start, q_end),
        "qs": p_set["qs"]
    }
    exam_ps60.append(clean_p)

exam_ps60.append(ps_discretes)
total_ps60_qs = sum(len(s["qs"]) for s in exam_ps60)
print(f"EXAM_PS60 assembled: {len(exam_ps60)} sets, {total_ps60_qs} questions")

# ==============================================================================
# Write to /home/cgslinde/DrillRoom/DrillRoom/exam_60min.js
# ==============================================================================
js_out = f"""/* ---- exam_60min.js ---- */
/* 60-minute practice sections for all 4 MCAT subjects.
   CP60: {total_cp60_qs} Qs | BB60: {total_bb60_qs} Qs | CARS60: {total_cars60_qs} Qs | PS60: {total_ps60_qs} Qs */

const EXAM_CP60 = {json.dumps(exam_cp60, indent=2)};

const EXAM_BB60 = {json.dumps(exam_bb60, indent=2)};

const EXAM_CARS60 = {json.dumps(exam_cars60, indent=2)};

const EXAM_PS60 = {json.dumps(exam_ps60, indent=2)};
"""

with open("/home/cgslinde/DrillRoom/DrillRoom/exam_60min.js", "w") as f:
    f.write(js_out)

print("exam_60min.js generated and written successfully!")
