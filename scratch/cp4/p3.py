# /home/cgslinde/DrillRoom/DrillRoom/scratch/cp4/p3.py
"""
Passage 3: Topic 253 — Laminar vs Turbulent Flow & Reynolds Number (Re)
"""

passage_data = {
    "id": "exam_cp90_4_p3",
    "sec": "C/P",
    "topic": "Laminar vs Turbulent Flow & Reynolds Number (Re) in Carotid Stenosis and Murmurs",
    "sheet": 3,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_4",
    "passage": "<div class=\"ttl\">Passage 3 (Questions 13&ndash;18)</div>\n"
               "<p>In healthy systemic blood vessels, blood flow is predominantly laminar, characterized by fluid traveling smoothly in concentric cylindrical laminae parallel to the vessel axis. The velocity profile is parabolic, with maximum velocity at the centerline and zero velocity at the vessel wall due to the no-slip condition. When fluid velocity increases or vessel geometry becomes disturbed, flow can transition into a turbulent regime characterized by chaotic fluid fluctuations, recirculating vortices, elevated wall shear stress, and acoustic murmurs or bruits detectable via stethoscope.</p>\n"
               "<p>The transition between laminar and turbulent flow in a cylindrical pipe is governed by the dimensionless Reynolds number ($Re$):\n"
               "$$Re = \\frac{\\rho v d}{\\eta}$$\n"
               "where $\\rho$ is blood density ($1060\\text{ kg/m}^3$), $v$ is mean cross-sectional flow velocity, $d$ is vessel inner diameter, and $\\eta$ is dynamic viscosity. Under steady flow conditions in smooth rigid conduits, flow is strictly laminar when $Re < 2000$. Between $2000 \\le Re \\le 3000$, flow is transitional and sensitive to local wall irregularities. Fully turbulent flow is typically established when $Re > 3000$, although pulsatile flow and arterial branching can trigger turbulence at lower thresholds ($Re \\approx 2000$).</p>\n"
               "<p>To investigate how hematocrit and focal carotid stenoses interact to provoke audible bruits, investigators constructed an in vitro pulsatile mock circulatory loop. Silicone vascular phantoms representing internal carotid arteries (nominal diameter $d_0 = 6.0\\text{ mm}$) were fabricated with varying degrees of concentric luminal diameter reduction (0%, 50%, and 70% stenosis). The loop was perfused at a fixed volumetric flow rate of $Q = 6.0\\text{ mL/s}$ ($6.0 \\times 10^{-6}\\text{ m}^3/\\text{s}$) using test fluids mimicking normal blood ($\\eta = 3.50 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}$) and severe anemia ($\\eta = 1.75 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}$). An acoustic hydrophone recorded sound intensity. Results are presented in Table 1.</p>\n"
               "<table class=\"tbl\">\n"
               "  <caption>Table 1 Hemodynamic parameters and acoustic bruit generation across carotid stenosis models</caption>\n"
               "  <thead>\n"
               "    <tr><th>Stenosis Severity</th><th>Fluid Condition</th><th>Dynamic Viscosity $\\eta$ ($10^{-3}$ Pa&middot;s)</th><th>Stenotic Diameter $d$ (mm)</th><th>Mean Velocity $v$ (m/s)</th><th>Reynolds Number ($Re$)</th><th>Acoustic Bruit Detected?</th></tr>\n"
               "  </thead>\n"
               "  <tbody>\n"
               "    <tr><td>0% (Control)</td><td>Normal Blood</td><td>3.50</td><td>6.0</td><td>0.212</td><td>385</td><td>No (Silent)</td></tr>\n"
               "    <tr><td>0% (Control)</td><td>Anemic Blood</td><td>1.75</td><td>6.0</td><td>0.212</td><td>770</td><td>No (Silent)</td></tr>\n"
               "    <tr><td>50% Stenosis</td><td>Normal Blood</td><td>3.50</td><td>3.0</td><td>0.849</td><td>770</td><td>No (Silent)</td></tr>\n"
               "    <tr><td>50% Stenosis</td><td>Anemic Blood</td><td>1.75</td><td>3.0</td><td>0.849</td><td>1540</td><td>Borderline Murmur</td></tr>\n"
               "    <tr><td>70% Stenosis</td><td>Normal Blood</td><td>3.50</td><td>1.8</td><td>2.358</td><td>1284</td><td>Weak Bruit</td></tr>\n"
               "    <tr><td>70% Stenosis</td><td>Anemic Blood</td><td>1.75</td><td>1.8</td><td>2.358</td><td>2568</td><td>High-Intensity Bruit</td></tr>\n"
               "  </tbody>\n"
               "</table>\n"
               "<p>Clinicians observe that when patients with severe aortic stenosis or carotid narrowing also suffer from untreated iron-deficiency anemia, the pitch and loudness of the associated murmur escalate markedly.</p>",
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
}
