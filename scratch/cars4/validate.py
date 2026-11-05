#!/usr/bin/env python3
import re
import sys

def clean_html(text):
    clean = re.sub(r'<[^>]+>', ' ', text)
    clean = clean.replace('&ndash;', '-').replace('&mdash;', '—').replace('&ldquo;', '"').replace('&rdquo;', '"')
    return clean

def count_words(text):
    cleaned = clean_html(text)
    lines = [line.strip() for line in cleaned.split('\n') if line.strip()]
    if lines and 'Passage' in lines[0] and 'Questions' in lines[0]:
        lines = lines[1:]
    body = ' '.join(lines)
    return len(body.split())

def validate_passage(p_obj, expected_q_count=6):
    errors = []
    pid = p_obj.get("id", "unknown")
    
    # 1. Word count
    wc = count_words(p_obj["passage"])
    if not (550 <= wc <= 650):
        errors.append(f"{pid}: Word count {wc} outside [550, 650]")
        
    qs = p_obj.get("qs", [])
    if len(qs) != expected_q_count:
        errors.append(f"{pid}: Expected {expected_q_count} questions, got {len(qs)}")
        
    letters = ['A', 'B', 'C', 'D']
    
    for idx, q in enumerate(qs, 1):
        q_label = f"{pid} Q{idx}"
        ch = q.get("ch", [])
        if len(ch) != 4:
            errors.append(f"{q_label}: Has {len(ch)} choices, expected 4")
            continue
            
        ans = q.get("a")
        if ans not in [0, 1, 2, 3]:
            errors.append(f"{q_label}: Invalid answer index {ans}")
            
        # Parity check: max length / min length <= 1.25 and max deviation from mean <= 20%
        lengths = [len(c) for c in ch]
        min_l, max_l = min(lengths), max(lengths)
        mean_l = sum(lengths) / len(lengths)
        max_dev = max(abs(l - mean_l) / mean_l for l in lengths)
        ratio = max_l / min_l if min_l > 0 else 999
        
        if ratio > 1.25 or max_dev > 0.20:
            errors.append(f"{q_label}: Length parity violated! min={min_l}, max={max_l}, ratio={ratio:.2f}, max_dev={max_dev*100:.1f}%, lens={lengths}")
            
        # Explanation checks
        e = q.get("e", "")
        if "<strong>" not in e or "</strong>" not in e:
            errors.append(f"{q_label}: Explanation missing <strong>...</strong>")
        if "<em>Distractor Traps:</em>" not in e:
            errors.append(f"{q_label}: Explanation missing '<em>Distractor Traps:</em>'")
            
        bullets = e.count("&bull;")
        if bullets != 3:
            errors.append(f"{q_label}: Expected 3 bullets, found {bullets}")
            
        expected_distractors = [letters[i] for i in range(4) if i != ans]
        for dl in expected_distractors:
            if f"&bull; {dl}" not in e:
                errors.append(f"{q_label}: Explanation missing bullet for distractor '{dl}'")
                
    return wc, errors

if __name__ == "__main__":
    print("Validator ready.")
