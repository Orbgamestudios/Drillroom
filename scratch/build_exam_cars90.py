import json, re
from parse_cars import s5, s6, parse_set_at

# List of the 9 selected passages: (source_script, source_id, new_id, topic, question_range)
passages_spec = [
    (
        s5,
        "cars_veblen",
        "exam_cars90_p1",
        "Thorstein Veblen — The Place of Science in Modern Civilisation",
        "Passage 1 (Questions 1&ndash;6)"
    ),
    (
        s6,
        "aamc_puritan_society",
        "exam_cars90_p2",
        "Nathaniel Hawthorne — Puritan Society and Orthodoxy",
        "Passage 2 (Questions 7&ndash;12)"
    ),
    (
        s6,
        "aamc_understanding_thomas_h",
        "exam_cars90_p3",
        "Literary Criticism — Understanding Thomas Hardy",
        "Passage 3 (Questions 13&ndash;18)"
    ),
    (
        s6,
        "aamc_maternal_psychology",
        "exam_cars90_p4",
        "Evolutionary Psychology — Maternal Emotional Response",
        "Passage 4 (Questions 19&ndash;24)"
    ),
    (
        s6,
        "aamc_huns_and_eurasian_hist",
        "exam_cars90_p5",
        "Historiography — The Huns and Eurasian History",
        "Passage 5 (Questions 25&ndash;30)"
    ),
    (
        s6,
        "aamc_energy_and_sustainable",
        "exam_cars90_p6",
        "Political Economy — Energy and Sustainable Development in Nigeria",
        "Passage 6 (Questions 31&ndash;36)"
    ),
    (
        s6,
        "aamc_primordial_and_complex",
        "exam_cars90_p7",
        "Philosophical Psychology — Primordial and Complex Jealousy",
        "Passage 7 (Questions 37&ndash;42)"
    ),
    (
        s6,
        "aamc_what_is_life",
        "exam_cars90_p8",
        "Philosophy of Science — The Nature of Biological Life",
        "Passage 8 (Questions 43&ndash;48)"
    ),
    (
        s5,
        "cars_addams",
        "exam_cars90_p9",
        "Jane Addams — Charity and the Democratic Standard",
        "Passage 9 (Questions 49&ndash;53)"
    )
]

exam_sets = []
total_questions = 0

for src, orig_id, new_id, topic, ttl_text in passages_spec:
    orig = parse_set_at(src, orig_id)
    
    # Update passage title div
    new_ttl = f'<div class="ttl">{ttl_text}</div>'
    passage_html = orig["passage"].strip()
    if re.search(r"^<div class=\"ttl\">.*?</div>", passage_html):
        passage_html = re.sub(r"^<div class=\"ttl\">.*?</div>", new_ttl, passage_html, count=1)
    else:
        passage_html = new_ttl + "\n" + passage_html
        
    # Clean and validate qs
    clean_qs = []
    for q in orig["qs"]:
        # Ensure proper keys
        clean_q = {
            "q": q["q"],
            "ch": [c.strip() for c in q["ch"]],
            "a": int(q["a"]),
            "e": q["e"]
        }
        clean_qs.append(clean_q)
        
    set_obj = {
        "id": new_id,
        "sec": "CARS",
        "topic": topic,
        "label": "Critical Analysis and Reasoning Skills",
        "examId": "cars90",
        "passage": passage_html,
        "qs": clean_qs
    }
    
    exam_sets.append(set_obj)
    total_questions += len(clean_qs)
    print(f"Added {new_id}: {topic} -> {len(clean_qs)} questions")

print(f"\nTotal exam sets: {len(exam_sets)}")
print(f"Total exam questions: {total_questions}")

# Format as JavaScript
header_comment = """/* ---- exam_cars90.js ---- */
/* Full 90-minute CARS practice section: 9 passages = 53 Qs (exact MCAT standard) */
"""
js_content = header_comment + "const EXAM_CARS90 = " + json.dumps(exam_sets, indent=2) + ";\n"

out_path = "/home/cgslinde/DrillRoom/DrillRoom/exam_cars90.js"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully wrote {out_path} ({len(js_content)} bytes)")
