import sys, os, json, re, copy

sys.path.append("/home/cgslinde/DrillRoom/DrillRoom/scratch")
from p1 import p1
from p2 import p2
from p3 import p3
from p4 import p4
from p5 import p5
from p6 import p6
from p7 import p7
from discretes import discretes

passages_90 = [p1, p2, p3, p4, p5, p6, p7]
all_90 = passages_90 + [discretes]

# Build 60-min exam
passages_60 = []
for idx, p in enumerate([p1, p2, p3, p4, p5]):
    p_copy = copy.deepcopy(p)
    p_copy["id"] = f"exam_bb60_9_p{idx+1}"
    p_copy["examId"] = "bb60_9"
    passages_60.append(p_copy)

disc_60 = copy.deepcopy(discretes)
disc_60["id"] = "exam_bb60_9_disc"
disc_60["sheet"] = 6
disc_60["examId"] = "bb60_9"
disc_60["qs"] = disc_60["qs"][:3]

all_60 = passages_60 + [disc_60]

# --- Validation Routine ---
def validate_exam(exam_data, name, expected_counts, expected_total):
    print(f"\n================ Validating {name} ================")
    total_qs = 0
    key_counts = {0: 0, 1: 0, 2: 0, 3: 0}
    letters = ["A", "B", "C", "D"]
    errors = []

    for s_idx, sec in enumerate(exam_data):
        # Validate passage if present
        if "passage" in sec and sec.get("passage"):
            raw = sec["passage"]
            if '<table class="tbl">' not in raw:
                errors.append(f"Section {sec['id']} missing <table class=\"tbl\">")
            prose = re.sub(r"<table[\s\S]*?</table>", "", raw)
            prose = re.sub(r"<div class=\"ttl\">[\s\S]*?</div>", "", prose)
            prose = re.sub(r"<[^>]+>", " ", prose)
            wc = len(prose.split())
            if not (200 <= wc <= 380):
                errors.append(f"Section {sec['id']} prose word count {wc} outside 200-380 words")
            else:
                print(f"Passage {sec['id']} word count: {wc} words (OK)")

        # Validate questions
        for q_idx, q in enumerate(sec["qs"]):
            total_qs += 1
            ch = q["ch"]
            if len(ch) != 4:
                errors.append(f"Q{total_qs} in {sec['id']} has {len(ch)} choices, expected 4")
            
            # Length parity
            lens = [len(c) for c in ch]
            ratio = max(lens) / min(lens)
            if ratio > 1.25:
                errors.append(f"Q{total_qs} in {sec['id']} length ratio {ratio:.3f} > 1.25 (lengths: {lens})")

            # Answer key
            ans = q["a"]
            if ans not in [0, 1, 2, 3]:
                errors.append(f"Q{total_qs} in {sec['id']} invalid answer key {ans}")
            else:
                key_counts[ans] += 1

            # Explanation checks
            exp = q["e"]
            if "<strong>" not in exp or "</strong>" not in exp:
                errors.append(f"Q{total_qs} in {sec['id']} missing <strong>...</strong> in explanation")
            if "<em>Distractor Traps:</em><br>" not in exp:
                errors.append(f"Q{total_qs} in {sec['id']} missing <em>Distractor Traps:</em><br>")
            
            # Check bullets
            bullets = re.findall(r"&bull;\s*([A-D])", exp)
            expected_distractors = [letters[i] for i in range(4) if i != ans]
            if bullets != expected_distractors:
                errors.append(f"Q{total_qs} in {sec['id']} bullets {bullets} do not match expected {expected_distractors}")

    print(f"Total questions: {total_qs} (expected {expected_total})")
    print(f"Key distribution: A={key_counts[0]}, B={key_counts[1]}, C={key_counts[2]}, D={key_counts[3]}")
    print(f"Expected distribution: {expected_counts}")
    
    if total_qs != expected_total:
        errors.append(f"Total Q count {total_qs} != expected {expected_total}")

    for idx, l in enumerate(letters):
        if key_counts[idx] != expected_counts[l]:
            errors.append(f"Key count for {l} is {key_counts[idx]}, expected {expected_counts[l]}")

    if errors:
        print("\nERRORS FOUND:")
        for err in errors:
            print(f" - {err}")
        return False
    else:
        print(f"All checks PASSED for {name}!")
        return True

v90 = validate_exam(all_90, "EXAM_BB90_9", {"A": 13, "B": 13, "C": 13, "D": 13}, 52)
v60 = validate_exam(all_60, "EXAM_BB60_9", {"A": 8, "B": 8, "C": 9, "D": 8}, 33)

if not (v90 and v60):
    print("\nValidation failed! Exiting without writing files.")
    sys.exit(1)

# Format JS output
def write_js_file(filepath, var_name, data, header_comment):
    js_content = f"/* ---- {os.path.basename(filepath)} ---- */\n{header_comment}\nconst {var_name} = "
    js_content += json.dumps(data, indent=2, ensure_ascii=False)
    js_content += f";\n\nif (typeof window !== 'undefined') {{\n  window.{var_name} = {var_name};\n}}\nif (typeof globalThis !== 'undefined') {{\n  globalThis.{var_name} = {var_name};\n}}\n"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"Wrote {filepath} successfully ({len(js_content)} bytes)")

write_js_file("/home/cgslinde/DrillRoom/DrillRoom/exam_bb90_9.js", "EXAM_BB90_9", all_90, "/* Full 90-minute Biochem/Bio Practice Exam 9: 7 passages (42 Qs) + 10 discrete Qs = 52 Qs */")
write_js_file("/home/cgslinde/DrillRoom/DrillRoom/exam_bb60_9.js", "EXAM_BB60_9", all_60, "/* 60-minute Biochem/Bio Practice Exam 9: 5 passages (30 Qs) + 3 discrete Qs = 33 Qs */")
print("\nAll done!")
