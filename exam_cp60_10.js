/* ---- exam_cp60_10.js ---- */
/* 60-minute Chem/Physical Practice Exam 10: 5 passages (30 Qs) + 3 discrete Qs = 33 Qs */
const EXAM_CP60_10 = [
  {
    "id": "exam_cp60_10_p1",
    "sec": "C/P",
    "topic": "Lithium-Ion Battery Intercalation Dynamics and Lead-Acid Secondary Cell Electrochemistry",
    "sheet": 1,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_10",
    "passage": "<div class=\"ttl\">Passage 1 (Questions 1&ndash;6)</div>\n<p>Rechargeable secondary electrochemical cells store electrical energy chemically through reversible reduction-oxidation reactions, discharging spontaneously as galvanic cells and recharging non-spontaneously under external potential as electrolytic cells. In a commercial lithium-ion secondary cell, the negative electrode consists of graphitic carbon ($Li_x C_6$), while the positive electrode consists of layered lithium cobalt oxide ($Li_{1-x}CoO_2$). The electrodes are separated by a porous polymer membrane and an anhydrous non-aqueous organic electrolyte ($1.0\\text{ M } LiPF_6$ in ethylene carbonate / dimethyl carbonate).</p>\n<p>During galvanic discharge, lithium ions spontaneously deintercalate from the graphite host lattice ($\\text{LiC}_6 \\to \\text{C}_6 + \\text{Li}^+ + e^-$) and migrate through the organic electrolyte toward the cathode. Simultaneously, electrons travel through the external circuit to reduce cobalt ions as lithium intercalates into the metal oxide ($CoO_2 + \\text{Li}^+ + e^- \\to \\text{LiCoO}_2$). During external recharge, an applied direct-current voltage forces electrons into the graphite electrode, driving non-spontaneous lithium re-intercalation while cobalt is oxidized at the positive terminal.</p>\n<p>By contrast, secondary lead-acid cells utilize a lead metal anode and a lead(IV) oxide ($PbO_2$) cathode submerged in aqueous sulfuric acid ($4.5\\text{ M } H_2SO_4$). During discharge, both electrodes are converted into insoluble lead(II) sulfate ($PbSO_4$):</p>\n$$\\text{Pb}(s) + \\text{PbO}_2(s) + 2\\text{H}_2\\text{SO}_4(aq) \\rightleftharpoons 2\\text{PbSO}_4(s) + 2\\text{H}_2\\text{O}(l)$$\n<p>During electrolytic charging, the generator drives the reverse non-spontaneous reaction, regenerating sulfuric acid and restoring electrolyte density.</p>\n<p>Physical electrochemists evaluated lithium-ion and lead-acid test cells using cyclic voltammetry at a scan rate of $0.10\\text{ mV/s}$ and galvanostatic cycling across variable operating temperatures. Table 1 summarizes the open-circuit potentials ($E_{\\text{ocv}}$), peak redox voltages, charge-transfer overpotentials ($\\eta$), and Coulombic efficiencies.</p>\n<table class=\"tbl\">\n  <caption>Table 1 Cyclic voltammetry redox parameters, cell potentials, overpotentials, and Coulombic efficiencies of secondary test cells</caption>\n  <thead>\n    <tr><th>Cell System</th><th>Operating Temp (°C)</th><th>Anodic Peak Epa (V)</th><th>Cathodic Peak Epc (V)</th><th>Open-Circuit Eocv (V)</th><th>Overpotential Eta (V)</th><th>Coulombic Efficiency (%)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Li-ion (LiCoO2 / C6)</td><td>25</td><td>+4.18</td><td>+3.88</td><td>+4.05</td><td>0.15</td><td>99.2 ± 0.3</td></tr>\n    <tr><td>Li-ion (LiCoO2 / C6)</td><td>0</td><td>+4.32</td><td>+3.70</td><td>+4.02</td><td>0.31</td><td>94.6 ± 0.5</td></tr>\n    <tr><td>Li-ion (LiCoO2 / C6)</td><td>45</td><td>+4.12</td><td>+3.94</td><td>+4.07</td><td>0.09</td><td>98.8 ± 0.4</td></tr>\n    <tr><td>Lead-Acid (PbO2 / Pb)</td><td>25</td><td>+2.24</td><td>+1.86</td><td>+2.05</td><td>0.19</td><td>88.5 ± 0.8</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "During the recharging of a lithium-ion battery via an external DC power source, what are the identity and electrical polarity of the graphite electrode?",
        "ch": [
          "It acts as an electrolytic cathode and carries negative electrical polarity",
          "It acts as an electrolytic anode and carries positive electrical polarity",
          "It acts as a galvanic cathode and maintains a positive electrical charge",
          "It acts as a galvanic anode and maintains a negative electrical polarity"
        ],
        "a": 0,
        "e": "<strong>Electrode polarity and functions during electrolytic recharging (Topic 415):</strong> Recharging a secondary battery requires an external power supply, converting the device into an electrolytic cell. Reduction always occurs at the cathode ('RED CAT'). During recharging, lithium cations must be reduced and re-intercalated into the graphite lattice: $\\text{C}_6 + \\text{Li}^+ + e^- \\to \\text{LiC}_6$. Because the external direct-current power supply pumps electrons onto the graphite electrode to drive this non-spontaneous reduction, the graphite electrode functions as the electrolytic cathode and carries a negative electrical polarity.<br><br><em>Distractor Traps:</em><br>&bull; B confuses cathode and anode; oxidation occurs at the anode, whereas graphite undergoes reduction during charging.<br>&bull; C incorrectly identifies the charging mode as galvanic rather than electrolytic.<br>&bull; D falsely claims the electrode acts as a galvanic anode, which only occurs during spontaneous discharge."
      },
      {
        "q": "During galvanic discharge of the lead-acid accumulator cell, what change occurs to the liquid electrolyte density and why?",
        "ch": [
          "Density rises because lead sulfate dissolves, releasing dense heavy cations into solution",
          "Density falls because sulfuric acid is consumed to produce water and solid lead sulfate",
          "Density stays constant because hydronium ions migrate without net molar mass changes",
          "Density falls because sulfuric acid evaporates rapidly as gaseous sulfur trioxide gas"
        ],
        "a": 1,
        "e": "<strong>Electrolyte density dynamics in lead-acid battery discharge (Topic 416):</strong> The overall discharge reaction of a lead-acid battery is: $\\text{Pb}(s) + \\text{PbO}_2(s) + 2\\text{H}_2\\text{SO}_4(aq) \\to 2\\text{PbSO}_4(s) + 2\\text{H}_2\\text{O}(l)$. Sulfuric acid is a dense solute (concentrated aqueous $\\text{H}_2\\text{SO}_4$ has a specific gravity of $\\approx 1.28\\text{ g/cm}^3$). During spontaneous discharge, aqueous sulfuric acid is continuously consumed to form solid, insoluble lead(II) sulfate precipitate and less dense liquid water ($1.00\\text{ g/cm}^3$). Consequently, hydrometer measurements demonstrate a pronounced drop in electrolyte density during discharge, which serves as a diagnostic indicator of battery state-of-charge.<br><br><em>Distractor Traps:</em><br>&bull; A falsely asserts lead sulfate is soluble and increases liquid density; $\\text{PbSO}_4$ is an insoluble precipitate ($K_{sp} \\approx 1.6 \\times 10^{-8}$).<br>&bull; C incorrectly claims electrolyte density remains constant despite stoichiometric consumption of dense $\\text{H}_2\\text{SO}_4$.<br>&bull; D proposes gas evaporation of $\\text{SO}_3$, which does not occur under normal battery operating conditions."
      },
      {
        "q": "If an industrial electroplating cell decomposes molten magnesium chloride (MgCl2) with a steady current of 9.65 A for 10,000 seconds, what mass of pure magnesium metal (molar mass = 24.3 g/mol) is deposited at the cathode? (Faraday's constant F = 96,500 C/mol e-)",
        "ch": [
          "Exactly 24.3 grams of magnesium metal",
          "Exactly 48.6 grams of magnesium metal",
          "Exactly 12.2 grams of magnesium metal",
          "Exactly 6.08 grams of magnesium metal"
        ],
        "a": 2,
        "e": "<strong>Faraday's law of electrolysis and quantitative deposition (Topic 415):</strong> According to Faraday's law of electrolysis, the total charge passed is $Q = I \\cdot t = (9.65\\text{ A})(10,000\\text{ s}) = 96,500\\text{ C}$. The moles of electrons transferred equals: $n_e = \\frac{Q}{F} = \\frac{96,500\\text{ C}}{96,500\\text{ C/mol }e^-} = 1.00\\text{ mol }e^-$. The cathodic reduction of magnesium from molten $\\text{MgCl}_2$ requires two electrons per atom: $\\text{Mg}^{2+} + 2e^- \\to \\text{Mg}(s)$. Therefore, the moles of magnesium metal produced is: $n_{\\text{Mg}} = \\frac{1.00\\text{ mol }e^-}{2} = 0.500\\text{ mol }\\text{Mg}$. The deposited mass is: $m = (0.500\\text{ mol})(24.3\\text{ g/mol}) = 12.15\\text{ g} \\approx 12.2\\text{ g}$.<br><br><em>Distractor Traps:</em><br>&bull; A forgets the stoichiometric valence factor $n = 2$ for divalent $\\text{Mg}^{2+}$, calculating $(1.00)(24.3) = 24.3\\text{ g}$.<br>&bull; B erroneously multiplies by 2 instead of dividing by the valence electron count, obtaining $48.6\\text{ g}$.<br>&bull; D mistakenly divides by $n = 4$, obtaining $6.08\\text{ g}$."
      },
      {
        "q": "Based on Table 1, why does lowering the temperature from 25 °C to 0 °C increase the overpotential (eta) from 0.15 V to 0.31 V in the lithium-ion cell?",
        "ch": [
          "Lower temperatures accelerate cobalt dissolution, creating thick metallic bridges",
          "Lower temperatures reduce thermodynamic cell voltage by shifting standard enthalpy",
          "Lower temperatures promote rapid spontaneous gas evolution at the negative plate",
          "Lower temperatures increase internal ohmic resistance and retard ionic migration"
        ],
        "a": 3,
        "e": "<strong>Temperature dependence of overpotential and kinetic activation (Topic 416):</strong> Electrochemical overpotential ($\\eta = |E - E_{\\text{eq}}|$) represents the extra potential required beyond thermodynamic equilibrium to overcome kinetic activation barriers, solid-state diffusion resistance, and internal ohmic resistance ($IR$ drop). Lowering the operating temperature to $0^\\circ\\text{C}$ increases the viscosity of the organic carbonate electrolyte, reduces the diffusion coefficient of $\\text{Li}^+$ ions through the electrolyte and solid-electrolyte interphase (SEI), and elevates charge-transfer resistance across electrode interfaces. These combined kinetic impediments manifest as a sharp increase in overpotential from $0.15\\text{ V}$ to $0.31\\text{ V}$.<br><br><em>Distractor Traps:</em><br>&bull; A describes severe long-term degradation or dendrite formation, not the immediate physical cause of elevated overpotential.<br>&bull; B confuses thermodynamic equilibrium potential ($E_{\\text{ocv}}$, which drops only minimally from $4.05\\text{ V}$ to $4.02\\text{ V}$) with kinetic overpotential $\\eta$.<br>&bull; C claims gas evolution increases at low temperatures; electrolyte gassing typically accelerates at elevated temperatures."
      },
      {
        "q": "Why must commercial lithium-ion batteries utilize anhydrous organic carbonates rather than aqueous electrolytes?",
        "ch": [
          "Metallic lithium and intercalated carbon react violently with water to generate H2 gas",
          "Water has a dielectric constant that completely inhibits ionic dissociation of salts",
          "Aqueous protons oxidize cobalt oxide to inactive metallic cobalt at cell potentials",
          "Water undergoes spontaneous polymerization into solid ice lattices at room ambient"
        ],
        "a": 0,
        "e": "<strong>Electrochemical stability window and water reactivity in lithium cells (Topic 416):</strong> The operating potential of commercial lithium-ion cells exceeds $4.0\\text{ V}$, which far surpasses the thermodynamic electrochemical stability window of liquid water ($1.23\\text{ V}$). Intercalated lithium in graphite ($\\text{LiC}_6$) has an extremely negative reduction potential ($E^\\circ \\approx -3.05\\text{ V}$ vs SHE), making it a ferocious reducing agent that spontaneously and violently reduces water to flammable hydrogen gas: $2\\text{LiC}_6 + 2\\text{H}_2\\text{O} \\to 2\\text{Li}^+ + 2\\text{OH}^- + \\text{H}_2(g) + 2\\text{C}_6$. Consequently, anhydrous aprotic organic carbonates (such as ethylene carbonate and dimethyl carbonate) must be used to provide an expanded electrochemical stability window ($> 4.5\\text{ V}$) devoid of acidic protons.<br><br><em>Distractor Traps:</em><br>&bull; B falsely claims water inhibits salt dissociation; water has an exceptionally high dielectric constant ($\\varepsilon \\approx 80$) that promotes ion dissociation.<br>&bull; C asserts aqueous protons reduce cobalt to metal; protons are reduced to $\\text{H}_2$ gas rather than reducing metal oxides.<br>&bull; D absurdly claims water polymerizes into ice at room temperature."
      },
      {
        "q": "In a cyclic voltammetry experiment, what does the peak separation Delta E_p = E_pa - E_pc signify regarding electrochemical reversibility?",
        "ch": [
          "A peak separation of zero millivolts proves the reaction is completely irreversible",
          "A separation close to 59 mV / n indicates a kinetically fast reversible redox couple",
          "Larger peak separation proves that electron transfer kinetics are infinitely fast",
          "Peak separation depends strictly on Faraday constant and is independent of kinetics"
        ],
        "a": 1,
        "e": "<strong>Diagnostic criteria for electrochemical reversibility in cyclic voltammetry (Topic 415):</strong> In cyclic voltammetry, a reversible Nernstian redox couple exhibits rapid heterogeneous electron transfer kinetics. At $25^\\circ\\text{C}$ ($298\\text{ K}$), the theoretical anodic-to-cathodic peak potential separation for a reversible process is: $\\Delta E_p = |E_{pa} - E_{pc}| = \\frac{2.303 RT}{nF} \\approx \\frac{59\\text{ mV}}{n}$, where $n$ is the number of electrons transferred. When electron transfer is sluggish (quasi-reversible or irreversible) or when uncompensated cell resistance is significant, overpotential shifts the anodic peak to more positive potentials and the cathodic peak to more negative potentials, widening $\\Delta E_p$ well beyond $59/n\\text{ mV}$.<br><br><em>Distractor Traps:</em><br>&bull; A asserts zero peak separation proves irreversibility; zero separation occurs in surface-confined ideal thin-layer adsorbate systems, never in irreversible diffusion couples.<br>&bull; C inverts the kinetic relationship; larger peak separation indicates slower, more hindered electron-transfer kinetics.<br>&bull; D falsely claims peak separation is independent of electron transfer rate kinetics."
      }
    ]
  },
  {
    "id": "exam_cp60_10_p2",
    "sec": "C/P",
    "topic": "Corrosion Kinetics of Structural Steel and Cathodic Protection via Sacrificial Galvanic Anodes",
    "sheet": 2,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_10",
    "passage": "<div class=\"ttl\">Passage 2 (Questions 7&ndash;12)</div>\n<p>Atmospheric and marine corrosion of structural carbon steel is a destructive electrochemical phenomenon driven by coupled galvanic micro-cells on the metallic surface. In aerated neutral or alkaline aqueous electrolytes, iron undergoes spontaneous oxidation at anodic micro-domains:</p>\n$$\\text{Fe}(s) \\to \\text{Fe}^{2+}(aq) + 2e^-, \\quad E^\\circ = -0.44\\text{ V}$$\n<p>Simultaneously, dissolved atmospheric oxygen is reduced at adjacent cathodic micro-domains:</p>\n$$\\text{O}_2(g) + 2\\text{H}_2\\text{O}(l) + 4e^- \\to 4\\text{OH}^-(aq), \\quad E^\\circ = +0.40\\text{ V}$$\n<p>The net spontaneous reaction produces insoluble iron(II) hydroxide ($E^\\circ_{\\text{cell}} = +0.84\\text{ V}$), which undergoes secondary oxidation with dissolved oxygen and moisture to form hydrated iron(III) oxide (rust, $\\text{Fe}_2\\text{O}_3 \\cdot x\\text{H}_2\\text{O}$).</p>\n<p>Cathodic protection via sacrificial galvanic anodes mitigates corrosion by electrically coupling the steel structure to a base metal with a more negative standard reduction potential, such as zinc ($E^\\circ_{\\text{Zn}^{2+}/\\text{Zn}} = -0.76\\text{ V}$) or magnesium ($E^\\circ_{\\text{Mg}^{2+}/\\text{Mg}} = -2.37\\text{ V}$). In galvanized steel, the zinc coating oxidizes preferentially, delivering electrons through metallic contact to the iron substrate. This polarizes the entire steel surface cathodically below its open-circuit corrosion threshold. Furthermore, oxidized zinc reacts with atmospheric carbon dioxide to form an adherent, protective passivating film of basic zinc carbonate ($\\text{Zn}_5(\\text{OH})_6(\\text{CO}_3)_2$).</p>\n<p>The rate of uniform corrosion is fundamentally governed by the rate of dissolved oxygen transport through the stagnant aqueous boundary layer to cathodic sites on the steel coupon. Under uncoupled baseline conditions, the measured corrosion current density ($i_{\\text{corr}} = 24.5\\,\\mu\\text{A/cm}^2$) corresponds to an annual metal thickness loss of approximately $0.285\\text{ mm/year}$. When sacrificial anodes are connected, they deliver a galvanic protection current that polarizes the steel's electrical potential into the cathodic immunity region of the iron-water Pourbaix diagram. Conversely, coupling steel to noble metals like copper ($E^\\circ_{\\text{Cu}^{2+}/\\text{Cu}} = +0.34\\text{ V}$) accelerates galvanic corrosion.</p>\n<p>Materials scientists submerged standardized carbon steel coupons (surface area $10.0\\text{ cm}^2$) into aerated $3.5\\text{ wt}\\%\\text{ NaCl}$ simulated ocean brine at $25^\\circ\\text{C}$ under varying galvanic couplings. Potentiodynamic polarization scans yielded corrosion potentials ($E_{\\text{corr}}$), corrosion current densities ($i_{\\text{corr}}$), and annualized corrosion penetration rates (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Potentiodynamic polarization parameters, corrosion current densities, and annualized corrosion rates of carbon steel under different galvanic couplings</caption>\n  <thead>\n    <tr><th>Specimen Configuration</th><th>Coupled Metal</th><th>Open-Circuit Ecorr (V vs SCE)</th><th>Corrosion Current icorr (μA/cm²)</th><th>Annual Penetration Rate (mm/yr)</th><th>Steel Mass Loss after 30 Days (mg)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Bare Carbon Steel (Control)</td><td>None</td><td>-0.61 ± 0.02</td><td>24.5 ± 1.2</td><td>0.285 ± 0.014</td><td>224.5 ± 9.8</td></tr>\n    <tr><td>Galvanized Steel (Zn-coated)</td><td>Zinc (Zn)</td><td>-0.98 ± 0.01</td><td>1.2 ± 0.1</td><td>0.014 ± 0.002</td><td>11.2 ± 1.1</td></tr>\n    <tr><td>Mg-Coupled Carbon Steel</td><td>Magnesium (Mg)</td><td>-1.35 ± 0.03</td><td>0.4 ± 0.1</td><td>0.005 ± 0.001</td><td>3.8 ± 0.8</td></tr>\n    <tr><td>Cu-Coupled Carbon Steel</td><td>Copper (Cu)</td><td>-0.38 ± 0.02</td><td>148.0 ± 5.6</td><td>1.722 ± 0.065</td><td>1355.0 ± 42.0</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "Why does zinc act as an effective sacrificial anode to protect carbon steel from marine corrosion, whereas copper accelerates steel destruction?",
        "ch": [
          "Zinc has a higher standard reduction potential than copper, allowing it to absorb excess electrons",
          "Zinc donates protons to the iron lattice, raising the local pH and forming insoluble basic oxides",
          "Zinc has a more negative reduction potential than iron, oxidizing preferentially as a sacrificial anode",
          "Zinc acts as an inert physical coating that prevents water from contacting the iron substrate metal"
        ],
        "a": 2,
        "e": "<strong>Electrochemical principles of sacrificial anodic protection (Topic 417):</strong> Cathodic protection via sacrificial anodes operates on relative reduction potentials. Zinc has a standard reduction potential of $E^\\circ_{\\text{red}} = -0.76\\text{ V}$, which is more negative than that of iron ($E^\\circ_{\\text{red}} = -0.44\\text{ V}$). When electrically connected, zinc possesses a greater thermodynamic driving force for oxidation (more positive oxidation potential: $+0.76\\text{ V}$ vs $+0.44\\text{ V}$). Zinc acts as the galvanic anode ('AN OX'), oxidizing preferentially and supplying electrons to the steel. The influx of electrons polarizes the steel negatively, suppressing iron oxidation and forcing it to act exclusively as a cathode. In contrast, copper has a positive reduction potential ($+0.34\\text{ V}$); when coupled to iron, copper serves as a massive cathode, driving rapid galvanic corrosion of iron.<br><br><em>Distractor Traps:</em><br>&bull; A reverses electrochemical terminology, claiming zinc has a higher reduction potential than copper ($+0.34\\text{ V} > -0.76\\text{ V}$).<br>&bull; B falsely proposes proton donation from metallic zinc into iron, which violates metallic bonding physics.<br>&bull; D describes a purely barrier coating (like paint); zinc provides active galvanic cathodic protection even if scratched."
      },
      {
        "q": "According to Faraday's law of electrolysis, if a sacrificial zinc anode delivers a steady protective galvanic current of 0.193 A for 100,000 seconds, what mass of zinc dissolves? (Molar mass of Zn = 65.4 g/mol, F = 96,500 C/mol e-)",
        "ch": [
          "Exactly 13.1 grams of zinc metal",
          "Exactly 26.2 grams of zinc metal",
          "Exactly 1.31 grams of zinc metal",
          "Exactly 6.54 grams of zinc metal"
        ],
        "a": 3,
        "e": "<strong>Faraday's law applied to sacrificial anode consumption (Topic 417):</strong> The total electrical charge transferred by the sacrificial zinc anode is calculated from current and time: $Q = I \\cdot t = (0.193\\text{ A})(100,000\\text{ s}) = 19,300\\text{ C}$. The moles of electrons released during oxidation is: $n_e = \\frac{Q}{F} = \\frac{19,300\\text{ C}}{96,500\\text{ C/mol }e^-} = 0.200\\text{ mol }e^-$. Zinc oxidation is a two-electron process: $\\text{Zn}(s) \\to \\text{Zn}^{2+} + 2e^-$. Thus, the moles of zinc consumed is: $n_{\\text{Zn}} = \\frac{0.200\\text{ mol }e^-}{2} = 0.100\\text{ mol }\\text{Zn}$. Multiplying by the molar mass of zinc yields the dissolved mass: $m = (0.100\\text{ mol})(65.4\\text{ g/mol}) = 6.54\\text{ g}$.<br><br><em>Distractor Traps:</em><br>&bull; A forgets to divide by the stoichiometric valence factor $n = 2$, obtaining $(0.200)(65.4) = 13.08\\text{ g} \\approx 13.1\\text{ g}$.<br>&bull; B erroneously multiplies by 2 instead of dividing, calculating $(0.400)(65.4) = 26.16\\text{ g} \\approx 26.2\\text{ g}$.<br>&bull; C makes a tenfold decimal placement calculation error, yielding $1.31\\text{ g}$."
      },
      {
        "q": "What chemical reaction occurs at cathodic regions of the carbon steel structure in aerated neutral seawater during corrosion?",
        "ch": [
          "Dissolved oxygen gas is reduced by four electrons in the presence of water to hydroxide ions",
          "Protons from autoionized water are reduced to evolve bubbles of hazardous hydrogen gas",
          "Metallic iron atoms lose two valence electrons to form aqueous iron(II) cations in brine",
          "Dissolved sodium chloride dissociates completely to generate gaseous chlorine molecules"
        ],
        "a": 0,
        "e": "<strong>Cathodic reduction mechanisms in neutral marine corrosion (Topic 417):</strong> In neutral or mildly alkaline aqueous environments exposed to air (such as seawater at $\\text{pH } 7.5\\text{--}8.2$), the thermodynamic reduction of dissolved molecular oxygen is the dominant cathodic reaction: $\\text{O}_2(g) + 2\\text{H}_2\\text{O}(l) + 4e^- \\to 4\\text{OH}^-(aq)$ ($E^\\circ = +0.40\\text{ V}$). Under acidic conditions ($\\text{pH} < 4$), hydrogen evolution ($2\\text{H}^+ + 2e^- \\to \\text{H}_2$) predominates. However, at neutral pH, the hydronium concentration is so low ($10^{-7}\\text{--}10^{-8}\\text{ M}$) that oxygen reduction dominates the kinetics of iron corrosion.<br><br><em>Distractor Traps:</em><br>&bull; B describes the hydrogen evolution reaction characteristic of acidic corrosion, not aerated neutral marine environments.<br>&bull; C describes anodic oxidation of iron ('AN OX'), not the reduction reaction occurring at cathodic sites.<br>&bull; D describes chloride oxidation, which occurs only in industrial electrolytic cells under high positive overpotentials."
      },
      {
        "q": "In Table 1, why does copper-coupled steel exhibit a 6-fold higher corrosion current density (148 microA/cm2) than bare carbon steel (24.5 microA/cm2)?",
        "ch": [
          "Copper releases toxic cupric ions that dissolve the passive oxide film on carbon steel",
          "Copper provides a large conductive cathode that accelerates cathodic oxygen reduction",
          "Copper reduces water directly, shifting local pH and dissolving iron as complex ions",
          "Copper transfers positive holes to the iron lattice, decreasing iron electron density"
        ],
        "a": 1,
        "e": "<strong>Galvanic corrosion kinetics and area-effect amplification (Topic 417):</strong> When carbon steel is electrically coupled to metallic copper, a galvanic couple is established with a significant potential difference ($E^\\circ_{\\text{cell}} = E^\\circ_{\\text{Cu}^{2+}/\\text{Cu}} - E^\\circ_{\\text{Fe}^{2+}/\\text{Fe}} = +0.34\\text{ V} - (-0.44\\text{ V}) = +0.78\\text{ V}$). Copper is much more noble (higher reduction potential) and has exceptionally low overpotential for the reduction of dissolved oxygen. The copper coupon acts as an efficient, expanded cathodic surface that rapidly consumes electrons. To satisfy the requirement of electroneutrality ($I_{\\text{anodic}} = I_{\\text{cathodic}}$), the coupled steel anode must dissolve at an accelerated rate, driving $i_{\\text{corr}}$ from $24.5\\,\\mu\\text{A/cm}^2$ up to $148.0\\,\\mu\\text{A/cm}^2$.<br><br><em>Distractor Traps:</em><br>&bull; A claims cupric ion dissolution attacks steel; copper remains metallic and cathodically protected, not dissolving into $\\text{Cu}^{2+}$.<br>&bull; C claims copper reduces water directly to create complex ions, which is chemically unfeasible.<br>&bull; D uses solid-state semiconductor jargon ('positive holes') that does not apply to metallic galvanic corrosion."
      },
      {
        "q": "If a galvanized steel sheet suffers a deep scratch that completely exposes the underlying iron, what occurs at the scratch boundary in moist air?",
        "ch": [
          "The exposed iron rusts immediately while the adjacent zinc remains completely unreacted",
          "Zinc transfers protons across the moisture layer, preventing oxygen from reaching iron",
          "Zinc continues to oxidize sacrificially, supplying electrons to protect the bare iron",
          "Both metals react at equal rates to form a mixed zinc-iron bimetallic crystalline alloy"
        ],
        "a": 2,
        "e": "<strong>Cathodic protection at coating discontinuities and scratches (Topic 417):</strong> The fundamental technological advantage of galvanization (zinc coating) over barrier coatings (such as paint, tin, or nickel) is sacrificial cathodic protection across defects. When a scratch penetrates to the underlying steel substrate, an electrolyte droplet (moisture from humid air) bridges the adjacent zinc and exposed iron. Because zinc has a substantially lower reduction potential ($E^\\circ = -0.76\\text{ V}$) than iron ($E^\\circ = -0.44\\text{ V}$), zinc oxidizes preferentially. Electrons flow through the metal from the zinc coating into the exposed iron, cathodically polarizing the bare iron and preventing rust formation even though it is directly exposed to oxygen and moisture.<br><br><em>Distractor Traps:</em><br>&bull; A describes the catastrophic failure that occurs with noble barrier coatings like tin (tinplate), but not with sacrificial zinc coatings.<br>&bull; B proposes proton transfer across moisture, which contradicts the electron transfer mechanism of cathodic protection.<br>&bull; D falsely claims the two metals react at identical rates to form an alloy at ambient temperature."
      },
      {
        "q": "In an impressed current cathodic protection (ICCP) system for an underground pipeline, how does the system prevent pipeline corrosion?",
        "ch": [
          "An AC generator induces high-frequency eddy currents to heat and dry pipeline soil",
          "A sacrificial copper rod is buried nearby to supply surplus electrons to the pipeline",
          "An external power supply removes electrons from the pipeline, forcing anodic oxidation",
          "An external DC source forces electrons into the pipeline, maintaining cathodic polarity"
        ],
        "a": 3,
        "e": "<strong>Mechanism of impressed current cathodic protection (ICCP) (Topic 417):</strong> Impressed Current Cathodic Protection (ICCP) is an alternative to galvanic sacrificial anodes for large industrial infrastructure such as subterranean pipelines and marine offshore platforms. An external direct-current (DC) power source (rectifier) is connected between an inert insoluble ground anode (such as mixed metal oxide or platinized titanium) and the buried pipeline. The negative terminal of the DC supply is connected directly to the steel pipeline. This continuously forces electrons into the pipeline, maintaining its electrical potential below the corrosion potential ($E < E_{\\text{corr}}$). This turns the entire pipeline into a cathode ('RED CAT'), completely suppressing iron oxidation.<br><br><em>Distractor Traps:</em><br>&bull; A describes induction soil heating, which is not an electrochemical cathodic protection mechanism.<br>&bull; B suggests using a copper rod as a sacrificial anode; copper is cathodic to iron and would destroy the pipeline.<br>&bull; C directionally inverts the electron flow; extracting electrons from the pipeline would make it an anode and accelerate dissolution."
      }
    ]
  },
  {
    "id": "exam_cp60_10_p3",
    "sec": "C/P",
    "topic": "Solubility Product Equilibria, Common-Ion Precipitation, and Diamminesilver(I) Complexation Dynamics",
    "sheet": 3,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_10",
    "passage": "<div class=\"ttl\">Passage 3 (Questions 13&ndash;18)</div>\n<p>The dissolution of sparingly soluble ionic salts in aqueous media is governed by the thermodynamic solubility product constant ($K_{sp}$). For silver chloride ($\\text{AgCl}$) at $25^\\circ\\text{C}$:</p>\n$$\\text{AgCl}(s) \\rightleftharpoons \\text{Ag}^+(aq) + \\text{Cl}^-(aq), \\quad K_{sp} = [\\text{Ag}^+][\\text{Cl}^-] = 1.8 \\times 10^{-10}$$\n<p>In pure water, the intrinsic molar solubility $s$ of silver chloride equals $\\sqrt{K_{sp}} \\approx 1.34 \\times 10^{-5}\\text{ M}$. Introducing a soluble common ion, such as chloride from dissolved sodium chloride ($\\text{NaCl}$), causes the reaction quotient ($Q = [\\text{Ag}^+][\\text{Cl}^-]$) to exceed $K_{sp}$. According to Le Châtelier's principle, the system re-establishes equilibrium by shifting toward solid precipitate formation, substantially depressing the concentration of free silver cations in solution.</p>\n<p>Conversely, sparingly soluble precipitates can be selectively brought into solution through complex ion formation. When aqueous ammonia ($\\text{NH}_3$) is introduced into an $\\text{AgCl}$ suspension, unshared electron pairs on the neutral nitrogen ligands coordinate the vacant $5s$ and $5p$ hybrid orbitals of the silver cation in a stepwise fashion to form the stable, linear diamminesilver(I) coordination complex:</p>\n$$\\text{Ag}^+(aq) + 2\\text{NH}_3(aq) \\rightleftharpoons [\\text{Ag}(\\text{NH}_3)_2]^+(aq), \\quad K_f = \\frac{[[\\text{Ag}(\\text{NH}_3)_2]^+]}{[\\text{Ag}^+][\\text{NH}_3]^2} = 1.7 \\times 10^7$$\n<p>Coupling precipitation and coordination equilibria produces the overall dissolution equilibrium:</p>\n$$\\text{AgCl}(s) + 2\\text{NH}_3(aq) \\rightleftharpoons [\\text{Ag}(\\text{NH}_3)_2]^+(aq) + \\text{Cl}^-(aq)$$\n<p>The overall equilibrium constant is $K_{\\text{overall}} = K_{sp} \\times K_f = (1.8 \\times 10^{-10})(1.7 \\times 10^7) = 3.06 \\times 10^{-3}$. In analytical chemistry, silver chloride dissolves readily in $1.0\\text{ M}$ aqueous ammonia because its coupled constant is relatively large. By comparison, silver bromide exhibits only moderate dissolution, while silver iodide remains virtually insoluble even in concentrated ammonia due to its extremely small solubility product ($K_{sp} = 8.3 \\times 10^{-17}$). Dissolving silver iodide requires far more powerful complexing agents, such as thiosulfate or cyanide.</p>\n<p>Analytical chemists equilibrated excess silver halide salts in various aqueous solutions at $25^\\circ\\text{C}$. Free $\\text{Ag}^+$ ion activity and total dissolved silver concentrations were measured using potentiometric ion-selective electrodes (ISE) and atomic absorption spectrophotometry (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Solubility product constants, experimental silver concentrations, and complexation parameters in aqueous media at 25 °C</caption>\n  <thead>\n    <tr><th>Silver Halide Salt</th><th>Aqueous Solution Medium</th><th>Literature Ksp</th><th>Free [Ag+] Activity (M)</th><th>Total Dissolved Ag (M)</th><th>Equilibrium Observation</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>AgCl</td><td>Pure deionized water</td><td>1.8 × 10⁻¹⁰</td><td>1.34 × 10⁻⁵</td><td>1.34 × 10⁻⁵</td><td>Saturated baseline dissolution</td></tr>\n    <tr><td>AgCl</td><td>0.10 M NaCl(aq)</td><td>1.8 × 10⁻¹⁰</td><td>1.80 × 10⁻⁹</td><td>1.80 × 10⁻⁹</td><td>Common-ion suppression</td></tr>\n    <tr><td>AgCl</td><td>1.0 M NH3(aq)</td><td>1.8 × 10⁻¹⁰</td><td>1.02 × 10⁻⁸</td><td>5.23 × 10⁻²</td><td>Extensive complex dissolution</td></tr>\n    <tr><td>AgBr</td><td>1.0 M NH3(aq)</td><td>5.0 × 10⁻¹³</td><td>1.72 × 10⁻⁹</td><td>2.92 × 10⁻³</td><td>Moderate complex dissolution</td></tr>\n    <tr><td>AgI</td><td>1.0 M NH3(aq)</td><td>8.3 × 10⁻¹⁷</td><td>2.21 × 10⁻¹¹</td><td>3.76 × 10⁻⁵</td><td>Negligible complex dissolution</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "What is the theoretical molar solubility of silver chloride (AgCl, Ksp = 1.8 x 10^-10) in an aqueous solution of 0.10 M sodium chloride (NaCl)?",
        "ch": [
          "Exactly 1.8 x 10^-9 mol/L",
          "Exactly 1.3 x 10^-5 mol/L",
          "Exactly 1.8 x 10^-11 mol/L",
          "Exactly 3.6 x 10^-8 mol/L"
        ],
        "a": 0,
        "e": "<strong>Calculation of molar solubility under the common-ion effect (Topic 418):</strong> In a solution containing $0.10\\text{ M }\\text{NaCl}$, the chloride anion dissociates completely: $[\\text{Cl}^-]_{\\text{initial}} = 0.10\\text{ M}$. When $\\text{AgCl}(s)$ dissolves to an extent $s$, the equilibrium concentrations are $[\\text{Ag}^+] = s$ and $[\\text{Cl}^-] = 0.10 + s$. Because $K_{sp} = 1.8 \\times 10^{-10}$ is tiny, the solubility $s$ is negligible relative to $0.10\\text{ M}$ ($0.10 + s \\approx 0.10$). Substituting into the solubility product expression: $K_{sp} = [\\text{Ag}^+][\\text{Cl}^-] = (s)(0.10) = 1.8 \\times 10^{-10}$. Solving for molar solubility: $s = \\frac{1.8 \\times 10^{-10}}{0.10} = 1.8 \\times 10^{-9}\\text{ mol/L}$.<br><br><em>Distractor Traps:</em><br>&bull; B calculates the intrinsic solubility in pure water without the common ion: $\\sqrt{1.8 \\times 10^{-10}} \\approx 1.34 \\times 10^{-5}\\text{ M}$.<br>&bull; C incorrectly divides by $0.10^2 = 0.01$, obtaining $1.8 \\times 10^{-11}\\text{ M}$.<br>&bull; D doubles the numerator before dividing, obtaining $3.6 \\times 10^{-8}\\text{ M}$."
      },
      {
        "q": "Why does silver chloride (AgCl) dissolve readily in 1.0 M aqueous ammonia, whereas silver iodide (AgI) remains virtually insoluble under identical conditions?",
        "ch": [
          "Ammonia forms a covalent precipitate with iodide ions that coats the crystal surface",
          "The Ksp of AgI is too small for complexation free energy to drive dissolution forward",
          "Iodide ions act as stronger Lewis bases than ammonia, displacing amine ligands easily",
          "Silver iodide decomposes into metallic silver and iodine gas in alkaline solutions"
        ],
        "a": 1,
        "e": "<strong>Coupled equilibria and thermodynamic feasibility of complexation (Topic 419):</strong> The dissolution of a silver halide in aqueous ammonia is governed by the coupled equilibrium constant: $K_{\\text{overall}} = K_{sp} \\times K_f$. For silver chloride: $K_{\\text{overall}} = (1.8 \\times 10^{-10})(1.7 \\times 10^7) = 3.06 \\times 10^{-3}$. This equilibrium constant is sufficiently large to dissolve over $0.05\\text{ M}$ of $\\text{AgCl}$ in $1.0\\text{ M }\\text{NH}_3$. In contrast, silver iodide has an extraordinarily small solubility product: $K_{sp} = 8.3 \\times 10^{-17}$. Its coupled constant is: $K_{\\text{overall}} = (8.3 \\times 10^{-17})(1.7 \\times 10^7) = 1.41 \\times 10^{-9}$. Because the lattice energy of $\\text{AgI}$ is so high and its $K_{sp}$ is seven orders of magnitude smaller than that of $\\text{AgCl}$, the formation free energy of $[\\text{Ag}(\\text{NH}_3)_2]^+$ is thermodynamic insufficient to drive dissolution.<br><br><em>Distractor Traps:</em><br>&bull; A falsely asserts ammonia reacts with iodide to form a covalent precipitate; $\\text{NH}_3$ coordinates $\\text{Ag}^+$, not anions.<br>&bull; C incorrectly claims iodide is a strong Lewis base; iodide is the conjugate base of strong acid $\\text{HI}$ ($pK_a \\approx -10$) and is a negligible base.<br>&bull; D proposes spontaneous decomposition into metallic silver and iodine gas, which does not occur under ambient alkaline conditions."
      },
      {
        "q": "If concentrated nitric acid (HNO3) is added dropwise to a clear solution of [Ag(NH3)2]+ and Cl-, what phenomenon will be observed?",
        "ch": [
          "Gaseous nitrogen dioxide evolves rapidly as silver is reduced to metallic mirrors",
          "The solution remains clear because nitrate forms a soluble complex with silver",
          "White silver chloride precipitates because acid protonates ammonia to ammonium",
          "Ammonia evaporates completely, leaving behind soluble silver nitrate and water"
        ],
        "a": 2,
        "e": "<strong>Le Châtelier disruption of complex ions via ligand protonation (Topic 419):</strong> In the clear ammoniacal solution, silver is held in solution as the soluble complex ion $[\\text{Ag}(\\text{NH}_3)_2]^+$. Ammonia ($\\text{NH}_3$) is a Brønsted-Lowry base ($pK_b = 4.75$). When concentrated nitric acid ($\\text{HNO}_3$, a strong acid) is introduced, hydronium ions rapidly protonate unshared electron pairs on ammonia: $\\text{NH}_3 + \\text{H}^+ \\to \\text{NH}_4^+$. The ammonium cation ($\\text{NH}_4^+$) lacks a lone pair and cannot coordinate silver cations. By Le Châtelier's principle, destroying the neutral amine ligand shifts the complexation equilibrium to the left, releasing free $\\text{Ag}^+$ cations into solution. The freed $\\text{Ag}^+$ immediately combines with chloride anions present in solution, forming a dense white precipitate of $\\text{AgCl}(s)$ ($Q > K_{sp}$).<br><br><em>Distractor Traps:</em><br>&bull; A confuses acid-base protonation with a redox reaction forming toxic $\\text{NO}_2$ gas and silver mirrors.<br>&bull; B fails to recognize that free $\\text{Cl}^-$ in solution will immediately precipitate with uncomplexed $\\text{Ag}^+$.<br>&bull; D asserts ammonia gas evaporates into the headspace rather than being protonated into aqueous ammonium in acidic solution."
      },
      {
        "q": "What is the coordination number and geometric molecular shape of the diamminesilver(I) complex ion, [Ag(NH3)2]+?",
        "ch": [
          "Coordination number of 4 with a square planar molecular geometry",
          "Coordination number of 4 with a tetrahedral molecular geometry",
          "Coordination number of 6 with an octahedral molecular geometry",
          "Coordination number of 2 with a linear 180-degree molecular geometry"
        ],
        "a": 3,
        "e": "<strong>Coordination chemistry and geometry of diamminesilver(I) (Topic 419):</strong> In the coordination complex $[\\text{Ag}(\\text{NH}_3)_2]^+$, the central silver(I) cation is directly bonded to two monodentate ammine ($\\text{NH}_3$) ligands, giving a coordination number of 2. Silver(I) has a closed-shell $d^{10}$ ground-state electron configuration ($[\\text{Kr}]4d^{10}5s^05p^0$). Bonding occurs through $sp$ hybridization of the vacant $5s$ and one $5p$ orbital, which hybridize to form two equivalent bonding orbitals directed in opposite directions. To minimize electrostatic repulsion between the two coordinate covalent ligand electron pairs, the geometry adopts a bond angle of $180^\\circ$, producing an ideal linear molecular geometry: $[\\text{H}_3\\text{N}-\\text{Ag}-\\text{NH}_3]^+$.<br><br><em>Distractor Traps:</em><br>&bull; A describes 4-coordinate square planar geometry typical of $d^8$ transition metal complexes like $\\text{Pt}^{2+}$ and $\\text{Pd}^{2+}$.<br>&bull; B describes 4-coordinate tetrahedral geometry typical of complexes like $[\\text{Zn}(\\text{NH}_3)_4]^{2+}$.<br>&bull; C describes 6-coordinate octahedral geometry typical of transition metals like $\\text{Fe}^{3+}$ or $\\text{Cr}^{3+}$."
      },
      {
        "q": "A solution contains 0.010 M Cl- and 0.010 M Br-. As AgNO3 is slowly added, which salt precipitates first and at what [Ag+] concentration? (Ksp AgCl = 1.8 x 10^-10, Ksp AgBr = 5.0 x 10^-13)",
        "ch": [
          "AgCl precipitates first when [Ag+] reaches 1.8 x 10^-8 mol/L",
          "AgBr precipitates first when [Ag+] reaches 5.0 x 10^-11 mol/L",
          "Both salts precipitate simultaneously at 1.0 x 10^-10 mol/L",
          "AgCl precipitates first because chloride has smaller radius"
        ],
        "a": 1,
        "e": "<strong>Selective fractional precipitation of halides (Topic 418):</strong> Precipitation of a sparingly soluble salt initiates when the ion product quotient reaches the solubility product constant ($Q = K_{sp}$). For silver chloride: $[\\text{Ag}^+] = \\frac{K_{sp}(\\text{AgCl})}{[\\text{Cl}^-]} = \\frac{1.8 \\times 10^{-10}}{0.010} = 1.8 \\times 10^{-8}\\text{ M}$. For silver bromide: $[\\text{Ag}^+] = \\frac{K_{sp}(\\text{AgBr})}{[\\text{Br}^-]} = \\frac{5.0 \\times 10^{-13}}{0.010} = 5.0 \\times 10^{-11}\\text{ M}$. Because $5.0 \\times 10^{-11}\\text{ M} \\ll 1.8 \\times 10^{-8}\\text{ M}$, the threshold $[\\text{Ag}^+]$ required to precipitate $\\text{AgBr}$ is nearly 360 times lower than that for $\\text{AgCl}$. Therefore, $\\text{AgBr}$ precipitates first as a pale yellow solid when $[\\text{Ag}^+]$ reaches $5.0 \\times 10^{-11}\\text{ M}$, allowing quantitative separation from chloride.<br><br><em>Distractor Traps:</em><br>&bull; A identifies the precipitation threshold of $\\text{AgCl}$, which requires a silver concentration over two orders of magnitude higher.<br>&bull; C incorrectly assumes simultaneous precipitation, ignoring the massive difference in solubility products.<br>&bull; D invokes periodic atomic radius trends rather than thermodynamic solubility product constants ($K_{sp}$)."
      },
      {
        "q": "What is the numerical value of the overall equilibrium constant K_overall for: AgCl(s) + 2 NH3(aq) <=> [Ag(NH3)2]+(aq) + Cl-(aq)?",
        "ch": [
          "Approximately 1.1 x 10^-17",
          "Approximately 9.4 x 10^16",
          "Approximately 3.1 x 10^-3",
          "Approximately 5.8 x 10^-4"
        ],
        "a": 2,
        "e": "<strong>Calculation of overall equilibrium constant for coupled reactions (Topic 419):</strong> The overall chemical equation is the algebraic sum of two elementary equilibria:<br>Reaction 1: $\\text{AgCl}(s) \\rightleftharpoons \\text{Ag}^+(aq) + \\text{Cl}^-(aq)$ with $K_1 = K_{sp} = 1.8 \\times 10^{-10}$<br>Reaction 2: $\\text{Ag}^+(aq) + 2\\text{NH}_3(aq) \\rightleftharpoons [\\text{Ag}(\\text{NH}_3)_2]^+(aq)$ with $K_2 = K_f = 1.7 \\times 10^7$<br>When two chemical equations are added together, their equilibrium constants multiply: $K_{\\text{overall}} = K_1 \\times K_2 = K_{sp} \\times K_f$. Calculating: $K_{\\text{overall}} = (1.8 \\times 10^{-10})(1.7 \\times 10^7) = 3.06 \\times 10^{-3} \\approx 3.1 \\times 10^{-3}$.<br><br><em>Distractor Traps:</em><br>&bull; A divides $K_{sp}$ by $K_f$, obtaining $(1.8 \\times 10^{-10}) / (1.7 \\times 10^7) \\approx 1.1 \\times 10^{-17}$.<br>&bull; B divides $K_f$ by $K_{sp}$, obtaining $(1.7 \\times 10^7) / (1.8 \\times 10^{-10}) \\approx 9.4 \\times 10^{16}$.<br>&bull; D incorrectly squares the solubility product before multiplying, calculating $(1.8 \\times 10^{-10})^2 \\times (1.7 \\times 10^7) \\approx 5.5 \\times 10^{-13}$."
      }
    ]
  },
  {
    "id": "exam_cp60_10_p4",
    "sec": "C/P",
    "topic": "Stereochemical Resolution, Polarimetric Optical Purity, and Cahn-Ingold-Prelog Configurations of Tartaric Acid Derivatives",
    "sheet": 4,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_10",
    "passage": "<div class=\"ttl\">Passage 4 (Questions 19&ndash;24)</div>\n<p>Stereochemical isomerism dictates molecular recognition in enzymatic binding pockets and synthetic pharmacology. Chiral enantiomers represent non-superimposable mirror-image stereoisomers that share identical scalar physical properties (melting points, boiling points, chromatographic retention on achiral stationary phases, and infrared vibrational spectra) in achiral environments, yet rotate plane-polarized light in equal and opposite directions. Specific optical rotation ($[\\alpha]_\\lambda^T$) is quantified via Biot's relation:</p>\n$$[\\alpha]_\\lambda^T = \\frac{\\alpha_{\\text{obs}}}{c \\cdot l}$$\n<p>where $\\alpha_{\\text{obs}}$ is the observed rotation angle in degrees, $c$ is analyte concentration in $\\text{g/mL}$, and $l$ is optical pathlength in decimeters ($\\text{dm}$).</p>\n<p>An equimolar mixture of enantiomers (racemate) exhibits an observed optical rotation of zero ($[\\alpha] = 0.0^\\circ$). The optical purity or enantiomeric excess ($ee$) of an asymmetric mixture is defined as:</p>\n$$ee = \\frac{|[\\alpha]_{\\text{obs}}|}{[\\alpha]_{\\text{pure}}} \\times 100\\% = |\\text{fraction}_R - \\text{fraction}_S| \\times 100\\%$$\n<p>Stereoisomers containing multiple stereocenters that are not mirror images are classified as diastereomers. Unlike enantiomers, diastereomers possess distinct thermodynamic and physical properties, enabling separation by fractional crystallization or achiral chromatography. A unique subclass, meso compounds, possess multiple asymmetric carbons with opposing $(R)$ and $(S)$ configurations but feature an internal mirror plane of symmetry ($\\sigma$) or inversion center ($i$). Consequently, meso stereoisomers are superimposable upon their mirror images and are completely optically inactive ($[\\alpha] = 0.0^\\circ$).</p>\n<p>Synthetic chemists resolved a racemic mixture of tartaric acid (2,3-dihydroxybutanedioic acid) using enantiopure $(1R,2S)-(-)$-ephedrine as a chiral resolving base. Resolved fractions and pure synthetic stereoisomers were evaluated using polarimetry at $20^\\circ\\text{C}$ ($\\lambda = 589\\text{ nm}$, $l = 1.0\\text{ dm}$, $c = 0.050\\text{ g/mL}$ in $\\text{H}_2\\text{O}$), differential scanning calorimetry, and Cahn-Ingold-Prelog priority analysis (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Stereochemical configurations, optical rotations, melting points, and enantiomeric purities of tartaric acid stereoisomers and resolved fractions</caption>\n  <thead>\n    <tr><th>Sample Fraction</th><th>Cahn-Ingold-Prelog Configuration</th><th>Observed Alpha (deg)</th><th>Specific Rotation [alpha]D (deg/(dm·g/mL))</th><th>Melting Point Tm (°C)</th><th>Enantiomeric Excess ee (%)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Pure (+)-Tartaric Acid</td><td>(2R, 3R)</td><td>+0.620</td><td>+12.4</td><td>168 &ndash; 170</td><td>100.0 (R,R)</td></tr>\n    <tr><td>Pure (&minus;)-Tartaric Acid</td><td>(2S, 3S)</td><td>&minus;0.620</td><td>&minus;12.4</td><td>168 &ndash; 170</td><td>100.0 (S,S)</td></tr>\n    <tr><td>Meso-Tartaric Acid</td><td>(2R, 3S)</td><td>0.000</td><td>0.0</td><td>140 &ndash; 142</td><td>0.0 (Achiral meso)</td></tr>\n    <tr><td>Racemic Tartaric Acid</td><td>1:1 (2R,3R) / (2S,3S)</td><td>0.000</td><td>0.0</td><td>206 &ndash; 208</td><td>0.0 (Racemate)</td></tr>\n    <tr><td>Resolved Fraction A</td><td>(2R, 3R) enriched</td><td>+0.465</td><td>+9.3</td><td>162 &ndash; 165</td><td>75.0 (R,R)</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "According to the Cahn-Ingold-Prelog (CIP) priority rules, what is the correct ranking of substituents attached to C2 in tartaric acid (HOOC-CH(OH)-CH(OH)-COOH) from highest (1) to lowest (4) priority?",
        "ch": [
          "-COOH (1) > -OH (2) > -CH(OH)COOH (3) > -H (4)",
          "-OH (1) > -H (2) > -CH(OH)COOH (3) > -COOH (4)",
          "-CH(OH)COOH (1) > -OH (2) > -COOH (3) > -H (4)",
          "-OH (1) > -COOH (2) > -CH(OH)COOH (3) > -H (4)"
        ],
        "a": 3,
        "e": "<strong>Cahn-Ingold-Prelog priority assignment rules (Topic 421):</strong> Priority is assigned based on decreasing atomic number of the atoms directly bonded to the chiral center (C2):<br>1. Hydroxyl ($-\\text{OH}$): directly bonded to oxygen (atomic number 8), which has the highest atomic number among all attached atoms. Priority 1.<br>4. Hydrogen ($-\\text{H}$): directly bonded to hydrogen (atomic number 1), lowest priority. Priority 4.<br>2 vs 3. Between carboxylic acid ($-\\text{COOH}$) and the adjacent methine group ($-\\text{CH(OH)COOH}$), both directly attach via carbon (atomic number 6). We compare the atoms bonded to each carbon in order of decreasing atomic number: The carboxylic acid carbonyl carbon ($C=O$) counts as two bonds to oxygen, plus one bond to $-\\text{OH}$, giving an atom list of $(\\text{O, O, O})$. The C3 methine carbon is bonded to one oxygen ($-\\text{OH}$), one carbon ($-\\text{COOH}$), and one hydrogen ($-\\text{H}$), giving an atom list of $(\\text{O, C, H})$. At the first point of difference, the second oxygen of $-\\text{COOH}$ outranks the carbon of $-\\text{CH(OH)COOH}$. Thus, $-\\text{COOH}$ is Priority 2, and $-\\text{CH(OH)COOH}$ is Priority 3. Overall priority: $-\\text{OH} (1) > -\\text{COOH} (2) > -\\text{CH(OH)COOH} (3) > -\\text{H} (4)$.<br><br><em>Distractor Traps:</em><br>&bull; A places $-\\text{COOH}$ ahead of $-\\text{OH}$, violating atomic number ranking ($8 > 6$).<br>&bull; B places hydrogen ahead of carbon substituents, inverting priority rules ($6 > 1$).<br>&bull; C incorrectly ranks $-\\text{CH(OH)COOH}$ over $-\\text{OH}$ based on total molecular mass rather than atomic number at point of attachment."
      },
      {
        "q": "Why does meso-tartaric acid display zero optical activity ([alpha] = 0.0 deg) despite containing two chiral stereocenters?",
        "ch": [
          "It possesses an internal mirror plane that makes its mirror image superimposable",
          "It exists as an equimolar equilibrium mixture of two interconverting enantiomers",
          "The hydroxyl groups undergo rapid tautomerization into an achiral enol isomer",
          "Its stereocenters rotate polarized light at identical speeds in the same direction"
        ],
        "a": 0,
        "e": "<strong>Structural symmetry and optical inactivity of meso compounds (Topic 422):</strong> A meso compound contains two or more chiral stereocenters with opposing absolute configurations (e.g., $2R, 3S$) and possesses an internal symmetry element—specifically an internal mirror plane of symmetry ($\\sigma$) or an inversion center ($i$). In meso-tartaric acid, a horizontal reflection plane bisects the central C2-C3 carbon-carbon bond: the top half of the molecule (bearing an $R$ configuration) is the exact reflection of the bottom half (bearing an $S$ configuration). Because the clockwise polarization rotation introduced by one half of the molecule is exactly canceled by the equal and opposite counterclockwise rotation of the other half through internal compensation, the molecule as a whole is achiral, superimposable on its mirror image, and optically inactive ($[\\alpha] = 0.0^\\circ$).<br><br><em>Distractor Traps:</em><br>&bull; B describes a racemic mixture (external compensation), not a single pure meso diastereomer.<br>&bull; C proposes keto-enol tautomerization; dihydroxy dicarboxylic acids do not undergo enolization to eliminate stereocenters.<br>&bull; D claims both stereocenters rotate light in the same direction; identical directions would reinforce rotation rather than canceling it."
      },
      {
        "q": "A solution of Resolved Fraction A has a measured specific rotation of +9.3 deg/(dm·g/mL). Given that pure (2R,3R)-tartaric acid has [alpha] = +12.4 deg/(dm·g/mL), what is the percentage of the (2R,3R) enantiomer in Fraction A?",
        "ch": [
          "Exactly 75.0% of the (2R,3R) enantiomer",
          "Exactly 87.5% of the (2R,3R) enantiomer",
          "Exactly 62.5% of the (2R,3R) enantiomer",
          "Exactly 93.8% of the (2R,3R) enantiomer"
        ],
        "a": 1,
        "e": "<strong>Enantiomeric excess and enantiomeric composition calculations (Topic 422):</strong> The enantiomeric excess ($ee$) is the ratio of measured specific rotation to that of the pure enantiomer: $ee = \\frac{|[\\alpha]_{\\text{obs}}|}{[\\alpha]_{\\text{pure}}} \\times 100\\% = \\frac{+9.3}{+12.4} \\times 100\\% = 75.0\\%$. By definition, $ee$ reflects the excess of the major enantiomer over the minor enantiomer: $ee = \\%R - \\%S = 75.0\\%$. Because the total mixture comprises both enantiomers: $\\%R + \\%S = 100.0\\%$. Adding the two equations: $2(\\%R) = 175.0\\% \\implies \\%R = \\frac{175.0\\%}{2} = 87.5\\%$ (and $\\%S = 12.5\\%$).<br><br><em>Distractor Traps:</em><br>&bull; A confuses enantiomeric excess ($ee = 75.0\\%$) with total percentage composition of the major enantiomer (which is $87.5\\%$).<br>&bull; C subtracts half of the excess from $100\\%$, obtaining $100 - 37.5 = 62.5\\%$.<br>&bull; D adds half of $75\\%$ ($37.5\\%$) to $50\\%$ and mistakenly averages with $100\\%$, calculating $93.75\\% \\approx 93.8\\%$."
      },
      {
        "q": "Why can enantiomers be separated by reacting them with a single enantiomer of a chiral resolving agent such as (1R,2S)-ephedrine?",
        "ch": [
          "The reaction converts covalent enantiomers into rapidly interconverting rotamers",
          "The resolving agent selectively destroys one enantiomer via an SN2 oxidation",
          "The resulting diastereomeric salts have distinct solubilities and crystal lattices",
          "The resolving agent forms a meso complex that precipitates spontaneously from water"
        ],
        "a": 2,
        "e": "<strong>Resolution of racemic mixtures via diastereomeric salt formation (Topic 422):</strong> Enantiomers possess identical scalar physical properties (solubility, melting point, density) in achiral environments and cannot be resolved by standard crystallization or fractional distillation. However, when a racemic mixture of $(2R,3R)$- and $(2S,3S)$-tartaric acid is reacted with an enantiopure chiral base $(1R,2S)-(-)$-ephedrine ($B^*$), two distinct ionic diastereomeric salts are formed: $[(2R,3R)\\text{-tartrate}][B^*\\text{H}^+]$ and $[(2S,3S)\\text{-tartrate}][B^*\\text{H}^+]$. Because diastereomers are stereoisomers that are not mirror images, they possess different free energies of hydration, different crystal lattice energies, and significantly different solubilities, allowing clean separation via selective fractional crystallization.<br><br><em>Distractor Traps:</em><br>&bull; A claims the salts are rapidly interconverting conformational rotamers, which would prevent physical separation.<br>&bull; B describes chemical destruction or kinetic resolution via chemical oxidation, rather than reversible non-destructive acid-base salt formation.<br>&bull; D asserts the salt forms a meso complex; ephedrine salts lack internal mirror planes and are not meso."
      },
      {
        "q": "For a molecule with formula CH3-CH(OH)-CH(OH)-CH3 (2,3-butanediol), how many total stereoisomers exist, and how many are optically active?",
        "ch": [
          "Four total stereoisomers exist, and all four isomers are optically active",
          "Two total stereoisomers exist, and both isomers are optically active",
          "Four total stereoisomers exist, and only two isomers are optically active",
          "Three total stereoisomers exist, and only two isomers are optically active"
        ],
        "a": 3,
        "e": "<strong>Stereoisomer counting in symmetrical molecules with stereocenters (Topic 422):</strong> 2,3-Butanediol contains two identical chiral carbons ($n = 2$), each bearing $-\\text{CH}_3$, $-\\text{OH}$, $-\\text{H}$, and $-\\text{CH(OH)CH}_3$. According to the $2^n$ rule, the maximum theoretical number of stereoisomers is $2^2 = 4$: $(2R, 3R)$, $(2S, 3S)$, $(2R, 3S)$, and $(2S, 3R)$. However, because both stereocenters have identical sets of substituents, the $(2R, 3S)$ and $(2S, 3R)$ configurations are superimposable mirror images of each other due to an internal plane of symmetry (meso-2,3-butanediol). Therefore, there are only 3 unique stereoisomers: a pair of chiral enantiomers [$(2R, 3R)$ and $(2S, 3S)$], both of which are optically active, and 1 achiral meso stereoisomer, which is optically inactive. Total = 3 isomers, 2 optically active.<br><br><em>Distractor Traps:</em><br>&bull; A blindly applies the $2^n = 4$ rule without checking for internal symmetry and meso degeneracy.<br>&bull; B neglects the meso compound entirely, counting only a single enantiomeric pair.<br>&bull; C counts 4 isomers and 2 active, failing to recognize that $(2R,3S)$ and $(2S,3R)$ represent the same identical chemical compound."
      },
      {
        "q": "What is the relationship between pure (+)-tartaric acid and meso-tartaric acid?",
        "ch": [
          "They are diastereomers with different melting points and different chemical stabilities",
          "They are enantiomers with identical boiling points and opposite optical rotations",
          "They are constitutional isomers with different covalent bonding connectivity orders",
          "They are identical conformers that interconvert spontaneously at room temperature"
        ],
        "a": 0,
        "e": "<strong>Distinction between enantiomers, diastereomers, and meso compounds (Topic 422):</strong> Pure $(+)$-tartaric acid has the $(2R, 3R)$ absolute configuration, whereas meso-tartaric acid has the $(2R, 3S)$ absolute configuration. Both molecules share the identical atomic connectivity (they are both 2,3-dihydroxybutanedioic acid). However, they are stereoisomers that are not mirror images of one another (the mirror image of $(2R, 3R)$ is $(2S, 3S)$, not $(2R, 3S)$). By definition, non-mirror image stereoisomers are diastereomers. Diastereomers possess completely different physical properties, as evidenced in Table 1: $(+)$-tartaric acid has a melting point of $168\\text{--}170^\\circ\\text{C}$ and specific rotation of $+12.4^\\circ$, whereas meso-tartaric acid has a melting point of $140\\text{--}142^\\circ\\text{C}$ and specific rotation of $0.0^\\circ$.<br><br><em>Distractor Traps:</em><br>&bull; B confuses diastereomers with enantiomers; enantiomers must be non-superimposable mirror images.<br>&bull; C claims they are constitutional isomers; both possess identical covalent bond connectivity.<br>&bull; D misidentifies them as conformers; interconversion requires breaking covalent bonds, not simple bond rotation."
      }
    ]
  },
  {
    "id": "exam_cp60_10_p5",
    "sec": "C/P",
    "topic": "Conformational Chair Analysis, A-Values, and Dynamic NMR Coupling in Substituted Cyclohexanes",
    "sheet": 5,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_10",
    "passage": "<div class=\"ttl\">Passage 5 (Questions 25&ndash;30)</div>\n<p>Cyclohexane rings adopt puckered chair conformations that simultaneously minimize angle strain (all ring carbon bond angles approximate the ideal tetrahedral angle of $109.5^\\circ$) and torsional strain (all adjacent carbon-hydrogen bonds adopt staggered conformations). In unsubstituted cyclohexane, twelve hydrogen atoms occupy two distinct chemical environments: six perpendicular axial bonds ($a$) parallel to the $C_3$ symmetry axis, and six outward-flaring equatorial bonds ($e$). Rapid chair-chair interconversion (ring flipping) exchanges axial and equatorial positions through higher-energy twist-boat and boat intermediates with an activation barrier of $\\Delta G^\\ddagger \\approx 45\\text{ kJ/mol}$.</p>\n<p>In monosubstituted cyclohexanes, the two interconverting chair conformers are non-degenerate. An axial substituent experiences severe non-bonded steric repulsion with the two syn-axial hydrogen atoms at the 3- and 5-positions (1,3-diaxial steric strain), structurally equivalent to two gauche-butane interactions. In the equatorial conformer, the substituent projects into unobstructed peripheral space, eliminating 1,3-diaxial strain. The thermodynamic preference is quantified by the substituent A-value:</p>\n$$A = -\\Delta G^\\circ = G^\\circ_{\\text{axial}} - G^\\circ_{\\text{equatorial}}$$\n<p>The conformational equilibrium constant obeys Boltzmann thermodynamics: $K_{\\text{eq}} = \\frac{[\\text{equatorial}]}{[\\text{axial}]} = e^{A / RT}$. Highly hindered groups, such as the tert-butyl group ($-C(CH_3)_3$, $A = 20.5\\text{ kJ/mol}$), lock the cyclohexane ring into a static conformation ($> 99.9\\%$ equatorial at $298\\text{ K}$).</p>\n<p>Conformational equilibria and vicinal proton stereochemistry were investigated using dynamic low-temperature $^1\\text{H-NMR}$ spectroscopy ($500\\text{ MHz}$, $-80^\\circ\\text{C}$). The Karplus relation governs three-bond spin-spin coupling constants ($^3J_{\\text{HH}}$): trans-diaxial protons ($\\theta \\approx 180^\\circ$) display large coupling constants ($^3J_{aa} = 10\\text{--}13\\text{ Hz}$), whereas equatorial-axial and equatorial-equatorial protons ($\\theta \\approx 60^\\circ$) display small coupling constants ($^3J_{ea}, ^3J_{ee} = 2\\text{--}5\\text{ Hz}$) (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Substituent A-values, equilibrium equatorial percentages at 298 K, and low-temperature 1H-NMR vicinal coupling constants</caption>\n  <thead>\n    <tr><th>Monosubstituted Cyclohexane</th><th>A-Value (kJ/mol)</th><th>A-Value (kcal/mol)</th><th>% Equatorial at 298 K</th><th>Keq ([eq]/[ax])</th><th>3J(H1-ax, H2-ax) (Hz)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Fluoro (&minus;F)</td><td>1.1</td><td>0.26</td><td>60.8</td><td>1.55</td><td>9.8 ± 0.2</td></tr>\n    <tr><td>Chloro (&minus;Cl)</td><td>2.2</td><td>0.53</td><td>70.9</td><td>2.44</td><td>10.4 ± 0.3</td></tr>\n    <tr><td>Methyl (&minus;CH3)</td><td>7.3</td><td>1.74</td><td>95.0</td><td>19.0</td><td>11.2 ± 0.3</td></tr>\n    <tr><td>Isopropyl (&minus;CH(CH3)2)</td><td>9.2</td><td>2.20</td><td>97.6</td><td>40.7</td><td>11.8 ± 0.4</td></tr>\n    <tr><td>tert-Butyl (&minus;C(CH3)3)</td><td>20.5</td><td>4.90</td><td>&gt; 99.9</td><td>&gt; 3900</td><td>12.6 ± 0.3</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "What is the physical origin of the energetic instability associated with an axial methyl group in methylcyclohexane compared to an equatorial methyl group?",
        "ch": [
          "Severe angle strain arising from compression of internal ring C-C-C angles to 90 degrees",
          "Steric van der Waals repulsion with syn-axial hydrogen atoms at the C3 and C5 positions",
          "Electrostatic dipole-dipole repulsion between the methyl carbon and adjacent ring protons",
          "Torsional strain produced by eclipsed C-H bonds between the ring and methyl hydrogens"
        ],
        "a": 1,
        "e": "<strong>Conformational energetics and 1,3-diaxial steric strain (Topic 423):</strong> In an axial orientation, a substituent projects perpendicularly along the vertical axis of the cyclohexane chair, placing its atoms in direct steric conflict with the two syn-axial hydrogen atoms located on the same face of the ring at carbons 3 and 5. This steric congestion—known as 1,3-diaxial strain—results from van der Waals electron-cloud overlap between non-bonded atoms forced closer than the sum of their van der Waals radii. Newman projection analysis along the C1-C2 and C1-C6 bonds reveals that an axial methyl group is in a gauche relationship with two ring C-C bonds (two gauche-butane interactions, each costing $\\approx 3.8\\text{ kJ/mol}$, totaling $7.3\\text{ kJ/mol}$). In contrast, an equatorial methyl group adopts an anti-coplanar relationship with the ring carbons, completely relieving 1,3-diaxial steric strain.<br><br><em>Distractor Traps:</em><br>&bull; A attributes strain to angle distortion; the chair conformation preserves ideal tetrahedral $109.5^\\circ$ angles.<br>&bull; C invokes electrostatic dipole repulsions; methyl and ring carbons are nonpolar hydrocarbons devoid of dipole charges.<br>&bull; D attributes strain to bond eclipsing; all bonds in chair cyclohexanes are fully staggered."
      },
      {
        "q": "Which of the following disubstituted cyclohexane isomers exists predominantly in a conformation where BOTH substituents occupy stable equatorial positions?",
        "ch": [
          "cis-1,2-dimethylcyclohexane",
          "trans-1,3-dimethylcyclohexane",
          "trans-1,4-dimethylcyclohexane",
          "cis-1,4-dimethylcyclohexane"
        ],
        "a": 2,
        "e": "<strong>Conformational analysis of disubstituted cyclohexanes (Topic 423):</strong> To determine whether both substituents can be equatorial, we evaluate the spatial geometry of substituents on the cyclohexane chair:<br>&bull; 1,4-disubstituted: At C1, 'up' is axial and 'down' is equatorial. At C4, 'up' is equatorial and 'down' is axial. In trans-1,4-dimethylcyclohexane, one methyl is 'up' and the other is 'down'. Therefore, one chair conformer is (equatorial, equatorial) while the flipped chair is (axial, axial). The diequatorial conformer is overwhelmingly favored ($> 99\\%$).<br>&bull; cis-1,2-dimethylcyclohexane: C1(up) is axial, C2(up) is equatorial. Thus cis-1,2 is always (axial, equatorial).<br>&bull; trans-1,3-dimethylcyclohexane: C1(up) is axial, C3(down) is axial. Thus trans-1,3 is always (axial, equatorial).<br>&bull; cis-1,4-dimethylcyclohexane: C1(up) is axial, C4(up) is equatorial. Thus cis-1,4 is always (axial, equatorial).<br>Only trans-1,4-dimethylcyclohexane can adopt a diequatorial (e, e) conformation.<br><br><em>Distractor Traps:</em><br>&bull; A is cis-1,2, which must possess one axial and one equatorial group (a, e).<br>&bull; B is trans-1,3, which must possess one axial and one equatorial group (a, e).<br>&bull; D is cis-1,4, which must possess one axial and one equatorial group (a, e)."
      },
      {
        "q": "In low-temperature 1H-NMR spectroscopy of trans-1-tert-butyl-4-chlorocyclohexane, what signal splitting pattern is observed for the C4 methine proton (H-C-Cl)?",
        "ch": [
          "A sharp singlet due to rapid room-temperature conformational chair-chair interconversion",
          "A doublet of doublets with two small coupling constants of approximately 2 Hz each",
          "A triplet with a single intermediate coupling constant of approximately 7 Hz each",
          "A triplet of triplets with two large (11-12 Hz) and two small (3-4 Hz) coupling constants"
        ],
        "a": 3,
        "e": "<strong>Dynamic 1H-NMR Karplus spin-spin splitting in chair cyclohexanes (Topic 423):</strong> The tert-butyl group has a massive A-value ($20.5\\text{ kJ/mol}$) that firmly locks it into the equatorial position at C1. In trans-1-tert-butyl-4-chlorocyclohexane, the chlorine substituent at C4 is trans to the equatorial tert-butyl group, placing the chlorine also in an equatorial position. Consequently, the methine proton at C4 ($\\text{H-C-Cl}$) is forced into the AXIAL orientation. The axial proton at C4 couples with four adjacent vicinal protons on C3 and C5: two trans-diaxial protons (axial-axial, dihedral angle $\\theta \\approx 180^\\circ$) and two gauche protons (axial-equatorial, dihedral angle $\\theta \\approx 60^\\circ$). By the Karplus relation, the two trans-diaxial protons yield a large coupling ($^3J_{aa} \\approx 11\\text{--}12\\text{ Hz}$), splitting the peak into a triplet. The two axial-equatorial protons yield a small coupling ($^3J_{ae} \\approx 3\\text{--}4\\text{ Hz}$), further splitting each triplet peak into a triplet, generating a characteristic triplet of triplets (tt).<br><br><em>Distractor Traps:</em><br>&bull; A describes room-temperature coalescence where rapid chair flipping averages coupling constants, which is frozen at $-80^\\circ\\text{C}$.<br>&bull; B assumes coupling occurs to only two protons rather than all four vicinal protons on C3 and C5.<br>&bull; C assumes an averaged freely rotating coupling constant, failing to account for rigid trans-diaxial vs axial-equatorial geometry."
      },
      {
        "q": "Using Table 1, what is the equilibrium constant Keq for the chair flip of methylcyclohexane (equatorial <=> axial) at 298 K?",
        "ch": [
          "Exactly 0.053",
          "Exactly 19.0",
          "Exactly 1.00",
          "Exactly 0.500"
        ],
        "a": 0,
        "e": "<strong>Thermodynamic equilibrium constant calculation for conformational chair flip (Topic 423):</strong> Table 1 reports the equilibrium constant for equatorial preference over axial: $K_{\\text{eq}}([\\text{eq}]/[\\text{ax}]) = 19.0$. The reaction specified in the question is the reverse conformational change: equatorial $\\rightleftharpoons$ axial. According to fundamental chemical equilibrium principles, the equilibrium constant for a reverse reaction is the reciprocal of the forward equilibrium constant: $K_{\\text{rev}} = \\frac{[\\text{axial}]}{[\\text{equatorial}]} = \\frac{1}{K_{\\text{forward}}} = \\frac{1}{19.0} \\approx 0.0526 \\approx 0.053$.<br><br><em>Distractor Traps:</em><br>&bull; B gives the equilibrium constant for the forward process (axial $\\to$ equatorial, $19.0$), directionally inverting the quotient.<br>&bull; C assumes equal distribution ($K = 1.00$), which occurs only in degenerate unsubstituted cyclohexane.<br>&bull; D represents an arbitrary fraction unrelated to the experimental thermodynamic ratio."
      },
      {
        "q": "Why does a tert-butyl substituent possess an exceptionally large A-value (20.5 kJ/mol) compared to an isopropyl substituent (9.2 kJ/mol)?",
        "ch": [
          "The tert-butyl carbon atom is sp2-hybridized, enforcing an unyielding planar geometry",
          "The isopropyl group can rotate its single hydrogen toward the ring to avoid all steric clash",
          "The tert-butyl group has three methyls, guaranteeing 1,3-diaxial clash regardless of rotation",
          "The tert-butyl group forms strong intramolecular hydrogen bonds with adjacent axial protons"
        ],
        "a": 2,
        "e": "<strong>Conformational flexibility and rotational freedom in alkyl substituents (Topic 423):</strong> The isopropyl substituent ($-\\text{CH(CH}_3)_2$) contains one hydrogen atom and two methyl groups bonded to its $\\alpha$-carbon. By rotating about the exocyclic $\\text{C-C}$ bond connecting it to the ring, the isopropyl group can position its small hydrogen atom directly over the cyclohexane ring facing the syn-axial hydrogens, directing its two bulky methyl groups outward away from the ring. This rotation relieves a substantial fraction of 1,3-diaxial steric strain (limiting its A-value to $9.2\\text{ kJ/mol}$). In contrast, the tert-butyl substituent ($-\\text{C(CH}_3)_3$) possesses three bulky methyl groups and zero hydrogens on its $\\alpha$-carbon. No matter how the tert-butyl group rotates, at least one of its bulky methyl groups must point directly inward toward the syn-axial C3 and C5 hydrogens, creating inescapable, severe van der Waals overlap ($A = 20.5\\text{ kJ/mol}$).<br><br><em>Distractor Traps:</em><br>&bull; A falsely asserts tert-butyl is $sp^2$-hybridized; all carbons in alkyl groups are $sp^3$-hybridized.<br>&bull; B describes the rotameric relief available to isopropyl, but does not identify the structural cause of tert-butyl's extreme penalty.<br>&bull; D absurdly asserts that aliphatic hydrocarbon methyl groups form hydrogen bonds with ring hydrogens."
      },
      {
        "q": "For cis-1-tert-butyl-4-methylcyclohexane, which conformation represents the most thermodynamically stable chair state?",
        "ch": [
          "Both the tert-butyl and methyl groups occupy stable equatorial positions simultaneously",
          "Both the tert-butyl and methyl groups occupy high-energy axial positions simultaneously",
          "The methyl group is equatorial while the tert-butyl group is forced into the axial position",
          "The tert-butyl group is equatorial while the methyl group is forced into the axial position"
        ],
        "a": 3,
        "e": "<strong>Steric strain resolution in cis-1,4-disubstituted cyclohexanes (Topic 423):</strong> In a cis-1,4-disubstituted cyclohexane, one substituent must be oriented 'up' and the other must be oriented 'down' relative to ring planes. Because C1(up) is axial and C4(up) is equatorial, the two interconverting chair conformations for any cis-1,4 isomer are: (1) C1 substituent axial and C4 substituent equatorial, or (2) C1 substituent equatorial and C4 substituent axial. Both substituents cannot be equatorial at the same time. Comparing A-values from Table 1: $A(\\text{tert-butyl}) = 20.5\\text{ kJ/mol}$ and $A(\\text{methyl}) = 7.3\\text{ kJ/mol}$. If the tert-butyl group were axial, the molecule would suffer a catastrophic steric penalty of $20.5\\text{ kJ/mol}$. By placing the bulky tert-butyl group in the equatorial position, the chair ring is locked, forcing the smaller methyl group into the axial position, which costs only $7.3\\text{ kJ/mol}$. Conformation (2) is favored by $\\Delta \\Delta G^\\circ = 20.5 - 7.3 = 13.2\\text{ kJ/mol}$ ($K_{\\text{eq}} > 200:1$).<br><br><em>Distractor Traps:</em><br>&bull; A violates stereochemical geometry; a cis-1,4 isomer cannot achieve a diequatorial (e, e) conformation.<br>&bull; B describes a diaxial state (a, a), which is geometrically impossible for a cis-1,4 isomer.<br>&bull; C inverts thermodynamic stability; placing tert-butyl axial costs $20.5\\text{ kJ/mol}$ vs $7.3\\text{ kJ/mol}$ for axial methyl."
      }
    ]
  },
  {
    "id": "exam_cp60_10_disc",
    "sec": "C/P",
    "topic": "C/P Standalone Discrete Questions",
    "sheet": 8,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_10",
    "passage": "<div class=\"ttl\">Item Set (Questions 43&ndash;52)</div>\n<p><strong>Directions:</strong> Questions 43&ndash;52 are standalone questions that are not based on a passage. Select the single best answer to each question.</p>",
    "qs": [
      {
        "d": true,
        "q": "Calcium carbonate (CaCO3, Ksp = 3.4 x 10^-9) is sparingly soluble in pure water at pH 7.0. Why does CaCO3 dissolve completely in an acidic aqueous solution at pH 3.0?",
        "ch": [
          "Hydronium ions react with basic carbonate anions to form bicarbonate and CO2 gas, shifting equilibrium",
          "Acid protonates calcium cations into dicationic hydrides, preventing crystal lattice re-precipitation",
          "Lowering the pH increases the dielectric constant of water, weakening ionic bonds between solid ions",
          "Hydronium ions oxidize solid calcium into soluble calcium oxide through a spontaneous redox reaction"
        ],
        "a": 0,
        "e": "<strong>pH-dependent solubility of basic salts via Le Châtelier's principle (Topic 420):</strong> The dissolution equilibrium of calcium carbonate is governed by: $\\text{CaCO}_3(s) \\rightleftharpoons \\text{Ca}^{2+}(aq) + \\text{CO}_3^{2-}(aq)$ ($K_{sp} = [\\text{Ca}^{2+}][\\text{CO}_3^{2-}] = 3.4 \\times 10^{-9}$). The carbonate anion ($\\text{CO}_3^{2-}$) is a moderately strong Brønsted base (the conjugate base of the weak acid bicarbonate, $\\text{HCO}_3^-$, with $pK_{a2} = 10.3$). When the solution is acidified to $\\text{pH } 3.0$, a high concentration of hydronium ions ($\\text{H}_3\\text{O}^+$) is introduced, which drives coupled acid-base reactions: $\\text{CO}_3^{2-} + \\text{H}_3\\text{O}^+ \\rightleftharpoons \\text{HCO}_3^- + \\text{H}_2\\text{O}$ and $\\text{HCO}_3^- + \\text{H}_3\\text{O}^+ \\rightleftharpoons \\text{H}_2\\text{CO}_3 \\rightleftharpoons \\text{H}_2\\text{O} + \\text{CO}_2(g)$. By continuously consuming the product anion $[\\text{CO}_3^{2-}]$, the reaction quotient $Q = [\\text{Ca}^{2+}][\\text{CO}_3^{2-}]$ is kept well below $K_{sp}$, driving dissolution forward by Le Châtelier's principle until the solid dissolves completely.<br><br><em>Distractor Traps:</em><br>&bull; B absurdly claims hydronium protonates positive metal cations ($\\text{Ca}^{2+}$) into hydrides, which violates electrostatic repulsion.<br>&bull; C asserts pH modulates water's macroscopic dielectric constant; dielectric constant is an intrinsic bulk property governed by temperature.<br>&bull; D invents a redox reaction between protons and calcium; calcium remains in the $+2$ oxidation state throughout."
      },
      {
        "d": true,
        "q": "When (2R)-2-butanol is treated with p-toluenesulfonyl chloride (TsCl) in pyridine, (2R)-2-butyl tosylate is formed. Why does this reaction proceed with retention of configuration?",
        "ch": [
          "Pyridine acts as a chiral directing auxiliary that enforces front-side hydride attack on the alcohol",
          "The reaction breaks the oxygen-hydrogen bond of the alcohol without cleaving any bonds to the chiral carbon",
          "The reaction proceeds through a planar carbocation intermediate that recrystallizes into a single isomer",
          "Tosyl chloride undergoes two successive Walden inversions at the stereocenter to restore original geometry"
        ],
        "a": 1,
        "e": "<strong>Protecting group and sulfonate ester synthesis with retention of configuration (Topic 431):</strong> To convert the poor leaving group of an alcohol ($-\\text{OH}$) into an exceptional leaving group ($-\\text{OTs}$ or $-\\text{OMs}$), the alcohol is reacted with sulfonyl chlorides (such as $p$-toluenesulfonyl chloride, $\\text{TsCl}$) in the presence of pyridine. The nucleophilic lone pair of the alcohol oxygen attacks the electrophilic sulfur atom of $\\text{TsCl}$, expelling a chloride anion: $\\text{R-O-H} + \\text{Ts-Cl} + \\text{pyr} \\to \\text{R-O-Ts} + \\text{pyr}\\cdot\\text{HCl}$. Crucially, throughout this entire transformation, the covalent bond connecting the oxygen atom to the chiral stereocenter carbon ($\\text{C-O}$) remains completely intact. The only covalent bond broken is the oxygen-hydrogen bond ($\\text{O-H}$). Because the four bonds to the chiral carbon center are undisturbed, the reaction proceeds with $100\\%$ retention of absolute configuration (i.e. $(2R)$-alcohol yields $(2R)$-tosylate).<br><br><em>Distractor Traps:</em><br>&bull; A claims pyridine acts as a chiral auxiliary; pyridine is an achiral aromatic base used solely to neutralize generated $\\text{HCl}$.<br>&bull; C invokes a carbocation intermediate, which would cause racemization and loss of optical purity.<br>&bull; D proposes double Walden inversion; tosylation does not involve attack at the chiral carbon atom."
      },
      {
        "d": true,
        "q": "When 2,3-dimethyl-2,3-butanediol (pinacol) is heated in concentrated sulfuric acid, what product is formed and what mechanism drives this rearrangement?",
        "ch": [
          "2,3-Dimethyl-1,3-butadiene is formed via sequential bimolecular E2 eliminations across adjacent carbons",
          "2,3-Dimethylbutanal is formed via an intramolecular hydride shift following concerted water loss",
          "3,3-Dimethyl-2-butanone is formed via a methyl shift to yield a resonance-stabilized oxocarbenium ion",
          "2,3-Epoxy-2,3-dimethylbutane is formed via intramolecular nucleophilic attack of the adjacent alkoxide"
        ],
        "a": 2,
        "e": "<strong>Pinacol-pinacolone rearrangement mechanics and carbocation resonance driving force (Topic 432):</strong> In the acid-catalyzed pinacol rearrangement, 2,3-dimethyl-2,3-butanediol is treated with strong acid. One of the symmetrical tertiary hydroxyl groups is protonated to form an alkyloxonium ion ($-\\text{OH}_2^+$), which departs as water to generate a stable tertiary carbocation at C2: $(\\text{CH}_3)_2\\text{C}^+-\\text{C(OH)(CH}_3)_2$. Next, a methyl group from the adjacent C3 carbon undergoes a 1,2-methide shift to the carbocation center. This migration shifts the positive charge to C3, placing it directly adjacent to the remaining hydroxyl oxygen: $(\\text{CH}_3)_3\\text{C}-\\text{C}^+(\\text{OH})-\\text{CH}_3$. The unshared lone pair on the oxygen atom donates into the adjacent vacant $p$-orbital, generating an exceptionally stable oxocarbenium ion intermediate ($-\\text{C}=\\text{O}^+-\\text{H}$) in which every atom possesses a complete octet. Deprotonation by solvent yields 3,3-dimethyl-2-butanone (pinacolone).<br><br><em>Distractor Traps:</em><br>&bull; A describes double elimination to a diene, which is disfavored due to the overwhelming thermodynamic stability of the carbonyl bond ($C=O$).<br>&bull; B describes a hydride shift forming an aldehyde; pinacol has no $\\alpha$-hydrides, only methyl groups available for 1,2-migration.<br>&bull; D describes epoxide formation, which requires basic Williamson-type conditions rather than concentrated sulfuric acid."
      }
    ]
  }
];

if (typeof window !== 'undefined') {
  window.EXAM_CP60_10 = EXAM_CP60_10;
}
if (typeof globalThis !== 'undefined') {
  globalThis.EXAM_CP60_10 = EXAM_CP60_10;
}
