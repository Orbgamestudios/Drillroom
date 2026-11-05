import json

# Passage 1: Acid-Base & Carbonic Anhydrase Kinetics
p1_html = """<div class="ttl">Passage 1 (Questions 1&ndash;6)</div>
<p>Carbonic anhydrases (CAs) are zinc metalloenzymes that catalyze the reversible hydration of carbon dioxide: CO<sub>2</sub> + H<sub>2</sub>O &rightleftharpoons; HCO<sub>3</sub><sup>&minus;</sup> + H<sup>+</sup>. In erythrocytes, CA II operates near the diffusion-controlled limit with a turnover number (<i>k</i><sub>cat</sub>) of 1.4 &times; 10<sup>6</sup> s<sup>&minus;1</sup>. The active site features a Zn<sup>2+</sup> ion coordinated tetrahedrally by three histidine imidazoles (His94, His96, His119) and a bound water molecule or hydroxide ion.</p>
<p>The catalytic mechanism involves two distinct stages: (1) nucleophilic attack of the zinc-bound hydroxide on CO<sub>2</sub> to form bicarbonate, which is subsequently displaced by a water molecule; and (2) regeneration of the active zinc-bound hydroxide via proton transfer to bulk solvent through a proton-shuttle residue, His64 (p<i>K</i><sub>a</sub> &asymp; 7.1).</p>
<p>To characterize the thermodynamic and kinetic barriers of CA II variants, investigators synthesized mutant enzymes altering His64 and His94. Catalytic activity was measured at 298 K in 50 mM HEPES buffer across a pH range of 6.0 to 8.5. Acetazolamide (AZA), a sulfonamide inhibitor, was titrated against each variant to determine the inhibition constant (<i>K</i><sub>i</sub>). Dissociation constants for Zn<sup>2+</sup> binding (<i>K</i><sub>d,Zn</sub>) were also quantified via isothermal titration calorimetry.</p>
<table>
<tr><th>Enzyme Variant</th><th><i>k</i><sub>cat</sub> (s<sup>&minus;1</sup>)</th><th><i>K</i><sub>m</sub> for CO<sub>2</sub> (mM)</th><th><i>k</i><sub>cat</sub> / <i>K</i><sub>m</sub> (M<sup>&minus;1</sup>s<sup>&minus;1</sup>)</th><th><i>K</i><sub>i</sub> for AZA (nM)</th><th><i>K</i><sub>d,Zn</sub> (pM)</th></tr>
<tr><td>Wild-Type (WT)</td><td class="n">1.4 &times; 10<sup>6</sup></td><td class="n">12.0</td><td class="n">1.2 &times; 10<sup>8</sup></td><td class="n">10</td><td class="n">4.0</td></tr>
<tr><td>H64A</td><td class="n">1.1 &times; 10<sup>4</sup></td><td class="n">12.5</td><td class="n">8.8 &times; 10<sup>5</sup></td><td class="n">12</td><td class="n">4.2</td></tr>
<tr><td>H94A</td><td class="n">2.3 &times; 10<sup>2</sup></td><td class="n">110.0</td><td class="n">2.1 &times; 10<sup>3</sup></td><td class="n">4500</td><td class="n">3.8 &times; 10<sup>5</sup></td></tr>
<tr><td>H64E</td><td class="n">3.5 &times; 10<sup>5</sup></td><td class="n">11.8</td><td class="n">3.0 &times; 10<sup>7</sup></td><td class="n">11</td><td class="n">4.1</td></tr>
</table>
<p class="cap"><b>Table 1</b> Kinetic and thermodynamic parameters for CA II variants at pH 7.4, 298 K.</p>"""

p1_qs = [
    {
        "q": "Based on Table 1, which catalytic step is most severely rate-limiting in the H64A variant compared to the wild-type enzyme?",
        "ch": [
            "Nucleophilic attack of the zinc-bound hydroxide on dissolved CO₂",
            "Displacement of coordinated bicarbonate by an incoming water molecule",
            "Intermolecular proton transfer from the zinc-bound water to bulk solvent",
            "Initial substrate binding of carbon dioxide into the hydrophobic pocket"
        ],
        "a": 2,
        "e": "<strong>His64 functions as the intramolecular proton shuttle.</strong> Mutating His64 to alanine (H64A) removes the imidazole proton acceptor/donor, causing <em>k</em><sub>cat</sub> to plummet by over two orders of magnitude (1.4 &times; 10<sup>6</sup> &rarr; 1.1 &times; 10<sup>4</sup> s<sup>&minus;1</sup>) while <em>K</em><sub>m</sub> remains essentially unchanged (12.0 &rarr; 12.5 mM). This selective ablation of catalytic turnover without disrupting substrate affinity indicates that the proton transfer step (regenerating Zn-OH<sup>&minus;</sup>) is the bottleneck."
    },
    {
        "q": "The zinc ion in carbonic anhydrase acts as a Lewis acid by:",
        "ch": [
            "donating an electron pair to the oxygen of water, lowering its pKa.",
            "accepting electron density from coordinated water, lowering its pKa from 14 to approximately 7.",
            "stabilizing the conjugate acid of bicarbonate via hydrogen bonding.",
            "oxidizing coordinated water to produce molecular oxygen and protons."
        ],
        "a": 1,
        "e": "<strong>Lewis acids are electron pair acceptors.</strong> The divalent Zn<sup>2+</sup> ion coordinates the lone pair on water's oxygen, polarizing the O&minus;H bond and stabilizing the resulting hydroxide ion. This dramatically depresses the p<em>K</em><sub>a</sub> of water from 15.7 (in bulk solution) down to ~7.0, enabling the formation of nucleophilic OH<sup>&minus;</sup> at physiological pH."
    },
    {
        "q": "If an untreated patient with severe respiratory acidosis has an arterial blood pH of 7.10 and a PCO<sub>2</sub> of 80 mmHg (dissolved [CO<sub>2</sub>] = 2.4 mM), what is the patient's plasma [HCO<sub>3</sub><sup>&minus;</sup>]? (Note: p<em>K</em><sub>a</sub> of the carbonic acid/bicarbonate system is 6.10, and log(10) = 1.0).",
        "ch": [
            "12 mM",
            "24 mM",
            "48 mM",
            "2.4 mM"
        ],
        "a": 1,
        "e": "<strong>Apply Henderson-Hasselbalch:</strong> pH = p<em>K</em><sub>a</sub> + log([HCO<sub>3</sub><sup>&minus;</sup>] / [CO<sub>2</sub>]).<br>7.10 = 6.10 + log([HCO<sub>3</sub><sup>&minus;</sup>] / 2.4 mM)<br>1.00 = log([HCO<sub>3</sub><sup>&minus;</sup>] / 2.4 mM)<br>10<sup>1.0</sup> = [HCO<sub>3</sub><sup>&minus;</sup>] / 2.4 mM &rArr; [HCO<sub>3</sub><sup>&minus;</sup>] = 2.4 &times; 10 = 24 mM."
    },
    {
        "q": "Why does the H94A mutation exhibit a 10<sup>5</sup>-fold increase in <em>K</em><sub>d,Zn</sub> and a 450-fold increase in <em>K</em><sub>i</sub> for acetazolamide, whereas H64A exhibits virtually no change in these parameters?",
        "ch": [
            "His94 directly coordinates the catalytic Zn²⁺ in the active site, whereas His64 resides on the surface.",
            "His64 is buried within the hydrophobic core, shielding the zinc ion from solvation.",
            "Acetazolamide acts as an uncompetitive inhibitor that binds exclusively to the His64-CO₂ complex.",
            "His94 undergoes phosphorylation during the catalytic cycle to maintain zinc coordination."
        ],
        "a": 0,
        "e": "<strong>His94 is a primary coordinating ligand for the central Zn<sup>2+</sup> ion.</strong> Replacing His94 with alanine eliminates one of the three histidine-imidazole coordination bonds, destabilizing the zinc coordination sphere (so <em>K</em><sub>d,Zn</sub> jumps to 3.8 &times; 10<sup>5</sup> pM). Because acetazolamide binds directly to the catalytic zinc atom, disrupting the zinc coordination geometry severely impairs inhibitor binding (<em>K</em><sub>i</sub> rises to 4500 nM). In contrast, His64 is a peripheral proton shuttle residue not involved in zinc chelation."
    },
    {
        "q": "At pH 8.1, what fraction of the wild-type His64 side chain (p<em>K</em><sub>a</sub> = 7.1) exists in its neutral (deprotonated imidazole) form?",
        "ch": [
            "10%",
            "50%",
            "90%",
            "99%"
        ],
        "a": 2,
        "e": "<strong>Use the Henderson-Hasselbalch ratio:</strong><br>pH &minus; p<em>K</em><sub>a</sub> = 8.1 &minus; 7.1 = 1.0.<br>log([Base]/[Acid]) = 1.0 &rArr; [Base]/[Acid] = 10/1.<br>Fraction deprotonated = [Base] / ([Base] + [Acid]) = 10 / (10 + 1) = 10/11 &asymp; 90.9% (approximately 90%)."
    },
    {
        "q": "A researcher bubbles pure <sup>18</sup>O-labeled CO<sub>2</sub> (C<sup>18</sup>O<sub>2</sub>) into an aqueous solution containing CA II and H<sub>2</sub><sup>16</sup>O. After one single catalytic turnover, the inorganic bicarbonate formed will contain:",
        "ch": [
            "three ¹⁸O atoms.",
            "two ¹⁸O atoms and one ¹⁶O atom.",
            "one ¹⁸O atom and two ¹⁶O atoms.",
            "three ¹⁶O atoms."
        ],
        "a": 1,
        "e": "<strong>Trace the oxygen atoms through the mechanism:</strong> C<sup>18</sup>O<sub>2</sub> has two <sup>18</sup>O atoms. The nucleophilic zinc-bound hydroxide is derived from solvent water (H<sub>2</sub><sup>16</sup>O), contributing a single <sup>16</sup>O atom. Nucleophilic addition of [Zn-<sup>16</sup>OH]<sup>&minus;</sup> across C=<sup>18</sup>O yields bicarbonate containing two <sup>18</sup>O atoms and one <sup>16</sup>O atom (HC<sup>18</sup>O<sub>2</sub><sup>16</sup>O<sup>&minus;</sup>)."
    }
]

# Passage 2: Fluid Dynamics & Doppler Ultrasound in Stenosis
p2_html = """<div class="ttl">Passage 2 (Questions 7&ndash;12)</div>
<p>Intravascular ultrasound (IVUS) and pulsed-wave Doppler velocimetry are diagnostic modalities used to assess atherosclerotic lesions and arterial stenoses. Blood is modeled as an incompressible, non-Newtonian suspension, but within large conducting arteries (e.g., the femoral artery, internal diameter <i>D</i><sub>0</sub> = 6.0 mm), laminar flow can be approximated by Poiseuille's law and the continuity equation: <i>A</i><sub>1</sub><i>v</i><sub>1</sub> = <i>A</i><sub>2</sub><i>v</i><sub>2</sub>.</p>
<p>An ultrasound transducer emitting acoustic waves at carrier frequency <i>f</i><sub>0</sub> = 5.0 MHz is oriented at an Doppler insonation angle &theta; = 60&deg; relative to the longitudinal vector of blood flow. The Doppler frequency shift &Delta;<i>f</i> is given by:</p>
<p style="text-align:center;font-style:italic">&Delta;f = (2 &middot; f<sub>0</sub> &middot; v &middot; cos &theta;) / c</p>
<p>where <i>v</i> is the flow velocity and <i>c</i> is the acoustic velocity in soft tissue (<i>c</i> = 1540 m/s). Note: cos(60&deg;) = 0.50.</p>
<p>Investigators tested an in vitro vascular phantom under steady pulsatile pressure (mean perfusion pressure &Delta;<i>P</i> = 100 mmHg &asymp; 13.3 kPa). A rigid axisymmetric constriction was introduced, reducing vessel luminal diameter across three test sections. Fluid density &rho; = 1.06 &times; 10<sup>3</sup> kg/m<sup>3</sup>, and dynamic viscosity &eta; = 3.5 &times; 10<sup>&minus;3</sup> Pa&middot;s. Turbulence occurs when the Reynolds number <i>Re</i> = (&rho; &middot; <i>v</i> &middot; <i>D</i>) / &eta; exceeds the critical threshold <i>Re</i><sub>crit</sub> &asymp; 2000.</p>
<table>
<tr><th>Vessel Segment</th><th>Luminal Diameter <i>D</i> (mm)</th><th>Cross-Sectional Area (mm<sup>2</sup>)</th><th>Doppler Shift &Delta;<i>f</i> (kHz)</th><th>Calculated Velocity <i>v</i> (m/s)</th><th>Reynolds Number (<i>Re</i>)</th></tr>
<tr><td>Proximal (Baseline)</td><td class="n">6.0</td><td class="n">28.3</td><td class="n">1.62</td><td class="n">0.50</td><td class="n">909</td></tr>
<tr><td>Moderate Stenosis</td><td class="n">3.0</td><td class="n">7.1</td><td class="n">6.49</td><td class="n">2.00</td><td class="n">1817</td></tr>
<tr><td>Severe Stenosis</td><td class="n">1.5</td><td class="n">1.8</td><td class="n">25.97</td><td class="n">8.00</td><td class="n">3634</td></tr>
</table>
<p class="cap"><b>Table 1</b> Hemodynamic parameters recorded in arterial phantom sections.</p>"""

p2_qs = [
    {
        "q": "According to the data in Table 1, when the lumen diameter decreases by a factor of 4 (from 6.0 mm to 1.5 mm), the blood velocity increases by a factor of:",
        "ch": [
            "4",
            "8",
            "16",
            "64"
        ],
        "a": 2,
        "e": "<strong>Continuity equation: A₁v₁ = A₂v₂.</strong> Cross-sectional area is proportional to the square of diameter: A &prop; D<sup>2</sup>. Decreasing diameter by a factor of 4 reduces area by 4<sup>2</sup> = 16. To conserve volumetric flux (Q = Av), velocity must increase 16-fold (0.50 m/s &times; 16 = 8.00 m/s)."
    },
    {
        "q": "Based on Bernoulli's principle, how does the hydrostatic pressure in the severe stenosis compare to that in the proximal baseline segment (assuming horizontal flow)?",
        "ch": [
            "The pressure is significantly higher in the severe stenosis due to the immense kinetic friction.",
            "The pressure is significantly lower in the severe stenosis due to the dramatic increase in fluid velocity.",
            "The pressure remains identical because volumetric flow rate is strictly conserved.",
            "The pressure in the stenosis drops to zero absolute atmospheres under all circumstances."
        ],
        "a": 1,
        "e": "<strong>The Venturi effect (Bernoulli's principle):</strong> P₁ + &frac12;&rho;v₁² = P₂ + &frac12;&rho;v₂². As blood accelerates through the constriction from 0.50 m/s to 8.00 m/s, kinetic energy density (&frac12;&rho;v²) surges by 8.0² / 0.5² = 256-fold. To conserve mechanical energy in streamline flow, static lateral pressure P must experience a sharp drop."
    },
    {
        "q": "What is the pressure drop &Delta;P<sub>dyn</sub> attributable solely to the change in kinetic energy density between the proximal baseline segment (v₁ = 0.50 m/s) and the severe stenosis (v₂ = 8.00 m/s)?",
        "ch": [
            "3.37 &times; 10⁴ Pa",
            "6.75 &times; 10⁴ Pa",
            "1.06 &times; 10³ Pa",
            "4.24 &times; 10⁵ Pa"
        ],
        "a": 0,
        "e": "<strong>Calculate &Delta;P = &frac12;&rho;(v₂² &minus; v₁²):</strong><br>&Delta;P = 0.5 &times; (1.06 &times; 10<sup>3</sup> kg/m<sup>3</sup>) &times; [(8.0)<sup>2</sup> &minus; (0.5)<sup>2</sup>]<br>= 530 &times; (64 &minus; 0.25) = 530 &times; 63.75 &asymp; 33,788 Pa &asymp; 3.38 &times; 10<sup>4</sup> Pa."
    },
    {
        "q": "In the severe stenosis segment, flow is expected to exhibit post-stenotic turbulence primarily because:",
        "ch": [
            "the fluid density decreases as velocity increases.",
            "the Reynolds number (3634) exceeds the critical transition value of ~2000.",
            "the acoustic velocity in tissue drops below 1540 m/s.",
            "the dynamic viscosity &eta; increases proportionally with shear rate."
        ],
        "a": 1,
        "e": "<strong>Turbulence is predicted by the Reynolds number:</strong> Re = (&rho;vD)/&eta;. The table lists Re = 3634 in the severe stenosis. Because this exceeds Re<sub>crit</sub> &asymp; 2000, inertial forces overwhelm viscous damping forces, producing chaotic eddy currents and turbulent flow."
    },
    {
        "q": "If the ultrasound sonographer tilts the probe such that the insonation angle &theta; increases from 60&deg; to 90&deg;, what Doppler shift frequency &Delta;f will be recorded?",
        "ch": [
            "0 kHz",
            "1.62 kHz",
            "3.24 kHz",
            "Infinite frequency"
        ],
        "a": 0,
        "e": "<strong>Doppler equation contains cos &theta;:</strong> At &theta; = 90&deg;, the ultrasound beam is perpendicular to the vector of blood motion. Because cos(90&deg;) = 0, &Delta;f = (2 f₀ v cos 90&deg;) / c = 0 kHz. No frequency shift can be detected when transmitting at a right angle to particle displacement."
    },
    {
        "q": "If a rigid vessel segment obeyed Poiseuille's law strictly during laminar flow with a fixed pressure gradient &Delta;P, reducing the luminal radius to 1/2 of its initial value would decrease the volumetric flow rate Q by a factor of:",
        "ch": [
            "2",
            "4",
            "8",
            "16"
        ],
        "a": 3,
        "e": "<strong>Poiseuille's equation states Q = (&pi; &Delta;P r⁴) / (8 &eta; L).</strong> Hydraulic resistance R varies inversely with the fourth power of radius (R &prop; 1/r⁴). Halving r multiplies resistance by (2)⁴ = 16, decreasing volumetric flow rate Q by a factor of 16."
    }
]

print("Building CP90 sets...")

# Passage 3: Multi-step organic synthesis of a kinase inhibitor
p3_html = """<div class="ttl">Passage 3 (Questions 13&ndash;18)</div>
<p>Receptor tyrosine kinases (RTKs) are frequently mutated or overexpressed in solid tumors. Chemists designed Compound <b>5</b>, a potent small-molecule competitive inhibitor targeting the ATP-binding pocket of an oncogenic RTK. The convergent synthetic route is outlined in Scheme 1.</p>
<p style="text-align:center;font-family:monospace;background:#F7F9FB;padding:8px;border:1px solid #D0D7DE;font-size:13px">
Compound 1 (4-chloropyrimidine-2-amine) + Compound 2 (4-(morpholinomethyl)aniline)<br>
&darr; <i>iPr₂NEt, n-BuOH, 110 &deg;C (Yield: 84%)</i><br>
Intermediate 3 &rarr; bromination (NBS, DMF, 0 &deg;C) &rarr; Intermediate 4<br>
&darr; <i>Suzuki-Miyaura coupling: PhB(OH)₂, Pd(PPh₃)₄, K₂CO₃, 1,4-dioxane/H₂O, 90 &deg;C (Yield: 76%)</i><br>
Target Compound 5
</p>
<p>In Step 1, nucleophilic aromatic substitution (S<sub>N</sub>Ar) of Compound <b>1</b> by the primary aromatic amine of Compound <b>2</b> occurs selectively at the 4-position rather than the 2-amino position. Reaction monitoring by proton nuclear magnetic resonance (<sup>1</sup>H-NMR) and Fourier-transform infrared (FT-IR) spectroscopy showed the disappearance of the primary amine stretch at 3450 cm<sup>&minus;1</sup> and the emergence of a broad secondary amine stretch at 3310 cm<sup>&minus;1</sup>.</p>
<p>To verify the stereochemical purity and solution conformation, optical rotation was measured on a polarimeter ([&alpha;]<sub>D</sub><sup>25</sup> = 0.00&deg; for all synthetic intermediates). In vitro inhibition assays against wild-type RTK and the gatekeeper mutant (T790M) yielded the IC<sub>50</sub> values in Table 1.</p>
<table>
<tr><th>Inhibitor</th><th>RTK WT IC<sub>50</sub> (nM)</th><th>RTK T790M IC<sub>50</sub> (nM)</th><th>Log <i>P</i> (octanol/water)</th><th>Polar Surface Area (&Aring;<sup>2</sup>)</th></tr>
<tr><td>Compound 5</td><td class="n">4.2</td><td class="n">8.6</td><td class="n">2.4</td><td class="n">68.5</td></tr>
<tr><td>Analog 5a (morpholine &rarr; piperidine)</td><td class="n">3.8</td><td class="n">9.1</td><td class="n">3.5</td><td class="n">59.3</td></tr>
<tr><td>Analog 5b (des-phenyl)</td><td class="n">420.0</td><td class="n">1150.0</td><td class="n">1.6</td><td class="n">68.5</td></tr>
</table>
<p class="cap"><b>Table 1</b> Pharmacological profile and physicochemical metrics of Compound 5 and analogs.</p>"""

p3_qs = [
    {
        "q": "The nucleophilic aromatic substitution (S<sub>N</sub>Ar) in Step 1 proceeds via which characteristic intermediate?",
        "ch": [
            "A planar aryl carbocation generated by loss of chloride ion",
            "A resonance-stabilized Meisenheimer complex carrying a formal negative charge in the ring",
            "A highly strained cyclic benzyne intermediate formed via elimination",
            "A free-radical aryl intermediate stabilized by diisopropylethylamine"
        ],
        "a": 1,
        "e": "<strong>S<sub>N</sub>Ar proceeds via an addition-elimination pathway through a Meisenheimer complex.</strong> Attack of the nucleophile (the aniline amino group) onto the electron-deficient chloropyrimidine ring adds electron density into the heteroaromatic system, forming a resonance-delocalized anionic intermediate (Meisenheimer complex). Subsequent elimination of the chloride leaving group restores heteroaromaticity."
    },
    {
        "q": "Which feature of the infrared spectrum uniquely confirms that Compound 2 successfully coupled to Compound 1 via its aniline nitrogen rather than the morpholine ring?",
        "ch": [
            "Appearance of a sharp carbonyl stretch at 1715 cm⁻¹",
            "Shift from a two-peak primary amine N–H doublet (3450 and 3350 cm⁻¹) to a single secondary amine N–H stretch at 3310 cm⁻¹",
            "Disappearance of the aliphatic C–H stretching bands at 2850–2950 cm⁻¹",
            "Appearance of a broad hydroxyl O–H stretch centered at 3200 cm⁻¹"
        ],
        "a": 1,
        "e": "<strong>Primary amines display two N–H stretching peaks; secondary amines display one.</strong> The primary aniline NH₂ group shows symmetric and asymmetric N–H stretching modes (~3450 and 3350 cm⁻¹). When it attacks the pyrimidine ring, it converts into a secondary amine (Ar–NH–Ar), which has only one N–H bond and produces a single stretching band at ~3310 cm⁻¹. The morpholine tertiary nitrogen has no N–H bonds."
    },
    {
        "q": "Why is the observed specific optical rotation [&alpha;]<sub>D</sub><sup>25</sup> equal to 0.00&deg; for Compound 5?",
        "ch": [
            "Compound 5 contains an equal equimolar mixture of diasteromeric atropisomers that cancel optical rotation.",
            "Compound 5 possesses no chiral centers and exists as an achiral structure with an internal plane of symmetry or plane of reflection.",
            "The solvent (dimethyl sulfoxide) undergoes mutarotation that suppresses optical activity.",
            "The morpholine nitrogen undergoes rapid inversion, converting a meso compound into a racemate."
        ],
        "a": 1,
        "e": "<strong>Compound 5 is an achiral molecule.</strong> Inspection of the molecular architecture shows no stereogenic (asymmetric) carbon centers. Molecules lacking stereocenters and chiral axes cannot rotate plane-polarized light; their specific rotation is identically 0&deg;."
    },
    {
        "q": "Based on Table 1, the 100-fold loss of potency in Analog 5b (IC<sub>50</sub> = 420 nM vs 4.2 nM) indicates that the phenyl group introduced by the Suzuki reaction participates in:",
        "ch": [
            "covalent bonding with the catalytic lysine residue in the active site.",
            "hydrophobic or &pi;&ndash;&pi; stacking interactions within an adjacent pocket of the kinase ATP-binding cleft.",
            "hydrogen-bond donation to the kinase hinge-region backbone carbonyl.",
            "coordination with an essential divalent magnesium cofactor."
        ],
        "a": 1,
        "e": "<strong>The phenyl ring is a nonpolar, aromatic moiety.</strong> Deletion of the phenyl ring (Analog 5b, des-phenyl) causes a massive 100-fold reduction in inhibitory potency against WT RTK (4.2 nM &rarr; 420 nM). Because a benzene ring cannot donate hydrogen bonds or form covalent bonds, its primary binding contribution is van der Waals / hydrophobic contacts and &pi;&ndash;&pi; stacking with aromatic residues in the kinase binding pocket."
    },
    {
        "q": "In the Suzuki-Miyaura cross-coupling step, what role does the palladium catalyst Pd(PPh<sub>3</sub>)<sub>4</sub> play in terms of reaction energetics?",
        "ch": [
            "It shifts the equilibrium constant K_eq by making &Delta;G&deg; significantly more negative.",
            "It lowers the activation energy of the carbon–carbon bond-forming transition state without altering &Delta;H&deg; or &Delta;G&deg; of the reaction.",
            "It oxidizes potassium carbonate to generate reactive superoxide radical anions.",
            "It acts as a Br&oslash;nsted base to deprotonate phenylboronic acid."
        ],
        "a": 1,
        "e": "<strong>Catalysts lower activation energy (E_a) without altering thermodynamic state functions.</strong> Transition-metal catalysts like Pd(0) provide a low-barrier pathway (oxidative addition, transmetalation, reductive elimination) to forge the C&minus;C bond. They do not alter &Delta;H&deg;, &Delta;S&deg;, &Delta;G&deg;, or the equilibrium constant K<sub>eq</sub>."
    },
    {
        "q": "Analog 5a replaces the morpholine ring with a piperidine ring (replacing the ring oxygen with a CH<sub>2</sub> group). Based on Table 1, this modification results in:",
        "ch": [
            "increased lipophilicity (higher Log P) and decreased polar surface area.",
            "decreased lipophilicity (lower Log P) and increased water solubility.",
            "a decrease in oral bioavailability due to complete loss of hydrogen bond donors.",
            "a shift in the formal charge of the molecule from +1 to &minus;1 at pH 7.4."
        ],
        "a": 0,
        "e": "<strong>Replacing an electronegative oxygen atom with a methylene (CH₂) group increases hydrophobicity.</strong> Morpholine contains an ether oxygen that contributes to the polar surface area (PSA = 68.5 &Aring;²). Replacing it with a CH₂ group (piperidine) removes this polar heteroatom, lowering PSA to 59.3 &Aring;² and significantly raising the octanol/water partition coefficient from Log P = 2.4 to 3.5 (a more lipophilic compound)."
    }
]

# Passage 4: Electrochemistry & Neurochemical Biosensors
p4_html = """<div class="ttl">Passage 4 (Questions 19&ndash;24)</div>
<p>In vivo electrochemical detection of neurotransmitters utilizes carbon-fiber microelectrodes (CFMEs) coupled with fast-scan cyclic voltammetry (FSCV). Dopamine (DA), a catecholamine neurotransmitter, undergoes a quasi-reversible two-electron, two-proton oxidation to dopamine-o-quinone (DAQ) at positive potentials:</p>
<p style="text-align:center;font-style:italic">DA &rightleftharpoons; DAQ + 2 H<sup>+</sup> + 2 e<sup>&minus;</sup> &nbsp;&nbsp;&nbsp;&nbsp;(E&deg; = +0.13 V vs. Ag/AgCl)</p>
<p>The standard cell potential <i>E</i>&deg;<sub>cell</sub> and standard free energy &Delta;<i>G</i>&deg; are related by &Delta;<i>G</i>&deg; = &minus;<i>nFE</i>&deg;<sub>cell</sub>, where <i>F</i> = 96,485 C/mol e<sup>&minus;</sup>. In FSCV, the potential of the CFME working electrode is ramped linearly from a resting holding potential of &minus;0.40 V to a switching potential of +1.30 V and back to &minus;0.40 V at a scan rate of 400 V/s.</p>
<p>Ascorbic acid (AA) is present in extracellular fluid at 500-fold higher concentrations than DA (~200 &mu;M vs. ~1 &mu;M) and oxidizes at approximately +0.15 V vs. Ag/AgCl via an irreversible 2e<sup>&minus;</sup>/2H<sup>+</sup> process:</p>
<p style="text-align:center;font-style:italic">Ascorbate &rarr; Dehydroascorbate + 2 H<sup>+</sup> + 2 e<sup>&minus;</sup></p>
<p>To eliminate ascorbate interference, electrodes are coated with Nafion, a sulfonated fluoropolymer carrying fixed negative charges (SO<sub>3</sub><sup>&minus;</sup>) at physiological pH (7.4). The electroactive surface area <i>A</i> of the cylindrical CFME is 1.5 &times; 10<sup>&minus;4</sup> cm<sup>2</sup>. The peak oxidation current <i>i</i><sub>p</sub> is governed by the Randles-Sevcik equation for a diffusion-controlled reversible process: <i>i</i><sub>p</sub> = (2.69 &times; 10<sup>5</sup>) <i>n</i><sup>3/2</sup> <i>A</i> <i>D</i><sup>1/2</sup> <i>C</i> <i>v</i><sup>1/2</sup>.</p>
<table>
<tr><th>Analyte</th><th>Physiological [C] (&mu;M)</th><th>Charge at pH 7.4</th><th>Bare CFME Peak Current (&mu;A)</th><th>Nafion-Coated CFME Peak Current (&mu;A)</th></tr>
<tr><td>Dopamine (DA)</td><td class="n">1.0</td><td class="n">+1</td><td class="n">0.12</td><td class="n">0.24</td></tr>
<tr><td>Ascorbic Acid (AA)</td><td class="n">250.0</td><td class="n">&minus;1</td><td class="n">14.80</td><td class="n">0.02</td></tr>
<tr><td>3,4-Dihydroxyphenylacetic acid (DOPAC)</td><td class="n">15.0</td><td class="n">&minus;1</td><td class="n">1.10</td><td class="n">0.01</td></tr>
</table>
<p class="cap"><b>Table 1</b> Voltammetric responses of bare vs. Nafion-coated CFMEs at pH 7.4.</p>"""

p4_qs = [
    {
        "q": "What is the standard free energy change &Delta;G&deg; for the two-electron oxidation of dopamine at 298 K (E&deg; = +0.13 V vs Ag/AgCl)? (Use F &asymp; 96,500 C/mol).",
        "ch": [
            "&minus;25.1 kJ/mol",
            "+25.1 kJ/mol",
            "&minus;12.5 kJ/mol",
            "+50.2 kJ/mol"
        ],
        "a": 0,
        "e": "<strong>Use &Delta;G&deg; = &minus;nFE&deg;:</strong> n = 2 electrons, F = 96,500 C/mol, E&deg; = +0.13 V (J/C).<br>&Delta;G&deg; = &minus;(2)(96,500)(0.13) = &minus;25,090 J/mol = &minus;25.1 kJ/mol. A positive standard reduction/oxidation potential indicates a thermodynamically favorable (spontaneous) process under standard conditions."
    },
    {
        "q": "Why does coating the microelectrode with Nafion attenuate the ascorbic acid and DOPAC oxidation currents by >99% while doubling the dopamine response?",
        "ch": [
            "Nafion hydrolyzes the catechol ring of acidic neurotransmitters, converting them to unreactive esters.",
            "Nafion possesses fixed anionic sulfonate groups that electrostatically repel anions (AA and DOPAC) while preconcentrating cationic dopamine.",
            "Nafion is a hydrophobic barrier through which charged species cannot diffuse at all.",
            "Ascorbic acid oxidizes the Nafion polymer itself, forming an insulating passivating layer."
        ],
        "a": 1,
        "e": "<strong>Electrostatic exclusion and preconcentration.</strong> At physiological pH (7.4), ascorbic acid and DOPAC are carboxylate/enediolate anions (charge &minus;1). The Nafion matrix contains dense negative sulfonate groups (SO₃⁻) that electrostatically repel these anions, preventing them from contacting the carbon surface. Conversely, dopamine contains a protonated primary amine (charge +1), which is electrostatically attracted into the Nafion membrane, preconcentrating it and doubling the peak current."
    },
    {
        "q": "If the scan rate v is quadrupled from 100 V/s to 400 V/s, how will the diffusion-controlled peak oxidation current i_p change according to the Randles-Sevcik equation?",
        "ch": [
            "It will double.",
            "It will quadruple.",
            "It will increase by a factor of 16.",
            "It will remain unchanged."
        ],
        "a": 0,
        "e": "<strong>Randles-Sevcik: i_p is proportional to the square root of scan rate (v<sup>1/2</sup>).</strong> Quadrupling v (400 / 100 = 4) increases i_p by a factor of &radic;4 = 2 (it doubles)."
    },
    {
        "q": "During cyclic voltammetry, when the electrode potential is swept in the cathodic direction (from +1.30 V back toward &minus;0.40 V), what electrochemical process occurs at the electrode surface?",
        "ch": [
            "Dopamine is oxidized to dopamine-o-quinone.",
            "Dopamine-o-quinone is reduced back to dopamine by gaining two electrons.",
            "Oxygen gas is generated at the cathode via water electrolysis.",
            "Protons are reduced to hydrogen gas (H₂)."
        ],
        "a": 1,
        "e": "<strong>Cathodic sweep corresponds to reduction (electron gain).</strong> In the forward (anodic) sweep, dopamine loses two electrons to form dopamine-o-quinone (DAQ). When the potential sweeps back negatively (cathodic sweep), the DAQ molecules remaining at the electrode surface are reduced back to dopamine by accepting two electrons from the electrode."
    },
    {
        "q": "According to the Nernst equation, if the extracellular pH drops from 7.4 to 6.4 (a tenfold increase in [H<sup>+</sup>]) during ischemia, the formal reduction potential E' of the DAQ/DA redox couple will:",
        "ch": [
            "increase by approximately 59 mV, making DAQ a stronger oxidizing agent.",
            "decrease by approximately 59 mV, making DAQ a weaker oxidizing agent.",
            "increase by 120 mV, making dopamine resistant to oxidation.",
            "remain unchanged because hydrogen ions do not carry electrical current."
        ],
        "a": 0,
        "e": "<strong>Nernst equation for DAQ + 2H⁺ + 2e⁻ &rightleftharpoons; DA:</strong><br>E = E&deg; &minus; (0.0592 / n) log([DA] / ([DAQ][H⁺]²)).<br>Factoring out [H⁺]: E = E&deg;' + (0.0592 / 2) log([H⁺]²) = E&deg;' &minus; 0.0592 &times; pH.<br>Dropping pH by 1.0 unit (from 7.4 to 6.4) increases E by +0.0592 V (+59.2 mV). Higher reduction potential means DAQ is more avidly reduced (a stronger oxidizing agent)."
    },
    {
        "q": "A researcher applies a constant oxidizing potential of +0.60 V to the CFME for 10 seconds in a solution containing 10 &mu;M dopamine, generating a total charge transfer of 5.8 &times; 10<sup>&minus;8</sup> Coulombs. How many moles of dopamine were oxidized during this period? (F &asymp; 96,500 C/mol).",
        "ch": [
            "3.0 &times; 10⁻¹³ mol",
            "6.0 &times; 10⁻¹³ mol",
            "1.2 &times; 10⁻¹² mol",
            "5.8 &times; 10⁻⁸ mol"
        ],
        "a": 0,
        "e": "<strong>Faraday's Law: Q = n &times; F &times; moles.</strong><br>moles = Q / (n &times; F).<br>For dopamine oxidation, n = 2 e⁻ per molecule.<br>moles = (5.8 &times; 10⁻⁸ C) / (2 &times; 96,500 C/mol) = (5.8 &times; 10⁻⁸) / (1.93 &times; 10⁵) &asymp; 3.0 &times; 10⁻¹³ mol."
    }
]

print("Added passages 3 & 4")

# Passage 5: Thermodynamic vs. Kinetic Control in Enolate Additions
p5_html = """<div class="ttl">Passage 5 (Questions 25&ndash;30)</div>
<p>In organic synthesis, the regiochemical outcome of ketone deprotonation is dictated by the competition between kinetic and thermodynamic enolates. 2-Methylcyclohexanone contains two non-equivalent &alpha;-carbons: the less hindered secondary C6 carbon and the more hindered tertiary C2 carbon.</p>
<p>Deprotonation at C6 yields the kinetic enolate (<b>K</b>), which forms more rapidly due to lower steric hindrance in the transition state. Deprotonation at C2 yields the thermodynamic enolate (<b>T</b>), which produces a more highly substituted, more stable alkene. The reaction coordinate diagrams reveal that the activation free energy &Delta;<i>G</i><sup>&Dagger;</sup><sub>K</sub> < &Delta;<i>G</i><sup>&Dagger;</sup><sub>T</sub>, but the standard free energy of the products &Delta;<i>G</i>&deg;<sub>T</sub> < &Delta;<i>G</i>&deg;<sub>K</sub>.</p>
<p>Investigators treated 2-methylcyclohexanone with two distinct bases: lithium diisopropylamide (LDA, a bulky, strong, non-nucleophilic base, p<i>K</i><sub>a</sub> of conjugate acid &asymp; 36) and potassium <i>tert</i>-butoxide (KO<i>t</i>Bu, p<i>K</i><sub>a</sub> &asymp; 17) in various solvents and temperatures. Following enolate generation, the mixtures were quenched with chlorotrimethylsilane (TMSCl) to trap the corresponding enol ethers, and the product ratios were quantified by gas chromatography-mass spectrometry (GC-MS).</p>
<table>
<tr><th>Entry</th><th>Base</th><th>Solvent</th><th>Temperature (&deg;C)</th><th>Equilibration Time</th><th>Ratio <b>K</b> : <b>T</b> (%)</th></tr>
<tr><td>1</td><td>LDA (1.1 eq)</td><td>THF</td><td class="n">&minus;78</td><td class="n">15 min</td><td>99 : 1</td></tr>
<tr><td>2</td><td>LDA (1.1 eq)</td><td>THF</td><td class="n">25</td><td class="n">24 h</td><td>65 : 35</td></tr>
<tr><td>3</td><td>KO<i>t</i>Bu (1.1 eq)</td><td><i>t</i>BuOH</td><td class="n">25</td><td class="n">2 h</td><td>15 : 85</td></tr>
<tr><td>4</td><td>KO<i>t</i>Bu (1.1 eq)</td><td><i>t</i>BuOH</td><td class="n">80</td><td class="n">4 h</td><td>5 : 95</td></tr>
<tr><td>5</td><td>LDA (0.9 eq)</td><td>THF</td><td class="n">&minus;78</td><td class="n">3 h</td><td>70 : 30</td></tr>
</table>
<p class="cap"><b>Table 1</b> Enolate trapping experiments with 2-methylcyclohexanone.</p>"""

p5_qs = [
    {
        "q": "Why does Entry 1 (LDA, THF, &minus;78 &deg;C) yield exclusively the kinetic enolate K (99:1 ratio)?",
        "ch": [
            "At &minus;78 &deg;C, the reaction is under thermodynamic control, favoring the product with the lowest &Delta;G&deg;.",
            "The bulky diisopropylamide base deprotonates the less hindered C6 proton with a lower activation energy, and the low temperature prevents equilibration.",
            "LDA coordinates to the carbonyl oxygen, forming an irreversible covalent hemiketal complex at C2.",
            "The thermodynamic enolate is unstable at temperatures below 0 &deg;C and undergoes spontaneous ring cleavage."
        ],
        "a": 1,
        "e": "<strong>Kinetic control conditions: bulky base, low temperature, aprotic solvent.</strong> The sterically bulky LDA cannot readily access the congested tertiary &alpha;-proton at C2, so it deprotonates the more accessible secondary C6 position faster (lower E<sub>a</sub>). At &minus;78 &deg;C, insufficient thermal energy exists to overcome the reverse barrier (k<sub>&minus;1</sub> &asymp; 0), trapping the kinetically favored product K."
    },
    {
        "q": "In Entry 5, using a slight sub-stoichiometric amount of LDA (0.9 equivalents) at &minus;78 &deg;C eroded the kinetic ratio from 99:1 to 70:30. What caused this equilibration despite the low temperature?",
        "ch": [
            "Unreacted ketone (0.1 eq) acts as a proton shuttle, allowing reversible proton transfer between enolates and neutral ketone.",
            "Lithium diisopropylamide decomposes into gaseous propene and ammonia.",
            "The excess TMSCl catalyzes the retro-aldol isomerization.",
            "The kinetic enolate tautomerizes directly via an intramolecular 1,3-hydride shift."
        ],
        "a": 0,
        "e": "<strong>Proton transfer catalyzed by excess neutral ketone.</strong> When less than 1.0 equivalent of base is added, 10% of unreacted neutral ketone remains in solution. The kinetic enolate can deprotonate neutral ketone molecules, and repeated reversible proton exchange allows the system to slowly drift toward the more stable thermodynamic enolate T."
    },
    {
        "q": "Thermodynamic enolate T is more stable than kinetic enolate K primarily because:",
        "ch": [
            "it contains a more highly substituted (tetrasubstituted vs trisubstituted) carbon–carbon double bond.",
            "the negative charge resides entirely on the more electronegative carbon atom.",
            "it possesses a chair conformation with an axial methyl substituent.",
            "it is aromatic and obeys Hückel's 4n+2 rule."
        ],
        "a": 0,
        "e": "<strong>Alkene substitution stability:</strong> Enolates are resonance hybrids between a carbonyl-stabilized carbanion and an oxyanion alkene. Thermodynamic enolate T has a double bond between C1 and C2 (tri/tetra-substituted with the methyl group and ring carbons), whereas kinetic enolate K has the double bond between C1 and C6 (less substituted). More highly substituted alkenes have lower standard free energy due to hyperconjugation."
    },
    {
        "q": "For the equilibration between K and T at 298 K in Entry 4 (95% T and 5% K at equilibrium), what is the approximate standard free energy difference &Delta;G&deg; = G&deg;<sub>T</sub> &minus; G&deg;<sub>K</sub>? (Note: R = 8.314 J/(mol&middot;K), ln(19) &asymp; 2.94).",
        "ch": [
            "&minus;7.3 kJ/mol",
            "+7.3 kJ/mol",
            "&minus;2.4 kJ/mol",
            "&minus;24.5 kJ/mol"
        ],
        "a": 0,
        "e": "<strong>Calculate &Delta;G&deg; = &minus;RT ln(K_eq):</strong><br>K_eq = [T] / [K] = 95 / 5 = 19.<br>&Delta;G&deg; = &minus;(8.314 J/mol&middot;K)(298 K)(ln 19)<br>= &minus;(2478)(2.94) = &minus;7285 J/mol &asymp; &minus;7.3 kJ/mol.<br>Because T is more stable than K, the conversion of K to T is exergonic (&Delta;G&deg; < 0)."
    },
    {
        "q": "If the trapped silyl enol ether of kinetic enolate K is treated with ozone followed by dimethyl sulfide (O₃, then Me₂S), what functional groups will be present in the final product?",
        "ch": [
            "A carboxylic acid and an alcohol",
            "An aldehyde and a keto-ester",
            "An aldehyde and a ketone (forming a dicarbonyl cleavage product)",
            "A single cyclic &alpha;,&beta;-unsaturated ketone"
        ],
        "a": 2,
        "e": "<strong>Reductive ozonolysis of an endocyclic enol ether cleavage.</strong> The C=C double bond between C1 and C6 is cleaved by ozone. C6 (bearing a hydrogen and a ring carbon) is cleaved to form an aldehyde. C1 (bearing the silyl ether / ketone equivalent) hydrolyzes to a ketone. The result is a ring-opened keto-aldehyde."
    },
    {
        "q": "Which of the following bases would be LEAST effective for selectively generating the kinetic enolate K at &minus;78 &deg;C?",
        "ch": [
            "Lithium diisopropylamide (LDA)",
            "Potassium hexamethyldisilazide (KHMDS)",
            "Lithium tetramethylpiperidide (LiTMP)",
            "Sodium hydride (NaH)"
        ],
        "a": 3,
        "e": "<strong>NaH is an unhindered, insoluble base that does not discriminate based on steric accessibility.</strong> LDA, KHMDS, and LiTMP are all sterically hindered organic dialkylamide bases designed specifically to deprotonate unhindered protons preferentially. NaH operates as a small hydride ion (H⁻) with negligible steric bulk and often exhibits poor kinetic regioselectivity."
    }
]

# Passage 6: Axonal Membrane Biophysics & Equivalent RC Circuits
p6_html = """<div class="ttl">Passage 6 (Questions 31&ndash;36)</div>
<p>Biophysicists model the passive electrical properties of unmyelinated and myelinated neural axons using cable theory and equivalent resistor-capacitor (RC) circuits. The lipid bilayer acts as a parallel-plate capacitor with specific capacitance <i>c</i><sub>m</sub> &asymp; 1.0 &mu;F/cm<sup>2</sup>, separating the conductive intracellular cytoplasm (axoplasm) from extracellular interstitial fluid. The dielectric constant of the hydrocarbon core of the membrane is &kappa; &asymp; 3.0, and membrane thickness is <i>d</i> &asymp; 3.0 nm.</p>
<p>The time constant &tau;<sub>m</sub> governs the temporal distortion of synaptic inputs and is defined as the product of membrane resistance and capacitance: &tau;<sub>m</sub> = <i>r</i><sub>m</sub> &middot; <i>c</i><sub>m</sub>. The length constant &lambda; governs electrotonic spatial decay of subthreshold voltages according to <i>V</i>(<i>x</i>) = <i>V</i><sub>0</sub> &middot; <i>e</i><sup>&minus;<i>x</i> / &lambda;</sup>, where &lambda; = &radic;(<i>r</i><sub>m</sub> / <i>r</i><sub>i</sub>). Here, <i>r</i><sub>m</sub> is membrane resistance per unit length (&Omega;&middot;cm) and <i>r</i><sub>i</sub> is longitudinal intracellular axoplasmic resistance per unit length (&Omega;/cm).</p>
<p>Myelin sheath wraps the axon in multiple compact lipid bilayers, effectively placing <i>N</i> membrane capacitors in series. Investigators studied passive cable properties in mammalian sensory axons before and after autoimmune demyelination induced by experimental allergic encephalomyelitis (EAE).</p>
<table>
<tr><th>Axon Type</th><th>Axon Diameter <i>d</i><sub>ax</sub> (&mu;m)</th><th>Myelin Lamellae (<i>N</i>)</th><th>Membrane Capacitance <i>C</i><sub>m</sub> (pF/mm)</th><th>Membrane Resistance <i>R</i><sub>m</sub> (M&Omega;&middot;mm)</th><th>Length Constant &lambda; (mm)</th><th>Conduction Velocity (m/s)</th></tr>
<tr><td>Healthy A&alpha; (Myelinated)</td><td class="n">12.0</td><td class="n">150</td><td class="n">2.5</td><td class="n">80.0</td><td class="n">2.8</td><td class="n">72.0</td></tr>
<tr><td>Demyelinated A&alpha; (EAE)</td><td class="n">12.0</td><td class="n">0</td><td class="n">375.0</td><td class="n">0.5</td><td class="n">0.22</td><td class="n">2.5</td></tr>
<tr><td>Healthy C-fiber (Unmyelinated)</td><td class="n">1.0</td><td class="n">0</td><td class="n">31.4</td><td class="n">6.4</td><td class="n">0.18</td><td class="n">1.0</td></tr>
</table>
<p class="cap"><b>Table 1</b> Passive cable properties and conduction metrics in sensory axons.</p>"""

p6_qs = [
    {
        "q": "Based on the physical model of the myelin sheath as N identical membrane capacitors in series, wrapping 150 myelin lamellae around an axon causes the total membrane capacitance to:",
        "ch": [
            "increase by a factor of 150.",
            "decrease by a factor of 150.",
            "remain constant because capacitance depends solely on cytoplasmic ion concentration.",
            "increase proportionally to the square of the lamellae number (150² = 22,500)."
        ],
        "a": 1,
        "e": "<strong>Capacitors in series add inversely: 1/C_total = &Sigma;(1/C_i).</strong> For N identical capacitors in series, C_total = C / N. Adding 150 myelin membrane wraps increases the effective dielectric thickness d by 150-fold, reducing membrane capacitance C = &kappa;&epsilon;₀A/d by a factor of 150 (375 pF/mm &rarr; 2.5 pF/mm in Table 1). Lower capacitance allows the transmembrane potential to charge much faster with fewer ions."
    },
    {
        "q": "In an unmyelinated axon, if an electrode injects a subthreshold voltage pulse V₀ = +20 mV at position x = 0, at what distance x will the membrane potential drop to approximately +7.36 mV? (Use &lambda; = 0.18 mm; note 1/e &asymp; 0.368).",
        "ch": [
            "0.09 mm",
            "0.18 mm",
            "0.36 mm",
            "0.54 mm"
        ],
        "a": 1,
        "e": "<strong>Spatial voltage decay: V(x) = V₀ e<sup>&minus;x/&lambda;</sup>.</strong> The length constant &lambda; is by definition the distance at which the voltage decays to 1/e (~36.8%) of its initial value. 20 mV &times; 0.368 = 7.36 mV. This occurs precisely at x = &lambda; = 0.18 mm."
    },
    {
        "q": "Why does demyelination in EAE cause conduction velocity to crash from 72 m/s down to 2.5 m/s, frequently resulting in complete conduction block?",
        "ch": [
            "The axoplasmic resistance r_i increases due to precipitation of neurofilaments.",
            "Membrane resistance crashes (current leaks out through exposed axolemma) and capacitance surges, drastically shortening &lambda;.",
            "The equilibrium potential of potassium shifts from &minus;90 mV to +60 mV.",
            "Voltage-gated sodium channels are destroyed by mechanical friction from myelin debris."
        ],
        "a": 1,
        "e": "<strong>Loss of myelin compromises both resistance and capacitance.</strong> Table 1 shows that upon demyelination, R_m drops 160-fold (80 &rarr; 0.5 M&Omega;&middot;mm) because ions leak through uninsulated membrane, while C_m surges 150-fold. This causes the length constant &lambda; = &radic;(r_m/r_i) to collapse from 2.8 mm down to 0.22 mm. The electrotonic current dissipates across the leaky membrane before reaching the next node of Ranvier, preventing the threshold voltage from being reached."
    },
    {
        "q": "If the axon radius r is doubled while retaining the same intracellular resistivity &rho;, the longitudinal cytoplasmic resistance per unit length r_i (&Omega;/cm) will:",
        "ch": [
            "halve.",
            "decrease to one-fourth of its initial value.",
            "double.",
            "quadruple."
        ],
        "a": 1,
        "e": "<strong>Longitudinal resistance: r_i = &rho; / A = &rho; / (&pi;r²).</strong> Cross-sectional area is proportional to the square of the radius. Doubling radius r increases cross-sectional area by 2² = 4, which reduces axoplasmic resistance per unit length to one-fourth (r_i &prop; 1/r²)."
    },
    {
        "q": "What is the membrane time constant &tau;<sub>m</sub> for the healthy myelinated A&alpha; axon in Table 1? (Note: R<sub>m</sub> = 80 M&Omega;&middot;mm, C<sub>m</sub> = 2.5 pF/mm).",
        "ch": [
            "0.20 ms",
            "2.0 ms",
            "20 ms",
            "200 &mu;s"
        ],
        "a": 0,
        "e": "<strong>&tau; = R &times; C:</strong><br>&tau; = (80 &times; 10⁶ &Omega;&middot;mm) &times; (2.5 &times; 10⁻¹² F/mm)<br>= 200 &times; 10⁻⁶ s = 0.20 &times; 10⁻³ s = 0.20 ms (or 200 &mu;s)."
    },
    {
        "q": "Which alteration would maximize the conduction velocity of an unmyelinated giant axon (such as the squid giant axon)?",
        "ch": [
            "Decreasing axon diameter to minimize surface area",
            "Increasing internal axoplasmic diameter to drastically lower longitudinal resistance r_i",
            "Increasing membrane capacitance by incorporating polar lipid headgroups",
            "Lowering extracellular sodium concentration to hyperpolarize the resting potential"
        ],
        "a": 1,
        "e": "<strong>Giant axons achieve high conduction velocity via large caliber (diameter).</strong> In unmyelinated axons lacking myelin insulation, conduction velocity scales as &radic;diameter. A massive internal diameter maximizes cross-sectional area A, minimizing longitudinal axoplasmic resistance r_i and allowing local depolarizing currents to propagate further and faster down the core."
    }
]

# Passage 7: Cisplatin Coordination Chemistry & Pharmacokinetics
p7_html = """<div class="ttl">Passage 7 (Questions 37&ndash;42)</div>
<p>Cisplatin (<i>cis</i>-diamminedichloroplatinum(II), [Pt(NH<sub>3</sub>)<sub>2</sub>Cl<sub>2</sub>]) is a neutral square-planar d<sup>8</sup> coordination complex widely used in chemotherapy. Its therapeutic activity stems from coordination to the N7 purine nitrogen of guanine bases in DNA, forming 1,2-intrastrand d(GpG) crosslinks that distort the DNA double helix and arrest replication.</p>
<p>In blood plasma ([Cl<sup>&minus;</sup>] &asymp; 103 mM), high extracellular chloride suppresses aquation, maintaining cisplatin in its uncharged dichloro form which passively permeates cell membranes. Upon entering the cytoplasm where chloride concentration drops to 4&ndash;10 mM, cisplatin undergoes stepwise aquation (hydrolysis) with loss of chloride ligands:</p>
<p style="text-align:center;font-style:italic">
[Pt(NH<sub>3</sub>)<sub>2</sub>Cl<sub>2</sub>] + H<sub>2</sub>O &rightleftharpoons; [Pt(NH<sub>3</sub>)<sub>2</sub>Cl(H<sub>2</sub>O)]<sup>+</sup> + Cl<sup>&minus;</sup> &nbsp;&nbsp;&nbsp;&nbsp;(k<sub>1</sub> = 2.5 &times; 10<sup>&minus;5</sup> s<sup>&minus;1</sup>)<br>
[Pt(NH<sub>3</sub>)<sub>2</sub>Cl(H<sub>2</sub>O)]<sup>+</sup> + H<sub>2</sub>O &rightleftharpoons; [Pt(NH<sub>3</sub>)<sub>2</sub>(H<sub>2</sub>O)<sub>2</sub>]<sup>2+</sup> + Cl<sup>&minus;</sup> &nbsp;&nbsp;&nbsp;&nbsp;(k<sub>2</sub> = 8.0 &times; 10<sup>&minus;6</sup> s<sup>&minus;1</sup>)
</p>
<p>The cationic diaqua and monoaqua species are reactive electrophiles that rapidly crosslink DNA. The geometric isomer <i>transplatin</i> (<i>trans</i>-diamminedichloroplatinum(II)) is clinically inactive because steric constraints prevent it from forming the requisite 1,2-intrastrand crosslinks, instead forming stereochemically repairable 1,3-intrastrand and interstrand adducts.</p>
<table>
<tr><th>Complex</th><th>Geometry</th><th>Coordination Number</th><th>Aquation Rate <i>k</i><sub>1</sub> (s<sup>&minus;1</sup>)</th><th>DNA Adduct Type</th><th>Cytotoxicity IC<sub>50</sub> (&mu;M)</th></tr>
<tr><td><i>cis</i>-[Pt(NH<sub>3</sub>)<sub>2</sub>Cl<sub>2</sub>] (Cisplatin)</td><td>Square planar</td><td class="n">4</td><td class="n">2.5 &times; 10<sup>&minus;5</sup></td><td>1,2-intrastrand d(GpG) (90%)</td><td class="n">1.8</td></tr>
<tr><td><i>trans</i>-[Pt(NH<sub>3</sub>)<sub>2</sub>Cl<sub>2</sub>] (Transplatin)</td><td>Square planar</td><td class="n">4</td><td class="n">9.8 &times; 10<sup>&minus;5</sup></td><td>1,3-intrastrand / interstrand</td><td class="n">85.0</td></tr>
<tr><td>Carboplatin (dicarboxylate chelate)</td><td>Square planar</td><td class="n">4</td><td class="n">1.2 &times; 10<sup>&minus;7</sup></td><td>1,2-intrastrand d(GpG)</td><td class="n">12.0</td></tr>
<tr><td>Oxaliplatin (DACH ligand)</td><td>Square planar</td><td class="n">4</td><td class="n">3.4 &times; 10<sup>&minus;6</sup></td><td>1,2-intrastrand d(GpG)</td><td class="n">2.2</td></tr>
</table>
<p class="cap"><b>Table 1</b> Chemical properties and biological parameters of platinum complexes.</p>"""

p7_qs = [
    {
        "q": "What is the formal oxidation state and d-electron count of the central platinum ion in cisplatin, [Pt(NH<sub>3</sub>)<sub>2</sub>Cl<sub>2</sub>]?",
        "ch": [
            "Pt(0), d¹⁰",
            "Pt(+2), d⁸",
            "Pt(+4), d⁶",
            "Pt(+2), d¹⁰"
        ],
        "a": 1,
        "e": "<strong>Determine oxidation state from ligands:</strong> Ammonia (NH₃) is a neutral ligand (charge 0). Each chloride (Cl⁻) carries a &minus;1 charge. For an overall neutral complex: Pt + 2(0) + 2(&minus;1) = 0 &rArr; Pt = +2. Neutral platinum (Group 10) has 10 valence electrons ([Xe] 4f¹⁴ 5d⁹ 6s¹ or 5d¹⁰). Losing two electrons yields Pt²⁺ with an [Xe] 4f¹⁴ 5d⁸ electron configuration (d⁸)."
    },
    {
        "q": "Why does cisplatin remain predominantly intact in extracellular circulation but rapidly hydrolyze inside tumor cells?",
        "ch": [
            "The extracellular pH is acidic (pH 4.0), preventing hydrolysis of chloride ligands.",
            "By Le Châtelier's principle, the high extracellular chloride concentration (~103 mM) suppresses ligand displacement, whereas low intracellular chloride (~4 mM) shifts the equilibrium toward aquation.",
            "Extracellular albumin acts as an allosteric inhibitor of platinum ligand exchange.",
            "Intracellular glutathione directly reduces platinum(II) to platinum(0) nanoparticles."
        ],
        "a": 1,
        "e": "<strong>Le Châtelier's principle and chloride equilibrium:</strong> The aquation reaction is [Pt(NH₃)₂Cl₂] + H₂O &rightleftharpoons; [Pt(NH₃)₂Cl(H₂O)]⁺ + Cl⁻. In bloodstream plasma, [Cl⁻] is high (~103 mM), pushing the equilibrium to the left and keeping the complex intact and uncharged (promoting membrane diffusion). In the cytoplasm, [Cl⁻] is 10- to 25-fold lower (4–10 mM), driving chloride displacement to form reactive cationic aquated species."
    },
    {
        "q": "Carboplatin exhibits a 200-fold slower aquation rate than cisplatin (Table 1: k₁ = 1.2 &times; 10⁻⁷ vs 2.5 &times; 10⁻⁵ s⁻¹) because:",
        "ch": [
            "the bidentate cyclobutane-1,1-dicarboxylate ligand forms a stable chelate ring that resists solvolysis.",
            "carboplatin adopts an octahedral geometry with coordination number 6.",
            "the ammonia ligands in carboplatin are substituted by secondary amines.",
            "carboplatin is insoluble in aqueous solutions."
        ],
        "a": 0,
        "e": "<strong>The Chelate Effect:</strong> Carboplatin replaces the two monodentate chloride leaving groups with a bidentate cyclobutane-1,1-dicarboxylate ligand. Bidentate ligands form a closed chelate ring with the metal center. Breaking a chelate ring requires dissociating two coordinating bonds sequentially, and the dangling coordinating arm rapidly re-binds before solvent water can displace it, providing high kinetic stability against aquation."
    },
    {
        "q": "Why is transplatin clinically inactive (IC₅₀ = 85 &mu;M) despite hydrolyzing faster than cisplatin (Table 1)?",
        "ch": [
            "Transplatin cannot enter cells via passive diffusion.",
            "The trans geometry prevents the platinum center from coordinating two adjacent guanine bases on the same DNA strand (1,2-intrastrand crosslink).",
            "Transplatin is oxidized to platinum(IV) by cellular catalase.",
            "Transplatin coordinates exclusively to the ribose phosphate backbone rather than purine bases."
        ],
        "a": 1,
        "e": "<strong>Stereospecific geometric constraint:</strong> In cisplatin, the two chloride leaving groups are adjacent (90&deg; cis orientation), with a Pt-leaving group separation of ~3.3 &Aring;, perfectly matching the distance between adjacent N7 atoms of adjacent guanines in a DNA strand (1,2-intrastrand d(GpG) crosslink). In transplatin, the leaving groups are opposite (180&deg; trans), forcing it to form 1,3-intrastrand or interstrand crosslinks that fail to bend DNA into the specific cytotoxic conformation and are readily repaired by nucleotide excision repair enzymes."
    },
    {
        "q": "The coordination geometry of d⁸ Pt(II) complexes is square planar rather than tetrahedral because:",
        "ch": [
            "Pt(II) is a low-spin d⁸ metal with strong ligand-field splitting that leaves the high-energy d(x²-y²) orbital unoccupied.",
            "steric repulsion between ligands forces a 90&deg; bond angle.",
            "the d-orbitals are completely empty in the Pt(II) valence shell.",
            "water molecules form hydrogen bonds that planarize the coordination sphere."
        ],
        "a": 0,
        "e": "<strong>Crystal field theory for square planar d⁸:</strong> Pt(II) is a 5d transition metal with large crystal field splitting (&Delta;). In a square-planar field, the d-orbitals split into four energy levels: d(xz), d(yz) < d(z²) < d(xy) << d(x²&minus;y²). The 8 d-electrons pair up and completely fill the four lower-energy orbitals, leaving the strongly antibonding d(x²&minus;y²) orbital completely vacant, yielding maximum crystal field stabilization energy (CFSE)."
    },
    {
        "q": "If an intravenous infusion of 100 mg of cisplatin (molar mass = 300 g/mol) is administered to a patient, what is the maximum theoretical mass of platinum contained in that dose? (Molar mass of Pt = 195 g/mol).",
        "ch": [
            "35 mg",
            "50 mg",
            "65 mg",
            "90 mg"
        ],
        "a": 2,
        "e": "<strong>Mass percent calculation:</strong><br>Mass % of Pt = (Molar mass Pt / Molar mass cisplatin) &times; 100%<br>= (195 g/mol / 300 g/mol) &times; 100% = 65.0%.<br>Total Pt mass in a 100 mg dose = 0.65 &times; 100 mg = 65 mg."
    }
]

# 10 Discrete Questions for C/P
cp_discretes = [
    {
        "q": "An endoscope utilizes optical fiber bundles to transmit light into the stomach. If the core of the optical fiber has an index of refraction n₁ = 1.60 and the cladding has n₂ = 1.28, what is the critical angle &theta;_c for total internal reflection within the fiber core?",
        "d": True,
        "ch": [
            "30°",
            "45°",
            "53°",
            "60°"
        ],
        "a": 2,
        "e": "<strong>Snell's Law at critical angle:</strong> sin(&theta;_c) = n₂ / n₁.<br>sin(&theta;_c) = 1.28 / 1.60 = 0.80.<br>Knowing standard trig values: sin(30&deg;) = 0.50, sin(45&deg;) &asymp; 0.707, sin(53&deg;) &asymp; 0.80 (from 3-4-5 right triangle), sin(60&deg;) &asymp; 0.866. Thus &theta;_c &asymp; 53&deg;."
    },
    {
        "q": "Technetium-99m (⁹⁹ᵐTc) is a gamma-emitting radioisotope used in myocardial perfusion imaging with a physical half-life of 6.0 hours. If a patient is administered 800 MBq of ⁹⁹ᵐTc, how much radioactivity remains in the patient's body after 24 hours (assuming negligible biological excretion)?",
        "d": True,
        "ch": [
            "200 MBq",
            "100 MBq",
            "50 MBq",
            "25 MBq"
        ],
        "a": 2,
        "e": "<strong>First-order radioactive decay:</strong> Number of half-lives elapsed n = 24 h / 6.0 h = 4 half-lives.<br>Activity remaining = A₀ &times; (&frac12;)⁴ = 800 &times; (1/16) = 50 MBq."
    },
    {
        "q": "Under which set of conditions does a real gas deviate MOST significantly from ideal behavior described by PV = nRT?",
        "d": True,
        "ch": [
            "High temperature and low pressure",
            "Low temperature and high pressure",
            "High temperature and high pressure",
            "Low temperature and low pressure"
        ],
        "a": 1,
        "e": "<strong>Real gas deviations (van der Waals behavior):</strong> Ideal gas law assumes (1) gas molecules possess zero volume, and (2) no intermolecular forces exist. At high pressure, molecules are crowded closely together, making their physical volume non-negligible (b parameter). At low temperature, molecules move slowly, allowing intermolecular attractive forces (a parameter) to pull molecules together and reduce pressure. Thus, low T and high P produce maximal deviation."
    },
    {
        "q": "An ideal gas in a cylinder with a movable frictionless piston expands isobarically at a constant pressure of 2.0 &times; 10⁵ Pa from an initial volume of 0.010 m³ to a final volume of 0.035 m³. How much mechanical work was performed by the gas during this expansion?",
        "d": True,
        "ch": [
            "2.5 kJ",
            "5.0 kJ",
            "7.0 kJ",
            "12.0 kJ"
        ],
        "a": 1,
        "e": "<strong>Isobaric work: W = P &Delta;V.</strong><br>&Delta;V = 0.035 &minus; 0.010 = 0.025 m³.<br>W = (2.0 &times; 10⁵ N/m²) &times; (0.025 m³) = 5000 J = 5.0 kJ."
    },
    {
        "q": "Which reaction represents a Lewis acid-base reaction that does NOT involve Brønsted-Lowry proton transfer?",
        "d": True,
        "ch": [
            "HCl(aq) + NaOH(aq) → NaCl(aq) + H₂O(l)",
            "BF₃ + :NH₃ → F₃B:NH₃",
            "CH₃COOH + H₂O ⇌ CH₃COO⁻ + H₃O⁺",
            "NH₄⁺ + OH⁻ → NH₃ + H₂O"
        ],
        "a": 1,
        "e": "<strong>Lewis acid-base coordination:</strong> BF₃ has an incomplete octet (vacant 2p orbital on boron), acting as a Lewis acid (electron-pair acceptor). Ammonia (:NH₃) has a lone pair on nitrogen, acting as a Lewis base (electron-pair donor). They form a coordinate covalent adduct (F₃B:NH₃) with no transfer of protons."
    },
    {
        "q": "A laboratory technician prepares a 1.0 L buffer solution containing 0.10 M acetic acid and 0.10 M sodium acetate (pH = 4.76). If 9.0 L of distilled water is added to dilute the solution tenfold to a total volume of 10.0 L, what will be the resulting pH of the buffer?",
        "d": True,
        "ch": [
            "3.76",
            "4.76",
            "5.76",
            "7.00"
        ],
        "a": 1,
        "e": "<strong>Dilution does not alter the buffer ratio:</strong> Henderson-Hasselbalch: pH = pKa + log([A⁻]/[HA]). When diluted tenfold, both [A⁻] and [HA] drop by a factor of 10 (from 0.10 M to 0.010 M). The ratio [A⁻]/[HA] remains exactly 1.0, so log(1.0) = 0, and pH = pKa = 4.76."
    },
    {
        "q": "A pure solution of an enantiomeric drug has a specific rotation [α] of +40°/(dm·g/mL). If a synthetic batch consists of 75% of this dextrorotatory enantiomer and 25% of the levorotatory enantiomer, what observed specific rotation will be measured?",
        "d": True,
        "ch": [
            "+10°",
            "+20°",
            "+30°",
            "+40°"
        ],
        "a": 1,
        "e": "<strong>Enantiomeric excess (ee) and optical rotation:</strong><br>ee = % Major &minus; % Minor = 75% &minus; 25% = 50% (0.50).<br>Observed rotation = ee &times; [pure rotation] = 0.50 &times; (+40&deg;) = +20&deg;."
    },
    {
        "q": "A biopsy specimen of bone tissue has a mass of 4.5 g in air and an apparent mass of 2.7 g when completely submerged in water (density = 1.0 g/cm³). What is the density of the bone specimen?",
        "d": True,
        "ch": [
            "1.5 g/cm³",
            "1.8 g/cm³",
            "2.5 g/cm³",
            "3.0 g/cm³"
        ],
        "a": 2,
        "e": "<strong>Archimedes' principle: Apparent weight loss = Buoyant force = weight of displaced fluid.</strong><br>Mass of displaced water = 4.5 g &minus; 2.7 g = 1.8 g.<br>Volume of displaced water (and bone) = mass / density = 1.8 g / (1.0 g/cm³) = 1.8 cm³.<br>Density of bone = mass in air / volume = 4.5 g / 1.8 cm³ = 2.5 g/cm³."
    },
    {
        "q": "During a biceps curl exercise, the biceps tendon inserts at a right angle into the forearm at a distance of 4.0 cm from the elbow joint axis. If the forearm and hand have a combined mass of 2.0 kg with center of mass 16.0 cm from the elbow, and the hand holds a 10.0 kg dumbbell at 32.0 cm from the elbow, what upward muscle force F_b must the biceps exert to hold the forearm horizontally in static equilibrium? (Use g = 9.8 m/s²).",
        "ch": [
            "352 N",
            "862 N",
            "980 N",
            "3450 N"
        ],
        "a": 1,
        "e": "<strong>Rotational equilibrium: &Sigma;&tau; = 0 around the elbow pivot.</strong><br>Counter-clockwise torque (biceps) = Clockwise torque (forearm + dumbbell).<br>F_b &times; (0.04 m) = [m_arm &times; g &times; r_arm] + [m_weight &times; g &times; r_weight]<br>F_b &times; 0.04 = [2.0 &times; 9.8 &times; 0.16] + [10.0 &times; 9.8 &times; 0.32]<br>F_b &times; 0.04 = [3.136] + [31.36] = 34.496 N&middot;m<br>F_b = 34.496 / 0.04 = 862.4 N &asymp; 862 N."
    },
    {
        "q": "Consider a standard galvanic electrochemical cell operating at 298 K with the half-reactions:<br>Cu²⁺(aq) + 2 e⁻ → Cu(s) &nbsp;&nbsp;(E° = +0.34 V)<br>Zn²⁺(aq) + 2 e⁻ → Zn(s) &nbsp;&nbsp;(E° = −0.76 V)<br>What is the standard cell potential E°_cell and the equilibrium constant K_eq?",
        "d": True,
        "ch": [
            "E°_cell = +0.42 V, K_eq < 1",
            "E°_cell = +1.10 V, K_eq = 1.6 × 10³⁷",
            "E°_cell = −1.10 V, K_eq = 6.2 × 10⁻³⁸",
            "E°_cell = +1.10 V, K_eq = 1.0"
        ],
        "a": 1,
        "e": "<strong>Galvanic cell potential:</strong> In a spontaneous galvanic cell, zinc undergoes oxidation at the anode and copper undergoes reduction at the cathode:<br>E&deg;_cell = E&deg;_cathode &minus; E&deg;_anode = +0.34 V &minus; (&minus;0.76 V) = +1.10 V.<br>Using &Delta;G&deg; = &minus;nFE&deg;_cell = &minus;RT ln(K_eq):<br>ln(K_eq) = (n &times; E&deg;_cell) / 0.0257 = (2 &times; 1.10) / 0.0257 &asymp; 85.6 &rArr; K_eq &asymp; 1.6 &times; 10³⁷ (vastly favors products)."
    }
]

# Assemble into EXAM_CP90
all_sets = [
    {
        "id": "exam_cp90_p1",
        "sec": "C/P",
        "topic": "Acid–base equilibria and carbonic anhydrase kinetics",
        "sheet": 13,
        "label": "Chemical and Physical Foundations of Biological Systems",
        "examId": "cp90",
        "passage": p1_html,
        "qs": p1_qs
    },
    {
        "id": "exam_cp90_p2",
        "sec": "C/P",
        "topic": "Doppler ultrasound and fluid dynamics in stenosis",
        "sheet": 67,
        "label": "Chemical and Physical Foundations of Biological Systems",
        "examId": "cp90",
        "passage": p2_html,
        "qs": p2_qs
    },
    {
        "id": "exam_cp90_p3",
        "sec": "C/P",
        "topic": "Organic synthesis, S_NAr mechanisms, and spectroscopy",
        "sheet": 19,
        "label": "Chemical and Physical Foundations of Biological Systems",
        "examId": "cp90",
        "passage": p3_html,
        "qs": p3_qs
    },
    {
        "id": "exam_cp90_p4",
        "sec": "C/P",
        "topic": "Electrochemistry and fast-scan cyclic voltammetry",
        "sheet": 15,
        "label": "Chemical and Physical Foundations of Biological Systems",
        "examId": "cp90",
        "passage": p4_html,
        "qs": p4_qs
    },
    {
        "id": "exam_cp90_p5",
        "sec": "C/P",
        "topic": "Thermodynamic vs kinetic control in enolate reactions",
        "sheet": 21,
        "label": "Chemical and Physical Foundations of Biological Systems",
        "examId": "cp90",
        "passage": p5_html,
        "qs": p5_qs
    },
    {
        "id": "exam_cp90_p6",
        "sec": "C/P",
        "topic": "Axonal cable biophysics and RC circuits",
        "sheet": 69,
        "label": "Chemical and Physical Foundations of Biological Systems",
        "examId": "cp90",
        "passage": p6_html,
        "qs": p6_qs
    },
    {
        "id": "exam_cp90_p7",
        "sec": "C/P",
        "topic": "Coordination chemistry and aquation kinetics of cisplatin",
        "sheet": 6,
        "label": "Chemical and Physical Foundations of Biological Systems",
        "examId": "cp90",
        "passage": p7_html,
        "qs": p7_qs
    },
    {
        "id": "exam_cp90_discretes",
        "sec": "C/P",
        "topic": "C/P Standalone Discrete Questions",
        "sheet": None,
        "label": "Chemical and Physical Foundations of Biological Systems",
        "examId": "cp90",
        "passage": "",
        "qs": cp_discretes
    }
]

total_qs = sum(len(s["qs"]) for s in all_sets)
print(f"Total C/P questions: {total_qs}")

# Write to exam_cp90.js
js_content = "/* ---- exam_cp90.js ---- */\n/* Full 90-minute Chem/Phys practice section: 7 passages (42 Qs) + 10 discrete Qs = 52 Qs */\nconst EXAM_CP90 = " + json.dumps(all_sets, indent=2) + ";\n"
with open("/home/cgslinde/DrillRoom/DrillRoom/exam_cp90.js", "w") as f:
    f.write(js_content)

print("exam_cp90.js written successfully!")
