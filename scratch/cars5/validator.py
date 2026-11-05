import re
import sys

def validate_passage(p_data, p_num, expected_qs):
    errors = []
    warnings = []
    
    # Check id, sec, topic, label, examId
    if p_data.get("id") != f"exam_cars90_5_p{p_num}":
        errors.append(f"Passage {p_num} id mismatch: expected exam_cars90_5_p{p_num}, got {p_data.get('id')}")
    if p_data.get("sec") != "CARS":
        errors.append(f"Passage {p_num} sec mismatch: expected CARS")
    if p_data.get("examId") != "cars90_5":
        errors.append(f"Passage {p_num} examId mismatch: expected cars90_5")
    if p_data.get("label") != "Critical Analysis and Reasoning Skills":
        errors.append(f"Passage {p_num} label mismatch")
        
    passage_html = p_data.get("passage", "")
    # Remove HTML tags to count words
    text_clean = re.sub(r'<[^>]+>', ' ', passage_html)
    # Remove title like "Passage X (Questions Y-Z)"
    text_clean = re.sub(r'Passage\s+\d+\s*\([^\)]+\)', ' ', text_clean)
    words = text_clean.split()
    word_count = len(words)
    
    if word_count < 550 or word_count > 650:
        errors.append(f"Passage {p_num} word count out of range (550-650): {word_count} words")
    else:
        print(f"Passage {p_num} word count OK: {word_count} words")
        
    qs = p_data.get("qs", [])
    if len(qs) != expected_qs:
        errors.append(f"Passage {p_num} question count mismatch: expected {expected_qs}, got {len(qs)}")
        
    for i, q in enumerate(qs):
        q_num = i + 1
        q_text = q.get("q", "")
        choices = q.get("ch", [])
        ans = q.get("a")
        exp = q.get("e", "")
        
        if not q_text:
            errors.append(f"Passage {p_num} Q{q_num}: empty question text")
        if len(choices) != 4:
            errors.append(f"Passage {p_num} Q{q_num}: expected 4 choices, got {len(choices)}")
        if ans not in [0, 1, 2, 3]:
            errors.append(f"Passage {p_num} Q{q_num}: invalid answer index {ans}")
            
        # Parity check
        if len(choices) == 4:
            lens = [len(c) for c in choices]
            min_l, max_l = min(lens), max(lens)
            ratio = min_l / max_l if max_l > 0 else 0
            if ratio < 0.80:
                errors.append(f"Passage {p_num} Q{q_num}: parity failure! min={min_l}, max={max_l}, ratio={ratio:.3f} (< 0.80). Lens: {lens}")
                
        # Explanation check
        if "<em>Distractor Traps:</em>" not in exp:
            errors.append(f"Passage {p_num} Q{q_num}: explanation missing '<em>Distractor Traps:</em>'")
        letters = ["A", "B", "C", "D"]
        distractors = [letters[j] for j in range(4) if j != ans]
        for d in distractors:
            if f"&bull; {d}" not in exp and f"&bull;{d}" not in exp:
                errors.append(f"Passage {p_num} Q{q_num}: distractor explanation missing bullet for '{d}'")

    return errors, word_count

if __name__ == "__main__":
    print("Validator ready.")
