from parse_cars import s5, s6, parse_set_at

sets_to_test = [
    (s5, "cars_veblen"),
    (s6, "aamc_puritan_society"),
    (s6, "aamc_understanding_thomas_h"),
    (s6, "aamc_maternal_psychology"),
    (s6, "aamc_huns_and_eurasian_hist"),
    (s6, "aamc_energy_and_sustainable"),
    (s6, "aamc_primordial_and_complex"),
    (s6, "aamc_what_is_life"),
    (s5, "cars_addams"),
]

total_qs = 0
for src, sid in sets_to_test:
    parsed = parse_set_at(src, sid)
    n_qs = len(parsed["qs"])
    total_qs += n_qs
    t = parsed.get("topic", "")
    print(f"{sid:30} | {n_qs} Qs | topic: {t}")
    for qi, q in enumerate(parsed["qs"]):
        num_ch = len(q["ch"])
        ans = q["a"]
        assert num_ch == 4, f"{sid} Q{qi+1} has {num_ch} choices!"
        assert ans in (0, 1, 2, 3), f"{sid} Q{qi+1} invalid answer {ans}"
        assert len(q["q"]) > 5, f"{sid} Q{qi+1} empty question"
        assert len(q["e"]) > 5, f"{sid} Q{qi+1} empty explanation"

print(f"\nALL 9 PASSAGES PARSED PERFECTLY! Total questions = {total_qs}")
