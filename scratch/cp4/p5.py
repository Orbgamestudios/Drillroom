# /home/cgslinde/DrillRoom/DrillRoom/scratch/cp4/p5.py
"""
Passage 5: Topic 255 — Blood Viscosity & Hematocrit Rheology (Fåhræus-Lindqvist Effect)
"""

passage_data = {
    "id": "exam_cp90_4_p5",
    "sec": "C/P",
    "topic": "Blood Viscosity & Hematocrit Rheology: The Fåhræus-Lindqvist Effect",
    "sheet": 5,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_4",
    "passage": "<div class=\"ttl\">Passage 5 (Questions 25&ndash;30)</div>\n"
               "<p>Whole blood is a complex non-Newtonian, shear-thinning (pseudoplastic) suspension composed of cellular elements&mdash;primarily biconcave erythrocytes (red blood cells, RBCs)&mdash;suspended in liquid plasma. In large conduit arteries (diameter $d > 1.0\\text{ mm}$), blood behaves approximately as a homogeneous fluid with a constant bulk dynamic viscosity of $\\eta_{bulk} \\approx 3.5\\text{ to }4.0\\text{ mPa}\\cdot\\text{s}$ at physiological hematocrit ($Hct \\approx 45\\%$). However, when blood flows through microvessels of diameters between $300\\ \\mu\\text{m}$ and $10\\ \\mu\\text{m}$, its apparent dynamic viscosity ($\\eta_{app}$) decreases progressively as vessel caliber narrows&mdash;a phenomenon known as the F&aring;hr&aelig;us-Lindqvist effect.</p>\n"
               "<p>The F&aring;hr&aelig;us-Lindqvist effect arises from the transverse hydrodynamic migration of flexible erythrocytes toward the high-velocity centerline of the vessel lumen (axial migration). This leaves a cell-depleted, low-viscosity plasma layer along the vessel periphery where shear rates ($\\dot{\\gamma} = dv/dr$) are highest. Because this peripheral cell-free marginal layer acts as a low-friction hydraulic lubricant, the overall resistance to flow diminishes, causing calculated apparent viscosity to drop. Furthermore, because erythrocytes travel faster in the central core than the slower peripheral plasma, the average hematocrit inside the microvessel (tube hematocrit, $H_t$) is lower than the discharge hematocrit ($H_d$) entering and exiting the vessel (the F&aring;hr&aelig;us effect).</p>\n"
               "<p>To profile microvascular rheology, biomedical researchers perfused human blood samples of varying hematocrits through calibrated glass microcapillary tubes ranging in inner diameter from $500\\ \\mu\\text{m}$ down to $5\\ \\mu\\text{m}$ at a standardized shear rate of $\\dot{\\gamma} = 500\\text{ s}^{-1}$ and $T = 37^\\circ\\text{C}$. The relative apparent viscosity ($\\eta_{rel} = \\eta_{app} / \\eta_{plasma}$, where $\\eta_{plasma} = 1.20\\text{ mPa}\\cdot\\text{s}$) and tube hematocrit ($H_t$, for an initial discharge hematocrit of $H_d = 45.0\\%$) were quantified. Table 1 summarizes the experimental measurements.</p>\n"
               "<table class=\"tbl\">\n"
               "  <caption>Table 1 Apparent blood viscosity and tube hematocrit across microcapillary diameters</caption>\n"
               "  <thead>\n"
               "    <tr><th>Capillary Diameter $d$ (&mu;m)</th><th>Discharge Hematocrit $H_d$ (%)</th><th>Tube Hematocrit $H_t$ (%)</th><th>Relative Tube $Hct$ ($H_t/H_d$)</th><th>Apparent Viscosity $\\eta_{app}$ (mPa&middot;s)</th><th>Relative Viscosity $\\eta_{rel}$</th></tr>\n"
               "  </thead>\n"
               "  <tbody>\n"
               "    <tr><td>500.0</td><td>45.0</td><td>45.0</td><td>1.00</td><td>3.84</td><td>3.20</td></tr>\n"
               "    <tr><td>200.0</td><td>45.0</td><td>41.4</td><td>0.92</td><td>3.48</td><td>2.90</td></tr>\n"
               "    <tr><td>100.0</td><td>45.0</td><td>36.9</td><td>0.82</td><td>2.88</td><td>2.40</td></tr>\n"
               "    <tr><td>30.0</td><td>45.0</td><td>30.6</td><td>0.68</td><td>2.16</td><td>1.80</td></tr>\n"
               "    <tr><td>10.0</td><td>45.0</td><td>27.0</td><td>0.60</td><td>1.80</td><td>1.50</td></tr>\n"
               "    <tr><td>5.0</td><td>45.0</td><td>31.5</td><td>0.70</td><td>3.12</td><td>2.60</td></tr>\n"
               "  </tbody>\n"
               "</table>\n"
               "<p>Researchers noted that this microvascular rheological adaptation significantly decreases cardiac workload by attenuating resistance in precapillary arteriole networks.</p>",
    "qs": [
        {
            "q": "What primary physical mechanism is responsible for the decrease in apparent blood viscosity observed as vessel diameter decreases from $500\\ \\mu\\text{m}$ to $10\\ \\mu\\text{m}$ (the Fåhræus-Lindqvist effect)?",
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
            "q": "According to the Fåhræus effect illustrated in Table 1, why is the tube hematocrit ($H_t = 27.0\\%$) within a $10\\ \\mu\\text{m}$ capillary substantially lower than the systemic discharge hematocrit ($H_d = 45.0\\%$)?",
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
            "e": "<strong>Non-Newtonian shear-thinning and rouleaux aggregation:</strong> At normal or high shear rates ($\\dot{\\gamma} > 100\\text{ s}^{-1}$), hydrodynamic shear forces deform and align flexible erythrocytes parallel to streamlines, minimizing viscous resistance. At very low shear rates ($\\dot{\\gamma} < 10\\text{ s}^{-1}$, e.g., low-flow states, shock, or venous stasis), shear forces are insufficient to overcome macromolecular attraction. Asymmetrical plasma proteins—predominantly fibrinogen and immunoglobulins—adsorb onto adjacent erythrocyte surfaces, bridging them together into linear stacked-coin aggregates known as rouleaux. These large macromolecular structures dramatically resist deformation, raising blood viscosity by up to an order of magnitude.<br><br><em>Distractor Traps:</em><br>&bull; A nonsensically proposes water evaporation inside closed systemic blood vessels.<br>&bull; B posits irreversible covalent cross-linking, but rouleaux formation is completely reversible upon restoring physiological shear.<br>&bull; C describes leukocyte phagocytosis of water, which is biologically meaningless."
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
}
