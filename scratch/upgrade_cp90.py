# scratch/upgrade_cp90.py
# Upgrades all 52 questions of EXAM_CP90 to authentic 5/5 Section Bank difficulty
# strictly adhering to the 5-Gate Review Protocol.

import json, re, sys

# Helper function to validate question gates
def parse_scientific_num(text):
    # Normalize minus signs and superscripts
    s = text.replace('−', '-').replace('&minus;', '-')
    sup_map = {'⁰':'0','¹':'1','²':'2','³':'3','⁴':'4','⁵':'5','⁶':'6','⁷':'7','⁸':'8','⁹':'9','⁻':'-'}
    for sup, char in sup_map.items():
        s = s.replace(sup, char)
    # Check for sci notation like 1.0 × 10^-12 or 1.0 x 10^-12
    m_sci = re.search(r'([-+]?\d*\.?\d+)\s*(?:[×x\*]\s*10\^?([-+]?\d+))', s)
    if m_sci:
        base = float(m_sci.group(1))
        exp = float(m_sci.group(2))
        return base * (10 ** exp)
    # Standard float
    m = re.search(r'[-+]?\d*\.?\d+', s)
    if m:
        return float(m.group(0))
    return None

def validate_question(q, idx):
    issues = []
    # Gate 4: Visual Symmetry & Anti-Cueing
    # Check if all choices are purely numeric (numbers with optional units)
    def is_num_choice(c):
        clean = c.replace('−', '-').replace('&minus;', '-').strip()
        # Starts with sign or digit, and has at most 3 tokens
        return bool(re.match(r'^[+\-]?\d', clean)) and len(c.strip().split()) <= 3

    is_numeric = all(is_num_choice(c) for c in q["ch"])
    lens = [len(c) for c in q["ch"]]
    r = max(lens) / max(min(lens), 1)
    
    if is_numeric:
        # Check numerical sorting
        nums = [parse_scientific_num(c) for c in q["ch"]]
        sorted_asc = sorted(nums)
        sorted_desc = sorted(nums, reverse=True)
        if nums != sorted_asc and nums != sorted_desc:
            issues.append(f"Q{idx} Gate 4: numeric choices not strictly sorted: {nums}")
    else:
        if r > 1.08:
            issues.append(f"Q{idx} Gate 4: ratio {r:.3f} > 1.08 (lens={lens})")
        corr_len = lens[q["a"]]
        if corr_len == max(lens) and lens.count(max(lens)) == 1:
            issues.append(f"Q{idx} Gate 4: correct choice is strict longest ({corr_len} vs others)")

    # Gate 5: Pedagogical Autopsy Structure
    e = q["e"]
    if "<strong>" not in e or "</strong>" not in e:
        issues.append(f"Q{idx} Gate 5: missing strong tag")
    if "Distractor Traps:" not in e:
        issues.append(f"Q{idx} Gate 5: missing Distractor Traps")
    bullets = re.findall(r'&bull;\s*([A-D])\s*(\([^\)]+\)):', e)
    if len(bullets) < 3:
        issues.append(f"Q{idx} Gate 5: < 3 bullets (found {len(bullets)})")
    
    # Check that bullet letters match non-correct choices
    expected_bullets = [chr(ord('A') + j) for j in range(4) if j != q["a"]]
    bullet_letters = [b[0] for b in bullets]
    if sorted(bullet_letters) != sorted(expected_bullets):
        issues.append(f"Q{idx} Gate 5: bullet letters {bullet_letters} do not match expected {expected_bullets}")
        
    return issues

print("Script template ready.")
