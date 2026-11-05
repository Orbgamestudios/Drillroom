import sys
import os

from validator import validate_section, count_words

def check(p_obj, is_discrete=False):
    wc, errors = validate_section(p_obj, is_discrete=is_discrete)
    print(f"ID: {p_obj.get('id')} | Word count: {wc} | Errors: {len(errors)}")
    for e in errors:
        print(f"  [ERROR] {e}")
    if not errors:
        for idx, q in enumerate(p_obj.get("qs", []), 1):
            lengths = [len(c) for c in q["ch"]]
            avg_l = sum(lengths) / 4.0
            max_dev = max(abs(l - avg_l) / avg_l for l in lengths)
            ratio = max(lengths) / min(lengths) if min(lengths) > 0 else 999
            ans_letter = ["A", "B", "C", "D"][q["a"]]
            print(f"  Q{idx}: ans={ans_letter}, lens={lengths}, avg={avg_l:.1f}, max_dev={max_dev:.1%}, ratio={ratio:.2f}")
    return len(errors) == 0

if __name__ == "__main__":
    pass
