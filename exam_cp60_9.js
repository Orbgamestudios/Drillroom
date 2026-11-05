/* ---- exam_cp60_9.js ---- */
/* 60-minute Chem/Physical Practice Exam 9: 5 passages (30 Qs) + 3 discrete Qs = 33 Qs */
const EXAM_CP60_9 = [
  {
    "id": "exam_cp60_9_p1",
    "sec": "C/P",
    "topic": "Water's Anomalous Phase Boundary, Clausius-Clapeyron Vapor Pressure & Boiling Point Mechanics",
    "sheet": 1,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_9",
    "passage": "<div class=\"ttl\">Passage 1 (Questions 1&ndash;6)</div>\n<p>Phase equilibria in pure substances and aqueous solutions are governed by thermodynamic chemical potential ($\\mu$). At any phase coexistence boundary, the chemical potentials of two equilibrium phases $\\alpha$ and $\\beta$ are identically equal ($\\mu_\\alpha = \\mu_\\beta$). Changes along this equilibrium boundary obey the Clapeyron equation:</p>\n$$\\frac{dP}{dT} = \\frac{\\Delta H_{\\text{trans}}}{T \\Delta V_{\\text{trans}}}$$\n<p>where $\\Delta H_{\\text{trans}}$ is the transition enthalpy and $\\Delta V_{\\text{trans}} = V_\\beta - V_\\alpha$ is the change in molar volume.</p>\n<p>For most molecular compounds (such as benzene or cyclohexane), solid-state crystal packing exhibits greater density than the disordered liquid state, resulting in $\\Delta V_{\\text{fus}} > 0$ and a positive solid-liquid coexistence slope ($dP/dT > 0$). In sharp contrast, water exhibits an anomalous negative solid-liquid phase boundary ($dP/dT < 0$). In ordinary hexagonal ice (ice Ih), each water molecule participates in four hydrogen bonds directed toward tetrahedral vertices, producing an open, cage-like hexagonal lattice with substantial empty interstitial space. Upon melting, the collapse of this rigid lattice causes liquid water to pack more densely than ice ($V_{\\text{solid}} = 19.65\\text{ cm}^3/\\text{mol}$ versus $V_{\\text{liquid}} = 18.02\\text{ cm}^3/\\text{mol}$ at $0^\\circ\\text{C}$), generating a negative volume of fusion ($\\Delta V_{\\text{fus}} = -1.63\\text{ cm}^3/\\text{mol}$). Consequently, compressive hydrostatic stress depresses the melting point.</p>\n<p>For liquid-vapor equilibria, assuming ideal gas behavior for the vapor phase ($V_g \\gg V_l$) and negligible liquid volume yields the Clausius-Clapeyron relation:</p>\n$$\\ln\\left(\\frac{P_2}{P_1}\\right) = -\\frac{\\Delta H_{\\text{vap}}}{R}\\left(\\frac{1}{T_2} - \\frac{1}{T_1}\\right)$$\n<p>Boiling occurs when the equilibrium liquid vapor pressure equals ambient atmospheric pressure ($P_{\\text{vap}} = P_{\\text{amb}}$). Physical chemists used a closed ebulliometer with a variable-pressure manifold to measure the boiling temperatures ($T_b$) of pure water and a 1.0 molal aqueous sucrose solution across pressures from $0.50\\text{ atm}$ to $2.00\\text{ atm}$. Cryo-baric cells were simultaneously utilized to measure ice I melting points under applied hydrostatic pressure (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Thermodynamic phase transition parameters, boiling points, and ice I melting temperatures under variable pressure</caption>\n  <thead>\n    <tr><th>Chamber Pressure (atm)</th><th>Chamber Pressure (kPa)</th><th>Pure Water Tb (°C)</th><th>Pure Water Tb (K)</th><th>1.0 m Sucrose Tb (°C)</th><th>1/Tb (K⁻¹)</th><th>Ice I Melting Tm (°C)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>0.50</td><td>50.7</td><td>81.3</td><td>354.4</td><td>81.8</td><td>0.002822</td><td>+0.004</td></tr>\n    <tr><td>1.00</td><td>101.3</td><td>100.0</td><td>373.2</td><td>100.5</td><td>0.002679</td><td>0.000</td></tr>\n    <tr><td>1.50</td><td>152.0</td><td>111.4</td><td>384.6</td><td>111.9</td><td>0.002600</td><td>-0.004</td></tr>\n    <tr><td>2.00</td><td>202.6</td><td>120.2</td><td>393.4</td><td>120.7</td><td>0.002542</td><td>-0.008</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "Why does solid ice I melt when subjected to elevated hydrostatic pressure, unlike almost all other molecular substances?",
        "ch": [
          "Liquid water has a higher density and smaller molar volume than ice, yielding a negative Clapeyron slope",
          "Ice absorbs latent heat during compression, initiating localized convective thermal flow along planes",
          "Pressure breaks covalent O-H bonds, generating transient hydronium and hydroxide ions in the lattice",
          "Compression lowers the chemical potential of the solid phase relative to that of the adjacent vapor"
        ],
        "a": 0,
        "e": "<strong>Thermodynamic basis of water's anomalous solid-liquid boundary (Topic 390):</strong> The Clapeyron equation describes the slope of any phase boundary: $\\frac{dP}{dT} = \\frac{\\Delta H_{\\text{fus}}}{T \\Delta V_{\\text{fus}}}$. Melting is endothermic ($\\Delta H_{\\text{fus}} > 0$). In water, open hexagonal ice packing has a lower density ($0.917\\text{ g/cm}^3$) and larger molar volume than liquid water ($1.000\\text{ g/cm}^3$). Thus, $\\Delta V_{\\text{fus}} = V_{\\text{liquid}} - V_{\\text{solid}} < 0$, yielding a negative slope ($dP/dT < 0$). By Le Châtelier's principle, applying pressure drives the system toward the denser phase with smaller volume (liquid water), lowering the melting point.<br><br><em>Distractor Traps:</em><br>&bull; B falsely claims mechanical compression causes latent heat absorption and thermal convection.<br>&bull; C incorrectly asserts that moderate mechanical pressure ruptures intramolecular covalent O-H bonds.<br>&bull; D inverts phase stability; compression increases the chemical potential of the less dense solid phase."
      },
      {
        "q": "A research team determines that water boils at 354.4 K at 0.50 atm and at 373.2 K at 1.00 atm. Given R = 8.314 J/(mol·K), which expression calculates Delta H_vap?",
        "ch": [
          "Delta H_vap = -R * ln(1.00 / 0.50) / (373.2 - 354.4)",
          "Delta H_vap = -R * ln(0.50 / 1.00) / (1/354.4 - 1/373.2)",
          "Delta H_vap = -R * (354.4 / 373.2) * ln(0.50 / 1.00)",
          "Delta H_vap = -R * (1/373.2 - 1/354.4) / ln(0.50 / 1.00)"
        ],
        "a": 1,
        "e": "<strong>Application of the Clausius-Clapeyron equation (Topic 391):</strong> The Clausius-Clapeyron equation relates equilibrium vapor pressure and absolute temperature: $\\ln(P_2 / P_1) = -\\frac{\\Delta H_{\\text{vap}}}{R}\\left(\\frac{1}{T_2} - \\frac{1}{T_1}\\right)$. Rearranging algebraically to isolate the enthalpy of vaporization gives: $\\Delta H_{\\text{vap}} = -R \\frac{\\ln(P_2 / P_1)}{(1/T_2 - 1/T_1)}$. Assigning state 1 as $(P_1 = 1.00\\text{ atm}, T_1 = 373.2\\text{ K})$ and state 2 as $(P_2 = 0.50\\text{ atm}, T_2 = 354.4\\text{ K})$ yields $\\Delta H_{\\text{vap}} = -R \\frac{\\ln(0.50 / 1.00)}{(1/354.4 - 1/373.2)}$.<br><br><em>Distractor Traps:</em><br>&bull; A erroneously uses linear temperature difference $(\\Delta T)$ in the denominator instead of reciprocal temperatures $(1/T)$.<br>&bull; C multiplies by the ratio of absolute temperatures rather than evaluating reciprocal temperature differences.<br>&bull; D inverts the quotient, placing temperature reciprocals in the numerator and pressure logarithms in the denominator."
      },
      {
        "q": "At a high-altitude research station where barometric pressure is 0.70 atm, how do water's vapor pressure and boiling temperature behave relative to sea level?",
        "ch": [
          "Vapor pressure at 25 °C is elevated, requiring more thermal heating and a higher temperature to reach boiling",
          "Liquid vapor pressure exceeds ambient barometric pressure at 25 °C, triggering spontaneous boiling at ambient",
          "Water boils at a reduced temperature because vapor pressure matches the lower ambient pressure with less heat",
          "Enthalpy of vaporization increases sharply, imposing a higher thermodynamic energy barrier for vapor formation"
        ],
        "a": 2,
        "e": "<strong>Boiling point mechanics and ambient atmospheric pressure (Topic 391):</strong> A liquid boils when its equilibrium vapor pressure equals the surrounding ambient barometric pressure ($P_{\\text{vap}} = P_{\\text{amb}}$). At high altitudes, ambient atmospheric pressure is substantially lower than sea level ($0.70\\text{ atm} < 1.00\\text{ atm}$). Consequently, water's vapor pressure reaches the reduced ambient threshold at a lower temperature (approximately $90^\\circ\\text{C}$ rather than $100^\\circ\\text{C}$), requiring less thermal energy input to boil.<br><br><em>Distractor Traps:</em><br>&bull; A directionally inverts boiling behavior, claiming high altitude elevates vapor pressure at room temperature and raises boiling point.<br>&bull; B falsely claims vapor pressure at $25^\\circ\\text{C}$ ($0.031\\text{ atm}$) exceeds $0.70\\text{ atm}$, which would mean water boils spontaneously at room temperature.<br>&bull; D asserts $\\Delta H_{\\text{vap}}$ increases significantly with altitude; enthalpy of vaporization is an intrinsic molecular property virtually unchanged by modest pressure shifts."
      },
      {
        "q": "What molecular structural property accounts for the lower density of solid ice compared to liquid water and water's density maximum at 4 °C?",
        "ch": [
          "Continuous formation of dense clathrate cages around ambient gases that rapidly collapse above 100 °C",
          "Planar hexagonal ring stacking mediated strictly by London dispersion forces between compact dipoles",
          "Proton tunneling between adjacent hydronium species that induces transient electrostatic repulsions",
          "A rigid tetrahedral hydrogen-bonded network in ice that partially collapses into denser liquid water"
        ],
        "a": 3,
        "e": "<strong>Hydrogen bonding geometry and ice crystal lattice architecture (Topic 390):</strong> In solid hexagonal ice (ice Ih), each water molecule donates two hydrogen bonds and accepts two hydrogen bonds, forming a rigid three-dimensional tetrahedral lattice. This tetrahedral geometry holds water molecules relatively far apart, creating an open hexagonal network with hollow hexagonal channels, resulting in a low density ($0.917\\text{ g/cm}^3$). Upon melting, thermal vibrations break approximately $15\\%$ of these rigid hydrogen bonds, allowing water molecules to tumble into the open voids and pack more densely. Between $0^\\circ\\text{C}$ and $4^\\circ\\text{C}$, the collapse of residual ice-like clusters outweighs normal thermal expansion, producing water's characteristic density maximum at $3.98^\\circ\\text{C}$.<br><br><em>Distractor Traps:</em><br>&bull; A misattributes density anomalies to gas clathrates collapsing only above $100^\\circ\\text{C}$.<br>&bull; B attributes ice structure to planar stacking and London dispersion forces rather than tetrahedral hydrogen bonding.<br>&bull; C describes proton tunneling (Grotthuss mechanism), which facilitates electrical conductivity but does not govern macroscopic lattice density."
      },
      {
        "q": "Unlike water, liquid benzene exhibits a positive solid-liquid coexistence slope (dP/dT > 0). What thermodynamic property dictates this standard behavior?",
        "ch": [
          "Solid benzene has a smaller molar volume and greater density than liquid benzene, yielding a positive Delta V_fus",
          "Benzene molecules possess permanent dipole moments that align anti-parallel during high-pressure crystallizations",
          "The fusion of solid benzene is an exothermic transition, releasing latent heat that destabilizes the liquid state",
          "Benzene vapor pressure is independent of temperature, preventing external pressure from shifting phase boundaries"
        ],
        "a": 0,
        "e": "<strong>Clapeyron equation and standard solid-liquid phase boundaries (Topic 390):</strong> The Clapeyron equation states that $\\frac{dP}{dT} = \\frac{\\Delta H_{\\text{fus}}}{T \\Delta V_{\\text{fus}}}$. For typical non-polar, non-associated organic liquids like benzene, the solid phase packs molecules more tightly than the mobile liquid phase ($V_{\\text{solid}} < V_{\\text{liquid}}$). Therefore, the molar volume change upon melting is positive ($\\Delta V_{\\text{fus}} = V_{\\text{liquid}} - V_{\\text{solid}} > 0$). Because melting is endothermic ($\\Delta H_{\\text{fus}} > 0$), both numerator and denominator are positive, yielding a standard positive slope ($dP/dT > 0$). Applying hydrostatic pressure stabilizes the denser solid phase, increasing the melting point.<br><br><em>Distractor Traps:</em><br>&bull; B falsely claims benzene possesses a permanent dipole moment; benzene is completely nonpolar with a dipole moment of zero ($\\mu = 0$).<br>&bull; C claims fusion is exothermic; melting a solid always requires an input of latent heat and is strictly endothermic ($\\Delta H_{\text{fus}} > 0$).<br>&bull; D asserts vapor pressure is independent of temperature, violating the Clausius-Clapeyron relation and fundamental thermodynamics."
      },
      {
        "q": "According to Table 1, the 1.0 m sucrose solution exhibits a higher boiling point than pure water across all pressures. What colligative mechanism causes this?",
        "ch": [
          "Sucrose dissociates into multiple hydrated ions, increasing solution electrostatic repulsion and internal pressure",
          "Non-volatile solute particles reduce solvent mole fraction, lowering equilibrium vapor pressure at all temperatures",
          "Sucrose chemically reacts with water molecules, producing an azeotrope that demands greater latent heat of vaporization",
          "Dissolved solute molecules elevate the chemical potential of the gas phase without altering the liquid phase entropy"
        ],
        "a": 1,
        "e": "<strong>Colligative boiling point elevation and vapor pressure lowering (Topics 391 & 402):</strong> When a non-volatile solute (such as sucrose) is dissolved in a solvent, solute particles occupy surface area and increase the entropy of the liquid phase. According to Raoult's Law ($P_{\\text{solution}} = X_{\\text{solvent}} P^\\circ_{\\text{solvent}}$), because $X_{\\text{solvent}} < 1$, the equilibrium vapor pressure of the solution is lower than that of pure water at any given temperature. To boil, the vapor pressure must reach ambient pressure; therefore, the solution must be heated to a higher temperature ($T_b$) before its vapor pressure matches ambient pressure, producing boiling point elevation ($\\Delta T_b = i K_b m$).<br><br><em>Distractor Traps:</em><br>&bull; A asserts sucrose dissociates into ions; sucrose is a non-ionic molecular carbohydrate with a van 't Hoff factor of $i = 1$.<br>&bull; C claims sucrose forms a reactive azeotrope; boiling point elevation is a physical colligative phenomenon, not a chemical azeotropic reaction.<br>&bull; D inverts chemical thermodynamics; non-volatile solute lowers the chemical potential and increases the entropy of the liquid phase, not the gas phase."
      }
    ]
  },
  {
    "id": "exam_cp60_9_p2",
    "sec": "C/P",
    "topic": "Second/Third Laws of Thermodynamics, Gibbs Free Energy (Delta G = Delta H - T*Delta S) & Temperature Spontaneity",
    "sheet": 2,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_9",
    "passage": "<div class=\"ttl\">Passage 2 (Questions 7&ndash;12)</div>\n<p>Thermodynamic spontaneity in macromolecular folding and ligand binding is governed by the Second Law of Thermodynamics: for any spontaneous process within an isolated system, the total entropy must increase ($\\Delta S_{\\text{univ}} = \\Delta S_{\\text{sys}} + \\Delta S_{\\text{surr}} > 0$). Under conditions of constant absolute temperature ($T$) and constant pressure ($P$), the entropy change of the surrounding thermal reservoir is determined by the heat released or absorbed by the reaction system ($\\Delta S_{\\text{surr}} = -\\Delta H_{\\text{sys}}/T$). Multiplying through by $-T$ yields the Gibbs free energy criterion:</p>\n$$\\Delta G_{\\text{sys}} = \\Delta H_{\\text{sys}} - T\\Delta S_{\\text{sys}} = -T\\Delta S_{\\text{univ}}$$\n<p>A biological transition is thermodynamically spontaneous if and only if $\\Delta G_{\\text{sys}} < 0$. The Third Law of Thermodynamics provides an absolute reference frame for entropy, stating that the entropy of a pure, perfectly ordered crystalline substance at absolute zero ($0\\text{ K}$) is identically zero ($S = 0$), enabling determination of standard absolute entropies ($S^\\circ$).</p>\n<p>Biophysicists employed Isothermal Titration Calorimetry (ITC) to characterize the binding thermodynamics between a humanized monoclonal antibody Fab fragment and recombinant viral envelope glycoprotein gp120 across temperatures from $283\\text{ K}$ to $323\\text{ K}$. At each temperature, microcalorimetric titration pulses measured the binding enthalpy ($\\Delta H$). Association constants ($K_a$) were determined through non-linear regression, from which free energies ($\\Delta G = -RT \\ln K_a$) and conformational/solvation entropy contributions ($-T\\Delta S$) were calculated (Table 2).</p>\n<p>At lower temperatures ($283\\text{ K}$), binding was endothermic ($\\Delta H > 0$) but driven favorably by a large positive entropy change ($\\Delta S > 0$) arising from hydrophobic desolvation of nonpolar interface residues. At higher temperatures ($310\\text{ K}$ and $323\\text{ K}$), binding transitioned to an exothermic enthalpy-driven regime ($\\Delta H < 0$) due to favorable hydrogen bond and van der Waals contact formation.</p>\n<table class=\"tbl\">\n  <caption>Table 2 Thermodynamic binding parameters and association constants for Fab-gp120 interaction across temperatures</caption>\n  <thead>\n    <tr><th>Temperature (K)</th><th>ΔH (kJ/mol)</th><th>ΔS (J/(mol·K))</th><th>-TΔS (kJ/mol)</th><th>ΔG (kJ/mol)</th><th>Ka (M⁻¹)</th><th>Thermodynamic Regime</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>283</td><td>+8.5 &plusmn; 0.4</td><td>+110.0 &plusmn; 4.2</td><td>-31.1 &plusmn; 1.2</td><td>-22.6 &plusmn; 0.9</td><td>1.5 &times; 10⁴</td><td>Entropy-driven (Hydrophobic)</td></tr>\n    <tr><td>298</td><td>-5.2 &plusmn; 0.3</td><td>+65.0 &plusmn; 2.5</td><td>-19.4 &plusmn; 0.7</td><td>-24.6 &plusmn; 0.8</td><td>2.1 &times; 10⁴</td><td>Enthalpy and Entropy favored</td></tr>\n    <tr><td>310</td><td>-18.0 &plusmn; 0.6</td><td>+24.0 &plusmn; 1.1</td><td>-7.4 &plusmn; 0.3</td><td>-25.4 &plusmn; 0.7</td><td>1.9 &times; 10⁴</td><td>Enthalpy-driven (Hydrogen bonds)</td></tr>\n    <tr><td>323</td><td>-32.5 &plusmn; 1.1</td><td>-21.0 &plusmn; 0.9</td><td>+6.8 &plusmn; 0.3</td><td>-25.7 &plusmn; 0.9</td><td>1.4 &times; 10⁴</td><td>Enthalpy-driven / Entropic penalty</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "According to the Second Law of Thermodynamics, what condition must be satisfied for an antibody-antigen binding reaction to proceed spontaneously at constant T and P?",
        "ch": [
          "The entropy of the isolated biological system must decrease to ensure proper structural order",
          "The enthalpy of the reaction system must be strictly negative under all cellular ionic conditions",
          "The total entropy of the universe, encompassing both system and surroundings, must strictly increase",
          "The entropy of the surrounding solvent reservoir must remain invariant and equal to exactly zero"
        ],
        "a": 2,
        "e": "<strong>Second Law of Thermodynamics criterion for spontaneous processes (Topic 392):</strong> The Second Law of Thermodynamics dictates that for any spontaneous natural process in the universe (an isolated system), total entropy must increase: $\\Delta S_{\\text{univ}} = \\Delta S_{\\text{sys}} + \\Delta S_{\\text{surr}} > 0$. At constant temperature and pressure, heat released to the surroundings is $q_{\\text{surr}} = -\\Delta H_{\\text{sys}}$, making $\\Delta S_{\\text{surr}} = -\\Delta H_{\\text{sys}}/T$. Substituting this into the Second Law inequality and multiplying by $-T$ yields $\\Delta G_{\\text{sys}} = \\Delta H_{\\text{sys}} - T\\Delta S_{\\text{sys}} < 0$. Thus, a negative Gibbs free energy change directly reflects a net increase in the entropy of the universe.<br><br><em>Distractor Traps:</em><br>&bull; A confuses system entropy with universe entropy; system entropy may decrease during folding or binding as long as surrounding entropy increases more.<br>&bull; B falsely claims enthalpy must be negative; endothermic reactions ($\\Delta H > 0$) can proceed spontaneously if driven by a sufficiently positive $\\Delta S$.<br>&bull; D asserts surrounding entropy must remain zero; heat exchange between system and solvent directly alters surrounding entropy."
      },
      {
        "q": "What foundational physical principle is established by the Third Law of Thermodynamics regarding absolute entropy?",
        "ch": [
          "Entropy increases monotonically during all reversible isothermal expansions of ideal gas mixtures",
          "Spontaneous biochemical processes continuously maximize the total energy of an isolated universe",
          "The heat capacity of an ideal solution approaches infinity as the system reaches dynamic equilibrium",
          "The entropy of a pure, perfectly ordered crystalline lattice at absolute zero temperature is zero"
        ],
        "a": 3,
        "e": "<strong>Third Law of Thermodynamics and absolute zero entropy reference (Topic 393):</strong> The Third Law of Thermodynamics states that the entropy of a pure, perfectly ordered crystalline substance at absolute zero ($0\\text{ K}$, or $-273.15^\\circ\\text{C}$) is identically zero ($S = 0$). By Boltzmann's statistical entropy equation ($S = k_B \\ln W$), a perfect crystal at ground state possesses only a single microscopic configuration ($W = 1$), so $S = k_B \\ln(1) = 0$. This provides an absolute non-arbitrary baseline from which standard molar entropies ($S^\\circ$) can be measured across all temperatures.<br><br><em>Distractor Traps:</em><br>&bull; A describes isothermal gas expansions, which relate to the Second Law rather than the Third Law.<br>&bull; B confuses entropy maximization with energy conservation; the First Law states energy is conserved, not maximized.<br>&bull; C incorrectly asserts heat capacity approaches infinity; Debye T-cubed law shows heat capacity approaches zero as $T \to 0\text{ K}$."
      },
      {
        "q": "At 283 K, the binding interaction is endothermic (Delta H = +8.5 kJ/mol) yet spontaneous (Delta G = -22.6 kJ/mol). What enables this spontaneity?",
        "ch": [
          "A positive entropy change (Delta S > 0) such that the -T*Delta S term overcomes the positive Delta H",
          "A negative entropy change (Delta S < 0) that lowers the total internal energy of the reacting system",
          "Complete cancellation of enthalpy by an equal and opposite increase in ambient barometric pressure",
          "Enzymatic catalysis by solvent molecules that alters the fundamental equilibrium constant of binding"
        ],
        "a": 0,
        "e": "<strong>Temperature-dependent spontaneity and entropy-driven binding (Topic 394):</strong> In the Gibbs free energy relationship $\\Delta G = \\Delta H - T\\Delta S$, an endothermic reaction has $\\Delta H > 0$, which opposes spontaneity. For $\\Delta G$ to be negative, the entropic contribution $-T\\Delta S$ must be negative and exceed the positive enthalpy term in magnitude. From Table 2, at $283\\text{ K}$, $\\Delta S = +110.0\\text{ J/(mol}\\cdot\\text{K)} = +0.110\\text{ kJ/(mol}\\cdot\\text{K)}$. The entropic term is $-T\\Delta S = -(283)(0.110) = -31.13\\text{ kJ/mol}$. Combining terms gives $\\Delta G = +8.5 - 31.13 = -22.63\\text{ kJ/mol} < 0$, confirming spontaneous entropy-driven binding.<br><br><em>Distractor Traps:</em><br>&bull; B falsely claims a negative entropy change promotes spontaneity; if $\\Delta S < 0$, the $-T\\Delta S$ term is positive, making $\\Delta G$ even more non-spontaneous.<br>&bull; C suggests pressure cancelation; at constant pressure, ambient barometric pressure does not cancel enthalpy.<br>&bull; D confuses kinetic catalysts with thermodynamic state functions; catalysts accelerate rates but never alter $\\Delta G$ or $K_{\text{eq}}$."
      },
      {
        "q": "For a mutant antibody binding event where Delta H = -40.0 kJ/mol and Delta S = -50.0 J/(mol·K), what is the calculated Delta G at 310 K?",
        "ch": [
          "Delta G is exactly -55.5 kJ/mol",
          "Delta G is exactly -24.5 kJ/mol",
          "Delta G is exactly +24.5 kJ/mol",
          "Delta G is exactly +55.5 kJ/mol"
        ],
        "a": 1,
        "e": "<strong>Gibbs free energy calculation and unit conversion (Topic 394):</strong> The Gibbs free energy is calculated via $\\Delta G = \\Delta H - T\\Delta S$. First, convert $\\Delta S$ from $\\text{J/(mol}\\cdot\\text{K)}$ to $\\text{kJ/(mol}\\cdot\\text{K)}$: $\\Delta S = -50.0\\text{ J/(mol}\\cdot\\text{K)} = -0.050\\text{ kJ/(mol}\\cdot\\text{K)}$. Next, calculate the entropic penalty: $-T\\Delta S = -(310\\text{ K})(-0.050\\text{ kJ/(mol}\\cdot\\text{K)}) = +15.5\\text{ kJ/mol}$. Finally, sum enthalpy and entropic terms: $\\Delta G = -40.0\\text{ kJ/mol} + 15.5\\text{ kJ/mol} = -24.5\\text{ kJ/mol}$. The reaction is spontaneous (enthalpy-driven with an entropic penalty).<br><br><em>Distractor Traps:</em><br>&bull; A fails to account for the negative sign in $-T\\Delta S$, computing $\\Delta G = -40.0 - 15.5 = -55.5\text{ kJ/mol}$.<br>&bull; C makes an overall algebraic sign error, reporting $+24.5\text{ kJ/mol}$.<br>&bull; D adds both terms positively, computing $+40.0 + 15.5 = +55.5\text{ kJ/mol}$."
      },
      {
        "q": "What molecular mechanism accounts for the large positive entropy change (Delta S > 0) observed during hydrophobic association at 283 K?",
        "ch": [
          "Unfolding of structured alpha-helical motifs into highly disordered random coil peptide backbones",
          "Formation of rigid, highly ordered hydrogen-bonded clathrate water cages around the binding site",
          "Release of ordered hydration water molecules into the bulk solvent, increasing rotational disorder",
          "Condensation of mobile counterions onto the charged surfaces of the newly formed protein complex"
        ],
        "a": 2,
        "e": "<strong>Hydrophobic effect and solvent desolvation entropy (Topic 392):</strong> Unbound nonpolar amino acid side chains force surrounding water molecules to adopt rigid, highly ordered, hydrogen-bonded 'clathrate-like' solvation cages that exhibit low conformational entropy. When the nonpolar epitope on gp120 buries against the nonpolar paratope of the Fab fragment, these hydrophobic surfaces are removed from water contact. The constrained clathrate water molecules are released into bulk solvent, where they gain extensive translational, rotational, and vibrational degrees of freedom. This release of structured water generates a large positive solvent entropy change ($\\Delta S_{\\text{solvent}} \\gg 0$) that drives binding at lower temperatures.<br><br><em>Distractor Traps:</em><br>&bull; A describes protein unfolding; antibody-antigen binding typically induces folding or structural stabilization, decreasing protein conformational entropy.<br>&bull; B directionally inverts the hydrophobic effect; clathrate cages form around exposed nonpolar groups before binding, whereas binding releases them.<br>&bull; D describes counterion condensation, which decreases ion translational entropy and opposes positive $\\Delta S$."
      },
      {
        "q": "When the binding interaction becomes exothermic (Delta H_sys < 0) at 310 K, how does this heat release affect the entropy of the surroundings (Delta S_surr)?",
        "ch": [
          "Delta S_surr remains invariant because external surroundings cannot exchange heat with liquid solutions",
          "Delta S_surr decreases because thermal energy transfer reduces the kinetic velocities of water molecules",
          "Delta S_surr becomes equal to system entropy change, preventing any net change in universe entropy states",
          "Delta S_surr increases because heat transferred into surroundings elevates solvent thermal microstates"
        ],
        "a": 3,
        "e": "<strong>Surrounding entropy and exothermic heat exchange (Topic 392):</strong> The entropy change of the surroundings is quantitatively defined by $\\Delta S_{\\text{surr}} = \\frac{q_{\\text{surr}}}{T} = -\\frac{\\Delta H_{\\text{sys}}}{T}$. During an exothermic reaction ($\\Delta H_{\\text{sys}} < 0$), heat is released by the system and absorbed by the surrounding thermal reservoir ($q_{\\text{surr}} > 0$). This input of thermal energy increases the average kinetic energy and dispersal of energy among the microscopic quantum states of the solvent molecules, causing $\\Delta S_{\\text{surr}}$ to increase ($\\Delta S_{\\text{surr}} > 0$).<br><br><em>Distractor Traps:</em><br>&bull; A asserts surroundings cannot exchange heat with liquid solutions, violating the First and Second Laws of Thermodynamics.<br>&bull; B claims heat transfer decreases molecular speeds; adding thermal energy increases kinetic energy and velocities.<br>&bull; C confuses surrounding entropy change with equilibrium zero net entropy change."
      }
    ]
  },
  {
    "id": "exam_cp60_9_p3",
    "sec": "C/P",
    "topic": "Kinetic vs Thermodynamic Control & Standard Free Energy / Equilibrium Relationships (Delta G° = -RT*ln K, Q vs K)",
    "sheet": 3,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_9",
    "passage": "<div class=\"ttl\">Passage 3 (Questions 13&ndash;18)</div>\n<p>In organic synthesis and metabolic transformations, reactions possessing competing pathways can yield distinct products depending on reaction conditions. When an asymmetric ketone such as 2-methylcyclohexanone undergoes deprotonation, two regioisomeric enolates can form:</p>\n<p>1. The kinetic enolate (deprotonation at C6): formed by abstracting a proton from the less sterically hindered secondary carbon. Because the activation barrier is lower ($E_{a,1} = 42\\text{ kJ/mol}$), this product forms at a much faster rate ($k_1 \\gg k_2$).</p>\n<p>2. The thermodynamic enolate (deprotonation at C2): formed by abstracting a proton from the more hindered tertiary carbon. Although it faces a higher activation energy ($E_{a,2} = 65\\text{ kJ/mol}$), the resulting tetrasubstituted alkene is stabilized by hyperconjugation and alkyl electron donation, rendering it thermodynamically more stable ($\\Delta G^\\circ = -8.8\\text{ kJ/mol}$ relative to the kinetic isomer).</p>\n<p>Under kinetic control (strong, sterically hindered base such as lithium diisopropylamide [LDA], aprotic solvent THF, low temperature $-78^\\circ\\text{C}$ / $195\\text{ K}$, and absence of excess ketone), deprotonation is virtually irreversible, selectively trapping the kinetic product. Conversely, under thermodynamic control (weaker, unhindered base such as potassium tert-butoxide or triethylamine in protic solvent, elevated temperature $80^\\circ\\text{C}$ / $353\\text{ K}$), proton transfer is reversible. Molecules possess sufficient thermal energy to surmount reverse activation barriers, establishing dynamic chemical equilibrium.</p>\n<p>At equilibrium, the product distribution obeys the standard Gibbs free energy relation:</p>\n$$\\Delta G^\\circ = -RT \\ln K_{\\text{eq}}$$\n<p>Under non-equilibrium conditions, reaction directionality is governed by the reaction quotient $Q$ in the non-standard free energy relation:</p>\n$$\\Delta G = \\Delta G^\\circ + RT \\ln Q$$\n<p>Enolate regioisomer ratios and kinetic parameters were quantified across systematic synthetic trials (Table 3).</p>\n<table class=\"tbl\">\n  <caption>Table 3 Regioisomeric enolate distributions, kinetic activation parameters, and equilibrium constants for 2-methylcyclohexanone deprotonation</caption>\n  <thead>\n    <tr><th>Trial</th><th>Base & Solvent System</th><th>Temperature (°C / K)</th><th>Kinetic Enolate (%)</th><th>Thermodynamic Enolate (%)</th><th>Reaction Quotient Q (at 5 min)</th><th>Equilibrium Constant Keq</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>1</td><td>LDA (1.1 eq), THF</td><td>-78 / 195</td><td>98 &plusmn; 1</td><td>2 &plusmn; 1</td><td>0.02 &plusmn; 0.01</td><td>2.3 &times; 10² (Irreversible)</td></tr>\n    <tr><td>2</td><td>LDA (1.1 eq), THF</td><td>0 / 273</td><td>84 &plusmn; 2</td><td>16 &plusmn; 2</td><td>0.19 &plusmn; 0.02</td><td>48 &plusmn; 3</td></tr>\n    <tr><td>3</td><td>KOtBu (0.9 eq), tBuOH</td><td>25 / 298</td><td>28 &plusmn; 2</td><td>72 &plusmn; 2</td><td>2.57 &plusmn; 0.15</td><td>35 &plusmn; 2</td></tr>\n    <tr><td>4</td><td>KOtBu (0.9 eq), tBuOH</td><td>80 / 353</td><td>5 &plusmn; 1</td><td>95 &plusmn; 1</td><td>19.0 &plusmn; 0.8</td><td>20.0 &plusmn; 0.7</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "On a reaction coordinate diagram comparing kinetic and thermodynamic enolates, how do activation energies and product ground-state free energies differ?",
        "ch": [
          "The kinetic enolate has a higher activation energy and a lower, more stable ground-state free energy",
          "The kinetic enolate has a lower activation energy, but a higher and less stable ground-state free energy",
          "Both enolate isomers share identical transition state energies, differing only in reaction enthalpy",
          "The thermodynamic enolate possesses a lower activation energy and a higher ground-state free energy"
        ],
        "a": 1,
        "e": "<strong>Reaction coordinate profiles of kinetic vs thermodynamic control (Topic 395):</strong> A reaction coordinate diagram illustrates that the kinetic pathway proceeds through a lower transition state free energy ($E_{a,\\text{kin}} < E_{a,\\text{thermo}}$), allowing the kinetic product to form more rapidly at low temperatures where thermal energy is limited. However, the thermodynamic product resides in a deeper potential energy well, meaning it possesses a lower, more stable ground-state free energy ($G_{\\text{thermo}} < G_{\\text{kin}}$, or $\\Delta G^\\circ < 0$ for the conversion of kinetic to thermodynamic product).<br><br><em>Distractor Traps:</em><br>&bull; A completely inverts both activation energy and ground-state thermodynamic stability.<br>&bull; C falsely asserts transition states are identical; the two pathways pass through structurally distinct transition states with different steric and electronic energies.<br>&bull; D claims the thermodynamic enolate has a lower activation energy; if it had lower $E_a$, it would be both the kinetic and thermodynamic product."
      },
      {
        "q": "At 353 K, the standard free energy difference between thermodynamic and kinetic enolates is Delta G° = -8.8 kJ/mol. Given R = 8.314 J/(mol·K), what is K_eq?",
        "ch": [
          "K_eq is approximately 0.05",
          "K_eq is approximately 1.00",
          "K_eq is approximately 20.0",
          "K_eq is approximately 400."
        ],
        "a": 2,
        "e": "<strong>Calculation of equilibrium constant from standard free energy (Topic 396):</strong> The relationship between standard Gibbs free energy and the equilibrium constant is $\\Delta G^\\circ = -RT \\ln K_{\\text{eq}}$. Rearranging to solve for $K_{\\text{eq}}$: $\\ln K_{\\text{eq}} = -\\frac{\\Delta G^\\circ}{RT}$. Converting units: $\\Delta G^\\circ = -8800\\text{ J/mol}$. At $T = 353\\text{ K}$, $RT = (8.314\\text{ J/(mol}\\cdot\\text{K)})(353\\text{ K}) \\approx 2935\\text{ J/mol}$. Calculating: $\\ln K_{\\text{eq}} = -\\frac{-8800}{2935} \\approx +3.00$. Therefore, $K_{\\text{eq}} = e^{3.00} \\approx 20.08 \\approx 20.0$. This matches the experimental equilibrium ratio in Table 4 ($95\\%$ thermodynamic / $5\\%$ kinetic $= 19$).<br><br><em>Distractor Traps:</em><br>&bull; A forgets the negative sign in $-\\Delta G^\\circ / RT$, computing $e^{-3.0} \u0007pprox 0.05$.<br>&bull; B assumes $\\Delta G^\\circ = 0$, which would yield $K_{\text{eq}} = 1.00$.<br>&bull; D forgets to divide by temperature or computes $e^{6.0} \u0007pprox 400$."
      },
      {
        "q": "During an equilibration experiment at 353 K, the reaction quotient Q is measured to be 2.5 while K_eq is 20.0. How will the reaction respond?",
        "ch": [
          "The reaction is at dynamic equilibrium, so the net forward and reverse reaction rates are identical",
          "Delta G is positive, driving net reverse reaction to generate additional kinetic enolate molecules",
          "Both forward and reverse rate constants drop to zero until additional base catalyst is introduced",
          "Delta G is negative, driving net forward reaction to convert kinetic into thermodynamic enolate"
        ],
        "a": 3,
        "e": "<strong>Reaction quotient Q versus K_eq and spontaneity direction (Topic 397):</strong> The non-standard free energy change is given by $\\Delta G = \\Delta G^\\circ + RT \\ln Q$. Because $\\Delta G^\\circ = -RT \\ln K_{\\text{eq}}$, this can be rewritten as $\\Delta G = RT \\ln(Q / K_{\\text{eq}})$. Here, $Q = 2.5$ and $K_{\\text{eq}} = 20.0$, so $Q < K_{\\text{eq}}$. Since $Q / K_{\\text{eq}} < 1$, $\\ln(Q / K_{\\text{eq}}) < 0$, making $\\Delta G < 0$. A negative $\\Delta G$ indicates that the forward reaction (conversion of kinetic enolate into thermodynamic enolate) is spontaneous, shifting equilibrium forward until $Q = K_{\\text{eq}}$.<br><br><em>Distractor Traps:</em><br>&bull; A claims the system is at equilibrium; dynamic equilibrium requires $Q = K_{\text{eq}}$ and $\\Delta G = 0$.<br>&bull; B falsely asserts $\\Delta G > 0$ and predicts a reverse shift; reverse shifts occur only when $Q > K_{\text{eq}}$.<br>&bull; C confuses thermodynamic driving force with kinetic rate constants; rate constants depend solely on temperature and activation energy."
      },
      {
        "q": "Why does treating 2-methylcyclohexanone with lithium diisopropylamide (LDA) at -78 °C selectively yield the kinetic enolate (deprotonation at C6)?",
        "ch": [
          "Bulky isopropyl groups selectively abstract the less sterically hindered proton at the faster rate",
          "LDA is a small nucleophile that coordinates selectively to the tertiary carbocation at the C2 carbon",
          "Deprotonation at C6 is an endothermic equilibrium process driven by high thermal kinetic energy",
          "Liquid nitrogen temperatures selectively lower the activation barrier for tetrasubstituted alkenes"
        ],
        "a": 0,
        "e": "<strong>Steric hindrance and kinetic enolate generation (Topic 395):</strong> Lithium diisopropylamide (LDA) features two bulky isopropyl groups attached to a strongly basic nitrogen atom ($pK_a \\approx 36$). Because of its substantial steric bulk, LDA cannot easily approach the more congested tertiary proton at C2 (bearing the methyl substituent). Instead, it rapidly abstracts one of the more sterically accessible secondary protons at C6. At $-78^\\circ\\text{C}$ in an aprotic solvent with no excess ketone, this deprotonation is irreversible, kinetically trapping the less substituted enolate in near-quantitative yield ($98\\%$).<br><br><em>Distractor Traps:</em><br>&bull; B falsely claims LDA is a small nucleophile; LDA is an extraordinarily bulky, non-nucleophilic strong base.<br>&bull; C asserts C6 deprotonation is driven by high thermal kinetic energy; it occurs at $-78^\\circ\text{C}$ (very low thermal energy).<br>&bull; D claims low temperature lowers activation barriers; activation energies are constant properties of the potential energy surface."
      },
      {
        "q": "What molecular structural feature provides enhanced thermodynamic stability to the thermodynamic enolate relative to its kinetic regioisomer?",
        "ch": [
          "Steric relief from placing negative charge on the more accessible terminal carbon atom",
          "Greater alkene substitution, allowing stabilizing hyperconjugation with alkyl groups",
          "Strong intramolecular hydrogen bonding between enolate oxygen and carbonyl carbons",
          "Complete loss of ring conformational strain, allowing cyclohexane to become planar"
        ],
        "a": 1,
        "e": "<strong>Alkene substitution and thermodynamic stability of enolates (Topic 395):</strong> Enolates possess significant double-bond character across the carbon-carbon bond (described by the resonance contributor $\\text{C}=\\text{C}-\\text{O}^-$). In the thermodynamic enolate (deprotonation at C2), the resulting carbon-carbon double bond is tetrasubstituted (bonded to two ring carbons, the methyl substituent, and the enolate oxygen). More highly substituted alkenes are thermodynamically more stable due to hyperconjugation (overlap of adjacent $\\text{C}-\\text{H}$ and $\\text{C}-\\text{C}$ $\\sigma$-orbitals with the empty $\\pi^*$ orbital) and greater $sp^2\\text{--}sp^3$ bonding orbital overlap.<br><br><em>Distractor Traps:</em><br>&bull; A describes kinetic accessibility rather than thermodynamic stabilization.<br>&bull; C posits intramolecular hydrogen bonding; enolates in aprotic media lack proton donors for intramolecular hydrogen bonding.<br>&bull; D claims the cyclohexane ring becomes planar; six-membered cyclohexenyl rings adopt a half-chair conformation, not a planar ring."
      },
      {
        "q": "Under non-standard conditions, free energy is given by Delta G = Delta G° + RT*ln(Q). What is the value of Delta G when the reaction reaches equilibrium?",
        "ch": [
          "Delta G = Delta G° because standard and non-standard states are identical at equilibrium",
          "Delta G approaches negative infinity because the reaction has reached maximum spontaneity",
          "Delta G = 0 because forward and reverse rates are equal and no net work can be extracted",
          "Delta G = RT*ln(K) because the reaction quotient exceeds equilibrium constants at dynamic stop"
        ],
        "a": 2,
        "e": "<strong>Non-standard Gibbs free energy at chemical equilibrium (Topic 397):</strong> At dynamic chemical equilibrium, the rate of the forward reaction equals the rate of the reverse reaction, and the concentrations of all reacting species remain constant over time. Because the chemical potentials of reactants and products are equal, the system can perform no net useful non-PV work; therefore, $\\Delta G = 0$. Substituting $\\Delta G = 0$ into the non-standard free energy equation gives $0 = \\Delta G^\\circ + RT \\ln K_{\\text{eq}}$, which yields the foundational thermodynamic equation $\\Delta G^\\circ = -RT \\ln K_{\\text{eq}}$. Note that while $\\Delta G = 0$ at equilibrium, $\\Delta G^\\circ$ is a non-zero constant reflecting standard-state free energies.<br><br><em>Distractor Traps:</em><br>&bull; A confuses $\\Delta G$ with $\\Delta G^\\circ$; standard free energy $\\Delta G^\\circ$ is a fixed constant, whereas $\\Delta G$ varies with concentration and reaches zero at equilibrium.<br>&bull; B asserts $\\Delta G$ approaches negative infinity; that would indicate an infinite driving force, which is impossible at equilibrium.<br>&bull; D asserts $\\Delta G = RT\\ln K$; at equilibrium $\\Delta G = 0$, and $\\Delta G^\\circ = -RT\\ln K$."
      }
    ]
  },
  {
    "id": "exam_cp60_9_p4",
    "sec": "C/P",
    "topic": "Coupled Biochemical Reactions (ATP Hydrolysis), Law of Mass Action (Kc vs Kp) & Le Châtelier Gas Volume Shifts",
    "sheet": 4,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_9",
    "passage": "<div class=\"ttl\">Passage 4 (Questions 19&ndash;24)</div>\n<p>Cellular metabolism relies on thermodynamic reaction coupling to drive endergonic biosynthetic pathways that would otherwise be non-spontaneous. In hepatocytes, the condensation of L-glutamate with ammonium to produce L-glutamine is energetically unfavorable under standard biochemical conditions:</p>\n$$\\text{Glutamate} + \\text{NH}_4^+ \\rightleftharpoons \\text{Glutamine} + \\text{H}_2\\text{O} \\quad (\\Delta G^{\\circ\\prime} = +14.2\\text{ kJ/mol}, K_{\\text{eq},1} = 3.2 \\times 10^{-3})$$\n<p>The enzyme glutamine synthetase couples this endergonic condensation to the highly exergonic hydrolysis of adenosine triphosphate (ATP):</p>\n$$\\text{ATP} + \\text{H}_2\\text{O} \\rightleftharpoons \\text{ADP} + \\text{P}_i \\quad (\\Delta G^{\\circ\\prime} = -30.5\\text{ kJ/mol}, K_{\\text{eq},2} = 2.2 \\times 10^5)$$\n<p>Coupling occurs via a transient high-energy intermediate ($\\gamma$-glutamyl phosphate). Because Gibbs free energy is a state function, standard free energy changes are strictly additive ($\\Delta G^{\\circ\\prime}_{\\text{net}} = \\Delta G^{\\circ\\prime}_1 + \\Delta G^{\\circ\\prime}_2 = -16.3\\text{ kJ/mol}$), and the overall equilibrium constant is multiplicative ($K_{\\text{net}} = K_1 \\times K_2 \\approx 7.0 \\times 10^2$).</p>\n<p>To supply ammonium for cellular glutamine biosynthesis in industrial bioprocess modeling, researchers utilized an enclosed gas-phase catalytic reactor synthesizing ammonia via the Haber-Bosch equilibrium:</p>\n$$\\text{N}_2(g) + 3\\text{H}_2(g) \\rightleftharpoons 2\\text{NH}_3(g) \\quad (\\Delta H^\\circ = -92.4\\text{ kJ/mol}, \\Delta n_{\\text{gas}} = 2 - 4 = -2)$$\n<p>The equilibrium constant in terms of partial pressures ($K_p$) relates to molar concentration equilibrium constant ($K_c$) through the ideal gas law:</p>\n$$K_p = K_c(RT)^{\\Delta n_{\\text{gas}}}$$\n<p>Pure solids and pure liquids are omitted from mass action expressions because their activities are unity. Chemical engineers tested Le Châtelier perturbations on the gas equilibrium inside a piston-sealed chamber, evaluating volume compression ($V/2$), volume expansion ($2V$), and argon gas injection under constant volume versus constant pressure regimes (Table 4).</p>\n<table class=\"tbl\">\n  <caption>Table 4 Bioenergetic coupling parameters and gas-phase equilibrium response to volume and pressure perturbations at 500 K</caption>\n  <thead>\n    <tr><th>Reaction / Perturbation Condition</th><th>Thermodynamic State / Perturbation</th><th>Δn_gas</th><th>Equilibrium Direction Shift</th><th>Product-to-Reactant Ratio</th><th>Observed Keq or Kp</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Glutamate amidation (uncoupled)</td><td>Uncoupled synthesis at pH 7.0</td><td>&mdash;</td><td>Favors reactants (Non-spontaneous)</td><td>3.2 &times; 10⁻³</td><td>3.2 &times; 10⁻³</td></tr>\n    <tr><td>ATP hydrolysis (isolated)</td><td>Standard biochemical state</td><td>&mdash;</td><td>Favors products (Spontaneous)</td><td>2.2 &times; 10⁵</td><td>2.2 &times; 10⁵</td></tr>\n    <tr><td>Glutamine synthetase (coupled)</td><td>Coupled through acyl-phosphate</td><td>&mdash;</td><td>Favors products (Net spontaneous)</td><td>7.0 &times; 10²</td><td>7.0 &times; 10²</td></tr>\n    <tr><td>Haber reactor: Volume halved (V → V/2)</td><td>Mechanical piston compression</td><td>-2</td><td>Shifts toward products (Forward)</td><td>Elevated (Q &lt; Kp)</td><td>Kp unchanged (1.44 &times; 10⁻⁵)</td></tr>\n    <tr><td>Haber reactor: Volume doubled (V → 2V)</td><td>Mechanical piston expansion</td><td>-2</td><td>Shifts toward reactants (Reverse)</td><td>Depressed (Q &gt; Kp)</td><td>Kp unchanged (1.44 &times; 10⁻⁵)</td></tr>\n    <tr><td>Haber reactor: Argon added (Constant V)</td><td>Inert noble gas injection</td><td>-2</td><td>No shift (Equilibrium maintained)</td><td>Unchanged (Q = Kp)</td><td>Kp unchanged (1.44 &times; 10⁻⁵)</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "When two chemical reactions are coupled through a common phosphorylated intermediate, how are free energy changes and equilibrium constants combined?",
        "ch": [
          "Free energies are multiplied together, whereas equilibrium constants are added algebraically",
          "Free energies are subtracted, whereas equilibrium constants remain independent of coupling",
          "Free energies are divided, whereas equilibrium constants are multiplied by Faraday constant",
          "Free energies are added algebraically, whereas overall equilibrium constants are multiplied"
        ],
        "a": 3,
        "e": "<strong>Additivity of Gibbs free energy and multiplicity of equilibrium constants (Topic 398):</strong> Gibbs free energy ($G$) is an extensive thermodynamic state function. When sequential or coupled reactions are combined algebraically, their standard free energy changes sum together: $\\Delta G^\\circ_{\\text{net}} = \\Delta G^\\circ_1 + \\Delta G^\\circ_2$. Because $\\Delta G^\\circ = -RT \\ln K$, exponentiating both sides yields $K = e^{-\\Delta G^\\circ / RT}$. Consequently, $K_{\\text{net}} = e^{-(\\Delta G^\\circ_1 + \\Delta G^\\circ_2)/RT} = e^{-\\Delta G^\\circ_1/RT} \\cdot e^{-\\Delta G^\\circ_2/RT} = K_1 \\times K_2$. Coupling glutamate amidation ($+14.2\\text{ kJ/mol}$) to ATP hydrolysis ($-30.5\\text{ kJ/mol}$) gives $\\Delta G^{\\circ\\prime} = -16.3\\text{ kJ/mol}$ and $K_{\\text{net}} = (3.2 \\times 10^{-3})(2.2 \\times 10^5) \\approx 7.0 \\times 10^2$.<br><br><em>Distractor Traps:</em><br>&bull; A inverts the rules of combination, asserting free energies multiply and equilibrium constants add.<br>&bull; B falsely claims equilibrium constants remain unaffected by energetic coupling through a common intermediate.<br>&bull; C introduces division and Faraday's constant, which is used in electrochemistry ($\\Delta G^\\circ = -nFE^\\circ$), not in coupled mass action."
      },
      {
        "q": "Which structural property of the ATP molecule contributes significantly to its large negative standard free energy of hydrolysis (Delta G°' = -30.5 kJ/mol)?",
        "ch": [
          "Electrostatic repulsion among negatively charged oxygen atoms of adjacent phosphate groups",
          "Rapid keto-enol tautomerization of the purine adenine base following phosphoanhydride loss",
          "Steric hindrance between the ribose furanose ring and terminal phosphoanhydride linkages",
          "High resonance strain localized specifically within the ribose five-membered carbohydrate"
        ],
        "a": 0,
        "e": "<strong>Molecular basis of high-energy phosphoanhydride bonds in ATP (Topic 398):</strong> ATP contains three phosphate groups linked by phosphoanhydride bonds. At physiological pH ($7.4$), these phosphate groups carry approximately four negative charges ($\\text{ATP}^{4-}$). These clustered negative charges on adjacent oxygens experience severe electrostatic repulsion. Hydrolysis cleaves the terminal phosphoanhydride bond, separating these like charges ($\\text{ADP}^{3-} + \\text{HPO}_4^{2-}$). Furthermore, the free orthophosphate product ($P_i$) gains extensive resonance stabilization (four equivalent resonance structures with delocalized negative charge), and the products exhibit higher hydration entropy than the strained reactant.<br><br><em>Distractor Traps:</em><br>&bull; B mentions adenine base tautomerization, which plays no role in phosphoanhydride bond energy.<br>&bull; C attributes high energy to steric hindrance between ribose and phosphate; the phosphoanhydride linkage is separated from ribose by an ester bond.<br>&bull; D claims ring strain in the ribose sugar causes high energy; the five-membered furanose ring is stable and not cleaved during hydrolysis."
      },
      {
        "q": "For the gas-phase ammonia synthesis equilibrium (N2 + 3 H2 <=> 2 NH3), what occurs when the reactor volume is halved at constant temperature?",
        "ch": [
          "The equilibrium constant Kp increases, causing the forward reaction rate to slow down",
          "The reaction shifts toward products because the product side has fewer total moles of gas",
          "The reaction shifts toward reactants because high pressure destabilizes covalent bonds",
          "The partial pressures of all gases decrease uniformly, leaving the system undisturbed"
        ],
        "a": 1,
        "e": "<strong>Le Châtelier's principle and volume compression in gas equilibria (Topic 400):</strong> The balanced reaction is $\\text{N}_2(g) + 3\\text{H}_2(g) \\rightleftharpoons 2\\text{NH}_3(g)$, which has $4\\text{ moles}$ of gas on the reactant side and $2\\text{ moles}$ of gas on the product side ($\\Delta n_{\\text{gas}} = 2 - 4 = -2$). Halving the volume of the container doubles total pressure and the partial pressures of all gaseous species. The reaction quotient immediately becomes $Q_p = \\frac{(2 P_{\\text{NH3}})^2}{(2 P_{\\text{N2}})(2 P_{\\text{H2}})^3} = \\frac{4 P_{\\text{NH3}}^2}{16 P_{\\text{N2}} P_{\\text{H2}}^3} = \\frac{1}{4} K_p < K_p$. By Le Châtelier's principle, the system shifts toward the side with fewer gas molecules (the forward direction, producing more $\\text{NH}_3$) to relieve the applied pressure increase.<br><br><em>Distractor Traps:</em><br>&bull; A claims the equilibrium constant $K_p$ changes; equilibrium constants depend strictly on temperature, not on volume or pressure.<br>&bull; C directionally inverts the Le Châtelier shift, claiming it favors the side with more moles of gas (reactants).<br>&bull; D asserts partial pressures decrease upon halving volume; Boyle's Law ($P \\propto 1/V$) dictates partial pressures double."
      },
      {
        "q": "If argon gas is injected into the sealed rigid bioreactor containing the ammonia equilibrium at constant volume, what effect is observed?",
        "ch": [
          "The equilibrium shifts toward reactants because the total pressure of the container has risen",
          "The equilibrium shifts toward products because argon forms van der Waals complexes with nitrogen",
          "The equilibrium position is unaffected because reactant and product partial pressures do not change",
          "The value of Kp decreases because inert collision partners alter the reaction activation barrier"
        ],
        "a": 2,
        "e": "<strong>Inert gas addition at constant volume in chemical equilibria (Topic 400):</strong> Adding an inert gas (such as Argon) to a rigid container at constant volume increases the total pressure ($P_{\\text{total}} = P_{\\text{gas}} + P_{\\text{Ar}}$). However, according to Dalton's Law of Partial Pressures, the partial pressure of each reacting gas is $P_i = \\frac{n_i R T}{V}$. Because neither the moles of reacting gases ($n_i$), the absolute temperature ($T$), nor the container volume ($V$) have changed, the partial pressures of $\\text{N}_2$, $\\text{H}_2$, and $\\text{NH}_3$ remain entirely invariant. Consequently, the reaction quotient $Q_p$ remains exactly equal to $K_p$, and the chemical equilibrium position does not shift.<br><br><em>Distractor Traps:</em><br>&bull; A mistakenly assumes that an increase in total pressure always shifts equilibrium, overlooking that individual partial pressures are unchanged.<br>&bull; B falsely claims argon forms chemical complexes with molecular nitrogen; argon is a chemically inert noble gas.<br>&bull; D asserts $K_p$ decreases; equilibrium constants depend solely on temperature and are completely unaffected by inert collision partners."
      },
      {
        "q": "For the gas-phase reaction N2(g) + 3 H2(g) <=> 2 NH3(g) at 500 K, which mathematical formula correctly relates Kp to Kc?",
        "ch": [
          "Kp = Kc * (RT)^2",
          "Kp = Kc * (RT)^4",
          "Kp = Kc * (RT)^1",
          "Kp = Kc * (RT)^-2"
        ],
        "a": 3,
        "e": "<strong>Relationship between Kp and Kc for gas-phase equilibria (Topic 399):</strong> For an ideal gas reaction, partial pressure relates to molar concentration by $P_i = [C_i] R T$. Substituting this into the mass action expression yields the relationship: $K_p = K_c (RT)^{\\Delta n_{\\text{gas}}}$, where $\\Delta n_{\\text{gas}} = \\sum n_{\\text{gas, products}} - \\sum n_{\\text{gas, reactants}}$. For the synthesis of ammonia: $\\text{N}_2(g) + 3\\text{H}_2(g) \\rightleftharpoons 2\\text{NH}_3(g)$, the stoichiometric coefficients give $\\Delta n_{\\text{gas}} = 2 - (1 + 3) = 2 - 4 = -2$. Therefore, $K_p = K_c (RT)^{-2} = \\frac{K_c}{(RT)^2}$.<br><br><em>Distractor Traps:</em><br>&bull; A computes $\\Delta n_{\text{gas}} = +2$, directionally inverting the subtraction ($4 - 2$).<br>&bull; B sums all gaseous stoichiometric coefficients ($1 + 3 + 2 = 6$) or uses total reactant moles ($4$).<br>&bull; C assumes $\\Delta n_{\text{gas}} = 1$, representing a reaction with an unequal stoichiometric shift."
      },
      {
        "q": "Why is liquid water omitted from the equilibrium mass action expression for ATP hydrolysis (ATP + H2O <=> ADP + Pi) in dilute aqueous solution?",
        "ch": [
          "Water is the solvent in vast excess, so its activity is effectively unity and its concentration is constant",
          "Water molecules do not participate directly in the transition state or chemical bond cleavage mechanisms",
          "Water possesses an equilibrium vapor pressure of zero under standard physiological assay conditions tested",
          "Water is a pure substance whose chemical potential remains zero across all chemical solution transitions"
        ],
        "a": 0,
        "e": "<strong>Convention for solvents and pure liquids in the Law of Mass Action (Topic 399):</strong> In dilute aqueous solutions (where solute concentrations are typically $\\le 10\\text{ mM}$), water acts as the solvent in overwhelming excess ($[\\text{H}_2\\text{O}] \\approx 55.5\\text{ M}$). During the course of the reaction, the concentration of water changes by an imperceptible fraction ($< 0.02\\%$), remaining essentially constant. By thermodynamic convention, the thermodynamic activity of a pure liquid or solvent in a dilute solution is defined as unity ($a_{\\text{H2O}} \\approx 1$). Because its activity is incorporated directly into the standard equilibrium constant ($K_{\\text{eq}}$), $[\\text{H}_2\\text{O}]$ is omitted from the mass action quotient.<br><br><em>Distractor Traps:</em><br>&bull; B falsely asserts water does not participate in bond cleavage; water is a nucleophile that directly attacks the gamma phosphate in the transition state.<br>&bull; C asserts water vapor pressure is zero; liquid water has a significant vapor pressure ($47.1\text{ mmHg}$ at $37^\\circ\text{C}$).<br>&bull; D claims chemical potential of water is zero; chemical potential of a substance is non-zero and depends on temperature, pressure, and activity."
      }
    ]
  },
  {
    "id": "exam_cp60_9_p5",
    "sec": "C/P",
    "topic": "Henry's Law (Decompression Sickness), Raoult's Law & Colligative Freezing Point Depression/Osmotic Pressure",
    "sheet": 5,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_9",
    "passage": "<div class=\"ttl\">Passage 5 (Questions 25&ndash;30)</div>\n<p>The physical chemistry of gas dissolution and colligative properties governs diving physiology and hyperosmolar intravenous therapy. When a scuba diver breathes compressed air ($78\\%\\text{ N}_2, 21\\%\\text{ O}_2$) underwater, ambient hydrostatic pressure increases by approximately $1.0\\text{ atm}$ for every $10\\text{ meters}$ of seawater depth ($P_{\\text{total}} = 1.0\\text{ atm} + d/10$). The concentration of gas dissolved in blood plasma and lipid-rich myelin sheaths obeys Henry's Law:</p>\n$$C = k_H P_{\\text{gas}}$$\n<p>where $k_H$ is Henry's solubility constant ($k_H = 0.64\\text{ mM/atm}$ for $\\text{N}_2$ in plasma at $37^\\circ\\text{C}$). During rapid, uncontrolled ascent, ambient pressure drops precipitously while dissolved gas cannot diffuse out through the pulmonary alveoli rapidly enough. The blood becomes supersaturated, causing nitrogen gas to nucleate into microscopic bubbles in venous capillaries, joints, and nervous tissue, causing decompression sickness ('the bends').</p>\n<p>In clinical emergency care, colligative properties govern fluid resuscitation and osmotherapy. Raoult's Law dictates that dissolving a non-volatile solute lowers solvent vapor pressure proportionally to solvent mole fraction:</p>\n$$P_{\\text{solution}} = X_{\\text{solvent}} P^\\circ_{\\text{solvent}}$$\n<p>Lowering vapor pressure elevates boiling point ($\\Delta T_b = i K_b m$) and depresses freezing point:</p>\n$$\\Delta T_f = i K_f m$$\n<p>where $K_f = 1.86^\\circ\\text{C}\\cdot\\text{kg/mol}$ for water, $m$ is molality, and $i$ is the van 't Hoff factor reflecting particle dissociation. Osmotic pressure ($\\Pi$) across semipermeable biological membranes follows the Morse equation:</p>\n$$\\Pi = i M R T$$\n<p>In acute cerebral edema, hypertonic $20\\%\\text{ w/v}$ mannitol ($1.10\\text{ M}$, $i = 1$) is infused intravenously. Because the blood-brain barrier is impermeable to mannitol, an osmotic pressure gradient draws excess interstitial and intracellular water from swollen neuronal parenchyma into the vascular space (Table 5).</p>\n<table class=\"tbl\">\n  <caption>Table 5 Hydrostatic pressure, nitrogen solubility, and colligative osmometry parameters of physiological solutions at 310 K</caption>\n  <thead>\n    <tr><th>Solution / Physiological Condition</th><th>Depth / Hydrostatic Pressure (atm)</th><th>Dissolved N2 (mM)</th><th>Solute Molality (mol/kg)</th><th>Van 't Hoff Factor (i)</th><th>Freezing Point Tf (°C)</th><th>Osmotic Pressure Π (atm at 310 K)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Sea level arterial blood (Air)</td><td>Surface (1.0 atm)</td><td>0.50 &plusmn; 0.02</td><td>0.30 &plusmn; 0.01</td><td>1.00</td><td>-0.56 &plusmn; 0.02</td><td>7.6 &plusmn; 0.2</td></tr>\n    <tr><td>Hyperbaric dive blood (30 m depth)</td><td>Depth 30 m (4.0 atm)</td><td>2.00 &plusmn; 0.08</td><td>0.30 &plusmn; 0.01</td><td>1.00</td><td>-0.56 &plusmn; 0.02</td><td>7.6 &plusmn; 0.2</td></tr>\n    <tr><td>Normal saline (0.9% w/v NaCl)</td><td>Surface (1.0 atm)</td><td>0.50 &plusmn; 0.02</td><td>0.154</td><td>1.86 &plusmn; 0.02</td><td>-0.53 &plusmn; 0.02</td><td>7.3 &plusmn; 0.2</td></tr>\n    <tr><td>Mannitol infusion (20% w/v)</td><td>Surface (1.0 atm)</td><td>0.50 &plusmn; 0.02</td><td>1.100</td><td>1.00</td><td>-2.05 &plusmn; 0.05</td><td>28.0 &plusmn; 0.8</td></tr>\n    <tr><td>Calcium chloride (0.10 m CaCl2)</td><td>Surface (1.0 atm)</td><td>&mdash;</td><td>0.100</td><td>2.65 &plusmn; 0.04</td><td>-0.49 &plusmn; 0.02</td><td>6.7 &plusmn; 0.2</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "A scuba diver descends to a depth of 30 meters where total ambient pressure is 4.0 atm. Assuming air is 78% N2 and k_H = 0.64 mM/atm, what is the dissolved N2 concentration in plasma?",
        "ch": [
          "Approximately 0.50 mM",
          "Approximately 0.82 mM",
          "Approximately 2.00 mM",
          "Approximately 5.12 mM"
        ],
        "a": 2,
        "e": "<strong>Calculation of gas solubility using Henry's Law (Topic 401):</strong> Henry's Law states that the dissolved gas concentration is directly proportional to its partial pressure above the solution: $C = k_H P_{\\text{gas}}$. First, calculate the partial pressure of nitrogen gas ($P_{\\text{N2}}$) at $30\\text{ m}$ depth, where total pressure is $4.0\\text{ atm}$: $P_{\\text{N2}} = X_{\\text{N2}} \\cdot P_{\\text{total}} = 0.78 \\times 4.0\\text{ atm} = 3.12\\text{ atm}$. Next, apply Henry's Law: $C_{\\text{N2}} = (0.64\\text{ mM/atm})(3.12\\text{ atm}) = 1.9968\\text{ mM} \\approx 2.00\\text{ mM}$. This 4-fold increase in dissolved nitrogen over sea level ($0.50\\text{ mM}$) creates the supersaturation hazard during rapid ascent.<br><br><em>Distractor Traps:</em><br>&bull; A reports sea-level dissolved nitrogen concentration ($0.50\text{ mM}$) at $1.0\text{ atm}$.<br>&bull; B calculates $0.64 / 0.78 = 0.82\text{ mM}$, dividing Henry's constant by mole fraction.<br>&bull; D multiplies total pressure by another factor of 2 or forgets the $0.78$ fraction ($0.64 \times 8$).\n"
      },
      {
        "q": "According to Raoult's Law (P_soln = X_solvent * P°_solvent), why does dissolving non-volatile mannitol in water reduce equilibrium vapor pressure?",
        "ch": [
          "Mannitol molecules decompose water molecules into non-volatile hydroxyl radicals at the solution surface",
          "Mannitol particles absorb ambient radiant heat, substantially cooling the bulk liquid solution surface",
          "Mannitol crystals precipitate at the meniscus, forming an impermeable mechanical barrier to evaporation",
          "Mannitol particles reduce solvent mole fraction and increase the entropy of the liquid solution mixture"
        ],
        "a": 3,
        "e": "<strong>Molecular and thermodynamic mechanism of Raoult's Law (Topic 402):</strong> Raoult's Law states that $P_{\\text{solution}} = X_{\\text{solvent}} P^\\circ_{\\text{solvent}}$. In a pure solvent, $100\\%$ of the surface area is occupied by volatile solvent molecules, which can escape into the vapor phase. When non-volatile solute particles (such as mannitol) are dissolved, they occupy surface positions, reducing the frequency of solvent molecules striking and escaping from the liquid-gas interface. Thermodynamically, dissolving solute particles increases the entropy ($S$) of the liquid mixture relative to the pure liquid, lowering the solvent's chemical potential ($\\mu_{\\text{liquid}}$) and decreasing its escaping tendency into the gas phase.<br><br><em>Distractor Traps:</em><br>&bull; A falsely asserts that mannitol decomposes water into free radicals; dissolution is a physical non-reactive process.<br>&bull; B claims solute cools the surface by absorbing radiant heat; vapor pressure lowering occurs isothermally at constant temperature.<br>&bull; C posits mechanical precipitation of crystals; mannitol remains fully dissolved in solution without forming surface crystals."
      },
      {
        "q": "Which aqueous solution will exhibit the greatest freezing point depression (lowest freezing temperature) assuming complete ionic dissociation?",
        "ch": [
          "0.10 m AlCl3",
          "0.10 m CaCl2",
          "0.10 m NaCl",
          "0.10 m Urea"
        ],
        "a": 0,
        "e": "<strong>Colligative freezing point depression and van 't Hoff factor comparison (Topic 403):</strong> Freezing point depression is given by $\\Delta T_f = i K_f m$, where $i$ is the van 't Hoff factor and $m$ is molality. Because $K_f$ is identical for all aqueous solutions and all solutions have $m = 0.10\\text{ m}$, the solution with the largest effective particle concentration ($i \\cdot m$) will produce the greatest $\\Delta T_f$ (and lowest freezing point):<br>&bull; $\\text{AlCl}_3 \\to \\text{Al}^{3+} + 3\\text{Cl}^- \\implies i = 4 \\implies i \\cdot m = 0.40\\text{ m}$<br>&bull; $\\text{CaCl}_2 \\to \\text{Ca}^{2+} + 2\\text{Cl}^- \\implies i = 3 \\implies i \\cdot m = 0.30\\text{ m}$<br>&bull; $\\text{NaCl} \\to \\text{Na}^+ + \\text{Cl}^- \\implies i = 2 \\implies i \\cdot m = 0.20\\text{ m}$<br>&bull; Urea is non-ionic $\\implies i = 1 \\implies i \\cdot m = 0.10\\text{ m}$.<br>Therefore, $0.10\\text{ m AlCl}_3$ exhibits the greatest freezing point depression.<br><br><em>Distractor Traps:</em><br>&bull; B represents $i = 3$ ($0.30\text{ m}$ particles), which is less than $\text{AlCl}_3$.<br>&bull; C represents $i = 2$ ($0.20\text{ m}$ particles), yielding smaller freezing depression.<br>&bull; D represents $i = 1$ ($0.10\text{ m}$ particles), yielding the smallest freezing depression."
      },
      {
        "q": "A 0.50 m aqueous solution of sodium chloride (NaCl, i = 1.90) is frozen. Given Kf for water is 1.86 °C·kg/mol, what is the predicted freezing point?",
        "ch": [
          "Exactly -0.93 °C",
          "Exactly -1.77 °C",
          "Exactly -3.53 °C",
          "Exactly -5.32 °C"
        ],
        "a": 1,
        "e": "<strong>Calculation of freezing point depression for an electrolyte solution (Topic 403):</strong> The freezing point depression is given by $\\Delta T_f = i K_f m$. Using the provided values ($i = 1.90$, $K_f = 1.86^\\circ\\text{C}\\cdot\\text{kg/mol}$, and $m = 0.50\\text{ mol/kg}$): $\\Delta T_f = (1.90)(1.86^\\circ\\text{C}\\cdot\\text{kg/mol})(0.50\\text{ mol/kg}) = 1.767^\\circ\\text{C} \\approx 1.77^\\circ\\text{C}$. Because the normal freezing point of pure water is $0.00^\\circ\\text{C}$, the solution freezes at $T_f = 0.00^\\circ\\text{C} - \\Delta T_f = -1.77^\\circ\\text{C}$.<br><br><em>Distractor Traps:</em><br>&bull; A omits the van 't Hoff factor $i = 1.90$, calculating $\\Delta T_f = 1.86 \times 0.50 = 0.93^\\circ\text{C}$ (freezing point $-0.93^\\circ\text{C}$).<br>&bull; C doubles the molality or computes $(1.90)(1.86) \u0007pprox 3.53^\\circ\text{C}$.<br>&bull; D multiplies by $i = 3$ or sums $(3.53 + 1.77) = 5.30^\\circ\text{C}$."
      },
      {
        "q": "How does an intravenous infusion of 20% mannitol reduce intracranial pressure in a patient suffering from acute traumatic cerebral edema?",
        "ch": [
          "Mannitol enters astrocytes via facilitated diffusion, where it hydrolyzes intracellular lactic acid",
          "Mannitol dilates cerebral capillaries, dramatically increasing intracranial venous blood volume",
          "Mannitol cannot cross the intact blood-brain barrier, drawing water osmotically into the vasculature",
          "Mannitol binds directly to neuronal GABA receptors, suppressing excessive electrical depolarization"
        ],
        "a": 2,
        "e": "<strong>Osmotic pressure and clinical osmotherapy across the blood-brain barrier (Topic 403):</strong> Mannitol is a six-carbon polyol sugar alcohol that cannot penetrate the tight junctions of an intact blood-brain barrier (reflection coefficient $\\sigma \\approx 1.0$). When hypertonic $20\\%\\text{ w/v}$ mannitol ($1.10\\text{ M}$, creating an osmotic pressure of $\\approx 28\\text{ atm}$) is infused intravenously, it markedly elevates the effective intravascular osmolarity relative to the brain parenchyma. In accordance with the Morse osmotic pressure relationship ($\\Pi = i M R T$), this establishes a steep transendothelial osmotic gradient that draws excess interstitial and intracellular water out of swollen cerebral tissue and into the capillary lumen, effectively reducing intracranial pressure (ICP).<br><br><em>Distractor Traps:</em><br>&bull; A falsely asserts mannitol enters astrocytes; the therapeutic mechanism depends strictly on mannitol's inability to cross the blood-brain barrier.<br>&bull; B claims mannitol increases intracranial venous blood volume; expanding intracranial volume would dangerously elevate intracranial pressure according to the Monro-Kellie doctrine.<br>&bull; D describes neuroactive sedatives or anticonvulsants (such as propofol or benzodiazepines), not hyperosmolar crystalloids."
      },
      {
        "q": "In concentrated solutions of divalent salts such as MgSO4, measured van 't Hoff factors (i = 1.30) are lower than theoretical values (i = 2.00). Why?",
        "ch": [
          "Divalent sulfate anions evaporate rapidly into the gas headspace above the liquid solution surface",
          "Magnesium ions undergo spontaneous radioactive decay, decreasing total dissolved particle counts",
          "Water molecules coordinate covalently with magnesium, forming an insoluble crystalline precipitate",
          "Oppositely charged ions form electrostatic ion pairs in solution, reducing effective particle counts"
        ],
        "a": 3,
        "e": "<strong>Ion pairing and deviations from ideal colligative behavior (Topic 403):</strong> In an ideal infinitely dilute solution, $\\text{MgSO}_4$ dissociates completely into $\\text{Mg}^{2+}$ and $\\text{SO}_4^{2-}$, yielding a theoretical van 't Hoff factor of $i = 2.00$. However, in real and concentrated solutions, divalent ions carry high charge densities ($z = \\pm 2$). According to Coulomb's Law ($F \\propto z_+ z_- / r^2$), electrostatic attraction between oppositely charged multivalent ions is four times stronger than between monovalent ions. Consequently, a substantial fraction of $\\text{Mg}^{2+}$ and $\\text{SO}_4^{2-}$ ions associate transiently into neutral electrostatic ion pairs $[\\text{Mg}^{2+}\\text{SO}_4^{2-}]^0$. Because these ion pairs behave as single kinetic particles, the effective particle concentration decreases, lowering the observed van 't Hoff factor ($i_{\\text{meas}} = 1.30$).<br><br><em>Distractor Traps:</em><br>&bull; A asserts non-volatile ionic sulfate anions evaporate into the headspace, which is physically impossible.<br>&bull; B invokes radioactive decay, which does not occur in non-radioactive stable magnesium isotopes.<br>&bull; C claims magnesium sulfate forms an insoluble precipitate; $\text{MgSO}_4$ is highly water-soluble."
      }
    ]
  },
  {
    "id": "exam_cp60_9_disc",
    "sec": "C/P",
    "topic": "C/P Standalone Discrete Questions",
    "sheet": 8,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_9",
    "passage": "<div class=\"ttl\">Item Set (Questions 43&ndash;52)</div>\n<p><strong>Directions:</strong> Questions 43&ndash;52 are standalone questions that are not based on a passage. Select the single best answer to each question.</p>",
    "qs": [
      {
        "d": true,
        "q": "In a standard galvanic (voltaic) cell composed of a zinc anode in ZnSO4 and a copper cathode in CuSO4 linked by a KCl salt bridge, how do ions migrate?",
        "ch": [
          "Chloride anions migrate toward the zinc anode while potassium cations migrate toward the copper cathode",
          "Potassium cations migrate toward the zinc anode while chloride anions migrate toward the copper cathode",
          "Both chloride and potassium ions migrate exclusively toward the zinc anode to prevent metal deposition",
          "Salt bridge ions remain stationary while electrons flow through the liquid electrolyte between vessels"
        ],
        "a": 0,
        "e": "<strong>Salt bridge ion flux and electroneutrality in galvanic cells (Topic 411):</strong> In a standard galvanic cell, oxidation occurs at the anode ('AN OX'): $\\text{Zn}(s) \\to \\text{Zn}^{2+}(aq) + 2e^-$. As zinc metal dissolves, positive $\\text{Zn}^{2+}$ cations accumulate in the anode compartment. Reduction occurs at the cathode ('RED CAT'): $\\text{Cu}^{2+}(aq) + 2e^- \\to \\text{Cu}(s)$, depleting positive $\\text{Cu}^{2+}$ cations and leaving behind excess $\\text{SO}_4^{2-}$ anions. To maintain electrical neutrality and allow sustained current flow, salt bridge anions ($\\text{Cl}^-$) migrate toward the anode compartment to balance accumulating $\\text{Zn}^{2+}$, while salt bridge cations ($\\text{K}^+$) migrate toward the cathode compartment to replace consumed $\\text{Cu}^{2+}$.<br><br><em>Distractor Traps:</em><br>&bull; B directionally inverts ion migration, which would exacerbate charge buildup and immediately halt cell current.<br>&bull; C claims both ions migrate to the anode, violating physical electroneutrality in the cathode.<br>&bull; D falsely claims ions remain stationary and electrons flow through liquid; electrons travel through the external wire, while ions carry current through electrolytes."
      },
      {
        "d": true,
        "q": "Given standard reduction potentials E°(Ag+/Ag) = +0.80 V and E°(Ni2+/Ni) = -0.25 V, what is E°cell for: Ni(s) + 2 Ag+(aq) -> Ni2+(aq) + 2 Ag(s)?",
        "ch": [
          "Exactly +0.55 V",
          "Exactly +1.05 V",
          "Exactly +1.35 V",
          "Exactly +1.85 V"
        ],
        "a": 1,
        "e": "<strong>Calculation of standard cell potential from reduction potentials (Topic 412):</strong> The standard cell potential is calculated using: $E^\\circ_{\\text{cell}} = E^\\circ_{\\text{cathode}} - E^\\circ_{\\text{anode}}$ (where both potentials are standard reduction potentials). In the provided reaction: $\\text{Ni}(s) + 2\\text{Ag}^+(aq) \\to \\text{Ni}^{2+}(aq) + 2\\text{Ag}(s)$, silver is reduced at the cathode ($\\text{Ag}^+ + e^- \\to \\text{Ag}$, $E^\\circ = +0.80\\text{ V}$), and nickel is oxidized at the anode ($\\text{Ni} \\to \\text{Ni}^{2+} + 2e^-$, $E^\\circ_{\\text{red}} = -0.25\\text{ V}$). Crucially, standard reduction potential is an intensive property and must NEVER be multiplied by stoichiometric coefficients. Substituting: $E^\\circ_{\\text{cell}} = +0.80\\text{ V} - (-0.25\\text{ V}) = +0.80 + 0.25 = +1.05\\text{ V}$.<br><br><em>Distractor Traps:</em><br>&bull; A erroneously subtracts $+0.80 - 0.25 = +0.55\text{ V}$, forgetting that subtracting a negative number yields addition.<br>&bull; C incorrectly multiplies the silver potential by stoichiometric coefficient $2$ before subtracting: $2(0.80) - 0.25 = 1.35\text{ V}$.<br>&bull; D multiplies by $2$ and adds: $2(0.80) + 0.25 = 1.85\text{ V}$."
      },
      {
        "d": true,
        "q": "For an electrochemical cell operating with a standard potential of E°cell = +1.10 V and transferring 2 moles of electrons, what is Delta G°?",
        "ch": [
          "Approximately +212 kJ/mol",
          "Approximately +106 kJ/mol",
          "Approximately -212 kJ/mol",
          "Approximately -106 kJ/mol"
        ],
        "a": 2,
        "e": "<strong>Relationship between standard cell potential and Gibbs free energy (Topic 413):</strong> The relationship between cell potential and standard free energy is given by $\\Delta G^\\circ = -n F E^\\circ_{\\text{cell}}$, where $n$ is the moles of electrons transferred and $F$ is Faraday's constant ($96,485\\text{ C/mol }e^- \\approx 96,500\\text{ J/(V}\\cdot\\text{mol)}$). Given $n = 2$ and $E^\\circ_{\\text{cell}} = +1.10\\text{ V}$: $\\Delta G^\\circ = -(2)(96,500\\text{ C/mol})(1.10\\text{ V}) = -212,300\\text{ J/mol} \\approx -212\\text{ kJ/mol}$. A positive standard cell potential ($E^\\circ > 0$) corresponds directly to a negative standard free energy change ($\\Delta G^\\circ < 0$), confirming thermodynamic spontaneity under standard conditions.<br><br><em>Distractor Traps:</em><br>&bull; A makes a sign error, omitting the negative sign in $\\Delta G^\\circ = -nFE^\\circ$ and reporting $+212\text{ kJ/mol}$.<br>&bull; B omits $n = 2$ and makes a sign error, calculating $+106\text{ kJ/mol}$.<br>&bull; D omits the stoichiometric electron factor $n = 2$, calculating $-(1)(96,500)(1.10) = -106\text{ kJ/mol}$."
      }
    ]
  }
];

if (typeof window !== 'undefined') {
  window.EXAM_CP60_9 = EXAM_CP60_9;
}
if (typeof globalThis !== 'undefined') {
  globalThis.EXAM_CP60_9 = EXAM_CP60_9;
}
