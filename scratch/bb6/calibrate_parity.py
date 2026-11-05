# Calibrate parity for BB6
import json, re

with open('/home/cgslinde/DrillRoom/DrillRoom/scratch/bb6/generate_all_bb6.py') as f:
    code = f.read()

# Let's inspect the exact lines where parity fails
from generate_all_bb6 import build_bb6
bb6 = build_bb6()

replacements = []

for s_idx, s in enumerate(bb6):
    for q_idx, q in enumerate(s['qs']):
        lens = [len(c) for c in q['ch']]
        ratio = max(lens) / min(lens)
        if ratio > 1.25:
            print(f"Set {s_idx+1} Q{q_idx+1} (ratio {ratio:.2f}): lens={lens}")
            for ci, c in enumerate(q['ch']):
                print(f"   [{ci}] len={len(c):2d}: {c}")
