# /home/cgslinde/DrillRoom/DrillRoom/scratch/cp_passages/p5.py
"""
Passage 5: Topic 238 — Uniform Circular Motion & Centripetal Acceleration
"""

passage_data = {
    "id": "exam_cp90_3_p5",
    "sec": "C/P",
    "topic": "Uniform Circular Motion & Centripetal Acceleration in Analytical Ultracentrifugation",
    "sheet": 5,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_3",
    "passage": "<div class=\"ttl\">Passage 5 (Questions 25&ndash;30)</div>\n"
               "<p>Analytical ultracentrifugation (AUC) is a cornerstone biophysical technique used to determine the molecular weight, oligomeric stoichiometry, and hydrodynamic conformation of macromolecules in native solution. When a sample solution containing proteins, lipoproteins, or viral capsids is loaded into an AUC titanium rotor and spun at high angular frequency, the particles execute uniform circular motion in a horizontal plane. Although the rotational frequency remains constant, the direction of each particle's tangential velocity vector ($\\vec{v}$) continuously changes, producing a continuous centripetal acceleration ($\\vec{a}_c$) directed radially inward toward the central axis of rotation.</p>\n"
               "<p>The magnitude of the centripetal acceleration is defined by $a_c = \\frac{v^2}{r} = \\omega^2 r$, where $r$ is the radial distance from the center of rotation to the sample cell, $v = \\omega r$ is the linear tangential speed, and $\\omega$ is the angular velocity in radians per second ($\\omega = 2\\pi \\times \\text{RPM} / 60$). By Newton's Second Law, this inward acceleration requires a net inward centripetal force, $F_c = m a_c = m \\omega^2 r$, provided by the rigid mechanical structure of the rotor holding the sample cell. In the non-inertial rotating frame of reference, particles experience an apparent outward centrifugal force that drives sedimentation against solvent buoyancy and viscous drag. Centrifugal performance is reported as the Relative Centrifugal Field (RCF), expressed in multiples of Earth's standard gravity ($g = 9.80\\text{ m/s}^2$): $\\text{RCF} = a_c / g$. Table 1 compiles rotor radii, operational speeds, centripetal accelerations, and RCF values across four analytical configurations.</p>\n"
               "<table class=\"tbl\">\n"
               "  <caption>Table 1 Ultracentrifugation kinematic and acceleration parameters for macromolecular separation</caption>\n"
               "  <thead>\n"
               "    <tr><th>Rotor Config</th><th>Radius $r$ (m)</th><th>Speed (RPM)</th><th>Angular Velocity &omega; (rad/s)</th><th>Centripetal Accel. $a_c$ (m/s<sup>2</sup>)</th><th>Relative Centrifugal Field (g)</th></tr>\n"
               "  </thead>\n"
               "  <tbody>\n"
               "    <tr><td>Config A</td><td>0.050</td><td>10,000</td><td>1047</td><td>5.48 &times; 10<sup>4</sup></td><td>5,590</td></tr>\n"
               "    <tr><td>Config B</td><td>0.100</td><td>10,000</td><td>1047</td><td>1.10 &times; 10<sup>5</sup></td><td>11,200</td></tr>\n"
               "    <tr><td>Config C</td><td>0.050</td><td>40,000</td><td>4189</td><td>8.77 &times; 10<sup>5</sup></td><td>89,500</td></tr>\n"
               "    <tr><td>Config D</td><td>0.100</td><td>60,000</td><td>6283</td><td>3.95 &times; 10<sup>6</sup></td><td>403,000</td></tr>\n"
               "  </tbody>\n"
               "</table>\n"
               "<p>Optical absorbance scanners record particle boundary movement over time to calculate sedimentation coefficients without disturbing the hydrodynamic equilibrium.</p>",
    "qs": [
        {
            "q": "What is the angular velocity $\\omega$ in radians per second of an ultracentrifuge rotor operating at 10,000 RPM in Config B?",
            "ch": [
                "167 rad/s",
                "524 rad/s",
                "1047 rad/s",
                "2094 rad/s"
            ],
            "a": 2,
            "e": "<strong>Angular velocity conversion:</strong> Rotational speed in revolutions per minute (RPM) is converted to radians per second by multiplying by $2\\pi\\text{ radians}$ per revolution and dividing by $60\\text{ seconds}$ per minute: $\\omega = \\frac{2\\pi \\times 10,000\\text{ rev/min}}{60\\text{ s/min}} = \\frac{20,000\\pi}{60} = \\frac{1000\\pi}{3} \\approx \\frac{3141.59}{3} \\approx 1047\\text{ rad/s}$.<br><br><em>Distractor Traps:</em><br>&bull; A (167 rad/s) divides by 60 but omits the $2\\pi$ factor ($10,000 / 60 = 167$).<br>&bull; B (524 rad/s) multiplies by $\\pi$ instead of $2\\pi$ ($1000\\pi / 6 = 524$).<br>&bull; D (2094 rad/s) doubles the correct value ($4\\pi$ per revolution)."
        },
        {
            "q": "Comparing Config A and Config B at the same rotational speed (10,000 RPM), why is the centripetal acceleration in Config B exactly twice that in Config A?",
            "ch": [
                "Centripetal acceleration is directly proportional to radius at constant angular velocity.",
                "Tangential speed is inversely proportional to radius at constant angular velocity.",
                "Rotational kinetic energy quadruples whenever radial distance from the spindle doubles.",
                "Buoyant forces acting on the solution decrease linearly with increasing rotor radius."
            ],
            "a": 0,
            "e": "<strong>Centripetal acceleration scaling at constant angular velocity:</strong> Centripetal acceleration can be expressed either as $a_c = v^2 / r$ or as $a_c = \\omega^2 r$. When comparing two rotors operating at the same angular velocity ($\\\omega = 1047\\text{ rad/s}$), $\\omega$ is held constant. Therefore, centripetal acceleration is strictly proportional to the first power of radius: $a_c \\propto r$. Because Config B has twice the radius of Config A ($0.100\\text{ m}$ vs $0.050\\text{ m}$), its centripetal acceleration is exactly double: $\\frac{a_{c,B}}{a_{c,A}} = \\frac{0.100}{0.050} = 2.0$.<br><br><em>Distractor Traps:</em><br>&bull; B is false: tangential speed is directly proportional to radius ($v = \\omega r$), not inversely.<br>&bull; C describes kinetic energy scaling, not acceleration.<br>&bull; D introduces buoyant forces, which do not dictate rotor centripetal acceleration."
        },
        {
            "q": "In uniform circular motion at constant angular speed, what is the net mechanical work performed by the inward centripetal force on a particle during one full revolution?",
            "ch": [
                "0.00 J, because centripetal force acts perpendicular to instantaneous displacement.",
                "2&pi; F_c r, because work equals the total inward force multiplied by circumference.",
                "0.50 m v^2, because kinetic energy is periodically replenished along orbital paths.",
                "m &omega;^2 r^2, because gravitational potential energy is converted into work."
            ],
            "a": 0,
            "e": "<strong>Work in uniform circular motion:</strong> Work is defined as the line integral of force along the path of motion: $W = \\int \\vec{F} \\cdot d\\vec{r} = \\int F \\cos\\phi \\, ds$. In uniform circular motion, the centripetal force vector $\\vec{F}_c$ is always directed radially inward toward the center of rotation, whereas the instantaneous displacement vector $d\\vec{r}$ is directed tangentially along the circumference. Because the force and displacement vectors are strictly orthogonal at every instant ($\\phi = 90^\\circ$), $\\cos(90^\\circ) = 0$. Consequently, the centripetal force does zero mechanical work ($W = 0.00\\text{ J}$). Tangential speed and kinetic energy remain constant.<br><br><em>Distractor Traps:</em><br>&bull; B computes force multiplied by circumference ($F \\times 2\\pi r$), ignoring the perpendicular vector angle.<br>&bull; C is the kinetic energy, not work.<br>&bull; D combines rotational parameters into an arbitrary energy term."
        },
        {
            "q": "If the rotational speed in Config A ($r = 0.050\\text{ m}$) is increased from 10,000 RPM to 40,000 RPM, by what factor does the centripetal acceleration increase?",
            "ch": [
                "2-fold",
                "4-fold",
                "8-fold",
                "16-fold"
            ],
            "a": 3,
            "e": "<strong>Quadratic dependence on angular velocity:</strong> Centripetal acceleration is given by $a_c = \\omega^2 r$. For a fixed radius $r$, centripetal acceleration is proportional to the square of angular velocity (or RPM): $a_c \\propto \\omega^2$. Increasing rotational speed from 10,000 RPM to 40,000 RPM represents a 4-fold increase in $\\omega$ ($\\omega_{new} = 4\\,\\omega_{old}$). Squaring this factor yields: $\\frac{a_{c,new}}{a_{c,old}} = \\left(\\frac{4\\,\\omega_{old}}{\\omega_{old}}\\right)^2 = 4^2 = 16$. Thus, the centripetal acceleration increases by a factor of 16.<br><br><em>Distractor Traps:</em><br>&bull; A (2-fold) takes the square root ($\\sqrt{4} = 2$).<br>&bull; B (4-fold) assumes a linear relationship ($a_c \\propto \\omega$).<br>&bull; C (8-fold) computes $4 \\times 2$ or $2^3$."
        },
        {
            "q": "What is the linear tangential speed $v$ of a sample cell positioned at $r = 0.100\\text{ m}$ in Config D spinning at $\\omega = 6283\\text{ rad/s}$?",
            "ch": [
                "62.8 m/s",
                "314 m/s",
                "628 m/s",
                "1256 m/s"
            ],
            "a": 2,
            "e": "<strong>Linear tangential velocity from angular velocity:</strong> Tangential speed is the product of angular velocity and radial distance: $v = \\omega r$. In Config D, $\\omega = 6283\\text{ rad/s}$ and $r = 0.100\\text{ m}$. Multiplying these values yields: $v = (6283\\text{ rad/s})(0.100\\text{ m}) = 628.3\\text{ m/s} \\approx 628\\text{ m/s}$. (This supersonic speed underscores why ultracentrifuge chambers operate under a high vacuum to eliminate aerodynamic heating).<br><br><em>Distractor Traps:</em><br>&bull; A (62.8 m/s) multiplies by 0.010 m instead of 0.100 m.<br>&bull; B (314 m/s) halves the tangential velocity ($100\\pi$).<br>&bull; D (1256 m/s) doubles the tangential velocity."
        },
        {
            "q": "Which statement accurately describes the geometric orientation of the velocity and acceleration vectors for a particle undergoing uniform circular motion?",
            "ch": [
                "Velocity is tangent to orbital path; acceleration points radially toward the center.",
                "Velocity points radially toward the center; acceleration is tangent to orbital path.",
                "Velocity and acceleration vectors both point radially outward from rotation center.",
                "Velocity and acceleration vectors both point tangentially in direction of motion."
            ],
            "a": 0,
            "e": "<strong>Vector kinematics of circular motion:</strong> In uniform circular motion, an object travels along a curved circular trajectory at constant speed. The instantaneous velocity vector $\\vec{v}$ is always tangent to the circular path in the instantaneous direction of motion. Because the velocity vector is constantly turning toward the center of curvature without changing magnitude, the instantaneous acceleration vector $\\vec{a}_c$ (centripetal acceleration) points strictly radially inward toward the center of rotation, perpendicular to the velocity vector at all times.<br><br><em>Distractor Traps:</em><br>&bull; B inverts the two vectors, assigning radial direction to velocity and tangential to acceleration.<br>&bull; C claims both vectors point outward (centrifugal misconception).<br>&bull; D claims both vectors are tangential, which would describe tangential linear acceleration (changing speed), not circular curvature."
        }
    ]
}

if __name__ == "__main__":
    import re
    clean = re.sub(r'<[^>]+>', ' ', passage_data["passage"])
    words = clean.split()
    print(f"Passage 5 word count: {len(words)}")
    assert 200 <= len(words) <= 400, f"Word count out of range: {len(words)}"
    assert len(passage_data["qs"]) == 6, f"Expected 6 questions, got {len(passage_data['qs'])}"
    for idx, q in enumerate(passage_data["qs"]):
        assert len(q["ch"]) == 4, f"Q{idx+25} does not have 4 choices"
        assert q["a"] in [0, 1, 2, 3], f"Q{idx+25} answer index invalid"
        assert "Distractor Traps:" in q["e"], f"Q{idx+25} missing Distractor Traps"
        lens = [len(c) for c in q["ch"]]
        avg = sum(lens) / 4.0
        max_dev = max(abs(l - avg) / avg for l in lens)
        print(f"Q{idx+25}: lengths={lens}, avg={avg:.1f}, max_dev={max_dev:.2%}")
        assert max_dev <= 0.25, f"Q{idx+25} length parity failed: {max_dev:.2%}"
    print("Passage 5 validated successfully!")
