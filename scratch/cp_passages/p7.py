# /home/cgslinde/DrillRoom/DrillRoom/scratch/cp_passages/p7.py
"""
Passage 7: Topic 240 — Conservative vs Non-Conservative Forces
"""

passage_data = {
    "id": "exam_cp90_3_p7",
    "sec": "C/P",
    "topic": "Conservative vs Non-Conservative Forces in Energy-Storing Prosthetics",
    "sheet": 7,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_3",
    "passage": "<div class=\"ttl\">Passage 7 (Questions 37&ndash;42)</div>\n"
               "<p>Modern running prostheses for lower-limb amputees incorporate curved, carbon-fiber composite springs (commonly termed running blades) designed to mimic the biological energy-storing function of the human Achilles tendon and gastrocnemius complex. During the initial ground-contact stance phase, downward gravitational and inertial forces compress the prosthetic leaf spring by a maximum displacement ($\\Delta x$), storing mechanical work as elastic potential energy: $U_e = \\frac{1}{2} k (\\Delta x)^2$, where $k$ is the effective spring constant. During the late stance and toe-off phases, the blade recoils elastically, returning this potential energy as forward kinetic energy to propel the runner into flight phase.</p>\n"
               "<p>In a purely conservative physical system, the mechanical energy is perfectly preserved ($\\Delta E_{mech} = \\Delta KE + \\Delta U = 0$). In physical carbon-fiber laminates and polymeric matrix resins, however, non-conservative internal frictional forces cause viscoelastic hysteresis. When plotted on a force-displacement ($F$-$x$) diagram across a complete compression-recoil cycle, the unloading recoil curve falls below the compression curve. The area bounded between these two curves represents non-conservative work ($W_{nc} = \\oint \\vec{F} \\cdot d\\vec{x} = \\Delta E_{diss}$), which is irreversibly dissipated into internal thermal energy (heat) and acoustic vibrations. Conversely, in specialized prosthetic knee orthoses, clinical engineers deliberately introduce non-conservative viscous fluid dampers ($F_d = -c v$) to dissipate excess kinetic energy during late swing phase, preventing knee hyperextension with an instantaneous rate of energy dissipation given by $P = c v^2$. Table 1 details mechanical metrics, stored energies, returned energies, and thermal dissipation measured across four prosthetic devices under standardized cyclic testing.</p>\n"
               "<table class=\"tbl\">\n"
               "  <caption>Table 1 Mechanical work, elastic energy storage, and dissipation in prosthetic springs and dampers</caption>\n"
               "  <thead>\n"
               "    <tr><th>Device</th><th>Mechanism</th><th>Stiffness $k$ (kN/m)</th><th>Peak Deflection (m)</th><th>Input Work $E_{in}$ (J)</th><th>Returned Energy $E_{out}$ (J)</th><th>Thermal Loss &Delta;E (J)</th></tr>\n"
               "  </thead>\n"
               "  <tbody>\n"
               "    <tr><td>Blade Model A</td><td>Carbon-Fiber Spring</td><td>40.0</td><td>0.050</td><td>50.0</td><td>46.0</td><td>4.0</td></tr>\n"
               "    <tr><td>Blade Model B</td><td>Stiff Sprint Blade</td><td>60.0</td><td>0.040</td><td>48.0</td><td>44.2</td><td>3.8</td></tr>\n"
               "    <tr><td>Damper Model C</td><td>Viscous Knee Orthosis</td><td>N/A</td><td>0.050</td><td>50.0</td><td>10.0</td><td>40.0</td></tr>\n"
               "    <tr><td>Ideal Spring</td><td>Theoretical Reference</td><td>40.0</td><td>0.050</td><td>50.0</td><td>50.0</td><td>0.0</td></tr>\n"
               "  </tbody>\n"
               "</table>\n"
               "<p>Materials scientists record infrared thermography during high-cadence treadmill sprints to verify that steady-state blade temperature rises match predicted cumulative hysteresis dissipation.</p>",
    "qs": [
        {
            "q": "What is the theoretical elastic potential energy stored in Blade Model A at its maximum stance deflection of $0.050\\text{ m}$ ($k = 40.0\\text{ kN/m}$)?",
            "ch": [
                "25.0 J",
                "1000 J",
                "100 J",
                "50.0 J"
            ],
            "a": 3,
            "e": "<strong>Hookean elastic potential energy:</strong> Elastic potential energy stored in an ideal spring compressed by displacement $x$ is given by $U_e = \\frac{1}{2} k x^2$. Converting the stiffness of Blade Model A to standard SI units: $k = 40.0\\text{ kN/m} = 4.00 \\times 10^4\\text{ N/m}$. The deflection is $x = 0.050\\text{ m}$. Substituting these values: $U_e = \\frac{1}{2}(4.00 \\times 10^4\\text{ N/m})(0.050\\text{ m})^2 = (2.00 \\times 10^4)(0.0025\\text{ m}^2) = 50.0\\text{ J}$.<br><br><em>Distractor Traps:</em><br>&bull; A (25.0 J) divides by 4 or mistakenly halves the correct energy.<br>&bull; B (1000 J) fails to square the deflection: $0.5 \\times 40,000 \\times 0.050 = 1000\\text{ J}$.<br>&bull; C (100 J) forgets the factor of 1/2, calculating $k x^2 = 40,000 \\times 0.0025 = 100\\text{ J}$."
        },
        {
            "q": "For Blade Model A, why is the returned mechanical energy ($46.0\\text{ J}$) during recoil strictly less than the mechanical work invested during compression ($50.0\\text{ J}$)?",
            "ch": [
                "Non-conservative internal polymeric friction dissipates mechanical energy as heat.",
                "Gravitational potential energy permanently converts mechanical energy into mass.",
                "The spring constant decreases exponentially during tensile unloading cycles.",
                "Normal force exerted by the running track does negative work on the prosthetic.",
                ],
            "a": 0,
            "e": "<strong>Non-conservative dissipation via viscoelastic hysteresis:</strong> Conservative forces (such as gravity or ideal elastic springs) conserve total mechanical energy over a complete cycle ($\\Delta E_{mech} = 0$). However, real materials experience internal friction between polymer chains and carbon fiber layers as they deform. This non-conservative internal friction performs negative work on the system ($W_{nc} = -4.0\\text{ J}$), transforming ordered mechanical strain energy into disordered thermal vibration (heat) and acoustic energy. Consequently, $E_{out} = E_{in} + W_{nc} = 50.0\\text{ J} - 4.0\\text{ J} = 46.0\\text{ J}$.<br><br><em>Distractor Traps:</em><br>&bull; B invokes mass-energy equivalence, which is completely irrelevant to classical biomechanics.<br>&bull; C is incorrect: the spring constant does not exponentially decay; rather, hysteresis causes path-dependent stress-strain loops.<br>&bull; D is false: track reaction force provides boundary support, but does not absorb net energy over stance."
        },
        {
            "q": "On a force versus displacement ($F$-$x$) diagram depicting the full compression and recoil cycle of Blade Model A, what does the area enclosed between the two curves represent?",
            "ch": [
                "The net mechanical kinetic energy transferred to the runner at toe-off",
                "The quantity of thermal energy dissipated through viscoelastic hysteresis",
                "The maximum instantaneous mechanical power produced during peak stance",
                "The total gravitational potential energy gained during the airborne phase"
            ],
            "a": 1,
            "e": "<strong>Physical significance of hysteresis loops:</strong> On a force-displacement graph, the area under the compression (loading) curve represents the total mechanical work done on the spring during compression: $W_{in} = \\int F_{load} \\, dx = 50.0\\text{ J}$. The area under the recoil (unloading) curve represents the mechanical work returned by the spring to the runner: $W_{out} = \\int F_{unload} \\, dx = 46.0\\text{ J}$. The closed area enclosed between the two curves is the difference: $\\oint F \\, dx = W_{in} - W_{out} = 4.0\\text{ J}$, which corresponds precisely to the thermal energy dissipated by non-conservative hysteresis forces.<br><br><em>Distractor Traps:</em><br>&bull; A describes the area under the unloading curve ($W_{out} = 46.0\\text{ J}$), not the enclosed loop area.<br>&bull; C confuses work (area under $F$-$x$ curve) with power (rate of work over time).<br>&bull; D confuses spring hysteresis with flight gravitational potential energy."
        },
        {
            "q": "If the $46.0\\text{ J}$ of returned elastic energy from Blade Model A is converted completely into kinetic energy of a runner's leg of effective mass $5.75\\text{ kg}$ at toe-off, what is the toe-off speed?",
            "ch": [
                "2.00 m/s",
                "4.00 m/s",
                "8.00 m/s",
                "16.0 m/s"
            ],
            "a": 1,
            "e": "<strong>Kinetic energy to velocity derivation:</strong> Kinetic energy is given by $KE = \\frac{1}{2}m v^2$. Rearranging to solve for velocity: $v = \\sqrt{\\frac{2 KE}{m}}$. Substituting $KE = 46.0\\text{ J}$ and $m = 5.75\\text{ kg}$: $v = \\sqrt{\\frac{2(46.0\\text{ J})}{5.75\\text{ kg}}} = \\sqrt{\\frac{92.0}{5.75}} = \\sqrt{16.0} = 4.00\\text{ m/s}$.<br><br><em>Distractor Traps:</em><br>&bull; A (2.00 m/s) forgets the factor of 2 in the numerator: $\\sqrt{46.0 / 5.75} = \\sqrt{8.0} \\approx 2.83$, or halves the correct velocity.<br>&bull; C (8.00 m/s) multiplies by 2 outside the square root or computes $92 / 5.75 = 16$ and forgets to take the square root.<br>&bull; D (16.0 m/s) forgets to take the square root entirely ($v^2 = 16.0$)."
        },
        {
            "q": "Which mathematical criterion rigorously defines a conservative force field $\\vec{F}$ acting on an object traveling along any arbitrary closed loop path $C$?",
            "ch": [
                "&oint;<sub>C</sub> F&middot;dr = 0",
                "&oint;<sub>C</sub> F&middot;dr > 0",
                "&oint;<sub>C</sub> F&middot;dr < 0",
                "&oint;<sub>C</sub> F&times;dr = 0"
            ],
            "a": 0,
            "e": "<strong>Mathematical definition of conservative forces:</strong> A force is defined as conservative if and only if the total work done by the force around any arbitrary closed loop path is strictly zero: $\\oint_C \\vec{F} \\cdot d\\vec{r} = 0$. Equivalently, the work done between any two points is completely path-independent. Non-conservative forces (like friction or viscous drag) do negative net work over a closed path ($\\oint_C \\vec{F}_{nc} \\cdot d\\vec{r} < 0$), continually removing mechanical energy from the system.<br><br><em>Distractor Traps:</em><br>&bull; B and C describe non-conservative work over a closed trajectory where net energy is added or removed.<br>&bull; D uses a cross product instead of a scalar dot product; work is fundamentally a scalar defined by the dot product."
        },
        {
            "q": "In Damper Model C, the viscous damping force is $F_d = -c v$, where $c = 200\\text{ N}\\cdot\\text{s/m}$. At an instantaneous speed of $v = 1.50\\text{ m/s}$, what is the instantaneous rate of energy dissipation?",
            "ch": [
                "150 W",
                "300 W",
                "450 W",
                "600 W"
            ],
            "a": 2,
            "e": "<strong>Instantaneous mechanical power dissipation:</strong> Power is defined as the scalar dot product of force and velocity: $P = \\vec{F} \\cdot \\vec{v} = F v$. For a linear viscous damper where resistive force magnitude is $F_d = c v$, the rate of mechanical energy dissipation (power) is $P = (c v) v = c v^2$. Substituting $c = 200\\text{ N}\\cdot\\text{s/m}$ and $v = 1.50\\text{ m/s}$: $P = (200\\text{ N}\\cdot\\text{s/m})(1.50\\text{ m/s})^2 = (200)(2.25) = 450\\text{ W}$.<br><br><em>Distractor Traps:</em><br>&bull; A (150 W) computes $P = c v / 2$ or forgets the square and divides by 2.<br>&bull; B (300 W) computes the damping force itself ($F_d = c v = 200 \\times 1.50 = 300\\text{ N}$), confusing force with power.<br>&bull; D (600 W) doubles the force or computes $200 \\times 3.0 = 600\\text{ W}$."
        }
    ]
}

if __name__ == "__main__":
    import re
    clean = re.sub(r'<[^>]+>', ' ', passage_data["passage"])
    words = clean.split()
    print(f"Passage 7 word count: {len(words)}")
    assert 200 <= len(words) <= 400, f"Word count out of range: {len(words)}"
    assert len(passage_data["qs"]) == 6, f"Expected 6 questions, got {len(passage_data['qs'])}"
    for idx, q in enumerate(passage_data["qs"]):
        assert len(q["ch"]) == 4, f"Q{idx+37} does not have 4 choices"
        assert q["a"] in [0, 1, 2, 3], f"Q{idx+37} answer index invalid"
        assert "Distractor Traps:" in q["e"], f"Q{idx+37} missing Distractor Traps"
        lens = [len(c) for c in q["ch"]]
        avg = sum(lens) / 4.0
        max_dev = max(abs(l - avg) / avg for l in lens)
        print(f"Q{idx+37}: lengths={lens}, avg={avg:.1f}, max_dev={max_dev:.2%}")
        assert max_dev <= 0.25, f"Q{idx+37} length parity failed: {max_dev:.2%}"
    print("Passage 7 validated successfully!")
