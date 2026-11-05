/* ---- exam_cp90_5.js ---- */
/* Full 90-minute Chem/Physical Practice Exam 5: 7 passages (42 Qs) + 10 discrete Qs = 52 Qs */
const EXAM_CP90_5 = [
  {
    "id": "exam_cp90_5_p1",
    "sec": "C/P",
    "topic": "Acoustic Cavitation in High-Intensity Focused Ultrasound (HIFU)",
    "sheet": 1,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_5",
    "passage": "<div class=\"ttl\">Passage 1 (Questions 1&ndash;6)</div>\n<p>High-intensity focused ultrasound (HIFU) is a non-invasive therapeutic intervention designed for precise thermal and mechanical ablation of solid tumors. In HIFU, concave piezoelectric transducers focus megahertz-frequency acoustic waves into a millimeter-scale focal volume, converting focused acoustic energy into thermal and mechanical stresses within target tissue. Propagation of ultrasound waves through biological media is governed by longitudinal pressure fluctuations characterized by speed of sound ($c \\approx 1540\\text{ m/s}$ in soft tissue), acoustic frequency ($f$), and wavelength ($\\lambda$).</p>\n<p>Beyond thermal coagulative necrosis, ultrasound beam interactions with biological fluids induce acoustic cavitation&mdash;the nucleation, oscillation, and collapse of microscopic gas bubbles. Cavitation is classified into two distinct mechanical regimes:</p>\n<p>1. <em>Stable (non-inertial) cavitation</em>: Microbubbles undergo sustained, periodic oscillations about an equilibrium radius in response to cyclic acoustic compression and rarefaction. This radial pulsation drives acoustic microstreaming in the surrounding fluid, producing shear stresses that transiently permeabilize cell membranes (sonoporation).</p>\n<p>2. <em>Inertial (transient) cavitation</em>: Under high peak rarefactional pressure ($P_r$), microbubbles expand rapidly to more than twice their equilibrium radius before collapsing violently during the compressive phase due to the inertia of the surrounding fluid. This catastrophic collapse generates localized temperatures exceeding $5000\\text{ K}$, local pressures above $100\\text{ MPa}$, high-speed liquid microjets, and the sonolytic cleavage of water into reactive hydroxyl radicals ($\\cdot\\text{OH}$).</p>\n<p>To quantify the likelihood of inertial cavitation, clinical systems compute the Mechanical Index ($MI$):</p>\n<p>$$MI = \\frac{P_r}{\\sqrt{f}}$$</p>\n<p>where $P_r$ is the derated peak rarefactional pressure in megapascals (MPa) and $f$ is the ultrasound center frequency in megahertz (MHz). An $MI > 1.9$ is generally required to initiate inertial cavitation in visceral tissues. Investigators tested four HIFU beam configurations in ex vivo tissue phantoms to establish cavitation thresholds (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Acoustic parameters, cavitation regimes, and ablation metrics across HIFU settings</caption>\n  <thead>\n    <tr><th>Setting</th><th>Frequency $f$ (MHz)</th><th>Peak Rarefactional $P_r$ (MPa)</th><th>Mechanical Index ($MI$)</th><th>Cavitation Mode</th><th>Mean Ablation Volume ($\\text{mm}^3$)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Setting 1</td><td>1.0</td><td>0.8</td><td>0.80</td><td>None (Thermal only)</td><td>12.4</td></tr>\n    <tr><td>Setting 2</td><td>1.0</td><td>1.5</td><td>1.50</td><td>Stable Cavitation</td><td>28.6</td></tr>\n    <tr><td>Setting 3</td><td>1.0</td><td>2.5</td><td>2.50</td><td>Inertial Cavitation</td><td>84.2</td></tr>\n    <tr><td>Setting 4</td><td>4.0</td><td>2.5</td><td>1.25</td><td>Stable Cavitation</td><td>31.0</td></tr>\n  </tbody>\n</table>\n<p>Investigators next monitored whether introducing microbubble contrast agents decreases the acoustic pressure threshold required for inertial cavitation.</p>",
    "qs": [
      {
        "q": "What is the acoustic wavelength $\\lambda$ of the ultrasound beam utilized in Setting 1 ($f = 1.0\\text{ MHz}$) when propagating through soft tissue ($c = 1540\\text{ m/s}$)?",
        "ch": [
          "1.54 mm",
          "0.65 mm",
          "3.08 mm",
          "0.77 mm"
        ],
        "a": 0,
        "e": "<strong>Ultrasound wave speed, frequency, and wavelength relationship:</strong> Acoustic propagation velocity through a medium is defined by the wave equation $v = f\\lambda$, where $v = c = 1540\\text{ m/s}$ and frequency $f = 1.0\\text{ MHz} = 1.0 \\times 10^6\\text{ Hz}$. Rearranging for wavelength gives $\\lambda = \\frac{c}{f} = \\frac{1540\\text{ m/s}}{1.0 \\times 10^6\\text{ s}^{-1}} = 1.54 \\times 10^{-3}\\text{ m} = 1.54\\text{ mm}$. At this wavelength, ultrasound provides an optimal compromise between focal penetration depth and spatial focus size in visceral organs.<br><br><em>Distractor Traps:</em><br>&bull; B (0.65 mm) erroneously inverts the wave velocity formula, calculating $f / c = 1.0 \\times 10^6 / 1540$.<br>&bull; C (3.08 mm) doubles the calculated wavelength by incorrectly multiplying the velocity by 2.<br>&bull; D (0.77 mm) halves the correct value, which would correspond to a frequency of 2.0 MHz."
      },
      {
        "q": "Based on the Mechanical Index equation provided in the passage, if a HIFU beam operates at $f = 2.25\\text{ MHz}$ with a peak rarefactional pressure of $P_r = 2.50\\text{ MPa}$, what is the resulting $MI$, and will it induce inertial cavitation?",
        "ch": [
          "MI = 1.11; the beam will readily initiate inertial cavitation",
          "MI = 1.67; the beam will remain below the inertial threshold",
          "MI = 2.05; the beam will readily initiate inertial cavitation",
          "MI = 3.75; the beam will remain below the inertial threshold"
        ],
        "a": 1,
        "e": "<strong>Mechanical Index calculation and cavitation threshold:</strong> The Mechanical Index is computed as $MI = \\frac{P_r}{\\sqrt{f}}$. Substituting $P_r = 2.50\\text{ MPa}$ and $f = 2.25\\text{ MHz}$: $\\sqrt{2.25} = 1.50$, so $MI = \\frac{2.50}{1.50} = 1.67$. The passage specifies that $MI > 1.9$ is required to overcome acoustic cavitation thresholds and initiate inertial cavitation in visceral tissues. Because $1.67 < 1.9$, the ultrasound beam will not trigger inertial cavitation and will instead remain in the stable cavitation or purely thermal regime.<br><br><em>Distractor Traps:</em><br>&bull; A (1.11) erroneously divides $P_r$ by $f$ directly ($2.50 / 2.25 = 1.11$) rather than taking the square root of $f$, and misinterprets the threshold rule.<br>&bull; C (2.05) erroneously calculates $\\sqrt{P_r} / f$ or makes an arithmetic error and falsely claims cavitation occurs.<br>&bull; D (3.75) multiplies $P_r$ by $\\sqrt{f}$ ($2.50 \\times 1.50 = 3.75$) instead of dividing."
      },
      {
        "q": "Which fundamental biophysical mechanism distinguishes inertial cavitation from stable cavitation during focused ultrasound therapy?",
        "ch": [
          "Sustained radial oscillation about a constant equilibrium bubble radius",
          "Acoustic microstreaming generated without any dynamic bubble expansion",
          "Rapid bubble expansion followed by catastrophic inertia-driven collapse",
          "Continuous acoustic wave reflection at rigid mineral-tissue interfaces"
        ],
        "a": 2,
        "e": "<strong>Mechanical dynamics of inertial versus stable cavitation:</strong> Stable cavitation involves non-destructive, rhythmic expansion and contraction of gas bubbles about an equilibrium radius over hundreds or thousands of acoustic cycles, inducing localized shear stresses via acoustic microstreaming. In contrast, inertial cavitation occurs when high rarefactional pressure causes a microbubble to expand unstably to more than double its initial radius, followed by an unrestrained, catastrophic collapse driven by the inertia of the surrounding fluid. This violent collapse focuses energy into microscopic shock waves, extreme temperatures ($>5000\\text{ K}$), and high-velocity microjets, resulting in mechanical tissue lysis.<br><br><em>Distractor Traps:</em><br>&bull; A describes stable (non-inertial) cavitation, where microbubbles oscillate symmetrically without collapsing.<br>&bull; B describes microstreaming without collapse, which is characteristic of low-intensity stable acoustic agitation.<br>&bull; D refers to acoustic reflection at acoustic impedance mismatches (e.g., bone-tissue interfaces), not bubble cavitation."
      },
      {
        "q": "Acoustic intensity is related to acoustic pressure amplitude by $I = \\frac{P^2}{2\\rho c}$. If the pressure amplitude $P$ delivered by an ultrasound transducer is tripled while tissue density $\\rho$ and speed of sound $c$ remain constant, by what factor does acoustic intensity increase?",
        "ch": [
          "A factor of 1.73",
          "A factor of 3.00",
          "A factor of 6.00",
          "A factor of 9.00"
        ],
        "a": 3,
        "e": "<strong>Proportionality between acoustic intensity and pressure amplitude:</strong> Acoustic intensity ($I$) is directly proportional to the square of the pressure amplitude ($P^2$): $I \\propto P^2$. If the pressure amplitude is tripled ($P' = 3P$), the new acoustic intensity becomes $I' = \\frac{(3P)^2}{2\\rho c} = 9 \\left(\\frac{P^2}{2\\rho c}\\right) = 9I$. Thus, acoustic intensity increases by a factor of $3^2 = 9.00$. This quadratic relationship explains why modest increases in transducer driving voltage produce dramatic increases in focal heating and mechanical cavitation power.<br><br><em>Distractor Traps:</em><br>&bull; A takes the square root of 3 ($\\sqrt{3} \\approx 1.73$), inverting the power exponent.<br>&bull; B assumes a direct linear relationship between intensity and pressure ($I \\propto P$), ignoring the quadratic power term.<br>&bull; C incorrectly multiplies the factor 3 by 2 rather than squaring it."
      },
      {
        "q": "During inertial cavitation, the formation of reactive hydroxyl radicals ($\\cdot\\text{OH}$) in sonicated aqueous tissue phantoms is primarily driven by which chemical mechanism?",
        "ch": [
          "Thermal sonolysis of water driven by localized adiabatic bubble collapse",
          "Photolytic excitation of dissolved molecular oxygen by emitted phonons",
          "Direct ionization of biological lipids by coherent acoustic radiation",
          "Electrochemical oxidation induced by static surface dielectric breakdown"
        ],
        "a": 0,
        "e": "<strong>Sonolysis of water during inertial cavitation:</strong> The violent, rapid collapse of an inertial cavitation bubble occurs on nanosecond timescales and is essentially an adiabatic compression process. The compression of trapped gas and water vapor heats the interior of the bubble to transient localized temperatures exceeding $5000\\text{ K}$ and pressures exceeding $100\\text{ MPa}$. Under these extreme conditions, homolytic cleavage of the $\\text{O}-\\text{H}$ covalent bonds in vaporized water occurs: $\\text{H}_2\\text{O} \\to \\text{H}\\cdot + \\cdot\\text{OH}$. This process, known as sonolysis, produces highly reactive hydroxyl radicals capable of oxidizing cellular macromolecules.<br><br><em>Distractor Traps:</em><br>&bull; B incorrectly attributes radical formation to phonon-induced photolysis of molecular oxygen.<br>&bull; C claims ultrasound radiation directly ionizes lipids; ultrasound is non-ionizing mechanical radiation and lacks sufficient photon/quantum energy to directly eject electrons.<br>&bull; D invents an electrostatic breakdown mechanism, conflating acoustic cavitation with high-voltage electroporation."
      },
      {
        "q": "As ultrasound frequency increases from 1.0 MHz (Setting 3) to 4.0 MHz (Setting 4), tissue acoustic attenuation increases significantly. What clinical trade-off does this frequency dependence impose on HIFU tumor ablation?",
        "ch": [
          "Higher frequency enhances deep penetration depth but degrades focal resolution",
          "Higher frequency improves focal spatial resolution but limits penetration depth",
          "Lower frequency decreases focal volume size while minimizing thermal absorption",
          "Lower frequency maximizes acoustic scattering while eliminating cavitation risks"
        ],
        "a": 1,
        "e": "<strong>Acoustic frequency trade-off between spatial resolution and penetration depth:</strong> In medical ultrasound, acoustic attenuation increases approximately linearly with frequency ($\\text{attenuation} = \\alpha \\cdot f \\cdot x$). A higher frequency (such as 4.0 MHz) produces shorter wavelengths ($\\lambda = c/f$), enabling tighter diffraction-limited focal spots and superior spatial resolution. However, high-frequency sound waves suffer rapid energy attenuation and exponential intensity loss with tissue depth ($I = I_0 e^{-\\mu x}$), severely restricting their effective penetration depth. Conversely, lower frequencies (such as 1.0 MHz) penetrate deeply into visceral tissues (e.g., deep liver or pelvic lesions) but produce larger focal volumes with reduced precision.<br><br><em>Distractor Traps:</em><br>&bull; A completely reverses the physical trade-off, falsely asserting that high frequency increases penetration and degrades resolution.<br>&bull; C incorrectly claims lower frequency decreases focal volume size; lower frequency yields longer wavelengths and larger diffraction-limited focal spots.<br>&bull; D falsely claims lower frequency eliminates cavitation; as shown by the $MI$ formula ($MI = P_r / \\sqrt{f}$), lower frequencies actually facilitate cavitation because the longer acoustic cycle allows bubbles more time to expand."
      }
    ]
  },
  {
    "id": "exam_cp90_5_p2",
    "sec": "C/P",
    "topic": "Peritoneal Dialysis Fluid Osmotic Ultrafiltration Kinetics",
    "sheet": 2,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_5",
    "passage": "<div class=\"ttl\">Passage 2 (Questions 7&ndash;12)</div>\n<p>Peritoneal dialysis (PD) is an established renal replacement therapy utilizing the patient's peritoneal microvasculature as a semipermeable membrane to clear uremic toxins and eliminate excess body water. Fluid extraction across the peritoneal membrane, termed osmotic ultrafiltration (UF), is driven by an osmotic pressure gradient generated by instilling a hypertonic dialysate into the peritoneal cavity.</p>\n<p>Transperitoneal fluid and solute transport is classically described by the three-pore model of capillary permeability:</p>\n<p>1. <em>Ultrasmall pores (Aquaporin-1, AQP1)</em>: Transcellular water-selective channels (~0.4 nm diameter) that completely exclude solutes (Staverman reflection coefficient $\\sigma = 1.0$). These channels mediate approximately 50% of initial transperitoneal water transport.</p>\n<p>2. <em>Small inter-endothelial pores</em>: Intercellular clefts (radius ~4.0&ndash;4.5 nm) accounting for ~90% of total pore area. These pores permit the transport of small solutes (urea, creatinine, electrolytes) and water. For dextrose (D-glucose, $MW = 180\\text{ Da}$), the reflection coefficient is $\\sigma \\approx 0.03&ndash;0.05$.</p>\n<p>3. <em>Large pores</em>: Sparsely distributed endothelial gaps (radius 20&ndash;40 nm) mediating macromolecular protein leakage, where $\\sigma \\approx 0$.</p>\n<p>The net volumetric fluid flux ($J_v$) is governed by the extended Starling equation:</p>\n<p>$$J_v = L_p S \\left[ \\Delta P - \\sum \\sigma_i \\Delta \\Pi_i \\right] - L_R$$</p>\n<p>where $L_p S$ is the hydraulic permeability-surface area product, $\\Delta P$ is the transperitoneal hydrostatic pressure gradient, $\\sigma_i$ is the reflection coefficient of solute $i$, $\\Delta \\Pi_i = i R T \\Delta C_i$ is the transperitoneal osmotic pressure gradient, and $L_R$ represents the continuous rate of lymphatic fluid reabsorption (~1.5 mL/min).</p>\n<p>During a dwell, dialysate dextrose diffuses down its concentration gradient into the capillary circulation. As glucose dissipates, $\\Delta \\Pi$ declines until lymphatic reabsorption exceeds transcapillary filtration, causing net fluid resorption. Table 1 outlines kinetic parameters for three dialysates over a 240-minute dwell.</p>\n<table class=\"tbl\">\n  <caption>Table 1 Dialysate solute concentrations, intraperitoneal volume, and ultrafiltration rates</caption>\n  <thead>\n    <tr><th>Dialysate Formulation</th><th>Dwell Time (min)</th><th>Dialysate Glucose (mM)</th><th>Dialysate $[\\text{Na}^+]$ (mEq/L)</th><th>Intraperitoneal Volume (mL)</th><th>Net UF Rate (mL/min)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td rowspan=\"3\">1.5% Dextrose</td><td>0</td><td>83</td><td>132</td><td>2000</td><td>+4.2</td></tr>\n    <tr><td>60</td><td>54</td><td>126</td><td>2180</td><td>+1.8</td></tr>\n    <tr><td>240</td><td>25</td><td>131</td><td>2120</td><td>-0.8</td></tr>\n    <tr><td rowspan=\"3\">4.25% Dextrose</td><td>0</td><td>236</td><td>132</td><td>2000</td><td>+12.5</td></tr>\n    <tr><td>60</td><td>148</td><td>118</td><td>2540</td><td>+6.4</td></tr>\n    <tr><td>240</td><td>58</td><td>129</td><td>2820</td><td>+0.4</td></tr>\n    <tr><td rowspan=\"2\">7.5% Icodextrin</td><td>0</td><td>0</td><td>132</td><td>2000</td><td>+2.2</td></tr>\n    <tr><td>240</td><td>0</td><td>131</td><td>2550</td><td>+2.1</td></tr>\n  </tbody>\n</table>\n<p>Investigators evaluate whether continuous ambulatory peritoneal dialysis patients develop aquaporin-1 dysfunction following recurrent peritonitis episodes.</p>",
    "qs": [
      {
        "q": "According to the van 't Hoff equation ($\\Pi = i C R T$), what theoretical osmotic pressure is generated by the initial dextrose concentration in the 4.25% dextrose formulation ($C = 236\\text{ mM} = 236\\text{ mol/m}^3$) at physiological temperature ($T = 310\\text{ K}$, $R = 8.314\\text{ J/(mol}\\cdot\\text{K)}$)?",
        "ch": [
          "152 kPa",
          "304 kPa",
          "608 kPa",
          "912 kPa"
        ],
        "a": 2,
        "e": "<strong>Van 't Hoff osmotic pressure calculation:</strong> The van 't Hoff equation describes osmotic pressure as $\\Pi = i C R T$. Dextrose (D-glucose) is a non-electrolyte and does not dissociate in aqueous solution, so the van 't Hoff factor is $i = 1$. Converting concentration to SI units yields $C = 236\\text{ mM} = 236\\text{ mol/m}^3$. Substituting the values: $\\Pi = (1)(236\\text{ mol/m}^3)(8.314\\text{ J/(mol}\\cdot\\text{K)})(310\\text{ K}) = 236 \\times 2577.34 = 608,252\\text{ Pa} \\approx 608\\text{ kPa}$. This substantial osmotic pressure gradient drives rapid initial fluid extraction into the peritoneal space.<br><br><em>Distractor Traps:</em><br>&bull; A (152 kPa) erroneously divides the calculated pressure by 4 or uses room temperature in Celsius.<br>&bull; B (304 kPa) erroneously divides by 2 or uses the concentration of the 1.5% dextrose formulation (83 mM $\\times 2577 \\approx 214$ kPa) with an arithmetic error.<br>&bull; D (912 kPa) multiplies the correct result by 1.5, assuming an incorrect van 't Hoff factor of 1.5."
      },
      {
        "q": "During the initial 60 minutes of the 4.25% dextrose dwell, dialysate sodium concentration drops from 132 mEq/L to 118 mEq/L (Table 1). What physical transport mechanism accounts for this 'sodium sieving' phenomenon?",
        "ch": [
          "Active secondary transport of sodium cations across peritoneal mesothelium",
          "Selective paracellular precipitation of sodium chloride within interstitium",
          "Rapid convective drag of dialysate sodium across large vascular pore clefts",
          "Solute-free water ultrafiltration through transcellular aquaporin channels"
        ],
        "a": 3,
        "e": "<strong>Sodium sieving and aquaporin-mediated transcellular water flux:</strong> Aquaporin-1 (AQP1) channels are ultra-small transcellular water pores that are completely impermeable to sodium and other electrolytes (reflection coefficient $\\sigma = 1.0$). Early in the dwell, the high transperitoneal crystalloid glucose gradient drives massive, rapid water flux through AQP1 into the peritoneal cavity without accompanying solutes. This influx of solute-free water dilutes the existing dialysate sodium, causing the observed dip from 132 to 118 mEq/L. Later, as glucose dissipates and small-pore diffusion continues, sodium equilibrates back toward plasma levels.<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly attributes the sodium drop to active transcellular mesothelial ion pumping rather than passive dilution by water flux.<br>&bull; B suggests chemical precipitation of sodium chloride, which does not occur under physiological fluid conditions.<br>&bull; C describes solvent drag across large pores; convective solute drag would move sodium along with water, preventing any concentration drop."
      },
      {
        "q": "The Staverman reflection coefficient ($\\sigma$) quantifies the selectivity of a semipermeable membrane toward a solute. If a membrane exhibits $\\sigma = 0$ for a given solute, how does that solute behave osmotically?",
        "ch": [
          "The solute is completely permeable and generates no effective osmotic pressure",
          "The solute is completely impermeable and exerts maximal theoretical pressure",
          "The solute undergoes unidirectional active transport against chemical gradients",
          "The solute binds irreversibly to endothelial glycocalyx without permeation"
        ],
        "a": 0,
        "e": "<strong>Staverman reflection coefficient and membrane selectivity:</strong> The reflection coefficient $\\sigma$ ranges from 0 to 1 and represents the fraction of solute molecules reflected (excluded) by the pore membrane. When $\\sigma = 0$, the solute is as freely permeable through the pore as water molecules, meaning the membrane offers zero resistance to solute transit. Consequently, no effective hydrostatic-osmotic pressure difference is maintained across the membrane (effective osmotic pressure $\\sigma \\Delta \\Pi = 0$). In contrast, when $\\sigma = 1$, the membrane is completely impermeable to the solute, enabling full expression of the theoretical van 't Hoff osmotic pressure.<br><br><em>Distractor Traps:</em><br>&bull; B describes the condition where $\\sigma = 1.0$ (complete impermeability), confusing the two boundary conditions.<br>&bull; C conflates passive reflection coefficients with active carrier-mediated primary or secondary transport.<br>&bull; D describes surface binding or adsorption rather than membrane permeability."
      },
      {
        "q": "In the 1.5% dextrose trial, the net ultrafiltration rate becomes negative ($-0.8\\text{ mL/min}$) at 240 minutes, causing a net decline in intraperitoneal volume. What biophysical factor drives this reversal of fluid flux?",
        "ch": [
          "Hydrostatic capillary pressure drops below venous pressure, reversing flow",
          "Glucose absorption dissipates the osmotic gradient below lymphatic uptake",
          "Aquaporin-1 channels undergo endocytic internalization after two hours dwell",
          "Active secretion of sodium into peritoneal capillaries draws dialysate water"
        ],
        "a": 1,
        "e": "<strong>Osmotic gradient dissipation and lymphatic fluid reabsorption:</strong> Over the 240-minute dwell, dextrose diffuses down its concentration gradient through small inter-endothelial pores into the peritoneal capillary circulation, dropping the dialysate glucose from 83 mM to 25 mM. As the crystalloid osmotic pressure gradient ($\\Delta \\Pi$) dissipates, the transcapillary ultrafiltration rate diminishes toward zero. Because the subdiaphragmatic and interstitial lymphatic vessels continuously resorb fluid from the peritoneal cavity at a constant rate ($L_R \\approx 1.5\\text{ mL/min}$), net fluid flux ($J_v = \\text{UF} - L_R$) becomes negative, leading to volume reabsorption.<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly claims capillary hydrostatic pressure drops below venous pressure; systemic hemodynamic pressures remain positive.<br>&bull; C invents an endocytic internalization mechanism for constitutive aquaporin-1 channels.<br>&bull; D falsely posits active sodium secretion across peritoneal capillaries driving reverse osmosis."
      },
      {
        "q": "Why does 7.5% icodextrin maintain a stable, positive ultrafiltration rate (+2.1 mL/min) through 240 minutes without inducing an early drop in dialysate sodium concentration (sodium sieving)?",
        "ch": [
          "Icodextrin directly activates primary active sodium-potassium ATPase pumps",
          "Icodextrin crosses endothelial tight junctions through convective bulk flow",
          "Icodextrin acts via colloid osmosis across small pores rather than aquaporins",
          "Icodextrin cleaves into monosaccharide glucose units inside peritoneal fluid"
        ],
        "a": 2,
        "e": "<strong>Colloid osmosis and icodextrin transport kinetics:</strong> Icodextrin is a high-molecular-weight glucose polymer (average $MW \\approx 13{,}000&ndash;19{,}000\\text{ Da}$). Because of its large hydrodynamic radius, icodextrin cannot pass through small endothelial pores and cannot enter ultrasmall aquaporin-1 channels (~0.4 nm). Instead, icodextrin exerts colloid (oncotic) osmosis primarily across the small inter-endothelial pores, which permit simultaneous movement of water and dissolved electrolytes. Because fluid extraction occurs across small pores alongside sodium rather than through solute-free aquaporin channels, sodium sieving does not occur, and ultrafiltration remains steady over long dwell times without rapid solute dissipation.<br><br><em>Distractor Traps:</em><br>&bull; A misattributes colloid osmosis to active enzymatic ATPase pumping.<br>&bull; B claims icodextrin crosses tight junctions via bulk flow; icodextrin is largely retained in the peritoneal cavity due to its size.<br>&bull; D claims icodextrin is hydrolyzed into monosaccharides; if it rapidly cleaved into glucose, it would dissipate quickly and trigger sodium sieving."
      },
      {
        "q": "A patient undergoing continuous peritoneal dialysis develops acute bacterial peritonitis, causing intense peritoneal inflammation and hypervascularity ($L_p S$). How does this condition affect dextrose absorption and ultrafiltration?",
        "ch": [
          "Dextrose absorption slows, maintaining a high osmotic gradient and excess UF",
          "Aquaporin-1 channel density doubles, accelerating sustained free-water flux",
          "Peritoneal lymphatic reabsorption ceases completely, enhancing fluid removal",
          "Dextrose absorption accelerates, prematurely dissipating the osmotic gradient"
        ],
        "a": 3,
        "e": "<strong>Impact of peritoneal inflammation on ultrafiltration kinetics:</strong> Acute peritonitis triggers inflammatory cytokine release, leading to intense peritoneal vasodilation, angiogenesis, and recruitment of perfused peritoneal capillaries. This expands the effective surface area ($S$) and small-pore permeability of the peritoneal membrane. Consequently, dextrose diffuses into the systemic circulation at an abnormally rapid rate. This rapid dissipation of dialysate dextrose prematurely abolishes the transperitoneal osmotic pressure gradient ($\\Delta \\Pi$). Once the osmotic driving force is lost early in the dwell, continuous lymphatic absorption ($L_R$) dominates, causing ultrafiltration failure and fluid overload.<br><br><em>Distractor Traps:</em><br>&bull; A reverses the effect of inflammation on solute permeability, falsely asserting that glucose diffusion slows.<br>&bull; B claims inflammation doubles AQP1 channels; aquaporin expression is not acutely upregulated in peritonitis.<br>&bull; C incorrectly states that lymphatic reabsorption ceases; lymphatic drainage remains active and often increases during inflammation."
      }
    ]
  },
  {
    "id": "exam_cp90_5_p3",
    "sec": "C/P",
    "topic": "Flow Past Bluff Bodies & Drag Coefficient in Blood Filters",
    "sheet": 3,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_5",
    "passage": "<div class=\"ttl\">Passage 3 (Questions 13&ndash;18)</div>\n<p>Inferior vena cava (IVC) filters are deployed endovascularly to intercept and trap lower-extremity deep vein thromboemboli, preventing potentially fatal pulmonary embolism in patients with contraindications to anticoagulation. When deployed inside the IVC lumen, the metallic filter frame (composed of nitinol struts in conical or umbrella configurations) functions hydrodynamically as an immersed bluff body obstructing venous blood flow.</p>\n<p>The total hydrodynamic drag force ($F_D$) exerted by blood flow upon an immersed filter is described by the drag equation:</p>\n<p>$$F_D = \\frac{1}{2} C_D \\rho A v^2$$</p>\n<p>where $C_D$ represents the dimensionless drag coefficient, $\\rho$ is the mass density of whole blood ($\\rho \\approx 1060\\text{ kg/m}^3$), $A$ is the projected frontal area perpendicular to blood flow, and $v$ is the mean upstream blood velocity (normally 0.10&ndash;0.25 m/s in the human infrarenal IVC).</p>\n<p>Total hydrodynamic drag comprises two primary components:</p>\n<p>1. <em>Form (pressure) drag</em>: Arising from an upstream-to-downstream pressure differential caused by flow separation and boundary layer detachment, creating a wide, turbulent, low-pressure wake downstream of the body.</p>\n<p>2. <em>Skin friction drag</em>: Tangential viscous shear stresses exerted along the wetted surface of the struts, governed by dynamic blood viscosity ($\\mu \\approx 3.50\\text{ mPa}\\cdot\\text{s}$).</p>\n<p>The flow regime is characterized by the dimensionless Reynolds number:</p>\n<p>$$Re = \\frac{\\rho v D}{\\mu}$$</p>\n<p>where $D$ represents the characteristic dimension (the caval lumen diameter). When an IVC filter captures a large thromboembolus, the trapped clot markedly increases the effective frontal area and alters flow geometry from slender struts into an acute bluff body, escalating mechanical drag on anchoring barbs. Biomedical engineers evaluated three IVC filter prototypes in an IVC phantom ($D = 20\\text{ mm}$, $\\rho = 1060\\text{ kg/m}^3$, $\\mu = 3.50\\text{ mPa}\\cdot\\text{s}$) at an inflow velocity of $v = 0.20\\text{ m/s}$ (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Projected area, drag coefficients, measured drag force, and peak shear stresses</caption>\n  <thead>\n    <tr><th>Filter Design</th><th>Thrombus Status</th><th>Projected Area $A$ ($\\text{mm}^2$)</th><th>Drag Coeff $C_D$</th><th>Measured Drag Force $F_D$ (mN)</th><th>Peak Wall Shear Stress (Pa)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td rowspan=\"2\">Conical (Filter A)</td><td>Clean (Unloaded)</td><td>8.0</td><td>0.95</td><td>0.16</td><td>1.8</td></tr>\n    <tr><td>Trapped Clot (50% Clot)</td><td>80.0</td><td>1.45</td><td>2.46</td><td>5.2</td></tr>\n    <tr><td rowspan=\"2\">Umbrella (Filter B)</td><td>Clean (Unloaded)</td><td>12.0</td><td>1.10</td><td>0.28</td><td>2.4</td></tr>\n    <tr><td>Trapped Clot (50% Clot)</td><td>95.0</td><td>1.60</td><td>3.22</td><td>6.8</td></tr>\n    <tr><td rowspan=\"2\">TrapEase (Filter C)</td><td>Clean (Unloaded)</td><td>10.0</td><td>0.85</td><td>0.18</td><td>1.6</td></tr>\n    <tr><td>Trapped Clot (50% Clot)</td><td>85.0</td><td>1.30</td><td>2.34</td><td>4.9</td></tr>\n  </tbody>\n</table>\n<p>Engineers evaluate whether elevated drag forces following clot capture risk cephalad migration or vena cava perforation.</p>",
    "qs": [
      {
        "q": "Using the parameters in Table 1 for the unloaded Conical Filter A ($A = 8.0\\text{ mm}^2 = 8.0 \\times 10^{-6}\\text{ m}^2$, $C_D = 0.95$, $\\rho = 1060\\text{ kg/m}^3$, $v = 0.20\\text{ m/s}$), what is the calculated hydrodynamic drag force?",
        "ch": [
          "0.16 mN",
          "0.80 mN",
          "1.61 mN",
          "3.22 mN"
        ],
        "a": 0,
        "e": "<strong>Hydrodynamic drag force calculation:</strong> The drag force equation is $F_D = \\frac{1}{2} C_D \\rho A v^2$. Converting the parameters to standard SI units: $C_D = 0.95$, $\\rho = 1060\\text{ kg/m}^3$, $A = 8.0 \\times 10^{-6}\\text{ m}^2$, and $v = 0.20\\text{ m/s}$. Substituting these values gives $F_D = 0.5 \\times 0.95 \\times 1060\\text{ kg/m}^3 \\times (8.0 \\times 10^{-6}\\text{ m}^2) \\times (0.20\\text{ m/s})^2 = 503.5 \\times 8.0 \\times 10^{-6} \\times 0.04 = 1.6112 \\times 10^{-4}\\text{ N} = 0.161\\text{ mN} \\approx 0.16\\text{ mN}$. This confirms the measured force reported in Table 1.<br><br><em>Distractor Traps:</em><br>&bull; B (0.80 mN) forgets to square the velocity term, multiplying by $v = 0.20$ rather than $v^2 = 0.04$.<br>&bull; C (1.61 mN) misplaces the decimal place by a factor of 10 during the millimeter-to-meter conversion ($10^{-5}$ instead of $10^{-6}$).<br>&bull; D (3.22 mN) omits the factor of $1/2$ in the drag equation and misplaces a decimal place."
      },
      {
        "q": "What is the Reynolds number ($Re$) for venous blood flow in the IVC phantom ($D = 20\\text{ mm} = 0.020\\text{ m}$) under baseline experimental conditions ($v = 0.20\\text{ m/s}$, $\\rho = 1060\\text{ kg/m}^3$, $\\mu = 3.50 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}$), and what flow regime does it reflect?",
        "ch": [
          "Re = 380; deeply turbulent flow dominated by fluid kinetic forces",
          "Re = 1210; predominantly laminar flow dominated by viscous forces",
          "Re = 2450; fully turbulent flow characterized by vortex shedding",
          "Re = 6050; supersonic shock boundary layer separation in the cava"
        ],
        "a": 1,
        "e": "<strong>Reynolds number calculation and flow regime determination:</strong> The Reynolds number is given by $Re = \\frac{\\rho v D}{\\mu}$. Substituting the values: $Re = \\frac{(1060\\text{ kg/m}^3)(0.20\\text{ m/s})(0.020\\text{ m})}{3.50 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}} = \\frac{4.24}{0.00350} = 1211.4 \\approx 1210$. For internal pipe flow (such as venous blood flow in a large blood vessel), the critical Reynolds number for turbulent transition is approximately 2000. Because $Re \\approx 1210 < 2000$, the flow is subcritical and predominantly laminar, where viscous forces dampen small perturbations.<br><br><em>Distractor Traps:</em><br>&bull; A (380) uses an incorrect viscosity or diameter and mischaracterizes low Re flow as turbulent.<br>&bull; C (2450) claims the flow is above 2000 and fully turbulent, which represents post-critical flow.<br>&bull; D (6050) miscalculates the fraction by orders of magnitude and inappropriately invokes supersonic compressibility effects."
      },
      {
        "q": "When a thromboembolus is captured by an IVC filter, form (pressure) drag becomes the primary component of total drag. What biophysical phenomenon drives the sharp increase in form drag behind the trapped clot?",
        "ch": [
          "Rapid suppression of downstream boundary layer velocity detachment",
          "Direct conversion of mechanical flow work into acoustic cavitation",
          "Boundary layer separation creating an adverse low-pressure wake zone",
          "Sharp reduction in upstream stagnation pressure facing leading edges"
        ],
        "a": 2,
        "e": "<strong>Fluid mechanics of boundary layer separation and form drag:</strong> Form (pressure) drag arises from the net imbalance between high dynamic pressure at the upstream stagnation point of a body and low static pressure in the downstream wake. In a streamlined body, fluid streamlines stay attached to the contours. In contrast, when blood encounters a bluff, blunt object like a trapped clot, the adverse pressure gradient forces the boundary layer to detach (flow separation). This separation produces an extensive recirculating, turbulent wake with markedly depressed hydrostatic pressure downstream. The resulting forward-to-backward pressure differential pushes forcefully against the clot, driving the dramatic escalation in $F_D$.<br><br><em>Distractor Traps:</em><br>&bull; A claims flow separation is suppressed, whereas detachment is actually triggered by the bluff geometry.<br>&bull; B mentions acoustic cavitation, which requires high-intensity ultrasound waves and does not occur in low-speed venous hemodynamics.<br>&bull; D falsely claims upstream stagnation pressure drops; upstream stagnation pressure actually remains high ($P_0 = P + \\frac{1}{2}\\rho v^2$)."
      },
      {
        "q": "During a hyperdynamic circulatory state (e.g., severe sepsis), mean caval blood velocity doubles from $0.20\\text{ m/s}$ to $0.40\\text{ m/s}$. Assuming frontal area and drag coefficient remain constant, by what factor does the drag force on the clot-laden filter increase?",
        "ch": [
          "A factor of 1.41",
          "A factor of 2.00",
          "A factor of 3.00",
          "A factor of 4.00"
        ],
        "a": 3,
        "e": "<strong>Quadratic velocity dependence of hydrodynamic drag:</strong> The hydrodynamic drag equation explicitly shows that drag force is proportional to the square of flow velocity: $F_D \\propto v^2$. If velocity doubles ($v' = 2v$), the new drag force is $F_D' = \\frac{1}{2} C_D \\rho A (2v)^2 = 4 \\left(\\frac{1}{2} C_D \\rho A v^2\\right) = 4 F_D$. Thus, doubling blood velocity quadruples the hydrodynamic drag force (a factor of $2^2 = 4.00$). This quadratic surge substantially increases mechanical stress on anchoring struts and wall barbs, elevating the risk of filter tilt or migration during sepsis.<br><br><em>Distractor Traps:</em><br>&bull; A takes the square root of 2 ($\\sqrt{2} \\approx 1.41$), inverting the quadratic relationship.<br>&bull; B assumes a direct linear dependence between velocity and drag ($F_D \\propto v$), failing to square the velocity.<br>&bull; C introduces an arbitrary factor of 3."
      },
      {
        "q": "Table 1 shows that peak wall shear stress reaches 6.8 Pa surrounding the trapped clot in Filter B. Why is elevated shear stress clinically concerning in endovascular filter deployments?",
        "ch": [
          "It triggers irreversible enzymatic degradation of circulating albumin",
          "It uncoils von Willebrand factor, inducing secondary clot formation",
          "It abolishes endothelial nitric oxide release by denaturing cadherins",
          "It causes profound erythrocyte hyperpolarization and rapid crenation"
        ],
        "a": 1,
        "e": "<strong>Shear-induced platelet activation and thrombogenesis:</strong> Blood is a non-Newtonian suspension of cells, and hemodynamic shear stresses play a critical regulatory role in hemostasis. High shear stresses ($> 5-10\\text{ Pa}$) near the narrowed flow passages surrounding a trapped thrombus cause the high-molecular-weight multimers of von Willebrand factor (vWF) to uncoil from a globular to an elongated conformation. This conformational transition exposes A1 domains, promoting vigorous binding to platelet glycoprotein Ib-IX-V complexes, triggering shear-induced platelet activation and secondary in situ thrombotic occlusion of the filter and vena cava.<br><br><em>Distractor Traps:</em><br>&bull; A claims mechanical shear enzymatically degrades albumin; hydrodynamic shear does not denature or cleave albumin peptide bonds.<br>&bull; C claims high shear abolishes nitric oxide release; actually, physiological shear stress stimulates endothelial nitric oxide synthase (eNOS) to increase NO production.<br>&bull; D invents an electrical hyperpolarization mechanism causing erythrocyte crenation."
      },
      {
        "q": "How does streamlining an IVC filter strut's cross-sectional geometry (e.g., transitioning from a blunt square cross-section to an elliptical foil profile) decrease its form drag coefficient $C_D$?",
        "ch": [
          "By maximizing boundary layer friction drag along wetted strut boundaries",
          "By converting downstream laminar streamlines into wide turbulent eddies",
          "By delaying boundary layer separation and narrowing the low-pressure wake",
          "By decreasing upstream stagnation pressure below downstream static levels"
        ],
        "a": 2,
        "e": "<strong>Aerodynamic streamlining and wake reduction:</strong> A blunt or square bluff body forces rapid boundary layer detachment at its sharp upstream corners, generating an expansive, chaotic low-pressure wake with high form drag. In contrast, streamlining the cross-section into a smooth elliptical or tear-drop foil profile creates a gentle favorable and unfavorable pressure gradient contour. This allows the boundary layer to remain attached much further along the body's length (delaying flow separation). Consequently, the downstream low-pressure wake is significantly narrowed, pressure recovery is achieved along the trailing edge, and the form drag coefficient ($C_D$) drops markedly.<br><br><em>Distractor Traps:</em><br>&bull; A claims increasing skin friction is the goal; streamlining minimizes total drag even if wetted surface area slightly increases.<br>&bull; B describes promoting wide turbulent eddies, which is the defining feature of high-drag bluff bodies.<br>&bull; D violates conservation of energy (Bernoulli's principle); upstream stagnation pressure cannot drop below downstream static pressure in a flow obstruction."
      }
    ]
  },
  {
    "id": "exam_cp90_5_p4",
    "sec": "C/P",
    "topic": "Capillary Refill Time as a Clinical Fluid Dynamic Index",
    "sheet": 4,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_5",
    "passage": "<div class=\"ttl\">Passage 4 (Questions 19&ndash;24)</div>\n<p>Capillary refill time (CRT) is an established bedside physical index of peripheral microvascular perfusion, defined as the duration required for skin erythema to return to the digital pulp following 5 seconds of sustained blanching pressure. Normal physiological CRT in normothermic adults is $\\le 2.0\\text{ seconds}$; prolonged CRT ($> 3.0\\text{ seconds}$) is a sensitive physical hallmark of shock and peripheral hypoperfusion.</p>\n<p>The fluid mechanics of microvascular reperfusion following blanching compression can be modeled using the Hagen-Poiseuille law for laminar viscous fluid flow through cylindrical vascular beds:</p>\n<p>$$Q = \\frac{\\Delta P \\cdot \\pi r^4}{8 \\eta L}$$</p>\n<p>where $Q$ is volumetric blood flow rate, $\\Delta P$ is the effective arteriolar-to-venular perfusion pressure gradient ($\\Delta P = P_{\\text{art}} - P_{\\text{ven}}$), $r$ is internal vessel radius, $\\eta$ is dynamic blood viscosity, and $L$ is microvascular path length. Microvascular hydraulic resistance ($R$) is defined as:</p>\n<p>$$R = \\frac{\\Delta P}{Q} = \\frac{8 \\eta L}{\\pi r^4}$$</p>\n<p>Because hydraulic resistance scales inversely with the fourth power of radius ($R \\propto r^{-4}$), neurohumoral sympathetic vasoconstriction mediated by $\\alpha_1$-adrenergic receptor stimulation drastically increases peripheral resistance, reducing volumetric refilling rate and prolonging CRT.</p>\n<p>Furthermore, microvascular refilling follows an exponential trajectory analogous to a charging resistor-capacitor ($RC$) circuit:</p>\n<p>$$\\Delta V(t) = \\Delta V_{\\text{max}} \\left( 1 - e^{-t / \\tau} \\right)$$</p>\n<p>where $\\tau = R \\cdot C$ represents the hydraulic time constant and $C = \\Delta V / \\Delta P$ is microvascular vascular compliance. Quantitative optical photoplethysmography (PPG) at 660 nm and 940 nm recorded CRT profiles across four circulatory cohorts (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Hemodynamic parameters, microvascular resistance, and quantitative CRT across clinical cohorts</caption>\n  <thead>\n    <tr><th>Clinical Cohort</th><th>Mean Arterial Pressure (mmHg)</th><th>Relative Arteriolar Radius ($r / r_0$)</th><th>Blood Viscosity $\\eta$ ($\\text{mPa}\\cdot\\text{s}$)</th><th>Relative Resistance ($R / R_0$)</th><th>Quantitative CRT (s)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Normotensive Control</td><td>92</td><td>1.00</td><td>3.50</td><td>1.00</td><td>1.45</td></tr>\n    <tr><td>Hypovolemic Shock</td><td>64</td><td>0.70</td><td>3.50</td><td>4.16</td><td>4.85</td></tr>\n    <tr><td>Septic Shock (Early Hyperdynamic)</td><td>65</td><td>1.25</td><td>3.20</td><td>0.37</td><td>0.95</td></tr>\n    <tr><td>Hypothermic Vasoconstriction ($32^\\circ\\text{C}$)</td><td>90</td><td>0.75</td><td>4.60</td><td>4.15</td><td>4.70</td></tr>\n  </tbody>\n</table>\n<p>Investigators evaluate whether core rewarming restores baseline microvascular filling kinetics in hypothermic shock patients.</p>",
    "qs": [
      {
        "q": "In the Hypovolemic Shock cohort, precapillary arteriolar radius decreases to $r = 0.70\\ r_0$ due to intense sympathetic vasoconstriction. According to the Hagen-Poiseuille law, what is the expected fold increase in hydraulic resistance ($R / R_0$)?",
        "ch": [
          "A factor of 1.43",
          "A factor of 2.04",
          "A factor of 2.86",
          "A factor of 4.16"
        ],
        "a": 3,
        "e": "<strong>Fourth-power radius dependence in Poiseuille resistance:</strong> The Hagen-Poiseuille equation dictates that vascular resistance is inversely proportional to the fourth power of vessel radius ($R \\propto 1/r^4$). When arteriolar radius contracts to $0.70\\ r_0$, the new resistance relative to baseline is $R / R_0 = \\frac{1}{(0.70)^4} = \\frac{1}{0.2401} \\approx 4.164$. Thus, even a modest 30% reduction in vascular caliber produces an extraordinary 4.16-fold increase in hydraulic resistance, sharply diminishing downstream capillary blood flow and significantly prolonging refill time.<br><br><em>Distractor Traps:</em><br>&bull; A (1.43) assumes an inverse linear relationship between resistance and radius ($1/0.70 \\approx 1.43$).<br>&bull; B (2.04) assumes an inverse square relationship ($1/0.70^2 = 1/0.49 \\approx 2.04$), confusing Poiseuille resistance with cross-sectional area.<br>&bull; C (2.86) uses an inverse cube relationship ($1/0.70^3 = 1/0.343 \\approx 2.91$ with slight rounding error)."
      },
      {
        "q": "The microvascular reperfusion time constant is defined as $\\tau = R \\cdot C$. If precapillary vasoconstriction quadruples hydraulic resistance ($R$) while microvascular compliance ($C$) remains constant, how is the time constant $\\tau$ altered?",
        "ch": [
          "The time constant quadruples, prolonging the duration of capillary refilling",
          "The time constant is quartered, accelerating the rate of capillary refilling",
          "The time constant doubles, producing negligible alteration in refill curves",
          "The time constant remains unchanged because compliance buffers resistance shift"
        ],
        "a": 0,
        "e": "<strong>Hydraulic time constant and resistance scaling:</strong> In a fluidic $RC$ circuit, the time constant $\\tau = R \\cdot C$ represents the characteristic time required for the vascular bed to fill to approximately $63.2\\%$ of its maximal reperfusion capacity ($1 - e^{-1} \\approx 0.632$). Because $\\tau$ is directly proportional to hydraulic resistance ($R$), a four-fold increase in resistance ($R' = 4R$) quadruples the time constant ($\\tau' = 4\\tau$). A larger time constant means that the rate of blood volume accumulation slows dramatically, directly prolonging the observed capillary refill time.<br><br><em>Distractor Traps:</em><br>&bull; B inverts the relationship, erroneously predicting that higher resistance speeds up refill.<br>&bull; C assumes a square-root dependence ($\\tau \\propto \\sqrt{R}$), which does not apply to linear first-order systems.<br>&bull; D falsely claims that constant compliance buffers or cancels the resistance increase."
      },
      {
        "q": "In the hypothermic cohort ($32^\\circ\\text{C}$), dynamic blood viscosity increases from $3.50\\text{ mPa}\\cdot\\text{s}$ to $4.60\\text{ mPa}\\cdot\\text{s}$. What physical mechanism explains this inverse relationship between fluid temperature and dynamic viscosity?",
        "ch": [
          "Elevated thermal kinetic energy enhances intermolecular cohesive bonds in fluid",
          "Reduced thermal kinetic energy allows intermolecular cohesive forces to dominate",
          "Thermal contraction of erythrocytes decreases overall cellular packing density",
          "Hypothermia accelerates fibrinogen polymerization into macro-fibrin polymers"
        ],
        "a": 1,
        "e": "<strong>Temperature dependence of liquid dynamic viscosity:</strong> In liquids and complex aqueous suspensions like blood, viscosity is determined by the balance between thermal kinetic energy and intermolecular cohesive forces. As temperature decreases, the average kinetic energy of water molecules and suspended plasma proteins decreases ($KE_{\\text{avg}} = \\frac{3}{2} k_B T$). With reduced thermal motion, attractive intermolecular forces and hydrogen bonding networks hold molecules together more tightly, increasing the internal friction resisting fluid shear. This causes blood dynamic viscosity to rise significantly during hypothermia, independently increasing microvascular resistance.<br><br><em>Distractor Traps:</em><br>&bull; A claims elevated kinetic energy increases cohesive bonding; increased kinetic energy actually disrupts cohesive bonds.<br>&bull; C incorrectly claims erythrocyte thermal contraction decreases packing density; hematocrit and erythrocyte rigidity actually rise with cooling.<br>&bull; D refers to fibrinogen clotting cascade activation, which is an enzymatic process that is actually slowed down by hypothermia."
      },
      {
        "q": "Table 1 demonstrates that patients in Early Hyperdynamic Septic Shock exhibit an abnormally rapid CRT (0.95 s, 'flash capillary refill'). Which hemodynamic alteration directly produces this physical finding?",
        "ch": [
          "Profound systemic arteriolar vasoconstriction driven by angiotensin II",
          "Marked hemoconcentration elevating postcapillary venular resistance",
          "Pathological systemic vasodilation markedly decreasing vascular resistance",
          "Complete mechanical occlusion of precapillary metarteriole sphincters"
        ],
        "a": 2,
        "e": "<strong>Hyperdynamic distributive vasodilation and flash capillary refill:</strong> Early septic shock is characterized by severe distributive shock. Inflammatory cytokines induce widespread nitric oxide synthesis and endothelial dysfunction, causing profound peripheral arteriolar vasodilation ($r / r_0 = 1.25$). According to Poiseuille's law, this dilated radius reduces relative hydraulic resistance dramatically to $0.37$ of baseline ($R \\propto 1/r^4$). With extremely low precapillary resistance and preserved initial cardiac output, capillary perfusion occurs under minimal viscous impedance, yielding an accelerated, flash refill ($< 1.0\\text{ s}$).<br><br><em>Distractor Traps:</em><br>&bull; A describes intense vasoconstriction, which occurs in hypovolemic or cardiogenic shock and causes prolonged CRT.<br>&bull; B describes increased venular resistance, which would impede drainage and capillary flow.<br>&bull; D describes complete sphincter occlusion, which would abolish capillary flow altogether."
      },
      {
        "q": "A clinician measures CRT with the patient's hand elevated 50 cm above heart level, versus resting at heart level. Assuming unchanged arteriolar radius, how does this limb elevation alter CRT, and via what physical principle?",
        "ch": [
          "CRT decreases because gravity accelerates arterial inflow down pressure paths",
          "CRT remains identical because vascular autoregulation perfectly resets flow",
          "CRT decreases because reduced hydrostatic pressure widens microvascular beds",
          "CRT prolongs because reduced hydrostatic pressure lowers local perfusion head"
        ],
        "a": 3,
        "e": "<strong>Hydrostatic pressure gradients and local perfusion pressure:</strong> Hydrostatic fluid column pressure is defined by $\\Delta P_h = \\rho g h$. Elevating the extremity 50 cm ($0.50\\text{ m}$) above the level of the right atrium introduces a negative hydrostatic column head: $\\Delta P_h = (1060\\text{ kg/m}^3)(9.8\\text{ m/s}^2)(0.50\\text{ m}) \\approx 5194\\text{ Pa} \\approx 39\\text{ mmHg}$. This hydrostatic reduction lowers local precapillary arterial pressure and effective perfusion pressure ($\\Delta P = P_{\\text{art}} - P_{\\text{ven}}$). Because volumetric flow is directly proportional to driving pressure ($Q = \\Delta P / R$), flow decreases, prolonging capillary refill time.<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly claims gravity accelerates arterial flow into an elevated limb; gravity actually opposes arterial ascent.<br>&bull; B claims autoregulation completely eliminates any hydrostatic effect, which is clinically false during acute positional challenges.<br>&bull; C falsely claims reducing hydrostatic pressure widens microvessels; lower transmural pressure actually promotes passive vascular recoil/narrowing."
      },
      {
        "q": "The quantitative optical sensor determines reperfusion by monitoring light absorption at 660 nm and 940 nm. According to the Beer-Lambert law ($A = \\varepsilon c l$), why does light absorption at 940 nm increase sharply as capillary refilling proceeds?",
        "ch": [
          "Inflowing oxygenated hemoglobin absorbs strongly at near-infrared 940 nm light",
          "Optical path length through dermal tissue decreases during vascular engorgement",
          "Interstitial edema clears from the subcutaneous space, reducing light scatter",
          "Deoxygenated hemoglobin selectively accumulates at the venular microcapillaries"
        ],
        "a": 0,
        "e": "<strong>Spectrophotometric detection and Beer-Lambert absorption of hemoglobin:</strong> The Beer-Lambert law states that absorbance is proportional to molar absorptivity, concentration, and path length: $A = \\varepsilon c l$. Oxyhemoglobin ($\\text{HbO}_2$) possesses a high extinction coefficient at near-infrared wavelengths (940 nm), whereas deoxygenated hemoglobin ($\\text{Hb}$) absorbs predominantly in the visible red spectrum (660 nm). During blanching compression, capillary blood is extruded. As the blanching force is released, fresh arterial blood rich in oxyhemoglobin rushes back into the microvascular lumen, sharply increasing the effective concentration $c$ of $\\text{HbO}_2$ and increasing optical absorbance at 940 nm.<br><br><em>Distractor Traps:</em><br>&bull; B claims optical path length decreases; vascular engorgement actually expands blood vessel volume, which would slightly increase path length through blood.<br>&bull; C claims edema clears during the two seconds of refill, which is physiologically impossible on subsecond timescales.<br>&bull; D asserts deoxygenated hemoglobin accumulates, which contradicts the influx of oxygenated arterial inflow."
      }
    ]
  },
  {
    "id": "exam_cp90_5_p5",
    "sec": "C/P",
    "topic": "Tracheobronchial Airway Branching & Fractal Flow Resistance",
    "sheet": 5,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_5",
    "passage": "<div class=\"ttl\">Passage 5 (Questions 25&ndash;30)</div>\n<p>The human tracheobronchial tree features an asymmetrical dichotomous branching architecture comprising approximately 23 generations ($z=0$ to $z=23$) descending from the trachea to microscopic alveolar sacs. According to the Weibel symmetric morphometric lung model:</p>\n<p>1. <em>Conducting Zone (Generations 0&ndash;16)</em>: Encompassing the trachea ($z=0$), mainstem and lobar bronchi, and terminal bronchioles ($z=16$). These conduits facilitate bulk convective gas transport and constitute the anatomical dead space (~150 mL).</p>\n<p>2. <em>Respiratory Zone (Generations 17&ndash;23)</em>: Encompassing respiratory bronchioles, alveolar ducts, and alveolar sacs, where alveolar-capillary gas exchange takes place.</p>\n<p>Gas transport through this fractal airway network exhibits a fundamental fluid dynamic paradox. By the principle of continuity for incompressible fluid flow:</p>\n<p>$$Q = A_{\\text{total}} \\cdot v_{\\text{mean}}$$</p>\n<p>where $Q$ is volumetric flow rate (typically $500\\text{ cm}^3/\\text{s}$ or $0.50\\text{ L/s}$ during quiet inspiration), $A_{\\text{total}} = N_z \\cdot \\frac{\\pi d_z^2}{4}$ is the aggregate cross-sectional area across all $N_z = 2^z$ parallel branches in generation $z$, and $v_{\\text{mean}}$ is the mean linear gas velocity.</p>\n<p>Although individual branch diameter ($d_z$) diminishes progressively, the geometric doubling of parallel conduits ($N_z = 2^z$) causes the total aggregate cross-sectional area to expand exponentially from $2.5\\text{ cm}^2$ in the trachea to over $10{,}000\\text{ cm}^2$ in terminal airspaces. According to the equivalent resistance formula for parallel conduits:</p>\n<p>$$\\frac{1}{R_{\\text{total}}} = \\sum_{i=1}^{N_z} \\frac{1}{R_i}$$</p>\n<p>Because millions of narrow bronchioles operate in parallel, peripheral airways contribute less than 20% of total pulmonary resistance. The maximum airflow resistance in a healthy lung resides in generations 3 to 5 (medium-sized segmental bronchi). Morphometric and hemodynamic parameters across seven generations are shown in Table 1.</p>\n<table class=\"tbl\">\n  <caption>Table 1 Airway branching generations, aggregate area, gas velocity, and segmental resistance</caption>\n  <thead>\n    <tr><th>Airway Generation ($z$)</th><th>Structure Type</th><th>Branch Count ($N_z$)</th><th>Single Caliber $d_z$ (mm)</th><th>Aggregate Area $A_{\\text{total}}$ ($\\text{cm}^2$)</th><th>Mean Velocity $v$ (cm/s)</th><th>Segmental Resistance ($\\text{cm H}_2\\text{O}/(\\text{L/s})$)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Gen 0</td><td>Trachea</td><td>1</td><td>18.0</td><td>2.5</td><td>200.0</td><td>0.20</td></tr>\n    <tr><td>Gen 2</td><td>Lobar Bronchi</td><td>4</td><td>8.3</td><td>2.2</td><td>227.3</td><td>0.35</td></tr>\n    <tr><td>Gen 4</td><td>Segmental Bronchi</td><td>16</td><td>4.5</td><td>2.5</td><td>200.0</td><td>0.65</td></tr>\n    <tr><td>Gen 8</td><td>Small Bronchi</td><td>256</td><td>1.4</td><td>3.9</td><td>128.2</td><td>0.30</td></tr>\n    <tr><td>Gen 12</td><td>Terminal Bronchioles</td><td>4096</td><td>0.6</td><td>11.6</td><td>43.1</td><td>0.12</td></tr>\n    <tr><td>Gen 16</td><td>Transitional Bronchioles</td><td>65,536</td><td>0.4</td><td>82.3</td><td>6.1</td><td>0.04</td></tr>\n    <tr><td>Gen 20</td><td>Alveolar Ducts</td><td>1,048,576</td><td>0.3</td><td>741.0</td><td>0.67</td><td>0.01</td></tr>\n  </tbody>\n</table>\n<p>Researchers evaluate whether bronchodilators selectively reduce airway resistance in segmental versus peripheral generations.</p>",
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
  },
  {
    "id": "exam_cp90_5_p6",
    "sec": "C/P",
    "topic": "Venturi Effect & Bronchodilator Jet Nebulizer Physics",
    "sheet": 6,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_5",
    "passage": "<div class=\"ttl\">Passage 6 (Questions 31&ndash;36)</div>\n<p>Pneumatic jet nebulizers are clinical aerosol delivery devices used to administer inhaled bronchodilators (e.g., albuterol sulfate and ipratropium bromide) to patients experiencing acute bronchospasm during asthma or COPD exacerbations. The operation of a jet nebulizer exploits Bernoulli's principle and the Venturi effect to entrain liquid medication from a reservoir and disperse it into respirable micro-droplets.</p>\n<p>In a jet nebulizer, compressed driving gas (medical air or oxygen, $\\rho \\approx 1.20\\text{ kg/m}^3$) is forced at a high flow rate ($Q = 6.0&ndash;8.0\\text{ L/min}$) through a narrow nozzle constriction. By the continuity equation ($A_1 v_1 = A_2 v_2$), this constriction accelerates the driving gas to high linear velocities ($v_2 > 80\\text{ m/s}$).</p>\n<p>Assuming horizontal inviscid gas flow, Bernoulli's equation dictates:</p>\n<p>$$P_1 + \\frac{1}{2}\\rho v_1^2 = P_2 + \\frac{1}{2}\\rho v_2^2$$</p>\n<p>The acceleration of gas through the nozzle produces a localized pressure drop ($P_2 < P_{\\text{atm}}$), creating a sub-atmospheric zone directly adjacent to a vertical capillary feed tube immersed in the liquid medication reservoir. The hydrostatic pressure differential between ambient atmospheric pressure acting on the open reservoir surface ($P_{\\text{atm}}$) and the low pressure at the jet tip ($P_2$) drives liquid upward through the feed tube into the gas stream.</p>\n<p>Upon exiting the capillary orifice, high-velocity gas shear stresses shatter the liquid column into primary aerosol droplets. This primary spray impacts an internal plastic baffle. Droplets with high inertia&mdash;characterized by large Stokes numbers ($Stk \\propto d_p^2$)&mdash;collide with the baffle and drain back into the reservoir. Fine aerosol droplets possessing a Mass Median Aerodynamic Diameter (MMAD) between $1.0\\ \\mu\\text{m}$ and $5.0\\ \\mu\\text{m}$ remain suspended in the streamlines and exit into the patient's breathing circuit. Investigators tested four nozzle geometries at $Q = 6.0\\text{ L/min} = 1.0 \\times 10^{-4}\\text{ m}^3/\\text{s}$ with 0.5% albuterol sulfate solution (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Nozzle diameter, jet velocity, Venturi pressure drop, entrainment, and aerosol MMAD</caption>\n  <thead>\n    <tr><th>Nozzle Design</th><th>Orifice Diameter $d_2$ (mm)</th><th>Orifice Area $A_2$ ($\\text{mm}^2$)</th><th>Gas Jet Velocity $v_2$ (m/s)</th><th>Venturi Pressure Drop $\\Delta P$ (kPa)</th><th>Liquid Entrainment (mL/min)</th><th>Aerosol MMAD ($\\mu\\text{m}$)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Nozzle A</td><td>1.20</td><td>1.13</td><td>88.5</td><td>4.7</td><td>0.18</td><td>5.8</td></tr>\n    <tr><td>Nozzle B</td><td>0.80</td><td>0.50</td><td>200.0</td><td>24.0</td><td>0.38</td><td>3.2</td></tr>\n    <tr><td>Nozzle C</td><td>0.60</td><td>0.28</td><td>357.1</td><td>76.5</td><td>0.62</td><td>2.1</td></tr>\n    <tr><td>Nozzle D</td><td>0.50</td><td>0.20</td><td>500.0</td><td>150.0</td><td>0.85</td><td>1.6</td></tr>\n  </tbody>\n</table>\n<p>Investigators evaluate whether reducing driving gas temperature modifies droplet evaporation and drug concentration in the inhaled mist.</p>",
    "qs": [
      {
        "q": "Using Bernoulli's equation with air density $\\rho = 1.20\\text{ kg/m}^3$ and assuming upstream gas velocity is negligible ($v_1 \\approx 0$), what theoretical pressure drop ($\\Delta P = P_1 - P_2$) is generated by Nozzle B when jet velocity reaches $v_2 = 200.0\\text{ m/s}$?",
        "ch": [
          "24.0 kPa",
          "12.0 kPa",
          "48.0 kPa",
          "96.0 kPa"
        ],
        "a": 0,
        "e": "<strong>Bernoulli equation and Venturi pressure drop calculation:</strong> Bernoulli's equation for horizontal streamline flow states that $P_1 + \\frac{1}{2}\\rho v_1^2 = P_2 + \\frac{1}{2}\\rho v_2^2$. Assuming upstream velocity is negligible ($v_1 \\approx 0$), the pressure drop is given by $\\Delta P = P_1 - P_2 = \\frac{1}{2}\\rho v_2^2$. Substituting $\\rho = 1.20\\text{ kg/m}^3$ and $v_2 = 200.0\\text{ m/s}$: $\\Delta P = \\frac{1}{2}(1.20\\text{ kg/m}^3)(200.0\\text{ m/s})^2 = 0.60 \\times 40{,}000\\text{ Pa} = 24{,}000\\text{ Pa} = 24.0\\text{ kPa}$. This sub-atmospheric pressure drop generates the suction head required to draw liquid drug from the reservoir.<br><br><em>Distractor Traps:</em><br>&bull; B (12.0 kPa) erroneously divides by an extra factor of 2 or forgets to square the velocity correctly.<br>&bull; C (48.0 kPa) omits the factor of $1/2$ in the kinetic energy term, calculating $\\rho v_2^2$.<br>&bull; D (96.0 kPa) multiplies the result by 4 or uses a velocity of 400 m/s."
      },
      {
        "q": "If the nozzle orifice diameter of a pneumatic nebulizer is halved while maintaining a constant volumetric driving flow rate ($Q$), by what factor does the exit gas velocity increase?",
        "ch": [
          "A factor of 2.00",
          "A factor of 4.00",
          "A factor of 8.00",
          "A factor of 16.0"
        ],
        "a": 1,
        "e": "<strong>Continuity equation and inverse-square diameter dependence:</strong> Volumetric flow rate is given by $Q = A \\cdot v$. For a circular orifice of diameter $d$, the cross-sectional area is $A = \\frac{\\pi d^2}{4}$, meaning $A \\propto d^2$. If the diameter is halved ($d' = d/2$), the new cross-sectional area is reduced by a factor of 4: $A' = \\frac{\\pi (d/2)^2}{4} = \\frac{A}{4}$. To maintain a constant volumetric flow rate ($Q = A v = A' v'$), the exit velocity must increase by the reciprocal factor: $v' = \\frac{Q}{A'} = 4 \\left(\\frac{Q}{A}\\right) = 4v$. Thus, exit velocity increases by a factor of $2^2 = 4.00$.<br><br><em>Distractor Traps:</em><br>&bull; A assumes an inverse linear relationship between diameter and velocity ($v \\propto 1/d$).<br>&bull; C introduces an inverse cubic relationship ($v \\propto 1/d^3$).<br>&bull; D squares the area factor, assuming an inverse fourth-power relationship ($v \\propto 1/d^4$)."
      },
      {
        "q": "What is the fundamental physical driving force responsible for lifting the liquid medication upward through the capillary feed tube in a jet nebulizer?",
        "ch": [
          "Electrostatic attraction between polarized water dipoles and nozzle walls",
          "Thermal capillary convection driven by frictional gas heating at the exit",
          "Pressure gradient between atmospheric pressure and sub-atmospheric jet exit",
          "Osmotic diffusion across the concentration gradient within reservoir fluid"
        ],
        "a": 2,
        "e": "<strong>Venturi suction mechanism and fluid entrainment:</strong> The medication reservoir is vented to the atmosphere, meaning the surface of the liquid medication experiences ambient atmospheric pressure ($P_{\\text{atm}}$). As high-velocity compressed gas accelerates through the constricted jet nozzle, Bernoulli's principle dictates that its static pressure drops significantly below atmospheric pressure ($P_2 < P_{\\text{atm}}$). The resulting hydrostatic pressure gradient ($\\Delta P = P_{\\text{atm}} - P_2$) between the bottom of the capillary tube and the nozzle tip drives bulk liquid upward into the gas stream, where high shear forces shatter it into droplets.<br><br><em>Distractor Traps:</em><br>&bull; A invents an electrostatic attraction mechanism between dipoles and walls.<br>&bull; B claims thermal convective flow lifts the fluid; the rapid expansion of gas actually cools the nozzle via the Joule-Thomson effect.<br>&bull; D refers to osmotic diffusion, which cannot lift macroscopic liquid columns against gravity."
      },
      {
        "q": "In pulmonary aerosol delivery, the respirable fraction is defined as particles with a Mass Median Aerodynamic Diameter (MMAD) between $1.0\\ \\mu\\text{m}$ and $5.0\\ \\mu\\text{m}$. Why are aerosol droplets with $\\text{MMAD} > 5.0\\ \\mu\\text{m}$ (such as those produced by Nozzle A) clinically ineffective at treating acute bronchospasm?",
        "ch": [
          "They undergo rapid acoustic evaporation before reaching the vocal cords",
          "They diffuse rapidly across the buccal mucosa directly into circulation",
          "They remain permanently suspended in dead space and are exhaled freely",
          "They impact inertial obstacles in the oropharynx, failing to reach lungs"
        ],
        "a": 3,
        "e": "<strong>Inertial impaction of large aerosol droplets:</strong> Particle deposition in the respiratory tract depends critically on aerodynamic particle size. Droplets larger than $5.0\\ \\mu\\text{m}$ possess substantial mass and momentum. As the inspired gas stream makes rapid directional turns in the upper airway (nasopharynx, posterior pharynx, and larynx), large droplets have high inertia (characterized by a high Stokes number: $Stk \\propto d_p^2$). Instead of following the bending gas streamlines into the trachea and bronchi, they continue on their straight ballistic trajectories and impact the posterior pharyngeal wall, resulting in high systemic oropharyngeal absorption and negligible pulmonary bronchodilation.<br><br><em>Distractor Traps:</em><br>&bull; A claims large droplets evaporate before reaching the throat; larger droplets have lower surface-area-to-volume ratios and evaporate much slower than fine droplets.<br>&bull; B describes rapid buccal mucosal absorption, which does not relieve smooth muscle bronchospasm in lower airways.<br>&bull; C describes particles smaller than $0.5\\ \\mu\\text{m}$, which remain suspended in air and are exhaled without settling."
      },
      {
        "q": "If medical air ($\\rho \\approx 1.20\\text{ kg/m}^3$) is replaced with Heliox ($\\rho \\approx 0.40\\text{ kg/m}^3$) at an identical jet velocity of $v_2 = 200.0\\text{ m/s}$, how will the Venturi pressure drop ($\\Delta P = \\frac{1}{2}\\rho v_2^2$) be affected?",
        "ch": [
          "The pressure drop decreases to one-third of its previous value (8.0 kPa)",
          "The pressure drop triples to three times its previous value (72.0 kPa)",
          "The pressure drop decreases to one-ninth of its previous value (2.7 kPa)",
          "The pressure drop remains entirely unchanged because jet speed is fixed"
        ],
        "a": 0,
        "e": "<strong>Fluid density scaling in the Bernoulli pressure drop:</strong> The Venturi pressure differential is given by $\\Delta P = \\frac{1}{2}\\rho v_2^2$. Because pressure drop is directly proportional to gas density ($\\Delta P \\propto \\rho$), substituting Heliox ($\\rho = 0.40\\text{ kg/m}^3$) for air ($\\rho = 1.20\\text{ kg/m}^3$) scales the density by $\\frac{0.40}{1.20} = \\frac{1}{3}$. Consequently, at an identical velocity of $200\\text{ m/s}$, the new pressure drop is $\\Delta P' = \\frac{1}{3}(24.0\\text{ kPa}) = 8.0\\text{ kPa}$. This lower suction head decreases liquid entrainment rate unless driving flow is increased.<br><br><em>Distractor Traps:</em><br>&bull; B triples the pressure drop, inverting the ratio of densities ($1.20 / 0.40 = 3$).<br>&bull; C squares the density ratio ($(1/3)^2 = 1/9$), giving $2.67$ kPa.<br>&bull; D falsely claims that fixing velocity makes the pressure drop independent of gas density."
      },
      {
        "q": "Adding a surfactant or reducing the dynamic viscosity of the liquid medication solution promotes the formation of smaller aerosol droplets. Which physical property change explains this enhanced atomization?",
        "ch": [
          "Elevated liquid surface tension increases the energy threshold of breakup",
          "Reduced surface tension lowers cohesive energy required to create surfaces",
          "Decreased viscosity prevents aerodynamic shear stress from acting on drops",
          "Lower surface tension accelerates inertial impaction against nebulizer walls"
        ],
        "a": 1,
        "e": "<strong>Surface energy and aerodynamic droplet atomization:</strong> Liquid atomization requires doing mechanical work against cohesive intermolecular forces to expand the total liquid surface area: $\\Delta W = \\gamma \\cdot \\Delta A$, where $\\gamma$ is surface tension and $\\Delta A$ is the increase in surface area. Because breaking a single liquid column into millions of microscopic droplets creates a vast surface area, high surface tension resists breakup. Lowering liquid surface tension reduces the cohesive energy barrier, allowing aerodynamic gas shear forces to more easily shatter the liquid filament into fine micro-droplets with lower MMAD.<br><br><em>Distractor Traps:</em><br>&bull; A states that elevated surface tension increases breakup threshold; while true physically, the question asked why *reducing* surface tension enhances atomization.<br>&bull; C claims decreasing viscosity prevents shear stress; lower viscosity actually facilitates droplet deformation and breakup.<br>&bull; D claims lower surface tension increases inertial impaction against walls; smaller droplets have lower inertia and avoid impaction."
      }
    ]
  },
  {
    "id": "exam_cp90_5_p7",
    "sec": "C/P",
    "topic": "Dynamic Compliance vs Static Compliance in Mechanical Ventilation",
    "sheet": 7,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_5",
    "passage": "<div class=\"ttl\">Passage 7 (Questions 37&ndash;42)</div>\n<p>In the intensive care unit, mechanical ventilation provides life-sustaining ventilatory support for patients with acute respiratory failure. Safe management requires rigorous monitoring of respiratory mechanics to avoid ventilator-induced lung injury (barotrauma and volutrauma).</p>\n<p>The physical motion of the respiratory system during positive-pressure volume-controlled ventilation is governed by the equation of motion:</p>\n<p>$$P_{\\text{aw}}(t) = P_{\\text{resistive}}(t) + P_{\\text{elastic}}(t) + \\text{PEEP} = R_{\\text{aw}} \\cdot \\dot{V}(t) + \\frac{V_T(t)}{C_{\\text{stat}}} + \\text{PEEP}$$</p>\n<p>where $P_{\\text{aw}}$ is airway pressure, $\\dot{V}$ is inspiratory flow rate, $R_{\\text{aw}}$ is airway resistance, $V_T$ is tidal volume, $C_{\\text{stat}}$ is static respiratory system compliance, and PEEP is positive end-expiratory pressure.</p>\n<p>Two key pressure measurements are obtained during constant-flow volume-controlled ventilation:</p>\n<p>1. <em>Peak Inspiratory Pressure (PIP)</em>: The maximum pressure measured at the conclusion of active inspiration, reflecting the sum of resistive pressure and elastic recoil of the lungs and chest wall:</p>\n<p>$$PIP = R_{\\text{aw}} \\cdot \\dot{V} + \\frac{V_T}{C_{\\text{stat}}} + \\text{PEEP}$$</p>\n<p>2. <em>Plateau Pressure ($P_{\\text{plat}}$)</em>: The pressure measured during an end-inspiratory pause. When gas flow is momentarily arrested ($\\dot{V} = 0$), resistive pressure dissipation drops to zero ($R_{\\text{aw}} \\cdot 0 = 0$), equilibrating airway pressure with alveolar elastic recoil:</p>\n<p>$$P_{\\text{plat}} = \\frac{V_T}{C_{\\text{stat}}} + \\text{PEEP}$$</p>\n<p>From these measurements, static compliance is derived as $C_{\\text{stat}} = \\frac{V_T}{P_{\\text{plat}} - \\text{PEEP}}$, and airway resistance is derived as $R_{\\text{aw}} = \\frac{PIP - P_{\\text{plat}}}{\\dot{V}}$. Critical care specialists recorded respiratory mechanics in adult patients ventilated at $V_T = 500\\text{ mL} = 0.50\\text{ L}$, constant inspiratory flow $\\dot{V} = 1.0\\text{ L/s}$, and $\\text{PEEP} = 5.0\\text{ cm H}_2\\text{O}$ across five clinical states (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Airway pressures, compliance, and calculated airway resistance across clinical states</caption>\n  <thead>\n    <tr><th>Clinical Condition</th><th>PIP ($\\text{cm H}_2\\text{O}$)</th><th>$P_{\\text{plat}}$ ($\\text{cm H}_2\\text{O}$)</th><th>PEEP ($\\text{cm H}_2\\text{O}$)</th><th>$PIP - P_{\\text{plat}}$ ($\\text{cm H}_2\\text{O}$)</th><th>$C_{\\text{stat}}$ ($\\text{mL/cm H}_2\\text{O}$)</th><th>$R_{\\text{aw}}$ ($\\text{cm H}_2\\text{O}/(\\text{L/s})$)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Baseline Healthy Lung</td><td>20.0</td><td>13.0</td><td>5.0</td><td>7.0</td><td>62.5</td><td>7.0</td></tr>\n    <tr><td>Acute Status Asthmaticus</td><td>45.0</td><td>15.0</td><td>5.0</td><td>30.0</td><td>50.0</td><td>30.0</td></tr>\n    <tr><td>Post-Albuterol Asthma</td><td>26.0</td><td>14.0</td><td>5.0</td><td>12.0</td><td>55.6</td><td>12.0</td></tr>\n    <tr><td>Severe ARDS</td><td>48.0</td><td>41.0</td><td>5.0</td><td>7.0</td><td>13.9</td><td>7.0</td></tr>\n    <tr><td>Tension Pneumothorax</td><td>52.0</td><td>44.0</td><td>5.0</td><td>8.0</td><td>12.8</td><td>8.0</td></tr>\n  </tbody>\n</table>\n<p>Clinicians evaluate whether titrating PEEP recruits collapsed alveoli without causing overdistension in ARDS lungs.</p>",
    "qs": [
      {
        "q": "In the patient with Severe ARDS, tidal volume is set to $V_T = 500\\text{ mL}$, $P_{\\text{plat}} = 41.0\\text{ cm H}_2\\text{O}$, and $\\text{PEEP} = 5.0\\text{ cm H}_2\\text{O}$. What is the patient's static compliance ($C_{\\text{stat}}$)?",
        "ch": [
          "10.4 mL/cm H2O",
          "12.2 mL/cm H2O",
          "13.9 mL/cm H2O",
          "15.6 mL/cm H2O"
        ],
        "a": 2,
        "e": "<strong>Static compliance formula and calculation:</strong> Static respiratory compliance measures the elastic distensibility of the lungs and chest wall at rest (zero flow): $C_{\\text{stat}} = \\frac{V_T}{P_{\\text{plat}} - \\text{PEEP}}$. Substituting the clinical parameters: $V_T = 500\\text{ mL}$, $P_{\\text{plat}} = 41.0\\text{ cm H}_2\\text{O}$, and $\\text{PEEP} = 5.0\\text{ cm H}_2\\text{O}$. The driving elastic pressure is $41.0 - 5.0 = 36.0\\text{ cm H}_2\\text{O}$. Thus, $C_{\\text{stat}} = \\frac{500\\text{ mL}}{36.0\\text{ cm H}_2\\text{O}} \\approx 13.889\\text{ mL/cm H}_2\\text{O} \\approx 13.9\\text{ mL/cm H}_2\\text{O}$. This represents a severe reduction from normal physiological compliance ($50&ndash;80\\text{ mL/cm H}_2\\text{O}$), indicating profound lung stiffening in ARDS.<br><br><em>Distractor Traps:</em><br>&bull; A (10.4 mL/cm H2O) erroneously uses PIP instead of $P_{\\text{plat}}$ in the denominator: $500 / (48 - 0) \\approx 10.4$.<br>&bull; B (12.2 mL/cm H2O) erroneously divides by $P_{\\text{plat}}$ directly without subtracting PEEP: $500 / 41 \\approx 12.2$.<br>&bull; D (15.6 mL/cm H2O) divides by $(PIP - P_{\\text{plat}} + \\text{PEEP})$ or makes an arithmetic error."
      },
      {
        "q": "During Acute Status Asthmaticus, $PIP = 45.0\\text{ cm H}_2\\text{O}$, $P_{\\text{plat}} = 15.0\\text{ cm H}_2\\text{O}$, and constant inspiratory flow is $\\dot{V} = 1.0\\text{ L/s}$. What is the patient's airway resistance ($R_{\\text{aw}}$)?",
        "ch": [
          "10.0 cm H2O/(L/s)",
          "15.0 cm H2O/(L/s)",
          "20.0 cm H2O/(L/s)",
          "30.0 cm H2O/(L/s)"
        ],
        "a": 3,
        "e": "<strong>Airway resistance calculation in mechanical ventilation:</strong> Airway resistance represents the resistive pressure drop per unit flow rate: $R_{\\text{aw}} = \\frac{P_{\\text{resistive}}}{\\dot{V}} = \\frac{PIP - P_{\\text{plat}}}{\\dot{V}}$. Substituting the measured values: $PIP = 45.0\\text{ cm H}_2\\text{O}$, $P_{\\text{plat}} = 15.0\\text{ cm H}_2\\text{O}$, and $\\dot{V} = 1.0\\text{ L/s}$. The resistive pressure drop across the tracheobronchial tree is $45.0 - 15.0 = 30.0\\text{ cm H}_2\\text{O}$. Therefore, $R_{\\text{aw}} = \\frac{30.0\\text{ cm H}_2\\text{O}}{1.0\\text{ L/s}} = 30.0\\text{ cm H}_2\\text{O}/(\\text{L/s})$. This marked elevation above normal ($< 10\\text{ cm H}_2\\text{O}/(\\text{L/s})$) reflects severe bronchospasm.<br><br><em>Distractor Traps:</em><br>&bull; A (10.0 cm H2O/(L/s)) subtracts PEEP from $P_{\\text{plat}}$ ($15 - 5 = 10$).<br>&bull; B (15.0 cm H2O/(L/s)) uses $P_{\\text{plat}}$ directly without subtracting from PIP.<br>&bull; C (20.0 cm H2O/(L/s)) subtracts 25 or miscalculates $45 - 15$."
      },
      {
        "q": "What clinical insight can a physician deduce when an alarm sounds for an acute increase in PIP from $20.0\\text{ cm H}_2\\text{O}$ to $45.0\\text{ cm H}_2\\text{O}$, but an inspiratory hold reveals that $P_{\\text{plat}}$ remains essentially unchanged at $15.0\\text{ cm H}_2\\text{O}$?",
        "ch": [
          "Airway resistance has escalated due to bronchospasm or endotracheal obstruction",
          "Parenchymal lung compliance has collapsed due to developing diffuse atelectasis",
          "A massive tension pneumothorax has caused widespread lung and chest stiffening",
          "Pulmonary capillary wedge pressure has spiked, precipitating cardiogenic edema"
        ],
        "a": 0,
        "e": "<strong>Differential diagnosis of isolated PIP elevation:</strong> Peak inspiratory pressure ($PIP$) reflects both airway resistance and static parenchymal compliance, whereas plateau pressure ($P_{\\text{plat}}$) reflects only static elastance. When PIP rises sharply while $P_{\\text{plat}}$ remains stable, the transpulmonary pressure gradient $(PIP - P_{\\text{plat}})$ widens substantially (from 7 to $30\\text{ cm H}_2\\text{O}$). By definition ($R_{\\text{aw}} = \\frac{PIP - P_{\\text{plat}}}{\\dot{V}}$), this isolated increase indicates a purely resistive airway issue, such as acute bronchospasm, mucus plugging, or a kinked or bitten endotracheal tube, rather than parenchymal stiffening.<br><br><em>Distractor Traps:</em><br>&bull; B describes alveolar atelectasis, which would decrease compliance and cause a simultaneous rise in $P_{\\text{plat}}$.<br>&bull; C describes tension pneumothorax, which acutely impairs chest/lung compliance and elevates both PIP and $P_{\\text{plat}}$.<br>&bull; D describes cardiogenic pulmonary edema, which fills alveoli and stiffens the lung, elevating $P_{\\text{plat}}$."
      },
      {
        "q": "Why does performing an end-inspiratory hold (pause) allow clinicians to isolate purely elastic alveolar recoil from resistive pressure losses?",
        "ch": [
          "The inspiratory hold reverses chest wall elasticity to baseline volumes",
          "Zero gas flow eliminates the viscous resistive pressure drop in conduits",
          "The pause activates pulmonary stretch receptors, inhibiting airway tone",
          "Alveolar gas diffusion ceases entirely, raising true oncotic pressure"
        ],
        "a": 1,
        "e": "<strong>Physical principle of the end-inspiratory pause:</strong> Resistive pressure in any hydraulic or pneumatic conduit depends directly on viscous friction and gas motion, governed by the fluid flow relationship $P_{\\text{resistive}} = R_{\\text{aw}} \\cdot \\dot{V}$. When the ventilator closes both its inspiratory and expiratory valves during an end-inspiratory hold, airflow drops to zero ($\\dot{V} = 0$). With zero flow, the viscous resistive pressure loss across the endotracheal tube and bronchial tree completely disappears ($R_{\\text{aw}} \\cdot 0 = 0$). Airway pressure then equilibrates with the pressure inside the expanded alveoli, isolating purely elastic recoil.<br><br><em>Distractor Traps:</em><br>&bull; A claims the hold reverses chest wall elasticity; lung volume remains elevated at $V_T$ throughout the pause.<br>&bull; C refers to Hering-Breuer reflexes, which are biological neural reflexes that do not explain the physical elimination of resistive pressure.<br>&bull; D claims molecular gas diffusion halts, which is false; diffusion continues across alveolar walls regardless of convective airflow pauses."
      },
      {
        "q": "Total work performed on the respiratory system per breath is given by $W = \\int P_{\\text{aw}}\\,dV$. On a dynamic pressure-volume loop, what physiological component of breathing does the enclosed hysteresis area between the inspiratory and expiratory limbs represent?",
        "ch": [
          "Static potential energy stored within expanded chest wall rib cage bands",
          "Energy conserved by the elastic recoil of elastin in the parenchyma beds",
          "Hydrostatic work done against gravity by blood entering pulmonary vessels",
          "Frictional energy dissipated to overcome airway and tissue viscous drag"
        ],
        "a": 3,
        "e": "<strong>Work of breathing and pressure-volume hysteresis loop:</strong> Work of breathing is the integral of pressure with respect to volume ($W = \\int P\\,dV$). On a dynamic ventilator pressure-volume loop, the area under the static elastance line represents conservative elastic potential energy stored in the stretched parenchymal elastic fibers and chest wall during inspiration, which is recovered to drive passive expiration. In contrast, the enclosed loop area (hysteresis) between the inspiratory and expiratory limbs represents non-conservative, irreversible energy dissipation—namely, the frictional work required to overcome viscous airflow resistance and tissue viscoelastic drag, dissipated as heat.<br><br><em>Distractor Traps:</em><br>&bull; A describes elastic potential energy stored in the rib cage, which is represented by the area beneath the static compliance line, not the hysteresis loop.<br>&bull; B describes conserved energy, which is elastic rather than dissipative hysteresis.<br>&bull; C invents a hydrostatic work component for pulmonary blood flow, which is not part of respiratory airway work."
      },
      {
        "q": "In patients with Severe ARDS, loss of functional pulmonary surfactant and diffuse inflammatory alveolar flooding lead to a severe drop in static compliance ($C_{\\text{stat}} = 13.9\\text{ mL/cm H}_2\\text{O}$). How is this reflected on the respiratory static pressure-volume curve?",
        "ch": [
          "The static PV slope is depressed and shifted to the right, requiring high P",
          "The static PV slope is steepened and shifted to the left, requiring low P",
          "The static PV curve rotates upward around the origin, expanding volume gain",
          "The static PV curve remains identical while the dynamic loop narrows fully"
        ],
        "a": 0,
        "e": "<strong>Compliance slope on the pressure-volume curve:</strong> Compliance is the slope of the volume-pressure curve ($C = \\frac{\\Delta V}{\\Delta P}$). In healthy lungs, high compliance produces a steep curve, meaning a large volume change is achieved with modest pressure. In severe ARDS, surfactant inactivation and alveolar flooding increase surface tension and stiffness, collapsing compliance from $62.5$ down to $13.9\\text{ mL/cm H}_2\\text{O}$. On the static PV plot, this causes a marked flattening (depression of slope) and shifts the curve to the right, indicating that much higher driving pressures ($P_{\\text{plat}} - \\text{PEEP}$) are required to achieve the same tidal volume.<br><br><em>Distractor Traps:</em><br>&bull; B describes increased compliance (steepened slope shifted left), which occurs in emphysema where elastin is destroyed.<br>&bull; C describes an upward rotation, which also represents increased compliance rather than stiffening.<br>&bull; D falsely claims the static curve is unchanged; static compliance is directly decreased in ARDS."
      }
    ]
  },
  {
    "id": "exam_cp90_5_disc",
    "sec": "C/P",
    "topic": "C/P Standalone Discrete Questions",
    "sheet": null,
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
        "d": true
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
        "d": true
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
        "d": true
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
        "d": true
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
        "d": true
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
        "d": true
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
        "d": true
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
        "d": true
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
        "d": true
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
        "d": true
      }
    ]
  }
];
