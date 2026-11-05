import json

# Passage 1: CRISPR-Cas9
p1_html = """<div class="ttl">Passage 1 (Questions 1&ndash;6)</div>
<p>The bacterial CRISPR-Cas9 endonuclease has been repurposed as a versatile tool for targeted genome editing. The Cas9 protein from <i>Streptococcus pyogenes</i> associates with a single guide RNA (sgRNA) consisting of a 20-nucleotide spacer complementary to the target protospacer on genomic DNA. Cleavage requires the presence of a protospacer adjacent motif (PAM, 5&prime;-NGG-3&prime;) immediately 3&prime; to the target strand.</p>
<p>Upon PAM recognition, the Cas9 HNH and RuvC endonuclease domains induce a double-strand break (DSB) 3 base pairs upstream of the PAM. Cells repair this lesion via one of two competing pathways: non-homologous end joining (NHEJ), an error-prone mechanism that introduces insertions and deletions (indels) leading to frameshift knockouts; or homology-directed repair (HDR), a high-fidelity mechanism that uses an exogenous single-stranded donor oligonucleotide (ssODN) template to introduce precise sequence modifications.</p>
<p>Investigators sought to correct a pathogenic G-to-A missense mutation in the human <i>HBB</i> gene (encoding &beta;-globin) in patient-derived hematopoietic stem and progenitor cells (HSPCs). Cells were electroporated with Cas9:sgRNA ribonucleoprotein (RNP) complexes alongside an ssODN donor template. Because off-target cleavages pose mutagenic risks, the researchers synthesized an engineered high-fidelity Cas9 variant (eCas9) containing four alanine substitutions (K848A, K1003A, R1060A, and K855A) designed to weaken non-specific interactions with the non-target DNA strand. On-target cleavage, off-target indels at the homologous <i>HBD</i> pseudogene locus, and HDR rates were measured by high-throughput sequencing 48 h post-transfection.</p>
<table>
<tr><th>Condition</th><th>Cas9 Enzyme</th><th>sgRNA Spacer Length (nt)</th><th>On-Target Cleavage (%)</th><th>HDR Efficiency (%)</th><th>Off-Target (<i>HBD</i>) Indels (%)</th></tr>
<tr><td>1</td><td>WT-Cas9</td><td class="n">20</td><td class="n">78.4</td><td class="n">28.2</td><td class="n">14.6</td></tr>
<tr><td>2</td><td>WT-Cas9</td><td class="n">18 (truncated)</td><td class="n">74.1</td><td class="n">31.5</td><td class="n">1.8</td></tr>
<tr><td>3</td><td>eCas9</td><td class="n">20</td><td class="n">72.0</td><td class="n">33.0</td><td class="n">0.2</td></tr>
<tr><td>4</td><td>eCas9</td><td class="n">18 (truncated)</td><td class="n">41.3</td><td class="n">18.5</td><td class="n">&lt;0.05</td></tr>
<tr><td>5</td><td>Catalytically Dead Cas9 (dCas9)</td><td class="n">20</td><td class="n">&lt;0.1</td><td class="n">&lt;0.1</td><td class="n">&lt;0.05</td></tr>
</table>
<p class="cap"><b>Table 1</b> On-target activity, HDR repair, and off-target cleavages in edited HSPCs.</p>"""

p1_qs = [
    {
        "q": "Based on Table 1, which strategy provided the optimal balance of maintaining high on-target HDR editing (>30%) while minimizing off-target genotoxicity at the HBD locus?",
        "ch": [
            "WT-Cas9 with a full-length 20-nt sgRNA",
            "eCas9 with a 20-nt sgRNA",
            "eCas9 with a truncated 18-nt sgRNA",
            "dCas9 with a 20-nt sgRNA"
        ],
        "a": 1,
        "e": "<strong>Compare on-target HDR and off-target rates:</strong> Condition 3 (eCas9 with 20-nt sgRNA) achieved 33.0% HDR efficiency while slashing off-target indels from 14.6% down to 0.2% (a 73-fold reduction). Condition 4 dropped off-target cleavages even further, but on-target HDR was compromised (dropping to 18.5%)."
    },
    {
        "q": "The engineered eCas9 variant contains four lysine/arginine-to-alanine mutations (K848A, K1003A, R1060A, K855A). At physiological pH (7.4), how do these substitutions alter the electrostatic interactions between Cas9 and the non-target DNA strand?",
        "ch": [
            "They replace positively charged basic side chains with neutral nonpolar residues, weakening non-specific electrostatic attractions to the negatively charged phosphodiester backbone.",
            "They replace negatively charged acidic residues with basic side chains, repelling the ribose rings.",
            "They introduce covalent disulfide linkages between the enzyme and the DNA target.",
            "They increase the net positive surface charge of the protein, tightening non-specific DNA binding."
        ],
        "a": 0,
        "e": "<strong>Lysine and Arginine are positively charged at physiological pH:</strong> At pH 7.4, Lys (pKa ~10.5) and Arg (pKa ~12.5) carry cationic ammonium/guanidinium groups that electrostatically attract the polyanionic phosphate backbone of DNA. Replacing them with neutral alanine (Ala) side chains removes these non-specific positive charges, so Cas9 requires near-perfect Watson-Crick base-pairing to undergo the conformational activation required for cleavage."
    },
    {
        "q": "Homology-directed repair (HDR) occurs almost exclusively during which phases of the eukaryotic cell cycle?",
        "ch": [
            "G0 and early G1 phase",
            "Late S and G2 phase",
            "Prophase of mitosis only",
            "Equally across all cell cycle phases"
        ],
        "a": 1,
        "e": "<strong>Cell cycle regulation of DNA double-strand break repair:</strong> HDR relies on homologous sister chromatids or exogenous homologous donor templates and requires resection by the MRN complex and RAD51. These homologous recombination enzymes are highly expressed and active only during late S and G2 phases when sister chromatids are present. In G1/G0, NHEJ dominates."
    },
    {
        "q": "The catalytically dead Cas9 (dCas9) in Condition 5 lacks endonuclease cleavage activity because point mutations (D10A and H840A) inactivate the RuvC and HNH catalytic domains. What biochemical property does dCas9 still retain?",
        "ch": [
            "Sequence-specific binding to the target genomic locus guided by sgRNA and PAM",
            "Exonuclease degradation of single-stranded RNA",
            "ATP-dependent DNA unwinding (helicase activity)",
            "Ligation of nicked phosphodiester bonds"
        ],
        "a": 0,
        "e": "<strong>dCas9 retains high-affinity, sequence-specific DNA binding:</strong> Inactivating the catalytic aspartate and histidine residues abolishes phosphodiester hydrolysis (cleavage), but the structural domains responsible for sgRNA binding, PAM interrogation, and R-loop formation remain completely intact, allowing dCas9 to act as a programmable sequence-specific DNA-binding platform."
    },
    {
        "q": "The PAM sequence for SpCas9 is 5'-NGG-3'. If the non-target strand sequence is 5'-ATCGG-3', what is the sequence of the corresponding PAM on the target (cleaved) strand?",
        "ch": [
            "5'-CCGAT-3'",
            "5'-CC-3' (oriented 5' to 3')",
            "5'-GG-3'",
            "3'-GG-5'"
        ],
        "a": 1,
        "e": "<strong>Antiparallel complementary base-pairing:</strong> If the PAM on the non-target strand is 5'-NGG-3', the complementary target strand must have the antiparallel sequence: 3'-NCC-5', which reads 5'-CCN-3' in the standard 5'-to-3' direction."
    },
    {
        "q": "If the pathogenic mutation in the HBB gene is an A-to-T transversion in the coding strand converting codon GAG to GTG, what is the resulting amino acid substitution in &beta;-globin?",
        "ch": [
            "Glutamate to Valine (the classic Sickle Cell Anemia mutation)",
            "Glutamate to Lysine",
            "Aspartate to Alanine",
            "Glutamine to Leucine"
        ],
        "a": 0,
        "e": "<strong>Sickle cell anemia genetics:</strong> GAG encodes Glutamate (Glu, an acidic, negatively charged amino acid). GTG (GUG in mRNA) encodes Valine (Val, a hydrophobic, nonpolar amino acid). This Glu6Val substitution on the surface of &beta;-globin creates a hydrophobic patch that promotes polymerization into hemoglobin S polymers under deoxygenated conditions."
    }
]

# Passage 2: Pyruvate Dehydrogenase Complex
p2_html = """<div class="ttl">Passage 2 (Questions 7&ndash;12)</div>
<p>The pyruvate dehydrogenase complex (PDC) is a 9.5-MDa multienzyme assembly localized within the mitochondrial matrix that links glycolysis to the tricarboxylic acid (TCA) cycle. PDC catalyzes the irreversible oxidative decarboxylation of pyruvate to acetyl-CoA:</p>
<p style="text-align:center;font-style:italic">Pyruvate + NAD<sup>+</sup> + CoA-SH &rarr; Acetyl-CoA + NADH + CO<sub>2</sub> + H<sup>+</sup> &nbsp;&nbsp;&nbsp;&nbsp;(&Delta;G&deg;&prime; = &minus;33.4 kJ/mol)</p>
<p>The complex comprises three catalytic enzymes requiring five non-protein cofactors: pyruvate dehydrogenase (E1, thiamine pyrophosphate [TPP]), dihydrolipoyl transacetylase (E2, lipoic acid and coenzyme A), and dihydrolipoyl dehydrogenase (E3, flavin adenine dinucleotide [FAD] and NAD<sup>+</sup>).</p>
<p>PDC activity is tightly regulated by covalent modification: pyruvate dehydrogenase kinase (PDK1&ndash;4) phosphorylates three specific serine residues on the E1&alpha; subunit (Ser264, Ser271, Ser203), inactivating the enzyme. Conversely, pyruvate dehydrogenase phosphatase (PDP1&ndash;2), stimulated by Ca<sup>2+</sup> and Mg<sup>2+</sup>, dephosphorylates these residues to restore activity.</p>
<p>In many solid tumors, hypoxia-inducible factor 1&alpha; (HIF-1&alpha;) upregulates PDK1, shunting pyruvate away from oxidative phosphorylation toward lactate dehydrogenase A (LDHA) despite adequate oxygen availability (the Warburg effect). Investigators treated glioblastoma cells with dichloroacetate (DCA), an investigational PDK inhibitor, or Compound <b>K</b>, a novel allosteric E1 activator. Intracellular metabolite levels, mitochondrial membrane potential (&Delta;&Psi;<sub>m</sub>), and reactive oxygen species (ROS) production were quantified.</p>
<table>
<tr><th>Treatment</th><th>PDC Activity (% of Control)</th><th>Lactate Production (mmol/L)</th><th>Oxygen Consumption Rate (pmol O<sub>2</sub>/min)</th><th>NADH/NAD<sup>+</sup> Ratio</th><th>Cell Viability (%)</th></tr>
<tr><td>Control (Vehicle)</td><td class="n">100</td><td class="n">18.4</td><td class="n">42.0</td><td class="n">0.25</td><td class="n">100</td></tr>
<tr><td>Hypoxia (1% O<sub>2</sub>)</td><td class="n">18</td><td class="n">44.2</td><td class="n">9.5</td><td class="n">0.68</td><td class="n">96</td></tr>
<tr><td>DCA (5 mM)</td><td class="n">280</td><td class="n">6.1</td><td class="n">86.5</td><td class="n">0.42</td><td class="n">58</td></tr>
<tr><td>Compound K (10 &mu;M)</td><td class="n">315</td><td class="n">4.8</td><td class="n">94.0</td><td class="n">0.48</td><td class="n">42</td></tr>
<tr><td>DCA + Rotenone (1 &mu;M)</td><td class="n">265</td><td class="n">38.0</td><td class="n">12.0</td><td class="n">0.95</td><td class="n">88</td></tr>
</table>
<p class="cap"><b>Table 1</b> Metabolic parameters and tumor viability following PDC modulation.</p>"""

p2_qs = [
    {
        "q": "Based on the reaction mechanism and cofactors described in the passage, which cofactor undergoes reversible oxidation-reduction between a disulfide ring and a dithiol form during E2 catalysis?",
        "ch": [
            "Thiamine pyrophosphate (TPP)",
            "Lipoic acid (lipoamide)",
            "Coenzyme A",
            "Pyridoxal phosphate (PLP)"
        ],
        "a": 1,
        "e": "<strong>Lipoic acid forms a swinging arm:</strong> Lipoamide is covalently linked to a lysine residue of E2. Its terminal dithiolane ring swings between the E1 active site (where it oxidizes the hydroxyethyl-TPP intermediate to an acetyl group, forming a thioester) and the E3 active site. In the process, the cyclic disulfide is reduced to a dihydrolipoyl dithiol. E3 then uses FAD to re-oxidize the dithiol back to the cyclic disulfide."
    },
    {
        "q": "According to Table 1, administering dichloroacetate (DCA) to glioblastoma cells causes which metabolic reconfiguration?",
        "ch": [
            "Reactivation of PDC, driving pyruvate into the mitochondria and boosting oxygen consumption rate while suppressing lactate production",
            "Complete inhibition of glycolysis, preventing glucose entry into cells",
            "Inhibition of Complex I of the electron transport chain, causing a surge in lactate",
            "Phosphorylation of E1&alpha; serine residues, triggering apoptotic cell death"
        ],
        "a": 0,
        "e": "<strong>DCA inhibits PDK, relieving inhibition of PDC:</strong> Table 1 shows that DCA boosts PDC activity from 100% to 280%, cuts lactate production from 18.4 to 6.1 mmol/L, and more than doubles oxygen consumption rate (OCR) from 42.0 to 86.5 pmol O₂/min. By inhibiting the kinase PDK, PDC remains unphosphorylated (active), diverting pyruvate away from fermentation and into mitochondrial oxidation."
    },
    {
        "q": "Why does adding rotenone to DCA-treated cells (Row 5) increase lactate production to 38.0 mmol/L despite PDC remaining active (265%)?",
        "ch": [
            "Rotenone directly activates lactate dehydrogenase A by covalent modification.",
            "Rotenone inhibits Complex I, blocking NADH oxidation in the electron transport chain and forcing cells to regenerate NAD⁺ via lactate fermentation.",
            "Rotenone prevents pyruvate from crossing the outer mitochondrial membrane.",
            "Rotenone dephosphorylates pyruvate dehydrogenase kinase."
        ],
        "a": 1,
        "e": "<strong>Rotenone blocks Complex I of the ETC:</strong> When Complex I is blocked, electrons cannot be transferred from NADH to ubiquinone. The NADH/NAD⁺ ratio surges to 0.95 (Row 5). Without mitochondrial NAD⁺ regeneration, oxidative phosphorylation halts (OCR drops to 12.0), and cells must rely on lactate dehydrogenase (Pyruvate + NADH + H⁺ &rarr; Lactate + NAD⁺) to replenish cytosolic NAD⁺ to keep glycolysis running."
    },
    {
        "q": "PDK is allosterically activated by which set of metabolites, signaling high cellular energy charge and feedback inhibition of PDC?",
        "ch": [
            "Pyruvate, ADP, and NAD⁺",
            "Acetyl-CoA, NADH, and ATP",
            "Coenzyme A, AMP, and Ca²⁺",
            "Lactate, FAD, and glucose"
        ],
        "a": 1,
        "e": "<strong>Allosteric regulation of PDK:</strong> High energy charge and accumulation of products (ATP, Acetyl-CoA, and NADH) allosterically stimulate PDK. Active PDK phosphorylates and inactivates PDC, shutting off unnecessary pyruvate decarboxylation when downstream fuels are already abundant. Conversely, ADP, pyruvate, and NAD⁺ inhibit PDK, keeping PDC active."
    },
    {
        "q": "Patients with severe chronic thiamine (vitamin B1) deficiency (beriberi or Wernicke-Korsakoff syndrome) accumulate which metabolites in blood plasma?",
        "ch": [
            "Pyruvate and &alpha;-ketoglutarate",
            "Oxaloacetate and citrate",
            "Acetyl-CoA and acetoacetate",
            "Succinate and fumarate"
        ],
        "a": 0,
        "e": "<strong>TPP is the cofactor for &alpha;-keto acid dehydrogenases:</strong> Thiamine is the precursor to thiamine pyrophosphate (TPP), the essential cofactor for both the pyruvate dehydrogenase complex (E1) and the &alpha;-ketoglutarate dehydrogenase complex in the TCA cycle. Deficiency of TPP impairs both complexes, causing their respective substrate &alpha;-keto acids (pyruvate and &alpha;-ketoglutarate) to accumulate in blood."
    },
    {
        "q": "Under standard biological conditions (&Delta;G&deg;&prime; = &minus;33.4 kJ/mol at 298 K), the oxidative decarboxylation of pyruvate has an equilibrium constant K&prime;_eq closest to: (Note: R = 8.314 J/(mol&middot;K), ln(10) &asymp; 2.303).",
        "ch": [
            "1.4 &times; 10⁻⁶",
            "1.0",
            "7.1 &times; 10⁵",
            "5.2 &times; 10¹⁴"
        ],
        "a": 2,
        "e": "<strong>Calculate K&prime;_eq from &Delta;G&deg;&prime;:</strong><br>&Delta;G&deg;&prime; = &minus;RT ln(K&prime;_eq)<br>&minus;33,400 J/mol = &minus;(8.314 &times; 298) ln(K&prime;_eq) = &minus;2478 ln(K&prime;_eq)<br>ln(K&prime;_eq) = 33,400 / 2478 &asymp; 13.48<br>log₁₀(K&prime;_eq) = 13.48 / 2.303 &asymp; 5.85 &rArr; K&prime;_eq = 10⁵˙⁸⁵ &asymp; 7.1 &times; 10⁵."
    }
]

# Passage 3: SGLT2 and Renal Tubular Transport
p3_html = """<div class="ttl">Passage 3 (Questions 13&ndash;18)</div>
<p>In the mammalian nephron, approximately 180 grams of D-glucose are filtered through glomeruli daily, virtually all of which is reabsorbed along the proximal convoluted tubule (PCT). Glucose reabsorption is mediated sequentially by two distinct transport systems: apical sodium-glucose cotransporters (SGLTs) and basolateral facilitated glucose transporters (GLUTs).</p>
<p>The early S1 segment of the PCT expresses SGLT2, a high-capacity, low-affinity symporter with a 1:1 Na<sup>+</sup>:glucose stoichiometric coupling ratio that accounts for ~90% of renal glucose reclamation. SGLT2 couples the uphill transport of glucose into the tubular epithelial cell to the steep inward electrochemical gradient of sodium established by the basolateral Na<sup>+</sup>/K<sup>+</sup>-ATPase. Reabsorbed intracellular glucose subsequently exits across the basolateral membrane down its concentration gradient into peritubular capillaries via GLUT2, a facilitated uniporter.</p>
<p>In diabetic nephropathy, sustained hyperglycemia upregulates SGLT2 expression, exacerbating glucotoxicity. SGLT2 inhibitors (gliflozins) are pharmacological agents that block glucose reabsorption, inducing therapeutic glucosuria. To characterize the inhibitory mechanism of dapagliflozin, investigators expressed recombinant human SGLT2 in HEK-293 cells and measured initial rates of [<sup>14</sup>C]-&alpha;-methyl-D-glucopyranoside (&alpha;-MDG, a non-metabolizable glucose analog) uptake across varying substrate concentrations with and without dapagliflozin.</p>
<table>
<tr><th>Condition</th><th>V<sub>max</sub> (nmol / 10<sup>6</sup> cells / min)</th><th>K<sub>m</sub> (&mu;M)</th><th>Lineweaver-Burk Characteristics</th></tr>
<tr><td>Control (Vehicle)</td><td class="n">48.0</td><td class="n">1200.0</td><td>Reference line (y-int = 0.021, x-int = &minus;0.00083)</td></tr>
<tr><td>Dapagliflozin (2.5 nM)</td><td class="n">47.8</td><td class="n">3600.0</td><td>Same y-intercept, x-intercept shifts rightward (&minus;0.00028)</td></tr>
<tr><td>Dapagliflozin (10.0 nM)</td><td class="n">48.2</td><td class="n">10800.0</td><td>Same y-intercept, x-intercept shifts rightward (&minus;0.00009)</td></tr>
<tr><td>Ouabain (100 &mu;M)</td><td class="n">2.1</td><td class="n">1250.0</td><td>V<sub>max</sub> crashes >95%, K<sub>m</sub> unchanged</td></tr>
</table>
<p class="cap"><b>Table 1</b> Kinetic parameters of SGLT2 &alpha;-MDG uptake under pharmacological inhibition.</p>"""

p3_qs = [
    {
        "q": "Based on Table 1, dapagliflozin inhibits SGLT2 via which kinetic mechanism?",
        "ch": [
            "Competitive inhibition, because K_m increases while V_max remains unchanged",
            "Noncompetitive inhibition, because V_max decreases while K_m remains constant",
            "Uncompetitive inhibition, because both V_max and K_m decrease proportionally",
            "Irreversible covalent inactivation of the sodium binding pocket"
        ],
        "a": 0,
        "e": "<strong>Lineweaver-Burk diagnostic for competitive inhibition:</strong> Table 1 shows that increasing dapagliflozin concentrations cause K<sub>m</sub> to rise dramatically (1200 &rarr; 3600 &rarr; 10800 &mu;M) while V<sub>max</sub> remains identical (~48.0 nmol/min, same y-intercept 1/V<sub>max</sub>). Because high substrate concentrations successfully outcompete the inhibitor to reach V<sub>max</sub>, dapagliflozin is a classic competitive inhibitor."
    },
    {
        "q": "Why does pre-treating cells with ouabain (a cardiac glycoside that selectively inhibits the Na⁺/K⁺-ATPase) cause SGLT2-mediated glucose uptake to collapse by >95% (Table 1, Row 4)?",
        "ch": [
            "Ouabain directly binds to the glucose-binding pocket of SGLT2.",
            "Dissipation of the basolateral sodium gradient eliminates the electrochemical driving force required for secondary active sodium-glucose cotransport.",
            "Ouabain hydrolyzes cellular ATP, depleting the energy source directly hydrolyzed by SGLT2.",
            "Ouabain causes immediate proteolytic degradation of apical brush-border proteins."
        ],
        "a": 1,
        "e": "<strong>SGLT2 is a secondary active transporter:</strong> SGLT2 does not hydrolyze ATP directly; it relies on the inward Na⁺ gradient maintained by the basolateral Na⁺/K⁺-ATPase. Ouabain blocks the Na⁺/K⁺-ATPase, allowing intracellular Na⁺ to rise and dissipating the transmembrane Na⁺ gradient. Without this inward electrochemical gradient, secondary active transport via SGLT2 ceases."
    },
    {
        "q": "In a healthy adult, when blood glucose concentration exceeds the renal threshold (transport maximum T_m &asymp; 375 mg/min, corresponding to plasma glucose > 200 mg/dL), what occurs in the urine?",
        "ch": [
            "The rate of glucose excretion drops to zero due to distal nephron compensation.",
            "SGLT2 transporters become saturated, and excess filtered glucose appears in the urine (glucosuria), causing osmotic diuresis.",
            "Urine osmolarity falls below 50 mOsm/L due to rapid water reabsorption in the collecting duct.",
            "Plasma bicarbonate is completely lost into the tubular lumen."
        ],
        "a": 1,
        "e": "<strong>Renal threshold and transport maximum (T_m):</strong> When the filtered load of glucose exceeds the saturation capacity (T_m) of proximal tubule SGLT transporters, the excess glucose cannot be reabsorbed and remains in the tubular fluid. This unabsorbed luminal solute exerts an osmotic force that inhibits water reabsorption, producing glucosuria and osmotic diuresis (polyuria)."
    },
    {
        "q": "Which characteristic distinguishes the apical SGLT2 transporter from the basolateral GLUT2 transporter in proximal tubular epithelial cells?",
        "ch": [
            "SGLT2 moves glucose down its concentration gradient, whereas GLUT2 moves glucose against its gradient.",
            "SGLT2 is a secondary active symporter requiring sodium, whereas GLUT2 is a passive uniporter mediating facilitated diffusion.",
            "GLUT2 hydrolyzes ATP directly, whereas SGLT2 hydrolyzes GTP.",
            "GLUT2 is exclusively expressed on the apical brush border membrane."
        ],
        "a": 1,
        "e": "<strong>SGLT vs GLUT transport mechanisms:</strong> SGLT2 is a secondary active cotransporter (symporter) located on the apical membrane that couples uphill glucose transport to downhill Na⁺ influx. GLUT2 is an uncoupled facilitated diffusion carrier (uniporter) on the basolateral membrane that allows accumulated intracellular glucose to exit passively down its concentration gradient into the interstitium."
    },
    {
        "q": "SGLT1, located in the late S3 segment of the PCT and the small intestine, has a 2:1 Na⁺:glucose coupling stoichiometry, whereas SGLT2 has a 1:1 stoichiometry. Thermodynamically, this 2:1 ratio enables SGLT1 to:",
        "ch": [
            "transport glucose against a significantly steeper intracellular-to-extracellular concentration gradient than SGLT2.",
            "operate independently of the transmembrane electrical potential.",
            "hydrolyze two molecules of ATP per glucose molecule transported.",
            "reabsorb sodium without reabsorbing any chloride or water."
        ],
        "a": 0,
        "e": "<strong>Thermodynamic driving force scales with stoichiometric coupling:</strong> The free energy available for transport is &Delta;G = n &times; &Delta;&mu;<sub>Na+</sub>. Coupling two Na⁺ ions per glucose molecule (n = 2) doubles the electrical and chemical driving force compared to 1:1 coupling. This allows SGLT1 in the late S3 segment to scavenge residual luminal glucose even when luminal glucose concentration is extremely low, concentrating it up to 10,000-fold."
    },
    {
        "q": "A diabetic patient starting dapagliflozin therapy experiences a 4 mmHg reduction in systolic blood pressure and mild volume contraction. What physiological mechanism explains this systemic effect?",
        "ch": [
            "Direct antagonism of vascular &alpha;₁-adrenergic receptors by dapagliflozin",
            "Osmotic diuresis and natriuresis resulting from excretion of unabsorbed glucose and sodium in the tubular fluid",
            "Suppression of aldosterone synthesis in the adrenal cortex",
            "Stimulation of atrial natriuretic peptide (ANP) release from cardiac myocytes"
        ],
        "a": 1,
        "e": "<strong>Glucosuria drives osmotic natriuresis:</strong> By inhibiting SGLT2, both glucose and sodium reabsorption in the proximal tubule are inhibited. The luminal glucose and Na⁺ hold water in the nephron, producing mild osmotic diuresis and natriuresis. This net reduction in intravascular plasma volume lowers systemic venous return, cardiac output, and mean arterial blood pressure."
    }
]

# Passage 4: GPCR & Beta-Arrestin Biased Signaling
p4_html = """<div class="ttl">Passage 4 (Questions 19&ndash;24)</div>
<p>The &beta;<sub>2</sub>-adrenergic receptor (&beta;<sub>2</sub>AR) is a prototypical family A G-protein-coupled receptor (GPCR) that regulates airway smooth muscle tone and myocardial contractility. Agonist binding induces a conformational change that promotes coupling to the heterotrimeric stimulatory G-protein (G&alpha;<sub>s</sub>&beta;&gamma;), stimulating exchange of GDP for GTP on the G&alpha;<sub>s</sub> subunit. Dissociated G&alpha;<sub>s</sub>-GTP activates adenylyl cyclase (AC), catalyzing conversion of ATP to cyclic adenosine monophosphate (cAMP). Elevated intracellular cAMP binds regulatory subunits of protein kinase A (PKA), releasing active catalytic subunits that phosphorylate downstream targets including myosin light chain kinase (MLCK) and phospholamban.</p>
<p>To terminate signaling and prevent excitotoxicity, active &beta;<sub>2</sub>ARs undergo homologous desensitization. G-protein-coupled receptor kinases (GRK2/3) phosphorylate specific serine and threonine residues within the receptor's intracellular C-terminal tail. Phosphorylated receptors recruit &beta;-arrestin-1 and &beta;-arrestin-2, which sterically interdict further G-protein coupling and target the receptor to clathrin-coated pits for dynamin-dependent endocytosis.</p>
<p>Pharmacologists designed \"biased agonists\" that selectively stimulate either the G&alpha;<sub>s</sub>-cAMP pathway (promoting bronchodilation) or the &beta;-arrestin pathway (promoting receptor internalization). Three compounds were evaluated in human bronchial smooth muscle cells: isoproterenol (unbiased full agonist), Compound <b>B1</b> (G&alpha;<sub>s</sub>-biased agonist), and Compound <b>B2</b> (&beta;-arrestin-biased agonist).</p>
<table>
<tr><th>Compound</th><th>cAMP Accumulation EC<sub>50</sub> (nM)</th><th>E<sub>max</sub> (% of Isoproterenol)</th><th>&beta;-Arrestin Recruitment E<sub>max</sub> (%)</th><th>Receptor Internalization at 60 min (%)</th></tr>
<tr><td>Isoproterenol</td><td class="n">5.2</td><td class="n">100</td><td class="n">100</td><td class="n">82</td></tr>
<tr><td>Compound B1</td><td class="n">4.8</td><td class="n">98</td><td class="n">8</td><td class="n">12</td></tr>
<tr><td>Compound B2</td><td class="n">>10,000</td><td class="n">&lt;5</td><td class="n">92</td><td class="n">78</td></tr>
<tr><td>Propranolol (Antagonist)</td><td class="n">—</td><td class="n">0</td><td class="n">0</td><td class="n">&lt;2</td></tr>
</table>
<p class="cap"><b>Table 1</b> Functional pharmacology of &beta;₂AR biased ligands in airway smooth muscle.</p>"""

p4_qs = [
    {
        "q": "Based on Table 1, why would Compound B1 be expected to cause LESS tachyphylaxis (loss of therapeutic efficacy over time) than isoproterenol during chronic asthma therapy?",
        "ch": [
            "B1 covalently binds to adenylyl cyclase, permanently locking it in an active conformation.",
            "B1 selectively activates G&alpha;_s signaling with minimal &beta;-arrestin recruitment, preventing receptor phosphorylation-mediated internalization and downregulation.",
            "B1 promotes rapid endocytosis and lysosomal degradation of &beta;₂ARs.",
            "B1 acts as an irreversible antagonist that permanently occupies the orthosteric binding pocket."
        ],
        "a": 1,
        "e": "<strong>Biased signaling avoids receptor desensitization:</strong> Chronic administration of full agonists like isoproterenol recruits &beta;-arrestin (100%), inducing 82% receptor internalization and tolerance (tachyphylaxis). Compound B1 is G&alpha;<sub>s</sub>-biased: it achieves full bronchodilatory cAMP production (E<sub>max</sub> = 98%) but minimal &beta;-arrestin recruitment (8%) and internalization (12%), maintaining functional surface receptors during chronic therapy."
    },
    {
        "q": "How does G&alpha;_s intrinsically terminate its own activation of adenylyl cyclase?",
        "ch": [
            "By phosphorylating cAMP into AMP",
            "Via intrinsic GTPase activity that hydrolyzes bound GTP to GDP, allowing re-association with the G&beta;&gamma; dimer",
            "By dissociating from the plasma membrane and entering the nucleus",
            "Through ubiquitination and degradation by the 26S proteasome"
        ],
        "a": 1,
        "e": "<strong>Intrinsic GTPase activity of G&alpha; subunits:</strong> G&alpha; subunits possess slow intrinsic GTPase enzymatic activity that cleaves the terminal phosphate of bound GTP: G&alpha;-GTP &rarr; G&alpha;-GDP + P<sub>i</sub>. Once bound to GDP, G&alpha; undergoes a conformational shift that lowers its affinity for adenylyl cyclase and restores high affinity for the G&beta;&gamma; dimer, reforming the inactive heterotrimer."
    },
    {
        "q": "Cholera toxin locks G&alpha;_s in a permanently active state by catalyzing ADP-ribosylation of an essential arginine residue. What physiological consequence occurs in intestinal epithelial cells exposed to cholera toxin?",
        "ch": [
            "cAMP levels crash to zero, blocking all ion transport.",
            "Constitutively elevated cAMP continuously activates PKA, which phosphorylates CFTR chloride channels, causing massive secretion of Cl⁻ and water (watery diarrhea).",
            "Phospholipase C is hyperactivated, generating excess IP₃ and DAG.",
            "Intestinal cells undergo immediate necrosis due to osmotic cell swelling."
        ],
        "a": 1,
        "e": "<strong>Cholera toxin mechanism of action:</strong> ADP-ribosylation inhibits the GTPase activity of G&alpha;<sub>s</sub>, trapping it in the active GTP-bound form. Adenylyl cyclase runs unchecked, causing intracellular cAMP to skyrocket. Hyperactivated PKA continuously phosphorylates CFTR (cystic fibrosis transmembrane conductance regulator) channels on the apical membrane, driving massive efflux of chloride, followed by sodium and water into the intestinal lumen."
    },
    {
        "q": "In airway smooth muscle, how does PKA activation by &beta;₂AR stimulation promote muscle relaxation (bronchodilation)?",
        "ch": [
            "PKA phosphorylates and inactivates Myosin Light Chain Kinase (MLCK), while stimulating Ca²⁺ extrusion into the sarcoplasmic reticulum.",
            "PKA phosphorylates actin filaments, causing immediate sarcomere cleavage.",
            "PKA activates voltage-gated L-type calcium channels, flooding the cytoplasm with calcium.",
            "PKA stimulates IP₃ receptor opening on the endoplasmic reticulum."
        ],
        "a": 0,
        "e": "<strong>Molecular mechanism of smooth muscle relaxation:</strong> PKA phosphorylates MLCK, significantly lowering its affinity for the Ca²⁺-calmodulin complex. Unphosphorylated myosin cannot bind actin. Furthermore, PKA phosphorylates phospholamban (activating SERCA to pump Ca²⁺ back into the sarcoplasmic reticulum) and open BK potassium channels (hyperpolarizing the cell and closing Ca²⁺ channels), leading to smooth muscle relaxation."
    },
    {
        "q": "If a cell is microinjected with a non-hydrolyzable GTP analog (GTP-&gamma;-S), the activation of adenylyl cyclase by isoproterenol will:",
        "ch": [
            "become irreversible and independent of continued agonist exposure.",
            "be completely abolished because GTP-&gamma;-S acts as a competitive inhibitor of G&alpha;_s.",
            "cause immediate degradation of the receptor.",
            "fail to dissociate the G&beta;&gamma; subunits."
        ],
        "a": 0,
        "e": "<strong>Non-hydrolyzable GTP analogs prevent deactivation:</strong> GTP-&gamma;-S binds to G&alpha;<sub>s</sub> in place of GTP, but its terminal thiophosphate bond cannot be hydrolyzed by the G&alpha; GTPase domain. G&alpha;<sub>s</sub> is locked in its active conformation, sustaining adenylyl cyclase activation indefinitely even after isoproterenol is washed out."
    },
    {
        "q": "Phosphodiesterase-4 (PDE4) inhibitors, such as roflumilast, are used in chronic obstructive pulmonary disease (COPD). Their therapeutic mechanism synergizes with &beta;₂-agonists by:",
        "ch": [
            "blocking degradation of cAMP to 5'-AMP, prolonging PKA activation.",
            "blocking synthesis of ATP from ADP.",
            "directly activating &beta;-arrestin recruitment.",
            "inhibiting G&alpha;_s translocation to the cell surface."
        ],
        "a": 0,
        "e": "<strong>PDE enzymes degrade cyclic nucleotides:</strong> Phosphodiesterases hydrolyze the 3',5'-cyclic phosphate bond of cAMP, converting it to inactive 5'-AMP. Inhibiting PDE4 blocks cAMP breakdown. When combined with &beta;₂AR agonists (which stimulate cAMP synthesis), intracellular cAMP accumulation is amplified, maximizing bronchodilation."
    }
]

# Passage 5: Cardiac Ventricular Electrophysiology & Long QT
p5_html = """<div class="ttl">Passage 5 (Questions 25&ndash;30)</div>
<p>The ventricular action potential (AP) is characterized by a prolonged plateau (Phase 2) lasting 200&ndash;400 ms that prevents tetanic contraction and synchronizes cardiac pumping. The morphology of the ventricular AP reflects a temporal orchestration of depolarizing inward and repolarizing outward transmembrane currents across five distinct phases (Figure 1):</p>
<ul style="margin-left:20px;font-size:13px;line-height:1.6">
<li><b>Phase 0 (Rapid Depolarization):</b> Rapid inward Na<sup>+</sup> current (<i>I</i><sub>Na</sub>) through voltage-gated Na<sub>v</sub>1.5 channels upon reaching threshold (&minus;65 mV).</li>
<li><b>Phase 1 (Early Repolarization):</b> Transient outward K<sup>+</sup> current (<i>I</i><sub>to</sub>) coupled with rapid inactivation of Na<sub>v</sub>1.5.</li>
<li><b>Phase 2 (Plateau):</b> Balance between inward depolarizing Ca<sup>2+</sup> current (<i>I</i><sub>Ca-L</sub> via Ca<sub>v</sub>1.2 L-type channels) and delayed rectifier outward K<sup>+</sup> currents (<i>I</i><sub>Kr</sub> and <i>I</i><sub>Ks</sub>).</li>
<li><b>Phase 3 (Rapid Repolarization):</b> Inactivation of Ca<sub>v</sub>1.2 alongside vigorous outward K<sup>+</sup> efflux through <i>I</i><sub>Kr</sub> (encoded by <i>hERG</i> / <i>KCNH2</i>) and <i>I</i><sub>Ks</sub> (<i>KCNQ1</i>).</li>
<li><b>Phase 4 (Resting Potential):</b> Stable resting membrane potential (&minus;85 mV) maintained by inward rectifier K<sup>+</sup> channels (<i>I</i><sub>K1</sub>) and the Na<sup>+</sup>/K<sup>+</sup>-ATPase.</li>
</ul>
<p>Long QT Syndrome (LQTS) is a cardiac channelopathy characterized by delayed ventricular repolarization, predisposing patients to polymorphic ventricular tachycardia (<i>Torsades de Pointes</i>) and sudden cardiac death. Investigators recorded whole-cell patch-clamp currents and action potential durations (APD<sub>90</sub>) in human induced pluripotent stem cell-derived cardiomyocytes (hiPSC-CMs) carrying congenital mutations or exposed to pharmacological blockers.</p>
<table>
<tr><th>Condition</th><th>Genetic / Pharmacologic Alteration</th><th>Peak <i>I</i><sub>Na</sub> (pA/pF)</th><th>Late <i>I</i><sub>Na,L</sub> (% of peak)</th><th>Peak <i>I</i><sub>Kr</sub> (pA/pF)</th><th>APD<sub>90</sub> (ms)</th><th>Arrhythmic Events (EADs)</th></tr>
<tr><td>Control</td><td>Wild-Type (WT)</td><td class="n">&minus;220</td><td class="n">0.2</td><td class="n">4.2</td><td class="n">340</td><td>None</td></tr>
<tr><td>LQT1 (Congenital)</td><td><i>KCNQ1</i> loss-of-function</td><td class="n">&minus;218</td><td class="n">0.2</td><td class="n">4.1</td><td class="n">480</td><td>Occasional</td></tr>
<tr><td>LQT2 (Congenital)</td><td><i>KCNH2</i> (<i>hERG</i>) dominant negative</td><td class="n">&minus;222</td><td class="n">0.2</td><td class="n">0.8</td><td class="n">590</td><td>Frequent</td></tr>
<tr><td>LQT3 (Congenital)</td><td><i>SCN5A</i> (Na<sub>v</sub>1.5) gain-of-function</td><td class="n">&minus;215</td><td class="n">2.8</td><td class="n">4.2</td><td class="n">560</td><td>Frequent</td></tr>
<tr><td>Drug-Induced LQTS</td><td>Dofetilide (100 nM, hERG blocker)</td><td class="n">&minus;219</td><td class="n">0.2</td><td class="n">0.4</td><td class="n">620</td><td>Frequent</td></tr>
<tr><td>Therapeutic Rescue</td><td>LQT3 + Mexiletine (Na<sub>v</sub> blocker)</td><td class="n">&minus;210</td><td class="n">0.3</td><td class="n">4.1</td><td class="n">355</td><td>Abolished</td></tr>
</table>
<p class="cap"><b>Table 1</b> Electrophysiological parameters and early afterdepolarizations (EADs) in hiPSC-CMs.</p>"""

p5_qs = [
    {
        "q": "Based on Table 1, LQT2 (caused by KCNH2/hERG mutation) and LQT3 (caused by SCN5A mutation) prolong action potential duration (APD_90) through which respective biophysical mechanisms?",
        "ch": [
            "LQT2 decreases repolarizing outward K⁺ current (I_Kr), whereas LQT3 increases sustained depolarizing inward Na⁺ current (late I_Na,L).",
            "LQT2 completely blocks the sodium-potassium pump, whereas LQT3 accelerates calcium extrusion.",
            "LQT2 accelerates Phase 0 depolarization, whereas LQT3 blocks Phase 1 repolarization.",
            "Both mutations selectively destroy the resting potassium conductance (I_K1)."
        ],
        "a": 0,
        "e": "<strong>Mechanisms of delayed repolarization:</strong> Table 1 shows that LQT2 severely impairs peak I<sub>Kr</sub> (collapsing from 4.2 to 0.8 pA/pF), reducing the outward positive current needed to repolarize the cell. LQT3 (gain-of-function in Na<sub>v</sub>1.5) exhibits normal peak I<sub>Na</sub> but a 14-fold surge in late, sustained Na⁺ current (I<sub>Na,L</sub>: 0.2% &rarr; 2.8%), maintaining inward depolarizing current during Phase 2. Both disrupt the balance between inward and outward currents, prolonging APD<sub>90</sub>."
    },
    {
        "q": "Early afterdepolarizations (EADs) that trigger Torsades de Pointes during prolonged Phase 2/3 plateaus are caused primarily by:",
        "ch": [
            "re-activation of L-type Ca²⁺ channels (Cav1.2) before complete repolarization has occurred.",
            "sudden opening of nuclear pore complexes.",
            "spontaneous ATP depletion in the mitochondrial matrix.",
            "rapid efflux of magnesium ions across the sarcolemma."
        ],
        "a": 0,
        "e": "<strong>Electrophysiological basis of EADs:</strong> When Phase 2/3 repolarization is pathologically delayed, the membrane potential lingers within the window voltage (&minus;30 to &minus;10 mV) where L-type Ca²⁺ channels (Ca<sub>v</sub>1.2) can recover from inactivation and reopen. This secondary inward Ca²⁺ influx produces an oscillatory depolarizing spike (an EAD) that can trigger ventricular arrhythmias."
    },
    {
        "q": "Why does mexiletine (Row 6) successfully rescue the electrophysiological phenotype in LQT3 cells, shortening APD_90 from 560 ms to 355 ms and abolishing arrhythmic events?",
        "ch": [
            "Mexiletine activates the hERG potassium channel to boost I_Kr tenfold.",
            "Mexiletine selectively inhibits the pathological late persistent sodium current (I_Na,L) without abolishing the peak I_Na required for Phase 0 upstroke.",
            "Mexiletine is an uncoupler of oxidative phosphorylation.",
            "Mexiletine acts as an agonist at &beta;₁-adrenergic receptors."
        ],
        "a": 1,
        "e": "<strong>Targeted rescue of late sodium current:</strong> Mexiletine is a Class Ib antiarrhythmic that preferentially binds to inactivated/open Na<sub>v</sub>1.5 channels during the plateau phase, selectively blocking the persistent late I<sub>Na,L</sub> (dropping it from 2.8% back to 0.3%) without impairing the rapid peak I<sub>Na</sub> required for Phase 0 upstroke (&minus;210 pA/pF)."
    },
    {
        "q": "During Phase 4, the resting membrane potential of ventricular myocytes (&minus;85 mV) sits very close to the equilibrium potential of potassium (E_K &asymp; &minus;90 mV). This is primarily because:",
        "ch": [
            "resting membrane permeability to potassium via I_K1 channels is far higher than permeability to sodium or calcium.",
            "the Na⁺/K⁺-ATPase pumps 3 K⁺ in for every 2 Na⁺ out.",
            "intracellular calcium concentration is zero.",
            "chloride ions are actively pumped out of the cell by secondary active transport."
        ],
        "a": 0,
        "e": "<strong>Goldman-Hodgkin-Katz equation:</strong> Membrane potential is governed by the relative permeabilities of permeant ions. At rest (Phase 4), voltage-gated Na⁺ and Ca²⁺ channels are closed, while inward rectifier K⁺ channels (I<sub>K1</sub>) are open. The massive resting K⁺ permeability (P<sub>K</sub> >> P<sub>Na</sub>, P<sub>Ca</sub>) pulls the membrane potential close to the Nernst potential of potassium (E<sub>K</sub> &asymp; &minus;90 mV)."
    },
    {
        "q": "In an electrocardiogram (ECG), the QT interval represents the time required for:",
        "ch": [
            "atrial depolarization only (the P wave).",
            "ventricular depolarization and repolarization (the entire ventricular electrical cycle).",
            "AV nodal conduction delay (the PR segment).",
            "sinoatrial node pacemaker firing."
        ],
        "a": 1,
        "e": "<strong>ECG intervals:</strong> The QRS complex represents ventricular depolarization, and the T wave represents ventricular repolarization. The QT interval (measured from the onset of the Q wave to the end of the T wave) represents the total duration of ventricular electrical systole (depolarization plus repolarization)."
    },
    {
        "q": "The absolute refractory period (ARP) of cardiac ventricular myocytes is exceptionally long (lasting nearly the entire duration of the plateau) because:",
        "ch": [
            "Nav1.5 sodium channels remain trapped in their inactivated state until the membrane repolarizes below approximately &minus;60 mV.",
            "action potentials cannot propagate through gap junctions.",
            "cardiac troponin C undergoes proteolytic cleavage during each contraction.",
            "extracellular potassium is completely depleted during Phase 2."
        ],
        "a": 0,
        "e": "<strong>Mechanism of the cardiac absolute refractory period:</strong> During Phase 0, Na<sub>v</sub>1.5 channels open and then rapidly transition into an inactivated (closed and non-activatable) state. They cannot be reopened by a second depolarizing stimulus until the membrane repolarizes to negative voltages (&minus;60 to &minus;70 mV) to allow recovery from inactivation. This long ARP prevents tetanic contraction, ensuring intermittent filling and pumping."
    }
]

# Passage 6: Mitochondrial Electron Transport Chain
p6_html = """<div class="ttl">Passage 6 (Questions 31&ndash;36)</div>
<p>In mammalian cells, oxidative phosphorylation accounts for >90% of ATP generation under aerobic conditions. High-energy electrons derived from catabolic substrates are shuttled via NADH and FADH<sub>2</sub> through four inner mitochondrial membrane complexes (Complexes I&ndash;IV). The energy released by exergonic electron transfer couples to the endergonic pumping of protons from the mitochondrial matrix into the intermembrane space (IMS):</p>
<ul style="margin-left:20px;font-size:13px;line-height:1.6">
<li><b>Complex I (NADH:ubiquinone oxidoreductase):</b> Transfers 2e<sup>&minus;</sup> from NADH to ubiquinone (Q), pumping 4 H<sup>+</sup>.</li>
<li><b>Complex II (Succinate dehydrogenase):</b> Transfers 2e<sup>&minus;</sup> from succinate to Q via FAD; pumps 0 H<sup>+</sup>.</li>
<li><b>Complex III (Ubiquinol:cytochrome c oxidoreductase):</b> Catalyzes the Q-cycle, transferring electrons to cytochrome c; pumps 4 H<sup>+</sup>.</li>
<li><b>Complex IV (Cytochrome c oxidase):</b> Transfers electrons to molecular O<sub>2</sub>, forming H<sub>2</sub>O; pumps 2 H<sup>+</sup>.</li>
</ul>
<p>The resulting electrochemical proton-motive force (&Delta;<i>p</i> = &Delta;&Psi;<sub>m</sub> &minus; 59&Delta;pH) drives proton translocation through the F<sub>0</sub> rotor of ATP synthase (Complex V), inducing rotational catalysis in the F<sub>1</sub> domain to synthesize ATP from ADP and P<sub>i</sub> (requiring ~4 H<sup>+</sup> per ATP synthesized and exported).</p>
<p>Biochemists incubated isolated rat liver mitochondria in respiration buffer supplemented with pyruvate/malate (Complex I substrates) or succinate (Complex II substrate, with rotenone present). Oxygen consumption rate (OCR) and ATP synthesis were monitored following sequential additions of inhibitors and uncouplers.</p>
<table>
<tr><th>Condition</th><th>Substrate</th><th>Additions</th><th>Oxygen Consumption Rate (nmol O<sub>2</sub>/mg/min)</th><th>ATP Synthesis Rate (nmol/mg/min)</th><th>Matrix pH</th></tr>
<tr><td>1 (State 4)</td><td>Pyruvate + Malate</td><td>Mitochondria alone</td><td class="n">14.0</td><td class="n">&lt;5.0</td><td class="n">7.95</td></tr>
<tr><td>2 (State 3)</td><td>Pyruvate + Malate</td><td>+ ADP (1 mM) + P<sub>i</sub></td><td class="n">98.0</td><td class="n">245.0</td><td class="n">7.65</td></tr>
<tr><td>3</td><td>Pyruvate + Malate</td><td>+ Rotenone (1 &mu;M)</td><td class="n">6.2</td><td class="n">&lt;5.0</td><td class="n">7.20</td></tr>
<tr><td>4</td><td>Pyruvate + Malate</td><td>Rotenone + Succinate (5 mM)</td><td class="n">112.0</td><td class="n">186.0</td><td class="n">7.70</td></tr>
<tr><td>5</td><td>Succinate</td><td>+ Antimycin A (1 &mu;M)</td><td class="n">5.0</td><td class="n">&lt;5.0</td><td class="n">7.20</td></tr>
<tr><td>6</td><td>Succinate</td><td>+ Oligomycin (2 &mu;M)</td><td class="n">12.5</td><td class="n">&lt;5.0</td><td class="n">8.10</td></tr>
<tr><td>7</td><td>Succinate</td><td>Oligomycin + 2,4-DNP (50 &mu;M)</td><td class="n">145.0</td><td class="n">&lt;5.0</td><td class="n">7.15</td></tr>
</table>
<p class="cap"><b>Table 1</b> Respiration rates, phosphorylation kinetics, and matrix pH in isolated mitochondria.</p>"""

p6_qs = [
    {
        "q": "Why does adding succinate restore oxygen consumption and ATP synthesis in rotenone-inhibited mitochondria (Condition 4 vs Condition 3)?",
        "ch": [
            "Succinate displaces rotenone from the Complex I NADH-binding pocket.",
            "Succinate delivers electrons directly to Complex II (succinate dehydrogenase), bypassing the block at Complex I to reduce ubiquinone (Q).",
            "Succinate acts as a chemical uncoupler that diffuses protons across the lipid bilayer.",
            "Succinate is directly oxidized by Complex IV to reduce oxygen."
        ],
        "a": 1,
        "e": "<strong>Complex II bypasses Complex I:</strong> Rotenone specifically blocks Complex I, preventing electron transfer from NADH to ubiquinone. Succinate is oxidized to fumarate by Complex II (succinate dehydrogenase), transferring electrons directly to FAD and then to ubiquinone (Q). Because Complex II donates electrons downstream of Complex I, adding succinate restores electron flow through Complexes III and IV, re-establishing proton pumping and ATP synthesis."
    },
    {
        "q": "In Condition 6, adding oligomycin (an ATP synthase inhibitor) suppresses oxygen consumption to 12.5 nmol O₂/min. However, subsequently adding 2,4-dinitrophenol (2,4-DNP, Condition 7) stimulates oxygen consumption to a maximal rate of 145.0 nmol O₂/min WITHOUT restoring ATP synthesis. This occurs because 2,4-DNP:",
        "ch": [
            "is a lipophilic weak acid that shuttles protons across the inner mitochondrial membrane, dissipating the proton gradient and uncoupling electron transport from phosphorylation.",
            "directly hydrolyzes ATP in the matrix, releasing heat.",
            "covalently binds to cytochrome c oxidase, increasing its V_max tenfold.",
            "acts as an allosteric activator of the F₁ subunit of ATP synthase."
        ],
        "a": 0,
        "e": "<strong>Mechanism of uncouplers (2,4-DNP):</strong> Oligomycin blocks the F₀ proton channel of ATP synthase, causing the proton gradient to back up until the immense electrochemical potential prevents further proton pumping by ETC complexes (respiratory control). 2,4-DNP is a lipophilic proton ionophore (uncoupler) that diffuses across the inner membrane carrying protons into the matrix. This collapses &Delta;p, releasing ETC complexes from back-pressure and allowing maximal electron flow and O₂ consumption, with the energy dissipated entirely as heat instead of ATP."
    },
    {
        "q": "Based on the proton stoichiometry in the passage, how many total protons are pumped into the intermembrane space per pair of electrons originating from NADH versus FADH₂?",
        "ch": [
            "NADH: 10 H⁺; FADH₂: 6 H⁺",
            "NADH: 4 H⁺; FADH₂: 4 H⁺",
            "NADH: 12 H⁺; FADH₂: 8 H⁺",
            "NADH: 6 H⁺; FADH₂: 10 H⁺"
        ],
        "a": 0,
        "e": "<strong>ETC proton pumping stoichiometry:</strong><br>Electrons from NADH pass through Complex I (4 H⁺) &rarr; Complex III (4 H⁺) &rarr; Complex IV (2 H⁺), totaling 10 H⁺ pumped per 2e⁻.<br>Electrons from FADH₂ enter Complex II (0 H⁺ pumped) &rarr; Complex III (4 H⁺) &rarr; Complex IV (2 H⁺), totaling 6 H⁺ pumped per 2e⁻.<br>This 10:6 (5:3) ratio explains why NADH yields ~2.5 ATP while FADH₂ yields ~1.5 ATP."
    },
    {
        "q": "Cyanide (CN⁻) and carbon monoxide (CO) act as potent cellular poisons by binding with high affinity to which electron transport component?",
        "ch": [
            "The iron-sulfur clusters of Complex I",
            "The heme a₃-Cu_B binuclear center of Complex IV (cytochrome c oxidase), blocking electron transfer to O₂",
            "The flavin mononucleotide (FMN) group of Complex I",
            "The c-ring rotor of ATP synthase"
        ],
        "a": 1,
        "e": "<strong>Complex IV inhibition:</strong> Cyanide and carbon monoxide bind to the reduced or oxidized iron of heme a₃ and Cu<sub>B</sub> in the active site of Complex IV (cytochrome c oxidase). This completely blocks the reduction of molecular oxygen to water, halting the entire electron transport chain upstream."
    },
    {
        "q": "During active State 3 respiration (Condition 2), why does the mitochondrial matrix pH drop from 7.95 to 7.65 compared to State 4 resting conditions (Condition 1)?",
        "ch": [
            "Protons rapidly re-enter the mitochondrial matrix through ATP synthase to drive ATP synthesis.",
            "Lactate accumulates within the matrix.",
            "Water molecules are hydrolyzed into hydrogen peroxide.",
            "Complex I reverses direction, pumping protons into the matrix."
        ],
        "a": 0,
        "e": "<strong>Proton flux during ATP synthesis:</strong> In State 4 (resting), protons cannot re-enter the matrix because ADP is absent, so the matrix remains highly alkaline (pH 7.95) as ETC complexes pump protons out. When ADP and P<sub>i</sub> are added (State 3), protons flow down their electrochemical gradient through the F₀ pore of ATP synthase into the matrix to drive ATP synthesis, bringing H⁺ back in and lowering matrix pH to 7.65."
    },
    {
        "q": "Brown adipose tissue (BAT) produces non-shivering thermogenesis in neonates using uncoupling protein 1 (UCP1 / thermogenin). The physiological mechanism of UCP1 is identical to the pharmacological action of:",
        "ch": [
            "rotenone.",
            "antimycin A.",
            "2,4-dinitrophenol (2,4-DNP).",
            "oligomycin."
        ],
        "a": 2,
        "e": "<strong>Thermogenin (UCP1) is a physiological uncoupler:</strong> UCP1 provides a regulated proton leak pathway across the inner mitochondrial membrane, allowing protons to bypass ATP synthase. Like 2,4-DNP, UCP1 dissipates the proton-motive force, uncoupling substrate oxidation from ATP phosphorylation so that the energy of the electrochemical gradient is released directly as metabolic heat."
    }
]

# Passage 7: B-cell Receptor V(D)J Recombination & Somatic Hypermutation
p7_html = """<div class="ttl">Passage 7 (Questions 37&ndash;42)</div>
<p>The human adaptive immune system generates over 10<sup>11</sup> distinct antibody specificities from a finite genome via somatic genetic diversification mechanisms: V(D)J recombination, junctional diversity, somatic hypermutation (SHM), and class-switch recombination (CSR).</p>
<p>During early B-cell ontogeny in the bone marrow, recombination-activating genes 1 and 2 (<i>RAG1</i> and <i>RAG2</i>) recognize recombination signal sequences (RSSs) flanking variable (V), diversity (D), and joining (J) gene segments. RAG1/2 introduces DNA double-strand breaks, forming hairpin intermediates on coding ends that are opened and joined by non-homologous end joining (NHEJ) enzymes, including Artemis and DNA ligase IV. Terminal deoxynucleotidyl transferase (TdT) adds non-templated (N) nucleotides at coding junctions, creating extensive junctional diversity within the complementarity-determining region 3 (CDR3).</p>
<p>Upon antigen encounter in secondary lymphoid germinal centers, activated B cells express activation-induced cytidine deaminase (AID), an enzyme that deaminates cytosine (C) to uracil (U) within single-stranded immunoglobulin DNA, triggering SHM (affinity maturation) and CSR (isotype switching from IgM to IgG, IgA, or IgE). Investigators analyzed peripheral blood lymphocytes from four pediatric patients presenting with severe recurrent bacterial and opportunistic infections.</p>
<table>
<tr><th>Patient</th><th>Serum IgM (mg/dL)</th><th>Serum IgG (mg/dL)</th><th>Serum IgA (mg/dL)</th><th>Circulating Mature B Cells (CD19<sup>+</sup>)</th><th>Germinal Centers in Lymph Nodes</th><th>Identified Genetic Mutation</th></tr>
<tr><td>Reference Normal</td><td class="n">40&ndash;230</td><td class="n">700&ndash;1600</td><td class="n">70&ndash;400</td><td class="n">10&ndash;20%</td><td>Present</td><td>None</td></tr>
<tr><td>Patient 1</td><td class="n">&lt;5</td><td class="n">&lt;10</td><td class="n">&lt;5</td><td class="n">&lt;0.1%</td><td>Absent</td><td><i>RAG1</i> null (frameshift)</td></tr>
<tr><td>Patient 2</td><td class="n">380</td><td class="n">&lt;10</td><td class="n">&lt;5</td><td class="n">14%</td><td>Absent / Disorganized</td><td><i>AICDA</i> (AID) catalytic dead</td></tr>
<tr><td>Patient 3</td><td class="n">&lt;5</td><td class="n">&lt;10</td><td class="n">&lt;5</td><td class="n">&lt;0.1%</td><td>Absent</td><td><i>BTK</i> (Bruton tyrosine kinase) null</td></tr>
<tr><td>Patient 4</td><td class="n">450</td><td class="n">&lt;10</td><td class="n">&lt;5</td><td class="n">12%</td><td>Present</td><td><i>CD40L</i> (CD154) nonsense</td></tr>
</table>
<p class="cap"><b>Table 1</b> Immunological phenotypes and sequencing findings in pediatric immunodeficiency patients.</p>"""

p7_qs = [
    {
        "q": "Why does Patient 1 (RAG1 null mutation) present with a near-total absence of mature circulating B cells (<0.1%) and pan-hypogammaglobulinemia?",
        "ch": [
            "RAG1 is essential for cleaving DNA hairpins during somatic hypermutation in germinal centers.",
            "RAG1 endonuclease activity is required to initiate V(D)J recombination; without it, developing pro-B cells cannot assemble functional immunoglobulin heavy- or light-chain genes and undergo apoptosis in the bone marrow.",
            "RAG1 is a transcription factor that upregulates CD19 and CD20 expression on mature B cells.",
            "RAG1 catalyzes class-switch recombination from IgM to IgG."
        ],
        "a": 1,
        "e": "<strong>RAG1/2 is required for V(D)J recombination:</strong> RAG1 and RAG2 endonucleases recognize RSSs to initiate gene rearrangement at immunoglobulin and T-cell receptor loci. Without RAG1, pro-B cells cannot assemble a functional heavy chain (pre-BCR) and arrest development at the pro-B to pre-B transition in the bone marrow, undergoing apoptosis. This leads to severe combined immunodeficiency (SCID) lacking both mature B and T lymphocytes."
    },
    {
        "q": "Patient 2 carries a catalytic mutation in activation-induced cytidine deaminase (AID), resulting in Hyper-IgM Syndrome Type 2. What biochemical reaction does AID normally catalyze on DNA?",
        "ch": [
            "Hydrolysis of the phosphodiester backbone between adjacent guanine residues",
            "Hydrolytic deamination of cytosine to uracil (C &rarr; U) in single-stranded DNA during transcription",
            "Methylation of adenine residues to form N⁶-methyladenine",
            "Addition of poly-A tails to the 3' end of heavy-chain pre-mRNAs"
        ],
        "a": 1,
        "e": "<strong>Mechanism of AID:</strong> Activation-induced cytidine deaminase (AID) attacks the amino group of cytosine within transcribed single-stranded DNA, converting cytosine into uracil (C &rarr; U). The resulting U:G mismatches are recognized by base excision repair (uracil-DNA glycosylase, UNG) and mismatch repair enzymes, creating DNA breaks that initiate somatic hypermutation in variable regions and class-switch recombination at switch regions."
    },
    {
        "q": "Why does Patient 2 exhibit elevated serum IgM (380 mg/dL) alongside virtually undetectable IgG (<10 mg/dL) and IgA (<5 mg/dL)?",
        "ch": [
            "IgM does not require V(D)J recombination, whereas IgG and IgA do.",
            "The primary transcript of the rearranged heavy chain natively encodes the C&mu; constant region; class switching to C&gamma; (IgG) or C&alpha; (IgA) requires AID-mediated double-strand breaks at switch regions.",
            "AID specifically degrades circulating IgG and IgA antibodies in the bloodstream.",
            "IgM is produced exclusively by T lymphocytes in the thymus."
        ],
        "a": 1,
        "e": "<strong>Class-switch recombination is AID-dependent:</strong> In naive mature B cells, the assembled VDJ segment is positioned immediately adjacent to the C&mu; (IgM) and C&delta; (IgD) constant region exons, which are expressed via alternative splicing. Switching to downstream constant regions (C&gamma; for IgG, C&alpha; for IgA, C&epsilon; for IgE) requires AID to generate double-strand DNA breaks in switch regions. Without functional AID, B cells cannot undergo CSR, producing exclusively high levels of unswitched IgM."
    },
    {
        "q": "Patient 4 has an X-linked Hyper-IgM Syndrome caused by a mutation in CD40L (CD154), a surface ligand expressed on activated T helper cells. How does CD40L deficiency prevent B-cell isotype switching?",
        "ch": [
            "CD40L is the catalytic subunit of RNA polymerase II in B cells.",
            "Engagement of CD40 on B cells by CD40L on follicular helper T cells provides the essential co-stimulatory signal required to induce AID expression and germinal center formation.",
            "CD40L directly binds and neutralizes secreted IgM.",
            "CD40L functions as a toll-like receptor that detects bacterial lipopolysaccharide."
        ],
        "a": 1,
        "e": "<strong>T-dependent B-cell activation:</strong> Isotype switching and somatic hypermutation in germinal centers require T-cell help. Activated CD4⁺ follicular helper T cells express CD40L, which binds CD40 on antigen-activated B cells. This contact-dependent co-stimulatory signal activates NF-&kappa;B transcription factors to induce AID expression. In the absence of CD40L, B cells cannot receive T-cell help, blocking CSR."
    },
    {
        "q": "Which molecular mechanism is primarily responsible for introducing non-templated junctional diversity at the V-D and D-J junctions during heavy-chain rearrangement?",
        "ch": [
            "Random nucleotide insertion by Terminal deoxynucleotidyl Transferase (TdT)",
            "Alternative splicing of mature heavy-chain mRNA",
            "Proofreading 3'&rarr;5' exonuclease activity of DNA polymerase &delta;",
            "Histone acetylation by p300/CBP"
        ],
        "a": 0,
        "e": "<strong>Terminal deoxynucleotidyl Transferase (TdT):</strong> During V(D)J recombination, after RAG1/2 and Artemis open the DNA hairpins, TdT randomly adds non-templated (N) nucleotides to the free 3' overhangs before end ligation by DNA ligase IV. This introduces extensive sequence diversity directly into CDR3, the antigen-binding loop that contacts antigen most intimately."
    },
    {
        "q": "Patient 3 has X-linked agammaglobulinemia (XLA) due to a mutation in Bruton tyrosine kinase (BTK). What is the normal function of BTK during B-cell development?",
        "ch": [
            "It phosphorylates RAG1 to initiate heavy chain rearrangement.",
            "It transduces essential survival and proliferation signals downstream of the pre-B cell receptor (pre-BCR), allowing pre-B cells to survive and proliferate.",
            "It catalyzes somatic hypermutation in secondary lymphoid organs.",
            "It functions as an Fc receptor for IgE on mast cells."
        ],
        "a": 1,
        "e": "<strong>Bruton tyrosine kinase (BTK) signaling:</strong> Once a developing pro-B cell successfully rearranges a &mu; heavy chain, it pairs with a surrogate light chain to form the pre-BCR complex. Pre-BCR signaling activates the cytoplasmic tyrosine kinase BTK, driving proliferation and progression to the pre-B cell stage. In XLA, BTK deficiency arrests B-cell development at the pre-B stage, leading to a complete absence of circulating mature B cells and antibodies."
    }
]

# 10 Discrete Questions for B/B
bb_discretes = [
    {
        "q": "What is the approximate isoelectric point (pI) of the tripeptide Glu-His-Ala? (Relevant pKa values: N-terminus = 9.0; C-terminus = 2.0; Glu side chain = 4.0; His side chain = 6.0).",
        "d": True,
        "ch": [
            "3.0",
            "5.0",
            "6.0",
            "7.5"
        ],
        "a": 1,
        "e": "<strong>Calculate pI for a peptide with ionizable side chains:</strong><br>At pH < 2.0: net charge = +2 (N-term +1, His +1, Glu 0, C-term 0).<br>At pH 2.0–4.0: C-terminus deprotonates (&minus;1), net charge = +1.<br>At pH 4.0–6.0: Glu side chain deprotonates (&minus;1), net charge = 0 (zwitterion).<br>At pH 6.0–9.0: His side chain deprotonates (0), net charge = &minus;1.<br>At pH > 9.0: N-terminus deprotonates (0), net charge = &minus;2.<br>The neutral species exists between pKa 4.0 (Glu) and pKa 6.0 (His).<br>pI = (4.0 + 6.0) / 2 = 5.0."
    },
    {
        "q": "A homotetrameric protein with a native molecular weight of 200 kDa consists of four identical 50 kDa subunits linked by interchain disulfide bonds. When analyzed by SDS-PAGE in the PRESENCE versus ABSENCE of &beta;-mercaptoethanol (&beta;-ME), what bands will be observed?",
        "d": True,
        "ch": [
            "With &beta;-ME: a single 50 kDa band; Without &beta;-ME: a single 200 kDa band",
            "With &beta;-ME: a single 200 kDa band; Without &beta;-ME: a single 50 kDa band",
            "With &beta;-ME: four distinct bands at 50, 100, 150, and 200 kDa; Without &beta;-ME: no bands",
            "With &beta;-ME: a 50 kDa band; Without &beta;-ME: two bands at 100 kDa"
        ],
        "a": 0,
        "e": "<strong>Reducing vs non-reducing SDS-PAGE:</strong> &beta;-mercaptoethanol is a reducing agent that cleaves covalent disulfide bonds (&minus;S&minus;S&minus; &rarr; 2 &minus;SH). In the presence of &beta;-ME, all interchain disulfide bridges are reduced, releasing individual 50 kDa monomer subunits (a single 50 kDa band). In the absence of &beta;-ME, disulfide bridges remain intact, so the entire 200 kDa tetramer migrates as a single 200 kDa band."
    },
    {
        "q": "In a human population in Hardy-Weinberg equilibrium, an autosomal recessive metabolic disorder affects 1 in 10,000 live births (q² = 0.0001). What fraction of the population are asymptomatic heterozygous carriers (2pq) of the disease allele?",
        "d": True,
        "ch": [
            "0.0002 (1 in 5,000)",
            "0.0198 (approximately 2% or 1 in 50)",
            "0.0400 (4%)",
            "0.0001 (1 in 10,000)"
        ],
        "a": 1,
        "e": "<strong>Hardy-Weinberg equilibrium:</strong> q² = 0.0001 &rArr; q = &radic;0.0001 = 0.01.<br>p = 1 &minus; q = 1 &minus; 0.01 = 0.99.<br>Heterozygous carrier frequency = 2pq = 2 &times; (0.99) &times; (0.01) = 0.0198 &asymp; 1.98% (~1 in 50 individuals)."
    },
    {
        "q": "Which tissue pair is correctly matched to its embryonic germ layer of origin?",
        "d": True,
        "ch": [
            "Adrenal medulla &ndash; Ectoderm (neural crest); Adrenal cortex &ndash; Mesoderm",
            "Adrenal medulla &ndash; Endoderm; Adrenal cortex &ndash; Ectoderm",
            "Thyroid follicular cells &ndash; Mesoderm; Adrenal medulla &ndash; Endoderm",
            "Pancreatic islets &ndash; Ectoderm; Spleen &ndash; Endoderm"
        ],
        "a": 0,
        "e": "<strong>Embryonic germ layer origins of the adrenal gland:</strong> The adrenal medulla arises from neural crest cells (ectoderm) and functions essentially as a specialized sympathetic ganglion secreting catecholamines. The adrenal cortex arises from intermediate mesoderm and secretes steroid hormones (aldosterone, cortisol, androgens)."
    },
    {
        "q": "A woman diagnosed with mitochondrial encephalomyopathy (MERRF syndrome, caused by a mutation in mitochondrial tRNA_Lys) marries an unaffected man. If they have four children (two sons and two daughters), what is the expected inheritance pattern among their offspring?",
        "ch": [
            "All four children will inherit the mitochondrial mutation and be affected.",
            "Only the two daughters will inherit the mutation, while the sons will be unaffected.",
            "Only the two sons will inherit the mutation via Y-linked inheritance.",
            "50% of the offspring will be affected following Mendelian autosomal dominant inheritance."
        ],
        "a": 0,
        "e": "<strong>Maternal inheritance of mitochondrial DNA:</strong> In humans, mitochondria are inherited exclusively from the maternal oocyte; sperm mitochondria are tagged with ubiquitin and degraded upon fertilization. Therefore, an affected mother transmits the mitochondrial mutation to 100% of her biological children, regardless of offspring sex. Affected males cannot transmit the disease to their children."
    },
    {
        "q": "Which statement correctly contrasts the cellular mechanism of action of peptide hormones (e.g., insulin, glucagon) with that of steroid hormones (e.g., cortisol, estrogen)?",
        "ch": [
            "Peptide hormones are lipophilic and bind nuclear receptors, whereas steroid hormones bind cell-surface G-protein coupled receptors.",
            "Peptide hormones bind cell-surface transmembrane receptors and act via second messenger cascades on a rapid timescale (seconds to minutes), whereas steroid hormones cross the lipid bilayer to bind intracellular/nuclear receptors that alter gene transcription on a slower timescale (hours to days).",
            "Steroid hormones circulate freely dissolved in plasma, whereas peptide hormones require plasma carrier proteins.",
            "Peptide hormones are synthesized from cholesterol, whereas steroid hormones are translated from mRNA."
        ],
        "a": 1,
        "e": "<strong>Peptide vs. steroid hormone signaling:</strong> Peptide hormones are polar and hydrophilic; they cannot cross the lipid bilayer, so they bind cell-surface receptors (GPCRs, RTKs) to trigger rapid kinase cascades. Steroid hormones are lipophilic derivatives of cholesterol; they circulate bound to plasma carrier proteins, passively diffuse across cell membranes, and bind nuclear receptors that act as transcription factors, producing slower but long-lasting effects on gene expression."
    },
    {
        "q": "Hemoglobin exhibits an oxygen-binding Hill coefficient (n_H) of approximately 2.8 to 3.0, whereas myoglobin has n_H = 1.0. This indicates that:",
        "ch": [
            "hemoglobin displays positive cooperativity (binding of O₂ at one subunit increases the affinity of remaining subunits), whereas myoglobin binds O₂ non-cooperatively.",
            "hemoglobin has a higher affinity for oxygen at all partial pressures than myoglobin.",
            "myoglobin contains four heme groups that bind oxygen simultaneously.",
            "hemoglobin displays negative cooperativity that inhibits oxygen loading in the lungs."
        ],
        "a": 0,
        "e": "<strong>Hill coefficient and cooperativity:</strong> A Hill coefficient n<sub>H</sub> > 1 indicates positive cooperativity, producing a sigmoidal oxygen binding curve (as in tetrameric hemoglobin, n<sub>H</sub> &asymp; 2.8). A Hill coefficient n<sub>H</sub> = 1.0 indicates completely independent, non-cooperative binding, yielding a hyperbolic binding curve (as in monomeric myoglobin)."
    },
    {
        "q": "A clinical pharmacologist measures the renal clearance of three compounds: Inulin (125 mL/min), Glucose (0 mL/min), and Para-aminohippurate (PAH, 650 mL/min). Based on these values, PAH is handled by the nephron via:",
        "ch": [
            "filtration alone with neither reabsorption nor secretion.",
            "filtration followed by complete tubular reabsorption.",
            "filtration plus extensive active tubular secretion, making its clearance equal to effective renal plasma flow (ERPF).",
            "exclusive reabsorption in the loop of Henle."
        ],
        "a": 2,
        "e": "<strong>Renal clearance principles:</strong> Inulin is freely filtered and neither reabsorbed nor secreted, so its clearance equals GFR (125 mL/min). Glucose is filtered and completely reabsorbed, yielding clearance = 0. PAH is freely filtered and so aggressively secreted by proximal tubule organic anion transporters that virtually all PAH entering the renal artery is cleared in a single pass, making PAH clearance equal to effective renal plasma flow (~650 mL/min)."
    },
    {
        "q": "On a Lineweaver-Burk double-reciprocal plot (1/v vs 1/[S]), an uncompetitive inhibitor will produce a line that:",
        "ch": [
            "intersects the uninhibited line directly on the y-axis (same 1/V_max).",
            "intersects the uninhibited line directly on the negative x-axis (same &minus;1/K_m).",
            "is parallel to the uninhibited line, with identical slope (K_m / V_max) and higher intercepts on both axes.",
            "crosses the uninhibited line in the fourth quadrant."
        ],
        "a": 2,
        "e": "<strong>Uncompetitive inhibition Lineweaver-Burk plot:</strong> Uncompetitive inhibitors bind exclusively to the enzyme-substrate (ES) complex. This reduces both V<sub>max</sub> and apparent K<sub>m</sub> by the exact same factor &alpha;'. Because both parameters decrease proportionally, the slope K<sub>m</sub>/V<sub>max</sub> is unchanged, producing parallel lines that never intersect."
    },
    {
        "q": "Which structural feature is essential for initiating cap-dependent translation of eukaryotic mRNAs, but is ABSENT in prokaryotic mRNAs?",
        "ch": [
            "A 5' 7-methylguanosine (m⁷G) triphosphate cap recognized by the eIF4E initiation complex",
            "A purine-rich Shine-Dalgarno sequence upstream of the start codon",
            "Polycistronic operon organization encoding multiple open reading frames",
            "Formylmethionine (fMet) as the first amino acid incorporated by initiator tRNA"
        ],
        "a": 0,
        "e": "<strong>Eukaryotic vs. prokaryotic translation initiation:</strong> Eukaryotic mRNAs are monocistronic and contain a 5' 7-methylguanosine (m⁷G) cap that is recognized by eukaryotic initiation factor 4E (eIF4E) to recruit the 40S ribosomal subunit. Prokaryotic mRNAs lack a 5' cap and instead utilize a conserved Shine-Dalgarno sequence (5'-AGGAGG-3') that base-pairs with 16S rRNA in the 30S subunit, and use formylmethionine (fMet) rather than standard methionine."
    }
]

all_bb_sets = [
    {
        "id": "exam_bb90_p1",
        "sec": "B/B",
        "topic": "CRISPR-Cas9 genome editing and DNA repair pathways",
        "sheet": 45,
        "label": "Biological and Biochemical Foundations of Living Systems",
        "examId": "bb90",
        "passage": p1_html,
        "qs": p1_qs
    },
    {
        "id": "exam_bb90_p2",
        "sec": "B/B",
        "topic": "Pyruvate dehydrogenase regulation and metabolic control",
        "sheet": 51,
        "label": "Biological and Biochemical Foundations of Living Systems",
        "examId": "bb90",
        "passage": p2_html,
        "qs": p2_qs
    },
    {
        "id": "exam_bb90_p3",
        "sec": "B/B",
        "topic": "SGLT2 glucose transport kinetics and diabetic nephropathy",
        "sheet": 37,
        "label": "Biological and Biochemical Foundations of Living Systems",
        "examId": "bb90",
        "passage": p3_html,
        "qs": p3_qs
    },
    {
        "id": "exam_bb90_p4",
        "sec": "B/B",
        "topic": "GPCR and beta-arrestin biased signaling in smooth muscle",
        "sheet": 32,
        "label": "Biological and Biochemical Foundations of Living Systems",
        "examId": "bb90",
        "passage": p4_html,
        "qs": p4_qs
    },
    {
        "id": "exam_bb90_p5",
        "sec": "B/B",
        "topic": "Cardiac ventricular action potential and Long QT syndrome",
        "sheet": 34,
        "label": "Biological and Biochemical Foundations of Living Systems",
        "examId": "bb90",
        "passage": p5_html,
        "qs": p5_qs
    },
    {
        "id": "exam_bb90_p6",
        "sec": "B/B",
        "topic": "Mitochondrial electron transport and oxidative phosphorylation",
        "sheet": 50,
        "label": "Biological and Biochemical Foundations of Living Systems",
        "examId": "bb90",
        "passage": p6_html,
        "qs": p6_qs
    },
    {
        "id": "exam_bb90_p7",
        "sec": "B/B",
        "topic": "V(D)J recombination, somatic hypermutation, and immunodeficiency",
        "sheet": 35,
        "label": "Biological and Biochemical Foundations of Living Systems",
        "examId": "bb90",
        "passage": p7_html,
        "qs": p7_qs
    },
    {
        "id": "exam_bb90_discretes",
        "sec": "B/B",
        "topic": "B/B Standalone Discrete Questions",
        "sheet": None,
        "label": "Biological and Biochemical Foundations of Living Systems",
        "examId": "bb90",
        "passage": "",
        "qs": bb_discretes
    }
]

total_qs = sum(len(s["qs"]) for s in all_bb_sets)
print(f"Total B/B questions: {total_qs}")

js_content = "/* ---- exam_bb90.js ---- */\n/* Full 90-minute Bio/Biochem practice section: 7 passages (42 Qs) + 10 discrete Qs = 52 Qs */\nconst EXAM_BB90 = " + json.dumps(all_bb_sets, indent=2) + ";\n"
with open("/home/cgslinde/DrillRoom/DrillRoom/exam_bb90.js", "w") as f:
    f.write(js_content)

print("exam_bb90.js written successfully!")
