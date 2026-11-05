# scratch/apply_upgraded_cp90.py
import json, re, sys

sys.path.append('scratch')
import upgrade_cp90_p1_to_p4 as p14
import upgrade_cp90_p5_to_p8 as p58
from upgrade_cp90 import validate_question

raw_items = [
    p14.cp_item1_qs, p14.cp_item2_qs, p14.cp_item3_qs, p14.cp_item4_qs,
    p58.cp_item5_qs, p58.cp_item6_qs, p58.cp_item7_qs, p58.cp_item8_qs
]

# Read original exam_cp90.js
with open('exam_cp90.js', 'r', encoding='utf-8') as f:
    orig_text = f.read()

prefix = 'const EXAM_CP90 = '
orig_json = orig_text.split(prefix)[1].rstrip().rstrip(';')
items = json.loads(orig_json)

assert len(items) == 8, f"Expected 8 items, got {len(items)}"

def is_num_choice(c):
    clean = c.replace('−', '-').replace('&minus;', '-').strip()
    return bool(re.match(r'^[+\-]?\d', clean)) and len(c.strip().split()) <= 3

# Targets for the 32 prose questions: 9 A, 4 B, 7 C, 12 D
prose_targets = ([0]*9 + [1]*4 + [2]*7 + [3]*12)
# Interleave them nicely
interleaved_prose_targets = []
# Pattern: [3, 0, 2, 0, 3, 2, 3, 1, 0, 3, 2, 0, 3, 1, 2, 0, 3, 2, 3, 0, 1, 3, 2, 0, 3, 1, 0, 3, 2, 0, 3, 3]
# Let's verify counts
from collections import Counter
prose_target_list = [3, 0, 2, 0, 3, 2, 3, 1, 0, 3, 2, 0, 3, 1, 2, 0, 3, 2, 3, 0, 1, 3, 2, 0, 3, 1, 0, 3, 0, 3, 2, 3]
assert Counter(prose_target_list) == Counter({0: 9, 1: 4, 2: 7, 3: 12}), f"Counter: {Counter(prose_target_list)}"

prose_idx = 0
q_global_idx = 0

for item_num, pqs in enumerate(raw_items):
    new_pqs = []
    for q in pqs:
        is_numeric = all(is_num_choice(c) for c in q['ch'])
        if is_numeric:
            # Numeric questions keep their sorted choices and answers
            new_q = q
        else:
            target_a = prose_target_list[prose_idx]
            prose_idx += 1
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
            
            # Check length symmetry
            lens = [len(c) for c in new_ch]
            r = max(lens) / min(lens)
            assert r <= 1.08, f"Q{q_global_idx+1} ratio {r:.3f} > 1.08"
            assert not (lens[target_a] == max(lens) and lens.count(max(lens)) == 1), f"Q{q_global_idx+1} correct is longest"
            
            # Update explanation bullets
            old_corr_letter = chr(ord('A') + old_a)
            new_corr_letter = chr(ord('A') + target_a)
            
            e = q['e']
            bullets = re.findall(r'&bull;\s*([A-D])\s*(\([^\)]+\)):(.*?)(?=(?:&bull;|$))', e, re.DOTALL)
            assert len(bullets) >= 3, f"Q{q_global_idx+1} < 3 bullets"
            
            new_bullets = []
            for k, (b_letter, b_trap, b_text) in enumerate(bullets):
                new_letter = chr(ord('A') + dist_new_indices[k])
                new_bullets.append((dist_new_indices[k], f'&bull; {new_letter} {b_trap}:{b_text}'))
            new_bullets.sort(key=lambda x: x[0])
            bullets_str = ''.join([b[1] for b in new_bullets]).strip()
            
            e_head = e.split('<em>Distractor Traps:</em>')[0]
            new_e = f'{e_head}<em>Distractor Traps:</em><br>{bullets_str}'
            
            new_q = {
                'q': q['q'],
                'ch': new_ch,
                'a': target_a,
                'e': new_e
            }
            
        # Validate question gates
        iss = validate_question(new_q, q_global_idx + 1)
        assert len(iss) == 0, f"Issues in Q{q_global_idx+1}: {iss}"
        
        new_pqs.append(new_q)
        q_global_idx += 1
    items[item_num]['qs'] = new_pqs

assert q_global_idx == 52, f"Expected 52 questions, got {q_global_idx}"

# Check final distribution
all_final_qs = [q for item in items for q in item['qs']]
counts = {i: 0 for i in range(4)}
for q in all_final_qs:
    counts[q['a']] += 1
print("Final EXAM_CP90 distribution:", {chr(ord('A')+k): v for k, v in counts.items()})

header = "/* ---- exam_cp90.js ---- */\n/* Full 90-minute Chemical and Physical Foundations practice section: 52 Qs */\n"
content = header + "const EXAM_CP90 = " + json.dumps(items, indent=2, ensure_ascii=False) + ";\n"

with open('exam_cp90.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated exam_cp90.js with 52 upgraded 5/5 difficulty questions!")
