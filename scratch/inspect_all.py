from parse_cars import s5, s6, parse_set_at
from test_all import sets_to_test

for i, (src, sid) in enumerate(sets_to_test, 1):
    parsed = parse_set_at(src, sid)
    print(f"=== Passage {i}: {sid} ===")
    print("Passage length (chars):", len(parsed["passage"]))
    for qi, q in enumerate(parsed["qs"], 1):
        q_len = len(q["q"])
        q_snippet = q["q"][:60]
        ans = q["a"]
        print(f"  Q{qi} (len {q_len}): {q_snippet}... -> ans={ans}")
        for ci, c in enumerate(q["ch"]):
            if len(c) == 0:
                print(f"    ERROR: empty choice {ci} in Q{qi} of {sid}")
        if len(q["e"]) < 20:
            print(f"    WARNING: short explanation in Q{qi} of {sid}: {q['e']}")
