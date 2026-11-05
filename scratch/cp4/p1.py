# /home/cgslinde/DrillRoom/DrillRoom/scratch/cp4/p1.py
"""
Passage 1: Topic 251 — Young-Laplace Law & Alveolar Surface Tension
"""

passage_data = {
    "id": "exam_cp90_4_p1",
    "sec": "C/P",
    "topic": "Young-Laplace Law & Alveolar Surface Tension in Neonatal Respiratory Distress",
    "sheet": 1,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_4",
    "passage": "<div class=\"ttl\">Passage 1 (Questions 1&ndash;6)</div>\n"
               "<p>Neonatal respiratory distress syndrome (NRDS) is a life-threatening disorder prevalent in premature infants born prior to 32 weeks of gestation, arising from insufficient synthesis of pulmonary surfactant by alveolar type II pneumocytes. Pulmonary surfactant is a complex mixture of phospholipids&mdash;primarily dipalmitoylphosphatidylcholine (DPPC)&mdash;and hydrophobic surfactant proteins (SP-B and SP-C). Surfactant adsorbs at the air-liquid interface lining the alveoli, where it significantly lowers surface tension ($\\gamma$).</p>\n"
               "<p>The mechanical stability of spherical alveoli is governed by the Young-Laplace law for a single spherical fluid interface: $\\Delta P = \\frac{2\\gamma}{r}$, where $\\Delta P$ represents the transmural collapsing pressure (the pressure difference between the interior air space and the surrounding interstitial fluid) and $r$ denotes the alveolar radius. In an untreated lung lacking surfactant, surface tension remains constant ($\\gamma \\approx 70.0\\text{ mN/m}$, approximating pure water) regardless of lung inflation volume. Under these conditions, smaller interconnected alveoli generate substantially higher collapsing pressures than larger alveoli, driving gas down the pressure gradient into the larger units and causing widespread microatelectasis.</p>\n"
               "<p>To evaluate synthetic lipid emulsions against a natural porcine surfactant extract (poractant alfa), researchers utilize a pulsating bubble surfactometer (PBS). A liquid surfactant suspension is placed in an enclosed chamber maintained at $37^\\circ\\text{C}$, and an air bubble is formed at the tip of a capillary tube. The bubble is cyclically oscillated between a maximum radius ($r_{max} = 0.55\\text{ mm}$) and a minimum radius ($r_{min} = 0.40\\text{ mm}$) at 20 cycles per minute to mimic neonatal tidal ventilation. Pressure sensors record dynamic transmural pressure, from which minimum surface tension ($\\gamma_{min}$ at $r_{min}$), maximum surface tension ($\\gamma_{max}$ at $r_{max}$), and dynamic compliance are determined. Results across four surfactant formulations are detailed in Table 1.</p>\n"
               "<table class=\"tbl\">\n"
               "  <caption>Table 1 Dynamic surface tension and collapsing pressures measured across surfactant formulations</caption>\n"
               "  <thead>\n"
               "    <tr><th>Formulation</th><th>Composition</th><th>$\\gamma_{min}$ at $r_{min}$ (mN/m)</th><th>$\\gamma_{max}$ at $r_{max}$ (mN/m)</th><th>Collapsing $\\Delta P$ at $r_{min}$ (Pa)</th><th>Dynamic Compliance (mL/cm H$_2$O)</th></tr>\n"
               "  </thead>\n"
               "  <tbody>\n"
               "    <tr><td>Saline Control</td><td>0.9% NaCl (Aqueous)</td><td>70.0</td><td>71.5</td><td>350</td><td>0.12</td></tr>\n"
               "    <tr><td>Formulation A</td><td>Synthetic DPPC alone</td><td>22.0</td><td>52.0</td><td>110</td><td>0.38</td></tr>\n"
               "    <tr><td>Formulation B</td><td>DPPC + 2% Recombinant SP-B/C</td><td>4.0</td><td>32.0</td><td>20</td><td>0.85</td></tr>\n"
               "    <tr><td>Poractant Alfa</td><td>Purified porcine lung extract</td><td>2.0</td><td>28.0</td><td>10</td><td>0.94</td></tr>\n"
               "  </tbody>\n"
               "</table>\n"
               "<p>Following tensiometric profiling, investigators examine whether adding recombinant SP-B peptide fragments preserves low surface tension during rapid compression-expansion cycling.</p>",
    "qs": [
        {
            "q": "In an infant suffering from untreated NRDS lacking surfactant ($\\gamma = 70.0\\text{ mN/m}$), what is the collapsing pressure $\\Delta P$ within an individual terminal alveolus having an effective radius of $50.0\\ \\mu\\text{m}$?",
            "ch": [
                "2.80 kPa",
                "1.40 kPa",
                "5.60 kPa",
                "0.70 kPa"
            ],
            "a": 0,
            "e": "<strong>Young-Laplace law calculation for collapsing pressure:</strong> The Young-Laplace law for a spherical fluid-air interface dictates that $\\Delta P = \\frac{2\\gamma}{r}$. Converting parameters into SI units: surface tension $\\gamma = 70.0\\text{ mN/m} = 0.0700\\text{ N/m}$, and radius $r = 50.0\\ \\mu\\text{m} = 5.00 \\times 10^{-5}\\text{ m}$. Substituting these values yields $\\Delta P = \\frac{2(0.0700\\text{ N/m})}{5.00 \\times 10^{-5}\\text{ m}} = \\frac{0.140}{5.00 \\times 10^{-5}} = 2800\\text{ Pa} = 2.80\\text{ kPa}$. In the absence of surfactant, this high collapsing pressure must be overcome during each inspiration, leading to severe respiratory fatigue.<br><br><em>Distractor Traps:</em><br>&bull; B (1.40 kPa) omits the factor of 2 in the numerator, calculating $\\Delta P = \\gamma / r$.<br>&bull; C (5.60 kPa) doubles the correct factor of 2, calculating $4\\gamma / r$ (which applies to a thin spherical film with two interfaces, like a free soap bubble in air, rather than an alveolus with a single liquid-air interface).<br>&bull; D (0.70 kPa) erroneously divides by 4 or squares the radius."
        },
        {
            "q": "If two surfactant-deficient alveoli of radii $r_1 = 40\\ \\mu\\text{m}$ and $r_2 = 80\\ \\mu\\text{m}$ are connected to the same alveolar duct with constant surface tension $\\gamma$, what physical phenomenon occurs?",
            "ch": [
                "Air flows into smaller alveoli because smaller radius generates lower inward pressure",
                "Air flows into larger alveoli because smaller radius generates higher inward pressure",
                "Gas diffusion ceases entirely because equilibrium surface tension stabilizes both units",
                "Transmural pressure equalizes spontaneously without any net gas redistribution between them"
            ],
            "a": 1,
            "e": "<strong>Alveolar instability and Laplace pressure gradient:</strong> According to the Young-Laplace law ($\\Delta P = 2\\gamma / r$), collapsing pressure is inversely proportional to radius when surface tension $\\gamma$ is constant. Consequently, the smaller alveolus ($r_1 = 40\\ \\mu\\text{m}$) generates twice the internal collapsing pressure of the larger alveolus ($r_2 = 80\\ \\mu\\text{m}$): $\\Delta P_1 = 2\\Delta P_2$. Air naturally moves down this pressure gradient from the region of higher pressure (the smaller alveolus) into the region of lower pressure (the larger alveolus). This causes the smaller alveolus to collapse completely (atelectasis) while overinflating the larger alveolus. Surfactant prevents this by lowering $\\gamma$ more in smaller alveoli.<br><br><em>Distractor Traps:</em><br>&bull; A reverses the direction of the pressure gradient, falsely asserting that smaller radius yields lower pressure.<br>&bull; C suggests static equilibrium, which violates the existence of a nonzero pressure gradient between interconnected units.<br>&bull; D incorrectly claims spontaneous pressure equalization occurs without fluid or gas movement."
        },
        {
            "q": "Dipalmitoylphosphatidylcholine (DPPC) reduces alveolar surface tension primarily through which biophysical mechanism at the air-water interface?",
            "ch": [
                "Covalently binding directly to dissolved oxygen molecules within fluid",
                "Catalyzing enzymatic hydrolysis of interstitial water dipole bonds",
                "Disrupting cohesive hydrogen bonding networks between water dipoles",
                "Increasing electrostatic repulsion among ionized carbonic acid ions"
            ],
            "a": 2,
            "e": "<strong>Amphipathic surfactant monolayer dynamics:</strong> Surface tension arises from cohesive intermolecular forces—primarily hydrogen bonding—among liquid water molecules, which pull surface molecules toward the interior of the liquid. DPPC is an amphipathic phospholipid possessing a hydrophilic zwitterionic phosphocholine headgroup and two hydrophobic saturated palmitic acid acyl chains. When DPPC adsorbs at the air-liquid interface, its hydrophobic tails orient toward the alveolar airspace while its hydrophilic headgroups interact with surface water. By interposing between adjacent water molecules, DPPC disrupts intermolecular hydrogen bonding, dramatically lowering the cohesive inward pull and reducing surface tension.<br><br><em>Distractor Traps:</em><br>&bull; A misattributes surfactant function to covalent chemical bonding with respiratory gas molecules.<br>&bull; B erroneously describes surfactant as an enzyme that catalyzes covalent hydrolysis of water bonds.<br>&bull; D refers to carbonic acid ionization, which alters acid-base balance rather than interfacial surface tension."
        },
        {
            "q": "Why does the dynamic surface tension of natural surfactant decrease to its lowest value ($\\gamma_{min}$) at minimum bubble radius ($r_{min}$) during expiration?",
            "ch": [
                "Thermal convection currents selectively desorb hydrophobic surfactant lipids",
                "Accelerated DPPC catabolism reduces lipid monolayer molecular packing density",
                "Phospholipid headgroups become fully protonated by rising basic fluid pH",
                "Surface area compression forces surfactant molecules into tight lateral packing"
            ],
            "a": 3,
            "e": "<strong>Dynamic compression of surfactant monolayer:</strong> As alveolar volume decreases during exhalation, the interfacial surface area contracts. Because the saturated acyl chains of DPPC are linear and pack tightly without steric hindrance from cis double bonds, area compression forces the phospholipid molecules into a highly condensed, solid-like monolayer. This tight lateral packing maximizes intermolecular repulsive forces that oppose liquid water cohesion, driving surface tension down to near-zero values ($< 2-5\\text{ mN/m}$). When the alveolus re-expands during inhalation, surface area increases, packing density decreases, and surface tension rises.<br><br><em>Distractor Traps:</em><br>&bull; A suggests desorption of lipids during compression, which would deplete the surface film and increase surface tension.<br>&bull; B posits lipid breakdown; catabolism would reduce surfactant abundance and elevate surface tension.<br>&bull; C is chemically inaccurate because alveolar fluid pH is physiological (~7.4) and does not undergo drastic basic shifts to alter headgroup ionization."
        },
        {
            "q": "Based on Table 1, administering Poractant Alfa rather than Formulation A benefits premature neonates by producing which physiological alteration?",
            "ch": [
                "Increasing lung compliance, thereby decreasing the muscular work of inspiration",
                "Decreasing lung compliance, thereby increasing thoracic elastic recoil velocity",
                "Elevating alveolar collapsing pressure, thereby preventing microvascular edema",
                "Restricting functional residual capacity, thereby enhancing expiratory velocity"
            ],
            "a": 0,
            "e": "<strong>Surfactant effect on pulmonary compliance and work of breathing:</strong> Pulmonary compliance is defined as the change in volume per unit change in distending pressure ($C = \\Delta V / \\Delta P$). Table 1 demonstrates that Poractant Alfa achieves a dynamic compliance of $0.94\\text{ mL/cm H}_2\\text{O}$, compared to only $0.38\\text{ mL/cm H}_2\\text{O}$ for Formulation A, alongside a 10-fold reduction in collapsing pressure (from $110\\text{ Pa}$ to $10\\text{ Pa}$). Higher compliance means the lungs expand much more readily at lower transpulmonary pressures, dramatically reducing the inspiratory muscular effort ($W = \\int P\\,dV$) required of the neonate to inflate the alveoli.<br><br><em>Distractor Traps:</em><br>&bull; B falsely claims Poractant Alfa decreases lung compliance; Table 1 explicitly shows compliance rises from 0.38 to 0.94.<br>&bull; C asserts collapsing pressure increases; Table 1 shows $\\Delta P$ falls from 110 Pa to 10 Pa.<br>&bull; D is incorrect because surfactant increases functional residual capacity by preventing alveolar collapse, rather than restricting it."
        },
        {
            "q": "In clinical obstetrics, fetal lung maturity is commonly assessed by measuring the lecithin-to-sphingomyelin (L/S) ratio in amniotic fluid. A ratio greater than 2.0 indicates mature surfactant production. Which statement best explains this diagnostic parameter?",
            "ch": [
                "Sphingomyelin is the primary surface-tension-reducing agent, rising rapidly after week 35",
                "Lecithin synthesis surges late in gestation, while sphingomyelin remains relatively constant",
                "Lecithin degrades spherical alveoli, while sphingomyelin stimulates alveolar septation growth",
                "Both lipids decline precipitously near term to permit rapid expansion of alveolar airspaces"
            ],
            "a": 1,
            "e": "<strong>Lecithin-to-sphingomyelin ratio physiology:</strong> Lecithin (specifically dipalmitoylphosphatidylcholine, DPPC) is the major functional component of pulmonary surfactant responsible for lowering alveolar surface tension. Throughout gestation, amniotic fluid sphingomyelin concentrations remain relatively constant or decline slightly. In contrast, lecithin production by type II pneumocytes increases sharply around 32&ndash;35 weeks of gestation. An L/S ratio $\\ge 2.0$ reflects adequate lecithin production to prevent neonatal respiratory distress syndrome upon delivery.<br><br><em>Distractor Traps:</em><br>&bull; A misattributes surfactant activity to sphingomyelin rather than lecithin (DPPC).<br>&bull; C nonsensically claims lecithin degrades alveoli, when it is the vital protective surfactant component.<br>&bull; D falsely claims both lipids decline, which would cause rather than prevent respiratory distress."
        }
    ]
}
