import json, sys
sys.path.append('/home/cgslinde/DrillRoom/DrillRoom/scratch')
from craft_ps90_p1_to_p4 import p1_qs, p2_qs, p3_qs, p4_qs
from craft_ps90_p5_to_p8 import p5_qs, p6_qs, p7_qs, discrete_qs

# Load existing exam_ps90.js
with open("/home/cgslinde/DrillRoom/DrillRoom/exam_ps90.js") as f:
    orig_text = f.read()

data = json.loads(orig_text[orig_text.find('['):orig_text.rfind(']')+1])
assert len(data) == 8, f"Expected 8 items in exam_ps90.js, got {len(data)}"

data[0]["qs"] = p1_qs
data[1]["qs"] = p2_qs
data[2]["qs"] = p3_qs
data[3]["qs"] = p4_qs
data[4]["qs"] = p5_qs
data[5]["qs"] = p6_qs
data[6]["qs"] = p7_qs
data[7]["qs"] = discrete_qs

# Build output JS
js_content = "/* ---- exam_ps90.js ---- */\n/* Full 90-minute Psych/Soc practice section: 7 passages (42 Qs) + 10 discrete Qs = 52 Qs */\nconst EXAM_PS90 = " + json.dumps(data, indent=2) + ";\n"

with open("/home/cgslinde/DrillRoom/DrillRoom/exam_ps90.js", "w") as f:
    f.write(js_content)

print("exam_ps90.js successfully overwritten with upgraded 5/5 questions!")
