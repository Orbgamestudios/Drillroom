# Passage 6: Topic 545 — Malate-Aspartate Shuttle vs Glycerol-3-Phosphate Shuttle
# Answer keys: 2 (C), 1 (B), 3 (D), 0 (A), 3 (D), 1 (B)

p6_data = {
  "id": "exam_bb90_5_p6",
  "sec": "B/B",
  "topic": "Malate-Aspartate Shuttle vs Glycerol-3-Phosphate Shuttle",
  "sheet": None,
  "label": "Biological and Biochemical Foundations of Living Systems",
  "examId": "bb90_5",
  "passage": """<div class="ttl">Passage 6 (Questions 31&ndash;6)</div>
<p>Glycolytic degradation of D-glucose produces two molecules of NADH in the cytoplasm at the glyceraldehyde-3-phosphate dehydrogenase (GAPDH) step. Because the inner mitochondrial membrane is strictly impermeable to $\\text{NAD}^+$ and NADH, cells utilize specialized substrate shuttles to transfer reducing equivalents into the mitochondrial matrix to regenerate cytosolic $\\text{NAD}^+$ and maximize aerobic ATP generation.</p>
<p>In cardiac muscle, liver, and kidneys, the malate-aspartate shuttle predominates. Cytosolic malate dehydrogenase (cMDH) reduces oxaloacetate to L-malate, oxidizing cytosolic NADH to $\\text{NAD}^+$. Malate enters the matrix via the malate-$\\alpha$-ketoglutarate antiporter in exchange for matrix $\\alpha$-ketoglutarate. Mitochondrial malate dehydrogenase (mMDH) re-oxidizes malate to oxaloacetate, producing matrix NADH, which transfers electrons into Complex I. Because oxaloacetate cannot cross the inner mitochondrial membrane, mitochondrial aspartate aminotransferase (mAST) transaminates oxaloacetate with glutamate to form aspartate and $\\alpha$-ketoglutarate. The glutamate-aspartate antiporter (Aralar1) electrogenically exports aspartate into the intermembrane space in exchange for cytosolic glutamate and a proton, driven by the membrane potential ($\\Delta\\Psi_m$), while cytosolic AST regenerates oxaloacetate.</p>
<p>In contrast, fast-twitch skeletal muscle and brain utilize the glycerol-3-phosphate shuttle. Cytosolic glycerol-3-phosphate dehydrogenase (cGPDH) reduces dihydroxyacetone phosphate (DHAP) to glycerol-3-phosphate (G3P), oxidizing cytosolic NADH. Mitochondrial glycerol-3-phosphate dehydrogenase (mGPDH) is anchored to the outer face of the inner mitochondrial membrane; its enzyme-bound $\\text{FAD}$ prosthetic group re-oxidizes G3P back to DHAP without requiring metabolite transport across the membrane. Reduced $\\text{FADH}_2$ donates electrons directly to ubiquinone ($Q$), feeding electrons into Complex III.</p>
<p>Researchers examined metabolic flux in murine myocardial and gastrocnemius preparations treated with aminooxyacetate (AOA, a transaminase inhibitor) or flavone sulfur conjugate (FSG, an mGPDH inhibitor) (Table 1).</p>
<table class="tbl">
  <caption>Table 1 Respiration, cytosolic redox balance, and net ATP yields in tissue preparations</caption>
  <thead>
    <tr><th>Tissue</th><th>Treatment / Inhibitor</th><th>Oxygen Consumption (nmol $\\text{O}_2$/min/mg)</th><th>Cytosolic $\\text{NAD}^+/\\text{NADH}$</th><th>Net ATP Yield (mol ATP / mol Glucose)</th><th>Shuttle Inhibition (%)</th></tr>
  </thead>
  <tbody>
    <tr><td>Myocardium</td><td>Vehicle (Control)</td><td>185 &plusmn; 8</td><td>720 &plusmn; 25</td><td>31.8 &plusmn; 0.4</td><td>0%</td></tr>
    <tr><td>Myocardium</td><td>Aminooxyacetate (AOA, 5 mM)</td><td>28 &plusmn; 3</td><td>45 &plusmn; 4</td><td>2.1 &plusmn; 0.2</td><td>85%</td></tr>
    <tr><td>Myocardium</td><td>mGPDH Inhibitor (FSG, 20 $\\mu\\text{M}$)</td><td>182 &plusmn; 7</td><td>710 &plusmn; 22</td><td>31.5 &plusmn; 0.4</td><td>2%</td></tr>
    <tr><td>Gastrocnemius</td><td>Vehicle (Control)</td><td>165 &plusmn; 7</td><td>680 &plusmn; 24</td><td>29.8 &plusmn; 0.3</td><td>0%</td></tr>
    <tr><td>Gastrocnemius</td><td>Aminooxyacetate (AOA, 5 mM)</td><td>160 &plusmn; 6</td><td>665 &plusmn; 20</td><td>29.5 &plusmn; 0.3</td><td>3%</td></tr>
    <tr><td>Gastrocnemius</td><td>mGPDH Inhibitor (FSG, 20 $\\mu\\text{M}$)</td><td>32 &plusmn; 3</td><td>52 &plusmn; 5</td><td>2.0 &plusmn; 0.2</td><td>81%</td></tr>
  </tbody>
</table>""",
  "qs": [
    {
      "q": "Which biochemical feature explains why complete glucose oxidation yields approximately 32 ATP in myocardium but only 30 ATP in gastrocnemius muscle?",
      "ch": [
        "Skeletal muscle lacks pyruvate dehydrogenase, forcing glucose-derived pyruvate into anaerobic homolactic fermentation.",
        "Cardiac mitochondria express a specialized ATP synthase c-ring that requires fewer protons per mechanical revolution.",
        "Cardiac tissue transfers electrons to matrix NAD+ via Complex I, whereas skeletal muscle delivers electrons to FAD and ubiquinone.",
        "Skeletal muscle consumes two additional ATP equivalents during the initial hexokinase phosphorylation of free glucose."
      ],
      "a": 2,
      "e": "<strong>ATP yield differences between reducing equivalent shuttles:</strong> In cardiac tissue, the malate-aspartate shuttle transfers electrons from cytosolic NADH to matrix $\\text{NAD}^+$. The resulting matrix NADH enters the electron transport chain at Complex I, which translocates 10 protons per electron pair ($4\\text{ H}^+$ at Complex I, $4\\text{ H}^+$ at Complex III, $2\\text{ H}^+$ at Complex IV), yielding $\\sim 2.5\\text{ ATP}$ per pair of electrons. Two cytosolic NADH per glucose thus generate $2 \\times 2.5 = 5.0\\text{ ATP}$, producing a net theoretical total of $32\\text{ ATP}$ per mole of glucose. In contrast, fast-twitch skeletal muscle relies on the glycerol-3-phosphate shuttle, where mGPDH transfers electrons to an enzyme-bound FAD group and subsequently to ubiquinone ($Q$), bypassing Complex I entirely. These electrons enter at Complex III and pump only 6 protons per electron pair ($4\\text{ H}^+$ at Complex III, $2\\text{ H}^+$ at Complex IV), yielding $\\sim 1.5\\text{ ATP}$ per electron pair ($2 \\times 1.5 = 3.0\\text{ ATP}$), producing a net total of $30\\text{ ATP}$ per glucose.<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly claims skeletal muscle lacks pyruvate dehydrogenase; skeletal muscle possesses active PDH for aerobic respiration during oxidative metabolism.<br>&bull; B invents a tissue-specific difference in the stoichiometry of the ATP synthase $c$-ring in mammalian tissues.<br>&bull; D invents extra ATP consumption during hexokinase activation; hexokinase consumes exactly one ATP per glucose in all mammalian tissues."
    },
    {
      "q": "Based on Table 1, why does aminooxyacetate (AOA) severely inhibit oxygen consumption in cardiac tissue while having virtually no effect on skeletal muscle?",
      "ch": [
        "AOA inhibits pyruvate carboxylase, which is an obligate anaplerotic enzyme in myocardium but absent in skeletal muscle.",
        "Cardiac cells depend on aspartate aminotransferase for the malate shuttle, whereas skeletal muscle relies on mGPDH.",
        "AOA selectively disrupts outer membrane porins in cardiac mitochondria, preventing cytosolic ADP entry into the IMS.",
        "Skeletal muscle metabolizes AOA into succinyl-CoA, thereby bypassing transaminase blockade to fuel the citric acid cycle."
      ],
      "a": 1,
      "e": "<strong>Differential shuttle dependence and transaminase inhibition by AOA:</strong> Aminooxyacetate (AOA) is a classic carbonyl-reacting competitive inhibitor of pyridoxal 5'-phosphate (PLP)-dependent transaminases (aminotransferases). In myocardial tissue, the malate-aspartate shuttle is the predominant mechanism for re-oxidizing glycolytic NADH. Because the inner mitochondrial membrane lacks an oxaloacetate transporter, transamination by aspartate aminotransferase (AST) is strictly required to convert oxaloacetate to aspartate for export. Blocking AST with AOA collapses the shuttle, depleting cytosolic $\\text{NAD}^+$ (from $720$ down to $45$), suppressing respiration by $85\\%$, and dropping ATP yield to the anaerobic baseline ($2.1\\text{ mol ATP/mol glucose}$). In contrast, fast-twitch skeletal muscle relies on the glycerol-3-phosphate shuttle, which does not require transamination reactions, rendering skeletal muscle respiration resistant to AOA ($3\\%$ inhibition).<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly identifies pyruvate carboxylase as the target of AOA; AOA targets PLP-dependent transaminases, not biotin-dependent carboxylases.<br>&bull; C invents outer membrane porin disruption; AOA does not disrupt mitochondrial membrane architecture or nucleotide translocases.<br>&bull; D invents metabolism of AOA into succinyl-CoA; AOA is an inhibitor, not an anaplerotic fuel source."
    },
    {
      "q": "What driving force energizes the export of aspartate from the mitochondrial matrix to the cytosol via the glutamate-aspartate antiporter (Aralar1)?",
      "ch": [
        "Direct enzymatic hydrolysis of one mole of matrix ATP per each exported aspartate anion across the membrane.",
        "An inward electrochemical gradient of inorganic phosphate maintained by the inner mitochondrial symporter.",
        "Passive electroneutral exchange with cytosolic alpha-ketoglutarate along its chemical concentration gradient.",
        "The electrical membrane potential (ΔΨm), which drives the inward co-transport of a proton with glutamate."
      ],
      "a": 3,
      "e": "<strong>Electrogenic transport mechanism of the glutamate-aspartate carrier:</strong> The mitochondrial glutamate-aspartate carrier (Aralar1/Citrin, SLC25A12/13) mediates the export of aspartate from the matrix in exchange for cytosolic glutamate plus a proton ($H^+$). At physiological matrix and cytosolic pH ($\\sim 7.8$ and $7.2$), aspartate and glutamate both exist predominantly as univalent anions ($\\text{Asp}^-$ and $\\text{Glu}^-$). However, because glutamate is co-transported inward with a proton (as a neutral species or zwitterion), the net exchange involves the inward movement of one positive charge with glutamate against the extrusion of univalent $\\text{Asp}^-$, or equivalent to the net movement of one negative charge outward. Consequently, the inward-negative mitochondrial membrane potential ($\\Delta\\Psi_m$, interior negative) electrogenically drives the unidirectional export of aspartate against steep concentration gradients.<br><br><em>Distractor Traps:</em><br>&bull; A describes primary active transport via an ATP-binding cassette or P-type ATPase; Aralar1 is a secondary active carrier that does not hydrolyze ATP.<br>&bull; B describes the inorganic phosphate symporter, which transports $\\text{H}_2\\text{PO}_4^-$ and $H^+$, but does not drive aspartate export.<br>&bull; C describes electroneutral exchange; the malate-$\\alpha$-ketoglutarate carrier is electroneutral, but the glutamate-aspartate carrier is obligatorily electrogenic."
    },
    {
      "q": "What structural localization of mitochondrial glycerol-3-phosphate dehydrogenase (mGPDH) enables it to operate without a metabolite transport carrier?",
      "ch": [
        "It is anchored to the outer leaflet of the inner membrane facing the IMS, allowing direct access to cytosolic G3P.",
        "It resides freely dissolved within the matrix space, where it directly oxidizes incoming glycolytic intermediates.",
        "It is embedded in the outer mitochondrial membrane, where it forms an open channel for cytosolic NADH translocation.",
        "It forms an integral component of the cristae junction complex, transferring electrons directly to cytochrome c."
      ],
      "a": 0,
      "e": "<strong>Topological localization of mitochondrial glycerol-3-phosphate dehydrogenase:</strong> Mitochondrial GPDH (mGPDH, encoded by GPD2) is an integral peripheral monotopic membrane flavoprotein embedded in the outer leaflet of the inner mitochondrial membrane, with its catalytic domain projecting directly into the intermembrane space (IMS). Because the outer mitochondrial membrane contains large, nonspecific voltage-dependent anion channels (VDAC / porins), cytosolic glycerol-3-phosphate (G3P) and dihydroxyacetone phosphate (DHAP) diffuse freely through the outer membrane into the IMS. Thus, mGPDH oxidizes G3P directly in the IMS without requiring any transport proteins to cross the impermeable inner mitochondrial membrane. The electrons are passed from G3P to an enzyme-bound FAD cofactor, through an internal iron-sulfur center, and into the lipophilic ubiquinone pool residing inside the inner membrane lipid bilayer.<br><br><em>Distractor Traps:</em><br>&bull; B erroneously places mGPDH in the mitochondrial matrix, which would require an inner membrane G3P transporter that mammalian cells lack.<br>&bull; C places mGPDH in the outer mitochondrial membrane and invents an open channel for NADH; the inner membrane remains strictly impermeable to NADH.<br>&bull; D invents cristae junction localization and direct electron transfer to cytochrome $c$; mGPDH transfers electrons to ubiquinone, not cytochrome $c$."
    },
    {
      "q": "If skeletal muscle mitochondria are incubated with dihydroxyacetone phosphate and cytosolic NADH, which electron transport complex is the first to accept these reducing equivalents?",
      "ch": [
        "Complex I (NADH:ubiquinone oxidoreductase), via electron transfer to FMN",
        "Complex II (succinate:ubiquinone oxidoreductase), via iron-sulfur centers",
        "Complex IV (cytochrome c oxidase), via direct reduction of copper centers",
        "Complex III (cytochrome bc1 complex), via reduction by the ubiquinol pool"
      ],
      "a": 3,
      "e": "<strong>Electron entry pathway of the glycerol-3-phosphate shuttle:</strong> When cytosolic NADH is generated, cytosolic GPDH reduces DHAP to glycerol-3-phosphate. At the inner mitochondrial membrane, mGPDH re-oxidizes glycerol-3-phosphate to DHAP, transferring two electrons to its enzyme-bound FAD prosthetic group. Reduced $\\text{FADH}_2$ then transfers these electrons directly into the inner membrane ubiquinone pool, reducing ubiquinone ($Q$) to ubiquinol ($\\text{QH}_2$). Ubiquinol diffuses laterally through the lipid bilayer to Complex III (cytochrome $bc_1$ complex), which is the first respiratory complex to accept these electrons and oxidize $\\text{QH}_2$ via the Q-cycle mechanism. Complexes I and II are completely bypassed.<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly identifies Complex I; cytosolic NADH cannot access Complex I, and the glycerol-3-phosphate shuttle bypasses Complex I entirely.<br>&bull; B refers to Complex II; Complex II oxidizes succinate, not glycerol-3-phosphate, although both feed electrons into the ubiquinone pool.<br>&bull; C refers to Complex IV, which receives electrons from cytochrome $c$ downstream of Complex III, not directly from ubiquinol."
    },
    {
      "q": "Under intense anaerobic exercise when skeletal muscle shuttle capacity is exceeded, how is cytosolic NAD+ regenerated to prevent the arrest of glycolysis?",
      "ch": [
        "Cytosolic malate dehydrogenase reduces oxaloacetate to malate, regenerating NAD+ while synthesizing glycogen.",
        "Lactate dehydrogenase reduces pyruvate to L-lactate, transferring electrons from cytosolic NADH to pyruvate.",
        "Pyruvate carboxylase carboxylates pyruvate to oxaloacetate, oxidizing cytosolic NADH through biotin linkage.",
        "Alcohol dehydrogenase reduces acetyl-CoA to ethanol, regenerating NAD+ to maintain high glycolytic throughput."
      ],
      "a": 1,
      "e": "<strong>Lactate dehydrogenase and anaerobic regeneration of cytosolic NAD+:</strong> During high-intensity anaerobic muscle contraction, the rate of glycolytic flux exceeds the mitochondrial capacity to re-oxidize cytosolic NADH via the glycerol-3-phosphate shuttle and electron transport chain. Without rapid regeneration of $\\text{NAD}^+$, the rate-limiting glyceraldehyde-3-phosphate dehydrogenase (GAPDH) step would halt, shutting down glycolytic ATP generation. To sustain glycolysis, skeletal muscle fibers utilize lactate dehydrogenase (specifically the muscle-type LDH-M / LDH-5 isozyme) to catalyze the rapid reduction of pyruvate to L-lactate: $\\text{pyruvate} + \\text{NADH} + \\text{H}^+ \\rightleftharpoons \\text{L-lactate} + \\text{NAD}^+$. This reaction stoichiometrically re-oxidizes cytosolic NADH to $\\text{NAD}^+$, enabling continuous glycolytic ATP production independent of mitochondrial oxygen availability.<br><br><em>Distractor Traps:</em><br>&bull; A describes malate dehydrogenase running in reverse, which does not regenerate $\\text{NAD}^+$ unless accompanied by shuttle export, and malate does not directly synthesize glycogen in muscle.<br>&bull; C misidentifies pyruvate carboxylase as an NADH-oxidizing enzyme; pyruvate carboxylase is a mitochondrial matrix enzyme that consumes ATP and $\\text{CO}_2$ without oxidizing NADH.<br>&bull; D describes alcoholic fermentation, which occurs in yeast and certain microorganisms, but does not occur in mammalian physiology."
    }
  ]
}
