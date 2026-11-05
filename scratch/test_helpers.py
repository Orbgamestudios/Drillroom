import re

def clean_html(text):
    clean = re.sub(r'<[^>]+>', ' ', text)
    clean = clean.replace('&ndash;', '-').replace('&mdash;', '—').replace('&ldquo;', '"').replace('&rdquo;', '"')
    return clean

def count_words(text):
    cleaned = clean_html(text)
    # Ignore the header line like Passage 1 (Questions 1-6)
    lines = [line.strip() for line in cleaned.split('\n') if line.strip()]
    if lines and 'Passage' in lines[0] and 'Questions' in lines[0]:
        lines = lines[1:]
    body = ' '.join(lines)
    return len(body.split())

def validate_passage_obj(p_obj):
    errors = []
    pid = p_obj.get("id", "unknown")
    
    # Check word count
    wc = count_words(p_obj["passage"])
    if not (550 <= wc <= 650):
        errors.append(f"Passage {pid}: word count is {wc}, outside target [550, 650]")
        
    qs = p_obj.get("qs", [])
    for idx, q in enumerate(qs, 1):
        ch = q.get("ch", [])
        if len(ch) != 4:
            errors.append(f"Passage {pid} Q{idx}: does not have exactly 4 choices (has {len(ch)})")
        
        # Check answer index
        ans = q.get("a")
        if ans not in [0, 1, 2, 3]:
            errors.append(f"Passage {pid} Q{idx}: answer index {ans} invalid")
            
        # Check length parity
        lengths = [len(c) for c in ch]
        min_l, max_l = min(lengths), max(lengths)
        ratio = max_l / min_l if min_l > 0 else 999
        if ratio > 1.35: # allow up to 35% difference in characters, ideally <= 1.25
            errors.append(f"Passage {pid} Q{idx}: choice length parity warning: min={min_l}, max={max_l}, ratio={ratio:.2f}")
            
        # Check explanation format
        e = q.get("e", "")
        if "<strong>" not in e or "</strong>" not in e:
            errors.append(f"Passage {pid} Q{idx}: explanation missing <strong>...</strong>")
        if "<em>Distractor Traps:</em>" not in e:
            errors.append(f"Passage {pid} Q{idx}: explanation missing '<em>Distractor Traps:</em>'")
        
        # Check bullets
        bullets = e.count("&bull;")
        if bullets != 3:
            errors.append(f"Passage {pid} Q{idx}: explanation has {bullets} &bull; bullets, expected exactly 3")
            
        # Check that the 3 distractors match the 3 incorrect letters
        letters = ['A', 'B', 'C', 'D']
        expected_distractor_letters = [letters[i] for i in range(4) if i != ans]
        for dl in expected_distractor_letters:
            if f"&bull; {dl}" not in e:
                errors.append(f"Passage {pid} Q{idx}: explanation missing distractor trap for '{dl}' (expected &bull; {dl})")
                
    return wc, errors

if __name__ == "__main__":
    from passages.p1_kant import passage_data
    wc, errors = validate_passage_obj(passage_data)
    print(f"Passage 1 word count: {wc}")
    if errors:
        print("Errors/Warnings:")
        for e in errors:
            print(" -", e)
    else:
        print("All validations passed for Passage 1!")
