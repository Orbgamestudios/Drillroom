import os, sys

output_path = "/home/cgslinde/DrillRoom/DrillRoom/MCAT-CURRICULUM-AND-TOPIC-TRACKER.md"

# Define the covered set mappings from our audit of DrillRoom
# 131 items currently covered across Base Sets, Exam 1, and Exam 2

covered_map = {
    # CARS (30 covered)
    1: "cars_veblen / exam_cars90_p1", # Philosophy of Culture & Scientism (Veblen)
    2: "aamc_puritan_society / exam_cars90_p2 / exam_cars60_p6", # Religious Orthodoxy & Individual Conscience (Hawthorne)
    3: "aamc_understanding_thomas_h / exam_cars90_p3", # Victorian Literary Aesthetics & Fatalism (Hardy)
    4: "aamc_maternal_psychology / exam_cars90_p4", # Evolutionary Psychology & Maternal Attachment
    5: "aamc_huns_and_eurasian_hist / exam_cars90_p5", # Historiography & Nomadic Migrations (The Huns)
    6: "aamc_energy_and_sustainable / exam_cars90_p6", # Energy Geopolitics & Resource Curse in Nigeria
    7: "aamc_primordial_and_complex / exam_cars90_p7", # Philosophical Psychology & Primordial vs Complex Jealousy
    8: "aamc_what_is_life / exam_cars90_p8", # Philosophy of Science & Definition of Biological Life
    9: "cars_addams / exam_cars90_p9", # Social Ethics & Democratic Standard (Jane Addams)
    10: "cars_1 / exam_cars60_p1", # Philosophy of History & Uses of the Past (Nietzsche)
    11: "cars_2 / exam_cars60_p2", # Aesthetics & The Problem of the Copy (Walter Benjamin)
    12: "cars_3 / exam_cars60_p3", # Social Science & Methodological Measurement of Poverty
    13: "cars_boas / exam_cars60_p4", # Cultural Anthropology & Aptitude from Achievement (Franz Boas)
    14: "cars_pater / exam_cars60_p5", # Aesthetic Criticism & Prose vs Poetry (Walter Pater)
    15: "aamc_the_ultimatum_game", # Behavioral Economics & Fairness in the Ultimatum Game
    16: "aamc_tools_for_thought", # Cognitive Science & Extended Cognition (Andy Clark)
    17: "aamc_deconstructionism_and_", # Post-Structuralist Literary Theory (Derrida)
    18: "aamc_does_free_will_exist", # Metaphysics & Determinism vs Free Will
    19: "aamc_designing_courthouses", # Architecture & Civic Ideology of Courtroom Design
    20: "aamc_censorship_an_unnecess", # Political Philosophy & Free Expression vs Censorship
    21: "aamc_antenatal_depression_a", # Medical Anthropology & Psychiatric Stigma in South Asia
    22: "exam_cars90_2_p1 / exam_cars60_2_p1", # Bioethics: Triage Allocation & Principle of Double Effect
    23: "exam_cars90_2_p2 / exam_cars60_2_p2", # Philosophy of Language: Wittgenstein's Language Games
    24: "exam_cars90_2_p3 / exam_cars60_2_p3", # Moral Philosophy: Aristotelian Virtue Ethics vs Utilitarianism
    25: "exam_cars90_2_p4 / exam_cars60_2_p4", # Aesthetics: Edmund Burke & Immanuel Kant on the Sublime
    26: "exam_cars90_2_p5 / exam_cars60_2_p5", # Legal Philosophy: Holmes's Legal Realism vs Formalism
    27: "exam_cars90_2_p6 / exam_cars60_2_p6", # Political Economy: Shoshana Zuboff's Surveillance Capitalism
    28: "exam_cars90_2_p7", # Economic Anthropology: Marcel Mauss & The Gift Economy
    29: "exam_cars90_2_p8", # Sociology of Education: Pierre Bourdieu's Cultural Reproduction
    30: "exam_cars90_2_p9", # Urban Sociology: Le Corbusier vs Jane Jacobs Sidewalk Ballet

    # C/P (33 covered)
    201: "cp_acid / exam_cp90_p1 / exam_cp60_p1", # Carbonic acid / bicarbonate buffer kinetics
    202: "cp_kin / exam_cp60_p2", # Reaction kinetics, Arrhenius activation energy, rate laws
    203: "cp_phys / exam_cp60_p3", # Fluid dynamics, Poiseuille flow, arterial stenosis
    204: "exam_cp90_p2", # Microvascular hemodynamics & Hagen-Poiseuille resistance
    205: "exam_cp90_p3", # SNAr mechanism, Meisenheimer intermediate, fluorine leaving group
    206: "exam_cp90_p4 / exam_cp60_p4", # Electrochemistry, cyclic voltammetry, Faradaic biosensors
    207: "exam_cp90_p5", # Regioselective enolate alkylation, kinetic vs thermodynamic enolates
    208: "exam_cp90_p6", # Axonal RC circuits, cable theory, membrane capacitance & time constant
    209: "exam_cp90_p7 / exam_cp60_p5", # Square-planar platinum coordination, cisplatin aquation kinetics
    210: "exam_cp90_discretes", # Thin lens equation, focal length, refractive power (diopters)
    211: "exam_cp90_discretes", # Faraday's law of electrolysis & electrodeposition stoichiometry
    212: "exam_cp90_discretes", # Rotational torque, lever-arm equilibrium in biomechanics
    213: "exam_cp90_discretes", # Van der Waals equation of state & real gas deviations
    214: "exam_cp90_discretes", # Snell's law, critical angle, total internal reflection in fiber optics
    215: "exam_cp90_discretes", # Kirchhoff's laws, parallel vs series capacitors
    216: "exam_cp90_discretes", # First-order radioactive decay kinetics & PET radiotracers
    217: "exam_cp90_2_p1 / exam_cp60_2_p1", # Polyprotic amino acid titrations (Histidine buffering & charge)
    218: "exam_cp90_2_p2 / exam_cp60_2_p2", # Galvanic concentration cells & Nernst transcellular potential
    219: "exam_cp90_2_p3 / exam_cp60_2_p3", # Calcium oxalate Ksp, common-ion effect & nephrolithiasis
    220: "exam_cp90_2_p4 / exam_cp60_2_p4", # Venturi effect, Bernoulli dynamic pressure & oxygen masks
    221: "exam_cp90_2_p5 / exam_cp60_2_p5", # Ultrasound acoustic impedance (Z = rho*v) & Doppler echocardiography
    222: "exam_cp90_2_p6", # Carbonyl aldol addition & glycolytic aldolase retro-aldol mechanism
    223: "exam_cp90_2_p7", # Strecker & Gabriel de novo amino acid syntheses & racemic racemates
    224: "exam_cp90_2_disc / exam_cp60_2_disc", # Calorimetry & enthalpy of solution (lattice vs hydration enthalpy)
    225: "exam_cp90_2_disc / exam_cp60_2_disc", # Colligative properties: Osmotic pressure (Pi = iMRT)
    226: "exam_cp90_2_disc / exam_cp60_2_disc", # Capacitor physics: Dielectric slab insertion (C = kappa*C0)
    227: "exam_cp90_2_disc", # UV-Vis spectrophotometry & Beer-Lambert law deviations at high conc
    228: "exam_cp90_2_disc", # Photoelectric effect, work function & maximum kinetic energy
    229: "exam_cp90_2_disc", # Carboxylic acid derivative reactivity hierarchy (acyl chloride > amide)
    230: "exam_cp90_2_disc", # Acetal & ketal protecting groups: Acid-catalyzed hydrolysis
    231: "exam_cp90_2_disc", # SN1 vs SN2 solvent effects (DMSO polar aprotic) & Walden inversion
    232: "exam_cp90_2_disc", # E1 vs E2 Hofmann vs Zaitsev elimination with bulky base (t-BuOK)
    233: "exam_cp90_2_disc", # Mass spectrometry isotopic signatures (Bromine 1:1 M/M+2 doublet)

    # B/B (35 covered)
    471: "bb_renal / exam_bb60_p1", # Countercurrent multiplication, loop of Henle, medullary gradient
    472: "bb_cv / exam_bb60_p2", # Cardiovascular hemodynamics, systemic vascular resistance, compliance
    473: "bb_resp / exam_bb60_p3", # Respiratory gas exchange, Bohr/Haldane effects, 2,3-BPG
    474: "bb_enz / exam_bb60_p4", # Michaelis-Menten kinetics, competitive vs non-competitive inhibition
    475: "bb_endo / exam_bb60_p5", # Hypothalamic-pituitary axes (HPA, HPT), feedback loops
    476: "bb_neuro", # Neuronal action potentials, voltage-gated ion channels, summation
    477: "exam_bb90_p1", # CRISPR-Cas9 endonuclease targeting, PAM motif, HDR vs NHEJ repair
    478: "exam_bb90_p2", # Pyruvate Dehydrogenase Complex (PDC) regulation, kinase/phosphatase
    479: "exam_bb90_p3", # SGLT2 secondary active transport, Lineweaver-Burk kinetics
    480: "exam_bb90_p4", # GPCR signaling, G-protein cascades, beta-arrestin biased agonism
    481: "exam_bb90_p5", # Cardiac action potential phases, hERG potassium channels, Long QT
    482: "exam_bb90_p6", # Mitochondrial ETC complexes (I-IV), ATP synthase, uncouplers (DNP)
    483: "exam_bb90_p7", # V(D)J somatic recombination, RAG1/2, immunoglobulin class switching
    484: "exam_bb90_discretes", # Isoelectric point (pI) calculations for polyprotic amino acids
    485: "exam_bb90_discretes", # Reducing vs non-reducing SDS-PAGE disulfide protein analysis
    486: "exam_bb90_discretes", # Hill coefficient (nH > 1) & sigmoidal allosteric cooperativity
    487: "exam_bb90_discretes", # Translation initiation (Shine-Dalgarno vs 5' cap Kozak scanning)
    488: "exam_bb90_discretes", # Hardy-Weinberg equilibrium population genetics (p^2 + 2pq + q^2 = 1)
    489: "exam_bb90_discretes", # Embryonic germ layer derivatives (ectoderm, mesoderm, endoderm)
    490: "exam_bb90_discretes", # Renal clearance equations, inulin GFR & PAH renal plasma flow
    491: "exam_bb90_2_p1 / exam_bb60_2_p1", # Pentose Phosphate Pathway (G6PDH, NADPH, glutathione & hemolysis)
    492: "exam_bb90_2_p2 / exam_bb60_2_p2", # Glycogen metabolism cascades (PKA, phosphorylase kinase, McArdle/Von Gierke)
    493: "exam_bb90_2_p3 / exam_bb60_2_p3", # Fatty acid beta-oxidation & carnitine shuttle (CPT-1, MCAD deficiency)
    494: "exam_bb90_2_p4 / exam_bb60_2_p4", # Nucleotide Excision Repair (NER / UV dimers / Xeroderma Pigmentosum)
    495: "exam_bb90_2_p5 / exam_bb60_2_p5", # Cardiac PV loops, stroke volume, Wiggers diagram, S1/S2 heart sounds
    496: "exam_bb90_2_p6", # Renal tubular acid-base transport (Type A vs B intercalated cells, RTA)
    497: "exam_bb90_2_p7", # Major Histocompatibility Complex (MHC-I vs MHC-II antigen presentation)
    498: "exam_bb90_2_disc / exam_bb60_2_disc", # Gluconeogenesis bypass enzymes & F-2,6-BP reciprocal regulation
    499: "exam_bb90_2_disc / exam_bb60_2_disc", # Monod-Wyman-Changeux (MWC) concerted allosteric cooperativity
    500: "exam_bb90_2_disc / exam_bb60_2_disc", # Histone acetyltransferases (HATs), HDACs & euchromatin remodeling
    501: "exam_bb90_2_disc", # Lac operon dual regulation: CAP-cAMP activation & repressor derepression
    502: "exam_bb90_2_disc", # RNA interference: miRNA translational repression vs siRNA endonucleolytic slicing
    503: "exam_bb90_2_disc", # Isoelectric focusing (IEF) gel migration to net zero charge at pI
    504: "exam_bb90_2_disc", # Microvascular Starling forces: Capillary hydrostatic pressure in edema
    505: "exam_bb90_2_disc", # Myosin cross-bridge cycle: ATP binding causing detachment from actin

    # P/S (33 covered)
    741: "ps_social / exam_ps60_p1", # Bystander effect, diffusion of responsibility, social loafing
    742: "ps_learn / exam_ps60_p2", # Classical & operant conditioning schedules, extinction
    743: "ps_disorders / exam_ps60_p3", # DSM-5 mood vs anxiety disorders, monoamine hypothesis
    744: "exam_ps90_p1", # Signal Detection Theory (d', criterion c), ROC curves in imaging
    745: "exam_ps90_p2 / exam_ps60_p4", # Stereotype threat, cognitive load, central executive working memory
    746: "exam_ps90_p3 / exam_ps60_p5", # Fundamental Cause Theory, residential segregation, weathering
    747: "exam_ps90_p4", # Elaboration Likelihood Model (central vs peripheral), cognitive dissonance
    748: "exam_ps90_p5", # Operant conditioning schedules (VR, FR, VI, FI), incentive-sensitization
    749: "exam_ps90_p6", # Dopamine hypothesis of schizophrenia, mesolimbic vs mesocortical
    750: "exam_ps90_p7", # Dramaturgical perspective (front stage vs back stage), impression management
    751: "exam_ps90_discretes", # Weber's law difference threshold (delta I / I = k)
    752: "exam_ps90_discretes", # Theories of emotion (Schachter-Singer two-factor cognitive appraisal)
    753: "exam_ps90_discretes", # Gestalt laws of visual organization (closure, proximity, similarity)
    754: "exam_ps90_discretes", # Sensory adaptation vs cognitive habituation
    755: "exam_ps90_discretes", # Erikson's psychosocial developmental stages (Identity vs Role Confusion)
    756: "exam_ps90_discretes", # Kohlberg's stages of moral reasoning (pre-conventional, conventional)
    757: "exam_ps90_discretes", # Fundamental attribution error vs actor-observer bias
    758: "exam_ps90_discretes", # George Herbert Mead's 'I' spontaneous vs 'Me' socialized persona
    759: "exam_ps90_discretes", # Institutional vs individual discrimination in clinical access
    760: "exam_ps90_2_p1 / exam_ps60_2_p1", # Visual phototransduction cascade (rhodopsin, transducin, PDE, cGMP, rods)
    761: "exam_ps90_2_p2 / exam_ps60_2_p2", # Auditory hair cell mechano-transduction (stereocilia tip links, endolymph K+)
    762: "exam_ps90_2_p3 / exam_ps60_2_p3", # Sleep architecture (N1-N3, sleep spindles, SCN melatonin, REM motor atonia)
    763: "exam_ps90_2_p4 / exam_ps60_2_p4", # Theories of language acquisition (Chomsky LAD vs Skinner Operant vs Vygotsky)
    764: "exam_ps90_2_p5 / exam_ps60_2_p5", # Pierre Bourdieu's forms of capital (Economic, Cultural, Social, Habitus)
    765: "exam_ps90_2_p6", # Talcott Parsons' sick role institutional rights & obligations, medicalization
    766: "exam_ps90_2_p7", # Social influence & conformity (Asch, Groupthink, Devil's advocate, Group polarization)
    767: "exam_ps90_2_disc / exam_ps60_2_disc", # Memory forgetting: Retroactive vs proactive interference
    768: "exam_ps90_2_disc / exam_ps60_2_disc", # Dual-process cognitive models: Representativeness vs availability heuristic
    769: "exam_ps90_2_disc / exam_ps60_2_disc", # Neurobiology of chronic stress: HPA axis, cortisol, hippocampal dendritic atrophy
    770: "exam_ps90_2_disc", # Neurology of emotion: Bilateral amygdala lesions & Klüver-Bucy syndrome
    771: "exam_ps90_2_disc", # Split-brain lateralization: Corpus callosotomy & verbal vs spatial processing
    772: "exam_ps90_2_disc", # Major sociological paradigms: Structural Functionalism vs Conflict vs Interactionism
    773: "exam_ps90_2_disc", # Social constructionism: Institutional facts vs brute physical facts
}

print(f"Total covered topics mapped: {len(covered_map)}")
