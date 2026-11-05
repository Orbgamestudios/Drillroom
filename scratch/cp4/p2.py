# /home/cgslinde/DrillRoom/DrillRoom/scratch/cp4/p2.py
"""
Passage 2: Topic 252 — Continuity Equation in Systemic Vascular Branching
"""

passage_data = {
    "id": "exam_cp90_4_p2",
    "sec": "C/P",
    "topic": "Continuity Equation & Microvascular Hemodynamics in Systemic Vascular Branching",
    "sheet": 2,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_4",
    "passage": "<div class=\"ttl\">Passage 2 (Questions 7&ndash;12)</div>\n"
               "<p>The human systemic circulation functions as a closed hydrodynamic circuit powered by the pulsatile ejection of blood from the left ventricle. Under steady-state conditions, conservation of mass for an incompressible fluid requires that the volumetric flow rate ($Q$) remain constant across any complete cross-section of the cardiovascular tree: $Q = A_{tot} \\cdot \\bar{v}$, where $A_{tot}$ represents the total cumulative cross-sectional area of all parallel conduits at a specific branching generation, and $\\bar{v}$ denotes the area-averaged linear flow velocity. Because blood is predominantly water, its density remains constant ($\\rho \\approx 1055\\text{ kg/m}^3$), satisfying the incompressibility criterion.</p>\n"
               "<p>As blood departs the ascending aorta, it traverses successive dichotomous and arborizing vascular bifurcations: large conduit arteries, muscular distributing arteries, terminal arterioles, capillary microvascular networks, postcapillary venules, and systemic veins, before coalescing into the inferior and superior venae cavae. Although individual vessel calibers diminish dramatically across distal generations&mdash;tapering from an aortic lumen diameter of $2.6\\text{ cm}$ down to capillary calibers of $8.0\\ \\mu\\text{m}$&mdash;the sheer multiplicity of parallel branches expands exponentially.</p>\n"
               "<p>To map microvascular fluid kinetics, biomedical engineers perfused an isolated mammalian mesentery preparation with a fluorophore-labeled dextran blood analogue under a constant physiological cardiac output of $Q = 84.0\\text{ cm}^3/\\text{s}$ ($5.04\\text{ L/min}$). High-speed intravital fluorescence video microscopy and pulsed-wave Doppler velocimetry tracked vessel caliber, estimated parallel vessel counts, total cross-sectional surface areas, and mean flow velocities across five anatomical vascular divisions. The quantitative measurements are summarized in Table 1.</p>\n"
               "<table class=\"tbl\">\n"
               "  <caption>Table 1 Morphometric and hemodynamic parameters across systemic vascular divisions</caption>\n"
               "  <thead>\n"
               "    <tr><th>Vascular Division</th><th>Mean Vessel Diameter ($d$)</th><th>Approximate Vessel Count ($N$)</th><th>Total Cross-Sectional Area ($A_{tot}$, cm$^2$)</th><th>Mean Blood Velocity ($\\bar{v}$, cm/s)</th><th>Mean Transit Time ($t$)</th></tr>\n"
               "  </thead>\n"
               "  <tbody>\n"
               "    <tr><td>Aorta</td><td>2.6 cm</td><td>1</td><td>5.3</td><td>15.8</td><td>0.03 s</td></tr>\n"
               "    <tr><td>Large Arteries</td><td>0.40 cm</td><td>160</td><td>20.1</td><td>4.18</td><td>0.24 s</td></tr>\n"
               "    <tr><td>Arterioles</td><td>30 &mu;m</td><td>$5.0 \\times 10^7$</td><td>353.4</td><td>0.238</td><td>0.84 s</td></tr>\n"
               "    <tr><td>Capillaries</td><td>8.0 &mu;m</td><td>$6.0 \\times 10^9$</td><td>3016.0</td><td>0.0278</td><td>1.08 s</td></tr>\n"
               "    <tr><td>Venae Cavae</td><td>3.0 cm</td><td>2</td><td>14.1</td><td>5.96</td><td>0.17 s</td></tr>\n"
               "  </tbody>\n"
               "</table>\n"
               "<p>Researchers also evaluated the hemodynamic impact of focal arterial stenoses on upstream and downstream velocity gradients.</p>",
    "qs": [
        {
            "q": "According to the continuity principle and data in Table 1, if the total cross-sectional area of the capillary bed expands from $3000\\text{ cm}^2$ to $4200\\text{ cm}^2$ during systemic vasodilation while volumetric flow rate remains at $84.0\\text{ cm}^3/\\text{s}$, what is the new mean capillary blood velocity?",
            "ch": [
                "0.010 cm/s",
                "0.050 cm/s",
                "0.020 cm/s",
                "0.080 cm/s"
            ],
            "a": 2,
            "e": "<strong>Continuity equation application:</strong> The continuity equation for an incompressible fluid dictates that volumetric flow rate is the product of cross-sectional area and average linear velocity: $Q = A \\cdot v$. Rearranging to solve for velocity gives $v = \\frac{Q}{A}$. Substituting the given parameters: $v = \\frac{84.0\\text{ cm}^3/\\text{s}}{4200\\text{ cm}^2} = 0.020\\text{ cm/s}$ ($0.20\\text{ mm/s}$). As the vascular bed vasodilates and recruits additional capillary units, total cross-sectional area rises and linear blood flow velocity slows proportionally.<br><br><em>Distractor Traps:</em><br>&bull; A (0.010 cm/s) erroneously doubles the cross-sectional area ($84 / 8400$).<br>&bull; B (0.050 cm/s) inverts the fraction or divides 4200 by 84 and misplaces decimal places ($4200 / 84 = 50$).<br>&bull; D (0.080 cm/s) incorrectly subtracts areas or uses $84 / 1050$."
        },
        {
            "q": "Which statement correctly compares the hemodynamic parameters of the capillaries to those of the aorta based on the principle of continuity?",
            "ch": [
                "Individual capillaries have higher flow rate and higher velocity than the aorta",
                "Individual capillaries have higher flow rate and lower velocity than the aorta",
                "Capillary bed has lower total flow rate and higher velocity than the aorta",
                "Capillary bed has equal total flow rate and lower velocity than the aorta"
            ],
            "a": 3,
            "e": "<strong>Continuity in branching vascular networks:</strong> In a closed circulatory loop without fluid loss, total volumetric flow rate ($Q$) is conserved across every vascular division: $Q_{aorta} = Q_{capillaries} = Q_{venae\\,cavae} = \\text{Cardiac Output}$. Because $Q = A_{tot} \\cdot \\bar{v}$, average blood velocity is inversely proportional to total cross-sectional area ($\\bar{v} = Q / A_{tot}$). The massive parallel branching of capillaries creates an enormous cumulative cross-sectional area ($A_{tot} \\approx 3016\\text{ cm}^2$) compared to the single aorta ($A \\approx 5.3\\text{ cm}^2$). Consequently, while the total capillary bed carries the exact same volumetric flow rate ($84.0\\text{ cm}^3/\\text{s}$), the linear blood velocity is orders of magnitude lower ($0.028\\text{ cm/s}$ vs $15.8\\text{ cm/s}$).<br><br><em>Distractor Traps:</em><br>&bull; A falsely claims individual capillaries carry higher flow rate and higher velocity; an individual capillary carries only a microscopic fraction ($Q/N \\approx 1.4 \\times 10^{-8}\\text{ cm}^3/\\text{s}$) at much lower velocity.<br>&bull; B erroneously asserts individual capillaries carry more volumetric flow than the entire aorta.<br>&bull; C violates conservation of mass by claiming total capillary flow rate is lower than aortic flow rate."
        },
        {
            "q": "A muscular branch artery with cross-sectional area $A_0 = 1.20\\text{ cm}^2$ conducting blood at $15.0\\text{ cm/s}$ bifurcates into two daughter branches of areas $A_1 = 0.80\\text{ cm}^2$ and $A_2 = 1.00\\text{ cm}^2$. If blood velocity in Branch 1 is $12.0\\text{ cm/s}$, what is the velocity in Branch 2?",
            "ch": [
                "8.40 cm/s",
                "6.20 cm/s",
                "4.80 cm/s",
                "9.60 cm/s"
            ],
            "a": 0,
            "e": "<strong>Bifurcation flow conservation:</strong> Incompressible continuity at a vascular bifurcation requires that total volumetric flow into the junction equals the sum of volumetric flows exiting through the daughter branches: $Q_0 = Q_1 + Q_2 \\implies A_0 v_0 = A_1 v_1 + A_2 v_2$. First, calculate parent vessel flow: $Q_0 = (1.20\\text{ cm}^2)(15.0\\text{ cm/s}) = 18.0\\text{ cm}^3/\\text{s}$. Next, calculate Branch 1 flow: $Q_1 = (0.80\\text{ cm}^2)(12.0\\text{ cm/s}) = 9.60\\text{ cm}^3/\\text{s}$. Subtracting gives Branch 2 flow: $Q_2 = Q_0 - Q_1 = 18.0 - 9.60 = 8.40\\text{ cm}^3/\\text{s}$. Solving for velocity in Branch 2: $v_2 = \\frac{Q_2}{A_2} = \\frac{8.40\\text{ cm}^3/\\text{s}}{1.00\\text{ cm}^2} = 8.40\\text{ cm/s}$.<br><br><em>Distractor Traps:</em><br>&bull; B (6.20 cm/s) results from subtracting velocities directly ($15.0 - 12.0 = 3.0$) and adding an arbitrary factor.<br>&bull; C (4.80 cm/s) mistakenly computes $(18.0 - 9.60) / 1.75$ or halves Branch 1 flow.<br>&bull; D (9.60 cm/s) assumes Branch 2 velocity equals Branch 1 volumetric flow rate."
        },
        {
            "q": "What is the primary physiological benefit derived from the marked reduction in linear blood velocity ($\\bar{v}$) observed within systemic capillaries?",
            "ch": [
                "Maximizing hydrostatic filtration pressure to eliminate plasma albumin",
                "Providing sufficient transit duration for diffusive capillary gas exchange",
                "Preventing laminar shear stress activation of endothelial nitric oxide",
                "Accelerating erythrocyte transit time through metabolic skeletal muscle"
            ],
            "a": 1,
            "e": "<strong>Physiological transit time for microvascular exchange:</strong> The inverse relationship between cumulative cross-sectional area and blood velocity ($v = Q / A_{tot}$) causes blood velocity to slow from ~16 cm/s in the aorta down to ~0.03 cm/s (0.3 mm/s) in capillaries. This marked deceleration provides a capillary transit time of approximately 0.75 to 1.5 seconds. This duration is essential to allow passive diffusion of oxygen, carbon dioxide, glucose, amino acids, and metabolic wastes across the endothelial membrane and interstitial fluid to reach equilibrium.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because capillaries are impermeable to plasma albumin; filtering albumin would destroy oncotic pressure and cause fatal edema.<br>&bull; C is incorrect because endothelial nitric oxide release is a normal regulatory response, not something to prevent.<br>&bull; D directly contradicts the physics; capillary architecture slows erythrocyte transit rather than accelerating it."
        },
        {
            "q": "An atheromatous plaque causes a concentric stenosis that narrows an artery's lumen diameter by 50% (from $4.0\\text{ mm}$ to $2.0\\text{ mm}$). If volumetric blood flow rate through the vessel remains constant, the blood velocity within the stenotic segment will:",
            "ch": [
                "decrease by a factor of 2",
                "increase by a factor of 2",
                "increase by a factor of 4",
                "decrease by a factor of 4"
            ],
            "a": 2,
            "e": "<strong>Continuity and stenosis velocity scaling:</strong> By the continuity equation, $v_1 A_1 = v_2 A_2 \\implies v_2 = v_1 \\left(\\frac{A_1}{A_2}\\right)$. For a circular cylindrical vessel, cross-sectional area is proportional to the square of diameter: $A = \\frac{\\pi d^2}{4}$, so $\\frac{A_1}{A_2} = \\left(\\frac{d_1}{d_2}\\right)^2$. Halving the diameter ($d_2 = 0.5\\,d_1$) reduces the cross-sectional area by a factor of $0.5^2 = 0.25$ (a 4-fold decrease). To maintain constant volumetric flow rate ($Q$), blood velocity must increase by a factor of $\\frac{1}{0.25} = 4$.<br><br><em>Distractor Traps:</em><br>&bull; A assumes velocity decreases and scales linearly with diameter.<br>&bull; B assumes velocity scales linearly with diameter ($v \\propto 1/d$) rather than quadratically ($v \\propto 1/d^2$).<br>&bull; D claims velocity decreases by a factor of 4, confusing the reduction in area with a reduction in velocity."
        },
        {
            "q": "Why is the blood flow velocity in the venae cavae ($5.96\\text{ cm/s}$) significantly lower than that in the aorta ($15.8\\text{ cm/s}$), despite both vessels carrying identical total volumetric flow ($Q$)?",
            "ch": [
                "The blood density within venous return vessels is significantly lower",
                "Venous blood experiences substantial dynamic friction along venous walls",
                "Gravity exerts an accelerating downward pull exclusively on aortic blood",
                "The cumulative cross-sectional area of the venae cavae exceeds the aorta"
            ],
            "a": 3,
            "e": "<strong>Comparative vascular cross-sectional geometry:</strong> By the continuity equation ($v = Q / A_{tot}$), when volumetric flow rate $Q$ is constant, linear velocity is strictly determined by cumulative cross-sectional area. As recorded in Table 1, the total cross-sectional area of the two venae cavae (superior and inferior) is $14.1\\text{ cm}^2$, whereas the cross-sectional area of the aorta is only $5.3\\text{ cm}^2$. Because the venae cavae have roughly 2.7 times the cross-sectional area of the aorta, the area-averaged blood velocity in the venae cavae must be approximately 2.7 times slower ($15.8 / 2.7 \\approx 5.96\\text{ cm/s}$).<br><br><em>Distractor Traps:</em><br>&bull; A is physically false; blood density is virtually identical in arteries and veins (~1055 kg/m^3).<br>&bull; B appeals to wall friction, but friction dictates pressure drop (Poiseuille resistance), not continuity-governed average velocity.<br>&bull; C is incorrect because gravity affects blood hydrostatic column pressure equally depending on height, not vascular cross-sectional velocity profiles."
        }
    ]
}
