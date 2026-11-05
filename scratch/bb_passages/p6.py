# Passage 6: Topic 511 — Hydrophobic Interactions & Entropy of Solvent Water During Protein Folding
# Answer keys: 2, 0, 3, 1, 0, 2

p6_data = {
    "id": "exam_bb90_3_p6",
    "sec": "B/B",
    "topic": "Hydrophobic Interactions & Entropy of Solvent Water During Protein Folding",
    "sheet": 6,
    "label": "Biological and Biochemical Foundations of Living Systems",
    "examId": "bb90_3",
    "passage": """<div class=\"ttl\">Passage 6 (Questions 31&ndash;36)</div>
<p>The spontaneous folding of a globular protein in aqueous solution is governed by the Gibbs free energy relationship: $\Delta G^\circ_{\text{fold}} = \Delta H^\circ_{\text{fold}} - T\Delta S^\circ_{\text{total}}$. During folding, the polypeptide chain transitions from an ensemble of thousands of disordered random-coil states to a single native tertiary conformation. This collapse entails a substantial loss of conformational entropy for the polypeptide backbone and side chains ($\Delta S^\circ_{\text{chain}} < 0$, $-T\Delta S^\circ_{\text{chain}} > 0$), an unfavorable thermodynamic barrier that must be overcome for folding to proceed.</p>
<p>The primary thermodynamic driving force that overcomes this conformational entropy penalty is the hydrophobic effect. In the unfolded state, nonpolar side chains (e.g., Leu, Ile, Val, Phe) are directly exposed to bulk aqueous solvent. Because nonpolar surfaces cannot engage in hydrogen bonding, surrounding water molecules are forced to reorient into rigid, highly ordered, hydrogen-bonded 'clathrate-like' solvation cages around each hydrophobic group. This local immobilization of water molecules imposes a severe entropic penalty on the solvent ($\Delta S^\circ_{\text{solvent}} < 0$).</p>
<p>Upon tertiary folding, hydrophobic side chains coalesce into the interior core of the protein. Burial of these nonpolar surfaces collapses the ordered clathrate cages, releasing hundreds of immobilized water molecules back into the disordered bulk solvent. This release produces a large, favorable gain in solvent entropy ($\Delta S^\circ_{\text{solvent}} \gg 0$, $-T\Delta S^\circ_{\text{solvent}} < 0$), rendering net $\Delta S^\circ_{\text{total}} > 0$ and driving folding spontaneously ($\Delta G^\circ_{\text{fold}} < 0$) at physiological temperatures.</p>
<p>Protein folding proceeds through a compact intermediate termed the 'molten globule,' which features native-like secondary structure and a collapsed hydrophobic interior, but lacks rigid, close-packed tertiary side-chain interactions. Biophysicists utilized isothermal titration calorimetry (ITC) and spectroscopy to measure thermodynamic parameters of wild-type Staphylococcal nuclease and hydrophobic core mutants at $25^\circ\text{C}$ (Table 1).</p>
<table class=\"tbl\">
  <caption>Table 1 Thermodynamic folding parameters and heat capacity changes of Staphylococcal nuclease variants</caption>
  <thead>
    <tr><th>Protein Construct / Condition</th><th>Structural Modification</th><th>$\Delta H^\circ_{\text{fold}}$ (kJ/mol)</th><th>$-T\Delta S^\circ_{\text{chain}}$ (kJ/mol)</th><th>$-T\Delta S^\circ_{\text{solvent}}$ (kJ/mol)</th><th>$\Delta G^\circ_{\text{fold}}$ (kJ/mol)</th><th>$\Delta C_p$ ($\text{kJ}/(\text{mol}\cdot\text{K})$)</th></tr>
  </thead>
  <tbody>
    <tr><td>WT Nuclease ($25^\circ\text{C}$)</td><td>Native wild-type sequence</td><td>&minus;65</td><td>+142</td><td>&minus;112</td><td>&minus;35</td><td>&minus;8.4</td></tr>
    <tr><td>Mutant L25A</td><td>Core cavity creation (loss of 3 carbons)</td><td>&minus;62</td><td>+139</td><td>&minus;92</td><td>&minus;15</td><td>&minus;6.1</td></tr>
    <tr><td>Mutant I58V</td><td>Core truncation (loss of 1 $-\text{CH}_2-$)</td><td>&minus;64</td><td>+141</td><td>&minus;106</td><td>&minus;29</td><td>&minus;7.6</td></tr>
    <tr><td>Mutant F34S</td><td>Polar substitution inside core</td><td>&minus;48</td><td>+140</td><td>&minus;88</td><td>+4</td><td>&minus;5.2</td></tr>
    <tr><td>WT Nuclease ($5^\circ\text{C}$)</td><td>Cold temperature challenge</td><td>&minus;110</td><td>+132</td><td>&minus;26</td><td>&minus;4</td><td>&minus;8.5</td></tr>
  </tbody>
</table>
<p>Globular protein folding universally exhibits a large negative change in heat capacity ($\Delta C_p < 0$), reflecting the burial of nonpolar surface area.</p>""",
    "qs": [
        {
            "q": "What constitutes the dominant favorable thermodynamic contributor to spontaneous protein folding in aqueous solution at 25 deg C?",
            "ch": [
                "The large decrease in conformational entropy of the polypeptide chain as it adopts a native fold",
                "The formation of covalent peptide bonds between adjacent hydrophobic amino acid side chains",
                "The gain in solvent water entropy upon collapse of ordered clathrate cages around nonpolar residues",
                "The spontaneous absorption of atmospheric heat energy by the folding polypeptide backbone"
            ],
            "a": 2,
            "e": "<strong>Thermodynamic driving force of the hydrophobic effect:</strong> When a protein is unfolded, nonpolar side chains order surrounding water molecules into rigid, quasi-crystalline clathrate cages, causing a massive reduction in solvent entropy ($\\Delta S_{\\text{solvent}} < 0$). Upon folding, hydrophobic side chains are buried into the anhydrous interior core, collapsing these clathrate cages and releasing hundreds of ordered water molecules into the bulk solvent. This release yields a very large positive entropy change for the solvent ($\\Delta S_{\\text{solvent}} \\gg 0$, meaning $-T\\Delta S_{\\text{solvent}} = -112\\;\\text{kJ/mol}$ in WT, Table 1). This solvent entropy gain easily overcomes the unfavorable conformational entropy loss of the polypeptide chain ($-T\\Delta S_{\\text{chain}} = +142\\;\\text{kJ/mol}$), making overall $\\Delta G^\\circ_{\\text{fold}} = -35\\;\\text{kJ/mol}$ spontaneous.<br><br><em>Distractor Traps:</em><br>&bull; A describes the loss of chain conformational entropy, which is an unfavorable thermodynamic penalty ($+142\\;\\text{kJ/mol}$), opposing folding.<br>&bull; B is incorrect because folding involves non-covalent interactions, not the formation of new covalent peptide bonds.<br>&bull; D is incorrect because folding is typically exothermic ($\\Delta H^\\circ_{\\text{fold}} < 0$, releasing heat) rather than absorbing heat."
        },
        {
            "q": "Why does the -T*DeltaS_chain term contribute an unfavorable positive value (+142 kJ/mol in WT, Table 1) to the free energy of folding?",
            "ch": [
                "Folding restricts a vast ensemble of flexible unfolded conformations into a single native state.",
                "Folding hydrolyzes ATP to generate disordered phosphate ions that disrupt the peptide backbone.",
                "Folding forces polar residues into the nonpolar interior, causing massive electrostatic repulsion.",
                "Folding expands the total volume occupied by the polypeptide, decreasing solvent density."
            ],
            "a": 0,
            "e": "<strong>Chain conformational entropy loss during folding:</strong> In the denatured unfolded state, the polypeptide chain is a highly flexible random coil that samples an astronomical number of possible conformations ($W_{\\text{unfolded}}$ is enormous). In the native state, the protein adopts a single, well-defined three-dimensional tertiary fold ($W_{\\text{native}} \\approx 1$). According to Boltzmann's entropy formula ($S = k_B \\ln W$), the conformational entropy of the polypeptide chain decreases dramatically upon folding ($\\Delta S_{\\text{chain}} = S_{\\text{native}} - S_{\\text{unfolded}} < 0$). In the Gibbs free energy equation ($\\Delta G = \\Delta H - T\\Delta S$), this negative entropy change generates a positive, unfavorable term: $-T\\Delta S_{\\text{chain}} > 0$ ($+142\\;\\text{kJ/mol}$).<br><br><em>Distractor Traps:</em><br>&bull; B is incorrect because spontaneous protein folding in vitro occurs without ATP hydrolysis.<br>&bull; C is incorrect because native folding buries nonpolar residues while keeping polar residues on the solvent-accessible exterior.<br>&bull; D is incorrect because folding is a collapse that compacts the protein volume rather than expanding it."
        },
        {
            "q": "Comparing WT Nuclease to mutants I58V and L25A reveals that truncation of buried hydrophobic side chains destabilizes Delta G_fold (Table 1). What explains this finding?",
            "ch": [
                "Truncating nonpolar groups increases the number of hydrogen bonds formed with the peptide backbone.",
                "Smaller side chains introduce bulky steric clashes that force the protein to unfold cooperatively.",
                "Truncated aliphatic residues spontaneously deprotonate, acquiring a destabilizing negative charge.",
                "Truncating buried nonpolar groups buries less hydrophobic surface, releasing fewer clathrate waters."
            ],
            "a": 3,
            "e": "<strong>Hydrophobic core truncation and free energy:</strong> The hydrophobic effect scales directly with the nonpolar surface area buried upon folding. Mutant I58V removes a single methylene group ($-\\text{CH}_2-$) from the isoleucine side chain, reducing the buried nonpolar surface area; consequently, fewer clathrate water molecules are released, making $-T\\Delta S_{\\text{solvent}}$ less negative ($-106\\;\\text{kJ/mol}$ vs $-112\\;\\text{kJ/mol}$) and destabilizing folding by $\\sim 6\\;\\text{kJ/mol}$. Mutant L25A truncates leucine to alanine (loss of three carbons, creating an internal packing cavity), leading to a larger loss of solvent entropy release ($-92\\;\\text{kJ/mol}$) and destabilizing $\\Delta G^\\circ_{\\text{fold}}$ from $-35$ to $-15\\;\\text{kJ/mol}$.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because aliphatic side chains (Leu, Ile, Val, Ala) cannot form hydrogen bonds.<br>&bull; B is backwards: truncating side chains creates packing voids/cavities, not bulky steric clashes.<br>&bull; C is incorrect because aliphatic hydrocarbon side chains do not deprotonate at physiological pH."
        },
        {
            "q": "How is the molten globule folding intermediate structurally distinguished from the fully folded native state?",
            "ch": [
                "It consists entirely of disordered random coils completely devoid of alpha-helices or beta-sheets.",
                "It possesses native-like secondary structure and hydrophobic collapse, but lacks fixed tertiary packing.",
                "It contains fully locked tertiary side-chain packing, but lacks all backbone hydrogen-bonded elements.",
                "It is an irreversible aggregate formed by intermolecular disulfide bonds between mismatched cysteines."
            ],
            "a": 1,
            "e": "<strong>Structural characteristics of the molten globule:</strong> The molten globule is a general intermediate state along the folding pathway of globular proteins. It is defined by three hallmark features: (1) substantial native-like secondary structure (detected by circular dichroism, showing intact $\\alpha$-helices and $\\beta$-sheets), (2) a compact, collapsed hydrophobic core that excludes bulk water, and (3) liquid-like, dynamic side-chain mobility in the interior (lacking the specific, rigid van der Waals packing and close-packed tertiary contacts of the native state).<br><br><em>Distractor Traps:</em><br>&bull; A describes the completely unfolded denatured state.<br>&bull; C reverses the structural definition: secondary structure forms first, followed by tight tertiary packing.<br>&bull; D describes non-native protein aggregation/precipitation, not a monomeric on-pathway folding intermediate."
        },
        {
            "q": "At 5 deg C, WT Nuclease exhibits a dramatic reduction in folding stability (Delta G_fold drops from -35 to -4 kJ/mol, Table 1). Why do globular proteins undergo cold denaturation?",
            "ch": [
                "The magnitude of the favorable -T*DeltaS_solvent term decreases, weakening the hydrophobic effect.",
                "Low temperatures cause covalent peptide bonds to spontaneously hydrolyze into free amino acids.",
                "Decreased thermal energy causes solvent water to freeze into ice crystals that shear alpha-helices.",
                "Cold temperatures cause all basic side chains to lose their positive charge, disrupting salt bridges."
            ],
            "a": 0,
            "e": "<strong>Thermodynamic mechanism of cold denaturation:</strong> The hydrophobic effect is uniquely temperature-dependent because the heat capacity change of folding is negative ($\\Delta C_p < 0$). As temperature decreases from $25^\\circ\\text{C}$ to $5^\\circ\\text{C}$, the $T\\Delta S$ term decreases in magnitude (at $5^\\circ\\text{C}$, $-T\\Delta S_{\\text{solvent}}$ shrinks from $-112\\;\\text{kJ/mol}$ to only $-26\\;\\text{kJ/mol}$, Table 1). In other words, at low temperatures, water molecules can organize into clathrate cages around exposed nonpolar groups with a much smaller entropic penalty. Because the entropic benefit of releasing these waters is drastically diminished, the hydrophobic effect weakens, allowing the unfavorable chain entropy to overcome folding and leading to cold denaturation.<br><br><em>Distractor Traps:</em><br>&bull; B is incorrect because low temperatures slow down, rather than accelerate, chemical peptide bond hydrolysis.<br>&bull; C is incorrect because liquid water does not freeze into ice crystals at $5^\\circ\\text{C}$ ($> 0^\\circ\\text{C}$).<br>&bull; D is incorrect because cold temperatures do not deprotonate basic side chains (Lys and Arg maintain high pKa values)."
        },
        {
            "q": "Protein folding is universally characterized by a negative change in heat capacity (Delta Cp < 0, Table 1). What molecular phenomenon accounts for this negative value?",
            "ch": [
                "The rapid absorption of vibrational kinetic energy by newly formed covalent disulfide cross-links",
                "The release of tightly bound magnesium cofactors from the active site into bulk aqueous solvent",
                "The reduction in ordered, iceberg-like water structure as nonpolar surfaces are buried internally",
                "The conversion of flexible glycine residues into sterically constrained proline pyrrolidine rings"
            ],
            "a": 2,
            "e": "<strong>Origin of negative heat capacity of folding (Delta Cp < 0):</strong> Heat capacity ($C_p$) reflects the amount of heat energy required to raise the temperature of a system by one degree. Ordered water molecules in clathrate cages around exposed nonpolar groups have high heat capacity because added heat melts these hydrogen-bonded cages. In the unfolded state, many nonpolar groups are exposed, creating extensive clathrate hydration shells with high total $C_p$. Upon folding, these nonpolar groups are buried internally, releasing the cage waters into bulk solution. Because bulk water has a lower heat capacity than clathrate water, the heat capacity of the folded protein-solvent system is substantially lower than that of the unfolded system: $\\Delta C_p = C_{p,\\text{folded}} - C_{p,\\text{unfolded}} < 0$ ($-8.4\\;\\text{kJ/(mol}\\cdot\\text{K)}$ in WT).<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because vibrational modes of covalent bonds contribute negligibly to the large negative $\\Delta C_p$ of protein folding.<br>&bull; B is incorrect because cofactor release is not a universal feature of protein folding and does not explain $\\Delta C_p < 0$.<br>&bull; D describes an impossible chemical transmutation of amino acids during folding."
        }
    ]
}
