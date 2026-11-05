# -*- coding: utf-8 -*-
"""
Suite 1 Bio/Biochem 90 Overhaul: Passages 1 to 4 (Questions 1 to 24)
5-Gate Review Protocol calibration
"""
import re

def validate_questions(qs_list, start_idx=1):
    for i, q in enumerate(qs_list):
        num = start_idx + i
        ans = q["a"]
        ch = q["ch"]
        lens = [len(c) for c in ch]
        
        ratio = max(lens) / min(lens) if min(lens) > 0 else 999
        assert ratio <= 1.0801, f"Q{num} length ratio violated: {ratio:.3f} (lens: {lens})"
        assert ans != lens.index(max(lens)), f"Q{num} correct choice is strictly longest! ans={ans}, lens={lens}"

        e = q["e"]
        assert "<strong>[Governing Principle:" in e, f"Q{num} missing Governing Principle tag"
        assert "<em>Distractor Traps:</em><br>&bull;" in e, f"Q{num} missing Distractor Traps tag"
        other_letters = [chr(65+j) for j in range(4) if j != ans]
        for ol in other_letters:
            assert f"&bull; {ol} (" in e, f"Q{num} missing autopsy for {ol}"
    print(f"Validated {len(qs_list)} questions starting at Q{start_idx} successfully!")

# Passage 1: CRISPR-Cas9 genome editing and DNA repair pathways (exam_bb90_p1)
# Key: D, C, A, B, D, C
p1_qs = [
    {
        "q": "Based on the data in Table 1, which Cas9 endonuclease configuration achieved the most clinically favorable therapeutic index, defined as maximizing on-target homology-directed repair while suppressing collateral genotoxicity at homologous loci?",
        "ch": [
            "WT-Cas9 paired with a full-length 20-nt guide yielding 78.4% target cleavage at the locus",
            "WT-Cas9 paired with an 18-nt truncated guide demonstrating 31.5% repair yield in trials",
            "eCas9 paired with an 18-nt truncated guide minimizing off-target insertions in HSPCs",
            "eCas9 paired with a full-length 20-nt guide preserving 33.0% repair efficiency in cells"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: CRISPR-Cas9 Specificity and Therapeutic Index Optimization]</strong><br><br>1. <em>Identify Clinical Criteria:</em> A successful clinical gene therapy for sickle cell anemia requires robust target correction (>30% HDR efficiency) while eliminating potentially oncogenic off-target double-strand breaks at the paralogous <i>HBD</i> locus.<br>2. <em>Evaluate Empirical Conditions:</em> Condition 1 (WT-Cas9 + 20-nt sgRNA) produces high on-target cleavage (78.4%) and acceptable HDR (28.2%), but incurs a severe 14.6% off-target lesion rate at <i>HBD</i>. Condition 2 reduces off-target lesions to 1.8% with 31.5% HDR. Condition 3 (eCas9 + 20-nt sgRNA) delivers 33.0% HDR (the highest among all conditions) while reducing <i>HBD</i> off-target indels to a negligible 0.2% (a 73-fold reduction vs WT-Cas9). In contrast, Condition 4 (eCas9 + 18-nt sgRNA) causes excessive loss of binding stability, dropping HDR to an inadequate 18.5%.<br>3. <em>Derive Optimal Configuration:</em> Condition 3 uniquely maximizes HDR above the 30% threshold while achieving near-complete abolition of off-target genotoxicity, establishing the premier therapeutic index.<br><br><em>Distractor Traps:</em><br>&bull; A (Toxicity Overlook): Confuses maximal raw endonuclease cleavage (78.4%) with therapeutic index; WT-Cas9 generates disastrous 14.6% off-target mutagenic indels.<br>&bull; B (Suboptimal Fidelity Trap): While 18-nt WT-Cas9 improves upon 20-nt WT-Cas9, its 1.8% off-target rate is still 9-fold higher than eCas9 with 20-nt sgRNA.<br>&bull; C (Over-Destabilization Trap): 18-nt truncated guides combined with eCas9 synergistically destabilize target engagement, causing HDR efficiency to collapse below therapeutic relevance (18.5%)."
    },
    {
        "q": "The engineered eCas9 variant carries four basic-to-alanine substitutions (K848A, K1003A, R1060A, and K855A). At physiological pH 7.4, how do these specific point mutations reduce off-target cleavage without abolishing on-target cleavage?",
        "ch": [
            "By disrupting covalent phosphodiester crosslinks that anchor Cas9 to the DNA strand",
            "By converting negatively charged residues into neutral groups to reduce repulsion forces",
            "By neutralizing cationic side chains to weaken non-specific backbone attraction in DNA",
            "By increasing the net positive surface charge to lock Cas9 onto target sequences tightly"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Electrostatic Interactions in Protein-DNA Recognition]</strong><br><br>1. <em>Biochemical Properties of Replaced Residues:</em> Lysine (ammonium side chain, pKa ~10.5) and arginine (guanidinium side chain, pKa ~12.5) are fully protonated, cationic (+1) residues at physiological pH 7.4. Alanine possesses a neutral, nonpolar methyl side chain.<br>2. <em>Mechanism of Non-Specific DNA Binding:</em> WT-Cas9 utilizes these positively charged basic residues to form favorable, non-sequence-specific electrostatic attractions with the polyanionic phosphodiester backbone of the non-target DNA strand, stabilizing the Cas9-DNA complex even when mismatches occur along the guide RNA.<br>3. <em>Functional Consequence of Alanine Mutations:</em> Replacing four cationic residues with neutral alanines eliminates these non-specific electrostatic contacts. Consequently, stable Cas9-DNA strand separation and endonuclease activation become strictly reliant on extensive, perfect Watson-Crick base pairing between sgRNA and target DNA. At off-target sites containing mismatches, the complex dissociates before cleavage occurs; at fully matched on-target sites, full complementarity provides sufficient free energy to drive cleavage.<br><br><em>Distractor Traps:</em><br>&bull; A (Covalent Misconception): Protein-DNA backbone associations are mediated through non-covalent hydrogen bonding and ionic interactions, not covalent phosphodiester bonds.<br>&bull; B (Charge Inversion Error): Lysine and arginine are basic (positively charged), not acidic (negatively charged).<br>&bull; D (Directional Inversion): Alanine substitution decreases net positive surface charge; increasing positive charge would enhance non-specific binding and increase off-target cleavage."
    },
    {
        "q": "Under physiological cell cycle regulation, homology-directed repair (HDR) operates almost exclusively during late S and G2 phases primarily because:",
        "ch": [
            "sister chromatids are physically present and elevated CDK1 activity promotes resection",
            "centrosome duplication provides the microtubule spindle needed for double-strand ligation",
            "nuclear envelope breakdown during interphase allows cytosolic exonucleases into chromatin",
            "cyclin-dependent kinase inhibitors selectively silence non-homologous end joining units"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Cell Cycle Regulation of Double-Strand Break Repair Pathways]</strong><br><br>1. <em>Cell Cycle State and Template Availability:</em> In G0 and G1 phases, each chromosome exists as a single chromatid; no identical homologous copy is in close physical proximity. In late S and G2 phases, DNA replication has synthesized an identical sister chromatid held in tight juxtaposition by cohesin complexes.<br>2. <em>Enzymatic Regulation:</em> HDR initiation requires 5'-to-3' end resection to generate 3' single-stranded DNA overhangs for RAD51-mediated strand invasion. This resection step is actively stimulated by CDK1/Cyclin B kinase activity, which peaks during S/G2 and is absent in G1.<br>3. <em>Integration:</em> The combined presence of high CDK activity licensing nucleolytic end resection and the immediate spatial proximity of identical sister chromatids restricts HDR execution to late S and G2 phases.<br><br><em>Distractor Traps:</em><br>&bull; B (Mitotic Machinery Distractor): Centrosomes and mitotic spindles mediate chromosome segregation during M phase, not enzymatic ligation during S/G2 double-strand break repair.<br>&bull; C (Temporal & Structural Error): Nuclear envelope breakdown occurs during prometaphase of mitosis, not interphase; DNA repair nucleases are nuclear enzymes.<br>&bull; D (False Mechanism Trap): G1 does not feature CDK inhibitor-mediated NHEJ silencing; rather, NHEJ remains constitutively active throughout all cell cycle stages (including G1)."
    },
    {
        "q": "The catalytically dead Cas9 (dCas9) engineered in Condition 5 carries D10A and H840A mutations that disable the RuvC and HNH nuclease domains. Which molecular function is retained by dCas9?",
        "ch": [
            "Dephosphorylation of the 5'-terminal monophosphate on cleaved protospacer fragments",
            "High-affinity, guide-RNA-directed binding to specific target genomic DNA sequences",
            "ATP-dependent helicase unwinding of duplex DNA independent of guide sequence matches",
            "Intrinsic exonuclease degradation of non-complementary single-stranded RNA loop folds"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Uncoupling of Substrate Binding from Catalytic Cleavage in Enzymes]</strong><br><br>1. <em>Domain Architecture of Cas9:</em> Cas9 comprises a recognition (REC) lobe that binds the sgRNA:DNA heteroduplex and a nuclease (NUC) lobe containing RuvC and HNH catalytic sites that cleave the non-target and target strands, respectively.<br>2. <em>Effect of Point Mutations:</em> D10A (in RuvC) and H840A (in HNH) replace critical catalytic carboxylate and imidazole side chains that coordinate Mg2+ ions required for phosphodiester hydrolysis. These substitutions abolish catalytic cleavage without altering the structural folding of the PAM-interacting or REC domains.<br>3. <em>Functional Retention:</em> dCas9 retains unimpaired, guide-RNA-programmed, high-affinity sequence-specific binding (Kd in the low nanomolar range), permitting its use as a programmable DNA-targeting platform for transcriptional regulation, epigenetic editing, or base editing.<br><br><em>Distractor Traps:</em><br>&bull; A (Invented Activity Trap): Cas9 is a phosphodiester endonuclease, not a phosphatase; furthermore, dCas9 has no catalytic cleavage activity.<br>&bull; C (Mechanism Inversion): Cas9 lacks ATP-dependent helicase activity; duplex unwinding is driven locally by the thermodynamic free energy of sgRNA:DNA base pairing, not ATP hydrolysis.<br>&bull; D (Nuclease Fabrication): Cas9 possesses no intrinsic RNA exonuclease activity."
    },
    {
        "q": "The protospacer adjacent motif (PAM) for SpCas9 is 5'-NGG-3'. If the non-target DNA strand sequence containing the PAM is 5'-ATCGG-3', what is the exact sequence of the corresponding motif on the target (cleaved) strand, oriented from 5' to 3'?",
        "ch": [
            "Sequence: 5'-TAGCC-3'",
            "Sequence: 5'-ATCGG-3'",
            "Sequence: 5'-GGCTA-3'",
            "Sequence 5'-CCGAT-3'"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Antiparallel Complementary Base-Pairing in Nucleic Acids]</strong><br><br>1. <em>Determine Polarity and Complementarity:</em> The non-target strand sequence is written 5'-A-T-C-G-G-3'. In duplex DNA, strands run in an antiparallel orientation with canonical Watson-Crick base pairing (A pairs with T, C pairs with G).<br>2. <em>Construct the Complementary Strand:</em> Pairing 3' to 5' against 5'-A-T-C-G-G-3' yields 3'-T-A-G-C-C-5'.<br>3. <em>Reorient to Standard 5'-to-3' Convention:</em> Reading this complementary strand in the mandatory 5'-to-3' direction gives 5'-C-C-G-A-T-3'. Specifically, the two guanine PAM bases on the 3' end of the non-target strand pair with two cytosine bases at the 5' end of the target strand motif.<br><br><em>Distractor Traps:</em><br>&bull; A (Parallel Reading Trap): Reads the complementary strand backwards from 3' to 5' without reversing orientation.<br>&bull; B (Identical Strand Trap): Fails to generate the complementary strand, repeating the non-target strand sequence verbatim.<br>&bull; C (Parallel Complement Trap): Assumes parallel strand polarity (5'-G-G-C-T-A-3'), failing to account for the antiparallel nature of DNA duplexes."
    },
    {
        "q": "The pathogenic sickle cell mutation in the HBB gene is an A-to-T transversion in the coding (non-template) strand converting codon GAG to GTG. What is the resulting amino acid substitution, and how does it alter hemoglobin biophysics?",
        "ch": [
            "Glutamate to Lysine, creating electrostatic repulsion along the beta-chain interface region",
            "Aspartate to Alanine, reducing polar solvation without enabling hydrophobic contact surfaces",
            "Glutamate to Valine, creating an adhesive hydrophobic patch that drives polymerization",
            "Glutamine to Leucine, destabilizing heme coordination by disrupting proximal histidine bonds"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Molecular Pathophysiology of Hemoglobin S Polymerization]</strong><br><br>1. <em>Genetic Translation:</em> Codon GAG encodes glutamate (Glu, an acidic residue with a carboxylate side chain carrying a -1 charge at pH 7.4). The coding strand mutation to GTG results in mRNA codon GUG, which translates to valine (Val, a neutral branched-chain amino acid with an aliphatic isopropyl side chain).<br>2. <em>Biophysical Transformation:</em> On the surface of the deoxygenated &beta;-globin tetramer, glutamate-6 normally participates in favorable polar hydrogen bonding and ionic interactions with water and adjacent proteins. Substituting hydrophobic valine exposes a nonpolar patch.<br>3. <em>Downstream Polymerization:</em> Under deoxygenated conditions (T-state conformation), this exposed hydrophobic valine lodges into a complementary hydrophobic pocket (formed by Phe85 and Leu88) on an adjacent deoxygenated &beta;-globin subunit, initiating non-covalent nucleation and helical fiber polymerization that distorts RBCs into sickle forms.<br><br><em>Distractor Traps:</em><br>&bull; A (Hemoglobin C Trap): Glutamate to lysine is the HbC mutation, which causes mild hemolytic anemia with crystal formation, not sickle-cell fiber polymerization.<br>&bull; B (Wrong Amino Acid Residues): The native residue is glutamate (codon GAG), not aspartate (GAC/GAU), and the mutant is valine, not alanine.<br>&bull; D (Wrong Substitution & Mechanism): Codon GTG encodes valine, not leucine; heme binding is coordinated by the proximal (His92/F8) and distal (His58/E7) histidines, not residue 6."
    }
]

# Passage 2: Pyruvate dehydrogenase regulation and metabolic control (exam_bb90_p2)
# Key: B, D, A, C, B, D
p2_qs = [
    {
        "q": "Based on the enzymatic mechanism and cofactors detailed in the passage, which cofactor undergoes transient covalent reductive acetylation during the catalytic cycle of the pyruvate dehydrogenase complex?",
        "ch": [
            "Flavin adenine dinucleotide bound to the dihydrolipoyl dehydrogenase subunit stably",
            "Lipoic acid covalently tethered to a lysine residue of transacetylase (E2) subunit",
            "Thiamine pyrophosphate bound to the pyruvate dehydrogenase subunit (E1) active site",
            "Nicotinamide adenine dinucleotide acting as a freely diffusible cosubstrate in matrix"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Multienzyme Complex Catalytic Cycle and Cofactor Mechanics]</strong><br><br>1. <em>Catalytic Sequence of PDC:</em> Step 1: E1 decarboxylates pyruvate, transferring the 2-carbon hydroxyethyl intermediate to thiamine pyrophosphate (TPP). Step 2: The hydroxyethyl group is oxidized to an acetyl group and transferred to the oxidized lipoamide prosthetic group on E2.<br>2. <em>Reductive Acetylation:</em> This transfer reduces the cyclic disulfide of lipoamide to a dihydrolipoamide thiol while simultaneously forming a high-energy thioester linkage (acetyllipoamide). Thus, lipoic acid is reductively acetylated.<br>3. <em>Subsequent Steps:</em> E2 transfers the acetyl group to Coenzyme A, forming acetyl-CoA. E3 uses FAD to re-oxidize the reduced dihydrolipoamide back to its active cyclic disulfide form, generating FADH2, which subsequently transfers electrons to NAD+, producing NADH + H+.<br><br><em>Distractor Traps:</em><br>&bull; A (Redox Cofactor Scope Error): FAD serves as an electron carrier within E3 to reoxidize dihydrolipoamide; it never forms a covalent bond with the acetyl group.<br>&bull; C (Initial Decarboxylation Distractor): TPP forms a covalent hydroxyethyl intermediate via nucleophilic attack of its carbanion on pyruvate's carbonyl carbon, but it does not undergo reductive acetylation.<br>&bull; D (Soluble Electron Acceptor Trap): NAD+ acts as the terminal electron acceptor in the E3 reaction; it does not bind or carry the acetyl moiety."
    },
    {
        "q": "According to Table 1, administering dichloroacetate (DCA) to glioblastoma cells restores mitochondrial respiration primarily by:",
        "ch": [
            "allosterically activating pyruvate dehydrogenase phosphatase 1 to cleave ATP stores",
            "competitively inhibiting lactate dehydrogenase to trap pyruvate within the cytosol",
            "directly binding complex I to bypass proton-pumping electron transport chain stages",
            "inhibiting pyruvate dehydrogenase kinase to maintain the E1alpha subunit active"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Covalent Regulation of Pyruvate Dehydrogenase in Cancer Metabolism]</strong><br><br>1. <em>Identify Pathological Baseline:</em> Hypoxia-inducible factor 1&alpha; (HIF-1&alpha;) upregulates PDK1 in glioblastoma cells. PDK1 hyperphosphorylates serine residues (Ser264, Ser271, Ser203) on the E1&alpha; subunit, inactivating PDC and shunting pyruvate to lactate (Warburg effect).<br>2. <em>Pharmacological Mechanism of DCA:</em> DCA is a structural analog of pyruvate that functions as a selective pan-PDK inhibitor. By inhibiting PDK, DCA prevents the inactivating phosphorylation of E1&alpha;.<br>3. <em>Metabolic Outcome:</em> Unopposed constitutive phosphatase (PDP) dephosphorylates E1&alpha;, restoring active unphosphorylated PDC. Table 1 demonstrates that DCA elevates PDC activity from 22% to 88%, slashes lactate from 18.4 to 4.2 mmol/L, and triples oxygen consumption from 42 to 134 pmol/min.<br><br><em>Distractor Traps:</em><br>&bull; A (Phosphatase Misclassification): DCA inhibits the kinase (PDK); it is not an allosteric activator of PDP, and phosphatases hydrolyze phosphoserine esters, they do not 'cleave ATP'.<br>&bull; B (Wrong Molecular Target): DCA does not inhibit LDHA directly; lactate crashes because pyruvate is diverted into mitochondria via active PDC.<br>&bull; C (Mitochondrial Target Conflation): DCA acts on the regulatory matrix kinase PDK, not on Complex I of the electron transport chain."
    },
    {
        "q": "Why does adding rotenone to DCA-treated glioblastoma cells (Condition 5) cause lactate production to surge from 4.2 to 19.6 mmol/L despite continuing PDK inhibition?",
        "ch": [
            "Complex I blockade halts the ETC, accumulating NADH that allosterically arrests PDC",
            "Rotenone phosphorylates pyruvate kinase, forcing phosphoenolpyruvate into glycogen chains",
            "Rotenone cleaves the mitochondrial outer membrane, releasing cytochrome c into cytosol",
            "Blockade of complex II depletes mitochondrial FAD, preventing transacetylase recycling"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Metabolic Feedback Regulation and Redox Homeostasis]</strong><br><br>1. <em>Site of Rotenone Action:</em> Rotenone is a specific, high-affinity inhibitor of Complex I (NADH:ubiquinone oxidoreductase) of the mitochondrial electron transport chain.<br>2. <em>Upstream Redox Consequences:</em> Blocking Complex I halts the re-oxidation of NADH to NAD+. The intramitochondrial NADH/NAD+ ratio surges (measured at 18.2 in Table 1). High NADH acts as a potent product inhibitor of the PDC E3 subunit.<br>3. <em>Diversion to Lactate:</em> Because PDC is functionally arrested by massive NADH product inhibition, pyruvate accumulates. To regenerate cytosolic NAD+ needed to sustain glycolytic ATP generation via glyceraldehyde-3-phosphate dehydrogenase (GAPDH), lactate dehydrogenase reduces pyruvate to lactate, causing lactate production to surge to 19.6 mmol/L.<br><br><em>Distractor Traps:</em><br>&bull; B (Glycolytic Enzyme Fabrication): Rotenone is an ETC inhibitor, not a kinase; it does not phosphorylate pyruvate kinase or stimulate glycogen synthesis.<br>&bull; C (Apoptosis Confabulation): Cytochrome c release triggers apoptosome assembly and caspase cascades; it does not explain the immediate acute surge in lactate production.<br>&bull; D (Target Mismatch): Rotenone inhibits Complex I, not Complex II; Complex II uses succinate and FAD, whereas E2 turnover depends on lipoamide and CoA-SH."
    },
    {
        "q": "Pyruvate dehydrogenase kinase (PDK) is allosterically activated by high cellular energy charge. Which set of metabolites will stimulate PDK activity to suppress pyruvate oxidation?",
        "ch": [
            "Elevated cytosolic pyruvate alongside high free coenzyme A and low cellular ATP levels",
            "Elevated intramitochondrial calcium ions alongside elevated ADP and AMP energy signals",
            "Elevated intramitochondrial acetyl-CoA, elevated NADH, and elevated cellular ATP",
            "Elevated intramitochondrial succinate, high NAD+, and reduced acyl-CoA cofactors"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Allosteric Regulation of Pyruvate Dehydrogenase Kinase]</strong><br><br>1. <em>Metabolic Function of PDK:</em> PDK phosphorylates and inactivates PDC. Inactivating PDC spares pyruvate and carbohydrates when downstream energy reserves are already saturated.<br>2. <em>Allosteric Activators:</em> Saturated energy charge is signaled by high levels of ATP, acetyl-CoA (the immediate product of PDC and &beta;-oxidation), and NADH (the product of PDC and the TCA cycle). These metabolites bind allosteric regulatory sites on PDK, enhancing its kinase activity toward E1&alpha;.<br>3. <em>Allosteric Inhibitors:</em> Conversely, high concentrations of pyruvate (substrate), ADP, NAD+, and CoA-SH signal energy depletion and actively inhibit PDK, ensuring PDC remains dephosphorylated and catalytically active.<br><br><em>Distractor Traps:</em><br>&bull; A (Substrate/Depletion Trap): Pyruvate, CoA, and low ATP inhibit PDK to keep PDC active; they do not activate PDK.<br>&bull; B (Phosphatase Activator Trap): Intramitochondrial Ca2+ activates PDP (the activating phosphatase) and ADP inhibits PDK.<br>&bull; D (Opposite Redox State): High NAD+ and reduced acyl-CoA reflect energy deficit, which suppresses PDK activity."
    },
    {
        "q": "Patients with severe chronic thiamine (vitamin B1) deficiency develop Wernicke-Korsakoff syndrome. In these patients, which biochemical intermediate directly accumulates in serum due to PDC dysfunction?",
        "ch": [
            "Succinyl-CoA, which accumulates due to impaired succinate thiokinase turnover in matrix",
            "Pyruvate, which cannot undergo oxidative decarboxylation and converts to lactate pool",
            "Citrate, which cannot be isomerized to isocitrate by mitochondrial aconitase enzymes",
            "Oxaloacetate, which cannot condense with acetyl-CoA due to synthase deficiency states"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Cofactor Dependencies and Inborn/Nutritional Metabolic Derangements]</strong><br><br>1. <em>Cofactor Requirement:</em> Thiamine pyrophosphate (TPP), the biologically active derivative of vitamin B1, is the prosthetic group for the E1 (pyruvate dehydrogenase) subunit of PDC and the &alpha;-ketoglutarate dehydrogenase complex of the TCA cycle.<br>2. <em>Enzymatic Block:</em> Without TPP, the E1 subunit cannot perform the nucleophilic decarboxylation of pyruvate to form the hydroxyethyl-TPP intermediate.<br>3. <em>Systemic Manifestation:</em> Pyruvate accumulates upstream of the metabolic block. Because it cannot enter the TCA cycle as acetyl-CoA, cytosolic lactate dehydrogenase reduces accumulating pyruvate to lactate to regenerate NAD+, causing pronounced lactic acidosis and hyperpyruvatemia in neurological and cardiovascular tissues.<br><br><em>Distractor Traps:</em><br>&bull; A (Downstream Intermediate Trap): Succinyl-CoA is formed downstream in the TCA cycle by &alpha;-ketoglutarate dehydrogenase (which also requires TPP); in thiamine deficiency, succinyl-CoA synthesis is impaired, not accumulated.<br>&bull; C (Aconitase Distractor): Citrate accumulation occurs with fluorocitrate inhibition of aconitase (an iron-sulfur enzyme), not thiamine deficiency.<br>&bull; D (Synthetic Block Inversion): Oxaloacetate requires acetyl-CoA to form citrate; with PDC impaired, acetyl-CoA is deficient, but oxaloacetate is shunted into malate or gluconeogenesis, not accumulated."
    },
    {
        "q": "The overall oxidative decarboxylation of pyruvate catalyzed by PDC is highly exergonic under standard physiological conditions (ΔG°' = -33.4 kJ/mol). What thermodynamic factor drives the irreversible commitment of this reaction?",
        "ch": [
            "The rapid hydrolysis of pyrophosphate by ubiquitous cytosolic inorganic pyrophosphatases",
            "The endergonic synthesis of ATP via substrate-level phosphorylation on the E3 subunit",
            "The formation of an exceptionally stable low-energy phosphodiester bond within acetyl-CoA",
            "The entropic gain accompanied by the release of carbon dioxide gas as a reaction product"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Thermodynamic Driving Forces in Decarboxylation Reactions]</strong><br><br>1. <em>Reaction Stoichiometry:</em> Pyruvate (3C) + NAD+ + CoA-SH &rarr; Acetyl-CoA (2C) + NADH + CO2 + H+.<br>2. <em>Entropic and Enthalpic Contributions:</em> Decarboxylation releases carbon dioxide (CO2), a stable, gaseous molecule. The liberation of CO2 gas provides a massive positive entropy change (&Delta;S > 0) and effectively escapes the local chemical equilibrium as it diffuses out of the cell and into capillaries, driving the reaction forward via Le Chatelier's principle.<br>3. <em>Irreversibility:</em> Despite the synthesis of a high-energy thioester bond in acetyl-CoA (&Delta;G°' of hydrolysis ~ -31.5 kJ/mol), the combined free energy release from C-C bond cleavage and favorable oxidation of NADH yields an overall &Delta;G°' of -33.4 kJ/mol, rendering the PDC reaction physiologically irreversible in animal cells.<br><br><em>Distractor Traps:</em><br>&bull; A (Pyrophosphatase Distractor): Pyrophosphate cleavage drives reactions that generate PPi (e.g., DNA replication, aminoacyl-tRNA synthesis, fatty acid activation); PDC releases CO2, not PPi.<br>&bull; B (Energy Misconception): PDC produces NADH, not ATP through substrate-level phosphorylation; substrate-level phosphorylation in the TCA cycle is catalyzed by succinyl-CoA synthetase.<br>&bull; C (Bond Type and Energy Error): Acetyl-CoA contains a high-energy thioester bond, not a low-energy phosphodiester bond."
    }
]

# Passage 3: SGLT2 glucose transport kinetics and diabetic nephropathy (exam_bb90_p3)
# Key: A, C, D, B, A, C
p3_qs = [
    {
        "q": "Based on the kinetic parameters in Table 1, which kinetic mechanism characterizes the inhibition of human SGLT2 by dapagliflozin?",
        "ch": [
            "Pure competitive inhibition, marked by unaltered Vmax alongside elevated apparent Km",
            "Noncompetitive inhibition, marked by diminished Vmax alongside unaltered substrate Km",
            "Uncompetitive inhibition, marked by proportional decreases in both Vmax and Km values",
            "Irreversible inhibition, marked by progressive destruction of functional transporters"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Enzyme Kinetics and Pharmacological Inhibition Modes]</strong><br><br>1. <em>Extract Kinetic Parameters from Table 1:</em> Control Vmax = 48.0 nmol/10^6 cells/min; 2.5 nM dapagliflozin Vmax = 47.8; 10.0 nM dapagliflozin Vmax = 48.2. Across all drug concentrations, Vmax remains essentially unchanged (~48 nmol).<br>2. <em>Examine Substrate Affinity (Km):</em> Control Km = 1,200 &mu;M; 2.5 nM dapagliflozin Km = 3,600 &mu;M (3-fold increase); 10.0 nM dapagliflozin Km = 10,800 &mu;M (9-fold increase).<br>3. <em>Lineweaver-Burk Diagnostics:</em> The y-intercept (1/Vmax) remains constant at 0.021, while the x-intercept (-1/Km) shifts rightward toward zero. An unchanged Vmax paired with an increased apparent Km is the definitive signature of reversible competitive inhibition, where dapagliflozin competes directly with glucose for the orthosteric binding pocket.<br><br><em>Distractor Traps:</em><br>&bull; B (Noncompetitive Trap): Noncompetitive inhibition lowers Vmax while leaving Km unchanged (as demonstrated by ouabain in Row 4).<br>&bull; C (Uncompetitive Trap): Uncompetitive inhibition lowers both Vmax and Km by binding exclusively to the substrate-transporter complex, shifting Lineweaver-Burk lines in parallel.<br>&bull; D (Irreversible Error): Irreversible inhibition permanently destroys active transporter molecules, causing a concentration-dependent collapse in Vmax that cannot be overcome by saturating substrate."
    },
    {
        "q": "Why does pre-treating renal tubular epithelial cells with ouabain (Row 4) cause SGLT2-mediated glucose uptake to crash by over 95% without altering SGLT2 protein integrity?",
        "ch": [
            "Ouabain acts as a transition-state analog that binds covalently to SGLT2's pore",
            "Ouabain chelates intracellular magnesium, preventing hexokinase phosphorylation",
            "Ouabain abolishes the transcellular sodium gradient driving secondary transport",
            "Ouabain blocks GLUT2 uniporters, producing lethal intracellular osmotic swelling"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Secondary Active Transport and Electrochemical Coupling]</strong><br><br>1. <em>Transporter Energetics:</em> SGLT2 is a secondary active symporter. It does not hydrolyze ATP directly; rather, it harnesses the potential energy stored in the steep inward electrochemical gradient of sodium (extracellular [Na+] ~140 mM vs intracellular [Na+] ~10-15 mM).<br>2. <em>Site of Ouabain Action:</em> Ouabain is a specific cardiac glycoside inhibitor of the basolateral Na+/K+-ATPase pump.<br>3. <em>Downstream Coupling Collapse:</em> Inhibiting the Na+/K+-ATPase stops the active extrusion of Na+, causing intracellular Na+ to rise and dissipating the inward sodium concentration gradient. Without this electrochemical driving force, SGLT2 cannot mediate the uphill cotransport of glucose, causing &alpha;-MDG uptake to collapse to near zero.<br><br><em>Distractor Traps:</em><br>&bull; A (Direct Transporter Inactivation): Ouabain targets the primary active basolateral Na+/K+-ATPase, not the apical SGLT2 symporter.<br>&bull; B (Metabolic Chelation Distractor): Ouabain binds the extracellular face of the Na+/K+-ATPase; it does not chelate magnesium or inhibit cytosolic hexokinase.<br>&bull; D (Basolateral Target Mismatch): GLUT2 is a facilitated diffusion uniporter located on the basolateral membrane; inhibiting SGLT2 transport via sodium gradient collapse does not cause osmotic cell lysis."
    },
    {
        "q": "In a healthy non-diabetic individual, when the filtered glucose load exceeds the tubular transport maximum (Tm) of approximately 375 mg/min, what physiological change occurs in the nephron?",
        "ch": [
            "Renal blood flow decreases sharply due to tubuloglomerular feedback activation pathways",
            "Proximal tubular cells secrete glucose via active ABC cassette efflux pumps in membrane",
            "Water reabsorption in collecting ducts increases via aquaporin-2 induction mechanisms",
            "Glucose excretion in urine increases linearly with filtered load as Tm is exceeded"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Renal Clearance, Threshold, and Transport Maximum Kinetics]</strong><br><br>1. <em>Renal Handling of Glucose:</em> Filtered Load = GFR &times; Plasma [Glucose]. At normal plasma concentrations (~70-100 mg/dL), the filtered load (~125 mg/min) is well below the transport maximum (Tm ~375 mg/min), and virtually 100% of filtered glucose is reclaimed in the proximal tubule.<br>2. <em>Saturation of Transporters:</em> As plasma glucose exceeds the renal threshold (~180-200 mg/dL), apical SGLT2 and SGLT1 symporters become saturated. Once transport maximum (Tm) is reached, reabsorption plateaus at Tm.<br>3. <em>Excretion Dynamics:</em> Excretion = Filtered Load - Reabsorbed Load. Because reabsorption is capped at Tm, any glucose filtered beyond Tm cannot be reabsorbed and is excreted in urine. The rate of urinary excretion rises in a strict 1:1 linear relationship with any further increase in filtered load.<br><br><em>Distractor Traps:</em><br>&bull; A (Hemodynamic Misapplication): Tubuloglomerular feedback responds to NaCl delivery at the macula densa; SGLT2 inhibition actually restores adenosine-mediated feedback to constrict afferent arterioles, not simple glucosuria.<br>&bull; B (Active Secretion Fabrication): The nephron possesses no active glucose secretory mechanism; all glucose transport is unidirectional from lumen to blood.<br>&bull; C (Counter-Osmotic Error): Unabsorbed luminal glucose exerts an osmotic diuretic effect that opposes water reabsorption, producing polyuria rather than enhanced water retention."
    },
    {
        "q": "Which molecular feature distinguishes the apical SGLT2 cotransporter from the basolateral GLUT2 transporter in proximal convoluted tubule epithelial cells?",
        "ch": [
            "SGLT2 functions as a monomer, whereas GLUT2 requires trimeric beta-barrel assembly units",
            "SGLT2 couples transport to an ion gradient, whereas GLUT2 mediates simple diffusion",
            "SGLT2 hydrolyzes ATP directly per turnover, whereas GLUT2 consumes pyrophosphate bonds",
            "SGLT2 transports phosphorylated glucose-6-phosphate, whereas GLUT2 moves free hexose"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Classification of Membrane Transport Mechanisms]</strong><br><br>1. <em>Apical Entry (SGLT2):</em> The apical membrane faces the tubular lumen. Glucose concentration inside the proximal tubule cell is higher than in the luminal filtrate. Thus, glucose entry requires active transport. SGLT2 is a secondary active symporter that couples the energetically unfavorable movement of glucose to the downhill influx of Na+.<br>2. <em>Basolateral Exit (GLUT2):</em> Once inside the cell, glucose reaches high intracellular concentrations. GLUT2, located on the basolateral membrane facing the interstitial space and peritubular capillaries, is a uniporter that mediates the passive, downhill efflux of glucose via facilitated diffusion.<br>3. <em>Energy Coupling Contrast:</em> SGLT2 depends on the electrochemical gradient generated by the Na+/K+-ATPase, whereas GLUT2 operates purely down glucose's chemical concentration gradient without direct or indirect ion coupling.<br><br><em>Distractor Traps:</em><br>&bull; A (Structural Fabrication): Both SGLT and GLUT proteins are multi-pass transmembrane alpha-helical proteins; neither forms bacterial-like beta-barrel trimers.<br>&bull; C (Primary Active Confusion): Neither transporter hydrolyzes ATP directly; SGLT2 is secondary active and GLUT2 is passive facilitated diffusion.<br>&bull; D (Substrate Error): Both SGLT2 and GLUT2 transport unphosphorylated D-glucose; phosphorylated glucose cannot cross these transmembrane carriers."
    },
    {
        "q": "SGLT1, located in the late S3 segment of the proximal tubule and the small intestine, exhibits a 2:1 Na+:glucose coupling stoichiometry compared to SGLT2's 1:1 ratio. What thermodynamic advantage does this 2:1 stoichiometry provide SGLT1?",
        "ch": [
            "It generates a much larger concentration gradient to reclaim residual luminal glucose",
            "It permits glucose transport to proceed without consuming basolateral ATP reserves at all",
            "It doubles the maximum turnover rate (Vmax) of hexose translocations across renal cell",
            "It allows SGLT1 to transport glucose independent of extracellular sodium concentrations"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Thermodynamic Coupling and Free Energy in Ion-Coupled Symport]</strong><br><br>1. <em>Thermodynamic Driving Force:</em> The free energy available to drive glucose uphill is derived from the electrochemical potential of Na+: &Delta;G_transport = &Delta;G_glucose + n &times; &Delta;&mu;_Na+, where n is the stoichiometric coupling ratio.<br>2. <em>Comparison of 1:1 vs 2:1:</em> For SGLT2 (n=1), the maximum achievable intracellular-to-luminal glucose concentration ratio is proportional to [Na+]_out / [Na+]_in &times; exp(-F&Delta;&Psi;/RT) (~100-fold). For SGLT1 (n=2), coupling two Na+ ions squares this term, enabling a theoretical accumulation ratio of ~10,000-fold.<br>3. <em>Physiological Specialization:</em> In the early S1 segment, luminal glucose is plentiful (~5 mM), so SGLT2's 1:1 ratio easily reclaims ~90% of filtered glucose with lower energy expenditure per glucose. In the late S3 segment, luminal glucose is nearly depleted (<0.5 mM); SGLT1's 2:1 ratio provides the massive thermodynamic pulling force required to scavenge the remaining glucose against an extreme concentration gradient.<br><br><em>Distractor Traps:</em><br>&bull; B (Energy Conservation Fallacy): Transporting 2 Na+ ions per glucose consumes MORE metabolic energy, because the basolateral Na+/K+-ATPase must hydrolyze more ATP to extrude the extra sodium.<br>&bull; C (Vmax vs Thermodynamics Confusion): Coupling ratio governs the thermodynamic equilibrium and maximum concentration gradient, not the kinetic turnover rate (Vmax). In fact, SGLT1 has a lower turnover capacity than SGLT2.<br>&bull; D (Sodium Dependence Inversion): A 2:1 ratio increases dependence on extracellular sodium, not decreases it."
    },
    {
        "q": "In clinical trials, diabetic patients administered dapagliflozin exhibit a sustained 4 mmHg reduction in mean systolic blood pressure alongside weight loss. What physiological mechanism explains this systemic hemodynamic effect?",
        "ch": [
            "Competitive antagonism of central alpha-1 adrenergic receptors in the human brainstem",
            "Direct relaxation of arteriolar vascular smooth muscle via cGMP upregulation cascades",
            "Osmotic diuresis induced by glucosuria combined with modest natriuretic volume loss",
            "Upregulation of the renin-angiotensin system producing widespread systemic vasodilation"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Renal Fluid Dynamics and Osmotic Diuresis]</strong><br><br>1. <em>Luminal Solute Retention:</em> By blocking SGLT2, dapagliflozin prevents glucose reabsorption in the proximal convoluted tubule. The unabsorbed glucose remains in the tubular lumen, acting as an impermeable, osmotically active solute.<br>2. <em>Osmotic Water Clearance:</em> Luminal glucose impairs osmotic water reabsorption throughout the proximal tubule and loop of Henle, generating an osmotic diuresis.<br>3. <em>Hemodynamic Consequence:</em> SGLT2 inhibition also induces mild natriuresis (Na+ loss). The resulting contraction of effective circulating plasma volume lowers cardiac preload and arterial wall tension, producing a mild, sustained reduction in systemic blood pressure.<br><br><em>Distractor Traps:</em><br>&bull; A (Wrong Site & Class): Dapagliflozin is a nephron-targeted transporter inhibitor; it does not cross the blood-brain barrier to block central alpha-1 receptors.<br>&bull; B (Direct Vascular Distractor): Gliflozins do not directly activate vascular soluble guanylyl cyclase or stimulate cGMP; vascular changes are secondary to volume reduction.<br>&bull; D (Endocrine Inversion): Mild hypovolemia may trigger compensatory RAAS activation, which promotes vasoconstriction and sodium retention, rather than vasodilation."
    }
]

# Passage 4: GPCR and beta-arrestin biased signaling in smooth muscle (exam_bb90_p4)
# Key: C, A, B, D, C, A
p4_qs = [
    {
        "q": "Based on the functional pharmacology in Table 1, why would Compound B1 be expected to produce significantly less tachyphylaxis during chronic asthma therapy than isoproterenol?",
        "ch": [
            "B1 covalently binds adenylyl cyclase, permanently locking it in an active enzyme state",
            "B1 operates as a competitive antagonist that permanently silences downstream signaling",
            "B1 selectively activates G-protein signaling with minimal beta-arrestin recruitment",
            "B1 accelerates clathrin-mediated endocytosis to degrade internalized receptors in cells"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Receptor Desensitization and Biased Agonism]</strong><br><br>1. <em>Mechanism of Tachyphylaxis (Tolerance):</em> Chronic stimulation of GPCRs by full agonists like isoproterenol causes GRK phosphorylation of the C-terminal tail, followed by high-affinity &beta;-arrestin recruitment. &beta;-arrestin sterically blocks further G&alpha;s coupling and targets the receptor to clathrin-coated pits for endocytosis and lysosomal degradation (downregulation), causing loss of bronchodilatory efficacy over time.<br>2. <em>Evaluate Compound B1 Profile:</em> Table 1 shows that Compound B1 achieves 98% of isoproterenol's efficacy for G&alpha;s-mediated cAMP accumulation (EC50 = 4.8 nM), but exhibits only 8% &beta;-arrestin recruitment and just 12% receptor internalization at 60 minutes (vs 82% for isoproterenol).<br>3. <em>Therapeutic Consequence:</em> By acting as a G&alpha;s-biased agonist that evades &beta;-arrestin recruitment, Compound B1 preserves surface receptor density on airway smooth muscle cells, substantially mitigating tachyphylaxis.<br><br><em>Distractor Traps:</em><br>&bull; A (Target & Mechanism Fabrication): B1 is a &beta;2AR ligand, not an adenylyl cyclase ligand; it does not bind or covalently modify adenylyl cyclase.<br>&bull; B (Pharmacological Class Error): B1 is a biased full agonist for cAMP generation (Emax 98%), not an antagonist.<br>&bull; D (Tolerance Mechanism Inversion): Accelerated endocytosis and lysosomal degradation would INCREASE tachyphylaxis, not prevent it."
    },
    {
        "q": "How does the activated Gαs subunit intrinsically terminate its own stimulation of adenylyl cyclase to ensure biological signal termination?",
        "ch": [
            "Its intrinsic GTPase hydrolyzes bound GTP to GDP, prompting trimer re-association",
            "Its intrinsic kinase activity phosphorylates bound GDP to GTP, terminating enzyme cycle",
            "Its intrinsic phosphodiesterase degrades cyclic AMP to 5'-adenosine monophosphate pools",
            "Its intrinsic ubiquitin ligase tags adenylyl cyclase for rapid proteasomal destruction"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Intrinsic GTPase Molecular Switch in Heterotrimeric G-Proteins]</strong><br><br>1. <em>Activation State:</em> Upon agonist-induced GEF (guanine nucleotide exchange factor) activity of the receptor, G&alpha;s exchanges bound GDP for GTP, undergoing a conformational change that causes dissociation from G&beta;&gamma; and activation of adenylyl cyclase.<br>2. <em>Intrinsic Hydrolysis:</em> G&alpha;s possesses a built-in GTPase domain that acts as an internal timing clock. It slowly hydrolyzes the terminal phosphoanhydride bond of bound GTP to produce bound GDP and inorganic phosphate (Pi).<br>3. <em>Signal Termination:</em> In the GDP-bound state, G&alpha;s has low affinity for adenylyl cyclase and high affinity for the G&beta;&gamma; heterodimer. G&alpha;s-GDP dissociates from adenylyl cyclase, ending cAMP production, and reassembles with G&beta;&gamma; into an inactive heterotrimer ready for subsequent activation.<br><br><em>Distractor Traps:</em><br>&bull; B (Nucleotide Inversion): G&alpha;s hydrolyzes GTP to GDP; it is not a kinase that phosphorylates GDP.<br>&bull; C (Enzyme Class Conflation): Phosphodiesterases (PDEs) degrade cAMP to 5'-AMP; G&alpha;s is a GTPase, not a cyclic nucleotide phosphodiesterase.<br>&bull; D (Degradation Distractor): G-protein signaling termination occurs via reversible conformational cycling through GTP hydrolysis, not ubiquitin-proteasome degradation of adenylyl cyclase."
    },
    {
        "q": "Cholera toxin catalyzes ADP-ribosylation of an essential arginine residue within Gαs, abolishing its intrinsic GTPase activity. What biochemical consequence ensues in intestinal mucosal cells?",
        "ch": [
            "Constitutive activation of phospholipase C floods enterocytes with inositol phosphate",
            "Constitutive activation of adenylyl cyclase elevates cAMP, opening CFTR channels",
            "Constitutive dephosphorylation of protein kinase A halts all active chloride extrusion",
            "Constitutive activation of beta-arrestin causes immediate endocytosis of all ion pumps"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Pathogenic ADP-Ribosylation and Signal Hyperactivation]</strong><br><br>1. <em>Toxin Mechanism:</em> Cholera toxin transfers an ADP-ribose moiety from NAD+ onto Arg201 of G&alpha;s. This steric modification blocks GTP hydrolysis while allowing GTP binding.<br>2. <em>Persistent Active Conformation:</em> G&alpha;s remains permanently trapped in its GTP-bound, active conformation, unable to hydrolyze GTP to GDP and uncouple from adenylyl cyclase.<br>3. <em>Downstream Pathology:</em> Adenylyl cyclase constitutively synthesizes cAMP. Persistently elevated cAMP hyperactivates protein kinase A (PKA). PKA phosphorylates the regulatory domain of apical CFTR chloride channels in intestinal crypt cells, driving massive, uncontrolled secretion of Cl- and water into the gut lumen (secretory diarrhea).<br><br><em>Distractor Traps:</em><br>&bull; A (G-Protein Pathway Mismatch): Phospholipase C (PLC) is coupled to G&alpha;q, not G&alpha;s.<br>&bull; C (Kinase Status Inversion): PKA is hyperactivated by elevated cAMP, not dephosphorylated or inactivated.<br>&bull; D (Arrestin Misconception): Cholera toxin targets G&alpha;s, not &beta;2-arrestin; furthermore, CFTR channels are not endocytosed but rather opened."
    },
    {
        "q": "In airway smooth muscle, what is the precise molecular mechanism by which protein kinase A (PKA) activation induces bronchodilation (smooth muscle relaxation)?",
        "ch": [
            "PKA phosphorylates actin filaments, preventing interaction with tropomyosin rods in cell",
            "PKA activates voltage-gated L-type calcium channels to flood muscle sarcoplasm with Ca2+",
            "PKA stimulates IP3 receptor opening on the sarcoplasmic reticulum membrane in myocytes",
            "PKA phosphorylates and inactivates MLCK while stimulating SR calcium re-uptake in cells"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Molecular Mechanisms of Smooth Muscle Contraction and Relaxation]</strong><br><br>1. <em>Smooth Muscle Contractile Cascade:</em> Unlike striated muscle (which uses troponin), smooth muscle contraction requires myosin light chain kinase (MLCK) to phosphorylate the 20-kDa regulatory light chain of myosin, enabling cross-bridge cycling with actin. MLCK activation requires Ca2+-calmodulin.<br>2. <em>PKA Inactivation of MLCK:</em> PKA directly phosphorylates MLCK at a specific regulatory site, decreasing MLCK's affinity for the Ca2+-calmodulin complex by over 10-fold and suppressing myosin phosphorylation.<br>3. <em>Calcium Clearance:</em> Concurrently, PKA phosphorylates phospholamban (disinhibiting the SERCA Ca2+ pump to sequester Ca2+ into the sarcoplasmic reticulum) and stimulates plasma membrane Ca2+-ATPases, lowering cytosolic Ca2+. Together, low Ca2+ and inactive MLCK allow myosin light chain phosphatase (MLCP) to dominate, producing profound smooth muscle relaxation (bronchodilation).<br><br><em>Distractor Traps:</em><br>&bull; A (Troponin/Striated Muscle Confabulation): Smooth muscle lacks troponin; regulation is mediated via myosin phosphorylation, not PKA phosphorylation of actin or tropomyosin.<br>&bull; B (Opposite Action Trap): Activating L-type calcium channels would flood the sarcoplasm with Ca2+ and induce bronchoconstriction, not bronchodilation.<br>&bull; C (Contractile Agonist Error): Stimulating IP3 receptors releases Ca2+ from the SR, which drives contraction (the mechanism of Gq-coupled muscarinic/histaminic bronchoconstrictors)."
    },
    {
        "q": "If cultured smooth muscle cells are microinjected with a non-hydrolyzable GTP analog (GTP-γ-S) prior to isoproterenol challenge, the resulting intracellular cAMP production will:",
        "ch": [
            "remain baseline because GTP-gamma-S cannot displace bound GDP on the G-protein complex",
            "transiently spike and then extinguish rapidly via accelerated receptor endocytosis steps",
            "become sustained and irreversible even after complete wash-out of isoproterenol in bath",
            "crash to zero because GTP-gamma-S acts as an irreversible antagonist on adenylyl cyclase"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Non-Hydrolyzable Guanine Nucleotides as Mechanistic Probes]</strong><br><br>1. <em>G-Protein Exchange Mechanism:</em> Agonist binding to &beta;2AR induces GDP dissociation from G&alpha;s. Microinjected GTP-&gamma;-S readily binds the vacant nucleotide-binding pocket.<br>2. <em>Blockade of Deactivation:</em> The terminal phosphorothioate bond in GTP-&gamma;-S resists cleavage by G&alpha;s's intrinsic GTPase domain. As a result, G&alpha;s cannot hydrolyze the nucleotide back to GDP.<br>3. <em>Irreversible Activation:</em> G&alpha;s remains locked in its active conformation, continuously stimulating adenylyl cyclase. Even if isoproterenol is completely washed out of the extracellular bath or displaced with propranolol, G&alpha;s cannot turn off, causing prolonged, irreversible cAMP synthesis.<br><br><em>Distractor Traps:</em><br>&bull; A (Binding Incompetence Error): GTP-&gamma;-S binds G&alpha;s with high affinity once agonist stimulation opens the nucleotide pocket.<br>&bull; B (Transient Kinetic Trap): Termination requires GTP hydrolysis; because hydrolysis cannot occur, activation cannot self-extinguish.<br>&bull; D (Antagonist Misclassification): GTP-&gamma;-S is a persistent activator of G&alpha; proteins, not an inhibitor of adenylyl cyclase."
    },
    {
        "q": "Roflumilast, a phosphodiesterase-4 (PDE4) inhibitor, is utilized in chronic obstructive pulmonary disease. How does roflumilast synergize pharmacologically with beta-2 adrenergic agonists?",
        "ch": [
            "By preventing enzymatic degradation of cAMP, prolonging downstream PKA signaling",
            "By directly opening CFTR chloride channels independent of intracellular nucleotide",
            "By inhibiting GRK phosphorylation to prevent beta-arrestin recruitment to membranes",
            "By increasing cellular ATP synthesis to provide more substrate for adenylyl cyclase"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Second Messenger Turnover and Synergistic Pharmacodynamics]</strong><br><br>1. <em>Metabolism of Cyclic AMP:</em> &beta;2-agonists stimulate adenylyl cyclase to synthesize cAMP from ATP. Intracellular cAMP is rapidly degraded to inactive 5'-AMP by phosphodiesterases (PDEs), predominantly PDE4 in airway smooth muscle and inflammatory leukocytes.<br>2. <em>Mechanism of PDE4 Inhibition:</em> Roflumilast selectively inhibits PDE4, blocking the hydrolytic cleavage of the 3',5'-cyclic phosphate ring of cAMP.<br>3. <em>Synergistic Amplification:</em> Combining a &beta;2-agonist (which accelerates cAMP production) with a PDE4 inhibitor (which halts cAMP breakdown) dramatically boosts steady-state cAMP concentrations and prolongs PKA-mediated smooth muscle relaxation and anti-inflammatory signaling.<br><br><em>Distractor Traps:</em><br>&bull; B (Direct Channel Action Error): Roflumilast targets phosphodiesterase, not ion channels directly; CFTR activation is secondary to elevated cAMP/PKA.<br>&bull; C (Desensitization Kinase Confabulation): Roflumilast does not inhibit GRK (G-protein-coupled receptor kinase); it targets cyclic nucleotide phosphodiesterase.<br>&bull; D (Substrate Abundance Fallacy): Intracellular ATP is maintained at millimolar concentrations (well above the Km of adenylyl cyclase); PDE inhibitors do not alter mitochondrial ATP synthesis."
    }
]

if __name__ == "__main__":
    validate_questions(p1_qs, 1)
    validate_questions(p2_qs, 7)
    validate_questions(p3_qs, 13)
    validate_questions(p4_qs, 19)
    print("ALL PASSAGES 1 TO 4 QUESTIONS VALIDATED 100% PERFECTLY!")
