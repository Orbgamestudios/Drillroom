# Passage 1: Topic 540 — Antimycin A Inhibition of Complex III (Cytochrome bc1)
# Answer keys: 0 (A), 1 (B), 2 (C), 3 (D), 0 (A), 1 (B)

p1_data = {
  "id": "exam_bb90_5_p1",
  "sec": "B/B",
  "topic": "Antimycin A Inhibition of Complex III (Cytochrome bc1)",
  "sheet": None,
  "label": "Biological and Biochemical Foundations of Living Systems",
  "examId": "bb90_5",
  "passage": """<div class="ttl">Passage 1 (Questions 1&ndash;6)</div>
<p>The mitochondrial electron transport chain (ETC) harnesses redox potential gradients to drive oxidative phosphorylation. Complex III (the cytochrome $bc_1$ complex or ubiquinol:cytochrome $c$ oxidoreductase) occupies an obligatory bioenergetic junction within this pathway, coupling the oxidation of the lipophilic two-electron carrier ubiquinol ($\\text{QH}_2$) to the reduction of the hydrophilic one-electron carrier cytochrome $c$ via the Q-cycle mechanism.</p>
<p>Structural and crystallographic analyses reveal that Complex III possesses two distinct quinone-binding pockets situated on opposite sides of the inner mitochondrial membrane. The outer $Q_o$ pocket faces the intermembrane space (IMS) and is situated in proximity to the Rieske $[2\\text{Fe}-2\\text{S}]$ iron-sulfur cluster and heme $b_L$. The inner $Q_i$ pocket faces the mitochondrial matrix, adjacent to heme $b_H$. During the bifurcated oxidation of $\\text{QH}_2$ at the $Q_o$ center, one electron is routed to the Rieske center and onward to heme $c_1$ and cytochrome $c$, while the second electron travels across hemes $b_L$ and $b_H$ to the $Q_i$ site, reducing an oxidized ubiquinone to a semiquinone intermediate ($Q^{\\bullet-}$).</p>
<p>To investigate the mechanistic consequences of site-specific inhibition, researchers incubated isolated murine hepatic mitochondria in a polarographic respirometry chamber. Respiration was initiated with succinate and ADP (State 3 respiration). Investigators subsequently added antimycin A (a specific $Q_i$-site antagonist), myxothiazol (a competitive $Q_o$-site inhibitor), or the artificial bypass electron donor system ascorbate plus $N,N,N',N'$-tetramethyl-$p$-phenylenediamine (TMPD), which donates electrons directly to cytochrome $c$. Respiration rates, mitochondrial membrane potential ($\\Delta\\Psi_m$), superoxide emission (measured by MitoSOX fluorescence), and cytochrome redox states were quantified (Table 1).</p>
<table class="tbl">
  <caption>Table 1 Respirometry parameters, redox states, and superoxide generation in isolated hepatic mitochondria</caption>
  <thead>
    <tr><th>Condition</th><th>Substrate / Additions</th><th>Oxygen Consumption (nmol $\\text{O}_2$/min/mg)</th><th>$\\Delta\\Psi_m$ (mV)</th><th>Superoxide Rate (pmol/min/mg)</th><th>Cytochrome $b$ Redox</th><th>Cytochrome $c$ Redox</th></tr>
  </thead>
  <tbody>
    <tr><td>1 (Control)</td><td>Succinate + ADP</td><td>165 &plusmn; 8</td><td>175 &plusmn; 5</td><td>12 &plusmn; 2</td><td>35% reduced</td><td>68% reduced</td></tr>
    <tr><td>2</td><td>Succinate + ADP + Antimycin A</td><td>4 &plusmn; 1</td><td>55 &plusmn; 4</td><td>98 &plusmn; 7</td><td>96% reduced</td><td>3% reduced</td></tr>
    <tr><td>3</td><td>Succinate + ADP + Myxothiazol</td><td>3 &plusmn; 1</td><td>50 &plusmn; 3</td><td>8 &plusmn; 1</td><td>5% reduced</td><td>2% reduced</td></tr>
    <tr><td>4</td><td>Antimycin A + Ascorbate / TMPD</td><td>158 &plusmn; 7</td><td>168 &plusmn; 6</td><td>95 &plusmn; 6</td><td>95% reduced</td><td>92% reduced</td></tr>
    <tr><td>5</td><td>Antimycin A + FCCP</td><td>5 &plusmn; 1</td><td>10 &plusmn; 2</td><td>110 &plusmn; 8</td><td>97% reduced</td><td>2% reduced</td></tr>
  </tbody>
</table>""",
  "qs": [
    {
      "q": "Which molecular mechanism accounts for the observed spectrophotometric redox states of cytochromes b and c following antimycin A administration?",
      "ch": [
        "Antimycin A blocks electron transfer at the Qi site, leaving cytochrome b reduced while cytochrome c is oxidized by Complex IV.",
        "Antimycin A blocks electron release at the Qo site, keeping cytochrome b oxidized while cytochrome c accumulates donor electrons.",
        "Antimycin A binds cytochrome c oxidase, preventing electron exit from cytochrome c while oxidizing upstream cytochrome b hemes.",
        "Antimycin A uncouples the proton gradient, accelerating electron loss from cytochrome b while trapping cytochrome c in reduction."
      ],
      "a": 0,
      "e": "<strong>Antimycin A mechanism and cytochrome redox states:</strong> Antimycin A binds with nanomolar affinity to the matrix-facing $Q_i$ pocket of Complex III (cytochrome $bc_1$), blocking the oxidation of reduced heme $b_H$ by ubiquinone or semiquinone. Consequently, incoming electrons derived from succinate (via Complex II and the ubiquinol pool) continue to enter Complex III at the $Q_o$ site, transferring electrons to heme $b_L$ and heme $b_H$. Because exit through the $Q_i$ site is blocked, hemes $b_L$ and $b_H$ become stalled in a fully reduced state ($96\\%$ reduced). Simultaneously, downstream electron transport from cytochrome $c_1$ through cytochrome $c$ and Complex IV to molecular oxygen continues until those mobile carriers are fully oxidized ($3\\%$ reduced), after which oxygen consumption ceases because upstream electrons cannot replenish cytochrome $c$.<br><br><em>Distractor Traps:</em><br>&bull; B reverses the oxidation states of the cytochromes and describes a $Q_o$ inhibitor such as myxothiazol or stigmatellin rather than antimycin A.<br>&bull; C misattributes the molecular target of antimycin A to Complex IV (cytochrome $c$ oxidase), which is inhibited by cyanide, azide, and carbon monoxide.<br>&bull; D invents an uncoupling mechanism for antimycin A; uncouplers collapse $\\Delta\\Psi_m$ without inhibiting electron transfer complexes or trapping cytochrome $b$ in a reduced state."
    },
    {
      "q": "Why does the addition of ascorbate and TMPD restore the oxygen consumption rate in antimycin A-treated mitochondria?",
      "ch": [
        "Ascorbate and TMPD displace antimycin A from the Qi pocket, restoring normal Q-cycle turnover across the inner membrane.",
        "Ascorbate and TMPD donate electrons directly to cytochrome c, bypassing the Complex III block to reduce oxygen at Complex IV.",
        "Ascorbate and TMPD deliver electrons directly to ubiquinone, enabling Complex II to pump protons independently of Complex III.",
        "Ascorbate and TMPD function as chemical protonophores, dissipating membrane potential to drive Complex I electron transport."
      ],
      "a": 1,
      "e": "<strong>Bypass electron donor systems in respirometry:</strong> $N,N,N',N'$-tetramethyl-$p$-phenylenediamine (TMPD) is a membrane-permeant artificial redox mediator that can donate electrons directly to oxidized cytochrome $c$. Ascorbate acts as a stoichiometric reducing agent that continuously regenerates reduced TMPD. Because antimycin A blocks electron flow upstream at Complex III ($Q_i$ site), cytochrome $c$ and Complex IV remain functional but starved of electrons. Adding ascorbate/TMPD directly re-reduces cytochrome $c$ (from $3\\%$ to $92\\%$ reduced in Table 1), enabling Complex IV to resume transfer of electrons to $\\text{O}_2$ and translocate protons, thereby restoring oxygen consumption ($158\\text{ nmol }\\text{O}_2/\\text{min/mg}$) and regenerating membrane potential ($168\\text{ mV}$) despite the continued presence of antimycin A.<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly asserts that ascorbate/TMPD displace antimycin A; Table 1 shows that cytochrome $b$ remains $95\\%$ reduced and superoxide emission remains elevated ($95\\text{ pmol/min/mg}$), demonstrating that Complex III remains fully inhibited.<br>&bull; C incorrectly claims that electrons are delivered to ubiquinone and that Complex II pumps protons; Complex II does not pump protons, and delivering electrons to ubiquinone would still encounter the Complex III block.<br>&bull; D falsely characterizes ascorbate/TMPD as an uncoupling protonophore; uncouplers dissipate the proton gradient and abolish ATP synthesis without restoring cytochrome $c$ reduction."
    },
    {
      "q": "Based on the data in Table 1, why does antimycin A markedly increase superoxide emission whereas myxothiazol does not?",
      "ch": [
        "Antimycin A disrupts manganese superoxide dismutase activity, whereas myxothiazol activates catalase in the peroxisome.",
        "Antimycin A directly reduces dissolved oxygen at Complex II, whereas myxothiazol accelerates electron flow to cytochrome c.",
        "Antimycin A stabilizes the reactive semiquinone at the Qo site, whereas myxothiazol prevents semiquinone radical formation.",
        "Antimycin A oxidizes the iron-sulfur clusters in Complex I, whereas myxothiazol prevents proton translocation through Complex V."
      ],
      "a": 2,
      "e": "<strong>Mechanisms of reactive oxygen species generation at Complex III:</strong> Superoxide ($\\text{O}_2^{\\bullet-}$) production at Complex III occurs primarily when an unstable semiquinone radical intermediate ($Q_o^{\\bullet-}$) at the outer $Q_o$ binding pocket donates an unpaired electron directly to molecular oxygen. Antimycin A blocks the downstream $Q_i$ site, preventing electron clearance from heme $b_H$. Consequently, heme $b_L$ remains reduced and cannot accept electrons from the $Q_o$ pocket, causing the reactive semiquinone radical at the $Q_o$ site to persist and react with $\\text{O}_2$ (elevating superoxide to $98\\text{ pmol/min/mg}$). In contrast, myxothiazol competitively inhibits the initial binding and oxidation of $\\text{QH}_2$ at the $Q_o$ site itself, preventing the formation of the semiquinone intermediate altogether and thereby suppressing superoxide emission ($8\\text{ pmol/min/mg}$).<br><br><em>Distractor Traps:</em><br>&bull; A misattributes the elevated ROS to antioxidant enzyme inhibition; antimycin A inhibits Complex III, not superoxide dismutase, and peroxisomal catalase does not regulate intramitochondrial superoxide.<br>&bull; B erroneously places superoxide production at Complex II rather than the $Q_o$ site of Complex III.<br>&bull; D misidentifies the molecular targets; antimycin A acts at the $Q_i$ site of Complex III rather than oxidatively modifying Complex I or directly inhibiting Complex V."
    },
    {
      "q": "During one complete Q-cycle in Complex III, what is the net stoichiometry of protons translocated into the intermembrane space per pair of electrons reaching cytochrome c?",
      "ch": [
        "One proton is pumped from the matrix and one proton is released into the intermembrane space.",
        "Two protons are taken up from the matrix and two protons are released into the intermembrane space.",
        "Two protons are pumped across the bilayer with four protons consumed from the intermembrane space.",
        "Two protons are absorbed from the matrix and four protons are released into the intermembrane space."
      ],
      "a": 3,
      "e": "<strong>Proton and electron stoichiometry of the Q-cycle:</strong> In one complete Q-cycle, two molecules of ubiquinol ($\\text{QH}_2$) are oxidized at the outer $Q_o$ pocket. Each $\\text{QH}_2$ oxidation releases two protons into the intermembrane space (IMS), totaling $4\\text{ H}^+$ released into the IMS. From the four electrons liberated, two electrons travel sequentially via the Rieske iron-sulfur cluster and heme $c_1$ to reduce two molecules of mobile cytochrome $c$ (one electron each). The other two electrons travel across hemes $b_L$ and $b_H$ to the inner $Q_i$ pocket, where they reduce one molecule of ubiquinone ($Q$) back to $\\text{QH}_2$, consuming $2\\text{ H}^+$ from the mitochondrial matrix. Thus, for every pair of electrons delivered to cytochrome $c$, the net stoichiometry is the uptake of $2\\text{ H}^+$ from the matrix and the net translocation/release of $4\\text{ H}^+$ into the IMS.<br><br><em>Distractor Traps:</em><br>&bull; A reflects an incorrect $1:1$ stoichiometry that ignores the bifurcated mechanism of the Q-cycle.<br>&bull; B describes a standard linear proton pump with a $2\\text{ H}^+/2e^-$ stoichiometry, failing to account for the doubling of proton translocation achieved by recycling one quinone.<br>&bull; C reverses the spatial direction of proton consumption and translocation across the inner membrane."
    },
    {
      "q": "If mitochondria are treated simultaneously with antimycin A and myxothiazol, what change in superoxide emission is most likely observed relative to antimycin A alone?",
      "ch": [
        "Superoxide emission decreases significantly because myxothiazol blocks ubiquinol oxidation at the Qo site.",
        "Superoxide emission increases substantially because both quinone-binding pockets are simultaneously blocked.",
        "Superoxide emission remains unchanged because antimycin A irreversibly denatures the Rieske center.",
        "Superoxide emission drops to zero because the mitochondrial inner membrane becomes permeable to protons."
      ],
      "a": 0,
      "e": "<strong>Competitive inhibition of the Qo site suppresses antimycin A-induced ROS:</strong> Antimycin A induces massive superoxide generation because it blocks the $Q_i$ site, trapping a reactive semiquinone radical intermediate ($Q_o^{\\bullet-}$) in the $Q_o$ pocket. Myxothiazol binds competitively to the $Q_o$ pocket and prevents ubiquinol ($\\text{QH}_2$) from entering and transferring its first electron to the Rieske iron-sulfur cluster. When myxothiazol is added in conjunction with antimycin A, ubiquinol cannot be oxidized to the semiquinone at $Q_o$. As a result, the semiquinone radical is never formed, and superoxide emission decreases dramatically back to basal or below-basal levels.<br><br><em>Distractor Traps:</em><br>&bull; B assumes additive toxicity, failing to recognize that myxothiazol blocks the upstream enzymatic step required to form the radical intermediate generated by antimycin A.<br>&bull; C incorrectly assumes antimycin A causes irreversible structural denaturation of the Rieske protein; antimycin A binds non-covalently to the $Q_i$ pocket of cytochrome $b$.<br>&bull; D confuses enzyme inhibition with protonophore action; neither antimycin A nor myxothiazol renders the inner mitochondrial membrane permeabilized to protons."
    },
    {
      "q": "What bioenergetic consequence explains the collapse in mitochondrial membrane potential (ΔΨm) after antimycin A administration?",
      "ch": [
        "Reverse electron transfer through Complex II consumes the remaining proton gradient to regenerate matrix succinate.",
        "Proton pumping by Complexes III and IV ceases, allowing basal proton leak and uninhibited ATP synthase to discharge ΔΨm.",
        "Antimycin A acts as an electrogenic ionophore that directly translocates potassium cations into the matrix space.",
        "Cytochrome c detaches from the outer membrane and forms large pores that permit nonspecific proton equilibration."
      ],
      "a": 1,
      "e": "<strong>Collapse of membrane potential upon respiratory chain inhibition:</strong> The mitochondrial proton-motive force ($\\Delta p = \\Delta\\Psi_m - 59\\,\\Delta\\text{pH}$) is dynamically generated by active proton extrusion through Complexes I, III, and IV. In succinate-fueled mitochondria, proton translocation depends entirely on Complexes III ($4\\text{ H}^+/2e^-$) and IV ($2\\text{ H}^+/2e^-$). When antimycin A inhibits Complex III, electron transfer to cytochrome $c$ and Complex IV halts immediately, terminating all active proton pumping. The electrochemical gradient then rapidly dissipates due to basal inner membrane proton leak and the continued inward translocation of protons through the $F_0$ subunit of ATP synthase (which synthesizes ATP until ADP/substrate equilibrium is reached), collapsing $\\Delta\\Psi_m$ from $175\\text{ mV}$ to $55\\text{ mV}$.<br><br><em>Distractor Traps:</em><br>&bull; A invents an uncoupled reverse succinate synthesis mechanism; Complex II is not a proton pump and cannot consume the proton gradient to reduce fumarate to succinate under these conditions.<br>&bull; C misidentifies antimycin A as a potassium ionophore; valinomycin is an electrogenic potassium ionophore, whereas antimycin A is an ETC Complex III inhibitor.<br>&bull; D confuses cytochrome $c$ with pore-forming pro-apoptotic Bcl-2 family proteins (Bax/Bak) in the outer mitochondrial membrane; cytochrome $c$ is a peripheral electron shuttle on the outer surface of the inner membrane, not a channel."
    }
  ]
}
