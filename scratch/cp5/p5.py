# /home/cgslinde/DrillRoom/DrillRoom/scratch/cp5/p5.py
"""
Passage 5: Topic 272 — Tracheobronchial Airway Branching & Fractal Flow Resistance
"""

passage_data = {
    "id": "exam_cp90_5_p5",
    "sec": "C/P",
    "topic": "Tracheobronchial Airway Branching & Fractal Flow Resistance",
    "sheet": 5,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_5",
    "passage": "<div class=\"ttl\">Passage 5 (Questions 25&ndash;30)</div>\n"
               "<p>The human tracheobronchial tree features an asymmetrical dichotomous branching architecture comprising approximately 23 generations ($z=0$ to $z=23$) descending from the trachea to microscopic alveolar sacs. According to the Weibel symmetric morphometric lung model:</p>\n"
               "<p>1. <em>Conducting Zone (Generations 0&ndash;16)</em>: Encompassing the trachea ($z=0$), mainstem and lobar bronchi, and terminal bronchioles ($z=16$). These conduits facilitate bulk convective gas transport and constitute the anatomical dead space (~150 mL).</p>\n"
               "<p>2. <em>Respiratory Zone (Generations 17&ndash;23)</em>: Encompassing respiratory bronchioles, alveolar ducts, and alveolar sacs, where alveolar-capillary gas exchange takes place.</p>\n"
               "<p>Gas transport through this fractal airway network exhibits a fundamental fluid dynamic paradox. By the principle of continuity for incompressible fluid flow:</p>\n"
               "<p>$$Q = A_{\\text{total}} \\cdot v_{\\text{mean}}$$</p>\n"
               "<p>where $Q$ is volumetric flow rate (typically $500\\text{ cm}^3/\\text{s}$ or $0.50\\text{ L/s}$ during quiet inspiration), $A_{\\text{total}} = N_z \\cdot \\frac{\\pi d_z^2}{4}$ is the aggregate cross-sectional area across all $N_z = 2^z$ parallel branches in generation $z$, and $v_{\\text{mean}}$ is the mean linear gas velocity.</p>\n"
               "<p>Although individual branch diameter ($d_z$) diminishes progressively, the geometric doubling of parallel conduits ($N_z = 2^z$) causes the total aggregate cross-sectional area to expand exponentially from $2.5\\text{ cm}^2$ in the trachea to over $10{,}000\\text{ cm}^2$ in terminal airspaces. According to the equivalent resistance formula for parallel conduits:</p>\n"
               "<p>$$\\frac{1}{R_{\\text{total}}} = \\sum_{i=1}^{N_z} \\frac{1}{R_i}$$</p>\n"
               "<p>Because millions of narrow bronchioles operate in parallel, peripheral airways contribute less than 20% of total pulmonary resistance. The maximum airflow resistance in a healthy lung resides in generations 3 to 5 (medium-sized segmental bronchi). Morphometric and hemodynamic parameters across seven generations are shown in Table 1.</p>\n"
               "<table class=\"tbl\">\n"
               "  <caption>Table 1 Airway branching generations, aggregate area, gas velocity, and segmental resistance</caption>\n"
               "  <thead>\n"
               "    <tr><th>Airway Generation ($z$)</th><th>Structure Type</th><th>Branch Count ($N_z$)</th><th>Single Caliber $d_z$ (mm)</th><th>Aggregate Area $A_{\\text{total}}$ ($\\text{cm}^2$)</th><th>Mean Velocity $v$ (cm/s)</th><th>Segmental Resistance ($\\text{cm H}_2\\text{O}/(\\text{L/s})$)</th></tr>\n"
               "  </thead>\n"
               "  <tbody>\n"
               "    <tr><td>Gen 0</td><td>Trachea</td><td>1</td><td>18.0</td><td>2.5</td><td>200.0</td><td>0.20</td></tr>\n"
               "    <tr><td>Gen 2</td><td>Lobar Bronchi</td><td>4</td><td>8.3</td><td>2.2</td><td>227.3</td><td>0.35</td></tr>\n"
               "    <tr><td>Gen 4</td><td>Segmental Bronchi</td><td>16</td><td>4.5</td><td>2.5</td><td>200.0</td><td>0.65</td></tr>\n"
               "    <tr><td>Gen 8</td><td>Small Bronchi</td><td>256</td><td>1.4</td><td>3.9</td><td>128.2</td><td>0.30</td></tr>\n"
               "    <tr><td>Gen 12</td><td>Terminal Bronchioles</td><td>4096</td><td>0.6</td><td>11.6</td><td>43.1</td><td>0.12</td></tr>\n"
               "    <tr><td>Gen 16</td><td>Transitional Bronchioles</td><td>65,536</td><td>0.4</td><td>82.3</td><td>6.1</td><td>0.04</td></tr>\n"
               "    <tr><td>Gen 20</td><td>Alveolar Ducts</td><td>1,048,576</td><td>0.3</td><td>741.0</td><td>0.67</td><td>0.01</td></tr>\n"
               "  </tbody>\n"
               "</table>\n"
               "<p>Researchers evaluate whether bronchodilators selectively reduce airway resistance in segmental versus peripheral generations.</p>",
    "qs": [
        {
            "q": "Using the continuity equation and Table 1, what is the mean linear gas velocity ($v$) through the trachea ($z=0$, $A = 2.5\\text{ cm}^2$) during deep inspiration when inspiratory flow increases to $Q = 2.0\\text{ L/s} = 2000\\text{ cm}^3/\\text{s}$?",
            "ch": [
                "400 cm/s (4.0 m/s)",
                "800 cm/s (8.0 m/s)",
                "1200 cm/s (12 m/s)",
                "1600 cm/s (16 m/s)"
            ],
            "a": 1,
            "e": "<strong>Continuity equation and linear gas velocity calculation:</strong> The continuity equation for fluid flow states that volumetric flow rate equals cross-sectional area multiplied by mean velocity: $Q = A \\cdot v$. Rearranging for linear velocity gives $v = \\frac{Q}{A}$. Given $Q = 2000\\text{ cm}^3/\\text{s}$ and tracheal cross-sectional area $A = 2.5\\text{ cm}^2$: $v = \\frac{2000\\text{ cm}^3/\\text{s}}{2.5\\text{ cm}^2} = 800\\text{ cm/s} = 8.0\\text{ m/s}$. During vigorous inhalation, high linear velocities in the trachea promote turbulent airflow and generate breath sounds audible on physical examination.<br><br><em>Distractor Traps:</em><br>&bull; A (400 cm/s) assumes a cross-sectional area of 5.0 $\\text{cm}^2$ or divides by an extra factor of 2.<br>&bull; C (1200 cm/s) makes an arithmetic multiplication error, calculating $Q \\times 1.5 / A$.<br>&bull; D (1600 cm/s) erroneously doubles the correct velocity or calculates $2000 / 1.25$."
        },
        {
            "q": "Despite individual bronchiolar calibers narrowing to fractions of a millimeter, why does segmental resistance drop from $0.65\\text{ cm H}_2\\text{O}/(\\text{L/s})$ in Generation 4 to $0.04\\text{ cm H}_2\\text{O}/(\\text{L/s})$ in Generation 16?",
            "ch": [
                "Alveolar surfactant lines conducting airways, abolishing wall boundary drag",
                "The gas transition from turbulent flow to supersonic inviscid flow speeds",
                "Exponential branching in parallel drastically lowers net equivalent resistance",
                "Smooth muscle tone dilates peripheral conduits during active inspiration"
            ],
            "a": 2,
            "e": "<strong>Parallel airway arrangement and the resistance paradox:</strong> According to the Hagen-Poiseuille law, the resistance of an individual narrow bronchiole is high because $R_i \\propto 1/r^4$. However, branching generates an exponential number of parallel pathways ($N_z = 2^z$). In Generation 16, there are 65,536 parallel transitional bronchioles. In parallel circuit mechanics, equivalent resistance is given by $\\frac{1}{R_{\\text{total}}} = \\sum \\frac{1}{R_i} = \\frac{N_z}{R_i} \\implies R_{\\text{total}} = \\frac{R_i}{N_z}$. Dividing individual resistance by 65,536 causes the aggregate resistance of the peripheral airways to drop to negligible levels.<br><br><em>Distractor Traps:</em><br>&bull; A claims surfactant lines conducting airways; surfactant is localized to alveoli and terminal respiratory units, not conducting bronchioles.<br>&bull; B invokes supersonic flow speeds, which are physically impossible in biological respiratory systems.<br>&bull; D claims peripheral airways dilate via active muscle tone, which does not explain the anatomical and physical basis of parallel branching resistance."
        },
        {
            "q": "In the trachea (Gen 0: $d = 18\\text{ mm} = 0.018\\text{ m}$, $v = 2.0\\text{ m/s}$), air has density $\\rho = 1.2\\text{ kg/m}^3$ and dynamic viscosity $\\mu = 1.8 \\times 10^{-5}\\text{ Pa}\\cdot\\text{s}$. What is the tracheal Reynolds number ($Re$), and how does it compare to flow in Gen 16?",
            "ch": [
                "Re = 240; both the trachea and Gen 16 exhibit deeply laminar Stokes streamlines",
                "Re = 1200; the trachea has laminar flow while Gen 16 exhibits severe turbulence",
                "Re = 1800; both the trachea and Gen 16 exhibit chaotic turbulent vortexes",
                "Re = 2400; the trachea exhibits turbulent flow while Gen 16 is purely laminar"
            ],
            "a": 3,
            "e": "<strong>Reynolds number across airway generations:</strong> The Reynolds number is calculated as $Re = \\frac{\\rho v d}{\\mu}$. For the trachea: $Re = \\frac{(1.2\\text{ kg/m}^3)(2.0\\text{ m/s})(0.018\\text{ m})}{1.8 \\times 10^{-5}\\text{ Pa}\\cdot\\text{s}} = \\frac{0.0432}{1.8 \\times 10^{-5}} = 2400$. Because $Re = 2400 > 2000$, tracheal flow is post-critical and transitional to turbulent. In contrast, in Generation 16, air velocity drops to $v = 0.061\\text{ m/s}$ and caliber drops to $d = 0.0004\\text{ m}$, yielding $Re = \\frac{1.2 \\times 0.061 \\times 0.0004}{1.8 \\times 10^{-5}} \\approx 1.63$. With $Re \\approx 1.6 \\ll 2000$, peripheral airway flow is deeply laminar.<br><br><em>Distractor Traps:</em><br>&bull; A miscalculates $Re$ as 240 and claims both zones are laminar.<br>&bull; B miscalculates $Re$ as 1200 and falsely claims peripheral airways are turbulent.<br>&bull; C calculates $Re = 1800$ and incorrectly asserts both zones are turbulent."
        },
        {
            "q": "Heliox (a mixture of 80% helium and 20% oxygen) is clinically administered to patients suffering from acute upper airway obstruction. What physical property of helium reduces the resistive pressure drop in large airways?",
            "ch": [
                "Markedly lower gas density, which decreases inertial and turbulent resistance",
                "Significantly higher dynamic viscosity, which accelerates laminar convection",
                "Greater molar heat capacity, which suppresses airway mucosal inflammation",
                "Enhanced van der Waals attractions, which prevent terminal bronchiolar spasm"
            ],
            "a": 0,
            "e": "<strong>Heliox physics and density-dependent turbulent pressure drop:</strong> In large conducting airways like the trachea and mainstem bronchi, airflow is turbulent, particularly in the setting of severe obstruction. Under turbulent flow, the pressure drop across the airway is governed by kinetic fluid energy and scales with fluid density: $\\Delta P \\propto \\rho v^2$. Helium has an atomic mass of $4\\text{ g/mol}$, compared to nitrogen ($28\\text{ g/mol}$), making Heliox approximately one-third as dense as ambient air. By lowering gas density $\\rho$, Heliox substantially reduces turbulent pressure losses and drops the Reynolds number ($Re \\propto \\rho$), restoring smoother flow and decreasing the work of breathing.<br><br><em>Distractor Traps:</em><br>&bull; B claims higher viscosity improves flow; helium has slightly higher viscosity than air, but viscosity affects laminar Poiseuille flow, not turbulent density-driven drag.<br>&bull; C attributes therapeutic benefit to thermal heat capacity, which has no hemodynamic or pneumatic effect on flow resistance.<br>&bull; D refers to intermolecular van der Waals forces, which are actually exceptionally weak in helium."
        },
        {
            "q": "According to Murray's law of physiological branching, the parent vessel radius $r_0$ relates to daughter vessel radii ($r_1, r_2$) by $r_0^3 = r_1^3 + r_2^3$. What evolutionary optimization does this cubic relationship achieve in fluid transport systems?",
            "ch": [
                "It maximizes convective kinetic velocity across all terminal airway junctions",
                "It ensures equal static pressure regardless of dynamic velocity transitions",
                "It minimizes the total energy cost of fluid flow and conduit tissue maintenance",
                "It eliminates hydrostatic pressure differences caused by gravity in erect lungs"
            ],
            "a": 2,
            "e": "<strong>Murray's law and biological work minimization:</strong> Murray's law is a mathematical principle describing optimal branching in vascular and respiratory transport networks. It balances two competing physiological costs: (1) the viscous work required to overcome hydraulic friction and pump fluid through conduits (which decreases as conduit radius increases: $W_{\\text{flow}} \\propto 1/r^4$), and (2) the metabolic energy required to synthesize, maintain, and house the volume of blood/tissue within the conduit (which increases with vessel volume: $W_{\\text{volume}} \\propto r^2$). Minimizing the sum of these two opposing energy functions with respect to radius yields the cubic branching rule $r_0^3 = r_1^3 + r_2^3$.<br><br><em>Distractor Traps:</em><br>&bull; A claims branching maximizes convective kinetic velocity; branching actually dramatically decreases velocity to facilitate diffusion.<br>&bull; B asserts static pressure remains identical across branches, which violates the existence of driving pressure gradients.<br>&bull; D claims Murray's law eliminates gravitational hydrostatic heads, which is physically impossible."
        },
        {
            "q": "In generations 17 to 23 of the respiratory zone, mean linear gas velocity drops to $< 0.1\\text{ cm/s}$. What physical mechanism dominates oxygen and carbon dioxide transport across these terminal gas exchange units?",
            "ch": [
                "Acoustic streaming driven by phonation frequencies along the vocal ligaments",
                "High-velocity convective jet mixing induced by pulsatile heart contractions",
                "Electroosmotic bulk fluid convection across wet alveolar epithelial membranes",
                "Molecular diffusion driven by chemical concentration gradients (Fick's law)"
            ],
            "a": 3,
            "e": "<strong>Convective-to-diffusive mass transport transition in terminal airways:</strong> In the upper conducting airways, bulk convective flow propelled by transpulmonary pressure gradients moves gas rapidly. However, because aggregate cross-sectional area increases dramatically to over $10{,}000\\text{ cm}^2$ in the alveolar zone, linear convective gas velocity drops to negligible levels ($< 1\\text{ mm/s}$). At these minimal velocities, bulk convective transport effectively halts. Over the microscopic distances ($< 1\\text{ mm}$) of the terminal alveolar ducts and sacs, thermal molecular diffusion—governed by Fick's first law of diffusion ($J = -D \\frac{dc}{dx}$)—is orders of magnitude faster than bulk flow, dominating gas mixing and alveolar-capillary exchange.<br><br><em>Distractor Traps:</em><br>&bull; A refers to phonation acoustic streaming, which plays no functional role in alveolar alveolar-capillary gas exchange.<br>&bull; B describes cardiogenic convective jet mixing; while heartbeats cause minor localized oscillations, they do not replace molecular diffusion.<br>&bull; C describes electroosmotic bulk convection, which applies to fluid motion past charged solid interfaces under external electric fields."
        }
    ]
}
