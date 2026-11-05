/* ---- exam_cp60_6.js ---- */
/* 60-minute Chem/Physical Practice Exam 6: 5 passages (30 Qs) + 3 discrete Qs = 33 Qs */
const EXAM_CP60_6 = [
  {
    "id": "exam_cp60_6_p1",
    "sec": "C/P",
    "topic": "Dielectric Breakdown & Electroporation in Cell Biology",
    "sheet": 1,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_6",
    "passage": "<div class=\"ttl\">Passage 1 (Questions 1&ndash;6)</div>\n<p>Electroporation is a biophysical technique that utilizes high-intensity pulsed electric fields ($E$) to induce transient permeability in cellular plasma membranes. The mammalian lipid bilayer can be modeled as a parallel-plate capacitor with thickness $d = 4.0\\text{ nm}$ and a hydrophobic core having a dielectric constant $\\kappa = 2.5$. Under physiological conditions, cells maintain an intrinsic resting transmembrane potential ($V_{rest} \\approx -70\\text{ mV}$, interior negative). When an external electric field $E_{ext}$ is applied across a spherical cell of radius $R$, it induces an additional transmembrane potential $\\Delta V_m$ described by the Schwan equation: $\\Delta V_m = 1.5 R E_{ext} \\cos(\\theta)$, where $\\theta$ is the angle between the electric field lines and the outward surface normal vector of the cell membrane.</p>\n<p>When the net transmembrane potential ($V_{net} = V_{rest} + \\Delta V_m$) exceeds a critical threshold known as the dielectric breakdown potential ($V_{crit} \\approx 1.0\\text{ V}$), the intense localized electric field generates compressive electrostatic Maxwell stress (electrostriction) that exceeds the mechanical shear modulus of the lipid bilayer. This stress drives the spontaneous nucleation and expansion of hydrophilic aqueous toroidal pores, facilitating the diffusion of impermeable xenobiotics, siRNA, and chemotherapeutic agents such as bleomycin into the cytoplasm.</p>\n<p>Biomedical engineers investigated the electroporation efficiency and survival of a human glioblastoma cell line ($R = 10.0\\ \\mu\\text{m}$) subjected to square electric pulses of duration $\\tau = 100\\ \\mu\\text{s}$ at various field strengths $E_{ext}$ in an electroporation cuvette with aluminum electrode gap $L = 2.0\\text{ mm}$. Membrane capacitance ($C_m$), pore formation density, bleomycin uptake percentage, and cell viability were quantified at $25^\\circ\\text{C}$ (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Electroporation parameters, pore density, bleomycin uptake, and cell viability</caption>\n  <thead>\n    <tr><th>Applied Field $E_{ext}$ (V/cm)</th><th>Electrode Voltage $V_0$ (V)</th><th>Peak $\\Delta V_m$ (V) at $\\theta = 0^\\circ$</th><th>Pore Density (pores/$\\mu\\text{m}^2$)</th><th>Bleomycin Uptake (%)</th><th>Cell Viability (%)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>200</td><td>40</td><td>0.30</td><td>0</td><td>1.2%</td><td>98.5%</td></tr>\n    <tr><td>500</td><td>100</td><td>0.75</td><td>0</td><td>2.5%</td><td>96.8%</td></tr>\n    <tr><td>800</td><td>160</td><td>1.20</td><td>18</td><td>44.2%</td><td>92.1%</td></tr>\n    <tr><td>1200</td><td>240</td><td>1.80</td><td>85</td><td>88.6%</td><td>81.4%</td></tr>\n    <tr><td>1800</td><td>360</td><td>2.70</td><td>210</td><td>96.4%</td><td>42.7%</td></tr>\n    <tr><td>2500</td><td>500</td><td>3.75</td><td>> 500 (irreversible)</td><td>99.1%</td><td>8.3%</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "Based on the Schwan equation and the data in Table 1, at what cellular location relative to the external field vector will dielectric breakdown and hydrophilic pore formation initiate first?",
        "ch": [
          "At the poles parallel to the field vector where theta equals zero or pi",
          "At the equator perpendicular to the field vector where theta equals pi/2",
          "Uniformly across the entire membrane surface regardless of orientation",
          "At random focal points governed strictly by local cholesterol density"
        ],
        "a": 0,
        "e": "<strong>Field angle dependence in the Schwan equation:</strong> The Schwan equation defines the induced potential as $\\Delta V_m = 1.5 R E_{ext} \\cos(\\theta)$. The cosine function achieves its maximum absolute magnitude ($|\\cos(\\theta)| = 1$) when $\\theta = 0^\\circ$ or $\\theta = 180^\\circ$ ($\\\\pi$ radians), which corresponds to the cell poles directly facing the anode and cathode along the field vector. Consequently, the induced potential reaches its highest amplitude at these poles, exceeding the breakdown threshold $V_{crit}$ before any other region of the cell membrane.<br><br><em>Distractor Traps:</em><br>&bull; B is incorrect because at the equator ($\\\theta = 90^\\circ$), $\\\\cos(90^\\circ) = 0$, meaning no external transmembrane potential is induced.<br>&bull; C is incorrect because the induced potential is strongly anisotropic and varies continuously with $\\\\cos(\\\theta)$.<br>&bull; D is incorrect because macroscale geometric orientation relative to the applied field vector dictates where threshold potential is breached, rather than stochastic cholesterol fluctuations."
      },
      {
        "q": "Assuming a cell membrane thickness of 4.0 nm and a dielectric breakdown potential of 1.0 V, what is the magnitude of the critical electric field within the hydrophobic core of the bilayer during breakdown?",
        "ch": [
          "1.0 x 10^7 V/m",
          "2.5 x 10^8 V/m",
          "4.0 x 10^5 V/m",
          "6.2 x 10^6 V/m"
        ],
        "a": 1,
        "e": "<strong>Calculation of uniform electric field across a thin dielectric:</strong> For a parallel-plate geometry, the electric field within the dielectric slab is given by $E = \\frac{\\Delta V}{d}$. Substituting the critical potential $\\Delta V = 1.0\\text{ V}$ and membrane thickness $d = 4.0\\text{ nm} = 4.0 \\times 10^{-9}\\text{ m}$: $E = \\frac{1.0\\text{ V}}{4.0 \\times 10^{-9}\\text{ m}} = 0.25 \\times 10^9\\text{ V/m} = 2.5 \\times 10^8\\text{ V/m}$. This enormous electrostatic field intensity directly destabilizes lipid packing.<br><br><em>Distractor Traps:</em><br>&bull; A erroneously divides $1.0$ by $1.0 \\times 10^{-7}$ or makes an order-of-magnitude exponent error.<br>&bull; C calculates $E = \\Delta V \\times d = 1.0 \\times 4.0 \\times 10^{-9}$ or inverts the metric prefix.<br>&bull; D multiplies the result by the dielectric constant $\\kappa = 2.5$ instead of recognizing that the measured potential difference already accounts for the medium."
      },
      {
        "q": "If the capacitance per unit area of the resting bilayer is 0.55 uF/cm^2, what is the total electrical charge stored on the outer leaflet of a spherical cell with radius 10.0 um at a resting potential of -70 mV?",
        "ch": [
          "1.8 x 10^-14 C",
          "9.2 x 10^-11 C",
          "4.8 x 10^-13 C",
          "2.4 x 10^-15 C"
        ],
        "a": 2,
        "e": "<strong>Capacitance and charge calculation for a spherical cell:</strong> The surface area of a sphere is $A = 4\\pi R^2$. For $R = 10.0\\ \\mu\\text{m} = 1.0 \\times 10^{-3}\\text{ cm}$, $A = 4\\pi (1.0 \\times 10^{-3}\\text{ cm})^2 = 4\\pi \\times 10^{-6}\\text{ cm}^2 \\approx 1.257 \\times 10^{-5}\\text{ cm}^2$. The total cell capacitance is $C = C_{area} \\times A = (0.55\\ \\mu\\text{F/cm}^2)(1.257 \\times 10^{-5}\\text{ cm}^2) \\approx 6.91 \\times 10^{-6}\\ \\mu\\text{F} = 6.91 \\times 10^{-12}\\text{ F}$. The stored charge magnitude is $Q = C \\times |V_{rest}| = (6.91 \\times 10^{-12}\\text{ F})(0.070\\text{ V}) \\approx 4.84 \\times 10^{-13}\\text{ C}$.<br><br><em>Distractor Traps:</em><br>&bull; A forgets the factor of $4$ in the spherical surface area formula, using $\\\\pi R^2$.<br>&bull; B fails to convert microfarads to farads, resulting in an answer two orders of magnitude too large.<br>&bull; D divides by the potential instead of multiplying by $V$ ($Q = C/V$)."
      },
      {
        "q": "To deliver bleomycin effectively while preserving cell viability above 80%, which applied electric field strength in Table 1 represents the optimal therapeutic window for reversible electroporation?",
        "ch": [
          "200 V/cm",
          "500 V/cm",
          "800 V/cm",
          "1200 V/cm"
        ],
        "a": 3,
        "e": "<strong>Evaluation of therapeutic window in electroporation:</strong> Effective electrochemotherapy requires high drug uptake paired with acceptable cellular survival. According to Table 1, at $E_{ext} = 1200\\text{ V/cm}$, bleomycin uptake reaches $88.6\\%$ while cell viability remains at $81.4\\%$ (which satisfies the criterion of $> 80\\%$). At $800\\text{ V/cm}$, uptake is only $44.2\\%$, and at $1800\\text{ V/cm}$, viability drops precipitously to $42.7\\%$ due to irreversible electroporation and cell lysis.<br><br><em>Distractor Traps:</em><br>&bull; A shows negligible drug uptake ($1.2\\%$) because the breakdown threshold has not been reached.<br>&bull; B produces no detectable pores and only $2.5\\%$ uptake.<br>&bull; C yields high survival ($92.1\\%$) but suboptimal uptake ($44.2\\%$), well below the maximal therapeutic efficacy achieved at $1200\\text{ V/cm}$."
      },
      {
        "q": "How does the electrostrictive compressive stress (Maxwell stress, P_M) acting on the lipid membrane scale with the transmembrane potential difference Delta V_m?",
        "ch": [
          "Inversely with the square root of the transmembrane potential difference",
          "Linearly in direct proportion to the transmembrane potential difference",
          "Quadratically in proportion to the square of transmembrane potential",
          "Independent of potential difference, depending only on bulk osmolarity"
        ],
        "a": 2,
        "e": "<strong>Scaling of Maxwell electrostatic stress with voltage:</strong> Electrostatic energy stored in a capacitor is $U = \\frac{1}{2} C V^2 = \\frac{1}{2} \\frac{\\kappa \\epsilon_0 A}{d} V^2$. The compressive electrostatic force between the plates is $F = -\\frac{dU}{dd} = \\frac{1}{2} \\frac{\\kappa \\epsilon_0 A}{d^2} V^2$. Dividing by area $A$ yields the compressive Maxwell pressure: $P_M = \\frac{1}{2} \\frac{\\kappa \\epsilon_0}{d^2} V^2 = \\frac{1}{2} \\kappa \\epsilon_0 E^2$. Thus, compressive stress scales quadratically ($P_M \\propto V^2$) with the transmembrane potential difference.<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly confuses stress with the inverse square root behavior seen in some diffusion equations.<br>&bull; B mistakes electric field force on an isolated single charge ($F = qE$) for electrostatic energy derivative of a distributed capacitor.<br>&bull; D falsely assumes mechanical stress is entirely osmotic, ignoring electrostatic attraction between opposite leaflet charges."
      },
      {
        "q": "If the distance between the cuvette electrodes were doubled to 4.0 mm while maintaining the power supply voltage V_0 at 240 V, what would be the resulting induced potential at theta = 0?",
        "ch": [
          "3.60 V",
          "2.40 V",
          "1.80 V",
          "0.90 V"
        ],
        "a": 3,
        "e": "<strong>Relationship between electrode separation, applied field, and induced potential:</strong> The electric field between parallel plate electrodes is $E_{ext} = \\frac{V_0}{L}$. When the distance $L$ is doubled from $2.0\\text{ mm}$ to $4.0\\text{ mm}$ at a constant voltage $V_0 = 240\\text{ V}$, the field is halved: $E_{ext} = \\frac{240\\text{ V}}{0.004\\text{ m}} = 60,000\\text{ V/m} = 600\\text{ V/cm}$ (compared to $1200\\text{ V/cm}$ previously). By the Schwan equation $\\Delta V_m = 1.5 R E_{ext} \\cos(\\theta)$, halving $E_{ext}$ proportionally halves the peak induced potential from $1.80\\text{ V}$ to $0.90\\text{ V}$.<br><br><em>Distractor Traps:</em><br>&bull; A mistakenly doubles the induced potential rather than halving it.<br>&bull; B assumes the induced potential is strictly equal to or fixed by the power supply voltage.<br>&bull; C fails to account for the change in electrode gap, assuming the field remains constant."
      }
    ]
  },
  {
    "id": "exam_cp60_6_p2",
    "sec": "C/P",
    "topic": "Ohm's Law & Axonal Axial vs Membrane Resistances",
    "sheet": 2,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_6",
    "passage": "<div class=\"ttl\">Passage 2 (Questions 7&ndash;12)</div>\n<p>Passive electrotonic conduction of graded potentials along cylindrical neuronal axons is quantitatively described by linear cable theory. An unmyelinated axon of radius $a$ behaves as an electrical transmission cable immersed in a conductive extracellular fluid. The electrical properties are parameterized by the intracellular axial resistance per unit length ($r_i$, in $\\Omega/\\text{cm}$) and the membrane resistance across a unit length of axon ($r_m$, in $\\Omega\\cdot\\text{cm}$). These linear cable parameters relate to intrinsic tissue resistivities via the axonal geometry: $r_i = \\frac{\\rho_i}{\\pi a^2}$ and $r_m = \\frac{R_m}{2\\pi a}$, where $\\rho_i$ is the cytoplasmic specific resistivity (typically $\\approx 100\\ \\Omega\\cdot\\text{cm}$) and $R_m$ is the specific membrane resistivity (in $\\Omega\\cdot\\text{cm}^2$).</p>\n<p>When a steady subthreshold depolarizing current $I_0$ is injected at point $x = 0$, the voltage deflection $V(x)$ decays exponentially with longitudinal distance $x$ according to the steady-state cable equation: $V(x) = V_0 e^{-x/\\lambda}$, where $\\lambda$ represents the axonal length constant (space constant): $\\lambda = \\sqrt{\\frac{r_m}{r_i}} = \\sqrt{\\frac{a R_m}{2 \\rho_i}}$. The length constant quantifies the distance over which electrotonic voltage attenuates to $1/e$ (approximately $36.8\\%$) of its initial value $V_0$. Concurrently, the temporal rate of membrane charging is governed by the membrane time constant $\\tau = r_m c_m = R_m C_m$, where $C_m$ is specific membrane capacitance.</p>\n<p>In demyelinating autoimmune neuropathies such as Guillain-Barr\\'{e} syndrome and multiple sclerosis, loss of the multi-lamellar myelin sheath reduces $R_m$ while increasing $C_m$. Neurophysiologists recorded electrotonic decay across four experimental axon preparations having different axonal radii and myelination states (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Cable properties, space constants, and conduction velocities across axon preparations</caption>\n  <thead>\n    <tr><th>Axon Type</th><th>Radius $a$ ($\\mu\\text{m}$)</th><th>$r_i$ ($10^6\\ \\Omega/\\text{cm}$)</th><th>$r_m$ ($10^5\\ \\Omega\\cdot\\text{cm}$)</th><th>Length Constant $\\lambda$ (mm)</th><th>Time Constant $\\tau$ (ms)</th><th>Conduction Velocity (m/s)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Type A (Large Myelinated)</td><td>5.0</td><td>1.27</td><td>250.0</td><td>4.44</td><td>1.8</td><td>55.0</td></tr>\n    <tr><td>Type B (Small Myelinated)</td><td>1.5</td><td>14.15</td><td>83.3</td><td>2.43</td><td>2.0</td><td>18.0</td></tr>\n    <tr><td>Type C (Unmyelinated C-Fiber)</td><td>0.5</td><td>127.32</td><td>1.59</td><td>0.11</td><td>12.5</td><td>1.1</td></tr>\n    <tr><td>Type D (Demyelinated Type A)</td><td>5.0</td><td>1.27</td><td>3.18</td><td>0.50</td><td>15.2</td><td>2.4 (conduction block)</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "Based on cable theory equations, how does the axonal length constant lambda scale with the axonal radius a in an unmyelinated cylindrical axon?",
        "ch": [
          "It scales directly with the square root of the axonal radius",
          "It scales inversely with the square of the axonal radius",
          "It scales linearly in direct proportion to the axonal radius",
          "It is completely independent of the axonal radius"
        ],
        "a": 0,
        "e": "<strong>Radius scaling of the axonal space constant:</strong> Substituting $r_i = \\frac{\\rho_i}{\\pi a^2}$ and $r_m = \\frac{R_m}{2\\pi a}$ into the length constant formula gives $\\lambda = \\sqrt{\\frac{r_m}{r_i}} = \\sqrt{\\frac{R_m / (2\\pi a)}{\\rho_i / (\\pi a^2)}} = \\sqrt{\\frac{a R_m}{2 \\rho_i}} = \\sqrt{a} \\sqrt{\\frac{R_m}{2\\rho_i}}$. Therefore, $\\lambda$ scales directly with the square root of the axonal radius ($\\lambda \\propto \\sqrt{a}$). This explains why the squid giant axon evolved a massive radius to maximize passive current spread.<br><br><em>Distractor Traps:</em><br>&bull; B confuses length constant scaling with the inverse square dependence of axial resistance $r_i$ on radius.<br>&bull; C overlooks the square root radical enclosing the ratio $r_m / r_i$.<br>&bull; D falsely assumes geometric variables cancel completely during algebraic simplification."
      },
      {
        "q": "At a distance of x = 2 lambda from the current injection electrode (x = 0), what fraction of the initial steady-state voltage deflection V_0 remains in a healthy axon?",
        "ch": [
          "50.0%",
          "13.5%",
          "36.8%",
          "4.9%"
        ],
        "a": 1,
        "e": "<strong>Exponential decay across multiples of the length constant:</strong> The steady-state cable voltage profile is $V(x) = V_0 e^{-x/\\lambda}$. Setting $x = 2\\lambda$ yields $V(2\\lambda) = V_0 e^{-2\\lambda / \\lambda} = V_0 e^{-2} = \\frac{V_0}{e^2} \\approx \\frac{V_0}{2.718^2} \\approx \\frac{V_0}{7.389} \\approx 0.1353 V_0$, which corresponds to $13.5\\%$ of $V_0$.<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly assumes linear voltage attenuation ($100\\% \\rightarrow 50\\% \\rightarrow 0\\%$).<br>&bull; C represents the voltage remaining at exactly one length constant ($x = \\lambda$), where $e^{-1} \\approx 36.8\\%$.<br>&bull; D calculates $e^{-3} \\approx 4.98\\%$, corresponding to a distance of $x = 3\\lambda$."
      },
      {
        "q": "Which biophysical alteration explains why demyelination in Type D axons causes catastrophic reduction of the length constant from 4.44 mm to 0.50 mm?",
        "ch": [
          "A massive elevation in cytoplasmic axial resistivity rho_i within the axoplasm",
          "A sharp contraction in axonal cross-sectional area due to mechanical pinching",
          "A precipitous loss of membrane resistance r_m due to trans-membrane leakage",
          "An increase in the extracellular fluid electrical resistance surrounding the axon"
        ],
        "a": 2,
        "e": "<strong>Mechanism of space constant collapse in demyelination:</strong> The length constant is defined as $\\lambda = \\sqrt{r_m / r_i}$. The myelin sheath consists of multiple wrapped lipid bilayers that provide enormous electrical insulation, yielding very high membrane resistance ($r_m = 250.0 \\times 10^5\\ \\Omega\\cdot\\text{cm}$). In demyelinated Type D axons, loss of the sheath creates high-conductance leak pathways through the exposed bare membrane, causing $r_m$ to plummet nearly 80-fold to $3.18 \\times 10^5\\ \\Omega\\cdot\\text{cm}$. Because $r_i$ remains unchanged ($1.27 \\times 10^6\\ \\Omega/\\text{cm}$), $\\lambda$ drops from $4.44\\text{ mm}$ to $\\sqrt{(3.18 \\times 10^5)/(1.27 \\times 10^6)} = 0.50\\text{ mm}$. Graded currents leak out before reaching the next node, resulting in conduction block.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because axoplasmic ionic composition and resistivity $\\rho_i$ are unaffected by external myelin loss.<br>&bull; B is incorrect because axonal diameter is preserved at $5.0\\ \\mu\\text{m}$ in Table 1.<br>&bull; D is incorrect because extracellular fluid volume and conductivity remain physiological and do not drive the length constant collapse."
      },
      {
        "q": "If a steady depolarizing current of 2.0 nA is injected into an axon with input resistance R_in = 25 MOhm, what is the initial voltage deflection V_0 at the injection site?",
        "ch": [
          "12.5 mV",
          "25.0 mV",
          "100.0 mV",
          "50.0 mV"
        ],
        "a": 3,
        "e": "<strong>Ohm's law calculation of input voltage deflection:</strong> By Ohm's law, the voltage deflection at the site of current injection is the product of the injected current and the input resistance of the cable: $V_0 = I_0 \\times R_{in}$. Substituting $I_0 = 2.0\\text{ nA} = 2.0 \\times 10^{-9}\\text{ A}$ and $R_{in} = 25\\text{ M}\\Omega = 25 \\times 10^6\\ \\Omega$: $V_0 = (2.0 \\times 10^{-9}\\text{ A})(25 \\times 10^6\\ \\Omega) = 50 \\times 10^{-3}\\text{ V} = 50.0\\text{ mV}$.<br><br><em>Distractor Traps:</em><br>&bull; A divides resistance by current or drops a factor of 4.<br>&bull; B divides the product by 2, incorrectly applying an alternating-current average formula.<br>&bull; C multiplies the current by 50 instead of 25, doubling the correct deflection."
      },
      {
        "q": "Why does a smaller membrane time constant tau (such as 1.8 ms in Type A versus 12.5 ms in Type C) accelerate action potential propagation along a nerve fiber?",
        "ch": [
          "The membrane capacitance charges and reaches threshold much more rapidly",
          "Axial resistance is converted into purely inductive reactance during charging",
          "The absolute refractory period of voltage-gated sodium channels is lengthened",
          "Active transport of sodium ions by Na+/K+-ATPase pumps is completely bypassed"
        ],
        "a": 0,
        "e": "<strong>Functional significance of the membrane time constant:</strong> The membrane time constant $\\tau = r_m c_m$ dictates the rate at which membrane potential changes in response to current flow: $\\Delta V(t) = V_{max}(1 - e^{-t/\\tau})$. A smaller $\\tau$ means the membrane capacitor charges rapidly, allowing the adjacent membrane segment to reach the threshold potential for activating voltage-gated sodium channels in a shorter timeframe. In myelinated Type A axons, low effective capacitance $c_m$ yields $\\tau = 1.8\\text{ ms}$, speeding saltatory conduction.<br><br><em>Distractor Traps:</em><br>&bull; B is incorrect because biological lipid membranes exhibit capacitive reactance, not inductive reactance.<br>&bull; C is incorrect because lengthening the refractory period would decrease firing frequency rather than speed propagation.<br>&bull; D is incorrect because primary active transport maintains steady-state ion gradients over minutes and is not the immediate kinetic driver of electrotonic depolarization."
      },
      {
        "q": "Comparing Type A and Type C axons in Table 1, by what approximate factor is the longitudinal axial resistance r_i higher in the unmyelinated C-fiber?",
        "ch": [
          "10-fold increase",
          "100-fold increase",
          "25-fold increase",
          "1000-fold increase"
        ],
        "a": 1,
        "e": "<strong>Axial resistance comparison from cable parameters:</strong> From Table 1, $r_i$ for Type A ($a = 5.0\\ \\mu\\text{m}$) is $1.27 \\times 10^6\\ \\Omega/\\text{cm}$, whereas $r_i$ for Type C ($a = 0.5\\ \\mu\\text{m}$) is $127.32 \\times 10^6\\ \\Omega/\\text{cm}$. Calculating the ratio: $\\frac{127.32 \\times 10^6}{1.27 \\times 10^6} \\approx 100.25 \\approx 100\\text{-fold}$. This aligns perfectly with the theoretical relationship $r_i \\propto 1/a^2$: since the radius of Type A is 10 times larger than Type C, its cross-sectional area is $10^2 = 100$ times larger, making $r_i$ 100 times smaller.<br><br><em>Distractor Traps:</em><br>&bull; A calculates the ratio of radii ($5.0 / 0.5 = 10$) instead of the inverse square ratio of cross-sectional areas.<br>&bull; C squares half the ratio of radii ($5^2 = 25$).<br>&bull; D adds an extra power of 10, confusing cross-sectional area with volume scaling."
      }
    ]
  },
  {
    "id": "exam_cp60_6_p3",
    "sec": "C/P",
    "topic": "Kirchhoff's Current & Voltage Rules in Multiloop Circuits",
    "sheet": 3,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_6",
    "passage": "<div class=\"ttl\">Passage 3 (Questions 13&ndash;18)</div>\n<p>Continuous invasive arterial blood pressure monitoring utilizes an intravascular catheter coupled to an external disposable pressure transducer. The core electrical sensing element is a Wheatstone bridge circuit fabricated from four piezoresistive silicon strain gauges ($R_1, R_2, R_3, R_4$) bonded to a flexible diaphragm. When arterial blood pressure flexes the diaphragm, mechanical strain induces fractional changes in resistance ($\\Delta R / R$). The circuit is analyzed using Kirchhoff's laws: the junction rule (conservation of electric charge, $\\sum I_{in} = \\sum I_{out}$) and the loop rule (conservation of electrical energy, $\\sum \\Delta V = 0$).</p>\n<p>The bridge is excited by a stable DC excitation voltage $V_{ex} = 5.00\\text{ V}$ applied across nodes A and C. The differential output voltage $V_{out} = V_B - V_D$ is measured across high-impedance instrumentation amplifier inputs at nodes B and D. In the baseline unstressed state, all four resistors are precisely matched: $R_1 = R_2 = R_3 = R_4 = R_0 = 1000.0\\ \\Omega$, yielding a balanced condition where $V_B = V_D = V_{ex}/2 = 2.50\\text{ V}$, such that $V_{out} = 0.00\\text{ mV}$. Under mechanical pressure $P$, the diaphragm flexes such that two opposing gauges experience tensile strain ($R_1 = R_4 = R_0 + \\Delta R$), while the other two experience compressive strain ($R_2 = R_3 = R_0 - \\Delta R$). Under this fully active four-arm bridge configuration, the differential output voltage is given by: $V_{out} = V_{ex} \\left( \\frac{\\Delta R}{R_0} \\right)$.</p>\n<p>Clinical engineers calibrated an arterial transducer by applying hydrostatic calibration pressures ranging from 0 to 300 mmHg using a mercury manometer and quantified resistance changes, branch currents, and amplifier output voltages (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Arterial pressure calibration, strain resistance changes, output voltages, and loop currents</caption>\n  <thead>\n    <tr><th>Applied Pressure (mmHg)</th><th>Strain Resistance $R_1$ ($\\Omega$)</th><th>$\\Delta R$ ($\\Omega$)</th><th>Node Voltage $V_B$ (V)</th><th>Node Voltage $V_D$ (V)</th><th>Output Voltage $V_{out}$ (mV)</th><th>Total Bridge Current $I_{total}$ (mA)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>0</td><td>1000.0</td><td>0.0</td><td>2.500</td><td>2.500</td><td>0.0</td><td>5.00</td></tr>\n    <tr><td>50</td><td>1002.5</td><td>+2.5</td><td>2.506</td><td>2.494</td><td>12.5</td><td>5.00</td></tr>\n    <tr><td>100</td><td>1005.0</td><td>+5.0</td><td>2.513</td><td>2.488</td><td>25.0</td><td>5.00</td></tr>\n    <tr><td>150</td><td>1007.5</td><td>+7.5</td><td>2.519</td><td>2.481</td><td>37.5</td><td>5.00</td></tr>\n    <tr><td>200</td><td>1010.0</td><td>+10.0</td><td>2.525</td><td>2.475</td><td>50.0</td><td>5.00</td></tr>\n    <tr><td>300</td><td>1015.0</td><td>+15.0</td><td>2.538</td><td>2.463</td><td>75.0</td><td>5.00</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "Kirchhoff's loop rule (voltage law) and junction rule (current law) are direct mathematical consequences of which fundamental physical conservation laws, respectively?",
        "ch": [
          "Conservation of electric energy and conservation of electric charge",
          "Conservation of linear momentum and conservation of electric energy",
          "Conservation of electric charge and conservation of magnetic flux",
          "Conservation of mechanical force and conservation of electric current"
        ],
        "a": 0,
        "e": "<strong>Physical foundation of Kirchhoff's laws:</strong> Kirchhoff's loop rule states that the directed sum of potential differences around any closed circuit loop is zero ($\\sum \\Delta V = 0$). Because electric potential is electric potential energy per unit charge, this rule is a direct statement of the conservation of electrical energy. Kirchhoff's junction rule states that the total current entering a circuit node equals the total current exiting ($\\sum I_{in} = \\sum I_{out}$). Because current is the rate of flow of charge ($I = dq/dt$), this rule directly reflects the conservation of electric charge.<br><br><em>Distractor Traps:</em><br>&bull; B erroneously cites conservation of linear momentum, which applies to mechanics and collisions rather than steady-state circuit loops.<br>&bull; C inverts the pair, matching the loop rule to charge and the junction rule to magnetic flux.<br>&bull; D cites 'conservation of mechanical force', which is not a valid physical conservation law."
      },
      {
        "q": "According to Table 1, why does the total bridge current I_total remain constant at exactly 5.00 mA across all applied pressures from 0 to 300 mmHg?",
        "ch": [
          "The excitation voltage source dynamically adjusts its output to maintain fixed current",
          "The equivalent resistance of each parallel branch (R1 + R2 and R3 + R4) remains exactly 2000 Ohms",
          "Current through compressive strain gauges is completely shunted into the ground reference",
          "The piezoresistive effect alters electron drift velocity without altering net circuit impedance"
        ],
        "a": 1,
        "e": "<strong>Equivalent resistance of the symmetric push-pull bridge:</strong> The Wheatstone bridge consists of two parallel branches connected across $V_{ex} = 5.00\\text{ V}$. Branch 1 consists of $R_1$ and $R_2$ in series: $R_{branch1} = R_1 + R_2 = (R_0 + \\Delta R) + (R_0 - \\Delta R) = 2R_0 = 2(1000.0\\ \\Omega) = 2000.0\\ \\Omega$. Similarly, Branch 2 consists of $R_3$ and $R_4$ in series: $R_{branch2} = R_3 + R_4 = (R_0 - \\Delta R) + (R_0 + \\Delta R) = 2R_0 = 2000.0\\ \\Omega$. Because $\\Delta R$ cancels out algebraically in both branches, the equivalent total resistance is $R_{eq} = \\frac{2000 \\times 2000}{2000 + 2000} = 1000.0\\ \\Omega$. Thus, $I_{total} = \\frac{V_{ex}}{R_{eq}} = \\frac{5.00\\text{ V}}{1000.0\\ \\Omega} = 5.00 \\times 10^{-3}\\text{ A} = 5.00\\text{ mA}$ at all pressures.<br><br><em>Distractor Traps:</em><br>&bull; A claims the voltage source is an active current-regulating servomechanism, whereas the passage specifies an ideal fixed $5.00\\text{ V}$ DC source.<br>&bull; C incorrectly assumes compressive resistors shunt current to ground, violating series loop continuity.<br>&bull; D provides a pseudo-scientific physical explanation that ignores Ohm's law and macroscopic resistance."
      },
      {
        "q": "What is the pressure sensitivity coefficient of this arterial pressure transducer expressed in microvolts of output per volt of excitation per mmHg (uV / V / mmHg)?",
        "ch": [
          "5.0 uV / V / mmHg",
          "25.0 uV / V / mmHg",
          "50.0 uV / V / mmHg",
          "10.0 uV / V / mmHg"
        ],
        "a": 2,
        "e": "<strong>Calculation of normalized transducer sensitivity:</strong> Sensitivity $S$ is defined as $S = \\frac{V_{out}}{V_{ex} \\times P}$. At an applied pressure $P = 100\\text{ mmHg}$, Table 1 indicates $V_{out} = 25.0\\text{ mV} = 25,000\\ \\mu\\text{V}$ and $V_{ex} = 5.00\\text{ V}$. Substituting these values yields: $S = \\frac{25,000\\ \\mu\\text{V}}{(5.00\\text{ V})(100\\text{ mmHg})} = \\frac{25,000}{500} = 50.0\\ \\mu\\text{V / V / mmHg}$. This matches the universal standard for clinical invasive physiological transducers.<br><br><em>Distractor Traps:</em><br>&bull; A divides by an extra factor of 10 or inverts the metric prefix.<br>&bull; B omits the excitation voltage normalization, calculating $V_{out} / P = 25\\text{ mV} / 100\\text{ mmHg} = 0.25\\text{ mV/mmHg} = 250\\ \\mu\\text{V/mmHg}$ and dividing incorrectly.<br>&bull; D calculates $50 / 5 = 10$, dividing by $V_{ex}$ twice."
      },
      {
        "q": "If resistor R2 experiences an accidental open-circuit failure (R2 -> infinity), what will be the resulting node voltage V_B and output voltage V_out at an applied pressure of 0 mmHg?",
        "ch": [
          "V_B = 0.00 V and V_out = -2.50 V",
          "V_B = 2.50 V and V_out = 0.00 V",
          "V_B = 1.25 V and V_out = -1.25 V",
          "V_B = 5.00 V and V_out = +2.50 V"
        ],
        "a": 3,
        "e": "<strong>Circuit analysis under open-circuit fault conditions:</strong> Node B is positioned between $R_1$ (connected to $V_{ex} = 5.00\\text{ V}$) and $R_2$ (connected to ground). By the voltage divider formula: $V_B = V_{ex} \\left( \\frac{R_2}{R_1 + R_2} \\right)$. When $R_2 \\rightarrow \\infty$, no current can flow to ground through Branch 1 ($I_1 = 0$). With zero current flowing through $R_1$, the voltage drop across $R_1$ is $\\Delta V_1 = I_1 R_1 = 0\\text{ V}$. Consequently, node B is pulled entirely up to the excitation rail: $V_B = 5.00\\text{ V}$. Meanwhile, Branch 2 remains healthy, so $V_D = 2.50\\text{ V}$. The differential output becomes $V_{out} = V_B - V_D = 5.00\\text{ V} - 2.50\\text{ V} = +2.50\\text{ V}$.<br><br><em>Distractor Traps:</em><br>&bull; A confuses an open circuit with a short circuit to ground, which would drop $V_B$ to $0\\text{ V}$.<br>&bull; B assumes the failure has no impact on branch symmetry.<br>&bull; C arbitrarily halves the node voltage without applying Kirchhoff's loop rule."
      },
      {
        "q": "What is the total electrical power dissipated as heat by the entire transducer bridge circuit during continuous arterial pressure monitoring?",
        "ch": [
          "50.0 mW",
          "10.0 mW",
          "25.0 mW",
          "12.5 mW"
        ],
        "a": 2,
        "e": "<strong>Calculation of electric power dissipation:</strong> Total electrical power dissipated by a resistive network is given by $P = V \\times I = I^2 R = \\frac{V^2}{R}$. Using the excitation voltage $V_{ex} = 5.00\\text{ V}$ and total bridge current $I_{total} = 5.00\\text{ mA} = 5.00 \\times 10^{-3}\\text{ A}$: $P = (5.00\\text{ V})(5.00 \\times 10^{-3}\\text{ A}) = 25.0 \\times 10^{-3}\\text{ W} = 25.0\\text{ mW}$. Alternatively, using equivalent resistance $R_{eq} = 1000\\ \\Omega$: $P = \\frac{V^2}{R_{eq}} = \\frac{5^2}{1000} = \\frac{25}{1000} = 25.0\\text{ mW}$.<br><br><em>Distractor Traps:</em><br>&bull; A multiplies by 2, incorrectly summing power across two independent supply rails.<br>&bull; B calculates power for only two of the four individual resistors ($12.5\\text{ mW} \\times 2$ miscalculation).<br>&bull; D calculates power dissipated in a single branch ($12.5\\text{ mW}$) rather than the entire bridge."
      },
      {
        "q": "In an unamplified transducer, if an intensive care patient's blood pressure drops acutely from 150 mmHg to 50 mmHg, what is the change in the differential output voltage Delta V_out?",
        "ch": [
          "-50.0 mV",
          "-37.5 mV",
          "-12.5 mV",
          "-25.0 mV"
        ],
        "a": 3,
        "e": "<strong>Voltage differential across hemodynamic pressure change:</strong> From Table 1, at $P = 150\\text{ mmHg}$, $V_{out} = 37.5\\text{ mV}$. At $P = 50\\text{ mmHg}$, $V_{out} = 12.5\\text{ mV}$. The change in differential output voltage is $\\Delta V_{out} = V_{final} - V_{initial} = 12.5\\text{ mV} - 37.5\\text{ mV} = -25.0\\text{ mV}$. This negative shift is accurately digitized by the ICU patient monitor to trigger a hypotension alarm.<br><br><em>Distractor Traps:</em><br>&bull; A doubles the correct drop, assuming a 200 mmHg pressure transition.<br>&bull; B reads the absolute value at 150 mmHg ($37.5\\text{ mV}$) instead of computing the difference.<br>&bull; C reads the final voltage ($12.5\\text{ mV}$) rather than the change $\\Delta V_{out}$."
      }
    ]
  },
  {
    "id": "exam_cp60_6_p4",
    "sec": "C/P",
    "topic": "Internal Resistance of Chemical Batteries & Electromotive Force",
    "sheet": 4,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_6",
    "passage": "<div class=\"ttl\">Passage 4 (Questions 19&ndash;24)</div>\n<p>Implantable cardiac pacemakers require exceptionally reliable primary electrochemical power sources to deliver rhythmic pacing stimuli to the myocardium over operating lifespans exceeding a decade. The gold standard cell chemistry is the lithium-iodine battery ($\\text{Li}/\\text{I}_2$-PVP), consisting of a metallic lithium anode and a solid poly-2-vinylpyridine iodine cathode. The overall cell discharge reaction is: $2\\text{Li}(s) + \\text{I}_2(s) \\rightarrow 2\\text{LiI}(s)$, exhibiting a standard electromotive force (EMF, $\\mathcal{E}$) of $2.80\\text{ V}$ at body temperature ($37^\\circ\\text{C}$).</p>\n<p>As the cell discharges, the reaction product, solid lithium iodide (LiI), precipitates at the interface between the anode and cathode, forming an electrolyte layer that conducts $\\text{Li}^+$ cations but acts as an electronic insulator. Consequently, the internal resistance ($r_{int}$) of the cell increases monotonically over time from an initial value of $< 100\\ \\Omega$ in a fresh battery to $> 10,000\\ \\Omega$ near end-of-life (EOL). The terminal voltage ($V_t$) delivered to the pacemaker pulse-generator circuit across load resistance $R_L$ is governed by Ohm's law and Kirchhoff's voltage rule: $V_t = \\mathcal{E} - I r_{int} = \\mathcal{E} \\left( \\frac{R_L}{R_L + r_{int}} \\right)$, where $I = \\frac{\\mathcal{E}}{R_L + r_{int}}$ is the operating current.</p>\n<p>During normal standby operation, the pacemaker circuitry draws a quiescent current across an equivalent load $R_L = 100\\text{ k}\\Omega$. When pacing pulses are delivered, current is temporarily drawn from a parallel output buffer capacitor. Biomedical engineers monitored the electrical discharge characteristics of five identical $\\text{Li}/\\text{I}_2$ cells over a simulated 12-year accelerated aging protocol (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Battery discharge metrics across simulated pacemaker service life</caption>\n  <thead>\n    <tr><th>Service Time (Years)</th><th>Delivered Capacity (Ah)</th><th>Internal Resistance $r_{int}$ ($\\Omega$)</th><th>Terminal Voltage $V_t$ (V) at $R_L = 100\\text{ k}\\Omega$</th><th>Operating Current $I$ ($\\mu\\text{A}$)</th><th>Pacing Status</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>0 (Beginning of Life, BOL)</td><td>0.00</td><td>80</td><td>2.798</td><td>27.98</td><td>Optimal Normal Function</td></tr>\n    <tr><td>3</td><td>0.35</td><td>350</td><td>2.790</td><td>27.90</td><td>Optimal Normal Function</td></tr>\n    <tr><td>6 (Mid-Life)</td><td>0.70</td><td>1,200</td><td>2.767</td><td>27.67</td><td>Optimal Normal Function</td></tr>\n    <tr><td>9 (Elective Replacement, ERI)</td><td>1.05</td><td>4,800</td><td>2.672</td><td>26.72</td><td>ERI Flag Triggered</td></tr>\n    <tr><td>11 (End of Service, EOS)</td><td>1.25</td><td>15,000</td><td>2.435</td><td>24.35</td><td>Pacing Rate Drops 10%</td></tr>\n    <tr><td>12 (Exhaustion)</td><td>1.30</td><td>55,000</td><td>1.806</td><td>18.06</td><td>Erratic Output / Failure</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "What fundamental electrochemical phenomenon causes the internal resistance r_int of the lithium-iodine pacemaker battery to increase by over two orders of magnitude over its service life?",
        "ch": [
          "Accumulation of poorly conductive solid lithium iodide precipitate at the electrode interface",
          "Depletion of metallic lithium causing an increase in electronic conductivity of the outer casing",
          "Volumetric expansion of gaseous iodine building extreme hydrostatic pressure in the cell",
          "Thermal breakdown of the poly-2-vinylpyridine complex into volatile hydrocarbon gases"
        ],
        "a": 0,
        "e": "<strong>Electrochemical mechanism of internal resistance growth:</strong> As the cell discharges via $2\\text{Li} + \\text{I}_2 \\rightarrow 2\\text{LiI}$, the solid lithium iodide product precipitates between the anode and cathode. While crystalline LiI allows slow interstitial $\\text{Li}^+$ hopping, it possesses low ionic conductivity and high ohmic resistance compared to metallic lithium and the liquid/paste electrolyte. As this LiI layer thickens with cumulative capacity delivered, the path length for ion diffusion increases, driving $r_{int}$ upward from $80\\ \\Omega$ to $55,000\\ \\Omega$.<br><br><em>Distractor Traps:</em><br>&bull; B is incorrect because metallic lithium depletion reduces capacity, but the high resistance is specifically caused by the thickening LiI salt layer.<br>&bull; C is incorrect because iodine is complexed into a solid poly-2-vinylpyridine matrix and does not generate gaseous iodine under body temperature conditions.<br>&bull; D is incorrect because the polymer complex is thermally stable at $37^\\circ\\text{C}$ and does not decompose into hydrocarbons."
      },
      {
        "q": "At year 9 (Elective Replacement Indicator, ERI), what is the terminal voltage V_t if a temporary diagnostic testing mode drops the effective circuit load resistance R_L to 10 kOhm?",
        "ch": [
          "2.67 V",
          "1.89 V",
          "2.25 V",
          "1.40 V"
        ],
        "a": 1,
        "e": "<strong>Calculation of loaded terminal voltage with internal resistance:</strong> At year 9, Table 1 specifies an internal resistance $r_{int} = 4,800\\ \\Omega = 4.8\\text{ k}\\Omega$ and cell EMF $\\mathcal{E} = 2.80\\text{ V}$. When the load is reduced to $R_L = 10\\text{ k}\\Omega = 10,000\\ \\Omega$, the terminal voltage is given by the voltage divider formula: $V_t = \\mathcal{E} \\left( \\frac{R_L}{R_L + r_{int}} \\right) = 2.80\\text{ V} \\left( \\frac{10,000}{10,000 + 4,800} \\right) = 2.80 \\left( \\frac{10,000}{14,800} \\right) = 2.80 \\times 0.6757 \\approx 1.892\\text{ V} \\approx 1.89\\text{ V}$. This severe voltage sag under higher current load is the exact diagnostic signature pacemakers use to detect battery depletion.<br><br><em>Distractor Traps:</em><br>&bull; A reflects the terminal voltage under the standard high-impedance $100\\text{ k}\\Omega$ load ($2.672\\text{ V}$).<br>&bull; C incorrectly sets $r_{int}$ to $2,400\\ \\Omega$ (half the actual value).<br>&bull; D divides the EMF by 2, assuming equal load and internal resistances ($10\\text{ k}\\Omega / 10\\text{ k}\\Omega$)."
      },
      {
        "q": "What is the maximum electrical power that this battery can theoretically transfer to an external resistive load at the Beginning of Life (r_int = 80 Ohms)?",
        "ch": [
          "98.0 mW",
          "49.0 mW",
          "24.5 mW",
          "12.2 mW"
        ],
        "a": 2,
        "e": "<strong>Maximum power transfer theorem calculation:</strong> By the maximum power transfer theorem, maximum power is delivered to an external load when the load resistance matches the internal resistance ($R_L = r_{int}$). Under this matched condition, $R_L = 80\\ \\Omega$, the circuit current is $I = \\frac{\\mathcal{E}}{2 r_{int}} = \\frac{2.80\\text{ V}}{160\\ \\Omega} = 0.0175\\text{ A} = 17.5\\text{ mA}$. The maximum power delivered to the load is $P_{max} = I^2 R_L = \\frac{\\mathcal{E}^2}{4 r_{int}} = \\frac{(2.80)^2}{4(80)} = \\frac{7.84}{320} = 0.0245\\text{ W} = 24.5\\text{ mW}$.<br><br><em>Distractor Traps:</em><br>&bull; A calculates $\\mathcal{E}^2 / r_{int} = 7.84 / 80 = 98\\text{ mW}$, which omits the factor of 4 in the denominator.<br>&bull; B calculates $\\mathcal{E}^2 / (2 r_{int}) = 7.84 / 160 = 49\\text{ mW}$, which is the total power dissipated by both internal and external resistors combined.<br>&bull; D divides by 8 instead of 4, yielding half the correct maximum power."
      },
      {
        "q": "Why does a standard digital voltmeter with a high input impedance of 10 MOhm fail to detect battery depletion if used to measure battery voltage disconnected from the circuit load?",
        "ch": [
          "High voltmeter resistance causes an excessive current draw that recharges the battery",
          "The voltmeter converts terminal DC voltage into alternating current via its internal diode bridge",
          "Internal resistance drops to zero whenever external connections are disconnected from the cell",
          "Negligible current flows through r_int, making the measured terminal voltage virtually equal to EMF"
        ],
        "a": 3,
        "e": "<strong>Voltmeter loading and internal resistance measurement:</strong> Terminal voltage is $V_t = \\mathcal{E} - I r_{int}$. A high-impedance voltmeter ($R_{meter} = 10\\text{ M}\\Omega = 10^7\\ \\Omega$) draws an infinitesimal current: $I = \\frac{\\mathcal{E}}{R_{meter} + r_{int}} \\approx \\frac{2.80\\text{ V}}{10^7\\ \\Omega} = 2.8 \\times 10^{-7}\\text{ A} = 0.28\\ \\mu\\text{A}$. Even at end of service where $r_{int} = 15,000\\ \\Omega$, the internal ohmic drop is only $I r_{int} = (2.8 \\times 10^{-7}\\text{ A})(15,000\\ \\Omega) \\approx 0.0042\\text{ V} = 4.2\\text{ mV}$. Thus, the meter measures $V_t = 2.80 - 0.004 = 2.796\\text{ V}$, appearing nearly pristine. To detect depletion, the cell must be measured under an active resistive load.<br><br><em>Distractor Traps:</em><br>&bull; A claims the meter draws excessive current and recharges the cell, which is physically impossible for a passive voltmeter.<br>&bull; B claims a DC voltmeter rectifies into AC, which is nonsensical.<br>&bull; C claims internal resistance vanishes when unloaded, whereas $r_{int}$ is an intrinsic material property of the physical LiI layer."
      },
      {
        "q": "If the total usable capacity of the battery is 1.30 Ah, what is the total theoretical electrical charge stored in the cell at BOL expressed in Coulombs?",
        "ch": [
          "4,680 Coulombs",
          "1,300 Coulombs",
          "78,000 Coulombs",
          "2,160 Coulombs"
        ],
        "a": 0,
        "e": "<strong>Unit conversion between Ampere-hours and Coulombs:</strong> Electric charge is current multiplied by time ($Q = I \\times t$). One Ampere-hour ($1\\text{ Ah}$) represents a current of one Ampere flowing for one hour ($3600\\text{ seconds}$). Therefore: $1\\text{ Ah} = (1\\text{ C/s})(3600\\text{ s}) = 3600\\text{ C}$. For a capacity of $1.30\\text{ Ah}$: $Q = 1.30 \\times 3600\\text{ C} = 4680\\text{ C}$.<br><br><em>Distractor Traps:</em><br>&bull; B assumes $1\\text{ Ah} = 1000\\text{ C}$ by treating the hour as a metric prefix.<br>&bull; C multiplies by 60,000 instead of 3,600.<br>&bull; D divides by 3600 instead of multiplying ($1.30 / 3600$)."
      },
      {
        "q": "Over the first 6 years of service, Table 1 shows internal resistance rising from 80 Ohms to 1,200 Ohms while current remains approximately 28 uA. What is the increase in power wasted as heat internally within the battery?",
        "ch": [
          "4.21 nW",
          "856.8 nW",
          "12.45 uW",
          "34.12 uW"
        ],
        "a": 1,
        "e": "<strong>Internal ohmic heat dissipation calculation:</strong> Power dissipated internally within the battery resistance is $P_{int} = I^2 r_{int}$. At BOL: $P_{BOL} = (27.98 \\times 10^{-6}\\text{ A})^2 (80\\ \\Omega) \\approx (7.83 \\times 10^{-10})(80) \\approx 6.26 \\times 10^{-8}\\text{ W} = 62.6\\text{ nW}$. At year 6: $P_{yr6} = (27.67 \\times 10^{-6}\\text{ A})^2 (1200\\ \\Omega) \\approx (7.66 \\times 10^{-10})(1200) \\approx 9.19 \\times 10^{-7}\\text{ W} = 919.4\\text{ nW}$. The increase in internally dissipated heat power is $\\Delta P_{int} = 919.4\\text{ nW} - 62.6\\text{ nW} = 856.8\\text{ nW}$.<br><br><em>Distractor Traps:</em><br>&bull; A makes an exponent error, calculating in picowatts.<br>&bull; C calculates $P = I V$ across the terminal voltage ($27.67\\ \\mu\\text{A} \\times 2.767\\text{ V} \\approx 76.5\\ \\mu\\text{W}$) rather than internal $I^2 r_{int}$.<br>&bull; D calculates total power delivered to the external load resistance."
      }
    ]
  },
  {
    "id": "exam_cp60_6_p5",
    "sec": "C/P",
    "topic": "RC Low-Pass and High-Pass Filters in Biomedical Signals",
    "sheet": 5,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_6",
    "passage": "<div class=\"ttl\">Passage 5 (Questions 25&ndash;30)</div>\n<p>Electrocardiography (ECG) records minute extracellular electrical potentials ($0.1\\text{ to }5.0\\text{ mV}$) generated by the synchronous depolarization and repolarization of myocardial syncytia. Diagnostic surface ECG recordings are severely vulnerable to two dominant sources of electrical noise: high-frequency electromyographic (EMG) muscle tremor interference and $60\\text{ Hz}$ AC powerline electromagnetic pickup, as well as ultra-low-frequency ($< 0.5\\text{ Hz}$) baseline wander artifacts caused by respiratory thorax movement and electrochemically unstable skin-electrode interfaces. To isolate physiological cardiac signals, analog front-end instrumentation amplifiers pass the raw biosignal through passive resistor-capacitor ($RC$) filter stages.</p>\n<p>A first-order passive $RC$ high-pass filter comprises a capacitor $C$ in series with the input followed by a shunt resistor $R$ across the output to ground. The capacitive reactance $X_C = \\frac{1}{2\\pi f C}$ approaches infinity at DC ($f = 0$), blocking DC offsets while passing higher frequencies. Conversely, a first-order passive $RC$ low-pass filter features a series resistor $R$ followed by a shunt capacitor $C$ to ground; at high frequencies, $X_C \\rightarrow 0$, shunting high-frequency noise to ground. In both topologies, the cutoff frequency ($f_c$, or $-3\\text{ dB}$ corner frequency) is defined as: $f_c = \\frac{1}{2\\pi R C}$. At $f = f_c$, the output voltage amplitude attenuates to $\\frac{1}{\\sqrt{2}} \\approx 70.7\\%$ of the input amplitude, and the phase angle shifts by $45^\\circ$. The transfer function voltage gain magnitude for the low-pass filter is $|H_{LP}(f)| = \\frac{1}{\\sqrt{1 + (f/f_c)^2}}$, and for the high-pass filter is $|H_{HP}(f)| = \\frac{f/f_c}{\\sqrt{1 + (f/f_c)^2}}$.</p>\n<p>Biomedical engineers designed an analog cascaded bandpass filter circuit for an ambulatory Holter monitor consisting of an $RC$ high-pass stage ($R_1 = 318\\text{ k}\\Omega, C_1 = 1.0\\ \\mu\\text{F}$) followed by an $RC$ low-pass stage ($R_2 = 1.06\\text{ k}\\Omega, C_2 = 1.0\\ \\mu\\text{F}$). Frequency response gain and attenuation characteristics were evaluated across simulated interference frequencies (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Frequency response, impedance reactance, and signal gain across ECG filter stages</caption>\n  <thead>\n    <tr><th>Frequency $f$ (Hz)</th><th>Signal Component</th><th>High-Pass Reactance $X_{C1}$ ($\\Omega$)</th><th>High-Pass Gain $|H_{HP}|$</th><th>Low-Pass Reactance $X_{C2}$ ($\\Omega$)</th><th>Low-Pass Gain $|H_{LP}|$</th><th>Net Cascaded Gain $|H_{net}|$</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>0.05</td><td>Baseline Wander</td><td>3,183,099</td><td>0.100</td><td>3,183,099</td><td>1.000</td><td>0.100 (-20 dB)</td></tr>\n    <tr><td>0.50</td><td>High-Pass Cutoff ($f_{c1}$)</td><td>318,310</td><td>0.707</td><td>318,310</td><td>1.000</td><td>0.707 (-3 dB)</td></tr>\n    <tr><td>10.0</td><td>ECG QRS Complex Peak</td><td>15,915</td><td>0.999</td><td>15,915</td><td>0.998</td><td>0.997 (-0.03 dB)</td></tr>\n    <tr><td>60.0</td><td>Powerline Hum</td><td>2,653</td><td>1.000</td><td>2,653</td><td>0.928</td><td>0.928 (-0.65 dB)</td></tr>\n    <tr><td>150.0</td><td>Low-Pass Cutoff ($f_{c2}$)</td><td>1,061</td><td>1.000</td><td>1,061</td><td>0.707</td><td>0.707 (-3 dB)</td></tr>\n    <tr><td>1500.0</td><td>EMG Noise / Radiofrequency</td><td>106</td><td>1.000</td><td>106</td><td>0.100</td><td>0.100 (-20 dB)</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "What is the primary physical mechanism that allows a series capacitor in an RC high-pass filter to eliminate respiratory baseline wander artifacts at 0.05 Hz?",
        "ch": [
          "Capacitive reactance approaches infinity as frequency approaches zero, blocking DC currents",
          "The capacitor stores electromagnetic energy within an internal toroidal magnetic core",
          "The capacitor undergoes dielectric breakdown, shorting baseline drift directly to ground",
          "Capacitive phase angle shifts by 180 degrees, cancelling signals by destructive interference"
        ],
        "a": 0,
        "e": "<strong>Capacitive reactance and DC blocking:</strong> Capacitive reactance is given by $X_C = \\frac{1}{2\\pi f C}$. As frequency $f$ approaches zero (direct current or slow baseline wander), $X_C \\rightarrow \\infty$, meaning the capacitor presents near-infinite impedance to the input signal. Because the capacitor is in series with the signal path, it acts as an open circuit to DC and ultra-low frequencies ($0.05\\text{ Hz}$), preventing baseline wander from reaching the amplifier input while allowing higher cardiac frequencies to pass.<br><br><em>Distractor Traps:</em><br>&bull; B describes the operation of an inductor with a ferromagnetic core, not a capacitor.<br>&bull; C describes destructive dielectric breakdown, which is a catastrophic component failure, not passive linear filtering.<br>&bull; D claims the phase shift is $180^\\circ$, whereas an ideal capacitor introduces a $90^\\circ$ phase shift (or $45^\\circ$ at cutoff)."
      },
      {
        "q": "Using the component values for the low-pass filter stage (R2 = 1.06 kOhm, C2 = 1.0 uF), what is the exact cutoff frequency fc2?",
        "ch": [
          "0.50 Hz",
          "150 Hz",
          "60.0 Hz",
          "1500 Hz"
        ],
        "a": 1,
        "e": "<strong>Calculation of low-pass cutoff frequency:</strong> The cutoff frequency is defined as $f_c = \\frac{1}{2\\pi R C}$. Substituting $R_2 = 1.06\\text{ k}\\Omega = 1060\\ \\Omega$ and $C_2 = 1.0\\ \\mu\\text{F} = 1.0 \\times 10^{-6}\\text{ F}$: $f_{c2} = \\frac{1}{2\\pi (1060)(1.0 \\times 10^{-6})} = \\frac{1}{6.2832 \\times 1.06 \\times 10^{-3}} = \\frac{1}{6.66 \\times 10^{-3}} \\approx 150.15\\text{ Hz} \\approx 150\\text{ Hz}$. This matches the standard AAMC diagnostic ECG upper bandwidth limit.<br><br><em>Distractor Traps:</em><br>&bull; A reflects the high-pass stage cutoff frequency ($f_{c1} = 0.5\\text{ Hz}$).<br>&bull; C is the powerline frequency ($60\\text{ Hz}$), which is inside the passband.<br>&bull; D is one decade above the cutoff frequency where attenuation reaches $-20\\text{ dB}$."
      },
      {
        "q": "At a frequency of 1500 Hz (such as high-frequency electromyographic noise), what is the attenuation of the low-pass filter stage in decibels (dB)?",
        "ch": [
          "-3 dB",
          "-6 dB",
          "-20 dB",
          "-40 dB"
        ],
        "a": 2,
        "e": "<strong>Decibel attenuation calculation for a first-order filter:</strong> Decibel voltage gain is defined as $\\text{dB} = 20 \\log_{10}(|H|)$. At $f = 1500\\text{ Hz}$, which is exactly one decade ($10 \\times$) above the low-pass cutoff $f_{c2} = 150\\text{ Hz}$, Table 1 indicates $|H_{LP}| = 0.100$. Computing the decibels: $\\text{dB} = 20 \\log_{10}(0.100) = 20(-1) = -20\\text{ dB}$. A first-order passive filter always rolls off at a characteristic rate of $-20\\text{ dB/decade}$.<br><br><em>Distractor Traps:</em><br>&bull; A corresponds to the attenuation at the corner frequency $f_c$ where $|H| = 1/\\sqrt{2} \\approx 0.707$.<br>&bull; B corresponds to an amplitude reduction by half ($|H| = 0.5$).<br>&bull; D corresponds to two decades of roll-off ($-40\\text{ dB}$ at $15\\text{ kHz}$) or a second-order filter slope."
      },
      {
        "q": "If the design team wishes to decrease the low-pass cutoff frequency fc2 from 150 Hz to 100 Hz without changing capacitor C2, how must resistor R2 be modified?",
        "ch": [
          "Decreased to 707 Ohms by placing a second parallel resistor",
          "Kept identical because cutoff frequency is independent of resistance",
          "Decreased to 530 Ohms by substituting a smaller carbon resistor",
          "Increased to 1.59 kOhms by adding series resistance to the input"
        ],
        "a": 3,
        "e": "<strong>Inverse relationship between resistance and cutoff frequency:</strong> Cutoff frequency is inversely proportional to resistance: $f_c = \\frac{1}{2\\pi R C} \\implies R = \\frac{1}{2\\pi f_c C}$. To decrease $f_c$ from $150\\text{ Hz}$ to $100\\text{ Hz}$ (a factor of $150/100 = 1.5$), $R$ must increase by the same factor: $R_{new} = 1.5 \\times R_{old} = 1.5 \\times 1060\\ \\Omega = 1590\\ \\Omega = 1.59\\text{ k}\\Omega$.<br><br><em>Distractor Traps:</em><br>&bull; A decreases resistance by $1/\\sqrt{2}$, confusing frequency scaling with $-3\\text{ dB}$ power ratios.<br>&bull; B falsely claims cutoff is independent of resistance.<br>&bull; C halves the resistance, which would double $f_c$ to $300\\text{ Hz}$."
      },
      {
        "q": "Why does this simple first-order RC low-pass filter fail to completely suppress 60 Hz powerline hum while recording an ECG?",
        "ch": [
          "60 Hz powerline hum is completely non-electrical in origin and cannot be filtered",
          "Powerline hum has infinite capacitive reactance that accelerates low-pass conduction",
          "60 Hz lies below the 150 Hz low-pass cutoff, remaining inside the unattenuated passband",
          "The filter only operates on alternating current, whereas 60 Hz hum is pure direct current"
        ],
        "a": 2,
        "e": "<strong>Passband characteristics and notch filter requirements:</strong> The low-pass filter has a cutoff frequency $f_{c2} = 150\\text{ Hz}$. All frequencies below $150\\text{ Hz}$ lie within the passband, where attenuation is minimal (Table 1 shows $|H_{LP}| = 0.928$, an attenuation of only $-0.65\\text{ dB}$). Because powerline hum ($60\\text{ Hz}$) is below $150\\text{ Hz}$, it passes through virtually unimpeded. To eliminate $60\\text{ Hz}$ interference without attenuating cardiac QRS complexes ($0.5\\text{ to }100\\text{ Hz}$), a dedicated narrow-band bandstop (notch) filter is required.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because powerline hum is electromagnetic interference and can be filtered by notch filters.<br>&bull; B is nonsensical; reactance at $60\\text{ Hz}$ is $2653\\ \\Omega$, which is finite.<br>&bull; D is incorrect because $60\\text{ Hz}$ powerline hum is alternating current ($60\\text{ cycles/second}$), not direct current."
      },
      {
        "q": "What is the phase angle shift between output voltage and input voltage at the exact cutoff frequency of the low-pass filter stage (fc2 = 150 Hz)?",
        "ch": [
          "+90 degrees (output leads input by 90 degrees)",
          "0 degrees (output and input are precisely in phase)",
          "+180 degrees (output is inverted relative to input)",
          "-45 degrees (output lags input by 45 degrees)"
        ],
        "a": 3,
        "e": "<strong>Phase shift of a first-order RC low-pass filter at cutoff:</strong> The complex transfer function of a low-pass filter is $H(j\\omega) = \\frac{1}{1 + j\\omega R C} = \\frac{1}{1 + j(f/f_c)}$. The phase angle is $\\phi = -\\arctan(f / f_c)$. At the cutoff frequency $f = f_c$, the ratio $f / f_c = 1$. Because $\\arctan(1) = 45^\\circ$ ($\\\\pi/4$ radians), the phase angle is $\\phi = -45^\\circ$. The negative sign indicates that the output voltage lags behind the input voltage by $45^\\circ$.<br><br><em>Distractor Traps:</em><br>&bull; A describes a pure differentiator or high-pass lead at low frequencies.<br>&bull; B describes the ideal passband far below cutoff ($f \\ll f_c$) where phase shift approaches $0^\\circ$.<br>&bull; C describes a complete signal inversion produced by an inverting operational amplifier, not a first-order passive $RC$ network."
      }
    ]
  },
  {
    "id": "exam_cp60_6_disc",
    "sec": "C/P",
    "topic": "C/P Standalone Discrete Questions",
    "sheet": 8,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp60_6",
    "passage": "<div class=\"ttl\">Item Set (Questions 43&ndash;52)</div>\n<p><strong>Directions:</strong> Questions 43&ndash;52 are standalone questions that are not based on a passage. Select the single best answer to each question.</p>",
    "qs": [
      {
        "d": true,
        "q": "How does myelination in peripheral motor axons accelerate action potential propagation via saltatory conduction?",
        "ch": [
          "It decreases membrane capacitance and increases membrane resistance, confining depolarization to nodes",
          "It increases axonal diameter at internodes, lowering axoplasmic resistance to absolute zero",
          "It eliminates the need for voltage-gated sodium channels along the entire length of the axon",
          "It converts transcellular electrical conduction into purely acoustic wave propagation"
        ],
        "a": 0,
        "e": "<strong>Biophysics of saltatory conduction (Topic 292):</strong> Myelin consists of concentric lipid bilayer wraps that dramatically increase the effective membrane thickness $d$. Because capacitance is $C = \\frac{\\kappa \\epsilon_0 A}{d}$, thickening the dielectric drastically decreases membrane capacitance ($C_m$), meaning far less charge is required to depolarize the membrane. Concurrently, myelin acts as an insulator, massively increasing membrane resistance ($R_m$) and preventing current leakage. Consequently, passive electrotonic current travels rapidly and with minimal attenuation through internodes to the Nodes of Ranvier, where high-density $\\text{Na}_V$ channels regenerate the action potential.<br><br><em>Distractor Traps:</em><br>&bull; B is incorrect because internodal axoplasm has finite resistivity and does not become a superconductor ($R = 0$).<br>&bull; C is incorrect because voltage-gated sodium channels are essential at the Nodes of Ranvier to regenerate the impulse.<br>&bull; D is nonsensical pseudoscience."
      },
      {
        "d": true,
        "q": "A long, straight clinical electrosurgical ground wire carries a direct current of 5.0 A. What is the magnitude of the magnetic field generated at a perpendicular distance of 10.0 cm from the wire? (mu_0 = 4*pi x 10^-7 T*m/A)",
        "ch": [
          "5.0 x 10^-5 T",
          "1.0 x 10^-5 T",
          "2.5 x 10^-6 T",
          "3.1 x 10^-4 T"
        ],
        "a": 1,
        "e": "<strong>Magnetic field of a long straight current-carrying wire (Topic 293):</strong> The magnetic field $B$ produced by a long straight wire is given by Ampere's law: $B = \\frac{\\mu_0 I}{2\\pi r}$. Converting distance $r = 10.0\\text{ cm} = 0.10\\text{ m}$: $B = \\frac{(4\\pi \\times 10^{-7}\\text{ T}\\cdot\\text{m/A})(5.0\\text{ A})}{2\\pi (0.10\\text{ m})} = \\frac{2 \\times 10^{-6}}{0.10} = 1.0 \\times 10^{-5}\\text{ T} = 10\\ \\mu\\text{T}$.<br><br><em>Distractor Traps:</em><br>&bull; A forgets the factor of $2\\pi$ in the denominator, computing $\\mu_0 I / r$.<br>&bull; C divides by $4\\pi$ instead of $2\\pi$, halving the field.<br>&bull; D forgets to convert centimeters to meters, resulting in a field two orders of magnitude too large."
      },
      {
        "d": true,
        "q": "A singly charged therapeutic proton (q = +1.6 x 10^-19 C, m = 1.67 x 10^-27 kg) enters a uniform magnetic field of B = 1.5 T in a medical cyclotron with a velocity of 3.0 x 10^7 m/s perpendicular to the field. What is the radius of the resulting circular trajectory?",
        "ch": [
          "0.42 m",
          "1.04 m",
          "0.21 m",
          "0.84 m"
        ],
        "a": 2,
        "e": "<strong>Cyclotron orbital radius from magnetic Lorentz force (Topic 294):</strong> The magnetic Lorentz force provides the necessary centripetal force: $F_B = q v B = \\frac{m v^2}{r}$. Solving for orbital radius $r$: $r = \\frac{m v}{q B}$. Substituting the parameters: $r = \\frac{(1.67 \\times 10^{-27}\\text{ kg})(3.0 \\times 10^7\\text{ m/s})}{(1.60 \\times 10^{-19}\\text{ C})(1.5\\text{ T})} = \\frac{5.01 \\times 10^{-20}}{2.40 \\times 10^{-19}} \\approx 0.20875\\text{ m} \\approx 0.21\\text{ m}$.<br><br><em>Distractor Traps:</em><br>&bull; A multiplies the correct answer by 2 ($0.42\\text{ m}$), confusing radius with diameter.<br>&bull; B calculates $m v^2 / (q B)$, multiplying by velocity twice.<br>&bull; D divides by $0.5 q B$ instead of $q B$."
      }
    ]
  }
];

if (typeof window !== 'undefined') {
  window.EXAM_CP60_6 = EXAM_CP60_6;
}
if (typeof globalThis !== 'undefined') {
  globalThis.EXAM_CP60_6 = EXAM_CP60_6;
}
