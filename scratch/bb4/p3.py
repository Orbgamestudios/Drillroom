# Passage 3: Topic 525 — Zymogen Proteolytic Activation Cascades: Enteropeptidase and Trypsin
# Answer keys: 1 (B), 2 (C), 0 (A), 3 (D), 0 (A), 2 (C)

p3_data = {
  "id": "exam_bb90_4_p3",
  "sec": "B/B",
  "topic": "Zymogen Proteolytic Activation Cascades: Enteropeptidase and Trypsin",
  "sheet": 3,
  "label": "Biological and Biochemical Foundations of Living Systems",
  "examId": "bb90_4",
  "passage": """<div class="ttl">Passage 3 (Questions 13&ndash;18)</div>
<p>To avert catastrophic autodigestion of the pancreas, pancreatic acinar cells synthesize endopeptidases and exopeptidases as inactive proenzymes, or zymogens. These zymogens (including trypsinogen, chymotrypsinogen, proelastase, and procarboxypeptidases) are condensed into membrane-bound zymogen granules alongside pancreatic secretory trypsin inhibitor (SPINK1). SPINK1 acts as a suicide peptide inhibitor that stoichiometrically neutralizes prematurely activated trypsin inside the acinus. Upon hormonal stimulation by cholecystokinin (CCK), zymogen granules fuse with the apical plasma membrane, releasing their contents into the pancreatic ductal system for delivery to the duodenum.</p>
<p>The physiological trigger of the intestinal digestive cascade is enteropeptidase (enterokinase), a heterodimeric serine protease localized to the brush-border membrane of duodenal enterocytes. Enteropeptidase displays exquisite substrate specificity, recognizing a polyanionic tetra-aspartyl motif ($\\text{Asp-Asp-Asp-Asp-Lys} \\downarrow \\text{Ile}$) at the N-terminus of trypsinogen. Enteropeptidase hydrolyzes the peptide bond immediately following the lysine residue, releasing a hexapeptide ($\\text{Val-Asp}_4\\text{-Lys}$) and liberating the mature trypsin chain.</p>
<p>Cleavage liberates a newly formed, positively charged N-terminus (Ile16). In the inactive zymogen, three flexible polypeptide segments known as the activation domain (loops 142&ndash;152, 184&ndash;193, and 216&ndash;223) are disordered, leaving the substrate-binding pocket and oxyanion hole improperly configured. Upon cleavage, the $\\alpha$-amino group of Ile16 inserts into the interior of the catalytic domain and forms an internal electrostatic salt bridge with the invariant carboxylate side chain of Asp194. This electrostatic interaction triggers a rigid structural transition that orders the activation domain, assembling the functional oxyanion hole (Gly193 and Ser195) and correctly orienting Asp189 at the base of the primary specificity pocket (S1 subsite).</p>
<p>Active trypsin then cleaves chymotrypsinogen, proelastase, and procarboxypeptidases, and catalyzes the autocatalytic cleavage of additional trypsinogen. Recombinant human cationic trypsinogen variants were purified and analyzed to investigate the cascade mechanism (Table 1).</p>
<table class="tbl">
  <caption>Table 1 Cleavage kinetics and catalytic parameters of recombinant human trypsinogen variants</caption>
  <thead>
    <tr><th>Trypsinogen Construct</th><th>Enteropeptidase Cleavage Rate ($\\text{nM}\\cdot\\text{s}^{-1}$)</th><th>Active Enzyme $k_{cat}$ on L-BAPNA ($\\text{s}^{-1}$)</th><th>$K_m$ for L-BAPNA (mM)</th><th>SPINK1 $K_i$ (nM)</th><th>Autolytic Half-Life $t_{1/2}$ (min)</th></tr>
  </thead>
  <tbody>
    <tr><td>Wild-Type (PRSS1)</td><td>48.5</td><td>42.0</td><td>0.82</td><td>0.05</td><td>65</td></tr>
    <tr><td>D194A</td><td>47.8</td><td>< 0.01</td><td>N/D</td><td>> 1000</td><td>> 600</td></tr>
    <tr><td>D189A</td><td>49.1</td><td>0.14</td><td>45.0</td><td>2.10</td><td>72</td></tr>
    <tr><td>R122H</td><td>48.2</td><td>41.8</td><td>0.84</td><td>0.05</td><td>> 600</td></tr>
  </tbody>
</table>""",
  "qs": [
    {
      "q": "Which structural feature of human trypsinogen is recognized specifically by duodenal enteropeptidase to initiate the cascade?",
      "ch": [
        "An internal hydrophobic stretch of aromatic residues flanking the active-site catalytic triad serine.",
        "A polyanionic tetra-aspartate sequence preceding a lysine residue located within the N-terminal peptide.",
        "A glycosylated C-terminal anchor motif that inserts directly into the duodenal brush-border bilayer.",
        "A covalent zinc-finger motif coordinated by invariant cysteine residues in the activation domain loop."
      ],
      "a": 1,
      "e": "<strong>Enteropeptidase substrate recognition:</strong> Enteropeptidase (enterokinase) exhibits high evolutionary fidelity for the canonical sequence $(\\text{Asp})_4\\text{-Lys} \\downarrow \\text{X}$. The catalytic domain of enteropeptidase possesses an extensive basic subsite lined with positively charged lysine and arginine residues that form multiple electrostatic interactions with the four consecutive aspartate side chains (polyanionic recognition sequence) of the trypsinogen propeptide. This stringent specificity ensures that enteropeptidase exclusively cleaves the $\\text{Lys-Ile}$ bond of trypsinogen at the mucosal brush border, preventing non-specific proteolysis in the intestinal lumen.<br><br><em>Distractor Traps:</em><br>&bull; A describes the recognition preference of chymotrypsin, which cleaves after bulky hydrophobic/aromatic residues, not enteropeptidase.<br>&bull; C describes GPI or transmembrane anchors that tether enteropeptidase to the enterocyte membrane, not the recognized sequence on trypsinogen.<br>&bull; D describes zinc-finger DNA-binding structural domains, which are absent in serine proteases and zymogens."
    },
    {
      "q": "Following enteropeptidase cleavage, what molecular rearrangement directly triggers the formation of the functional active site in trypsin?",
      "ch": [
        "Formation of an intermolecular disulfide crosslink between adjacent cysteine residues in the loop.",
        "Dissociation of an autoinhibitory regulatory dimer subunit from the catalytic monomeric domain.",
        "Insertion of the new N-terminal Ile16 into the protein interior to form a salt bridge with Asp194.",
        "Direct phosphorylation of Ser195 by an enteropeptidase-activated duodenal brush-border kinase."
      ],
      "a": 2,
      "e": "<strong>Conformational mechanism of trypsin activation:</strong> Cleavage of the hexapeptide from trypsinogen exposes a new N-terminus with a free $\\alpha$-amino group at residue Ile16. The hydrophobic isoleucine residue turns inward into the protein core, allowing its positively charged $\\alpha$-$\\text{NH}_3^+$ group to form an internal ionic bond (salt bridge) with the negatively charged $\\beta$-carboxylate of Asp194. This electrostatic linkage pulls loop regions of the 'activation domain' into their rigid, active conformations, correctly aligning the oxyanion hole (composed of main-chain amide nitrogens of Gly193 and Ser195) and the primary substrate-binding pocket (S1 subsite).<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because intramolecular disulfide bonds are already formed in the zymogen and do not rearrange during cleavage activation.<br>&bull; B describes the allosteric dissociation mechanism of protein kinase A (PKA), not monomeric serine proteases.<br>&bull; D describes covalent kinase phosphorylation cascades (like glycogen phosphorylase); trypsinogen is activated purely by proteolytic cleavage without phosphate addition."
    },
    {
      "q": "Based on the experimental data in Table 1, why does the D194A mutant fail to hydrolyze L-BAPNA despite normal enteropeptidase cleavage?",
      "ch": [
        "Inability to form the internal Ile16-Asp194 ion pair prevents maturation of the oxyanion hole and S1 pocket.",
        "Enteropeptidase fails to release the hexapeptide from the D194A mutant due to electrostatic steric clash.",
        "The D194A mutation abolishes the nucleophilicity of the catalytic triad histidine via charge neutralization.",
        "The mutant enzyme undergoes instantaneous irreversible autolytic digestion immediately following cleavage."
      ],
      "a": 0,
      "e": "<strong>Structural consequence of the D194A mutation:</strong> Table 1 shows that enteropeptidase cleaves the D194A trypsinogen propeptide at a normal wild-type rate ($47.8\\;\\text{nM}\\cdot\\text{s}^{-1}$ vs $48.5\\;\\text{nM}\\cdot\\text{s}^{-1}$), confirming that propeptide removal is intact. However, because residue 194 is mutated from aspartate to neutral alanine, the newly liberated $\\alpha$-amino group of Ile16 cannot form the indispensable internal salt bridge. Consequently, the activation domain remains disordered, the oxyanion hole cannot stabilize the tetrahedral transition state, and the S1 pocket cannot bind L-BAPNA, resulting in a negligible catalytic rate ($k_{cat} < 0.01\\;\\text{s}^{-1}$).<br><br><em>Distractor Traps:</em><br>&bull; B directly contradicts Table 1, which proves enteropeptidase cleaves D194A at the normal wild-type rate.<br>&bull; C confuses Asp194 (salt bridge partner) with Asp102 of the catalytic triad (Ser195-His57-Asp102).<br>&bull; D contradicts the half-life data in Table 1; D194A exhibits exceptional stability ($t_{1/2} > 600\\;\\text{min}$) precisely because it lacks catalytic activity to autodigest."
    },
    {
      "q": "What is the primary physiological function of pancreatic secretory trypsin inhibitor (SPINK1) synthesized within acinar cells?",
      "ch": [
        "It activates mucosal enteropeptidase within the duodenal lumen to ensure rapid postprandial digestion.",
        "It cleaves proelastase and chymotrypsinogen to prevent their premature accumulation inside secretory granules.",
        "It competitively displaces calcium ions from zymogen granules to induce secretory vesicle membrane fusion.",
        "It binds prematurely formed active trypsin with high affinity to prevent autocatalytic intrapancreatic injury."
      ],
      "a": 3,
      "e": "<strong>Role of SPINK1 in preventing pancreatitis:</strong> Under normal physiological conditions, small amounts ($< 0.5\\%$) of trypsinogen can undergo spontaneous or calcium-assisted autoactivation within pancreatic acinar cells or secretory ducts. To prevent this trace active trypsin from triggering an uncontrolled, destructive activation cascade that digests pancreatic parenchyma, acinar cells co-package SPINK1 into zymogen granules. SPINK1 binds to the active site of mature trypsin with picomolar affinity ($K_i = 0.05\\;\\text{nM}$, Table 1), acting as a physical plug that blocks substrate access and neutralizes trypsin activity before it can damage pancreatic tissue.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because SPINK1 inhibits trypsin; it does not activate brush-border enteropeptidase.<br>&bull; B is incorrect because SPINK1 is a protease inhibitor, not a proteolytic enzyme.<br>&bull; C is incorrect because calcium ions stabilize zymogen granules and are not displaced by SPINK1."
    },
    {
      "q": "During duodenal digestion, the generation of active trypsin over time displays a sigmoidal progress curve. What accounts for this non-linear kinetic profile?",
      "ch": [
        "Active trypsin catalyzes the cleavage and activation of its own zymogen via positive feedback amplification.",
        "Enteropeptidase activity is allosterically stimulated by high concentrations of bicarbonate ions in the bile.",
        "Duodenal peristalsis progressively removes competitive peptide inhibitors from the enterocyte brush border.",
        "Trypsinogen undergoes cooperativity where binding of one substrate molecule opens six adjacent active sites."
      ],
      "a": 0,
      "e": "<strong>Autocatalytic positive feedback of trypsin:</strong> Once duodenal enteropeptidase cleaves the initial molecules of trypsinogen to generate mature trypsin, active trypsin itself can recognize and cleave the basic lysine residue within the N-terminal propeptide of remaining trypsinogen molecules. This autocatalytic cleavage generates additional active trypsin, establishing an exponential positive feedback loop. Consequently, the activation progress curve displays an initial lag phase (enteropeptidase-dependent priming) followed by a steep, sigmoidal burst of rapid trypsin generation and subsequent downstream activation of all other pancreatic zymogens.<br><br><em>Distractor Traps:</em><br>&bull; B describes pancreatic ductal bicarbonate neutralization, which buffers pH but does not allosterically alter enteropeptidase to generate sigmoidal kinetics.<br>&bull; C describes physical mechanical propulsion, which does not govern molecular cleavage kinetics.<br>&bull; D is incorrect because trypsinogen is a monomeric enzyme lacking allosteric cooperative subunits."
    },
    {
      "q": "How does the primary substrate specificity of active trypsin compare to that of chymotrypsin and elastase?",
      "ch": [
        "Trypsin cleaves after acidic aspartate and glutamate residues, whereas chymotrypsin cleaves basic lysines.",
        "Trypsin cleaves after bulky aromatic residues, whereas chymotrypsin and elastase target basic side chains.",
        "Trypsin cleaves after positively charged lysine and arginine, whereas chymotrypsin targets bulky aromatics.",
        "Trypsin cleaves after small neutral residues, whereas chymotrypsin and elastase cleave branched aliphatics."
      ],
      "a": 2,
      "e": "<strong>Serine protease subsite specificities:</strong> The catalytic triads (Ser-His-Asp) of trypsin, chymotrypsin, and elastase are virtually identical, but their primary substrate binding pockets (S1 subsites) differ fundamentally. In trypsin, the base of the deep S1 pocket contains a negatively charged aspartate residue (Asp189, Table 1), which forms a favorable electrostatic salt bridge with positively charged basic side chains (Lys and Arg). In chymotrypsin, the S1 pocket is deep, uncharged, and lined with hydrophobic residues, favoring bulky aromatic side chains (Phe, Tyr, Trp). In elastase, the S1 pocket is shallow and obstructed by bulky valine and threonine residues (Val216 and Thr226), accommodating only small, uncharged residues (Ala, Gly, Val).<br><br><em>Distractor Traps:</em><br>&bull; A reverses the charge preferences; trypsin cleaves basic residues, not acidic ones.<br>&bull; B attributes chymotrypsin specificity to trypsin.<br>&bull; D attributes elastase specificity to trypsin."
    }
  ]
}
