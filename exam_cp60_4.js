/* ---- exam_cp60_4.js ---- */
/* 60-minute C/P Practice Exam 4: 5 passages + 3 discrete (33 Qs) */

const EXAM_CP60_4 = [
  {
    "id": "exam_cp60_4_p1",
    "sec": "C/P",
    "topic": "Young-Laplace Law & Alveolar Surface Tension in Neonatal Respiratory Distress",
    "sheet": 1,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_4",
    "passage": "<div class=\"ttl\">Passage 1 (Questions 1&ndash;6)</div>\n<p>Neonatal respiratory distress syndrome (NRDS) is a life-threatening disorder prevalent in premature infants born prior to 32 weeks of gestation, arising from insufficient synthesis of pulmonary surfactant by alveolar type II pneumocytes. Pulmonary surfactant is a complex mixture of phospholipids&mdash;primarily dipalmitoylphosphatidylcholine (DPPC)&mdash;and hydrophobic surfactant proteins (SP-B and SP-C). Surfactant adsorbs at the air-liquid interface lining the alveoli, where it significantly lowers surface tension ($\\gamma$).</p>\n<p>The mechanical stability of spherical alveoli is governed by the Young-Laplace law for a single spherical fluid interface: $\\Delta P = \\frac{2\\gamma}{r}$, where $\\Delta P$ represents the transmural collapsing pressure (the pressure difference between the interior air space and the surrounding interstitial fluid) and $r$ denotes the alveolar radius. In an untreated lung lacking surfactant, surface tension remains constant ($\\gamma \\approx 70.0\\text{ mN/m}$, approximating pure water) regardless of lung inflation volume. Under these conditions, smaller interconnected alveoli generate substantially higher collapsing pressures than larger alveoli, driving gas down the pressure gradient into the larger units and causing widespread microatelectasis.</p>\n<p>To evaluate synthetic lipid emulsions against a natural porcine surfactant extract (poractant alfa), researchers utilize a pulsating bubble surfactometer (PBS). A liquid surfactant suspension is placed in an enclosed chamber maintained at $37^\\circ\\text{C}$, and an air bubble is formed at the tip of a capillary tube. The bubble is cyclically oscillated between a maximum radius ($r_{max} = 0.55\\text{ mm}$) and a minimum radius ($r_{min} = 0.40\\text{ mm}$) at 20 cycles per minute to mimic neonatal tidal ventilation. Pressure sensors record dynamic transmural pressure, from which minimum surface tension ($\\gamma_{min}$ at $r_{min}$), maximum surface tension ($\\gamma_{max}$ at $r_{max}$), and dynamic compliance are determined. Results across four surfactant formulations are detailed in Table 1.</p>\n<table class=\"tbl\">\n  <caption>Table 1 Dynamic surface tension and collapsing pressures measured across surfactant formulations</caption>\n  <thead>\n    <tr><th>Formulation</th><th>Composition</th><th>$\\gamma_{min}$ at $r_{min}$ (mN/m)</th><th>$\\gamma_{max}$ at $r_{max}$ (mN/m)</th><th>Collapsing $\\Delta P$ at $r_{min}$ (Pa)</th><th>Dynamic Compliance (mL/cm H$_2$O)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Saline Control</td><td>0.9% NaCl (Aqueous)</td><td>70.0</td><td>71.5</td><td>350</td><td>0.12</td></tr>\n    <tr><td>Formulation A</td><td>Synthetic DPPC alone</td><td>22.0</td><td>52.0</td><td>110</td><td>0.38</td></tr>\n    <tr><td>Formulation B</td><td>DPPC + 2% Recombinant SP-B/C</td><td>4.0</td><td>32.0</td><td>20</td><td>0.85</td></tr>\n    <tr><td>Poractant Alfa</td><td>Purified porcine lung extract</td><td>2.0</td><td>28.0</td><td>10</td><td>0.94</td></tr>\n  </tbody>\n</table>\n<p>Following tensiometric profiling, investigators examine whether adding recombinant SP-B peptide fragments preserves low surface tension during rapid compression-expansion cycling.</p>",
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
        "e": "<strong>Amphipathic surfactant monolayer dynamics:</strong> Surface tension arises from cohesive intermolecular forces\u2014primarily hydrogen bonding\u2014among liquid water molecules, which pull surface molecules toward the interior of the liquid. DPPC is an amphipathic phospholipid possessing a hydrophilic zwitterionic phosphocholine headgroup and two hydrophobic saturated palmitic acid acyl chains. When DPPC adsorbs at the air-liquid interface, its hydrophobic tails orient toward the alveolar airspace while its hydrophilic headgroups interact with surface water. By interposing between adjacent water molecules, DPPC disrupts intermolecular hydrogen bonding, dramatically lowering the cohesive inward pull and reducing surface tension.<br><br><em>Distractor Traps:</em><br>&bull; A misattributes surfactant function to covalent chemical bonding with respiratory gas molecules.<br>&bull; B erroneously describes surfactant as an enzyme that catalyzes covalent hydrolysis of water bonds.<br>&bull; D refers to carbonic acid ionization, which alters acid-base balance rather than interfacial surface tension."
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
  },
  {
    "id": "exam_cp60_4_p2",
    "sec": "C/P",
    "topic": "Continuity Equation & Microvascular Hemodynamics in Systemic Vascular Branching",
    "sheet": 2,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_4",
    "passage": "<div class=\"ttl\">Passage 2 (Questions 7&ndash;12)</div>\n<p>The human systemic circulation functions as a closed hydrodynamic circuit powered by the pulsatile ejection of blood from the left ventricle. Under steady-state conditions, conservation of mass for an incompressible fluid requires that the volumetric flow rate ($Q$) remain constant across any complete cross-section of the cardiovascular tree: $Q = A_{tot} \\cdot \\bar{v}$, where $A_{tot}$ represents the total cumulative cross-sectional area of all parallel conduits at a specific branching generation, and $\\bar{v}$ denotes the area-averaged linear flow velocity. Because blood is predominantly water, its density remains constant ($\\rho \\approx 1055\\text{ kg/m}^3$), satisfying the incompressibility criterion.</p>\n<p>As blood departs the ascending aorta, it traverses successive dichotomous and arborizing vascular bifurcations: large conduit arteries, muscular distributing arteries, terminal arterioles, capillary microvascular networks, postcapillary venules, and systemic veins, before coalescing into the inferior and superior venae cavae. Although individual vessel calibers diminish dramatically across distal generations&mdash;tapering from an aortic lumen diameter of $2.6\\text{ cm}$ down to capillary calibers of $8.0\\ \\mu\\text{m}$&mdash;the sheer multiplicity of parallel branches expands exponentially.</p>\n<p>To map microvascular fluid kinetics, biomedical engineers perfused an isolated mammalian mesentery preparation with a fluorophore-labeled dextran blood analogue under a constant physiological cardiac output of $Q = 84.0\\text{ cm}^3/\\text{s}$ ($5.04\\text{ L/min}$). High-speed intravital fluorescence video microscopy and pulsed-wave Doppler velocimetry tracked vessel caliber, estimated parallel vessel counts, total cross-sectional surface areas, and mean flow velocities across five anatomical vascular divisions. The quantitative measurements are summarized in Table 1.</p>\n<table class=\"tbl\">\n  <caption>Table 1 Morphometric and hemodynamic parameters across systemic vascular divisions</caption>\n  <thead>\n    <tr><th>Vascular Division</th><th>Mean Vessel Diameter ($d$)</th><th>Approximate Vessel Count ($N$)</th><th>Total Cross-Sectional Area ($A_{tot}$, cm$^2$)</th><th>Mean Blood Velocity ($\\bar{v}$, cm/s)</th><th>Mean Transit Time ($t$)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Aorta</td><td>2.6 cm</td><td>1</td><td>5.3</td><td>15.8</td><td>0.03 s</td></tr>\n    <tr><td>Large Arteries</td><td>0.40 cm</td><td>160</td><td>20.1</td><td>4.18</td><td>0.24 s</td></tr>\n    <tr><td>Arterioles</td><td>30 &mu;m</td><td>$5.0 \\times 10^7$</td><td>353.4</td><td>0.238</td><td>0.84 s</td></tr>\n    <tr><td>Capillaries</td><td>8.0 &mu;m</td><td>$6.0 \\times 10^9$</td><td>3016.0</td><td>0.0278</td><td>1.08 s</td></tr>\n    <tr><td>Venae Cavae</td><td>3.0 cm</td><td>2</td><td>14.1</td><td>5.96</td><td>0.17 s</td></tr>\n  </tbody>\n</table>\n<p>Researchers also evaluated the hemodynamic impact of focal arterial stenoses on upstream and downstream velocity gradients.</p>",
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
  },
  {
    "id": "exam_cp60_4_p3",
    "sec": "C/P",
    "topic": "Laminar vs Turbulent Flow & Reynolds Number (Re) in Carotid Stenosis and Murmurs",
    "sheet": 3,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_4",
    "passage": "<div class=\"ttl\">Passage 3 (Questions 13&ndash;18)</div>\n<p>In healthy systemic blood vessels, blood flow is predominantly laminar, characterized by fluid traveling smoothly in concentric cylindrical laminae parallel to the vessel axis. The velocity profile is parabolic, with maximum velocity at the centerline and zero velocity at the vessel wall due to the no-slip condition. When fluid velocity increases or vessel geometry becomes disturbed, flow can transition into a turbulent regime characterized by chaotic fluid fluctuations, recirculating vortices, elevated wall shear stress, and acoustic murmurs or bruits detectable via stethoscope.</p>\n<p>The transition between laminar and turbulent flow in a cylindrical pipe is governed by the dimensionless Reynolds number ($Re$):\n$$Re = \\frac{\\rho v d}{\\eta}$$\nwhere $\\rho$ is blood density ($1060\\text{ kg/m}^3$), $v$ is mean cross-sectional flow velocity, $d$ is vessel inner diameter, and $\\eta$ is dynamic viscosity. Under steady flow conditions in smooth rigid conduits, flow is strictly laminar when $Re < 2000$. Between $2000 \\le Re \\le 3000$, flow is transitional and sensitive to local wall irregularities. Fully turbulent flow is typically established when $Re > 3000$, although pulsatile flow and arterial branching can trigger turbulence at lower thresholds ($Re \\approx 2000$).</p>\n<p>To investigate how hematocrit and focal carotid stenoses interact to provoke audible bruits, investigators constructed an in vitro pulsatile mock circulatory loop. Silicone vascular phantoms representing internal carotid arteries (nominal diameter $d_0 = 6.0\\text{ mm}$) were fabricated with varying degrees of concentric luminal diameter reduction (0%, 50%, and 70% stenosis). The loop was perfused at a fixed volumetric flow rate of $Q = 6.0\\text{ mL/s}$ ($6.0 \\times 10^{-6}\\text{ m}^3/\\text{s}$) using test fluids mimicking normal blood ($\\eta = 3.50 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}$) and severe anemia ($\\eta = 1.75 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}$). An acoustic hydrophone recorded sound intensity. Results are presented in Table 1.</p>\n<table class=\"tbl\">\n  <caption>Table 1 Hemodynamic parameters and acoustic bruit generation across carotid stenosis models</caption>\n  <thead>\n    <tr><th>Stenosis Severity</th><th>Fluid Condition</th><th>Dynamic Viscosity $\\eta$ ($10^{-3}$ Pa&middot;s)</th><th>Stenotic Diameter $d$ (mm)</th><th>Mean Velocity $v$ (m/s)</th><th>Reynolds Number ($Re$)</th><th>Acoustic Bruit Detected?</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>0% (Control)</td><td>Normal Blood</td><td>3.50</td><td>6.0</td><td>0.212</td><td>385</td><td>No (Silent)</td></tr>\n    <tr><td>0% (Control)</td><td>Anemic Blood</td><td>1.75</td><td>6.0</td><td>0.212</td><td>770</td><td>No (Silent)</td></tr>\n    <tr><td>50% Stenosis</td><td>Normal Blood</td><td>3.50</td><td>3.0</td><td>0.849</td><td>770</td><td>No (Silent)</td></tr>\n    <tr><td>50% Stenosis</td><td>Anemic Blood</td><td>1.75</td><td>3.0</td><td>0.849</td><td>1540</td><td>Borderline Murmur</td></tr>\n    <tr><td>70% Stenosis</td><td>Normal Blood</td><td>3.50</td><td>1.8</td><td>2.358</td><td>1284</td><td>Weak Bruit</td></tr>\n    <tr><td>70% Stenosis</td><td>Anemic Blood</td><td>1.75</td><td>1.8</td><td>2.358</td><td>2568</td><td>High-Intensity Bruit</td></tr>\n  </tbody>\n</table>\n<p>Clinicians observe that when patients with severe aortic stenosis or carotid narrowing also suffer from untreated iron-deficiency anemia, the pitch and loudness of the associated murmur escalate markedly.</p>",
    "qs": [
      {
        "q": "What is the Reynolds number ($Re$) for a large systemic artery with inner diameter $d = 8.0\\text{ mm}$, conducting blood (density $\\rho = 1060\\text{ kg/m}^3$, viscosity $\\eta = 3.50 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}$) at a mean velocity of $v = 0.40\\text{ m/s}$?",
        "ch": [
          "970; flow is strictly laminar",
          "485; flow is strictly laminar",
          "1940; flow is unstable laminar",
          "3880; flow is fully turbulent"
        ],
        "a": 0,
        "e": "<strong>Reynolds number calculation and flow regime:</strong> The Reynolds number is calculated as $Re = \\frac{\\rho v d}{\\eta}$. Converting all parameters to SI units: $\\rho = 1060\\text{ kg/m}^3$, $v = 0.40\\text{ m/s}$, $d = 8.0\\text{ mm} = 8.0 \\times 10^{-3}\\text{ m}$, and $\\eta = 3.50 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}$. Substituting these values: $Re = \\frac{(1060\\text{ kg/m}^3)(0.40\\text{ m/s})(8.0 \\times 10^{-3}\\text{ m})}{3.50 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}} = \\frac{3.392}{3.50 \\times 10^{-3}} = 969.1 \\approx 970$. Because $Re < 2000$, viscous forces dominate inertial forces, and the flow is strictly laminar.<br><br><em>Distractor Traps:</em><br>&bull; B (485) mistakenly uses radius ($r = 4.0\\text{ mm}$) instead of diameter ($d = 8.0\\text{ mm}$).<br>&bull; C (1940) doubles the velocity or uses an incorrect viscosity value.<br>&bull; D (3880) quadruples the correct value and erroneously characterizes the flow as turbulent."
      },
      {
        "q": "Why are patients with severe chronic anemia predisposed to developing audible functional cardiac murmurs and vascular bruits even in the absence of severe structural stenosis?",
        "ch": [
          "Elevated hemoglobin concentration increases blood density and raises inertial resistance",
          "Decreased erythrocyte count elevates blood viscosity, increasing driving vascular pressure",
          "Reduced hematocrit lowers dynamic viscosity, markedly elevating the local Reynolds number",
          "Decreased blood volume causes peripheral vasoconstriction, slowing centerline flow velocity"
        ],
        "a": 2,
        "e": "<strong>Anemia, blood viscosity, and Reynolds number:</strong> Blood viscosity is largely determined by hematocrit (the volume percentage of red blood cells). In severe anemia, reduced hematocrit cuts dynamic blood viscosity substantially (e.g., from $3.50 \\times 10^{-3}$ down to $1.75 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}$, as demonstrated in Table 1). Because dynamic viscosity $\\eta$ appears in the denominator of the Reynolds number ($Re = \\rho v d / \\eta$), halving viscosity doubles the Reynolds number. Furthermore, to maintain tissue oxygen delivery, the body compensates by increasing cardiac output and blood velocity ($v$), driving $Re$ above the critical threshold of 2000 and producing turbulent flow that vibrates vessel walls, creating an audible \"flow murmur.\"<br><br><em>Distractor Traps:</em><br>&bull; A falsely asserts that hemoglobin concentration is elevated in anemia, when it is severely diminished.<br>&bull; B claims decreased RBC count increases viscosity; in reality, fewer RBCs reduce viscosity.<br>&bull; D claims flow velocity slows; compensatory physiology increases cardiac output and velocity."
      },
      {
        "q": "In a vessel with a constant volumetric flow rate ($Q$), why does reducing lumen diameter ($d$) through a stenosis increase the Reynolds number ($Re$), despite $d$ appearing in the numerator of $Re = \\rho v d / \\eta$?",
        "ch": [
          "Blood density rises sharply within a narrow stenosis due to localized erythrocyte compression",
          "Velocity increases as the inverse square of diameter, causing the product v &middot; d to scale as 1/d",
          "Dynamic viscosity decreases to near zero in the throat of the stenosis due to high wall friction",
          "Volumetric flow rate increases exponentially through narrowed conduits to conserve total mass"
        ],
        "a": 1,
        "e": "<strong>Stenotic velocity scaling and Reynolds number:</strong> In incompressible flow, volumetric flow rate is $Q = A v = \\frac{\\pi d^2}{4} v$, which means linear velocity scales as $v = \\frac{4Q}{\\pi d^2} \\propto \\frac{1}{d^2}$. Substituting this expression for $v$ into the Reynolds number equation yields: $Re = \\frac{\\rho v d}{\\eta} = \\frac{\\rho (4Q / \\pi d^2) d}{\\eta} = \\frac{4\\rho Q}{\\pi \\eta d} \\propto \\frac{1}{d}$. Therefore, although diameter is in the numerator of the original formula, the velocity increase ($1/d^2$) overpowers the linear diameter reduction ($d^1$), resulting in an overall inverse dependence on diameter ($1/d$). Halving the diameter doubles the Reynolds number for a fixed flow rate.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because blood is an incompressible fluid whose density remains constant.<br>&bull; C appeals to viscosity dropping to near zero, which is physically impossible and unphysical.<br>&bull; D falsely claims volumetric flow rate increases exponentially; continuity dictates flow rate is conserved."
      },
      {
        "q": "How does the radial velocity profile across a blood vessel cross-section differ between fully laminar flow and fully turbulent flow?",
        "ch": [
          "Laminar flow produces a blunted flat profile, whereas turbulent flow produces a sharp parabolic profile",
          "Laminar flow exhibits chaotic eddy fluctuations, whereas turbulent flow maintains concentric fluid laminae",
          "Laminar flow exhibits non-zero velocity at the wall, whereas turbulent flow enforces the no-slip condition",
          "Laminar flow produces a parabolic velocity profile, whereas turbulent flow produces a blunted flat profile"
        ],
        "a": 3,
        "e": "<strong>Velocity profile comparison:</strong> In fully developed laminar flow, fluid layers slide smoothly over each other against viscous shear, yielding a parabolic (Poiseuille) velocity profile described by $v(r) = v_{max}(1 - r^2/R^2)$, where velocity is maximal at the centerline and zero at the wall. In turbulent flow, chaotic radial mixing and turbulent eddies rapidly transport momentum across the entire lumen. This intense cross-stream mixing homogenizes velocities across the core, producing a blunted, flattened velocity profile with steep velocity gradients confined to a very thin boundary layer immediately adjacent to the wall.<br><br><em>Distractor Traps:</em><br>&bull; A completely reverses the two profiles, attributing the flat profile to laminar and parabolic to turbulent.<br>&bull; B reverses the fluid mechanics, assigning chaotic eddies to laminar flow.<br>&bull; C incorrectly claims laminar flow violates the no-slip condition; the no-slip condition holds universally for all real viscous fluids."
      },
      {
        "q": "When fluid flow transitions from laminar to turbulent in a rigid conduit, how does the relationship between the driving pressure gradient ($\\Delta P$) and volumetric flow rate ($Q$) change?",
        "ch": [
          "$\\Delta P \\propto Q$ in laminar flow, but changes to $\\Delta P \\propto Q^2$ in turbulent flow",
          "$\\Delta P \\propto Q^2$ in laminar flow, but changes to $\\Delta P \\propto Q$ in turbulent flow",
          "$\\Delta P \\propto Q$ in laminar flow, but changes to $\\Delta P \\propto Q^4$ in turbulent flow",
          "$\\Delta P$ becomes entirely independent of $Q$ once full turbulent flow is fully established"
        ],
        "a": 0,
        "e": "<strong>Pressure-flow relationships across flow regimes:</strong> In laminar flow governed by Poiseuille's law, energy dissipation occurs entirely through viscous shear between adjacent fluid layers, yielding a direct linear relationship between driving pressure drop and volumetric flow rate: $\\Delta P = R \\cdot Q \\implies \\Delta P \\propto Q$. When flow becomes turbulent, significant additional kinetic energy is dissipated into random, chaotic eddies, vortices, and wall collisions. In this turbulent regime, the Darcy-Weisbach formulation reveals that frictional head loss and pressure drop scale quadratically with flow velocity: $\\Delta P \\propto v^2 \\propto Q^2$. Consequently, driving turbulent blood flow requires substantially greater pumping pressure from the heart.<br><br><em>Distractor Traps:</em><br>&bull; B reverses the relationship, assigning quadratic scaling to laminar and linear to turbulent.<br>&bull; C incorrectly invokes a fourth-power dependence ($Q^4$), confusing Poiseuille's radius dependence ($r^4$) with flow rate scaling.<br>&bull; D falsely claims pressure drop becomes independent of flow rate."
      },
      {
        "q": "Auscultation of a vascular bruit over a stenosed carotid artery detects high-frequency acoustic murmurs. What physical process generates this acoustic energy?",
        "ch": [
          "Resonance of stationary laminar boundary layers vibrating against adjacent endothelial basement membranes",
          "Deposition of insoluble calcium crystals along the fibrous cap creating repetitive microscopic crackling",
          "Turbulent flow eddies generating pressure fluctuations that induce mechanical resonance in the vessel wall",
          "Frictional heating of circulating red blood cells radiating electromagnetic sound waves into neck tissue"
        ],
        "a": 2,
        "e": "<strong>Biophysics of vascular bruits and murmurs:</strong> In laminar flow, fluid streamlines are parallel and silent because there are no rapid temporal or spatial pressure fluctuations. When the Reynolds number exceeds the critical threshold ($Re > 2000$), flow separates and disintegrates into a chaotic field of turbulent vortices and eddies. These turbulent eddies produce rapid, local static pressure fluctuations against the arterial lumen. The fluctuating forces transmit mechanical strain into the viscoelastic arterial wall, causing it to vibrate at audible frequencies (typically $100&ndash;800\\text{ Hz}$). These vibrations propagate through surrounding soft tissue to the surface of the skin, where they are auscultated as a vascular bruit or cardiac murmur.<br><br><em>Distractor Traps:</em><br>&bull; A describes laminar flow, which is completely silent because fluid layers glide smoothly without rapid pressure fluctuations.<br>&bull; B suggests sounds originate from solid calcium crystal snapping, which is not the fluid mechanical mechanism of a bruit.<br>&bull; D is physically absurd, invoking electromagnetic radiation from frictional heating."
      }
    ]
  },
  {
    "id": "exam_cp60_4_p4",
    "sec": "C/P",
    "topic": "Poiseuille Resistance & Vascular Vasoconstriction in Arteriolar Hemodynamics",
    "sheet": 4,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_4",
    "passage": "<div class=\"ttl\">Passage 4 (Questions 19&ndash;24)</div>\n<p>Systemic vascular resistance (total peripheral resistance, TPR) is the primary determinant of mean arterial blood pressure ($\\text{MAP}$) for a given cardiac output ($\\text{CO}$), governed by the hemodynamic analogue of Ohm's law: $\\Delta P = \\text{CO} \\times \\text{TPR}$, where $\\Delta P = \\text{MAP} - \\text{RAP}$ (mean arterial pressure minus right atrial pressure). Because capillaries are arranged in an immense parallel network that dramatically lowers their net equivalent resistance, terminal arterioles&mdash;possessing thick muscular media capable of active contraction&mdash;serve as the principal &ldquo;stopcocks&rdquo; of the circulatory system, generating over 60% of total vascular resistance and producing the steepest drop in intravascular pressure.</p>\n<p>For laminar flow of a Newtonian fluid through a cylindrical vessel of length $L$ and internal radius $r$, resistance to flow ($R$) is defined by the Hagen-Poiseuille equation:\n$$R = \\frac{8\\eta L}{\\pi r^4}$$\nwhere $\\eta$ is dynamic blood viscosity. The volumetric flow rate is given by $Q = \\frac{\\Delta P}{R} = \\frac{\\Delta P \\pi r^4}{8\\eta L}$. Because vascular resistance exhibits an inverse fourth-power dependence on lumen radius ($R \\propto 1/r^4$), minute changes in vascular smooth muscle tone exert an outsized impact on local tissue perfusion and systemic blood pressure. A 16% reduction in arteriolar radius doubles hydraulic resistance, while a 50% luminal constriction escalates resistance by sixteen-fold ($2^4 = 16$).</p>\n<p>To quantify the pharmacological control of arteriolar caliber, vascular physiologists isolated and perfused an intact rat mesenteric microvascular bed with oxygenated Krebs-Henseleit buffer ($\\eta = 1.00 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}$, density $\\rho = 1000\\text{ kg/m}^3$) under a constant driving pressure of $\\Delta P = 80.0\\text{ mmHg}$ ($1.066 \\times 10^4\\text{ Pa}$). Vessels were exposed to baseline buffer, cumulative doses of the $\\alpha_1$-adrenergic agonist phenylephrine (PE, a potent vasoconstrictor), and the endothelium-dependent vasodilator acetylcholine (ACh). Arteriolar lumen diameter ($d = 2r$), volumetric flow rate ($Q$), and calculated hydraulic resistance ($R = \\Delta P / Q$) were recorded, as shown in Table 1.</p>\n<table class=\"tbl\">\n  <caption>Table 1 Mesenteric arteriolar diameter, volumetric flow rate, and vascular resistance across vasoactive trials</caption>\n  <thead>\n    <tr><th>Perfusion Condition</th><th>Vasoactive Agent</th><th>Vessel Diameter $d$ (&mu;m)</th><th>Vessel Radius $r$ (&mu;m)</th><th>Flow Rate $Q$ (&mu;L/min)</th><th>Vascular Resistance $R$ ($10^{10}$ Pa&middot;s/m$^3$)</th><th>Relative Resistance ($R/R_0$)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Baseline Control</td><td>Vehicle buffer</td><td>60.0</td><td>30.0</td><td>120.0</td><td>0.533</td><td>1.00</td></tr>\n    <tr><td>Mild Vasoconstriction</td><td>$10^{-7}$ M Phenylephrine</td><td>50.4</td><td>25.2</td><td>59.8</td><td>1.070</td><td>2.01</td></tr>\n    <tr><td>Severe Vasoconstriction</td><td>$10^{-5}$ M Phenylephrine</td><td>30.0</td><td>15.0</td><td>7.50</td><td>8.528</td><td>16.00</td></tr>\n    <tr><td>Maximum Vasoconstriction</td><td>$10^{-4}$ M Phenylephrine</td><td>20.0</td><td>10.0</td><td>1.48</td><td>43.220</td><td>81.09</td></tr>\n    <tr><td>Vasodilation</td><td>$10^{-6}$ M Acetylcholine</td><td>75.0</td><td>37.5</td><td>293.0</td><td>0.218</td><td>0.41</td></tr>\n  </tbody>\n</table>\n<p>Investigators noted that in vivo blood flow is further influenced by the non-Newtonian rheological properties of cellular suspensions and the parallel topology of peripheral microbeds.</p>",
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
  },
  {
    "id": "exam_cp60_4_p5",
    "sec": "C/P",
    "topic": "Blood Viscosity & Hematocrit Rheology: The F\u00e5hr\u00e6us-Lindqvist Effect",
    "sheet": 5,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_4",
    "passage": "<div class=\"ttl\">Passage 5 (Questions 25&ndash;30)</div>\n<p>Whole blood is a complex non-Newtonian, shear-thinning (pseudoplastic) suspension composed of cellular elements&mdash;primarily biconcave erythrocytes (red blood cells, RBCs)&mdash;suspended in liquid plasma. In large conduit arteries (diameter $d > 1.0\\text{ mm}$), blood behaves approximately as a homogeneous fluid with a constant bulk dynamic viscosity of $\\eta_{bulk} \\approx 3.5\\text{ to }4.0\\text{ mPa}\\cdot\\text{s}$ at physiological hematocrit ($Hct \\approx 45\\%$). However, when blood flows through microvessels of diameters between $300\\ \\mu\\text{m}$ and $10\\ \\mu\\text{m}$, its apparent dynamic viscosity ($\\eta_{app}$) decreases progressively as vessel caliber narrows&mdash;a phenomenon known as the F&aring;hr&aelig;us-Lindqvist effect.</p>\n<p>The F&aring;hr&aelig;us-Lindqvist effect arises from the transverse hydrodynamic migration of flexible erythrocytes toward the high-velocity centerline of the vessel lumen (axial migration). This leaves a cell-depleted, low-viscosity plasma layer along the vessel periphery where shear rates ($\\dot{\\gamma} = dv/dr$) are highest. Because this peripheral cell-free marginal layer acts as a low-friction hydraulic lubricant, the overall resistance to flow diminishes, causing calculated apparent viscosity to drop. Furthermore, because erythrocytes travel faster in the central core than the slower peripheral plasma, the average hematocrit inside the microvessel (tube hematocrit, $H_t$) is lower than the discharge hematocrit ($H_d$) entering and exiting the vessel (the F&aring;hr&aelig;us effect).</p>\n<p>To profile microvascular rheology, biomedical researchers perfused human blood samples of varying hematocrits through calibrated glass microcapillary tubes ranging in inner diameter from $500\\ \\mu\\text{m}$ down to $5\\ \\mu\\text{m}$ at a standardized shear rate of $\\dot{\\gamma} = 500\\text{ s}^{-1}$ and $T = 37^\\circ\\text{C}$. The relative apparent viscosity ($\\eta_{rel} = \\eta_{app} / \\eta_{plasma}$, where $\\eta_{plasma} = 1.20\\text{ mPa}\\cdot\\text{s}$) and tube hematocrit ($H_t$, for an initial discharge hematocrit of $H_d = 45.0\\%$) were quantified. Table 1 summarizes the experimental measurements.</p>\n<table class=\"tbl\">\n  <caption>Table 1 Apparent blood viscosity and tube hematocrit across microcapillary diameters</caption>\n  <thead>\n    <tr><th>Capillary Diameter $d$ (&mu;m)</th><th>Discharge Hematocrit $H_d$ (%)</th><th>Tube Hematocrit $H_t$ (%)</th><th>Relative Tube $Hct$ ($H_t/H_d$)</th><th>Apparent Viscosity $\\eta_{app}$ (mPa&middot;s)</th><th>Relative Viscosity $\\eta_{rel}$</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>500.0</td><td>45.0</td><td>45.0</td><td>1.00</td><td>3.84</td><td>3.20</td></tr>\n    <tr><td>200.0</td><td>45.0</td><td>41.4</td><td>0.92</td><td>3.48</td><td>2.90</td></tr>\n    <tr><td>100.0</td><td>45.0</td><td>36.9</td><td>0.82</td><td>2.88</td><td>2.40</td></tr>\n    <tr><td>30.0</td><td>45.0</td><td>30.6</td><td>0.68</td><td>2.16</td><td>1.80</td></tr>\n    <tr><td>10.0</td><td>45.0</td><td>27.0</td><td>0.60</td><td>1.80</td><td>1.50</td></tr>\n    <tr><td>5.0</td><td>45.0</td><td>31.5</td><td>0.70</td><td>3.12</td><td>2.60</td></tr>\n  </tbody>\n</table>\n<p>Researchers noted that this microvascular rheological adaptation significantly decreases cardiac workload by attenuating resistance in precapillary arteriole networks.</p>",
    "qs": [
      {
        "q": "What primary physical mechanism is responsible for the decrease in apparent blood viscosity observed as vessel diameter decreases from $500\\ \\mu\\text{m}$ to $10\\ \\mu\\text{m}$ (the F\u00e5hr\u00e6us-Lindqvist effect)?",
        "ch": [
          "Axial migration of erythrocytes creating a low-viscosity cell-free plasma lubrication layer",
          "Laminar shear stress inducing irreversible enzymatic denaturation of plasma albumin proteins",
          "Erythrocytes polymerizing into rigid linear rouleaux stacks that glide along the vessel wall",
          "Localized heating from viscous wall friction lowering water density at the fluid boundary"
        ],
        "a": 0,
        "e": "<strong>Fluid mechanics of the F&aring;hr&aelig;us-Lindqvist effect:</strong> In small cylindrical conduits ($10&ndash;300\\ \\mu\\text{m}$), red blood cells experience cross-stream hydrodynamic lift forces that cause them to migrate toward the centerline of the stream (axial migration). This creates a two-phase flow structure: a central core rich in erythrocytes and an erythrocyte-depleted, cell-free marginal plasma layer along the wall. Because fluid shear stress is greatest near the wall, having pure plasma (viscosity $\\sim 1.2\\text{ mPa}\\cdot\\text{s}$) adjacent to the endothelium lubricates the flow and substantially diminishes the overall apparent viscosity of the bulk suspension.<br><br><em>Distractor Traps:</em><br>&bull; B erroneously attributes the phenomenon to protein denaturation under physiological shear rates.<br>&bull; C describes rouleaux formation, which occurs at extremely low shear rates and increases viscosity rather than decreasing it.<br>&bull; D posits frictional heating and water density changes, which are negligible in physiological microcirculation."
      },
      {
        "q": "According to the F\u00e5hr\u00e6us effect illustrated in Table 1, why is the tube hematocrit ($H_t = 27.0\\%$) within a $10\\ \\mu\\text{m}$ capillary substantially lower than the systemic discharge hematocrit ($H_d = 45.0\\%$)?",
        "ch": [
          "Excess red blood cells are selectively filtered through fenestrations into the interstitium",
          "Erythrocytes travel in the high-velocity central core faster than slower peripheral plasma",
          "Erythrocytes undergo rapid hemolysis upon contacting narrow capillary endothelial boundaries",
          "Blood pressure forces plasma to accelerate downstream while erythrocytes become immobilized"
        ],
        "a": 1,
        "e": "<strong>Mechanism of the F&aring;hr&aelig;us effect:</strong> Because erythrocytes migrate axially toward the vessel center, they reside primarily within the high-velocity central core of the parabolic velocity profile. In contrast, the cell-free marginal layer consisting of plasma travels near the wall where velocity approaches zero (no-slip condition). As a result, the mean linear velocity of erythrocytes ($\\bar{v}_{rbc}$) is significantly faster than the mean velocity of the surrounding plasma ($\\bar{v}_{plasma}$). By mass conservation ($Q_{rbc} = A \\cdot H_t \\cdot \\bar{v}_{rbc}$), because RBCs transit the vessel faster, fewer of them need to be present inside the vessel lumen at any single instant to maintain the entering discharge flow ($H_d$). Consequently, $H_t < H_d$.<br><br><em>Distractor Traps:</em><br>&bull; A suggests erythrocytes filter into the interstitium, which would represent pathological capillary rupture or hemorrhage.<br>&bull; C asserts cells hemolyze; intact RBCs pass through safely without cell lysis.<br>&bull; D claims plasma travels faster than RBCs, which completely reverses the velocity relationship."
      },
      {
        "q": "In Table 1, when capillary diameter is reduced further from $10.0\\ \\mu\\text{m}$ to $5.0\\ \\mu\\text{m}$, apparent viscosity increases sharply from $1.80\\text{ mPa}\\cdot\\text{s}$ to $3.12\\text{ mPa}\\cdot\\text{s}$. What explains this inversion?",
        "ch": [
          "Plasma proteins precipitate spontaneously below critical Reynolds numbers",
          "Blood flow transitions into a fully developed chaotic turbulent flow state",
          "Vessel caliber is smaller than erythrocyte diameter, requiring deformation",
          "Peripheral cell-free layers expand to occupy the entire capillary diameter"
        ],
        "a": 2,
        "e": "<strong>F&aring;hr&aelig;us-Lindqvist inversion phenomenon:</strong> A human erythrocyte has a resting biconcave disk diameter of approximately $7.5&ndash;8.5\\ \\mu\\text{m}$. As long as vessel diameter exceeds $\\sim 10\\ \\mu\\text{m}$, erythrocytes can travel suspended within the core stream surrounded by a lubricating plasma layer. However, when the capillary diameter drops below $8\\ \\mu\\text{m}$ (such as the $5.0\\ \\mu\\text{m}$ capillary in Table 1), the cell diameter exceeds the tube lumen. Erythrocytes are forced into single-file flow and must undergo severe viscoelastic deformation (folding into parachute or slipper shapes). The cell membrane directly rubs against the vessel wall or an ultra-thin glycocalyx layer, introducing large steric frictional resistance that drives apparent viscosity sharply upward.<br><br><em>Distractor Traps:</em><br>&bull; A claims plasma proteins precipitate, which does not happen in microcirculation.<br>&bull; B suggests turbulent flow; in a 5 &mu;m tube, flow velocity is microscopic ($Re \\ll 1$), ensuring strictly creeping laminar (Stokes) flow.<br>&bull; D falsely claims the cell-free layer expands; in a 5 &mu;m tube, the cell-free layer is virtually eliminated as RBCs occupy the entire lumen."
      },
      {
        "q": "Blood is classified as a non-Newtonian, pseudoplastic (shear-thinning) fluid. At extremely low shear rates (such as during circulatory stasis or low flow), blood viscosity increases markedly primarily because:",
        "ch": [
          "Decreased pressure causes water molecules to evaporate from plasma into interstitial air spaces",
          "Erythrocyte membranes become rigid and undergo irreversible covalent cross-linking reactions",
          "Circulating leukocytes phagocytose free water dipoles to form dense crystalline macrofibrils",
          "Fibrinogen bridges adjacent erythrocytes into multi-cellular rouleaux stacks that resist flow"
        ],
        "a": 3,
        "e": "<strong>Non-Newtonian shear-thinning and rouleaux aggregation:</strong> At normal or high shear rates ($\\dot{\\gamma} > 100\\text{ s}^{-1}$), hydrodynamic shear forces deform and align flexible erythrocytes parallel to streamlines, minimizing viscous resistance. At very low shear rates ($\\dot{\\gamma} < 10\\text{ s}^{-1}$, e.g., low-flow states, shock, or venous stasis), shear forces are insufficient to overcome macromolecular attraction. Asymmetrical plasma proteins\u2014predominantly fibrinogen and immunoglobulins\u2014adsorb onto adjacent erythrocyte surfaces, bridging them together into linear stacked-coin aggregates known as rouleaux. These large macromolecular structures dramatically resist deformation, raising blood viscosity by up to an order of magnitude.<br><br><em>Distractor Traps:</em><br>&bull; A nonsensically proposes water evaporation inside closed systemic blood vessels.<br>&bull; B posits irreversible covalent cross-linking, but rouleaux formation is completely reversible upon restoring physiological shear.<br>&bull; C describes leukocyte phagocytosis of water, which is biologically meaningless."
      },
      {
        "q": "In polycythemia vera, a neoplastic myeloproliferative disorder, hematocrit often rises above 65%. What hemodynamic consequence directly results from this abnormal rheological state?",
        "ch": [
          "Elevated Reynolds number triggers turbulent bruits throughout all systemic conduit veins",
          "Markedly increased bulk blood viscosity raises total peripheral resistance and cardiac work",
          "Decreased blood viscosity reduces peripheral resistance, precipitating circulatory collapse",
          "Enhanced axial migration of cells reduces apparent microvascular viscosity to near zero"
        ],
        "a": 1,
        "e": "<strong>Polycythemia and blood viscosity:</strong> Bulk blood viscosity increases exponentially with hematocrit. When hematocrit rises from a normal 45% to >65% in polycythemia vera, dynamic viscosity can more than double (from ~3.5 to >8.0 mPa&middot;s). By Poiseuille's law ($R = 8\\eta L / \\pi r^4$), vascular resistance is directly proportional to dynamic viscosity $\\eta$. Consequently, total peripheral resistance (TPR) increases substantially, forcing the left ventricle to generate much higher systolic pressures to maintain cardiac output ($\\text{MAP} = \\text{CO} \\times \\text{TPR}$), increasing cardiac workload and elevating the risk of thrombotic stroke and ischemia.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because increased viscosity actually lowers the Reynolds number ($Re = \\rho v d / \\eta$), stabilizing laminar flow and suppressing turbulence.<br>&bull; C falsely states viscosity decreases.<br>&bull; D is incorrect because severe cell overcrowding hinders axial migration and elevates microvascular resistance."
      },
      {
        "q": "If an experimental capillary tube ($d = 30\\ \\mu\\text{m}$, length $L$) is perfused with whole blood ($\\eta_{app} = 2.16\\text{ mPa}\\cdot\\text{s}$) and subsequently with pure plasma ($\\eta_{plasma} = 1.20\\text{ mPa}\\cdot\\text{s}$) under identical pressure gradients ($\\Delta P$), what is the ratio of volumetric flow rate of plasma to whole blood ($Q_{plasma} / Q_{blood}$)?",
        "ch": [
          "0.56",
          "1.00",
          "1.80",
          "3.24"
        ],
        "a": 2,
        "e": "<strong>Poiseuille flow rate and viscosity ratio:</strong> Poiseuille's equation states that $Q = \\frac{\\Delta P \\pi r^4}{8\\eta L}$. When pressure gradient $\\Delta P$, tube radius $r$, and length $L$ are held constant, volumetric flow rate is inversely proportional to dynamic viscosity: $Q \\propto \\frac{1}{\\eta}$. Therefore, the ratio of flow rates is the inverse ratio of their dynamic viscosities: $\\frac{Q_{plasma}}{Q_{blood}} = \\frac{\\eta_{blood}}{\\eta_{plasma}} = \\frac{2.16\\text{ mPa}\\cdot\\text{s}}{1.20\\text{ mPa}\\cdot\\text{s}} = 1.80$. Pure plasma flows 1.80 times faster than whole blood under identical driving pressures.<br><br><em>Distractor Traps:</em><br>&bull; A (0.56) inverts the ratio ($1.20 / 2.16 = 0.556$).<br>&bull; B (1.00) assumes viscosity has no effect on volumetric flow rate.<br>&bull; D (3.24) squares the ratio ($1.80^2 = 3.24$)."
      }
    ]
  },
  {
    "id": "exam_cp60_4_disc",
    "sec": "C/P",
    "topic": "C/P Standalone Discrete Questions",
    "sheet": null,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_4",
    "passage": "",
    "qs": [
      {
        "q": "The Monro-Kellie hypothesis states that the adult cranial vault is a rigid, non-compliant container with a fixed total volume composed of brain parenchyma, cerebrospinal fluid (CSF), and blood. When an acute epidural hematoma begins to expand within the intracranial vault, why does intracranial pressure (ICP) initially remain near normal before eventually rising exponentially?",
        "ch": [
          "CSF and venous blood are displaced into spinal and extracranial vascular reservoirs",
          "Brain parenchyma compresses elastically into porous cranial diploic bone marrow",
          "Arterial systolic pressure drops precipitously to maintain stable perfusion volume",
          "Choroid plexus ependymal cells immediately cease active cerebrospinal production"
        ],
        "a": 0,
        "d": true,
        "e": "<strong>Monro-Kellie hypothesis and intracranial volume compensation:</strong> The adult skull is a rigid, non-distensible cavity with a fixed internal volume: $V_{total} = V_{brain} + V_{CSF} + V_{blood} = \\text{constant}$. When an abnormal mass (such as an acute arterial epidural hematoma) expands, the intracranial vault initially compensates by shunting equal volumes of low-pressure, highly compliant fluid components out of the skull. Specifically, CSF is displaced down the spinal subarachnoid space and into dural sinuses, while venous blood is squeezed out of low-pressure cerebral veins into the jugular system. This maintains intracranial compliance, buffering ICP. However, once these reserves are completely exhausted, the volume-pressure curve steepens sharply into a non-compliant state, where any further volume expansion causes an exponential spike in ICP, precipitating brain herniation.<br><br><em>Distractor Traps:</em><br>&bull; B is anatomically impossible because intact solid brain parenchyma cannot compress or enter diploic marrow spaces through the inner skull table.<br>&bull; C is physiologically opposite; the Cushing reflex elevates systemic arterial systolic pressure in response to rising ICP to preserve cerebral perfusion pressure.<br>&bull; D is incorrect because the choroid plexus produces CSF at a relatively constant metabolic rate (~500 mL/day) that does not automatically shut down upon acute mass expansion."
      },
      {
        "q": "A pulmonary diagnostic spirometer utilizes a Pitot-static tube to determine a patient's peak expiratory airflow velocity. If the differential pressure transducer measures a dynamic pressure difference of $\\Delta P = P_{stagnation} - P_{static} = 240\\text{ Pa}$ and the expired air density is $\\rho = 1.20\\text{ kg/m}^3$, what is the peak expiratory airflow velocity?",
        "ch": [
          "10.0 m/s",
          "20.0 m/s",
          "40.0 m/s",
          "80.0 m/s"
        ],
        "a": 1,
        "d": true,
        "e": "<strong>Pitot-static tube and stagnation pressure:</strong> A Pitot tube measures total stagnation pressure ($P_{stagnation}$), where fluid brought to rest converts its kinetic energy into static pressure. By Bernoulli's equation: $P_{stagnation} = P_{static} + \\frac{1}{2}\\rho v^2$. The dynamic pressure difference is $\\Delta P = P_{stagnation} - P_{static} = \\frac{1}{2}\\rho v^2$. Solving for fluid flow velocity: $v = \\sqrt{\\frac{2\\Delta P}{\\rho}}$. Substituting the given values: $v = \\sqrt{\\frac{2(240\\text{ Pa})}{1.20\\text{ kg/m}^3}} = \\sqrt{\\frac{480}{1.20}} = \\sqrt{400} = 20.0\\text{ m/s}$.<br><br><em>Distractor Traps:</em><br>&bull; A (10.0 m/s) forgets to multiply by 2 under the radical, calculating $\\sqrt{240 / 1.20} = \\sqrt{200} \\approx 14.1$ or dividing 20 by 2.<br>&bull; C (40.0 m/s) doubles the correct velocity or neglects the square root ($400 / 10$).<br>&bull; D (80.0 m/s) computes $(2 \\times 240) / (1.2 \\times 5)$ or fails to apply the square root."
      },
      {
        "q": "In microfluidic lab-on-a-chip capillary electrophoresis using negatively charged fused-silica channels at physiological pH 7.4, what physical mechanism allows both negatively and positively charged peptide fragments to migrate toward the cathode (negative electrode) detector?",
        "ch": [
          "Cations undergo spontaneous nuclear fission to generate outward repulsive propulsion",
          "Negative peptides reverse electric dipole polarity upon encountering laminar friction",
          "Strong cathodic electroosmotic bulk flow overcomes opposing electrophoretic migration",
          "Laminar drag forces accelerate uncharged peptides faster than smaller charged ions"
        ],
        "a": 2,
        "d": true,
        "e": "<strong>Electroosmotic flow vs electrophoretic mobility:</strong> At pH 7.4, silanol groups on fused-silica microchannel walls deprotonate to form fixed negative charges ($\\text{Si-O}^-$). Cations in the running buffer accumulate along the wall to form an electrical double layer. When an axial electric field is applied, the mobile hydrated cations in the diffuse layer are pulled toward the cathode (negative electrode). Through viscous shear, these moving cations drag the entire bulk aqueous fluid along the channel toward the cathode\u2014a bulk transport phenomenon termed electroosmotic flow (EOF). Because the magnitude of EOF is typically significantly greater than the intrinsic upstream electrophoretic mobility ($\\mu_{ep}$) of anionic peptides, both cations, neutrals, and anions are carried downstream toward the cathode, while differences in individual charge-to-size ratios achieve high-resolution separation.<br><br><em>Distractor Traps:</em><br>&bull; A appeals to nuclear fission, which never occurs in biochemical microfluidic chips.<br>&bull; B nonsensically suggests peptides reverse their net electrical dipole polarity due to friction.<br>&bull; D is incorrect because neutrals move at the EOF velocity, while cations move faster and anions move slower than neutrals."
      }
    ]
  }
];
