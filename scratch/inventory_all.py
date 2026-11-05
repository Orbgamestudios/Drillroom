import json, re

inventory = {}

# 1. Exams
for fn, var_names in [
    ('exam_cp90.js', ['EXAM_CP90']),
    ('exam_bb90.js', ['EXAM_BB90']),
    ('exam_cars90.js', ['EXAM_CARS90']),
    ('exam_ps90.js', ['EXAM_PS90']),
    ('exam_60min.js', ['EXAM_CP60', 'EXAM_BB60', 'EXAM_CARS60', 'EXAM_PS60'])
]:
    with open('/home/cgslinde/DrillRoom/DrillRoom/' + fn) as f:
        t = f.read()
    for v in var_names:
        s = t.find(v)
        b1 = t.find('[', s)
        d = 0; b2 = -1; in_s = False; esc = False; sc = ''
        for i in range(b1, len(t)):
            c = t[i]
            if esc: esc = False; continue
            if c == '\\': esc = True; continue
            if in_s:
                if c == sc: in_s = False
                continue
            if c in ('"', "'"): in_s = True; sc = c; continue
            if c == '[': d += 1
            elif c == ']':
                d -= 1
                if d == 0: b2 = i; break
        data = json.loads(t[b1:b2+1])
        inventory[v] = [(item.get('id'), item.get('sec'), item.get('topic'), len(item.get('qs', []))) for item in data]

print("=== EXAM CONTENT INVENTORY ===")
for v, items in inventory.items():
    print(f"\n{v} ({len(items)} sets/passages):")
    for sid, sec, top, nq in items:
        print(f"  [{sec}] {sid:22} | {nq:2} Qs | {top}")

