import re, json
import sys
sys.path.append('scratch')
from parse_cars import JSObjectParser, parse_set_at

with open("DrillRoom.html") as f:
    html = f.read()

scripts = re.findall(r"<script>(.*?)</script>", html, re.DOTALL)

def update_title(passage_html, passage_num, q_start, q_end):
    new_ttl = f'<div class="ttl">Passage {passage_num} (Questions {q_start}&ndash;{q_end})</div>'
    if '<div class="ttl">' in passage_html:
        return re.sub(r'<div class="ttl">.*?</div>', new_ttl, passage_html, count=1)
    else:
        return f'{new_ttl}\n{passage_html}'

# ==========================================
# 1. EXAM_CP60
# ==========================================
# P1: cp_acid (Q1-Q5)
cp_p1_raw = parse_set_at(scripts[2], "cp_acid")
cp_p1 = {
    "id": "exam_cp60_p1",
    "sec": "C/P",
    "topic": "Acid–base equilibria and buffer systems in physiological buffering",
    "sheet": 13,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60",
    "passage": update_title(cp_p1_raw["passage"], 1, 1, 5),
    "qs": cp_p1_raw["qs"][:5]
}

# P2: cp_kin (Q1-Q6)
cp_p2_raw = parse_set_at(scripts[2], "cp_kin")
cp_p2 = {
    "id": "exam_cp60_p2",
    "sec": "C/P",
    "topic": "Chemical kinetics, reaction mechanisms, and catalysis",
    "sheet": 8,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60",
    "passage": update_title(cp_p2_raw["passage"], 2, 6, 11),
    "qs": cp_p2_raw["qs"][:6]
}

# P3: cp_phys (Q1, Q2, Q3, Q4, Q6) -> 5 Qs
cp_p3_raw = parse_set_at(scripts[4], "cp_phys")
cp_p3_qs = [cp_p3_raw["qs"][0], cp_p3_raw["qs"][1], cp_p3_raw["qs"][2], cp_p3_raw["qs"][3], cp_p3_raw["qs"][5]]
cp_p3 = {
    "id": "exam_cp60_p3",
    "sec": "C/P",
    "topic": "Fluid dynamics, Poiseuille flow, and circulatory resistance",
    "sheet": 67,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60",
    "passage": update_title(cp_p3_raw["passage"], 3, 12, 16),
    "qs": cp_p3_qs
}

# P4: Fresh Organic Synthesis passage (Q17-Q22, 6 Qs)
cp_p4_html = """<div class="ttl">Passage 4 (Questions 17&ndash;22)</div>
<p>Nonsteroidal anti-inflammatory drugs (NSAIDs) such as ibuprofen inhibit cyclooxygenase (COX) enzymes, but their acidic carboxylic acid moiety frequently causes gastrointestinal mucosal erosion. To circumvent this, medicinal chemists synthesized a series of bioreversible amide-ester prodrugs designed to remain intact in the acidic gastric environment (pH &asymp; 1.5&ndash;2.0) and undergo enzymatic hydrolysis in the small intestine (pH &asymp; 6.8&ndash;7.4).</p>
<p>The synthetic scheme began by activating (<i>S</i>)-2-(4-isobutylphenyl)propanoic acid (Compound 1) with thionyl chloride (SOCl<sub>2</sub>) to yield the corresponding acyl chloride. This intermediate was reacted with 2-aminoethanol in anhydrous dichloromethane in the presence of triethylamine (Et<sub>3</sub>N) at 273 K to yield Compound 2. Subsequent acylation of Compound 2 with acetyl chloride in pyridine yielded the target prodrug, Compound 3.</p>
<p>Reaction progress was monitored by thin-layer chromatography (TLC) on silica gel plates developed in 3:1 hexanes:ethyl acetate and visualized under UV illumination (254 nm). Purified products were characterized by Fourier-transform infrared (FTIR) spectroscopy and <sup>1</sup>H-NMR spectroscopy in CDCl<sub>3</sub>.</p>
<table>
<tr><th>Compound</th><th>Molecular Formula</th><th>TLC <i>R</i><sub>f</sub></th><th>Key FTIR Absorption Bands (cm<sup>&minus;1</sup>)</th><th>Selected <sup>1</sup>H-NMR Shifts (&delta;, ppm)</th></tr>
<tr><td>1 (Ibuprofen)</td><td>C<sub>13</sub>H<sub>18</sub>O<sub>2</sub></td><td class="n">0.52</td><td class="n">1710 (C=O), 2500&ndash;3300 (broad O&minus;H)</td><td class="n">3.71 (q, 1H), 1.50 (d, 3H)</td></tr>
<tr><td>2 (Amide intermediate)</td><td>C<sub>15</sub>H<sub>23</sub>NO<sub>2</sub></td><td class="n">0.18</td><td class="n">1645 (amide C=O), 3320 (broad N&minus;H/O&minus;H)</td><td class="n">3.65 (q, 1H), 3.42 (t, 2H), 1.48 (d, 3H)</td></tr>
<tr><td>3 (Prodrug)</td><td>C<sub>17</sub>H<sub>25</sub>NO<sub>3</sub></td><td class="n">0.44</td><td class="n">1738 (ester C=O), 1650 (amide C=O), 3310 (sharp N&minus;H)</td><td class="n">4.18 (t, 2H), 3.64 (q, 1H), 2.05 (s, 3H)</td></tr>
</table>
<p class="cap"><b>Table 1</b> Chromatographic, vibrational, and magnetic resonance parameters for synthetic intermediates.</p>"""

cp_p4_qs = [
    {
        "q": "Based on the TLC data in Table 1, which ranking correctly orders the compounds by increasing polarity when evaluated on normal-phase silica gel?",
        "ch": [
            "Compound 2 < Compound 3 < Compound 1",
            "Compound 1 < Compound 3 < Compound 2",
            "Compound 2 < Compound 1 < Compound 3",
            "Compound 3 < Compound 1 < Compound 2"
        ],
        "a": 1,
        "e": "<strong>Higher polarity corresponds to stronger adsorption to silica gel and lower Rf:</strong> Normal-phase silica gel is highly polar (containing surface silanol &minus;Si&minus;OH groups), while the 3:1 hexanes:ethyl acetate mobile phase is relatively nonpolar. More polar compounds bind tightly to the stationary phase and travel more slowly (lower <i>R</i><sub>f</sub>). With <i>R</i><sub>f</sub> values of 0.52 (Compound 1) > 0.44 (Compound 3) > 0.18 (Compound 2), increasing polarity order is Compound 1 < Compound 3 < Compound 2. Compound 2 has both a secondary amide and a free primary alcohol, making it the most polar."
    },
    {
        "q": "What is the primary mechanistic function of triethylamine (Et<sub>3</sub>N) in the conversion of the activated acyl chloride to Compound 2?",
        "ch": [
            "It acts as a Lewis acid to polarize the acyl chloride carbonyl oxygen.",
            "It acts as a phase-transfer catalyst that shuttles chloride ions into the organic layer.",
            "It acts as a Br&oslash;nsted base that neutralizes generated HCl, preventing protonation and deactivation of the amine nucleophile.",
            "It acts as a nucleophilic catalyst by forming a persistent tetrahedral adduct with Compound 1."
        ],
        "a": 2,
        "e": "<strong>Triethylamine acts as an acid scavenger:</strong> Nucleophilic attack of 2-aminoethanol on the acyl chloride liberates hydrochloric acid (HCl). Because 2-aminoethanol is basic, unneutralized HCl would protonate the amine to form an unreactive ammonium salt (&minus;NH<sub>3</sub><sup>+</sup>), arresting the reaction. The tertiary amine Et<sub>3</sub>N (p<i>K</i><sub>a</sub> of conjugate acid &asymp; 10.75) is sufficiently basic to neutralize HCl forming Et<sub>3</sub>NH<sup>+</sup>Cl<sup>&minus;</sup> precipitate, while steric hindrance prevents Et<sub>3</sub>N from competitively attacking the acyl chloride."
    },
    {
        "q": "The FTIR spectrum of Compound 3 exhibits a prominent absorption band at 1738 cm<sup>&minus;1</sup> that is absent in Compound 2. This absorption band corresponds to which vibrational mode?",
        "ch": [
            "C=C stretching of the aromatic isobutylphenyl ring",
            "C=O stretching of the newly formed ester group",
            "N&minus;H bending of the secondary amide",
            "C&minus;O single bond stretching of the primary alcohol"
        ],
        "a": 1,
        "e": "<strong>Ester carbonyl stretches typically appear at 1735&ndash;1750 cm<sup>&minus;1</sup>:</strong> Converting the primary alcohol of Compound 2 to an acetate ester in Compound 3 introduces an ester carbonyl, which vibrates at a higher frequency (1738 cm<sup>&minus;1</sup>) than the amide carbonyl (1650 cm<sup>&minus;1</sup>) due to the electron-withdrawing inductive effect of the ester oxygen. Choice A appears at ~1500&ndash;1600 cm<sup>&minus;1</sup>; Choice C appears near 1550 cm<sup>&minus;1</sup>; Choice D appears in the fingerprint region (~1050&ndash;1150 cm<sup>&minus;1</sup>)."
    },
    {
        "q": "In the <sup>1</sup>H-NMR spectrum of Compound 1, the methine proton on the chiral carbon appears as a quartet at &delta; 3.71 ppm. According to the <i>n</i> + 1 spin-spin coupling rule, this splitting pattern arises because the proton is adjacent to:",
        "ch": [
            "four equivalent protons on the aromatic ring.",
            "two equivalent methylene protons on the isobutyl substituent.",
            "three equivalent methyl protons on the &alpha;-methyl group.",
            "one exchangeable carboxylic acid proton."
        ],
        "a": 2,
        "e": "<strong>Spin-spin splitting follows the n + 1 rule:</strong> The chiral methine proton &minus;CH(CH<sub>3</sub>)&minus; is coupled to the three protons of the adjacent methyl group (&minus;CH<sub>3</sub>). With <i>n</i> = 3 equivalent neighboring protons, the multiplicity is <i>n</i> + 1 = 3 + 1 = 4 (a quartet). Carboxylic acid protons undergo rapid chemical exchange and generally do not split adjacent C&minus;H protons."
    },
    {
        "q": "A synthetic batch of Compound 1 was analyzed by polarimetry. The observed specific rotation was [&alpha;] = +48&deg;/(dm&middot;g/mL). If optically pure (<i>S</i>)-ibuprofen has a specific rotation of +60&deg;/(dm&middot;g/mL), what is the percentage of the (<i>R</i>)-enantiomer in the synthetic batch?",
        "ch": [
            "10%",
            "20%",
            "40%",
            "80%"
        ],
        "a": 0,
        "e": "<strong>Calculate enantiomeric excess (ee) and solve for the minor enantiomer:</strong><br>ee = ([&alpha;]<sub>obs</sub> / [&alpha;]<sub>pure</sub>) &times; 100% = (+48&deg; / +60&deg;) &times; 100% = 80%.<br>An ee of 80% means 80% of the solution consists of pure (<i>S</i>)-enantiomer, while the remaining 20% is a racemic mixture of equal parts (<i>S</i>) and (<i>R</i>).<br>Therefore, % (<i>R</i>) = 20% / 2 = 10%, and % (<i>S</i>) = 80% + 10% = 90%. Choice B (20%) is the classic trap of taking the remaining non-excess percentage without dividing by 2."
    },
    {
        "q": "The transformation of the activated acyl chloride into Compound 2 proceeds via which reaction mechanism?",
        "ch": [
            "Electrophilic aromatic substitution",
            "S<sub>N</sub>2 displacement with inversion of configuration at the chiral center",
            "Nucleophilic acyl substitution via an addition-elimination pathway",
            "E2 elimination followed by conjugate addition"
        ],
        "a": 2,
        "e": "<strong>Carboxylic acid derivatives undergo nucleophilic acyl substitution:</strong> The primary amino group of 2-aminoethanol acts as a nucleophile, attacking the electrophilic carbonyl carbon of the acyl chloride to form a tetrahedral intermediate (addition step). Collapse of the tetrahedral intermediate reforms the C=O double bond and eliminates chloride as a leaving group (elimination step). The chiral center at the &alpha;-carbon is not involved in the reaction and retains its stereochemical integrity."
    }
]

cp_p4 = {
    "id": "exam_cp60_p4",
    "sec": "C/P",
    "topic": "Organic synthesis, nucleophilic acyl substitution, and spectroscopy",
    "sheet": 24,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60",
    "passage": cp_p4_html,
    "qs": cp_p4_qs
}

# P5: Fresh Electrochemistry biosensor passage (Q23-Q27, 5 Qs)
cp_p5_html = """<div class="ttl">Passage 5 (Questions 23&ndash;27)</div>
<p>Continuous monitoring of blood lactate is essential in critical care and sports medicine to evaluate tissue hypoperfusion. Electrochemical biosensors couple the enzymatic specificity of lactate oxidase (LOx) to amperometric transduction. LOx catalyzes the oxidation of L-lactate to pyruvate while reducing molecular oxygen to hydrogen peroxide (Reaction 1):</p>
<p style="text-align:center;font-style:italic">L-Lactate + O<sub>2</sub> &rarr; Pyruvate + H<sub>2</sub>O<sub>2</sub> &nbsp;&nbsp;&nbsp;&nbsp;(Reaction 1)</p>
<p>Direct electrochemical oxidation of H<sub>2</sub>O<sub>2</sub> at platinum electrodes requires a high anodic potential (+0.65 V vs Ag/AgCl), at which endogenous reducing agents (ascorbic acid, uric acid, and acetaminophen) undergo direct electro-oxidation, generating substantial false-positive current. To eliminate interference, researchers engineered an electrode modified with Prussian Blue (PB, ferric hexacyanoferrate), an electrocatalytic mediator that reduces H<sub>2</sub>O<sub>2</sub> to water at low potential (Reaction 2):</p>
<p style="text-align:center;font-style:italic">H<sub>2</sub>O<sub>2</sub> + 2 H<sup>+</sup> + 2 e<sup>&minus;</sup> &rarr; 2 H<sub>2</sub>O &nbsp;&nbsp;&nbsp;&nbsp;(Reaction 2)</p>
<p>The biosensor was tested in an electrochemical cell using a three-electrode setup (PB/LOx glassy carbon working electrode, Ag/AgCl reference electrode, Pt wire counter electrode) in 0.10 M phosphate-buffered saline (pH 7.4) at 298 K.</p>
<table>
<tr><th>Applied Potential (V vs Ag/AgCl)</th><th>Lactate Sensitivity (&mu;A&middot;mM<sup>&minus;1</sup>&middot;cm<sup>&minus;2</sup>)</th><th>Current from 0.1 mM Ascorbic Acid (&mu;A)</th><th>Current from 0.1 mM Uric Acid (&mu;A)</th><th>Limit of Detection (mM)</th></tr>
<tr><td class="n">+0.65</td><td class="n">14.2</td><td class="n">8.60</td><td class="n">4.20</td><td class="n">0.25</td></tr>
<tr><td class="n">+0.30</td><td class="n">11.8</td><td class="n">2.10</td><td class="n">0.95</td><td class="n">0.12</td></tr>
<tr><td class="n">+0.05</td><td class="n">10.5</td><td class="n">&lt;0.02</td><td class="n">&lt;0.01</td><td class="n">0.02</td></tr>
<tr><td class="n">&minus;0.15</td><td class="n">6.1</td><td class="n">&lt;0.01</td><td class="n">&lt;0.01</td><td class="n">0.08</td></tr>
</table>
<p class="cap"><b>Table 1</b> Biosensor response parameters and interferent currents as a function of working electrode potential.</p>"""

cp_p5_qs = [
    {
        "q": "Based on Table 1, why does operating the working electrode at +0.05 V vs Ag/AgCl provide superior analytical performance compared to +0.65 V?",
        "ch": [
            "It increases lactate sensitivity by accelerating the turnover rate of LOx.",
            "It shifts the thermodynamic reduction potential of hydrogen peroxide to a more negative value.",
            "It suppresses electro-oxidation of ascorbic acid and uric acid below their respective oxidation thresholds while preserving catalytic H<sub>2</sub>O<sub>2</sub> reduction.",
            "It prevents dissolved oxygen from participating in the enzymatic reaction."
        ],
        "a": 2,
        "e": "<strong>Electrochemical selectivity via potential window:</strong> Ascorbic acid (oxidation potential ~ +0.35&ndash;0.40 V) and uric acid (~ +0.30&ndash;0.35 V) require potentials above +0.30 V to be oxidized. At +0.05 V, the electrode is thermodynamically incapable of driving their oxidation, virtually eliminating interferent current (<0.02 &mu;A vs 8.60 &mu;A at +0.65 V), thereby achieving high selectivity and a low detection limit (0.02 mM)."
    },
    {
        "q": "In Reaction 1, the conversion of L-lactate (CH<sub>3</sub>CH(OH)COO<sup>&minus;</sup>) to pyruvate (CH<sub>3</sub>COCOO<sup>&minus;</sup>) represents:",
        "ch": [
            "a 2-electron oxidation in which the &alpha;-carbon oxidation state increases from 0 to +2.",
            "a 2-electron reduction in which the &alpha;-carbon oxidation state decreases from +2 to 0.",
            "a decarboxylation reaction yielding a one-carbon homologue.",
            "a disproportionation reaction involving no net electron transfer."
        ],
        "a": 0,
        "e": "<strong>Oxidation state calculation for carbon:</strong> In lactate, the C2 (&alpha;-carbon) is bonded to H (&minus;1), OH (+1), COO<sup>&minus;</sup> (+1), and CH<sub>3</sub> (0); net oxidation state = 0. In pyruvate, C2 is double-bonded to =O (+2), and bonded to COO<sup>&minus;</sup> (+1) and CH<sub>3</sub> (0); net oxidation state = +2. The carbon loses two electrons (0 &rarr; +2), which are transferred via FAD to O<sub>2</sub> to generate H<sub>2</sub>O<sub>2</sub>. Thus, it is a 2-electron oxidation."
    },
    {
        "q": "If the biosensor operates at a steady-state cathodic current of 9.65 &mu;A for 100 seconds during H<sub>2</sub>O<sub>2</sub> reduction, how many moles of electrons are transferred across the working electrode? (Faraday's constant <i>F</i> &asymp; 96,500 C/mol).",
        "ch": [
            "1.0 &times; 10<sup>&minus;8</sup> mol",
            "2.0 &times; 10<sup>&minus;8</sup> mol",
            "1.0 &times; 10<sup>&minus;5</sup> mol",
            "9.65 &times; 10<sup>&minus;4</sup> mol"
        ],
        "a": 0,
        "e": "<strong>Apply Faraday's law of electrolysis:</strong><br>Total charge <i>Q</i> = <i>I</i> &times; <i>t</i> = (9.65 &times; 10<sup>&minus;6</sup> A) &times; (100 s) = 9.65 &times; 10<sup>&minus;4</sup> C.<br>Moles of electrons = <i>Q</i> / <i>F</i> = (9.65 &times; 10<sup>&minus;4</sup> C) / (96,500 C/mol) = 1.0 &times; 10<sup>&minus;8</sup> mol."
    },
    {
        "q": "For an electrochemical cell with a standard cell potential <i>E</i>&deg;<sub>cell</sub> = +0.34 V involving a 2-electron transfer at 298 K, what is the standard Gibbs free energy change &Delta;<i>G</i>&deg;? (<i>F</i> = 96,500 C/mol).",
        "ch": [
            "+65.6 kJ/mol",
            "&minus;65.6 kJ/mol",
            "&minus;32.8 kJ/mol",
            "+32.8 kJ/mol"
        ],
        "a": 1,
        "e": "<strong>Use &Delta;G&deg; = &minus;nFE&deg;<sub>cell</sub>:</strong><br>&Delta;<i>G</i>&deg; = &minus;(2 mol e<sup>&minus;</sup>) &times; (96,500 C/mol) &times; (+0.34 V) = &minus;65,620 J/mol = &minus;65.6 kJ/mol. A positive cell potential corresponds to a spontaneous process with a negative &Delta;<i>G</i>&deg;."
    },
    {
        "q": "According to the Nernst equation (<i>E</i> = <i>E</i>&deg; &minus; (0.0592 / <i>n</i>) log <i>Q</i> at 298 K), how does an increase in the local concentration of H<sub>2</sub>O<sub>2</sub> affect the reduction potential for Reaction 2?",
        "ch": [
            "It decreases the reduction potential because H<sub>2</sub>O<sub>2</sub> is a product.",
            "It increases the reduction potential because H<sub>2</sub>O<sub>2</sub> is a reactant, shifting the reaction quotient Q to a smaller value.",
            "It has no effect because standard reduction potentials are intensive properties.",
            "It shifts the reaction quotient Q to a value greater than 1, reducing the cell potential."
        ],
        "a": 1,
        "e": "<strong>Nernst equation for a reduction half-reaction:</strong> For H<sub>2</sub>O<sub>2</sub> + 2 H<sup>+</sup> + 2 e<sup>&minus;</sup> &rarr; 2 H<sub>2</sub>O, the reaction quotient is <i>Q</i> = 1 / ([H<sub>2</sub>O<sub>2</sub>][H<sup>+</sup>]<sup>2</sup>). Increasing [H<sub>2</sub>O<sub>2</sub>] increases the denominator, thereby decreasing <i>Q</i>. Because &minus;log(<i>Q</i>) becomes more positive, <i>E</i> increases. Thermodynamically, adding reactant increases the driving force for reduction."
    }
]

cp_p5 = {
    "id": "exam_cp60_p5",
    "sec": "C/P",
    "topic": "Electrochemistry, Nernst potentials, and amperometric biosensors",
    "sheet": 16,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60",
    "passage": cp_p5_html,
    "qs": cp_p5_qs
}

# CP Discretes (Q28-Q32, 5 Qs)
cp_discretes = [
    {
        "q": "An optometrist prescribes a thin converging lens with a focal length of +20 cm to correct a patient's vision. If an object is placed 30 cm in front of this lens, where is the image formed, and what are its characteristics?",
        "d": True,
        "ch": [
            "12 cm in front of the lens; virtual and upright",
            "60 cm behind the lens; real and inverted",
            "60 cm in front of the lens; virtual and inverted",
            "15 cm behind the lens; real and upright"
        ],
        "a": 1,
        "e": "<strong>Thin lens equation: 1/f = 1/d<sub>o</sub> + 1/d<sub>i</sub>.</strong><br>1/d<sub>i</sub> = 1/f &minus; 1/d<sub>o</sub> = 1/20 &minus; 1/30 = 3/60 &minus; 2/60 = 1/60 cm<sup>&minus;1</sup> &rArr; d<sub>i</sub> = +60 cm.<br>A positive image distance indicates a real image formed on the opposite side (behind the lens). Magnification <i>m</i> = &minus;d<sub>i</sub> / d<sub>o</sub> = &minus;60 / 30 = &minus;2.0. The negative sign denotes an inverted image."
    },
    {
        "q": "A 12 V DC power supply is connected to a circuit containing a 4.0 &Omega; resistor connected in series with a parallel combination of two 6.0 &Omega; resistors. What is the total electric current supplied by the power source?",
        "d": True,
        "ch": [
            "1.2 A",
            "1.7 A",
            "2.4 A",
            "3.0 A"
        ],
        "a": 1,
        "e": "<strong>Calculate equivalent resistance:</strong><br>The two 6.0 &Omega; resistors in parallel have equivalent resistance <i>R</i><sub>p</sub> = (6.0 &times; 6.0) / (6.0 + 6.0) = 36 / 12 = 3.0 &Omega;.<br>The total resistance of the circuit is <i>R</i><sub>eq</sub> = <i>R</i><sub>series</sub> + <i>R</i><sub>p</sub> = 4.0 &Omega; + 3.0 &Omega; = 7.0 &Omega;.<br>By Ohm's Law: <i>I</i> = <i>V</i> / <i>R</i><sub>eq</sub> = 12 V / 7.0 &Omega; &asymp; 1.71 A &asymp; 1.7 A."
    },
    {
        "q": "Across Period 3 of the periodic table, from sodium (Na) to chlorine (Cl), the first ionization energy generally increases. What is the primary physical cause of this periodic trend?",
        "d": True,
        "ch": [
            "An increase in the principal quantum number n of the valence shell",
            "An increase in effective nuclear charge (Z<sub>eff</sub>) while core electron shielding remains relatively constant",
            "A decrease in the total number of protons in the atomic nucleus",
            "Enhanced electron-electron repulsion among electrons occupying identical subshells"
        ],
        "a": 1,
        "e": "<strong>Effective nuclear charge increases across a period:</strong> Across Period 3, protons are added to the nucleus (+1 for each step from Na to Cl) while valence electrons are added to the same <i>n</i> = 3 principal energy shell. The inner-shell core electrons ([Ne] core) remain constant at 10 electrons, providing roughly constant shielding. Consequently, <i>Z</i><sub>eff</sub> increases significantly (from &asymp; +1 in Na to &asymp; +7 in Cl), pulling valence electrons closer to the nucleus and requiring greater energy to ionize."
    },
    {
        "q": "A rigid 2.0 L sealed container at 300 K contains a gaseous mixture of 0.50 mol O<sub>2</sub>(g) and 1.50 mol N<sub>2</sub>(g). If the total pressure in the vessel is 24 atm, what is the partial pressure of O<sub>2</sub>?",
        "d": True,
        "ch": [
            "4.0 atm",
            "6.0 atm",
            "8.0 atm",
            "18.0 atm"
        ],
        "a": 1,
        "e": "<strong>Dalton's Law of partial pressures: P<sub>i</sub> = &chi;<sub>i</sub> &times; P<sub>total</sub>.</strong><br>Total moles of gas = 0.50 mol + 1.50 mol = 2.00 mol.<br>Mole fraction of oxygen &chi;(O<sub>2</sub>) = 0.50 / 2.00 = 0.25.<br>Partial pressure <i>P</i>(O<sub>2</sub>) = 0.25 &times; 24 atm = 6.0 atm."
    },
    {
        "q": "A 10 kg medical supply box is pushed up a frictionless ramp inclined at 30&deg; to the horizontal. If the box is moved a distance of 4.0 m along the ramp surface at constant speed, what is the total mechanical work performed against gravity? (Use <i>g</i> = 9.8 m/s<sup>2</sup>).",
        "d": True,
        "ch": [
            "98 J",
            "196 J",
            "339 J",
            "392 J"
        ],
        "a": 1,
        "e": "<strong>Work against gravity depends solely on vertical height: W = mgh.</strong><br>Vertical height <i>h</i> = <i>d</i> &times; sin(&theta;) = 4.0 m &times; sin(30&deg;) = 4.0 m &times; 0.50 = 2.0 m.<br><i>W</i> = <i>m</i> &times; <i>g</i> &times; <i>h</i> = (10 kg) &times; (9.8 m/s<sup>2</sup>) &times; (2.0 m) = 196 J.<br>Choice D (392 J) is the trap of multiplying force by ramp length without accounting for the 30&deg; angle."
    }
]

cp_disc = {
    "id": "exam_cp60_disc",
    "sec": "C/P",
    "topic": "C/P Standalone Discrete Questions",
    "sheet": None,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60",
    "passage": "",
    "qs": cp_discretes
}

EXAM_CP60 = [cp_p1, cp_p2, cp_p3, cp_p4, cp_p5, cp_disc]
print("EXAM_CP60 constructed! Total Qs:", sum(len(s["qs"]) for s in EXAM_CP60))

