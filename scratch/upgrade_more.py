import json
from upgrade_distractors import load_file, save_file, find_and_replace_choice

# B/B
bb, pfx, sfx = load_file('exam_bb90.js')
find_and_replace_choice(
    bb,
    "be completely abolished because GTP-&gamma;-S acts as a competitive inhibitor",
    "exhibit transient, self-limiting cAMP accumulation followed by rapid G&alpha;_s deactivation.",
    "<strong>AAMC Trap Analysis:</strong> Choice B is a normal-physiology trap: GTP-&gamma;-S is a non-hydrolyzable GTP analog that locks G&alpha;_s in a permanently active conformation, preventing the intrinsic GTPase activity from terminating cAMP synthesis."
)
save_file('exam_bb90.js', bb, pfx, sfx)

# P/S
ps, pfx, sfx = load_file('exam_ps90.js')
find_and_replace_choice(
    ps,
    "A completely flat horizontal line indicating behavioral extinction",
    "A steady, moderate response slope without post-reinforcement pauses",
    "<strong>AAMC Trap Analysis:</strong> Choice A describes a Variable Interval (VI) schedule, which produces steady, moderate rates of responding rather than the scalloped pattern of Fixed Interval (FI)."
)
find_and_replace_choice(
    ps,
    "Craving becomes solely governed by the prefrontal cortex while the nucleus accumbens undergoes complete atrophy",
    "Mesolimbic dopamine release increases during active drug consumption, but remains at baseline during conditioned cue exposure.",
    "<strong>AAMC Trap Analysis:</strong> Choice D is an inversion of incentive-sensitization: Robinson & Berridge demonstrated that dopamine sensitization causes conditioned environmental cues to trigger massive dopamine surges and intense craving, even when hedonic liking blunts."
)
save_file('exam_ps90.js', ps, pfx, sfx)

print("Remaining extreme distractors successfully replaced!")
