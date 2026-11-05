# Passage 1: Topic 523 — Cofactors and Coenzymes: Nicotinamide, Flavin, Biotin, and Cobalamin
# Answer keys: 0 (A), 1 (B), 2 (C), 3 (D), 0 (A), 1 (B)

p1_data = {
  "id": "exam_bb90_4_p1",
  "sec": "B/B",
  "topic": "Cofactors and Coenzymes: Nicotinamide, Flavin, Biotin, and Cobalamin",
  "sheet": 1,
  "label": "Biological and Biochemical Foundations of Living Systems",
  "examId": "bb90_4",
  "passage": """<div class="ttl">Passage 1 (Questions 1&ndash;6)</div>
<p>Cellular metabolism relies on organic coenzymes and inorganic cofactors to facilitate chemical transformations that cannot be executed by the twenty canonical amino acid side chains alone. In mitochondrial catabolism, fatty acids and branched-chain amino acids are degraded into propionyl-CoA and acetyl-CoA. These convergent metabolic pathways depend on distinct cofactors with specialized chemical reactivities, including nicotinamide adenine dinucleotide ($\\text{NAD}^+$), flavin adenine dinucleotide (FAD), biotin (vitamin $\\text{B}_7$), and 5'-deoxyadenosylcobalamin (vitamin $\\text{B}_{12}$).</p>
<p>Propionyl-CoA is converted into the citric acid cycle intermediate succinyl-CoA via a three-step pathway. First, the biotin-dependent enzyme propionyl-CoA carboxylase (PCC) catalyzes the ATP-driven carboxylation of propionyl-CoA to D-methylmalonyl-CoA. Biotin is covalently coupled to an active-site lysine residue via an amide bond, forming a flexible biocytin arm that transfers activated carboxy groups between subdomains. Following epimerization to L-methylmalonyl-CoA, methylmalonyl-CoA mutase (MCM) catalyzes a carbon-skeleton isomerization to succinyl-CoA. MCM relies on 5'-deoxyadenosylcobalamin, which coordinates a central cobalt atom ($\\text{Co}^{3+}$) surrounded by a corrin ring; homolytic cleavage of the cobalt-carbon bond generates a primary carbon radical that initiates substrate hydrogen abstraction.</p>
<p>In contrast, redox dehydrogenases utilize either mobile co-substrates or enzyme-bound prosthetic groups. In mitochondrial $\\beta$-oxidation, short-chain acyl-CoA dehydrogenase (SCAD) utilizes tightly bound FAD to oxidize acyl-CoA to $\\text{trans}$-$\\Delta^2$-enoyl-CoA via sequential one-electron transfers involving a semiquinone intermediate. Downstream, L-3-hydroxyacyl-CoA dehydrogenase (HADH) reduces $\\text{NAD}^+$ to NADH via an obligatory two-electron hydride transfer.</p>
<p>To characterize cofactor binding kinetics and catalytic dependencies, investigators purified recombinant human PCC, MCM, SCAD, and HADH. Binding affinities ($K_d$), cofactor dissociation rate constants ($k_{off}$), and catalytic efficiencies ($k_{cat}/K_m$) were measured in the presence of native cofactors or structural analogs (Table 1).</p>
<table class="tbl">
  <caption>Table 1 Cofactor binding kinetics and catalytic efficiencies of purified mitochondrial enzymes</caption>
  <thead>
    <tr><th>Enzyme</th><th>Cofactor Condition</th><th>Cofactor $K_d$ (M)</th><th>$k_{off}$ ($\\text{s}^{-1}$)</th><th>$k_{cat}/K_m$ ($\\text{M}^{-1}\\text{s}^{-1}$)</th><th>Relative Activity (%)</th></tr>
  </thead>
  <tbody>
    <tr><td>PCC (WT)</td><td>Native Biotin + ATP</td><td>$1.2 \\times 10^{-7}$</td><td>$3.5 \\times 10^{-5}$</td><td>$4.8 \\times 10^5$</td><td>100%</td></tr>
    <tr><td>PCC (K678A)</td><td>Biotin + ATP</td><td>$> 1.0 \\times 10^{-2}$</td><td>N/A</td><td>$< 1.0$</td><td>< 0.1%</td></tr>
    <tr><td>MCM (WT)</td><td>Native AdoCbl</td><td>$4.5 \\times 10^{-8}$</td><td>$1.8 \\times 10^{-4}$</td><td>$3.2 \\times 10^5$</td><td>100%</td></tr>
    <tr><td>MCM (WT)</td><td>Hydroxocobalamin</td><td>$6.2 \\times 10^{-7}$</td><td>$8.4 \\times 10^{-3}$</td><td>$< 1.0$</td><td>< 0.1%</td></tr>
    <tr><td>SCAD (WT)</td><td>Native FAD</td><td>$8.1 \\times 10^{-10}$</td><td>$4.2 \\times 10^{-6}$</td><td>$6.7 \\times 10^6$</td><td>100%</td></tr>
    <tr><td>HADH (WT)</td><td>Native $\\text{NAD}^+$</td><td>$2.4 \\times 10^{-5}$</td><td>$5.6 \\times 10^2$</td><td>$1.9 \\times 10^6$</td><td>100%</td></tr>
  </tbody>
</table>""",
  "qs": [
    {
      "q": "Which statement accurately compares the fundamental electron-transfer mechanisms of nicotinamide and flavin coenzymes?",
      "ch": [
        "NAD+ accepts an obligate two-electron hydride ion, whereas FAD can accept single electrons sequentially.",
        "NAD+ forms a resonance-stabilized semiquinone intermediate, whereas FAD only transfers hydride ions.",
        "FAD accepts electrons exclusively via hydride transfer, whereas NAD+ participates in one-electron steps.",
        "FAD dissociates freely after reduction, whereas NAD+ remains covalently bound to the catalytic subunit."
      ],
      "a": 0,
      "e": "<strong>Mechanisms of nicotinamide versus flavin redox catalysis:</strong> Nicotinamide adenine dinucleotide ($\\text{NAD}^+$) undergoes an obligatory two-electron reduction in which a hydride ion ($:H^-$, two electrons and one proton) is transferred directly to the C4 position of the pyridine ring, converting $\\text{NAD}^+$ to NADH without stable single-electron radical intermediates. In contrast, the isoalloxazine ring of flavin adenine dinucleotide (FAD) can accept electrons either one at a time (forming a resonance-stabilized neutral or anionic semiquinone radical intermediate, $\\text{FAD}^{\\bullet-}/\\text{FADH}^\\bullet$) or simultaneously as two electrons (yielding $\\text{FADH}_2$). This versatility allows flavins to bridge obligate two-electron donors (such as metabolic metabolites) and one-electron acceptors (such as iron-sulfur clusters and cytochromes in the electron transport chain).<br><br><em>Distractor Traps:</em><br>&bull; B reverses the chemical properties of the coenzymes; FAD forms a semiquinone radical, whereas $\\text{NAD}^+$ cannot form a stable radical.<br>&bull; C inverts the electron transfer modes; FAD participates in one- or two-electron chemistry, whereas $\\text{NAD}^+$ transfers hydride ions exclusively.<br>&bull; D confuses coenzyme binding modes; $\\text{NAD}^+$ dissociates freely as a co-substrate, whereas FAD is a tightly bound prosthetic group."
    },
    {
      "q": "During the catalytic cycle of propionyl-CoA carboxylase (PCC), what is the biochemical role of the biotin prosthetic group?",
      "ch": [
        "It activates molecular oxygen to catalyze oxidative decarboxylation of carboxylate intermediates.",
        "It covalently carries an activated carboxyl group on its ureido nitrogen via a flexible lysyl arm.",
        "It accepts a hydride ion from bicarbonate to reduce acyl substrates prior to carbon-carbon cleavage.",
        "It coordinates a divalent cobalt ion to generate an adenosyl free radical for skeletal rearrangement."
      ],
      "a": 1,
      "e": "<strong>Biotin-mediated carboxylation mechanism:</strong> Biotin serves as a specialized cofactor for carboxylases (including propionyl-CoA carboxylase, pyruvate carboxylase, and acetyl-CoA carboxylase). Biotin is attached to the $\\epsilon$-amino group of a specific active-site lysine residue via an amide bond, creating a long, flexible arm (biocytin, $\\sim 14\\text{ \\AA}$) that swings between two catalytic subsites. In the first subsite, ATP activates bicarbonate to form carboxyphosphate, which then carboxylates the $N1'$ nitrogen of the biotin ureido ring to form carboxybiotin. The arm then translocates to the second subsite, where the activated carbon dioxide is transferred to the $\\alpha$-carbon of propionyl-CoA, producing D-methylmalonyl-CoA.<br><br><em>Distractor Traps:</em><br>&bull; A describes oxygenase or flavin monooxygenase activity, not biotin-dependent carboxylation.<br>&bull; C invents a hydride reduction step; carboxylation transfers a carboxyl group ($\\text{COO}^-$) without reducing the acyl backbone.<br>&bull; D describes the role of cobalamin (vitamin $\\text{B}_{12}$) in methylmalonyl-CoA mutase, not biotin."
    },
    {
      "q": "According to the experimental findings in Table 1, what catalytic feature distinguishes methylmalonyl-CoA mutase (MCM)?",
      "ch": [
        "MCM requires free ATP hydrolysis to generate a stable carboxyphosphate intermediate for group transfer.",
        "MCM undergoes reversible non-covalent dissociation from nicotinamide coenzymes during each turnover.",
        "MCM utilizes 5'-deoxyadenosylcobalamin to trigger homolytic cleavage and generate a carbon free radical.",
        "MCM utilizes an enzyme-bound flavin cofactor to catalyze direct one-electron reduction of succinyl-CoA."
      ],
      "a": 2,
      "e": "<strong>Adenosylcobalamin radical catalysis in MCM:</strong> Methylmalonyl-CoA mutase requires 5'-deoxyadenosylcobalamin (AdoCbl), an active cofactor form of vitamin $\\text{B}_{12}$. The catalytic hallmark of AdoCbl is the homolytic cleavage of its relatively weak cobalt-carbon bond ($Co-C$, bond dissociation energy $\\sim 130\\text{ kJ/mol}$), generating a divalent cobalt species ($\\text{Co}^{2+}$, cob[II]alamin) and a 5'-deoxyadenosyl free radical. This radical abstracts a hydrogen atom from the methyl group of L-methylmalonyl-CoA, generating a substrate radical that undergoes an intramolecular rearrangement to produce succinyl-CoA. In Table 1, replacing AdoCbl with hydroxocobalamin (which lacks the 5'-deoxyadenosyl moiety) eliminates catalytic activity ($< 0.1\\%$), demonstrating that the adenosyl group and its radical-forming capacity are indispensable.<br><br><em>Distractor Traps:</em><br>&bull; A describes the biotin-dependent mechanism of propionyl-CoA carboxylase, not MCM.<br>&bull; B erroneously attributes nicotinamide dependence to MCM; MCM uses cobalamin, not $\\text{NAD}^+$.<br>&bull; D misattributes flavin-dependent electron transfer to MCM, which catalyzes an isomerization rather than a net redox reaction."
    },
    {
      "q": "Based on the dissociation rate constants reported in Table 1, how do NAD+ and FAD differ in their interactions with dehydrogenases?",
      "ch": [
        "NAD+ functions as a covalently tethered prosthetic group, whereas FAD functions as a diffusing substrate.",
        "Both NAD+ and FAD remain irreversibly anchored to apoenzymes through high-affinity disulfide linkages.",
        "FAD exhibits rapid equilibrium dissociation, whereas NAD+ remains permanently bound inside the pocket.",
        "NAD+ functions as a dissociable co-substrate, whereas FAD remains tightly bound as a prosthetic group."
      ],
      "a": 3,
      "e": "<strong>Co-substrates versus prosthetic groups:</strong> Enzyme cofactors are classified based on their affinity and residence time on the enzyme. Table 1 shows that short-chain acyl-CoA dehydrogenase (SCAD) binds FAD with sub-nanomolar affinity ($K_d = 8.1 \\times 10^{-10}\\text{ M}$) and an extremely slow off-rate ($k_{off} = 4.2 \\times 10^{-6}\\text{ s}^{-1}$), meaning FAD remains continuously bound to the enzyme as a prosthetic group throughout catalytic cycling. In contrast, L-3-hydroxyacyl-CoA dehydrogenase (HADH) binds $\\text{NAD}^+$ with micromolar affinity ($K_d = 2.4 \\times 10^{-5}\\text{ M}$) and exhibits an off-rate of $5.6 \\times 10^2\\text{ s}^{-1}$. Thus, $\\text{NAD}^+$ functions as a dissociable co-substrate that binds, accepts electrons, and rapidly dissociates as NADH to be re-oxidized elsewhere.<br><br><em>Distractor Traps:</em><br>&bull; A reverses the two coenzymes; $\\text{NAD}^+$ is the diffusing co-substrate, and FAD is the prosthetic group.<br>&bull; B is factually incorrect; neither cofactor forms an irreversible disulfide linkage to dehydrogenases.<br>&bull; C directly contradicts the quantitative kinetics in Table 1, where HADH ($\\text{NAD}^+$) has a $k_{off}$ eight orders of magnitude faster than SCAD (FAD)."
    },
    {
      "q": "Patients with an inborn error affecting holocarboxylase synthetase display impaired activity across multiple carboxylases. Which biochemical defect explains this presentation?",
      "ch": [
        "Inability to covalently attach biotin to the epsilon-amino group of conserved lysine active-site residues",
        "Failure to synthesize the corrin ring system required for coordinated cobalt binding and radical transfer",
        "Disruption of mitochondrial nicotinamide transport channels leading to depleted matrix pools of NADH",
        "Impaired riboflavin phosphorylation preventing the assembly of functional flavin adenine dinucleotide"
      ],
      "a": 0,
      "e": "<strong>Holocarboxylase synthetase deficiency and biotinylation:</strong> Holocarboxylase synthetase is the essential enzyme responsible for transferring biotin onto the apoenzyme forms of all four human biotin-dependent carboxylases: propionyl-CoA carboxylase, pyruvate carboxylase, acetyl-CoA carboxylase, and $\\beta$-methylcrotonyl-CoA carboxylase. The enzyme catalyzes the ATP-dependent covalent condensation of biotin with the $\\epsilon$-amino group of a strictly conserved active-site lysine residue (as shown by the inactive K678A mutant in Table 1). Deficiency of this synthetase results in multiple carboxylase deficiency, causing metabolic acidosis, accumulation of organic acids, and impaired gluconeogenesis and odd-chain fatty acid oxidation.<br><br><em>Distractor Traps:</em><br>&bull; B relates to cobalamin (vitamin $\\text{B}_{12}$) synthesis/processing, which affects methylmalonyl-CoA mutase and methionine synthase, not carboxylases.<br>&bull; C describes nicotinamide cofactors, which are not substrates for holocarboxylase synthetase.<br>&bull; D describes flavokinase and FAD synthase, which assemble FMN and FAD from riboflavin."
    },
    {
      "q": "In an experimental variant of propionyl-CoA carboxylase where the catalytic lysine is mutated to alanine (K678A), what kinetic outcome is expected?",
      "ch": [
        "Complete loss of ATP hydrolysis while biotin carboxylation by bicarbonate proceeds at normal wild-type rates.",
        "Complete loss of carboxylase activity because biotin can no longer be covalently attached to the apoenzyme.",
        "A marked increase in catalytic efficiency (kcat/Km) resulting from elimination of steric bulk at the cleft.",
        "Normal carboxyl transfer to propionyl-CoA accompanied by failure to release the resulting D-methylmalonyl-CoA."
      ],
      "a": 1,
      "e": "<strong>Role of lysine in covalent biotin attachment:</strong> The covalent linkage of biotin to the apocarboxylase requires the primary amino group of a specific lysine side chain (Lys678 in PCC). Mutating this residue to an alanine (K678A) removes the nucleophilic $\\epsilon$-amino group, completely preventing post-translational biotinylation. As reported in Table 1, the K678A mutant exhibits an apparent $K_d > 10^{-2}\\text{ M}$ (no measurable high-affinity cofactor binding) and relative activity $< 0.1\\%$. Without the swinging biocytin arm, the enzyme cannot capture activated carbon dioxide or transfer it to propionyl-CoA.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because carboxyphosphate requires biotin to accept the carboxyl group; without biotin, productive carboxyl transfer cannot occur.<br>&bull; C contradicts Table 1 and fundamental enzymology; eliminating an essential catalytic tether abolishes activity rather than increasing catalytic efficiency.<br>&bull; D is incorrect because the mutant cannot synthesize carboxybiotin or form D-methylmalonyl-CoA in the first place."
    }
  ]
}
