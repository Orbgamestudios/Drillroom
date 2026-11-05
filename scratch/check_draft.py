import json

# We will test lengths and print any violation where max(lengths)/min(lengths) > 1.25
def test_lengths(q_num, ch):
    lens = [len(c) for c in ch]
    mn, mx = min(lens), max(lens)
    ratio = mx / mn
    status = "OK" if ratio <= 1.25 else "FAIL"
    print(f"Q{q_num}: ratio={ratio:.3f} [{mn} - {mx}] -> {status}")
    if ratio > 1.25:
        for i, c in enumerate(ch):
            print(f"  {chr(65+i)} ({len(c)}): {c}")
    return ratio <= 1.25

print("Draft checker ready")
