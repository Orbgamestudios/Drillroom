# scratch/upgrade_cp90_p1_to_p4.py
# Items 1 to 4 of EXAM_CP90 (Questions 1 to 24)
import sys

cp_item1_qs = [
    {
        "q": "Based on Table 1, which catalytic step is most severely rate-limiting in the H64A variant compared to the wild-type enzyme?",
        "ch": [
            "Nucleophilic attack of zinc-bound hydroxide on dissolved substrate carbon dioxide.",
            "Displacement of coordinated bicarbonate by an incoming solvent water molecule.",
            "Intermolecular proton transfer from the zinc-bound water to bulk solvent buffer.",
            "Initial substrate binding of carbon dioxide into the hydrophobic active pocket."
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Kinetic Decoupling of Substrate Affinity and Proton Shuttling]</strong> In carbonic anhydrase II, catalytic turnover requires rapid regeneration of the active zinc-hydroxide nucleophile via an intramolecular proton shuttle.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Table 1 shows that mutating His64 to alanine (H64A) causes kcat to drop by over two orders of magnitude (1.4 &times; 10⁶ to 1.1 &times; 10⁴ s⁻¹), whereas Km is unchanged (12.0 vs 12.5 mM).<br>2. <em>Mechanistic Bridge</em>: Because Km reflects substrate binding affinity, the invariance of Km demonstrates that CO₂ binding and coordination are unimpaired. The severe decline in kcat indicates that the chemical step mediated by His64—transferring a proton from the zinc-bound water to the external buffer—is the rate-determining bottleneck.<br>3. <em>Deduction</em>: Proton transfer is the selectively impaired step.<br><br><em>Distractor Traps:</em><br>&bull; A (Km Invariance Trap): Nucleophilic attack on CO₂ would alter effective binding kinetics or Km, which remains unchanged in H64A.<br>&bull; B (Ligand Displacement Error): Bicarbonate displacement is facilitated by the zinc coordination sphere, not the peripheral His64 residue.<br>&bull; D (Binding vs Catalysis Confusion): Confuses substrate association (governed by the hydrophobic pocket) with catalytic regeneration (governed by the proton shuttle)."
    },
    {
        "q": "The zinc ion in carbonic anhydrase acts as a Lewis acid during catalysis primarily by:",
        "ch": [
            "donating an electron pair to water, lowering its pKa from 14 down to approximately 7.",
            "accepting electron density from coordinated water, lowering its pKa down from 14 to 7.",
            "stabilizing the conjugate acid form of bicarbonate via electrostatic hydrogen bonding.",
            "oxidizing coordinated water molecules to produce molecular oxygen and free protons."
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Lewis Acidic Polarization of Coordinated Ligands]</strong> A Lewis acid accepts electron density, polarizing coordinated bonds and dramatically depressing the pKa of bound protic ligands.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Definition</em>: Lewis acids are electron-pair acceptors. The divalent Zn²⁺ cation coordinates the lone pair of water's oxygen.<br>2. <em>Chemical Mechanism</em>: By drawing electron density toward the metal center, Zn²⁺ polarizes the O–H bond, stabilizing the conjugate base (hydroxide).<br>3. <em>Physiological Consequence</em>: This depression of water's pKa from ~14 to 7 generates a powerful hydroxide nucleophile at physiological pH.<br><br><em>Distractor Traps:</em><br>&bull; A (Lewis Acid/Base Inversion): States that Zn²⁺ donates an electron pair, which is the definition of a Lewis base, not an acid.<br>&bull; C (Charge Inversion): Bicarbonate is an anion; stabilizing its 'conjugate acid' (carbonic acid) does not drive hydroxide activation.<br>&bull; D (Redox Confabulation): Zn²⁺ is redox-inert in biological catalysis and does not oxidize water to oxygen."
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
            "His94 directly coordinates the catalytic Zn²⁺, whereas His64 resides on the surface.",
            "His64 is buried within the core, shielding the zinc ion from aqueous solvation.",
            "Acetazolamide acts as an uncompetitive inhibitor binding only to a His64-CO₂ complex.",
            "His94 undergoes phosphorylation during catalysis to maintain zinc ion coordination."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Active Site Coordination vs Peripheral Solvent Shuttling]</strong> Primary coordinating ligands directly maintain the metal-binding pocket, whereas peripheral shuttle residues modulate kinetic transfer without altering binding thermodynamics.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Structural Roles</em>: His94 is one of three direct dative ligands chelating Zn²⁺; His64 is an exocyclic residue extending into the solvent channel.<br>2. <em>Consequence of Alanine Substitution</em>: Mutating His94 abolishes a critical zinc-imidazole bond, destabilizing Zn²⁺ retention (Kd,Zn surges by 10⁵) and distorting the drug-binding pharmacophore (Ki surges 450-fold).<br>3. <em>His64 Independence</em>: Because His64 does not contact Zn²⁺ or acetazolamide, H64A leaves these thermodynamic binding constants intact.<br><br><em>Distractor Traps:</em><br>&bull; B (Structural Inversion): His94 is in the core pocket; His64 is surface-exposed to shuttle protons to solvent.<br>&bull; C (Inhibition Mode Confabulation): Acetazolamide is a classic competitive inhibitor that coordinates directly to Zn²⁺, not an uncompetitive inhibitor.<br>&bull; D (Biochemical Fiction): Histidine is not phosphorylated during CA II catalysis; coordination occurs via neutral dative bonding."
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
            "three ¹⁸O atoms and no ¹⁶O atoms.",
            "two ¹⁸O atoms and one ¹⁶O atom.",
            "one ¹⁸O atom and two ¹⁶O atoms.",
            "no ¹⁸O atoms and three ¹⁶O atoms."
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Isotopic Tracing of Metalloenzyme Addition Mechanisms]</strong> In carbonic anhydrase hydration, bicarbonate is formed by nucleophilic addition of a solvent-derived zinc-hydroxide across the electrophilic carbon of carbon dioxide.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Substrate Inventory</em>: Dissolved carbon dioxide provides the carbon atom and two oxygen atoms: both are ¹⁸O (C¹⁸O₂).<br>2. <em>Nucleophile Source</em>: The catalytic nucleophile is Zn²⁺–OH⁻, generated by deprotonating solvent water (H₂¹⁶O). Thus, the oxygen atom of the hydroxide is ¹⁶O.<br>3. <em>Product Stoichiometry</em>: Nucleophilic attack of [Zn–¹⁶OH]⁻ on C¹⁸O₂ produces HC¹⁸O₂¹⁶O⁻: exactly two ¹⁸O atoms and one ¹⁶O atom.<br><br><em>Distractor Traps:</em><br>&bull; A (Anhydrous Bicarbonate Error): Assumes bicarbonate oxygens originate exclusively from CO₂, ignoring solvent water incorporation.<br>&bull; C (Multiple Turnover Inversion): Reflects wash-out of ¹⁸O after numerous successive reversible hydration/dehydration cycles in excess H₂¹⁶O.<br>&bull; D (Total Exchange Fiction): Assumes complete isotopic exchange occurs with solvent prior to product release in a single turnover."
    }
]

cp_item2_qs = [
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
            "The hydrostatic pressure decreases significantly due to the dramatic increase in fluid velocity.",
            "The hydrostatic pressure increases significantly due to the immense friction of the vessel wall.",
            "The hydrostatic pressure remains unchanged because the volumetric flow rate is strictly conserved.",
            "The hydrostatic pressure increases proportionally with the square of the dynamic blood velocity."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: The Venturi Effect and Energy Density Conservation]</strong> In horizontal streamline flow, an increase in fluid velocity necessitates a concomitant decrease in static hydrostatic pressure to conserve total mechanical energy density.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Bernoulli Equation</em>: P₁ + &frac12;&rho;v₁² = P₂ + &frac12;&rho;v₂² (horizontal flow, &Delta;h = 0).<br>2. <em>Kinetic Energy Density Surge</em>: In the stenosis, blood velocity surges from 0.50 m/s to 8.00 m/s, causing kinetic energy density (&frac12;&rho;v²) to increase dramatically.<br>3. <em>Static Pressure Consequence</em>: Because the sum is constant, static lateral wall pressure P₂ must drop precipitously (Venturi effect).<br><br><em>Distractor Traps:</em><br>&bull; B (Intuitive Resistance Fallacy): Common student misconception that 'constriction increases pressure'; constriction increases resistance, but *lateral hydrostatic pressure* drops as kinetic energy rises.<br>&bull; C (Conservation Confusion): Confuses conservation of volumetric flow rate (A₁v₁ = A₂v₂) with constancy of pressure.<br>&bull; D (Direct Inversion): States hydrostatic pressure increases with velocity squared, which violates conservation of energy."
    },
    {
        "q": "What is the pressure drop &Delta;P attributable solely to the change in kinetic energy density between the proximal baseline segment (v₁ = 0.50 m/s) and the severe stenosis (v₂ = 8.00 m/s)?",
        "ch": [
            "1.06 × 10³ Pa",
            "3.38 × 10⁴ Pa",
            "6.75 × 10⁴ Pa",
            "4.24 × 10⁵ Pa"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Dynamic Pressure Drop in Constricted Conduits]</strong> The dynamic pressure loss between two points in horizontal inviscid flow equals the difference in their kinetic energy densities: &Delta;P = &frac12;&rho;(v₂² &minus; v₁²).<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Evaluate Velocity Squares</em>: v₁² = (0.50)² = 0.25 m²/s²; v₂² = (8.00)² = 64.0 m²/s².<br>2. <em>Calculate Velocity Difference</em>: v₂² &minus; v₁² = 64.0 &minus; 0.25 = 63.75 m²/s².<br>3. <em>Multiply by Half Density</em>: &Delta;P = 0.5 &times; (1060 kg/m³) &times; 63.75 m²/s² = 530 &times; 63.75 &asymp; 33,788 Pa = 3.38 &times; 10⁴ Pa.<br><br><em>Distractor Traps:</em><br>&bull; A (Linear Velocity Error): Evaluates &Delta;P = &frac12;&rho;(v₂ &minus; v₁) = 530 &times; 7.50 = 3975 Pa &asymp; 1.06 &times; 10³ Pa, forgetting to square velocities.<br>&bull; C (Omission of Half Factor): Calculates &Delta;P = &rho;(v₂² &minus; v₁²) = 1060 &times; 63.75 = 6.75 &times; 10⁴ Pa, forgetting the factor of &frac12;.<br>&bull; D (Dimensional Scaling Error): Incorrectly computes (v₂ &minus; v₁)² with wrong decimal placement, yielding 4.24 &times; 10⁵ Pa."
    },
    {
        "q": "In the severe stenosis segment, blood flow is expected to transition into post-stenotic turbulence primarily because:",
        "ch": [
            "the Reynolds number (3634) exceeds the critical transition value of 2000.",
            "the fluid density decreases proportionally as blood flow velocity surges.",
            "the dynamic viscosity increases dramatically with local shear strain rate.",
            "the acoustic velocity in human vascular tissue drops below 1540 meters/s."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Dimensionless Reynolds Criteria for Laminar-to-Turbulent Transition]</strong> Fluid flow in cylindrical vessels becomes turbulent when inertial forces dominate viscous dampening, parameterized by a Reynolds number exceeding ~2000.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Reynolds Formula</em>: Re = (&rho; &times; v &times; D) / &eta;.<br>2. <em>Data Interrogation</em>: Table 1 explicitly reports Re = 3634 for the severe stenosis.<br>3. <em>Physical Threshold</em>: In cylindrical conduits, Re < 2000 indicates laminar flow, whereas Re > 2000–3000 promotes vortex shedding and turbulent eddy formation.<br><br><em>Distractor Traps:</em><br>&bull; B (Incompressibility Violation): Blood is an incompressible liquid whose density remains invariant with velocity.<br>&bull; C (Non-Newtonian Inversion): Blood exhibits shear-thinning (viscosity *decreases* or remains flat at high shear rates, not increases).<br>&bull; D (Domain Mismatch): Acoustic speed of sound in tissue (1540 m/s) governs ultrasound imaging propagation, not fluid hydrodynamics."
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

cp_item3_qs = [
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
            "Appearance of a sharp carbonyl ester stretching frequency centered near 1715 cm⁻¹.",
            "Shift from a primary amine N–H doublet to a single secondary amine band at 3310 cm⁻¹.",
            "Complete disappearance of the aliphatic C–H stretching bands at 2850 to 2950 cm⁻¹.",
            "Emergence of an intense and broad hydroxyl O–H stretching band centered near 3200 cm⁻¹."
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Diagnostic Vibrational Modes of Primary and Secondary Amines]</strong> Primary amines exhibit two N–H stretching peaks (symmetric and asymmetric), whereas secondary amines exhibit exactly one N–H stretch.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Starting Material Inspection</em>: Compound 2 has an aniline primary amine (–NH₂) exhibiting two diagnostic N–H stretching bands (3450 and 3350 cm⁻¹).<br>2. <em>Post-Coupling Transformation</em>: Nucleophilic attack of the aniline nitrogen converts it into a secondary aryl amine (–NH–Ar), which exhibits a single N–H stretching band.<br>3. <em>Morpholine Invariance</em>: Morpholine is already a tertiary amine in the product and has no N–H stretch; thus, conversion of a doublet to a singlet uniquely pinpoints aniline coupling.<br><br><em>Distractor Traps:</em><br>&bull; A (Carbonyl Unrelatedness): Carbonyl stretches do not distinguish between primary and secondary amine functionalization.<br>&bull; C (Aliphatic Invariance): The aliphatic C–H bonds of the morpholine ring remain fully present in the coupled product.<br>&bull; D (Hydroxyl Confabulation): No alcohol or hydroxyl group is created during the amine coupling reaction."
    },
    {
        "q": "Why is the observed specific optical rotation [&alpha;] equal to 0.00° for pure Compound 5 in solution?",
        "ch": [
            "Compound 5 contains an equimolar mixture of diastereomeric atropisomers that cancel.",
            "Compound 5 lacks stereocenters and is an achiral molecule with a plane of symmetry.",
            "The dimethyl sulfoxide solvent undergoes mutarotation that quenches optical activity.",
            "Rapid nitrogen inversion in the morpholine ring converts a meso isomer into a racemate."
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Molecular Symmetry Criteria for Optical Inactivity]</strong> A molecule is optically active only if it is chiral (non-superimposable on its mirror image); molecules lacking stereocenters and possessing internal planes of symmetry are achiral and optically inactive.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Stereocenter Audit</em>: Compound 5 consists of planar aromatic rings (pyrimidine, phenyl) and a symmetrical morpholine ring lacking asymmetric carbons.<br>2. <em>Symmetry Evaluation</em>: The molecule possesses an internal plane of reflection and lacks restricted rotational hindrance (atropisomerism).<br>3. <em>Deduction</em>: Pure achiral molecules cannot rotate plane-polarized light, yielding an observed [&alpha;] = 0.00&deg;.<br><br><em>Distractor Traps:</em><br>&bull; A (Atropisomer Confabulation): The single biaryl bond lacks the bulky ortho-tetrasubstitution necessary to restrict rotation into atropisomers.<br>&bull; C (Solvent Fiction): DMSO is an achiral solvent and does not undergo mutarotation (which is specific to reducing sugars).<br>&bull; D (Amine Inversion Confusion): Nitrogen inversion occurs in tertiary amines, but does not convert meso compounds into racemates in an inherently achiral molecule."
    },
    {
        "q": "Based on Table 1, the 100-fold loss of potency in Analog 3b (IC₅₀ = 420 nM vs 4.2 nM in parent) when replacing –OCH₃ with –H indicates that the methoxy group:",
        "ch": [
            "participates in an essential hydrogen-bonding or electronic interaction with the kinase.",
            "serves exclusively as a hydrophobic steric shield protecting the ester from hydrolysis.",
            "undergoes metabolic oxidation in situ to form a covalent adduct with active site residues.",
            "is required to accelerate the rate of nucleophilic aromatic substitution in the enzyme."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Structure-Activity Relationships in Targeted Kinase Inhibition]</strong> Selective loss of inhibitory potency upon removing a functional group reveals the critical binding interactions mediated by that pharmacophore motif.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Analog 3b lacks the 3-methoxy substituent and displays a 100-fold increase in IC₅₀ (4.2 &rarr; 420 nM), reflecting a two orders-of-magnitude reduction in binding affinity.<br>2. <em>Binding Analysis</em>: A methoxy group acts as a hydrogen-bond acceptor via its ether oxygen and donates electron density into the phenyl ring via resonance.<br>3. <em>Conclusion</em>: Removing it strips the inhibitor of a critical binding contact within the ATP-binding pocket.<br><br><em>Distractor Traps:</em><br>&bull; B (Steric Shield Trap): In vitro enzyme assays measure direct kinase inhibition, not pharmacokinetic esterase degradation.<br>&bull; C (Covalent Zinc Fiction): Kinases utilize ATP and Mg²⁺, not catalytic zinc; nor do methoxy groups undergo covalent hydroxylation with metals.<br>&bull; D (Reaction Mode Error): The inhibitor acts via non-covalent binding to the kinase target, not by undergoing S_NAr with the enzyme."
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
            "decrease the aqueous solubility of the compound while increasing lipophilicity.",
            "increase the aqueous solubility of the compound by enhancing hydrogen bonding.",
            "cause the piperidine nitrogen to permanently lose its basic nucleophilic character.",
            "eliminate all inhibitory potency by preventing coordination to catalytic zinc."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Heteroatomic Contributions to Aqueous Solvation and Lipophilicity]</strong> Replacing an electronegative hydrogen-bond-accepting ether oxygen with a non-polar methylene group increases hydrophobicity and reduces aqueous solubility.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Structural Comparison</em>: Morpholine contains an oxygen atom that participates in dipole-dipole interactions and hydrogen bonding with water.<br>2. <em>Physicochemical Shift</em>: Piperidine replaces this oxygen with a –CH₂– unit, removing a hydrogen-bond acceptor.<br>3. <em>Pharmacological Consequence</em>: The compound becomes more hydrophobic/lipophilic (higher LogP) and less soluble in aqueous buffers.<br><br><em>Distractor Traps:</em><br>&bull; B (Direct Inversion): Piperidine lacks the ether oxygen, reducing hydrogen-bonding capacity with solvent water.<br>&bull; C (Electronic Fallacy): Piperidine is actually slightly *more* basic than morpholine because it lacks the electron-withdrawing oxygen atom.<br>&bull; D (Kinase Mechanism Error): Target kinase binding does not rely on coordination to catalytic zinc."
    }
]

cp_item4_qs = [
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
            "Nafion possesses negatively charged sulfonate groups that electrostatically repel ascorbate.",
            "Nafion contains positively charged quaternary amines that selectively bind dopamine cations.",
            "Ascorbic acid is too sterically bulky to permeate through the fluoropolymer pore matrix.",
            "Nafion catalytically oxidizes ascorbic acid to dehydroascorbic acid before it touches carbon."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Charge-Selective Electrostatic Permeation in Biosensors]</strong> Ion-exchange polymer coatings exclude interfering analytes based on charge complementarity with fixed functional groups.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Physiological Speciation</em>: At pH 7.4, ascorbic acid (pKa = 4.2) exists as an anion (ascorbate⁻), whereas dopamine (pKa = 8.9) exists as a cation (dopamine⁺).<br>2. <em>Membrane Chemistry</em>: Nafion is a sulfonated tetrafluoroethylene polymer decorated with fixed, negatively charged sulfonate groups (–SO₃⁻).<br>3. <em>Electrostatic Discrimination</em>: Anionic ascorbate is electrostatically repelled from the electrode surface, while cationic dopamine easily partitions across the membrane.<br><br><em>Distractor Traps:</em><br>&bull; B (Chemical Inversion): Nafion contains anionic sulfonates, not cationic quaternary ammonium groups.<br>&bull; C (Size-Exclusion Error): Ascorbate (MW ~176) and dopamine (MW ~153) are virtually identical in molecular size; exclusion is electrostatic, not steric.<br>&bull; D (Enzymatic Confabulation): Nafion is an inert polyfluorinated membrane, not a redox catalyst."
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
            "two-electron reduction of dopamine-o-quinone back to regenerated dopamine.",
            "reduction of dissolved molecular oxygen to hydrogen peroxide at the electrode.",
            "reduction of oxidized carbon surface functional groups to phenolic alcohols.",
            "electrochemical reduction of zinc cations present in the extracellular buffer."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Reversibility and Mass Transport in Cyclic Voltammetry]</strong> In a reversible or quasi-reversible redox couple, species oxidized during the forward anodic sweep remain near the diffusion layer and are reduced during the reverse cathodic sweep.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Forward Anodic Sweep</em>: Dopamine is oxidized at the carbon surface to dopamine-o-quinone (DOQ) with loss of 2 electrons and 2 protons.<br>2. <em>Reverse Cathodic Sweep</em>: As the potential sweeps back negatively, DOQ remaining in the immediate diffusion layer accepts 2 electrons and 2 protons.<br>3. <em>Deduction</em>: The cathodic current peak is the specific reduction of dopamine-o-quinone back to dopamine.<br><br><em>Distractor Traps:</em><br>&bull; B (Background Solvent Interference): Oxygen reduction occurs at substantially more negative potentials and is subtracted out via background subtraction.<br>&bull; C (Electrode Surface Background): Carbon surface oxide transitions contribute to the capacitive background current, not the analyte faradaic peak.<br>&bull; D (Extraneous Metal Trap): Extracellular buffer does not contain electroactive zinc ions in this voltammetric paradigm."
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

if __name__ == "__main__":
    print("Validating Items 1 to 4...")
    all_qs = cp_item1_qs + cp_item2_qs + cp_item3_qs + cp_item4_qs
    from upgrade_cp90 import validate_question
    all_issues = []
    for i, q in enumerate(all_qs):
        iss = validate_question(q, i+1)
        all_issues.extend(iss)
    if all_issues:
        print(f"Found {len(all_issues)} issues:")
        for iss in all_issues:
            print("  ", iss)
        sys.exit(1)
    else:
        print(f"All {len(all_qs)} questions in Items 1-4 passed all 5 gates with 100% compliance!")
