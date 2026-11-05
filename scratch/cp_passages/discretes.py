# /home/cgslinde/DrillRoom/DrillRoom/scratch/cp_passages/discretes.py
"""
Discretes: Topics 241 to 250 (Questions 43 to 52)
All marked with d: True
"""

discrete_data = {
    "id": "exam_cp90_3_disc",
    "sec": "C/P",
    "topic": "C/P Standalone Discrete Questions",
    "sheet": None,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_3",
    "passage": "",
    "qs": [
        {
            "q": "During locomotion, the human Achilles tendon undergoes tensile elongation, storing elastic potential energy that is recovered during push-off. If a tendon with an effective stiffness of $k = 2.00 \\times 10^5\\text{ N/m}$ stretches elastically by $6.00\\text{ mm}$ ($6.00 \\times 10^{-3}\\text{ m}$), what is the total elastic strain energy stored within the tendon?",
            "ch": [
                "1.80 J",
                "7.20 J",
                "3.60 J",
                "12.0 J"
            ],
            "a": 2,
            "d": True,
            "e": "<strong>Hookean elastic potential energy in biological tissues:</strong> The elastic strain energy stored in a stretched tendon behaving as an ideal Hookean spring is given by $U_e = \\frac{1}{2} k x^2$. Substituting the tendon stiffness $k = 2.00 \\times 10^5\\text{ N/m}$ and displacement $x = 6.00 \\times 10^{-3}\\text{ m}$: $U_e = \\frac{1}{2}(2.00 \\times 10^5\\text{ N/m})(6.00 \\times 10^{-3}\\text{ m})^2 = (1.00 \\times 10^5)(3.60 \\times 10^{-5}\\text{ m}^2) = 3.60\\text{ J}$.<br><br><em>Distractor Traps:</em><br>&bull; A (1.80 J) divides by 4 or halves the correct energy ($0.25 \\times k x^2$).<br>&bull; B (7.20 J) forgets the factor of 1/2, calculating $k x^2 = 7.20\\text{ J}$.<br>&bull; D (12.0 J) forgets to square the displacement: $0.5 \\times (2.00 \\times 10^5) \\times (6.00 \\times 10^{-3}) = 600\\text{ J}$, or miscalculates $2 \\times 6$."
        },
        {
            "q": "A 70.0 kg athlete sprints up a stadium stairwell with a total vertical elevation gain of 6.00 m in an elapsed time of 4.00 s. Assuming acceleration due to gravity is $g = 9.80\\text{ m/s}^2$, what is the athlete's average mechanical power output against gravity?",
            "ch": [
                "257 W",
                "515 W",
                "4116 W",
                "1029 W"
            ],
            "a": 3,
            "d": True,
            "e": "<strong>Mechanical power against gravity:</strong> Power is defined as work done divided by elapsed time: $P = \\frac{W}{\\Delta t}$. The work required to elevate mass $m$ to height $h$ against gravity is equal to the change in gravitational potential energy: $W = mgh$. Calculating work: $W = (70.0\\text{ kg})(9.80\\text{ m/s}^2)(6.00\\text{ m}) = 4116\\text{ J}$. Dividing by time $\\Delta t = 4.00\\text{ s}$: $P = \\frac{4116\\text{ J}}{4.00\\text{ s}} = 1029\\text{ W}$. (Over short sprints, elite athletes can generate explosive power exceeding 1000 W).<br><br><em>Distractor Traps:</em><br>&bull; A (257 W) divides power by 4.<br>&bull; B (515 W) divides power by 2 or uses an incorrect time interval ($8.0\\text{ s}$).<br>&bull; C (4116 W) reports the total mechanical work in Joules ($W$), failing to divide by time."
        },
        {
            "q": "During a collision in ice hockey, a puck of mass 0.160 kg traveling horizontally at $35.0\\text{ m/s}$ strikes a goalkeeper's padded glove and is brought completely to rest in an impact duration of $\\Delta t = 0.0200\\text{ s}$. What is the magnitude of the average impact force exerted on the glove?",
            "ch": [
                "70.0 N",
                "140 N",
                "280 N",
                "560 N"
            ],
            "a": 2,
            "d": True,
            "e": "<strong>Impulse-momentum theorem derivation:</strong> The impulse-momentum theorem states that impulse equals change in linear momentum: $J = \\Delta p = m(v_f - v_i) = F_{avg} \\Delta t$. Here, the puck is brought to rest ($v_f = 0$), so the magnitude of momentum change is $|\\Delta p| = m |v_i| = (0.160\\text{ kg})(35.0\\text{ m/s}) = 5.60\\text{ N}\\cdot\\text{s}$. Solving for the average impact force: $F_{avg} = \\frac{|\\Delta p|}{\\Delta t} = \\frac{5.60\\text{ N}\\cdot\\text{s}}{0.0200\\text{ s}} = 280\\text{ N}$.<br><br><em>Distractor Traps:</em><br>&bull; A (70.0 N) divides by 4 or misplaces a factor of 4.<br>&bull; B (140 N) doubles the impact time or halves the force.<br>&bull; D (560 N) doubles the force or assumes an elastic rebound where $\\Delta v = 70.0\\text{ m/s}$."
        },
        {
            "q": "In an automated cell sorter, an erythrocyte of mass $m_1 = 2.00\\,\\mu\\text{g}$ moving at $v_1 = 6.00\\text{ mm/s}$ collides head-on and coalesces completely with an identical stationary cell of mass $m_2 = 2.00\\,\\mu\\text{g}$. What percentage of initial kinetic energy is lost as thermal dissipation during this collision?",
            "ch": [
                "0.0% loss",
                "25.0% loss",
                "75.0% loss",
                "50.0% loss"
            ],
            "a": 3,
            "d": True,
            "e": "<strong>Kinetic energy loss in perfectly inelastic collisions:</strong> When two bodies coalesce and stick together, the collision is perfectly inelastic. Momentum is strictly conserved: $m_1 v_1 + m_2 v_2 = (m_1 + m_2)v_f$. Substituting $v_2 = 0$: $(2.00)(6.00) + 0 = (2.00 + 2.00)v_f \\implies 12.0 = 4.00 v_f \\implies v_f = 3.00\\text{ mm/s}$. The initial kinetic energy is $KE_i = \\frac{1}{2}m_1 v_1^2 = \\frac{1}{2}(2.00)(6.00)^2 = 36.0\\text{ pJ}$. The final kinetic energy is $KE_f = \\frac{1}{2}(m_1 + m_2)v_f^2 = \\frac{1}{2}(4.00)(3.00)^2 = 18.0\\text{ pJ}$. The kinetic energy lost is $\\Delta KE = 36.0 - 18.0 = 18.0\\text{ pJ}$, which represents $\\frac{18.0}{36.0} = 50.0\\%$ of the initial kinetic energy.<br><br><em>Distractor Traps:</em><br>&bull; A (0.0% loss) assumes a perfectly elastic collision where mechanical energy is conserved.<br>&bull; B (25.0% loss) calculates $KE$ proportional to final velocity ($3/6 = 0.5$ squared is $0.25$).<br>&bull; C (75.0% loss) calculates $(1 - v_f^2 / v_i^2)$ with mismatched mass."
        },
        {
            "q": "A modular prosthetic leg is modeled as three collinear point masses along the vertical axis: foot ($m_1 = 1.00\\text{ kg}$ at $y_1 = 10.0\\text{ cm}$), lower leg ($m_2 = 3.00\\text{ kg}$ at $y_2 = 30.0\\text{ cm}$), and thigh ($m_3 = 6.00\\text{ kg}$ at $y_3 = 60.0\\text{ cm}$). What is the vertical center of mass coordinate ($y_{cm}$) of the prosthetic system?",
            "ch": [
                "46.0 cm",
                "33.3 cm",
                "40.0 cm",
                "50.0 cm"
            ],
            "a": 0,
            "d": True,
            "e": "<strong>Center of mass for discrete multi-body systems:</strong> The center of mass coordinate along a single coordinate axis is given by the mass-weighted average of position: $y_{cm} = \\frac{\\sum m_i y_i}{\\sum m_i}$. Evaluating the numerator: $\\sum m_i y_i = (1.00\\text{ kg})(10.0\\text{ cm}) + (3.00\\text{ kg})(30.0\\text{ cm}) + (6.00\\text{ kg})(60.0\\text{ cm}) = 10.0 + 90.0 + 360.0 = 460.0\\text{ kg}\\cdot\\text{cm}$. The total mass is $M_{tot} = 1.00 + 3.00 + 6.00 = 10.00\\text{ kg}$. Dividing gives: $y_{cm} = \\frac{460.0\\text{ kg}\\cdot\\text{cm}}{10.00\\text{ kg}} = 46.0\\text{ cm}$.<br><br><em>Distractor Traps:</em><br>&bull; B (33.3 cm) is the unweighted arithmetic mean of positions: $(10.0 + 30.0 + 60.0) / 3 = 33.3\\text{ cm}$.<br>&bull; C (40.0 cm) assigns equal 1/3 weighting to each position.<br>&bull; D (50.0 cm) inverts the weights or assumes the thigh dominates completely."
        },
        {
            "q": "A clinical urinometer (hydrometer) floats in pure water ($\\rho_w = 1.000\\text{ g/cm}^3$) with $82.0\\%$ of its total volume submerged. When transferred to a patient's urine specimen, the urinometer floats with $80.0\\%$ of its volume submerged. What is the specific gravity (SG) of the urine sample?",
            "ch": [
                "0.976",
                "1.000",
                "1.025",
                "1.050"
            ],
            "a": 2,
            "d": True,
            "e": "<strong>Hydrometer principle and specific gravity:</strong> A floating object displaces a weight of fluid equal to its own weight ($W = \\rho_{fluid} V_{sub} g = m_{obj} g$). Because the hydrometer's total mass $m_{obj}$ is constant: $\\rho_w V_{sub,w} = \\rho_{urine} V_{sub,urine}$. Specific gravity is the ratio of fluid density to water density: $\\text{SG} = \\frac{\\rho_{urine}}{\\rho_w} = \\frac{V_{sub,w}}{V_{sub,urine}}$. Substituting the submerged volume percentages: $\\text{SG} = \\frac{0.820\\,V_{tot}}{0.800\\,V_{tot}} = \\frac{82.0}{80.0} = 1.025$. (Normal physiological urine specific gravity ranges from 1.005 to 1.030).<br><br><em>Distractor Traps:</em><br>&bull; A (0.976) inverts the volume ratio ($80.0 / 82.0 = 0.976$), which would incorrectly indicate a fluid less dense than water.<br>&bull; B (1.000) is the specific gravity of pure water.<br>&bull; D (1.050) doubles the density increment ($1 + 2 \\times 0.025$)."
        },
        {
            "q": "In an adult patient standing erect, the vertical distance from the aortic valve to the foot is $1.35\\text{ m}$. Assuming blood density is $\\rho = 1060\\text{ kg/m}^3$, $g = 9.80\\text{ m/s}^2$, and $1.00\\text{ mmHg} = 133.3\\text{ Pa}$, what is the hydrostatic pressure difference between the heart and foot?",
            "ch": [
                "52.6 mmHg",
                "85.0 mmHg",
                "140 mmHg",
                "105 mmHg"
            ],
            "a": 3,
            "d": True,
            "e": "<strong>Hydrostatic fluid column pressure:</strong> The hydrostatic pressure difference between two points separated by vertical height $h$ in a stationary fluid column is given by $\\Delta P = \\rho g h$. Substituting $\\rho = 1060\\text{ kg/m}^3$, $g = 9.80\\text{ m/s}^2$, and $h = 1.35\\text{ m}$: $\\Delta P = (1060\\text{ kg/m}^3)(9.80\\text{ m/s}^2)(1.35\\text{ m}) = 14,023.8\\text{ Pa}$. Converting to mmHg using $1.00\\text{ mmHg} = 133.3\\text{ Pa}$: $\\Delta P = \\frac{14,023.8\\text{ Pa}}{133.3\\text{ Pa/mmHg}} = 105.2\\text{ mmHg} \\approx 105\\text{ mmHg}$. This explains why arterial blood pressure in the feet of a standing person is ~105 mmHg higher than at heart level.<br><br><em>Distractor Traps:</em><br>&bull; A (52.6 mmHg) halves the column height ($0.675\\text{ m}$).<br>&bull; B (85.0 mmHg) uses water density ($\\rho = 1000\\text{ kg/m}^3$) and misdivides by 160.<br>&bull; C (140 mmHg) forgets to divide by 133.3 or confuses column height with total height."
        },
        {
            "q": "A hydraulic hospital bed lift operates via Pascal's principle. The small circular input piston has a radius of $r_1 = 2.00\\text{ cm}$, while the load-bearing output piston has a radius of $r_2 = 12.0\\text{ cm}$. If an operator applies a downward force of $100\\text{ N}$ to the input piston, what is the maximum weight the lift can support?",
            "ch": [
                "600 N",
                "1200 N",
                "2400 N",
                "3600 N"
            ],
            "a": 3,
            "d": True,
            "e": "<strong>Pascal's principle and hydraulic force multiplication:</strong> Pascal's principle states that pressure applied to an enclosed incompressible fluid is transmitted undiminished to every portion of the fluid: $P_1 = P_2 \\implies \\frac{F_1}{A_1} = \\frac{F_2}{A_2} \\implies F_2 = F_1 \\left(\\frac{A_2}{A_1}\\right)$. The cross-sectional areas of circular pistons are proportional to the square of their radii: $\\frac{A_2}{A_1} = \\frac{\\pi r_2^2}{\\pi r_1^2} = \\left(\\frac{r_2}{r_1}\\right)^2$. Substituting $r_2 = 12.0\\text{ cm}$ and $r_1 = 2.00\\text{ cm}$: $\\frac{A_2}{A_1} = \\left(\\frac{12.0}{2.00}\\right)^2 = (6.00)^2 = 36.0$. Multiplying by input force $F_1 = 100\\text{ N}$: $F_2 = (100\\text{ N})(36.0) = 3600\\text{ N}$.<br><br><em>Distractor Traps:</em><br>&bull; A (600 N) uses the linear radius ratio ($r_2 / r_1 = 6$) rather than area ratio: $100 \\times 6 = 600\\text{ N}$.<br>&bull; B (1200 N) doubles the linear ratio ($100 \\times 12 = 1200\\text{ N}$).<br>&bull; C (2400 N) incorrectly computes $(12 / 2) \\times 400$ or miscalculates area."
        },
        {
            "q": "A researcher determines the density of a cortical bone biopsy specimen via hydrostatic weighing. The specimen registers a dry weight of $0.450\\text{ N}$ in air, but registers an apparent weight of $0.250\\text{ N}$ when completely submerged in pure water (density $\\rho_w = 1.00 \\times 10^3\\text{ kg/m}^3$). What is the specific gravity of the bone specimen?",
            "ch": [
                "0.56",
                "1.80",
                "2.25",
                "4.50"
            ],
            "a": 2,
            "d": True,
            "e": "<strong>Archimedes' principle and specific gravity:</strong> Archimedes' principle states that the buoyant force ($F_b$) on a submerged object equals the weight of displaced fluid: $F_b = W_{air} - W_{sub}$. For this specimen: $F_b = 0.450\\text{ N} - 0.250\\text{ N} = 0.200\\text{ N}$. The volume of the submerged object equals the volume of displaced water ($V = F_b / (\\rho_w g)$). The density of the object is $\\rho_{obj} = \\frac{m}{V} = \\frac{W_{air}/g}{F_b / (\\rho_w g)} = \\left(\\frac{W_{air}}{F_b}\\right)\\rho_w$. Therefore, the specific gravity is simply the ratio of weight in air to buoyant force: $\\text{SG} = \\frac{W_{air}}{F_b} = \\frac{0.450\\text{ N}}{0.200\\text{ N}} = 2.25$.<br><br><em>Distractor Traps:</em><br>&bull; A (0.56) computes $W_{sub} / W_{air} = 0.250 / 0.450 = 0.556$.<br>&bull; B (1.80) divides weight in air by submerged apparent weight ($0.450 / 0.250 = 1.80$).<br>&bull; D (4.50) divides $0.450 / 0.100$ or doubles 2.25."
        },
        {
            "q": "Jurin's law dictates that the equilibrium height $h$ to which a wetting liquid ascends in a narrow vertical tube is given by $h = \\frac{2\\gamma\\cos\\theta}{\\rho g r}$. If blood serum with contact angle $\\theta \\approx 0^\\circ$ rises to a height of $4.00\\text{ cm}$ in a glass capillary tube of inner radius $r$, what height will the serum reach in a narrower capillary tube of radius $r/2$ under identical conditions?",
            "ch": [
                "1.00 cm",
                "2.00 cm",
                "4.00 cm",
                "8.00 cm"
            ],
            "a": 3,
            "d": True,
            "e": "<strong>Capillary action and Jurin's law scaling:</strong> Jurin's law establishes that the capillary rise height is inversely proportional to the tube's inner radius: $h = \\frac{2\\gamma\\cos\\theta}{\\rho g r} \\implies h \\propto \\frac{1}{r}$. When surface tension $\\gamma$, contact angle $\\theta$, density $\\rho$, and gravity $g$ remain constant, halving the tube radius ($r_{new} = r/2$) yields: $h_{new} = \\frac{2\\gamma\\cos\\theta}{\\rho g (r/2)} = 2 \\left(\\frac{2\\gamma\\cos\\theta}{\\rho g r}\\right) = 2 h$. Therefore, the fluid will rise to twice its original height: $h_{new} = 2 \\times 4.00\\text{ cm} = 8.00\\text{ cm}$.<br><br><em>Distractor Traps:</em><br>&bull; A (1.00 cm) assumes an inverse-square relationship ($(1/2)^2 = 1/4$).<br>&bull; B (2.00 cm) assumes a direct relationship where halving radius halves height.<br>&bull; C (4.00 cm) assumes capillary height is independent of radius."
        }
    ]
}

if __name__ == "__main__":
    assert len(discrete_data["qs"]) == 10, f"Expected 10 questions, got {len(discrete_data['qs'])}"
    for idx, q in enumerate(discrete_data["qs"]):
        assert len(q["ch"]) == 4, f"Q{idx+43} does not have 4 choices"
        assert q["a"] in [0, 1, 2, 3], f"Q{idx+43} answer index invalid"
        assert q.get("d") is True, f"Q{idx+43} missing d: True"
        assert "Distractor Traps:" in q["e"], f"Q{idx+43} missing Distractor Traps"
        lens = [len(c) for c in q["ch"]]
        avg = sum(lens) / 4.0
        max_dev = max(abs(l - avg) / avg for l in lens)
        print(f"Q{idx+43}: lengths={lens}, avg={avg:.1f}, max_dev={max_dev:.2%}")
        assert max_dev <= 0.25, f"Q{idx+43} length parity failed: {max_dev:.2%}"
    print("Discretes validated successfully!")
