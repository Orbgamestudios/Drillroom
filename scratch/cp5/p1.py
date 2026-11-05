# /home/cgslinde/DrillRoom/DrillRoom/scratch/cp5/p1.py
"""
Passage 1: Topic 268 — Acoustic Cavitation in High-Intensity Focused Ultrasound (HIFU)
"""

passage_data = {
    "id": "exam_cp90_5_p1",
    "sec": "C/P",
    "topic": "Acoustic Cavitation in High-Intensity Focused Ultrasound (HIFU)",
    "sheet": 1,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_5",
    "passage": "<div class=\"ttl\">Passage 1 (Questions 1&ndash;6)</div>\n"
               "<p>High-intensity focused ultrasound (HIFU) is a non-invasive therapeutic intervention designed for precise thermal and mechanical ablation of solid tumors. In HIFU, concave piezoelectric transducers focus megahertz-frequency acoustic waves into a millimeter-scale focal volume, converting focused acoustic energy into thermal and mechanical stresses within target tissue. Propagation of ultrasound waves through biological media is governed by longitudinal pressure fluctuations characterized by speed of sound ($c \\approx 1540\\text{ m/s}$ in soft tissue), acoustic frequency ($f$), and wavelength ($\\lambda$).</p>\n"
               "<p>Beyond thermal coagulative necrosis, ultrasound beam interactions with biological fluids induce acoustic cavitation&mdash;the nucleation, oscillation, and collapse of microscopic gas bubbles. Cavitation is classified into two distinct mechanical regimes:</p>\n"
               "<p>1. <em>Stable (non-inertial) cavitation</em>: Microbubbles undergo sustained, periodic oscillations about an equilibrium radius in response to cyclic acoustic compression and rarefaction. This radial pulsation drives acoustic microstreaming in the surrounding fluid, producing shear stresses that transiently permeabilize cell membranes (sonoporation).</p>\n"
               "<p>2. <em>Inertial (transient) cavitation</em>: Under high peak rarefactional pressure ($P_r$), microbubbles expand rapidly to more than twice their equilibrium radius before collapsing violently during the compressive phase due to the inertia of the surrounding fluid. This catastrophic collapse generates localized temperatures exceeding $5000\\text{ K}$, local pressures above $100\\text{ MPa}$, high-speed liquid microjets, and the sonolytic cleavage of water into reactive hydroxyl radicals ($\\cdot\\text{OH}$).</p>\n"
               "<p>To quantify the likelihood of inertial cavitation, clinical systems compute the Mechanical Index ($MI$):</p>\n"
               "<p>$$MI = \\frac{P_r}{\\sqrt{f}}$$</p>\n"
               "<p>where $P_r$ is the derated peak rarefactional pressure in megapascals (MPa) and $f$ is the ultrasound center frequency in megahertz (MHz). An $MI > 1.9$ is generally required to initiate inertial cavitation in visceral tissues. Investigators tested four HIFU beam configurations in ex vivo tissue phantoms to establish cavitation thresholds (Table 1).</p>\n"
               "<table class=\"tbl\">\n"
               "  <caption>Table 1 Acoustic parameters, cavitation regimes, and ablation metrics across HIFU settings</caption>\n"
               "  <thead>\n"
               "    <tr><th>Setting</th><th>Frequency $f$ (MHz)</th><th>Peak Rarefactional $P_r$ (MPa)</th><th>Mechanical Index ($MI$)</th><th>Cavitation Mode</th><th>Mean Ablation Volume ($\\text{mm}^3$)</th></tr>\n"
               "  </thead>\n"
               "  <tbody>\n"
               "    <tr><td>Setting 1</td><td>1.0</td><td>0.8</td><td>0.80</td><td>None (Thermal only)</td><td>12.4</td></tr>\n"
               "    <tr><td>Setting 2</td><td>1.0</td><td>1.5</td><td>1.50</td><td>Stable Cavitation</td><td>28.6</td></tr>\n"
               "    <tr><td>Setting 3</td><td>1.0</td><td>2.5</td><td>2.50</td><td>Inertial Cavitation</td><td>84.2</td></tr>\n"
               "    <tr><td>Setting 4</td><td>4.0</td><td>2.5</td><td>1.25</td><td>Stable Cavitation</td><td>31.0</td></tr>\n"
               "  </tbody>\n"
               "</table>\n"
               "<p>Investigators next monitored whether introducing microbubble contrast agents decreases the acoustic pressure threshold required for inertial cavitation.</p>",
    "qs": [
        {
            "q": "What is the acoustic wavelength $\\lambda$ of the ultrasound beam utilized in Setting 1 ($f = 1.0\\text{ MHz}$) when propagating through soft tissue ($c = 1540\\text{ m/s}$)?",
            "ch": [
                "1.54 mm",
                "0.65 mm",
                "3.08 mm",
                "0.77 mm"
            ],
            "a": 0,
            "e": "<strong>Ultrasound wave speed, frequency, and wavelength relationship:</strong> Acoustic propagation velocity through a medium is defined by the wave equation $v = f\\lambda$, where $v = c = 1540\\text{ m/s}$ and frequency $f = 1.0\\text{ MHz} = 1.0 \\times 10^6\\text{ Hz}$. Rearranging for wavelength gives $\\lambda = \\frac{c}{f} = \\frac{1540\\text{ m/s}}{1.0 \\times 10^6\\text{ s}^{-1}} = 1.54 \\times 10^{-3}\\text{ m} = 1.54\\text{ mm}$. At this wavelength, ultrasound provides an optimal compromise between focal penetration depth and spatial focus size in visceral organs.<br><br><em>Distractor Traps:</em><br>&bull; B (0.65 mm) erroneously inverts the wave velocity formula, calculating $f / c = 1.0 \\times 10^6 / 1540$.<br>&bull; C (3.08 mm) doubles the calculated wavelength by incorrectly multiplying the velocity by 2.<br>&bull; D (0.77 mm) halves the correct value, which would correspond to a frequency of 2.0 MHz."
        },
        {
            "q": "Based on the Mechanical Index equation provided in the passage, if a HIFU beam operates at $f = 2.25\\text{ MHz}$ with a peak rarefactional pressure of $P_r = 2.50\\text{ MPa}$, what is the resulting $MI$, and will it induce inertial cavitation?",
            "ch": [
                "MI = 1.11; the beam will readily initiate inertial cavitation",
                "MI = 1.67; the beam will remain below the inertial threshold",
                "MI = 2.05; the beam will readily initiate inertial cavitation",
                "MI = 3.75; the beam will remain below the inertial threshold"
            ],
            "a": 1,
            "e": "<strong>Mechanical Index calculation and cavitation threshold:</strong> The Mechanical Index is computed as $MI = \\frac{P_r}{\\sqrt{f}}$. Substituting $P_r = 2.50\\text{ MPa}$ and $f = 2.25\\text{ MHz}$: $\\sqrt{2.25} = 1.50$, so $MI = \\frac{2.50}{1.50} = 1.67$. The passage specifies that $MI > 1.9$ is required to overcome acoustic cavitation thresholds and initiate inertial cavitation in visceral tissues. Because $1.67 < 1.9$, the ultrasound beam will not trigger inertial cavitation and will instead remain in the stable cavitation or purely thermal regime.<br><br><em>Distractor Traps:</em><br>&bull; A (1.11) erroneously divides $P_r$ by $f$ directly ($2.50 / 2.25 = 1.11$) rather than taking the square root of $f$, and misinterprets the threshold rule.<br>&bull; C (2.05) erroneously calculates $\\sqrt{P_r} / f$ or makes an arithmetic error and falsely claims cavitation occurs.<br>&bull; D (3.75) multiplies $P_r$ by $\\sqrt{f}$ ($2.50 \\times 1.50 = 3.75$) instead of dividing."
        },
        {
            "q": "Which fundamental biophysical mechanism distinguishes inertial cavitation from stable cavitation during focused ultrasound therapy?",
            "ch": [
                "Sustained radial oscillation about a constant equilibrium bubble radius",
                "Acoustic microstreaming generated without any dynamic bubble expansion",
                "Rapid bubble expansion followed by catastrophic inertia-driven collapse",
                "Continuous acoustic wave reflection at rigid mineral-tissue interfaces"
            ],
            "a": 2,
            "e": "<strong>Mechanical dynamics of inertial versus stable cavitation:</strong> Stable cavitation involves non-destructive, rhythmic expansion and contraction of gas bubbles about an equilibrium radius over hundreds or thousands of acoustic cycles, inducing localized shear stresses via acoustic microstreaming. In contrast, inertial cavitation occurs when high rarefactional pressure causes a microbubble to expand unstably to more than double its initial radius, followed by an unrestrained, catastrophic collapse driven by the inertia of the surrounding fluid. This violent collapse focuses energy into microscopic shock waves, extreme temperatures ($>5000\\text{ K}$), and high-velocity microjets, resulting in mechanical tissue lysis.<br><br><em>Distractor Traps:</em><br>&bull; A describes stable (non-inertial) cavitation, where microbubbles oscillate symmetrically without collapsing.<br>&bull; B describes microstreaming without collapse, which is characteristic of low-intensity stable acoustic agitation.<br>&bull; D refers to acoustic reflection at acoustic impedance mismatches (e.g., bone-tissue interfaces), not bubble cavitation."
        },
        {
            "q": "Acoustic intensity is related to acoustic pressure amplitude by $I = \\frac{P^2}{2\\rho c}$. If the pressure amplitude $P$ delivered by an ultrasound transducer is tripled while tissue density $\\rho$ and speed of sound $c$ remain constant, by what factor does acoustic intensity increase?",
            "ch": [
                "A factor of 1.73",
                "A factor of 3.00",
                "A factor of 6.00",
                "A factor of 9.00"
            ],
            "a": 3,
            "e": "<strong>Proportionality between acoustic intensity and pressure amplitude:</strong> Acoustic intensity ($I$) is directly proportional to the square of the pressure amplitude ($P^2$): $I \\propto P^2$. If the pressure amplitude is tripled ($P' = 3P$), the new acoustic intensity becomes $I' = \\frac{(3P)^2}{2\\rho c} = 9 \\left(\\frac{P^2}{2\\rho c}\\right) = 9I$. Thus, acoustic intensity increases by a factor of $3^2 = 9.00$. This quadratic relationship explains why modest increases in transducer driving voltage produce dramatic increases in focal heating and mechanical cavitation power.<br><br><em>Distractor Traps:</em><br>&bull; A takes the square root of 3 ($\\sqrt{3} \\approx 1.73$), inverting the power exponent.<br>&bull; B assumes a direct linear relationship between intensity and pressure ($I \\propto P$), ignoring the quadratic power term.<br>&bull; C incorrectly multiplies the factor 3 by 2 rather than squaring it."
        },
        {
            "q": "During inertial cavitation, the formation of reactive hydroxyl radicals ($\\cdot\\text{OH}$) in sonicated aqueous tissue phantoms is primarily driven by which chemical mechanism?",
            "ch": [
                "Thermal sonolysis of water driven by localized adiabatic bubble collapse",
                "Photolytic excitation of dissolved molecular oxygen by emitted phonons",
                "Direct ionization of biological lipids by coherent acoustic radiation",
                "Electrochemical oxidation induced by static surface dielectric breakdown"
            ],
            "a": 0,
            "e": "<strong>Sonolysis of water during inertial cavitation:</strong> The violent, rapid collapse of an inertial cavitation bubble occurs on nanosecond timescales and is essentially an adiabatic compression process. The compression of trapped gas and water vapor heats the interior of the bubble to transient localized temperatures exceeding $5000\\text{ K}$ and pressures exceeding $100\\text{ MPa}$. Under these extreme conditions, homolytic cleavage of the $\\text{O}-\\text{H}$ covalent bonds in vaporized water occurs: $\\text{H}_2\\text{O} \\to \\text{H}\\cdot + \\cdot\\text{OH}$. This process, known as sonolysis, produces highly reactive hydroxyl radicals capable of oxidizing cellular macromolecules.<br><br><em>Distractor Traps:</em><br>&bull; B incorrectly attributes radical formation to phonon-induced photolysis of molecular oxygen.<br>&bull; C claims ultrasound radiation directly ionizes lipids; ultrasound is non-ionizing mechanical radiation and lacks sufficient photon/quantum energy to directly eject electrons.<br>&bull; D invents an electrostatic breakdown mechanism, conflating acoustic cavitation with high-voltage electroporation."
        },
        {
            "q": "As ultrasound frequency increases from 1.0 MHz (Setting 3) to 4.0 MHz (Setting 4), tissue acoustic attenuation increases significantly. What clinical trade-off does this frequency dependence impose on HIFU tumor ablation?",
            "ch": [
                "Higher frequency enhances deep penetration depth but degrades focal resolution",
                "Higher frequency improves focal spatial resolution but limits penetration depth",
                "Lower frequency decreases focal volume size while minimizing thermal absorption",
                "Lower frequency maximizes acoustic scattering while eliminating cavitation risks"
            ],
            "a": 1,
            "e": "<strong>Acoustic frequency trade-off between spatial resolution and penetration depth:</strong> In medical ultrasound, acoustic attenuation increases approximately linearly with frequency ($\\text{attenuation} = \\alpha \\cdot f \\cdot x$). A higher frequency (such as 4.0 MHz) produces shorter wavelengths ($\\lambda = c/f$), enabling tighter diffraction-limited focal spots and superior spatial resolution. However, high-frequency sound waves suffer rapid energy attenuation and exponential intensity loss with tissue depth ($I = I_0 e^{-\\mu x}$), severely restricting their effective penetration depth. Conversely, lower frequencies (such as 1.0 MHz) penetrate deeply into visceral tissues (e.g., deep liver or pelvic lesions) but produce larger focal volumes with reduced precision.<br><br><em>Distractor Traps:</em><br>&bull; A completely reverses the physical trade-off, falsely asserting that high frequency increases penetration and degrades resolution.<br>&bull; C incorrectly claims lower frequency decreases focal volume size; lower frequency yields longer wavelengths and larger diffraction-limited focal spots.<br>&bull; D falsely claims lower frequency eliminates cavitation; as shown by the $MI$ formula ($MI = P_r / \\sqrt{f}$), lower frequencies actually facilitate cavitation because the longer acoustic cycle allows bubbles more time to expand."
        }
    ]
}
