# Passage 3: Topic 542 — Oligomycin Inhibition of ATP Synthase F0 Subunit
# Answer keys: 1 (B), 2 (C), 0 (A), 3 (D), 0 (A), 2 (C)

p3_data = {
  "id": "exam_bb90_5_p3",
  "sec": "B/B",
  "topic": "Oligomycin Inhibition of ATP Synthase F0 Subunit",
  "sheet": None,
  "label": "Biological and Biochemical Foundations of Living Systems",
  "examId": "bb90_5",
  "passage": """<div class="ttl">Passage 3 (Questions 13&ndash;18)</div>
<p>Mitochondrial ATP synthase (Complex V) couples the transmembrane electrochemical proton-motive force ($\\Delta p = \\Delta\\Psi_m - 59\\,\\Delta\\text{pH}$) to the rotary mechanical synthesis of ATP from ADP and inorganic phosphate ($\\text{P}_i$). Complex V consists of two functional domains: the hydrophobic, membrane-embedded $F_0$ base and the hydrophilic, matrix-projecting $F_1$ catalytic headpiece.</p>
<p>The $F_0$ domain comprises a static subunit $a$ containing two aqueous half-channels and a cylindrical rotor composed of 8 to 10 hydrophobic $c$-subunits. Each $c$-subunit contains an essential carboxylate residue (glutamate 58 in mammals, Glu58) positioned midway through its transmembrane helix. Entry of a proton from the intermembrane space (IMS) half-channel protonates Glu58, neutralizing its negative charge and enabling the subunit to rotate into the hydrophobic lipid bilayer. Upon completing a revolution, Glu58 faces the matrix half-channel, where the lower proton concentration triggers deprotonation. This rotary translocation turns the central $\\gamma\\epsilon$ stalk, which sequentially alters the conformation of the three catalytic $\\beta$ subunits in the $F_1$ hexamer ($\\alpha_3\\beta_3$) through Open, Loose, and Tight states to synthesize and release ATP.</p>
<p>Oligomycin, a macrolide antibiotic, binds specifically at the interface between the $c$-ring and the $a$-subunit in the $F_0$ domain, interacting directly with Glu58 to block proton movement. Researchers examined the bioenergetic consequences of oligomycin inhibition using isolated cardiac mitochondria fueled by succinate in the presence of rotenone. ADP was added to establish State 3 respiration. Investigators then evaluated the effects of oligomycin (1 $\\mu\\text{M}$), the protonophore uncoupler carbonyl cyanide $p$-trifluoromethoxyphenylhydrazone (FCCP), and a knock-in mouse strain harboring a homozygous $c$-subunit mutation (E58Q) (Table 1).</p>
<table class="tbl">
  <caption>Table 1 Respirometry parameters, proton gradient, and ATP synthesis in isolated cardiac mitochondria</caption>
  <thead>
    <tr><th>Condition</th><th>Genotype / Additions</th><th>Oxygen Consumption (nmol $\\text{O}_2$/min/mg)</th><th>ATP Synthesis Rate (nmol ATP/min/mg)</th><th>$\\Delta\\Psi_m$ (mV)</th><th>$\\Delta\\text{pH}$ (units)</th><th>Respiratory State</th></tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>Wild-type + Succinate</td><td>28 &plusmn; 2</td><td>2 &plusmn; 1</td><td>160 &plusmn; 4</td><td>0.82 &plusmn; 0.04</td><td>State 2 (Basal)</td></tr>
    <tr><td>2</td><td>Wild-type + Succinate + ADP</td><td>175 &plusmn; 8</td><td>410 &plusmn; 15</td><td>142 &plusmn; 4</td><td>0.65 &plusmn; 0.03</td><td>State 3 (Active)</td></tr>
    <tr><td>3</td><td>Condition 2 + Oligomycin</td><td>32 &plusmn; 3</td><td>4 &plusmn; 1</td><td>185 &plusmn; 5</td><td>0.98 &plusmn; 0.04</td><td>Oligomycin-arrested</td></tr>
    <tr><td>4</td><td>Condition 3 + FCCP</td><td>215 &plusmn; 9</td><td>0 &plusmn; 0</td><td>15 &plusmn; 2</td><td>0.05 &plusmn; 0.01</td><td>Uncoupled State</td></tr>
    <tr><td>5</td><td>E58Q Knock-in + Succinate + ADP</td><td>30 &plusmn; 3</td><td>0 &plusmn; 0</td><td>182 &plusmn; 5</td><td>0.95 &plusmn; 0.04</td><td>Insensitive Mutant</td></tr>
  </tbody>
</table>""",
  "qs": [
    {
      "q": "Which statement accurately describes the direct molecular target and inhibitory mechanism of oligomycin?",
      "ch": [
        "Oligomycin binds the F1 catalytic beta subunit, preventing the spontaneous condensation of bound ADP and inorganic phosphate.",
        "Oligomycin binds the F0 c-subunit ring interface, locking the essential carboxylate residue and blocking proton translocation.",
        "Oligomycin binds the adenine nucleotide translocase, irreversibly halting the antiport of matrix ATP for cytosolic ADP.",
        "Oligomycin binds the central stalk gamma subunit, preventing conformational switching between open, loose, and tight states."
      ],
      "a": 1,
      "e": "<strong>Molecular mechanism and target of oligomycin:</strong> Oligomycin is a macrolide antibiotic whose binding site is located within the membrane-embedded $F_0$ sector of ATP synthase. Specifically, oligomycin binds at the interface between the proton-conducting subunit $a$ and the rotating $c$-subunit ring, directly contacting the carboxyl side chain of the critical glutamate residue (Glu58 in mammals, Asp61 in yeast/bacteria). By sterically blocking the proton transfer path and locking Glu58 in an unprotonated or immobilized state, oligomycin prevents the mechanical rotation of the $c$-ring, completely arresting proton translocation from the intermembrane space into the matrix.<br><br><em>Distractor Traps:</em><br>&bull; A describes direct inhibition of the catalytic $F_1$ headpiece; aurovertin and efrapeptin target $F_1$, whereas oligomycin specifically targets $F_0$.<br>&bull; C describes inhibition of the adenine nucleotide translocase (ANT), which is targeted by atractyloside or bongkrekic acid, not oligomycin.<br>&bull; D misidentifies the central rotor stalk ($\\gamma\\epsilon$) as the binding site; oligomycin binds within the hydrophobic membrane bilayer at the $c$-ring, not the hydrophilic matrix stalk."
    },
    {
      "q": "Why does the oxygen consumption rate sharply decline from State 3 following the addition of oligomycin (Condition 3)?",
      "ch": [
        "Oligomycin directly oxidizes the heme groups of cytochrome c oxidase, terminating final electron transfer to molecular oxygen.",
        "Proton accumulation in the matrix raises matrix pH beyond the optimal catalytic range of citric acid cycle dehydrogenases.",
        "Cessation of proton entry through F0 hyperpolarizes the membrane, creating electrochemical backpressure that stalls the ETC.",
        "Oligomycin activates uncoupling protein 1 in the inner mitochondrial membrane, causing extensive loss of membrane integrity."
      ],
      "a": 2,
      "e": "<strong>Respiratory control and thermodynamic backpressure:</strong> In coupled mitochondria, electron transport and ATP synthesis are obligatorily coupled. When ADP is added (State 3), protons flow rapidly into the matrix through $F_0$ to drive ATP synthesis, partially discharging the proton gradient ($\\Delta\\Psi_m$ drops to $142\\text{ mV}$) and relieving the resistance against proton pumping. When oligomycin blocks $F_0$, proton influx stops immediately. However, Complexes III and IV continue pumping protons until the electrochemical gradient reaches a maximal thermodynamic ceiling (hyperpolarization to $185\\text{ mV}$ and $\\Delta\\text{pH} = 0.98$). The free energy required to pump an additional proton against this steep gradient ($\\Delta G_{\\text{pump}} = zF\\Delta\\Psi_m + 2.3RT\\Delta\\text{pH}$) exceeds the free energy released by succinate oxidation, creating thermodynamic backpressure that halts electron flow and drops the oxygen consumption rate from $175$ to $32\\text{ nmol }\\text{O}_2/\\text{min/mg}$.<br><br><em>Distractor Traps:</em><br>&bull; A erroneously attributes a direct inhibitory effect on Complex IV (cytochrome $c$ oxidase) to oligomycin; oligomycin has no direct chemical affinity for respiratory complexes.<br>&bull; B describes matrix alkalinization as enzyme denaturing; while matrix pH rises slightly, respiratory inhibition is due to electrochemical backpressure, not dehydrogenase denaturation.<br>&bull; D invents uncoupling protein 1 (UCP1) activation; UCP1 dissipates the proton gradient to stimulate respiration, whereas oligomycin causes membrane hyperpolarization and respiratory arrest."
    },
    {
      "q": "Based on Table 1, why does subsequent addition of FCCP (Condition 4) trigger maximal oxygen consumption without restoring ATP synthesis?",
      "ch": [
        "FCCP translocates protons across the lipid bilayer, relieving thermodynamic backpressure on the ETC without passing through F0.",
        "FCCP allosterically displaces oligomycin from the c-subunit ring, reactivating rotary catalysis in the F1 catalytic headpiece.",
        "FCCP hydrolyzes matrix ATP to generate inorganic phosphate, fueling substrate-level phosphorylation independently of Complex V.",
        "FCCP directly transfers electrons from ubiquinol to dissolved molecular oxygen, bypassing Complexes III and IV entirely."
      ],
      "a": 0,
      "e": "<strong>Mechanism of chemical uncoupling by protonophores:</strong> Carbonyl cyanide $p$-trifluoromethoxyphenylhydrazone (FCCP) is an amphipathic, lipophilic weak acid that acts as a protonophore. It binds protons in the intermembrane space, diffuses across the hydrophobic core of the inner mitochondrial membrane as a neutral species, and releases protons into the alkaline matrix, thereby shuttling protons down their electrochemical gradient independently of the $F_0$ channel. This collapses both $\\Delta\\Psi_m$ (to $15\\text{ mV}$) and $\\Delta\\text{pH}$ (to $0.05$). Relieved of thermodynamic backpressure, respiratory complexes pump protons at their maximum uninhibited velocity, driving oxygen consumption to $215\\text{ nmol }\\text{O}_2/\\text{min/mg}$. However, because the proton gradient is dissipated across the bilayer and $F_0$ remains blocked by oligomycin, no protons drive the rotary catalysis of ATP synthase, resulting in zero ATP synthesis ($0\\text{ nmol/min/mg}$).<br><br><em>Distractor Traps:</em><br>&bull; B incorrectly claims that FCCP displaces oligomycin; FCCP operates as an independent membrane-permeant carrier and does not reverse oligomycin binding to $F_0$.<br>&bull; C describes ATP hydrolysis and substrate-level phosphorylation, which does not explain why oxygen consumption is accelerated.<br>&bull; D invents a short-circuit bypass where FCCP transfers electrons directly to oxygen; FCCP transports protons ($H^+$), not electrons ($e^-$)."
    },
    {
      "q": "What biochemical consequence explains why the homozygous E58Q c-ring knock-in mutant exhibits zero ATP synthesis and oligomycin insensitivity?",
      "ch": [
        "Glutamine substitution prevents assembly of the F1 alpha3beta3 hexamer, dislodging the catalytic headpiece into the matrix.",
        "Glutamine introduces a permanent positive charge that repels incoming matrix hydronium ions from entering the a-subunit channel.",
        "Glutamine undergoes spontaneous deamidation to aspartate, forming an irreversible covalent ester bond with the central stalk.",
        "Glutamine cannot undergo reversible protonation and deprotonation, abolishing proton transport and preventing oligomycin binding."
      ],
      "a": 3,
      "e": "<strong>Functional requirement of a titratable carboxylate in the c-ring:</strong> The mechanical rotation of the $c$-ring requires a strictly conserved, titratable carboxyl group (glutamate in mammals, Glu58; aspartate in bacteria, Asp61). This residue alternates between an unprotonated charged state ($\\text{COO}^-$) in the aqueous subunit $a$ half-channels and a protonated uncharged state ($\\text{COOH}$) in the lipid membrane. In the E58Q mutant, glutamine has an uncharged carboxamide side chain ($-\\text{CONH}_2$) that cannot accept or release a proton under physiological conditions ($pK_a > 14$). Consequently, the $c$-ring cannot undergo reversible protonation-driven rotation, abolishing proton translocation and ATP synthesis ($0\\text{ nmol/min/mg}$). Furthermore, because oligomycin requires specific hydrogen-bonding and electrostatic interactions with the native carboxylate of Glu58, the E58Q substitution eliminates the high-affinity drug-binding pocket, rendering the mutant genetically resistant to oligomycin.<br><br><em>Distractor Traps:</em><br>&bull; A assumes that an $F_0$ membrane mutation prevents assembly of the soluble $F_1$ catalytic domain; $F_1$ hexamers assemble normally and attach to the stalk.<br>&bull; B incorrectly assigns a positive charge to glutamine; glutamine is a neutral, polar amino acid with an amide side chain, not a positively charged basic residue.<br>&bull; C describes non-enzymatic ester crosslinking with the central stalk, which does not occur with glutamine side chains."
    },
    {
      "q": "According to the chemiosmotic hypothesis, why does the mitochondrial membrane potential (ΔΨm) increase from 142 mV in State 3 to 185 mV after oligomycin treatment?",
      "ch": [
        "Protons pumped by Complexes III and IV cannot re-enter the matrix, accumulating positive charge in the intermembrane space.",
        "Oligomycin activates potassium channels, causing rapid electrogenic efflux of positively charged potassium ions into the IMS.",
        "Reverse proton pumping by Complex II actively drives hydronium ions into the matrix against the existing chemical gradient.",
        "Depletion of matrix ATP eliminates negative charge shielding, unmasking an artificial voltage artifact on the electrode."
      ],
      "a": 0,
      "e": "<strong>Hyperpolarization of the inner mitochondrial membrane upon F0 blockade:</strong> In the chemiosmotic model formulated by Peter Mitchell, the mitochondrial membrane potential ($\\Delta\\Psi_m$, positive outside in the IMS, negative inside the matrix) represents the electrical component of the proton-motive force. During State 3 (Condition 2), continuous inward proton flux through the $F_0$ rotor consumes electrical charge, depressing $\\Delta\\Psi_m$ to $142\\text{ mV}$. When oligomycin completely seals the $F_0$ pathway, protons pumped outward by the respiratory chain (Complexes III and IV) can no longer re-enter the matrix. As positively charged hydronium ions ($H^+$) accumulate in the intermembrane space without charge compensation, the electrical potential across the inner membrane hyperpolarizes to $185\\text{ mV}$.<br><br><em>Distractor Traps:</em><br>&bull; B describes potassium efflux via channels; oligomycin does not gate ion channels, and $\\Delta\\Psi_m$ is generated by proton extrusion via the ETC.<br>&bull; C incorrectly attributes reverse proton pumping to Complex II; Complex II does not span the membrane as a proton pump and cannot pump hydronium ions in either direction.<br>&bull; D invents an electrode artifact based on ATP charge shielding; $\\Delta\\Psi_m$ is an authentic electrochemical gradient measured using potentiometric lipophilic cations (such as TMRM or safranin)."
    },
    {
      "q": "How does the bioenergetic profile of oligomycin-arrested mitochondria fundamentally contrast with that of uncoupler-treated mitochondria?",
      "ch": [
        "Oligomycin collapses the proton gradient while accelerating respiration; uncouplers maximize ΔΨm while stalling respiration.",
        "Oligomycin sustains continuous ATP synthesis at reduced rates; uncouplers completely halt respiration by inhibiting Complex I.",
        "Oligomycin hyperpolarizes the membrane and suppresses respiration; uncouplers collapse the gradient and maximize respiration.",
        "Oligomycin selectively inhibits Complex II electron transfer; uncouplers inhibit the phosphate carrier in the inner membrane."
      ],
      "a": 2,
      "e": "<strong>Bioenergetic contrast between ATP synthase inhibitors and uncouplers:</strong> Both oligomycin and uncouplers (such as FCCP or 2,4-dinitrophenol) abolish net oxidative phosphorylation (ATP synthesis rate $\\approx 0$), but they do so through opposite bioenergetic mechanisms. Oligomycin inhibits the terminal proton translocator ($F_0$), causing protons to back up across the inner membrane; this maximizes $\\Delta\\Psi_m$ (hyperpolarization to $185\\text{ mV}$) and represses respiration ($32\\text{ nmol }\\text{O}_2/\\text{min/mg}$) via thermodynamic backpressure. In contrast, uncouplers provide an artificial, low-resistance conduit for protons through the lipid bilayer; this completely discharges and collapses $\\Delta\\Psi_m$ (to $15\\text{ mV}$) and $\\Delta\\text{pH}$, uncoupling electron transport from phosphorylation and accelerating respiration to its absolute maximum unconstrained rate ($215\\text{ nmol }\\text{O}_2/\\text{min/mg}$).<br><br><em>Distractor Traps:</em><br>&bull; A completely reverses the biophysical effects of oligomycin and uncouplers on membrane potential and respiration.<br>&bull; B erroneously asserts that oligomycin allows continued ATP synthesis and that uncouplers inhibit Complex I; uncouplers accelerate respiration and do not directly inhibit respiratory complexes.<br>&bull; D misidentifies the molecular targets; oligomycin inhibits Complex V ($F_0$), not Complex II, and uncouplers dissipate the proton gradient rather than targeting the phosphate carrier."
    }
  ]
}
