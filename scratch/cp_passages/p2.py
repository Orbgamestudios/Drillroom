# /home/cgslinde/DrillRoom/DrillRoom/scratch/cp_passages/p2.py
"""
Passage 2: Topic 235 — Two-Dimensional Projectile Motion & Vector Independence
"""

passage_data = {
    "id": "exam_cp90_3_p2",
    "sec": "C/P",
    "topic": "Two-Dimensional Projectile Motion & Vector Independence in Paralympic Biomechanics",
    "sheet": 2,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_3",
    "passage": "<div class=\"ttl\">Passage 2 (Questions 7&ndash;12)</div>\n"
               "<p>In Paralympic throwing sports, seated athletes launch competitive implements (e.g., shot put, javelin) from specialized throwing frames anchored to a concrete circle. Because trunk stability, shoulder positioning, and release heights differ substantially from standing throws, sports biomechanists use high-speed optical motion capture (500 frames/s) to optimize release parameters. The projectile's flight path through the air is modeled by decoupling its continuous trajectory into two independent, mutually perpendicular kinematic components: a horizontal axis ($x$) with zero net acceleration ($a_x = 0$), and a vertical axis ($y$) dominated by constant gravitational downward acceleration ($a_y = -g = -9.80\\text{ m/s}^2$).</p>\n"
               "<p>An elite seated athlete launched a standardized 4.00 kg shot put at varying release angles ($\\theta$) relative to the horizontal, with a constant initial launch speed of $v_0 = 10.0\\text{ m/s}$ from a fixed seated release height of $y_0 = 1.60\\text{ m}$. Kinematic equations for horizontal and vertical positions as functions of elapsed flight time $t$ are given by $x(t) = (v_0\\cos\\theta)t$ and $y(t) = y_0 + (v_0\\sin\\theta)t - \\frac{1}{2}gt^2$. The vertical velocity at any instant is $v_y(t) = v_0\\sin\\theta - gt$. Table 1 displays the launch parameters, velocity components, time to apogee, maximum vertical height ($y_{max}$), and measured horizontal range ($R$) at ground landing ($y = 0\\text{ m}$) across four experimental trials.</p>\n"
               "<table class=\"tbl\">\n"
               "  <caption>Table 1 Kinematic trajectory parameters of a 4.00 kg shot launched at 10.0 m/s from 1.60 m height</caption>\n"
               "  <thead>\n"
               "    <tr><th>Trial</th><th>Launch Angle &theta; (&deg;)</th><th>Initial $v_x$ (m/s)</th><th>Initial $v_y$ (m/s)</th><th>Time to Apogee (s)</th><th>Max Height $y_{max}$ (m)</th><th>Horizontal Range $R$ (m)</th></tr>\n"
               "  </thead>\n"
               "  <tbody>\n"
               "    <tr><td>Trial 1</td><td>0.0</td><td>10.00</td><td>0.00</td><td>0.00</td><td>1.60</td><td>5.71</td></tr>\n"
               "    <tr><td>Trial 2</td><td>30.0</td><td>8.66</td><td>5.00</td><td>0.51</td><td>2.88</td><td>11.08</td></tr>\n"
               "    <tr><td>Trial 3</td><td>45.0</td><td>7.07</td><td>7.07</td><td>0.72</td><td>4.15</td><td>11.60</td></tr>\n"
               "    <tr><td>Trial 4</td><td>60.0</td><td>5.00</td><td>8.66</td><td>0.88</td><td>5.43</td><td>9.65</td></tr>\n"
               "  </tbody>\n"
               "</table>\n"
               "<p>Aerodynamic drag is determined to contribute less than 1.5% variance over the short flight duration, allowing pure ballistic equations to accurately predict implement trajectories.</p>",
    "qs": [
        {
            "q": "At the apogee (peak height) of the trajectory in Trial 3, what are the magnitude of velocity and the acceleration of the projectile?",
            "ch": [
                "Velocity is 0.00 m/s; acceleration is 9.80 m/s^2 directed downward.",
                "Velocity is 7.07 m/s; acceleration is 9.80 m/s^2 directed downward.",
                "Velocity is 7.07 m/s; acceleration is 0.00 m/s^2 along the trajectory.",
                "Velocity is 10.0 m/s; acceleration is 9.80 m/s^2 directed downward."
            ],
            "a": 1,
            "e": "<strong>Vector independence at apogee:</strong> At the highest point of a parabolic trajectory, the vertical component of velocity momentarily vanishes ($v_y = 0\\text{ m/s}$). However, because horizontal acceleration is zero, the horizontal velocity component remains constant throughout the flight: $v_x = v_0\\cos(45.0^\\circ) = 7.07\\text{ m/s}$. Thus, the overall velocity magnitude at apogee is $\\sqrt{v_x^2 + v_y^2} = \\sqrt{(7.07)^2 + 0^2} = 7.07\\text{ m/s}$. Gravity acts downward continuously throughout the entire flight, so acceleration is strictly $g = 9.80\\text{ m/s}^2$ downward.<br><br><em>Distractor Traps:</em><br>&bull; A confuses the total velocity with the vertical component, incorrectly assuming total velocity is zero at the peak.<br>&bull; C incorrectly assumes acceleration ceases at the peak where vertical velocity is zero.<br>&bull; D uses the initial launch speed ($v_0 = 10.0\\text{ m/s}$), neglecting the loss of vertical kinetic energy."
        },
        {
            "q": "In Trial 2, how much time elapses between implement release and the moment the shot reaches its maximum vertical elevation?",
            "ch": [
                "0.26 s",
                "1.02 s",
                "0.88 s",
                "0.51 s"
            ],
            "a": 3,
            "e": "<strong>Time to apogee derivation:</strong> The vertical velocity equation is $v_y(t) = v_{0y} - gt$. At maximum height, vertical velocity is zero: $0 = v_{0y} - gt_{apex} \\implies t_{apex} = \\frac{v_{0y}}{g}$. In Trial 2, $v_{0y} = v_0\\sin(30.0^\\circ) = 10.0 \\times 0.500 = 5.00\\text{ m/s}$. Therefore, $t_{apex} = \\frac{5.00\\text{ m/s}}{9.80\\text{ m/s}^2} \\approx 0.510\\text{ s}$.<br><br><em>Distractor Traps:</em><br>&bull; A (0.26 s) incorrectly divides by $2g$ instead of $g$.<br>&bull; B (1.02 s) represents the total round-trip flight time to return to the original release height ($2 \\times t_{apex}$).<br>&bull; C (0.88 s) uses the vertical velocity component from Trial 4 ($8.66 / 9.80$)."
        },
        {
            "q": "If the athlete increases launch velocity from 10.0 m/s to 14.0 m/s at a 45.0&deg; launch angle from ground level ($y_0 = 0$), by what percentage does the horizontal range increase?",
            "ch": [
                "40% increase",
                "70% increase",
                "96% increase",
                "140% increase"
            ],
            "a": 2,
            "e": "<strong>Range proportionality with launch speed:</strong> For a projectile launched from and returning to ground level ($y_0 = 0$), the horizontal range is given by $R = \\frac{v_0^2\\sin(2\\theta)}{g}$. For a fixed launch angle, range is directly proportional to the square of initial velocity: $R \\propto v_0^2$. Taking the ratio of new to old range: $\\frac{R_{new}}{R_{old}} = \\left(\\frac{14.0}{10.0}\\right)^2 = (1.40)^2 = 1.96$. A ratio of 1.96 corresponds to a $96\\%$ increase in range ($1.96 - 1.00 = 0.96$).<br><br><em>Distractor Traps:</em><br>&bull; A (40%) reflects a linear scaling error ($14.0 / 10.0 = 1.40$, a 40% increase), forgetting that velocity is squared.<br>&bull; B (70%) assumes range scales with $v_0 \\sqrt{2}$.<br>&bull; D (140%) is the new range expressed as a percentage of the original plus 40%."
        },
        {
            "q": "Which fundamental physical principle explains why the horizontal velocity component remains constant throughout the implement's flight?",
            "ch": [
                "Zero net horizontal force results in zero horizontal acceleration.",
                "Gravitational field lines exert equal and opposite torque vectors.",
                "Conservation of momentum strictly requires orthogonal decoupling.",
                "Centripetal forces exactly counterbalance gravitational pull vectors."
            ],
            "a": 0,
            "e": "<strong>Newton's First Law and vector independence:</strong> According to Newton's First Law of Motion, an object continues in its state of uniform motion unless acted upon by an external net force. Because gravity acts strictly in the vertical direction (downward toward Earth's center) and aerodynamic drag is neglected, the net horizontal force is zero ($F_{net,x} = 0$). By Newton's Second Law ($F_{net,x} = ma_x$), horizontal acceleration is zero ($a_x = 0$), meaning horizontal velocity $v_x$ remains constant throughout the trajectory.<br><br><em>Distractor Traps:</em><br>&bull; B invents a pseudo-scientific explanation involving gravitational torques.<br>&bull; C misapplies momentum conservation, which applies to closed multi-body systems rather than external gravitational trajectories.<br>&bull; D incorrectly introduces centripetal force into linear free-fall motion."
        },
        {
            "q": "In Trial 1 ($\theta = 0.0^\circ$, $y_0 = 1.60\text{ m}$), what is the magnitude of the vertical component of velocity $v_y$ immediately prior to ground landing?",
            "ch": [
                "2.80 m/s",
                "5.60 m/s",
                "8.66 m/s",
                "10.0 m/s"
            ],
            "a": 1,
            "e": "<strong>Vertical velocity upon ground impact:</strong> In Trial 1, the implement is launched horizontally, so its initial vertical velocity is zero ($v_{0y} = 0\\text{ m/s}$). The vertical motion is pure free fall from rest over a vertical displacement of $\\Delta y = -1.60\\text{ m}$. Applying Torricelli's equation for the vertical axis: $v_y^2 = v_{0y}^2 + 2g|\\Delta y| = 0 + 2(9.80\\text{ m/s}^2)(1.60\\text{ m}) = 31.36\\text{ m}^2/\\text{s}^2$. Taking the square root: $|v_y| = \\sqrt{31.36} = 5.60\\text{ m/s}$.<br><br><em>Distractor Traps:</em><br>&bull; A (2.80 m/s) forgets the factor of 2 inside the square root: $\\sqrt{g \\Delta y} = \\sqrt{15.68} \\approx 3.96$, or halves 5.60.<br>&bull; C (8.66 m/s) confuses the velocity with horizontal velocity components from other trials.<br>&bull; D (10.0 m/s) is the horizontal velocity component $v_x$."
        },
        {
            "q": "Why does the optimal launch angle for achieving maximum horizontal range shift to less than 45.0&deg; when projectiles are released from an elevated platform ($y_0 > 0$)?",
            "ch": [
                "Shallower angles maximize horizontal speed without sacrificing extra flight time.",
                "Elevated launch heights increase the effective local gravitational acceleration.",
                "Horizontal drag forces decrease significantly when projectiles stay close to ground.",
                "Higher release angles cause implement rotation that disrupts laminar air streams."
            ],
            "a": 0,
            "e": "<strong>Elevated launch angle optimization:</strong> When launching from ground level ($y = 0$), $45.0^\\circ$ provides the perfect symmetry between horizontal velocity ($v_x = v_0\\cos\\theta$) and flight time ($t = 2v_0\\sin\\theta / g$). However, when launching from an elevation ($y_0 > 0$), the projectile has extra fall distance below the release point, providing extra flight time even with a smaller initial vertical velocity. Athletes can therefore trade away some vertical velocity in favor of a larger horizontal velocity ($v_x = v_0\\cos\\theta$) by using a shallower angle (typically $38^\\circ$--$42^\\circ$), maximizing horizontal distance traveled.<br><br><em>Distractor Traps:</em><br>&bull; B falsely claims that gravitational acceleration varies with small elevation changes.<br>&bull; C is incorrect because drag does not decrease near the ground.<br>&bull; D focuses on rotational aerodynamic effects, whereas the angle shift is a purely kinematic effect present even in a total vacuum."
        }
    ]
}

if __name__ == "__main__":
    import re
    clean = re.sub(r'<[^>]+>', ' ', passage_data["passage"])
    words = clean.split()
    print(f"Passage 2 word count: {len(words)}")
    assert 200 <= len(words) <= 400, f"Word count out of range: {len(words)}"
    assert len(passage_data["qs"]) == 6, f"Expected 6 questions, got {len(passage_data['qs'])}"
    for idx, q in enumerate(passage_data["qs"]):
        assert len(q["ch"]) == 4, f"Q{idx+7} does not have 4 choices"
        assert q["a"] in [0, 1, 2, 3], f"Q{idx+7} answer index invalid"
        assert "Distractor Traps:" in q["e"], f"Q{idx+7} missing Distractor Traps"
        lens = [len(c) for c in q["ch"]]
        avg = sum(lens) / 4.0
        max_dev = max(abs(l - avg) / avg for l in lens)
        print(f"Q{idx+7}: lengths={lens}, avg={avg:.1f}, max_dev={max_dev:.2%}")
        assert max_dev <= 0.25, f"Q{idx+7} length parity failed: {max_dev:.2%}"
    print("Passage 2 validated successfully!")
