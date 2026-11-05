import json, os

output_path = "/home/cgslinde/DrillRoom/DrillRoom/MCAT-CURRICULUM-AND-TOPIC-TRACKER.md"

content = """# MCAT Master Curriculum & Topic Coverage Tracker

A comprehensive audit of all created content in **DrillRoom**, mapped against the official AAMC Foundational Concepts and past exam topic blueprints.

> **Purpose:** Use this document to track content coverage across CARS, C/P, B/B, and P/S. Before generating new 90-minute or 60-minute sections, consult this tracker to select unchecked `[ ]` topics. Once implemented, mark them as checked `[x]` and cite the file and set ID to ensure zero duplication and maximum content breadth.

---

## 📊 Content Coverage Dashboard

| Section | Total Blueprint Topics | Created & Integrated `[x]` | Remaining Uncovered `[ ]` | Coverage % |
| :--- | :---: | :---: | :---: | :---: |
| **CARS** (Critical Analysis & Reasoning) | 48 | 30 | 18 | **62.5%** |
| **C/P** (Chemical & Physical Foundations) | 52 | 33 | 19 | **63.5%** |
| **B/B** (Biological & Biochemical Foundations) | 56 | 35 | 21 | **62.5%** |
| **P/S** (Psychological, Social & Biological) | 54 | 33 | 21 | **61.1%** |
| **TOTALS** | **210** | **131** | **79** | **62.4%** |

---

## 🔍 Audit of Currently Created Content in DrillRoom

### 1. CARS Existing Passages (30 Sets / Passages)
#### Exam 1 Suite & Base Drill Sets
* `cars_veblen` / `exam_cars90_p1`: **Thorstein Veblen — The Place of Science in Modern Civilisation** (Philosophy of Culture & Scientism)
* `aamc_puritan_society` / `exam_cars90_p2` / `exam_cars60_p6`: **Nathaniel Hawthorne — Puritan Society & Religious Individualism** (American History & Religious Orthodoxy)
* `aamc_understanding_thomas_h` / `exam_cars90_p3`: **Literary Criticism — Understanding Thomas Hardy** (Victorian Literature & Aesthetic Fatalism)
* `aamc_maternal_psychology` / `exam_cars90_p4`: **Evolutionary Psychology — Maternal Emotional Response & Attachment** (Psychology & Behavioral Ecology)
* `aamc_huns_and_eurasian_hist` / `exam_cars90_p5`: **Historiography — The Huns and Eurasian Nomadic Migrations** (World History & Historiographical Evidence)
* `aamc_energy_and_sustainable` / `exam_cars90_p6`: **Political Economy — Energy and Sustainable Development in Nigeria** (Resource Curse & Energy Policy)
* `aamc_primordial_and_complex` / `exam_cars90_p7`: **Philosophical Psychology — Primordial and Complex Jealousy** (Philosophy of Mind & Emotion)
* `aamc_what_is_life` / `exam_cars90_p8`: **Philosophy of Science — The Definition of Biological Life** (Epistemology & Biosemiotics)
* `cars_addams` / `exam_cars90_p9`: **Jane Addams — Charity and the Democratic Standard** (Social Ethics & Progressive Reform)
* `cars_1` / `exam_cars60_p1`: **Philosophy of History — The Uses and Abuses of the Past** (Nietzschean Historiography)
* `cars_2` / `exam_cars60_p2`: **Aesthetics — The Problem of the Copy and Artistic Authenticity** (Visual Arts & Mechanical Reproduction)
* `cars_3` / `exam_cars60_p3`: **Social Science — The Methodological Measurement of Poverty** (Sociology & Welfare Economics)
* `cars_boas` / `exam_cars60_p4`: **Franz Boas — Inferring Aptitude from Cultural Achievement** (Cultural Anthropology & Anti-Racist Science)
* `cars_pater` / `exam_cars60_p5`: **Walter Pater — The Distinction Between Prose and Poetry** (Aesthetic Criticism & Literary Style)
* `aamc_the_ultimatum_game`: **Behavioral Economics — Fairness and the Ultimatum Game** (Game Theory & Rational Choice)
* `aamc_tools_for_thought`: **Cognitive Science — Tools for Thought and Extended Cognition** (Philosophy of Mind & Cybernetics)
* `aamc_deconstructionism_and_`: **Literary Theory — Derridean Deconstruction and Textual Ambiguity** (Post-Structuralism & Critical Theory)
* `aamc_does_free_will_exist`: **Metaphysics — Determinism and the Problem of Free Will** (Philosophy of Action)
* `aamc_designing_courthouses`: **Architecture & Civic Space — Ideology of Courtroom Design** (Architecture & Legal Theory)
* `aamc_censorship_an_unnecess`: **Political Philosophy — Free Expression and Censorship** (First Amendment & Democratic Norms)
* `aamc_antenatal_depression_a`: **Medical Anthropology — Antenatal Depression and Social Stigma in South Asia** (Global Health & Cultural Psychiatry)

#### Exam 2 Suite
* `exam_cars90_2_p1` / `exam_cars60_2_p1`: **Bioethics & Crisis Standards of Care — Triage Allocation & Double Effect** (Ethics & Medical Humanities)
* `exam_cars90_2_p2` / `exam_cars60_2_p2`: **Ludwig Wittgenstein — Language Games & Private Language** (Philosophy of Language)
* `exam_cars90_2_p3` / `exam_cars60_2_p3`: **Aristotelian Virtue Ethics — Phronesis vs Rule-Based Morality** (Moral Philosophy)
* `exam_cars90_2_p4` / `exam_cars60_2_p4`: **Edmund Burke & Immanuel Kant — The Aesthetics of the Sublime** (Philosophical Aesthetics)
* `exam_cars90_2_p5` / `exam_cars60_2_p5`: **Oliver Wendell Holmes Jr. — The Common Law & Legal Realism** (Jurisprudence & Legal Philosophy)
* `exam_cars90_2_p6` / `exam_cars60_2_p6`: **Shoshana Zuboff — Surveillance Capitalism & Behavioral Modification** (Political Economy & Technology)
* `exam_cars90_2_p7`: **Marcel Mauss — The Gift Economy and Social Reciprocity** (Economic Anthropology)
* `exam_cars90_2_p8`: **Pierre Bourdieu — Cultural Reproduction in the University Academy** (Sociology of Education)
* `exam_cars90_2_p9`: **Le Corbusier vs Jane Jacobs — Radiant City Modernism vs Sidewalk Ballet** (Urbanism & Social Ecology)

---

### 2. C/P Existing Topics (33 Topics)
#### Exam 1 Suite & Base Drill Sets
* `cp_acid` / `exam_cp90_p1` / `exam_cp60_p1`: Carbonic acid / bicarbonate buffer kinetics, Henderson-Hasselbalch, and metabolic acidosis
* `cp_kin` / `exam_cp60_p2`: Reaction kinetics, Arrhenius activation energy, rate laws, and reaction coordinates
* `cp_phys` / `exam_cp60_p3`: Fluid mechanics, Poiseuille flow, Bernoulli principle, and arterial stenosis hemodynamics
* `exam_cp90_p2`: Capillary hemodynamics, Hagen-Poiseuille resistance, and pressure gradients
* `exam_cp90_p3`: Nucleophilic aromatic substitution ($S_NAr$) mechanism, Meisenheimer complex, leaving groups
* `exam_cp90_p4` / `exam_cp60_p4`: Electrochemistry, cyclic voltammetry, Faradaic current, and biosensors
* `exam_cp90_p5`: Regioselective enolate alkylation, kinetic vs thermodynamic enolates, LDA steric hindrance
* `exam_cp90_p6`: Axonal RC circuits, membrane capacitance, cable theory, time constant ($\tau = RC$)
* `exam_cp90_p7` / `exam_cp60_p5`: Square-planar platinum coordination chemistry, cisplatin aquation, ligand displacement
* `exam_cp90_discretes`: Thin lens equation, focal length, refractive power (diopters), and hyperopia/myopia correction
* `exam_cp90_discretes`: Faraday's law of electrolysis, electrical charge ($q = It$), and electrodeposition stoichiometry
* `exam_cp90_discretes`: Rotational torque, center of mass, and lever-arm equilibrium in human joints
* `exam_cp90_discretes`: Van der Waals equation of state and real gas non-ideal behavior
* `exam_cp90_discretes`: Snell's law, critical angle, and total internal reflection in fiber-optic endoscopes
* `exam_cp90_discretes`: Kirchhoff's circuit laws, parallel vs series capacitors, and equivalent capacitance
* `exam_cp90_discretes`: First-order radioactive decay kinetics, half-life, and PET radiotracer activity

#### Exam 2 Suite
* `exam_cp90_2_p1` / `exam_cp60_2_p1`: **Polyprotic Amino Acid Titrations** (Histidine buffering zones, equivalence points, charge transitions, active site pKa shifts)
* `exam_cp90_2_p2` / `exam_cp60_2_p2`: **Galvanic Concentration Cells & Transcellular Electrochemical Potentials** (Nernst equation, $E = E^\circ - (RT/zF)\ln Q$, electrogenic $\text{Na}^+/\text{K}^+$-ATPase)
* `exam_cp90_2_p3` / `exam_cp60_2_p3`: **Solubility Product Constant ($K_{sp}$) & Calcium Oxalate Nephrolithiasis** (Common-ion effect, selective precipitation, $Q_{sp}$ vs $K_{sp}$, urinary citrate chelation)
* `exam_cp90_2_p4` / `exam_cp60_2_p4`: **Fluid Mechanics, Bernoulli Principle & Venturi Flow Dynamics** (Bernoulli equation, Venturi throat dynamic vs static pressure drop, oxygen entrainment masks)
* `exam_cp90_2_p5` / `exam_cp60_2_p5`: **Ultrasound Physics, Acoustic Impedance & Doppler Echocardiography** (Acoustic impedance $Z = \rho v$, intensity reflection coefficient $R$, Doppler shift $\Delta f = 2 f_0 v \cos\theta / c$)
* `exam_cp90_2_p6`: **Carbonyl Chemistry, Directed Aldol & Glycolytic Retro-Aldol Cleavage** (Aldol addition/condensation, retro-aldol mechanism, Class I aldolase lysine Schiff base)
* `exam_cp90_2_p7`: **Strecker and Gabriel Amino Acid Syntheses & Stereochemical Outcomes** (Imine/aminonitrile intermediate, phthalimide alkylation, planar achiral intermediates yielding racemic mixtures)
* `exam_cp90_2_disc` / `exam_cp60_2_disc`: **Calorimetry & Enthalpy of Solution** (Lattice energy vs exothermic hydration enthalpy)
* `exam_cp90_2_disc` / `exam_cp60_2_disc`: **Colligative Properties & Osmotic Pressure** ($\Pi = iMRT$, van 't Hoff factor)
* `exam_cp90_2_disc` / `exam_cp60_2_disc`: **Capacitor Physics & Dielectric Insertion** ($C = \kappa C_0$, voltage and potential energy changes in isolated capacitors)
* `exam_cp90_2_disc`: **UV-Vis Spectrophotometry & Beer-Lambert Law Deviations** (Stray light and molecular aggregation at high concentration)
* `exam_cp90_2_disc`: **Photoelectric Effect & Metal Work Functions** ($KE_{max} = hf - \Phi$)
* `exam_cp90_2_disc`: **Carboxylic Acid Derivative Reactivity Hierarchy** (Acyl chloride > anhydride > ester > amide nucleophilic acyl substitution)
* `exam_cp90_2_disc`: **Acetal and Ketal Protecting Group Chemistry** (Acid-catalyzed hydrolysis of cyclic acetals)
* `exam_cp90_2_disc`: **$S_N1$ vs $S_N2$ Kinetic and Stereochemical Profiles** (DMSO polar aprotic solvent driving Walden inversion)
* `exam_cp90_2_disc`: **Elimination Mechanisms ($E1$ vs $E2$) & Regiochemistry** (Sterically hindered base $t$-BuOK favoring Hofmann over Zaitsev)
* `exam_cp90_2_disc`: **Mass Spectrometry Isotopic Signatures** (Bromine $^{79}\text{Br}/^{81}\text{Br}$ 1:1 molecular ion doublet)

---

### 3. B/B Existing Topics (35 Topics)
#### Exam 1 Suite & Base Drill Sets
* `bb_renal` / `exam_bb60_p1`: Countercurrent multiplication, loop of Henle, vasa recta, medullary osmotic gradient
* `bb_cv` / `exam_bb60_p2`: Cardiovascular hemodynamics, systemic vascular resistance, compliance, baroreceptors
* `bb_resp` / `exam_bb60_p3`: Respiratory mechanics, alveolar gas equation, Bohr/Haldane effects, 2,3-BPG
* `bb_enz` / `exam_bb60_p4`: Michaelis-Menten kinetics, competitive vs non-competitive vs uncompetitive inhibition
* `bb_endo` / `exam_bb60_p5`: Hypothalamic-pituitary axes (HPA, HPT), negative feedback, peptide vs steroid hormones
* `bb_neuro`: Action potential generation, voltage-gated ion channels, spatial/temporal summation
* `exam_bb90_p1`: CRISPR-Cas9 genome editing, sgRNA targeting, PAM motif, HDR vs NHEJ repair pathways
* `exam_bb90_p2`: Pyruvate Dehydrogenase Complex (PDC) regulation, PDH kinase/phosphatase, cofactors
* `exam_bb90_p3`: SGLT2 secondary active transport, Lineweaver-Burk kinetics, phlorizin competitive inhibition
* `exam_bb90_p4`: GPCR signaling, $G\alpha_s$/$G\alpha_q$ cascades, $\beta$-arrestin biased agonism, receptor desensitization
* `exam_bb90_p5`: Cardiac action potential phases (0 to 4), hERG potassium channels, Long QT syndrome
* `exam_bb90_p6`: Mitochondrial electron transport chain complexes (I–IV), ATP synthase, uncouplers (DNP)
* `exam_bb90_p7`: V(D)J somatic recombination, RAG1/2 endonucleases, immunoglobulin heavy-chain class switching
* `exam_bb90_discretes`: Isoelectric point (pI) calculation for basic/acidic polyprotic amino acids
* `exam_bb90_discretes`: Reducing vs non-reducing SDS-PAGE analysis of multimeric disulfide proteins
* `exam_bb90_discretes`: Hill coefficient ($n_H > 1$), sigmoidal binding kinetics, positive cooperativity
* `exam_bb90_discretes`: Prokaryotic (Shine-Dalgarno) vs eukaryotic (Kozak/5' cap) translation initiation
* `exam_bb90_discretes`: Hardy-Weinberg equilibrium population genetics ($p^2 + 2pq + q^2 = 1$)
* `exam_bb90_discretes`: Embryonic germ layer derivatives (ectoderm, mesoderm, endoderm)
* `exam_bb90_discretes`: Renal clearance equations, inulin GFR measurement, and PAH effective renal plasma flow

#### Exam 2 Suite
* `exam_bb90_2_p1` / `exam_bb60_2_p1`: **Pentose Phosphate Pathway (PPP) & Glutathione Redox Homeostasis** (G6PDH regulation, NADPH generation, glutathione reduction, oxidative hemolysis in G6PD deficiency)
* `exam_bb90_2_p2` / `exam_bb60_2_p2`: **Glycogen Metabolism, Phosphorylase Cascades & Inborn Errors** (Glycogen phosphorylase vs synthase, PKA cascade, McArdle Type V vs Von Gierke Type I)
* `exam_bb90_2_p3` / `exam_bb60_2_p3`: **Fatty Acid $\beta$-Oxidation, Carnitine Shuttle & Ketogenesis** (CPT-1 malonyl-CoA regulation, acyl-CoA dehydrogenase, FADH2/NADH, MCAD deficiency)
* `exam_bb90_2_p4` / `exam_bb60_2_p4`: **DNA Excision Repair, Nucleotide Excision Repair & Xeroderma Pigmentosum** (UV cyclobutane pyrimidine dimers, XPF/XPG dual endonucleases, complementation groups)
* `exam_bb90_2_p5` / `exam_bb60_2_p5`: **Cardiac Cycle Electromechanics, Pressure-Volume Loops & Wiggers Diagram** (Left ventricular PV loops, stroke volume, isovolumetric phases, S1/S2 heart sounds)
* `exam_bb90_2_p6`: **Renal Tubular Acid-Base Transport & Intercalated Cell Dynamics** (Type A intercalated cells secreting $H^+$ via $H^+$-ATPase and AE1; Type B pendrin $HCO_3^-$ secretion; Distal vs Proximal RTA)
* `exam_bb90_2_p7`: **Major Histocompatibility Complex (MHC) & Antigen Presentation Pathways** (Endogenous MHC-I presentation to CD8+ CTLs vs Exogenous MHC-II presentation to CD4+ TH cells, TAP, invariant chain/CLIP)
* `exam_bb90_2_disc` / `exam_bb60_2_disc`: **Gluconeogenesis Bypass Enzymes & Allosteric Modulators** (Fructose-2,6-bisphosphate reciprocal regulation of PFK-1 and FBPase-1)
* `exam_bb90_2_disc` / `exam_bb60_2_disc`: **Enzyme Allosteric Cooperativity Models** (Monod-Wyman-Changeux concerted T/R state model)
* `exam_bb90_2_disc` / `exam_bb60_2_disc`: **Chromatin Remodeling & Histone Epigenetics** (Histone acetyltransferases [HATs] neutralizing positive lysine charges to form euchromatin)
* `exam_bb90_2_disc`: **Prokaryotic Operon Regulation** (Lac operon dual control: CAP-cAMP activation and allolactose repressor derepression)
* `exam_bb90_2_disc`: **RNA Interference (RNAi) Mechanisms** (miRNA partial seed match translational repression vs siRNA full match endonucleolytic slicing)
* `exam_bb90_2_disc`: **Protein Separation via Isoelectric Focusing (IEF)** (Gel pH gradient migration to zero net charge at pI)
* `exam_bb90_2_disc`: **Microvascular Starling Forces in Disease** (Capillary hydrostatic pressure $P_c$ elevation driving peripheral edema)
* `exam_bb90_2_disc`: **Sliding Filament Cross-Bridge Cycle Dynamics** (ATP binding inducing myosin head detachment from actin)
* `exam_bb90_2_disc`: **Endocrine Calcium Homeostasis** (Parathyroid hormone PTH stimulation of osteoclasts, renal distal calcium reabsorption, and $1\alpha$-hydroxylase)
* `exam_bb90_2_disc`: **Hypothalamic-Pituitary-Gonadal (HPG) Axis Dynamics** (High-dose sustained estradiol positive feedback triggering the mid-cycle LH surge)

---

### 4. P/S Existing Topics (33 Topics)
#### Exam 1 Suite & Base Drill Sets
* `ps_social` / `exam_ps60_p1`: Bystander effect, diffusion of responsibility, attribution theory, social loafing
* `ps_learn` / `exam_ps60_p2`: Classical conditioning, operant schedules, extinction, spontaneous recovery
* `ps_disorders` / `exam_ps60_p3`: DSM-5 criteria, mood vs anxiety disorders, biological bases (monoamine hypothesis)
* `exam_ps90_p1`: Signal Detection Theory ($d'$, criterion $c$), receiver operating characteristics (ROC)
* `exam_ps90_p2` / `exam_ps60_p4`: Stereotype threat, cognitive load, central executive working memory depletion
* `exam_ps90_p3` / `exam_ps60_p5`: Fundamental Cause Theory, residential segregation, allostatic load, weathering
* `exam_ps90_p4`: Elaboration Likelihood Model (central vs peripheral), cognitive dissonance resolution
* `exam_ps90_p5`: Operant conditioning schedules (VR, FR, VI, FI), incentive-sensitization theory of addiction
* `exam_ps90_p6`: Dopamine hypothesis of schizophrenia, mesolimbic vs mesocortical vs nigrostriatal pathways
* `exam_ps90_p7`: Dramaturgical perspective (front stage vs back stage), impression management, role conflict
* `exam_ps90_discretes`: Weber's law difference threshold ($\Delta I / I = k$) calculations
* `exam_ps90_discretes`: Theories of emotion (Schachter-Singer two-factor cognitive appraisal vs James-Lange)
* `exam_ps90_discretes`: Gestalt laws of perceptual grouping (closure, proximity, similarity, continuity)
* `exam_ps90_discretes`: Sensory adaptation vs cognitive habituation
* `exam_ps90_discretes`: Erikson's psychosocial developmental stages (Identity vs Role Confusion, Generativity)
* `exam_ps90_discretes`: Kohlberg's stages of moral reasoning (pre-conventional, conventional, post-conventional)
* `exam_ps90_discretes`: Fundamental attribution error vs actor-observer bias
* `exam_ps90_discretes`: George Herbert Mead's sociological theory of self ('I' spontaneous vs 'Me' socialized)
* `exam_ps90_discretes`: Institutional vs individual discrimination in clinical settings

#### Exam 2 Suite
* `exam_ps90_2_p1` / `exam_ps60_2_p1`: **Visual Phototransduction Cascade & Retinal Circuitry** (Rhodopsin 11-cis to all-trans retinal isomerization, transducin, PDE6, cGMP drop, rod hyperpolarization, ON-center bipolar disinhibition)
* `exam_ps90_2_p2` / `exam_ps60_2_p2`: **Auditory Hair Cell Mechano-Transduction & Tonotopic Mapping** (Stereocilia deflection, protocadherin-15 tip links, endolymph high $K^+$ influx, basilar membrane frequency mapping)
* `exam_ps90_2_p3` / `exam_ps60_2_p3`: **Sleep Architecture, Circadian Oscillations & Memory Consolidation** (Polysomnography N1-N3/REM, sleep spindles, SCN melatonin regulation, N3 declarative vs REM procedural memory)
* `exam_ps90_2_p4` / `exam_ps60_2_p4`: **Theories of Language Acquisition & Neurocognitive Processing** (Chomsky's Nativist LAD & critical period vs Skinner's Operant conditioning vs Vygotsky's Interactionism; Broca's aphasia)
* `exam_ps90_2_p5` / `exam_ps60_2_p5`: **Bourdieu's Forms of Capital, Habitus & Healthcare Access Disparities** (Economic capital, Cultural capital [embodied, objectified, institutionalized], Social capital, Habitus)
* `exam_ps90_2_p6`: **Medicalization, Demedicalization & Talcott Parsons' Sick Role** (Parsons' sick role institutional rights & obligations, medicalization of deviance, DSM demedicalization, contested illnesses)
* `exam_ps90_2_p7`: **Social Influence, Conformity Paradigms & Group Decision Dynamics** (Asch line judgment [normative vs informational influence], Groupthink symptoms & Devil's advocate, Group polarization)
* `exam_ps90_2_disc` / `exam_ps60_2_disc`: **Memory Forgetting & Interference Models** (Retroactive vs proactive interference)
* `exam_ps90_2_disc` / `exam_ps60_2_disc`: **Dual-Process Cognitive Models & Heuristics** (Representativeness heuristic vs availability heuristic vs anchoring)
* `exam_ps90_2_disc` / `exam_ps60_2_disc`: **Neurobiology of Chronic Stress & Allostatic Load** (HPA axis, cortisol neurotoxicity, hippocampal dendritic atrophy)
* `exam_ps90_2_disc`: **Neurology of Emotion & Limbic Lesions** (Bilateral amygdala ablation and Klüver-Bucy syndrome)
* `exam_ps90_2_disc`: **Consciousness & Split-Brain Lateralization** (Corpus callosotomy: right hemisphere left-hand motor execution vs left hemisphere verbal speech)
* `exam_ps90_2_disc`: **Major Sociological Paradigms Comparison** (Structural Functionalism manifest/latent functions vs Conflict Theory vs Symbolic Interactionism)
* `exam_ps90_2_disc`: **Social Constructionism Principles** (Institutional facts vs brute physical facts in currency and disease classifications)
* `exam_ps90_2_disc`: **Intersectionality Theory in Health Inequity** (Compounding, non-additive interaction of race, gender, and socioeconomic class)
* `exam_ps90_2_disc`: **Sociology of Deviance & Labeling Theory** (Edwin Lemert's Primary vs Secondary deviance internalization)
* `exam_ps90_2_disc`: **Demographic Transition Model (DTM)** (Stage 2 declining death rates with high birth rates driving rapid population expansion)

---

## 🧭 Master Extrapolated Topic Checklist for Future Sections

Use the checklists below when designing future 90-minute and 60-minute sections. Unchecked `[ ]` items represent high-yield topics frequently tested on recent AAMC administrations that have not yet been developed into dedicated passage sets.

---

### SECTION 1: Critical Analysis & Reasoning Skills (CARS)

#### A. Humanities & Ethics
- [x] Philosophy of Culture & Scientism *(Veblen)* — `cars_veblen`
- [x] Religious Orthodoxy & Individual Conscience *(Hawthorne)* — `aamc_puritan_society`
- [x] Victorian Literary Aesthetics & Fatalism *(Thomas Hardy)* — `aamc_understanding_thomas_h`
- [x] Social Ethics & Democratic Philanthropy *(Jane Addams)* — `cars_addams`
- [x] Uses & Abuses of History *(Nietzsche)* — `cars_1`
- [x] Artistic Reproduction & Aesthetic Authenticity *(Benjamin/The Copy)* — `cars_2`
- [x] Poetic Form vs Prose Distinction *(Walter Pater)* — `cars_pater`
- [x] Post-Structuralist Literary Theory *(Derridean Deconstruction)* — `aamc_deconstructionism_and_`
- [x] Metaphysics of Free Will & Moral Responsibility — `aamc_does_free_will_exist`
- [x] Political Philosophy of Censorship & Free Expression — `aamc_censorship_an_unnecess`
- [x] **Bioethics:** Allocation of scarce medical resources and the principle of double effect — `exam_cars90_2_p1`
- [x] **Philosophy of Language:** Wittgenstein's language games and private language argument — `exam_cars90_2_p2`
- [x] **Moral Philosophy:** Aristotelian virtue ethics vs modern rule-based utilitarianism — `exam_cars90_2_p3`
- [x] **Aesthetics & The Sublime:** Edmund Burke and Immanuel Kant on terror and the sublime — `exam_cars90_2_p4`
- [x] **Legal Philosophy:** Legal Realism vs Formalism (Oliver Wendell Holmes Jr. on the life of the law) — `exam_cars90_2_p5`
- [ ] **Historiography of Science:** Thomas Kuhn's paradigm shifts and incommensurability
- [ ] **Architectural Hermeneutics:** Civic monuments and the memorialization of contentious historical trauma
- [ ] **Philosophy of Technology:** Martin Heidegger's "The Question Concerning Technology" and enframing
- [ ] **Epistemology:** The Gettier problem and the inadequacy of justified true belief

#### B. Social Sciences & Cultural Studies
- [x] Evolutionary Behavioral Ecology *(Maternal Attachment)* — `aamc_maternal_psychology`
- [x] Eurasian Nomadic Migration Historiography *(The Huns)* — `aamc_huns_and_eurasian_hist`
- [x] Energy Geopolitics & Resource Curse in Nigeria — `aamc_energy_and_sustainable`
- [x] Philosophical Psychology of Jealousy — `aamc_primordial_and_complex`
- [x] Epistemology of Life & Biosemiotics — `aamc_what_is_life`
- [x] Methodological Measurement of Poverty — `cars_3`
- [x] Anti-Racist Cultural Anthropology *(Franz Boas)* — `cars_boas`
- [x] Experimental Game Theory & Ultimatum Game — `aamc_the_ultimatum_game`
- [x] Extended Cognition & Cybernetics *(Andy Clark)* — `aamc_tools_for_thought`
- [x] Architecture of Civic Spaces & Ideology of Courtrooms — `aamc_designing_courthouses`
- [x] Medical Anthropology & South Asian Psychiatric Stigma — `aamc_antenatal_depression_a`
- [x] **Political Economy of Technology:** Shoshana Zuboff's "Surveillance Capitalism" and behavioral futures — `exam_cars90_2_p6`
- [x] **Economic Anthropology:** Marcel Mauss and the gift economy vs market commodification — `exam_cars90_2_p7`
- [x] **Sociology of Education:** Pierre Bourdieu's cultural reproduction in elite academic institutions — `exam_cars90_2_p8`
- [x] **Urban Sociology:** Le Corbusier's high-modernist urbanism vs Jane Jacobs's street-level sidewalk social fabric — `exam_cars90_2_p9`
- [ ] **Sociology of Knowledge:** Michel Foucault's panopticism and disciplinary power in clinical asylums
- [ ] **Critical Race Theory:** W.E.B. Du Bois's double consciousness and the color line
- [ ] **Post-Colonial Theory:** Edward Said's Orientalism and colonialist textual representation
- [ ] **Linguistic Anthropology:** The Sapir-Whorf hypothesis and endangered language revitalization
- [ ] **Media Ecology:** Marshall McLuhan's "the medium is the message" in digital social networks
- [ ] **Archaeological Epistemology:** Interpreting prehistoric symbolic culture from non-literate material remains

---

### SECTION 2: Chemical & Physical Foundations (C/P)

#### A. General Chemistry & Physics
- [x] Carbonic acid / bicarbonate physiologic buffer kinetics — `cp_acid` / `exam_cp90_p1`
- [x] Reaction kinetics, Arrhenius equation, and catalysis — `cp_kin`
- [x] Fluid dynamics (Bernoulli/Poiseuille) and arterial stenosis — `cp_phys` / `exam_cp90_p2`
- [x] Electrochemistry, cyclic voltammetry, and Faradaic biosensors — `exam_cp90_p4` / `exam_cp60_p4`
- [x] Axonal RC circuits, cable theory, and membrane capacitance — `exam_cp90_p6`
- [x] Square-planar coordination chemistry and cisplatin aquation — `exam_cp90_p7` / `exam_cp60_p5`
- [x] Thin lens equation, corrective lenses, and diopters — `exam_cp90_discretes`
- [x] Faraday's law of electrolysis and electrochemical charge — `exam_cp90_discretes`
- [x] Torque and rotational equilibrium in human joints — `exam_cp90_discretes`
- [x] Van der Waals equation and real gas deviations — `exam_cp90_discretes`
- [x] Snell's law and total internal reflection in fiber optics — `exam_cp90_discretes`
- [x] Kirchhoff's circuit laws and parallel capacitors — `exam_cp90_discretes`
- [x] Radioactive decay kinetics and medical PET isotopes — `exam_cp90_discretes`
- [x] **Polyprotic Amino Acid Titrations:** Buffering regions, equivalence points, and charge transitions — `exam_cp90_2_p1` / `exam_cp60_2_p1`
- [x] **Galvanic Concentration Cells:** Nernst equation application to transcellular resting membrane potential — `exam_cp90_2_p2` / `exam_cp60_2_p2`
- [x] **Solubility Product Constant ($K_{sp}$):** Common-ion effect and selective precipitation in kidney stone pathogenesis — `exam_cp90_2_p3` / `exam_cp60_2_p3`
- [x] **Venturi Effect & Respiratory Devices:** Dynamic pressure drop in oxygen masks and atomizers — `exam_cp90_2_p4` / `exam_cp60_2_p4`
- [x] **Ultrasound Attenuation & Acoustic Impedance:** Reflection at tissue boundaries ($Z = \rho v$) and Doppler shift — `exam_cp90_2_p5` / `exam_cp60_2_p5`
- [x] **Calorimetry & Enthalpy of Solution:** Constant-pressure calorimetry and lattice energy vs hydration enthalpy — `exam_cp90_2_disc` / `exam_cp60_2_disc`
- [x] **Colligative Properties:** Osmotic pressure ($\Pi = iMRT$), van 't Hoff factor — `exam_cp90_2_disc` / `exam_cp60_2_disc`
- [x] **Capacitance & Dielectrics:** Biological membranes with varying lipid composition and dielectric breakdown — `exam_cp90_2_disc` / `exam_cp60_2_disc`
- [x] **Spectrophotometry & Beer-Lambert Law:** Molar absorptivity, path length, and deviation at high concentrations — `exam_cp90_2_disc`
- [x] **Photoelectric Effect & Work Functions:** Work function, threshold frequency, and maximum kinetic energy — `exam_cp90_2_disc`
- [ ] **Gas-Phase Phase Diagrams:** Supercritical fluids, triple point, and Clausius-Clapeyron vaporization
- [ ] **Surface Tension & Capillary Action:** Young-Laplace equation in pulmonary surfactant physiology
- [ ] **Magnetic Fields & Mass Spectrometry:** Lorentz force ($F = qvB$), velocity selectors, and deflection radius
- [ ] **Nuclear Magnetic Resonance (NMR) Physics:** Larmor frequency, spin-lattice ($T_1$) and spin-spin ($T_2$) relaxation in MRI

#### B. Organic Chemistry
- [x] $S_NAr$ mechanism, Meisenheimer complex, and fluorine leaving group — `exam_cp90_p3`
- [x] Thermodynamic vs kinetic enolates and regioselective alkylation — `exam_cp90_p5`
- [x] FTIR and ¹H-NMR spectroscopic identification of drug intermediates — `exam_cp90_p3`
- [x] **Carbonyl Aldol Condensation:** Directed aldol, cross-aldol, and retro-aldol in glycolysis (aldolase mechanism) — `exam_cp90_2_p6`
- [x] **Carboxylic Acid Derivative Reactivity:** Acyl chloride > anhydride > ester > amide nucleophilic acyl substitution — `exam_cp90_2_disc`
- [x] **Strecker & Gabriel Syntheses:** De novo amino acid synthesis and stereocenter generation — `exam_cp90_2_p7`
- [x] **Acetal & Ketal Protection:** Protecting group strategies in carbohydrate synthesis and acid-catalyzed hydrolysis — `exam_cp90_2_disc`
- [x] **$S_N1$ vs $S_N2$ Kinetics:** Stereochemical inversion vs racemization, carbocation stability, and solvent effects — `exam_cp90_2_disc`
- [x] **Elimination Mechanisms ($E1$ vs $E2$):** Zaitsev vs Hofmann product distributions in sterically hindered alcohol dehydration — `exam_cp90_2_disc`
- [x] **Mass Spectrometry Fragmentation:** Base peak, molecular ion peak ($M^+$), and isotopic clusters — `exam_cp90_2_disc`
- [ ] **¹³C-NMR & DEPT Spectroscopy:** Identifying quaternary vs methyl carbons in terpene natural products
- [ ] **Liquid-Liquid Acid/Base Extraction:** Flowchart separating amine, carboxylic acid, phenol, and neutral hydrocarbon
- [ ] **Enantiomeric Resolution:** Chiral derivatization into diastereomeric tartrate salts and fractional crystallization
- [ ] **Fischer Esterification & Saponification:** Acid-catalyzed ester synthesis vs base-catalyzed triglyceride cleavage

---

### SECTION 3: Biological & Biochemical Foundations (B/B)

#### A. Biochemistry & Molecular Biology
- [x] CRISPR-Cas9 endonuclease targeting and HDR vs NHEJ repair — `exam_bb90_p1`
- [x] Pyruvate Dehydrogenase Complex (PDC) regulation and cofactors — `exam_bb90_p2`
- [x] SGLT2 secondary active transport kinetics and Lineweaver-Burk — `exam_bb90_p3`
- [x] GPCR and β-arrestin biased signaling pathways — `exam_bb90_p4`
- [x] Mitochondrial ETC complexes, chemiosmosis, and uncouplers — `exam_bb90_p6`
- [x] V(D)J recombination, RAG1/2, and immunoglobulin class switching — `exam_bb90_p7`
- [x] Polyprotic amino acid pI calculations — `exam_bb90_discretes`
- [x] Reducing vs non-reducing SDS-PAGE protein analysis — `exam_bb90_discretes`
- [x] Hill coefficient and sigmoidal allosteric kinetics — `exam_bb90_discretes`
- [x] Translation initiation mechanisms (prokaryotic vs eukaryotic) — `exam_bb90_discretes`
- [x] **Pentose Phosphate Pathway (PPP):** G6PDH regulation, NADPH generation, and glutathione reduction in RBC hemolytic anemia — `exam_bb90_2_p1` / `exam_bb60_2_p1`
- [x] **Glycogen Metabolism:** Phosphorylase kinase cascade, glycogen phosphorylase vs synthase, and Von Gierke's/McArdle disease — `exam_bb90_2_p2` / `exam_bb60_2_p2`
- [x] **Fatty Acid β-Oxidation & Ketogenesis:** Carnitine shuttle, CPT-1, MCAD deficiency, and ketoacidosis — `exam_bb90_2_p3` / `exam_bb60_2_p3`
- [x] **DNA Mismatch & Excision Repair:** Nucleotide excision repair (NER / UV thymine dimers / xeroderma pigmentosum) vs BER — `exam_bb90_2_p4` / `exam_bb60_2_p4`
- [x] **Gluconeogenesis Bypass Enzymes:** Pyruvate carboxylase, PEPCK, FBPase-1, and G6Pase regulation by F-2,6-BP — `exam_bb90_2_disc` / `exam_bb60_2_disc`
- [x] **Enzyme Cooperativity & Two-State Models:** Monod-Wyman-Changeux (MWC) vs Koshland sequential model — `exam_bb90_2_disc` / `exam_bb60_2_disc`
- [x] **Chromatin Remodeling & Epigenetics:** Histone acetyltransferases (HATs), HDACs, and euchromatin vs heterochromatin — `exam_bb90_2_disc` / `exam_bb60_2_disc`
- [x] **Prokaryotic Operon Genetics:** Lac operon catabolite repression (CAP-cAMP) and repressor derepression — `exam_bb90_2_disc`
- [x] **RNA Interference & Non-Coding RNAs:** miRNA and siRNA RISC complex gene silencing in cancer — `exam_bb90_2_disc`
- [x] **Biochemical Separation Techniques:** Size-exclusion, ion-exchange, and isoelectric focusing gels — `exam_bb90_2_disc`
- [ ] **Eukaryotic DNA Replication Fork:** Pol $\alpha/\delta/\epsilon$, PCNA sliding clamp, RFC, and telomerase reverse transcription
- [ ] **Post-Translational Protein Modifications:** Ubiquitination (26S proteasome), glycosylation, phosphorylation, and zymogen cleavage
- [ ] **Lipid Classification & Membrane Fluidity:** Cholesterol dual thermal buffer, sphingolipids, glycosphingolipids, and lipid rafts

#### B. Cell Biology & Physiology
- [x] Renal concentrating mechanism and countercurrent multiplication — `bb_renal` / `exam_bb60_p1`
- [x] Cardiovascular hemodynamics and vascular resistance — `bb_cv` / `exam_bb60_p2`
- [x] Respiratory gas exchange and hemoglobin Bohr/Haldane effects — `bb_resp` / `exam_bb60_p3`
- [x] Cardiac action potential electrophysiology and Long QT syndromes — `exam_bb90_p5`
- [x] Endocrine feedback loops (HPA, HPT) — `bb_endo` / `exam_bb60_p5`
- [x] Neuronal action potentials and synaptic transmission — `bb_neuro`
- [x] Hardy-Weinberg population genetics — `exam_bb90_discretes`
- [x] Embryonic germ layer derivatives — `exam_bb90_discretes`
- [x] Renal clearance and GFR measurement via inulin/PAH — `exam_bb90_discretes`
- [x] **Cardiac Cycle & Wiggers Diagram:** Pressure-volume loops, valve timing, and heart sounds — `exam_bb90_2_p5` / `exam_bb60_2_p5`
- [x] **Renal Tubular Acid-Base Transport:** Intercalated cells, type A (acid secretion) vs type B (bicarbonate secretion), and RTA — `exam_bb90_2_p6`
- [x] **Major Histocompatibility Complex (MHC):** Endogenous (MHC-I) vs exogenous (MHC-II) antigen processing pathways — `exam_bb90_2_p7`
- [x] **Microvascular Starling Forces:** Capillary hydrostatic vs oncotic pressures in pulmonary and peripheral edema — `exam_bb90_2_disc`
- [x] **Sliding Filament Cross-Bridge Cycle:** ATP binding, hydrolysis, power stroke, rigor mortis, and calcium-troponin C regulation — `exam_bb90_2_disc`
- [x] **Endocrine Calcium Homeostasis:** PTH, Calcitonin, and Calcitriol (Vitamin D3) actions on bone, gut, and kidney — `exam_bb90_2_disc`
- [x] **Hypothalamic-Pituitary-Gonadal (HPG) Axis:** Menstrual cycle follicular, ovulatory, and luteal phases, LH surge, estrogen feedback — `exam_bb90_2_disc`
- [ ] **Adaptive Cell-Mediated Immunity:** CD4+ Th1/Th2/Th17 differentiation vs CD8+ cytotoxic T-cell perforin/granzyme apoptosis
- [ ] **Gastrointestinal Digestion & Absorption:** Enteropeptidase activation cascade, lipid micelle formation, and chylomicron packaging
- [ ] **Hepatic Biotransformation:** Phase I (cytochrome P450 oxidation) and Phase II (glucuronidation/glutathione conjugation) drug metabolism
- [ ] **Embryology & Morphogen Gradients:** Sonic hedgehog (Shh), homeobox (Hox) genes, and limb axis patterning

---

### SECTION 4: Psychological, Social & Biological Foundations (P/S)

#### A. Sensation, Perception, Cognition & Biology
- [x] Signal Detection Theory ($d'$ and criterion $c$) in diagnostic imaging — `exam_ps90_p1`
- [x] Stereotype threat and central executive working memory depletion — `exam_ps90_p2` / `exam_ps60_p4`
- [x] Operant schedules of reinforcement and incentive-sensitization — `exam_ps90_p5`
- [x] Schizophrenia dopamine pathways and antipsychotic pharmacology — `exam_ps90_p6`
- [x] Weber's law difference threshold calculation — `exam_ps90_discretes`
- [x] Theories of emotion (Schachter-Singer two-factor model) — `exam_ps90_discretes`
- [x] Gestalt laws of visual organization — `exam_ps90_discretes`
- [x] Sensory adaptation vs habituation — `exam_ps90_discretes`
- [x] **Visual Psychophysics & Phototransduction:** Rhodopsin, transducin, PDE, cGMP drop, and bipolar cell disinhibition — `exam_ps90_2_p1` / `exam_ps60_2_p1`
- [x] **Auditory Hair Cell Mechano-Transduction:** Stereocilia deflection, tip links, K⁺ influx from endolymph, and tonotopic organization — `exam_ps90_2_p2` / `exam_ps60_2_p2`
- [x] **Sleep Architecture & Circadian Regulation:** Melatonin, SCN, polysomnography, REM atonia, and slow-wave sleep memory consolidation — `exam_ps90_2_p3` / `exam_ps60_2_p3`
- [x] **Theories of Language Acquisition:** Chomsky's Universal Grammar/LAD vs Skinner's Operant conditioning vs Vygotsky's Interactionism — `exam_ps90_2_p4` / `exam_ps60_2_p4`
- [x] **Memory Encoding & Forgetting Models:** Ebbinghaus forgetting curve, proactive vs retroactive interference — `exam_ps90_2_disc` / `exam_ps60_2_disc`
- [x] **Dual-Process Cognitive Models:** System 1 (heuristic/intuitive) vs System 2 (analytical/deliberative) and cognitive biases — `exam_ps90_2_disc` / `exam_ps60_2_disc`
- [x] **Neurobiology of Stress & Allostatic Load:** HPA axis, CRH, ACTH, cortisol, hippocampal dendritic atrophy — `exam_ps90_2_disc` / `exam_ps60_2_disc`
- [x] **Neurology of Limbic Emotion:** Amygdala fear conditioning, prefrontal emotional regulation, and Klüver-Bucy syndrome — `exam_ps90_2_disc`
- [x] **Consciousness & Split-Brain Phenomena:** Corpus callosum agenesis, left hemisphere verbal interpreter vs right hemisphere spatial processing — `exam_ps90_2_disc`
- [ ] **Olfactory & Gustatory Transduction:** G-protein coupled olfaction, glomeruli mitral cells, and taste receptor cells
- [ ] **Somatosensory Proprioception & Pain:** A-beta, A-delta, and C nerve fibers, gate control theory of pain, and phantom limb
- [ ] **Working Memory Architecture:** Baddeley's model (phonological loop, visuospatial sketchpad, episodic buffer, central executive)

#### B. Society, Social Psychology & Stratification
- [x] Fundamental Cause Theory and residential segregation weathering — `exam_ps90_p3` / `exam_ps60_p5`
- [x] Elaboration Likelihood Model and cognitive dissonance — `exam_ps90_p4`
- [x] Dramaturgical perspective (front/back stage) and role dynamics — `exam_ps90_p7`
- [x] Helping behavior, bystander effect, and diffusion of responsibility — `ps_social` / `exam_ps60_p1`
- [x] Erikson's developmental crises — `exam_ps90_discretes`
- [x] Kohlberg's stages of moral development — `exam_ps90_discretes`
- [x] Fundamental attribution error vs actor-observer bias — `exam_ps90_discretes`
- [x] George Herbert Mead's 'I' vs 'Me' social self — `exam_ps90_discretes`
- [x] Institutional vs individual discrimination — `exam_ps90_discretes`
- [x] **Forms of Capital:** Bourdieu's Economic, Cultural (embodied/objectified/institutionalized), and Social Capital — `exam_ps90_2_p5` / `exam_ps60_2_p5`
- [x] **Medicalization & The Sick Role:** Talcott Parsons' rights and obligations of the sick role vs demedicalization — `exam_ps90_2_p6`
- [x] **Social Influence & Conformity Paradigms:** Asch line judgment (normative vs informational influence), Groupthink, and Group polarization — `exam_ps90_2_p7`
- [x] **Sociological Paradigms Comparison:** Structural Functionalism (manifest/latent) vs Conflict Theory vs Symbolic Interactionism — `exam_ps90_2_disc`
- [x] **Social Constructionism:** Money, gender, and illness as socially constructed institutional facts — `exam_ps90_2_disc`
- [x] **Intersectionality & Health Inequity:** Compounding effects of race, gender, class, and sexual orientation on clinical outcomes — `exam_ps90_2_disc`
- [x] **Deviance & Social Control:** Labeling theory (primary vs secondary deviance), Differential Association theory, and Merton's Strain theory — `exam_ps90_2_disc`
- [x] **Demographic Transition Model:** Stages 1–5 (birth/death rate dynamics) and population pyramids — `exam_ps90_2_disc`
- [ ] **Social Identity & Self-Concept:** In-group favoritism, out-group derogation, ethnocentrism vs cultural relativism
- [ ] **Urbanization & Health Disparities:** Gentrification, food deserts, environmental racism, and spatial mismatch
- [ ] **Social Mobility & Stratification:** Intergenerational vs intragenerational mobility, horizontal vs vertical, and meritocracy

---

## 🛠️ Content Creator Workflow (How to Avoid Duplication)

When designing a new passage set or discrete question block for DrillRoom:

1. **Check the Coverage Dashboard**: Identify the section with the lowest coverage percentage.
2. **Scan the Master Checklist**: Select an uncovered topic marked with `[ ]`.
3. **Verify Existing Passage Titles**: Confirm that the target concept has not been previously utilized as a primary passage subject.
4. **Adhere to AAMC Distractor Engineering Guidelines**:
   * Build distractors using the 6 core AAMC trap archetypes (Formula Inversion, One-Step-Short, Sign Flips, Familiar Falsehood, Extreme Scope, Unwarranted Extrapolation).
   * Maintain character length parity ($\pm 20\%$) across all four options.
   * Ban extreme cueing words (*always*, *never*, *solely*, *completely*).
   * Order numerical options monotonically (ascending or descending).
   * Include detailed distractor trap analyses in the explanation (`q.e`).
5. **Update the Master Tracker**: Once the code is integrated into `practice_exam.js` and `DrillRoom.html`, check off the item (`[x]`), record the unique set ID, and increment the dashboard counters.
"""

with open(output_path, "w") as f:
    f.write(content)

print("MCAT-CURRICULUM-AND-TOPIC-TRACKER.md successfully updated with Exam 2 coverage!")
