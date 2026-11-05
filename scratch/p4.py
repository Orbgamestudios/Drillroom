p4 = {
  "id": "exam_bb90_9_p4",
  "sec": "B/B",
  "topic": "Sex-Linked & Non-Mendelian Genetics: X-Linked Recessive/Dominant, Mitochondrial Inheritance & Heteroplasmy",
  "sheet": 4,
  "label": "Biological and Biochemical Foundations of Living Systems",
  "examId": "bb90_9",
  "passage": """<div class=\"ttl\">Passage 4 (Questions 19&ndash;24)</div>
<p>Non-autosomal inheritance paradigms deviate fundamentally from standard Mendelian segregation ratios due to unequal chromosomal distribution and non-nuclear organellar genomes. X-linked traits reside on the sex chromosome X. In X-linked recessive disorders, such as Duchenne muscular dystrophy (<em>DMD</em>) and Hemophilia A (<em>F8</em>), hemizygous males (<em>X</em><sup>r</sup><em>Y</em>) invariably manifest the disease phenotype because they lack a second homologous counter-allele. Heterozygous females (<em>X</em><sup>R</sup><em>X</em><sup>r</sup>) are typically asymptomatic carriers; however, due to lyonization—the random transcriptional inactivation of one X chromosome in early female blastocysts mediated by the <em>Xist</em> long non-coding RNA—skewed inactivation can rarely yield mild manifestations in carrier females. Crucially, affected males cannot transmit an X-linked recessive trait to their sons, but transmit the mutant allele to 100% of their daughters.</p>
<p>In contrast, X-linked dominant disorders, such as Fragile X-associated tremor/ataxia syndrome and X-linked hypophosphatemic rickets (<em>PHEX</em>), manifest in both heterozygous females (<em>X</em><sup>D</sup><em>X</em><sup>d</sup>) and hemizygous males (<em>X</em><sup>D</sup><em>Y</em>). Pedigrees feature a pathognomonic absence of male-to-male transmission: an affected father transmits the dominant trait to 100% of his daughters and 0% of his sons, whereas an affected heterozygous mother transmits the condition to 50% of her offspring regardless of sex.</p>
<p>Mitochondrial inheritance governs traits encoded by the circular 16.6-kb mitochondrial DNA (mtDNA), which encodes 13 core polypeptides of the electron transport chain, 22 tRNAs, and 2 rRNAs. Mitochondria are transmitted exclusively through the oocyte cytoplasm; sperm mitochondria are tagged with ubiquitin and selectively degraded by maternal autophagy inside the fertilized egg. Consequently, an affected mother transmits the trait to 100% of her biological offspring, whereas an affected father never transmits the condition to any child. Intracellular mtDNA exists in multiple copies (hundreds to thousands per cell). In mitochondrial disorders such as Mitochondrial Encephalomyopathy, Lactic Acidosis, and Stroke-like episodes (MELAS, caused by m.3243A&rarr;G in <em>MT-TL1</em>), mutant and wild-type mtDNA coexist—a state known as heteroplasmy. Clinical disease manifests only when the proportion of mutant mtDNA exceeds a tissue-specific bioenergetic threshold (typically 60–80%), primarily debilitating oxidative tissues such as skeletal muscle and brain.</p>
<p>A genetics consortium tracked three multigenerational families representing Duchenne muscular dystrophy, X-linked hypophosphatemia, and MELAS. Heteroplasmy levels and electron transport Complex I activity were measured in muscle biopsies (Table 1).</p>
<table class=\"tbl\">
  <caption>Table 1 Pedigree segregation metrics, muscle heteroplasmy, and Complex I respiration across human disease kindreds</caption>
  <thead>
    <tr><th>Pedigree &amp; Proband</th><th>Suspected Inheritance Mode</th><th>Maternal Transmission (%)</th><th>Paternal to Daughters (%)</th><th>Paternal to Sons (%)</th><th>Muscle Heteroplasmy (%)</th><th>Complex I (nmol/min/mg)</th></tr>
  </thead>
  <tbody>
    <tr><td>Family A: Proband Male (<em>DMD</em>)</td><td>X-Linked Recessive</td><td>50% (from carrier mother)</td><td>100% (carrier daughters)</td><td>0%</td><td>0% (Nuclear Gene)</td><td>88.4 &plusmn; 4.2</td></tr>
    <tr><td>Family B: Proband Male (<em>PHEX</em>)</td><td>X-Linked Dominant</td><td>50% (from affected mother)</td><td>100% (affected daughters)</td><td>0%</td><td>0% (Nuclear Gene)</td><td>86.9 &plusmn; 3.8</td></tr>
    <tr><td>Family C-1: Mother (Asymptomatic)</td><td>Mitochondrial (Low Load)</td><td>100% (to all 4 children)</td><td>N/A</td><td>N/A</td><td>24.5 &plusmn; 2.1%</td><td>79.2 &plusmn; 3.6</td></tr>
    <tr><td>Family C-2: Son (Severe MELAS)</td><td>Mitochondrial (High Load)</td><td>N/A</td><td>0% (to his 2 daughters)</td><td>0% (to his 1 son)</td><td>84.2 &plusmn; 3.5%</td><td>14.8 &plusmn; 1.6</td></tr>
    <tr><td>Family C-3: Daughter (Myopathy)</td><td>Mitochondrial (Intermediate)</td><td>100% (to both children)</td><td>N/A</td><td>N/A</td><td>62.8 &plusmn; 3.1%</td><td>46.5 &plusmn; 2.9</td></tr>
  </tbody>
</table>""",
  "qs": [
    {
      "q": "An affected male with an X-linked dominant condition marries an unaffected female. What fraction of their daughters and sons will exhibit the trait?",
      "ch": [
        "50% of daughters and 50% of sons, because the dominant allele segregates equally among gametes in meiosis",
        "100% of daughters and 0% of sons, because daughters receive his X chromosome and sons receive his Y chromosome",
        "100% of sons and 0% of daughters, because the dominant condition requires hemizygous expression to manifest",
        "0% of daughters and 100% of sons, because male meiosis preferentially packages mutant X alleles into bodies"
      ],
      "a": 1,
      "e": "<strong>Inheritance patterns of X-linked dominant disorders (Topic 619):</strong> An affected male has the hemizygous genotype $X^D Y$, and the unaffected female has the homozygous genotype $X^d X^d$. In human sexual reproduction, sex determination is chromosomal: the father contributes his single $X$ chromosome ($X^D$) to 100% of his female offspring (who receive one $X$ from each parent: $X^D X^d$), and his $Y$ chromosome to 100% of his male offspring (who receive their $X$ exclusively from the mother: $X^d Y$). Because the trait is **dominant**, the presence of a single $X^D$ allele is fully sufficient to produce the disease phenotype in daughters ($100\%$ affected). Conversely, sons receive the father's unaffected $Y$ chromosome and an unaffected maternal $X^d$ chromosome, meaning **$0\%$ of sons** inherit the allele or exhibit the condition. This absolute dichotomy—100% affected daughters and 0% affected sons from an affected father—is the diagnostic hallmark of X-linked dominant pedigrees.<br><br><em>Distractor Traps:</em><br>&bull; A describes the transmission from an affected *heterozygous mother* ($X^D X^d \times X^d Y$), who transmits the allele to 50% of her sons and 50% of her daughters.<br>&bull; C displays complete Directional Inversion; sons never receive an X chromosome from their father.<br>&bull; D is biologically nonsensical; meiotic polar bodies are generated exclusively during female oogenesis, not male spermatogenesis."
    },
    {
      "q": "Why do Family C-2 (84.2% heteroplasmy) and C-3 (62.8% heteroplasmy) display drastically different clinical severity despite sharing the same mutation?",
      "ch": [
        "Individual C-2 possesses an additional nuclear mutation that completely disables mitochondrial transcription",
        "Individual C-3 underwent lyonization that selectively silenced the maternal mitochondrial genome in myocytes",
        "Individual C-2 lacks peroxisomal enzymes needed to import wild-type mitochondrial tRNAs from the cytoplasm",
        "Mitochondrial disease exhibits a threshold effect where respiratory failure occurs when mutant mtDNA exceeds 70%"
      ],
      "a": 3,
      "e": "<strong>Mitochondrial heteroplasmy, replicative segregation, and the threshold effect (Topic 620):</strong> Human cells contain hundreds to thousands of individual mitochondrial DNA (mtDNA) genomes. In mitochondrial genetic disorders, wild-type and mutant mtDNA molecules coexist within individual cells—a non-Mendelian genetic state termed **heteroplasmy**. During embryonic cell division, mitochondria replicate and distribute randomly into daughter cells by replicative segregation, resulting in different tissues and individuals harboring varying percentages of mutant genomes. Mitochondrial disease does not follow linear dose-response curves; rather, it exhibits a strict **threshold effect**. Biochemical cellular respiration relies on redundancy: oxidative phosphorylation functions normally as long as the fraction of wild-type mtDNA is sufficient to produce adequate respiratory enzymes. However, once the proportion of mutant mtDNA surpasses a critical bioenergetic threshold—typically 70% to 80% in high-energy oxidative tissues like skeletal muscle—electron transport capacity collapses. In Family C-3, 62.8% heteroplasmy remains near or below the critical threshold, preserving partial Complex I activity (46.5 nmol/min/mg) and resulting in mild/moderate symptoms. In Family C-2, 84.2% heteroplasmy clearly surpasses the threshold, crashing Complex I activity to 14.8 nmol/min/mg and triggering severe, life-threatening MELAS.<br><br><em>Distractor Traps:</em><br>&bull; A is an unsupported assumption; the passage explicitly attributes the clinical divergence to heteroplasmy levels, not a second unmentioned nuclear mutation.<br>&bull; B describes Lyonization (X-chromosome inactivation); mitochondrial DNA is cytoplasmic and circular, not nuclear, and never undergoes X-inactivation.<br>&bull; C describes mitochondrial tRNA import from peroxisomes; mitochondria transcribe their own 22 tRNAs from mtDNA and do not import tRNAs via peroxisomes."
    },
    {
      "q": "Which molecular mechanism enforces strict maternal inheritance of human mitochondrial DNA and prevents transmission of paternal mtDNA?",
      "ch": [
        "Paternal mitochondria in the fertilizing sperm are ubiquitinated and degraded by maternal autophagosomes in eggs",
        "The mitochondrial genome of mature spermatozoa lacks an origin of replication and cannot replicate in zygotes",
        "Maternal DNA polymerases selectively methylate paternal mitochondrial DNA to induce rapid endonuclease cleavage",
        "Sperm mitochondria enter the nuclear envelope upon fertilization, where they are converted into heterochromatin"
      ],
      "a": 0,
      "e": "<strong>Molecular mechanisms of maternal mitochondrial inheritance (Topic 620):</strong> In humans and nearly all mammals, mitochondrial DNA is transmitted in a strictly maternal fashion. While mature spermatozoa contain approximately 50 to 100 mitochondria in their midpiece to power flagellar motility, paternal mitochondria are actively targeted for destruction upon entering the oocyte cytoplasm. During spermatogenesis and immediately upon fertilization, paternal mitochondria are tagged with **ubiquitin** by specialized ubiquitin ligases (e.g., Parkin/Mul1). The egg's internal surveillance machinery, particularly the selective autophagy pathway (**mitophagy** coordinated by p62/SQSTM1 and LC3), recognizes these polyubiquitinated paternal mitochondria and engulfs them within autophagosomes. These autophagosomes fuse with maternal lysosomes, leading to the rapid, complete degradation of all paternal mitochondria and their mtDNA before the first embryonic cleavage. Combined with the massive numerical disparity (a human oocyte contains 100,000 to 500,000 mtDNA copies compared to < 100 in sperm), maternal transmission is absolute.<br><br><em>Distractor Traps:</em><br>&bull; B is factually incorrect; sperm mtDNA possesses the identical heavy- and light-strand origins of replication (O_H and O_L) as maternal mtDNA.<br>&bull; C describes bacterial restriction-modification systems (methylation and restriction endonucleases), which do not operate in eukaryotic zygotic mitochondria.<br>&bull; D describes nuclear envelope entry and heterochromatinization; mitochondria are cytoplasmic organellar organelles that never enter the nucleus."
    },
    {
      "q": "A female carrier of Duchenne muscular dystrophy unexpectedly exhibits mild focal muscle weakness and elevated serum creatine kinase. What genetic event explains this?",
      "ch": [
        "Meiotic non-disjunction in the maternal lineage generated a 45,X karyotype lacking normal dystrophin alleles",
        "The wild-type dystrophin allele underwent somatic reversion to a frameshift insertion in early myoblasts",
        "Skewed X-inactivation resulted in preferential silencing of the paternal X chromosome bearing normal dystrophin",
        "The dystrophin gene underwent somatic recombination with the Y chromosome, creating an unexpressed pseudogene"
      ],
      "a": 2,
      "e": "<strong>Lyonization, mosaicism, and manifesting heterozygotes in X-linked recessive traits (Topic 618):</strong> In female mammalian embryos ($XX$), dosage compensation between females ($XX$) and males ($XY$) is achieved through **lyonization** (X-chromosome inactivation). Around the late blastocyst stage, each cell randomly and independently silences either the maternal $X$ ($X_m$) or the paternal $X$ ($X_p$) into a condensed, transcriptionally silent Barr body. In most females, this inactivation is roughly equal ($50:50$ distribution across tissues), meaning female carriers of Duchenne muscular dystrophy (a recessive *DMD* mutation on one X) express sufficient wild-type dystrophin from the active X in 50% of myonuclei to maintain normal muscle integrity. However, by stochastic variation during early commitment, non-random or **skewed X-inactivation** can occur, where the X chromosome bearing the healthy wild-type allele is silenced in a high percentage (e.g., > 80–90%) of skeletal muscle progenitor cells. In these cells, the mutant X remains active, leaving the myofibers deficient in functional dystrophin. This results in patchy sarcolemmal fragility, focal muscle fiber necrosis, leakage of creatine kinase into the serum, and clinical weakness—a condition known as a **manifesting carrier**.<br><br><em>Distractor Traps:</em><br>&bull; A describes Turner syndrome ($45,X$), which is a rare whole-chromosome aneuploidy causing characteristic syndromic features (short stature, webbed neck), not the standard genetic mechanism of manifesting carriers.<br>&bull; B describes somatic reversion, which would correct a mutant allele rather than causing a healthy carrier to develop symptoms.<br>&bull; D describes recombination with the Y chromosome; female carriers possess two X chromosomes ($XX$) and lack a Y chromosome entirely."
    },
    {
      "q": "Individual C-2 (a male with severe MELAS) has three children with an unaffected woman. What is the probability that any of his children will inherit MELAS?",
      "ch": [
        "100%, because mitochondrial mutations are dominant and express complete penetrance across all descendants",
        "0%, because mitochondrial DNA is transmitted exclusively through the maternal lineage and males never pass mtDNA",
        "50%, because paternal mitochondria contribute half of the initial mitochondrial pool during implantation",
        "25%, because paternal mitochondrial transmission follows autosomal recessive recurrence risks in families"
      ],
      "a": 1,
      "e": "<strong>Paternal transmission exclusion in mitochondrial pedigrees (Topic 620):</strong> Mitochondrial disorders follow strict maternal inheritance because human zygotes inherit their mitochondrial DNA exclusively from the oocyte cytoplasm. While affected females transmit mutant mtDNA to 100% of their biological offspring (as demonstrated by Family C-1 transmitting to all 4 children and C-3 transmitting to both children in Table 1), **affected males never transmit their mitochondrial mutations to their progeny**. Any paternal mitochondria introduced by the sperm during fertilization are systematically destroyed by ubiquitin-mediated mitophagy inside the egg. Consequently, the children of male Individual C-2 will receive 100% of their mitochondria from their unaffected mother. The probability that any of his children will inherit the m.3243A&rarr;G mutation or develop MELAS is strictly **0%**.<br><br><em>Distractor Traps:</em><br>&bull; A confuses maternal mitochondrial transmission with paternal transmission; while affected mothers transmit to ~100% of offspring, affected fathers transmit to 0%.<br>&bull; C is a True Fact Wrong Question / Mendelian Misattribution trap; biparental $50:50$ contribution applies to autosomal nuclear genes, not cytoplasmic mitochondrial DNA.<br>&bull; D confuses mitochondrial inheritance with Mendelian autosomal recessive inheritance."
    },
    {
      "q": "Why does the m.3243A>G mutation in MT-TL1 (encoding tRNA-Leu) directly diminish mitochondrial respiratory Complex I activity?",
      "ch": [
        "The mutation prevents the transcription of all 13 mitochondrial mRNAs by destabilizing the core promoter",
        "The mutation halts the import of nuclear-encoded electron transport chain subunits through the TOM complex",
        "The mutation converts the anticodon of tRNA-Leu into an Amber stop codon that prematurely truncates proteins",
        "Defective tRNA-Leu impairs mitochondrial translation of seven hydrophobic Complex I core subunits from mtDNA"
      ],
      "a": 3,
      "e": "<strong>Mitochondrial translation and respiratory chain subunit architecture (Topic 620):</strong> Human mitochondrial DNA (mtDNA) contains only 37 genes: 2 rRNAs, 22 tRNAs, and 13 polypeptides. All 13 polypeptides are essential, highly hydrophobic transmembrane subunits of the oxidative phosphorylation system: 7 subunits of NADH dehydrogenase (Complex I: ND1, ND2, ND3, ND4, ND4L, ND5, ND6), 1 subunit of Complex III (cytochrome b), 3 subunits of Cytochrome c oxidase (Complex IV: COX1, COX2, COX3), and 2 subunits of ATP synthase (Complex V: ATP6, ATP8). The m.3243A&rarr;G mutation resides in the *MT-TL1* gene, which encodes mitochondrial transfer RNA leucine ($tRNA^{\text{Leu(UUR)}}$). The mutation alters the D-loop/anticodon structural conformation of $tRNA^{\text{Leu}}$, severely impairing aminoacylation and codon recognition on mitoribosomes. Because Complex I requires seven mtDNA-encoded subunits that are rich in leucine residues, defective mitochondrial translation disproportionately halts the assembly and enzymatic function of Complex I. In Table 1, high heteroplasmy in Individual C-2 crashes Complex I activity to 14.8 nmol/min/mg, causing lactic acidosis because cells are forced to rely on anaerobic glycolysis for ATP.<br><br><em>Distractor Traps:</em><br>&bull; A is a Mechanism Misattribution trap; the mutation is in a transfer RNA gene, not in the mitochondrial promoter (D-loop heavy/light strand promoters HSP/LSP), so transcription of polycistronic RNA still occurs.<br>&bull; B describes the nuclear-encoded protein import machinery (TOM/TIM), which operates independently of mitochondrial tRNA sequence.<br>&bull; C describes an Amber nonsense suppressor mutation; m.3243A&rarr;G alters tRNA structure, not the anticodon loop into an Amber (UAG) reader."
    }
  ]
}

from check_draft import test_lengths
print("Checking P4 lengths:")
for i, q in enumerate(p4["qs"]):
    test_lengths(i+19, q["ch"])
