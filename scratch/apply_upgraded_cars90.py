# scratch/apply_upgraded_cars90.py
import json, re, os, sys

sys.path.append('scratch')
import craft_cars90_p1_to_p4 as p14
import craft_cars90_p5_to_p9 as p59

raw_qs = [
    p14.p1_qs, p14.p2_qs, p14.p3_qs, p14.p4_qs,
    p59.p5_qs, p59.p6_qs, p59.p7_qs, p59.p8_qs, p59.p9_qs
]

cycle = [0, 1, 2, 3, 1, 2, 3, 0, 2, 3, 0, 1, 3, 0, 1, 2]

# Read original exam_cars90.js to preserve passage metadata
with open('exam_cars90.js', 'r', encoding='utf-8') as f:
    orig_text = f.read()

prefix = 'const EXAM_CARS90 = '
orig_json = orig_text.split(prefix)[1].rstrip().rstrip(';')
passages = json.loads(orig_json)

assert len(passages) == 9, f"Expected 9 passages, got {len(passages)}"

q_idx = 0
for p_num, pqs in enumerate(raw_qs):
    new_pqs = []
    for q in pqs:
        target_a = cycle[q_idx % len(cycle)]
        old_a = q['a']
        correct_choice = q['ch'][old_a]
        distractors = [c for j, c in enumerate(q['ch']) if j != old_a]
        
        new_ch = [None] * 4
        new_ch[target_a] = correct_choice
        d_idx = 0
        dist_new_indices = []
        for j in range(4):
            if j != target_a:
                new_ch[j] = distractors[d_idx]
                dist_new_indices.append(j)
                d_idx += 1
        
        # Verify Gate 4
        lens = [len(c) for c in new_ch]
        r = max(lens) / min(lens)
        assert r <= 1.08, f"Q{q_idx+1} ratio {r:.3f} > 1.08 (lens={lens})"
        assert not (lens[target_a] == max(lens) and lens.count(max(lens)) == 1), f"Q{q_idx+1} correct is longest"
        
        old_corr_letter = chr(ord('A') + old_a)
        new_corr_letter = chr(ord('A') + target_a)
        
        e = q['e']
        bullets = re.findall(r'&bull;\s*([A-D])\s*(\([^\)]+\)):(.*?)(?=(?:&bull;|$))', e, re.DOTALL)
        assert len(bullets) >= 3, f"Q{q_idx+1} < 3 bullets"
        
        new_bullets = []
        for k, (b_letter, b_trap, b_text) in enumerate(bullets):
            new_letter = chr(ord('A') + dist_new_indices[k])
            new_bullets.append((dist_new_indices[k], f'&bull; {new_letter} {b_trap}:{b_text}'))
        new_bullets.sort(key=lambda x: x[0])
        bullets_str = ''.join([b[1] for b in new_bullets]).strip()
        
        e_head = e.split('<em>Distractor Traps:</em>')[0]
        new_e = f'{e_head}<em>Distractor Traps:</em><br>{bullets_str}'
        new_e = re.sub(r'Choice\s+' + old_corr_letter, f'Choice {new_corr_letter}', new_e)
        new_e = re.sub(r'choice\s+' + old_corr_letter, f'choice {new_corr_letter}', new_e)
        
        # Verify bullets match non-correct letters
        b_letters = re.findall(r'&bull;\s*([A-D])', new_e)
        expected_b_letters = [chr(ord('A') + j) for j in range(4) if j != target_a]
        assert b_letters == expected_b_letters, f"Q{q_idx+1} bullets {b_letters} != {expected_b_letters}"
        
        new_q = {
            'q': q['q'],
            'ch': new_ch,
            'a': target_a,
            'e': new_e
        }
        new_pqs.append(new_q)
        q_idx += 1
    passages[p_num]['qs'] = new_pqs

assert q_idx == 53, f"Expected 53 questions, got {q_idx}"

# Write back to exam_cars90.js
header = "/* ---- exam_cars90.js ---- */\n/* Full 90-minute CARS practice section: 9 passages = 53 Qs (exact MCAT standard) */\n"
content = header + "const EXAM_CARS90 = " + json.dumps(passages, indent=2, ensure_ascii=False) + ";\n"

with open('exam_cars90.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated exam_cars90.js with 53 upgraded 5/5 difficulty questions!")
