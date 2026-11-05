import re
from parse_cars import JSObjectParser, parse_set_at

with open("DrillRoom.html") as f:
    html = f.read()

scripts = re.findall(r"<script>(.*?)</script>", html, re.DOTALL)

for sid, sc_idx in [
    ("bb_renal", 1), ("bb_cv", 1), ("bb_resp", 1), ("ps_social", 1), ("ps_learn", 1),
    ("cp_acid", 2), ("cp_kin", 2), ("bb_enz", 2), ("bb_endo", 2), ("cars_1", 2),
    ("cars_2", 4), ("cars_3", 4), ("ps_disorders", 4), ("bb_neuro", 4), ("cp_phys", 4), ("bb_genetics", 4),
    ("cars_veblen", 5), ("cars_boas", 5), ("cars_addams", 5), ("cars_pater", 5),
    ("aamc_puritan_society", 6), ("aamc_understanding_thomas_h", 6), ("aamc_huns_and_eurasian_hist", 6)
]:
    obj = parse_set_at(scripts[sc_idx], sid)
    print(f"Parsed {sid:25}: qs={len(obj['qs'])} | table={'<table>' in obj.get('passage', '')}")

