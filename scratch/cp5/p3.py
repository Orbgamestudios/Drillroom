# /home/cgslinde/DrillRoom/DrillRoom/scratch/cp5/p3.py
"""
Passage 3: Topic 270 — Flow Past Bluff Bodies & Drag Coefficient in Blood Filters
"""

passage_data = {
    "id": "exam_cp90_5_p3",
    "sec": "C/P",
    "topic": "Flow Past Bluff Bodies & Drag Coefficient in Blood Filters",
    "sheet": 3,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_5",
    "passage": "<div class=\"ttl\">Passage 3 (Questions 13&ndash;18)</div>\n"
               "<p>Inferior vena cava (IVC) filters are deployed endovascularly to intercept and trap lower-extremity deep vein thromboemboli, preventing potentially fatal pulmonary embolism in patients with contraindications to anticoagulation. When deployed inside the IVC lumen, the metallic filter frame (composed of nitinol struts in conical or umbrella configurations) functions hydrodynamically as an immersed bluff body obstructing venous blood flow.</p>\n"
               "<p>The total hydrodynamic drag force ($F_D$) exerted by blood flow upon an immersed filter is described by the drag equation:</p>\n"
               "<p>$$F_D = \\frac{1}{2} C_D \\rho A v^2$$</p>\n"
               "<p>where $C_D$ represents the dimensionless drag coefficient, $\\rho$ is the mass density of whole blood ($\\rho \\approx 1060\\text{ kg/m}^3$), $A$ is the projected frontal area perpendicular to blood flow, and $v$ is the mean upstream blood velocity (normally 0.10&ndash;0.25 m/s in the human infrarenal IVC).</p>\n"
               "<p>Total hydrodynamic drag comprises two primary components:</p>\n"
               "<p>1. <em>Form (pressure) drag</em>: Arising from an upstream-to-downstream pressure differential caused by flow separation and boundary layer detachment, creating a wide, turbulent, low-pressure wake downstream of the body.</p>\n"
               "<p>2. <em>Skin friction drag</em>: Tangential viscous shear stresses exerted along the wetted surface of the struts, governed by dynamic blood viscosity ($\\mu \\approx 3.50\\text{ mPa}\\cdot\\text{s}$).</p>\n"
               "<p>The flow regime is characterized by the dimensionless Reynolds number:</p>\n"
               "<p>$$Re = \\frac{\\rho v D}{\\mu}$$</p>\n"
               "<p>where $D$ represents the characteristic dimension (the caval lumen diameter). When an IVC filter captures a large thromboembolus, the trapped clot markedly increases the effective frontal area and alters flow geometry from slender struts into an acute bluff body, escalating mechanical drag on anchoring barbs. Biomedical engineers evaluated three IVC filter prototypes in an IVC phantom ($D = 20\\text{ mm}$, $\\rho = 1060\\text{ kg/m}^3$, $\\mu = 3.50\\text{ mPa}\\cdot\\text{s}$) at an inflow velocity of $v = 0.20\\text{ m/s}$ (Table 1).</p>\n"
               "<table class=\"tbl\">\n"
               "  <caption>Table 1 Projected area, drag coefficients, measured drag force, and peak shear stresses</caption>\n"
               "  <thead>\n"
               "    <tr><th>Filter Design</th><th>Thrombus Status</th><th>Projected Area $A$ ($\\text{mm}^2$)</th><th>Drag Coeff $C_D$</th><th>Measured Drag Force $F_D$ (mN)</th><th>Peak Wall Shear Stress (Pa)</th></tr>\n"
               "  </thead>\n"
               "  <tbody>\n"
               "    <tr><td rowspan=\"2\">Conical (Filter A)</td><td>Clean (Unloaded)</td><td>8.0</td><td>0.95</td><td>0.16</td><td>1.8</td></tr>\n"
               "    <tr><td>Trapped Clot (50% Clot)</td><td>80.0</td><td>1.45</td><td>2.46</td><td>5.2</td></tr>\n"
               "    <tr><td rowspan=\"2\">Umbrella (Filter B)</td><td>Clean (Unloaded)</td><td>12.0</td><td>1.10</td><td>0.28</td><td>2.4</td></tr>\n"
               "    <tr><td>Trapped Clot (50% Clot)</td><td>95.0</td><td>1.60</td><td>3.22</td><td>6.8</td></tr>\n"
               "    <tr><td rowspan=\"2\">TrapEase (Filter C)</td><td>Clean (Unloaded)</td><td>10.0</td><td>0.85</td><td>0.18</td><td>1.6</td></tr>\n"
               "    <tr><td>Trapped Clot (50% Clot)</td><td>85.0</td><td>1.30</td><td>2.34</td><td>4.9</td></tr>\n"
               "  </tbody>\n"
               "</table>\n"
               "<p>Engineers evaluate whether elevated drag forces following clot capture risk cephalad migration or vena cava perforation.</p>",
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
}
