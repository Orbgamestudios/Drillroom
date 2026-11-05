# /home/cgslinde/DrillRoom/DrillRoom/scratch/cp_passages/p4.py
"""
Passage 4: Topic 237 — Static vs Kinetic Friction on Inclined Planes
"""

passage_data = {
    "id": "exam_cp90_3_p4",
    "sec": "C/P",
    "topic": "Static vs Kinetic Friction on Inclined Planes in Orthopedic Biomechanics",
    "sheet": 4,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_3",
    "passage": "<div class=\"ttl\">Passage 4 (Questions 19&ndash;24)</div>\n"
               "<p>Friction plays a dual role in orthopedic rehabilitation: high static friction is vital to prevent slips on wheelchair access ramps, whereas minimal kinetic friction is essential to prevent wear and aseptic loosening in total hip and knee arthroplasty. To evaluate joint bearing longevity and hospital surface safety, tribologists utilize an instrumented inclined plane apparatus. An articulated test sled of mass $m = 10.0\\text{ kg}$ is mounted with interchangeable material specimens and placed onto a motorized ramp whose inclination angle $\\theta$ can be continuously varied from $0.0^\\circ$ to $50.0^\\circ$.</p>\n"
               "<p>Resolving the gravitational force vector ($F_g = mg$, with $g = 9.80\\text{ m/s}^2$) into orthogonal components yields a perpendicular contact force balanced by the normal force, $F_N = mg\\cos\\theta$, and a parallel downhill driving force, $F_\\parallel = mg\\sin\\theta$. At low tilt angles, static friction opposes sliding: $f_s = mg\\sin\\theta \\le f_{s,max} = \\mu_s F_N = \\mu_s mg\\cos\\theta$. As the incline angle is incrementally increased, the sled begins to slip at a characteristic critical sliding angle $\\theta_c$, where $mg\\sin\\theta_c = \\mu_s mg\\cos\\theta_c$, establishing the mathematical relation $\\tan\\theta_c = \\mu_s$. Once motion commences, kinetic friction acts up the plane: $f_k = \\mu_k F_N = \\mu_k mg\\cos\\theta$. Applying Newton's Second Law along the incline gives the downward acceleration: $a = g(\\sin\\theta - \\mu_k\\cos\\theta)$. Table 1 displays the friction coefficients, critical slip angles, and downhill accelerations at $\\theta = 30.0^\\circ$ across four bearing and flooring interfaces.</p>\n"
               "<table class=\"tbl\">\n"
               "  <caption>Table 1 Tribological parameters and downhill kinematics of a 10.0 kg sled across test interfaces</caption>\n"
               "  <thead>\n"
               "    <tr><th>Interface</th><th>Material Pairing</th><th>Static Coeff. &mu;<sub>s</sub></th><th>Kinetic Coeff. &mu;<sub>k</sub></th><th>Critical Slip Angle &theta;<sub>c</sub> (&deg;)</th><th>Acceleration at 30.0&deg; (m/s<sup>2</sup>)</th></tr>\n"
               "  </thead>\n"
               "  <tbody>\n"
               "    <tr><td>Interface 1</td><td>CoCr Alloy on Dry UHMWPE</td><td>0.25</td><td>0.18</td><td>14.0</td><td>3.37</td></tr>\n"
               "    <tr><td>Interface 2</td><td>Ceramic on Lubricated UHMWPE</td><td>0.08</td><td>0.05</td><td>4.6</td><td>4.48</td></tr>\n"
               "    <tr><td>Interface 3</td><td>Rubber Sole on Wet Aluminum Ramp</td><td>0.60</td><td>0.45</td><td>31.0</td><td>0.00</td></tr>\n"
               "    <tr><td>Interface 4</td><td>Rubber Sole on High-Traction Grit</td><td>0.90</td><td>0.70</td><td>42.0</td><td>0.00</td></tr>\n"
               "  </tbody>\n"
               "</table>\n"
               "<p>Researchers confirm that for all tested interfaces, the static friction coefficient strictly exceeds the kinetic friction coefficient ($\\mu_s > \\mu_k$), characteristic of macroscopic Coulomb friction.</p>",
    "qs": [
        {
            "q": "At the critical tilt angle $\\theta_c$ where the sled spontaneously begins to slip from rest, which formula directly expresses the static coefficient of friction $\\mu_s$?",
            "ch": [
                "&mu;<sub>s</sub> = sin &theta;<sub>c</sub>",
                "&mu;<sub>s</sub> = cos &theta;<sub>c</sub>",
                "&mu;<sub>s</sub> = cot &theta;<sub>c</sub>",
                "&mu;<sub>s</sub> = tan &theta;<sub>c</sub>"
            ],
            "a": 3,
            "e": "<strong>Critical slip angle derivation:</strong> At the verge of slipping, the parallel downhill component of gravity is precisely balanced by the maximum static friction force: $mg\\sin\\theta_c = f_{s,max} = \\mu_s F_N$. Because the normal force on an incline is $F_N = mg\\cos\\theta_c$, substituting yields $mg\\sin\\theta_c = \\mu_s mg\\cos\\theta_c$. Dividing both sides by $mg\\cos\\theta_c$ cancels the mass and gravitational constant: $\\mu_s = \\frac{\\sin\\theta_c}{\\cos\\theta_c} = \\tan\\theta_c$.<br><br><em>Distractor Traps:</em><br>&bull; A confuses tangent with sine, valid only if normal force equaled total weight.<br>&bull; B confuses tangent with cosine.<br>&bull; C inverts the trigonometric ratio (cotangent instead of tangent)."
        },
        {
            "q": "For Interface 1 sliding on an incline tilted at $30.0^\\circ$ ($\sin 30.0^\\circ = 0.500$, $\cos 30.0^\\circ = 0.866$), what is the magnitude of the kinetic friction force acting on the 10.0 kg sled?",
            "ch": [
                "8.82 N",
                "15.3 N",
                "24.5 N",
                "49.0 N"
            ],
            "a": 1,
            "e": "<strong>Kinetic friction on an incline:</strong> The kinetic friction force is given by $f_k = \\mu_k F_N = \\mu_k mg\\cos\\theta$. For Interface 1, $\\mu_k = 0.18$, $m = 10.0\\text{ kg}$, $g = 9.80\\text{ m/s}^2$, and $\\cos(30.0^\\circ) = 0.866$. Substituting: $f_k = (0.18)(10.0\\text{ kg})(9.80\\text{ m/s}^2)(0.866) = (0.18)(98.0\\text{ N})(0.866) = 15.28\\text{ N} \\approx 15.3\\text{ N}$.<br><br><em>Distractor Traps:</em><br>&bull; A (8.82 N) mistakenly uses $\\sin(30.0^\\circ)$ instead of $\\cos(30.0^\\circ)$: $0.18 \\times 98 \\times 0.50 = 8.82\\text{ N}$.<br>&bull; C (24.5 N) uses static friction coefficient: $0.25 \\times 98 = 24.5\\text{ N}$.<br>&bull; D (49.0 N) is the parallel gravitational force component: $mg\\sin(30.0^\\circ) = 10 \\times 9.8 \\times 0.50 = 49.0\\text{ N}$."
        },
        {
            "q": "If the mass of the sled on Interface 1 is doubled from 10.0 kg to 20.0 kg, how will the critical slip angle $\\theta_c$ be affected?",
            "ch": [
                "The critical slip angle decreases because normal force increases contact cohesion.",
                "The critical slip angle doubles because static friction force scales with mass.",
                "The critical slip angle remains unchanged because mass cancels from the force balance.",
                "The critical slip angle halves because gravitational shear forces overwhelm friction."
            ],
            "a": 2,
            "e": "<strong>Mass independence of critical slip angle:</strong> The equilibrium condition at the slip threshold is $mg\\sin\\theta_c = \\mu_s mg\\cos\\theta_c$. Because mass $m$ appears as a linear factor on both sides of the equation, it cancels entirely: $\\tan\\theta_c = \\mu_s \\implies \\theta_c = \\arctan(\\mu_s)$. Consequently, the critical slip angle depends solely on the coefficient of static friction between the contact materials, completely independent of the sled's mass.<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly asserts that increased normal force alters the friction coefficient.<br>&bull; B confuses the static friction <i>force</i> (which doubles) with the critical <i>angle</i> (which is unchanged).<br>&bull; D erroneously claims greater weight promotes easier slipping on an incline."
        },
        {
            "q": "Why does the test sled on Interface 3 remain completely stationary when the ramp is set to an inclination of $30.0^\\circ$?",
            "ch": [
                "The normal force cancels the entire magnitude of the gravitational vector.",
                "The maximum available static friction exceeds the downhill gravitational force.",
                "Kinetic friction dynamically adjusts to match downhill gravitational acceleration.",
                "Atmospheric pressure generates a downward clamping force exceeding gravity."
            ],
            "a": 1,
            "e": "<strong>Static equilibrium on an incline:</strong> For Interface 3, $\\mu_s = 0.60$. The critical slip angle is $\\theta_c = \\arctan(0.60) \\approx 31.0^\\circ$. At $\\theta = 30.0^\\circ$, the downhill gravitational driving force is $F_\\parallel = mg\\sin(30.0^\\circ) = (10)(9.8)(0.500) = 49.0\\text{ N}$. The maximum possible static friction force that the surface can provide is $f_{s,max} = \\mu_s mg\\cos(30.0^\\circ) = (0.60)(10)(9.8)(0.866) = 50.9\\text{ N}$. Because $f_{s,max} > F_\\parallel$ (50.9 N > 49.0 N), static friction easily prevents motion, providing exactly $49.0\\text{ N}$ of opposing force to keep acceleration at $0.00\\text{ m/s}^2$.<br><br><em>Distractor Traps:</em><br>&bull; A is false: normal force only cancels the perpendicular component of gravity ($mg\\cos\\theta$), not the whole vector.<br>&bull; C is false: kinetic friction only acts when an object is sliding; stationary objects experience static friction.<br>&bull; D invents atmospheric clamping."
        },
        {
            "q": "The sled with Interface 1 slides a distance of $4.00\\text{ m}$ down a $30.0^\\circ$ incline. What is the total work performed by the kinetic friction force on the sled?",
            "ch": [
                "-122 J",
                "-61.2 J",
                "+61.2 J",
                "+122 J"
            ],
            "a": 1,
            "e": "<strong>Work done by friction:</strong> Work is defined as $W = \\vec{F} \\cdot \\vec{d} = F d \\cos\\phi$. Because kinetic friction acts directly opposite to the direction of sliding motion along the ramp, the angle between the friction force and displacement is $\\phi = 180^\\circ$, giving $\\cos(180^\\circ) = -1$. Using the kinetic friction force calculated previously ($f_k = 15.3\\text{ N}$) and displacement $d = 4.00\\text{ m}$: $W_f = -f_k \\cdot d = -(15.28\\text{ N})(4.00\\text{ m}) = -61.12\\text{ J} \\approx -61.2\\text{ J}$. Friction does negative work, dissipating mechanical energy as heat.<br><br><em>Distractor Traps:</em><br>&bull; A (-122 J) multiplies by 8.0 m or uses a static coefficient.<br>&bull; C (+61.2 J) has the wrong algebraic sign: kinetic friction removes mechanical energy and thus performs negative work.<br>&bull; D (+122 J) combines a sign error with a magnitude error."
        },
        {
            "q": "As an external pulling force parallel to the surface is gradually increased on a stationary sled until it accelerates, which pattern best describes the friction force?",
            "ch": [
                "Increases linearly with applied force to a peak, then drops to a constant plateau.",
                "Remains at a fixed constant value regardless of the applied external pulling force.",
                "Grows exponentially until slipping occurs, then asymptotically approaches infinity.",
                "Follows a symmetrical parabolic arc that peaks at slip and smoothly drops to zero."
            ],
            "a": 0,
            "e": "<strong>Static vs kinetic friction force profile:</strong> While the object remains stationary, static friction exactly matches the applied external force ($f_s = F_{pull}$) to maintain zero net force. This produces a linear graph of friction versus applied force with a slope of +1. Once the applied force exceeds the maximum static friction threshold ($f_{s,max} = \\mu_s F_N$), the object breaks free and begins to slide. At that precise transition, friction drops abruptly to the kinetic friction value ($f_k = \\mu_k F_N$), which remains constant as a horizontal plateau independent of speed or applied force (for Coulomb friction).<br><br><em>Distractor Traps:</em><br>&bull; B describes kinetic friction behavior or incorrectly assumes static friction is always at its maximum.<br>&bull; C falsely describes exponential growth and asymptotic infinity.<br>&bull; D invents a parabolic decline, which contradicts the discrete step-down to constant kinetic friction."
        }
    ]
}

if __name__ == "__main__":
    import re
    clean = re.sub(r'<[^>]+>', ' ', passage_data["passage"])
    words = clean.split()
    print(f"Passage 4 word count: {len(words)}")
    assert 200 <= len(words) <= 400, f"Word count out of range: {len(words)}"
    assert len(passage_data["qs"]) == 6, f"Expected 6 questions, got {len(passage_data['qs'])}"
    for idx, q in enumerate(passage_data["qs"]):
        assert len(q["ch"]) == 4, f"Q{idx+19} does not have 4 choices"
        assert q["a"] in [0, 1, 2, 3], f"Q{idx+19} answer index invalid"
        assert "Distractor Traps:" in q["e"], f"Q{idx+19} missing Distractor Traps"
        lens = [len(c) for c in q["ch"]]
        avg = sum(lens) / 4.0
        max_dev = max(abs(l - avg) / avg for l in lens)
        print(f"Q{idx+19}: lengths={lens}, avg={avg:.1f}, max_dev={max_dev:.2%}")
        assert max_dev <= 0.25, f"Q{idx+19} length parity failed: {max_dev:.2%}"
    print("Passage 4 validated successfully!")
