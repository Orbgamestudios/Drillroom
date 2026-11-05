# /home/cgslinde/DrillRoom/DrillRoom/scratch/cp4/p4.py
"""
Passage 4: Topic 254 — Poiseuille Resistance & Vascular Vasoconstriction
"""

passage_data = {
    "id": "exam_cp90_4_p4",
    "sec": "C/P",
    "topic": "Poiseuille Resistance & Vascular Vasoconstriction in Arteriolar Hemodynamics",
    "sheet": 4,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_4",
    "passage": "<div class=\"ttl\">Passage 4 (Questions 19&ndash;24)</div>\n"
               "<p>Systemic vascular resistance (total peripheral resistance, TPR) is the primary determinant of mean arterial blood pressure ($\\text{MAP}$) for a given cardiac output ($\\text{CO}$), governed by the hemodynamic analogue of Ohm's law: $\\Delta P = \\text{CO} \\times \\text{TPR}$, where $\\Delta P = \\text{MAP} - \\text{RAP}$ (mean arterial pressure minus right atrial pressure). Because capillaries are arranged in an immense parallel network that dramatically lowers their net equivalent resistance, terminal arterioles&mdash;possessing thick muscular media capable of active contraction&mdash;serve as the principal &ldquo;stopcocks&rdquo; of the circulatory system, generating over 60% of total vascular resistance and producing the steepest drop in intravascular pressure.</p>\n"
               "<p>For laminar flow of a Newtonian fluid through a cylindrical vessel of length $L$ and internal radius $r$, resistance to flow ($R$) is defined by the Hagen-Poiseuille equation:\n"
               "$$R = \\frac{8\\eta L}{\\pi r^4}$$\n"
               "where $\\eta$ is dynamic blood viscosity. The volumetric flow rate is given by $Q = \\frac{\\Delta P}{R} = \\frac{\\Delta P \\pi r^4}{8\\eta L}$. Because vascular resistance exhibits an inverse fourth-power dependence on lumen radius ($R \\propto 1/r^4$), minute changes in vascular smooth muscle tone exert an outsized impact on local tissue perfusion and systemic blood pressure. A 16% reduction in arteriolar radius doubles hydraulic resistance, while a 50% luminal constriction escalates resistance by sixteen-fold ($2^4 = 16$).</p>\n"
               "<p>To quantify the pharmacological control of arteriolar caliber, vascular physiologists isolated and perfused an intact rat mesenteric microvascular bed with oxygenated Krebs-Henseleit buffer ($\\eta = 1.00 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}$, density $\\rho = 1000\\text{ kg/m}^3$) under a constant driving pressure of $\\Delta P = 80.0\\text{ mmHg}$ ($1.066 \\times 10^4\\text{ Pa}$). Vessels were exposed to baseline buffer, cumulative doses of the $\\alpha_1$-adrenergic agonist phenylephrine (PE, a potent vasoconstrictor), and the endothelium-dependent vasodilator acetylcholine (ACh). Arteriolar lumen diameter ($d = 2r$), volumetric flow rate ($Q$), and calculated hydraulic resistance ($R = \\Delta P / Q$) were recorded, as shown in Table 1.</p>\n"
               "<table class=\"tbl\">\n"
               "  <caption>Table 1 Mesenteric arteriolar diameter, volumetric flow rate, and vascular resistance across vasoactive trials</caption>\n"
               "  <thead>\n"
               "    <tr><th>Perfusion Condition</th><th>Vasoactive Agent</th><th>Vessel Diameter $d$ (&mu;m)</th><th>Vessel Radius $r$ (&mu;m)</th><th>Flow Rate $Q$ (&mu;L/min)</th><th>Vascular Resistance $R$ ($10^{10}$ Pa&middot;s/m$^3$)</th><th>Relative Resistance ($R/R_0$)</th></tr>\n"
               "  </thead>\n"
               "  <tbody>\n"
               "    <tr><td>Baseline Control</td><td>Vehicle buffer</td><td>60.0</td><td>30.0</td><td>120.0</td><td>0.533</td><td>1.00</td></tr>\n"
               "    <tr><td>Mild Vasoconstriction</td><td>$10^{-7}$ M Phenylephrine</td><td>50.4</td><td>25.2</td><td>59.8</td><td>1.070</td><td>2.01</td></tr>\n"
               "    <tr><td>Severe Vasoconstriction</td><td>$10^{-5}$ M Phenylephrine</td><td>30.0</td><td>15.0</td><td>7.50</td><td>8.528</td><td>16.00</td></tr>\n"
               "    <tr><td>Maximum Vasoconstriction</td><td>$10^{-4}$ M Phenylephrine</td><td>20.0</td><td>10.0</td><td>1.48</td><td>43.220</td><td>81.09</td></tr>\n"
               "    <tr><td>Vasodilation</td><td>$10^{-6}$ M Acetylcholine</td><td>75.0</td><td>37.5</td><td>293.0</td><td>0.218</td><td>0.41</td></tr>\n"
               "  </tbody>\n"
               "</table>\n"
               "<p>Investigators noted that in vivo blood flow is further influenced by the non-Newtonian rheological properties of cellular suspensions and the parallel topology of peripheral microbeds.</p>",
    "qs": [
        {
            "q": "Based on Poiseuille's law and Table 1, when phenylephrine reduces the arteriolar radius by exactly 50% (from $30.0\\ \\mu\\text{m}$ to $15.0\\ \\mu\\text{m}$), hydraulic resistance increases by what factor?",
            "ch": [
                "4-fold increase",
                "16-fold increase",
                "2-fold increase",
                "8-fold increase"
            ],
            "a": 1,
            "e": "<strong>Fourth-power radius dependence in Poiseuille resistance:</strong> Vascular resistance according to the Hagen-Poiseuille equation is $R = \\frac{8\\eta L}{\\pi r^4} \\propto \\frac{1}{r^4}$. When arteriolar radius is halved ($r_{new} = 0.50\\,r_0$), the new resistance becomes: $R_{new} = \\frac{8\\eta L}{\\pi (0.50\\,r_0)^4} = \\frac{1}{(0.50)^4} R_0 = \\frac{1}{0.0625} R_0 = 16\\,R_0$. Table 1 confirms this exact scaling: at baseline ($r = 30.0\\ \\mu\\text{m}$), $R = 0.533 \\times 10^{10}\\text{ Pa}\\cdot\\text{s/m}^3$, and under severe vasoconstriction ($r = 15.0\\ \\mu\\text{m}$), $R = 8.528 \\times 10^{10}\\text{ Pa}\\cdot\\text{s/m}^3$, which is precisely $16.00$ times baseline.<br><br><em>Distractor Traps:</em><br>&bull; A (4-fold increase) assumes resistance scales inversely with cross-sectional area ($1/r^2$).<br>&bull; C (2-fold increase) assumes a linear relationship ($1/r$).<br>&bull; D (8-fold increase) assumes a cubic relationship ($1/r^3$).<br>"
        },
        {
            "q": "Why do muscular terminal arterioles generate a significantly larger pressure drop ($\\Delta P$) than the capillary beds, even though individual capillaries possess much smaller lumen diameters?",
            "ch": [
                "Arteriolar blood flow velocity is substantially lower than capillary flow velocity",
                "Arterioles lack an endothelial lining, exposing circulating blood to rough collagen",
                "Capillaries contain circumferential smooth muscle rings that dilate spontaneously",
                "Vast parallel branching of capillaries yields a much lower net vascular resistance"
            ],
            "a": 3,
            "e": "<strong>Parallel vascular resistance in capillary beds:</strong> The equivalent resistance of $N$ identical parallel conduits is $R_{eq} = \\frac{R_{individual}}{N}$. Although an individual capillary has a very high individual resistance due to its narrow $8\\ \\mu\\text{m}$ caliber, there are billions ($N \\approx 10^{10}$) of capillaries arranged in parallel. This immense parallel branching drops the equivalent resistance of the entire capillary bed to a relatively low level. In contrast, there are far fewer arterioles in parallel (~$5 \\times 10^7$), so the collective resistance of the arteriolar segment remains the highest in the systemic circulation, driving the steepest pressure drop ($\\Delta P = Q \\cdot R$).<br><br><em>Distractor Traps:</em><br>&bull; A contradicts fluid continuity; blood velocity is much higher in arterioles than in capillaries.<br>&bull; B is anatomically false; all blood vessels possess an inner monolayer of vascular endothelium.<br>&bull; C is anatomically false; capillaries completely lack smooth muscle cells and cannot active dilate or constrict."
        },
        {
            "q": "If an arteriolar vessel undergoes vasodilation such that its radius increases by 20% (to $1.20\\,r_0$) while the driving pressure gradient ($\\Delta P$) remains constant, by what factor does volumetric flow rate increase?",
            "ch": [
                "2.07-fold",
                "1.20-fold",
                "1.44-fold",
                "4.00-fold"
            ],
            "a": 0,
            "e": "<strong>Flow rate scaling with arteriolar vasodilation:</strong> From Poiseuille's law, volumetric flow rate at constant pressure drop and viscosity is directly proportional to the fourth power of the radius: $Q \\propto r^4$. When radius increases by 20% ($r_{new} = 1.20\\,r_0$), the new volumetric flow rate is $Q_{new} = (1.20)^4 Q_0 = 1.20 \\times 1.20 \\times 1.20 \\times 1.20 \\times Q_0 = 1.44 \\times 1.44 \\times Q_0 = 2.0736\\,Q_0 \\approx 2.07\\,Q_0$. Thus, a modest 20% dilation more than doubles tissue blood perfusion.<br><br><em>Distractor Traps:</em><br>&bull; B (1.20-fold) assumes a linear relationship ($Q \\propto r$).<br>&bull; C (1.44-fold) assumes an area relationship ($Q \\propto r^2 = 1.20^2$).<br>&bull; D (4.00-fold) overestimates the expansion or computes $2^2$."
        },
        {
            "q": "The derivation of the Hagen-Poiseuille equation ($Q = \\Delta P \\pi r^4 / (8\\eta L)$) relies fundamentally on which set of physical assumptions?",
            "ch": [
                "Compressible gas flow, turbulent velocity fluctuations, and flexible elastic conduits",
                "Incompressible Newtonian fluid, steady laminar streamlines, and rigid cylindrical conduits",
                "Non-Newtonian shear-thinning fluid, slip boundary conditions, and parabolic conical walls",
                "Zero-viscosity ideal superfluid, turbulent eddy dissipation, and tortuous capillary bends"
            ],
            "a": 1,
            "e": "<strong>Physical assumptions underlying Poiseuille's law:</strong> The classical Hagen-Poiseuille law is derived by integrating the Navier-Stokes equations under specific boundary conditions: (1) the fluid is Newtonian (viscosity $\\eta$ is constant and independent of shear rate), (2) the fluid is incompressible (density $\\rho$ is constant), (3) the flow is steady, fully developed, and laminar (no turbulent eddies or time-dependent fluctuations), (4) the conduit is a straight, rigid, uniform circular cylinder, and (5) the fluid obeys the no-slip condition at the wall ($v(R) = 0$).<br><br><em>Distractor Traps:</em><br>&bull; A erroneously includes compressible gas and turbulent flow, both of which violate Poiseuille assumptions.<br>&bull; C cites non-Newtonian rheology and slip boundary conditions, which require complex non-linear constitutive models.<br>&bull; D invokes zero-viscosity superfluids and turbulence, which directly contradict viscous laminar pipe flow."
        },
        {
            "q": "A clinical patient develops secondary polycythemia, elevating their hematocrit from 42% to 63% and doubling blood dynamic viscosity ($\\eta$). If mean arterial pressure remains constant, what compensatory alteration in arteriolar radius ($r$) would be required to maintain normal baseline cardiac output?",
            "ch": [
                "Arteriolar radius must decrease by roughly 50% through sympathetic vasoconstriction",
                "Arteriolar radius must double in caliber to overcome the heightened viscous friction",
                "Arteriolar radius must decrease by roughly 19% through active smooth muscle spasm",
                "Arteriolar radius must increase by roughly 19% through active smooth muscle relaxation"
            ],
            "a": 3,
            "e": "<strong>Compensatory vasodilation for hyperviscosity:</strong> Volumetric flow rate is $Q = \\frac{\\Delta P \\pi r^4}{8\\eta L}$. For cardiac output ($Q$) and perfusion pressure ($\\Delta P$) to remain constant when dynamic viscosity doubles ($\\eta_{new} = 2\\eta_0$), the ratio $\\frac{r^4}{\\eta}$ must be conserved: $\\frac{r_{new}^4}{2\\eta_0} = \\frac{r_0^4}{\\eta_0} \\implies r_{new}^4 = 2\\,r_0^4 \\implies r_{new} = 2^{1/4} r_0$. Calculating the fourth root of 2: $2^{0.25} \\approx 1.189 \\approx 1.19$. Therefore, arterioles must dilate by approximately 19% ($r_{new} = 1.19\\,r_0$) to compensate for the doubled viscosity and prevent hypoperfusion.<br><br><em>Distractor Traps:</em><br>&bull; A suggests vasoconstriction, which would compound the resistance increase ($R \\propto \\eta / r^4$) and cause catastrophic hypoperfusion.<br>&bull; B assumes radius must scale linearly with viscosity, which would increase flow 8-fold ($2^4 / 2 = 8$).<br>&bull; C asserts radius must decrease by 19%, inverting the required physiological response."
        },
        {
            "q": "During strenuous exercise, intense skeletal muscle vasodilation occurs as thousands of capillary beds open in parallel. How does this physiological recruitment affect total peripheral resistance (TPR) and cardiac workload?",
            "ch": [
                "TPR increases because additional vessel conduits add series resistance to systemic flow",
                "TPR remains unchanged because systemic vasoconstriction exactly cancels microbed shifts",
                "TPR decreases because parallel vascular channels lower net equivalent vascular resistance",
                "TPR decreases because circulating blood density drops rapidly during muscular excretion"
            ],
            "a": 2,
            "e": "<strong>Parallel vascular resistance during exercise:</strong> When vascular beds are arranged in parallel, the equivalent total resistance satisfies $\\frac{1}{R_{total}} = \\frac{1}{R_1} + \\frac{1}{R_2} + \\dots + \\frac{1}{R_n}$. When metabolic vasodilation recruits and dilates thousands of parallel capillary pathways within active skeletal muscle, new conductive pathways are added. This significantly reduces total peripheral resistance (TPR). Because $\\text{MAP} - \\text{RAP} = \\text{CO} \\times \\text{TPR}$, this reduction in afterload enables the heart to increase cardiac output 4- to 5-fold with only a moderate increase in mean arterial pressure.<br><br><em>Distractor Traps:</em><br>&bull; A treats the recruited beds as series resistances; series additions increase resistance, whereas parallel additions decrease resistance.<br>&bull; B is incorrect because local skeletal muscle metabolic dilation far outweighs splanchnic and renal vasoconstriction during heavy exertion, resulting in a net decrease in TPR.<br>&bull; D is physically false; blood density does not drop during exercise (sweating can actually cause mild hemoconcentration)."
        }
    ]
}
