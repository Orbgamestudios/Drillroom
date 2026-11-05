import re
import sys

def count_words(passage_html):
    p_texts = re.findall(r"<p>(.*?)</p>", passage_html, re.DOTALL)
    if not p_texts:
        clean = re.sub(r'<[^>]+>', ' ', passage_html)
        return len(clean.split())
    prose = re.sub(r"<[^>]+>", " ", " ".join(p_texts))
    return len(prose.split())

def validate_section(p_obj, is_discrete=False):
    errors = []
    pid = p_obj.get("id", "unknown")
    qs = p_obj.get("qs", [])
    
    if not is_discrete:
        if len(qs) != 6:
            errors.append(f"{pid}: expected 6 questions, found {len(qs)}")
        wc = count_words(p_obj.get("passage", ""))
        if not (200 <= wc <= 420):
            errors.append(f"{pid}: prose word count {wc} outside [200, 420]")
        if '<table class="tbl">' not in p_obj.get("passage", ""):
            errors.append(f"{pid}: missing experimental <table class=\"tbl\">")
    else:
        if len(qs) != 10:
            errors.append(f"{pid}: expected 10 discrete questions, found {len(qs)}")
        wc = 0
            
    for idx, q in enumerate(qs, 1):
        ch = q.get("ch", [])
        if len(ch) != 4:
            errors.append(f"{pid} Q{idx}: does not have exactly 4 choices")
            continue
        ans = q.get("a")
        if ans not in [0, 1, 2, 3]:
            errors.append(f"{pid} Q{idx}: invalid answer index {ans}")
            
        lengths = [len(c) for c in ch]
        avg_l = sum(lengths) / 4.0
        max_dev = max(abs(l - avg_l) / avg_l for l in lengths) if avg_l > 0 else 999
        if max_dev > 0.20:
            errors.append(f"{pid} Q{idx}: length parity failed: max_dev={max_dev:.1%}, lengths={lengths}")
            
        e = q.get("e", "")
        if "<strong>" not in e:
            errors.append(f"{pid} Q{idx}: missing <strong> topic explanation")
        if "Distractor Traps:" not in e:
            errors.append(f"{pid} Q{idx}: missing 'Distractor Traps:'")
        if is_discrete and q.get("d") is not True:
            errors.append(f"{pid} Q{idx}: discrete question missing d: True")
            
    return wc, errors
