# Passage 4: Topic 509 — Alpha-Helix Geometry: Hydrogen Bonding Patterns & Destabilizing Residues
# Answer keys: 0, 3, 1, 2, 0, 1

p4_data = {
    "id": "exam_bb90_3_p4",
    "sec": "B/B",
    "topic": "Alpha-Helix Geometry: Hydrogen Bonding Patterns & Destabilizing Residues",
    "sheet": 4,
    "label": "Biological and Biochemical Foundations of Living Systems",
    "examId": "bb90_3",
    "passage": """<div class=\"ttl\">Passage 4 (Questions 19&ndash;24)</div>
<p>The $\alpha$-helix is the most abundant secondary structural element in globular and membrane proteins. In an idealized right-handed $\alpha$-helix, the polypeptide backbone completes one turn every 3.6 amino acid residues, corresponding to a vertical translation (pitch) of 5.4 \AA\ (1.5 \AA\ rise per residue) with dihedral angles of $\phi \approx -57^\circ$ and $\psi \approx -47^\circ$. The structure is stabilized by intrachain hydrogen bonds between the backbone carbonyl oxygen ($C=\text{O}$) of residue $i$ and the backbone amide proton ($\text{N}-\text{H}$) of residue $i+4$. These hydrogen bonds align nearly parallel to the central helical axis.</p>
<p>Because individual peptide bonds possess a permanent dipole moment ($\sim 3.5\text{ Debye}$ pointing from the carbonyl oxygen to the amide nitrogen), their parallel alignment generates a cumulative helix macrodipole. This macrodipole confers a net partial positive charge ($\delta^+$) near the N-terminus and a net partial negative charge ($\delta^-$) near the C-terminus. Consequently, the incorporation of negatively charged residues (e.g., Asp, Glu) near the N-terminus stabilizes the helix via favorable electrostatic capping, whereas positively charged residues (e.g., Lys, Arg) at the N-terminus are destabilizing.</p>
<p>Helical propensity is strongly governed by side-chain sterics and conformational entropy. Alanine exhibits the highest helical propensity due to its compact, non-bulky methyl side chain. Conversely, proline is termed a 'helix breaker' because its cyclic pyrrolidine ring lacks an amide proton for $i+4$ hydrogen bonding and imposes rigid steric constraints ($\phi$ locked near $-65^\circ$). Glycine is also a classic helix breaker, but through an entropic mechanism: its hydrogen side chain affords excessive conformational flexibility in the unfolded state, imposing a steep entropic penalty ($\Delta S^\circ < 0$) upon confinement into a rigid helix.</p>
<p>Biophysicists measured helical content ($[\theta]_{222}$) and thermal melting points ($T_m$) for a designed 20-residue model peptide ($\text{Ac-AAAAKAAAAKAAAAKAAAA-NH}_2$) and several point mutants (Table 1).</p>
<table class=\"tbl\">
  <caption>Table 1 Circular dichroism ellipticity and thermal denaturation parameters of model 20-residue helical peptides</caption>
  <thead>
    <tr><th>Peptide Construct</th><th>Structural Modification</th><th>Molar Ellipticity at 222 nm ($[\theta]_{222}$, $\text{deg}\cdot\text{cm}^2/\text{dmol}$)</th><th>Helical Content (%)</th><th>Melting Temperature $T_m$ ($^\circ\text{C}$)</th><th>$\Delta G^\circ_{\text{unfold}}$ at 25$^\circ\text{C}$ (kJ/mol)</th></tr>
  </thead>
  <tbody>
    <tr><td>Peptide 1 (WT)</td><td>Model Poly-Ala reference peptide</td><td>&minus;28,500</td><td>88%</td><td>58.4</td><td>14.2</td></tr>
    <tr><td>Peptide 2</td><td>Ala6Pro substitution</td><td>&minus;7,200</td><td>22%</td><td>24.1</td><td>2.8</td></tr>
    <tr><td>Peptide 3</td><td>Ala6Gly substitution</td><td>&minus;11,500</td><td>35%</td><td>31.6</td><td>4.6</td></tr>
    <tr><td>Peptide 4</td><td>Ala1Glu (N-terminal electrostatic cap)</td><td>&minus;31,800</td><td>98%</td><td>66.8</td><td>18.5</td></tr>
    <tr><td>Peptide 5</td><td>Ala1Lys (N-terminal electrostatic cap)</td><td>&minus;21,200</td><td>65%</td><td>46.2</td><td>9.8</td></tr>
    <tr><td>Peptide 6</td><td>Ala10Asp / Ala14Arg ($i, i+4$ salt bridge)</td><td>&minus;32,100</td><td>99%</td><td>68.2</td><td>19.1</td></tr>
  </tbody>
</table>
<p>Circular dichroism spectroscopy monitors peptide secondary structure: an intact $\alpha$-helix displays characteristic negative ellipticity minima at 208 nm and 222 nm.</p>""",
    "qs": [
        {
            "q": "In an ideal right-handed alpha-helix, which atoms participate directly in the periodic intrachain hydrogen bonds that stabilize the core architecture?",
            "ch": [
                "The backbone carbonyl oxygen of residue i and the backbone amide proton of residue i+4",
                "The backbone carbonyl oxygen of residue i and the backbone amide proton of residue i+3",
                "The side-chain carboxylate of residue i and the side-chain ammonium of residue i+4",
                "The backbone carbonyl oxygen of residue i and the side-chain hydroxyl of residue i+2"
            ],
            "a": 0,
            "e": "<strong>Hydrogen bonding geometry of the alpha-helix:</strong> The classic $\\alpha$-helix ($3.6_{13}$-helix) is characterized by regular intrachain hydrogen bonds formed between the backbone carbonyl oxygen ($C=\\text{O}$) of amino acid residue $i$ and the backbone amide proton ($\\text{N}-\\text{H}$) of residue $i+4$. Each hydrogen bond spans 13 backbone atoms in the closed hydrogen-bonded loop, stabilizing the structure with $3.6$ residues per turn and orienting all hydrogen bonds parallel to the helical axis.<br><br><em>Distractor Traps:</em><br>&bull; B describes a $3_{10}$-helix (which has $i \\rightarrow i+3$ hydrogen bonds), a tighter and less common secondary structure.<br>&bull; C describes side-chain salt bridges, not the fundamental backbone hydrogen-bonding network.<br>&bull; D describes side-chain-to-backbone interactions, such as those found in helix caps or beta-turns, not the repetitive helical core."
        },
        {
            "q": "Why does the single Ala6Pro substitution in Peptide 2 cause a dramatic collapse in helical content from 88% to 22% (Table 1)?",
            "ch": [
                "Proline's side chain carries a bulky negative charge that electrostatically repels carbonyl oxygens.",
                "Proline coordinates solvent water molecules that enzymatically hydrolyze neighboring peptide bonds.",
                "Proline's conformational flexibility increases the entropy of the folded helical state.",
                "Proline's pyrrolidine ring lacks a backbone amide proton and sterically clashes with the helix."
            ],
            "a": 3,
            "e": "<strong>Proline as a helix breaker:</strong> Proline destabilizes $\\alpha$-helices through two distinct structural constraints: (1) Its aliphatic side chain cyclizes back onto the backbone nitrogen to form a five-membered pyrrolidine ring, locking the backbone $\\phi$ dihedral angle near $-65^\\circ$ and introducing steric hindrance with the preceding turn. (2) Because the backbone nitrogen is part of a tertiary amide (an imino acid derivative), it lacks an amide proton ($N-H$) when incorporated into a peptide bond, making it chemically incapable of acting as a hydrogen bond donor to the $i-4$ carbonyl oxygen. Consequently, introducing proline into an $\\alpha$-helix produces an obligatory kink or terminates the helix entirely.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because proline has a neutral, nonpolar aliphatic pyrrolidine ring, not a negatively charged group.<br>&bull; B is incorrect because proline does not enzymatically hydrolyze peptide bonds.<br>&bull; C states the exact opposite: proline is the most conformationally rigid amino acid, not flexible."
        },
        {
            "q": "Unlike proline, glycine destabilizes alpha-helices primarily through an entropic mechanism because:",
            "ch": [
                "its hydrogen side chain forms steric clashes with adjacent carbonyl oxygen atoms.",
                "its lack of a beta-carbon permits high conformational freedom in the unfolded state.",
                "its nonpolar nature prevents favorable hydrophobic interactions with the solvent water.",
                "it donates two protons simultaneously to the same carbonyl oxygen in the peptide backbone."
            ],
            "a": 1,
            "e": "<strong>Glycine helix-breaking entropic mechanism:</strong> Glycine possesses only a single hydrogen atom as its side chain ($R = -H$) and lacks a $\\beta$-carbon. This absence of side-chain steric bulk allows glycine to adopt a wide range of backbone dihedral angles ($\\phi, \\psi$) across all four quadrants of the Ramachandran plot. In the unfolded state, glycine therefore confers extraordinarily high conformational entropy. Restricting glycine into the rigid, narrow dihedral angles required for an $\\alpha$-helix ($\\phi \\approx -57^\\circ, \\psi \\approx -47^\\circ$) requires a very large entropic penalty ($\\Delta S_{\\text{conf}} \\ll 0$, so $-T\\Delta S > 0$), making helix formation thermodynamically unfavorable compared to more rigid residues like alanine.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because glycine's small hydrogen atom minimizes, rather than creates, steric clashes.<br>&bull; C is incorrect because glycine's destabilization is entropic, not driven by poor water interactions.<br>&bull; D is impossible because an amide nitrogen in a peptide bond has only one proton."
        },
        {
            "q": "Why does the Ala1Glu substitution (Peptide 4) increase helix stability while Ala1Lys (Peptide 5) decreases it (Table 1)?",
            "ch": [
                "Lysine's positive charge forms a covalent cross-link that locks the helix in an unfolded state.",
                "Glutamate donates a carboxylate proton to form a disulfide bond with the C-terminal amide.",
                "Glutamate's negative charge neutralizes the partial positive dipole at the helix N-terminus.",
                "Lysine introduces an excessive beta-branched side chain that alters the local Ramachandran angle."
            ],
            "a": 2,
            "e": "<strong>Helix macrodipole and electrostatic capping:</strong> Because all backbone peptide dipoles align parallel to the helical axis (pointing from $C=\\text{O}$ toward $\\text{N}-\\text{H}$), an $\\alpha$-helix acts as a macrodipole with a net partial positive charge ($\\delta^+$) at its N-terminus and a net partial negative charge ($\\delta^-$) at its C-terminus. Introducing a negatively charged glutamate residue at the N-terminus (Peptide 4, Ala1Glu) provides favorable electrostatic attraction with the $\\delta^+$ pole, stabilizing the helix ($T_m$ increases to $66.8^\\circ\\text{C}$). Conversely, introducing a positively charged lysine at the N-terminus (Peptide 5, Ala1Lys) causes unfavorable electrostatic repulsion with the $\\delta^+$ pole, destabilizing the helix ($T_m$ drops to $46.2^\\circ\\text{C}$).<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because lysine does not form covalent cross-links that lock the unfolded state; it destabilizes via electrostatic repulsion.<br>&bull; B is incorrect because glutamate cannot form disulfide bonds (disulfides are formed by cysteines).<br>&bull; D is incorrect because lysine is not a beta-branched amino acid (valine, isoleucine, and threonine are beta-branched)."
        },
        {
            "q": "Peptide 6 incorporates an Asp at position 10 and an Arg at position 14, producing a substantial increase in Tm (68.2 deg C). What explains this stabilization?",
            "ch": [
                "Residues spaced i and i+4 align on the same helical face, forming a favorable salt bridge.",
                "Residues spaced i and i+4 point in opposite directions, preventing steric side-chain collision.",
                "The Asp and Arg side chains form a covalent peptide bond that cross-links the two turns.",
                "The interaction alters the helix from a right-handed geometry into a left-handed conformation."
            ],
            "a": 0,
            "e": "<strong>Helical wheel spacing and side-chain interactions:</strong> An $\\alpha$-helix has $3.6$ residues per turn, which means that residues separated by 3 or 4 positions along the primary sequence ($i$ and $i+3$ or $i$ and $i+4$) align on the exact same spatial face of the helix cylinder. In Peptide 6, the negatively charged carboxylate of Asp10 and the positively charged guanidinium of Arg14 are positioned at $i$ and $i+4$. Being adjacent on the same face, they form an intrahelical salt bridge (ion pair), providing substantial electrostatic stabilization that raises the melting temperature to $68.2^\\circ\\text{C}$ and helical content to $99\\%$.<br><br><em>Distractor Traps:</em><br>&bull; B describes residues separated by 2 positions ($i$ and $i+2$), which project on opposite sides of the helix.<br>&bull; C is incorrect because side chains in native folded proteins form non-covalent ionic bonds (salt bridges), not covalent isopeptide bonds.<br>&bull; D is incorrect because the peptide maintains a standard right-handed alpha-helical conformation."
        },
        {
            "q": "A straight, uninterrupted alpha-helix spanning a biological membrane contains exactly 36 amino acid residues. What is the approximate length of this helix along its central axis?",
            "ch": [
                "126 Angstroms, based on an axial rise of 3.5 Angstroms per amino acid residue",
                "54 Angstroms, based on an axial rise of 1.5 Angstroms per amino acid residue",
                "36 Angstroms, based on an axial rise of 1.0 Angstroms per amino acid residue",
                "194 Angstroms, based on an axial rise of 5.4 Angstroms per amino acid residue"
            ],
            "a": 1,
            "e": "<strong>Calculation of alpha-helix dimensions:</strong> In an $\\alpha$-helix, each complete turn comprises $3.6$ amino acid residues and has a pitch (vertical translation per turn) of $5.4\\;\\text{\\AA}$. The axial rise per amino acid residue is therefore $5.4\\;\\text{\\AA} / 3.6 = 1.5\\;\\text{\\AA}$ per residue. For an uninterrupted helix of 36 residues, the total length along the central axis is: $36 \\times 1.5\\;\\text{\\AA} = 54\\;\\text{\\AA}$.<br><br><em>Distractor Traps:</em><br>&bull; A uses $3.5\\;\\text{\\AA}$ per residue, which is the translation distance for an extended $\\beta$-strand, not an $\\alpha$-helix ($36 \\times 3.5 = 126\\;\\text{\\AA}$).<br>&bull; C assumes $1.0\\;\\text{\\AA}$ per residue.<br>&bull; D multiplies by $5.4\\;\\text{\\AA}$ per residue, confusing the pitch per turn with the rise per individual residue ($36 \\times 5.4 = 194.4\\;\\text{\\AA}$)."
        }
    ]
}
