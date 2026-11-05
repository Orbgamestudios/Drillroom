import json

passages = []

# ==============================================================================
# PASSAGE 1: Pentose Phosphate Pathway, G6PDH & Glutathione Redox Homeostasis
# Topics: G6PDH regulation, NADPH generation, glutathione reduction, oxidative hemolysis
# ==============================================================================
p1_html = r"""<div class="ttl">Passage 1 (Questions 1&ndash;6)</div>
<p>The pentose phosphate pathway (PPP, or hexose monophosphate shunt) branches from glycolysis at glucose-6-phosphate (G6P) to satisfy two vital cellular requirements: the generation of reducing equivalents in the form of nicotinamide adenine dinucleotide phosphate (NADPH) and the synthesis of ribose-5-phosphate for nucleotide biosynthesis. The pathway comprises an irreversible oxidative phase and a reversible non-oxidative phase.</p>
<p>In the first committed step of the oxidative phase, glucose-6-phosphate dehydrogenase (G6PDH) catalyzes the oxidation of G6P to 6-phosphoglucono-$\delta$-lactone with concomitant reduction of $\text{NADP}^+$ to NADPH:</p>
<p>$$\text{Glucose-6-Phosphate} + \text{NADP}^+ \xrightarrow{\text{G6PDH}} \text{6-Phosphoglucono-}\delta\text{-lactone} + \text{NADPH} + \text{H}^+$$</p>
<p>G6PDH is allosterically regulated by the intracellular $[\text{NADPH}]/[\text{NADP}^+]$ ratio, with NADPH serving as a potent competitive feedback inhibitor. In mature erythrocytes, which lack mitochondria, nuclei, and ribosomes, the PPP constitutes the sole metabolic source of NADPH. Erythrocytes depend on NADPH to maintain the tripeptide glutathione ($\gamma$-glutamylcysteinylglycine, GSH) in its active reduced monomeric state. Glutathione reductase uses NADPH to reduce oxidized glutathione disulfide (GSSG) back to two molecules of GSH. Reduced GSH is subsequently utilized by glutathione peroxidase to detoxify endogenous reactive oxygen species (ROS), converting hydrogen peroxide ($\text{H}_2\text{O}_2$) and lipid hydroperoxides into inert water and lipid alcohols, thereby protecting erythrocyte membrane phospholipids and hemoglobin tetramers from oxidative cross-linking (Heinz body formation) and extravascular hemolytic anemia.</p>
<p>Researchers characterized red blood cells from wild-type volunteers and patients carrying the Mediterranean variant of G6PDH ($G6PD^{\text{Med}}$, Ser188Phe) before and after in vitro exposure to 50 $\mu\text{M}$ primaquine (an antimalarial agent that induces intracellular ROS generation). Intracellular metabolite concentrations and enzymatic velocities are shown in Table 1.</p>
<table class="tbl">
  <caption>Table 1 Erythrocyte redox parameters and enzymatic velocities before and after primaquine challenge</caption>
  <thead>
    <tr><th>Erythrocyte Source</th><th>Primaquine (50 &mu;M)</th><th>G6PDH Velocity ($\mu\text{mol}/(\text{min}\cdot\text{g Hb})$)</th><th>$[\text{NADPH}]/[\text{NADP}^+]$ Ratio</th><th>Reduced GSH ($\mu\text{mol/g Hb}$)</th><th>% Hemolysis at 4 Hours</th></tr>
  </thead>
  <tbody>
    <tr><td>Wild-Type</td><td>&minus;</td><td>8.4</td><td>65 : 1</td><td>7.2</td><td>0.4%</td></tr>
    <tr><td>Wild-Type</td><td>+</td><td>19.8</td><td>42 : 1</td><td>6.8</td><td>1.1%</td></tr>
    <tr><td>$G6PD^{\text{Med}}$</td><td>&minus;</td><td>1.1</td><td>12 : 1</td><td>4.5</td><td>2.2%</td></tr>
    <tr><td>$G6PD^{\text{Med}}$</td><td>+</td><td>1.3</td><td>1.8 : 1</td><td>0.9</td><td>38.6%</td></tr>
  </tbody>
</table>
<p>In the non-oxidative branch, transketolase (a thiamine pyrophosphate-dependent enzyme) and transaldolase interconvert excess pentose phosphates into the glycolytic intermediates fructose-6-phosphate (F6P) and glyceraldehyde-3-phosphate (G3P).</p>"""

p1_qs = [
    {
        "q": "Why does exposure to primaquine stimulate G6PDH catalytic velocity by more than two-fold in wild-type erythrocytes (Table 1)?",
        "ch": [
            "Primaquine directly phosphorylates the active site of G6PDH to stabilize its tetrameric assembly.",
            "Accelerated ROS consumption of NADPH relieves allosteric competitive feedback inhibition by NADPH.",
            "Primaquine triggers the transcription and translation of new G6PDH enzyme copies.",
            "Oxidized glutathione acts as a suicide inhibitor that permanently alkylates transketolase."
        ],
        "a": 1,
        "e": "<strong>Feedback regulation of G6PDH:</strong> The passage notes that G6PDH is allosterically regulated by the $[\\text{NADPH}]/[\\text{NADP}^+]$ ratio, where NADPH acts as a potent competitive feedback inhibitor. When primaquine introduces oxidative stress, glutathione reductase rapidly consumes NADPH to regenerate GSH, depleting intracellular NADPH and elevating $[\\text{NADP}^+]$. The drop in $[\\text{NADPH}]$ relieves feedback inhibition while the rise in substrate $[\\text{NADP}^+]$ accelerates G6PDH flux, increasing enzymatic velocity from $8.4$ to $19.8\\;\\mu\\text{mol}/(\\text{min}\\cdot\\text{g Hb})$.<br><br><em>Distractor Traps:</em><br>&bull; A invents direct drug phosphorylation.<br>&bull; C is impossible in mature erythrocytes, which lack nuclei and ribosomes and cannot synthesize new proteins.<br>&bull; D describes transketolase inhibition, which does not explain G6PDH activation."
    },
    {
        "q": "What is the primary physiological consequence of impaired NADPH synthesis in G6PD-deficient erythrocytes exposed to oxidative stressors such as primaquine?",
        "ch": [
            "Excessive accumulation of reduced glutathione causes toxic hyperpolarization of the cell membrane.",
            "Failure to regenerate reduced GSH leads to peroxidative lipid damage and membrane lysis.",
            "The erythrocyte switches to mitochondrial oxidative phosphorylation, depleting cellular oxygen.",
            "Excess pentose phosphates accumulate and trigger premature mitotic chromosome condensation."
        ],
        "a": 1,
        "e": "<strong>Pathophysiology of G6PD deficiency:</strong> Because mature erythrocytes rely solely on the PPP for NADPH, low G6PDH activity prevents the efficient reduction of GSSG back to GSH. Without sufficient reduced GSH, glutathione peroxidase cannot neutralize $\\text{H}_2\\text{O}_2$ and organic peroxides. Unchecked ROS oxidize membrane polyunsaturated fatty acids (lipid peroxidation) and cross-link hemoglobin sulfhydryl groups into Heinz bodies, compromising erythrocyte deformability and causing massive intravascular and extravascular hemolysis ($38.6\\%$ in Table 1).<br><br><em>Distractor Traps:</em><br>&bull; A states the exact opposite: GSH is severely depleted ($0.9\\;\\mu\\text{mol/g Hb}$), not accumulated.<br>&bull; C is impossible because erythrocytes lack mitochondria.<br>&bull; D is impossible because mature erythrocytes lack nuclei and chromosomes."
    },
    {
        "q": "The cofactor thiamine pyrophosphate (TPP) is an indispensable catalytic prosthetic group for which enzyme in the non-oxidative branch of the pentose phosphate pathway?",
        "ch": [
            "Glucose-6-phosphate dehydrogenase",
            "6-Phosphogluconate dehydrogenase",
            "Transaldolase",
            "Transketolase"
        ],
        "a": 3,
        "e": "<strong>Cofactor requirement of transketolase:</strong> Transketolase transfers two-carbon glycoaldehyde units between phosphorylated sugars in the reversible non-oxidative phase of the PPP and requires thiamine pyrophosphate (TPP, Vitamin B1) and $\\text{Mg}^{2+}$ as essential cofactors. Transketolase erythrocyte activity assays are clinically used to diagnose thiamine deficiency (beriberi/Wernicke-Korsakoff syndrome). Transaldolase transfers three-carbon units via a Schiff base intermediate and does not use TPP.<br><br><em>Distractor Traps:</em><br>&bull; A and B are dehydrogenases in the oxidative phase that utilize $\\text{NADP}^+$.<br>&bull; C (Transaldolase) utilizes an active-site lysine Schiff base rather than TPP."
    },
    {
        "q": "How many moles of NADPH and carbon dioxide (CO_2) are produced per mole of glucose-6-phosphate processed through the oxidative branch of the pentose phosphate pathway?",
        "ch": [
            "1 mole of NADPH and 0 moles of CO_2",
            "1 mole of NADPH and 1 mole of CO_2",
            "2 moles of NADPH and 1 mole of CO_2",
            "2 moles of NADPH and 2 moles of CO_2"
        ],
        "a": 2,
        "e": "<strong>Oxidative branch stoichiometry:</strong> The oxidative branch comprises two separate dehydrogenase reactions: (1) G6PDH oxidizes G6P (6 carbons) to 6-phosphoglucono-$\\delta$-lactone, reducing 1 $\\text{NADP}^+$ to 1 NADPH. (2) 6-phosphogluconolactonase hydrolyzes the lactone to 6-phosphogluconate. (3) 6-phosphogluconate dehydrogenase oxidatively decarboxylates 6-phosphogluconate (6 carbons) to ribulose-5-phosphate (5 carbons), releasing 1 mole of $\\text{CO}_2$ and reducing a second mole of $\\text{NADP}^+$ to NADPH. Thus, the overall net yield is exactly 2 NADPH and 1 $\\text{CO}_2$ per G6P.<br><br><em>Distractor Traps:</em><br>&bull; A and B account for only one of the two dehydrogenase steps.<br>&bull; D incorrectly doubles the decarboxylation yield."
    },
    {
        "q": "Under physiological conditions in rapidly dividing neoplastic cells that require high rates of de novo purine nucleotide synthesis but minimal additional reducing equivalents, how is glucose-6-phosphate primarily channeled?",
        "ch": [
            "Solely through the oxidative PPP branch, generating excess NADPH for mitochondrial respiration.",
            "Through glycolysis to F6P and G3P, which are converted to ribose-5-phosphate via the reversible non-oxidative PPP branch.",
            "Directly into glycogen synthesis to store excess hexose units for future mitotic cycles.",
            "Through the complete Krebs cycle to maximize mitochondrial carbon dioxide output."
        ],
        "a": 1,
        "e": "<strong>Flexibility of non-oxidative PPP:</strong> When the cellular requirement for ribose-5-phosphate (nucleotide precursor) exceeds the need for NADPH, the oxidative phase is bypassed to avoid excess NADPH accumulation. Instead, glucose undergoes glycolysis to produce fructose-6-phosphate (F6P) and glyceraldehyde-3-phosphate (G3P). The reversible non-oxidative PPP enzymes (transketolase and transaldolase) then run in reverse, converting two moles of F6P and one mole of G3P into three moles of ribose-5-phosphate without producing any NADPH.<br><br><em>Distractor Traps:</em><br>&bull; A produces unnecessary NADPH and limits ribose yield.<br>&bull; C sequesters carbons away from nucleotide synthesis.<br>&bull; D burns carbons to $\\text{CO}_2$ instead of providing pentose backbones."
    },
    {
        "q": "The tripeptide glutathione contains which specific amino acid residue whose thiol (-SH) group is directly responsible for reducing reactive peroxides?",
        "ch": [
            "Methionine",
            "Cysteine",
            "Serine",
            "Threonine"
        ],
        "a": 1,
        "e": "<strong>Structure and chemistry of glutathione:</strong> Glutathione is the tripeptide $\\gamma$-L-glutamyl-L-cysteinylglycine. The central amino acid is cysteine, which possesses a nucleophilic, easily oxidizable sulfhydryl (thiol, $-\\text{SH}$) group. In the presence of reactive peroxides, two reduced GSH monomers donate two electrons and protons, forming a covalent disulfide bond ($\\text{GS-SG}$) while reducing peroxide to water ($2\\text{ GSH} + \\text{H}_2\\text{O}_2 \\rightarrow \\text{GSSG} + 2\\text{ H}_2\\text{O}$).<br><br><em>Distractor Traps:</em><br>&bull; A (Methionine) contains a non-nucleophilic thioether ($-\\text{S}-\\text{CH}_3$) that cannot form disulfide bonds.<br>&bull; C and D contain hydroxyl groups ($-\\text{OH}$), not thiol groups."
    }
]

passages.append({
    "id": "exam_bb90_2_p1",
    "sec": "B/B",
    "topic": "Pentose Phosphate Pathway, G6PDH & Glutathione Redox Homeostasis",
    "label": "Biological and Biochemical Foundations of Living Systems",
    "examId": "bb90_2",
    "passage": p1_html,
    "qs": p1_qs
})

print("Passage 1 defined.")

# ==============================================================================
# PASSAGE 2: Glycogen Metabolism, Phosphorylase Cascades & Inborn Errors
# Topics: Glycogen phosphorylase vs synthase, PKA cascade, glucagon/epinephrine, Von Gierke/McArdle
# ==============================================================================
p2_html = r"""<div class="ttl">Passage 2 (Questions 7&ndash;12)</div>
<p>Hepatic and skeletal muscle glycogen stores represent the primary mobilized storage form of glucose in human physiology. Glycogen is a branched homopolysaccharide composed of D-glucose residues linked by $\alpha(1\rightarrow 4)$ glycosidic bonds along the linear chains and $\alpha(1\rightarrow 6)$ glycosidic bonds at branch points occurring every 8 to 12 residues. Glycogen synthesis and breakdown are reciprocally regulated by hormone-activated phosphorylation cascades to prevent futile substrate cycling.</p>
<p>During fasting or physiological stress, glucagon (in hepatocytes) or epinephrine (in myocytes and hepatocytes) binds to $G\alpha_s$-coupled GPCRs, stimulating adenylate cyclase to produce cyclic AMP (cAMP). Elevated cAMP allosterically activates protein kinase A (PKA). Active PKA directly phosphorylates and activates phosphorylase kinase, which in turn phosphorylates the inactive, dephosphorylated form of glycogen phosphorylase (phosphorylase <i>b</i>) to its active, phosphorylated form (phosphorylase <i>a</i>). Glycogen phosphorylase catalyzes the phosphorolytic cleavage of $\alpha(1\rightarrow 4)$ glycosidic linkages from the non-reducing ends of glycogen chains, consuming inorganic phosphate ($\text{P}_i$) to release glucose-1-phosphate (G1P). Simultaneously, PKA phosphorylates glycogen synthase, converting it from its active dephosphorylated <i>a</i> form to its inactive phosphorylated <i>b</i> form, halting glycogenesis.</p>
<p>Phosphoglucomutase interconverts G1P and G6P. In hepatocytes, the endoplasmic reticulum-anchored lumenal enzyme glucose-6-phosphatase (G6Pase) hydrolyzes G6P to free glucose, which is exported into the bloodstream via GLUT2 to maintain systemic euglycemia. Skeletal myocytes lack G6Pase; consequently, G6P generated by muscle glycogenolysis is shunted directly into glycolysis for local ATP synthesis.</p>
<p>Physicians evaluated three pediatric patients presenting with severe exercise intolerance or fasting hypoglycemia. Enzymatic activity assays on tissue biopsies and systemic blood metabolite profiles are summarized in Table 1.</p>
<table class="tbl">
  <caption>Table 1 Enzymatic activities in tissue biopsies and post-exercise/fasting metabolic profiles</caption>
  <thead>
    <tr><th>Subject</th><th>Hepatic G6Pase Activity (% normal)</th><th>Muscle Glycogen Phosphorylase Activity (% normal)</th><th>Fasting Blood Glucose (mg/dL)</th><th>Post-Exercise Venous Lactate</th><th>Clinical Presentation</th></tr>
  </thead>
  <tbody>
    <tr><td>Control</td><td>100%</td><td>100%</td><td>88 (Normal)</td><td>Marked rise (4.2 mM)</td><td>Normal exercise tolerance</td></tr>
    <tr><td>Patient A</td><td>4%</td><td>98%</td><td>38 (Severe hypoglycemia)</td><td>Moderate rise (2.5 mM)</td><td>Hepatomegaly, lactic acidosis, failure to thrive</td></tr>
    <tr><td>Patient B</td><td>100%</td><td>2%</td><td>92 (Normal)</td><td>Zero rise (0.8 mM)</td><td>Severe muscle cramping, myoglobinuria on exertion</td></tr>
    <tr><td>Patient C</td><td>99%</td><td>100%</td><td>86 (Normal)</td><td>Marked rise (4.0 mM)</td><td>Normal exercise, mild asymptomatic hyperuricemia</td></tr>
  </tbody>
</table>
<p>In muscle, glycogen phosphorylase <i>b</i> can also be allosterically activated without phosphorylation by high concentrations of 5'-AMP, while being allosterically inhibited by ATP and G6P.</p>"""

p2_qs = [
    {
        "q": "Based on the biopsy and metabolic findings in Table 1, which inborn errors of glycogen metabolism affect Patient A and Patient B, respectively?",
        "ch": [
            "Patient A has McArdle disease (Type V), and Patient B has Pompe disease (Type II).",
            "Patient A has Von Gierke disease (Type I), and Patient B has McArdle disease (Type V).",
            "Patient A has Cori disease (Type III), and Patient B has Von Gierke disease (Type I).",
            "Patient A has Pompe disease (Type II), and Patient B has Anderson disease (Type IV)."
        ],
        "a": 1,
        "e": "<strong>Differential diagnosis of glycogen storage diseases:</strong> Patient A presents with severe fasting hypoglycemia (38 mg/dL), hepatomegaly, lactic acidosis, and profoundly deficient hepatic glucose-6-phosphatase activity (4%), which is diagnostic for Type I Glycogen Storage Disease (Von Gierke disease). Because G6P cannot be converted to free glucose, it backs up into glycolysis and lactate. Patient B exhibits normal hepatic G6Pase and normal fasting blood glucose, but nearly zero muscle glycogen phosphorylase (myophosphorylase) activity (2%), accompanied by exercise-induced muscle cramps, rhabdomyolysis/myoglobinuria, and failure of venous lactate to rise during ischemic exercise, which is classic for Type V Glycogen Storage Disease (McArdle disease).<br><br><em>Distractor Traps:</em><br>&bull; A, C, and D misassign the specific enzymatic lesions."
    },
    {
        "q": "Why does Patient B fail to exhibit a rise in venous blood lactate following strenuous anaerobic forearm exercise?",
        "ch": [
            "Myocytes lack functional lactate dehydrogenase to convert pyruvate to lactate.",
            "Deficiency of muscle glycogen phosphorylase prevents the generation of G6P substrates for anaerobic glycolysis.",
            "Excessive hepatic gluconeogenesis immediately clears all peripheral blood lactate.",
            "Muscle capillary blood flow is completely arrested by structural sarcomere collapse."
        ],
        "a": 1,
        "e": "<strong>Pathophysiology of McArdle disease:</strong> During intense anaerobic exercise, skeletal muscle relies predominantly on the rapid breakdown of internal glycogen stores to yield G1P, which is converted to G6P and enters glycolysis to generate ATP and lactate. Because Patient B lacks muscle glycogen phosphorylase (myophosphorylase), myocytes cannot mobilize glycogen into G6P. Without this primary anaerobic fuel supply, glycolytic flux and downstream pyruvate production cease, resulting in a flat post-exercise lactate curve (a classic ischemic forearm exercise test finding).<br><br><em>Distractor Traps:</em><br>&bull; A describes LDH deficiency (a rare, distinct disorder).<br>&bull; C describes the Cori cycle, which cannot clear lactate instantly during active exertion.<br>&bull; D invents structural capillary collapse."
    },
    {
        "q": "What is the energetic benefit of phosphorolytic cleavage of glycogen by glycogen phosphorylase compared to simple hydrolytic cleavage?",
        "ch": [
            "It generates free glucose that can freely diffuse across the sarcolemma without GLUT transporters.",
            "It yields glucose-1-phosphate directly, saving one ATP equivalent per hexose unit entering glycolysis.",
            "It consumes two moles of ATP per glycosidic bond cleaved to accelerate reaction velocity.",
            "It avoids producing phosphorylated intermediates that could trigger allosteric hexokinase inhibition."
        ],
        "a": 1,
        "e": "<strong>Energetics of phosphorolysis:</strong> Glycogen phosphorylase uses inorganic phosphate ($\\text{P}_i$) to cleave $\\alpha(1\\rightarrow 4)$ bonds, producing glucose-1-phosphate (G1P). Phosphoglucomutase then converts G1P to glucose-6-phosphate (G6P) without consuming any ATP. If glycogen were hydrolyzed with water, free glucose would be released, requiring hexokinase to consume 1 mole of ATP (converting glucose + ATP to G6P + ADP). Therefore, phosphorolysis conserves one high-energy phosphate bond (1 ATP) per mobilized glucosyl unit entering glycolysis.<br><br><em>Distractor Traps:</em><br>&bull; A is false: phosphorolysis yields G1P, which is charged and trapped in the cell.<br>&bull; C states it consumes ATP (phosphorolysis consumes inorganic $\\text{P}_i$, not ATP).<br>&bull; D is false: G6P is an allosteric inhibitor of hexokinase, but this does not negate the ATP savings."
    },
    {
        "q": "During intense skeletal muscle contraction in an unphosphorylated resting state, glycogen phosphorylase b is allosterically activated by which intracellular metabolite?",
        "ch": [
            "ATP",
            "Glucose-6-phosphate",
            "5'-AMP",
            "Citrate"
        ],
        "a": 2,
        "e": "<strong>Allosteric regulation of myophosphorylase:</strong> In skeletal muscle, when vigorous contraction hydrolyzes ATP into ADP and then AMP (via adenylate kinase), intracellular $[\\text{5'-AMP}]$ rises sharply. AMP binds to an allosteric nucleotide-binding site on glycogen phosphorylase <i>b</i>, inducing a conformational shift from the inactive T (tense) state to the active R (relaxed) state, activating the enzyme even in the absence of hormone-driven phosphorylation. ATP and G6P compete with AMP for this site and stabilize the inactive T state.<br><br><em>Distractor Traps:</em><br>&bull; A, B, and D are allosteric inhibitors of glycogen phosphorylase."
    },
    {
        "q": "Which enzymatic cascade accurately describes the activation of glycogenolysis in hepatocytes in response to glucagon binding?",
        "ch": [
            "Glucagon &rarr; Gi-protein &rarr; adenylate cyclase &rarr; cAMP drop &rarr; PKA inactivation",
            "Glucagon &rarr; Gs-protein &rarr; adenylate cyclase &rarr; cAMP rise &rarr; PKA activation &rarr; Phosphorylase kinase activation &rarr; Glycogen phosphorylase a activation",
            "Glucagon &rarr; Gq-protein &rarr; phospholipase C &rarr; IP3 rise &rarr; Calmodulin kinase &rarr; Glycogen synthase activation",
            "Glucagon &rarr; Receptor tyrosine kinase &rarr; Ras &rarr; MAPK &rarr; Protein phosphatase-1 activation"
        ],
        "a": 1,
        "e": "<strong>Glucagon signaling cascade:</strong> Glucagon binds to hepatic $G\\alpha_s$-coupled GPCRs $\\rightarrow$ activates adenylate cyclase $\\rightarrow$ increases intracellular cAMP $\\rightarrow$ activates PKA $\\rightarrow$ PKA phosphorylates and activates phosphorylase kinase $\\rightarrow$ phosphorylase kinase phosphorylates glycogen phosphorylase <i>b</i> into active glycogen phosphorylase <i>a</i> $\\rightarrow$ triggers glycogen breakdown.<br><br><em>Distractor Traps:</em><br>&bull; A uses $G\\alpha_i$ (inhibitory).<br>&bull; C describes $G\\alpha_q$ signaling.<br>&bull; D describes RTK/insulin signaling, which activates PP1 and promotes glycogenesis."
    },
    {
        "q": "Why does epinephrine stimulate glycogenolysis in both skeletal muscle and liver, whereas glucagon stimulates glycogenolysis almost exclusively in the liver?",
        "ch": [
            "Skeletal muscle fibers lack glucagon GPCR receptors on their sarcolemma.",
            "Myocytes possess a modified PKA isoform that is selectively insensitive to cAMP.",
            "Glucagon is degraded instantly upon entering peripheral capillaries by myoglobin.",
            "Skeletal muscle cell membranes are impermeable to all peptide hormone ligands."
        ],
        "a": 0,
        "e": "<strong>Tissue specificity of glucagon and epinephrine receptors:</strong> Hepatocytes express receptors for both glucagon (glucagon GPCRs) and epinephrine ($\\beta_2$- and $\\alpha_1$-adrenergic receptors), enabling the liver to maintain systemic blood glucose in response to both fasting (glucagon) and acute stress (epinephrine). In contrast, skeletal myocytes express high densities of $\\beta_2$-adrenergic receptors for epinephrine (fight-or-flight energy mobilization) but completely lack glucagon receptors, rendering muscle tissue unresponsive to systemic glucagon.<br><br><em>Distractor Traps:</em><br>&bull; B is false: muscle PKA is fully cAMP-dependent.<br>&bull; C invents enzymatic degradation of glucagon by myoglobin.<br>&bull; D is false: myocytes readily respond to insulin and epinephrine."
    }
]

passages.append({
    "id": "exam_bb90_2_p2",
    "sec": "B/B",
    "topic": "Glycogen Metabolism, Phosphorylase Cascades & Inborn Errors",
    "label": "Biological and Biochemical Foundations of Living Systems",
    "examId": "bb90_2",
    "passage": p2_html,
    "qs": p2_qs
})

print("Passage 2 defined.")

# ==============================================================================
# PASSAGE 3: Fatty Acid Beta-Oxidation, Carnitine Shuttle & Ketogenesis
# Topics: Carnitine palmitoyltransferase-1 (CPT-1), malonyl-CoA, acyl-CoA DH, FADH2/NADH, MCAD
# ==============================================================================
p3_html = r"""<div class="ttl">Passage 3 (Questions 13&ndash;18)</div>
<p>Mitochondrial $\beta$-oxidation of fatty acids represents the predominant source of metabolic ATP in cardiac muscle, resting skeletal muscle, and the fasting liver. Long-chain fatty acids (such as palmitate, $\text{C}_{16:0}$) are initially activated in the cytosol by long-chain acyl-CoA synthetase to form fatty acyl-CoA esters, consuming two high-energy phosphoanhydride equivalents (ATP $\rightarrow$ AMP + $\text{PP}_i$).</p>
<p>Because the inner mitochondrial membrane (IMM) is impermeable to hydrophilic acyl-CoA esters, translocation into the mitochondrial matrix requires the three-component <i>carnitine shuttle</i>. On the outer mitochondrial membrane (OMM), carnitine palmitoyltransferase-1 (CPT-1) transesterifies the fatty acyl moiety from coenzyme A to L-carnitine, forming acylcarnitine. Carnitine-acylcarnitine translocase (CACT) antiporters exchange cytosolic acylcarnitine for matrix carnitine across the IMM. Finally, carnitine palmitoyltransferase-2 (CPT-2) in the matrix regenerates the fatty acyl-CoA and releases free carnitine. CPT-1 is the rate-limiting committed regulatory enzyme of $\beta$-oxidation and is potently allosterically inhibited by malonyl-CoA, the first committed intermediate of de novo fatty acid synthesis catalyzed by acetyl-CoA carboxylase (ACC).</p>
<p>Once inside the matrix, each spiral of $\beta$-oxidation shortens the acyl-CoA chain by two carbons via four sequential reactions: (1) oxidation by flavin adenine dinucleotide (FAD)-dependent acyl-CoA dehydrogenase to generate a <i>trans</i>-$\Delta^2$-enoyl-CoA and $\text{FADH}_2$, (2) hydration by enoyl-CoA hydratase to form an L-$\beta$-hydroxyacyl-CoA, (3) oxidation by $\text{NAD}^+$-dependent $\beta$-hydroxyacyl-CoA dehydrogenase to yield a $\beta$-ketoacyl-CoA and NADH, and (4) thiolytic cleavage by $\beta$-ketothiolase with coenzyme A to release one molecule of acetyl-CoA and a shortened fatty acyl-CoA.</p>
<p>In prolonged fasting, excess hepatic acetyl-CoA exceeds the condensing capacity of oxaloacetate in the citric acid cycle and is shunted into ketogenesis, synthesizing acetoacetate and $\beta$-hydroxybutyrate. Pediatric geneticists investigated fibroblasts from infants presenting with lethargy, hypoketotic hypoglycemia, and dicarboxylic aciduria during viral infections. Metabolic flux rates and enzyme activities are shown in Table 1.</p>
<table class="tbl">
  <caption>Table 1 Fatty acid oxidation flux and enzyme kinetics in control and patient fibroblasts</caption>
  <thead>
    <tr><th>Cell Line</th><th>Palmitate Oxidation Rate (nmol/min/mg protein)</th><th>CPT-1 Activity (% normal)</th><th>Medium-Chain Acyl-CoA DH (MCAD) Activity (% normal)</th><th>Serum Ketones on 24-hr Fast</th><th>Accumulated Metabolite Profile</th></tr>
  </thead>
  <tbody>
    <tr><td>Wild-Type Control</td><td>4.5</td><td>100%</td><td>100%</td><td>Elevated (3.8 mM)</td><td>None</td></tr>
    <tr><td>Patient 1</td><td>0.3</td><td>4%</td><td>102%</td><td>Near zero (0.1 mM)</td><td>Free carnitine, long-chain acyl-CoA</td></tr>
    <tr><td>Patient 2</td><td>1.2</td><td>98%</td><td>6%</td><td>Near zero (0.2 mM)</td><td>$\text{C}_6\text{--C}_{10}$ dicarboxylic acids, octanoylcarnitine</td></tr>
    <tr><td>Patient 3</td><td>4.4</td><td>99%</td><td>97%</td><td>Elevated (3.5 mM)</td><td>None</td></tr>
  </tbody>
</table>
<p>In Patient 2, impaired mitochondrial $\beta$-oxidation diverts accumulating medium-chain fatty acids into microsomal $\omega$-oxidation in the endoplasmic reticulum, producing dicarboxylic acids.</p>"""

p3_qs = [
    {
        "q": "Why is CPT-1 allosterically inhibited by malonyl-CoA in physiological states of nutritional abundance?",
        "ch": [
            "To prevent newly synthesized cytosolic fatty acids from being immediately translocated into mitochondria and degraded.",
            "To stimulate mitochondrial uncoupling protein-1 (UCP-1) thermogenesis in white adipose tissue.",
            "To trigger the irreversible proteolytic cleavage of Carnitine-Acylcarnitine Translocase in the outer membrane.",
            "To accelerate the conversion of acetoacetate into toxic acetone vapors in pulmonary alveoli."
        ],
        "a": 0,
        "e": "<strong>Reciprocal regulation of lipid metabolism:</strong> In the well-fed state (high insulin/glucagon ratio), acetyl-CoA carboxylase (ACC) is dephosphorylated and active, producing malonyl-CoA for de novo lipogenesis. Malonyl-CoA allosterically inhibits CPT-1 on the outer mitochondrial membrane. This reciprocal inhibition prevents newly synthesized fatty acids from entering the mitochondrial matrix, shutting off $\\beta$-oxidation and preventing a futile metabolic cycle where fatty acids are simultaneously synthesized and degraded.<br><br><em>Distractor Traps:</em><br>&bull; B describes brown fat non-shivering thermogenesis.<br>&bull; C invents irreversible translocase proteolysis.<br>&bull; D describes uncontrolled ketoacidosis."
    },
    {
        "q": "How many total rounds of beta-oxidation and how many molecules of acetyl-CoA are generated from the complete mitochondrial degradation of one molecule of palmitoyl-CoA (C_16:0)?",
        "ch": [
            "7 rounds of beta-oxidation and 7 acetyl-CoA molecules",
            "7 rounds of beta-oxidation and 8 acetyl-CoA molecules",
            "8 rounds of beta-oxidation and 8 acetyl-CoA molecules",
            "8 rounds of beta-oxidation and 16 acetyl-CoA molecules"
        ],
        "a": 1,
        "e": "<strong>Stoichiometry of palmitate $\\beta$-oxidation:</strong> Palmitoyl-CoA is a 16-carbon saturated fatty acyl-CoA ($C_n$, $n = 16$). Each round of $\\beta$-oxidation cleaves a 2-carbon acetyl-CoA unit. The number of cycles required is $(n/2) - 1 = (16/2) - 1 = 7$ rounds. The final 7th round cleaves a 4-carbon acetoacetyl-CoA into two separate molecules of acetyl-CoA. Thus, 7 rounds of $\\beta$-oxidation produce exactly $n/2 = 8$ molecules of acetyl-CoA, 7 $\\text{FADH}_2$, and 7 NADH.<br><br><em>Distractor Traps:</em><br>&bull; A calculates only 7 acetyl-CoA.<br>&bull; C incorrectly assumes 8 cycles are needed.<br>&bull; D doubles the carbon count."
    },
    {
        "q": "Based on Table 1, why does Patient 2 present with hypoketotic hypoglycemia and elevated octanoylcarnitine during fasting?",
        "ch": [
            "Severe CPT-1 deficiency completely blocks the entry of all fatty acids into the mitochondrial matrix.",
            "MCAD deficiency arrests beta-oxidation at medium-chain lengths, preventing acetyl-CoA generation for ketogenesis and ATP for gluconeogenesis.",
            "Excessive accumulation of malonyl-CoA stimulates uncontrolled insulin hypersecretion by pancreatic beta cells.",
            "Hepatic glycogen stores are irreversibly converted into insoluble dicarboxylic acid crystals."
        ],
        "a": 1,
        "e": "<strong>Pathophysiology of MCAD deficiency:</strong> Patient 2 has severe Medium-Chain Acyl-CoA Dehydrogenase (MCAD) deficiency (6% activity). Long-chain fatty acids enter mitochondria and are degraded normally until they reach medium-chain length ($C_6-C_{10}$, predominantly $C_8$ octanoate). At this point, MCAD cannot oxidize them, causing $\beta$-oxidation to arrest. The lack of downstream acetyl-CoA impairs hepatic ketogenesis (causing hypoketonemia), and the resulting lack of ATP and NADH impairs hepatic gluconeogenesis (causing profound hypoglycemia). Accumulating medium-chain acyl groups are transesterified back to carnitine (yielding octanoylcarnitine) or oxidized via microsomal $\omega$-oxidation into dicarboxylic acids.<br><br><em>Distractor Traps:</em><br>&bull; A describes Patient 1 (CPT-1 deficiency).<br>&bull; C invents malonyl-CoA insulin stimulation.<br>&bull; D invents crystal formation."
    },
    {
        "q": "The first reaction in each spiral of mitochondrial fatty acid beta-oxidation introduces a trans double bond between carbons C2 and C3. Which electron carrier directly accepts electrons in this initial oxidation step?",
        "ch": [
            "NADP^+",
            "NAD^+",
            "FAD",
            "L-Carnitine"
        ],
        "a": 2,
        "e": "<strong>Acyl-CoA dehydrogenase cofactor:</strong> The first step is catalyzed by acyl-CoA dehydrogenase, an enzyme that uses flavin adenine dinucleotide (FAD) as its tightly bound prosthetic group to oxidize an alkane to an alkene ($-\\text{CH}_2-\\text{CH}_2- \\rightarrow -\\text{CH}=\\text{CH}-$). FAD is reduced to $\\text{FADH}_2$, which subsequently transfers electrons to the mitochondrial electron transport chain via the electron-transferring flavoprotein (ETF) and ubiquinone (Complex III). The third step ($\\beta$-hydroxyacyl-CoA dehydrogenase) uses $\\text{NAD}^+$.<br><br><em>Distractor Traps:</em><br>&bull; A ($\\text{NADP}^+$) is used in fatty acid synthesis and the PPP.<br>&bull; B ($\\text{NAD}^+$) is used in step 3 (hydroxyl to keto oxidation).<br>&bull; D (Carnitine) is a carrier, not an electron acceptor."
    },
    {
        "q": "Which ketone body produced by the liver during prolonged starvation is chemically spontaneous and non-enzymatically converted into acetone?",
        "ch": [
            "Acetoacetate",
            "beta-Hydroxybutyrate",
            "Acetyl-CoA",
            "Succinyl-CoA"
        ],
        "a": 0,
        "e": "<strong>Non-enzymatic decarboxylation of acetoacetate:</strong> The primary ketone bodies synthesized in the mitochondrial matrix of hepatocytes are acetoacetate and $\\beta$-hydroxybutyrate. Acetoacetate is a $\\beta$-keto acid ($\\text{CH}_3-\\text{C}(=\\text{O})-\\text{CH}_2-\\text{COO}^-$). Like all $\\beta$-keto acids, it is thermodynamically unstable and undergoes slow, spontaneous non-enzymatic decarboxylation to release carbon dioxide ($\\text{CO}_2$) and volatile acetone ($\\text{CH}_3-\\text{C}(=\\text{O})-\\text{CH}_3$), giving the characteristic fruity breath odor in severe diabetic ketoacidosis.<br><br><em>Distractor Traps:</em><br>&bull; B ($\\beta$-hydroxybutyrate) is a $\\beta$-hydroxy acid, not a $\\beta$-keto acid, and cannot decarboxylate spontaneously.<br>&bull; C and D are high-energy thioesters, not ketone bodies."
    },
    {
        "q": "Why is the liver incapable of utilizing the ketone bodies it synthesizes for its own metabolic energy needs?",
        "ch": [
            "Hepatocytes lack the enzyme beta-ketoacyl-CoA transferase (thiophorase).",
            "Hepatocyte inner mitochondrial membranes are completely impermeable to ketone bodies.",
            "Ketone bodies irreversibly inhibit hepatic electron transport chain Complex IV.",
            "Hepatic mitochondria lack the Krebs cycle enzyme citrate synthase."
        ],
        "a": 0,
        "e": "<strong>Tissue utilization of ketone bodies and thiophorase:</strong> Extrahepatic tissues (brain, cardiac muscle, skeletal muscle, renal cortex) convert acetoacetate back to acetyl-CoA using the key enzyme $\\beta$-ketoacyl-CoA transferase (also known as <i>thiophorase</i> or succinyl-CoA:3-ketoacid CoA transferase). Thiophorase transfers a CoA moiety from succinyl-CoA to acetoacetate, generating acetoacetyl-CoA. The liver lacks thiophorase activity; consequently, hepatocytes cannot utilize ketone bodies and must export them into the circulation for extrahepatic fuel, preventing futile consumption.<br><br><em>Distractor Traps:</em><br>&bull; B is false: ketone bodies are small, water-soluble molecules that readily cross membranes.<br>&bull; C invents Complex IV inhibition.<br>&bull; D is false: hepatocytes have abundant citrate synthase."
    }
]

passages.append({
    "id": "exam_bb90_2_p3",
    "sec": "B/B",
    "topic": "Fatty Acid Beta-Oxidation, Carnitine Shuttle & Ketogenesis",
    "label": "Biological and Biochemical Foundations of Living Systems",
    "examId": "bb90_2",
    "passage": p3_html,
    "qs": p3_qs
})

print("Passage 3 defined.")

# ==============================================================================
# PASSAGE 4: DNA Excision Repair, Nucleotide Excision Repair & Xeroderma Pigmentosum
# Topics: UV thymine dimers, NER vs BER, XP endonucleases, AP endonuclease, DNA ligase
# ==============================================================================
p4_html = r"""<div class="ttl">Passage 4 (Questions 19&ndash;24)</div>
<p>Genomic integrity is continually threatened by environmental mutagens that induce covalent DNA structural lesions. Ultraviolet (UV) radiation (primarily UVB, $\lambda = 280\text{--}315\text{ nm}$) induces photochemical cross-linking between adjacent pyrimidine bases on the same DNA strand, generating bulky distorting adducts: cyclobutane pyrimidine dimers (CPDs, predominantly thymine-thymine dimers, $\text{T}<>\text{T}$) and 6-4 photoproducts (6-4PPs). These helix-distorting lesions disrupt Watson-Crick base pairing and stall high-fidelity replicative DNA polymerases ($\text{Pol } \delta$ and $\text{Pol } \epsilon$), initiating translesion synthesis or apoptosis.</p>
<p>In humans, pyrimidine dimers are repaired exclusively through <i>nucleotide excision repair</i> (NER). The NER mechanism proceeds through four coordinated stages: (1) <b>Lesion recognition</b>: In global genome NER (GG-NER), the XPC-RAD23B protein complex recognizes helical distortion, whereas in transcription-coupled NER (TC-NER), stalled RNA polymerase II recruits the CSB and CSA proteins. (2) <b>Pre-incision complex assembly and unwinding</b>: The multi-subunit transcription factor TFIIH is recruited; its ATP-dependent DNA helicase subunits, XPB ($3'\rightarrow 5'$) and XPD ($5'\rightarrow 3'$), unwind approximately 20 to 30 base pairs around the lesion. (3) <b>Dual endonucleolytic incision and excision</b>: The structure-specific endonuclease XPF-ERCC1 cleaves the damaged strand $5'$ to the lesion (approximately 20&ndash;22 nucleotides upstream), while the XPG endonuclease cleaves $3'$ to the lesion (approximately 5&ndash;6 nucleotides downstream), releasing an oligonucleotide fragment of 24 to 32 nucleotides containing the damaged dimer. (4) <b>Resynthesis and ligation</b>: DNA polymerase $\delta$ or $\epsilon$ fills the resulting single-stranded gap using the undamaged complementary strand as a template, and DNA ligase I (or Ligase III$\alpha$-XRCC1) seals the remaining phosphodiester nick.</p>
<p>In contrast, non-bulky oxidative lesions (such as 8-oxoguanine) or spontaneous deamination events (such as cytosine to uracil) are resolved via <i>base excision repair</i> (BER), initiated by a lesion-specific DNA glycosylase that cleaves the $N$-glycosidic bond, leaving an apurinic/apyrimidinic (AP) site cleaved by AP endonuclease.</p>
<p>Biochemists assessed NER proficiency in skin fibroblasts isolated from a healthy donor and two patients suffering from Xeroderma Pigmentosum (XP), an autosomal recessive disorder characterized by extreme solar sensitivity and a >1,000-fold increase in skin malignancies. Cells were irradiated with 10 $\text{J/m}^2$ of 254 nm UVC light, and DNA repair parameters were quantified in Table 1.</p>
<table class="tbl">
  <caption>Table 1 DNA damage repair and unscheduled DNA synthesis in normal and XP patient fibroblasts</caption>
  <thead>
    <tr><th>Cell Strain</th><th>Genetic Complementation Group</th><th>Residual T&lt;&gt;T Dimers at 24 hr (%)</th><th>Unscheduled DNA Synthesis (UDS, % normal)</th><th>Excision Fragment Size</th><th>Clinical Features</th></tr>
  </thead>
  <tbody>
    <tr><td>Wild-Type</td><td>Control</td><td>< 5%</td><td>100%</td><td>28&ndash;30 nucleotides</td><td>Normal solar tolerance</td></tr>
    <tr><td>Patient 1</td><td>XP-A (Defective lesion verification)</td><td>> 95%</td><td>< 2%</td><td>None detected</td><td>Severe early sunburns, multiple basal/squamous cell carcinomas</td></tr>
    <tr><td>Patient 2</td><td>XP-G (Defective 3' incision)</td><td>> 90%</td><td>< 3%</td><td>None detected</td><td>Cutaneous photosensitivity, neurological degeneration</td></tr>
    <tr><td>Patient 3</td><td>Cockayne Syndrome (CS-B)</td><td>~45%</td><td>75% (GG-NER intact)</td><td>28&ndash;30 nt (slow)</td><td>Severe developmental delay, microcephaly, no skin cancer</td></tr>
  </tbody>
</table>
<p>Complementation assays demonstrated that fusing Patient 1 fibroblasts with Patient 2 fibroblasts restored 100% normal UV resistance and excision fragment release.</p>"""

p4_qs = [
    {
        "q": "What type of chemical covalent linkage is created when UV radiation induces the formation of a thymine-thymine cyclobutane pyrimidine dimer?",
        "ch": [
            "A phosphodiester bond linking two adjacent phosphate backbones",
            "A four-membered cyclobutane ring connecting the C5 and C6 carbons of adjacent thymines",
            "An N-glycosidic bond linking the thymine base to deoxyribose",
            "A disulfide bridge cross-linking cysteine residues in adjacent histones"
        ],
        "a": 1,
        "e": "<strong>Photochemistry of pyrimidine dimers:</strong> Absorption of UVB/UVC photons excites the conjugated $\\pi$-electrons of adjacent pyrimidine bases (such as two thymines on the same strand). This induces a photochemical $[2+2]$ cycloaddition between the carbon-carbon double bonds at positions C5 and C6 of the two adjacent rings, forming a stable four-membered cyclobutane ring. This structure severely bends and distorts the DNA B-form double helix by $\\sim 30^\\circ$.<br><br><em>Distractor Traps:</em><br>&bull; A describes normal backbone bonds.<br>&bull; C describes the base-sugar linkage.<br>&bull; D describes protein disulfide bonds."
    },
    {
        "q": "How does the molecular mechanism of Nucleotide Excision Repair (NER) fundamentally differ from Base Excision Repair (BER)?",
        "ch": [
            "NER removes an oligonucleotide fragment (24&ndash;32 nucleotides) via dual endonucleolytic cleavage, whereas BER removes a single damaged base via glycosylase cleavage.",
            "NER operates exclusively in mitochondrial DNA, whereas BER functions exclusively in the nucleus.",
            "NER requires reverse transcriptase to synthesize a cDNA template, whereas BER uses DNA ligase.",
            "NER fixes non-bulky oxidative base lesions, whereas BER fixes bulky helix-distorting photoproducts."
        ],
        "a": 0,
        "e": "<strong>NER vs BER mechanisms:</strong> NER targets bulky, helix-distorting lesions (such as CPDs and cisplatin adducts) by making dual endonucleolytic incisions on both sides of the lesion, excising an entire single-stranded oligonucleotide patch (24&ndash;32 nucleotides). In contrast, BER resolves small, non-distorting base modifications (e.g., uracil, 8-oxoguanine) using a DNA glycosylase to cleave only the $N$-glycosidic bond of the single damaged base, creating an AP site that is subsequently incised by AP endonuclease and repaired with a single-nucleotide or short-patch insertion.<br><br><em>Distractor Traps:</em><br>&bull; B is false: mitochondria rely primarily on BER and lack canonical NER.<br>&bull; C describes retroviral replication.<br>&bull; D reverses the lesion substrate specificities of the two pathways."
    },
    {
        "q": "Why did cell fusion between fibroblasts from Patient 1 (XP-A) and Patient 2 (XP-G) restore normal DNA repair capacity in the complementation assay?",
        "ch": [
            "Patient 1 supplied functional XPG protein, while Patient 2 supplied functional XPA protein, rescuing the heterokaryon.",
            "Cell fusion induced spontaneous translesion synthesis polymerases that bypass all pyrimidine dimers.",
            "The fusion procedure heated the cells to 95 &deg;C, melting the cyclobutane pyrimidine rings.",
            "Patient 1 fibroblasts contained reverse transcriptase that replaced all mutated genomic loci."
        ],
        "a": 0,
        "e": "<strong>Genetic complementation:</strong> Xeroderma Pigmentosum exhibits locus heterogeneity with multiple complementation groups (XP-A through XP-G). Patient 1 carries biallelic mutations in <i>XPA</i> (but has wild-type <i>XPG</i>), whereas Patient 2 carries mutations in <i>XPG</i> (but has wild-type <i>XPA</i>). When these two cell strains are fused into a hybrid binucleated cell (heterokaryon), the intact gene products from one nucleus compensate for the defective gene products of the other, reconstituting a fully intact multi-protein NER machinery.<br><br><em>Distractor Traps:</em><br>&bull; B describes error-prone translesion bypass (Pol $\eta$), which does not excise dimers.<br>&bull; C would denature and kill living cells.<br>&bull; D invents reverse transcriptase gene replacement."
    },
    {
        "q": "What specific enzymatic role does the endonuclease XPF-ERCC1 execute during eukaryotic nucleotide excision repair?",
        "ch": [
            "Cleaving the phosphodiester backbone 5' to the DNA lesion",
            "Cleaving the phosphodiester backbone 3' to the DNA lesion",
            "Cleaving the N-glycosidic bond linking thymine to deoxyribose",
            "Synthesizing the replacement DNA strand in the 5' to 3' direction"
        ],
        "a": 0,
        "e": "<strong>Dual incision polarity in NER:</strong> The structure-specific endonuclease XPF-ERCC1 makes the 5' incision relative to the damaged pyrimidine dimer (approximately 20&ndash;22 nucleotides upstream of the lesion). The XPG endonuclease makes the complementary 3' incision (approximately 5&ndash;6 nucleotides downstream). Together, these dual endonucleolytic cuts liberate the 24&ndash;32 nucleotide damaged oligonucleotide.<br><br><em>Distractor Traps:</em><br>&bull; B is executed by XPG endonuclease.<br>&bull; C is executed by DNA glycosylases in BER.<br>&bull; D is executed by DNA polymerase $\delta$/$\epsilon$."
    },
    {
        "q": "Why are individuals with Xeroderma Pigmentosum predisposed to developing cutaneous squamous and basal cell carcinomas primarily in sun-exposed areas?",
        "ch": [
            "Failure to repair UV lesions stalls replicative polymerases, forcing error-prone translesion bypass that inserts mismatched bases (C to T transitions).",
            "Unrepaired thymine dimers directly catalyze the phosphorylation of proto-oncogene promoters.",
            "UV radiation stimulates the direct integration of oncogenic retroviruses into keratinocyte DNA.",
            "DNA ligase I incorporates radioactive phosphate isotopes into epidermal stem cell telomeres."
        ],
        "a": 0,
        "e": "<strong>Molecular mechanism of UV carcinogenesis:</strong> When NER is deficient, pyrimidine dimers persist in genomic DNA. During S-phase replication, high-fidelity polymerases ($\text{Pol }\delta/\epsilon$) stall at these bulky lesions. Error-prone translesion DNA polymerases (such as Pol $\eta$ or Pol $\zeta$) are recruited to bypass the lesion. These bypass polymerases frequently misread pyrimidine dimers, predominantly incorporating adenines opposite cyclobutane dimers, leading to characteristic UV signature mutations: $\text{C}\rightarrow\text{T}$ and $\text{CC}\rightarrow\text{TT}$ transitions in critical tumor suppressor genes (e.g., <i>TP53</i>), driving malignant transformation.<br><br><em>Distractor Traps:</em><br>&bull; B asserts that dimers directly catalyze phosphorylation.<br>&bull; C describes oncogenic retroviruses (e.g., HPV/HTLV), not UV mutagenesis.<br>&bull; D invents radioactive telomere incorporation."
    },
    {
        "q": "In the final resynthesis step of nucleotide excision repair, what chemical functional groups are joined by DNA ligase to seal the phosphodiester backbone?",
        "ch": [
            "A 5'-triphosphate and a 3'-triphosphate",
            "A 5'-phosphate and a 3'-hydroxyl group",
            "A 5'-hydroxyl and a 3'-phosphate group",
            "An N-terminal amine and a C-terminal carboxylate"
        ],
        "a": 1,
        "e": "<strong>DNA ligase reaction chemistry:</strong> DNA ligase catalyzes the formation of a phosphodiester bond to seal a single-stranded nick in duplex DNA. It joins an adjacent 3'-hydroxyl group ($3'\\text{-OH}$) of the newly synthesized replacement strand to the 5'-monophosphate group ($5'\\text{-PO}_4$) of the existing flanking strand, utilizing the hydrolysis of ATP (in eukaryotes) or $\\text{NAD}^+$ (in bacteria) to drive adenylation of the nicked 5'-phosphate.<br><br><em>Distractor Traps:</em><br>&bull; A, C, and D state incorrect chemical reactive pairs (D describes a peptide bond)."
    }
]

passages.append({
    "id": "exam_bb90_2_p4",
    "sec": "B/B",
    "topic": "DNA Excision Repair, Nucleotide Excision Repair & Xeroderma Pigmentosum",
    "label": "Biological and Biochemical Foundations of Living Systems",
    "examId": "bb90_2",
    "passage": p4_html,
    "qs": p4_qs
})

print("Passage 4 defined.")

# ==============================================================================
# PASSAGE 5: Cardiac Cycle Electromechanics, Pressure-Volume Loops & Wiggers Diagram
# Topics: LV pressure-volume loops, stroke volume, isovolumetric contraction/relaxation, valve timing
# ==============================================================================
p5_html = r"""<div class="ttl">Passage 5 (Questions 25&ndash;30)</div>
<p>The mechanical performance of the human left ventricle (LV) across the cardiac cycle is quantitatively analyzed using pressure-volume (PV) loops and the classical Wiggers diagram. A standard LV PV loop traces ventricular intracavitary pressure against volume through four distinct thermodynamic phases, bounded by the opening and closure of the mitral (bicuspid) atrioventricular valve and the aortic semilunar valve.</p>
<p>Figure 1 illustrates the normal left ventricular PV loop. Phase 1 (Diastolic Filling, segment $A\rightarrow B$) begins with mitral valve opening at Point A at the end-systolic volume ($\text{ESV} \approx 50\text{ mL}$) and lowest diastolic pressure ($\sim 5\text{ mmHg}$). As blood fills the compliant ventricle, volume increases to the end-diastolic volume ($\text{EDV} \approx 120\text{ mL}$) at Point B ($\text{LVEDP} \approx 10\text{ mmHg}$). Phase 2 (Isovolumetric Contraction, segment $B\rightarrow C$) begins when ventricular pressure exceeds left atrial pressure, snapping the mitral valve shut (generating the first heart sound, $\text{S}_1$). Both mitral and aortic valves remain closed; the myocardium contracts against an incompressible fluid volume, driving pressure upward to approximately $80\text{ mmHg}$ at constant volume.</p>
<p>Phase 3 (Systolic Ejection, segment $C\rightarrow D$) begins when LV pressure exceeds aortic diastolic pressure at Point C, forcing the aortic valve open. Blood is ejected into the systemic aorta, reaching peak systolic pressure ($\sim 120\text{ mmHg}$) before pressure declines as volume decreases back to $\text{ESV}$ ($50\text{ mL}$) at Point D. Phase 4 (Isovolumetric Relaxation, segment $D\rightarrow A$) begins when LV pressure drops below aortic pressure, snapping the aortic valve shut (generating the second heart sound, $\text{S}_2$). With both valves closed, pressure plummets from $100\text{ mmHg}$ to $5\text{ mmHg}$ at constant volume ($\text{ESV}$) until mitral opening resets the cycle.</p>
<p>Stroke volume is defined as $\text{SV} = \text{EDV} - \text{ESV}$, and cardiac output is $\text{CO} = \text{HR} \times \text{SV}$. Cardiologists conducted hemodynamic catheterization studies on four clinical subjects under resting conditions ($\text{HR} = 75\text{ bpm}$). Hemodynamic parameters are compiled in Table 1.</p>
<table class="tbl">
  <caption>Table 1 Hemodynamic catheterization measurements and calculated LV indices</caption>
  <thead>
    <tr><th>Subject</th><th>End-Diastolic Volume (EDV, mL)</th><th>End-Systolic Volume (ESV, mL)</th><th>Peak Systolic LV Pressure (mmHg)</th><th>Calculated Stroke Volume (SV, mL)</th><th>Ejection Fraction (EF, %)</th></tr>
  </thead>
  <tbody>
    <tr><td>Control</td><td>120</td><td>50</td><td>120</td><td>70</td><td>58.3%</td></tr>
    <tr><td>Patient 1</td><td>160</td><td>110</td><td>110</td><td>50</td><td>31.3%</td></tr>
    <tr><td>Patient 2</td><td>110</td><td>30</td><td>190</td><td>80</td><td>72.7%</td></tr>
    <tr><td>Patient 3</td><td>180</td><td>60</td><td>125</td><td>120</td><td>66.7%</td></tr>
  </tbody>
</table>
<p>In Patient 2, severe aortic stenosis imposes a high ventricular afterload, forcing compensatory concentric myocardial hypertrophy.</p>"""

p5_qs = [
    {
        "q": "Which cardiac event is directly responsible for generating the first heart sound (S_1)?",
        "ch": [
            "Closure of the aortic and pulmonary semilunar valves at the end of systole",
            "Closure of the mitral and tricuspid atrioventricular valves at the onset of systole",
            "Rapid turbulent blood filling into a stiff non-compliant ventricle during early diastole",
            "Opening of the aortic valve during peak ventricular ejection"
        ],
        "a": 1,
        "e": "<strong>Valvular origins of heart sounds:</strong> The first heart sound ($S_1$, 'lub') is produced by the sudden reverberation of blood and closure of the atrioventricular (AV) valves (mitral and tricuspid) at the beginning of ventricular systole (Point B on the PV loop), signaling the start of isovolumetric contraction. The second heart sound ($S_2$, 'dub') is produced by the closure of the semilunar valves (aortic and pulmonary) at the end of systole (Point D), signaling the start of isovolumetric relaxation.<br><br><em>Distractor Traps:</em><br>&bull; A describes $S_2$.<br>&bull; C describes a pathological third heart sound ($S_3$).<br>&bull; D is silent in normal hearts."
    },
    {
        "q": "Based on Table 1, what is the resting cardiac output (CO) of Patient 1 (HR = 75 bpm)?",
        "ch": [
            "2.35 L/min",
            "3.75 L/min",
            "5.25 L/min",
            "8.25 L/min"
        ],
        "a": 1,
        "e": "<strong>Cardiac output calculation:</strong> Cardiac output is defined as $\\text{CO} = \\text{HR} \\times \\text{SV}$. For Patient 1, the stroke volume is $\\text{SV} = \\text{EDV} - \\text{ESV} = 160\\text{ mL} - 110\\text{ mL} = 50\\text{ mL} = 0.050\\text{ L}$. With a heart rate of $75\\text{ bpm}$: $\\text{CO} = 75\\text{ beats/min} \\times 0.050\\text{ L/beat} = 3.75\\text{ L/min}$. This depressed cardiac output and low ejection fraction ($31.3\\%$) indicate systolic heart failure.<br><br><em>Distractor Traps:</em><br>&bull; A ($2.35\\text{ L/min}$) uses $(160 - 110) \\times 47$.<br>&bull; C ($5.25\\text{ L/min}$) is the normal control output ($75 \\times 0.070 = 5.25\\text{ L/min}$).<br>&bull; D ($8.25\\text{ L/min}$) uses $\\text{ESV}$ as stroke volume."
    },
    {
        "q": "During Phase 2 (isovolumetric contraction) of the left ventricular cycle, how do ventricular volume and ventricular pressure change?",
        "ch": [
            "Volume decreases rapidly while pressure remains constant.",
            "Volume increases gradually while pressure decreases.",
            "Volume remains strictly constant while pressure increases sharply.",
            "Volume remains strictly constant while pressure plummets to near zero."
        ],
        "a": 2,
        "e": "<strong>Isovolumetric contraction mechanics:</strong> During isovolumetric contraction, the mitral valve has closed but ventricular pressure has not yet exceeded aortic pressure to open the aortic valve. Because blood is incompressible and all four cardiac valves are closed, the left ventricular volume cannot change (it remains fixed at $\\text{EDV}$). However, active tension development by contracting ventricular myocytes causes ventricular intracavitary pressure to spike precipitously from $\\sim 10\\text{ mmHg}$ to $\\sim 80\\text{ mmHg}$ until the aortic valve is forced open.<br><br><em>Distractor Traps:</em><br>&bull; A describes systolic ejection.<br>&bull; B describes ventricular filling.<br>&bull; D describes isovolumetric relaxation."
    },
    {
        "q": "According to the Frank-Starling law of the heart, an acute increase in venous return (end-diastolic volume) enhances stroke volume primarily because:",
        "ch": [
            "myocardial fiber stretch optimizes sarcomere actin-myosin overlap and increases calcium sensitivity.",
            "elevated volume directly activates beta-1 adrenergic receptors via mechanical tension.",
            "increased venous blood temperature accelerates the speed of conduction along the bundle of His.",
            "the pericardium contracts involuntarily to squeeze blood out of the left ventricle."
        ],
        "a": 0,
        "e": "<strong>Frank-Starling law mechanism:</strong> The Frank-Starling law states that the force of ventricular contraction is directly proportional to the initial end-diastolic length (stretch) of myocardial fibers (preload). In resting myocytes, sarcomeres are at a sub-optimal length ($\sim 1.8-2.0\\;\\mu\\text{m}$). Increased venous return stretches sarcomeres closer to their optimal length ($\sim 2.2\\;\\mu\\text{m}$), which optimizes the physical overlap between thick myosin and thin actin filaments, reduces lateral interfilament spacing, and increases the affinity of troponin C for $\\text{Ca}^{2+}$, maximizing cross-bridge cycling and force of contraction.<br><br><em>Distractor Traps:</em><br>&bull; B is false: Frank-Starling is an intrinsic physical property of muscle fibers, independent of autonomic adrenergic stimulation.<br>&bull; C and D are biologically incorrect."
    },
    {
        "q": "Patient 2 exhibits severe aortic stenosis with a peak systolic LV pressure of 190 mmHg compared to normal 120 mmHg. How will this increased afterload alter the appearance of the left ventricular PV loop?",
        "ch": [
            "The loop will shift downward with a lower top boundary and increased stroke volume.",
            "The loop will shift upward with a higher top boundary and increased end-systolic volume.",
            "The loop will widen horizontally toward higher end-diastolic volume with zero change in pressure.",
            "The loop will collapse into a single vertical line without any ejection phase."
        ],
        "a": 1,
        "e": "<strong>Afterload elevation on PV loops:</strong> Aortic stenosis increases afterload&mdash;the resistance against which the ventricle must pump to eject blood. To overcome the stenotic aortic valve, the myocardium must generate much higher pressures, elevating the upper boundary of the PV loop (up to $190\\text{ mmHg}$). Because the ventricle works against higher resistance, ejection ceases at a higher end-systolic pressure, leaving more blood behind in the ventricle ($\text{ESV}$ increases, reducing stroke volume unless contractility hypertrophies).<br><br><em>Distractor Traps:</em><br>&bull; A states the opposite (lower top boundary occurs in hypotension/vasodilation).<br>&bull; C describes an isolated increase in preload.<br>&bull; D is an extreme scenario compatible with complete aortic occlusion and instantaneous death."
    },
    {
        "q": "On a standard electrocardiogram (ECG) trace correlated with the Wiggers diagram, ventricular isovolumetric contraction begins immediately following which electrical waveform?",
        "ch": [
            "The peak of the P wave",
            "The QRS complex",
            "The ST segment",
            "The peak of the T wave"
        ],
        "a": 1,
        "e": "<strong>ECG electromechanical coupling:</strong> The QRS complex represents ventricular depolarization. Ventricular myocyte depolarization triggers calcium-induced calcium release (CICR) and myocardial tension development. Consequently, mechanical contraction and the resulting closure of the mitral valve (start of isovolumetric contraction) occurs immediately following the QRS complex. The P wave represents atrial depolarization, and the T wave represents ventricular repolarization.<br><br><em>Distractor Traps:</em><br>&bull; A (P wave) precedes atrial contraction.<br>&bull; C (ST segment) corresponds to the rapid systolic ejection phase.<br>&bull; D (T wave) precedes isovolumetric relaxation."
    }
]

passages.append({
    "id": "exam_bb90_2_p5",
    "sec": "B/B",
    "topic": "Cardiac Cycle Electromechanics, Pressure-Volume Loops & Wiggers Diagram",
    "label": "Biological and Biochemical Foundations of Living Systems",
    "examId": "bb90_2",
    "passage": p5_html,
    "qs": p5_qs
})

print("Passage 5 defined.")

# ==============================================================================
# PASSAGE 6: Renal Tubular Acid-Base Transport & Intercalated Cell Dynamics
# Topics: Type A vs Type B intercalated cells, H+-ATPase, AE1, pendrin, Renal Tubular Acidosis
# ==============================================================================
p6_html = r"""<div class="ttl">Passage 6 (Questions 31&ndash;36)</div>
<p>Systemic arterial blood pH is tightly defended within the narrow physiological range of 7.35 to 7.45. While the lungs modulate blood carbonic acid levels via ventilatory clearance of carbon dioxide ($\text{CO}_2$), the kidneys are responsible for the long-term maintenance of acid-base balance by reabsorbing virtually all filtered bicarbonate ($\text{HCO}_3^-$) in the proximal convoluted tubule (PCT) and actively secreting metabolic protons ($\text{H}^+$) in the late distal tubule and collecting duct.</p>
<p>The late distal convoluted tubule and cortical collecting duct contain two distinct subpopulations of intercalated cells with reciprocal functional polarities: <b>Type A intercalated cells</b> (acid-secreting) and <b>Type B intercalated cells</b> (bicarbonate-secreting). In Type A intercalated cells, intracellular carbonic anhydrase II ($\text{CA II}$) hydrates $\text{CO}_2$ into carbonic acid, which dissociates into $\text{H}^+$ and $\text{HCO}_3^-$. The apical (luminal) membrane possesses primary electrogenic $\text{H}^+\text{-ATPases}$ (vacuolar proton pumps) and electroneutral $\text{H}^+/\text{K}^+\text{-ATPases}$ that pump protons into the tubular lumen against steep electrochemical gradients (lowering minimal urine pH to $\sim 4.5$). The basolateral membrane contains the electroneutral anion exchanger-1 (AE1, or Band 3), which exports newly synthesized $\text{HCO}_3^-$ into the peritubular capillary blood in exchange for interstitial chloride ($\text{Cl}^-$).</p>
<p>Conversely, Type B intercalated cells operate during systemic metabolic alkalosis. Their polarity is reversed: an apical $\text{Cl}^-/\text{HCO}_3^-$ exchanger (pendrin) secretes excess bicarbonate into the tubular lumen, while basolateral $\text{H}^+\text{-ATPases}$ extrude protons into the systemic circulation.</p>
<p>Nephrologists evaluated three patients presenting with unexplained metabolic acidosis or electrolyte derangements. Diagnostic blood gas values, urinary electrolytes, and ammonium ($\text{NH}_4^+$) excretion parameters are presented in Table 1.</p>
<table class="tbl">
  <caption>Table 1 Arterial blood gas parameters, serum electrolytes, and urinary findings in study subjects</caption>
  <thead>
    <tr><th>Patient</th><th>Arterial pH</th><th>Serum $[\text{HCO}_3^-]$ (mEq/L)</th><th>Serum Anion Gap (mEq/L)</th><th>Urine pH</th><th>Urinary Anion Gap $(\text{Na}^+ + \text{K}^+ - \text{Cl}^-)$</th><th>Clinical Diagnosis</th></tr>
  </thead>
  <tbody>
    <tr><td>Control</td><td>7.40</td><td>24</td><td>10 (Normal 8&ndash;12)</td><td>5.8</td><td>Negative (&minus;20)</td><td>Eumetabolic</td></tr>
    <tr><td>Patient 1</td><td>7.24</td><td>12</td><td>10 (Normal gap)</td><td>6.8</td><td>Positive (+25)</td><td>Distal RTA (Type 1)</td></tr>
    <tr><td>Patient 2</td><td>7.26</td><td>14</td><td>11 (Normal gap)</td><td>5.0</td><td>Negative (&minus;30)</td><td>Proximal RTA (Type 2)</td></tr>
    <tr><td>Patient 3</td><td>7.22</td><td>10</td><td>26 (High gap)</td><td>4.8</td><td>Negative (&minus;15)</td><td>Diabetic Ketoacidosis (DKA)</td></tr>
  </tbody>
</table>
<p>In Patient 1, genetic sequencing identified a loss-of-function missense mutation in the basolateral AE1 anion exchanger, preventing bicarbonate reabsorption in Type A intercalated cells.</p>"""

p6_qs = [
    {
        "q": "Why is Patient 1 (Distal RTA, Type 1) unable to acidify the urine below pH 6.0 despite severe systemic acidemia (arterial pH 7.24)?",
        "ch": [
            "Proximal tubular reabsorption of sodium bicarbonate is completely blocked by aldosterone deficiency.",
            "Type A intercalated cells fail to actively secrete protons across the apical membrane into the collecting duct lumen.",
            "Glomerular filtration rate drops to zero, precluding fluid delivery to the loop of Henle.",
            "Urinary carbonic anhydrase II hydrolyzes all filtered protons into molecular hydrogen gas."
        ],
        "a": 1,
        "e": "<strong>Pathophysiology of Type 1 (Distal) RTA:</strong> In healthy individuals experiencing systemic acidemia, Type A intercalated cells in the collecting duct maximally pump $\\text{H}^+$ into the urine via apical $\\text{H}^+$-ATPases, lowering urine pH to its physiological minimum ($\sim 4.5$). In Distal RTA (Type 1), the apical proton pumps or basolateral AE1 anion exchangers in Type A cells are defective. Because these cells cannot secrete $\\text{H}^+$ or reabsorb new $\\text{HCO}_3^-$, net acid excretion fails, and the urine remains inappropriately alkaline ($\text{pH} > 5.5$, measured at $6.8$ in Patient 1) despite severe systemic metabolic acidosis.<br><br><em>Distractor Traps:</em><br>&bull; A describes Type 2 (Proximal) RTA (as in Patient 2).<br>&bull; C is false: GFR is maintained in isolated RTA.<br>&bull; D is chemically nonsensical; CA II does not produce hydrogen gas."
    },
    {
        "q": "In Patient 2, who has Proximal RTA (Type 2), why does the urine pH drop to 5.0 when serum bicarbonate is low (14 mEq/L)?",
        "ch": [
            "Distal Type A intercalated cell proton secretion remains intact and acidifies urine once filtered bicarbonate drops below the impaired proximal threshold.",
            "Type B intercalated cells switch their apical pendrin exchangers to pump potassium ions.",
            "Proximal tubule brush border enzymes spontaneously deaminate all filtered amino acids.",
            "Carbonic anhydrase IV is up-regulated in the bladder urothelium to neutralize bicarbonate."
        ],
        "a": 0,
        "e": "<strong>Intact distal acidification in Proximal RTA:</strong> Type 2 (Proximal) RTA is caused by a defect in proximal tubular $\\text{HCO}_3^-$ reabsorption (which normally reabsorbs $\sim 80-90\\%$ of filtered bicarbonate). When serum $\\text{HCO}_3^-$ drops to low levels ($14\\text{ mEq/L}$), the filtered load of $\\text{HCO}_3^-$ matches the reduced proximal reabsorptive capacity, so little bicarbonate escapes to the distal nephron. Because distal Type A intercalated cells possess fully functional $\\text{H}^+$-ATPases, they normally secrete protons and acidify the urine ($\text{urine pH} = 5.0$).<br><br><em>Distractor Traps:</em><br>&bull; B and D invent unphysiological transporter switches and bladder enzyme mechanisms.<br>&bull; C describes generalized proximal Fanconi syndrome without explaining distal acidification."
    },
    {
        "q": "What is the primary cellular mechanism by which Type B intercalated cells respond to systemic metabolic alkalosis?",
        "ch": [
            "Apical H^+-ATPases pump protons into the tubular lumen to acidify the final urine.",
            "Apical pendrin exchangers secrete bicarbonate into the lumen in exchange for chloride.",
            "Basolateral AE1 exchangers pump excess bicarbonate into peritubular capillaries.",
            "Endoplasmic reticulum ribosomes synthesize new carbonic anhydrase II to generate acid."
        ],
        "a": 1,
        "e": "<strong>Type B intercalated cell function:</strong> In systemic metabolic alkalosis, the kidney must eliminate excess base. Type B intercalated cells have the reverse polarity of Type A cells. They express the $\\text{Cl}^-/\\text{HCO}_3^-$ exchanger <i>pendrin</i> on their apical (luminal) membrane, which secretes $\\text{HCO}_3^-$ into the tubular fluid in exchange for luminal $\\text{Cl}^-$, while basolateral $\\text{H}^+$-ATPases pump protons into the interstitial capillary blood to restore normal plasma pH.<br><br><em>Distractor Traps:</em><br>&bull; A and C describe Type A intercalated cells.<br>&bull; D does not address the active bicarbonate secretory mechanism."
    },
    {
        "q": "The urinary anion gap (UAG = [Na^+] + [K^+] - [Cl^-]) is clinically utilized to estimate urinary excretion of which unmeasured cation?",
        "ch": [
            "Calcium (Ca^2+)",
            "Ammonium (NH_4^+)",
            "Magnesium (Mg^2+)",
            "Proton (free H^+)"
        ],
        "a": 1,
        "e": "<strong>Urinary anion gap and ammonium:</strong> The kidney eliminates metabolic acid primarily as ammonium ions ($\\text{NH}_4^+$) paired with chloride ($\\text{Cl}^-$). In metabolic acidosis with intact renal acid excretion (such as diarrhea or DKA), the kidneys ramp up $\\text{NH}_4^+\\text{Cl}^-$ excretion. Because $\\text{Cl}^-$ is measured but $\\text{NH}_4^+$ is an unmeasured cation, high $[\\text{Cl}^-]$ drives the urinary anion gap negative ($[\\text{Na}^+] + [\\text{K}^+] - [\\text{Cl}^-] < 0$, seen in Control, Patient 2, and Patient 3). In distal RTA (Patient 1), failure of $\\text{NH}_4^+$ excretion yields low urinary $[\\text{Cl}^-]$, causing a characteristically positive UAG ($+25\\text{ mEq/L}$).<br><br><em>Distractor Traps:</em><br>&bull; A, C, and D are present in much lower concentrations than ammonium ($\text{NH}_4^+$ is excreted at $30-200\\text{ mEq/day}$). Free $\text{H}^+$ at pH 5 is only $10^{-5}\\text{ M}$ ($0.01\\text{ mEq/L}$)."
    },
    {
        "q": "Which pharmacological agent acts as a reversible inhibitor of carbonic anhydrase in the proximal convoluted tubule, promoting urinary bicarbonate excretion?",
        "ch": [
            "Furosemide",
            "Acetazolamide",
            "Spironolactone",
            "Hydrochlorothiazide"
        ],
        "a": 1,
        "e": "<strong>Carbonic anhydrase inhibitors:</strong> Acetazolamide is a sulfonamide derivative that selectively and reversibly inhibits both luminal (CA IV) and intracellular (CA II) carbonic anhydrase in proximal convoluted tubule cells. This prevents the dehydration of luminal $\\text{H}_2\\text{CO}_3$ into $\\text{CO}_2$ and the intracellular generation of $\\text{H}^+$ and $\\text{HCO}_3^-$, leading to significant bicarbonate wasting in the urine, urine alkalinization, and mild metabolic acidosis (used clinically for altitude sickness and glaucoma).<br><br><em>Distractor Traps:</em><br>&bull; A (Furosemide) inhibits the $\text{Na}^+/\text{K}^+/2\text{Cl}^-$ cotransporter in the thick ascending limb.<br>&bull; C (Spironolactone) is an aldosterone receptor antagonist.<br>&bull; D (Hydrochlorothiazide) inhibits the $\text{Na}^+/\text{Cl}^-$ cotransporter in the distal tubule."
    },
    {
        "q": "Why does Patient 3 (Diabetic Ketoacidosis) exhibit an elevated serum anion gap (26 mEq/L) compared to Patients 1 and 2 (10&ndash;11 mEq/L)?",
        "ch": [
            "Accumulation of unmeasured organic ketoacid anions (acetoacetate and beta-hydroxybutyrate) displaces bicarbonate.",
            "Hyperglycemia directly increases the serum concentration of dissolved univalent chloride ions.",
            "Loss of functional glomeruli leads to retention of positively charged basic amino acids in serum.",
            "Severe dehydration decreases total serum sodium concentration below 100 mEq/L."
        ],
        "a": 0,
        "e": "<strong>Serum anion gap in metabolic acidosis:</strong> The serum anion gap is defined as $\\text{AG} = [\\text{Na}^+] - ([\\text{Cl}^-] + [\\text{HCO}_3^-])$. In normal states ($8-12\\text{ mEq/L}$), the gap represents unmeasured plasma proteins (primarily albumin). In DKA (Patient 3), large quantities of unmeasured organic conjugate base anions&mdash;acetoacetate and $\\beta$-hydroxybutyrate&mdash;accumulate in the bloodstream. For every proton neutralized by bicarbonate (lowering $[\\text{HCO}_3^-]$ to $10\\text{ mEq/L}$), one unmeasured ketoacid anion replaces it, widening the anion gap to $26\\text{ mEq/L}$ (a classic high-anion-gap metabolic acidosis). In contrast, RTAs are normal-gap (hyperchloremic) acidoses.<br><br><em>Distractor Traps:</em><br>&bull; B is false: chloride does not rise in DKA; ketoacid anions rise.<br>&bull; C describes renal failure retention of phosphate/sulfate, not basic amino acids.<br>&bull; D is false: dehydration causes hypernatremia or pseudohyponatremia, not severe true hyponatremia."
    }
]

passages.append({
    "id": "exam_bb90_2_p6",
    "sec": "B/B",
    "topic": "Renal Tubular Acid-Base Transport & Intercalated Cell Dynamics",
    "label": "Biological and Biochemical Foundations of Living Systems",
    "examId": "bb90_2",
    "passage": p6_html,
    "qs": p6_qs
})

print("Passage 6 defined.")

# ==============================================================================
# PASSAGE 7: Major Histocompatibility Complex (MHC) & Antigen Presentation Pathways
# Topics: MHC-I vs MHC-II, CD8+ vs CD4+ T cells, proteasome, TAP transporter, CLIP/HLA-DM
# ==============================================================================
p7_html = r"""<div class="ttl">Passage 7 (Questions 37&ndash;42)</div>
<p>The adaptive immune system discriminates between self and non-self peptides using cell-surface glycoproteins encoded by the Major Histocompatibility Complex (MHC; known in humans as Human Leukocyte Antigens, HLA). MHC molecules display fragmented peptide antigens to T-cell receptors (TCRs) through two distinct, evolutionary specialized antigen-processing pathways: the <i>endogenous (MHC Class I)</i> pathway and the <i>exogenous (MHC Class II)</i> pathway.</p>
<p><b>MHC Class I molecules</b> are expressed on virtually all nucleated cells and present peptides derived from endogenous intracellular proteins (such as viral antigens or mutated tumor neoantigens) to $\text{CD8}^+$ cytotoxic T lymphocytes (CTLs). Intracellular proteins are tagged with polyubiquitin chains and degraded into oligopeptides (8 to 10 amino acids) by the 26S proteasome (or immunoproteasome). The Transporter associated with Antigen Processing (TAP1/TAP2 heterodimer) translocates these peptides into the endoplasmic reticulum (ER) lumen via ATP hydrolysis. Inside the ER, peptides bind to the peptide-binding cleft of the MHC-I heterodimer (composed of a polymorphic $\alpha$ heavy chain and the invariant non-covalently associated $\beta_2$-microglobulin subunit). Stable MHC-I/peptide complexes traffic through the Golgi apparatus to the plasma membrane. Recognition by a mature $\text{CD8}^+$ CTL triggers targeted exocytosis of perforin (forming membrane pores) and granzymes (inducing caspase-dependent apoptosis).</p>
<p><b>MHC Class II molecules</b> are restricted to professional antigen-presenting cells (APCs: dendritic cells, macrophages, and B lymphocytes) and present peptides derived from internalized extracellular pathogens to $\text{CD4}^+$ helper T lymphocytes ($\text{T}_H$ cells). MHC-II heterodimers ($\alpha$ and $\beta$ chains) assemble in the ER bound to the invariant chain (Ii, CD74), which physically blocks the binding groove to prevent premature loading of endogenous ER peptides. The complex is transported to acidic endolysosomal compartments, where endosomal cathepsins degrade the invariant chain, leaving only a small fragment&mdash;the Class II-associated invariant chain peptide (CLIP)&mdash;in the groove. The non-classical chaperone HLA-DM catalyzes the dissociation of CLIP, allowing high-affinity exogenous peptides (13 to 25 amino acids) to bind before the complex is routed to the cell surface.</p>
<p>Immunologists investigated viral immune evasion mechanisms in four human lymphoblastoid cell lines exposed to an intracellular herpesvirus. T-cell activation responses and surface HLA expression were quantified in Table 1.</p>
<table class="tbl">
  <caption>Table 1 Antigen presentation parameters and cytotoxic T-cell responses in infected lymphoblastoid lines</caption>
  <thead>
    <tr><th>Cell Line</th><th>Viral Protein Expressed</th><th>Surface MHC-I Expression (% normal)</th><th>Surface MHC-II Expression (% normal)</th><th>Peptide Translocation into ER</th><th>CD8+ CTL Lysis (%)</th></tr>
  </thead>
  <tbody>
    <tr><td>Wild-Type (Uninfected)</td><td>None</td><td>100%</td><td>100%</td><td>Normal</td><td>2.1%</td></tr>
    <tr><td>Infected Strain A</td><td>Wild-Type Herpesvirus</td><td>12%</td><td>98%</td><td>Completely blocked</td><td>4.5%</td></tr>
    <tr><td>Infected Strain B</td><td>ICP47-Null Mutant Virus</td><td>95%</td><td>100%</td><td>Normal</td><td>78.4%</td></tr>
    <tr><td>Infected Strain C</td><td>US6-Expressing Vector</td><td>8%</td><td>97%</td><td>Completely blocked</td><td>5.1%</td></tr>
  </tbody>
</table>
<p>Viral protein ICP47 binds to the cytosolic peptide-binding site of TAP with high affinity, functioning as a competitive antagonist of peptide translocation.</p>"""

p7_qs = [
    {
        "q": "Why does the herpesvirus protein ICP47 protect infected cells from CD8+ cytotoxic T-cell lysis (Table 1)?",
        "ch": [
            "It selectively hydrolyzes beta-2-microglobulin in the extracellular space.",
            "It competitively inhibits TAP transporter, preventing viral peptides from reaching MHC Class I in the ER.",
            "It acts as a suicide inhibitor of cathepsin proteases inside endolysosomes.",
            "It cross-links CD4 co-receptors to block helper T-cell interleukin-2 release."
        ],
        "a": 1,
        "e": "<strong>Mechanism of ICP47 immune evasion:</strong> As stated in the passage, ICP47 binds to the cytosolic face of the TAP1/TAP2 heterodimer, competitively blocking peptide translocation into the ER lumen. Without peptide loading, MHC Class I $\\alpha$ heavy chains cannot assemble stably with $\\beta_2$-microglobulin and are degraded in the ER. Consequently, surface MHC Class I expression drops to 12% (Strain A), preventing $\\text{CD8}^+$ cytotoxic T-cells from recognizing viral peptides and drastically suppressing CTL lysis (from 78.4% in ICP47-null to 4.5%).<br><br><em>Distractor Traps:</em><br>&bull; A claims extracellular hydrolysis.<br>&bull; C describes an MHC-II endolysosomal process.<br>&bull; D refers to CD4 helper T-cells, whereas CTLs are CD8+."
    },
    {
        "q": "Which molecular component prevents premature binding of endogenous cellular peptides to newly synthesized MHC Class II molecules within the endoplasmic reticulum?",
        "ch": [
            "Beta-2-microglobulin",
            "The invariant chain (Ii, CD74)",
            "Transporter associated with Antigen Processing (TAP)",
            "Ubiquitin ligase E3"
        ],
        "a": 1,
        "e": "<strong>Role of the invariant chain (CD74):</strong> Newly synthesized MHC Class II $\\alpha$ and $\\beta$ chains assemble in the ER. To prevent the binding of abundant endogenous peptides present in the ER lumen (which belong on MHC-I), the invariant chain (CD74) associates with the MHC-II complex, inserting a specific segment (CLIP) into the antigen-binding groove. The invariant chain also targets the complex to endolysosomal vesicles, where it is degraded by cathepsins prior to exogenous peptide loading.<br><br><em>Distractor Traps:</em><br>&bull; A ($\\beta_2$-microglobulin) is the invariant light chain of MHC Class I.<br>&bull; C (TAP) transports peptides into the ER for MHC Class I.<br>&bull; D (Ubiquitin ligase) tags cytosolic proteins for proteasomal degradation."
    },
    {
        "q": "How do CD8 and CD4 co-receptors enforce immunological restriction between T-cell subsets and MHC classes?",
        "ch": [
            "CD8 binds specifically to the invariant alpha-3 domain of MHC Class I, while CD4 binds to the beta-2 domain of MHC Class II.",
            "CD8 binds directly to foreign peptide side chains, while CD4 binds to the surrounding lipid bilayer.",
            "CD8 catalyzes the phosphorylation of extracellular antibodies, while CD4 secretes perforin.",
            "CD8 binds exclusively to carbohydrate residues on MHC Class II, while CD4 binds to MHC Class I."
        ],
        "a": 0,
        "e": "<strong>MHC coreceptor restriction:</strong> The TCR recognizes the polymorphic peptide-MHC interface, while the T-cell co-receptors (CD8 or CD4) bind to invariant domains of the MHC molecule to stabilize the immunological synapse and recruit the intracellular tyrosine kinase Lck. Specifically, CD8 binds to the invariant $\\alpha_3$ domain of MHC Class I molecules, restricting cytotoxic T-cells to MHC-I. CD4 binds to the non-polymorphic $\\beta_2$ domain of MHC Class II molecules, restricting helper T-cells to MHC-II.<br><br><em>Distractor Traps:</em><br>&bull; B is false: the TCR binds the peptide, not the coreceptor.<br>&bull; C invents antibody phosphorylation.<br>&bull; D reverses the coreceptor binding targets."
    },
    {
        "q": "Which enzymatic complex is primarily responsible for generating the 8-to-10 amino acid peptide fragments loaded onto MHC Class I molecules?",
        "ch": [
            "Lysosomal cathepsins B and D",
            "The 26S proteasome (or immunoproteasome)",
            "Endoplasmic reticulum signal peptidase",
            "Extracellular matrix metalloproteinases (MMPs)"
        ],
        "a": 1,
        "e": "<strong>Proteasomal generation of MHC-I epitopes:</strong> In the endogenous pathway, intracellular proteins (viral, tumor, or misfolded self-proteins) are targeted for destruction by polyubiquitination. The cytosolic 26S proteasome (and during inflammation, the interferon-induced immunoproteasome) hydrolyzes peptide bonds to produce short oligopeptides typically 8 to 10 amino acids in length&mdash;the exact length required to fit tightly into the closed-ended peptide binding cleft of MHC Class I.<br><br><em>Distractor Traps:</em><br>&bull; A (Cathepsins) digest proteins in lysosomes for MHC Class II.<br>&bull; C (Signal peptidase) cleaves signal sequences of secretory proteins.<br>&bull; D (MMPs) remodel the extracellular matrix."
    },
    {
        "q": "What is the structural role of the non-classical MHC molecule HLA-DM in the exogenous antigen presentation pathway?",
        "ch": [
            "It acts as a molecular chaperone to catalyze the dissociation of the CLIP fragment from MHC Class II.",
            "It translocates peptides across the outer mitochondrial membrane via ATP hydrolysis.",
            "It directly phosphorylates CD8 co-receptors on the surface of cytotoxic T lymphocytes.",
            "It cleaves polyubiquitin chains from misfolded proteins in the cytosol."
        ],
        "a": 0,
        "e": "<strong>Chaperone function of HLA-DM:</strong> In the endolysosomal compartment, after cathepsins degrade the invariant chain, the remaining CLIP peptide remains lodged in the MHC Class II peptide-binding groove. HLA-DM is an intracellular non-polymorphic MHC-like chaperone that binds to the MHC-II/CLIP complex, inducing a conformational change that promotes the release of CLIP. This empties the groove, allowing high-affinity exogenous antigenic peptides to bind stably before the MHC-II complex is displayed on the cell surface.<br><br><em>Distractor Traps:</em><br>&bull; B describes mitochondrial translocases (TOM/TIM).<br>&bull; C invents CD8 coreceptor phosphorylation.<br>&bull; D describes deubiquitinating enzymes (DUBs)."
    },
    {
        "q": "Natural killer (NK) cells identify and eliminate virally infected cells that down-regulate surface MHC Class I expression via which immunological mechanism?",
        "ch": [
            "Activation of killer inhibitory receptors (KIRs) by high levels of surface MHC Class I",
            "The 'missing-self' response, where absence of MHC Class I relieves inhibition of NK cell cytotoxicity",
            "Direct phagocytosis of infected cells mediated by intracellular complement component C3b",
            "Somatic V(D)J hypermutation generating high-affinity antibodies against viral envelope capsids"
        ],
        "a": 1,
        "e": "<strong>NK cell 'missing-self' recognition:</strong> Natural killer (NK) cells express killer cell immunoglobulin-like receptors (KIRs), which are inhibitory receptors that recognize self MHC Class I molecules. In normal healthy cells, high surface MHC-I engages KIRs, sending an overriding inhibitory signal that prevents NK cell activation. When viruses (like herpesviruses in Table 1) down-regulate MHC Class I to evade $\\text{CD8}^+$ CTLs, the inhibitory signal is lost ('missing self'). Unopposed activating signals trigger NK cell degranulation, killing the infected cell via perforin and granzymes.<br><br><em>Distractor Traps:</em><br>&bull; A describes NK cell inhibition (preventing killing).<br>&bull; C describes macrophage phagocytosis.<br>&bull; D describes B-cell affinity maturation (NK cells do not undergo V(D)J recombination)."
    }
]

passages.append({
    "id": "exam_bb90_2_p7",
    "sec": "B/B",
    "topic": "Major Histocompatibility Complex (MHC) & Antigen Presentation Pathways",
    "label": "Biological and Biochemical Foundations of Living Systems",
    "examId": "bb90_2",
    "passage": p7_html,
    "qs": p7_qs
})

print("Passage 7 defined.")

# ==============================================================================
# DISCRETE QUESTIONS (10 Standalone Questions: 43 to 52)
# Topics: Gluconeogenesis bypass enzymes & F-2,6-BP, MWC vs Koshland allosteric models,
# chromatin remodeling (HATs/HDACs/methylation), Lac operon catabolite repression,
# miRNA vs siRNA RISC, protein separation / isoelectric focusing, microvascular Starling forces,
# sliding filament cross-bridge cycle, endocrine calcium (PTH/Calcitonin/Vit D), HPG axis LH surge
# ==============================================================================
bb_discretes = [
    {
        "q": "Fructose-2,6-bisphosphate (F-2,6-BP) reciprocally regulates glycolysis and gluconeogenesis in hepatocytes. How does an elevated concentration of F-2,6-BP modulate phosphofructokinase-1 (PFK-1) and fructose-1,6-bisphosphatase-1 (FBPase-1)?",
        "ch": [
            "It allosterically inhibits PFK-1 and allosterically activates FBPase-1.",
            "It allosterically activates PFK-1 and allosterically inhibits FBPase-1.",
            "It competitively inhibits both PFK-1 and FBPase-1 at their catalytic active sites.",
            "It promotes the covalent proteolytic degradation of both PFK-1 and FBPase-1."
        ],
        "a": 1,
        "e": "<strong>Reciprocal allosteric regulation by F-2,6-BP:</strong> Fructose-2,6-bisphosphate is the most potent allosteric regulator of hepatic carbohydrate flux. In the fed state, insulin promotes the synthesis of F-2,6-BP (via the PFK-2 domain of PFK-2/FBPase-2). F-2,6-BP strongly activates PFK-1 (overcoming ATP inhibition and accelerating glycolysis) while simultaneously allosterically inhibiting FBPase-1 (shutting down gluconeogenesis). Conversely, in fasting, glucagon reduces [F-2,6-BP], relieving inhibition on FBPase-1 to drive gluconeogenesis.<br><br><em>Distractor Traps:</em><br>&bull; A reverses the regulatory roles.<br>&bull; C describes competitive active site inhibition.<br>&bull; D invents proteolytic degradation."
    },
    {
        "q": "According to the Monod-Wyman-Changeux (MWC, concerted) model of enzyme cooperativity, how does an allosteric activator modulate the equilibrium between the T (tense) and R (relaxed) conformational states?",
        "ch": [
            "It binds sequentially to individual subunits, causing one subunit at a time to change shape.",
            "It binds preferentially to the R-state, shifting the pre-existing equilibrium toward the high-affinity form.",
            "It irreversibly cross-links adjacent polypeptide chains into an inactive oligomer.",
            "It cleaves terminal peptide residues to expose buried substrate-binding pockets."
        ],
        "a": 1,
        "e": "<strong>Concerted (MWC) model of cooperativity:</strong> The MWC (concerted or symmetry) model posits that an allosteric multimeric protein exists in a dynamic equilibrium between two distinct conformational states: an inactive or low-affinity T (tense) state and an active or high-affinity R (relaxed) state, with all subunits maintaining the identical conformation simultaneously. An allosteric activator binds with higher affinity to the R-state conformation, stabilizing it and shifting the entire pre-existing allosteric equilibrium ($T \\rightleftharpoons R$) toward the R-state. The Koshland (sequential) model, by contrast, proposes induced-fit conformational changes subunit by subunit.<br><br><em>Distractor Traps:</em><br>&bull; A describes the Koshland sequential model.<br>&bull; C describes denaturation/cross-linking.<br>&bull; D describes zymogen activation."
    },
    {
        "q": "How does histone acetylation by histone acetyltransferases (HATs) structurally facilitate active gene transcription?",
        "ch": [
            "It adds positive charges to lysine residues, increasing their electrostatic attraction to DNA phosphates.",
            "It neutralizes positive charges on lysine residues, relaxing chromatin into accessible euchromatin.",
            "It methylates cytosine bases in CpG islands to recruit transcriptional repressors.",
            "It hydrolyzes the phosphodiester backbone of linker DNA to release intact nucleosomes."
        ],
        "a": 1,
        "e": "<strong>Mechanism of histone acetylation:</strong> Histone octamers are rich in positively charged basic amino acids (lysine and arginine), which form tight electrostatic interactions with the negatively charged phosphodiester backbone of DNA. Histone acetyltransferases (HATs) transfer acetyl groups from acetyl-CoA to the $\\epsilon$-amino groups of lysine side chains. Acetylation converts positively charged ammonium groups ($-\\text{NH}_3^+$) into neutral amides ($-\\text{NH}-\\text{CO}-\\text{CH}_3$). Neutralizing this positive charge weakens histone-DNA electrostatic attraction, decondensing the 30-nm chromatin fiber into open, transcriptionally accessible euchromatin ('beads on a string').<br><br><em>Distractor Traps:</em><br>&bull; A claims acetylation adds positive charge (it neutralizes it).<br>&bull; C describes DNA methylation (DNMTs), which silences transcription.<br>&bull; D describes endonuclease cleavage."
    },
    {
        "q": "In Escherichia coli, under what environmental nutrient conditions is the lac operon transcribed at its maximal level?",
        "ch": [
            "High glucose and high lactose",
            "High glucose and low lactose",
            "Low glucose and high lactose",
            "Low glucose and low lactose"
        ],
        "a": 2,
        "e": "<strong>Dual regulation of the lac operon:</strong> Maximal transcription of the <i>lac</i> operon requires two simultaneous conditions: (1) Absence of glucose: Low glucose causes adenylate cyclase to produce high cAMP, which binds the Catabolite Activator Protein (CAP). The active CAP-cAMP complex binds the CAP site upstream of the promoter, recruiting RNA polymerase. (2) Presence of lactose: Lactose is converted to allolactose, which binds the Lac repressor (LacI), causing it to dissociate from the operator. Both conditions must be met: low glucose (positive activation via CAP-cAMP) and high lactose (derepression via allolactose removal of LacI).<br><br><em>Distractor Traps:</em><br>&bull; A has catabolite repression (low cAMP, CAP inactive).<br>&bull; B has both catabolite repression and active Lac repressor bound.<br>&bull; D has active Lac repressor bound to operator."
    },
    {
        "q": "What is the primary mechanistic difference between small interfering RNAs (siRNAs) and microRNAs (miRNAs) during eukaryotic RNA interference (RNAi)?",
        "ch": [
            "siRNAs are single-stranded peptides, whereas miRNAs are double-stranded DNA oligonucleotides.",
            "siRNAs typically exhibit complete complementarity to their target mRNA causing endonucleolytic cleavage, whereas miRNAs usually exhibit partial complementarity leading to translational repression.",
            "siRNAs function exclusively inside the mitochondrial matrix, whereas miRNAs function in the nucleus.",
            "siRNAs are synthesized by RNA polymerase I, whereas miRNAs are transcribed by DNA polymerase alpha."
        ],
        "a": 1,
        "e": "<strong>siRNA vs miRNA mechanisms:</strong> Both siRNAs and miRNAs are short non-coding regulatory RNAs (21&ndash;23 nucleotides) loaded into the RNA-Induced Silencing Complex (RISC) containing an Argonaute protein. siRNAs are typically exogenous or synthetic double-stranded RNAs that possess 100% perfect sequence complementarity to a specific target mRNA; Argonaute-2 directly cleaves the target mRNA phosphodiester backbone (endonucleolytic slicing). In contrast, endogenous miRNAs typically match their target mRNAs (primarily in the 3' UTR) with partial complementarity (exact matching only in the 2&ndash;8 nucleotide 'seed' region), leading to translation inhibition, deadenylation, and mRNA decay.<br><br><em>Distractor Traps:</em><br>&bull; A confuses RNAs with peptides/DNA.<br>&bull; C and D state incorrect subcellular localization and polymerases."
    },
    {
        "q": "In an isoelectric focusing (IEF) gel with a stable pH gradient ranging from pH 3.0 at the anode to pH 10.0 at the cathode, an electric field is applied. Where will a protein with an isoelectric point of pI = 6.5 come to rest?",
        "ch": [
            "At the anode, because it maintains a net positive charge throughout migration",
            "At the cathode, because it maintains a net negative charge throughout migration",
            "At the region where the local gel pH equals 6.5, where its net electrical charge becomes zero",
            "It will migrate continuously back and forth between the electrodes without stopping"
        ],
        "a": 2,
        "e": "<strong>Principles of isoelectric focusing:</strong> In IEF, a stable pH gradient is established with low pH at the positive anode ($+$) and high pH at the negative cathode ($-$). When a protein is placed in a region where $\\text{pH} < pI$, it is protonated and carries a net positive charge, migrating toward the cathode. When it is in a region where $\\text{pH} > pI$, it is deprotonated and carries a net negative charge, migrating toward the anode. As soon as the protein enters the zone where the local $\\text{pH} = pI$ (6.5), its net electrical charge becomes identically zero ($q = 0$). Because electrical force is $F = qE$, the net driving force ceases, and the protein stops migrating, focusing into a sharp band.<br><br><em>Distractor Traps:</em><br>&bull; A and B assume the charge never changes.<br>&bull; D ignores the loss of net charge at the isoelectric point."
    },
    {
        "q": "In systemic arterial hypertension, which perturbation in microvascular Starling forces directly promotes the pathological development of peripheral tissue edema?",
        "ch": [
            "A decrease in capillary hydrostatic pressure (P_c)",
            "An increase in capillary hydrostatic pressure (P_c)",
            "An increase in plasma colloid oncotic pressure (pi_c)",
            "A decrease in interstitial fluid hydrostatic pressure (P_i)"
        ],
        "a": 1,
        "e": "<strong>Starling forces and edema:</strong> Net fluid filtration across a capillary wall is governed by Starling's equation: $J_v = K_f [(P_c - P_i) - \sigma (\pi_c - \pi_i)]$. Capillary hydrostatic pressure ($P_c$) drives fluid out of the vascular lumen into the interstitial space. In severe hypertension or venous congestion, elevated intravascular pressure increases capillary hydrostatic pressure ($P_c$). When the rate of microvascular fluid filtration exceeds the drainage capacity of lymphatic vessels, excess fluid accumulates in the interstitium, causing peripheral edema.<br><br><em>Distractor Traps:</em><br>&bull; A would favor fluid reabsorption.<br>&bull; C (increased $\pi_c$) pulls fluid into the capillary, preventing edema.<br>&bull; D is a minor consequence, not the primary hypertensive driving force."
    },
    {
        "q": "During the cross-bridge cycle of skeletal muscle contraction, what immediate biochemical event causes the myosin head to detach from the actin thin filament?",
        "ch": [
            "Hydrolysis of ATP into ADP and inorganic phosphate",
            "Binding of a new molecule of ATP to the myosin nucleotide-binding pocket",
            "Dissociation of calcium ions from troponin C",
            "Release of inorganic phosphate (P_i) from the myosin head"
        ],
        "a": 1,
        "e": "<strong>Cross-bridge cycle detachment mechanism:</strong> At the end of the power stroke, the myosin head remains tightly locked to the actin filament in a low-energy state (the rigor conformation). Detachment of the myosin head from actin strictly requires the binding of a new molecule of ATP to the nucleotide-binding site on the myosin head. ATP binding induces an allosteric conformational shift that dramatically decreases myosin's affinity for actin, causing immediate dissociation. (In death, lack of ATP prevents detachment, resulting in rigor mortis). Hydrolysis of ATP into $\text{ADP} + \text{P}_i$ then 'cocks' the head into the high-energy state.<br><br><em>Distractor Traps:</em><br>&bull; A causes cocking of the myosin head, not detachment.<br>&bull; C causes tropomyosin to block actin binding sites during relaxation.<br>&bull; D triggers the power stroke itself."
    },
    {
        "q": "How does parathyroid hormone (PTH) act on bone and renal tubules to restore extracellular ionized calcium levels during hypocalcemia?",
        "ch": [
            "It stimulates osteoblast mineralization and increases renal calcium excretion in urine.",
            "It stimulates osteoclast bone resorption and increases renal distal tubular calcium reabsorption while promoting 1-alpha-hydroxylase activity.",
            "It directly activates calcitonin release from thyroid parafollicular cells.",
            "It inhibits intestinal calcium absorption by degrading calcitriol."
        ],
        "a": 1,
        "e": "<strong>Parathyroid hormone physiological actions:</strong> Released by chief cells in response to low serum ionized calcium ($[\text{Ca}^{2+}]$), PTH acts through three coordinated mechanisms: (1) In bone, it binds osteoblasts, up-regulating RANKL to stimulate osteoclastogenesis and bone resorption, releasing $\text{Ca}^{2+}$ and phosphate into plasma. (2) In kidneys, it increases $\text{Ca}^{2+}$ reabsorption in the distal convoluted tubule while inhibiting proximal phosphate reabsorption (causing phosphaturia). (3) In the proximal tubule, it induces $1\alpha$-hydroxylase (CYP27B1), converting 25-hydroxyvitamin D into active 1,25-dihydroxyvitamin D (calcitriol), which enhances dietary calcium absorption in the gut.<br><br><em>Distractor Traps:</em><br>&bull; A describes calcitonin-like mineralization.<br>&bull; C is false: calcitonin lowers blood calcium and is stimulated by hypercalcemia.<br>&bull; D states the exact opposite of PTH's effect on calcitriol."
    },
    {
        "q": "During the late follicular phase of the human menstrual cycle, what endocrine phenomenon triggers the massive luteinizing hormone (LH) surge that induces ovulation?",
        "ch": [
            "Progesterone drops to undetectable levels, releasing pituitary gonadotropes from tonic inhibition.",
            "Sustained high plasma concentrations of estradiol switch feedback on the anterior pituitary and hypothalamus from negative to positive.",
            "Human chorionic gonadotropin (hCG) is secreted by the unfertilized secondary oocyte.",
            "Inhibin B directly stimulates hypothalamic GnRH pulsatile release into portal vessels."
        ],
        "a": 1,
        "e": "<strong>The mid-cycle LH surge mechanism:</strong> Throughout most of the follicular phase, moderate levels of estrogen exert negative feedback on gonadotropin-releasing hormone (GnRH) and LH/FSH secretion. However, as the dominant Graafian follicle matures, its granulosa cells secrete escalating quantities of estradiol. When plasma estradiol concentrations exceed a critical threshold ($\sim 200\text{ pg/mL}$) for approximately 36 to 48 hours, estrogen paradoxically switches its feedback mechanism from negative to positive. This positive feedback triggers a dramatic release of GnRH and sensitization of pituitary gonadotropes, causing the massive mid-cycle LH surge that initiates follicular rupture and ovulation.<br><br><em>Distractor Traps:</em><br>&bull; A is false: progesterone rises <i>after</i> ovulation during the luteal phase.<br>&bull; C describes syncytiotrophoblasts after implantation.<br>&bull; D is false: inhibin B selectively suppresses pituitary FSH secretion."
    }
]

passages.append({
    "id": "exam_bb90_2_disc",
    "sec": "B/B",
    "topic": "B/B Standalone Discrete Questions",
    "sheet": None,
    "label": "Biological and Biochemical Foundations of Living Systems",
    "examId": "bb90_2",
    "passage": "",
    "qs": bb_discretes
})

print("Discretes defined.")

total_qs = sum(len(p["qs"]) for p in passages)
print(f"Total B/B Exam 2 questions: {total_qs}")

# Write to exam_bb90_2.js
js_content = "/* ---- exam_bb90_2.js ---- */\n/* Full 90-minute Bio/Biochem Practice Exam 2: 7 passages (42 Qs) + 10 discrete Qs = 52 Qs */\nconst EXAM_BB90_2 = " + json.dumps(passages, indent=2) + ";\n"
with open("/home/cgslinde/DrillRoom/DrillRoom/exam_bb90_2.js", "w") as f:
    f.write(js_content)

print("exam_bb90_2.js written successfully!")
