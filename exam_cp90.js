/* ---- exam_cp90.js ---- */
/* Full 90-minute Chemical and Physical Foundations practice section: 52 Qs */
const EXAM_CP90 = [
  {
    "id": "exam_cp90_p1",
    "sec": "C/P",
    "topic": "Acid–base equilibria and carbonic anhydrase kinetics",
    "sheet": 13,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90",
    "passage": "<div class=\"ttl\">Passage 1 (Questions 1&ndash;6)</div>\n<p>Carbonic anhydrases (CAs) are zinc metalloenzymes that catalyze the reversible hydration of carbon dioxide: CO<sub>2</sub> + H<sub>2</sub>O &rightleftharpoons; HCO<sub>3</sub><sup>&minus;</sup> + H<sup>+</sup>. In erythrocytes, CA II operates near the diffusion-controlled limit with a turnover number (<i>k</i><sub>cat</sub>) of 1.4 &times; 10<sup>6</sup> s<sup>&minus;1</sup>. The active site features a Zn<sup>2+</sup> ion coordinated tetrahedrally by three histidine imidazoles (His94, His96, His119) and a bound water molecule or hydroxide ion.</p>\n<p>The catalytic mechanism involves two distinct stages: (1) nucleophilic attack of the zinc-bound hydroxide on CO<sub>2</sub> to form bicarbonate, which is subsequently displaced by a water molecule; and (2) regeneration of the active zinc-bound hydroxide via proton transfer to bulk solvent through a proton-shuttle residue, His64 (p<i>K</i><sub>a</sub> &asymp; 7.1).</p>\n<p>To characterize the thermodynamic and kinetic barriers of CA II variants, investigators synthesized mutant enzymes altering His64 and His94. Catalytic activity was measured at 298 K in 50 mM HEPES buffer across a pH range of 6.0 to 8.5. Acetazolamide (AZA), a sulfonamide inhibitor, was titrated against each variant to determine the inhibition constant (<i>K</i><sub>i</sub>). Dissociation constants for Zn<sup>2+</sup> binding (<i>K</i><sub>d,Zn</sub>) were also quantified via isothermal titration calorimetry.</p>\n<table>\n<tr><th>Enzyme Variant</th><th><i>k</i><sub>cat</sub> (s<sup>&minus;1</sup>)</th><th><i>K</i><sub>m</sub> for CO<sub>2</sub> (mM)</th><th><i>k</i><sub>cat</sub> / <i>K</i><sub>m</sub> (M<sup>&minus;1</sup>s<sup>&minus;1</sup>)</th><th><i>K</i><sub>i</sub> for AZA (nM)</th><th><i>K</i><sub>d,Zn</sub> (pM)</th></tr>\n<tr><td>Wild-Type (WT)</td><td class=\"n\">1.4 &times; 10<sup>6</sup></td><td class=\"n\">12.0</td><td class=\"n\">1.2 &times; 10<sup>8</sup></td><td class=\"n\">10</td><td class=\"n\">4.0</td></tr>\n<tr><td>H64A</td><td class=\"n\">1.1 &times; 10<sup>4</sup></td><td class=\"n\">12.5</td><td class=\"n\">8.8 &times; 10<sup>5</sup></td><td class=\"n\">12</td><td class=\"n\">4.2</td></tr>\n<tr><td>H94A</td><td class=\"n\">2.3 &times; 10<sup>2</sup></td><td class=\"n\">110.0</td><td class=\"n\">2.1 &times; 10<sup>3</sup></td><td class=\"n\">4500</td><td class=\"n\">3.8 &times; 10<sup>5</sup></td></tr>\n<tr><td>H64E</td><td class=\"n\">3.5 &times; 10<sup>5</sup></td><td class=\"n\">11.8</td><td class=\"n\">3.0 &times; 10<sup>7</sup></td><td class=\"n\">11</td><td class=\"n\">4.1</td></tr>\n</table>\n<p class=\"cap\"><b>Table 1</b> Kinetic and thermodynamic parameters for CA II variants at pH 7.4, 298 K.</p>",
    "qs": [
      {
        "q": "Based on Table 1, which catalytic step is most severely rate-limiting in the H64A variant compared to the wild-type enzyme?",
        "ch": [
          "Nucleophilic attack of zinc-bound hydroxide on dissolved substrate carbon dioxide.",
          "Displacement of coordinated bicarbonate by an incoming solvent water molecule.",
          "Initial substrate binding of carbon dioxide into the hydrophobic active pocket.",
          "Intermolecular proton transfer from the zinc-bound water to bulk solvent buffer."
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Kinetic Decoupling of Substrate Affinity and Proton Shuttling]</strong> In carbonic anhydrase II, catalytic turnover requires rapid regeneration of the active zinc-hydroxide nucleophile via an intramolecular proton shuttle.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Table 1 shows that mutating His64 to alanine (H64A) causes kcat to drop by over two orders of magnitude (1.4 &times; 10⁶ to 1.1 &times; 10⁴ s⁻¹), whereas Km is unchanged (12.0 vs 12.5 mM).<br>2. <em>Mechanistic Bridge</em>: Because Km reflects substrate binding affinity, the invariance of Km demonstrates that CO₂ binding and coordination are unimpaired. The severe decline in kcat indicates that the chemical step mediated by His64—transferring a proton from the zinc-bound water to the external buffer—is the rate-determining bottleneck.<br>3. <em>Deduction</em>: Proton transfer is the selectively impaired step.<br><br><em>Distractor Traps:</em><br>&bull; A (Km Invariance Trap): Nucleophilic attack on CO₂ would alter effective binding kinetics or Km, which remains unchanged in H64A.<br>&bull; B (Ligand Displacement Error): Bicarbonate displacement is facilitated by the zinc coordination sphere, not the peripheral His64 residue.<br>&bull; C (Binding vs Catalysis Confusion): Confuses substrate association (governed by the hydrophobic pocket) with catalytic regeneration (governed by the proton shuttle)."
      },
      {
        "q": "The zinc ion in carbonic anhydrase acts as a Lewis acid during catalysis primarily by:",
        "ch": [
          "accepting electron density from coordinated water, lowering its pKa down from 14 to 7.",
          "donating an electron pair to water, lowering its pKa from 14 down to approximately 7.",
          "stabilizing the conjugate acid form of bicarbonate via electrostatic hydrogen bonding.",
          "oxidizing coordinated water molecules to produce molecular oxygen and free protons."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Lewis Acidic Polarization of Coordinated Ligands]</strong> A Lewis acid accepts electron density, polarizing coordinated bonds and dramatically depressing the pKa of bound protic ligands.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Definition</em>: Lewis acids are electron-pair acceptors. The divalent Zn²⁺ cation coordinates the lone pair of water's oxygen.<br>2. <em>Chemical Mechanism</em>: By drawing electron density toward the metal center, Zn²⁺ polarizes the O–H bond, stabilizing the conjugate base (hydroxide).<br>3. <em>Physiological Consequence</em>: This depression of water's pKa from ~14 to 7 generates a powerful hydroxide nucleophile at physiological pH.<br><br><em>Distractor Traps:</em><br>&bull; B (Lewis Acid/Base Inversion): States that Zn²⁺ donates an electron pair, which is the definition of a Lewis base, not an acid.<br>&bull; C (Charge Inversion): Bicarbonate is an anion; stabilizing its 'conjugate acid' (carbonic acid) does not drive hydroxide activation.<br>&bull; D (Redox Confabulation): Zn²⁺ is redox-inert in biological catalysis and does not oxidize water to oxygen."
      },
      {
        "q": "If an untreated patient with severe respiratory acidosis has an arterial blood pH of 7.10 and a PCO₂ of 80 mmHg (dissolved [CO₂] = 2.4 mM), what is the patient's plasma [HCO₃⁻]? (Note: pKa of the carbonic acid/bicarbonate system is 6.10).",
        "ch": [
          "2.4 mM",
          "12 mM",
          "24 mM",
          "48 mM"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Henderson-Hasselbalch Equilibrium in Acid-Base Disturbances]</strong> Arterial pH is dictated by the logarithmic ratio of bicarbonate conjugate base to dissolved carbon dioxide acid.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Formula Setup</em>: pH = pKa + log([HCO₃⁻] / [CO₂]).<br>2. <em>Substitute Knowns</em>: 7.10 = 6.10 + log([HCO₃⁻] / 2.4 mM) &rArr; log([HCO₃⁻] / 2.4 mM) = 1.00.<br>3. <em>Solve for Concentration</em>: 10^(1.00) = [HCO₃⁻] / 2.4 mM &rArr; [HCO₃⁻] = 2.4 &times; 10 = 24 mM.<br><br><em>Distractor Traps:</em><br>&bull; A (Equimolar Trap): Conflates bicarbonate concentration directly with dissolved CO₂ (2.4 mM).<br>&bull; B (Inverted Ratio Error): Evaluates 10^(-1.0) = 0.1 instead of 10^(+1.0) = 10, then multiplies by 5.<br>&bull; D (Normal pH Multiplier): Multiplies 2.4 mM by 20 (the ratio for normal pH 7.40) rather than 10 (acidemic pH 7.10)."
      },
      {
        "q": "Why does the H94A mutation exhibit a 10⁵-fold increase in Kd,Zn and a 450-fold increase in Ki for acetazolamide, whereas H64A exhibits virtually no change in these parameters?",
        "ch": [
          "His64 is buried within the core, shielding the zinc ion from aqueous solvation.",
          "Acetazolamide acts as an uncompetitive inhibitor binding only to a His64-CO₂ complex.",
          "His94 directly coordinates the catalytic Zn²⁺, whereas His64 resides on the surface.",
          "His94 undergoes phosphorylation during catalysis to maintain zinc ion coordination."
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Active Site Coordination vs Peripheral Solvent Shuttling]</strong> Primary coordinating ligands directly maintain the metal-binding pocket, whereas peripheral shuttle residues modulate kinetic transfer without altering binding thermodynamics.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Structural Roles</em>: His94 is one of three direct dative ligands chelating Zn²⁺; His64 is an exocyclic residue extending into the solvent channel.<br>2. <em>Consequence of Alanine Substitution</em>: Mutating His94 abolishes a critical zinc-imidazole bond, destabilizing Zn²⁺ retention (Kd,Zn surges by 10⁵) and distorting the drug-binding pharmacophore (Ki surges 450-fold).<br>3. <em>His64 Independence</em>: Because His64 does not contact Zn²⁺ or acetazolamide, H64A leaves these thermodynamic binding constants intact.<br><br><em>Distractor Traps:</em><br>&bull; A (Structural Inversion): His94 is in the core pocket; His64 is surface-exposed to shuttle protons to solvent.<br>&bull; B (Inhibition Mode Confabulation): Acetazolamide is a classic competitive inhibitor that coordinates directly to Zn²⁺, not an uncompetitive inhibitor.<br>&bull; D (Biochemical Fiction): Histidine is not phosphorylated during CA II catalysis; coordination occurs via neutral dative bonding."
      },
      {
        "q": "At pH 8.1, what fraction of the wild-type His64 side chain (pKa = 7.1) exists in its neutral (deprotonated imidazole) form?",
        "ch": [
          "10%",
          "50%",
          "90%",
          "99%"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Logarithmic Dissociation Ratios and Fractional Speciation]</strong> The ionization state of an amino acid residue depends upon the difference between environmental pH and the residue's pKa.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Calculate Offset</em>: pH &minus; pKa = 8.1 &minus; 7.1 = +1.0.<br>2. <em>Logarithmic Ratio</em>: log([Base]/[Acid]) = 1.0 &rArr; [Base]/[Acid] = 10/1.<br>3. <em>Calculate Fraction</em>: Fraction neutral base = [Base] / ([Base] + [Acid]) = 10 / (10 + 1) = 10/11 &asymp; 90.9% (approximately 90%).<br><br><em>Distractor Traps:</em><br>&bull; A (Reciprocal Fraction Error): Calculates the cationic protonated fraction [Acid]/([Base]+[Acid]) = 1/11 &asymp; 9.1% (10%).<br>&bull; B (Equivalence Point Trap): Occurs only when pH = pKa (pH 7.10), where conjugate base and acid fractions are exactly 50%.<br>&bull; D (Two-Unit Offset Error): Occurs when pH is 2 full units above pKa (pH 9.10), yielding 99% deprotonation."
      },
      {
        "q": "A researcher bubbles pure ¹⁸O-labeled CO₂ (C¹⁸O₂) into an aqueous solution containing CA II and H₂¹⁶O. After one single catalytic turnover, the inorganic bicarbonate formed will contain:",
        "ch": [
          "two ¹⁸O atoms and one ¹⁶O atom.",
          "three ¹⁸O atoms and no ¹⁶O atoms.",
          "one ¹⁸O atom and two ¹⁶O atoms.",
          "no ¹⁸O atoms and three ¹⁶O atoms."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Isotopic Tracing of Metalloenzyme Addition Mechanisms]</strong> In carbonic anhydrase hydration, bicarbonate is formed by nucleophilic addition of a solvent-derived zinc-hydroxide across the electrophilic carbon of carbon dioxide.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Substrate Inventory</em>: Dissolved carbon dioxide provides the carbon atom and two oxygen atoms: both are ¹⁸O (C¹⁸O₂).<br>2. <em>Nucleophile Source</em>: The catalytic nucleophile is Zn²⁺–OH⁻, generated by deprotonating solvent water (H₂¹⁶O). Thus, the oxygen atom of the hydroxide is ¹⁶O.<br>3. <em>Product Stoichiometry</em>: Nucleophilic attack of [Zn–¹⁶OH]⁻ on C¹⁸O₂ produces HC¹⁸O₂¹⁶O⁻: exactly two ¹⁸O atoms and one ¹⁶O atom.<br><br><em>Distractor Traps:</em><br>&bull; B (Anhydrous Bicarbonate Error): Assumes bicarbonate oxygens originate exclusively from CO₂, ignoring solvent water incorporation.<br>&bull; C (Multiple Turnover Inversion): Reflects wash-out of ¹⁸O after numerous successive reversible hydration/dehydration cycles in excess H₂¹⁶O.<br>&bull; D (Total Exchange Fiction): Assumes complete isotopic exchange occurs with solvent prior to product release in a single turnover."
      }
    ]
  },
  {
    "id": "exam_cp90_p2",
    "sec": "C/P",
    "topic": "Doppler ultrasound and fluid dynamics in stenosis",
    "sheet": 67,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90",
    "passage": "<div class=\"ttl\">Passage 2 (Questions 7&ndash;12)</div>\n<p>Intravascular ultrasound (IVUS) and pulsed-wave Doppler velocimetry are diagnostic modalities used to assess atherosclerotic lesions and arterial stenoses. Blood is modeled as an incompressible, non-Newtonian suspension, but within large conducting arteries (e.g., the femoral artery, internal diameter <i>D</i><sub>0</sub> = 6.0 mm), laminar flow can be approximated by Poiseuille's law and the continuity equation: <i>A</i><sub>1</sub><i>v</i><sub>1</sub> = <i>A</i><sub>2</sub><i>v</i><sub>2</sub>.</p>\n<p>An ultrasound transducer emitting acoustic waves at carrier frequency <i>f</i><sub>0</sub> = 5.0 MHz is oriented at an Doppler insonation angle &theta; = 60&deg; relative to the longitudinal vector of blood flow. The Doppler frequency shift &Delta;<i>f</i> is given by:</p>\n<p style=\"text-align:center;font-style:italic\">&Delta;f = (2 &middot; f<sub>0</sub> &middot; v &middot; cos &theta;) / c</p>\n<p>where <i>v</i> is the flow velocity and <i>c</i> is the acoustic velocity in soft tissue (<i>c</i> = 1540 m/s). Note: cos(60&deg;) = 0.50.</p>\n<p>Investigators tested an in vitro vascular phantom under steady pulsatile pressure (mean perfusion pressure &Delta;<i>P</i> = 100 mmHg &asymp; 13.3 kPa). A rigid axisymmetric constriction was introduced, reducing vessel luminal diameter across three test sections. Fluid density &rho; = 1.06 &times; 10<sup>3</sup> kg/m<sup>3</sup>, and dynamic viscosity &eta; = 3.5 &times; 10<sup>&minus;3</sup> Pa&middot;s. Turbulence occurs when the Reynolds number <i>Re</i> = (&rho; &middot; <i>v</i> &middot; <i>D</i>) / &eta; exceeds the critical threshold <i>Re</i><sub>crit</sub> &asymp; 2000.</p>\n<table>\n<tr><th>Vessel Segment</th><th>Luminal Diameter <i>D</i> (mm)</th><th>Cross-Sectional Area (mm<sup>2</sup>)</th><th>Doppler Shift &Delta;<i>f</i> (kHz)</th><th>Calculated Velocity <i>v</i> (m/s)</th><th>Reynolds Number (<i>Re</i>)</th></tr>\n<tr><td>Proximal (Baseline)</td><td class=\"n\">6.0</td><td class=\"n\">28.3</td><td class=\"n\">1.62</td><td class=\"n\">0.50</td><td class=\"n\">909</td></tr>\n<tr><td>Moderate Stenosis</td><td class=\"n\">3.0</td><td class=\"n\">7.1</td><td class=\"n\">6.49</td><td class=\"n\">2.00</td><td class=\"n\">1817</td></tr>\n<tr><td>Severe Stenosis</td><td class=\"n\">1.5</td><td class=\"n\">1.8</td><td class=\"n\">25.97</td><td class=\"n\">8.00</td><td class=\"n\">3634</td></tr>\n</table>\n<p class=\"cap\"><b>Table 1</b> Hemodynamic parameters recorded in arterial phantom sections.</p>",
    "qs": [
      {
        "q": "According to the data in Table 1, when the lumen diameter decreases by a factor of 4 (from 6.0 mm to 1.5 mm), the blood velocity increases by a factor of:",
        "ch": [
          "4-fold",
          "8-fold",
          "16-fold",
          "64-fold"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Hydrodynamic Continuity and Cross-Sectional Area Scaling]</strong> For an incompressible fluid in steady laminar flow, volumetric flow rate is conserved: Q = A₁v₁ = A₂v₂.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Area Scaling</em>: Cross-sectional area of a cylindrical lumen is A = &pi;(D/2)² &prop; D².<br>2. <em>Ratio Assessment</em>: When diameter D decreases by a factor of 4, cross-sectional area A decreases by a factor of 4² = 16.<br>3. <em>Velocity Compensation</em>: To maintain constant Q, velocity must increase by the reciprocal factor: v₂ = v₁ &times; (A₁/A₂) = 16v₁ (Table 1 confirms 0.50 m/s &rarr; 8.00 m/s, exactly 16-fold).<br><br><em>Distractor Traps:</em><br>&bull; A (Linear Diameter Error): Forgets to square the diameter, assuming velocity scales linearly with D (4-fold).<br>&bull; B (Arithmetic Mean Trap): Arbitrary intermediate value confusing area scaling with flow resistance.<br>&bull; D (Volumetric Cubic Error): Incorrectly scales diameter to the third power (4³ = 64) as if calculating spherical volume."
      },
      {
        "q": "Based on Bernoulli's principle, how does the hydrostatic pressure in the severe stenosis compare to that in the proximal baseline segment (assuming horizontal flow)?",
        "ch": [
          "The hydrostatic pressure increases significantly due to the immense friction of the vessel wall.",
          "The hydrostatic pressure remains unchanged because the volumetric flow rate is strictly conserved.",
          "The hydrostatic pressure increases proportionally with the square of the dynamic blood velocity.",
          "The hydrostatic pressure decreases significantly due to the dramatic increase in fluid velocity."
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: The Venturi Effect and Energy Density Conservation]</strong> In horizontal streamline flow, an increase in fluid velocity necessitates a concomitant decrease in static hydrostatic pressure to conserve total mechanical energy density.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Bernoulli Equation</em>: P₁ + &frac12;&rho;v₁² = P₂ + &frac12;&rho;v₂² (horizontal flow, &Delta;h = 0).<br>2. <em>Kinetic Energy Density Surge</em>: In the stenosis, blood velocity surges from 0.50 m/s to 8.00 m/s, causing kinetic energy density (&frac12;&rho;v²) to increase dramatically.<br>3. <em>Static Pressure Consequence</em>: Because the sum is constant, static lateral wall pressure P₂ must drop precipitously (Venturi effect).<br><br><em>Distractor Traps:</em><br>&bull; A (Intuitive Resistance Fallacy): Common student misconception that 'constriction increases pressure'; constriction increases resistance, but *lateral hydrostatic pressure* drops as kinetic energy rises.<br>&bull; B (Conservation Confusion): Confuses conservation of volumetric flow rate (A₁v₁ = A₂v₂) with constancy of pressure.<br>&bull; C (Direct Inversion): States hydrostatic pressure increases with velocity squared, which violates conservation of energy."
      },
      {
        "q": "What is the pressure drop &Delta;P attributable solely to the change in kinetic energy density between the proximal baseline segment (v₁ = 0.50 m/s) and the severe stenosis (v₂ = 8.00 m/s)?",
        "ch": [
          "1.06 × 10³ Pa",
          "6.75 × 10⁴ Pa",
          "3.38 × 10⁴ Pa",
          "4.24 × 10⁵ Pa"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Dynamic Pressure Drop in Constricted Conduits]</strong> The dynamic pressure loss between two points in horizontal inviscid flow equals the difference in their kinetic energy densities: &Delta;P = &frac12;&rho;(v₂² &minus; v₁²).<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Evaluate Velocity Squares</em>: v₁² = (0.50)² = 0.25 m²/s²; v₂² = (8.00)² = 64.0 m²/s².<br>2. <em>Calculate Velocity Difference</em>: v₂² &minus; v₁² = 64.0 &minus; 0.25 = 63.75 m²/s².<br>3. <em>Multiply by Half Density</em>: &Delta;P = 0.5 &times; (1060 kg/m³) &times; 63.75 m²/s² = 530 &times; 63.75 &asymp; 33,788 Pa = 3.38 &times; 10⁴ Pa.<br><br><em>Distractor Traps:</em><br>&bull; A (Linear Velocity Error): Evaluates &Delta;P = &frac12;&rho;(v₂ &minus; v₁) = 530 &times; 7.50 = 3975 Pa &asymp; 1.06 &times; 10³ Pa, forgetting to square velocities.<br>&bull; B (Omission of Half Factor): Calculates &Delta;P = &rho;(v₂² &minus; v₁²) = 1060 &times; 63.75 = 6.75 &times; 10⁴ Pa, forgetting the factor of &frac12;.<br>&bull; D (Dimensional Scaling Error): Incorrectly computes (v₂ &minus; v₁)² with wrong decimal placement, yielding 4.24 &times; 10⁵ Pa."
      },
      {
        "q": "In the severe stenosis segment, blood flow is expected to transition into post-stenotic turbulence primarily because:",
        "ch": [
          "the fluid density decreases proportionally as blood flow velocity surges.",
          "the dynamic viscosity increases dramatically with local shear strain rate.",
          "the acoustic velocity in human vascular tissue drops below 1540 meters/s.",
          "the Reynolds number (3634) exceeds the critical transition value of 2000."
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Dimensionless Reynolds Criteria for Laminar-to-Turbulent Transition]</strong> Fluid flow in cylindrical vessels becomes turbulent when inertial forces dominate viscous dampening, parameterized by a Reynolds number exceeding ~2000.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Reynolds Formula</em>: Re = (&rho; &times; v &times; D) / &eta;.<br>2. <em>Data Interrogation</em>: Table 1 explicitly reports Re = 3634 for the severe stenosis.<br>3. <em>Physical Threshold</em>: In cylindrical conduits, Re < 2000 indicates laminar flow, whereas Re > 2000–3000 promotes vortex shedding and turbulent eddy formation.<br><br><em>Distractor Traps:</em><br>&bull; A (Incompressibility Violation): Blood is an incompressible liquid whose density remains invariant with velocity.<br>&bull; B (Non-Newtonian Inversion): Blood exhibits shear-thinning (viscosity *decreases* or remains flat at high shear rates, not increases).<br>&bull; C (Domain Mismatch): Acoustic speed of sound in tissue (1540 m/s) governs ultrasound imaging propagation, not fluid hydrodynamics."
      },
      {
        "q": "If the ultrasound sonographer tilts the transducer such that the insonation angle &theta; increases from 60° to 90°, what Doppler shift frequency &Delta;f will be recorded?",
        "ch": [
          "0 kHz",
          "1.62 kHz",
          "3.24 kHz",
          "6.48 kHz"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Trigonometric Insonation Dependence of Doppler Velocimetry]</strong> The recorded Doppler frequency shift is directly proportional to the cosine of the angle between the ultrasound beam axis and blood velocity vector.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Doppler Equation</em>: &Delta;f = (2 &times; f₀ &times; v &times; cos &theta;) / c.<br>2. <em>Evaluate Angle</em>: When the beam is perpendicular to blood flow (&theta; = 90&deg;), cos(90&deg;) = 0.0.<br>3. <em>Calculate Shift</em>: &Delta;f = (2 &times; f₀ &times; v &times; 0) / c = 0 kHz.<br><br><em>Distractor Traps:</em><br>&bull; B (Quarter Shift Error): Confuses cos(90&deg;) with cos(60&deg;)/2, predicting 1.62 kHz.<br>&bull; C (Baseline Preservation Trap): Assumes the baseline 60&deg; Doppler shift (3.24 kHz) remains unchanged regardless of beam angle.<br>&bull; D (Sine/Cosine Confusion): Mistakenly calculates with sin(90&deg;) = 1.0, doubling the apparent frequency shift to 6.48 kHz."
      },
      {
        "q": "If a rigid vessel segment obeyed Poiseuille's law strictly during laminar flow with a fixed pressure gradient &Delta;P, reducing the luminal radius to 1/2 of its initial value would decrease the volumetric flow rate Q by a factor of:",
        "ch": [
          "2-fold",
          "4-fold",
          "8-fold",
          "16-fold"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Fourth-Power Radius Dependence of Hydraulic Conductance]</strong> In Poiseuille flow, volumetric flow rate is extraordinarily sensitive to luminal caliber, scaling with the fourth power of vessel radius.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Poiseuille Equation</em>: Q = (&pi; &times; &Delta;P &times; r⁴) / (8 &times; &eta; &times; L).<br>2. <em>Apply Perturbation</em>: If r_new = r / 2, then r_new⁴ = (r/2)⁴ = r⁴ / 16.<br>3. <em>Deduction</em>: Flow rate Q decreases to 1/16 of its initial value (a 16-fold reduction).<br><br><em>Distractor Traps:</em><br>&bull; A (Linear Radius Error): Assumes flow rate is directly proportional to radius r (2-fold).<br>&bull; B (Cross-Sectional Area Trap): Scales flow rate with cross-sectional area &pi;r² (2² = 4-fold).<br>&bull; C (Cubic Scaling Trap): Scales flow rate with three-dimensional volume r³ (2³ = 8-fold)."
      }
    ]
  },
  {
    "id": "exam_cp90_p3",
    "sec": "C/P",
    "topic": "Organic synthesis, S_NAr mechanisms, and spectroscopy",
    "sheet": 19,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90",
    "passage": "<div class=\"ttl\">Passage 3 (Questions 13&ndash;18)</div>\n<p>Receptor tyrosine kinases (RTKs) are frequently mutated or overexpressed in solid tumors. Chemists designed Compound <b>5</b>, a potent small-molecule competitive inhibitor targeting the ATP-binding pocket of an oncogenic RTK. The convergent synthetic route is outlined in Scheme 1.</p>\n<p style=\"text-align:center;font-family:monospace;background:#F7F9FB;padding:8px;border:1px solid #D0D7DE;font-size:13px\">\nCompound 1 (4-chloropyrimidine-2-amine) + Compound 2 (4-(morpholinomethyl)aniline)<br>\n&darr; <i>iPr₂NEt, n-BuOH, 110 &deg;C (Yield: 84%)</i><br>\nIntermediate 3 &rarr; bromination (NBS, DMF, 0 &deg;C) &rarr; Intermediate 4<br>\n&darr; <i>Suzuki-Miyaura coupling: PhB(OH)₂, Pd(PPh₃)₄, K₂CO₃, 1,4-dioxane/H₂O, 90 &deg;C (Yield: 76%)</i><br>\nTarget Compound 5\n</p>\n<p>In Step 1, nucleophilic aromatic substitution (S<sub>N</sub>Ar) of Compound <b>1</b> by the primary aromatic amine of Compound <b>2</b> occurs selectively at the 4-position rather than the 2-amino position. Reaction monitoring by proton nuclear magnetic resonance (<sup>1</sup>H-NMR) and Fourier-transform infrared (FT-IR) spectroscopy showed the disappearance of the primary amine stretch at 3450 cm<sup>&minus;1</sup> and the emergence of a broad secondary amine stretch at 3310 cm<sup>&minus;1</sup>.</p>\n<p>To verify the stereochemical purity and solution conformation, optical rotation was measured on a polarimeter ([&alpha;]<sub>D</sub><sup>25</sup> = 0.00&deg; for all synthetic intermediates). In vitro inhibition assays against wild-type RTK and the gatekeeper mutant (T790M) yielded the IC<sub>50</sub> values in Table 1.</p>\n<table>\n<tr><th>Inhibitor</th><th>RTK WT IC<sub>50</sub> (nM)</th><th>RTK T790M IC<sub>50</sub> (nM)</th><th>Log <i>P</i> (octanol/water)</th><th>Polar Surface Area (&Aring;<sup>2</sup>)</th></tr>\n<tr><td>Compound 5</td><td class=\"n\">4.2</td><td class=\"n\">8.6</td><td class=\"n\">2.4</td><td class=\"n\">68.5</td></tr>\n<tr><td>Analog 5a (morpholine &rarr; piperidine)</td><td class=\"n\">3.8</td><td class=\"n\">9.1</td><td class=\"n\">3.5</td><td class=\"n\">59.3</td></tr>\n<tr><td>Analog 5b (des-phenyl)</td><td class=\"n\">420.0</td><td class=\"n\">1150.0</td><td class=\"n\">1.6</td><td class=\"n\">68.5</td></tr>\n</table>\n<p class=\"cap\"><b>Table 1</b> Pharmacological profile and physicochemical metrics of Compound 5 and analogs.</p>",
    "qs": [
      {
        "q": "The nucleophilic aromatic substitution (S_NAr) in Step 1 proceeds via which characteristic intermediate?",
        "ch": [
          "A planar aryl carbocation generated by the spontaneous heterolytic loss of chloride.",
          "A resonance-stabilized Meisenheimer complex carrying negative charge in the ring.",
          "A highly strained cyclic benzyne intermediate formed via concerted elimination.",
          "A neutral free-radical aryl intermediate stabilized by a diisopropylethylamine base."
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Addition-Elimination Mechanism in Electron-Deficient Arenes]</strong> S_NAr requires strongly electron-withdrawing ortho/para substituents that stabilize a tetrahedral anionic cyclohexadienyl intermediate (Meisenheimer complex).<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Reagent Analysis</em>: Compound 1 features a pyrimidine ring with an electron-withdrawing nitro/carboxylate group and a 4-chloro leaving group.<br>2. <em>Nucleophilic Addition</em>: Amine attack occurs at the ipso carbon, generating an sp³-hybridized, resonance-stabilized carbanion (Meisenheimer complex).<br>3. <em>Elimination</em>: Expulsion of chloride restores aromaticity. Aryl carbocations (SN1) and benzynes (elimination-addition) do not form under these mild conditions.<br><br><em>Distractor Traps:</em><br>&bull; A (SN1 Aryl Cation Fallacy): Aryl carbocations are extremely unstable sp-hybridized species that do not form in S_NAr reactions.<br>&bull; C (Elimination-Addition Trap): Benzyne intermediates require extremely strong bases (e.g. NaNH₂ in liquid NH₃), not mild tertiary amines like DIPEA.<br>&bull; D (Radical Confabulation): S_NAr is a two-electron polar addition-elimination process, not a radical mechanism."
      },
      {
        "q": "Which feature of the infrared spectrum uniquely confirms that Compound 2 successfully coupled via its aniline nitrogen rather than the morpholine ring?",
        "ch": [
          "Shift from a primary amine N–H doublet to a single secondary amine band at 3310 cm⁻¹.",
          "Appearance of a sharp carbonyl ester stretching frequency centered near 1715 cm⁻¹.",
          "Complete disappearance of the aliphatic C–H stretching bands at 2850 to 2950 cm⁻¹.",
          "Emergence of an intense and broad hydroxyl O–H stretching band centered near 3200 cm⁻¹."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Diagnostic Vibrational Modes of Primary and Secondary Amines]</strong> Primary amines exhibit two N–H stretching peaks (symmetric and asymmetric), whereas secondary amines exhibit exactly one N–H stretch.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Starting Material Inspection</em>: Compound 2 has an aniline primary amine (–NH₂) exhibiting two diagnostic N–H stretching bands (3450 and 3350 cm⁻¹).<br>2. <em>Post-Coupling Transformation</em>: Nucleophilic attack of the aniline nitrogen converts it into a secondary aryl amine (–NH–Ar), which exhibits a single N–H stretching band.<br>3. <em>Morpholine Invariance</em>: Morpholine is already a tertiary amine in the product and has no N–H stretch; thus, conversion of a doublet to a singlet uniquely pinpoints aniline coupling.<br><br><em>Distractor Traps:</em><br>&bull; B (Carbonyl Unrelatedness): Carbonyl stretches do not distinguish between primary and secondary amine functionalization.<br>&bull; C (Aliphatic Invariance): The aliphatic C–H bonds of the morpholine ring remain fully present in the coupled product.<br>&bull; D (Hydroxyl Confabulation): No alcohol or hydroxyl group is created during the amine coupling reaction."
      },
      {
        "q": "Why is the observed specific optical rotation [&alpha;] equal to 0.00° for pure Compound 5 in solution?",
        "ch": [
          "Compound 5 contains an equimolar mixture of diastereomeric atropisomers that cancel.",
          "The dimethyl sulfoxide solvent undergoes mutarotation that quenches optical activity.",
          "Rapid nitrogen inversion in the morpholine ring converts a meso isomer into a racemate.",
          "Compound 5 lacks stereocenters and is an achiral molecule with a plane of symmetry."
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Molecular Symmetry Criteria for Optical Inactivity]</strong> A molecule is optically active only if it is chiral (non-superimposable on its mirror image); molecules lacking stereocenters and possessing internal planes of symmetry are achiral and optically inactive.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Stereocenter Audit</em>: Compound 5 consists of planar aromatic rings (pyrimidine, phenyl) and a symmetrical morpholine ring lacking asymmetric carbons.<br>2. <em>Symmetry Evaluation</em>: The molecule possesses an internal plane of reflection and lacks restricted rotational hindrance (atropisomerism).<br>3. <em>Deduction</em>: Pure achiral molecules cannot rotate plane-polarized light, yielding an observed [&alpha;] = 0.00&deg;.<br><br><em>Distractor Traps:</em><br>&bull; A (Atropisomer Confabulation): The single biaryl bond lacks the bulky ortho-tetrasubstitution necessary to restrict rotation into atropisomers.<br>&bull; B (Solvent Fiction): DMSO is an achiral solvent and does not undergo mutarotation (which is specific to reducing sugars).<br>&bull; C (Amine Inversion Confusion): Nitrogen inversion occurs in tertiary amines, but does not convert meso compounds into racemates in an inherently achiral molecule."
      },
      {
        "q": "Based on Table 1, the 100-fold loss of potency in Analog 3b (IC₅₀ = 420 nM vs 4.2 nM in parent) when replacing –OCH₃ with –H indicates that the methoxy group:",
        "ch": [
          "serves exclusively as a hydrophobic steric shield protecting the ester from hydrolysis.",
          "undergoes metabolic oxidation in situ to form a covalent adduct with active site residues.",
          "participates in an essential hydrogen-bonding or electronic interaction with the kinase.",
          "is required to accelerate the rate of nucleophilic aromatic substitution in the enzyme."
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Structure-Activity Relationships in Targeted Kinase Inhibition]</strong> Selective loss of inhibitory potency upon removing a functional group reveals the critical binding interactions mediated by that pharmacophore motif.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Analog 3b lacks the 3-methoxy substituent and displays a 100-fold increase in IC₅₀ (4.2 &rarr; 420 nM), reflecting a two orders-of-magnitude reduction in binding affinity.<br>2. <em>Binding Analysis</em>: A methoxy group acts as a hydrogen-bond acceptor via its ether oxygen and donates electron density into the phenyl ring via resonance.<br>3. <em>Conclusion</em>: Removing it strips the inhibitor of a critical binding contact within the ATP-binding pocket.<br><br><em>Distractor Traps:</em><br>&bull; A (Steric Shield Trap): In vitro enzyme assays measure direct kinase inhibition, not pharmacokinetic esterase degradation.<br>&bull; B (Covalent Zinc Fiction): Kinases utilize ATP and Mg²⁺, not catalytic zinc; nor do methoxy groups undergo covalent hydroxylation with metals.<br>&bull; D (Reaction Mode Error): The inhibitor acts via non-covalent binding to the kinase target, not by undergoing S_NAr with the enzyme."
      },
      {
        "q": "In the Suzuki-Miyaura cross-coupling step, what role does the aqueous base (K₂CO₃) play in the catalytic cycle?",
        "ch": [
          "It coordinates the boronic acid to form an activated organoborate for transmetalation.",
          "It oxidizes palladium(0) to palladium(II) to initiate oxidative addition with halide.",
          "It serves as a phase-transfer catalyst that accelerates reductive elimination of product.",
          "It acts as a Brønsted acid that protonates the leaving group to enhance its departure."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Base Activation of Boronic Acids in Suzuki Transmetalation]</strong> Organoboronic acids are poor nucleophiles that cannot undergo transmetalation until coordinated by a base to form an anionic, electron-rich 'ate' complex.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Catalytic Cycle Progression</em>: (1) Oxidative addition of aryl halide to Pd(0) yields Ar–Pd(II)–X; (2) Transmetalation transfers the organic group from boron to palladium; (3) Reductive elimination yields product and regenerates Pd(0).<br>2. <em>The Role of Base</em>: Neutral organoboronic acids [R–B(OH)₂] have empty p-orbitals. Hydroxide or carbonate coordinates to boron, forming a tetrahedral [R–B(OH)₃]⁻ ate complex, increasing nucleophilicity and facilitating transfer of the R group to Pd(II).<br>3. <em>Selection</em>: Choice A accurately defines this essential mechanistic step.<br><br><em>Distractor Traps:</em><br>&bull; B (Redox Inversion): The aryl halide, not base, oxidizes Pd(0) to Pd(II) during oxidative addition.<br>&bull; C (Catalytic Misclassification): K₂CO₃ is an inorganic salt, not a phase-transfer catalyst; nor does it directly catalyze reductive elimination.<br>&bull; D (Acid/Base Inversion): K₂CO₃ is a base, not a Brønsted acid, and cannot protonate leaving groups."
      },
      {
        "q": "Analog 5a replaces the morpholine ring with a piperidine ring (replacing –O– with –CH₂–). This modification will most likely:",
        "ch": [
          "increase the aqueous solubility of the compound by enhancing hydrogen bonding.",
          "cause the piperidine nitrogen to permanently lose its basic nucleophilic character.",
          "eliminate all inhibitory potency by preventing coordination to catalytic zinc.",
          "decrease the aqueous solubility of the compound while increasing lipophilicity."
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Heteroatomic Contributions to Aqueous Solvation and Lipophilicity]</strong> Replacing an electronegative hydrogen-bond-accepting ether oxygen with a non-polar methylene group increases hydrophobicity and reduces aqueous solubility.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Structural Comparison</em>: Morpholine contains an oxygen atom that participates in dipole-dipole interactions and hydrogen bonding with water.<br>2. <em>Physicochemical Shift</em>: Piperidine replaces this oxygen with a –CH₂– unit, removing a hydrogen-bond acceptor.<br>3. <em>Pharmacological Consequence</em>: The compound becomes more hydrophobic/lipophilic (higher LogP) and less soluble in aqueous buffers.<br><br><em>Distractor Traps:</em><br>&bull; A (Direct Inversion): Piperidine lacks the ether oxygen, reducing hydrogen-bonding capacity with solvent water.<br>&bull; B (Electronic Fallacy): Piperidine is actually slightly *more* basic than morpholine because it lacks the electron-withdrawing oxygen atom.<br>&bull; C (Kinase Mechanism Error): Target kinase binding does not rely on coordination to catalytic zinc."
      }
    ]
  },
  {
    "id": "exam_cp90_p4",
    "sec": "C/P",
    "topic": "Electrochemistry and fast-scan cyclic voltammetry",
    "sheet": 15,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90",
    "passage": "<div class=\"ttl\">Passage 4 (Questions 19&ndash;24)</div>\n<p>In vivo electrochemical detection of neurotransmitters utilizes carbon-fiber microelectrodes (CFMEs) coupled with fast-scan cyclic voltammetry (FSCV). Dopamine (DA), a catecholamine neurotransmitter, undergoes a quasi-reversible two-electron, two-proton oxidation to dopamine-o-quinone (DAQ) at positive potentials:</p>\n<p style=\"text-align:center;font-style:italic\">DA &rightleftharpoons; DAQ + 2 H<sup>+</sup> + 2 e<sup>&minus;</sup> &nbsp;&nbsp;&nbsp;&nbsp;(E&deg; = +0.13 V vs. Ag/AgCl)</p>\n<p>The standard cell potential <i>E</i>&deg;<sub>cell</sub> and standard free energy &Delta;<i>G</i>&deg; are related by &Delta;<i>G</i>&deg; = &minus;<i>nFE</i>&deg;<sub>cell</sub>, where <i>F</i> = 96,485 C/mol e<sup>&minus;</sup>. In FSCV, the potential of the CFME working electrode is ramped linearly from a resting holding potential of &minus;0.40 V to a switching potential of +1.30 V and back to &minus;0.40 V at a scan rate of 400 V/s.</p>\n<p>Ascorbic acid (AA) is present in extracellular fluid at 500-fold higher concentrations than DA (~200 &mu;M vs. ~1 &mu;M) and oxidizes at approximately +0.15 V vs. Ag/AgCl via an irreversible 2e<sup>&minus;</sup>/2H<sup>+</sup> process:</p>\n<p style=\"text-align:center;font-style:italic\">Ascorbate &rarr; Dehydroascorbate + 2 H<sup>+</sup> + 2 e<sup>&minus;</sup></p>\n<p>To eliminate ascorbate interference, electrodes are coated with Nafion, a sulfonated fluoropolymer carrying fixed negative charges (SO<sub>3</sub><sup>&minus;</sup>) at physiological pH (7.4). The electroactive surface area <i>A</i> of the cylindrical CFME is 1.5 &times; 10<sup>&minus;4</sup> cm<sup>2</sup>. The peak oxidation current <i>i</i><sub>p</sub> is governed by the Randles-Sevcik equation for a diffusion-controlled reversible process: <i>i</i><sub>p</sub> = (2.69 &times; 10<sup>5</sup>) <i>n</i><sup>3/2</sup> <i>A</i> <i>D</i><sup>1/2</sup> <i>C</i> <i>v</i><sup>1/2</sup>.</p>\n<table>\n<tr><th>Analyte</th><th>Physiological [C] (&mu;M)</th><th>Charge at pH 7.4</th><th>Bare CFME Peak Current (&mu;A)</th><th>Nafion-Coated CFME Peak Current (&mu;A)</th></tr>\n<tr><td>Dopamine (DA)</td><td class=\"n\">1.0</td><td class=\"n\">+1</td><td class=\"n\">0.12</td><td class=\"n\">0.24</td></tr>\n<tr><td>Ascorbic Acid (AA)</td><td class=\"n\">250.0</td><td class=\"n\">&minus;1</td><td class=\"n\">14.80</td><td class=\"n\">0.02</td></tr>\n<tr><td>3,4-Dihydroxyphenylacetic acid (DOPAC)</td><td class=\"n\">15.0</td><td class=\"n\">&minus;1</td><td class=\"n\">1.10</td><td class=\"n\">0.01</td></tr>\n</table>\n<p class=\"cap\"><b>Table 1</b> Voltammetric responses of bare vs. Nafion-coated CFMEs at pH 7.4.</p>",
    "qs": [
      {
        "q": "What is the standard free energy change &Delta;G° for the two-electron oxidation of dopamine at standard conditions (E° = +0.18 V)? (Use F = 96,500 C/mol).",
        "ch": [
          "-69.5 kJ/mol",
          "-34.7 kJ/mol",
          "+34.7 kJ/mol",
          "+69.5 kJ/mol"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Thermodynamic Coupling of Electrochemical Potentials]</strong> The standard Gibbs free energy change of a redox reaction is related to cell potential by &Delta;G&deg; = &minus;nFE&deg;.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Identify Variables</em>: n = 2 electrons; F = 96,500 C/mol; E&deg; = +0.18 V.<br>2. <em>Calculate Energy in Joules</em>: &Delta;G&deg; = &minus;(2) &times; (96,500 C/mol) &times; (+0.18 J/C) = &minus;34,740 J/mol.<br>3. <em>Convert to Kilojoules</em>: &minus;34.74 kJ/mol &asymp; &minus;34.7 kJ/mol.<br><br><em>Distractor Traps:</em><br>&bull; A (Double Electron Trap): Multiplies by n = 4, yielding &minus;69.5 kJ/mol.<br>&bull; C (Sign Inversion Error): Forgets the negative sign in &Delta;G&deg; = &minus;nFE&deg;, yielding +34.7 kJ/mol.<br>&bull; D (Compound Sign and Stoichiometry Error): Both inverts the thermodynamic sign and doubles the electron count (+69.5 kJ/mol)."
      },
      {
        "q": "Why does coating the carbon-fiber microelectrode with a Nafion fluoropolymer membrane selectively attenuate ascorbic acid interference during dopamine detection?",
        "ch": [
          "Nafion contains positively charged quaternary amines that selectively bind dopamine cations.",
          "Nafion possesses negatively charged sulfonate groups that electrostatically repel ascorbate.",
          "Ascorbic acid is too sterically bulky to permeate through the fluoropolymer pore matrix.",
          "Nafion catalytically oxidizes ascorbic acid to dehydroascorbic acid before it touches carbon."
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Charge-Selective Electrostatic Permeation in Biosensors]</strong> Ion-exchange polymer coatings exclude interfering analytes based on charge complementarity with fixed functional groups.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Physiological Speciation</em>: At pH 7.4, ascorbic acid (pKa = 4.2) exists as an anion (ascorbate⁻), whereas dopamine (pKa = 8.9) exists as a cation (dopamine⁺).<br>2. <em>Membrane Chemistry</em>: Nafion is a sulfonated tetrafluoroethylene polymer decorated with fixed, negatively charged sulfonate groups (–SO₃⁻).<br>3. <em>Electrostatic Discrimination</em>: Anionic ascorbate is electrostatically repelled from the electrode surface, while cationic dopamine easily partitions across the membrane.<br><br><em>Distractor Traps:</em><br>&bull; A (Chemical Inversion): Nafion contains anionic sulfonates, not cationic quaternary ammonium groups.<br>&bull; C (Size-Exclusion Error): Ascorbate (MW ~176) and dopamine (MW ~153) are virtually identical in molecular size; exclusion is electrostatic, not steric.<br>&bull; D (Enzymatic Confabulation): Nafion is an inert polyfluorinated membrane, not a redox catalyst."
      },
      {
        "q": "In fast-scan cyclic voltammetry governed by semi-infinite linear diffusion, quadrupling the scan rate v from 100 V/s to 400 V/s will increase the peak oxidation current i_p by a factor of:",
        "ch": [
          "2-fold",
          "4-fold",
          "8-fold",
          "16-fold"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Square-Root Scan Rate Dependence of Diffusional Voltammetric Current]</strong> The Randles-Sevcik relationship establishes that peak diffusion-controlled current scales with the square root of scan rate: i_p &prop; &radic;v.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Mathematical Relation</em>: i_p = 0.4463 &times; nFAC &times; &radic;[(nFvD) / (RT)], demonstrating that i_p &prop; &radic;v.<br>2. <em>Apply Quadrupling</em>: If v_new = 4 &times; v_old, then &radic;(v_new) = &radic;(4 &times; v_old) = 2 &times; &radic;(v_old).<br>3. <em>Conclusion</em>: Peak current i_p increases by exactly a factor of 2 (2-fold).<br><br><em>Distractor Traps:</em><br>&bull; B (Linear Scaling Fallacy): Assumes current is directly proportional to scan rate (4-fold), which applies only to surface-adsorbed species.<br>&bull; C (Intermediate Power Error): Confuses square-root dependence with fractional exponential scaling.<br>&bull; D (Quadratic Scaling Fallacy): Squares the scan rate factor (4² = 16-fold), inverting the true root relationship."
      },
      {
        "q": "During cyclic voltammetry, when the electrode potential is swept in the reverse (cathodic) direction, the observed reduction peak corresponds to the:",
        "ch": [
          "reduction of dissolved molecular oxygen to hydrogen peroxide at the electrode.",
          "reduction of oxidized carbon surface functional groups to phenolic alcohols.",
          "two-electron reduction of dopamine-o-quinone back to regenerated dopamine.",
          "electrochemical reduction of zinc cations present in the extracellular buffer."
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Reversibility and Mass Transport in Cyclic Voltammetry]</strong> In a reversible or quasi-reversible redox couple, species oxidized during the forward anodic sweep remain near the diffusion layer and are reduced during the reverse cathodic sweep.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Forward Anodic Sweep</em>: Dopamine is oxidized at the carbon surface to dopamine-o-quinone (DOQ) with loss of 2 electrons and 2 protons.<br>2. <em>Reverse Cathodic Sweep</em>: As the potential sweeps back negatively, DOQ remaining in the immediate diffusion layer accepts 2 electrons and 2 protons.<br>3. <em>Deduction</em>: The cathodic current peak is the specific reduction of dopamine-o-quinone back to dopamine.<br><br><em>Distractor Traps:</em><br>&bull; A (Background Solvent Interference): Oxygen reduction occurs at substantially more negative potentials and is subtracted out via background subtraction.<br>&bull; B (Electrode Surface Background): Carbon surface oxide transitions contribute to the capacitive background current, not the analyte faradaic peak.<br>&bull; D (Extraneous Metal Trap): Extracellular buffer does not contain electroactive zinc ions in this voltammetric paradigm."
      },
      {
        "q": "According to the Nernst equation at 298 K, if the ratio [Ox]/[Red] for a two-electron redox couple increases by a factor of 10, the electrode equilibrium potential E will shift by:",
        "ch": [
          "+14.8 mV",
          "+29.6 mV",
          "+59.2 mV",
          "+118.4 mV"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Logarithmic Nernstian Dependence on Reaction Quotients]</strong> The equilibrium electrode potential varies linearly with the base-10 logarithm of the redox ratio, modulated inversely by the electron stoichiometry n.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Nernst Equation</em>: E = E&deg; + (0.0592 V / n) &times; log([Ox]/[Red]) at 298 K.<br>2. <em>Evaluate Tenfold Shift</em>: If [Ox]/[Red] increases by 10, log(10) = 1.0.<br>3. <em>Calculate Potential Shift</em>: &Delta;E = (0.0592 V / 2) &times; 1.0 = +0.0296 V = +29.6 mV.<br><br><em>Distractor Traps:</em><br>&bull; A (Quarter Scaling Trap): Divides 0.0592 V by n = 4, yielding +14.8 mV.<br>&bull; C (Single-Electron Trap): Forgets to divide by n = 2 electrons, assuming an n = 1 process (+59.2 mV).<br>&bull; D (Multiplicative Electron Trap): Multiplies 0.0592 V by n = 2 rather than dividing by n (+118.4 mV)."
      },
      {
        "q": "A researcher applies a constant oxidizing potential of +0.60 V to a microelectrode for 10 seconds, recording a steady Faradaic current of 19.3 nA. How many moles of dopamine were oxidized during this period? (Use F = 96,500 C/mol).",
        "ch": [
          "1.0 × 10⁻¹² mol",
          "2.0 × 10⁻¹² mol",
          "1.0 × 10⁻⁹ mol",
          "2.0 × 10⁻⁹ mol"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Quantitative Coulometry and Faraday's Law of Electrolysis]</strong> Total charge passed is the time integral of electric current, directly proportional to the moles of chemical substance transformed: Q = I &times; t = n &times; N &times; F.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Calculate Total Charge Q</em>: Q = I &times; t = (19.3 &times; 10⁻⁹ A) &times; (10 s) = 1.93 &times; 10⁻⁷ Coulombs.<br>2. <em>Apply Faraday's Formula</em>: Moles of substance N = Q / (n &times; F).<br>3. <em>Compute Moles</em>: N = (1.93 &times; 10⁻⁷ C) / (2 &times; 96,500 C/mol) = (1.93 &times; 10⁻⁷) / (1.93 &times; 10⁵) = 1.0 &times; 10⁻¹² mol.<br><br><em>Distractor Traps:</em><br>&bull; B (Single Electron Error): Forgets that dopamine oxidation is a 2-electron process (dividing by n=1 gives 2.0 &times; 10⁻¹² mol).<br>&bull; C (Time Omission Error): Omits the 10-second duration and miscalculates decimal orders of magnitude (1.0 &times; 10⁻⁹ mol).<br>&bull; D (Compound Stoichiometric Error): Combines the n=1 error with exponential miscalculation (2.0 &times; 10⁻⁹ mol)."
      }
    ]
  },
  {
    "id": "exam_cp90_p5",
    "sec": "C/P",
    "topic": "Thermodynamic vs kinetic control in enolate reactions",
    "sheet": 21,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90",
    "passage": "<div class=\"ttl\">Passage 5 (Questions 25&ndash;30)</div>\n<p>In organic synthesis, the regiochemical outcome of ketone deprotonation is dictated by the competition between kinetic and thermodynamic enolates. 2-Methylcyclohexanone contains two non-equivalent &alpha;-carbons: the less hindered secondary C6 carbon and the more hindered tertiary C2 carbon.</p>\n<p>Deprotonation at C6 yields the kinetic enolate (<b>K</b>), which forms more rapidly due to lower steric hindrance in the transition state. Deprotonation at C2 yields the thermodynamic enolate (<b>T</b>), which produces a more highly substituted, more stable alkene. The reaction coordinate diagrams reveal that the activation free energy &Delta;<i>G</i><sup>&Dagger;</sup><sub>K</sub> < &Delta;<i>G</i><sup>&Dagger;</sup><sub>T</sub>, but the standard free energy of the products &Delta;<i>G</i>&deg;<sub>T</sub> < &Delta;<i>G</i>&deg;<sub>K</sub>.</p>\n<p>Investigators treated 2-methylcyclohexanone with two distinct bases: lithium diisopropylamide (LDA, a bulky, strong, non-nucleophilic base, p<i>K</i><sub>a</sub> of conjugate acid &asymp; 36) and potassium <i>tert</i>-butoxide (KO<i>t</i>Bu, p<i>K</i><sub>a</sub> &asymp; 17) in various solvents and temperatures. Following enolate generation, the mixtures were quenched with chlorotrimethylsilane (TMSCl) to trap the corresponding enol ethers, and the product ratios were quantified by gas chromatography-mass spectrometry (GC-MS).</p>\n<table>\n<tr><th>Entry</th><th>Base</th><th>Solvent</th><th>Temperature (&deg;C)</th><th>Equilibration Time</th><th>Ratio <b>K</b> : <b>T</b> (%)</th></tr>\n<tr><td>1</td><td>LDA (1.1 eq)</td><td>THF</td><td class=\"n\">&minus;78</td><td class=\"n\">15 min</td><td>99 : 1</td></tr>\n<tr><td>2</td><td>LDA (1.1 eq)</td><td>THF</td><td class=\"n\">25</td><td class=\"n\">24 h</td><td>65 : 35</td></tr>\n<tr><td>3</td><td>KO<i>t</i>Bu (1.1 eq)</td><td><i>t</i>BuOH</td><td class=\"n\">25</td><td class=\"n\">2 h</td><td>15 : 85</td></tr>\n<tr><td>4</td><td>KO<i>t</i>Bu (1.1 eq)</td><td><i>t</i>BuOH</td><td class=\"n\">80</td><td class=\"n\">4 h</td><td>5 : 95</td></tr>\n<tr><td>5</td><td>LDA (0.9 eq)</td><td>THF</td><td class=\"n\">&minus;78</td><td class=\"n\">3 h</td><td>70 : 30</td></tr>\n</table>\n<p class=\"cap\"><b>Table 1</b> Enolate trapping experiments with 2-methylcyclohexanone.</p>",
    "qs": [
      {
        "q": "Why does Entry 1 (LDA, THF, −78 °C) yield exclusively the kinetic enolate K (99:1 ratio)?",
        "ch": [
          "At −78 °C, the reaction is under thermodynamic control favoring the most stable enolate.",
          "LDA coordinates directly to the carbonyl oxygen, forming an irreversible hemiketal bond.",
          "The thermodynamic enolate is unstable below 0 °C and undergoes spontaneous ring cleavage.",
          "The bulky diisopropylamide base deprotonates the less hindered C6 proton more rapidly."
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Kinetic vs Thermodynamic Control in Enolate Deprotonation]</strong> A sterically hindered, strong base at cryogenic temperatures selectively removes the most sterically accessible alpha-proton under irreversible, non-equilibrating conditions.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Reagent Sterics</em>: Lithium diisopropylamide (LDA) possesses two bulky isopropyl groups that encounter high steric hindrance when approaching the more substituted C2 carbon.<br>2. <em>Kinetic Barrier</em>: Deprotonation at the less hindered C6 methylene carbon proceeds with a significantly lower activation energy (Ea_kin < Ea_therm), forming enolate K faster.<br>3. <em>Irreversibility</em>: At &minus;78 &deg;C in aprotic THF, there is no proton source to allow equilibration back to the starting ketone, trapping the kinetic product.<br><br><em>Distractor Traps:</em><br>&bull; A (Regime Inversion): Low temperature enforces kinetic control, not thermodynamic control; thermodynamic control favors the lowest free energy product at elevated temperatures.<br>&bull; B (Mechanism Confabulation): LDA acts as a Brønsted base to deprotonate the alpha position, not as a nucleophile forming a covalent hemiketal.<br>&bull; C (Decomposition Fiction): The thermodynamic enolate is stable once formed and does not undergo spontaneous ring cleavage below 0 &deg;C."
      },
      {
        "q": "In Entry 5, using a slight sub-stoichiometric amount of LDA (0.9 equivalents) at −78 °C eroded the kinetic ratio from 99:1 to 70:30. What caused this equilibration despite the low temperature?",
        "ch": [
          "Lithium diisopropylamide decomposes into gaseous propene and ammonia through beta-elimination.",
          "Excess chlorotrimethylsilane catalyzes the rapid retro-aldol isomerization between enolates.",
          "Unreacted ketone (0.1 eq) acts as a proton shuttle, enabling reversible enolate equilibration.",
          "The kinetic enolate tautomerizes directly into the thermodynamic enolate via 1,3-hydride shift."
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Proton-Shuttle Equilibration in Sub-Stoichiometric Deprotonation]</strong> When a strong base is present in sub-stoichiometric amounts, unreacted neutral carbonyl molecules remain in solution, serving as weak acids that exchange protons with enolates to establish thermodynamic equilibrium.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Mass Balance Assessment</em>: Adding 0.9 equivalents of LDA deprotonates 90% of the ketone to form kinetic enolate K, leaving 10% unreacted neutral ketone.<br>2. <em>Proton Exchange Mechanism</em>: Kinetic enolate K can abstract an alpha-proton from the unreacted ketone (specifically at C2), generating the more stable thermodynamic enolate T and regenerating a ketone.<br>3. <em>Outcome</em>: Even at &minus;78 &deg;C, this intermolecular proton shuttle bypasses the high activation barrier, steadily isomerizing K into T.<br><br><em>Distractor Traps:</em><br>&bull; A (Reagent Decomposition Fiction): LDA is stable in THF at &minus;78 &deg;C and does not decompose into propene and ammonia.<br>&bull; B (Reagent Role Error): TMSCl acts as an electrophilic trapping agent (silylating enolates), not as a retro-aldol catalyst.<br>&bull; D (Symmetry-Forbidden Pericyclic Shift): Direct intramolecular 1,3-hydride shifts are geometrically constrained and symmetry-forbidden under orbital rules."
      },
      {
        "q": "Thermodynamic enolate T is more stable than kinetic enolate K primarily because:",
        "ch": [
          "the formal negative charge resides entirely on the more electronegative carbon atom.",
          "it adopts an ideal chair conformation with an axial methyl group on the six-ring.",
          "it is aromatic and completely satisfies Hückel's 4n+2 cyclic conjugation rule.",
          "it contains a more highly substituted (tetrasubstituted) carbon–carbon double bond."
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Hyperconjugative and Orbital Stabilization of Substituted Alkenes]</strong> Enolates are resonance hybrids with substantial alkene character; more highly substituted carbon-carbon double bonds are thermodynamically favored due to hyperconjugation.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Structural Comparison</em>: Kinetic enolate K has a double bond between C1 and C6 (trisubstituted alkene). Thermodynamic enolate T has a double bond between C1 and C2 (tetrasubstituted alkene with two methyl groups).<br>2. <em>Electronic Stabilization</em>: Alkyl groups donate electron density into the &pi;* antibonding orbitals via hyperconjugation (&sigma;C–H &rarr; &pi;*), lowering the electronic ground state energy of the tetrasubstituted alkene.<br>3. <em>Conclusion</em>: Enolate T possesses greater thermodynamic stability because its C=C bond is tetrasubstituted.<br><br><em>Distractor Traps:</em><br>&bull; A (Resonance Inversion): In enolates, the major resonance contributor places negative charge on the more electronegative *oxygen* atom, not carbon.<br>&bull; B (Conformational Instability): Axial substituents experience destabilizing 1,3-diaxial steric strain, not stabilization.<br>&bull; C (Aromaticity Fabrication): Cyclic enolates are non-aromatic; they lack a continuous cyclic conjugated 4n+2 pi-system."
      },
      {
        "q": "For the equilibration between K and T at 298 K in Entry 4 (95% T and 5% K at equilibrium), what is the approximate standard free energy difference &Delta;G° = G°_T − G°_K? (Note: R = 8.314 J/(mol·K), ln(19) ≈ 2.94).",
        "ch": [
          "-24.5 kJ/mol",
          "-7.3 kJ/mol",
          "-2.4 kJ/mol",
          "+7.3 kJ/mol"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Thermodynamic Free Energy and Equilibrium Constants]</strong> The standard free energy difference between two interconverting species is related to their equilibrium constant by &Delta;G&deg; = &minus;RT ln(K_eq).<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Calculate K_eq</em>: For the reaction K &rightleftharpoons; T, K_eq = [T] / [K] = 95% / 5% = 19.<br>2. <em>Formula Setup</em>: &Delta;G&deg; = &minus;RT ln(K_eq) = &minus;(8.314 J/(mol&middot;K)) &times; (298 K) &times; ln(19).<br>3. <em>Compute Product</em>: &Delta;G&deg; &asymp; &minus;(2478 J/mol) &times; (2.94) &asymp; &minus;7,285 J/mol &asymp; &minus;7.3 kJ/mol.<br><br><em>Distractor Traps:</em><br>&bull; A (Factor of 10 Exaggeration): Incorrectly scales the free energy to &minus;24.5 kJ/mol.<br>&bull; C (Log-e vs Log-10 Confusion): Divides by 2.303 or evaluates log10(19) without natural log factor (&minus;2.4 kJ/mol).<br>&bull; D (Sign Inversion Error): Omits the negative sign in &Delta;G&deg; = &minus;RT ln(K_eq), producing +7.3 kJ/mol (predicting non-spontaneous equilibrium favoring K)."
      },
      {
        "q": "If the trapped silyl enol ether of kinetic enolate K is treated with ozone followed by dimethyl sulfide (O₃, then Me₂S), what functional groups will be present in the final product?",
        "ch": [
          "An aldehyde and a ketone in a single cleaved molecule.",
          "A carboxylic acid and a free secondary aliphatic alcohol.",
          "An ester and a cyclic alpha,beta-unsaturated enone motif.",
          "Two separate terminal dicarboxylic acid derivative units."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Reductive Ozonolysis of Silyl Enol Ethers]</strong> Ozonolysis of an endocyclic silyl enol ether cleaves the double bond into two carbonyl moieties: the silylated carbon becomes a ketone (or ester derivative) and the alkene carbon becomes an aldehyde.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Substrate Structure</em>: The silyl enol ether of K has a double bond between C1 (bearing –OTMS and a methyl group) and C6 (an unsubstituted =CH– carbon).<br>2. <em>Ozonolysis Cleavage</em>: O₃ cleaves the C1=C6 double bond.<br>3. <em>Reductive Workup</em>: Me₂S reduces the molozonide/ozonide. C1 (bearing –OTMS and methyl) hydrolyzes to a methyl ketone, while C6 (bearing –H) becomes an aldehyde.<br><br><em>Distractor Traps:</em><br>&bull; B (Oxidative Over-Oxidation Trap): Carboxylic acids form under oxidative workup (H₂O₂), not mild reductive workup (Me₂S).<br>&bull; C (Conjugated Enone Error): Ozonolysis cleaves C=C bonds; it does not generate alpha,beta-unsaturated enones.<br>&bull; D (Intermolecular Cleavage Fiction): Cleaving an endocyclic double bond opens the ring into a single acyclic dicarbonyl molecule, not two separate fragments."
      },
      {
        "q": "Which of the following bases would be LEAST effective for selectively generating the kinetic enolate K at −78 °C?",
        "ch": [
          "Lithium diisopropylamide (LDA) in tetrahydrofuran solvent.",
          "Sodium hydride (NaH) suspended in dry dimethylformamide.",
          "Potassium hexamethyldisilazide (KHMDS) in tetrahydrofuran.",
          "Lithium tetramethylpiperidide (LiTMP) in aprotic solvent."
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Steric Discrimination in Kinetic Base Selection]</strong> Selective kinetic deprotonation requires a sterically demanding, soluble secondary amide base; small, unhindered, insoluble bases do not discriminate between alpha-protons.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Criteria for Kinetic Deprotonation</em>: The base must be (1) strong enough to deprotonate irreversibly, (2) bulky enough to favor the less hindered alpha-proton, and (3) soluble at cryogenic temperatures.<br>2. <em>Evaluation of Amide Bases</em>: LDA, KHMDS, and LiTMP are all sterically hindered, highly soluble amide bases that cleanly deprotonate C6.<br>3. <em>Evaluation of NaH</em>: NaH is a small, unhindered hydride ion that is insoluble in organic solvents, reacting heterogeneously and yielding thermodynamic equilibration.<br><br><em>Distractor Traps:</em><br>&bull; A (Ideal Kinetic Base): LDA is the gold-standard bulky kinetic base.<br>&bull; C (Effective Silyl Base): KHMDS features two bulky TMS groups and strongly favors kinetic deprotonation.<br>&bull; D (Hindered Piperidide): LiTMP is even more sterically hindered than LDA, providing excellent kinetic selectivity."
      }
    ]
  },
  {
    "id": "exam_cp90_p6",
    "sec": "C/P",
    "topic": "Axonal cable biophysics and RC circuits",
    "sheet": 69,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90",
    "passage": "<div class=\"ttl\">Passage 6 (Questions 31&ndash;36)</div>\n<p>Biophysicists model the passive electrical properties of unmyelinated and myelinated neural axons using cable theory and equivalent resistor-capacitor (RC) circuits. The lipid bilayer acts as a parallel-plate capacitor with specific capacitance <i>c</i><sub>m</sub> &asymp; 1.0 &mu;F/cm<sup>2</sup>, separating the conductive intracellular cytoplasm (axoplasm) from extracellular interstitial fluid. The dielectric constant of the hydrocarbon core of the membrane is &kappa; &asymp; 3.0, and membrane thickness is <i>d</i> &asymp; 3.0 nm.</p>\n<p>The time constant &tau;<sub>m</sub> governs the temporal distortion of synaptic inputs and is defined as the product of membrane resistance and capacitance: &tau;<sub>m</sub> = <i>r</i><sub>m</sub> &middot; <i>c</i><sub>m</sub>. The length constant &lambda; governs electrotonic spatial decay of subthreshold voltages according to <i>V</i>(<i>x</i>) = <i>V</i><sub>0</sub> &middot; <i>e</i><sup>&minus;<i>x</i> / &lambda;</sup>, where &lambda; = &radic;(<i>r</i><sub>m</sub> / <i>r</i><sub>i</sub>). Here, <i>r</i><sub>m</sub> is membrane resistance per unit length (&Omega;&middot;cm) and <i>r</i><sub>i</sub> is longitudinal intracellular axoplasmic resistance per unit length (&Omega;/cm).</p>\n<p>Myelin sheath wraps the axon in multiple compact lipid bilayers, effectively placing <i>N</i> membrane capacitors in series. Investigators studied passive cable properties in mammalian sensory axons before and after autoimmune demyelination induced by experimental allergic encephalomyelitis (EAE).</p>\n<table>\n<tr><th>Axon Type</th><th>Axon Diameter <i>d</i><sub>ax</sub> (&mu;m)</th><th>Myelin Lamellae (<i>N</i>)</th><th>Membrane Capacitance <i>C</i><sub>m</sub> (pF/mm)</th><th>Membrane Resistance <i>R</i><sub>m</sub> (M&Omega;&middot;mm)</th><th>Length Constant &lambda; (mm)</th><th>Conduction Velocity (m/s)</th></tr>\n<tr><td>Healthy A&alpha; (Myelinated)</td><td class=\"n\">12.0</td><td class=\"n\">150</td><td class=\"n\">2.5</td><td class=\"n\">80.0</td><td class=\"n\">2.8</td><td class=\"n\">72.0</td></tr>\n<tr><td>Demyelinated A&alpha; (EAE)</td><td class=\"n\">12.0</td><td class=\"n\">0</td><td class=\"n\">375.0</td><td class=\"n\">0.5</td><td class=\"n\">0.22</td><td class=\"n\">2.5</td></tr>\n<tr><td>Healthy C-fiber (Unmyelinated)</td><td class=\"n\">1.0</td><td class=\"n\">0</td><td class=\"n\">31.4</td><td class=\"n\">6.4</td><td class=\"n\">0.18</td><td class=\"n\">1.0</td></tr>\n</table>\n<p class=\"cap\"><b>Table 1</b> Passive cable properties and conduction metrics in sensory axons.</p>",
    "qs": [
      {
        "q": "Based on the physical model of the myelin sheath as N identical membrane capacitors in series, wrapping 150 myelin lamellae around an axon causes the total membrane capacitance to:",
        "ch": [
          "increase by a factor of 150 due to the accumulation of surface charge.",
          "remain constant because membrane capacitance depends only on axon length.",
          "increase proportionally to the square of the lamellae number (22,500-fold).",
          "decrease by a factor of 150 due to the series arrangement of capacitors."
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Series Capacitance and Transverse Dielectric Thickness]</strong> Capacitors in series add reciprocally; increasing the effective dielectric thickness of a membrane reduces its capacitance proportionally: C_total = C_single / N.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Circuit Model</em>: Each myelin layer acts as a parallel-plate capacitor with capacitance C_m. The 150 wraps are layered concentrically in series across the radial axis.<br>2. <em>Series Formula</em>: 1 / C_total = &Sigma;(1 / C_i) = 150 &times; (1 / C_m) &rArr; C_total = C_m / 150.<br>3. <em>Physical Consequence</em>: Total capacitance drops 150-fold, dramatically lowering the charge required to depolarize the membrane and accelerating action potential propagation.<br><br><em>Distractor Traps:</em><br>&bull; A (Parallel Capacitance Trap): Capacitors in *parallel* add directly (C_total = N &times; C), which applies to membrane surface area, not radial series layers.<br>&bull; B (Permittivity Fallacy): Total capacitance is inversely proportional to thickness d; adding 150 layers increases d by 150, reducing C.<br>&bull; C (Geometric Quadratic Error): Confuses series capacitance scaling with quadratic area equations."
      },
      {
        "q": "In an unmyelinated axon, if an electrode injects a subthreshold voltage pulse V₀ = +20 mV at position x = 0, at what distance x will the membrane potential drop to approximately +7.36 mV? (Use &lambda; = 0.18 mm; note 1/e ≈ 0.368).",
        "ch": [
          "0.09 mm",
          "0.18 mm",
          "0.36 mm",
          "0.54 mm"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Exponential Electrotonic Attenuation and Space Constant Definition]</strong> The axonal length constant &lambda; is defined as the physical distance over which an electrotonic voltage pulse decays to 1/e (~36.8%) of its initial amplitude.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Cable Equation</em>: V(x) = V₀ &times; e^(&minus;x / &lambda;).<br>2. <em>Target Ratio</em>: +7.36 mV / +20.0 mV = 0.368 = 1/e = e^(&minus;1).<br>3. <em>Solve for x</em>: e^(&minus;x / &lambda;) = e^(&minus;1) &rArr; x / &lambda; = 1 &rArr; x = &lambda; = 0.18 mm.<br><br><em>Distractor Traps:</em><br>&bull; A (Half-Length Trap): Divides &lambda; by 2 (0.09 mm), confusing 1/e with a half-decay distance.<br>&bull; C (Two-Length Error): Evaluates x = 2&lambda; (0.36 mm), where voltage drops to (1/e)² = 13.5% (+2.7 mV).<br>&bull; D (Three-Length Error): Evaluates x = 3&lambda; (0.54 mm), where voltage drops to (1/e)³ = 5.0% (+1.0 mV)."
      },
      {
        "q": "Why does demyelination in experimental autoimmune encephalomyelitis (EAE) cause axonal conduction velocity to crash from 72 m/s down to 2.5 m/s?",
        "ch": [
          "Axoplasmic core resistance surges due to the massive aggregation of neurofilaments.",
          "The resting equilibrium potential of potassium ions shifts from −90 mV up to 0 mV.",
          "Membrane resistance crashes and capacitance surges, collapsing the space constant.",
          "Voltage-gated sodium channels are cleaved enzymatically from the paranodal axolemma."
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Cable Property Collapse in Demyelinating Neuropathies]</strong> Stripping the myelin sheath strips the high transverse resistance and low capacitance of the axon, causing local current to dissipate across the leaky naked membrane rather than flowing forward longitudinally.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Cable Parameter Shifts</em>: Demyelination exposes naked axolemma: transverse membrane resistance (r_m) drops precipitously, while membrane capacitance (c_m) surges 150-fold.<br>2. <em>Effect on Length Constant</em>: The space constant &lambda; = &radic;(r_m / r_i). When r_m crashes, &lambda; collapses, preventing passive current from reaching the next node of Ranvier.<br>3. <em>Effect on Time Constant</em>: Increased c_m delays membrane charging (&tau;_m = r_m &times; c_m), converting rapid saltatory conduction into sluggish, failing continuous conduction.<br><br><em>Distractor Traps:</em><br>&bull; A (Internal Resistance Misattribution): Axoplasmic resistance r_i is governed by intracellular diameter and ion mobility, which is not the primary driver of demyelination block.<br>&bull; B (Equilibrium Potential Fiction): Demyelination affects cable insulating properties, not the fundamental intracellular/extracellular potassium concentration gradient.<br>&bull; D (Channel Proteolysis Fiction): Sodium channels in the node remain intact initially; conduction fails due to electrical current leakage, not enzymatic channel proteolysis."
      },
      {
        "q": "If an unmyelinated axon's radius r is doubled while retaining the same membrane and axoplasmic resistivities, the space constant &lambda; will increase by a factor of:",
        "ch": [
          "1.41-fold (√2)",
          "2.00-fold",
          "2.83-fold (2√2)",
          "4.00-fold"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Radius Dependence of Cable Parameters]</strong> The space constant &lambda; scales with the square root of the fiber radius: &lambda; &prop; &radic;r.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Resistance Scaling</em>: Specific membrane resistance per unit length r_m = R_m / (2&pi;r) &prop; 1/r. Internal axoplasmic resistance per unit length r_i = &rho;_i / (&pi;r²) &prop; 1/r².<br>2. <em>Space Constant Formula</em>: &lambda; = &radic;(r_m / r_i) = &radic;[(R_m / 2&pi;r) / (&rho;_i / &pi;r²)] = &radic;[(R_m &times; r) / (2&rho;_i)] &prop; &radic;r.<br>3. <em>Apply Doubling</em>: If r increases by 2, &lambda; increases by &radic;2 &asymp; 1.41-fold.<br><br><em>Distractor Traps:</em><br>&bull; B (Linear Radius Fallacy): Assumes &lambda; scales linearly with r (2.00-fold).<br>&bull; C (3/2 Power Trap): Confuses cross-sectional scaling with &radic;(r³) &asymp; 2.83-fold.<br>&bull; D (Area Quadratic Trap): Scales &lambda; with cross-sectional area r² (2² = 4.00-fold)."
      },
      {
        "q": "What is the membrane time constant &tau;_m for an axonal segment with specific membrane resistance R_m = 0.20 &Omega;·m² and specific membrane capacitance C_m = 0.010 F/m²?",
        "ch": [
          "2.0 ms",
          "5.0 ms",
          "20.0 ms",
          "50.0 ms"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: The RC Membrane Time Constant]</strong> The membrane time constant &tau;_m represents the time required for passive charging of the lipid bilayer capacitance through transverse membrane resistance: &tau;_m = R_m &times; C_m.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Formula Setup</em>: &tau;_m = R_m &times; C_m.<br>2. <em>Multiply Values</em>: &tau;_m = (0.20 &Omega;&middot;m²) &times; (0.010 F/m²) = 0.0020 seconds.<br>3. <em>Convert to Milliseconds</em>: 0.0020 s &times; 1000 ms/s = 2.0 ms.<br><br><em>Distractor Traps:</em><br>&bull; B (Reciprocal Error): Evaluates C_m / R_m = 0.010 / 0.20 = 0.05 s = 50 ms or 5.0 ms.<br>&bull; C (Order of Magnitude Error): Misplaces the decimal point by a factor of 10 (20.0 ms).<br>&bull; D (Compound Math Error): Combines reciprocal inversion with decimal error (50.0 ms)."
      },
      {
        "q": "Which of the following physiological modifications will MAXIMIZE the action potential conduction velocity along a nerve fiber?",
        "ch": [
          "Increasing myelin sheath thickness and increasing internal axonal diameter.",
          "Increasing membrane capacitance and increasing axoplasmic core resistance.",
          "Decreasing axonal core radius and decreasing transverse membrane resistance.",
          "Decreasing extracellular sodium levels and decreasing ambient temperature."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Optimization of Cable Parameters for Rapid Conduction]</strong> Conduction velocity is maximized by maximizing the length constant &lambda; (high r_m, low r_i) and minimizing the time constant &tau;_m (low c_m).<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Myelin Sheath Thickness</em>: Wrapping more myelin increases radial thickness, drastically lowering capacitance c_m (faster charging) and raising membrane resistance r_m (less leakage).<br>2. <em>Axonal Diameter</em>: Increasing axonal core radius r lowers internal longitudinal resistance r_i (r_i &prop; 1/r²), allowing current to travel farther forward.<br>3. <em>Synthesis</em>: Large-diameter, heavily myelinated fibers (A&alpha; motor fibers) achieve the highest conduction velocities in biology (~120 m/s).<br><br><em>Distractor Traps:</em><br>&bull; B (Direct Inversion): Higher capacitance and higher internal resistance both severely slow conduction velocity.<br>&bull; C (Opposite Direction Trap): Decreasing radius and decreasing membrane resistance collapse the space constant &lambda;.<br>&bull; D (Inhibition Trap): Lowering sodium concentration reduces action potential amplitude and cooling slows channel kinetics."
      }
    ]
  },
  {
    "id": "exam_cp90_p7",
    "sec": "C/P",
    "topic": "Coordination chemistry and aquation kinetics of cisplatin",
    "sheet": 6,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90",
    "passage": "<div class=\"ttl\">Passage 7 (Questions 37&ndash;42)</div>\n<p>Cisplatin (<i>cis</i>-diamminedichloroplatinum(II), [Pt(NH<sub>3</sub>)<sub>2</sub>Cl<sub>2</sub>]) is a neutral square-planar d<sup>8</sup> coordination complex widely used in chemotherapy. Its therapeutic activity stems from coordination to the N7 purine nitrogen of guanine bases in DNA, forming 1,2-intrastrand d(GpG) crosslinks that distort the DNA double helix and arrest replication.</p>\n<p>In blood plasma ([Cl<sup>&minus;</sup>] &asymp; 103 mM), high extracellular chloride suppresses aquation, maintaining cisplatin in its uncharged dichloro form which passively permeates cell membranes. Upon entering the cytoplasm where chloride concentration drops to 4&ndash;10 mM, cisplatin undergoes stepwise aquation (hydrolysis) with loss of chloride ligands:</p>\n<p style=\"text-align:center;font-style:italic\">\n[Pt(NH<sub>3</sub>)<sub>2</sub>Cl<sub>2</sub>] + H<sub>2</sub>O &rightleftharpoons; [Pt(NH<sub>3</sub>)<sub>2</sub>Cl(H<sub>2</sub>O)]<sup>+</sup> + Cl<sup>&minus;</sup> &nbsp;&nbsp;&nbsp;&nbsp;(k<sub>1</sub> = 2.5 &times; 10<sup>&minus;5</sup> s<sup>&minus;1</sup>)<br>\n[Pt(NH<sub>3</sub>)<sub>2</sub>Cl(H<sub>2</sub>O)]<sup>+</sup> + H<sub>2</sub>O &rightleftharpoons; [Pt(NH<sub>3</sub>)<sub>2</sub>(H<sub>2</sub>O)<sub>2</sub>]<sup>2+</sup> + Cl<sup>&minus;</sup> &nbsp;&nbsp;&nbsp;&nbsp;(k<sub>2</sub> = 8.0 &times; 10<sup>&minus;6</sup> s<sup>&minus;1</sup>)\n</p>\n<p>The cationic diaqua and monoaqua species are reactive electrophiles that rapidly crosslink DNA. The geometric isomer <i>transplatin</i> (<i>trans</i>-diamminedichloroplatinum(II)) is clinically inactive because steric constraints prevent it from forming the requisite 1,2-intrastrand crosslinks, instead forming stereochemically repairable 1,3-intrastrand and interstrand adducts.</p>\n<table>\n<tr><th>Complex</th><th>Geometry</th><th>Coordination Number</th><th>Aquation Rate <i>k</i><sub>1</sub> (s<sup>&minus;1</sup>)</th><th>DNA Adduct Type</th><th>Cytotoxicity IC<sub>50</sub> (&mu;M)</th></tr>\n<tr><td><i>cis</i>-[Pt(NH<sub>3</sub>)<sub>2</sub>Cl<sub>2</sub>] (Cisplatin)</td><td>Square planar</td><td class=\"n\">4</td><td class=\"n\">2.5 &times; 10<sup>&minus;5</sup></td><td>1,2-intrastrand d(GpG) (90%)</td><td class=\"n\">1.8</td></tr>\n<tr><td><i>trans</i>-[Pt(NH<sub>3</sub>)<sub>2</sub>Cl<sub>2</sub>] (Transplatin)</td><td>Square planar</td><td class=\"n\">4</td><td class=\"n\">9.8 &times; 10<sup>&minus;5</sup></td><td>1,3-intrastrand / interstrand</td><td class=\"n\">85.0</td></tr>\n<tr><td>Carboplatin (dicarboxylate chelate)</td><td>Square planar</td><td class=\"n\">4</td><td class=\"n\">1.2 &times; 10<sup>&minus;7</sup></td><td>1,2-intrastrand d(GpG)</td><td class=\"n\">12.0</td></tr>\n<tr><td>Oxaliplatin (DACH ligand)</td><td>Square planar</td><td class=\"n\">4</td><td class=\"n\">3.4 &times; 10<sup>&minus;6</sup></td><td>1,2-intrastrand d(GpG)</td><td class=\"n\">2.2</td></tr>\n</table>\n<p class=\"cap\"><b>Table 1</b> Chemical properties and biological parameters of platinum complexes.</p>",
    "qs": [
      {
        "q": "What is the formal oxidation state and d-electron count of the central platinum atom in cisplatin, cis-[Pt(NH₃)₂Cl₂]?",
        "ch": [
          "Pt(0), d¹⁰",
          "Pt(II), d⁶",
          "Pt(IV), d⁶",
          "Pt(II), d⁸"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Coordination Complex Oxidation States and d-Electron Accounting]</strong> Formal metal oxidation state equals overall complex charge minus the sum of formal ligand charges; d-electron count equals group number minus oxidation state.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Ligand Charges</em>: Ammine (NH₃) is a neutral ligand (charge = 0); chloride (Cl⁻) is an anionic ligand (charge = &minus;1).<br>2. <em>Solve for Platinum Charge</em>: Total charge = 0 &rArr; Pt + 2(0) + 2(&minus;1) = 0 &rArr; Pt = +2, so platinum is Pt(II).<br>3. <em>Count d-Electrons</em>: Platinum is in Group 10. For Pt(II), d-electron count = 10 &minus; 2 = 8 (d⁸ configuration).<br><br><em>Distractor Traps:</em><br>&bull; A (Neutral Metal Fallacy): Mistakenly treats coordinated chlorides as neutral chlorine radicals (Pt(0), d¹⁰).<br>&bull; B (Group 8 Error): Confuses platinum with Group 8 iron/ruthenium, miscalculating 8 &minus; 2 = 6.<br>&bull; C (Over-Oxidation to Pt IV): Occurs in octahedral prodrugs like oxaliplatin derivatives, not square planar cisplatin."
      },
      {
        "q": "Why does cisplatin remain predominantly intact in extracellular blood plasma, but undergoes rapid aquation upon entering the cytoplasm of a tumor cell?",
        "ch": [
          "Intracellular glutathione directly reduces Pt(II) to insoluble metallic platinum Pt(0).",
          "High extracellular chloride (100 mM) suppresses aquation via Le Chatelier's rule.",
          "Blood serum albumin covalently binds both chloride ligands, preventing ligand exchange.",
          "Tumor cells possess high lysosomal pH that catalytically accelerates ester hydrolysis."
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Thermodynamic Chloride Suppression of Platinum Aquation]</strong> Aquation of cisplatin is a reversible nucleophilic displacement of chloride by water: [Pt(NH₃)₂Cl₂] + H₂O &rightleftharpoons; [Pt(NH₃)₂Cl(H₂O)]⁺ + Cl⁻.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Extracellular Environment</em>: Blood plasma maintains a high chloride concentration ([Cl⁻] &asymp; 100 mM), driving the equilibrium far to the left (intact neutral drug).<br>2. <em>Intracellular Environment</em>: Upon entering the cell, cytoplasmic chloride plummets to [Cl⁻] &asymp; 4–10 mM.<br>3. <em>Le Chatelier's Shift</em>: The 10- to 20-fold drop in chloride shifts the equilibrium toward the mono- and diaqua cationic complexes, which are the active electrophiles that crosslink DNA.<br><br><em>Distractor Traps:</em><br>&bull; A (Redox Inactivation Fallacy): Glutathione can detoxify platinum by coordinating sulfur, but does not reduce Pt(II) to metallic Pt(0).<br>&bull; C (Albumin Binding Error): Albumin binds platinum slowly and irreversibly, but does not protect chloride ligands from water exchange.<br>&bull; D (pH Inversion): Tumor microenvironments are acidic, not alkaline; furthermore, aquation is inorganic ligand displacement, not ester hydrolysis."
      },
      {
        "q": "Carboplatin exhibits a 200-fold slower aquation rate than cisplatin. This reduced reactivity is primarily due to the fact that:",
        "ch": [
          "the bidentate dicarboxylate chelate ring confers substantial kinetic stability.",
          "carboplatin contains platinum in the higher Pt(IV) oxidation state than Pt(II).",
          "the bulky cyclobutane ring sterically blocks the incoming DNA phosphate backbone.",
          "carboplatin is completely insoluble in aqueous neutral physiological saline."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Chelate Effect and Activation Barriers in Bidentate Substitution]</strong> Bidentate chelating ligands exhibit substantially higher kinetic and thermodynamic stability than monodentate ligands due to the chelate effect and high activation energies of ring opening.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Structural Comparison</em>: Cisplatin has two monodentate chloride leaving groups. Carboplatin has a bidentate 1,1-cyclobutanedicarboxylate chelate ring.<br>2. <em>Kinetic Barrier</em>: Aquation of carboplatin requires opening a stable 6-membered chelate ring. Ring opening has a much higher activation energy (Ea) than simple monodentate Cl⁻ dissociation.<br>3. <em>Clinical Consequence</em>: Slower aquation produces fewer acute toxicities (less nephrotoxicity and emesis) compared to cisplatin.<br><br><em>Distractor Traps:</em><br>&bull; B (Oxidation State Invariance): Both carboplatin and cisplatin contain Pt(II), d⁸ square planar centers.<br>&bull; C (Mechanism Mismatch): The slow rate-limiting step is aquation (displacement by water), which occurs prior to contacting DNA.<br>&bull; D (Solubility Inversion): Carboplatin is highly water-soluble, which facilitates its intravenous clinical delivery."
      },
      {
        "q": "Why is transplatin, trans-[Pt(NH₃)₂Cl₂], clinically inactive as an antitumor drug compared to its cis isomer?",
        "ch": [
          "Transplatin decomposes spontaneously into metallic platinum before entering tumor cells.",
          "The trans ammine ligands are irreversible competitive inhibitors of cellular RNA polymerase.",
          "Transplatin has a net formal charge of +2 that prevents passive plasma membrane diffusion.",
          "Transplatin cannot form intrastrand 1,2-d(GpG) crosslinks due to geometric constraints."
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Stereochemical Requirements for Intrastrand DNA Bifunctional Adducts]</strong> Cisplatin's cytotoxicity relies on forming 1,2-intrastrand crosslinks between adjacent guanine bases, inducing a severe ~35° bend in DNA that prevents repair.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Spatial Geometry</em>: In cisplatin, the two labile chloride leaving groups are mutually cis (90&deg; separation, ~3.3 &Aring; apart). This distance perfectly matches the distance between adjacent purines on a DNA strand.<br>2. <em>Transplatin Geometry</em>: In transplatin, the leaving groups are trans (180&deg; separation, ~4.7 &Aring; apart). It cannot form 1,2-intrastrand crosslinks, forming instead less toxic 1,3-crosslinks and interstrand links.<br>3. <em>Biological Repair</em>: DNA repair machinery easily excises transplatin adducts, rendering it therapeutically ineffective.<br><br><em>Distractor Traps:</em><br>&bull; A (Decomposition Fiction): Transplatin is chemically stable in solution and does not decompose into metallic platinum.<br>&bull; B (Enzyme Mode Fiction): Ammine ligands do not directly bind RNA polymerase as competitive inhibitors.<br>&bull; C (Charge Equivalence): Both cisplatin and transplatin are neutral complexes (formal charge = 0) with identical molecular formulas."
      },
      {
        "q": "The coordination geometry of d⁸ Pt(II) complexes is square planar rather than tetrahedral primarily because:",
        "ch": [
          "large ligand-field splitting places all eight d-electrons into low-energy orbitals.",
          "tetrahedral geometry requires four identical ligands to satisfy spatial VSEPR rules.",
          "platinum is an early transition metal that prefers low coordination numbers in nature.",
          "chloride and ammine ligands form covalent triple bonds that enforce 90° bond angles."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Crystal Field Stabilization Energy in 5d Metal Centers]</strong> Heavy 5d transition metals produce exceptionally large ligand field splitting (&Delta;), making low-spin square planar geometry thermodynamically favorable for d⁸ electron configurations.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>d-Orbital Splitting</em>: In square planar geometry, the d-orbitals split into four energy levels: d(xy), d(xz), d(yz) are low, d(z²) is intermediate, and d(x²&minus;y²) is pushed to very high energy.<br>2. <em>Electron Filling</em>: In d⁸ Pt(II), all 8 electrons fill the four lower orbitals, leaving the highly antibonding d(x²&minus;y²) orbital completely empty.<br>3. <em>CFSE Advantage</em>: Because Pt is a 5d metal, &Delta; is immense (&Delta;_sp > P, the pairing energy), yielding enormous Crystal Field Stabilization Energy compared to tetrahedral geometry.<br><br><em>Distractor Traps:</em><br>&bull; B (VSEPR Fallacy): Transition metal complexes are governed by d-orbital crystal field theory, not simple VSEPR; tetrahedral complexes routinely form with non-identical ligands.<br>&bull; C (Periodic Table Error): Platinum is a late 5d transition metal (Group 10), not an early transition metal.<br>&bull; D (Bond Order Fiction): Chloride and ammine ligands form single dative sigma bonds, not triple bonds."
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
        "e": "<strong>[Governing Principle: Mass Fraction and Stoichiometric Content of Coordination Compounds]</strong> The mass of a constituent element in a pure chemical dose equals total dose multiplied by the element's mass fraction: m_element = m_total &times; (MW_element / MW_total).<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Mass Fraction Calculation</em>: Fraction Pt = Molar mass of Pt / Molar mass of cisplatin = 195 g/mol / 300 g/mol.<br>2. <em>Simplify Ratio</em>: 195 / 300 = 65 / 100 = 0.65 (exactly 65%).<br>3. <em>Multiply by Dose</em>: 100 mg &times; 0.65 = 65 mg of elemental platinum.<br><br><em>Distractor Traps:</em><br>&bull; A (Complementary Mass Error): Calculates the mass of non-platinum ligands (100 &minus; 65 = 35 mg).<br>&bull; B (Arbitrary Estimate Trap): Midpoint guess ignoring the heavy atomic mass of platinum (50 mg).<br>&bull; D (Overestimate Trap): Confuses platinum with high mass loading in other heavy complexes (90 mg)."
      }
    ]
  },
  {
    "id": "exam_cp90_discretes",
    "sec": "C/P",
    "topic": "C/P Standalone Discrete Questions",
    "sheet": null,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90",
    "passage": "",
    "qs": [
      {
        "q": "An endoscope utilizes optical fiber bundles to transmit light into the stomach. If the core of the optical fiber has an index of refraction n₁ = 1.60 and the cladding has n₂ = 1.28, what is the critical angle &theta;_c for total internal reflection within the fiber core?",
        "ch": [
          "30°",
          "45°",
          "53°",
          "60°"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Snell's Law and Boundary Total Internal Reflection]</strong> Total internal reflection occurs when light traveling in a denser medium strikes an interface with a less dense medium at an incident angle exceeding the critical angle: sin(&theta;_c) = n_cladding / n_core.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Formula Setup</em>: sin(&theta;_c) = n₂ / n₁.<br>2. <em>Substitute Indices</em>: sin(&theta;_c) = 1.28 / 1.60 = 128 / 160 = 4 / 5 = 0.80.<br>3. <em>Determine Angle</em>: For standard MCAT reference triangles, arcsin(0.80) &asymp; 53&deg; (from the 3-4-5 right triangle).<br><br><em>Distractor Traps:</em><br>&bull; A (sin = 0.50 Error): Arcsin of 0.50 corresponds to 30&deg;, which would require n₂/n₁ = 0.50.<br>&bull; B (sin = 0.707 Error): Arcsin of 1/&radic;2 corresponds to 45&deg;, which would require n₂/n₁ = 0.71.<br>&bull; D (sin = 0.866 Error): Arcsin of &radic;3/2 corresponds to 60&deg;, which would require n₂/n₁ = 0.866."
      },
      {
        "q": "Technetium-99m (⁹⁹ᵐTc) is a gamma-emitting radioisotope with a half-life of 6.0 hours. If a patient is administered 800 MBq of ⁹⁹ᵐTc, how much radioactivity remains in the patient's body after 24 hours (assuming negligible biological excretion)?",
        "ch": [
          "25 MBq",
          "50 MBq",
          "100 MBq",
          "200 MBq"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: First-Order Radioactive Decay Kinetics]</strong> In exponential decay, the remaining activity is halved with every elapsed half-life: A(t) = A₀ &times; (1/2)^n, where n = t / t_(1/2).<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Calculate Elapsed Half-Lives</em>: n = 24 hours / 6.0 hours = 4 half-lives.<br>2. <em>Compute Decay Factor</em>: (1/2)⁴ = 1/16.<br>3. <em>Compute Remaining Activity</em>: A = 800 MBq / 16 = 50 MBq.<br><br><em>Distractor Traps:</em><br>&bull; A (5 Half-Lives Error): Evaluates 5 half-lives (800 / 32 = 25 MBq).<br>&bull; C (3 Half-Lives Error): Evaluates 3 half-lives (800 / 8 = 100 MBq).<br>&bull; D (2 Half-Lives Error): Evaluates 2 half-lives (800 / 4 = 200 MBq)."
      },
      {
        "q": "Under which set of thermodynamic conditions does a real gas deviate MOST significantly from ideal behavior described by PV = nRT?",
        "ch": [
          "High temperature and low pressure",
          "High temperature and high pressure",
          "Low temperature and low pressure",
          "Low temperature and high pressure"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Van der Waals Deviations and Intermolecular Potential Energy]</strong> Real gases deviate from ideality when molecular volume is non-negligible compared to container volume and intermolecular attractions become significant.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Ideal Gas Assumptions</em>: (1) Gas particles occupy zero physical volume; (2) Particles experience zero intermolecular attractive or repulsive forces.<br>2. <em>Maximizing Deviations</em>: At *high pressure*, gas particles are crowded together, making their finite volume significant. At *low temperature*, particles move slowly with low kinetic energy, allowing intermolecular forces (van der Waals attractions) to capture molecules.<br>3. <em>Conclusion</em>: Real gas behavior deviates most dramatically under low temperature and high pressure.<br><br><em>Distractor Traps:</em><br>&bull; A (Ideal Limit Trap): High temperature and low pressure represent the conditions where real gases behave *most ideally*.<br>&bull; B (Half-Ideal Condition): High temperature provides high kinetic energy that overcomes intermolecular attractions.<br>&bull; C (Half-Ideal Condition): Low pressure keeps molecules far apart, minimizing the impact of finite molecular volume."
      },
      {
        "q": "An ideal gas in a cylinder with a movable frictionless piston expands isobarically at a constant pressure of 2.0 &times; 10⁵ Pa from an initial volume of 0.010 m³ to a final volume of 0.035 m³. How much mechanical work was performed by the gas during this expansion?",
        "ch": [
          "2.5 kJ",
          "5.0 kJ",
          "7.0 kJ",
          "12.0 kJ"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Pressure-Volume Mechanical Work in Isobaric Processes]</strong> For an isobaric expansion against constant external pressure, work performed by the gas equals pressure multiplied by change in volume: W = P &times; &Delta;V.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Calculate Volume Change</em>: &Delta;V = V_final &minus; V_initial = 0.035 m³ &minus; 0.010 m³ = 0.025 m³.<br>2. <em>Calculate Work in Joules</em>: W = P &times; &Delta;V = (2.0 &times; 10⁵ N/m²) &times; (0.025 m³) = 5,000 Joules.<br>3. <em>Convert to Kilojoules</em>: 5,000 J / 1000 J/kJ = 5.0 kJ.<br><br><em>Distractor Traps:</em><br>&bull; A (Half Pressure Trap): Multiplies by 1.0 &times; 10⁵ Pa instead of 2.0 &times; 10⁵ Pa (2.5 kJ).<br>&bull; C (Total Volume Trap): Multiplies P by V_final (2.0 &times; 10⁵ &times; 0.035 = 7.0 kJ), forgetting to subtract initial volume.<br>&bull; D (Compound Math Error): Evaluates P &times; (V_initial + V_final) or wrong arithmetic (12.0 kJ)."
      },
      {
        "q": "Which of the following chemical reactions represents a Lewis acid-base coordination that does NOT involve Brønsted-Lowry proton transfer?",
        "ch": [
          "HCl(aq) + NaOH(aq) → NaCl(aq) + H₂O(l) via aqueous proton transfer.",
          "CH₃COOH + H₂O ⇌ CH₃COO⁻ + H₃O⁺ via reversible hydronium transfer.",
          "BF₃ + :NH₃ → F₃B:NH₃ via coordinate electron-pair dative donation.",
          "NH₄⁺ + OH⁻ → NH₃ + H₂O through direct ammonium deprotonation step."
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Lewis Electron-Pair Donation vs Brønsted-Lowry Proton Transfer]</strong> A Lewis acid-base reaction involves donation and acceptance of an electron pair to form a coordinate covalent bond without necessarily transferring a hydrogen ion (proton).<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Identify Electron Deficient Species</em>: Boron trifluoride (BF₃) has an incomplete valence octet (6 valence electrons, vacant 2p orbital on boron), acting as a quintessential Lewis acid.<br>2. <em>Identify Electron Rich Species</em>: Ammonia (:NH₃) has a lone pair on nitrogen, acting as a Lewis base.<br>3. <em>Bond Formation</em>: Nitrogen donates its lone pair into boron's empty p-orbital, forming a neutral adduct (F₃B&larr;NH₃) without transferring any protons.<br><br><em>Distractor Traps:</em><br>&bull; A (Brønsted Neutralization): Involves transfer of a proton from HCl to OH⁻.<br>&bull; B (Brønsted Dissociation): Involves transfer of a proton from acetic acid to water.<br>&bull; D (Brønsted Acid-Base): Involves transfer of a proton from ammonium cation to hydroxide."
      },
      {
        "q": "A laboratory technician prepares a 1.0 L buffer solution containing 0.10 M acetic acid and 0.10 M sodium acetate (pH = 4.76). If 9.0 L of pure distilled water is added to dilute the solution tenfold to a total volume of 10.0 L, what will be the resulting pH of the buffer?",
        "ch": [
          "3.76",
          "4.76",
          "5.76",
          "7.00"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Volume Independence of Buffer Ratios]</strong> In the Henderson-Hasselbalch equation, the ratio [A⁻]/[HA] equals moles of A⁻ divided by moles of HA, making buffer pH independent of dilution over moderate concentration ranges.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Formula Setup</em>: pH = pKa + log([A⁻] / [HA]) = pKa + log(mol A⁻ / mol HA).<br>2. <em>Effect of Dilution</em>: Adding 9.0 L of water dilutes both acetic acid and sodium acetate by the identical factor of 10 (0.010 M each).<br>3. <em>Evaluate Ratio</em>: The ratio remains [A⁻]/[HA] = 0.010 / 0.010 = 1.0. Because log(1.0) = 0, pH = pKa = 4.76.<br><br><em>Distractor Traps:</em><br>&bull; A (Acidic Dilution Error): Assumes diluting an acid increases its acidity (pH drops to 3.76).<br>&bull; C (Alkaline Dilution Fallacy): Mistakenly assumes tenfold dilution must shift pH by 1.0 unit toward neutral (5.76).<br>&bull; D (Pure Water Fallacy): Assumes adding excess water completely overwhelms buffer capacity, forcing pH to pure water's neutral 7.00."
      },
      {
        "q": "A pure solution of an enantiomeric drug has a specific rotation [&alpha;] of +40°/(dm·g/mL). If a synthetic batch consists of 75% of this dextrorotatory enantiomer and 25% of the levorotatory enantiomer, what observed specific rotation will be measured?",
        "ch": [
          "+10°",
          "+20°",
          "+30°",
          "+40°"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Enantiomeric Excess and Net Optical Rotation]</strong> In a scalemic mixture of enantiomers, the observed optical rotation is directly proportional to the enantiomeric excess (ee): [&alpha;]_obs = ee &times; [&alpha;]_pure.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Calculate Enantiomeric Excess</em>: ee = % Major enantiomer &minus; % Minor enantiomer = 75% &minus; 25% = 50% = 0.50.<br>2. <em>Formula Setup</em>: [&alpha;]_obs = ee &times; [&alpha;]_pure.<br>3. <em>Calculate Observed Rotation</em>: [&alpha;]_obs = 0.50 &times; (+40&deg;) = +20&deg;.<br><br><em>Distractor Traps:</em><br>&bull; A (Quarter Scaling Trap): Multiplies +40&deg; by 25% (minor component), yielding +10&deg;.<br>&bull; C (Major Percentage Trap): Multiplies +40&deg; directly by 75% without subtracting the cancelling minor enantiomer (0.75 &times; 40&deg; = +30&deg;).<br>&bull; D (Pure Enantiomer Trap): Assumes optical rotation equals pure enantiomer rotation (+40&deg;), ignoring racemic cancellation."
      },
      {
        "q": "A biopsy specimen of bone tissue has a mass of 4.5 g in air and an apparent mass of 2.7 g when completely submerged in water (density = 1.0 g/cm³). What is the density of the bone specimen?",
        "ch": [
          "1.5 g/cm³",
          "1.8 g/cm³",
          "2.5 g/cm³",
          "3.0 g/cm³"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Archimedes' Principle and Hydrostatic Specific Gravity]</strong> The buoyant force experienced by a fully submerged object equals the weight of displaced fluid, directly yielding the object's volume.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Calculate Apparent Mass Loss</em>: Apparent mass loss = Mass in air &minus; Apparent mass in water = 4.5 g &minus; 2.7 g = 1.8 g.<br>2. <em>Determine Specimen Volume</em>: By Archimedes' principle, mass of displaced water = 1.8 g. Since &rho;_water = 1.0 g/cm³, volume V = 1.8 cm³.<br>3. <em>Compute Specimen Density</em>: &rho;_bone = Mass in air / Volume = 4.5 g / 1.8 cm³ = 45 / 18 = 5 / 2 = 2.5 g/cm³.<br><br><em>Distractor Traps:</em><br>&bull; A (Inverted Ratio Error): Evaluates 2.7 / 1.8 = 1.5 g/cm³.<br>&bull; B (Displaced Mass Confusion): Equates density directly with apparent mass loss (1.8 g/cm³).<br>&bull; D (Apparent Mass Division): Divides mass in air by apparent mass in water: 4.5 / 2.7 = 1.67 or 3.0 g/cm³."
      },
      {
        "q": "During a biceps curl exercise, the biceps tendon inserts at a right angle into the forearm at 4.0 cm from the elbow joint. The forearm/hand has mass 2.0 kg with center of mass at 16.0 cm, and the hand holds a 10.0 kg dumbbell at 32.0 cm. What upward force F_b must the biceps exert to hold the forearm horizontally in static equilibrium? (Use g = 9.8 m/s²).",
        "ch": [
          "352 N",
          "862 N",
          "980 N",
          "3450 N"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Rotational Static Equilibrium and Torque Summation]</strong> In static equilibrium, the net torque about any pivot axis must equal zero: &Sigma;&tau; = 0.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Clockwise Torques (Gravity)</em>: &tau;_arm = (2.0 kg &times; 9.8 m/s²) &times; (0.16 m) = 19.6 N &times; 0.16 m = 3.136 N&middot;m. &tau;_dumbbell = (10.0 kg &times; 9.8 m/s²) &times; (0.32 m) = 98.0 N &times; 0.32 m = 31.36 N&middot;m. Total clockwise torque = 3.136 + 31.36 = 34.496 N&middot;m.<br>2. <em>Counter-Clockwise Torque (Muscle)</em>: &tau;_biceps = F_b &times; (0.040 m).<br>3. <em>Solve for Force</em>: F_b &times; 0.040 m = 34.496 N&middot;m &rArr; F_b = 34.496 / 0.040 = 862.4 N &asymp; 862 N.<br><br><em>Distractor Traps:</em><br>&bull; A (Linear Gravity Sum): Fails to account for lever arms, computing (2 kg + 10 kg) &times; 9.8 / 0.32 &asymp; 352 N.<br>&bull; C (Direct Weight Error): Forgets lever arm mechanical disadvantage, equating force with total weight: (2 + 10) &times; 9.8 &asymp; 118 N or 980 N.<br>&bull; D (Length Inversion Trap): Multiplies torque by 100 instead of dividing by lever arm (3450 N)."
      },
      {
        "q": "Consider a standard galvanic cell operating at 298 K with the half-reactions: Cu²⁺(aq) + 2 e⁻ → Cu(s) (E° = +0.34 V) and Zn²⁺(aq) + 2 e⁻ → Zn(s) (E° = −0.76 V). What is the standard cell potential E°_cell and equilibrium constant K_eq?",
        "ch": [
          "E°_cell = −1.10 V, K_eq = 6.2 × 10⁻³⁸",
          "E°_cell = +0.42 V, K_eq = 7.8 × 10⁻¹⁵",
          "E°_cell = +1.10 V, K_eq = 1.0 × 10⁰⁰",
          "E°_cell = +1.10 V, K_eq = 1.6 × 10³⁷"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Galvanic Cell Spontaneity and Thermodynamic Equilibrium Constants]</strong> In a spontaneous galvanic cell, the half-cell with the more positive reduction potential acts as cathode (reduction), while the other is inverted to act as anode (oxidation): E&deg;_cell = E&deg;_cathode &minus; E&deg;_anode > 0.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Identify Cathode and Anode</em>: E&deg;(Cu²⁺/Cu) = +0.34 V is more positive than E&deg;(Zn²⁺/Zn) = &minus;0.76 V. Thus, Cu²⁺ is reduced (cathode) and Zn is oxidized (anode).<br>2. <em>Calculate Standard Potential</em>: E&deg;_cell = E&deg;_cathode &minus; E&deg;_anode = (+0.34 V) &minus; (&minus;0.76 V) = +0.34 + 0.76 = +1.10 V.<br>3. <em>Relate to Equilibrium Constant</em>: E&deg;_cell = (0.0592 V / n) &times; log(K_eq). For n = 2: 1.10 = (0.0296) &times; log(K_eq) &rArr; log(K_eq) &asymp; 37.16 &rArr; K_eq &asymp; 10^(37.16) &asymp; 1.6 &times; 10³⁷.<br><br><em>Distractor Traps:</em><br>&bull; A (Electrolytic Inversion Trap): Inverts cathode and anode, computing non-spontaneous potential &minus;1.10 V and K_eq &asymp; 6.2 &times; 10⁻³⁸.<br>&bull; B (Direct Subtraction Error): Evaluates E&deg; = 0.76 &minus; 0.34 = +0.42 V.<br>&bull; C (Zero-Potential Equilibrium Error): Claims K_eq = 1.0 (which corresponds to E&deg;_cell = 0.00 V)."
      }
    ]
  }
];
