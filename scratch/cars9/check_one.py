import sys
import importlib
from validator import validate_passage

if len(sys.argv) < 2:
    print("Usage: python3 check_one.py <passage_num> [expected_qs]")
    sys.exit(1)

num = sys.argv[1]
exp_qs = int(sys.argv[2]) if len(sys.argv) > 2 else (5 if num == '9' else 6)

mod_name = f"p{num}"
mod = importlib.import_module(mod_name)
wc, errs = validate_passage(mod.passage_data, exp_qs)
print(f"Passage {num}: {wc} words, {len(mod.passage_data['qs'])} questions")
if errs:
    print("ERRORS:")
    for e in errs:
        print("  -", e)
    sys.exit(1)
else:
    print("SUCCESS: All criteria passed!")
