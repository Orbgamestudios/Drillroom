# Passage 4: Topic 526 — Ribozyme Catalysis: The Peptidyl Transferase Center in the 28S/23S rRNA
# Answer keys: 3 (D), 0 (A), 1 (B), 2 (C), 1 (B), 3 (D)

p4_data = {
  "id": "exam_bb90_4_p4",
  "sec": "B/B",
  "topic": "Ribozyme Catalysis: The Peptidyl Transferase Center in the 28S/23S rRNA",
  "sheet": 4,
  "label": "Biological and Biochemical Foundations of Living Systems",
  "examId": "bb90_4",
  "passage": """<div class="ttl">Passage 4 (Questions 19&ndash;24)</div>
<p>In all cellular life, the synthesis of proteins is executed by ribosomes, colossal ribonucleoprotein machines composed of a small subunit (30S in prokaryotes, 40S in eukaryotes) and a large subunit (50S in prokaryotes, 60S in eukaryotes). The large subunit houses the peptidyl transferase center (PTC), which catalyzes the fundamental reaction of protein synthesis: the transfer of the nascent peptide chain from peptidyl-tRNA in the peptidyl (P) site to the $\\alpha$-amino group of aminoacyl-tRNA in the aminoacyl (A) site, generating a new peptide bond.</p>
<p>High-resolution crystallographic and cryo-electron microscopy structures revealed that the catalytic core of the PTC consists entirely of folded ribosomal RNA (23S rRNA in bacteria, 28S rRNA in eukaryotes), devoid of amino acid side chains within $18\\text{ \\AA}$ of the nascent peptide bond. The ribosome is therefore classified as a ribozyme (RNA enzyme). Ribosomal proteins serve predominantly to stabilize the structural architecture of peripheral RNA helices rather than directly contributing catalytic amino acid side chains to peptide bond formation.</p>
<p>The PTC accelerates peptide bond synthesis through two primary mechanisms. First, it functions as an entropic trap, utilizing an extensive hydrogen-bonding network of conserved nucleotides (including A2451 and U2506 in 23S rRNA) to precisely align the attacking $\\alpha$-amino group and the electrophilic ester carbonyl, dramatically reducing activation entropy ($\\Delta S^\\ddagger$). Second, the PTC employs substrate-assisted catalysis: the $2'$-hydroxyl group ($2'\\text{-OH}$) of the invariant terminal adenosine (A76) of the P-site tRNA donates a proton to the departing $3'$-oxyanion while accepting a proton from the nucleophilic amino group in a concerted six-membered transition state.</p>
<p>Investigators reconstituted ribosomal cores with wild-type or mutant 23S rRNA and assayed peptide bond synthesis using native or modified tRNAs, puromycin (an A-site analog), and nuclease/protease treatments (Table 1).</p>
<table class="tbl">
  <caption>Table 1 Peptidyl transfer kinetics and enzymatic stability of reconstituted ribosomal complexes</caption>
  <thead>
    <tr><th>Ribosome Core</th><th>tRNA Substrate Condition</th><th>Peptidyl Transfer Rate $k_{pep}$ ($\\text{s}^{-1}$)</th><th>Puromycin $K_m$ ($\\mu\\text{M}$)</th><th>Residual Activity after Proteinase K (%)</th><th>Residual Activity after RNase A (%)</th></tr>
  </thead>
  <tbody>
    <tr><td>Wild-Type 50S</td><td>Native P-site tRNA (A76)</td><td>$1.2 \\times 10^1$</td><td>140</td><td>98%</td><td>< 0.1%</td></tr>
    <tr><td>Wild-Type 50S</td><td>$2'\\text{-deoxy-A76}$ P-site tRNA</td><td>$8.5 \\times 10^{-4}$</td><td>145</td><td>97%</td><td>< 0.1%</td></tr>
    <tr><td>A2451U 50S</td><td>Native P-site tRNA (A76)</td><td>$1.8 \\times 10^0$</td><td>185</td><td>99%</td><td>< 0.1%</td></tr>
    <tr><td>U2506C 50S</td><td>Native P-site tRNA (A76)</td><td>$3.4 \\times 10^{-1}$</td><td>620</td><td>98%</td><td>< 0.1%</td></tr>
    <tr><td>$Mg^{2+}$-depleted 50S</td><td>Native P-site tRNA (A76)</td><td>$< 1.0 \\times 10^{-4}$</td><td>N/D</td><td>0%</td><td>< 0.1%</td></tr>
  </tbody>
</table>""",
  "qs": [
    {
      "q": "Which experimental finding provided definitive proof that the ribosomal peptidyl transferase center is a ribozyme?",
      "ch": [
        "Puromycin acts as an allosteric inhibitor that binds a regulatory cavity located between ribosomal subunits.",
        "Reconstitution of translation in vitro requires equal molar ratios of elongation factor Tu and guanosine GTP.",
        "Peptide bond formation proceeds through a high-energy covalent acyl-enzyme intermediate on a cysteine residue.",
        "Catalytic activity persists after thorough protein digestion but is abolished by treatment with ribonuclease."
      ],
      "a": 3,
      "e": "<strong>Experimental proof of ribozyme catalysis:</strong> The classification of the ribosome as a ribozyme rests on structural and biochemical evidence demonstrating that RNA, not protein, carries out catalysis. In Table 1, treating the reconstituted large subunit with Proteinase K (which degrades protein components) leaves $98\\%$ of peptidyl transferase activity intact, whereas treatment with Ribonuclease A (RNase A, which hydrolyzes phosphodiester RNA backbones) reduces activity to $< 0.1\\%$. Coupled with structural evidence showing no amino acid side chains within $18\\text{ \\AA}$ of the reaction center, these findings prove that rRNA constitutes the catalytic engine of the ribosome.<br><br><em>Distractor Traps:</em><br>&bull; A describes puromycin's action incorrectly; puromycin is an active-site substrate analog, not an allosteric regulator.<br>&bull; B describes translational accessory factors, which deliver aminoacyl-tRNAs but are not intrinsic catalytic components of the PTC.<br>&bull; C describes the mechanism of cysteine proteases (like papain or caspases), which is the exact opposite of ribozyme-mediated direct aminolysis."
    },
    {
      "q": "What is the primary catalytic mechanism employed by the peptidyl transferase center to accelerate peptide bond formation?",
      "ch": [
        "Positional approximation of attacking substrates and substrate-assisted proton transfer via the tRNA 2'-OH.",
        "Formation of a transient covalent thioester intermediate between the nascent polypeptide and 23S rRNA uracil.",
        "General base catalysis executed by the imidazole side chain of a conserved active-site histidine residue.",
        "Nucleophilic attack of an rRNA phosphodiester oxygen onto the ester carbonyl group of the peptidyl-tRNA."
      ],
      "a": 0,
      "e": "<strong>Catalytic mechanism of the peptidyl transferase center:</strong> The PTC accelerates peptide bond formation primarily through substrate alignment (proximity and orientation, lowering $\\Delta S^\\ddagger$) and substrate-assisted catalysis. The ribozyme active site tightly confines the nucleophilic $\\alpha$-amino group of the A-site aminoacyl-tRNA and the ester carbonyl of the P-site peptidyl-tRNA. Catalysis is assisted by the $2'\\text{-OH}$ group of the invariant terminal adenosine (A76) of the P-site tRNA, which acts as a proton relay in a concerted six-membered cyclic transition state, shuttling a proton from the attacking amino group to the leaving $3'$-oxygen atom.<br><br><em>Distractor Traps:</em><br>&bull; B is chemically incorrect because RNA ribose and uracil bases do not form covalent thioesters (thioesters require sulfhydryl groups from cysteine or coenzyme A).<br>&bull; C describes proteinaceous serine/cysteine proteases; the PTC contains no amino acid side chains in its catalytic pocket.<br>&bull; D is incorrect because the reaction is a direct nucleophilic attack of the $\\alpha$-amino group on the substrate carbonyl without rRNA phosphodiester intervention."
    },
    {
      "q": "Based on the kinetic data in Table 1, why does substituting native P-site tRNA with a 2'-deoxy-A76 modified tRNA reduce kpep by over 10^4-fold?",
      "ch": [
        "The 2'-deoxyribose modification prevents the aminoacyl ester bond from undergoing spontaneous hydrolysis.",
        "The lack of the 2'-hydroxyl group abolishes the hydrogen-shuttle network that stabilizes the transition state.",
        "The 2'-deoxy-A76 nucleotide causes global denaturation of the 50S large subunit secondary structure.",
        "The modification blocks base-pairing between the tRNA anticodon loop and the mRNA codon in the P site."
      ],
      "a": 1,
      "e": "<strong>Role of P-site tRNA A76 2'-OH in substrate-assisted catalysis:</strong> As described in the passage, the $2'\\text{-OH}$ of A76 on the P-site tRNA participates directly in catalysis as a proton donor/acceptor. When this single hydroxyl group is replaced with a hydrogen atom ($2'\\text{-deoxy-A76}$ tRNA), the rate of peptidyl transfer ($k_{pep}$) plummets from $12\\;\\text{s}^{-1}$ to $8.5 \\times 10^{-4}\\;\\text{s}^{-1}$ (a $> 10^4$-fold reduction), while the affinity for puromycin ($K_m$) remains unchanged ($140\\;\\mu\\text{M}$ vs $145\\;\\mu\\text{M}$, Table 1). This confirms that the $2'\\text{-OH}$ does not mediate substrate binding, but provides critical chemical assistance to proton transfer in the transition state.<br><br><em>Distractor Traps:</em><br>&bull; A describes background non-enzymatic ester stability, which does not explain the loss of enzymatic rate acceleration.<br>&bull; C is incorrect because modifying a single terminal nucleotide on the tRNA substrate does not denature the massive 50S rRNA subunit architecture.<br>&bull; D is incorrect because the A76 residue is located at the $3'$ CCA acceptor terminus in the large subunit, while the anticodon loop is located $\\sim 75\\text{ \\AA}$ away in the small subunit."
    },
    {
      "q": "What biophysical role do divalent magnesium ions (Mg2+) play in the catalytic function of the ribosomal peptidyl transferase center?",
      "ch": [
        "They coordinate incoming aminoacyl-tRNA molecules through covalent coordination bonds to adenine bases.",
        "They function as general acids by donating protons to the attacking alpha-amino nucleophile at the A site.",
        "They shield negative charges on the phosphodiester backbone to stabilize the folded tertiary rRNA core.",
        "They hydrolyze GTP molecules coupled to the movement of elongation factor G during mRNA translocation."
      ],
      "a": 2,
      "e": "<strong>Magnesium stabilization of ribozyme tertiary structure:</strong> RNA molecules are polyanions due to the negatively charged phosphate groups on every nucleotide of the phosphodiester backbone. To fold into intricate, compact tertiary structures such as the catalytic pocket of Domain V of the 23S/28S rRNA, these negative charges must be neutralized. Divalent magnesium ions ($\\text{Mg}^{2+}$) coordinate to the backbone phosphates and water molecules, shielding electrostatic repulsion and stabilizing the tertiary folds of ribozymes. As seen in Table 1, $\\text{Mg}^{2+}$ depletion completely abolishes catalytic activity ($k_{pep} < 10^{-4}\\;\\text{s}^{-1}$) because the ribozyme unfolds.<br><br><em>Distractor Traps:</em><br>&bull; A describes covalent coordination, which does not occur between divalent metals and base adenines to anchor tRNAs.<br>&bull; B is incorrect because $\\text{Mg}^{2+}$ does not act as a general acid donor for the amino nucleophile in the PTC.<br>&bull; D confuses $\\text{Mg}^{2+}$-dependent GTPase activity of EF-G (a protein elongation factor) with the structural role of $\\text{Mg}^{2+}$ in the PTC ribozyme core."
    },
    {
      "q": "How does the antibiotic puromycin inhibit translation in both prokaryotic and eukaryotic ribosomal complexes?",
      "ch": [
        "It binds to the 30S small subunit decoding center, inducing high-frequency misreading of mRNA codons.",
        "It mimics an aminoacyl-tRNA in the A site, accepting the nascent chain to cause premature release.",
        "It covalently crosslinks the 23S/28S rRNA peptidyl transferase loop to the ribosomal protein L22 tunnel.",
        "It traps elongation factor EF-G in a GDP-bound conformation, preventing post-translocational sliding."
      ],
      "a": 1,
      "e": "<strong>Mechanism of puromycin action:</strong> Puromycin is a structural analog of the $3'$ terminal end of an aminoacyl-tRNA (specifically tyrosyl-tRNA). It enters the ribosomal A site, where its $\\alpha$-amino group attacks the ester carbonyl of the peptidyl-tRNA in the P site, forming a peptide bond with the nascent chain. However, unlike a bona fide aminoacyl-tRNA where the amino acid is attached via an ester bond, puromycin possesses a stable amide linkage to its modified aminonucleoside core. Consequently, the peptidyl-puromycin cannot undergo further elongation or translocation, dissociates prematurely from the ribosome, and terminates protein synthesis.<br><br><em>Distractor Traps:</em><br>&bull; A describes aminoglycoside antibiotics (such as streptomycin or gentamicin) that target the 30S decoding center, not puromycin.<br>&bull; C describes macrolide antibiotics (like erythromycin) that bind inside the peptide exit tunnel near L22.<br>&bull; D describes fusidic acid, which prevents EF-G dissociation from the ribosome after GTP hydrolysis."
    },
    {
      "q": "What evolutionary implication is derived from the discovery that the ribosomal peptidyl transferase center is an RNA catalyst?",
      "ch": [
        "Ancient organisms relied entirely on proteinaceous enzymes before the spontaneous emergence of RNA molecules.",
        "Ribosomal proteins evolved to catalyze translation before being replaced by structural RNA scaffolds.",
        "Eukaryotic translation evolved completely independently from prokaryotic ribosomal structural mechanisms.",
        "RNA served as both the genetic material and the primary catalytic machinery during early evolutionary history."
      ],
      "a": 3,
      "e": "<strong>The RNA World hypothesis and ribosomal evolution:</strong> The discovery that the catalytic core of the universal protein-synthesizing machine is composed entirely of RNA provides strong biochemical support for the 'RNA World' hypothesis. In modern biology, DNA stores genetic information, while proteins catalyze biochemical reactions. However, because protein synthesis itself depends on RNA catalysis (the ribosome ribozyme), self-replicating catalytic RNA molecules must have preceded proteins during the origin of life, simultaneously serving as informational templates (genotype) and biocatalysts (phenotype).<br><br><em>Distractor Traps:</em><br>&bull; A states the exact opposite of the RNA World hypothesis, which posits RNA preceded proteins.<br>&bull; B reverses ribosomal evolution; structural and phylogenetic data show rRNA is ancestral and proteins were added subsequently.<br>&bull; C contradicts universal biology; the PTC core is strictly conserved across bacteria, archaea, and eukaryotes, proving common ancestry."
    }
  ]
}
