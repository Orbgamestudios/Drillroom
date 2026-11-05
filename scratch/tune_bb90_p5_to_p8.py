import re

with open("/home/cgslinde/DrillRoom/DrillRoom/scratch/craft_bb90_p5_to_p8.py") as f:
    text = f.read()

# P5 adjustments
# Q25 (P5 Q1): ans=D (3). Make B longer than D.
text = text.replace(
    '"LQT2 destroys resting potassium conductance IK1, whereas LQT3 blocks inward L-type calcium channels",',
    '"LQT2 destroys resting potassium conductance IK1 in membrane, whereas LQT3 blocks inward L-type calcium",\n            "LQT2 blocks voltage-gated chloride channels in cells, whereas LQT3 accelerates delayed rectifier K+",\n            "LQT2 impairs repolarizing outward IKr, whereas LQT3 promotes sustained depolarizing late INa,L",'
)
text = text.replace(
    '"LQT2 blocks voltage-gated chloride channels, whereas LQT3 accelerates outward delayed rectifier K+",\n            "LQT2 impairs repolarizing outward IKr, whereas LQT3 promotes sustained depolarizing late INa,L influx"',
    ''
)

# Q26 (P5 Q2): ans=B (1). Make A longer than B.
text = text.replace(
    '"sudden opening of nuclear pore complexes allowing calcium leakage into the sarcoplasm of cells",',
    '"sudden opening of nuclear pore complexes allowing calcium leakage into the sarcoplasm of cells in heart",'
)

# Q29 (P5 Q5): ans=D (3). Make B longer than D.
text = text.replace(
    '"The isolated period of ventricular mechanical contraction occurring strictly during systole",',
    '"The isolated period of ventricular mechanical contraction occurring strictly during cardiac systole",'
)

# P6 adjustments
# Q32 (P6 Q2): ans=D (3).
text = text.replace(
    '"Oligomycin oxidizes all intramitochondrial NADH molecules into NAD+ to deplete electrons",\n            "Oligomycin covalently cleaves cytochrome c, severing electron flow between III and IV in cristae",\n            "Oligomycin opens giant outer membrane channels, dissipating all mitochondrial substrates",\n            "Proton pumping against a hyperpolarized electrochemical gradient becomes thermodynamically blocked"',
    '"Oligomycin oxidizes all intramitochondrial NADH molecules into NAD+ to deplete electron flow",\n            "Oligomycin covalently cleaves cytochrome c, severing electron transfer between III and IV in cristae",\n            "Oligomycin opens giant outer membrane channels, dissipating all mitochondrial substrate gradients",\n            "Proton pumping against a hyperpolarized electrochemical gradient is thermodynamically blocked"'
)

# Q33 (P6 Q3): ans=A (0). Make B longer than A.
text = text.replace(
    '"NADH translocates 12 H+ (4 at I, 4 at III, 4 at IV); FADH2 translocates 8 H+ (4 at III, 4 at IV)",',
    '"NADH translocates 12 H+ (4 at I, 4 at III, 4 at IV); FADH2 translocates 8 H+ (4 at III, 4 at IV) in runs",'
)

# Q34 (P6 Q4): ans=C (2). Make A longer than C.
text = text.replace(
    '"Complex I, preventing electron transfer from flavin mononucleotide to iron-sulfur centers",',
    '"Complex I, preventing electron transfer from flavin mononucleotide to iron-sulfur centers in complex",'
)
text = text.replace(
    '"Complex IV (cytochrome c oxidase), blocking terminal electron transfer to molecular oxygen",',
    '"Complex IV (cytochrome c oxidase), blocking terminal electron transfer to molecular oxygen in cristae",'
)

# Q35 (P6 Q5): ans=B (1). Make C longer than B.
text = text.replace(
    '"The matrix is more alkaline (higher pH) and electrically negative relative to the space",\n            "The matrix is more alkaline (higher pH) and electrically positive relative to the space",',
    '"The matrix is more alkaline (higher pH) and electrically negative relative to space",\n            "The matrix is more alkaline (higher pH) and electrically positive relative to the outer space",'
)

# Q36 (P6 Q6): ans=D (3). Make B longer than D.
text = text.replace(
    '"It selectively blocks oxygen consumption at Complex IV, releasing latent chemical enthalpy",\n            "It accelerates ATP synthase rotation to hydrolyze newly formed ATP into heat energy directly",\n            "It acts as a competitive substrate for Complex II, driving futile redox cycling in cristae",\n            "It allows protons to re-enter matrix without passing through ATP synthase, dissipating PMF as heat"',
    '"It selectively blocks oxygen consumption at Complex IV, releasing latent chemical enthalpy in cristae",\n            "It accelerates ATP synthase rotation to hydrolyze newly formed ATP into heat energy directly in BAT",\n            "It acts as a competitive substrate for Complex II, driving futile redox cycling in inner cristae",\n            "It allows protons to re-enter matrix without passing through ATP synthase, dissipating PMF as heat"'
)

# P7 adjustments
# Q37 (P7 Q1): ans=A (0). Equalize lens.
text = text.replace(
    '"RAG1/2 endonucleases are indispensable for initiating DNA cleavage at conserved RSSs",\n            "RAG1 is a transcriptional master regulator required for interleukin-7 receptor surface expression",\n            "RAG1 catalyzes non-homologous end joining ligation of broken chromosomal DNA strands",\n            "RAG1 phosphorylates Bruton tyrosine kinase to activate pre-B cell receptor signaling"',
    '"RAG1/2 endonucleases are indispensable for initiating DNA cleavage at conserved RSSs in lymphocytes",\n            "RAG1 is a transcriptional master regulator required for interleukin-7 receptor surface expression",\n            "RAG1 catalyzes non-homologous end joining ligation of broken chromosomal DNA strands in the marrow",\n            "RAG1 phosphorylates Bruton tyrosine kinase to activate pre-B cell receptor signaling cascades in cells"'
)

# Q38 (P7 Q2): ans=C (2). Equalize lens.
text = text.replace(
    '"Initial V(D)J recombination of immunoglobulin heavy and light chain variable loci in marrow",\n            "Junctional diversity generated by terminal deoxynucleotidyl transferase (TdT) nucleotide insertion",\n            "Somatic hypermutation (SHM) for affinity maturation and class-switch recombination (CSR)",\n            "Alternative RNA splicing of primary transcripts yielding membrane-bound versus secreted IgM"',
    '"Initial V(D)J recombination of immunoglobulin heavy and light chain variable loci in bone marrow",\n            "Junctional diversity generated by terminal deoxynucleotidyl transferase (TdT) nucleotide insertion",\n            "Somatic hypermutation (SHM) for affinity maturation and class-switch recombination (CSR) in nodes",\n            "Alternative RNA splicing of primary transcripts yielding membrane-bound versus secreted IgM forms"'
)

# Q39 (P7 Q3): ans=D (3). Make B longer than D.
text = text.replace(
    '"AID normally acts as a transcriptional repressor that suppresses baseline IgM synthesis in cells",\n            "IgM expression requires RAG1-mediated inversion, whereas other isotypes require RNA degradation",\n            "T-helper cells selectively destroy B cells that attempt to secrete IgG or IgA in lymph nodes",\n            "B cells can transcribe the default Cμ constant region, but cannot undergo CSR to downstream isotypes"',
    '"AID normally acts as a transcriptional repressor that suppresses baseline IgM synthesis in B lymphocytes",\n            "IgM expression requires RAG1-mediated inversion, whereas other isotypes require RNA degradation in cells",\n            "T-helper cells selectively destroy B cells that attempt to secrete IgG or IgA in secondary lymph nodes",\n            "B cells can transcribe default Cμ constant region, but cannot undergo CSR to downstream isotypes"'
)

# Q42 (P7 Q6): ans=C (2). Make B longer than C.
text = text.replace(
    '"During terminal differentiation of memory B lymphocytes into antibody-secreting plasma cells",\n            "During common lymphoid progenitor commitment to the B-cell lineage before heavy chain assembly",\n            "At the pre-B cell stage (transition from pro-B to mature pre-B) in the fetal liver and bone marrow",\n            "In peripheral germinal centers following CD40 co-stimulation and antigen challenge in spleen"',
    '"During terminal differentiation of memory B lymphocytes into antibody-secreting plasma cells in organs",\n            "During common lymphoid progenitor commitment to the B-cell lineage before heavy chain assembly stage",\n            "At the pre-B cell stage (transition from pro-B to mature pre-B) in the fetal liver and bone marrow",\n            "In peripheral germinal centers following CD40 co-stimulation and antigen challenge in the spleen"'
)

# Discretes adjustments
# Q44 (Discretes Q2): ans=B (1).
text = text.replace(
    '"Reducing: four separate bands at 50, 100, 150, 200 kDa; Non-reducing: a single 50 kDa band",\n            "Reducing: a single 50 kDa band; Non-reducing: a single 200 kDa band",\n            "Reducing: a single 200 kDa band; Non-reducing: a single 50 kDa band",\n            "Reducing: two distinct bands at 100 kDa; Non-reducing: a single 200 kDa band"',
    '"Reducing: four separate bands at 50, 100, 150, 200 kDa; Non-reducing: a single band",\n            "Reducing: a single sharp 50 kDa band; Non-reducing: a single intact 200 kDa band",\n            "Reducing: a single intact 200 kDa band; Non-reducing: a single sharp 50 kDa band",\n            "Reducing: two distinct bands at 100 kDa; Non-reducing: a single intact 200 kDa band"'
)

# Q47 (Discretes Q5): ans=A (0). Make B longer than A.
text = text.replace(
    '"All four children will inherit the maternal mitochondrial mutation and risk developing clinical disease",\n            "Only the two daughters will inherit the mutation, whereas both sons will remain completely unaffected",',
    '"All four children inherit the maternal mitochondrial mutation and risk developing clinical disease",\n            "Only the two daughters will inherit the mutation, whereas both sons will remain completely unaffected in life",'
)

# Q48 (Discretes Q6): ans=B (1). Make C longer than B.
text = text.replace(
    '"Peptide hormones are lipophilic and cross the plasma membrane to bind nuclear transcription factors",\n            "Peptide hormones act via cell-surface receptors and second messengers, while steroids alter gene expression",\n            "Steroid hormones circulate freely dissolved in plasma, whereas peptide hormones require carrier globulins",',
    '"Peptide hormones are lipophilic and cross the plasma membrane to bind nuclear transcription factors",\n            "Peptide hormones act via cell-surface receptors and second messengers, while steroids alter expression",\n            "Steroid hormones circulate freely dissolved in plasma, whereas peptide hormones require carrier globulin proteins",'
)

# Q49 (Discretes Q7): ans=C (2). Make D longer than C.
text = text.replace(
    '"Hemoglobin displays positive cooperativity, where O2 binding at one subunit increases affinity at other sites",\n            "Myoglobin contains four cooperative heme groups, whereas hemoglobin binds O2 through a single porphyrin"',
    '"Hemoglobin displays positive cooperativity, where O2 binding at one subunit increases affinity at other sites",\n            "Myoglobin contains four cooperative heme groups, whereas hemoglobin binds O2 through a single porphyrin ring"'
)

# Q52 (Discretes Q10): ans=B (1).
text = text.replace(
    '"A purine-rich Shine-Dalgarno consensus motif located upstream of the translation initiation codon",\n            "A 5\' 7-methylguanosine (m7G) triphosphate cap recognized by the eIF4E eukaryotic initiation factor",\n            "A polycistronic operon organization that translates multiple distinct open reading frames simultaneously",\n            "A formylmethionine (fMet) moiety loaded onto the initiator tRNA that pairs with the AUG codon"',
    '"A purine-rich Shine-Dalgarno consensus motif located upstream of the translation initiation codon in mRNA",\n            "A 5\' 7-methylguanosine (m7G) triphosphate cap recognized by the eIF4E eukaryotic initiation factor",\n            "A polycistronic operon organization that translates multiple distinct open reading frames simultaneously",\n            "A formylmethionine (fMet) moiety loaded onto initiator tRNA that pairs with the AUG start codon in cells"'
)

with open("/home/cgslinde/DrillRoom/DrillRoom/scratch/craft_bb90_p5_to_p8.py", "w") as f:
    f.write(text)

print("Replacement done!")
