# /home/cgslinde/DrillRoom/DrillRoom/scratch/cp_passages/p6.py
"""
Passage 6: Topic 239 — Work-Energy Theorem & Kinetic Energy
"""

passage_data = {
    "id": "exam_cp90_3_p6",
    "sec": "C/P",
    "topic": "Work-Energy Theorem & Kinetic Energy in Cardiac Hemodynamics",
    "sheet": 6,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_3",
    "passage": "<div class=\"ttl\">Passage 6 (Questions 31&ndash;6)</div>\n"
               "<p>During each cardiac cycle, the muscular wall of the human left ventricle (LV) performs mechanical work to eject oxygenated blood into the aorta against the resistive impedance of the systemic arterial tree. In clinical physiology, ventricular performance is evaluated using pressure-volume ($P$-$V$) loops obtained via conductance catheterization. The external mechanical work performed by the myocardium during a single contraction, termed stroke work ($W_{stroke}$), corresponds to the integration of ventricular pressure over the change in cavity volume: $W_{stroke} = \\oint P \\, dV$. For a simplified rectangular approximation, stroke work is calculated as the product of mean aortic ejection pressure ($P_{mean}$) and stroke volume ($\\Delta V = SV = \\text{EDV} - \\text{ESV}$), where EDV is end-diastolic volume and ESV is end-systolic volume ($1.00\\text{ mmHg} = 133.3\\text{ Pa}$, $1.00\\text{ mL} = 1.00 \\times 10^{-6}\\text{ m}^3$).</p>\n"
               "<p>According to the Work-Energy Theorem, the net mechanical work performed on a parcel of blood accelerates its mass ($m$) from rest in the ventricular cavity ($v_i = 0\\text{ m/s}$) to a peak ejection velocity ($v_f$) in the aortic root: $W_{net} = \\Delta KE = \\frac{1}{2}m v_f^2 - \\frac{1}{2}m v_i^2 = \\frac{1}{2}m v_f^2$. Assuming a physiological blood density of $\\rho = 1050\\text{ kg/m}^3$, the mass of blood ejected per stroke is $m = \\rho \\cdot SV$. Beyond accelerating blood mass, cardiac work also overcomes viscous dissipation in peripheral microvascular beds, where mechanical flow energy is irreversibly degraded into thermal energy. Table 1 lists hemodynamic parameters, ventricular stroke work, and peak aortic blood velocities across four clinical cardiovascular conditions in a 70 kg patient.</p>\n"
               "<table class=\"tbl\">\n"
               "  <caption>Table 1 Hemodynamic parameters and mechanical stroke work across physiological conditions</caption>\n"
               "  <thead>\n"
               "    <tr><th>Cardiovascular State</th><th>EDV (mL)</th><th>ESV (mL)</th><th>Stroke Vol. (mL)</th><th>Mean Pressure (mmHg)</th><th>Stroke Work (J)</th><th>Peak Velocity (m/s)</th></tr>\n"
               "  </thead>\n"
               "  <tbody>\n"
               "    <tr><td>Baseline Rest</td><td>120</td><td>50</td><td>70</td><td>95</td><td>0.89</td><td>1.00</td></tr>\n"
               "    <tr><td>Strenuous Exercise</td><td>150</td><td>40</td><td>110</td><td>120</td><td>1.76</td><td>2.00</td></tr>\n"
               "    <tr><td>Severe Aortic Stenosis</td><td>130</td><td>60</td><td>70</td><td>180</td><td>1.68</td><td>4.00</td></tr>\n"
               "    <tr><td>Dilated Cardiomyopathy</td><td>200</td><td>150</td><td>50</td><td>75</td><td>0.50</td><td>0.70</td></tr>\n"
               "  </tbody>\n"
               "</table>\n"
               "<p>Continuous Doppler echocardiography confirms that blood flow profiles remain predominantly laminar in healthy aortic roots but transition to turbulent jets across stenotic valves.</p>",
    "qs": [
        {
            "q": "For the Baseline Rest state, what is the calculated external mechanical stroke work performed by the left ventricle if mean pressure is 95 mmHg ($1.27 \\times 10^4\\text{ Pa}$) and stroke volume is 70 mL ($7.0 \\times 10^{-5}\\text{ m}^3$)?",
            "ch": [
                "0.089 J",
                "0.89 J",
                "8.90 J",
                "89.0 J"
            ],
            "a": 1,
            "e": "<strong>Pressure-volume work calculation:</strong> Mechanical work is the product of pressure and volume change: $W = P \\Delta V$. Pressure must be expressed in Pascals ($\\text{N/m}^2$) and volume in cubic meters ($\\text{m}^3$): $P = 95\\text{ mmHg} \\times 133.3\\text{ Pa/mmHg} \\approx 1.266 \\times 10^4\\text{ Pa}$, and $\\Delta V = 70\\text{ mL} \\times 10^{-6}\\text{ m}^3/\\text{mL} = 7.0 \\times 10^{-5}\\text{ m}^3$. Multiplying: $W = (1.266 \\times 10^4\\text{ N/m}^2)(7.0 \\times 10^{-5}\\text{ m}^3) = 0.886\\text{ J} \\approx 0.89\\text{ J}$.<br><br><em>Distractor Traps:</em><br>&bull; A (0.089 J) divides by an extra factor of 10 or misconverts milliliters ($10^{-7}$).<br>&bull; C (8.90 J) multiplies by 10 or forgets a power of 10.<br>&bull; D (89.0 J) forgets the $10^{-6}$ volumetric conversion factor or uses Liters directly without converting to cubic meters."
        },
        {
            "q": "According to the Work-Energy Theorem, what net work must be done on an ejected blood mass of $0.070\\text{ kg}$ to accelerate it from rest to a peak velocity of $1.00\\text{ m/s}$?",
            "ch": [
                "0.018 J",
                "0.140 J",
                "0.070 J",
                "0.035 J"
            ],
            "a": 3,
            "e": "<strong>Work-Energy Theorem kinetic energy derivation:</strong> The Work-Energy Theorem establishes that the net work performed on an object equals its change in kinetic energy: $W_{net} = \\Delta KE = \\frac{1}{2}m v_f^2 - \\frac{1}{2}m v_i^2$. Because blood starts from rest within the ventricle ($v_i = 0$), the equation simplifies to $W_{net} = \\frac{1}{2}m v_f^2$. Substituting $m = 0.070\\text{ kg}$ and $v_f = 1.00\\text{ m/s}$: $W_{net} = \\frac{1}{2}(0.070\\text{ kg})(1.00\\text{ m/s})^2 = 0.035\\text{ J}$. Note that this kinetic work is a small fraction (~4%) of the total stroke work (0.89 J), the vast majority of which is expended establishing potential pressure energy.<br><br><em>Distractor Traps:</em><br>&bull; A (0.018 J) halves the result again ($0.25 \\times m v^2$).<br>&bull; B (0.140 J) doubles the kinetic energy ($2 m v^2$).<br>&bull; C (0.070 J) forgets the factor of 1/2 in kinetic energy ($m v^2$)."
        },
        {
            "q": "During Strenuous Exercise, peak aortic blood velocity increases from 1.00 m/s to 2.00 m/s. By what factor does the kinetic energy per unit volume of ejected blood increase?",
            "ch": [
                "1.4-fold",
                "2.0-fold",
                "4.0-fold",
                "8.0-fold"
            ],
            "a": 2,
            "e": "<strong>Quadratic velocity scaling of kinetic energy:</strong> Kinetic energy per unit volume is given by $\\frac{KE}{V} = \\frac{1}{2}\\rho v^2$. Because fluid density $\\rho$ remains constant, kinetic energy density scales with the square of velocity: $KE \\propto v^2$. Doubling the velocity from $1.00\\text{ m/s}$ to $2.00\\text{ m/s}$ scales the kinetic energy by a factor of: $\\frac{KE_{exercise}}{KE_{rest}} = \\left(\\frac{2.00}{1.00}\\right)^2 = 2^2 = 4.0$. Thus, kinetic energy increases 4-fold.<br><br><em>Distractor Traps:</em><br>&bull; A (1.4-fold) takes the square root ($\\sqrt{2} \\approx 1.41$).<br>&bull; B (2.0-fold) assumes a linear relationship with velocity ($KE \\propto v$).<br>&bull; D (8.0-fold) assumes a cubic power ($2^3 = 8$)."
        },
        {
            "q": "If the heart beats at a frequency of 72 beats per minute at Baseline Rest with a stroke work of 0.89 J per beat, what is the average mechanical power output of the left ventricle?",
            "ch": [
                "0.53 W",
                "1.07 W",
                "64.1 W",
                "107 W"
            ],
            "a": 1,
            "e": "<strong>Cardiac mechanical power output:</strong> Power is the rate at which work is performed: $P = \\frac{W}{\\Delta t} = W_{stroke} \\times f$, where $f$ is the heart rate in beats per second (Hertz). Converting 72 beats/min to seconds: $f = \\frac{72\\text{ beats}}{60\\text{ s}} = 1.20\\text{ beats/s}$. Multiplying by the stroke work per beat: $P = (0.89\\text{ J/beat}) \\times (1.20\\text{ beats/s}) = 1.068\\text{ W} \\approx 1.07\\text{ W}$.<br><br><em>Distractor Traps:</em><br>&bull; A (0.53 W) divides the power by 2.<br>&bull; C (64.1 W) forgets to convert minutes to seconds, multiplying $0.89 \\times 72 = 64.08\\text{ W}$.<br>&bull; D (107 W) multiplies by an erroneous factor of 100."
        },
        {
            "q": "On a diagnostic ventricular pressure-volume (P-V) loop, which geometric characteristic directly represents the net external mechanical stroke work performed during one cardiac cycle?",
            "ch": [
                "The area enclosed within the perimeter of the four phases of the loop",
                "The linear slope of the end-systolic elastance relationship boundary",
                "The horizontal width of the loop between the end-systolic and diastolic volumes",
                "The vertical height of the isovolumetric contraction segment on pressure axis"
            ],
            "a": 0,
            "e": "<strong>Geometric interpretation of P-V loops:</strong> Work is mathematically defined as the integral $\\oint P \\, dV$. On a Cartesian plot where pressure ($P$) is the vertical axis and volume ($V$) is the horizontal axis, the integral of $P$ with respect to $V$ around a closed operating trajectory corresponds exactly to the two-dimensional area enclosed within the loop boundaries. Counter-clockwise traversal of the four phases (filling, isovolumetric contraction, ejection, isovolumetric relaxation) yields net positive external mechanical work done on the vasculature.<br><br><em>Distractor Traps:</em><br>&bull; B represents myocardial contractility (end-systolic elastance $E_{es}$), not work.<br>&bull; C represents stroke volume ($SV = \\text{EDV} - \\text{ESV}$), which is only one component of work.<br>&bull; D represents the pressure developed during isovolumetric contraction without volume change ($W = 0$ during that phase)."
        },
        {
            "q": "Why does the systemic circulation require continuous ventricular mechanical work to maintain blood flow, rather than operating as a self-sustaining conservative system?",
            "ch": [
                "Non-conservative viscous drag dissipates fluid mechanical energy into heat.",
                "Negative gravitational potential energy continually destroys circulating kinetic energy.",
                "Capillary expansion breaks hydrostatic fluid columns to create energy sinks.",
                "Erythrocyte membranes absorb fluid mechanical work to drive active ion pumps."
            ],
            "a": 0,
            "e": "<strong>Non-conservative viscous dissipation in hemodynamics:</strong> A conservative mechanical system conserves the sum of kinetic and potential energy indefinitely ($\\Delta E_{mech} = 0$). In the vascular system, however, blood is a viscous fluid flowing through narrow microvessels (arterioles and capillaries). Internal fluid friction (viscosity) and shear stresses along vessel walls are non-conservative forces. As blood circulates, viscous shear performs negative work ($W_{nc} < 0$), continually degrading fluid pressure and kinetic energy into non-recoverable thermal energy (heat). The heart must continuously pump to replenish this dissipated energy and sustain circulation.<br><br><em>Distractor Traps:</em><br>&bull; B is false: the cardiovascular system is a closed hydrodynamic loop where gravity cancels out over any complete circuit.<br>&bull; C falsely claims cross-sectional expansion destroys energy.<br>&bull; D invents active transport powered directly by hydrodynamic flow work."
        }
    ]
}

if __name__ == "__main__":
    import re
    clean = re.sub(r'<[^>]+>', ' ', passage_data["passage"])
    words = clean.split()
    print(f"Passage 6 word count: {len(words)}")
    assert 200 <= len(words) <= 400, f"Word count out of range: {len(words)}"
    assert len(passage_data["qs"]) == 6, f"Expected 6 questions, got {len(passage_data['qs'])}"
    for idx, q in enumerate(passage_data["qs"]):
        assert len(q["ch"]) == 4, f"Q{idx+31} does not have 4 choices"
        assert q["a"] in [0, 1, 2, 3], f"Q{idx+31} answer index invalid"
        assert "Distractor Traps:" in q["e"], f"Q{idx+31} missing Distractor Traps"
        lens = [len(c) for c in q["ch"]]
        avg = sum(lens) / 4.0
        max_dev = max(abs(l - avg) / avg for l in lens)
        print(f"Q{idx+31}: lengths={lens}, avg={avg:.1f}, max_dev={max_dev:.2%}")
        assert max_dev <= 0.25, f"Q{idx+31} length parity failed: {max_dev:.2%}"
    print("Passage 6 validated successfully!")
