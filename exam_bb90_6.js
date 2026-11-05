/* ---- exam_bb90_6.js ---- */
/* Full 90-minute Biochem/Bio Practice Exam 6: 7 passages (42 Qs) + 10 discrete Qs = 52 Qs */
const EXAM_BB90_6 = [
  {
    "id": "exam_bb90_6_p1",
    "sec": "B/B",
    "topic": "Lipoprotein Classification & Apolipoprotein Functions (Chylomicrons, VLDL, LDL, HDL)",
    "sheet": 1,
    "label": "Biological and Biochemical Foundations of Living Systems",
    "examId": "bb90_6",
    "passage": "<div class=\"ttl\">Passage 1 (Questions 1&ndash;6)</div>\n<p>Because hydrophobic lipids cannot circulate freely in aqueous blood plasma, they are packaged into macromolecular pseudo-spherical complexes termed lipoproteins. Each lipoprotein consists of an amphipathic surface monolayer containing unesterified cholesterol, phospholipids, and specialized structural and regulatory proteins known as apolipoproteins, surrounding a hydrophobic core composed of triacylglycerols (TAGs) and cholesteryl esters (CEs). Lipoproteins are classified according to their hydrated density into chylomicrons, very-low-density lipoproteins (VLDL), intermediate-density lipoproteins (IDL), low-density lipoproteins (LDL), and high-density lipoproteins (HDL). Density is inversely proportional to lipid content and directly proportional to protein percentage.</p>\n<p>Apolipoproteins mediate receptor recognition and activate critical intravascular enzymes. Dietary TAGs and cholesterol absorbed by enterocytes are assembled into nascent chylomicrons containing apolipoprotein B-48 (ApoB-48), generated via post-transcriptional mRNA editing of the <em>APOB</em> transcript by the cytidine deaminase APOBEC-1. Upon entering the systemic circulation via the thoracic duct, chylomicrons acquire ApoC-II and ApoE from circulating HDL. ApoC-II is an obligatory allosteric cofactor for lipoprotein lipase (LPL) anchored to the capillary endothelium of adipose tissue and striated muscle, which hydrolyzes core TAGs into free fatty acids and glycerol. Chylomicron remnants, enriched in CEs, are subsequently cleared by hepatic low-density lipoprotein receptor-related protein 1 (LRP1) through high-affinity binding to ApoE.</p>\n<p>Investigators isolated plasma lipoproteins from a cohort of patients presenting with severe dyslipidemia. Lipoprotein fractions were separated by preparative ultracentrifugation and analyzed for lipid-to-protein ratios, apolipoprotein profiles, and LPL activation kinetics (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Biophysical characteristics, apolipoprotein composition, and LPL activation across lipoprotein fractions</caption>\n  <thead>\n    <tr><th>Lipoprotein Fraction</th><th>Density (g/mL)</th><th>Core Composition (% TAG / % CE)</th><th>Primary Structural Apolipoprotein</th><th>Regulatory Cofactor Apolipoprotein</th><th>Relative LPL Activation ($V_{max}$, %)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Chylomicron</td><td>< 0.950</td><td>85% TAG / 5% CE</td><td>ApoB-48</td><td>ApoC-II</td><td>100.0%</td></tr>\n    <tr><td>VLDL</td><td>0.950&ndash;1.006</td><td>55% TAG / 20% CE</td><td>ApoB-100</td><td>ApoC-II</td><td>78.4%</td></tr>\n    <tr><td>IDL</td><td>1.006&ndash;1.019</td><td>25% TAG / 35% CE</td><td>ApoB-100</td><td>ApoE</td><td>14.2%</td></tr>\n    <tr><td>LDL</td><td>1.019&ndash;1.063</td><td>8% TAG / 50% CE</td><td>ApoB-100</td><td>None</td><td>< 1.0%</td></tr>\n    <tr><td>HDL</td><td>1.063&ndash;1.210</td><td>5% TAG / 40% CE</td><td>ApoA-I</td><td>ApoC-II / ApoE (reservoir)</td><td>N/A (inhibitory)</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "Which molecular mechanism explains why intestinal enterocytes produce ApoB-48, whereas hepatocytes synthesize full-length ApoB-100 from the identical APOB gene?",
        "ch": [
          "Tissue-specific mRNA cytidine deamination introducing a premature stop codon",
          "Alternative pre-mRNA splicing excluding thirty consecutive internal exons",
          "Differential promoter methylation silencing the C-terminal transcription unit",
          "Post-translational proteolytic cleavage of full ApoB-100 in secretory vesicles"
        ],
        "a": 0,
        "e": "<strong>Molecular mechanism of ApoB-48 generation:</strong> In human enterocytes, the enzyme APOBEC-1 (apolipoprotein B mRNA editing enzyme, catalytic polypeptide 1) deaminates a specific cytidine residue at nucleotide 6666 of the <em>APOB</em> transcript into a uridine (C-to-U editing). This transformation alters a glutamine codon (CAA) into an in-frame stop codon (UAA). Translation termination results in a truncated protein containing exactly the N-terminal $48\\%$ of the sequence (ApoB-48). In hepatocytes, where APOBEC-1 is not expressed, the transcript remains unedited, directing the synthesis of full-length ApoB-100 ($4536\\text{ amino acids}$).<br><br><em>Distractor Traps:</em><br>&bull; B is incorrect because ApoB-48 is produced by post-transcriptional single-base mRNA editing, not alternative splicing.<br>&bull; C is incorrect because DNA promoter methylation regulates transcriptional initiation rate, not transcript truncation.<br>&bull; D is incorrect because ApoB-48 is translated directly from the edited mRNA, not generated by post-translational protease cleavage."
      },
      {
        "q": "A pediatric patient presents with massive eruptive xanthomas, lipemia retinalis, and fasting plasma triacylglycerol levels exceeding 2,500 mg/dL. Genetic sequencing reveals a homozygous loss-of-function mutation in APOC2. Which enzymatic step is directly blocked in this patient?",
        "ch": [
          "Lysosomal degradation of endocytosed LDL particles by acid lipase",
          "Hydrolysis of core triacylglycerols in chylomicrons and VLDL by LPL",
          "Hepatic esterification of free cholesterol by acyl-CoA cholesterol transferase",
          "Microsomal triacylglycerol transfer protein mediated assembly of VLDL"
        ],
        "a": 1,
        "e": "<strong>ApoC-II function in familial chylomicronemia:</strong> ApoC-II functions as the essential obligate allosteric activator of lipoprotein lipase (LPL) on capillary endothelial surfaces. In the absence of functional ApoC-II, LPL cannot hydrolyze core triacylglycerols in circulating chylomicrons and VLDL. Consequently, chylomicrons accumulate massively in plasma (Type Ib hyperlipoproteinemia), giving the serum a creamy lactescent appearance and predisposing the child to recurrent acute pancreatitis.<br><br><em>Distractor Traps:</em><br>&bull; A describes Wolman disease or cholesteryl ester storage disease caused by lysosomal acid lipase (LIPA) deficiency.<br>&bull; C describes ACAT inhibition, which impairs intracellular cholesterol esterification.<br>&bull; D describes abetalipoproteinemia caused by MTTP loss-of-function, which prevents lipoprotein secretion and causes hypolipidemia."
      },
      {
        "q": "Based on the density gradient in Table 1, why do high-density lipoproteins (HDL) possess the highest buoyant density (1.063 to 1.210 g/mL) among all lipoprotein classes?",
        "ch": [
          "HDL contains heavy calcium phosphate crystal deposits within its lipid core",
          "HDL contains saturated fatty acids with an unusually high atomic packing density",
          "HDL possesses the highest protein-to-lipid ratio among all lipoprotein classes",
          "HDL actively excludes neutral cholesteryl esters from its central core matrix"
        ],
        "a": 2,
        "e": "<strong>Determinants of lipoprotein buoyant density:</strong> The density of biological macromolecules is determined by their chemical composition: proteins have a relatively high density ($\\approx 1.35\\text{ g/mL}$), whereas neutral lipids (TAGs and cholesteryl esters) have a low density ($\\approx 0.90\\text{ to }0.93\\text{ g/mL}$). HDL particles are approximately $50\\%$ protein by dry mass (primarily ApoA-I and ApoA-II), giving them the highest protein-to-lipid ratio and consequently the greatest buoyant density ($1.063\\text{ to }1.210\\text{ g/mL}$) during ultracentrifugation.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because lipoproteins do not contain calcium phosphate crystals.<br>&bull; B is incorrect because fatty acid chain packing has a minor effect compared to the vast density contrast between proteins and lipids.<br>&bull; D is incorrect because mature HDL core is heavily enriched in cholesteryl esters ($40\\%$)."
      },
      {
        "q": "Which apolipoprotein acts as the primary high-affinity ligand mediating hepatic receptor-mediated clearance of chylomicron remnants and IDL particles?",
        "ch": [
          "Apolipoprotein A-I",
          "Apolipoprotein B-48",
          "Apolipoprotein C-III",
          "Apolipoprotein E"
        ],
        "a": 3,
        "e": "<strong>Receptor-mediated clearance via Apolipoprotein E:</strong> Chylomicron remnants and intermediate-density lipoproteins (IDL) are cleared from plasma primarily by hepatocytes expressing the LDL receptor and low-density lipoprotein receptor-related protein 1 (LRP1). Both receptors recognize and bind with high affinity to Apolipoprotein E (ApoE) present on the remnant surface. Mutations in ApoE (such as the ApoE2/E2 genotype) impair remnant binding, causing Type III hyperlipoproteinemia (dysbetalipoproteinemia).<br><br><em>Distractor Traps:</em><br>&bull; A is the structural protein of HDL that activates LCAT, not a remnant clearance ligand.<br>&bull; B lacks the C-terminal receptor-binding domain of ApoB-100 and cannot bind the LDL receptor.<br>&bull; C is an inhibitor of LPL and remnant uptake, not a clearance-promoting ligand."
      },
      {
        "q": "In the transition from VLDL to IDL and ultimately to LDL, what fundamental compositional shift occurs in the hydrophobic core of the particle?",
        "ch": [
          "Phospholipids are actively transferred from the surface into the interior core",
          "Unesterified cholesterol is completely converted into water-soluble bile acids",
          "Triacylglycerols are depleted by LPL, leaving a core enriched in cholesteryl esters",
          "Apolipoproteins are internalized into the core to replace neutral storage lipids"
        ],
        "a": 2,
        "e": "<strong>Core lipid remodeling in the VLDL-IDL-LDL cascade:</strong> Nascent VLDL secreted by the liver is rich in triacylglycerols ($55\\%$ TAG, $20\\%$ CE). As VLDL circulates through capillary beds, LPL progressively hydrolyzes its core triacylglycerols into free fatty acids and glycerol. As TAGs are depleted, the particle shrinks into intermediate-density lipoprotein (IDL, $25\\%$ TAG, $35\\%$ CE). Further TAG removal by hepatic lipase yields LDL, whose core is composed predominantly of cholesteryl esters ($50\\%$ CE, $8\\%$ TAG).<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because polar amphipathic phospholipids remain strictly on the outer surface monolayer.<br>&bull; B is incorrect because bile acid synthesis occurs exclusively within hepatocytes, not inside circulating lipoproteins.<br>&bull; D is incorrect because amphipathic apolipoproteins reside on the particle surface to interface with aqueous plasma."
      },
      {
        "q": "If an endocytosis inhibitor prevents hepatic uptake of LDL particles, what phenotypic change in peripheral tissue cholesterol homeostasis will occur?",
        "ch": [
          "Severe depletion of cellular cholesterol and compensatory upregulation of SREBP-2",
          "Complete cessation of endogenous de novo cellular cholesterol biosynthesis",
          "Extensive accumulation of cholesteryl esters in peripheral cell lysosomes",
          "Elevation of circulating plasma LDL-cholesterol with prolonged particle half-life"
        ],
        "a": 3,
        "e": "<strong>Consequences of impaired hepatic LDL clearance:</strong> The liver expresses approximately $70\\%$ of all systemic LDL receptors. If hepatic LDL endocytosis is blocked (as occurs in Familial Hypercholesterolemia or PCSK9 overexpression), LDL particles cannot be cleared from the bloodstream. This leads to a severe increase in circulating plasma LDL-cholesterol levels and extends the plasma half-life of LDL from normal ($2.5\\text{ days}$) to $> 4.5\\text{ days}$, driving atherogenesis.<br><br><em>Distractor Traps:</em><br>&bull; A describes the intracellular response of cells that rely entirely on receptor uptake when denied cholesterol, but systemic plasma phenotype is dramatic hypercholesterolemia.<br>&bull; B is incorrect because when extracellular uptake is blocked, cells upregulate de novo synthesis via HMG-CoA reductase.<br>&bull; C is incorrect because LDL cannot enter lysosomes if endocytosis is blocked."
      }
    ]
  },
  {
    "id": "exam_bb90_6_p2",
    "sec": "B/B",
    "topic": "Reverse Cholesterol Transport & High-Density Lipoproteins (HDL)",
    "sheet": 2,
    "label": "Biological and Biochemical Foundations of Living Systems",
    "examId": "bb90_6",
    "passage": "<div class=\"ttl\">Passage 2 (Questions 7&ndash;12)</div>\n<p>Reverse cholesterol transport (RCT) is an anti-atherogenic physiological pathway wherein excess unesterified cholesterol is extracted from peripheral tissues&mdash;particularly lipid-laden arterial wall macrophages (foam cells)&mdash;and transported via high-density lipoproteins (HDL) to the liver for biliary secretion or conversion into bile salts. The initial committed step involves the interaction of lipid-poor apolipoprotein A-I (ApoA-I), synthesized by the liver and small intestine, with the ATP-binding cassette transporter A1 (ABCA1) located on the plasma membrane of peripheral cells. ABCA1 utilizes the free energy of ATP hydrolysis to translocate unesterified free cholesterol (FC) and phosphatidylcholine to extracellular ApoA-I, generating discoidal nascent pre-$\\beta$-HDL.</p>\n<p>To establish a continuous sink gradient for peripheral cholesterol efflux, nascent HDL must sequester free cholesterol within its hydrophobic interior. This is catalyzed by lecithin-cholesterol acyltransferase (LCAT), a plasma enzyme synthesized by hepatocytes and activated allosterically by ApoA-I. LCAT transfers a fatty acyl group from the $sn$-2 position of phosphatidylcholine (lecithin) to the 3-beta-hydroxyl group of free cholesterol, generating cholesteryl ester (CE) and lyso-phosphatidylcholine. The nonpolar CE partitions into the interior core, transforming the disc into a spherical, mature $\\alpha$-HDL particle (HDL$_3$, which expands into HDL$_2$).</p>\n<p>In human plasma, cholesteryl ester transfer protein (CETP) facilitates a neutral lipid exchange, transferring CEs from mature HDL to ApoB-containing lipoproteins (VLDL and LDL) in exchange for TAGs. Alternatively, HDL-CEs are delivered directly to hepatocytes via scavenger receptor class B type I (SR-BI) without whole-particle endocytic degradation (selective lipid uptake). Clinical biochemists analyzed cholesterol efflux and LCAT esterification kinetics in healthy controls and patients harboring genetic mutations in key RCT proteins (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Reverse cholesterol transport metrics across genetic patient cohorts</caption>\n  <thead>\n    <tr><th>Patient Cohort</th><th>Genetic Defect</th><th>Plasma HDL-C (mg/dL)</th><th>Macrophage ABCA1 Efflux (% of Control)</th><th>LCAT Activity (% of Control)</th><th>Atherosclerosis Phenotype</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Control</td><td>None (Wild-Type)</td><td>52.4 &plusmn; 3.2</td><td>100.0%</td><td>100.0%</td><td>Low Cardiovascular Risk</td></tr>\n    <tr><td>Tangier Disease</td><td>Homozygous <em>ABCA1</em> Null</td><td>1.8 &plusmn; 0.4</td><td>4.2%</td><td>18.5%</td><td>Severe Premature CAD / Hepatosplenomegaly</td></tr>\n    <tr><td>Norum Disease</td><td>Homozygous <em>LCAT</em> Null</td><td>6.5 &plusmn; 1.1</td><td>88.6%</td><td>< 1.0%</td><td>Corneal Opacities / Renal Failure</td></tr>\n    <tr><td>CETP Deficiency</td><td>Homozygous <em>CETP</em> Loss</td><td>118.2 &plusmn; 8.6</td><td>105.4%</td><td>112.0%</td><td>Markedly Elevated Large HDL / Normal Lifespan</td></tr>\n    <tr><td>SR-BI Variant</td><td>Heterozygous <em>SCARB1</em> P376L</td><td>88.5 &plusmn; 5.4</td><td>98.2%</td><td>95.4%</td><td>Elevated HDL-C but Increased CAD Risk</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "Why does homozygous loss of the ABCA1 transporter in Tangier disease patients lead to near-complete absence of circulating plasma HDL-cholesterol (< 2 mg/dL)?",
        "ch": [
          "Lipid-poor ApoA-I cannot acquire phospholipids and cholesterol, undergoing rapid renal catabolism",
          "Hepatic transcription of the APOA1 structural gene is completely repressed by unesterified sterols",
          "Macrophage apoptosis releases endonucleases that degrade circulating mature HDL particles",
          "CETP activity accelerates by 100-fold, transferring all HDL cholesterol into chylomicrons"
        ],
        "a": 0,
        "e": "<strong>Pathophysiology of Tangier disease (ABCA1 deficiency):</strong> ABCA1 is the obligatory lipid translocase that lipolyzes newly secreted, lipid-poor ApoA-I with cellular phospholipids and unesterified cholesterol to generate nascent discoidal pre-$\\beta$-HDL. When ABCA1 is nonfunctional, ApoA-I fails to acquire lipids. Naked, lipid-free ApoA-I is unstable in plasma and is rapidly filtered across the renal glomerular basement membrane and catabolized by proximal tubular epithelial cells. As a result, mature HDL cannot form, causing plasma HDL-C to plummet below $2\\text{ mg/dL}$ and trapping cholesterol in peripheral tissues.<br><br><em>Distractor Traps:</em><br>&bull; B is incorrect because hepatic and intestinal synthesis of ApoA-I protein is normal in Tangier disease; the protein is degraded after secretion.<br>&bull; C is nonsensical because apoptosis does not release systemic HDL-destroying endonucleases.<br>&bull; D is incorrect because CETP requires mature spherical HDL as a substrate; it cannot act on nonexistent particles."
      },
      {
        "q": "What specific chemical transformation does lecithin-cholesterol acyltransferase (LCAT) catalyze to convert discoidal nascent HDL into mature spherical alpha-HDL?",
        "ch": [
          "Enzymatic phosphorylation of the 3-beta-hydroxyl group of cholesterol using cytosolic ATP",
          "Transesterification of a fatty acid from phosphatidylcholine to cholesterol, yielding cholesteryl ester",
          "Oxidative cleavage of the cholesterol aliphatic hydrocarbon side chain, yielding pregnenolone",
          "Hydrolysis of storage cholesteryl esters into free unesterified cholesterol and free fatty acids"
        ],
        "a": 1,
        "e": "<strong>LCAT catalytic mechanism:</strong> LCAT binds to nascent HDL discs and is allosterically activated by ApoA-I. It cleaves the fatty acyl chain from the $sn$-2 position of phosphatidylcholine (lecithin) and transfers it onto the 3-$\\beta$-hydroxyl group of unesterified free cholesterol. This reaction yields two products: a highly hydrophobic cholesteryl ester (CE) and water-soluble lyso-phosphatidylcholine. Because CEs are completely insoluble in aqueous environments, they partition into the interior core of the disc, pulling the bilayer into a spherical core (mature $\\alpha$-HDL).<br><br><em>Distractor Traps:</em><br>&bull; A describes a kinase reaction; cholesterol is not phosphorylated in lipoproteins.<br>&bull; C describes the reaction catalyzed by mitochondrial cytochrome P450scc (CYP11A1) in steroidogenesis.<br>&bull; D describes cholesteryl ester hydrolase (CEH), which acts in the reverse direction."
      },
      {
        "q": "How does the pharmacological inhibition of CETP affect circulating lipoprotein concentrations in human patients?",
        "ch": [
          "It causes profound hypertriglyceridemia by inhibiting endothelial lipoprotein lipase",
          "It lowers plasma HDL-cholesterol while sharply elevating circulating VLDL remnants",
          "It raises plasma HDL-cholesterol levels by preventing transfer of cholesteryl esters to VLDL and LDL",
          "It prevents the cellular uptake of chylomicron remnants by hepatic LRP1 receptors"
        ],
        "a": 2,
        "e": "<strong>Effect of CETP inhibition on lipoprotein profiles:</strong> Cholesteryl ester transfer protein (CETP) mediates the hetero-exchange of cholesteryl esters from HDL to ApoB-containing particles (VLDL and LDL) in exchange for triacylglycerols. Inhibiting CETP (or in genetic CETP deficiency, Table 1) traps cholesteryl esters within HDL particles, markedly elevating plasma HDL-cholesterol (often $> 100\\text{ mg/dL}$) while moderately reducing circulating LDL-cholesterol.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because CETP does not inhibit LPL.<br>&bull; B is the opposite of the observed effect; CETP inhibition elevates HDL-C, not lowers it.<br>&bull; D is incorrect because LRP1 recognizes ApoE on remnants, an interaction independent of CETP activity."
      },
      {
        "q": "In Table 1, patients with the SCARB1 P376L variant exhibit elevated plasma HDL-C (88.5 mg/dL) yet suffer from increased coronary artery disease risk. What explains this apparent paradox?",
        "ch": [
          "Elevated HDL particles undergo spontaneous fusion to form occlusive arterial thrombi",
          "HDL particles in these patients are completely depleted of all apolipoprotein A-I",
          "The variant activates endothelial nitric oxide synthase, causing profound hypotension",
          "Defective SR-BI impairs hepatic selective uptake, preventing final cholesterol excretion"
        ],
        "a": 3,
        "e": "<strong>Dysfunctional HDL and SR-BI mediated selective uptake:</strong> Scavenger receptor class B type I (SR-BI) mediates the selective uptake of cholesteryl esters from circulating HDL into hepatocytes without internalizing or degrading the HDL protein scaffold. The P376L mutation renders SR-BI nonfunctional. Although HDL-cholesterol accumulates in plasma (yielding high static HDL-C levels), the reverse cholesterol transport pathway is blocked at the final hepatic delivery step. Cholesterol cannot be cleared into bile, leaving peripheral tissues overloaded and paradoxically increasing atherosclerosis risk.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because HDL particles do not aggregate into mechanical thrombi.<br>&bull; B is incorrect because SR-BI mutations do not prevent ApoA-I incorporation.<br>&bull; C is incorrect because hypotension does not cause coronary atheroma plaque formation."
      },
      {
        "q": "Which active transport mechanism directly provides the driving force for macrophage cholesterol efflux to lipid-poor ApoA-I?",
        "ch": [
          "ATP-binding cassette transporter A1 (ABCA1) primary active transport",
          "Secondary active symport driven by the sodium electrochemical potential gradient",
          "Facilitated diffusion through voltage-gated potassium ion channels",
          "Receptor-mediated endocytosis of extracellular ApoA-I via clathrin-coated pits"
        ],
        "a": 0,
        "e": "<strong>Primary active transport by ABCA1:</strong> ABCA1 is a member of the ATP-binding cassette (ABC) transporter superfamily. It couples the binding and hydrolysis of two ATP molecules to a major conformational change that translocates free cholesterol and phospholipids across the plasma membrane bilayer, presenting them to extracellular ApoA-I. This is a primary active transport process.<br><br><em>Distractor Traps:</em><br>&bull; B describes sodium-dependent secondary active transporters such as SGLT1 or NKCC, which do not transport bulky sterols.<br>&bull; C is incorrect because potassium channels conduct single dehydrated $\\text{K}^+$ ions, not cholesterol molecules.<br>&bull; D describes endocytic uptake, whereas ABCA1 mediates extracellular efflux."
      },
      {
        "q": "Why do patients with Norum disease (LCAT deficiency) develop corneal clouding (opacities) and progressive renal glomerular dysfunction?",
        "ch": [
          "Precipitation of insoluble calcium oxalate monohydrate crystals in ocular and renal tissues",
          "Deposition of unesterified cholesterol in the corneal stroma and glomerular basement membrane",
          "Excessive accumulation of glycogen granules within podocytes and corneal keratocytes",
          "Autoimmune cytotoxic T-cell destruction of corneal endothelial collagen fibers"
        ],
        "a": 1,
        "e": "<strong>Pathology of Norum disease (LCAT deficiency):</strong> Without functional LCAT, unesterified free cholesterol cannot be converted into hydrophobic cholesteryl esters for storage in the HDL core. Consequently, nascent HDL remains an abnormal discoidal bilayer particle (termed lipoprotein X) that is overloaded with unesterified cholesterol and phosphatidylcholine. This excess free cholesterol partitions into tissue membranes, depositing in the corneal stroma (producing a dense grey-white circular corneal arcus or clouding) and into renal glomerular basement membranes, causing proteinuria, glomerulosclerosis, and ESRD.<br><br><em>Distractor Traps:</em><br>&bull; A describes primary hyperoxaluria, which forms calcium oxalate stones, not cholesterol deposits.<br>&bull; C describes glycogen storage diseases (e.g., Pompe disease).<br>&bull; D describes autoimmune keratitis, not an inborn error of lipid metabolism."
      }
    ]
  },
  {
    "id": "exam_bb90_6_p3",
    "sec": "B/B",
    "topic": "Low-Density Lipoprotein (LDL) Receptor Endocytosis & Familial Hypercholesterolemia",
    "sheet": 3,
    "label": "Biological and Biochemical Foundations of Living Systems",
    "examId": "bb90_6",
    "passage": "<div class=\"ttl\">Passage 3 (Questions 13&ndash;18)</div>\n<p>Cellular cholesterol homeostasis is orchestrated by the receptor-mediated endocytosis of low-density lipoproteins (LDL), a pathway elucidated by Brown and Goldstein. The human LDL receptor (LDLR) is a single-pass transmembrane glycoprotein composed of 839 amino acids partitioned into five functional domains: an N-terminal cysteine-rich ligand-binding domain containing seven repeat modules, an epidermal growth factor (EGF) precursor homology domain that coordinates pH-dependent ligand release, an $O$-linked oligosaccharide sugar domain, a hydrophobic transmembrane anchor, and a 50-amino acid cytoplasmic tail containing an essential $\\text{NPxY}$ (Asn-Pro-x-Tyr) internalizing signal motif.</p>\n<p>At the neutral pH of blood plasma (pH 7.4), the LDLR ligand-binding repeats coordinate calcium ions ($\\text{Ca}^{2+}$) to bind the ApoB-100 moiety of LDL with nanomolar affinity. The cytoplasmic $\\text{NPxY}$ motif binds the endocytic adaptor protein ARH (autosomal recessive hypercholesterolemia protein), which recruits clathrin heavy and light chains to cluster the ligand-receptor complexes into clathrin-coated pits. Following dynamin-mediated GTPase pinching, the internalized coated vesicle sheds its clathrin coat to form an early sorting endosome. As the endosomal membrane-bound $\\text{V-ATPase}$ proton pump acidifies the endosomal lumen to pH $5.0\\text{ to }5.5$, histidine residues within the EGF precursor domain become protonated, driving an intramolecular conformational rearrangement wherein the EGF domain binds the ligand-binding repeats. This conformational shift sterically displaces ApoB-100, liberating the LDL particle. The uncoupled LDLR recycles back to the plasma membrane (completing up to 150 cycles per 20-hour lifespan), whereas the released LDL is routed to lysosomes, where acid lipases hydrolyze CEs into unesterified cholesterol.</p>\n<p>Genetic mutations in <em>LDLR</em> cause Familial Hypercholesterolemia (FH). Cell biologists characterized human fibroblast lines isolated from healthy controls and patients representing distinct FH mutation classes (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 LDLR synthesis, binding, internalization, and degradation kinetics across FH mutation classes</caption>\n  <thead>\n    <tr><th>Cell Line / Mutation Class</th><th>Molecular Defect</th><th>Receptor Synthesis Rate (% Control)</th><th>LDL Surface Binding ($4^\\circ\\text{C}$) (% Control)</th><th>LDL Internalization ($37^\\circ\\text{C}$) (% Control)</th><th>Lysosomal LDL Degradation (% Control)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Control (Wild-Type)</td><td>Normal Function</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td></tr>\n    <tr><td>Class 1 (Null)</td><td>Promoter deletion / nonsense</td><td>< 1.0%</td><td>< 1.0%</td><td>< 1.0%</td><td>< 1.0%</td></tr>\n    <tr><td>Class 2 (Transport Defective)</td><td>ER retention / folding arrest</td><td>95.4%</td><td>3.2%</td><td>2.1%</td><td>1.8%</td></tr>\n    <tr><td>Class 3 (Binding Defective)</td><td>Point mutation in repeat 5</td><td>98.6%</td><td>5.8%</td><td>4.6%</td><td>4.1%</td></tr>\n    <tr><td>Class 4 (Internalization Defective)</td><td>Tyr807Cys in $\\text{NPxY}$ motif</td><td>102.1%</td><td>96.4%</td><td>6.2%</td><td>5.5%</td></tr>\n    <tr><td>Class 5 (Recycling Defective)</td><td>EGF domain deletion</td><td>94.2%</td><td>92.8%</td><td>88.4% (single round)</td><td>18.2%</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "Which molecular defect characterizes Class 4 Familial Hypercholesterolemia fibroblasts, where surface LDL binding at 4 degrees C is completely normal (96.4%) but internalization at 37 degrees C is severely impaired (6.2%)?",
        "ch": [
          "A mutation in the cytoplasmic NPxY motif preventing recruitment to clathrin-coated pits",
          "A premature stop codon in the promoter preventing transcription of the LDLR gene",
          "Misfolding of the N-terminal repeats causing permanent retention in the endoplasmic reticulum",
          "Deletion of the transmembrane domain causing complete secretion of the receptor into media"
        ],
        "a": 0,
        "e": "<strong>Mechanism of Class 4 LDLR mutations:</strong> In Class 4 FH (internalization-defective mutants, such as the classic patient J.D. harboring a Tyr807Cys substitution), the receptor is synthesized normally, undergoes proper post-translational glycosylation in the Golgi, and reaches the plasma membrane where its intact extracellular domain binds LDL normally ($96.4\\%$ binding at $4^\\circ\\text{C}$). However, the mutation alters the cytoplasmic $\\text{NPxY}$ internalization motif, preventing its interaction with the endocytic adaptor protein ARH. As a result, the receptor cannot cluster into clathrin-coated pits and cannot be endocytosed at $37^\\circ\\text{C}$ ($6.2\\%$ internalization).<br><br><em>Distractor Traps:</em><br>&bull; B describes Class 1 null mutations where no protein is synthesized.<br>&bull; C describes Class 2 transport-defective mutations where the protein is trapped in the ER.<br>&bull; D describes soluble secreted receptor truncations that never anchor in the plasma membrane."
      },
      {
        "q": "What fundamental biochemical mechanism triggers the dissociation of the LDL particle from the LDL receptor inside early endosomes?",
        "ch": [
          "Direct phosphorylation of ApoB-100 by an endosomal receptor tyrosine kinase enzyme",
          "Endosomal acidification to pH 5.5 causing protonation of histidine residues in the EGF domain",
          "Enzymatic cleavage of the LDLR ligand-binding domain by endosomal cathepsin proteases",
          "A massive surge in calcium ion concentration driving competitive sterol displacement"
        ],
        "a": 1,
        "e": "<strong>pH-dependent ligand release mechanism:</strong> Early endosomes contain vacuolar-type $\\text{H}^+$-ATPases (V-ATPases) that pump protons into the lumen, dropping internal pH from neutral ($7.4$) to acidic ($5.0\\text{ to }5.5$). At this lower pH, specific histidine residues within the EGF precursor homology domain of the LDLR become protonated (imidazole $\\text{p}K_a \\approx 6.0$). The resulting positive charges drive an intramolecular conformational change: the EGF domain folds back and binds to the ligand-binding repeats with high affinity, physically displacing the ApoB-100 protein of LDL.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because endosomal uncoupling is non-enzymatic and driven entirely by pH-dependent allosteric shifts.<br>&bull; C describes lysosomal proteolysis, which destroys LDL proteins but occurs after the receptor has already uncoupled and recycled.<br>&bull; D is incorrect because endosomes have lower free calcium than extracellular plasma, not higher."
      },
      {
        "q": "How does free cholesterol released from lysosomal LDL degradation downregulate de novo cellular cholesterol synthesis?",
        "ch": [
          "It binds directly to nuclear SREBP-2 to enhance transcriptional activation of the LDLR gene",
          "It binds to and activates adenylate cyclase to elevate intracellular cyclic AMP levels",
          "It retains the SCAP-SREBP complex in the ER, suppressing HMG-CoA reductase transcription",
          "It acts as an irreversible inhibitor of squalene synthase within the cytoplasmic compartment"
        ],
        "a": 2,
        "e": "<strong>SREBP-2 feedback regulation by cholesterol:</strong> When lysosomal cholesterol enters the endoplasmic reticulum membrane, it binds directly to SCAP (SREBP cleavage-activating protein). This sterol binding induces a conformational change that locks SCAP in a complex with the ER-resident anchor protein Insig. Consequently, the SCAP-SREBP-2 complex is trapped in the ER and cannot bud into COPII vesicles for transport to the Golgi. In the absence of Golgi-localized S1P and S2P protease cleavages, the active basic helix-loop-helix transcription factor domain of SREBP-2 is not released. Transcription of HMG-CoA reductase and the LDLR gene ceases, suppressing de novo synthesis.<br><br><em>Distractor Traps:</em><br>&bull; A describes the opposite response: when cholesterol is high, SREBP-2 processing is repressed, not stimulated.<br>&bull; B describes GPCR signaling, which is not the primary mechanism of sterol feedback.<br>&bull; D is incorrect because cholesterol exerts regulatory control via transcriptional repression and proteasomal degradation of HMGCR, not irreversible covalent inactivation of squalene synthase."
      },
      {
        "q": "Why do Class 5 LDLR mutant fibroblasts show normal internalization during a single cycle but exhibit a severe reduction in long-term cumulative LDL degradation (18.2% of control)?",
        "ch": [
          "The mutant receptor fails to bind clathrin adaptors and cannot enter coated pits",
          "Lysosomal hydrolases are inhibited by the mutant receptor's extracellular domains",
          "The mutant receptor undergoes premature degradation in the endoplasmic reticulum",
          "Failure of low-pH ligand release routes the receptor to lysosomes for degradation"
        ],
        "a": 3,
        "e": "<strong>Pathophysiology of Class 5 recycling-defective LDLR mutations:</strong> Class 5 mutants have deletions or mutations in the EGF precursor homology domain. These receptors fold properly, traffic to the cell surface, bind LDL, and undergo normal endocytosis. However, inside the acidic endosome, they cannot undergo the conformational shift required to release LDL. Because the receptor remains locked to its ligand, it fails to enter the recycling tubular endosome pathway and is instead trafficked along with LDL into lysosomes, where both the ligand and the receptor are degraded. Each receptor executes only a single round of endocytosis instead of the normal 150 rounds, causing rapid receptor depletion.<br><br><em>Distractor Traps:</em><br>&bull; A describes Class 4 mutants.<br>&bull; B is incorrect because lysosomal proteases are fully active and degrade the trapped receptor.<br>&bull; C describes Class 2 mutants."
      },
      {
        "q": "Proprotein convertase subtilisin/kexin type 9 (PCSK9) is a circulating hepatic protein that binds extracellularly to the LDLR. How does gain-of-function PCSK9 promote severe hypercholesterolemia?",
        "ch": [
          "It hydrolyzes ApoB-100 into small peptide fragments within circulating LDL particles",
          "It phosphorylates HMG-CoA reductase, locking the enzyme in a permanently active state",
          "It binds LDLR, blocking endosomal acid uncoupling and targeting it for lysosomal degradation",
          "It binds to macrophage scavenger receptors, completely preventing foam cell formation"
        ],
        "a": 2,
        "e": "<strong>PCSK9 mechanism of action:</strong> Secreted PCSK9 binds with high affinity to the EGF-A domain on the extracellular surface of the LDLR at neutral pH. When the LDLR-PCSK9 complex is endocytosed, the low pH of the endosome increases the binding affinity of PCSK9 for the receptor by 150-fold. This tight cross-linking prevents the receptor from adopting the closed recycling conformation. Consequently, the receptor cannot recycle to the cell surface and is escorted directly to lysosomes for degradation. Gain-of-function PCSK9 destroys hepatic LDLRs, drastically lowering cell-surface receptor density and causing severe hypercholesterolemia.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because PCSK9 does not act as a general protease against circulating ApoB-100.<br>&bull; B describes AMP-activated protein kinase (AMPK) regulation of HMGCR, not PCSK9.<br>&bull; D is incorrect because PCSK9 promotes atherogenesis rather than preventing foam cell formation."
      },
      {
        "q": "Which therapeutic intervention directly mimics the cellular response to low intracellular cholesterol by stimulating the hepatic clearance of circulating LDL?",
        "ch": [
          "Oral administration of non-absorbable bile acids to suppress intestinal fat absorption",
          "Monoclonal neutralizing antibodies that bind and inhibit the enterocyte NPC1L1 transporter",
          "Dietary supplementation with saturated triacylglycerols and unesterified free cholesterol",
          "HMG-CoA reductase inhibitors (statins) that deplete intracellular cholesterol and upregulate LDLR"
        ],
        "a": 3,
        "e": "<strong>Mechanism of statin-induced LDLR upregulation:</strong> Statins competitively inhibit HMG-CoA reductase, the rate-limiting enzyme in de novo cholesterol synthesis. Depletion of intracellular hepatic cholesterol frees SCAP from Insig in the ER membrane, enabling SCAP-SREBP-2 translocation to the Golgi and proteolytic release of mature SREBP-2. SREBP-2 enters the nucleus and binds to sterol regulatory elements (SREs) in the promoter of the <em>LDLR</em> gene, driving a multi-fold increase in LDLR synthesis and surface expression. Hepatocytes clear circulating LDL from the blood, reducing plasma LDL-cholesterol by $30\\text{ to }50\\%$.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because administering bile acids downregulates 7-alpha-hydroxylase and spares cholesterol.<br>&bull; B describes ezetimibe (a small molecule, not a monoclonal antibody), which blocks intestinal absorption but does not directly inhibit HMGCR.<br>&bull; C elevates intracellular cholesterol, suppressing LDLR expression and worsening hypercholesterolemia."
      }
    ]
  },
  {
    "id": "exam_bb90_6_p4",
    "sec": "B/B",
    "topic": "Cholesterol Biosynthesis: HMG-CoA Reductase & Statin Pharmacodynamics",
    "sheet": 4,
    "label": "Biological and Biochemical Foundations of Biological Systems",
    "examId": "bb90_6",
    "passage": "<div class=\"ttl\">Passage 4 (Questions 19&ndash;24)</div>\n<p>De novo cholesterol biosynthesis is a 37-step metabolic pathway occurring primarily in the cytosol and endoplasmic reticulum of hepatocytes. All 27 carbon atoms of the tetracyclic steroid core originate from cytosolic acetyl-CoA. The pathway initiates with the condensation of two acetyl-CoA molecules by acetoacetyl-CoA thiolase, followed by the addition of a third acetyl-CoA catalyzed by 3-hydroxy-3-methylglutaryl-CoA (HMG-CoA) synthase to yield HMG-CoA. The committed, rate-limiting step of the entire biosynthetic sequence is the four-electron reduction of HMG-CoA to mevalonate, catalyzed by HMG-CoA reductase (HMGCR), an integral glycoprotein of the smooth endoplasmic reticulum membrane: $\\text{HMG-CoA} + 2\\text{ NADPH} + 2\\text{ H}^+ \\rightarrow \\text{Mevalonate} + \\text{CoA-SH} + 2\\text{ NADP}^+$.</p>\n<p>HMGCR is subject to exquisite multivalent regulation at transcriptional, translational, and post-translational levels. Post-translationally, AMP-activated protein kinase (AMPK) phosphorylates HMGCR at Ser872 during states of cellular energy depletion (elevated AMP/ATP ratio), allosterically inactivating the enzyme to preserve ATP. In addition, when sterol levels in the ER membrane are high, sterols bind the transmembrane sterol-sensing domain (SSD) of HMGCR, recruiting Insig-1 and Insig-2 associated with gp78 ubiquitin ligases. This triggers lysine ubiquitination of HMGCR, driving its retrotranslocation into the cytosol for proteasomal degradation by the 26S proteasome (endoplasmic reticulum-associated degradation, ERAD).</p>\n<p>Statins are competitive transition-state analogs of the HMG-CoA substrate that bind the catalytic domain of HMGCR with nanomolar dissociation constants ($K_i = 1\\text{ to }10\\text{ nM}$), outcompeting the native substrate ($K_m \\approx 4\\ \\mu\\text{M}$). Pharmacologists evaluated the inhibition kinetics, intracellular sterol concentrations, and SREBP-2 nuclear translocation in cultured human hepatocytes treated with atorvastatin, mevalonate, or the AMPK activator AICAR (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 HMGCR activity, hepatic sterol pools, and SREBP-2 nuclear localization across experimental conditions</caption>\n  <thead>\n    <tr><th>Condition</th><th>Apparent HMGCR $K_m$ ($\\mu\\text{M}$)</th><th>Apparent $V_{max}$ (nmol/min/mg)</th><th>Phospho-Ser872 HMGCR (% Control)</th><th>Nuclear SREBP-2 (% Control)</th><th>Surface LDLR Expression (% Control)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Control (Untreated)</td><td>4.2</td><td>100.0</td><td>100.0%</td><td>100.0%</td><td>100.0%</td></tr>\n    <tr><td>Atorvastatin (10 nM)</td><td>28.6</td><td>99.4</td><td>102.1%</td><td>340.5%</td><td>310.2%</td></tr>\n    <tr><td>Atorvastatin + Mevalonate (1 mM)</td><td>29.1</td><td>98.8</td><td>101.4%</td><td>95.2%</td><td>98.6%</td></tr>\n    <tr><td>AICAR (AMPK Activator, 0.5 mM)</td><td>4.3</td><td>18.4</td><td>485.0%</td><td>110.2%</td><td>105.4%</td></tr>\n    <tr><td>Sterol Overload (25-HC)</td><td>4.1</td><td>22.1 (ERAD degradation)</td><td>104.2%</td><td>12.4%</td><td>14.8%</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "Based on the kinetic parameters in Table 1, what type of enzyme inhibition does atorvastatin exhibit against HMG-CoA reductase?",
        "ch": [
          "Competitive inhibition, characterized by an increase in apparent Km with no change in Vmax",
          "Noncompetitive inhibition, characterized by a decrease in Vmax with no change in Km",
          "Uncompetitive inhibition, characterized by proportional decreases in both Km and Vmax",
          "Irreversible covalent suicide inhibition, characterized by permanent destruction of Vmax"
        ],
        "a": 0,
        "e": "<strong>Enzyme kinetic profile of statins:</strong> Table 1 shows that in the presence of $10\\text{ nM}$ atorvastatin, the apparent $K_m$ of HMGCR increases from $4.2\\ \\mu\\text{M}$ to $28.6\\ \\mu\\text{M}$ (reflecting reduced apparent affinity because inhibitor and substrate compete for the same active site), while $V_{max}$ remains unchanged ($99.4\\%$ vs $100.0\\%$). This diagnostic signature ($K_m$ increases, $V_{max}$ unaffected) defines reversible competitive inhibition. High substrate concentrations can fully displace the statin.<br><br><em>Distractor Traps:</em><br>&bull; B describes noncompetitive inhibition where $V_{max}$ drops and $K_m$ is constant.<br>&bull; C describes uncompetitive inhibition where both $K_m$ and $V_{max}$ decrease in parallel.<br>&bull; D describes irreversible covalent inactivation, which permanently eliminates active enzyme and suppresses $V_{max}$."
      },
      {
        "q": "Why does co-administration of exogenous mevalonate completely reverse atorvastatin-induced SREBP-2 nuclear translocation and LDLR upregulation in Table 1?",
        "ch": [
          "Mevalonate degrades atorvastatin via a direct chemical nucleophilic substitution reaction",
          "Mevalonate restores downstream sterol synthesis, triggering Insig-mediated ER retention of SCAP",
          "Mevalonate acts as an allosteric inhibitor of the nuclear transport karyopherin exportins",
          "Mevalonate irreversibly phosphorylates the basic helix-loop-helix domain of SREBP-2"
        ],
        "a": 1,
        "e": "<strong>Downstream rescue of sterol feedback by mevalonate:</strong> Statins block the synthesis of mevalonate, starving the hepatocyte of downstream intermediates (isopentenyl pyrophosphate, squalene, and cholesterol). The resulting depletion of ER membrane sterols triggers SCAP-SREBP-2 translocation to the Golgi and nuclear release of active SREBP-2. Providing exogenous mevalonate bypasses the blocked HMGCR step, restoring downstream cholesterol biosynthesis. The re-synthesized sterols bind SCAP, inducing Insig binding and trapping SCAP-SREBP-2 in the ER. Consequently, nuclear SREBP-2 falls back to baseline ($95.2\\%$) and LDLR upregulation is abolished ($98.6\\%$).<br><br><em>Distractor Traps:</em><br>&bull; A is chemically implausible; mevalonate does not degrade statins.<br>&bull; C is incorrect because mevalonate does not block nuclear pore karyopherins.<br>&bull; D is incorrect because SREBP-2 regulation is governed by ER-to-Golgi translocation and proteolytic cleavage, not direct phosphorylation by mevalonate."
      },
      {
        "q": "How does AMP-activated protein kinase (AMPK) activation by AICAR reduce HMG-CoA reductase activity without altering the enzyme's affinity (Km) for HMG-CoA?",
        "ch": [
          "AMPK phosphorylates the active-site catalytic histidine to induce competitive inhibition",
          "AMPK ubiquitinates HMGCR to target it directly to the 20S core particle for proteolysis",
          "AMPK phosphorylates Ser872, shifting the enzyme into a low-activity state (lowering Vmax)",
          "AMPK cleaves the N-terminal transmembrane domain, causing cytosolic enzyme precipitation"
        ],
        "a": 2,
        "e": "<strong>Covalent regulation of HMGCR by AMPK:</strong> When cellular energy status is compromised (elevated AMP/ATP ratio), AMPK is activated and phosphorylates HMGCR at a conserved serine residue (Ser872 in humans). This covalent phosphorylation induces a conformational change that locks the catalytic tetramer in an inactive state, reducing $V_{max}$ from $100\\%$ to $18.4\\%$ (Table 1) without altering the intrinsic binding affinity of unphosphorylated active sites ($K_m$ remains $\\approx 4.3\\ \\mu\\text{M}$). This serves as an energetic brake, shutting down energy-intensive cholesterol synthesis (which consumes 18 ATP and 14 NADPH per molecule).<br><br><em>Distractor Traps:</em><br>&bull; A confuses allosteric/covalent $V_{max}$ suppression with competitive active-site inhibition.<br>&bull; B describes the Insig/gp78 ERAD pathway triggered by sterol overload, not AMPK.<br>&bull; D is incorrect because phosphorylation does not cleave the transmembrane anchor."
      },
      {
        "q": "What is the stoichiometric consumption of NADPH reducing equivalents during the complete reduction of one mole of HMG-CoA to one mole of mevalonate?",
        "ch": [
          "0.5 moles of NADPH",
          "1 mole of NADPH",
          "4 moles of NADPH",
          "2 moles of NADPH"
        ],
        "a": 3,
        "e": "<strong>Stoichiometry of the HMGCR reaction:</strong> The enzymatic reduction of HMG-CoA to mevalonate is a four-electron reduction that proceeds via two successive hydride transfers from NADPH. In the first step, HMG-CoA is reduced to a transient enzyme-bound hemithioacetal intermediate with release of $\\text{CoASH}$ and consumption of one NADPH, generating mevaldine. In the second step, mevaldine is reduced to mevalonate with consumption of a second NADPH: $\\text{HMG-CoA} + 2\\text{ NADPH} + 2\\text{ H}^+ \\rightarrow \\text{Mevalonate} + \\text{CoA-SH} + 2\\text{ NADP}^+$. Thus, exactly 2 moles of NADPH are consumed per mole of mevalonate generated.<br><br><em>Distractor Traps:</em><br>&bull; A and B underestimate the stoichiometry, forgetting that reducing a thioester carbonyl to a primary alcohol is a four-electron (two-hydride) reduction.<br>&bull; C confuses the number of electrons transferred (4 electrons) with the number of NADPH molecules consumed (each NADPH transfers a hydride ion, $2e^-$)."
      },
      {
        "q": "In addition to cholesterol, which critical downstream isoprenoid intermediate synthesized from mevalonate is depleted by statin therapy, potentially contributing to statin-induced myopathy?",
        "ch": [
          "Coenzyme Q10 (ubiquinone) and dolichol phosphate",
          "Acetyl-CoA carboxylase and malonyl-CoA precursor",
          "Tetrahydrofolate and S-adenosylmethionine donor",
          "Prostaglandin H2 and thromboxane A2 eicosanoids"
        ],
        "a": 0,
        "e": "<strong>Non-sterol isoprenoid products of the mevalonate pathway:</strong> The mevalonate pathway bifurcates downstream into non-sterol isoprenoids. Mevalonate is converted into isopentenyl pyrophosphate (IPP) and farnesyl pyrophosphate (FPP). FPP is required for the synthesis of ubiquinone (Coenzyme Q10, essential for mitochondrial electron transport chain Complexes I-III), dolichol phosphate (required for $N$-linked glycoprotein synthesis in the ER), and geranylgeranyl pyrophosphate (required for prenylation and membrane targeting of Rho/Rab/Ras GTPases). Depletion of CoQ10 impairs mitochondrial respiration and ATP generation in skeletal muscle, contributing to statin-induced myopathy and rhabdomyolysis.<br><br><em>Distractor Traps:</em><br>&bull; B describes fatty acid synthesis precursors, which are upstream of HMGCR.<br>&bull; C describes one-carbon folate and methyl metabolism, which are independent of mevalonate.<br>&bull; D describes eicosanoids synthesized from arachidonic acid via cyclooxygenases."
      },
      {
        "q": "What is the subcellular localization of the HMG-CoA synthase enzyme that participates in de novo cholesterol synthesis versus the isozyme that participates in ketogenesis?",
        "ch": [
          "Both isozymes are localized exclusively within the mitochondrial matrix space",
          "Cholesterogenic HMGCS is cytosolic, whereas ketogenic HMGCS is mitochondrial",
          "Cholesterogenic HMGCS is peroxisomal, whereas ketogenic HMGCS is nuclear",
          "Both isozymes are localized exclusively on the extracellular surface of plasma membranes"
        ],
        "a": 1,
        "e": "<strong>Compartmentalization of HMG-CoA synthase isozymes:</strong> Eukaryotic cells maintain two distinct pools of HMG-CoA segregated by subcellular compartmentalization. De novo cholesterol synthesis utilizes cytosolic HMG-CoA synthase (HMGCS1), generating HMG-CoA in the cytoplasm to feed the smooth ER-anchored HMG-CoA reductase. In contrast, ketogenesis occurs exclusively in the liver during fasting or carbohydrate restriction and utilizes mitochondrial HMG-CoA synthase (HMGCS2), generating HMG-CoA inside the mitochondrial matrix to feed mitochondrial HMG-CoA lyase for acetoacetate synthesis.<br><br><em>Distractor Traps:</em><br>&bull; A ignores compartmentalization; ketogenesis is mitochondrial, but cholesterol synthesis is cytosolic/ER.<br>&bull; C is incorrect because neither isozyme resides in the nucleus.<br>&bull; D is incorrect because both pathways are intracellular."
      }
    ]
  },
  {
    "id": "exam_bb90_6_p5",
    "sec": "B/B",
    "topic": "Bile Acid Synthesis, Enterohepatic Circulation & Cholesterol Elimination",
    "sheet": 5,
    "label": "Biological and Biochemical Foundations of Biological Systems",
    "examId": "bb90_6",
    "passage": "<div class=\"ttl\">Passage 5 (Questions 25&ndash;30)</div>\n<p>Because the human body lacks the metabolic machinery to degrade the cyclopentanoperhydrophenanthrene steroid nucleus into carbon dioxide and water, conversion into bile acids represents the primary quantitative pathway for systemic cholesterol elimination. Synthesis of primary bile acids occurs exclusively in hepatocytes via two convergent metabolic routes: the classic (neutral) pathway, which accounts for $> 90\\%$ of bile acid output under physiological conditions, and the alternative (acidic) pathway. The committed, rate-limiting step of the classic pathway is the $7\\alpha$-hydroxylation of cholesterol catalyzed by cholesterol $7\\alpha$-hydroxylase (CYP7A1), a microsomal cytochrome P450 monooxygenase: $\\text{Cholesterol} + \\text{NADPH} + \\text{H}^+ + \\text{O}_2 \\rightarrow 7\\alpha\\text{-Hydroxycholesterol} + \\text{NADP}^+ + \\text{H}_2\\text{O}$.</p>\n<p>Subsequent multi-step enzymatic modifications yield the two primary bile acids: cholic acid (a trihydroxy bile acid) and chenodeoxycholic acid (a dihydroxy bile acid). Before secretion into bile canaliculi via the bile salt export pump (BSEP / ABCB11), the terminal C-24 carboxyl group of primary bile acids is conjugated via an amide bond to either glycine or taurine by bile acid-CoA:amino acid $N$-acyltransferase (BAAT). Conjugation dramatically lowers the $\\text{p}K_a$ of the bile acid from $\\approx 5.0$ to $\\approx 3.7$ for glyco-conjugates and $\\approx 1.5$ for tauro-conjugates. At the neutral-to-alkaline pH of the duodenum (pH 6.5 to 7.5), conjugated bile salts exist entirely as fully ionized, water-soluble amphipathic anions that form mixed micelles with dietary lipids and fat-soluble vitamins.</p>\n<p>In the terminal ileum, $> 95\\%$ of secreted bile salts are actively reabsorbed by the apical sodium-dependent bile acid transporter (ASBT / SLC10A2) and returned to the liver via the portal circulation (enterohepatic circulation). Enteric bacteria in the colon deconjugate unabsorbed bile salts and catalyze $7\\alpha$-dehydroxylation to produce secondary bile acids: deoxycholic acid (from cholic acid) and lithocholic acid (from chenodeoxycholic acid). In hepatocytes, bile acids bind the nuclear farnesoid X receptor (FXR), inducing small heterodimer partner (SHP) to repress <em>CYP7A1</em> transcription. Pharmacologists studied the effects of the bile acid sequestrant cholestyramine, an ASBT inhibitor, and an FXR agonist on bile acid synthesis and plasma LDL-cholesterol (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Bile acid synthesis rate, fecal bile excretion, and plasma lipid profiles across treatments</caption>\n  <thead>\n    <tr><th>Treatment Condition</th><th>Mechanism of Action</th><th>Hepatic CYP7A1 Activity (% Control)</th><th>Fecal Bile Acid Excretion (g/day)</th><th>Hepatic Nuclear SREBP-2 (% Control)</th><th>Plasma LDL-C (% Control)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Control (Baseline)</td><td>Untreated Physiology</td><td>100.0%</td><td>0.5 &plusmn; 0.1</td><td>100.0%</td><td>100.0%</td></tr>\n    <tr><td>Cholestyramine (16 g/day)</td><td>Non-absorbable anion-exchange resin</td><td>420.5%</td><td>4.8 &plusmn; 0.4</td><td>245.0%</td><td>72.4% (-28%)</td></tr>\n    <tr><td>ASBT Inhibitor (Volixibat)</td><td>Blocks ileal apical bile reabsorption</td><td>385.0%</td><td>4.2 &plusmn; 0.3</td><td>220.0%</td><td>76.8% (-23%)</td></tr>\n    <tr><td>FXR Agonist (Obeticholic Acid)</td><td>Activates nuclear FXR-SHP axis</td><td>22.4%</td><td>0.2 &plusmn; 0.05</td><td>65.0%</td><td>118.2% (+18%)</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "Why does conjugation of primary bile acids to taurine or glycine dramatically improve their biological efficacy as lipid-emulsifying detergents in the duodenum?",
        "ch": [
          "It lowers their pKa below duodenal pH, ensuring they exist as fully ionized amphipathic anions",
          "It converts the hydrophobic steroid ring into an open-chain aliphatic hydrocarbon",
          "It prevents bile salts from forming mixed micelles with dietary triacylglycerols",
          "It allows bile salts to cross enterocyte membranes via unassisted nonpolar passive diffusion"
        ],
        "a": 0,
        "e": "<strong>Biochemical consequence of bile acid conjugation:</strong> Unconjugated bile acids have a $\\text{p}K_a$ of approximately $5.0$. At duodenal pH ($6.0\\text{ to }7.0$), a significant fraction would exist as protonated, unionized, water-insoluble molecules that precipitate out of solution. Conjugating the carboxyl group to glycine lowers the $\\text{p}K_a$ to $\\approx 3.7$, and conjugation to taurine (containing a sulfonic acid group) lowers it to $\\approx 1.5$. At physiological duodenal pH, both conjugated forms exist $100\\%$ as fully ionized, negatively charged bile salts. These charged species possess high water solubility and potent amphipathic detergent activity, self-assembling into mixed micelles that solubilize dietary lipids.<br><br><em>Distractor Traps:</em><br>&bull; B is incorrect because conjugation modifies only the C-24 side chain; the four-ring steroid nucleus remains intact.<br>&bull; C describes the opposite effect; conjugation is essential for mixed micelle formation.<br>&bull; D is incorrect because ionized bile salts cannot passively diffuse across lipid bilayers and require the ASBT transporter."
      },
      {
        "q": "How does administration of the non-absorbable bile acid sequestrant cholestyramine lead to a 28% reduction in circulating plasma LDL-cholesterol (Table 1)?",
        "ch": [
          "It directly binds circulating LDL particles in the bloodstream and targets them to the spleen",
          "It binds bile acids in the gut, interrupting enterohepatic return and upregulating hepatic LDLR",
          "It irreversibly inhibits HMG-CoA reductase by binding to its active-site cysteine residue",
          "It accelerates renal excretion of free unesterified cholesterol via glomerular filtration"
        ],
        "a": 1,
        "e": "<strong>Mechanism of bile acid sequestrants on LDL-cholesterol:</strong> Cholestyramine is a positively charged non-absorbable anion-exchange resin that binds negatively charged bile salts in the small intestinal lumen, preventing their reabsorption in the terminal ileum. Fecal bile acid excretion surges nearly 10-fold (from $0.5$ to $4.8\\text{ g/day}$, Table 1). To compensate for the loss of the bile acid pool, hepatocytes must convert more cholesterol into bile acids, upregulating the rate-limiting enzyme CYP7A1 by $420\\%$. This conversion depletes intracellular hepatic cholesterol, triggering SCAP-SREBP-2 translocation to the nucleus (nuclear SREBP-2 rises to $245\\%$). SREBP-2 upregulates LDLR expression, accelerating the clearance of circulating LDL from plasma.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because cholestyramine is never absorbed into the bloodstream; its action is entirely intraluminal.<br>&bull; C describes statins, not bile acid sequestrants.<br>&bull; D is incorrect because cholesterol is not filtered by the renal glomerulus."
      },
      {
        "q": "What is the primary product formed when colonic enteric bacteria catalyze 7-alpha-dehydroxylation of the primary bile acid chenodeoxycholic acid?",
        "ch": [
          "Cholic acid molecule",
          "Deoxycholic acid",
          "Lithocholic acid",
          "Ursodeoxycholic acid"
        ],
        "a": 2,
        "e": "<strong>Bacterial conversion of primary to secondary bile acids:</strong> In the colon, anaerobic bacteria (such as <em>Clostridium scindens</em>) express $7\\alpha$-dehydroxylase enzymes. Cholic acid (which has hydroxyl groups at $3\\alpha, 7\\alpha, 12\\alpha$) is dehydroxylated at the $7\\alpha$ position to produce deoxycholic acid ($3\\alpha, 12\\alpha$). Chenodeoxycholic acid (which has hydroxyl groups at $3\\alpha, 7\\alpha$) is dehydroxylated at the $7\\alpha$ position to yield lithocholic acid ($3\\alpha$). Lithocholic acid is hydrophobic, insoluble, and predominantly excreted in feces.<br><br><em>Distractor Traps:</em><br>&bull; A is a primary bile acid synthesized in the liver.<br>&bull; B is the secondary bile acid derived from cholic acid.<br>&bull; D is a $7\\beta$-epimer of chenodeoxycholic acid, not the $7\\alpha$-dehydroxylation product."
      },
      {
        "q": "How does activation of the nuclear farnesoid X receptor (FXR) by the agonist obeticholic acid repress hepatic CYP7A1 transcription (Table 1)?",
        "ch": [
          "FXR directly phosphorylates the promoter region of the CYP7A1 gene to block RNA polymerase",
          "FXR induces ubiquitin ligases that destroy mature CYP7A1 enzyme within the endoplasmic reticulum",
          "FXR binds directly to the active site of CYP7A1, acting as an uncompetitive pathway inhibitor",
          "FXR induces transcription of Small Heterodimer Partner (SHP), which represses LRH-1 on CYP7A1"
        ],
        "a": 3,
        "e": "<strong>FXR-SHP feedback repression of bile acid synthesis:</strong> Bile acids serve as endogenous ligands for the nuclear receptor FXR. When bile acids return to the liver via the portal vein, they bind FXR in the nucleus. Liganded FXR heterodimerizes with RXR and binds to the promoter of the <em>SHP</em> gene (small heterodimer partner, an atypical nuclear receptor lacking a DNA-binding domain). Elevated SHP protein physically interacts with and inhibits Liver Receptor Homolog-1 (LRH-1). Because LRH-1 is an obligatory transcriptional activator of <em>CYP7A1</em>, its inhibition shuts down <em>CYP7A1</em> transcription, dropping activity to $22.4\\%$ (Table 1).<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because nuclear receptors are transcription factors, not DNA kinases.<br>&bull; B describes proteasomal degradation (ERAD), which is not the primary nuclear feedback mechanism.<br>&bull; C confuses a nuclear receptor transcription factor with a direct competitive enzyme inhibitor."
      },
      {
        "q": "Which anatomical region of the gastrointestinal tract contains the apical sodium-dependent bile acid transporter (ASBT) responsible for the active reabsorption of > 95% of secreted bile salts?",
        "ch": [
          "Fundus and body of the stomach organ",
          "Descending segment of the human duodenum",
          "Terminal ileum of the small intestine",
          "Ascending segment of the large colon"
        ],
        "a": 2,
        "e": "<strong>Anatomical site of enterohepatic bile reabsorption:</strong> Active conjugated bile salt reabsorption is localized almost exclusively to the brush-border membrane of enterocytes in the terminal ileum. Here, the secondary active transporter ASBT (apical sodium-dependent bile acid transporter / SLC10A2) harnesses the inwardly directed sodium gradient established by basolateral $\\text{Na}^+/\\text{K}^+$-ATPases to transport bile salts across the apical membrane into the enterocyte. Enterocytes then export bile salts across the basolateral membrane via the heterodimeric transporter OST$\\alpha$/OST$\\beta$ into the portal vein. Surgical resection or Crohn's disease inflammation of the terminal ileum disrupts this absorption, causing bile acid malabsorption, secretory diarrhea, and fat malabsorption.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because the stomach does not absorb bile salts.<br>&bull; B is the site where bile enters the GI tract via the ampulla of Vater, but active reabsorption does not occur here.<br>&bull; D is where unabsorbed bile salts undergo bacterial deconjugation and conversion into secondary bile acids."
      },
      {
        "q": "Why does long-term surgical resection of the terminal ileum lead to the formation of radiolucent cholesterol gallstones in the gallbladder?",
        "ch": [
          "Bile salts precipitate with calcium carbonate, forming hard pigment gallstones",
          "The liver halts all biliary cholesterol secretion to protect against bile toxicity",
          "Bacterial overgrowth in the ileum hydrolyzes all dietary cholesterol into fatty acids",
          "The bile salt pool is depleted, reducing the bile-salt-to-cholesterol ratio in bile"
        ],
        "a": 3,
        "e": "<strong>Pathogenesis of cholesterol gallstones in ileal resection:</strong> Cholesterol is an extremely hydrophobic molecule that is kept soluble in bile by being incorporated into mixed micelles alongside amphipathic bile salts and phospholipids (lecithin). Terminal ileal resection disrupts the enterohepatic circulation, causing massive fecal loss of bile salts that exceeds the maximal synthetic capacity of hepatic CYP7A1. As the systemic bile salt pool shrinks, the ratio of bile salts to cholesterol in bile plummets. When the cholesterol saturation index exceeds $1.0$, cholesterol precipitates out of solution as microscopic monohydrate crystals, which aggregate to form radiolucent cholesterol gallstones.<br><br><em>Distractor Traps:</em><br>&bull; A describes black pigment gallstones, which are composed of calcium bilirubinate and arise from chronic hemolysis.<br>&bull; B is incorrect because hepatocytes continue secreting unesterified cholesterol into bile.<br>&bull; C is incorrect because cholesterol is not converted into fatty acids by enteric bacteria."
      }
    ]
  },
  {
    "id": "exam_bb90_6_p6",
    "sec": "B/B",
    "topic": "Triacylglycerol Mobilization: Hormone-Sensitive Lipase (HSL) vs Lipoprotein Lipase (LPL)",
    "sheet": 6,
    "label": "Biological and Biochemical Foundations of Biological Systems",
    "examId": "bb90_6",
    "passage": "<div class=\"ttl\">Passage 6 (Questions 31&ndash;36)</div>\n<p>Triacylglycerols (TAGs) stored in white adipose tissue droplets represent the principal long-term energy reservoir in humans, yielding $9\\text{ kcal/g}$ upon complete oxidation compared to $4\\text{ kcal/g}$ for glycogen or protein. The mobilization and clearance of lipid fuel are governed by the reciprocal, tissue-specific regulation of two key lipases: hormone-sensitive lipase (HSL) within adipocyte lipid droplets and lipoprotein lipase (LPL) anchored to capillary endothelial surfaces.</p>\n<p>During fasting, exercise, or acute stress, catecholamines (epinephrine and norepinephrine) bind adipocyte $\\beta_3$-adrenergic receptors, activating $\\text{G}_{\\alpha s}$ to stimulate adenylyl cyclase. The resulting elevation in cyclic AMP (cAMP) activates protein kinase A (PKA). PKA phosphorylates two critical targets: perilipin-1 (PLIN1), which coats the lipid droplet surface, and cytosolic HSL at Ser660. Unphosphorylated perilipin-1 binds and sequesters comparative gene identification-58 (CGI-58). Upon PKA phosphorylation, CGI-58 is released and allosterically activates adipose triglyceride lipase (ATGL), which catalyzes the initial and rate-limiting step of lipolysis: $\\text{TAG} \\rightarrow \\text{Diacylglycerol (DAG)} + \\text{FFA}$. Concurrently, phosphorylated HSL translocates from the cytosol to the droplet surface, where it hydrolyzes DAG to monoacylglycerol (MAG). Finally, monoacylglycerol lipase (MGL) hydrolyzes MAG to glycerol and a third FFA. Free fatty acids are released into plasma bound to serum albumin, while glycerol travels to the liver for gluconeogenesis.</p>\n<p>In contrast, in the postprandial well-fed state, elevated insulin stimulates protein phosphatase 1 (PP1) and phosphodiesterase 3B (PDE3B), which degrades cAMP, thereby dephosphorylating and inactivating HSL and ATGL to suppress lipolysis. Simultaneously, insulin upregulates LPL synthesis in adipose tissue to promote the uptake and storage of dietary fatty acids. Physiologists quantified lipolytic flux, enzyme phosphorylation, and free fatty acid release in human adipocyte cultures across hormonal and pharmacological conditions (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Lipolytic enzyme phosphorylation, intracellular cAMP, and free fatty acid release in adipocytes</caption>\n  <thead>\n    <tr><th>Experimental Condition</th><th>Intracellular cAMP (pmol/mg)</th><th>Phospho-HSL (Ser660) (% Control)</th><th>Phospho-Perilipin-1 (% Control)</th><th>Glycerol Release ($\\mu\\text{mol/g/hr}$)</th><th>FFA Release ($\\mu\\text{mol/g/hr}$)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Basal Control (No Hormone)</td><td>1.2 &plusmn; 0.2</td><td>100.0%</td><td>100.0%</td><td>2.1 &plusmn; 0.3</td><td>6.2 &plusmn; 0.5</td></tr>\n    <tr><td>Epinephrine ($1\\ \\mu\\text{M}$)</td><td>14.8 &plusmn; 1.5</td><td>540.0%</td><td>610.0%</td><td>18.4 &plusmn; 1.2</td><td>55.1 &plusmn; 3.2</td></tr>\n    <tr><td>Epinephrine + Insulin (100 nM)</td><td>2.4 &plusmn; 0.4</td><td>125.0%</td><td>130.0%</td><td>3.6 &plusmn; 0.4</td><td>10.8 &plusmn; 0.8</td></tr>\n    <tr><td>Epinephrine + Propranolol ($10\\ \\mu\\text{M}$)</td><td>1.4 &plusmn; 0.3</td><td>105.0%</td><td>108.0%</td><td>2.3 &plusmn; 0.3</td><td>6.8 &plusmn; 0.6</td></tr>\n    <tr><td>Forskolin (Adenylate Cyclase Activator)</td><td>18.2 &plusmn; 1.8</td><td>620.0%</td><td>680.0%</td><td>21.2 &plusmn; 1.6</td><td>63.4 &plusmn; 3.8</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "Why does complete enzymatic hydrolysis of one mole of triacylglycerol inside an adipocyte yield exactly three moles of free fatty acids and one mole of glycerol?",
        "ch": [
          "A triacylglycerol molecule consists of three fatty acids esterified to a single glycerol backbone",
          "Three glycerol molecules condense into a triacylglycerol during post-absorptive lipid synthesis",
          "Adipocyte lipases cleave peptide bonds connecting amino acid side chains to free fatty acids",
          "Glycerol is an 18-carbon unsaturated lipid that spontaneously fragments into three acetate molecules"
        ],
        "a": 0,
        "e": "<strong>Triacylglycerol chemical structure and lipolytic stoichiometry:</strong> A triacylglycerol (triglyceride) molecule consists of a three-carbon glycerol backbone esterified to three fatty acyl chains via ester linkages at the C-1, C-2, and C-3 positions. Complete intracellular lipolysis requires three sequential hydrolytic steps: ATGL removes the first fatty acid from TAG to yield DAG; HSL removes the second fatty acid from DAG to yield MAG; and MGL removes the third fatty acid from MAG to yield free glycerol. Thus, the stoichiometric ratio of products is exactly $3\\text{ moles of FFA}$ to $1\\text{ mole of glycerol}$. In Table 1, the ratio of FFA release to glycerol release is consistently $3:1$ ($55.1 / 18.4 \\approx 3.0$).<br><br><em>Distractor Traps:</em><br>&bull; B reverses the stoichiometry, claiming three glycerols condense into one TAG.<br>&bull; C describes proteolysis of peptide bonds, not ester hydrolysis of lipids.<br>&bull; D confuses glycerol (a 3-carbon triol) with an 18-carbon fatty acid."
      },
      {
        "q": "What is the biochemical mechanism by which insulin antagonizes epinephrine-stimulated lipolysis in Table 1, reducing glycerol release from 18.4 to 3.6 umol/g/hr?",
        "ch": [
          "Insulin phosphorylates and activates beta-3 adrenergic receptors on the adipocyte surface",
          "Insulin activates phosphodiesterase 3B (PDE3B) via PKB/Akt, hydrolyzing cAMP into 5'-AMP",
          "Insulin irreversibly denatures adipose triglyceride lipase (ATGL) within lipid droplets",
          "Insulin directly binds to albumin in the extracellular space, preventing fatty acid binding"
        ],
        "a": 1,
        "e": "<strong>Antilipolytic signaling cascade of insulin:</strong> Insulin binds its receptor tyrosine kinase on adipocytes, triggering autophosphorylation and recruitment of IRS-1/2, which activates the $\\text{PI3K-Akt}$ (PKB) pathway. Akt directly phosphorylates and activates phosphodiesterase 3B (PDE3B). Active PDE3B rapidly hydrolyzes cyclic AMP into inactive $5'\\text{-AMP}$, dropping intracellular cAMP levels from $14.8\\text{ pmol/mg}$ to $2.4\\text{ pmol/mg}$ (Table 1). Without cAMP, PKA becomes inactive, and protein phosphatase-1 (PP1) dephosphorylates HSL and perilipin-1, shutting down lipolytic flux.<br><br><em>Distractor Traps:</em><br>&bull; A describes receptor stimulation, which would promote lipolysis, not inhibit it.<br>&bull; C is incorrect because insulin regulates lipolysis through reversible phosphorylation/dephosphorylation, not protein denaturation.<br>&bull; D is incorrect because insulin acts via intracellular signaling cascades, not direct binding to serum albumin."
      },
      {
        "q": "Why can white adipocytes not utilize the free glycerol produced by lipolysis to re-esterify fatty acids back into triacylglycerols?",
        "ch": [
          "Glycerol is completely impermeable to the adipocyte plasma membrane bilayer",
          "Adipocyte mitochondria oxidize all free glycerol directly into carbon dioxide",
          "Adipocytes lack glycerol kinase and cannot convert glycerol into glycerol-3-phosphate",
          "Glycerol is an allosteric inhibitor of diacylglycerol acyltransferase (DGAT)"
        ],
        "a": 2,
        "e": "<strong>Enzyme deficiency in adipose tissue:</strong> To synthesize triacylglycerols, the glycerol backbone must first be phosphorylated into glycerol-3-phosphate (G3P). Mature white adipocytes lack the enzyme glycerol kinase. Consequently, the free glycerol liberated by lipolysis cannot be phosphorylated in adipose tissue; instead, it is transported via aquaporin-7 into plasma and carried to the liver, which expresses abundant glycerol kinase. In white adipocytes, G3P required for TAG synthesis must be derived from glycolytic dihydroxyacetone phosphate (DHAP) via G3P dehydrogenase, making adipocyte fat synthesis strictly dependent on glucose availability.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because glycerol readily crosses adipocyte membranes through aquaglyceroporins (AQP7).<br>&bull; B is incorrect because glycerol must be phosphorylated to enter metabolic pathways.<br>&bull; D is incorrect because glycerol does not inhibit DGAT."
      },
      {
        "q": "How does lipoprotein lipase (LPL) activity differ fundamentally in its regulation between adipose tissue and cardiac muscle in the fasting state?",
        "ch": [
          "LPL is synthesized exclusively in cardiac muscle and is entirely absent from adipose tissue",
          "Fasting stimulates adipose LPL while completely shutting down cardiac LPL synthesis",
          "Both tissues inactivate LPL during fasting to force utilization of ketone bodies",
          "Fasting decreases adipose LPL expression but increases cardiac muscle LPL expression"
        ],
        "a": 3,
        "e": "<strong>Reciprocal tissue regulation of LPL:</strong> Lipoprotein lipase is regulated in an opposite, tissue-specific manner to route metabolic fuels appropriately. In the well-fed state (high insulin), adipose LPL is upregulated to store circulating triacylglycerols, while muscle LPL is low. During fasting or exercise (low insulin, high catecholamines), adipose LPL expression and endothelial presentation decrease markedly to halt fat storage. In contrast, cardiac and skeletal muscle LPL expression increases, and cardiac LPL has a much lower $K_m$ for TAGs. This ensures that circulating VLDL and chylomicrons are selectively routed to cardiac muscle to provide fatty acids for ATP generation.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because LPL is abundantly expressed in both adipose and muscle tissues.<br>&bull; B and C describe opposite or uniform regulation, missing the reciprocal physiological routing of lipid fuels."
      },
      {
        "q": "What is the primary physiological function of the lipid-droplet coat protein perilipin-1 (PLIN1) in the basal, unphosphorylated state?",
        "ch": [
          "It forms a physical barrier that prevents cytosolic lipases from accessing the lipid droplet core",
          "It catalyzes the rapid transfer of triacylglycerols across the mitochondrial inner membrane",
          "It recruits clathrin heavy chains to drive endocytosis of unesterified fatty acids into vesicles",
          "It converts fatty acids into acyl-carnitine esters to promote mitochondrial beta-oxidation"
        ],
        "a": 0,
        "e": "<strong>Barrier function of unphosphorylated perilipin-1:</strong> In the basal, resting state, unphosphorylated perilipin-1 coats the surface of the intracellular lipid droplet. It acts as a physical barrier that shields core triacylglycerols from cytosolic lipases. Furthermore, unphosphorylated perilipin-1 binds and sequesters the co-activator CGI-58, preventing it from activating ATGL. When PKA phosphorylates perilipin-1 on multiple serines, it undergoes a conformational change that releases CGI-58 and creates docking sites for phosphorylated HSL, opening access to the lipid droplet.<br><br><em>Distractor Traps:</em><br>&bull; B describes the carnitine palmitoyltransferase system, not a lipid droplet coat protein.<br>&bull; C describes clathrin-mediated endocytosis of membrane receptors.<br>&bull; D describes carnitine acyltransferases (CPT-1)."
      },
      {
        "q": "Why does administration of the beta-blocker propranolol completely block epinephrine-stimulated lipolysis in Table 1?",
        "ch": [
          "Propranolol acts as an irreversible suicide inhibitor of monoacylglycerol lipase",
          "Propranolol competitive antagonism prevents epinephrine from activating beta-receptors and G-alpha-s",
          "Propranolol enters the lipid droplet and precipitates free fatty acids into insoluble soaps",
          "Propranolol stimulates phosphodiesterase 3B directly without requiring insulin signaling"
        ],
        "a": 1,
        "e": "<strong>Mechanism of beta-adrenergic blockade:</strong> Epinephrine stimulates lipolysis by binding to $\\beta$-adrenergic receptors coupled to $\\text{G}_{\\alpha s}$, which activates adenylate cyclase. Propranolol is a competitive antagonist of $\\beta$-adrenergic receptors. By occupying the ligand-binding pocket, propranolol prevents epinephrine from binding and activating $\\text{G}_{\\alpha s}$. As shown in Table 1, in the presence of propranolol, cAMP levels remain at basal ($1.4\\text{ pmol/mg}$), HSL and perilipin-1 phosphorylation do not increase, and lipolysis is suppressed.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because propranolol is an adrenergic receptor antagonist, not an MGL inhibitor.<br>&bull; C is nonsensical because propranolol does not precipitate fatty acids into soaps.<br>&bull; D is incorrect because propranolol acts upstream at the plasma membrane receptor, not directly on PDE3B."
      }
    ]
  },
  {
    "id": "exam_bb90_6_p7",
    "sec": "B/B",
    "topic": "Odd-Chain Fatty Acid Oxidation & Succinyl-CoA Entry into the TCA Cycle",
    "sheet": 7,
    "label": "Biological and Biochemical Foundations of Biological Systems",
    "examId": "bb90_6",
    "passage": "<div class=\"ttl\">Passage 7 (Questions 37&ndash;42)</div>\n<p>While the overwhelming majority of dietary and endogenous fatty acids possess an even number of carbon atoms, odd-chain fatty acids (OCFAs, such as heptadecanoic acid, $\\text{C}17:0$) are ingested from dairy fats and ruminant meats or generated via microbial fermentation in the rumen and human colon. Even-chain fatty acids undergo successive cycles of mitochondrial $\\beta$-oxidation, yielding exclusively two-carbon acetyl-CoA units. In humans, because the pyruvate dehydrogenase complex reaction is irreversible ($\\text{Pyruvate} \\rightarrow \\text{Acetyl-CoA} + \\text{CO}_2$) and the two carbons entering the citric acid cycle as acetyl-CoA are released as two $\\text{CO}_2$ molecules prior to oxaloacetate, even-chain fatty acids cannot yield net glucose synthesis.</p>\n<p>In contrast, mitochondrial $\\beta$-oxidation of an odd-chain fatty acid proceeds identically through sequential two-carbon cleavages until the final round, which cleaves a five-carbon $\\beta$-ketoacyl-CoA intermediate into one molecule of acetyl-CoA and one three-carbon molecule of propionyl-CoA. Propionyl-CoA is converted into the citric acid cycle intermediate succinyl-CoA through a three-step anaplerotic pathway: (1) carboxylation of propionyl-CoA to (S)-methylmalonyl-CoA catalyzed by the biotin-dependent enzyme propionyl-CoA carboxylase (PCC), requiring ATP and $\\text{HCO}_3^-$; (2) epimerization to (R)-methylmalonyl-CoA by methylmalonyl-CoA epimerase; and (3) carbon-skeleton isomerization to succinyl-CoA catalyzed by methylmalonyl-CoA mutase (MCM), a mitochondrial enzyme requiring 5'-deoxyadenosylcobalamin (vitamin $\\text{B}_{12}$). Succinyl-CoA enters the citric acid cycle, where it can be converted to malate, exported to the cytosol, and converted into phosphoenolpyruvate by PEPCK, enabling odd-chain fatty acids to serve as anaplerotic substrates for net gluconeogenesis.</p>\n<p>Inborn errors of propionate metabolism cause severe metabolic acidoses. Propionic acidemia results from deficiency of PCC, whereas methylmalonic acidemia arises from mutations in the <em>MUT</em> gene or defects in cobalamin metabolism. Biochemical geneticists investigated primary fibroblast cultures isolated from patients with suspected inborn errors of organic acid metabolism bathed in medium supplemented with $[\\text{U-}^{13}\\text{C}]\\text{heptadecanoate}$ ($\\text{C}17:0$) (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Metabolism of [U-13C]heptadecanoate in patient skin fibroblast cultures</caption>\n  <thead>\n    <tr><th>Patient Cell Line</th><th>Genetic Disorder</th><th>Intracellular Propionyl-CoA ($\\mu\\text{M}$)</th><th>Intracellular Methylmalonyl-CoA ($\\mu\\text{M}$)</th><th>${}^{13}\\text{C}$-Succinyl-CoA Incorporation (% Control)</th><th>${}^{13}\\text{C}$-Glucose Production (% Control)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Control (Wild-Type)</td><td>Normal Function</td><td>4.2 &plusmn; 0.5</td><td>2.8 &plusmn; 0.3</td><td>100.0%</td><td>100.0%</td></tr>\n    <tr><td>Patient 1</td><td>Propionic Acidemia (<em>PCCA</em> null)</td><td>88.6 &plusmn; 6.4</td><td>< 0.1</td><td>< 1.0%</td><td>< 1.0%</td></tr>\n    <tr><td>Patient 2</td><td>Methylmalonic Acidemia (<em>MUT</em> null)</td><td>14.2 &plusmn; 1.2</td><td>94.8 &plusmn; 7.2</td><td>< 1.0%</td><td>< 1.0%</td></tr>\n    <tr><td>Patient 3</td><td>Cobalamin $cblA$ Defect (AdoCbl synthesis)</td><td>11.8 &plusmn; 1.0</td><td>82.4 &plusmn; 5.8</td><td>6.2%</td><td>5.8% (responsive to $\\text{B}_{12}$)</td></tr>\n    <tr><td>Patient 4</td><td>Biotinidase Deficiency</td><td>76.4 &plusmn; 5.2</td><td>< 0.1</td><td>4.5%</td><td>3.8% (responsive to biotin)</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "Why can the terminal three-carbon propionyl-CoA fragment of an odd-chain fatty acid contribute to net gluconeogenesis in humans, whereas even-chain fatty acids cannot?",
        "ch": [
          "Propionyl-CoA is converted to succinyl-CoA, providing net four-carbon anaplerotic flux to oxaloacetate",
          "Propionyl-CoA bypasses the mitochondria and is converted directly to glucose-6-phosphate in lysosomes",
          "Even-chain fatty acids lack carboxyl groups and therefore cannot enter the beta-oxidation spiral",
          "Propionyl-CoA is converted directly into fructose-1,6-bisphosphate via an aldol condensation"
        ],
        "a": 0,
        "e": "<strong>Anaplerotic gluconeogenesis from odd-chain fatty acids:</strong> During even-chain fatty acid oxidation, acetyl-CoA ($2\\text{ carbons}$) condenses with oxaloacetate ($4\\text{ carbons}$) to form citrate ($6\\text{ carbons}$). In the citric acid cycle, two carbons are decarboxylated as $2\\text{ CO}_2$ before oxaloacetate is regenerated, resulting in zero net carbon gain for gluconeogenesis. In contrast, the terminal propionyl-CoA ($3\\text{ carbons}$) from an odd-chain fatty acid is carboxylated to succinyl-CoA ($4\\text{ carbons}$). This enters the TCA cycle as a net anaplerotic replenishment of intermediates. Succinyl-CoA is oxidized to malate, which exits to the cytosol and is converted to phosphoenolpyruvate by PEPCK, enabling net de novo glucose synthesis.<br><br><em>Distractor Traps:</em><br>&bull; B is incorrect because propionyl-CoA metabolism is mitochondrial, not lysosomal.<br>&bull; C is incorrect because even-chain fatty acids are carboxylic acids and readily undergo $\\beta$-oxidation.<br>&bull; D is incorrect because propionyl-CoA is not converted into F1,6BP via direct aldol condensation."
      },
      {
        "q": "Based on the metabolite accumulation profile in Table 1, which enzymatic step is defective in Patient 2, who exhibits massive accumulation of methylmalonyl-CoA (94.8 uM) and low propionyl-CoA?",
        "ch": [
          "Carbamoyl phosphate synthetase I (CPS-I) in the urea cycle",
          "Methylmalonyl-CoA mutase (MCM), preventing conversion to succinyl-CoA",
          "Propionyl-CoA carboxylase (PCC), preventing carboxylation of propionate",
          "Medium-chain acyl-CoA dehydrogenase (MCAD), halting beta-oxidation"
        ],
        "a": 1,
        "e": "<strong>Diagnosis of methylmalonic acidemia from metabolite profiles:</strong> Patient 2 exhibits massive intracellular accumulation of methylmalonyl-CoA ($94.8\\ \\mu\\text{M}$) alongside severe depletion of downstream $^{13}\\text{C}$-succinyl-CoA and $^{13}\\text{C}$-glucose ($< 1.0\\%$). Because methylmalonyl-CoA is synthesized from propionyl-CoA by PCC and epimerase, upstream carboxylation is fully functional. The metabolic block lies at the subsequent step: the isomerization of (R)-methylmalonyl-CoA to succinyl-CoA catalyzed by methylmalonyl-CoA mutase (MCM). Mutations in the <em>MUT</em> gene cause methylmalonic acidemia.<br><br><em>Distractor Traps:</em><br>&bull; A describes urea cycle disorders.<br>&bull; C describes propionic acidemia (seen in Patient 1), where propionyl-CoA accumulates and methylmalonyl-CoA is undetectable ($< 0.1\\ \\mu\\text{M}$).<br>&bull; D describes MCAD deficiency, which causes hypoketotic hypoglycemia without methylmalonic aciduria."
      },
      {
        "q": "What essential organic cofactor is required by methylmalonyl-CoA mutase to generate the transient primary free radical that initiates the carbon-skeleton rearrangement?",
        "ch": [
          "Pyridoxal phosphate coenzyme (PLP, vitamin B6)",
          "Tetrahydrobiopterin cofactor complex (BH4)",
          "5'-Deoxyadenosylcobalamin (vitamin B12 coenzyme)",
          "Thiamine pyrophosphate coenzyme (TPP, vitamin B1)"
        ],
        "a": 2,
        "e": "<strong>Cofactor requirement of methylmalonyl-CoA mutase:</strong> Methylmalonyl-CoA mutase requires 5'-deoxyadenosylcobalamin (AdoCbl), an active coenzyme form of vitamin $\\text{B}_{12}$. The coenzyme coordinates a central cobalt atom ($\\text{Co}^{3+}$) with a unique carbon-cobalt covalent bond. During catalysis, homolytic cleavage of the weak $\\text{Co}-\\text{C}$ bond generates a $5'$-deoxyadenosyl carbon radical that abstracts a hydrogen atom from methylmalonyl-CoA, initiating a complex radical rearrangement that translocates the $\\text{COSCoA}$ group to form succinyl-CoA.<br><br><em>Distractor Traps:</em><br>&bull; A is the cofactor for transaminases and glycogen phosphorylase.<br>&bull; B is the cofactor for aromatic amino acid hydroxylases (phenylalanine hydroxylase).<br>&bull; D is the cofactor for pyruvate dehydrogenase and $\\alpha$-ketoglutarate dehydrogenase."
      },
      {
        "q": "How many total cycles of mitochondrial beta-oxidation are required to completely degrade one molecule of heptadecanoic acid (C17:0) into acetyl-CoA and propionyl-CoA?",
        "ch": [
          "8 cycles, yielding 8 acetyl-CoA and 1 propionyl-CoA",
          "7 cycles, yielding 7 acetyl-CoA and 2 propionyl-CoA",
          "9 cycles, yielding 9 acetyl-CoA and 0 propionyl-CoA",
          "7 cycles, yielding 7 acetyl-CoA and 1 propionyl-CoA"
        ],
        "a": 3,
        "e": "<strong>Calculation of beta-oxidation cycles for odd-chain fatty acids:</strong> Each round of $\\beta$-oxidation shortens the fatty acyl-CoA chain by two carbons, releasing one molecule of acetyl-CoA ($2\\text{ carbons}$). For a 17-carbon fatty acid ($\\text{C}17:0$): after 7 cycles, $7 \\times 2 = 14\\text{ carbons}$ have been cleaved as 7 molecules of acetyl-CoA. The remaining fragment is a three-carbon acyl-CoA: propionyl-CoA ($3\\text{ carbons}$). Therefore, exactly 7 cycles of $\\beta$-oxidation occur, yielding $7\\text{ acetyl-CoA} + 1\\text{ propionyl-CoA}$ ($7 \\times 2 + 3 = 17\\text{ carbons}$).<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly assumes an 8th cycle can occur; an 8th cycle would require an 18-carbon chain.<br>&bull; B erroneously suggests two propionyl-CoA molecules are formed.<br>&bull; C assumes complete degradation to acetyl-CoA, which is impossible for an odd-chain fatty acid."
      },
      {
        "q": "Why does Patient 4 (biotinidase deficiency) exhibit elevated propionyl-CoA and low methylmalonyl-CoA in Table 1, and why does high-dose oral biotin restore metabolic function?",
        "ch": [
          "Biotin is an allosteric inhibitor of methylmalonyl-CoA mutase in mitochondria",
          "Biotin acts as a general antioxidant that prevents non-enzymatic beta-oxidation",
          "Biotinidase recycles free biotin, an obligatory cofactor for propionyl-CoA carboxylase",
          "Biotin enters the citric acid cycle directly as a four-carbon anaplerotic substrate"
        ],
        "a": 2,
        "e": "<strong>Role of biotinidase and biotin in propionate metabolism:</strong> Propionyl-CoA carboxylase (PCC) is a biotin-dependent carboxylase. Biotin is covalently attached to an active-site lysine residue (forming biocytin). During normal protein turnover, biotinidase cleaves biocytin to release free biotin, which is then reattached to newly synthesized apocarboxylases by holocarboxylase synthetase. In biotinidase deficiency, free biotin is rapidly lost in urine, starving PCC of its cofactor. Without biotin, PCC cannot carboxylate propionyl-CoA to methylmalonyl-CoA. Supplying pharmacological high-dose free biotin ($10\\text{ to }20\\text{ mg/day}$) bypasses the recycling defect, restoring holocarboxylase synthesis and normalizing metabolic flux (Patient 4 shows $3.8\\%$ baseline rising upon biotin rescue).<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because biotin is a cofactor, not an inhibitor.<br>&bull; B describes general antioxidants (vitamins C and E).<br>&bull; D is incorrect because biotin is a catalytic prosthetic group, not a consumed anaplerotic fuel."
      },
      {
        "q": "In patients with untreated propionic acidemia or methylmalonic acidemia, secondary hyperammonemia frequently develops. What is the molecular mechanism underlying this secondary urea cycle impairment?",
        "ch": [
          "Propionyl-CoA phosphorylates and destroys argininosuccinate lyase in the cytosol",
          "Elevated propionate competitively inhibits intestinal absorption of dietary amino acids",
          "Propionyl-CoA and methylmalonate are converted into ammonia by enteric bacteria in gut",
          "Propionyl-CoA depletes free CoA and directly inhibits N-acetylglutamate synthase (NAGS)"
        ],
        "a": 3,
        "e": "<strong>Molecular pathogenesis of secondary hyperammonemia in organic acidemias:</strong> Propionyl-CoA accumulates massively when its downstream catabolism is blocked. Propionyl-CoA competes with acetyl-CoA and acts as a potent competitive inhibitor of $N$-acetylglutamate synthase (NAGS). NAGS synthesizes $N$-acetylglutamate (NAG), the obligatory allosteric activator of carbamoyl phosphate synthetase I (CPS-I), the rate-limiting committed enzyme of the urea cycle. Depletion of NAG halts CPS-I activity. Furthermore, trapping free coenzyme A as propionyl-CoA starves mitochondria of free CoA. Together, these effects shut down hepatic urea synthesis, resulting in life-threatening secondary hyperammonemia.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because argininosuccinate lyase is not regulated by propionyl phosphorylation.<br>&bull; B is incorrect because hyperammonemia arises from blocked ammonia detoxification, not amino acid malabsorption.<br>&bull; C is incorrect because organic acids do not contain nitrogen and cannot be degraded to ammonia."
      }
    ]
  },
  {
    "id": "exam_bb90_6_disc",
    "sec": "B/B",
    "topic": "B/B Standalone Discrete Questions",
    "sheet": 8,
    "label": "Biological and Biochemical Foundations of Biological Systems",
    "examId": "bb90_6",
    "passage": "<div class=\"ttl\">Item Set (Questions 43&ndash;52)</div>\n<p><strong>Directions:</strong> Questions 43&ndash;52 are standalone questions that are not based on a passage. Select the single best answer to each question.</p>",
    "qs": [
      {
        "d": true,
        "q": "Why cannot phytanic acid (a 20-carbon branched-chain fatty acid derived from dietary dairy and chlorophyll) undergo initial beta-oxidation, requiring peroxisomal alpha-oxidation instead?",
        "ch": [
          "A methyl group located at the beta-carbon sterically blocks the formation of a beta-ketoacyl intermediate",
          "Phytanic acid contains an odd number of carbon atoms that cannot cross the peroxisomal boundary membrane",
          "The carboxyl group of phytanic acid is permanently esterified to a purine ring within the matrix space",
          "Phytanic acid lacks alpha-hydrogens, completely preventing the enzymatic attachment of coenzyme A molecules"
        ],
        "a": 0,
        "e": "<strong>Biochemical mechanism of alpha-oxidation (Topic 564):</strong> Standard mitochondrial $\\beta$-oxidation requires an unsubstituted $\\beta$-carbon to allow oxidation to a $\\beta$-ketoacyl-CoA intermediate by acyl-CoA dehydrogenase. Phytanic acid ($3,7,11,15$-tetramethylhexadecanoic acid) possesses a methyl group substituted at carbon-3 (the $\\beta$-carbon). This $\\beta$-methyl group sterically and chemically blocks $\\beta$-oxidation. To bypass this obstruction, phytanic acid is routed to peroxisomes for $\\alpha$-oxidation catalyzed by phytanoyl-CoA hydroxylase (PhyH). Hydroxylation and decarboxylation at the $\\alpha$-carbon (carbon-2) removes one carbon as $\\text{CO}_2$, yielding pristanic acid, which has its methyl group on the $\\alpha$-carbon, leaving the new $\\beta$-carbon free for standard $\\beta$-oxidation. In Refsum disease, PhyH deficiency causes toxic phytanic acid accumulation.<br><br><em>Distractor Traps:</em><br>&bull; B is incorrect because phytanic acid has 20 carbons (an even number), and peroxisomes readily oxidize branched lipids.<br>&bull; C is incorrect because phytanic acid has a standard free carboxylic acid group.<br>&bull; D is incorrect because phytanic acid possesses two $\\alpha$-hydrogens at carbon-2."
      },
      {
        "d": true,
        "q": "When mitochondrial beta-oxidation is severely impaired (such as in MCAD deficiency or carnitine shuttle defects), which microsomal pathway is upregulated to oxidize fatty acids into dicarboxylic acids?",
        "ch": [
          "Peroxisomal beta-cleavage of very-long-chain fatty acid chains",
          "Cytochrome P450 4A-mediated omega-oxidation in the endoplasmic reticulum",
          "Cytosolic alpha-oxidation of branched-chain phytanic acid molecules",
          "Lysosomal acid lipase-mediated hydrolysis of core cholesteryl esters"
        ],
        "a": 1,
        "e": "<strong>Microsomal omega-oxidation of fatty acids (Topic 565):</strong> In the smooth endoplasmic reticulum, fatty acids can undergo $\\omega$-oxidation catalyzed by the cytochrome P450 4A family (CYP4A). Instead of oxidizing the carboxyl-proximal $\\beta$-carbon, CYP4A hydroxylates the terminal methyl group (the $\\omega$-carbon). Subsequent cytosolic dehydrogenase reactions oxidize the $\\omega$-alcohol to an aldehyde and then to a carboxylic acid, yielding a dicarboxylic acid (e.g., adipic, suberic, or sebacic acid). These dicarboxylic acids can undergo shortened $\\beta$-oxidation from both ends. Under conditions of impaired mitochondrial $\\beta$-oxidation (MCAD deficiency), $\\omega$-oxidation is heavily induced, leading to diagnostic dicarboxylic aciduria.<br><br><em>Distractor Traps:</em><br>&bull; A describes peroxisomal processing of $\\text{C} \\ge 22$ lipids, not dicarboxylic acid formation via $\\omega$-hydroxylation.<br>&bull; C describes $\\alpha$-oxidation, which yields odd-chain monocarboxylic acids, not dicarboxylic acids.<br>&bull; D describes lysosomal cholesterol storage metabolism."
      },
      {
        "d": true,
        "q": "What is the stoichiometric yield of acetoacetate and beta-hydroxybutyrate formed from the condensation of three molecules of mitochondrial acetyl-CoA during hepatic ketogenesis?",
        "ch": [
          "Three molecules of acetoacetate and three molecules of beta-hydroxybutyrate",
          "Two molecules of acetoacetate and one molecule of beta-hydroxybutyrate in liver",
          "One molecule of acetoacetate, which can be reversibly reduced to beta-hydroxybutyrate",
          "One molecule of acetone and two molecules of carbon dioxide released non-enzymatically"
        ],
        "a": 2,
        "e": "<strong>Stoichiometry of hepatic ketogenesis (Topic 566):</strong> Ketogenesis begins with two acetyl-CoA ($2 \\times 2\\text{C} = 4\\text{C}$) condensing to form acetoacetyl-CoA. A third acetyl-CoA ($2\\text{C}$) condenses via mitochondrial HMG-CoA synthase to produce HMG-CoA ($6\\text{C}$). HMG-CoA lyase then cleaves HMG-CoA into one molecule of acetyl-CoA ($2\\text{C}$, recycled) and one molecule of acetoacetate ($4\\text{C}$). Acetoacetate can then be reduced reversibly to $\\beta$-hydroxybutyrate by mitochondrial $\\beta$-hydroxybutyrate dehydrogenase consuming one NADH. Alternatively, a small fraction of acetoacetate undergoes slow non-enzymatic spontaneous decarboxylation to acetone and $\\text{CO}_2$. Thus, net synthesis yields one mole of four-carbon ketone body per three acetyl-CoA consumed (with one acetyl-CoA regenerated).<br><br><em>Distractor Traps:</em><br>&bull; A and B violate carbon conservation; three acetyl-CoA ($6\\text{ carbons}$) cannot yield multiple four-carbon ketone bodies.<br>&bull; D describes acetone decarboxylation, which is a minor non-enzymatic side product ($< 2\\%$), not the primary metabolic yield."
      },
      {
        "d": true,
        "q": "In an uncontrolled Type 1 diabetic presenting with diabetic ketoacidosis (DKA), which metabolic abnormality distinguishes this pathological state from physiological fasting ketosis?",
        "ch": [
          "A complete absence of circulating free fatty acids due to severe hyperinsulinism",
          "Profound metabolic alkalosis accompanied by massive hypoventilation in the patient",
          "Total suppression of hepatic gluconeogenesis and low blood glucose concentrations",
          "Severe hyperglycemia and high-anion-gap acidosis from unchecked lipolysis and gluconeogenesis"
        ],
        "a": 3,
        "e": "<strong>Pathophysiology of DKA versus fasting ketosis (Topic 567):</strong> In physiological fasting ketosis, low insulin and modest glucagon maintain ketone levels between $1\\text{ to }5\\text{ mM}$, and blood glucose remains normal ($70\\text{ to }90\\text{ mg/dL}$) because basal insulin prevents runaway lipolysis. In diabetic ketoacidosis (DKA), absolute insulin deficiency paired with severe glucagon excess completely removes the brake on adipose lipolysis. A massive deluge of free fatty acids enters hepatic ketogenesis, driving plasma acetoacetate and $\\beta$-hydroxybutyrate $> 15\\text{ to }25\\text{ mM}$. The accumulation of these organic anions causes a severe high-anion-gap metabolic acidosis ($\\text{pH} < 7.2$, serum bicarbonate $< 15\\text{ mEq/L}$). Concurrently, uninhibited hepatic gluconeogenesis and lack of peripheral glucose uptake cause severe hyperglycemia ($> 300\\text{ to }500\\text{ mg/dL}$) and osmotic diuresis.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because DKA features massive circulating free fatty acids due to absent insulin.<br>&bull; B is incorrect because DKA is a metabolic acidosis, which triggers compensatory Kussmaul hyperventilation (respiratory alkalosis), not hypoventilation.<br>&bull; C describes the opposite of DKA, which features rampant gluconeogenesis and severe hyperglycemia."
      },
      {
        "d": true,
        "q": "During amino acid catabolism, what common keto-acid functions as the universal amino group acceptor in transamination reactions catalyzed by ALT and AST?",
        "ch": [
          "Alpha-ketoglutarate, which is converted into L-glutamate",
          "Oxaloacetate, which is converted directly into fumarate",
          "Pyruvate, which is converted directly into acetyl-CoA",
          "Citrate, which is converted directly into isocitrate"
        ],
        "a": 0,
        "e": "<strong>Role of alpha-ketoglutarate in transamination (Topic 568):</strong> Transaminases (aminotransferases) utilize pyridoxal phosphate (PLP) to transfer an $\\alpha$-amino group from an amino acid donor onto an $\\alpha$-keto acid acceptor. In virtually all mammalian transaminations, $\\alpha$-ketoglutarate functions as the universal amino group acceptor: $\\text{Amino Acid} + \\alpha\\text{-Ketoglutarate} \\rightleftharpoons \\alpha\\text{-Keto Acid} + \\text{L-Glutamate}$. Specifically, alanine aminotransferase (ALT) transfers alanine's amino group to $\\alpha$-ketoglutarate, producing pyruvate and glutamate. Aspartate aminotransferase (AST) transfers aspartate's amino group to $\\alpha$-ketoglutarate, producing oxaloacetate and glutamate. Glutamate acts as the central amino reservoir in the mitochondrial matrix.<br><br><em>Distractor Traps:</em><br>&bull; B describes the product of aspartate transamination, not the universal amino group acceptor.<br>&bull; C describes the carbon skeleton produced when alanine is transaminated.<br>&bull; D describes a TCA cycle intermediate that does not participate in amino transfer."
      },
      {
        "d": true,
        "q": "Mitochondrial glutamate dehydrogenase (GDH) catalyzes the oxidative deamination of glutamate to regenerate alpha-ketoglutarate. What inorganic nitrogen product is released by this reaction?",
        "ch": [
          "Urea diamide (H2N-CO-NH2)",
          "Free ammonium ion (NH4+)",
          "Nitric oxide radical (NO)",
          "Molecular nitrogen gas (N2)"
        ],
        "a": 1,
        "e": "<strong>Oxidative deamination catalyzed by glutamate dehydrogenase (Topic 569):</strong> Glutamate dehydrogenase (GDH) resides in the mitochondrial matrix and catalyzes the reversible oxidative deamination of L-glutamate: $\\text{L-Glutamate} + \\text{NAD(P)}^+ + \\text{H}_2\\text{O} \\rightleftharpoons \\alpha\\text{-Ketoglutarate} + \\text{NH}_4^+ + \\text{NAD(P)H} + \\text{H}^+$. This reaction releases free ammonium ion ($\\text{NH}_4^+$), which immediately enters the urea cycle by reacting with bicarbonate and ATP via carbamoyl phosphate synthetase I (CPS-I). GDH is allosterically activated by ADP and GDP (signaling low cellular energy) and inhibited by ATP and GTP.<br><br><em>Distractor Traps:</em><br>&bull; A describes the final non-toxic diamide product excreted by the kidneys after the entire four-step urea cycle.<br>&bull; C is synthesized from arginine by nitric oxide synthase (NOS).<br>&bull; D is molecular nitrogen gas, which is fixed by prokaryotic nitrogenases, not released by human enzymes."
      },
      {
        "d": true,
        "q": "What is the committed, rate-limiting step of the urea cycle, and what allosteric activator is obligatorily required for its catalytic activity?",
        "ch": [
          "Arginase-1, which requires allosteric activation by unesterified cholesterol ligands",
          "Ornithine transcarbamoylase, which requires allosteric activation by citrulline pools",
          "Carbamoyl phosphate synthetase I (CPS-I), requiring N-acetylglutamate activation",
          "Argininosuccinate synthetase, which requires allosteric activation by fumarate ions"
        ],
        "a": 2,
        "e": "<strong>Committed step of the urea cycle (Topic 570):</strong> The committed, rate-limiting step of hepatic urea synthesis is catalyzed by carbamoyl phosphate synthetase I (CPS-I) in the mitochondrial matrix: $\\text{NH}_4^+ + \\text{HCO}_3^- + 2\\text{ ATP} \\rightarrow \\text{Carbamoyl Phosphate} + 2\\text{ ADP} + \\text{P}_i$. CPS-I is completely inactive in the absence of its obligate allosteric activator, $N$-acetylglutamate (NAG). NAG is synthesized by NAGS from acetyl-CoA and glutamate, an activation signal triggered by elevated arginine (indicating protein abundance).<br><br><em>Distractor Traps:</em><br>&bull; A describes the final cytosolic step of the urea cycle that releases urea, which is regulated by substrate availability, not cholesterol.<br>&bull; B describes the second mitochondrial step catalyzed by OTC, which does not require citrulline activation.<br>&bull; D describes the cytosolic condensation of citrulline with aspartate."
      },
      {
        "d": true,
        "q": "Which enzymatic reactions of the five-step hepatic urea cycle occur in the mitochondrial matrix, and which occur in the cytosol?",
        "ch": [
          "All five reactions occur strictly within the mitochondrial matrix space",
          "All five reactions occur strictly within the cytoplasmic compartment space",
          "CPS-I and arginase are matrix enzymes; OTC and ASS reside in the cytosol",
          "CPS-I and OTC occur in the matrix; ASS, ASL, and arginase occur in the cytosol"
        ],
        "a": 3,
        "e": "<strong>Subcellular compartmentalization of the urea cycle (Topic 571):</strong> The urea cycle spans two subcellular compartments in hepatocytes: (1) Formation of carbamoyl phosphate by CPS-I occurs in the mitochondrial matrix; (2) Condensation of carbamoyl phosphate with ornithine to form citrulline by ornithine transcarbamoylase (OTC) also occurs in the matrix. Citrulline is then transported across the inner mitochondrial membrane into the cytosol via the ORNT1 antiporter. In the cytosol, three steps occur: (3) Argininosuccinate synthetase (ASS) condenses citrulline with aspartate to form argininosuccinate; (4) Argininosuccinate lyase (ASL) cleaves argininosuccinate into arginine and fumarate; and (5) Arginase-1 hydrolyzes arginine into urea and ornithine. Ornithine recycles back into the matrix.<br><br><em>Distractor Traps:</em><br>&bull; A and B fail to recognize that the urea cycle is compartmentalized across mitochondria and cytoplasm.<br>&bull; C incorrectly places arginase in the matrix; arginase-1 is strictly cytosolic."
      },
      {
        "d": true,
        "q": "An infant presents with lethargy, hyperventilation, and extreme hyperammonemia. Laboratory analysis reveals elevated urinary orotic acid and low plasma citrulline. This clinical presentation is diagnostic for:",
        "ch": [
          "X-linked ornithine transcarbamoylase (OTC) enzyme deficiency",
          "Autosomal recessive carbamoyl phosphate synthetase I deficiency",
          "Classic phenylketonuria due to phenylalanine hydroxylase defect",
          "Medium-chain acyl-CoA dehydrogenase (MCAD) enzyme deficiency"
        ],
        "a": 0,
        "e": "<strong>Diagnostic differentiation of OTC deficiency (Topic 572):</strong> Ornithine transcarbamoylase (OTC) deficiency is the most common urea cycle disorder and the only one inherited in an X-linked recessive pattern. Blocked OTC activity leads to accumulation of carbamoyl phosphate in the mitochondrial matrix. Excess carbamoyl phosphate spills out into the cytosol, where it enters the pyrimidine synthesis pathway via cytosolic carbamoyl phosphate synthetase II (CPS-II), driving the massive overproduction and urinary excretion of orotic acid (orotic aciduria). In contrast, CPS-I deficiency also causes hyperammonemia but exhibits low or absent orotic acid because carbamoyl phosphate cannot be formed.<br><br><em>Distractor Traps:</em><br>&bull; B causes severe hyperammonemia but with low orotic acid.<br>&bull; C is a defect in phenylalanine catabolism causing elevated phenylalanine and phenylketones, not hyperammonemia or orotic aciduria.<br>&bull; D is a fatty acid oxidation disorder characterized by hypoketotic hypoglycemia."
      },
      {
        "d": true,
        "q": "Which two amino acids are exclusively ketogenic, meaning their carbon skeletons yield exclusively acetyl-CoA or acetoacetate and can never contribute to net gluconeogenesis?",
        "ch": [
          "Alanine and glutamine amino acids",
          "Leucine and lysine amino acids",
          "Aspartate and glutamate amino acids",
          "Glycine and serine amino acids"
        ],
        "a": 1,
        "e": "<strong>Exclusively ketogenic amino acids (Topic 573):</strong> Among the twenty canonical amino acids, exactly two are exclusively ketogenic: leucine and lysine. Their catabolic pathways produce exclusively acetyl-CoA and/or acetoacetate, neither of which can provide net carbon for gluconeogenesis in humans. Five amino acids are both glucogenic and ketogenic (tryptophan, tyrosine, threonine, isoleucine, and phenylalanine: mnemonic 'PITTT'). The remaining thirteen amino acids are purely glucogenic (yielding pyruvate, $\\alpha$-ketoglutarate, succinyl-CoA, fumarate, or oxaloacetate).<br><br><em>Distractor Traps:</em><br>&bull; A consists of purely glucogenic amino acids (alanine forms pyruvate; glutamine forms $\\alpha$-ketoglutarate).<br>&bull; C consists of purely glucogenic amino acids (aspartate forms oxaloacetate; glutamate forms $\\alpha$-ketoglutarate).<br>&bull; D consists of purely glucogenic amino acids (glycine and serine form pyruvate)."
      }
    ]
  }
];

if (typeof window !== 'undefined') {
  window.EXAM_BB90_6 = EXAM_BB90_6;
}
if (typeof globalThis !== 'undefined') {
  globalThis.EXAM_BB90_6 = EXAM_BB90_6;
}
