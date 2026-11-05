# scratch/upgrade_cp90_p5_to_p8.py
# Items 5 to 8 of EXAM_CP90 (Questions 25 to 52)
import sys

cp_item5_qs = [
    {
        "q": "Why does Entry 1 (LDA, THF, −78 °C) yield exclusively the kinetic enolate K (99:1 ratio)?",
        "ch": [
            "At −78 °C, the reaction is under thermodynamic control favoring the most stable enolate.",
            "The bulky diisopropylamide base deprotonates the less hindered C6 proton more rapidly.",
            "LDA coordinates directly to the carbonyl oxygen, forming an irreversible hemiketal bond.",
            "The thermodynamic enolate is unstable below 0 °C and undergoes spontaneous ring cleavage."
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Kinetic vs Thermodynamic Control in Enolate Deprotonation]</strong> A sterically hindered, strong base at cryogenic temperatures selectively removes the most sterically accessible alpha-proton under irreversible, non-equilibrating conditions.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Reagent Sterics</em>: Lithium diisopropylamide (LDA) possesses two bulky isopropyl groups that encounter high steric hindrance when approaching the more substituted C2 carbon.<br>2. <em>Kinetic Barrier</em>: Deprotonation at the less hindered C6 methylene carbon proceeds with a significantly lower activation energy (Ea_kin < Ea_therm), forming enolate K faster.<br>3. <em>Irreversibility</em>: At &minus;78 &deg;C in aprotic THF, there is no proton source to allow equilibration back to the starting ketone, trapping the kinetic product.<br><br><em>Distractor Traps:</em><br>&bull; A (Regime Inversion): Low temperature enforces kinetic control, not thermodynamic control; thermodynamic control favors the lowest free energy product at elevated temperatures.<br>&bull; C (Mechanism Confabulation): LDA acts as a Brønsted base to deprotonate the alpha position, not as a nucleophile forming a covalent hemiketal.<br>&bull; D (Decomposition Fiction): The thermodynamic enolate is stable once formed and does not undergo spontaneous ring cleavage below 0 &deg;C."
    },
    {
        "q": "In Entry 5, using a slight sub-stoichiometric amount of LDA (0.9 equivalents) at −78 °C eroded the kinetic ratio from 99:1 to 70:30. What caused this equilibration despite the low temperature?",
        "ch": [
            "Unreacted ketone (0.1 eq) acts as a proton shuttle, enabling reversible enolate equilibration.",
            "Lithium diisopropylamide decomposes into gaseous propene and ammonia through beta-elimination.",
            "Excess chlorotrimethylsilane catalyzes the rapid retro-aldol isomerization between enolates.",
            "The kinetic enolate tautomerizes directly into the thermodynamic enolate via 1,3-hydride shift."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Proton-Shuttle Equilibration in Sub-Stoichiometric Deprotonation]</strong> When a strong base is present in sub-stoichiometric amounts, unreacted neutral carbonyl molecules remain in solution, serving as weak acids that exchange protons with enolates to establish thermodynamic equilibrium.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Mass Balance Assessment</em>: Adding 0.9 equivalents of LDA deprotonates 90% of the ketone to form kinetic enolate K, leaving 10% unreacted neutral ketone.<br>2. <em>Proton Exchange Mechanism</em>: Kinetic enolate K can abstract an alpha-proton from the unreacted ketone (specifically at C2), generating the more stable thermodynamic enolate T and regenerating a ketone.<br>3. <em>Outcome</em>: Even at &minus;78 &deg;C, this intermolecular proton shuttle bypasses the high activation barrier, steadily isomerizing K into T.<br><br><em>Distractor Traps:</em><br>&bull; B (Reagent Decomposition Fiction): LDA is stable in THF at &minus;78 &deg;C and does not decompose into propene and ammonia.<br>&bull; C (Reagent Role Error): TMSCl acts as an electrophilic trapping agent (silylating enolates), not as a retro-aldol catalyst.<br>&bull; D (Symmetry-Forbidden Pericyclic Shift): Direct intramolecular 1,3-hydride shifts are geometrically constrained and symmetry-forbidden under orbital rules."
    },
    {
        "q": "Thermodynamic enolate T is more stable than kinetic enolate K primarily because:",
        "ch": [
            "it contains a more highly substituted (tetrasubstituted) carbon–carbon double bond.",
            "the formal negative charge resides entirely on the more electronegative carbon atom.",
            "it adopts an ideal chair conformation with an axial methyl group on the six-ring.",
            "it is aromatic and completely satisfies Hückel's 4n+2 cyclic conjugation rule."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Hyperconjugative and Orbital Stabilization of Substituted Alkenes]</strong> Enolates are resonance hybrids with substantial alkene character; more highly substituted carbon-carbon double bonds are thermodynamically favored due to hyperconjugation.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Structural Comparison</em>: Kinetic enolate K has a double bond between C1 and C6 (trisubstituted alkene). Thermodynamic enolate T has a double bond between C1 and C2 (tetrasubstituted alkene with two methyl groups).<br>2. <em>Electronic Stabilization</em>: Alkyl groups donate electron density into the &pi;* antibonding orbitals via hyperconjugation (&sigma;C–H &rarr; &pi;*), lowering the electronic ground state energy of the tetrasubstituted alkene.<br>3. <em>Conclusion</em>: Enolate T possesses greater thermodynamic stability because its C=C bond is tetrasubstituted.<br><br><em>Distractor Traps:</em><br>&bull; B (Resonance Inversion): In enolates, the major resonance contributor places negative charge on the more electronegative *oxygen* atom, not carbon.<br>&bull; C (Conformational Instability): Axial substituents experience destabilizing 1,3-diaxial steric strain, not stabilization.<br>&bull; D (Aromaticity Fabrication): Cyclic enolates are non-aromatic; they lack a continuous cyclic conjugated 4n+2 pi-system."
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
            "A carboxylic acid and a free secondary aliphatic alcohol.",
            "An ester and a cyclic alpha,beta-unsaturated enone motif.",
            "An aldehyde and a ketone in a single cleaved molecule.",
            "Two separate terminal dicarboxylic acid derivative units."
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Reductive Ozonolysis of Silyl Enol Ethers]</strong> Ozonolysis of an endocyclic silyl enol ether cleaves the double bond into two carbonyl moieties: the silylated carbon becomes a ketone (or ester derivative) and the alkene carbon becomes an aldehyde.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Substrate Structure</em>: The silyl enol ether of K has a double bond between C1 (bearing –OTMS and a methyl group) and C6 (an unsubstituted =CH– carbon).<br>2. <em>Ozonolysis Cleavage</em>: O₃ cleaves the C1=C6 double bond.<br>3. <em>Reductive Workup</em>: Me₂S reduces the molozonide/ozonide. C1 (bearing –OTMS and methyl) hydrolyzes to a methyl ketone, while C6 (bearing –H) becomes an aldehyde.<br><br><em>Distractor Traps:</em><br>&bull; A (Oxidative Over-Oxidation Trap): Carboxylic acids form under oxidative workup (H₂O₂), not mild reductive workup (Me₂S).<br>&bull; B (Conjugated Enone Error): Ozonolysis cleaves C=C bonds; it does not generate alpha,beta-unsaturated enones.<br>&bull; D (Intermolecular Cleavage Fiction): Cleaving an endocyclic double bond opens the ring into a single acyclic dicarbonyl molecule, not two separate fragments."
    },
    {
        "q": "Which of the following bases would be LEAST effective for selectively generating the kinetic enolate K at −78 °C?",
        "ch": [
            "Lithium diisopropylamide (LDA) in tetrahydrofuran solvent.",
            "Potassium hexamethyldisilazide (KHMDS) in tetrahydrofuran.",
            "Lithium tetramethylpiperidide (LiTMP) in aprotic solvent.",
            "Sodium hydride (NaH) suspended in dry dimethylformamide."
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Steric Discrimination in Kinetic Base Selection]</strong> Selective kinetic deprotonation requires a sterically demanding, soluble secondary amide base; small, unhindered, insoluble bases do not discriminate between alpha-protons.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Criteria for Kinetic Deprotonation</em>: The base must be (1) strong enough to deprotonate irreversibly, (2) bulky enough to favor the less hindered alpha-proton, and (3) soluble at cryogenic temperatures.<br>2. <em>Evaluation of Amide Bases</em>: LDA, KHMDS, and LiTMP are all sterically hindered, highly soluble amide bases that cleanly deprotonate C6.<br>3. <em>Evaluation of NaH</em>: NaH is a small, unhindered hydride ion that is insoluble in organic solvents, reacting heterogeneously and yielding thermodynamic equilibration.<br><br><em>Distractor Traps:</em><br>&bull; A (Ideal Kinetic Base): LDA is the gold-standard bulky kinetic base.<br>&bull; B (Effective Silyl Base): KHMDS features two bulky TMS groups and strongly favors kinetic deprotonation.<br>&bull; C (Hindered Piperidide): LiTMP is even more sterically hindered than LDA, providing excellent kinetic selectivity."
    }
]

cp_item6_qs = [
    {
        "q": "Based on the physical model of the myelin sheath as N identical membrane capacitors in series, wrapping 150 myelin lamellae around an axon causes the total membrane capacitance to:",
        "ch": [
            "increase by a factor of 150 due to the accumulation of surface charge.",
            "decrease by a factor of 150 due to the series arrangement of capacitors.",
            "remain constant because membrane capacitance depends only on axon length.",
            "increase proportionally to the square of the lamellae number (22,500-fold)."
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Series Capacitance and Transverse Dielectric Thickness]</strong> Capacitors in series add reciprocally; increasing the effective dielectric thickness of a membrane reduces its capacitance proportionally: C_total = C_single / N.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Circuit Model</em>: Each myelin layer acts as a parallel-plate capacitor with capacitance C_m. The 150 wraps are layered concentrically in series across the radial axis.<br>2. <em>Series Formula</em>: 1 / C_total = &Sigma;(1 / C_i) = 150 &times; (1 / C_m) &rArr; C_total = C_m / 150.<br>3. <em>Physical Consequence</em>: Total capacitance drops 150-fold, dramatically lowering the charge required to depolarize the membrane and accelerating action potential propagation.<br><br><em>Distractor Traps:</em><br>&bull; A (Parallel Capacitance Trap): Capacitors in *parallel* add directly (C_total = N &times; C), which applies to membrane surface area, not radial series layers.<br>&bull; C (Permittivity Fallacy): Total capacitance is inversely proportional to thickness d; adding 150 layers increases d by 150, reducing C.<br>&bull; D (Geometric Quadratic Error): Confuses series capacitance scaling with quadratic area equations."
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
            "Membrane resistance crashes and capacitance surges, collapsing the space constant.",
            "The resting equilibrium potential of potassium ions shifts from −90 mV up to 0 mV.",
            "Voltage-gated sodium channels are cleaved enzymatically from the paranodal axolemma."
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Cable Property Collapse in Demyelinating Neuropathies]</strong> Stripping the myelin sheath strips the high transverse resistance and low capacitance of the axon, causing local current to dissipate across the leaky naked membrane rather than flowing forward longitudinally.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Cable Parameter Shifts</em>: Demyelination exposes naked axolemma: transverse membrane resistance (r_m) drops precipitously, while membrane capacitance (c_m) surges 150-fold.<br>2. <em>Effect on Length Constant</em>: The space constant &lambda; = &radic;(r_m / r_i). When r_m crashes, &lambda; collapses, preventing passive current from reaching the next node of Ranvier.<br>3. <em>Effect on Time Constant</em>: Increased c_m delays membrane charging (&tau;_m = r_m &times; c_m), converting rapid saltatory conduction into sluggish, failing continuous conduction.<br><br><em>Distractor Traps:</em><br>&bull; A (Internal Resistance Misattribution): Axoplasmic resistance r_i is governed by intracellular diameter and ion mobility, which is not the primary driver of demyelination block.<br>&bull; C (Equilibrium Potential Fiction): Demyelination affects cable insulating properties, not the fundamental intracellular/extracellular potassium concentration gradient.<br>&bull; D (Channel Proteolysis Fiction): Sodium channels in the node remain intact initially; conduction fails due to electrical current leakage, not enzymatic channel proteolysis."
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
            "Increasing membrane capacitance and increasing axoplasmic core resistance.",
            "Increasing myelin sheath thickness and increasing internal axonal diameter.",
            "Decreasing axonal core radius and decreasing transverse membrane resistance.",
            "Decreasing extracellular sodium levels and decreasing ambient temperature."
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Optimization of Cable Parameters for Rapid Conduction]</strong> Conduction velocity is maximized by maximizing the length constant &lambda; (high r_m, low r_i) and minimizing the time constant &tau;_m (low c_m).<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Myelin Sheath Thickness</em>: Wrapping more myelin increases radial thickness, drastically lowering capacitance c_m (faster charging) and raising membrane resistance r_m (less leakage).<br>2. <em>Axonal Diameter</em>: Increasing axonal core radius r lowers internal longitudinal resistance r_i (r_i &prop; 1/r²), allowing current to travel farther forward.<br>3. <em>Synthesis</em>: Large-diameter, heavily myelinated fibers (A&alpha; motor fibers) achieve the highest conduction velocities in biology (~120 m/s).<br><br><em>Distractor Traps:</em><br>&bull; A (Direct Inversion): Higher capacitance and higher internal resistance both severely slow conduction velocity.<br>&bull; C (Opposite Direction Trap): Decreasing radius and decreasing membrane resistance collapse the space constant &lambda;.<br>&bull; D (Inhibition Trap): Lowering sodium concentration reduces action potential amplitude and cooling slows channel kinetics."
    }
]

cp_item7_qs = [
    {
        "q": "What is the formal oxidation state and d-electron count of the central platinum atom in cisplatin, cis-[Pt(NH₃)₂Cl₂]?",
        "ch": [
            "Pt(0), d¹⁰",
            "Pt(II), d⁸",
            "Pt(II), d⁶",
            "Pt(IV), d⁶"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Coordination Complex Oxidation States and d-Electron Accounting]</strong> Formal metal oxidation state equals overall complex charge minus the sum of formal ligand charges; d-electron count equals group number minus oxidation state.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Ligand Charges</em>: Ammine (NH₃) is a neutral ligand (charge = 0); chloride (Cl⁻) is an anionic ligand (charge = &minus;1).<br>2. <em>Solve for Platinum Charge</em>: Total charge = 0 &rArr; Pt + 2(0) + 2(&minus;1) = 0 &rArr; Pt = +2, so platinum is Pt(II).<br>3. <em>Count d-Electrons</em>: Platinum is in Group 10. For Pt(II), d-electron count = 10 &minus; 2 = 8 (d⁸ configuration).<br><br><em>Distractor Traps:</em><br>&bull; A (Neutral Metal Fallacy): Mistakenly treats coordinated chlorides as neutral chlorine radicals (Pt(0), d¹⁰).<br>&bull; C (Group 8 Error): Confuses platinum with Group 8 iron/ruthenium, miscalculating 8 &minus; 2 = 6.<br>&bull; D (Over-Oxidation to Pt IV): Occurs in octahedral prodrugs like oxaliplatin derivatives, not square planar cisplatin."
    },
    {
        "q": "Why does cisplatin remain predominantly intact in extracellular blood plasma, but undergoes rapid aquation upon entering the cytoplasm of a tumor cell?",
        "ch": [
            "High extracellular chloride (100 mM) suppresses aquation via Le Chatelier's rule.",
            "Intracellular glutathione directly reduces Pt(II) to insoluble metallic platinum Pt(0).",
            "Blood serum albumin covalently binds both chloride ligands, preventing ligand exchange.",
            "Tumor cells possess high lysosomal pH that catalytically accelerates ester hydrolysis."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Thermodynamic Chloride Suppression of Platinum Aquation]</strong> Aquation of cisplatin is a reversible nucleophilic displacement of chloride by water: [Pt(NH₃)₂Cl₂] + H₂O &rightleftharpoons; [Pt(NH₃)₂Cl(H₂O)]⁺ + Cl⁻.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Extracellular Environment</em>: Blood plasma maintains a high chloride concentration ([Cl⁻] &asymp; 100 mM), driving the equilibrium far to the left (intact neutral drug).<br>2. <em>Intracellular Environment</em>: Upon entering the cell, cytoplasmic chloride plummets to [Cl⁻] &asymp; 4–10 mM.<br>3. <em>Le Chatelier's Shift</em>: The 10- to 20-fold drop in chloride shifts the equilibrium toward the mono- and diaqua cationic complexes, which are the active electrophiles that crosslink DNA.<br><br><em>Distractor Traps:</em><br>&bull; B (Redox Inactivation Fallacy): Glutathione can detoxify platinum by coordinating sulfur, but does not reduce Pt(II) to metallic Pt(0).<br>&bull; C (Albumin Binding Error): Albumin binds platinum slowly and irreversibly, but does not protect chloride ligands from water exchange.<br>&bull; D (pH Inversion): Tumor microenvironments are acidic, not alkaline; furthermore, aquation is inorganic ligand displacement, not ester hydrolysis."
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
            "Transplatin cannot form intrastrand 1,2-d(GpG) crosslinks due to geometric constraints.",
            "Transplatin decomposes spontaneously into metallic platinum before entering tumor cells.",
            "The trans ammine ligands are irreversible competitive inhibitors of cellular RNA polymerase.",
            "Transplatin has a net formal charge of +2 that prevents passive plasma membrane diffusion."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Stereochemical Requirements for Intrastrand DNA Bifunctional Adducts]</strong> Cisplatin's cytotoxicity relies on forming 1,2-intrastrand crosslinks between adjacent guanine bases, inducing a severe ~35° bend in DNA that prevents repair.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Spatial Geometry</em>: In cisplatin, the two labile chloride leaving groups are mutually cis (90&deg; separation, ~3.3 &Aring; apart). This distance perfectly matches the distance between adjacent purines on a DNA strand.<br>2. <em>Transplatin Geometry</em>: In transplatin, the leaving groups are trans (180&deg; separation, ~4.7 &Aring; apart). It cannot form 1,2-intrastrand crosslinks, forming instead less toxic 1,3-crosslinks and interstrand links.<br>3. <em>Biological Repair</em>: DNA repair machinery easily excises transplatin adducts, rendering it therapeutically ineffective.<br><br><em>Distractor Traps:</em><br>&bull; B (Decomposition Fiction): Transplatin is chemically stable in solution and does not decompose into metallic platinum.<br>&bull; C (Enzyme Mode Fiction): Ammine ligands do not directly bind RNA polymerase as competitive inhibitors.<br>&bull; D (Charge Equivalence): Both cisplatin and transplatin are neutral complexes (formal charge = 0) with identical molecular formulas."
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

cp_item8_qs = [
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
            "BF₃ + :NH₃ → F₃B:NH₃ via coordinate electron-pair dative donation.",
            "CH₃COOH + H₂O ⇌ CH₃COO⁻ + H₃O⁺ via reversible hydronium transfer.",
            "NH₄⁺ + OH⁻ → NH₃ + H₂O through direct ammonium deprotonation step."
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Lewis Electron-Pair Donation vs Brønsted-Lowry Proton Transfer]</strong> A Lewis acid-base reaction involves donation and acceptance of an electron pair to form a coordinate covalent bond without necessarily transferring a hydrogen ion (proton).<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Identify Electron Deficient Species</em>: Boron trifluoride (BF₃) has an incomplete valence octet (6 valence electrons, vacant 2p orbital on boron), acting as a quintessential Lewis acid.<br>2. <em>Identify Electron Rich Species</em>: Ammonia (:NH₃) has a lone pair on nitrogen, acting as a Lewis base.<br>3. <em>Bond Formation</em>: Nitrogen donates its lone pair into boron's empty p-orbital, forming a neutral adduct (F₃B&larr;NH₃) without transferring any protons.<br><br><em>Distractor Traps:</em><br>&bull; A (Brønsted Neutralization): Involves transfer of a proton from HCl to OH⁻.<br>&bull; C (Brønsted Dissociation): Involves transfer of a proton from acetic acid to water.<br>&bull; D (Brønsted Acid-Base): Involves transfer of a proton from ammonium cation to hydroxide."
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

if __name__ == "__main__":
    print("Validating Items 5 to 8...")
    all_qs = cp_item5_qs + cp_item6_qs + cp_item7_qs + cp_item8_qs
    from upgrade_cp90 import validate_question
    all_issues = []
    for i, q in enumerate(all_qs):
        iss = validate_question(q, i+25)
        all_issues.extend(iss)
    if all_issues:
        print(f"Found {len(all_issues)} issues:")
        for iss in all_issues:
            print("  ", iss)
        sys.exit(1)
    else:
        print(f"All {len(all_qs)} questions in Items 5-8 passed all 5 gates with 100% compliance!")
