# Generator for C/P Exam 6
import json, re

# We will construct EXAM_CP90_6 with 7 passages and 1 discrete set (10 Qs)
passages = []

# Passage 1: Topic 285 - Dielectric Breakdown & Electroporation in Cell Biology
p1 = {
    "id": "exam_cp90_6_p1",
    "sec": "C/P",
    "topic": "Dielectric Breakdown & Electroporation in Cell Biology",
    "sheet": 1,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_6",
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
            "e": "<strong>Field angle dependence in the Schwan equation:</strong> The Schwan equation defines the induced potential as $\\Delta V_m = 1.5 R E_{ext} \\cos(\\theta)$. The cosine function achieves its maximum absolute magnitude ($|\\cos(\\theta)| = 1$) when $\\theta = 0^\\circ$ or $\\theta = 180^\\circ$ ($\\\pi$ radians), which corresponds to the cell poles directly facing the anode and cathode along the field vector. Consequently, the induced potential reaches its highest amplitude at these poles, exceeding the breakdown threshold $V_{crit}$ before any other region of the cell membrane.<br><br><em>Distractor Traps:</em><br>&bull; B is incorrect because at the equator ($\\\theta = 90^\\circ$), $\\\cos(90^\\circ) = 0$, meaning no external transmembrane potential is induced.<br>&bull; C is incorrect because the induced potential is strongly anisotropic and varies continuously with $\\\cos(\\\theta)$.<br>&bull; D is incorrect because macroscale geometric orientation relative to the applied field vector dictates where threshold potential is breached, rather than stochastic cholesterol fluctuations."
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
            "e": "<strong>Capacitance and charge calculation for a spherical cell:</strong> The surface area of a sphere is $A = 4\\pi R^2$. For $R = 10.0\\ \\mu\\text{m} = 1.0 \\times 10^{-3}\\text{ cm}$, $A = 4\\pi (1.0 \\times 10^{-3}\\text{ cm})^2 = 4\\pi \\times 10^{-6}\\text{ cm}^2 \\approx 1.257 \\times 10^{-5}\\text{ cm}^2$. The total cell capacitance is $C = C_{area} \\times A = (0.55\\ \\mu\\text{F/cm}^2)(1.257 \\times 10^{-5}\\text{ cm}^2) \\approx 6.91 \\times 10^{-6}\\ \\mu\\text{F} = 6.91 \\times 10^{-12}\\text{ F}$. The stored charge magnitude is $Q = C \\times |V_{rest}| = (6.91 \\times 10^{-12}\\text{ F})(0.070\\text{ V}) \\approx 4.84 \\times 10^{-13}\\text{ C}$.<br><br><em>Distractor Traps:</em><br>&bull; A forgets the factor of $4$ in the spherical surface area formula, using $\\\pi R^2$.<br>&bull; B fails to convert microfarads to farads, resulting in an answer two orders of magnitude too large.<br>&bull; D divides by the potential instead of multiplying by $V$ ($Q = C/V$)."
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
}
passages.append(p1)

print('Passage 1 generated.')
"