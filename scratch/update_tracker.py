with open("/home/cgslinde/DrillRoom/DrillRoom/MCAT-CURRICULUM-AND-TOPIC-TRACKER.md", "r") as f:
    tracker = f.read()

# 1. Add Exam 9 Suite to the section-by-section listing under Section 3 (B/B)
exam8_suite_target = "* `exam_bb90_8_disc`: **Base Excision Repair (BER): DNA Glycosylases & AP Endonuclease**\n\n---"

exam9_suite_text = """* `exam_bb90_8_disc`: **Base Excision Repair (BER): DNA Glycosylases & AP Endonuclease**

#### Exam 9 Suite (26 Topics)
* `exam_bb90_9_p1 / exam_bb60_9_p1`: **Double-Strand Break Repair: Homologous Recombination (HR) & BRCA1/BRCA2**
* `exam_bb90_9_p1 / exam_bb60_9_p1`: **Double-Strand Break Repair: Non-Homologous End Joining (NHEJ) & Ku70/80**
* `exam_bb90_9_p2 / exam_bb60_9_p2`: **Chemical DNA Mutagens: Alkylating Agents & Cross-Linking Nitrogen Mustards**
* `exam_bb90_9_p2 / exam_bb60_9_p2`: **Somatic vs Germline Mutations & Evolutionary Heritability**
* `exam_bb90_9_p3 / exam_bb60_9_p3`: **Mendelian Autosomal Dominant Inheritance & Achondroplasia**
* `exam_bb90_9_p3 / exam_bb60_9_p3`: **Mendelian Autosomal Recessive Inheritance & Cystic Fibrosis (CFTR)**
* `exam_bb90_9_p4 / exam_bb60_9_p4`: **X-Linked Recessive Inheritance: Hemophilia A & Duchenne Muscular Dystrophy**
* `exam_bb90_9_p4 / exam_bb60_9_p4`: **X-Linked Dominant Inheritance: Fragile X & Rett Syndrome**
* `exam_bb90_9_p4 / exam_bb60_9_p4`: **Mitochondrial Maternal Inheritance & Heteroplasmy**
* `exam_bb90_9_p5 / exam_bb60_9_p5`: **Genetic Penetrance vs Expressivity in Human Disease**
* `exam_bb90_9_p5 / exam_bb60_9_p5`: **Genetic Linkage & Recombination Frequency (Centimorgans / Map Units)**
* `exam_bb90_9_p6`: **Eukaryotic Pre-mRNA Splicing: Spliceosome Assembly & Lariat Intermediate**
* `exam_bb90_9_p6`: **Alternative Splicing: Exon Skipping & Mutual Exclusion**
* `exam_bb90_9_p6`: **RNA Editing: Apolipoprotein B-100 vs B-48 Cytidine Deamination**
* `exam_bb90_9_p7`: **The Genetic Code: Wobble Hypothesis & Inosine Base-Pairing**
* `exam_bb90_9_p7`: **Aminoacyl-tRNA Synthetase Fidelity & The Double-Sieve Proofreading Mechanism**
* `exam_bb90_9_disc / exam_bb60_9_disc`: **Ribosome Architecture: A, P, E Sites & 28S rRNA Peptidyl Transferase Ribozyme**
* `exam_bb90_9_disc / exam_bb60_9_disc`: **Translational Control: Eukaryotic Initiation Factor-2 (eIF-2alpha) Phosphorylation**
* `exam_bb90_9_disc / exam_bb60_9_disc`: **Translation Elongation Factors (eEF1A / eEF2) & Diphtheria Toxin ADP-Ribosylation**
* `exam_bb90_9_disc`: **Nonsense-Mediated mRNA Decay (NMD) & Exon Junction Complexes**
* `exam_bb90_9_disc`: **Post-Translational Glycosylation: ER N-Linked vs Golgi O-Linked**
* `exam_bb90_9_disc`: **Ubiquitin-Proteasome System: E1, E2, and E3 Ubiquitin Ligase Substrate Specificity**
* `exam_bb90_9_disc`: **Zymogen Activation Cascades: Duodenal Enteropeptidase & Pancreatic Trypsinogen**
* `exam_bb90_9_disc`: **Protein Targeting & Cotranslational Translocation: Signal Recognition Particle (SRP) & Sec61**
* `exam_bb90_9_disc`: **Nuclear Transport: Nuclear Localization Signals (NLS), Importin Alpha/Beta & Ran GTPase**
* `exam_bb90_9_disc`: **Mitochondrial Protein Import: Amphipathic Presequence & TOM/TIM23 Translocases**

---"""

if exam8_suite_target in tracker:
    tracker = tracker.replace(exam8_suite_target, exam9_suite_text)
    print("Added Exam 9 Suite to summary list")
else:
    print("WARNING: exam8_suite_target not found!")

# 2. Update topics 612-637 in master list
replacements = {
    "- [ ] **612. Double-Strand Break Repair: Homologous Recombination (HR) & BRCA1/BRCA2**":
    "- [x] **612. Double-Strand Break Repair: Homologous Recombination (HR) & BRCA1/BRCA2**  — `exam_bb90_9_p1 / exam_bb60_9_p1`",

    "- [ ] **613. Double-Strand Break Repair: Non-Homologous End Joining (NHEJ) & Ku70/80**":
    "- [x] **613. Double-Strand Break Repair: Non-Homologous End Joining (NHEJ) & Ku70/80**  — `exam_bb90_9_p1 / exam_bb60_9_p1`",

    "- [ ] **614. Chemical DNA Mutagens: Alkylating Agents & Cross-Linking Nitrogen Mustards**":
    "- [x] **614. Chemical DNA Mutagens: Alkylating Agents & Cross-Linking Nitrogen Mustards**  — `exam_bb90_9_p2 / exam_bb60_9_p2`",

    "- [ ] **615. Somatic vs Germline Mutations & Evolutionary Heritability**":
    "- [x] **615. Somatic vs Germline Mutations & Evolutionary Heritability**  — `exam_bb90_9_p2 / exam_bb60_9_p2`",

    "- [ ] **616. Mendelian Autosomal Dominant Inheritance & Achondroplasia**":
    "- [x] **616. Mendelian Autosomal Dominant Inheritance & Achondroplasia**  — `exam_bb90_9_p3 / exam_bb60_9_p3`",

    "- [ ] **617. Mendelian Autosomal Recessive Inheritance & Cystic Fibrosis (CFTR)**":
    "- [x] **617. Mendelian Autosomal Recessive Inheritance & Cystic Fibrosis (CFTR)**  — `exam_bb90_9_p3 / exam_bb60_9_p3`",

    "- [ ] **618. X-Linked Recessive Inheritance: Hemophilia A & Duchenne Muscular Dystrophy**":
    "- [x] **618. X-Linked Recessive Inheritance: Hemophilia A & Duchenne Muscular Dystrophy**  — `exam_bb90_9_p4 / exam_bb60_9_p4`",

    "- [ ] **619. X-Linked Dominant Inheritance: Fragile X & Rett Syndrome**":
    "- [x] **619. X-Linked Dominant Inheritance: Fragile X & Rett Syndrome**  — `exam_bb90_9_p4 / exam_bb60_9_p4`",

    "- [ ] **620. Mitochondrial Maternal Inheritance & Heteroplasmy**":
    "- [x] **620. Mitochondrial Maternal Inheritance & Heteroplasmy**  — `exam_bb90_9_p4 / exam_bb60_9_p4`",

    "- [ ] **621. Genetic Penetrance vs Expressivity in Human Disease**":
    "- [x] **621. Genetic Penetrance vs Expressivity in Human Disease**  — `exam_bb90_9_p5 / exam_bb60_9_p5`",

    "- [ ] **622. Genetic Linkage & Recombination Frequency (Centimorgans / Map Units)**":
    "- [x] **622. Genetic Linkage & Recombination Frequency (Centimorgans / Map Units)**  — `exam_bb90_9_p5 / exam_bb60_9_p5`",

    "- [ ] **623. Eukaryotic Pre-mRNA Splicing: Spliceosome Assembly & Lariat Intermediate**":
    "- [x] **623. Eukaryotic Pre-mRNA Splicing: Spliceosome Assembly & Lariat Intermediate**  — `exam_bb90_9_p6`",

    "- [ ] **624. Alternative Splicing: Exon Skipping & Mutual Exclusion**":
    "- [x] **624. Alternative Splicing: Exon Skipping & Mutual Exclusion**  — `exam_bb90_9_p6`",

    "- [ ] **625. RNA Editing: Apolipoprotein B-100 vs B-48 Cytidine Deamination**":
    "- [x] **625. RNA Editing: Apolipoprotein B-100 vs B-48 Cytidine Deamination**  — `exam_bb90_9_p6`",

    "- [ ] **626. The Genetic Code: Wobble Hypothesis & Inosine Base-Pairing**":
    "- [x] **626. The Genetic Code: Wobble Hypothesis & Inosine Base-Pairing**  — `exam_bb90_9_p7`",

    "- [ ] **627. Aminoacyl-tRNA Synthetase Fidelity & The Double-Sieve Proofreading Mechanism**":
    "- [x] **627. Aminoacyl-tRNA Synthetase Fidelity & The Double-Sieve Proofreading Mechanism**  — `exam_bb90_9_p7`",

    "- [ ] **628. Prokaryotic Ribosome Structure: 70S (50S + 30S) & Antibiotic Targets**":
    "- [x] **628. Ribosome Structure & Peptidyl Transferase Ribozyme (28S/23S rRNA)**  — `exam_bb90_9_disc / exam_bb60_9_disc`",

    "- [ ] **629. Eukaryotic Ribosome Structure: 80S (60S + 40S) & Ribosomal Toxins**":
    "- [x] **629. Eukaryotic Translation Initiation & eIF2alpha Phosphorylation Stress Response**  — `exam_bb90_9_disc / exam_bb60_9_disc`",

    "- [ ] **630. Translational Control: Eukaryotic Initiation Factor-2 (eIF-2) Phosphorylation**":
    "- [x] **630. Translation Elongation Factors (eEF1A / eEF2) & Diphtheria Toxin ADP-Ribosylation**  — `exam_bb90_9_disc / exam_bb60_9_disc`",

    "- [ ] **631. The Trp Operon: Transcriptional Attenuation Mechanism**":
    "- [x] **631. Nonsense-Mediated mRNA Decay (NMD) & Exon Junction Complexes (EJCs)**  — `exam_bb90_9_disc`",

    "- [ ] **632. Chromatin Remodeling: Histone Deacetylases (HDACs) & Transcriptional Repression**":
    "- [x] **632. Post-Translational Glycosylation: ER N-Linked vs Golgi O-Linked**  — `exam_bb90_9_disc`",

    "- [ ] **633. DNA Methylation: DNA Methyltransferases (DNMT1 vs DNMT3A/3B)**":
    "- [x] **633. Ubiquitin-Proteasome System: E1, E2, and E3 Ubiquitin Ligase Specificity**  — `exam_bb90_9_disc`",

    "- [ ] **634. Genomic Imprinting: Epigenetic Parent-of-Origin Expression**":
    "- [x] **634. Zymogen Activation Cascades: Duodenal Enteropeptidase & Pancreatic Proteases**  — `exam_bb90_9_disc`",

    "- [ ] **635. X-Chromosome Inactivation (Lyonization) & The Xist lncRNA**":
    "- [x] **635. Protein Sorting & Targeting: N-Terminal Signal Peptide, SRP & Sec61 Translocon**  — `exam_bb90_9_disc`",

    "- [ ] **636. Enhancer Loops & Mediator Complex in Eukaryotic Transcription**":
    "- [x] **636. Nuclear Localization Signals (NLS), Importin Alpha/Beta & Ran GTPase Transport**  — `exam_bb90_9_disc`",

    "- [ ] **637. Polymerase Chain Reaction (PCR): Primers, Taq Polymerase & Thermal Cycles**":
    "- [x] **637. Mitochondrial Protein Import: N-Terminal Transit Peptide & TOM/TIM Machinery**  — `exam_bb90_9_disc`"
}

for k, v in replacements.items():
    if k in tracker:
        tracker = tracker.replace(k, v)
    else:
        print(f"WARNING: Topic target not found: {k}")

with open("/home/cgslinde/DrillRoom/DrillRoom/MCAT-CURRICULUM-AND-TOPIC-TRACKER.md", "w") as f:
    f.write(tracker)

print("Updated MCAT-CURRICULUM-AND-TOPIC-TRACKER.md successfully")
