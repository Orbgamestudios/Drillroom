# Passage 5: Topic 527 — Allosteric Feedback Inhibition: ATCase and CTP / ATP Modulation
# Answer keys: 0 (A), 3 (D), 2 (C), 1 (B), 0 (A), 2 (C)

p5_data = {
  "id": "exam_bb90_4_p5",
  "sec": "B/B",
  "topic": "Allosteric Feedback Inhibition: ATCase and CTP / ATP Modulation",
  "sheet": 5,
  "label": "Biological and Biochemical Foundations of Living Systems",
  "examId": "bb90_4",
  "passage": """<div class="ttl">Passage 5 (Questions 25&ndash;30)</div>
<p>Metabolic homeostasis requires precise coordination between biosynthetic pathways to avoid wasteful accumulation of intermediates. Aspartate transcarbamoylase (ATCase) from <i>Escherichia coli</i> serves as a paradigm of allosteric regulation and end-product feedback inhibition. ATCase catalyzes the committed step of <i>de novo</i> pyrimidine nucleotide biosynthesis: the condensation of carbamoyl phosphate and L-aspartate to yield N-carbamoyl-L-aspartate and inorganic phosphate ($P_i$).</p>
<p>Native ATCase is a dodecameric complex ($c_6r_6$, molecular mass $\\sim 310\\;\\text{kDa}$) organized as two catalytic trimers ($2 \\times c_3$) held together by three regulatory dimers ($3 \\times r_2$). Each regulatory polypeptide contains a structural domain with a structural zinc atom coordinated by four cysteine residues, as well as an allosteric binding pocket for nucleotide effectors. The enzyme exhibits positive cooperativity (homotropic regulation) for its substrate L-aspartate, generating a sigmoidal velocity curve characterized by a Hill coefficient ($n_H$) greater than 1.0.</p>
<p>According to the Monod-Wyman-Changeux (MWC) model of allosteric transitions, ATCase exists in an equilibrium between two distinct quaternary conformations: a low-activity, low-affinity Tense (T) state and a high-activity, high-affinity Relaxed (R) state. The transition from the T state to the R state involves an outward expansion in which the catalytic trimers separate by $11\\text{ \\AA}$ and rotate by $12^\\circ$ relative to each other along the threefold symmetry axis.</p>
<p>ATCase activity is modulated by two opposing heterotropic effectors that bind the same regulatory pocket: cytidine triphosphate (CTP, an end product of the pyrimidine pathway) and adenosine triphosphate (ATP, a purine nucleotide). Treatment with mercurials such as $p$-hydroxymercuribenzoate (pHMB) disrupts zinc-thiolate coordination, dissociating the dodecamer into isolated catalytic trimers ($c_3$) and regulatory dimers ($r_2$). Investigators measured initial velocities of native ATCase and isolated subunits under various effector conditions (Table 1).</p>
<table class="tbl">
  <caption>Table 1 Steady-state kinetic parameters and cooperativity of ATCase assemblies</caption>
  <thead>
    <tr><th>Enzyme Preparation</th><th>Effector Added</th><th>$K_{0.5}$ for L-Aspartate (mM)</th><th>$V_{max}$ ($\\mu\\text{mol}\\cdot\\text{mg}^{-1}\\cdot\\text{min}^{-1}$)</th><th>Hill Coefficient ($n_H$)</th><th>Favored Allosteric State</th></tr>
  </thead>
  <tbody>
    <tr><td>Native Holoenzyme ($c_6r_6$)</td><td>None (Control)</td><td>12.5</td><td>48.0</td><td>1.75</td><td>T $\\rightleftharpoons$ R Equilibrium</td></tr>
    <tr><td>Native Holoenzyme ($c_6r_6$)</td><td>2.0 mM CTP</td><td>23.0</td><td>47.5</td><td>2.10</td><td>T State (Tense)</td></tr>
    <tr><td>Native Holoenzyme ($c_6r_6$)</td><td>2.0 mM ATP</td><td>6.2</td><td>48.2</td><td>1.30</td><td>R State (Relaxed)</td></tr>
    <tr><td>Native Holoenzyme ($c_6r_6$)</td><td>$10\\;\\mu\\text{M}$ PALA</td><td>4.5</td><td>48.0</td><td>1.05</td><td>R State (Relaxed)</td></tr>
    <tr><td>Isolated Catalytic Trimer ($c_3$)</td><td>None (Control)</td><td>4.2</td><td>52.0</td><td>1.02</td><td>Constitutive R-like</td></tr>
    <tr><td>Isolated Catalytic Trimer ($c_3$)</td><td>2.0 mM CTP</td><td>4.2</td><td>51.8</td><td>1.01</td><td>Constitutive R-like</td></tr>
  </tbody>
</table>""",
  "qs": [
    {
      "q": "How do the kinetic properties of the isolated catalytic trimer (c3) compare to those of intact native ATCase (c6r6)?",
      "ch": [
        "The isolated trimer displays hyperbolic kinetics with high substrate affinity and no response to CTP or ATP.",
        "The isolated trimer displays sigmoidal kinetics with heightened sensitivity to feedback inhibition by CTP.",
        "The isolated trimer is completely catalytically inactive due to the loss of essential structural zinc ions.",
        "The isolated trimer requires allosteric activation by ATP before it can bind carbamoyl phosphate molecules."
      ],
      "a": 0,
      "e": "<strong>Properties of the isolated ATCase catalytic subunit:</strong> When native ATCase ($c_6r_6$) is treated with mercurials, it dissociates into independent catalytic trimers ($c_3$) and regulatory dimers ($r_2$). The isolated $c_3$ subunit retains full catalytic activity and displays hyperbolic Michaelis-Menten kinetics with a Hill coefficient of $1.0$ (Table 1), indicating a complete loss of cooperativity. Furthermore, because allosteric binding sites for CTP and ATP reside exclusively on the regulatory subunits, the isolated $c_3$ trimer is entirely unresponsive to CTP inhibition or ATP activation ($K_{0.5}$ remains $4.2\\;\\text{mM}$ regardless of CTP addition).<br><br><em>Distractor Traps:</em><br>&bull; B is incorrect because cooperativity (sigmoidal kinetics) and feedback inhibition require the presence of regulatory subunits and quaternary interactions.<br>&bull; C is incorrect because the structural zinc atoms reside on regulatory subunits; the catalytic trimer remains folded and highly active.<br>&bull; D is incorrect because the isolated catalytic trimer binds substrates readily in a high-affinity, R-like state without ATP."
    },
    {
      "q": "Based on the steady-state data in Table 1, what effect does the addition of 2.0 mM CTP have on intact wild-type ATCase?",
      "ch": [
        "It acts as an uncompetitive inhibitor that decreases both Vmax and the apparent substrate affinity.",
        "It acts as a non-competitive inhibitor that lowers Vmax while keeping the aspartate K0.5 constant.",
        "It shifts the quaternary equilibrium toward the R state, decreasing the K0.5 for aspartate binding.",
        "It stabilizes the low-affinity T state, increasing the K0.5 for aspartate without altering the Vmax."
      ],
      "a": 3,
      "e": "<strong>Allosteric feedback inhibition by CTP:</strong> CTP is an allosteric heterotropic inhibitor that binds specifically to the regulatory subunits of intact ATCase. Binding of CTP stabilizes the low-affinity Tense (T) quaternary state. As seen in Table 1, adding $2.0\\;\\text{mM}$ CTP shifts the sigmoidal substrate saturation curve to the right, increasing the apparent $K_{0.5}$ for L-aspartate from $12.5\\;\\text{mM}$ to $23.0\\;\\text{mM}$ and increasing cooperativity ($n_H = 2.10$). Crucially, because saturating concentrations of substrate can fully overcome this inhibition and drive the enzyme into the R state, $V_{max}$ is unaffected ($47.5\\;\\mu\\text{mol}\\cdot\\text{mg}^{-1}\\cdot\\text{min}^{-1}$ vs $48.0\\;\\mu\\text{mol}\\cdot\\text{mg}^{-1}\\cdot\\text{min}^{-1}$).<br><br><em>Distractor Traps:</em><br>&bull; A describes uncompetitive inhibition, which reduces both $V_{max}$ and $K_m$ by binding exclusively to the ES complex.<br>&bull; B describes classic non-competitive inhibition, which reduces $V_{max}$ without changing $K_m$.<br>&bull; C describes the effect of allosteric activators such as ATP, which decrease $K_{0.5}$ and stabilize the R state."
    },
    {
      "q": "From a metabolic regulatory perspective, what is the physiological advantage of ATP functioning as an allosteric activator of ATCase?",
      "ch": [
        "It signals energy depletion, shifting glucose flux away from pentose phosphate synthesis toward glycolysis.",
        "It inhibits mitochondrial carbamoyl phosphate synthetase I to balance urea cycle intermediates in liver.",
        "It signals high purine abundance, stimulating pyrimidine synthesis to maintain equal nucleotide pools.",
        "It provides the primary phosphoryl group needed to convert N-carbamoyl-L-aspartate into dihydroorotate."
      ],
      "a": 2,
      "e": "<strong>Purine-pyrimidine cross-pathway regulation:</strong> In cellular physiology, DNA and RNA synthesis require stoichiometric balances between purine nucleotides (adenine, guanine) and pyrimidine nucleotides (cytosine, uracil, thymine). If cellular ATP (a purine) is abundant, it signals that cellular energy is high and purine pools are replete. By binding to ATCase and acting as an allosteric activator (lowering $K_{0.5}$ to $6.2\\;\\text{mM}$, Table 1), ATP stimulates pyrimidine nucleotide synthesis, maintaining balanced intracellular purine-to-pyrimidine ratios necessary for nucleic acid replication and transcription.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because high ATP signals cellular energy abundance, not energy depletion (which is signaled by AMP).<br>&bull; B describes hepatic urea cycle regulation; ATCase in E. coli is pyrimidine-specific and does not participate in the urea cycle.<br>&bull; D describes group transfer chemistry; dihydroorotase cyclizes N-carbamoyl-L-aspartate via condensation without ATP hydrolysis."
    },
    {
      "q": "When low, sub-saturating concentrations of the bisubstrate analog PALA are added to wild-type ATCase, initial velocity increases. Why?",
      "ch": [
        "PALA phosphorylates regulatory chains, inducing irreversible covalent activation of catalytic domains.",
        "PALA binding to one catalytic subunit induces a global quaternary shift from the T state to the R state.",
        "PALA acts as an allosteric coenzyme that donates activated carbamoyl groups to free aspartate residues.",
        "PALA dissociates regulatory dimers from catalytic trimers, converting holoenzymes into isolated subunits."
      ],
      "a": 1,
      "e": "<strong>Conformational transition induced by PALA:</strong> N-(phosphonacetyl)-L-aspartate (PALA) is a stable bisubstrate analog that mimics the tetrahedral intermediate of the ATCase reaction. When present at very low concentrations relative to enzyme active sites, PALA binds to just one or two catalytic subunits per dodecamer. Because of strong allosteric cooperativity (concerted MWC transition), ligand binding to a minority of subunits forces the entire quaternary dodecamer into the high-affinity R state. This activates the remaining unliganded active sites, allowing them to bind substrate with elevated affinity and increasing the reaction velocity at sub-saturating substrate levels.<br><br><em>Distractor Traps:</em><br>&bull; A describes covalent phosphorylation; PALA is a non-covalent transition-state analog that does not phosphorylate the enzyme.<br>&bull; C is incorrect because PALA is an unreactive competitive inhibitor, not a catalytic coenzyme.<br>&bull; D describes the effect of organomercurials (like pHMB), not PALA, which stabilizes the intact R-state dodecamer."
    },
    {
      "q": "What primary conformational rearrangement occurs in intact ATCase during the allosteric transition from the T state to the R state?",
      "ch": [
        "Catalytic trimers rotate and separate along the threefold axis, expanding the entire quaternary structure.",
        "Regulatory dimers completely dissociate into monomeric chains and diffuse away from the catalytic core.",
        "The two catalytic trimers collapse together, compressing the central cavity and expelling bound water.",
        "Active-site zinc ions translocate from regulatory polypeptide chains to the catalytic domain interface."
      ],
      "a": 0,
      "e": "<strong>Quaternary structural changes in ATCase:</strong> Structural crystallography demonstrates that the allosteric transition from the T state to the R state involves large-scale quaternary reorganization. The two catalytic trimers rotate by approximately $12^\\circ$ relative to each other and separate by $11\\text{ \\AA}$ along the vertical threefold symmetry axis, while the regulatory dimers rotate by $15^\\circ$. This outward expansion widens the central cavity and brings catalytic residues into correct geometrical alignment, dramatically increasing affinity for L-aspartate.<br><br><em>Distractor Traps:</em><br>&bull; B describes subunit dissociation, which only occurs upon chemical denaturation or organomercurial treatment, not during the physiological T-to-R transition.<br>&bull; C states the exact opposite: the trimers separate and expand outward rather than collapsing together.<br>&bull; D describes zinc translocation; the zinc ions remain permanently coordinated by four cysteines in the regulatory subunits."
    },
    {
      "q": "In biosynthetic pathways, allosteric feedback inhibition typically operates at the committed step. What makes ATCase an ideal target for this control?",
      "ch": [
        "The reaction catalyzed by ATCase is fully reversible, permitting equilibrium buffering of pyrimidines.",
        "ATCase catalyzes a non-specific reaction shared across both pyrimidine and purine synthesis pathways.",
        "ATCase catalyzes the first irreversible reaction unique to the de novo pyrimidine pathway in bacteria.",
        "ATCase operates with zero-order kinetics at all physiological concentrations of carbamoyl phosphate."
      ],
      "a": 2,
      "e": "<strong>The committed step in metabolic feedback inhibition:</strong> In metabolic pathways, regulatory enzymes typically catalyze the 'committed step'—the first essentially irreversible reaction that is unique to that specific biosynthetic branch. Carbamoyl phosphate can be utilized in other pathways (such as arginine synthesis in organisms with a shared pool), but its condensation with L-aspartate to form N-carbamoyl-L-aspartate is uniquely dedicated to pyrimidine production. Inhibiting ATCase via end-product CTP feedback shuts down the entire pathway early, preventing the wasteful expenditure of high-energy phosphate bonds and substrate intermediates.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because committed regulatory steps are thermodynamically irreversible under physiological conditions, not freely reversible.<br>&bull; B is incorrect because ATCase is dedicated specifically to pyrimidines; purines are synthesized via an entirely separate PRPP-dependent pathway.<br>&bull; D describes saturated zero-order kinetics, which does not explain why an enzyme is selected as a feedback-regulated committed step."
    }
  ]
}
