import re

def check_parity(qs):
    failures = []
    for idx, q in enumerate(qs):
        lengths = [len(c) for c in q["ch"]]
        ratio = max(lengths) / min(lengths)
        if ratio > 1.25:
            failures.append((idx + 1, ratio, lengths, q["ch"]))
    return failures

print("Helper ready")
