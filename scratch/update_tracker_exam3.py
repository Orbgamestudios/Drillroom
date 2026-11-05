import re

path = "/home/cgslinde/DrillRoom/DrillRoom/MCAT-CURRICULUM-AND-TOPIC-TRACKER.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update Content Coverage Dashboard
dashboard_old = """| Section | Total Blueprint Topics | Created & Integrated `[x]` | Remaining Uncovered `[ ]` | Coverage % |
| :--- | :---: | :---: | :---: | :---: |
| **CARS** (Critical Analysis & Reasoning) | 200 | 30 | 170 | **15.0%** |
| **C/P** (Chemical & Physical Foundations) | 270 | 33 | 237 | **12.2%** |
| **B/B** (Biological & Biochemical Foundations) | 270 | 35 | 235 | **13.0%** |
| **P/S** (Psychological, Social & Biological) | 260 | 33 | 227 | **12.7%** |
| **TOTALS** | **1,000** | **131** | **869** | **13.1%** |"""

dashboard_new = """| Section | Total Blueprint Topics | Created & Integrated `[x]` | Remaining Uncovered `[ ]` | Coverage % |
| :--- | :---: | :---: | :---: | :---: |
| **CARS** (Critical Analysis & Reasoning) | 200 | 39 | 161 | **19.5%** |
| **C/P** (Chemical & Physical Foundations) | 270 | 50 | 220 | **18.5%** |
| **B/B** (Biological & Biochemical Foundations) | 270 | 52 | 218 | **19.3%** |
| **P/S** (Psychological, Social & Biological) | 260 | 50 | 210 | **19.2%** |
| **TOTALS** | **1,000** | **191** | **809** | **19.1%** |"""

assert dashboard_old in text, "Dashboard table not found"
text = text.replace(dashboard_old, dashboard_new)

# 2. Update Audit section header
text = text.replace("## 🔍 Audit of Currently Created Content in DrillRoom (131 Covered Sets)", "## 🔍 Audit of Currently Created Content in DrillRoom (191 Covered Sets)")
text = text.replace("### 1. CARS Existing Passages (30 Passages / Sets)", "### 1. CARS Existing Passages (39 Passages / Sets)")
text = text.replace("### 2. C/P Existing Topics (33 Topics / Sets)", "### 2. C/P Existing Topics (50 Topics / Sets)")
text = text.replace("### 3. B/B Existing Topics (35 Topics / Sets)", "### 3. B/B Existing Topics (52 Topics / Sets)")
text = text.replace("### 4. P/S Existing Topics (33 Topics / Sets)", "### 4. P/S Existing Topics (50 Topics / Sets)")

# 3. Add Exam 3 Suite to CARS audit
cars_exam3_audit = """* `exam_cars90_2_p9`: **Urban Sociology: Le Corbusier vs Jane Jacobs Urbanism**

#### Exam 3 Suite (9 Passages)
* `exam_cars90_3_p1 / exam_cars60_3_p1`: **Kantian Deontology & The Categorical Imperative**
* `exam_cars90_3_p2 / exam_cars60_3_p2`: **Utilitarian Consequentialism & Preference Aggregation**
* `exam_cars90_3_p3 / exam_cars60_3_p3`: **Existentialist Ethics of Freedom & Bad Faith (Sartre)**
* `exam_cars90_3_p4 / exam_cars60_3_p4`: **Pragmatist Epistemology & Instrumental Truth (William James)**
* `exam_cars90_3_p5 / exam_cars60_3_p5`: **Epistemological Skepticism & The Brain in a Vat (Putnam)**
* `exam_cars90_3_p6 / exam_cars60_3_p6`: **Philosophy of Science: Thomas Kuhn & Paradigm Incommensurability**
* `exam_cars90_3_p7`: **Philosophy of Science: Karl Popper & Falsificationism**
* `exam_cars90_3_p8`: **Philosophy of Mind: The Hard Problem of Consciousness (Chalmers)**
* `exam_cars90_3_p9`: **Epistemic Injustice: Testimonial & Hermeneutical Harm (Fricker)**"""

text = text.replace("* `exam_cars90_2_p9`: **Urban Sociology: Le Corbusier vs Jane Jacobs Urbanism**", cars_exam3_audit)

# 4. Add Exam 3 Suite to C/P audit
cp_exam3_audit = """* `exam_cp90_2_disc`: **Mass Spectrometry Isotopic Signatures (Bromine & Chlorine)**

#### Exam 3 Suite (17 Topics)
* `exam_cp90_3_p1 / exam_cp60_3_p1`: **One-Dimensional Kinematics & Freefall Acceleration in Pulmonary Drug Delivery**
* `exam_cp90_3_p2 / exam_cp60_3_p2`: **Two-Dimensional Projectile Motion & Vector Independence in Paralympic Biomechanics**
* `exam_cp90_3_p3 / exam_cp60_3_p3`: **Newton's Laws of Motion & Inertial Reference Frames in Clinical Transport and Traction**
* `exam_cp90_3_p4 / exam_cp60_3_p4`: **Static vs Kinetic Friction on Inclined Planes in Orthopedic Biomechanics**
* `exam_cp90_3_p5 / exam_cp60_3_p5`: **Uniform Circular Motion & Centripetal Acceleration in Analytical Ultracentrifugation**
* `exam_cp90_3_p6`: **Work-Energy Theorem & Kinetic Energy in Cardiac Hemodynamics**
* `exam_cp90_3_p7`: **Conservative vs Non-Conservative Forces in Energy-Storing Prosthetics**
* `exam_cp90_3_disc / exam_cp60_3_disc`: **Hooke's Law & Elastic Potential Energy in Tendons**
* `exam_cp90_3_disc / exam_cp60_3_disc`: **Mechanical Power & Human Metabolic Energy Expenditure**
* `exam_cp90_3_disc / exam_cp60_3_disc`: **Linear Momentum & Impulse in Traumatic Impacts**
* `exam_cp90_3_disc`: **Elastic vs Inelastic Collisions & Kinetic Energy Losses**
* `exam_cp90_3_disc`: **Center of Mass Calculation for Multi-Body Biological Systems**
* `exam_cp90_3_disc`: **Density, Specific Gravity & Hydrometer Measurements**
* `exam_cp90_3_disc`: **Hydrostatic Pressure & Barometric Mercury Manometers**
* `exam_cp90_3_disc`: **Pascal's Principle & Hydraulic Multiplication in Medical Equipment**
* `exam_cp90_3_disc`: **Archimedes' Principle & Specific Gravity of Submerged Bodies**
* `exam_cp90_3_disc`: **Surface Tension & Capillary Action in Glass Tubes**"""

text = text.replace("* `exam_cp90_2_disc`: **Mass Spectrometry Isotopic Signatures (Bromine & Chlorine)**", cp_exam3_audit)

# 5. Add Exam 3 Suite to B/B audit
bb_exam3_audit = """* `exam_bb90_2_disc`: **Myosin Cross-Bridge Cycle & Rigor Mortis Mechanics**

#### Exam 3 Suite (17 Topics)
* `exam_bb90_3_p1 / exam_bb60_3_p1`: **Parathyroid Hormone (PTH), Calcitonin & Calcitriol Calcium Triad**
* `exam_bb90_3_p2 / exam_bb60_3_p2`: **Hypothalamic-Pituitary-Gonadal (HPG) Axis & The Mid-Cycle LH Surge**
* `exam_bb90_3_p3 / exam_bb60_3_p3`: **Primary Structure & Disulfide Bond Chemistry of Insulin**
* `exam_bb90_3_p4 / exam_bb60_3_p4`: **Alpha-Helix Geometry: Hydrogen Bonding Patterns & Destabilizing Residues**
* `exam_bb90_3_p5 / exam_bb60_3_p5`: **Beta-Pleated Sheet Architecture: Parallel vs Antiparallel Topology**
* `exam_bb90_3_p6`: **Hydrophobic Interactions & Entropy of Solvent Water During Protein Folding**
* `exam_bb90_3_p7`: **Denaturation of Proteins: Guanidinium Chloride, Urea, and Thermal Melting**
* `exam_bb90_3_disc / exam_bb60_3_disc`: **Chaperone-Assisted Protein Folding: Hsp70 and GroEL/GroES Chaperonins**
* `exam_bb90_3_disc / exam_bb60_3_disc`: **Collagen Biosynthesis, Prolyl Hydroxylase & Vitamin C (Scurvy)**
* `exam_bb90_3_disc / exam_bb60_3_disc`: **Affinity Chromatography: Polyhistidine-Tags & Nickel-NTA Resin**
* `exam_bb90_3_disc`: **Catalytic Triad Mechanism of Chymotrypsin: Ser195, His57, Asp102**
* `exam_bb90_3_disc`: **Koshland-Némethy-Filmer (KNF) Sequential Model of Cooperativity**
* `exam_bb90_3_disc`: **Enzyme Catalytic Efficiency (kcat / Km) & Diffusion-Controlled Limit**
* `exam_bb90_3_disc`: **Lineweaver-Burk Double Reciprocal Transformations & Diagnostic Axes**
* `exam_bb90_3_disc`: **Uncompetitive Enzyme Inhibition & The E-S Complex**
* `exam_bb90_3_disc`: **Mixed Enzyme Inhibition & Allosteric Active Site Distortion**
* `exam_bb90_3_disc`: **Irreversible Enzyme Inactivation: Organophosphates & Acetylcholinesterase**"""

text = text.replace("* `exam_bb90_2_disc`: **Myosin Cross-Bridge Cycle & Rigor Mortis Mechanics**", bb_exam3_audit)

# 6. Add Exam 3 Suite to P/S audit
ps_exam3_audit = """* `exam_ps90_2_disc`: **Social Constructionism: Institutional Realities vs Brute Physical Facts**

#### Exam 3 Suite (17 Topics)
* `exam_ps90_3_p1 / exam_ps60_3_p1`: **Visual Anatomy & Optics of the Human Eye**
* `exam_ps90_3_p2 / exam_ps60_3_p2`: **Retinal Circuitry: Photoreceptors to Retinal Ganglion Cells**
* `exam_ps90_3_p3 / exam_ps60_3_p3`: **Parallel Visual Processing: Parvocellular vs Magnocellular Pathways**
* `exam_ps90_3_p4 / exam_ps60_3_p4`: **Visual Cortex Architecture: Feature Detection & Receptive Fields**
* `exam_ps90_3_p5 / exam_ps60_3_p5`: **Theories of Color Vision: Trichromatic vs Opponent-Process Theory**
* `exam_ps90_3_p6`: **Depth Perception Cues: Monocular vs Binocular Mechanisms**
* `exam_ps90_3_p7`: **Visual Perceptual Constancies: Size, Shape & Color Constancy**
* `exam_ps90_3_disc / exam_ps60_3_disc`: **Auditory Peripheral Anatomy: Middle Ear Impedance Matching**
* `exam_ps90_3_disc / exam_ps60_3_disc`: **Central Auditory Pathway & Subcortical Sound Localization**
* `exam_ps90_3_disc / exam_ps60_3_disc`: **Vestibular System: Semicircular Canals & Otolith Organs**
* `exam_ps90_3_disc`: **Somatosensory Mechanoreceptors: Tactile Transduction & Adaptation**
* `exam_ps90_3_disc`: **Pain Neurobiology: Nociception, Anterolateral System & Gate Control**
* `exam_ps90_3_disc`: **Proprioceptive Neuromuscular Sensors: Muscle Spindles & Golgi Organs**
* `exam_ps90_3_disc`: **Olfactory Anatomy & Signal Transduction Mechanisms**
* `exam_ps90_3_disc`: **Gustatory System: Papillae, Taste Buds & Signal Transduction**
* `exam_ps90_3_disc`: **Pheromonal Signaling & The Accessory Olfactory System**
* `exam_ps90_3_disc`: **Synesthesia & Intersensory Cross-Modal Integration**"""

text = text.replace("* `exam_ps90_2_disc`: **Social Constructionism: Institutional Realities vs Brute Physical Facts**", ps_exam3_audit)

# 7. Check off topics in the 1,000 topic list
topic_updates = {
    # CARS Topics 31-39
    31: ("31. Kantian Deontology & The Categorical Imperative", "exam_cars90_3_p1 / exam_cars60_3_p1"),
    32: ("32. Utilitarian Consequentialism & Preference Aggregation", "exam_cars90_3_p2 / exam_cars60_3_p2"),
    33: ("33. Existentialist Ethics of Freedom & Bad Faith (Sartre)", "exam_cars90_3_p3 / exam_cars60_3_p3"),
    34: ("34. Pragmatist Epistemology & Instrumental Truth (William James)", "exam_cars90_3_p4 / exam_cars60_3_p4"),
    35: ("35. Epistemological Skepticism & The Brain in a Vat", "exam_cars90_3_p5 / exam_cars60_3_p5"),
    36: ("36. Philosophy of Science: Thomas Kuhn & Paradigm Incommensurability", "exam_cars90_3_p6 / exam_cars60_3_p6"),
    37: ("37. Philosophy of Science: Karl Popper & Falsificationism", "exam_cars90_3_p7"),
    38: ("38. Philosophy of Mind: The Hard Problem of Consciousness (Chalmers)", "exam_cars90_3_p8"),
    39: ("39. Epistemic Injustice: Testimonial & Hermeneutical Harm (Fricker)", "exam_cars90_3_p9"),

    # C/P Topics 234-250
    234: ("234. One-Dimensional Kinematics & Freefall Acceleration", "exam_cp90_3_p1 / exam_cp60_3_p1"),
    235: ("235. Two-Dimensional Projectile Motion & Vector Independence", "exam_cp90_3_p2 / exam_cp60_3_p2"),
    236: ("236. Newton's Laws of Motion & Inertial Reference Frames", "exam_cp90_3_p3 / exam_cp60_3_p3"),
    237: ("237. Static vs Kinetic Friction on Inclined Planes", "exam_cp90_3_p4 / exam_cp60_3_p4"),
    238: ("238. Uniform Circular Motion & Centripetal Acceleration", "exam_cp90_3_p5 / exam_cp60_3_p5"),
    239: ("239. Work-Energy Theorem & Kinetic Energy", "exam_cp90_3_p6"),
    240: ("240. Conservative vs Non-Conservative Forces", "exam_cp90_3_p7"),
    241: ("241. Hooke's Law & Elastic Potential Energy in Tendons", "exam_cp90_3_disc / exam_cp60_3_disc"),
    242: ("242. Mechanical Power & Human Metabolic Energy Expenditure", "exam_cp90_3_disc / exam_cp60_3_disc"),
    243: ("243. Linear Momentum & Impulse in Traumatic Impacts", "exam_cp90_3_disc / exam_cp60_3_disc"),
    244: ("244. Elastic vs Inelastic Collisions & Coefficient of Restitution", "exam_cp90_3_disc"),
    245: ("245. Center of Mass Calculation for Multi-Body Biological Systems", "exam_cp90_3_disc"),
    246: ("246. Density, Specific Gravity & Hydrometer Measurements", "exam_cp90_3_disc"),
    247: ("247. Hydrostatic Pressure & Barometric Mercury Manometers", "exam_cp90_3_disc"),
    248: ("248. Pascal's Principle & Hydraulic Multiplication in Medical Equipment", "exam_cp90_3_disc"),
    249: ("249. Archimedes' Principle & Specific Gravity of Submerged Bodies", "exam_cp90_3_disc"),
    250: ("250. Surface Tension & Capillary Action in Glass Tubes", "exam_cp90_3_disc"),

    # B/B Topics 506-522
    506: ("506. Parathyroid Hormone (PTH), Calcitonin & Calcitriol Calcium Triad", "exam_bb90_3_p1 / exam_bb60_3_p1"),
    507: ("507. Hypothalamic-Pituitary-Gonadal (HPG) Axis & The Mid-Cycle LH Surge", "exam_bb90_3_p2 / exam_bb60_3_p2"),
    508: ("508. Primary Structure & Disulfide Bond Chemistry of Insulin", "exam_bb90_3_p3 / exam_bb60_3_p3"),
    509: ("509. Alpha-Helix Geometry: Hydrogen Bonding Patterns & Destabilizing Residues", "exam_bb90_3_p4 / exam_bb60_3_p4"),
    510: ("510. Beta-Pleated Sheet Architecture: Parallel vs Antiparallel Topology", "exam_bb90_3_p5 / exam_bb60_3_p5"),
    511: ("511. Hydrophobic Interactions & Entropy of Solvent Water During Protein Folding", "exam_bb90_3_p6"),
    512: ("512. Denaturation of Proteins: Guanidinium Chloride, Urea, and Thermal Melting", "exam_bb90_3_p7"),
    513: ("513. Chaperone-Assisted Protein Folding: Hsp70 and GroEL/GroES Chaperonins", "exam_bb90_3_disc / exam_bb60_3_disc"),
    514: ("514. Collagen Biosynthesis, Prolyl Hydroxylase & Vitamin C (Scurvy)", "exam_bb90_3_disc / exam_bb60_3_disc"),
    515: ("515. Affinity Chromatography: Polyhistidine-Tags & Nickel-NTA Resin", "exam_bb90_3_disc / exam_bb60_3_disc"),
    516: ("516. Catalytic Triad Mechanism of Chymotrypsin: Ser195, His57, Asp102", "exam_bb90_3_disc"),
    517: ("517. Koshland-Némethy-Filmer (KNF) Sequential Model of Cooperativity", "exam_bb90_3_disc"),
    518: ("518. Enzyme Catalytic Efficiency (kcat / Km) & Diffusion-Controlled Limit", "exam_bb90_3_disc"),
    519: ("519. Lineweaver-Burk Double Reciprocal Transformations & Diagnostic Axes", "exam_bb90_3_disc"),
    520: ("520. Uncompetitive Enzyme Inhibition & The E-S Complex", "exam_bb90_3_disc"),
    521: ("521. Mixed Enzyme Inhibition & Allosteric Active Site Distortion", "exam_bb90_3_disc"),
    522: ("522. Irreversible Enzyme Inactivation: Organophosphates & Acetylcholinesterase", "exam_bb90_3_disc"),

    # P/S Topics 774-790
    774: ("774. Visual Anatomy & Optics of the Human Eye", "exam_ps90_3_p1 / exam_ps60_3_p1"),
    775: ("775. Retinal Circuitry: Photoreceptors to Retinal Ganglion Cells", "exam_ps90_3_p2 / exam_ps60_3_p2"),
    776: ("776. Parallel Visual Processing: Parvocellular vs Magnocellular Pathways", "exam_ps90_3_p3 / exam_ps60_3_p3"),
    777: ("777. Visual Cortex Architecture: Feature Detection & Receptive Fields", "exam_ps90_3_p4 / exam_ps60_3_p4"),
    778: ("778. Theories of Color Vision: Trichromatic vs Opponent-Process Theory", "exam_ps90_3_p5 / exam_ps60_3_p5"),
    779: ("779. Depth Perception Cues: Monocular vs Binocular Mechanisms", "exam_ps90_3_p6"),
    780: ("780. Visual Perceptual Constancies: Size, Shape & Color Constancy", "exam_ps90_3_p7"),
    781: ("781. Auditory Peripheral Anatomy: Middle Ear Impedance Matching", "exam_ps90_3_disc / exam_ps60_3_disc"),
    782: ("782. Central Auditory Pathway & Subcortical Sound Localization", "exam_ps90_3_disc / exam_ps60_3_disc"),
    783: ("783. Vestibular System: Semicircular Canals & Otolith Organs", "exam_ps90_3_disc / exam_ps60_3_disc"),
    784: ("784. Somatosensory Mechanoreceptors: Tactile Transduction & Adaptation", "exam_ps90_3_disc"),
    785: ("785. Pain Neurobiology: Nociception, Anterolateral System & Gate Control", "exam_ps90_3_disc"),
    786: ("786. Proprioceptive Neuromuscular Sensors: Muscle Spindles & Golgi Organs", "exam_ps90_3_disc"),
    787: ("787. Olfactory Anatomy & Signal Transduction Mechanisms", "exam_ps90_3_disc"),
    788: ("788. Gustatory System: Papillae, Taste Buds & Signal Transduction", "exam_ps90_3_disc"),
    789: ("789. Pheromonal Signaling & The Accessory Olfactory System", "exam_ps90_3_disc"),
    790: ("790. Synesthesia & Intersensory Cross-Modal Integration", "exam_ps90_3_disc"),
}

for num, (title, cite) in topic_updates.items():
    # Target pattern: - [ ] **num. Title**
    target_pattern = rf"- \[ \] \*\*{re.escape(title)}\*\*"
    replacement = rf"- [x] **{title}** — `{cite}`"
    if not re.search(target_pattern, text):
        print(f"WARNING: Could not find target pattern for Topic {num}: {title}")
    text = re.sub(target_pattern, replacement, text)

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("MCAT-CURRICULUM-AND-TOPIC-TRACKER.md successfully updated!")
