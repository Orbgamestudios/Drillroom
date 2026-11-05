with open("/home/cgslinde/DrillRoom/DrillRoom/scratch/craft_bb90_p5_to_p8.py") as f:
    text = f.read()

# Q25
text = text.replace(
    '''            "LQT2 accelerates inward Phase 0 depolarization, whereas LQT3 suppresses transient Phase 1 efflux",
            "LQT2 destroys resting potassium conductance IK1 in membrane, whereas LQT3 blocks inward L-type calcium",
            "LQT2 blocks voltage-gated chloride channels in cells, whereas LQT3 accelerates delayed rectifier K+",
            "LQT2 impairs repolarizing outward IKr, whereas LQT3 promotes sustained depolarizing late INa,L",''',
    '''            "LQT2 accelerates inward Phase 0 depolarization, whereas LQT3 suppresses transient Phase 1 efflux",
            "LQT2 destroys resting potassium conductance IK1, whereas LQT3 blocks inward L-type calcium channels",
            "LQT2 blocks voltage-gated chloride channels in cells, whereas LQT3 accelerates delayed rectifier K+",
            "LQT2 impairs repolarizing outward IKr, whereas LQT3 promotes sustained late INa,L influx in cells",'''
)

# Q26
text = text.replace(
    '''            "sudden opening of nuclear pore complexes allowing calcium leakage into the sarcoplasm of cells in heart",
            "re-activation of voltage-gated L-type Ca2+ channels (Cav1.2) during prolonged Phase 2/3 plateaus",
            "spontaneous ATP depletion within the matrix causing rapid potassium channel opening in cells",
            "abrupt efflux of divalent magnesium ions through sarcolemmal calcium-activated pump units",''',
    '''            "sudden opening of nuclear pore complexes allowing calcium leakage into the sarcoplasm of myocytes",
            "re-activation of voltage-gated L-type Ca2+ channels (Cav1.2) during prolonged Phase 2/3 plateaus",
            "spontaneous ATP depletion within the matrix causing rapid potassium channel opening in myocytes",
            "abrupt efflux of divalent magnesium ions through sarcolemmal calcium-activated pump complexes",'''
)

# Q29
text = text.replace(
    '''            "The time required for electrical conduction to traverse the atrioventricular AV node alone",
            "The isolated period of ventricular mechanical contraction occurring strictly during cardiac systole",
            "The duration of atrial depolarization and subsequent repolarization prior to the QRS wave",
            "The total time required for ventricular depolarization and subsequent complete repolarization",''',
    '''            "The time required for electrical conduction to traverse the atrioventricular AV node alone in heart",
            "The isolated period of ventricular mechanical contraction occurring strictly during systole phase",
            "The duration of atrial depolarization and subsequent repolarization prior to the QRS wave in rhythm",
            "The total time required for ventricular depolarization and subsequent complete repolarization",'''
)

# Q32
text = text.replace(
    '''            "Oligomycin oxidizes all intramitochondrial NADH molecules into NAD+ to deplete electron flow",
            "Oligomycin covalently cleaves cytochrome c, severing electron transfer between III and IV in cristae",
            "Oligomycin opens giant outer membrane channels, dissipating all mitochondrial substrate gradients",
            "Proton pumping against a hyperpolarized electrochemical gradient is thermodynamically blocked",''',
    '''            "Oligomycin oxidizes all intramitochondrial NADH molecules into NAD+ to deplete electron pools",
            "Oligomycin covalently cleaves cytochrome c, severing electron transfer between III and IV cristae",
            "Oligomycin opens giant outer membrane channels, dissipating all mitochondrial substrate gradients",
            "Proton pumping against a hyperpolarized electrochemical gradient is thermodynamically arrested",'''
)

# Q33
text = text.replace(
    '''            "NADH translocates 10 H+ (4 at I, 4 at III, 2 at IV); FADH2 translocates 6 H+ (4 at III, 2 at IV)",
            "NADH translocates 12 H+ (4 at I, 4 at III, 4 at IV); FADH2 translocates 8 H+ (4 at III, 4 at IV) in runs",
            "NADH translocates 8 H+ (4 at I, 2 at III, 2 at IV); FADH2 translocates 4 H+ (2 at III, 2 at IV)",
            "NADH translocates 6 H+ (2 at I, 2 at III, 2 at IV); FADH2 translocates 3 H+ (2 at III, 1 at IV)",''',
    '''            "NADH translocates 10 H+ (4 at I, 4 at III, 2 at IV); FADH2 translocates 6 H+ (4 at III, 2 at IV)",
            "NADH translocates 12 H+ (4 at I, 4 at III, 4 at IV); FADH2 translocates 8 H+ (4 at III, 4 at IV) net",
            "NADH translocates 8 H+ (4 at I, 2 at III, 2 at IV); FADH2 translocates 4 H+ (2 at III, 2 at IV) net",
            "NADH translocates 6 H+ (2 at I, 2 at III, 2 at IV); FADH2 translocates 3 H+ (2 at III, 1 at IV) net",'''
)

# Q34
text = text.replace(
    '''            "Complex I, preventing electron transfer from flavin mononucleotide to iron-sulfur centers in complex",
            "Complex II, preventing oxidation of succinate into fumarate during the citric acid cycle",
            "Complex IV (cytochrome c oxidase), blocking terminal electron transfer to molecular oxygen in cristae",
            "Complex III (cytochrome bc1), preventing ubiquinol oxidation via the Q cycle mechanism",''',
    '''            "Complex I, preventing electron transfer from flavin mononucleotide to iron-sulfur centers in core",
            "Complex II, preventing oxidation of succinate into fumarate during the citric acid cycle in cells",
            "Complex IV (cytochrome c oxidase), blocking terminal electron transfer to molecular oxygen gas",
            "Complex III (cytochrome bc1), preventing ubiquinol oxidation via the Q cycle mechanism in cristae",'''
)

# Q35
text = text.replace(
    '''            "The matrix is more acidic (lower pH) and electrically positive relative to the space",
            "The matrix is more alkaline (higher pH) and electrically negative relative to space",
            "The matrix is more alkaline (higher pH) and electrically positive relative to the outer space",
            "The matrix is iso-osmolar with identical pH and zero potential relative to the space",''',
    '''            "The matrix is more acidic (lower pH) and electrically positive relative to space in organelle",
            "The matrix is more alkaline (higher pH) and electrically negative relative to space in organelle",
            "The matrix is more alkaline (higher pH) and electrically positive relative to the outer organelle",
            "The matrix is iso-osmolar with identical pH and zero potential relative to space in organelle",'''
)

# Q39
text = text.replace(
    '''            "AID normally acts as a transcriptional repressor that suppresses baseline IgM synthesis in B lymphocytes",
            "IgM expression requires RAG1-mediated inversion, whereas other isotypes require RNA degradation in cells",
            "T-helper cells selectively destroy B cells that attempt to secrete IgG or IgA in secondary lymph nodes",
            "B cells can transcribe default Cμ constant region, but cannot undergo CSR to downstream isotypes",''',
    '''            "AID normally acts as a transcriptional repressor that suppresses baseline IgM synthesis in B lymphocytes",
            "IgM expression requires RAG1-mediated inversion, whereas other isotypes require RNA degradation in cells",
            "T-helper cells selectively destroy B cells that attempt to secrete IgG or IgA in secondary lymph nodes",
            "B cells can transcribe the default Cμ constant region, but cannot undergo CSR to other isotypes in body",'''
)

# Q47
text = text.replace(
    '''            "All four children inherit the maternal mitochondrial mutation and risk developing clinical disease",
            "Only the two daughters will inherit the mutation, whereas both sons will remain completely unaffected in life",
            "Only the two sons will inherit the mutation via non-recombining holandric Y-chromosome transmission",
            "Fifty percent of the children will inherit the mutation following typical Mendelian dominant genetics",''',
    '''            "All four children inherit the maternal mitochondrial mutation and risk developing clinical symptoms",
            "Only the two daughters will inherit the mutation, whereas both sons will remain completely unaffected here",
            "Only the two sons will inherit the mutation via non-recombining holandric Y-chromosome transmission line",
            "Fifty percent of the children will inherit the mutation following typical Mendelian dominant genetics",'''
)

# Q48
text = text.replace(
    '''            "Peptide hormones are lipophilic and cross the plasma membrane to bind nuclear transcription factors",
            "Peptide hormones act via cell-surface receptors and second messengers, while steroids alter expression",
            "Steroid hormones circulate freely dissolved in plasma, whereas peptide hormones require carrier globulin proteins",
            "Peptide hormones are synthesized directly from cholesterol, whereas steroid hormones translate from mRNA",''',
    '''            "Peptide hormones are lipophilic and cross the plasma membrane to bind nuclear transcription factors in cell",
            "Peptide hormones act via cell-surface receptors and second messengers, while steroids alter expression",
            "Steroid hormones circulate freely dissolved in plasma, whereas peptide hormones require carrier globulins",
            "Peptide hormones are synthesized directly from cholesterol, whereas steroid hormones translate from mRNA",'''
)

# Q49
text = text.replace(
    '''            "Hemoglobin has a significantly higher overall affinity for oxygen across all physiological pO2 values",
            "Hemoglobin exhibits negative cooperativity, meaning oxygen binding promotes rapid subunit disassembly",
            "Hemoglobin displays positive cooperativity, where O2 binding at one subunit increases affinity at other sites",
            "Myoglobin contains four cooperative heme groups, whereas hemoglobin binds O2 through a single porphyrin ring",''',
    '''            "Hemoglobin has a significantly higher overall affinity for oxygen across all physiological tissue pO2 values",
            "Hemoglobin exhibits negative cooperativity, meaning oxygen binding promotes rapid subunit disassembly in cells",
            "Hemoglobin displays positive cooperativity, where O2 binding at one subunit increases affinity elsewhere",
            "Myoglobin contains four cooperative heme groups, whereas hemoglobin binds O2 through a single porphyrin ring",'''
)

with open("/home/cgslinde/DrillRoom/DrillRoom/scratch/craft_bb90_p5_to_p8.py", "w") as f:
    f.write(text)

print("Applied fixes!")
