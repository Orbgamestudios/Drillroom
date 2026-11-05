# /home/cgslinde/DrillRoom/DrillRoom/scratch/cp5/p7.py
"""
Passage 7: Topic 274 — Dynamic Compliance vs Static Compliance in Mechanical Ventilation
"""

passage_data = {
    "id": "exam_cp90_5_p7",
    "sec": "C/P",
    "topic": "Dynamic Compliance vs Static Compliance in Mechanical Ventilation",
    "sheet": 7,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_5",
    "passage": "<div class=\"ttl\">Passage 7 (Questions 37&ndash;42)</div>\n"
               "<p>In the intensive care unit, mechanical ventilation provides life-sustaining ventilatory support for patients with acute respiratory failure. Safe management requires rigorous monitoring of respiratory mechanics to avoid ventilator-induced lung injury (barotrauma and volutrauma).</p>\n"
               "<p>The physical motion of the respiratory system during positive-pressure volume-controlled ventilation is governed by the equation of motion:</p>\n"
               "<p>$$P_{\\text{aw}}(t) = P_{\\text{resistive}}(t) + P_{\\text{elastic}}(t) + \\text{PEEP} = R_{\\text{aw}} \\cdot \\dot{V}(t) + \\frac{V_T(t)}{C_{\\text{stat}}} + \\text{PEEP}$$</p>\n"
               "<p>where $P_{\\text{aw}}$ is airway pressure, $\\dot{V}$ is inspiratory flow rate, $R_{\\text{aw}}$ is airway resistance, $V_T$ is tidal volume, $C_{\\text{stat}}$ is static respiratory system compliance, and PEEP is positive end-expiratory pressure.</p>\n"
               "<p>Two key pressure measurements are obtained during constant-flow volume-controlled ventilation:</p>\n"
               "<p>1. <em>Peak Inspiratory Pressure (PIP)</em>: The maximum pressure measured at the conclusion of active inspiration, reflecting the sum of resistive pressure and elastic recoil of the lungs and chest wall:</p>\n"
               "<p>$$PIP = R_{\\text{aw}} \\cdot \\dot{V} + \\frac{V_T}{C_{\\text{stat}}} + \\text{PEEP}$$</p>\n"
               "<p>2. <em>Plateau Pressure ($P_{\\text{plat}}$)</em>: The pressure measured during an end-inspiratory pause. When gas flow is momentarily arrested ($\\dot{V} = 0$), resistive pressure dissipation drops to zero ($R_{\\text{aw}} \\cdot 0 = 0$), equilibrating airway pressure with alveolar elastic recoil:</p>\n"
               "<p>$$P_{\\text{plat}} = \\frac{V_T}{C_{\\text{stat}}} + \\text{PEEP}$$</p>\n"
               "<p>From these measurements, static compliance is derived as $C_{\\text{stat}} = \\frac{V_T}{P_{\\text{plat}} - \\text{PEEP}}$, and airway resistance is derived as $R_{\\text{aw}} = \\frac{PIP - P_{\\text{plat}}}{\\dot{V}}$. Critical care specialists recorded respiratory mechanics in adult patients ventilated at $V_T = 500\\text{ mL} = 0.50\\text{ L}$, constant inspiratory flow $\\dot{V} = 1.0\\text{ L/s}$, and $\\text{PEEP} = 5.0\\text{ cm H}_2\\text{O}$ across five clinical states (Table 1).</p>\n"
               "<table class=\"tbl\">\n"
               "  <caption>Table 1 Airway pressures, compliance, and calculated airway resistance across clinical states</caption>\n"
               "  <thead>\n"
               "    <tr><th>Clinical Condition</th><th>PIP ($\\text{cm H}_2\\text{O}$)</th><th>$P_{\\text{plat}}$ ($\\text{cm H}_2\\text{O}$)</th><th>PEEP ($\\text{cm H}_2\\text{O}$)</th><th>$PIP - P_{\\text{plat}}$ ($\\text{cm H}_2\\text{O}$)</th><th>$C_{\\text{stat}}$ ($\\text{mL/cm H}_2\\text{O}$)</th><th>$R_{\\text{aw}}$ ($\\text{cm H}_2\\text{O}/(\\text{L/s})$)</th></tr>\n"
               "  </thead>\n"
               "  <tbody>\n"
               "    <tr><td>Baseline Healthy Lung</td><td>20.0</td><td>13.0</td><td>5.0</td><td>7.0</td><td>62.5</td><td>7.0</td></tr>\n"
               "    <tr><td>Acute Status Asthmaticus</td><td>45.0</td><td>15.0</td><td>5.0</td><td>30.0</td><td>50.0</td><td>30.0</td></tr>\n"
               "    <tr><td>Post-Albuterol Asthma</td><td>26.0</td><td>14.0</td><td>5.0</td><td>12.0</td><td>55.6</td><td>12.0</td></tr>\n"
               "    <tr><td>Severe ARDS</td><td>48.0</td><td>41.0</td><td>5.0</td><td>7.0</td><td>13.9</td><td>7.0</td></tr>\n"
               "    <tr><td>Tension Pneumothorax</td><td>52.0</td><td>44.0</td><td>5.0</td><td>8.0</td><td>12.8</td><td>8.0</td></tr>\n"
               "  </tbody>\n"
               "</table>\n"
               "<p>Clinicians evaluate whether titrating PEEP recruits collapsed alveoli without causing overdistension in ARDS lungs.</p>",
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
}
