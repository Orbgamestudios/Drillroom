# /home/cgslinde/DrillRoom/DrillRoom/scratch/cp_passages/p3.py
"""
Passage 3: Topic 236 — Newton's Laws of Motion & Inertial Reference Frames
"""

passage_data = {
    "id": "exam_cp90_3_p3",
    "sec": "C/P",
    "topic": "Newton's Laws of Motion & Inertial Reference Frames in Clinical Transport and Traction",
    "sheet": 3,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_3",
    "passage": "<div class=\"ttl\">Passage 3 (Questions 13&ndash;18)</div>\n"
               "<p>Transporting critically injured trauma patients between hospital floors requires rigorous management of dynamic inertial forces. Rapid acceleration or deceleration of hospital elevators alters the apparent weight ($W_{app}$) experienced by patients, potentially exacerbating unstable cervical spine fractures or displacing orthopedic skeletal traction pins. The biomechanical interaction between a supine patient of mass $m_p = 70.0\\text{ kg}$ and an instrumented transport bed of mass $m_b = 50.0\\text{ kg}$ (total system mass $M_{sys} = 120.0\\text{ kg}$) is analyzed in an elevator cab suspended by high-tensile steel cables.</p>\n"
               "<p>According to Newton's Second Law, the motion of the patient within an inertial reference frame fixed to the elevator shaft is governed by $\\sum F_y = F_N - m_p g = m_p a$, where $F_N$ represents the upward contact normal force exerted by the mattress on the patient, $g = 9.80\\text{ m/s}^2$ is the acceleration due to gravity, and $a$ is the vertical acceleration of the elevator cab (with upward taken as positive). The apparent weight recorded by piezoresistive pressure sensors embedded beneath the mattress reflects this normal force: $W_{app} = F_N = m_p(g + a)$. Simultaneously, load cells measure the total tensile force ($T$) supported by the overhead hoist cables: $T = M_{sys}(g + a)$. Table 1 details the kinematic states, normal force readings, cable tensions, and perceived g-force ratios across five operational phases of inter-floor transit.</p>\n"
               "<table class=\"tbl\">\n"
               "  <caption>Table 1 Dynamic sensor measurements for a 70.0 kg patient on a 50.0 kg bed during elevator transit</caption>\n"
               "  <thead>\n"
               "    <tr><th>Phase</th><th>Kinematic Description</th><th>Acceleration $a$ (m/s<sup>2</sup>)</th><th>Patient Normal Force $F_N$ (N)</th><th>Cable Tension $T$ (N)</th><th>Apparent Weight Ratio ($F_N / m_p g$)</th></tr>\n"
               "  </thead>\n"
               "  <tbody>\n"
               "    <tr><td>Phase 1</td><td>Stationary on ground floor</td><td>0.00</td><td>686</td><td>1176</td><td>1.00</td></tr>\n"
               "    <tr><td>Phase 2</td><td>Upward acceleration</td><td>+2.00</td><td>826</td><td>1416</td><td>1.20</td></tr>\n"
               "    <tr><td>Phase 3</td><td>Upward constant velocity (3.0 m/s)</td><td>0.00</td><td>686</td><td>1176</td><td>1.00</td></tr>\n"
               "    <tr><td>Phase 4</td><td>Upward deceleration (slowing down)</td><td>-1.80</td><td>560</td><td>960</td><td>0.82</td></tr>\n"
               "    <tr><td>Phase 5</td><td>Downward acceleration</td><td>-2.00</td><td>546</td><td>936</td><td>0.80</td></tr>\n"
               "  </tbody>\n"
               "</table>\n"
               "<p>Additionally, clinical engineers evaluate orthopedic traction setups, wherein a suspended counterweight provides continuous axial tension along fractured long bones via a low-friction pulley system.</p>",
    "qs": [
        {
            "q": "During Phase 2, what is the magnitude of the apparent weight experienced by the 70.0 kg patient as measured by the bed sensors?",
            "ch": [
                "546 N",
                "686 N",
                "966 N",
                "826 N"
            ],
            "a": 3,
            "e": "<strong>Apparent weight during upward acceleration:</strong> The apparent weight of a body is defined as the magnitude of the normal force ($F_N$) supporting it. Setting up Newton's Second Law for the patient: $\\sum F_y = F_N - m_p g = m_p a \\implies F_N = m_p(g + a)$. In Phase 2, upward acceleration is $a = +2.00\\text{ m/s}^2$. Substituting the parameters: $F_N = (70.0\\text{ kg})(9.80\\text{ m/s}^2 + 2.00\\text{ m/s}^2) = (70.0\\text{ kg})(11.80\\text{ m/s}^2) = 826\\text{ N}$.<br><br><em>Distractor Traps:</em><br>&bull; A (546 N) calculates the apparent weight during downward acceleration ($g - a = 7.80\\text{ m/s}^2$).<br>&bull; B (686 N) is the true gravitational weight ($m_p g$) when stationary or moving at constant velocity.<br>&bull; C (966 N) adds twice the acceleration or miscalculates $70 \\times 13.8$."
        },
        {
            "q": "In Phase 4, the elevator cab decelerates at $1.80\\text{ m/s}^2$ while ascending. What is the magnitude of the net force acting on the total system (patient plus bed, mass = 120.0 kg)?",
            "ch": [
                "126 N",
                "216 N",
                "960 N",
                "1176 N"
            ],
            "a": 1,
            "e": "<strong>Newton's Second Law net force calculation:</strong> According to Newton's Second Law, the net external force acting on any physical system is strictly equal to the product of total mass and acceleration: $F_{net} = M_{sys} \\cdot |a|$. For the combined patient-bed system ($M_{sys} = 70.0\\text{ kg} + 50.0\\text{ kg} = 120.0\\text{ kg}$) undergoing a deceleration magnitude of $|a| = 1.80\\text{ m/s}^2$: $F_{net} = (120.0\\text{ kg})(1.80\\text{ m/s}^2) = 216\\text{ N}$ directed downward.<br><br><em>Distractor Traps:</em><br>&bull; A (126 N) calculates the net force on the patient alone ($70.0 \\times 1.80 = 126\\text{ N}$), ignoring the bed.<br>&bull; C (960 N) is the upward cable tension $T$, not the net force.<br>&bull; D (1176 N) is the static gravitational force acting on the combined system ($M_{sys} g$)."
        },
        {
            "q": "Which pair of forces constitutes an authentic Newton's Third Law action-reaction pair in the elevator scenario?",
            "ch": [
                "Upward normal force on the patient and downward gravitational pull on patient",
                "Upward normal force on the patient and downward contact force on the mattress",
                "Upward hoist tension on elevator cab and downward gravitational pull on cab",
                "Upward normal force on the patient and downward cable tension on elevator cab"
            ],
            "a": 1,
            "e": "<strong>Newton's Third Law force pairs:</strong> Newton's Third Law states that every action force is accompanied by an equal and opposite reaction force acting on the <i>other</i> interacting body ($F_{A\\rightarrow B} = -F_{B\\rightarrow A}$). The contact normal force exerted upward by the mattress on the patient ($F_{\\text{bed}\\rightarrow\\text{patient}}$) is paired with the contact force exerted downward by the patient on the mattress ($F_{\\text{patient}\\rightarrow\\text{bed}}$). These forces are identical in magnitude, opposite in direction, and act on two distinct objects.<br><br><em>Distractor Traps:</em><br>&bull; A pairs normal force and gravity; although they may balance when stationary, both act on the patient (gravity is exerted by Earth, normal force by the bed), so they are not an action-reaction pair.<br>&bull; C pairs cable tension and gravity on the cab, which also act on the same object from different sources.<br>&bull; D connects two entirely separate contact/tension interfaces."
        },
        {
            "q": "While the elevator ascends at a constant vertical velocity of 3.0 m/s in Phase 3, how does the patient's scale reading compare to the stationary reading in Phase 1?",
            "ch": [
                "Lower, because upward motion continually reduces contact pressure against bed.",
                "Higher, because upward kinetic energy generates supplementary dynamic thrust.",
                "Identical, because zero vertical acceleration implies zero net dynamic force.",
                "Oscillating, because uniform linear velocity induces cyclic inertial waves."
            ],
            "a": 2,
            "e": "<strong>Inertial reference frames and zero acceleration:</strong> An elevator ascending at constant velocity constitutes an inertial reference frame. By Newton's First and Second Laws, if velocity is constant, acceleration is strictly zero ($a = 0$). Consequently, $\\sum F_y = F_N - m_p g = m_p(0) = 0 \\implies F_N = m_p g$. The scale reading in Phase 3 ($686\\text{ N}$) is identical to the scale reading when stationary in Phase 1 ($686\\text{ N}$). Velocity alone does not generate force; only acceleration alters apparent weight.<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly asserts that upward motion relieves weight.<br>&bull; B falsely claims kinetic energy generates an upward contact thrust.<br>&bull; D invents fictitious inertial oscillations during uniform motion."
        },
        {
            "q": "If the elevator hoist cables were to completely sever during descent, causing unrestricted free fall ($a = -9.80\\text{ m/s}^2$), what normal force would the mattress exert on the patient?",
            "ch": [
                "0.00 N",
                "343 N",
                "686 N",
                "1372 N"
            ],
            "a": 0,
            "e": "<strong>Apparent weightlessness in free fall:</strong> In unrestricted free fall, both the elevator cab and the patient accelerate downward at identical rates equal to gravitational acceleration ($a = -g$). Evaluating the normal force equation: $F_N = m_p(g + a) = m_p(g - g) = 0.00\\text{ N}$. Because both the mattress and the patient accelerate downward together at $g$, there is no mutual compressive contact force between them, resulting in complete apparent weightlessness ($F_N = 0$).<br><br><em>Distractor Traps:</em><br>&bull; B (343 N) is half the patient's stationary weight.<br>&bull; C (686 N) is the stationary gravitational weight, ignoring free fall acceleration.<br>&bull; D (1372 N) adds gravity instead of subtracting it, doubling the weight ($m_p \\times 2g$)."
        },
        {
            "q": "An orthopedic traction cable runs over a low-friction pulley and supports a suspended mass of $5.00\\text{ kg}$. During Phase 2, when the elevator accelerates upward at $2.00\\text{ m/s}^2$, what is the tension in the traction cable?",
            "ch": [
                "39.0 N",
                "49.0 N",
                "59.0 N",
                "69.0 N"
            ],
            "a": 2,
            "e": "<strong>Tension under vertical acceleration:</strong> Applying Newton's Second Law to the suspended counterweight ($m_w = 5.00\\text{ kg}$), the upward cable tension $T$ and downward gravity $m_w g$ yield a net upward acceleration $a$: $\\sum F_y = T - m_w g = m_w a \\implies T = m_w(g + a)$. Substituting $g = 9.80\\text{ m/s}^2$ and $a = +2.00\\text{ m/s}^2$: $T = (5.00\\text{ kg})(9.80 + 2.00) = (5.00\\text{ kg})(11.80\\text{ m/s}^2) = 59.0\\text{ N}$.<br><br><em>Distractor Traps:</em><br>&bull; A (39.0 N) subtracts acceleration: $5.00 \\times (9.80 - 2.00) = 39.0\\text{ N}$, which corresponds to downward acceleration.<br>&bull; B (49.0 N) is the static tension when stationary: $5.00 \\times 9.80 = 49.0\\text{ N}$.<br>&bull; D (69.0 N) adds an extra $10\\text{ N}$ or assumes $a = 4.0\\text{ m/s}^2$."
        }
    ]
}

if __name__ == "__main__":
    import re
    clean = re.sub(r'<[^>]+>', ' ', passage_data["passage"])
    words = clean.split()
    print(f"Passage 3 word count: {len(words)}")
    assert 200 <= len(words) <= 400, f"Word count out of range: {len(words)}"
    assert len(passage_data["qs"]) == 6, f"Expected 6 questions, got {len(passage_data['qs'])}"
    for idx, q in enumerate(passage_data["qs"]):
        assert len(q["ch"]) == 4, f"Q{idx+13} does not have 4 choices"
        assert q["a"] in [0, 1, 2, 3], f"Q{idx+13} answer index invalid"
        assert "Distractor Traps:" in q["e"], f"Q{idx+13} missing Distractor Traps"
        lens = [len(c) for c in q["ch"]]
        avg = sum(lens) / 4.0
        max_dev = max(abs(l - avg) / avg for l in lens)
        print(f"Q{idx+13}: lengths={lens}, avg={avg:.1f}, max_dev={max_dev:.2%}")
        assert max_dev <= 0.25, f"Q{idx+13} length parity failed: {max_dev:.2%}"
    print("Passage 3 validated successfully!")
