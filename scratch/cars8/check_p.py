#!/usr/bin/env python3
import sys
import importlib
from validator import validate_passage, count_words

if len(sys.argv) < 2:
    print("Usage: python3 check_p.py <module_name> [q_count]")
    sys.exit(1)

mod_name = sys.argv[1]
q_count = int(sys.argv[2]) if len(sys.argv) > 2 else 6

mod = importlib.import_module(mod_name)
wc, errs = validate_passage(mod.passage_data, q_count)
print(f"Passage: {mod_name} | Word count: {wc} words | Questions: {len(mod.passage_data['qs'])}")

lengths_info = []
for idx, q in enumerate(mod.passage_data['qs'], 1):
    lens = [len(c) for c in q['ch']]
    ratio = max(lens) / min(lens)
    print(f"  Q{idx} (Ans {chr(65+q['a'])}): lens={lens}, ratio={ratio:.2f}")

if errs:
    print("ERRORS:")
    for e in errs:
        print("  -", e)
    sys.exit(1)
else:
    print("PASS: All checks passed!")
