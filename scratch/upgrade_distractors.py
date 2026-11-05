import json

def load_file(fn):
    with open('/home/cgslinde/DrillRoom/DrillRoom/' + fn) as f:
        t = f.read()
    b1 = t.find('[')
    b2 = t.rfind(']')
    data = json.loads(t[b1:b2+1])
    prefix = t[:b1]
    suffix = t[b2+1:]
    return data, prefix, suffix

def save_file(fn, data, prefix, suffix):
    with open('/home/cgslinde/DrillRoom/DrillRoom/' + fn, 'w') as f:
        f.write(prefix + json.dumps(data, indent=2) + suffix)
    print(f"Updated {fn} successfully!")

def find_and_replace_choice(data, old_sub, new_choice, new_explanation_addition=None):
    count = 0
    for s in data:
        for q in s["qs"]:
            for ci, c in enumerate(q["ch"]):
                if old_sub in c:
                    q["ch"][ci] = new_choice
                    if new_explanation_addition:
                        q["e"] = q["e"] + "<br><br>" + new_explanation_addition
                    count += 1
    print(f"Replaced {count} instances of '{old_sub[:30]}...'")
    return count

# ==============================================================================
# 1. UPGRADE EXAM_CP90
# ==============================================================================
cp, pfx, sfx = load_file('exam_cp90.js')

find_and_replace_choice(
    cp,
    "drops to zero absolute atmospheres",
    "The hydrostatic pressure in the stenosis increases proportionally with the square of fluid velocity.",
    "<strong>AAMC Distractor Trap Analysis:</strong> The 'pressure increase' distractor is an inversion trap: students recall that dynamic pressure scales as v², but erroneously add it to static pressure rather than recognizing that lateral hydrostatic pressure drops as kinetic energy rises along a streamline."
)

find_and_replace_choice(
    cp,
    "depends solely on cytoplasmic ion concentration",
    "remain constant because membrane capacitance depends on lipid bilayer permittivity and thickness rather than axon length.",
    "<strong>AAMC Distractor Trap Analysis:</strong> Choice C is a classic 'true fact, wrong question' trap: while specific membrane capacitance per unit area depends on membrane permittivity and thickness, the question asks for <em>total</em> axonal capacitance, which scales with physical surface area."
)

find_and_replace_choice(
    cp,
    "the d-orbitals are completely empty in the Pt(II)",
    "Pt(II) is a d¹⁰ transition metal species with fully filled d-subshells.",
    "<strong>AAMC Distractor Trap Analysis:</strong> Choice C is an electron-counting trap: students frequently confuse elemental Group 10 valence (10 valence electrons) with the d-count of the oxidized +2 ion (which is d⁸)."
)

save_file('exam_cp90.js', cp, pfx, sfx)

# ==============================================================================
# 2. UPGRADE EXAM_BB90
# ==============================================================================
bb, pfx, sfx = load_file('exam_bb90.js')

find_and_replace_choice(
    bb,
    "immediate proteolytic degradation",
    "Ouabain directly binds the intracellular sodium-binding pocket of SGLT2, acting as an uncompetitive inhibitor.",
    "<strong>AAMC Distractor Trap Analysis:</strong> Choice D is a plausible mechanism trap: students misattribute the pharmacological target of ouabain to SGLT2 itself rather than the basolateral primary active transporter that generates the electrochemical gradient."
)

find_and_replace_choice(
    bb,
    "Plasma bicarbonate is completely lost",
    "Inhibition of SGLT2 triggers compensatory hyperactivation of apical Na⁺/H⁺ antiporters (NHE3), resulting in profound metabolic alkalosis.",
    "<strong>AAMC Distractor Trap Analysis:</strong> Choice D is an extrapolation trap: SGLT2 does not trigger compensatory NHE3 hyperactivation sufficient to disturb blood pH."
)

find_and_replace_choice(
    bb,
    "completely blocks the sodium-potassium pump",
    "LQT2 selectively suppresses inward rectifier potassium channels (IK1), whereas LQT3 accelerates calcium-activated chloride conductance.",
    "<strong>AAMC Distractor Trap Analysis:</strong> Choice B is a channel subtype trap: students confuse the delayed rectifier (I_Kr) with the inward rectifier (I_K1) that maintains resting potential in Phase 4."
)

find_and_replace_choice(
    bb,
    "extracellular potassium is completely depleted",
    "rapid inward Ca²⁺ influx through Cav1.2 depolarizes the membrane potential above the reversal potential for potassium (E_K).",
    "<strong>AAMC Distractor Trap Analysis:</strong> Choice D is an electrophysiological trap: the membrane potential during Phase 2 (+10 mV) is far below E_Ca (+120 mV) and far above E_K (-90 mV); potassium does not stop flowing because of reversal potential parity, but because outward K⁺ flux matches inward Ca²⁺ flux."
)

save_file('exam_bb90.js', bb, pfx, sfx)

# ==============================================================================
# 3. UPGRADE EXAM_PS90
# ==============================================================================
ps, pfx, sfx = load_file('exam_ps90.js')

find_and_replace_choice(
    ps,
    "completely inhibits HPA axis activation",
    "cognitive reappraisal blocks peripheral glucocorticoid receptor binding in the hippocampus, terminating cortisol synthesis via direct negative feedback.",
    "<strong>AAMC Distractor Trap Analysis:</strong> Choice A is a biological mechanism trap: reappraisal is a prefrontal cortical cognitive-affective strategy that modulates emotional appraisal; it does not directly act as a peripheral receptor antagonist at hippocampal glucocorticoid receptors."
)

find_and_replace_choice(
    ps,
    "solely mediated by peripheral neuromuscular",
    "the decline was mediated by proactive interference from previously acquired engineering concepts stored in long-term memory.",
    "<strong>AAMC Distractor Trap Analysis:</strong> Choice D is an interference trap: the acute drop during threat is due to working memory resource depletion and evaluative anxiety, not proactive interference from prior long-term memory storage."
)

find_and_replace_choice(
    ps,
    "decays completely within 6 weeks",
    "peripheral route persuasion creates sleeper effects that surpass central route favorability after 6 weeks.",
    "<strong>AAMC Distractor Trap Analysis:</strong> Choice D is a cognitive fallacy trap: while sleeper effects occur under specific discounting cue paradigms, peripheral cues alone reliably decay rapidly relative to deeply elaborated central arguments."
)

find_and_replace_choice(
    ps,
    "completely avoids crossing the blood-brain barrier",
    "It acts as a selective 5-HT1A full antagonist in the dorsal raphe, suppressing striatal dopamine synthesis.",
    "<strong>AAMC Distractor Trap Analysis:</strong> Choice C is an exact pharmacological trap: Aripiprazole is actually a 5-HT1A <em>partial agonist</em> (which assists in anxiolytic and antidepressant action), not a full antagonist."
)

find_and_replace_choice(
    ps,
    "solely causes downward economic mobility without biological factors",
    "The social drift hypothesis, asserting that downward socioeconomic mobility fully accounts for the elevated clinical prevalence of schizophrenia without any genetic contribution.",
    "<strong>AAMC Distractor Trap Analysis:</strong> The revised choice models the genuine sociological debate (social drift vs social causation) without relying on extreme qualifier giveaways."
)

save_file('exam_ps90.js', ps, pfx, sfx)

# Also sync to exam_60min.js!
print("\nSyncing upgrades to exam_60min.js...")
