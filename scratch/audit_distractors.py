import json, re

def check_file(fn, var):
    with open('/home/cgslinde/DrillRoom/DrillRoom/' + fn) as f:
        t = f.read()
    b1 = t.find('[', t.find(var))
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
    
    print(f"\n==========================================")
    print(f"AUDITING {var} ({fn})")
    print(f"==========================================")
    
    flags = []
    for si, s in enumerate(data):
        topic = s.get("topic", f"Set {si+1}")
        for qi, q in enumerate(s["qs"]):
            ch = q["ch"]
            correct_idx = q["a"]
            
            # Check length disparity
            lens = [len(c) for c in ch]
            max_l, min_l = max(lens), min(lens)
            if max_l > 3 * min_l and min_l < 30:
                flags.append((si, qi, topic, "Length Disparity", f"Min {min_l} chars vs Max {max_l} chars", ch))
            
            # Check extreme words in distractors
            for ci, c in enumerate(ch):
                if ci != correct_idx:
                    if re.search(r'\b(completely|zero absolute|solely|never|always)\b', c, re.I):
                        flags.append((si, qi, topic, "Extreme Qualifier in Distractor", f"Choice {'ABCD'[ci]}: '{c}'", ch))
    
    print(f"Total flagged items in {var}: {len(flags)}")
    for f in flags[:8]:
        print(f"  [{f[2]}] Q{f[1]+1} - {f[3]}: {f[4]}")

check_file('exam_cp90.js', 'EXAM_CP90')
check_file('exam_bb90.js', 'EXAM_BB90')
check_file('exam_ps90.js', 'EXAM_PS90')
