# /home/cgslinde/DrillRoom/DrillRoom/scratch/cp5/discretes.py
"""
Discrete Questions: Topics 275 to 284 (Questions 43 to 52)
"""

discrete_data = {
    "id": "exam_cp90_5_disc",
    "sec": "C/P",
    "topic": "C/P Standalone Discrete Questions",
    "sheet": None,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_5",
    "passage": "",
    "qs": [
        {
            "q": "In clinical thermodilution, a bolus of cold saline ($I = 10\\text{ mL}$ at $0^\\circ\\text{C}$) is injected into the right atrium, and blood temperature is recorded downstream in the pulmonary artery over time. Cardiac output ($CO$) is calculated via the Stewart-Hamilton equation:\n$$CO = \\frac{I}{\\int_0^\\infty \\Delta T(t)\\,dt}$$\nwhere the denominator represents the area under the temperature-time dilution curve (AUC). If an athlete undergoing treadmill exercise increases cardiac output from $5.0\\text{ L/min}$ to $20.0\\text{ L/min}$, how does the thermodilution curve change, assuming an identical indicator bolus?",
            "ch": [
                "The area under the curve quadruples as faster flow concentrates the thermal bolus",
                "The area under the curve drops to one-fourth as faster flow clears thermal bolus",
                "The area under the curve remains unchanged because indicator mass is conserved in",
                "The area under the curve doubles while peak dilution amplitude drops to baseline"
            ],
            "a": 1,
            "e": "<strong>Stewart-Hamilton indicator dilution and flow rate inverse proportionality:</strong> The Stewart-Hamilton principle expresses conservation of indicator mass. Rearranging the formula demonstrates that the area under the concentration (or temperature) dilution curve is inversely proportional to volumetric flow rate: $\\int_0^\\infty \\Delta T(t)\\,dt = \\frac{I}{CO}$. When cardiac output quadruples from $5.0\\text{ L/min}$ to $20.0\\text{ L/min}$ ($CO' = 4 CO$), the larger volume of blood flowing past the detector dilutes and clears the cold thermal bolus four times faster. Consequently, the integral of temperature change over time drops to one-fourth ($\\text{AUC}' = \\frac{1}{4}\\text{AUC}$) of its resting value.<br><br><em>Distractor Traps:</em><br>&bull; A erroneously claims AUC quadruples, which would imply cardiac output decreased to one-fourth.<br>&bull; C argues that conservation of indicator mass keeps AUC constant, ignoring the fact that indicator concentration depends on dilution volume per unit time.<br>&bull; D arbitrarily doubles the area while assuming peak amplitude drops to baseline.",
            "d": True
        },
        {
            "q": "A respiratory physiologist measures lung volume as a function of transpulmonary pressure ($P_{\\text{tp}} = P_{\\text{alv}} - P_{\\text{ip}}$) during a full inflation-deflation cycle. The resulting pressure-volume loop exhibits marked hysteresis, such that at any given intermediate lung volume, transpulmonary pressure is higher during inspiration than during expiration. What is the fundamental physical explanation for this hysteresis phenomenon?",
            "ch": [
                "Alveolar pressure becomes positive during inspiration, expelling gas from bronchi",
                "Intrapleural fluid volume expands during inspiration, altering hydrostatic heads",
                "Surface tension is higher during inflation than deflation due to surfactant delay",
                "Elastic fibers in parenchyma stretch reversibly without any viscous dissipation"
            ],
            "a": 2,
            "e": "<strong>Alveolar surface tension hysteresis and surfactant dynamics:</strong> Pulmonary pressure-volume hysteresis is primarily governed by the kinetic behavior of pulmonary surfactant at the alveolar air-liquid interface. During inspiration (inflation), the alveolar surface area expands rapidly. The recruitment and adsorption of surfactant phospholipids (DPPC) into the expanding surface monolayer lags behind area expansion, resulting in a transiently higher surface tension ($\\gamma$). By the Young-Laplace law ($\\Delta P = 2\\gamma / r$), higher surface tension requires a greater distending transpulmonary pressure to hold any given volume. During expiration (deflation), the monolayer is compressed, packing surfactant molecules tightly and driving surface tension to near zero, requiring much less pressure to maintain volume.<br><br><em>Distractor Traps:</em><br>&bull; A claims alveolar pressure becomes positive during inspiration; alveolar pressure is negative during spontaneous inhalation.<br>&bull; B refers to intrapleural fluid volume shifts, which are negligible and do not account for PV loop hysteresis.<br>&bull; D asserts parenchymal fibers stretch purely reversibly without energy dissipation; tissue viscoelasticity and surface tension recruitments are dissipative processes.",
            "d": True
        },
        {
            "q": "Transvascular fluid movement across capillary endothelia is governed by the Starling equation: $J_v = L_p A [(P_c - P_i) - \\sigma (\\pi_c - \\pi_i)]$. In a healthy skeletal muscle capillary bed, albumin has a reflection coefficient of $\\sigma = 0.95$. In a patient with septic shock, bacterial endotoxins induce severe endothelial glycocalyx degradation and intercellular gap widening. If the reflection coefficient for albumin drops to $\\sigma = 0.10$, how will this change affect transvascular fluid movement?",
            "ch": [
                "Fluid filtration into interstitium accelerates, causing profound systemic edema",
                "Fluid reabsorption into capillaries accelerates, expanding vascular blood volume",
                "Oncotic pressure difference triples, perfectly buffering capillary pressure rise",
                "Transvascular fluid flux ceases entirely because albumin reaches dynamic balance"
            ],
            "a": 0,
            "e": "<strong>Staverman reflection coefficient and Starling oncotic balance in sepsis:</strong> In the Starling equation, the effective colloid osmotic pressure opposing filtration is given by $\\sigma (\\pi_c - \\pi_i)$. The Staverman reflection coefficient $\\sigma$ represents the fraction of osmotic pressure actually exerted across the membrane. When $\\sigma = 0.95$, the capillary membrane retains albumin effectively, generating a powerful inward osmotic pull that counterbalances capillary hydrostatic pressure ($P_c$). When glycocalyx breakdown drops $\\sigma$ to $0.10$, the capillary becomes freely permeable to albumin, abolishing over $90\\%$ of the effective colloid oncotic gradient. Hydrostatic pressure ($P_c$) then acts unopposed, driving massive transvascular fluid filtration into the interstitial space, precipitating severe hypovolemic shock and peripheral edema.<br><br><em>Distractor Traps:</em><br>&bull; B reverses the direction of fluid shift, claiming reabsorption into capillaries increases.<br>&bull; C claims oncotic pressure difference triples, which contradicts the loss of membrane selectivity.<br>&bull; D asserts fluid flux ceases, ignoring the substantial unbuffered hydrostatic filtration pressure.",
            "d": True
        },
        {
            "q": "Pulse wave velocity (PWV) is the speed at which the arterial pressure wave propagates through the arterial tree, modeled by the Moens-Korteweg equation:\n$$PWV = \\sqrt{\\frac{E \\cdot h}{\\rho \\cdot D}}$$\nwhere $E$ is Young's modulus of wall elasticity (vascular stiffness), $h$ is arterial wall thickness, $\\rho$ is blood density, and $D$ is internal vessel diameter. In an elderly patient with severe arteriosclerosis and vascular calcification, arterial wall Young's modulus ($E$) increases by a factor of 4 while wall thickness, vessel caliber, and blood density remain relatively constant. How is the patient's arterial pulse wave velocity altered?",
            "ch": [
                "PWV is quartered, slowing the transmission of the pulse wave to distal limbs",
                "PWV is halved, delaying the arrival of reflected pressure waves at the heart",
                "PWV quadruples, causing severe attenuation of distal peripheral pulse peaks",
                "PWV doubles, causing arterial pressure waves to travel twice as fast to limbs"
            ],
            "a": 3,
            "e": "<strong>Moens-Korteweg equation and vascular stiffness scaling:</strong> The Moens-Korteweg equation indicates that pulse wave velocity is proportional to the square root of Young's modulus of wall elasticity: $PWV \\propto \\sqrt{E}$. When vascular calcification and loss of elastic lamellae increase arterial wall stiffness four-fold ($E' = 4E$), the new pulse wave velocity becomes $PWV' = \\sqrt{4E \\cdot h / (\\rho D)} = 2 \\sqrt{E \\cdot h / (\\rho D)} = 2 PWV$. Thus, PWV doubles ($2.0$-fold increase). Faster pulse wave propagation causes wave reflections from peripheral vascular branch points to return early during systole rather than diastole, augmenting central aortic systolic blood pressure and widening pulse pressure.<br><br><em>Distractor Traps:</em><br>&bull; A inverts the relationship and squares the factor, claiming PWV is quartered ($1/4$).<br>&bull; B inverts the square root relationship, claiming PWV is halved ($1/2$).<br>&bull; C fails to take the square root of the stiffness increase, falsely asserting that PWV quadruples ($4\\times$).",
            "d": True
        },
        {
            "q": "Goldmann applanation tonometry measures intraocular pressure (IOP) based on the Imbert-Fick law ($P = F / A$), which states that internal fluid pressure equals the external force ($F$) required to flatten a spherical membrane over a circular contact area ($A$). If a tonometer applies an applanation force of $F = 0.032\\text{ N}$ to flatten a standardized circular corneal area of $A = 7.35 \\times 10^{-6}\\text{ m}^2$, what is the measured intraocular pressure in millimeters of mercury ($1\\text{ mmHg} \\approx 133.3\\text{ Pa}$)?",
            "ch": [
                "16.3 mmHg",
                "32.7 mmHg",
                "49.0 mmHg",
                "65.3 mmHg"
            ],
            "a": 1,
            "e": "<strong>Imbert-Fick law and tonometric pressure conversion:</strong> Pressure is defined as force per unit area: $P = \\frac{F}{A}$. Substituting the measured applanation force and area: $P = \\frac{0.032\\text{ N}}{7.35 \\times 10^{-6}\\text{ m}^2} \\approx 4353.7\\text{ Pa}$. To convert Pascals to clinical units of millimeters of mercury (mmHg): $P = \\frac{4353.7\\text{ Pa}}{133.3\\text{ Pa/mmHg}} \\approx 32.66\\text{ mmHg} \\approx 32.7\\text{ mmHg}$. An IOP of 32.7 mmHg is significantly elevated above the normal range ($10&ndash;21\\text{ mmHg}$), indicating ocular hypertension and high risk for glaucomatous optic neuropathy.<br><br><em>Distractor Traps:</em><br>&bull; A (16.3 mmHg) halves the correct result by dividing by 2 or doubling the effective area.<br>&bull; C (49.0 mmHg) multiplies the correct result by 1.5, assuming an incorrect calibration factor.<br>&bull; D (65.3 mmHg) doubles the calculated pressure by neglecting the standard radius-to-diameter conversion.",
            "d": True
        },
        {
            "q": "Left ventricular stroke work (SW) represents the mechanical external work generated by the myocardium during a single cardiac cycle, mathematically expressed as the integral of pressure over volume: $SW = \\oint P\\,dV$. On a left ventricular pressure-volume (PV) loop, how is stroke work graphically determined?",
            "ch": [
                "The slope of the end-systolic elastance line connecting the loop origin",
                "The total rectangular area under the end-diastolic pressure boundary axis",
                "The total area enclosed within the four boundaries of the cyclical PV loop",
                "The difference between end-diastolic volume and end-systolic volume points"
            ],
            "a": 2,
            "e": "<strong>Left ventricular pressure-volume loop area and stroke work:</strong> Mechanical work is defined as the integral of force over displacement, which in fluid systems translates to $W = \\int P\\,dV$. Over a complete closed cardiac cycle, the net external mechanical work performed by the left ventricle on the ejected stroke volume is represented by the enclosed cyclic line integral $\\oint P\\,dV$. On a standard pressure-volume loop, this integral equals the exact two-dimensional area enclosed within the four continuous phases: isovolumetric contraction, ventricular ejection, isovolumetric relaxation, and ventricular filling.<br><br><em>Distractor Traps:</em><br>&bull; A describes end-systolic elastance ($E_{\\text{es}}$), which is a measure of myocardial contractility (slope), not stroke work.<br>&bull; B describes the area under the end-diastolic pressure-volume relationship (EDPVR), which relates to passive diastolic compliance.<br>&bull; D describes stroke volume ($SV = EDV - ESV$), which is a volume displacement rather than mechanical work ($P \\times \\Delta V$).",
            "d": True
        },
        {
            "q": "Coulomb's law describes the electrostatic force between two point charges: $F = k_e \\frac{|q_1 q_2|}{\\epsilon_r r^2}$, where $\\epsilon_r$ is the relative dielectric constant of the surrounding medium. An ionic salt bridge between a positively charged arginine guanidinium group and a negatively charged aspartate carboxylate group has an inter-charge separation distance of $r = 0.35\\text{ nm}$. If this salt bridge is relocated from the solvent-exposed protein surface (surrounded by aqueous bulk water, $\\epsilon_r \\approx 80$) to the buried hydrophobic protein core ($\\epsilon_r \\approx 4$), how does the electrostatic attractive force change?",
            "ch": [
                "The electrostatic attraction decreases to one-twentieth of its previous value",
                "The electrostatic attraction decreases to one-four-hundredth of surface value",
                "The electrostatic attraction remains unchanged because charge distance is fixed",
                "The electrostatic attraction increases to twenty times its solvent-exposed value"
            ],
            "a": 3,
            "e": "<strong>Dielectric screening and Coulombic salt bridge stabilization:</strong> Coulomb's law states that the electrostatic force between charges is inversely proportional to the dielectric constant of the intervening solvent medium ($F \\propto 1/\\epsilon_r$). Bulk aqueous water has a very high dielectric constant ($\\epsilon_r \\approx 80$) because its polar dipoles reorient around ions, screening their charges and weakening electrostatic interactions. In contrast, the nonpolar hydrophobic core of a globular protein contains closely packed hydrocarbon side chains with minimal dipole mobility, resulting in a low dielectric constant ($\\epsilon_r \\approx 4$). Relocating the salt bridge from water to the core scales the attractive force by $\\frac{F_{\\text{core}}}{F_{\\text{water}}} = \\frac{\\epsilon_{r,\\text{water}}}{\\epsilon_{r,\\text{core}}} = \\frac{80}{4} = 20$. The attractive force increases 20-fold, providing immense conformational stability.<br><br><em>Distractor Traps:</em><br>&bull; A inverts the dielectric ratio, incorrectly predicting that low dielectric decreases electrostatic attraction.<br>&bull; B squares the dielectric ratio ($(80/4)^2 = 400$) and inverts it.<br>&bull; C incorrectly assumes the dielectric constant has no effect on Coulombic interactions when distance is fixed.",
            "d": True
        },
        {
            "q": "In a standard protein $\\alpha$-helix, each amino acid peptide unit possesses an individual electric dipole moment oriented along the peptide bond ($\\text{N}-\\text{H}\\cdots\\text{O}=\\text{C}$). Because all hydrogen bonds point in the same direction parallel to the helical cylinder axis, these microdipoles sum vectorially to generate an overall helix macrodipole. How is this macrodipole oriented, and which functional consequence does it produce?",
            "ch": [
                "Positive at the N-terminus and negative at C-terminus; binds phosphate ligands",
                "Negative at the N-terminus and positive at C-terminus; binds magnesium cations",
                "Neutral across both termini; prevents any electrostatic interaction with ions",
                "Symmetrically positive at both termini; repels all polar and charged peptides"
            ],
            "a": 0,
            "e": "<strong>Peptide alpha-helix macrodipole and ligand binding polarity:</strong> In an $\\alpha$-helix, the dipole moments of individual peptide bonds ($\\sim 3.5\\text{ Debye}$, pointing from the partially positive amide $\\text{N}-\\text{H}$ to the partially negative carbonyl $\\text{C}=\\text{O}$) are aligned in parallel along the longitudinal axis of the helix. Summing these microdipoles over multiple turns generates a cumulative helix macrodipole with an effective partial charge of approximately $+0.5e$ at the N-terminus and $-0.5e$ at the C-terminus. Consequently, the electropositive N-terminus commonly functions as a binding site for negatively charged ligands, such as the phosphate moieties of ATP and GTP (e.g., the Walker A motif / P-loop).<br><br><em>Distractor Traps:</em><br>&bull; B reverses the electrostatic polarity of the helix macrodipole, falsely placing negative charge at the N-terminus.<br>&bull; C falsely asserts the helix is electrically neutral along its axis, ignoring the constructive alignment of backbone peptide dipoles.<br>&bull; D invents a symmetric positive charge distribution, violating dipole conservation of charge.",
            "d": True
        },
        {
            "q": "Electrostatic potential energy between two point charges is given by $U = \\frac{k_e q_1 q_2}{\\epsilon_r r}$. In an allosteric enzyme, protein kinase A phosphorylates a regulatory serine residue, appending a dianionic phosphate group ($-\\text{PO}_4^{2-}$ at pH 7.4) located $0.50\\text{ nm}$ from an adjacent glutamate residue ($-\\text{COO}^-$). What energetic change occurs at this locus, and how does it drive an allosteric conformational switch?",
            "ch": [
                "Negative potential energy forms, stabilizing a strong salt bridge attraction",
                "Positive potential energy causes repulsion, driving a conformational opening",
                "Potential energy drops to zero, abolishing all steric and electrostatic forces",
                "Electrons transfer covalently to glutamate, forming a transient ester linkage"
            ],
            "a": 1,
            "e": "<strong>Electrostatic potential energy and phosphorylation-driven conformational switches:</strong> Electrostatic potential energy between charges of like sign ($q_1 < 0$ and $q_2 < 0$) is positive ($U > 0$), representing an energetically unfavorable, repulsive interaction. Introducing a bulky, dianionic phosphate group ($-\\text{PO}_4^{2-}$) adjacent to an already negatively charged glutamate carboxylate side chain ($-\\text{COO}^-$) creates strong Coulombic repulsion. To minimize this repulsive electrostatic potential energy and return to a thermodynamically favored ground state, the local polypeptide backbone undergoes a conformational rearrangement that rotates or displaces the two acidic moieties away from each other, propagating structural changes throughout the enzyme.<br><br><em>Distractor Traps:</em><br>&bull; A claims negative potential energy and attractive salt bridges form; like negative charges repel each other, producing positive potential energy.<br>&bull; C asserts potential energy becomes zero, ignoring the strong non-zero Coulombic field between the charges.<br>&bull; D invents a covalent electron transfer forming an anhydride/ester, which is biochemically inaccurate.",
            "d": True
        },
        {
            "q": "A mammalian cell maintains a resting membrane potential of $\\Delta V = -70\\text{ mV} = -7.0 \\times 10^{-2}\\text{ V}$ across its plasma membrane (cytosolic interior negative relative to extracellular fluid). Assuming the hydrophobic core of the lipid bilayer has a uniform thickness of $d = 4.0\\text{ nm} = 4.0 \\times 10^{-9}\\text{ m}$ and acts as an idealized parallel-plate capacitor, what is the magnitude of the electric field ($E = \\Delta V / d$) across the membrane, and how are equipotential surfaces oriented?",
            "ch": [
                "E = 1.75 x 10^4 V/m; equipotential surfaces run perpendicular to membrane planes",
                "E = 2.80 x 10^5 V/m; equipotential surfaces spiral along helical lipid channels",
                "E = 1.75 x 10^7 V/m; equipotential surfaces run parallel to the membrane planes",
                "E = 2.80 x 10^8 V/m; equipotential surfaces form concentric spherical spheres"
            ],
            "a": 2,
            "e": "<strong>Membrane electric field gradient and equipotential planar geometry:</strong> The magnitude of a uniform electric field between two parallel conductive plates is given by $E = \\frac{|\\Delta V|}{d}$. Substituting the membrane parameters: $E = \\frac{7.0 \\times 10^{-2}\\text{ V}}{4.0 \\times 10^{-9}\\text{ m}} = 1.75 \\times 10^7\\text{ V/m}$. This represents an immense electric field gradient ($17.5\\text{ million volts per meter}$) across the thin lipid bilayer. Because electric field vectors point perpendicularly from the positive extracellular plate to the negative intracellular plate, equipotential surfaces (planes of constant electrical potential) run perpendicular to the field vectors and thus parallel to the lipid bilayer planes.<br><br><em>Distractor Traps:</em><br>&bull; A (1.75 x 10^4 V/m) miscalculates the nanometer power of ten ($10^{-6}$ instead of $10^{-9}$) and falsely claims equipotential lines are perpendicular to the membrane.<br>&bull; B (2.80 x 10^5 V/m) multiplies $\\Delta V$ by $d$ instead of dividing and invents spiraling equipotentials.<br>&bull; D (2.80 x 10^8 V/m) multiplies by 4 instead of dividing by 4 and describes concentric spheres.",
            "d": True
        }
    ]
}
