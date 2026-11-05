# Passage 2: Topic 541 — Rotenone and Amytal Inhibition of Complex I (NADH Dehydrogenase)
# Answer keys: 2 (C), 3 (D), 0 (A), 1 (B), 2 (C), 3 (D)

p2_data = {
  "id": "exam_bb90_5_p2",
  "sec": "B/B",
  "topic": "Rotenone and Amytal Inhibition of Complex I (NADH Dehydrogenase)",
  "sheet": None,
  "label": "Biological and Biochemical Foundations of Living Systems",
  "examId": "bb90_5",
  "passage": """<div class="ttl">Passage 2 (Questions 7&ndash;12)</div>
<p>Mitochondrial Complex I (NADH:ubiquinone oxidoreductase) is an L-shaped multiprotein assembly composed of 45 subunits with a hydrophilic peripheral arm extending into the matrix and a hydrophobic arm embedded in the inner mitochondrial membrane. Complex I catalyzes the oxidation of matrix NADH by ubiquinone ($Q$), coupling the transfer of two electrons to the vectorial extrusion of four protons into the intermembrane space:</p>
<p>$$\\text{NADH} + \\text{H}^+ + Q + 4\\text{ H}^+_{\\text{matrix}} \\rightarrow \\text{NAD}^+ + \\text{QH}_2 + 4\\text{ H}^+_{\\text{IMS}}$$</p>
<p>NADH binds near the tip of the peripheral arm, transferring a hydride ion ($:H^-$) to flavin mononucleotide (FMN). Electrons subsequently travel down an intramolecular wire composed of seven iron-sulfur ($Fe-S$) clusters to the terminal high-potential cluster N2. From cluster N2, electrons are delivered to ubiquinone residing within a narrow hydrophobic tunnel located at the interface between the peripheral arm and membrane domain subunits (ND1, PSST, and TYKY).</p>
<p>Rotenone (a plant-derived isoflavonoid) and amytal (a substituted barbiturate) act as potent, selective inhibitors of Complex I by binding within the ubiquinone-binding pocket, sterically occluding quinone reduction. To evaluate the metabolic consequences of Complex I blockade, researchers performed high-resolution respirometry on isolated rat cerebral cortical mitochondria. Respiration was supported by either Complex I-linked substrates (pyruvate + malate, generating NADH) or Complex II-linked substrates (succinate, generating $\\text{FADH}_2$). Respiration rates, ATP synthesis, matrix $\\text{NADH}/\\text{NAD}^+$ ratios, and neuronal lactate-to-pyruvate ratios were measured (Table 1).</p>
<table class="tbl">
  <caption>Table 1 High-resolution respirometry and biochemical parameters in isolated cerebral mitochondria and cortical neurons</caption>
  <thead>
    <tr><th>Condition</th><th>Substrates / Additions</th><th>Oxygen Consumption (nmol $\\text{O}_2$/min/mg)</th><th>ATP Synthesis Rate (nmol ATP/min/mg)</th><th>Matrix $\\text{NADH}/\\text{NAD}^+$ Ratio</th><th>Neuronal Lactate/Pyruvate Ratio</th></tr>
  </thead>
  <tbody>
    <tr><td>1 (Control)</td><td>Pyruvate + Malate + ADP</td><td>142 &plusmn; 6</td><td>320 &plusmn; 14</td><td>0.22 &plusmn; 0.03</td><td>12 &plusmn; 1</td></tr>
    <tr><td>2</td><td>Pyruvate + Malate + ADP + Rotenone</td><td>6 &plusmn; 1</td><td>8 &plusmn; 2</td><td>4.85 &plusmn; 0.25</td><td>86 &plusmn; 5</td></tr>
    <tr><td>3</td><td>Pyruvate + Malate + ADP + Amytal</td><td>8 &plusmn; 2</td><td>12 &plusmn; 3</td><td>4.60 &plusmn; 0.22</td><td>82 &plusmn; 6</td></tr>
    <tr><td>4</td><td>Condition 2 + Succinate</td><td>185 &plusmn; 8</td><td>265 &plusmn; 12</td><td>4.70 &plusmn; 0.20</td><td>18 &plusmn; 2</td></tr>
    <tr><td>5</td><td>Condition 2 + Ascorbate / TMPD</td><td>170 &plusmn; 7</td><td>160 &plusmn; 9</td><td>4.75 &plusmn; 0.21</td><td>24 &plusmn; 3</td></tr>
  </tbody>
</table>""",
  "qs": [
    {
      "q": "Which biochemical interaction explains why both rotenone and amytal specifically abolish respiration driven by pyruvate and malate?",
      "ch": [
        "Rotenone and amytal covalently alkylate the flavin mononucleotide cofactor, preventing initial hydride acceptance from NADH.",
        "Rotenone and amytal bind the dicarboxylate carrier, blocking mitochondrial transport of pyruvate and malate into the matrix.",
        "Rotenone and amytal occupy the ubiquinone-binding pocket, halting electron transfer from terminal cluster N2 to ubiquinone.",
        "Rotenone and amytal deplete the inner membrane cardiolipin pool, disassembling Complex I into isolated peripheral subunits."
      ],
      "a": 2,
      "e": "<strong>Molecular mechanism of Complex I inhibition by rotenone and amytal:</strong> Both rotenone and amobarbital (amytal) bind with high affinity inside the hydrophobic ubiquinone-binding cavity of Complex I, situated at the junction of the hydrophilic peripheral arm (subunits PSST and TYKY) and the membrane domain (subunit ND1). By occluding this tunnel, they prevent mobile ubiquinone ($Q$) from accessing the terminal iron-sulfur center (cluster N2). Consequently, electrons derived from NADH cannot be transferred to the coenzyme Q pool, stalling Complex I in a fully reduced state and halting upstream oxidation of NADH generated from pyruvate and malate.<br><br><em>Distractor Traps:</em><br>&bull; A describes alkylating agents such as diphenyleneiodonium (DPI) that target flavin groups, whereas rotenone and amytal bind non-covalently in the quinone pocket.<br>&bull; B misattributes inhibition to the dicarboxylate carrier or mitochondrial pyruvate carrier (MPC); rotenone directly inhibits respiratory Complex I rather than substrate transport.<br>&bull; D invents cardiolipin depletion and complex disassembly; rotenone binds reversibly and non-destructively to an intact holocomplex without requiring subunit dissociation."
    },
    {
      "q": "Why does the addition of succinate completely rescue the oxygen consumption rate in rotenone-treated mitochondria?",
      "ch": [
        "Succinate allosterically displaces rotenone from the Complex I ubiquinone pocket, restoring NADH oxidation across the chain.",
        "Succinate dehydrogenase hydrolyzes matrix ATP, driving reverse proton pumping to bypass blocked Complex I electron transfer.",
        "Succinate transfers electrons directly to cytochrome c oxidase, circumventing all upstream quinone pools and iron-sulfur centers.",
        "Succinate delivers reducing equivalents directly to ubiquinone via Complex II, bypassing the blocked Complex I entry pathway."
      ],
      "a": 3,
      "e": "<strong>Substrate bypass via Complex II in Complex I-inhibited mitochondria:</strong> Electrons enter the mitochondrial respiratory chain via two independent entry gates: Complex I (which oxidizes NADH) and Complex II (succinate dehydrogenase, which oxidizes succinate to fumarate). Complex II utilizes an enzyme-bound FAD cofactor and three iron-sulfur clusters to reduce ubiquinone ($Q$) to ubiquinol ($\\text{QH}_2$) completely independently of Complex I. When rotenone blocks Complex I, adding succinate (Condition 4) supplies reducing equivalents directly into the ubiquinone pool via Complex II. These electrons flow unhindered through Complex III, cytochrome $c$, and Complex IV to molecular oxygen, restoring robust oxygen consumption ($185\\text{ nmol }\\text{O}_2/\\text{min/mg}$) and ATP synthesis ($265\\text{ nmol ATP/min/mg}$).<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly claims succinate displaces rotenone; Table 1 shows matrix $\\text{NADH}/\\text{NAD}^+$ remains elevated at $4.70$, confirming that Complex I remains completely inhibited.<br>&bull; B describes ATP-driven reverse electron flow rather than forward oxidative phosphorylation fueled by succinate oxidation.<br>&bull; C describes artificial electron donors like ascorbate/TMPD, whereas succinate reduces ubiquinone upstream of Complex III, not cytochrome $c$ oxidase directly."
    },
    {
      "q": "Based on Table 1, what metabolic consequence results from the dramatic accumulation of matrix NADH following Complex I inhibition?",
      "ch": [
        "High NADH/NAD+ allosterically inhibits isocitrate dehydrogenase and alpha-ketoglutarate dehydrogenase, stalling TCA cycle flux.",
        "High NADH/NAD+ allosterically activates pyruvate carboxylase, accelerating anaplerotic synthesis of matrix oxaloacetate.",
        "High NADH/NAD+ promotes rapid non-enzymatic decarboxylation of acetyl-CoA, diverting carbons into mitochondrial ketogenesis.",
        "High NADH/NAD+ stimulates succinate dehydrogenase expression, doubling electron throughput to Complex III and cytochrome c."
      ],
      "a": 0,
      "e": "<strong>Feedback allosteric regulation of the citric acid cycle by NADH:</strong> In uninhibited mitochondria, the matrix $\\text{NADH}/\\text{NAD}^+$ ratio is maintained at low steady-state levels ($0.22$). Blocking Complex I prevents the regeneration of $\\text{NAD}^+$, causing matrix NADH to accumulate ($4.85$ in Condition 2). High concentrations of NADH and an elevated $\\text{NADH}/\\text{NAD}^+$ ratio exert potent negative allosteric feedback on key regulatory enzymes of the citric acid cycle, including the pyruvate dehydrogenase complex, isocitrate dehydrogenase, and $\\alpha$-ketoglutarate dehydrogenase. Additionally, the highly endergonic malate dehydrogenase reaction ($\\text{L-malate} + \\text{NAD}^+ \\rightleftharpoons \\text{oxaloacetate} + \\text{NADH} + \\text{H}^+$) is pushed strongly in reverse by Le Chatelier's principle, depleting oxaloacetate and arresting citric acid cycle flux.<br><br><em>Distractor Traps:</em><br>&bull; B misidentifies the allosteric effector of pyruvate carboxylase; pyruvate carboxylase is activated by acetyl-CoA, not by NADH.<br>&bull; C describes non-enzymatic decarboxylation of acetyl-CoA, which does not occur biochemically; ketogenesis requires enzymatic condensation of acetyl-CoA by thiolase and HMG-CoA synthase.<br>&bull; D invents immediate transcriptional induction of Complex II; acute respirometry experiments reflect rapid allosteric and thermodynamic responses, not nuclear gene expression changes."
    },
    {
      "q": "Why is the maximal rate of ATP synthesis lower during succinate respiration (Condition 4) than during uninhibited pyruvate/malate respiration (Condition 1)?",
      "ch": [
        "Succinate oxidation generates only one matrix proton, which is insufficient to drive the c-ring rotation of ATP synthase.",
        "Complex II does not pump protons, yielding fewer translocated protons per electron pair than the Complex I-driven pathway.",
        "Succinate competitively inhibits the adenine nucleotide translocase, slowing the exchange of matrix ATP for cytosolic ADP.",
        "Complex II requires stoichiometric consumption of ATP to oxidize succinate, reducing the net yield of phosphorylated ADP."
      ],
      "a": 1,
      "e": "<strong>Proton pumping stoichiometry and P/O ratio differences:</strong> Complete oxidation of one pair of electrons entering at Complex I (via pyruvate/malate-derived NADH) results in the translocation of 10 protons across the inner mitochondrial membrane ($4\\text{ H}^+$ from Complex I, $4\\text{ H}^+$ from Complex III, and $2\\text{ H}^+$ from Complex IV), yielding approximately $2.5\\text{ ATP}$ per pair of electrons. In contrast, electrons entering via Complex II (succinate-derived $\\text{FADH}_2$) bypass Complex I entirely. Because Complex II does not translocate any protons across the membrane, only 6 protons are pumped per electron pair ($4\\text{ H}^+$ from Complex III and $2\\text{ H}^+$ from Complex IV), yielding approximately $1.5\\text{ ATP}$ per pair of electrons. Thus, for a given respiratory rate, succinate generates less proton-motive force and sustains a lower rate of ATP synthesis ($265\\text{ vs } 320\\text{ nmol ATP/min/mg}$).<br><br><em>Distractor Traps:</em><br>&bull; A invents a single-proton yield and misunderstands ATP synthase mechanics; proton translocation is performed by respiratory complexes, not the succinate molecule itself.<br>&bull; C incorrectly claims succinate inhibits the adenine nucleotide translocase (ANT); ANT is specifically inhibited by atractyloside or bongkrekic acid, not succinate.<br>&bull; D falsely asserts that Complex II consumes ATP; the oxidation of succinate to fumarate is exergonic ($\\Delta G^{\\circ\\prime} \\approx -6\\text{ kJ/mol}$) and coupled to FAD reduction without requiring ATP."
    },
    {
      "q": "What accounts for the marked elevation in the neuronal lactate-to-pyruvate ratio observed after exposure to rotenone or amytal?",
      "ch": [
        "Rotenone stimulates pyruvate kinase, accelerating phosphoenolpyruvate conversion to pyruvate beyond mitochondrial capacity.",
        "Rotenone induces mitochondrial membrane permeability transition, releasing cytochrome c to activate cytosolic caspases.",
        "Cytosolic NADH accumulation drives lactate dehydrogenase to reduce pyruvate to lactate to regenerate NAD+ for glycolysis.",
        "Rotenone directly inhibits hepatic glucose-6-phosphatase, trapping glycolytic intermediates inside cerebral cortical cells.",
        ],
      "a": 2,
      "e": "<strong>Lactate dehydrogenase and cytosolic redox balancing:</strong> When Complex I is inhibited, mitochondrial re-oxidation of cytosolic NADH (via the malate-aspartate and glycerol-3-phosphate shuttles) ceases because the mitochondrial electron transport chain is blocked upstream. As cytosolic NADH accumulates, the cytosolic $\\text{NADH}/\\text{NAD}^+$ ratio increases dramatically. To sustain glycolytic ATP generation at the glyceraldehyde-3-phosphate dehydrogenase (GAPDH) step, which requires continuous $\\text{NAD}^+$ availability, lactate dehydrogenase (LDH) shifts its thermodynamic equilibrium to rapidly reduce pyruvate to L-lactate: $\\text{pyruvate} + \\text{NADH} + \\text{H}^+ \\rightleftharpoons \\text{lactate} + \\text{NAD}^+$. This conversion drives up the lactate-to-pyruvate ratio from $12$ to $>80$, resulting in cellular lactic acidosis.<br><br><em>Distractor Traps:</em><br>&bull; A describes allosteric activation of pyruvate kinase by fructose-1,6-bisphosphate, which does not explain why lactate specifically accumulates relative to pyruvate.<br>&bull; B describes the apoptotic cascade triggered by cytochrome $c$ release, which occurs downstream of severe prolonged stress but does not directly govern the enzymatic equilibrium of LDH.<br>&bull; D misattributes inhibition to glucose-6-phosphatase, which is an enzyme of gluconeogenesis found in liver and kidney, not brain, and is unaffected by rotenone."
    },
    {
      "q": "In the electron transport sequence within Complex I, which cofactor serves as the immediate electron acceptor for the terminal iron-sulfur cluster N2?",
      "ch": [
        "The mobile electron carrier cytochrome c",
        "The binuclear iron center of heme a3",
        "The enzyme-bound flavin mononucleotide",
        "The lipophilic electron carrier ubiquinone"
      ],
      "a": 3,
      "e": "<strong>Intramolecular electron transfer pathway in Complex I:</strong> The precise sequence of redox centers in Complex I begins with matrix NADH donating two electrons as a hydride ion to the flavin mononucleotide (FMN) prosthetic group: $\\text{NADH} + \\text{H}^+ + \\text{FMN} \\rightarrow \\text{NAD}^+ + \\text{FMNH}_2$. Electrons then migrate sequentially through a series of iron-sulfur centers: $\\text{FMN} \\rightarrow \\text{N3} \\rightarrow \\text{N1b} \\rightarrow \\text{N4} \\rightarrow \\text{N5} \\rightarrow \\text{N6a} \\rightarrow \\text{N6b} \\rightarrow \\text{N2}$. Cluster N2 is the most electropositive $Fe-S$ center ($E^{\\circ\\prime} \\approx -140\\text{ mV}$) in Complex I and donates electrons directly to the physiological acceptor, ubiquinone ($Q$, $E^{\\circ\\prime} \\approx +100\\text{ mV}$), residing in the hydrophobic quinone tunnel.<br><br><em>Distractor Traps:</em><br>&bull; A refers to cytochrome $c$, which serves as the electron acceptor for Complex III and electron donor for Complex IV, not Complex I.<br>&bull; B refers to heme $a_3$, which forms the oxygen-reducing binuclear center in Complex IV (along with $\\text{Cu}_B$).<br>&bull; C describes the initial electron acceptor that accepts electrons from NADH at the top of the peripheral arm, not the downstream acceptor for cluster N2."
    }
  ]
}
