# /home/cgslinde/DrillRoom/DrillRoom/scratch/cp4/p6.py
"""
Passage 6: Topic 256 — Transmural Vascular Pressure & Laplace's Law for Aortic Aneurysms
"""

passage_data = {
    "id": "exam_cp90_4_p6",
    "sec": "C/P",
    "topic": "Transmural Vascular Pressure & Laplace's Law in Abdominal Aortic Aneurysms",
    "sheet": 6,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_4",
    "passage": "<div class=\"ttl\">Passage 6 (Questions 31&ndash;36)</div>\n"
               "<p>An abdominal aortic aneurysm (AAA) is a focal dilation of the infrarenal abdominal aorta characterized by chronic destruction of elastin and collagen within the tunica media and adventitia. Left untreated, AAAs tend to expand progressively, culminating in catastrophic retroperitoneal rupture with mortality exceeding 80%. In cardiovascular mechanics, the equilibrium of forces in an elastic cylindrical blood vessel is modeled by the Law of Laplace for thin-walled cylinders:\n"
               "$$T = P_{tm} \\cdot r$$\n"
               "where $T$ is circumferential wall tension (force per unit axial length, $\\text{N/m}$), $P_{tm}$ is transmural pressure ($P_{in} - P_{out}$, where $P_{out} \\approx 0\\text{ mmHg}$ relative to atmospheric intra-abdominal pressure), and $r$ is internal lumen radius.</p>\n"
               "<p>Because clinical rupture is ultimately governed by whether internal material stress exceeds the ultimate tensile strength of the degraded arterial wall, bioengineers analyze circumferential wall stress ($\\sigma$, force per unit cross-sectional wall area, $\\text{N/m}^2$ or $\\text{Pa}$):\n"
               "$$\\sigma = \\frac{T}{w} = \\frac{P_{tm} \\cdot r}{w}$$\n"
               "where $w$ represents arterial wall thickness. As an aneurysm balloons outward, radius $r$ expands while conservation of wall volume or tissue degradation causes wall thickness $w$ to diminish. This double compounding&mdash;increasing numerator and decreasing denominator&mdash;drives wall stress upward at an accelerating rate, creating a mechanical instability that escalates rupture risk.</p>\n"
               "<p>To establish biomechanical rupture risk thresholds, vascular surgeons and engineers performed ex vivo inflation testing on resected healthy abdominal aorta segments and aneurysmal specimens of varying calibers. Specimens were mounted in an organ bath and subjected to physiological systolic blood pressure ($P_{tm} = 120.0\\text{ mmHg} = 1.60 \\times 10^4\\text{ Pa}$). High-resolution optical micrometers quantified inner radius ($r$), wall thickness ($w$), circumferential wall tension ($T$), and circumferential wall stress ($\\sigma$). Table 1 details the experimental biomechanical data.</p>\n"
               "<table class=\"tbl\">\n"
               "  <caption>Table 1 Geometric dimensions, wall tension, and wall stress across aortic aneurysm dilation stages</caption>\n"
               "  <thead>\n"
               "    <tr><th>Aortic Specimen</th><th>Lumen Radius $r$ (cm)</th><th>Wall Thickness $w$ (mm)</th><th>Transmural Pressure $P_{tm}$ (kPa)</th><th>Circumferential Tension $T$ (N/m)</th><th>Circumferential Wall Stress $\\sigma$ (kPa)</th><th>Rupture Risk Assessment</th></tr>\n"
               "  </thead>\n"
               "  <tbody>\n"
               "    <tr><td>Normal Aorta</td><td>1.00</td><td>2.00</td><td>16.0</td><td>160.0</td><td>80.0</td><td>Negligible (&lt;1%/yr)</td></tr>\n"
               "    <tr><td>Ectatic Aorta</td><td>1.50</td><td>1.80</td><td>16.0</td><td>240.0</td><td>133.3</td><td>Minimal (&lt;1%/yr)</td></tr>\n"
               "    <tr><td>Small AAA</td><td>2.00</td><td>1.50</td><td>16.0</td><td>320.0</td><td>213.3</td><td>Low (~1&ndash;2%/yr)</td></tr>\n"
               "    <tr><td>Moderate AAA</td><td>2.50</td><td>1.20</td><td>16.0</td><td>400.0</td><td>333.3</td><td>Moderate (~5%/yr)</td></tr>\n"
               "    <tr><td>Large AAA</td><td>3.00</td><td>1.00</td><td>16.0</td><td>480.0</td><td>480.0</td><td>High (~10&ndash;20%/yr)</td></tr>\n"
               "    <tr><td>Critical AAA</td><td>3.50</td><td>0.80</td><td>16.0</td><td>560.0</td><td>700.0</td><td>Severe (&gt;30%/yr; surgical repair)</td></tr>\n"
               "  </tbody>\n"
               "</table>\n"
               "<p>Clinical guidelines recommend elective surgical or endovascular repair when aneurysm diameter reaches $5.5\\text{ cm}$ ($r = 2.75\\text{ cm}$) or when expansion exceeds $0.5\\text{ cm/year}$.</p>",
    "qs": [
        {
            "q": "Based on Laplace's law for a cylindrical vessel ($T = P \\cdot r$), what is the circumferential wall tension in a Large AAA with inner radius $r = 3.00\\text{ cm}$ under a transmural blood pressure of $16.0\\text{ kPa}$?",
            "ch": [
                "160 N/m",
                "240 N/m",
                "320 N/m",
                "480 N/m"
            ],
            "a": 3,
            "e": "<strong>Laplace's law for cylindrical wall tension:</strong> For a thin-walled cylinder, circumferential wall tension is the product of transmural pressure and vessel inner radius: $T = P_{tm} \\cdot r$. Converting radius into SI units: $r = 3.00\\text{ cm} = 0.0300\\text{ m}$. Transmural pressure is $P_{tm} = 16.0\\text{ kPa} = 16,000\\text{ Pa} = 16,000\\text{ N/m}^2$. Multiplying these parameters: $T = (16,000\\text{ N/m}^2)(0.0300\\text{ m}) = 480\\text{ N/m}$. Table 1 corroborates this value.<br><br><em>Distractor Traps:</em><br>&bull; A (160 N/m) is the wall tension of a normal aorta of radius $1.00\\text{ cm}$.<br>&bull; B (240 N/m) is the tension of an ectatic vessel of radius $1.50\\text{ cm}$.<br>&bull; C (320 N/m) is the tension of a small AAA of radius $2.00\\text{ cm}$."
        },
        {
            "q": "Why is an aneurysmal aorta significantly more prone to spontaneous mechanical rupture than a normal aorta, even when both vessels experience identical systemic blood pressure ($120\\text{ mmHg}$)?",
            "ch": [
                "Expanded radius and reduced wall thickness markedly escalate circumferential wall stress",
                "Aneurysmal dilation accelerates centerline blood velocity, dropping dynamic shear stress",
                "Lower wall tension in aneurysms impairs elastic recoil, trapping stagnant acidic thrombi",
                "Aneurysmal vessels trigger cavitation shockwaves that pit and perforate arterial elastin"
            ],
            "a": 0,
            "e": "<strong>Laplace wall stress and aneurysm instability:</strong> Mechanical rupture occurs when the circumferential tensile wall stress exceeds the ultimate tensile strength of the vessel wall tissue. According to Laplace's law for wall stress ($\\sigma = \\frac{P_{tm} \\cdot r}{w}$), wall stress is directly proportional to radius ($r$) and inversely proportional to wall thickness ($w$). In an aneurysm, the inner radius expands while the wall stretches and thins. As shown in Table 1, dilating from $1.00\\text{ cm}$ to $3.50\\text{ cm}$ while thinning from $2.00\\text{ mm}$ to $0.80\\text{ mm}$ increases wall stress from $80.0\\text{ kPa}$ to $700.0\\text{ kPa}$ (an 8.75-fold increase), overwhelming degraded collagen fibers.<br><br><em>Distractor Traps:</em><br>&bull; B contradicts continuity; expanding the cross-sectional area decreases blood velocity ($v = Q/A$) rather than accelerating it.<br>&bull; C incorrectly claims wall tension is lower; Laplace's law proves tension is substantially higher ($T \\propto r$).<br>&bull; D invents cavitation shockwaves, which occur in prosthetic mechanical heart valves, not native aortic aneurysms."
        },
        {
            "q": "In contrast to cylindrical fusiform aneurysms ($\\sigma_{cyl} = P\\cdot r / w$), focal saccular cerebral aneurysms are often modeled as thin-walled spheres. For a spherical aneurysm of radius $r$ and wall thickness $w$, the Laplace wall stress is given by:",
            "ch": [
                "$\\sigma = \\frac{2P \\cdot r}{w}$",
                "$\\sigma = \\frac{P \\cdot r}{2w}$",
                "$\\sigma = \\frac{4P \\cdot r}{w}$",
                "$\\sigma = \\frac{P \\cdot r}{4w}$"
            ],
            "a": 1,
            "e": "<strong>Spherical Laplace law derivation:</strong> Consider a hemisphere of radius $r$. The total outward pressure force acting on the circular cross-section is $F_p = P \\cdot A = P (\\pi r^2)$. This outward force is balanced by the internal material stress ($\\sigma$) acting across the circumferential wall cross-section: $A_{wall} \\approx 2\\pi r w$. In static equilibrium: $\\Sigma F = 0 \\implies P (\\pi r^2) = \\sigma (2\\pi r w)$. Dividing both sides by $2\\pi r w$ yields: $\\sigma_{sph} = \\frac{P \\cdot r}{2w}$. Notice that for identical radius, pressure, and wall thickness, wall stress in a sphere is exactly half that in a cylinder ($\\sigma_{sph} = \\frac{1}{2}\\sigma_{cyl}$) because curvature in two orthogonal directions supports the pressure load.<br><br><em>Distractor Traps:</em><br>&bull; A multiplies by 2 rather than dividing by 2, incorrectly doubling cylindrical stress.<br>&bull; C multiplies by 4, confusing soap bubble surface interfaces with solid thin-walled stress balance.<br>&bull; D introduces an erroneous factor of 4 in the denominator."
        },
        {
            "q": "According to Table 1, as the aorta dilates from a Normal vessel ($r = 1.00\\text{ cm}$) to a Critical AAA ($r = 3.50\\text{ cm}$), wall thickness decreases from $2.00\\text{ mm}$ to $0.80\\text{ mm}$. By what overall factor does circumferential wall stress ($\\sigma$) increase?",
            "ch": [
                "3.50-fold",
                "4.38-fold",
                "8.75-fold",
                "17.5-fold"
            ],
            "a": 2,
            "e": "<strong>Fold-change calculation in Laplace wall stress:</strong> Circumferential wall stress is given by $\\sigma = \\frac{P \\cdot r}{w}$. Because transmural pressure $P$ is constant ($16.0\\text{ kPa}$), the relative change in stress is: $\\frac{\\sigma_{critical}}{\\sigma_{normal}} = \\left(\\frac{r_{critical}}{r_{normal}}\\right) \\left(\\frac{w_{normal}}{w_{critical}}\\right)$. Substituting the values: $\\frac{\\sigma_{critical}}{\\sigma_{normal}} = \\left(\\frac{3.50\\text{ cm}}{1.00\\text{ cm}}\\right) \\left(\\frac{2.00\\text{ mm}}{0.80\\text{ mm}}\\right) = (3.50)(2.50) = 8.75$. Checking Table 1 directly: $\\frac{700.0\\text{ kPa}}{80.0\\text{ kPa}} = 8.75$.<br><br><em>Distractor Traps:</em><br>&bull; A (3.50-fold) accounts only for the increase in radius ($3.50 / 1.00$), ignoring wall thinning.<br>&bull; B (4.38-fold) divides 8.75 by 2 or computes $(3.50 \\times 2.50) / 2$.<br>&bull; D (17.5-fold) doubles the correct factor."
        },
        {
            "q": "Vascular surgeons frequently prescribe $\\beta$-blockers (e.g., atenolol) to patients with small, unruptured abdominal aortic aneurysms. Which hemodynamic mechanism best justifies this pharmacological strategy?",
            "ch": [
                "Stimulating vascular smooth muscle proliferation to thicken the aneurysmal adventitia",
                "Accelerating resting cardiac heart rate to increase mean volumetric laminar flow rate",
                "Increasing blood hematocrit to elevate viscous cushioning along damaged elastin walls",
                "Reducing mean arterial pressure and cardiac contractility ($dP/dt$) to minimize stress"
            ],
            "a": 3,
            "e": "<strong>Hemodynamic rationale for $\\beta$-blockade in aneurysms:</strong> In Laplace's law ($\\sigma = P_{tm} \\cdot r / w$), wall stress is directly proportional to transmural blood pressure. $\\beta_1$-adrenergic antagonists ($\\beta$-blockers) decrease heart rate and ventricular contractility, reducing mean arterial pressure ($P_{tm}$) and lowering the rate of systolic pressure rise ($dP/dt$, pulsatile impulse). By lowering peak systolic pressure and dynamic mechanical fatigue on degraded collagen fibers, $\\beta$-blockers reduce wall stress $\\sigma$, slowing aneurysm expansion and reducing the cumulative hazard of rupture.<br><br><em>Distractor Traps:</em><br>&bull; A is pharmacologically incorrect; $\\beta$-blockers do not stimulate medial smooth muscle proliferation.<br>&bull; B is incorrect because $\\beta$-blockers decrease heart rate (negative chronotropy), rather than accelerating it.<br>&bull; C is incorrect because changing hematocrit does not repair vascular collagen and would increase blood viscosity."
        },
        {
            "q": "Applying Bernoulli's principle to blood flow within an abdominal aortic aneurysm, as the vessel cross-sectional area dilates and blood velocity slows down ($v = Q/A$), what effect does this velocity change exert on the local internal lateral static pressure ($P_{static}$) acting on the aneurysmal wall?",
            "ch": [
                "Static lateral pressure increases slightly because kinetic energy converts to static pressure",
                "Static lateral pressure drops to zero because blood velocity decelerates in the dilation",
                "Static lateral pressure remains unchanged because Bernoulli's law applies only to gases",
                "Static lateral pressure decreases markedly because slow-moving fluid loses all momentum"
            ],
            "a": 0,
            "e": "<strong>Bernoulli effect in aneurysmal dilation:</strong> Bernoulli's equation for steady fluid flow along a horizontal streamline states that total mechanical pressure is conserved: $P_{static} + \\frac{1}{2}\\rho v^2 = \\text{constant}$. By the continuity equation ($Q = A v$), when the vessel lumen dilates, cross-sectional area $A$ increases, causing blood flow velocity $v$ to decrease. As velocity drops, dynamic pressure ($\\frac{1}{2}\\rho v^2$) decreases. To conserve total energy, the lateral static pressure ($P_{static}$) exerted against the vessel wall must increase. This phenomenon further exacerbates transmural distending pressure within the aneurysm.<br><br><em>Distractor Traps:</em><br>&bull; B asserts static pressure drops to zero; in reality, kinetic energy is converted into static pressure, raising lateral wall pressure.<br>&bull; C falsely claims Bernoulli's principle applies only to gases; it applies to all continuous fluid flow.<br>&bull; D confuses dynamic pressure (which decreases) with lateral static pressure (which increases)."
        }
    ]
}
