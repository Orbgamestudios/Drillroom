# Passage 5: Topic 510 — Beta-Pleated Sheet Architecture: Parallel vs Antiparallel Topology
# Answer keys: 1, 2, 0, 3, 1, 0

p5_data = {
    "id": "exam_bb90_3_p5",
    "sec": "B/B",
    "topic": "Beta-Pleated Sheet Architecture: Parallel vs Antiparallel Topology",
    "sheet": 5,
    "label": "Biological and Biochemical Foundations of Living Systems",
    "examId": "bb90_3",
    "passage": """<div class=\"ttl\">Passage 5 (Questions 25&ndash;30)</div>
<p>Beta-pleated sheets ($\beta$-sheets) are secondary structural motifs composed of laterally aligned, extended $\beta$-strands. Within an individual $\beta$-strand, the polypeptide backbone adopts an extended conformation with $\phi \approx -120^\circ$ to $-140^\circ$ and $\psi \approx +130^\circ$ to $+150^\circ$, yielding a translation distance of approximately 3.5 \AA\ per residue (compared to 1.5 \AA\ in an $\alpha$-helix). Because the peptide bond is planar and trans, side-chain R-groups project alternately above and below the average plane of the pleated sheet with a two-residue repeat distance of 7.0 \AA.</p>
<p>$\beta$-Sheets occur in two fundamental topologies: parallel and antiparallel. In antiparallel $\beta$-sheets, adjacent strands run in opposite amino-to-carboxyl directions ($N \rightarrow C$ adjacent to $C \rightarrow N$). This geometry allows inter-strand hydrogen bonds between backbone carbonyl oxygens ($C=\text{O}$) and amide hydrogens ($\text{N}-\text{H}$) to form collinear ($180^\circ$), perpendicular to the strand axis. In contrast, parallel $\beta$-sheets feature adjacent strands running in the identical direction ($N \rightarrow C$ adjacent to $N \rightarrow C$). This parallel orientation forces inter-strand hydrogen bonds to form at a slanted, non-collinear angle ($\sim 150^\circ$), making individual parallel hydrogen bonds weaker and requiring a minimum of four or five strands to achieve thermodynamic stability.</p>
<p>In transmembrane $\beta$-barrel proteins (e.g., bacterial outer membrane porins), antiparallel strands assemble into a cylindrical barrel with an alternating primary sequence: hydrophobic residues face the lipid bilayer, while polar or charged residues line the aqueous pore. In contrast, aberrant conformational transitions can cause globular proteins to misfold into cross-$\beta$ amyloid fibrils. In amyloid fibrils, $\beta$-strands run perpendicular to the fibrillar axis, while intermolecular hydrogen bonds propagate parallel to the axis, binding diagnostic dyes such as Thioflavin T (ThT) and Congo Red.</p>
<p>Structural biologists evaluated synthetic 16-residue $\beta$-hairpin models and amyloidogenic peptides to assess structural stability and dye binding (Table 1).</p>
<table class=\"tbl\">
  <caption>Table 1 Biophysical properties and spectroscopic readouts of synthetic beta-sheet constructs</caption>
  <thead>
    <tr><th>Peptide Construct</th><th>Sheet Topology / Sequence Motif</th><th>Mean H-Bond Angle ($^\circ$)</th><th>$T_m$ ($^\circ\text{C}$)</th><th>Thioflavin T Fluorescence (a.u.)</th><th>Congo Red Birefringence</th></tr>
  </thead>
  <tbody>
    <tr><td>Hairpin 1</td><td>Antiparallel ($\beta$-turn tethered)</td><td>178$^\circ$</td><td>64.5</td><td>4</td><td>Negative</td></tr>
    <tr><td>Hairpin 2</td><td>Parallel (Diamine tethered)</td><td>148$^\circ$</td><td>41.2</td><td>5</td><td>Negative</td></tr>
    <tr><td>Peptide 3</td><td>$(\text{Val-Lys-Phe-Glu})_4$ (Alternating amphipathic)</td><td>176$^\circ$</td><td>72.8</td><td>12</td><td>Negative</td></tr>
    <tr><td>Peptide 4</td><td>$(\text{Val}_4\text{-Lys}_4\text{-Phe}_4\text{-Glu}_4)$ (Block sequence)</td><td>152$^\circ$</td><td>32.4</td><td>6</td><td>Negative</td></tr>
    <tr><td>Fibril WT</td><td>$A\beta_{42}$ Wild-Type (Cross-$\beta$ assembly)</td><td>179$^\circ$</td><td>> 95</td><td>880</td><td>Apple-green</td></tr>
    <tr><td>Fibril Mut</td><td>$A\beta_{42}$ Val18Pro / Phe20Pro mutant</td><td>N/A</td><td>< 20</td><td>18</td><td>Negative</td></tr>
  </tbody>
</table>
<p>Cross-$\beta$ diffraction produces characteristic X-ray reflections at 4.7 \AA\ (inter-strand spacing) and 10 \AA\ (inter-sheet stacking distance).</p>""",
    "qs": [
        {
            "q": "Why is the antiparallel beta-hairpin (Hairpin 1) thermodynamically more stable than the parallel beta-hairpin (Hairpin 2, Table 1)?",
            "ch": [
                "Parallel strands require interchain disulfide bonds between adjacent glycine residues to fold.",
                "Antiparallel strands permit collinear (180 deg) hydrogen bonds, which are electrostatically stronger.",
                "Antiparallel strands eliminate steric repulsion by aligning all side chains on a single face.",
                "Parallel strands generate an uncompensated macrodipole that hydrolyzes backbone peptide bonds."
            ],
            "a": 1,
            "e": "<strong>Collinear hydrogen bonding in antiparallel beta-sheets:</strong> Hydrogen bonds achieve maximal electrostatic stability and covalent orbital overlap when the donor ($N-H$), hydrogen, and acceptor ($O=C$) atoms are collinear (angle $\\approx 180^\\circ$). In antiparallel $\\beta$-sheets, the opposing chain directions allow planar, perpendicular, and collinear hydrogen bonds ($178^\\circ$ in Hairpin 1). In parallel $\\beta$-sheets, the identical chain orientations force hydrogen bonds to align at a slanted, distorted angle ($148^\\circ$ in Hairpin 2), weakening the dipoles and substantially decreasing thermal stability ($T_m = 41.2^\\circ\\text{C}$ vs $64.5^\\circ\\text{C}$).<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because glycine lacks a sulfhydryl group and cannot form disulfide bonds (cysteines form disulfides).<br>&bull; C is incorrect because beta-sheets alternate side chains above and below the sheet plane, not on a single face.<br>&bull; D is incorrect because parallel beta-sheets do not undergo spontaneous peptide bond hydrolysis; their instability is purely conformational/thermodynamic."
        },
        {
            "q": "In a fully extended beta-strand within an antiparallel sheet, what is the spatial orientation of adjacent side-chain R-groups along the primary sequence?",
            "ch": [
                "They project in the identical direction, clustering entirely on one surface of the pleated sheet.",
                "They rotate continuously around the peptide bond, forming a spiral with 3.6 residues per turn.",
                "They project alternately in opposite directions, pointing above and below the sheet plane.",
                "They fold back toward the peptide backbone to form covalent ester cross-links with amide nitrogens."
            ],
            "a": 2,
            "e": "<strong>Alternating stereochemistry of beta-strands:</strong> Because the peptide bond is planar and trans, the extended conformation of a $\\beta$-strand (dihedral angles $\\phi \\approx -140^\\circ, \\psi \\approx +135^\\circ$) causes the side-chain $R$-groups of consecutive amino acids to point in strictly alternating directions across the plane of the pleated sheet. Residue $i$ points 'up' (above the plane), residue $i+1$ points 'down' (below the plane), and residue $i+2$ points 'up'. The repeat distance for two consecutive residues on the same face is $7.0\\;\\text{\\AA}$ ($3.5\\;\\text{\\AA}$ per residue).<br><br><em>Distractor Traps:</em><br>&bull; A describes an impossible planar conformation that would produce severe steric clashes.<br>&bull; B describes an alpha-helix (3.6 residues per turn), not a beta-strand.<br>&bull; D describes covalent ester formation, which does not occur between side chains and backbone amide groups."
        },
        {
            "q": "Peptide 3 self-assembles into a stable beta-sheet (Tm = 72.8 deg C), whereas Peptide 4 shows minimal stability (Tm = 32.4 deg C, Table 1). Why does the alternating sequence favor sheet formation?",
            "ch": [
                "Alternating hydrophobic and polar residues segregate into two distinct faces upon beta-sheet folding.",
                "Block sequences cause adjacent side chains of opposite charge to attract and neutralize each other.",
                "The alternating sequence prevents the formation of inter-strand backbone carbonyl hydrogen bonds.",
                "Block hydrophobic segments undergo spontaneous oxidation to form cyclic lactones."
            ],
            "a": 0,
            "e": "<strong>Amphipathic beta-sheet segregation:</strong> In Peptide 3, hydrophobic residues (Val, Phe) alternate strictly with hydrophilic charged residues (Lys, Glu) in a $(\\text{Nonpolar-Polar-Nonpolar-Polar})_n$ pattern. Because side chains in a $\\beta$-strand alternate pointing above and below the sheet plane, all hydrophobic residues (Val, Phe) project onto one face of the sheet, while all hydrophilic residues (Lys, Glu) project onto the opposite face. The hydrophobic faces can pack together to bury nonpolar surface area away from water, while the polar face remains favorably solvated. In contrast, Peptide 4 has block sequences, preventing the formation of an amphipathic segregated surface and creating severe charge repulsion.<br><br><em>Distractor Traps:</em><br>&bull; B is incorrect because charge neutralization alone does not overcome the lack of an organized hydrophobic face.<br>&bull; C is incorrect because both peptides form backbone hydrogen bonds; alternating sequences stabilize, rather than prevent, these bonds.<br>&bull; D is nonsensical: aliphatic/aromatic side chains do not oxidize into cyclic lactones."
        },
        {
            "q": "In pathological amyloid fibrils displaying apple-green birefringence under polarized light, what is the relative orientation of beta-strands and hydrogen bonds?",
            "ch": [
                "Beta-strands wrap in concentric left-handed alpha-helices around a central hydrophobic pore.",
                "Beta-strands run parallel to the fibril axis, while hydrogen bonds run perpendicular to the axis.",
                "Beta-strands form planar rings interconnected entirely by intermolecular disulfide bridges.",
                "Beta-strands run perpendicular to the fibril axis, while hydrogen bonds run parallel to the axis."
            ],
            "a": 3,
            "e": "<strong>Cross-beta amyloid architecture:</strong> The structural hallmark of amyloid fibrils is the 'cross-$\\beta$' architecture. In cross-$\\beta$ fibrils, individual $\\beta$-strands run perpendicular to the long fibrillar growth axis. The continuous array of inter-strand hydrogen bonds runs parallel to the fibril axis, holding thousands of stacked $\\beta$-strands together in an indefinitely propagating ribbon. This regular repeating structure generates the characteristic X-ray diffraction pattern ($4.7\\;\\text{\\AA}$ meridian reflection) and binds Congo Red to produce apple-green birefringence under polarized light.<br><br><em>Distractor Traps:</em><br>&bull; A describes alpha-helical coiled-coils or channel proteins, not cross-beta amyloid fibrils.<br>&bull; B reverses the two axes: strands are perpendicular, not parallel, to the fibril axis.<br>&bull; C is incorrect because amyloid fibrils are stabilized by continuous non-covalent backbone hydrogen bonds, not disulfide cross-linked rings."
        },
        {
            "q": "Why did the Val18Pro / Phe20Pro mutations in Abeta42 abolish Thioflavin T fluorescence and prevent fibril formation (Table 1)?",
            "ch": [
                "Proline introduces a flexible beta-carbon that allows the peptide to adopt a molten globule state.",
                "Proline lacks an amide proton for inter-strand H-bonding and sterically disrupts sheet planarity.",
                "Proline's charged side chain causes massive electrostatic repulsion between adjacent beta-strands.",
                "Proline accelerates proteolytic cleavage of the peptide by endogenous alpha-secretase enzymes."
            ],
            "a": 1,
            "e": "<strong>Proline disruption of beta-sheet amyloid assembly:</strong> Fibrillization of $A\\beta_{42}$ into cross-$\\beta$ amyloid requires extensive, unbroken inter-strand hydrogen bonding and planar $\\beta$-sheet stacking. Introducing proline residues at positions 18 and 20 potently blocks amyloid formation for two reasons: (1) Proline's nitrogen lacks an amide hydrogen ($N-H$) when incorporated into a peptide bond, eliminating an essential hydrogen-bond donor required to hold the $\\beta$-sheet together. (2) Its rigid cyclic pyrrolidine ring introduces a steric protrusion that clashes with adjacent $\\beta$-strands and prevents the extended $\\phi, \\psi$ dihedral angles necessary for $\\beta$-sheet formation. As shown in Table 1, ThT fluorescence drops from 880 to 18, and Congo Red birefringence is abolished.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because proline is the most conformationally rigid amino acid, not flexible, and lacks a free beta-carbon.<br>&bull; C is incorrect because proline is an uncharged, nonpolar aliphatic amino acid.<br>&bull; D is incorrect because the assay used pure synthetic peptides in vitro without secretase enzymes."
        },
        {
            "q": "A bacterial outer membrane porin is composed of an antiparallel 16-stranded beta-barrel. How are amino acid residues organized in the transmembrane region of each strand?",
            "ch": [
                "Hydrophobic residues face the lipid membrane exterior, while hydrophilic residues face the pore.",
                "Hydrophilic residues face the lipid membrane exterior, while hydrophobic residues face the pore.",
                "Positively charged basic residues line both the exterior lipid interface and the interior pore.",
                "Glycine and proline residues strictly alternate to maintain high curvature around the pore."
            ],
            "a": 0,
            "e": "<strong>Transmembrane beta-barrel topology:</strong> Outer membrane porins are antiparallel $\\beta$-barrels that span the bacterial outer membrane, forming an aqueous channel for solute diffusion. In the transmembrane segments of each $\\beta$-strand, side chains alternate in a (Hydrophobic-Hydrophilic)$_n$ pattern. Because side chains alternate pointing in opposite directions, all hydrophobic nonpolar residues face outward toward the fatty acyl chains of the lipid bilayer, while hydrophilic (polar and charged) residues project inward to line the water-filled central pore.<br><br><em>Distractor Traps:</em><br>&bull; B states the exact inverse, which would place hydrophilic residues in contact with hydrophobic lipid tails, thermodynamically preventing membrane insertion.<br>&bull; C is incorrect because charged residues cannot be stably embedded in the nonpolar core of the lipid bilayer without high energy penalties.<br>&bull; D is incorrect because frequent proline and glycine residues would break the $\\beta$-strands and destroy the structural integrity of the barrel."
        }
    ]
}
