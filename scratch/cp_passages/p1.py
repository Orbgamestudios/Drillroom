# /home/cgslinde/DrillRoom/DrillRoom/scratch/cp_passages/p1.py
"""
Passage 1: Topic 234 — One-Dimensional Kinematics & Freefall Acceleration
"""

passage_data = {
    "id": "exam_cp90_3_p1",
    "sec": "C/P",
    "topic": "One-Dimensional Kinematics & Freefall Acceleration in Pulmonary Drug Delivery",
    "sheet": 1,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_3",
    "passage": "<div class=\"ttl\">Passage 1 (Questions 1&ndash;6)</div>\n"
               "<p>Targeted pulmonary drug delivery requires precise control over the aerodynamic deposition of nebulized aerosol droplets in deep alveolar tissue. To avoid premature upper-airway impaction, pharmacologists synthesize polymeric microparticles and evaluate their sedimentation behavior. In an analytical testing facility, microparticles are introduced into an instrumented drop tower consisting of two parallel vertical columns: an evacuated vacuum column ($P < 10^{-4}\\text{ Torr}$) and a fluid-filled settling column maintained at atmospheric pressure ($1.00\\text{ atm}$, $T = 293\\text{ K}$) containing standard dry air (density $\\rho_{air} = 1.20\\text{ kg/m}^3$, dynamic viscosity $\\eta = 1.81 \\times 10^{-5}\\text{ Pa}\\cdot\\text{s}$).</p>\n"
               "<p>In the vacuum column, particles accelerate solely under the influence of gravity ($g = 9.80\\text{ m/s}^2$). Kinematic sensors track downward position $y(t)$, instantaneous velocity $v(t)$, and elapsed fall time $t$ over a standardized vertical drop distance of $h = 4.90\\text{ m}$ from rest ($v_0 = 0\\text{ m/s}$). In the atmospheric column, particles encounter a velocity-dependent linear aerodynamic drag force, $F_d = -b v$, where $b$ represents the Stokes drag coefficient governed by sphere diameter $d$ ($b = 3\\pi\\eta d$). As downward velocity increases, aerodynamic drag opposes the gravitational force ($F_g = mg$), causing net acceleration to diminish until reaching terminal velocity ($v_t$), at which point net force is zero. Physical dimensions, mass, fall times, and measured terminal velocities for four therapeutic microsphere formulations are summarized in Table 1.</p>\n"
               "<table class=\"tbl\">\n"
               "  <caption>Table 1 Physical parameters and sedimentation kinematics of therapeutic microspheres</caption>\n"
               "  <thead>\n"
               "    <tr><th>Formulation</th><th>Diameter $d$ (&mu;m)</th><th>Mass $m$ ($10^{-11}$ kg)</th><th>Vacuum Fall Time from 4.90 m (s)</th><th>Measured Terminal Velocity $v_t$ (m/s)</th><th>Linear Drag Coeff. $b$ ($10^{-8}$ N&middot;s/m)</th></tr>\n"
               "  </thead>\n"
               "  <tbody>\n"
               "    <tr><td>Formulation 1</td><td>10.0</td><td>0.52</td><td>1.00</td><td>0.30</td><td>1.70</td></tr>\n"
               "    <tr><td>Formulation 2</td><td>20.0</td><td>4.16</td><td>1.00</td><td>1.20</td><td>3.40</td></tr>\n"
               "    <tr><td>Formulation 3</td><td>30.0</td><td>14.04</td><td>1.00</td><td>2.70</td><td>5.10</td></tr>\n"
               "    <tr><td>Formulation 4</td><td>40.0</td><td>33.28</td><td>1.00</td><td>4.80</td><td>6.80</td></tr>\n"
               "  </tbody>\n"
               "</table>\n"
               "<p>Following sedimentation trials, researchers conduct high-speed landing deceleration tests on viscoelastic collection plates to ensure encapsulated peptide drugs do not rupture upon alveolar impact.</p>",
    "qs": [
        {
            "q": "In the evacuated drop column ($g = 9.80\\text{ m/s}^2$), what is the downward impact velocity of Formulation 2 when dropped from rest through a total height of 19.6 m?",
            "ch": [
                "9.80 m/s",
                "14.0 m/s",
                "39.2 m/s",
                "19.6 m/s"
            ],
            "a": 3,
            "e": "<strong>Torricelli kinematic equation in vacuum:</strong> In the absence of air resistance, motion under constant gravitational acceleration is governed by $v^2 = v_0^2 + 2gh$. With an initial velocity of $v_0 = 0\\text{ m/s}$, this simplifies to $v = \\sqrt{2gh} = \\sqrt{2 \\times 9.80\\text{ m/s}^2 \\times 19.6\\text{ m}} = \\sqrt{384.16} = 19.6\\text{ m/s}$.<br><br><em>Distractor Traps:</em><br>&bull; A (9.80 m/s) is the velocity after falling for only 1.0 s or from a height of 4.90 m.<br>&bull; B (14.0 m/s) is the velocity after falling 10.0 m.<br>&bull; C (39.2 m/s) results from forgetting to take the square root ($2gh / 9.8$ or doubling the correct velocity)."
        },
        {
            "q": "Which differential expression describes the instantaneous downward acceleration $a(t)$ of a microsphere of mass $m$ falling through the atmospheric column with linear drag $F_d = -bv$?",
            "ch": [
                "a(t) = g - (b/m)v",
                "a(t) = g + (b/m)v",
                "a(t) = g - (m/b)v",
                "a(t) = (b/m)v - g"
            ],
            "a": 0,
            "e": "<strong>Newton's Second Law with aerodynamic drag:</strong> Defining downward as the positive direction, two forces act on the falling microsphere: downward gravity ($F_g = mg$) and upward resistive drag ($F_d = -bv$). Summing forces gives $F_{net} = mg - bv = ma(t)$. Dividing both sides by mass $m$ yields the instantaneous acceleration: $a(t) = g - \\frac{b}{m}v$. At terminal velocity, $a(t) = 0$, giving $v_t = \\frac{mg}{b}$.<br><br><em>Distractor Traps:</em><br>&bull; B adds drag to gravity instead of subtracting it, which would imply air resistance accelerates the sphere downward.<br>&bull; C inverts the mass-to-drag ratio ($m/b$ instead of $b/m$), which has incorrect physical dimensions.<br>&bull; D reverses the signs of gravity and drag, indicating upward acceleration."
        },
        {
            "q": "A specialized nebulizer nozzle ejects a Formulation 1 droplet vertically upward into the evacuated column with an initial speed of $14.0\\text{ m/s}$. Neglecting air resistance, what maximum height above the nozzle does the droplet reach?",
            "ch": [
                "5.00 m",
                "7.14 m",
                "10.0 m",
                "20.0 m"
            ],
            "a": 2,
            "e": "<strong>Maximum height in free fall:</strong> At the apex of vertical flight, instantaneous velocity is zero ($v = 0\\text{ m/s}$). Applying $v^2 = v_0^2 - 2gh_{max} \\implies 0 = (14.0\\text{ m/s})^2 - 2(9.80\\text{ m/s}^2)h_{max}$. Solving for height: $h_{max} = \\frac{v_0^2}{2g} = \\frac{196}{19.6} = 10.0\\text{ m}$.<br><br><em>Distractor Traps:</em><br>&bull; A (5.00 m) mistakenly divides by $4g$ or divides the correct height by 2.<br>&bull; B (7.14 m) calculates $v_0 / 1.96$ or confuses displacement with apex time multiplied by velocity.<br>&bull; D (20.0 m) forgets the factor of 2 in the denominator, computing $v_0^2 / g$."
        },
        {
            "q": "During a landing impact test, a Formulation 4 capsule strikes a viscoelastic test plate at $12.0\\text{ m/s}$ and decelerates uniformly to rest over a displacement of $0.060\\text{ m}$. What is the magnitude of the deceleration?",
            "ch": [
                "100 m/s^2",
                "600 m/s^2",
                "2400 m/s^2",
                "1200 m/s^2"
            ],
            "a": 3,
            "e": "<strong>Kinematic deceleration derivation:</strong> Using the kinematic equation $v_f^2 = v_i^2 + 2ad$, where $v_f = 0\\text{ m/s}$, $v_i = 12.0\\text{ m/s}$, and $d = 0.060\\text{ m}$: $0 = (12.0)^2 + 2a(0.060) \\implies 0 = 144 + 0.120a$. Solving for the deceleration magnitude: $|a| = \\frac{144}{0.120} = 1200\\text{ m/s}^2$.<br><br><em>Distractor Traps:</em><br>&bull; A (100 m/s^2) divides velocity by distance ($12.0 / 0.060 = 200$) and halves it.<br>&bull; B (600 m/s^2) forgets the factor of 2 in the denominator, computing $v^2 / (4d)$ or $v^2 / (2 \\times 0.120)$.<br>&bull; C (2400 m/s^2) forgets the factor of 2 in $2ad$, calculating $v^2 / d = 144 / 0.060 = 2400\\text{ m/s}^2$."
        },
        {
            "q": "When Formulation 3 falls through air and reaches exactly half of its terminal velocity ($v = 0.50\\,v_t$), what percentage of the gravitational force is balanced by aerodynamic drag?",
            "ch": [
                "25% of gravitational force",
                "50% of gravitational force",
                "71% of gravitational force",
                "100% of gravitational force"
            ],
            "a": 1,
            "e": "<strong>Linear drag relationship:</strong> For Stokes flow, the drag force is strictly linear with respect to velocity: $F_d = bv$. At terminal velocity $v_t$, aerodynamic drag exactly balances gravity: $F_d(v_t) = b v_t = mg = 100\\%\\text{ of } F_g$. When falling at $v = 0.50\\,v_t$, the drag force is $F_d = b(0.50\\,v_t) = 0.50(b v_t) = 0.50 mg$, which is exactly $50\\%$ of the gravitational force.<br><br><em>Distractor Traps:</em><br>&bull; A (25%) erroneously assumes quadratic drag ($F_d \\propto v^2$), where $(0.5)^2 = 0.25$.<br>&bull; C (71%) invokes $\\sqrt{0.5} \\approx 0.707$, confusing velocity scaling with kinetic energy or RMS values.<br>&bull; D (100%) is only true when the particle reaches terminal velocity ($v = v_t$)."
        },
        {
            "q": "Which statement correctly describes the mathematical relationship between elapsed fall time $t$ and release height $h$ for particles dropped from rest in a vacuum?",
            "ch": [
                "Fall time is directly proportional to the square root of release height.",
                "Fall time is directly proportional to the second power of release height.",
                "Fall time is linearly proportional to the release height divided by mass.",
                "Fall time is inversely proportional to the square root of release height."
            ],
            "a": 0,
            "e": "<strong>Kinematic scaling of fall time:</strong> For free fall from rest in a vacuum, displacement is given by $h = \\frac{1}{2}gt^2$. Rearranging to solve for elapsed time yields $t = \\sqrt{\\frac{2h}{g}} = \\sqrt{\\frac{2}{g}} \\cdot \\sqrt{h}$. Because $g$ is constant, fall time $t$ is directly proportional to the square root of the release height ($t \\propto \\sqrt{h}$). Note that mass does not appear in this equation, confirming Galilean equivalence.<br><br><em>Distractor Traps:</em><br>&bull; B states $t \\propto h^2$, inverting the power relationship ($h \\propto t^2$, not $t \\propto h^2$).<br>&bull; C incorrectly introduces mass and assumes a linear relationship.<br>&bull; D claims an inverse relationship ($t \\propto 1/\\sqrt{h}$), which would absurdly imply taller falls take less time."
        }
    ]
}

if __name__ == "__main__":
    import re
    # Validate word count
    clean = re.sub(r'<[^>]+>', ' ', passage_data["passage"])
    words = clean.split()
    print(f"Passage 1 word count: {len(words)}")
    assert 200 <= len(words) <= 400, f"Word count out of range: {len(words)}"
    
    # Validate questions
    assert len(passage_data["qs"]) == 6, f"Expected 6 questions, got {len(passage_data['qs'])}"
    for idx, q in enumerate(passage_data["qs"]):
        assert len(q["ch"]) == 4, f"Q{idx+1} does not have 4 choices"
        assert q["a"] in [0, 1, 2, 3], f"Q{idx+1} answer index invalid"
        assert "Distractor Traps:" in q["e"], f"Q{idx+1} missing Distractor Traps"
        lens = [len(c) for c in q["ch"]]
        avg = sum(lens) / 4.0
        max_dev = max(abs(l - avg) / avg for l in lens)
        print(f"Q{idx+1}: lengths={lens}, avg={avg:.1f}, max_dev={max_dev:.2%}")
        assert max_dev <= 0.25, f"Q{idx+1} length parity failed: {max_dev:.2%}"
    print("Passage 1 validated successfully!")
