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

def validate_passage(p_obj, target_q_count=6):
    errors = []
    pid = p_obj.get("id", "unknown")
    
    # Check word count (550 to 650 words)
    wc = count_words(p_obj["passage"])
    if not (550 <= wc <= 650):
        errors.append(f"Passage {pid}: word count is {wc}, outside target [550, 650]")
        
    qs = p_obj.get("qs", [])
    if len(qs) != target_q_count:
        errors.append(f"Passage {pid}: has {len(qs)} questions, expected {target_q_count}")
        
    letters = ['A', 'B', 'C', 'D']
    for idx, q in enumerate(qs, 1):
        ch = q.get("ch", [])
        if len(ch) != 4:
            errors.append(f"Passage {pid} Q{idx}: does not have exactly 4 choices (has {len(ch)})")
            continue
        
        ans = q.get("a")
        if ans not in [0, 1, 2, 3]:
            errors.append(f"Passage {pid} Q{idx}: answer index {ans} invalid")
            
        # Check length parity: max / min ratio <= 1.25 (strict length parity)
        lengths = [len(c) for c in ch]
        min_l, max_l = min(lengths), max(lengths)
        ratio = max_l / min_l if min_l > 0 else 999
        if ratio > 1.25:
            errors.append(f"Passage {pid} Q{idx}: length parity exceeded: min={min_l}, max={max_l}, ratio={ratio:.2f} > 1.25")
            
        # Check explanation format
        e = q.get("e", "")
        if "<strong>" not in e or "</strong>" not in e:
            errors.append(f"Passage {pid} Q{idx}: explanation missing <strong>...</strong>")
        if "<em>Distractor Traps:</em>" not in e:
            errors.append(f"Passage {pid} Q{idx}: explanation missing '<em>Distractor Traps:</em>'")
            
        bullets = e.count("&bull;")
        if bullets != 3:
            errors.append(f"Passage {pid} Q{idx}: explanation has {bullets} &bull; bullets, expected exactly 3")
            
        expected_distractors = [letters[i] for i in range(4) if i != ans]
        for dl in expected_distractors:
            if f"&bull; {dl}" not in e:
                errors.append(f"Passage {pid} Q{idx}: missing trap for '&bull; {dl}'")
                
    return wc, errors
