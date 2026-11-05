# generate_full_exam7.py
import json
import re
import os
import sys

def prose_words(html_str):
    text = re.sub(r'<table[\s\S]*?</table>', ' ', html_str)
    text = re.sub(r'<div class="ttl">[\s\S]*?</div>', ' ', text)
    # remove math first
    text = re.sub(r'\$\$[\s\S]*?\$\$', ' ', text)
    text = re.sub(r'\$[^\$]*\$', ' ', text)
    # remove html tags
    text = re.sub(r'<[^>]+>', ' ', text)
    words = [w for w in re.split(r'\s+', text) if len(w.strip()) > 0]
    return len(words)

# =========================================================================
# PASSAGE 1
# =========================================================================
p1 = {
  "id": "exam_cp90_7_p1",
  "sec": "C/P",
  "topic": "Harmonic Standing Waves & Acoustic Intensity in Human Auditory Canal",
  "sheet": 1,
  "label": "Chemical and Physical Foundations of Biological Systems",
  "examId": "cp90_7",
  "passage": """<div class="ttl">Passage 1 (Questions 1&ndash;6)</div>
<p>The human external auditory canal functions as an acoustic resonator that amplifies sound pressure frequencies critical for speech perception. Acoustically, the adult ear canal can be modeled as an open-closed cylindrical acoustic pipe of physical length $L \\approx 2.5\\text{ cm}$ and internal radius $r \\approx 0.4\\text{ cm}$. The lateral canal boundary at the concha opens directly to the ambient atmosphere, establishing an acoustic pressure node (and corresponding air molecule displacement antinode) where acoustic pressure equals atmospheric pressure. Conversely, the medial canal boundary terminates at the compliant, tense tympanic membrane (eardrum), which constrains axial particle motion and establishes an air displacement node (and acoustic pressure antinode).</p>
<p>For an acoustic waveguide closed at one end and open at the other, standing wave resonances satisfy longitudinal boundary conditions exclusively at odd harmonic modes ($n = 1, 3, 5, \\dots$):</p>
$$\\lambda_n = \\frac{4 L_{eff}}{n}, \\quad f_n = \\frac{n v}{4 L_{eff}}$$
<p>where $v$ is the acoustic propagation velocity in warm humid air ($v \\approx 350\\text{ m/s}$ at physiological body temperature, $37^\\circ\\text{C}$), and $L_{eff} = L + 0.6r$ represents the end-corrected acoustic length that accounts for radiation impedance at the open aperture. Sound intensity level $\\beta$ in decibels (dB) quantifies sound intensity $I$ on a logarithmic scale relative to the human auditory threshold reference ($I_0 = 1.0 \\times 10^{-12}\\text{ W/m}^2$):</p>
$$\\beta = 10 \\log_{10}\\left(\\frac{I}{I_0}\\right)$$
<p>Auditory biophysicists evaluated the resonance behavior and tympanic pressure gain of an anatomically contoured ear canal simulator (effective length $L_{eff} = 2.50\\text{ cm}$) coupled to an artificial mastoid and a calibrated subminiature microphone. Pure-tone sound waves of constant incident intensity ($I_{in} = 1.0 \\times 10^{-6}\\text{ W/m}^2$, $\\beta_{in} = 60.0\\text{ dB}$) were delivered at the canal opening across a range of frequencies. Acoustic pressure gain ($\\Delta \\beta = \\beta_{tymp} - \\beta_{in}$) and transmitted tympanic intensity were measured (Table 1).</p>
<table class="tbl">
  <caption>Table 1 Acoustic response, tympanic sound intensity, and resonant gain across stimulus frequencies</caption>
  <thead>
    <tr><th>Stimulus Frequency $f$ (Hz)</th><th>Acoustic Mode ($n$)</th><th>Incident Intensity $I_{in}$ (W/m$^2$)</th><th>Tympanic Intensity $I_{tymp}$ (W/m$^2$)</th><th>Acoustic Gain $\\Delta \\beta$ (dB)</th><th>Tympanic Sound Level $\\beta_{tymp}$ (dB)</th></tr>
  </thead>
  <tbody>
    <tr><td>1000</td><td>Sub-resonant</td><td>1.0 &times; 10<sup>&minus;6</sup></td><td>1.6 &times; 10<sup>&minus;6</sup></td><td>+2.0</td><td>62.0</td></tr>
    <tr><td>2500</td><td>Near fundamental</td><td>1.0 &times; 10<sup>&minus;6</sup></td><td>2.5 &times; 10<sup>&minus;5</sup></td><td>+14.0</td><td>74.0</td></tr>
    <tr><td>3500</td><td>Fundamental ($n = 1$)</td><td>1.0 &times; 10<sup>&minus;6</sup></td><td>1.0 &times; 10<sup>&minus;4</sup></td><td>+20.0</td><td>80.0</td></tr>
    <tr><td>5000</td><td>Inter-harmonic</td><td>1.0 &times; 10<sup>&minus;6</sup></td><td>1.3 &times; 10<sup>&minus;6</sup></td><td>+1.1</td><td>61.1</td></tr>
    <tr><td>7000</td><td>Anti-resonant</td><td>1.0 &times; 10<sup>&minus;6</sup></td><td>7.9 &times; 10<sup>&minus;7</sup></td><td>&minus;1.0</td><td>59.0</td></tr>
    <tr><td>10500</td><td>Third harmonic ($n = 3$)</td><td>1.0 &times; 10<sup>&minus;6</sup></td><td>4.0 &times; 10<sup>&minus;5</sup></td><td>+16.0</td><td>76.0</td></tr>
  </tbody>
</table>""",
  "qs": [
    {
      "q": "At the tympanic membrane boundary during acoustic resonance, how do the air molecule displacement and acoustic pressure fluctuations compare?",
      "ch": [
        "Minimum displacement with maximum pressure fluctuation amplitude",
        "Maximum displacement with minimum pressure fluctuation amplitude",
        "Maximum displacement with maximum pressure fluctuation amplitude",
        "Minimum displacement with minimum pressure fluctuation amplitude"
      ],
      "a": 0,
      "e": "<strong>Boundary conditions in open-closed acoustic pipes:</strong> In an open-closed pipe like the human auditory canal, the closed termination (the tympanic membrane) prevents axial longitudinal translation of air molecules, enforcing a displacement node (zero particle displacement amplitude). Because particles collide against this rigid barrier during each wave cycle, the periodic compression and rarefaction reach their greatest extremes here, creating an acoustic pressure antinode (maximum pressure fluctuation).<br><br><em>Distractor Traps:</em><br>&bull; B describes the open boundary condition at the concha, directionally inverting the node and antinode.<br>&bull; C incorrectly assumes displacement and pressure oscillate in phase with identical antinodal maxima at a closed boundary.<br>&bull; D incorrectly suggests complete acoustic cancellation at the boundary where sound reflection occurs."
    },
    {
      "q": "Given an effective canal length of 2.50 cm and an acoustic velocity of 350 m/s in warm air, what is the fundamental resonant frequency (n = 1) of the simulator?",
      "ch": [
        "1.75 kHz",
        "3.50 kHz",
        "7.00 kHz",
        "14.0 kHz"
      ],
      "a": 1,
      "e": "<strong>Calculation of fundamental frequency for an open-closed pipe:</strong> For a pipe closed at one end, the fundamental harmonic ($n = 1$) wavelength is $\\lambda_1 = 4 L_{eff} = 4(0.0250\\text{ m}) = 0.100\\text{ m}$. Using the wave speed equation $v = f \\lambda$, the resonant frequency is $f_1 = \\frac{v}{4 L_{eff}} = \\frac{350\\text{ m/s}}{0.100\\text{ m}} = 3500\\text{ Hz} = 3.50\\text{ kHz}$. This aligns precisely with the peak resonance measured in Table 1.<br><br><em>Distractor Traps:</em><br>&bull; A computes $f = v / (8 L)$, introducing an extraneous factor of 2 into the denominator.<br>&bull; C computes $f = v / (2 L) = 350 / 0.05 = 7.00\\text{ kHz}$, erroneously applying the open-open pipe formula.<br>&bull; D computes $f = v / L = 350 / 0.025 = 14.0\\text{ kHz}$, failing to account for quarter-wavelength standing wave geometry."
    },
    {
      "q": "Based on Table 1, at the fundamental frequency of 3500 Hz, the acoustic gain is +20.0 dB. This gain corresponds to what fold-increase in acoustic intensity?",
      "ch": [
        "2-fold increase",
        "20-fold increase",
        "100-fold increase",
        "200-fold increase"
      ],
      "a": 2,
      "e": "<strong>Decibel calculation and logarithmic intensity ratios:</strong> Acoustic gain is defined as $\\Delta \\beta = 10 \\log_{10}\\left(\\frac{I_{tymp}}{I_{in}}\\right)$. Substituting $\\Delta \\beta = +20.0\\text{ dB}$: $20.0 = 10 \\log_{10}\\left(\\frac{I_{tymp}}{I_{in}}\\right) \\implies 2.0 = \\log_{10}\\left(\\frac{I_{tymp}}{I_{in}}\\right) \\implies \\frac{I_{tymp}}{I_{in}} = 10^{2.0} = 100$. This matches the experimental values in Table 1, where $I_{tymp} = 1.0 \\times 10^{-4}\\text{ W/m}^2$ is exactly 100 times $I_{in} = 1.0 \\times 10^{-6}\\text{ W/m}^2$.<br><br><em>Distractor Traps:</em><br>&bull; A divides the decibel gain by 10 and confuses the logarithmic exponent with a linear multiplier ($20/10 = 2$).<br>&bull; B assumes the decibel gain scale is linear, treating a 20 dB increase as a 20-fold change.<br>&bull; D multiplies the linear exponent by 100 or uses an erroneous factor of 2."
    },
    {
      "q": "Why does the auditory canal simulator fail to exhibit an acoustic resonance peak at 7000 Hz, despite exhibiting strong peaks at 3500 Hz and 10,500 Hz?",
      "ch": [
        "Acoustic absorption by the eardrum eliminates even-numbered frequencies",
        "Longitudinal waves undergo destructive cancellation at 7000 Hz in air",
        "Sound waves cannot propagate through cylindrical tubes above 5000 Hz",
        "Cylinders closed at one end support only odd harmonic standing waves"
      ],
      "a": 3,
      "e": "<strong>Odd harmonic restriction in open-closed acoustic resonators:</strong> In a pipe with one open end and one closed end, one boundary must be a displacement node and the other a displacement antinode. This asymmetric constraint requires an odd number of quarter-wavelengths to fit inside the pipe: $L = n(\\lambda/4)$ where $n = 1, 3, 5, \\dots$. Even multiples ($n = 2, 4, \\dots$) would require identical boundary states at both ends (either two nodes or two antinodes), which is physically impossible here. Thus, the $n = 2$ mode ($f_2 = 2 \\times 3500 = 7000\\text{ Hz}$) cannot form a standing wave.<br><br><em>Distractor Traps:</em><br>&bull; A erroneously attributes the absence of even modes to material absorption rather than fundamental boundary physics.<br>&bull; B falsely claims air exhibits selective molecular phase cancellation at 7000 Hz.<br>&bull; C is factually incorrect because sound propagates freely through cylindrical pipes across the entire audible spectrum up to 20 kHz."
    },
    {
      "q": "An audiometric point sound source is moved away from a listener so that its distance from the ear canal entrance triples. How does the sound intensity change?",
      "ch": [
        "It decreases by a factor of 9, reducing intensity level by approximately 9.5 dB",
        "It decreases by a factor of 3, reducing intensity level by approximately 4.8 dB",
        "It decreases by a factor of 6, reducing intensity level by approximately 7.8 dB",
        "It decreases by a factor of 27, reducing intensity level by about 14.3 dB"
      ],
      "a": 0,
      "e": "<strong>Inverse-square law and decibel attenuation:</strong> The acoustic intensity emitted by an isotropic point source decreases inversely with the square of the distance: $I = \\frac{P}{4\\pi r^2}$. If distance triples ($r' = 3r$), the intensity drops by a factor of $3^2 = 9$: $I' = \\frac{I}{9}$. The corresponding change in sound intensity level is $\\Delta \\beta = 10 \\log_{10}\\left(\\frac{1}{9}\\right) = -10 \\log_{10}(9) \\approx -10(0.954) = -9.54\\text{ dB}$.<br><br><em>Distractor Traps:</em><br>&bull; B applies a linear $1/r$ dependence instead of the inverse-square law ($10 \\log_{10}(1/3) \\approx -4.8\\text{ dB}$).<br>&bull; C incorrectly assumes intensity is halved or scales with $2r$ ($10 \\log_{10}(1/6) \\approx -7.8\\text{ dB}$).<br>&bull; D applies an inverse-cube law ($1/r^3 = 1/27$), which applies to magnetic dipole fields rather than propagating spherical acoustic radiation."
    },
    {
      "q": "If the ambient temperature inside the canal drops from 37 C to 10 C, what will happen to the speed of sound and the fundamental resonant frequency?",
      "ch": [
        "Speed of sound increases, causing the fundamental frequency to shift higher",
        "Speed of sound decreases, causing the fundamental frequency to shift lower",
        "Speed of sound remains constant, keeping the fundamental frequency unchanged",
        "Speed of sound decreases, causing the fundamental frequency to shift higher"
      ],
      "a": 1,
      "e": "<strong>Temperature dependence of acoustic velocity and resonant frequency:</strong> The speed of sound in an ideal gas depends on absolute temperature: $v = \\sqrt{\\frac{\\gamma R T}{M}}$, where $T$ is in kelvins. As temperature drops from $37^\\circ\\text{C}$ ($310\\text{ K}$) to $10^\\circ\\text{C}$ ($283\\text{ K}$), the average kinetic energy and velocity of air molecules decrease, causing acoustic speed $v$ to decrease. Because the fundamental resonant frequency is directly proportional to speed ($f_1 = \\frac{v}{4 L}$), a decrease in $v$ results in a downward shift in resonant frequency.<br><br><em>Distractor Traps:</em><br>&bull; A claims speed increases with lower temperature, which contradicts kinetic molecular theory for gases.<br>&bull; C incorrectly assumes acoustic velocity is an invariant physical constant independent of thermal state.<br>&bull; D correctly identifies the speed decrease but erroneously inverts the relationship between wave speed and frequency ($f = v / \\lambda$)."
    }
  ]
}

# =========================================================================
# PASSAGE 2
# =========================================================================
p2 = {
  "id": "exam_cp90_7_p2",
  "sec": "C/P",
  "topic": "Doppler Ultrasound Hemodynamics & Pulse-Echo Time-of-Flight",
  "sheet": 2,
  "label": "Chemical and Physical Foundations of Biological Systems",
  "examId": "cp90_7",
  "passage": """<div class="ttl">Passage 2 (Questions 7&ndash;12)</div>
<p>Duplex vascular ultrasonography integrates real-time B-mode brightness imaging with pulsed-wave spectral Doppler velocimetry to assess vascular patency and arterial hemodynamics. In B-mode pulse-echo ranging, a piezoelectric transducer converts electrical pulses into high-frequency longitudinal acoustic compressions ($f_0 = 5.0\\text{ MHz}$). As the ultrasonic pulse traverses tissue layers, reflections occur at acoustic impedance mismatches ($Z = \\rho c$). Assuming an average sound speed in non-fatty soft tissue of $c = 1540\\text{ m/s}$, the round-trip time-of-flight ($\\Delta t$) allows spatial localization of the vessel lumen at depth $d$:</p>
$$d = \\frac{c \\Delta t}{2}$$
<p>When ultrasonic waves encounter moving erythrocytes (red blood cells) with velocity $v$, the backscattered wave exhibits a Doppler frequency shift ($\\Delta f$). The red blood cells first act as moving receivers absorbing incident wave pulses, and subsequently as moving sources re-radiating backscattered ultrasound to the stationary transducer. This dual Doppler interaction yields the clinical Doppler equation:</p>
$$\\Delta f = \\frac{2 f_0 v \\cos\\theta}{c}$$
<p>where $\\theta$ is the insonation angle between the transmitted acoustic beam axis and the blood flow vector.</p>
<p>To calibrate flow quantification and evaluate velocity overestimation artifacts in carotid artery stenosis, vascular specialists deployed a tissue-mimicking flow phantom (attenuation coefficient $\\alpha = 0.5\\text{ dB}/(\\text{cm}\\cdot\\text{MHz})$) with an embedded silicone vessel of variable luminal narrowing. The transducer was operated at $f_0 = 5.0\\text{ MHz}$ at a standardized insonation angle $\\theta = 60.0^\\circ$ ($\\cos 60^\\circ = 0.500$). Measured round-trip delay ($\\Delta t$), observed Doppler shift ($\\Delta f$), and peak systolic velocity ($PSV$) were recorded across healthy and stenotic vessel segments (Table 2).</p>
<table class="tbl">
  <caption>Table 2 Pulse-echo ranging parameters and Doppler velocity metrics in carotid flow phantom</caption>
  <thead>
    <tr><th>Vessel Segment</th><th>Lumen Diameter (mm)</th><th>Pulse-Echo Delay $\\Delta t$ ($\\mu$s)</th><th>Depth $d$ (cm)</th><th>Doppler Shift $\\Delta f$ (kHz)</th><th>Blood Velocity $v$ (m/s)</th><th>Flow Pattern</th></tr>
  </thead>
  <tbody>
    <tr><td>Healthy Segment</td><td>6.0</td><td>26.0</td><td>2.00</td><td>2.60</td><td>0.80</td><td>Laminar</td></tr>
    <tr><td>Mild Stenosis (30%)</td><td>4.2</td><td>26.0</td><td>2.00</td><td>3.64</td><td>1.12</td><td>Laminar</td></tr>
    <tr><td>Moderate Stenosis (50%)</td><td>3.0</td><td>26.0</td><td>2.00</td><td>5.84</td><td>1.80</td><td>Disturbed</td></tr>
    <tr><td>Severe Stenosis (70%)</td><td>1.8</td><td>26.0</td><td>2.00</td><td>9.74</td><td>3.00</td><td>Turbulent jet</td></tr>
    <tr><td>Critical Stenosis (90%)</td><td>0.6</td><td>26.0</td><td>2.00</td><td>16.23</td><td>5.00</td><td>High-velocity jet</td></tr>
  </tbody>
</table>""",
  "qs": [
    {
      "q": "In Table 2, the pulse-echo round-trip delay from the skin surface to the anterior vessel wall is measured at 26.0 us. What is the calculated vessel depth?",
      "ch": [
        "4.00 cm",
        "1.00 cm",
        "2.00 cm",
        "8.00 cm"
      ],
      "a": 2,
      "e": "<strong>Calculation of depth via pulse-echo time-of-flight:</strong> In pulse-echo ultrasound, the transmitted wave must travel to the target boundary and return to the transducer crystal, covering a total distance of $2d$. Thus, $d = \\frac{c \\Delta t}{2}$. Substituting soft tissue sound velocity $c = 1540\\text{ m/s}$ and round-trip delay $\\Delta t = 26.0\\ \\mu\\text{s} = 2.60 \\times 10^{-5}\\text{ s}$: $d = \\frac{(1540\\text{ m/s})(2.60 \\times 10^{-5}\\text{ s})}{2} = \\frac{0.04004\\text{ m}}{2} = 0.02002\\text{ m} \\approx 2.00\\text{ cm}$.<br><br><em>Distractor Traps:</em><br>&bull; A computes $d = c \\Delta t = 4.00\\text{ cm}$, forgetting to divide by 2 for round-trip travel.<br>&bull; B divides the correct depth by 2, introducing an extra factor of one-half.<br>&bull; D multiplies the one-way distance by 4, creating an order-of-magnitude geometric error."
    },
    {
      "q": "Why does the clinical Doppler ultrasound equation contain a factor of 2 in the numerator?",
      "ch": [
        "Transducers contain dual piezoelectric crystals pulsed in rapid alternating phase",
        "Arterial pulse waves bifurcate into two symmetric branch pathways during systole",
        "Acoustic beam power splits equally into reflected and transmitted energy fractions",
        "Erythrocytes shift frequency twice by acting as moving receivers and moving sources"
      ],
      "a": 3,
      "e": "<strong>Physical origin of the factor of two in the Doppler equation:</strong> A two-step Doppler interaction occurs during pulse-echo sonography. First, moving erythrocytes act as a moving receiver intercepting the incident acoustic pulse emitted from the stationary transducer, shifting frequency by $\\Delta f_1 \\approx f_0 \\frac{v \\cos\\theta}{c}$. Second, as the erythrocytes backscatter acoustic wavelets, they behave as a moving source re-radiating sound back to the stationary transducer crystal, shifting frequency a second time by $\\Delta f_2 \\approx f_0 \\frac{v \\cos\\theta}{c}$. The total cumulative Doppler shift detected is the sum of both shifts: $\\Delta f \\approx \\frac{2 f_0 v \\cos\\theta}{c}$.<br><br><em>Distractor Traps:</em><br>&bull; A refers to dual-element continuous wave transducers, which do not explain the kinematic frequency shift derivation.<br>&bull; B confuses anatomical arterial branching with acoustic wave reflection physics.<br>&bull; C describes acoustic reflection coefficients across impedance boundaries, having no bearing on frequency shift."
    },
    {
      "q": "For the severe stenosis segment in Table 2, what peak systolic velocity corresponds to an observed Doppler frequency shift of 9.74 kHz at an insonation angle of 60.0 degrees?",
      "ch": [
        "3.00 m/s",
        "1.50 m/s",
        "6.00 m/s",
        "0.75 m/s"
      ],
      "a": 0,
      "e": "<strong>Velocity calculation from the Doppler shift equation:</strong> Rearranging the Doppler equation for blood velocity gives $v = \\frac{\\Delta f \\cdot c}{2 f_0 \\cos\\theta}$. Substituting $\\Delta f = 9.74\\text{ kHz} = 9740\\text{ Hz}$, $c = 1540\\text{ m/s}$, $f_0 = 5.0\\text{ MHz} = 5.0 \\times 10^6\\text{ Hz}$, and $\\theta = 60.0^\\circ$ (where $\\cos 60.0^\\circ = 0.500$): $v = \\frac{(9740\\text{ Hz})(1540\\text{ m/s})}{2(5.0 \\times 10^6\\text{ Hz})(0.500)} = \\frac{1.49996 \\times 10^7}{5.0 \\times 10^6} \\approx 3.00\\text{ m/s}$.<br><br><em>Distractor Traps:</em><br>&bull; B forgets that $\\cos 60^\\circ = 0.5$ in the denominator, effectively doubling the denominator and halving velocity to $1.50\\text{ m/s}$.<br>&bull; C forgets the factor of 2 in the denominator, computing $v = \\frac{\\Delta f \\cdot c}{f_0 \\cos\\theta} = 6.00\\text{ m/s}$.<br>&bull; D squares the cosine term, halving velocity twice."
    },
    {
      "q": "What clinical artifact or error occurs if a vascular sonographer positions the ultrasound beam exactly perpendicular (90 degrees) to the axis of blood flow?",
      "ch": [
        "Transmitted acoustic pulses undergo severe constructive phase interference",
        "Zero Doppler shift is detected because the cosine of ninety degrees is zero",
        "The detected blood velocity is overestimated by a factor of exactly two",
        "Transducer crystals overheat due to excessive trapped backscattered energy"
      ],
      "a": 1,
      "e": "<strong>Cosine dependency and the ninety-degree Doppler artifact:</strong> The Doppler frequency shift is directly proportional to $\\cos\\theta$. When the acoustic beam is directed perpendicular to vessel flow ($\\theta = 90.0^\\circ$), $\\cos(90.0^\\circ) = 0$. Consequently, $\\Delta f = \\frac{2 f_0 v (0)}{c} = 0\\text{ Hz}$. Even if high-velocity turbulent blood flow is present, the instrument detects no Doppler shift, producing a false-negative clinical reading. For this reason, clinical standards dictate insonation angles between $45^\\circ$ and $60^\\circ$.<br><br><em>Distractor Traps:</em><br>&bull; A describes spatial wave interference, which does not govern Doppler frequency shifts.<br>&bull; C is a directional inversion; velocity is underestimated (reading zero), not overestimated.<br>&bull; D is nonsensical because biological backscatter returns less than 1% of emitted acoustic power."
    },
    {
      "q": "According to fluid dynamics principles, why does blood flow velocity increase dramatically through the stenotic lumen segments in Table 2?",
      "ch": [
        "Blood viscosity drops to zero as fluid enters narrowed vascular sections",
        "Arterial wall compliance expands dramatically to absorb systolic pressure",
        "Volumetric flow rate is conserved, requiring velocity to rise as area drops",
        "Blood density decreases markedly under high shear stress inside the throat"
      ],
      "a": 2,
      "e": "<strong>The continuity equation in cardiovascular hemodynamics:</strong> For an incompressible fluid such as blood flowing through an unbranched vessel segment, the volumetric flow rate ($Q$) must remain constant along the stream: $Q = A_1 v_1 = A_2 v_2$. As arterial plaque narrows the lumen cross-sectional area ($A = \\pi r^2$), the flow velocity must increase inversely with the area ($v \\propto 1/A$) to maintain mass conservation. In Table 2, when lumen diameter drops from 6.0 mm to 1.8 mm (a cross-sectional area reduction of approximately 91%), blood velocity increases from 0.80 m/s to 3.00 m/s.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because blood remains a viscous fluid; shear rate increases near walls.<br>&bull; B describes compliant arterial expansion, which would widen rather than constrict the vessel lumen.<br>&bull; D is incorrect because blood is essentially an incompressible liquid of constant density ($\\rho \\approx 1060\\text{ kg/m}^3$)."
    },
    {
      "q": "Why do clinical vascular exams use 5 to 10 MHz transducers for carotid imaging but switch to 2 to 3.5 MHz transducers for deep abdominal aorta evaluations?",
      "ch": [
        "Lower frequencies produce greater acoustic reflection at muscular boundaries",
        "Higher frequencies travel significantly faster through dense parenchymal tissue",
        "Lower frequencies provide superior axial resolution for resolving minor lesions",
        "Higher frequencies undergo greater tissue attenuation, limiting imaging depth"
      ],
      "a": 3,
      "e": "<strong>Frequency tradeoffs between acoustic attenuation and spatial resolution:</strong> Acoustic attenuation in soft tissue increases linearly with ultrasound frequency (typically $\\alpha \\approx 0.5\\text{--}1.0\\text{ dB}/(\\text{cm}\\cdot\\text{MHz})$) due to thermal absorption and scattering. Consequently, high-frequency sound (5–10 MHz) is attenuated rapidly over short distances, restricting its use to superficial structures like the carotid artery ($d \\approx 2\\text{ cm}$). For deep abdominal organs ($d \\ge 10\\text{--}15\\text{ cm}$), lower frequencies (2–3.5 MHz) must be used to ensure sufficient acoustic penetration, accepting poorer axial resolution ($\text{axial resolution} \\approx \\lambda/2$).<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because reflection magnitude depends on acoustic impedance mismatch ($Z$), not frequency.<br>&bull; B is false because acoustic velocity in soft tissue ($c \\approx 1540\\text{ m/s}$) is essentially independent of frequency.<br>&bull; C directionally inverts resolution; higher frequencies have shorter wavelengths and yield superior resolution."
    }
  ]
}

# =========================================================================
# PASSAGE 3
# =========================================================================
p3 = {
  "id": "exam_cp90_7_p3",
  "sec": "C/P",
  "topic": "Snell's Law & Total Internal Reflection in Fiber-Optic Endoscopes",
  "sheet": 3,
  "label": "Chemical and Physical Foundations of Biological Systems",
  "examId": "cp90_7",
  "passage": """<div class="ttl">Passage 3 (Questions 13&ndash;18)</div>
<p>Medical endoscopy relies on flexible coherent fiber-optic bundles to deliver illumination and transmit high-fidelity optical images from visceral organ lumens. Each individual optical waveguide consists of a cylindrical central core composed of high-purity fused silica glass (refractive index $n_{core}$) surrounded by an outer optical cladding layer of lower refractive index ($n_{clad} < n_{core}$).</p>
<p>When light propagates from a medium of higher refractive index into one of lower refractive index, the transmitted ray bends away from the surface normal according to Snell's law:</p>
$$n_{core} \\sin\\theta_1 = n_{clad} \\sin\\theta_2$$
<p>As the incident angle $\\theta_1$ increases, the angle of refraction $\\theta_2$ approaches $90^\\circ$. At the critical angle $\\theta_c$, the refracted ray propagates parallel to the interface ($\\theta_2 = 90^\\circ$). Because $\\sin 90^\\circ = 1$, the critical angle is given by:</p>
$$\\sin\\theta_c = \\frac{n_{clad}}{n_{core}} \\implies \\theta_c = \\arcsin\\left(\\frac{n_{clad}}{n_{core}}\\right)$$
<p>Total internal reflection (TIR) occurs when the angle of incidence at the core-cladding boundary equals or exceeds $\\theta_c$, trapping light within the core without radiative loss.</p>
<p>At the distal entrance face of the fiber, light enters from an external medium (air, $n_0 = 1.00$) over a conical angular range. The maximum angle of incidence $\\alpha_{max}$ relative to the central fiber axis that permits total internal reflection defines the Numerical Aperture ($NA$):</p>
$$NA = n_0 \\sin\\alpha_{max} = \\sqrt{n_{core}^2 - n_{clad}^2}$$
<p>A larger numerical aperture expands the light-acceptance cone, increasing the illumination flux collected by the fiber bundle.</p>
<p>Biomedical optics engineers characterized five prototype silica fibers fabricated with various fluorosilicate and polymer cladding formulations. Critical angles, numerical apertures, acceptance half-angles, and transmission retention during $180^\\circ$ bending around a 10-mm radius mandrel were quantified (Table 3).</p>
<table class="tbl">
  <caption>Table 3 Optical parameters and transmission performance of prototype endoscopy fibers</caption>
  <thead>
    <tr><th>Fiber Prototype</th><th>Core Index $n_{core}$</th><th>Cladding Index $n_{clad}$</th><th>Critical Angle $\\theta_c$ (deg)</th><th>Numerical Aperture $NA$</th><th>Acceptance Angle $\\alpha_{max}$ (deg)</th><th>Bent Transmission (%)</th></tr>
  </thead>
  <tbody>
    <tr><td>Fib-A</td><td>1.50</td><td>1.48</td><td>80.6</td><td>0.24</td><td>14.1</td><td>68.4%</td></tr>
    <tr><td>Fib-B</td><td>1.55</td><td>1.45</td><td>69.3</td><td>0.55</td><td>33.2</td><td>89.2%</td></tr>
    <tr><td>Fib-C</td><td>1.60</td><td>1.44</td><td>64.2</td><td>0.70</td><td>44.2</td><td>96.5%</td></tr>
    <tr><td>Fib-D</td><td>1.62</td><td>1.40</td><td>59.8</td><td>0.82</td><td>54.7</td><td>98.1%</td></tr>
    <tr><td>Fib-E</td><td>1.46</td><td>1.46</td><td>No TIR</td><td>0.00</td><td>0.0</td><td>0.0%</td></tr>
  </tbody>
</table>""",
  "qs": [
    {
      "q": "When light enters the flat entrance face of Fib-C (n_core = 1.60) from air (n_0 = 1.00) at an incident angle of 30.0 degrees, what is the angle of refraction inside the core?",
      "ch": [
        "18.2 degrees",
        "30.0 degrees",
        "53.1 degrees",
        "48.6 degrees"
      ],
      "a": 0,
      "e": "<strong>Refraction at an air-glass planar interface:</strong> Snell's law governs refraction at the entrance face: $n_0 \\sin\\alpha = n_{core} \\sin\\theta_r$. Substituting $n_0 = 1.00$, $\\alpha = 30.0^\\circ$, and $n_{core} = 1.60$: $1.00 \\sin(30.0^\\circ) = 1.60 \\sin\\theta_r \\implies 1.00(0.500) = 1.60 \\sin\\theta_r \\implies \\sin\\theta_r = \\frac{0.500}{1.60} = 0.3125$. Taking the inverse sine: $\\theta_r = \\arcsin(0.3125) \\approx 18.2^\\circ$. The light ray bends toward the surface normal as it transitions into the optically denser core medium.<br><br><em>Distractor Traps:</em><br>&bull; B assumes light passes undeflected across the dielectric boundary ($\\theta_r = \\alpha$).<br>&bull; C inverts the refractive index ratio, calculating $\\sin\\theta_r = 1.60 \\times 0.500 = 0.800 \\implies \\theta_r \\approx 53.1^\\circ$.<br>&bull; D computes the complement of the angle of incidence ($90^\\circ - 30^\\circ = 60^\\circ$) or makes an inverse trigonometry error."
    },
    {
      "q": "According to Snell's law and Table 3, what is the critical angle for total internal reflection in Fib-C (n_core = 1.60, n_clad = 1.44)?",
      "ch": [
        "44.2 degrees",
        "64.2 degrees",
        "75.8 degrees",
        "90.0 degrees"
      ],
      "a": 1,
      "e": "<strong>Calculation of critical angle for total internal reflection:</strong> Total internal reflection occurs when the refracted ray would propagate at $90^\\circ$. Setting $\\theta_2 = 90.0^\\circ$ in Snell's law: $n_{core} \\sin\\theta_c = n_{clad} \\sin(90.0^\\circ) \\implies \\sin\\theta_c = \\frac{n_{clad}}{n_{core}}$. For Fib-C, $\\sin\\theta_c = \\frac{1.44}{1.60} = 0.900$. Taking the inverse sine gives $\\theta_c = \\arcsin(0.900) \\approx 64.2^\\circ$. At any incidence angle equal to or greater than $64.2^\\circ$, 100% of incident light is reflected internally.<br><br><em>Distractor Traps:</em><br>&bull; A confuses the critical angle $\\theta_c$ with the external acceptance angle $\\alpha_{max} = 44.2^\\circ$.<br>&bull; C computes $\\arcsin(1.44 / 1.50) \\approx 75.8^\\circ$, using the refractive index of Fib-A instead of Fib-C.<br>&bull; D represents grazing incidence along the interface rather than the internal critical angle."
    },
    {
      "q": "Which physical conditions must be simultaneously satisfied for total internal reflection to occur within an optical fiber?",
      "ch": [
        "Light must enter a higher refractive medium at an incident angle less than critical",
        "Light must enter a lower refractive medium at an incident angle less than critical",
        "Light must enter a lower refractive medium at an incident angle exceeding critical",
        "Light must enter a higher refractive medium at an incident angle exceeding critical"
      ],
      "a": 2,
      "e": "<strong>Physical requirements for total internal reflection:</strong> Two criteria must be met concurrently for total internal reflection: (1) The incident wave must travel from a medium of higher refractive index toward a medium of lower refractive index ($n_1 > n_2$), which allows the refracted ray to bend away from the normal; and (2) the angle of incidence $\\theta_1$ must equal or exceed the critical angle ($\\theta_1 \\ge \\theta_c$). If light travels into a denser medium ($n_2 > n_1$), it always bends toward the normal, making total internal reflection mathematically impossible.<br><br><em>Distractor Traps:</em><br>&bull; A fails on both criteria: light cannot undergo TIR when entering a denser medium, nor at sub-critical angles.<br>&bull; B describes standard partial refraction and transmission, which occurs when $\\theta_1 < \\theta_c$.<br>&bull; D incorrectly states that light must travel into a higher refractive index medium."
    },
    {
      "q": "Why does Fib-D (NA = 0.82) exhibit superior illumination coupling efficiency from an endoscopy arc lamp compared to Fib-A (NA = 0.24)?",
      "ch": [
        "Fib-D completely polarizes incoming light, eliminating destructive internal phase shifts",
        "Fib-D accelerates guided photons to a substantially faster group velocity along the core",
        "Fib-D converts infrared thermal wavelengths into visible diagnostic green light rays",
        "Fib-D accepts incident light rays across a substantially wider angular cone of entrance"
      ],
      "a": 3,
      "e": "<strong>Numerical aperture and light collection cone:</strong> The numerical aperture ($NA = \\sqrt{n_{core}^2 - n_{clad}^2}$) defines the light-gathering capacity of an optical fiber by setting the half-angle of the acceptance cone: $\\sin\\alpha_{max} = NA / n_0$. For Fib-D ($NA = 0.82$), $\\alpha_{max} = 54.7^\\circ$, corresponding to a broad solid angle acceptance cone. In contrast, Fib-A ($NA = 0.24$) has $\\alpha_{max} = 14.1^\\circ$, rejecting rays outside this narrow cone. Fib-D captures a vastly larger proportion of diverging light emitted by the illuminator.<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly attributes coupling efficiency to polarization, but endoscopy fibers guide unpolarized light via boundary reflection.<br>&bull; B is false because wave speed is $v = c / n_{core}$; higher core index ($n = 1.62$) actually slows light down ($1.85 \\times 10^8\\text{ m/s}$ vs $2.00 \\times 10^8\\text{ m/s}$).<br>&bull; C describes non-linear upconversion fluorescence, not passive fiber-optic waveguiding."
    },
    {
      "q": "When a flexible endoscope is bent sharply around an anatomical curvature, why does light leakage into the cladding increase?",
      "ch": [
        "Core refractive index increases under stress, raising critical angle to ninety degrees",
        "Mechanical compression permanently destroys silica glass electronic bandgap energy",
        "Incident angles at the outer curved boundary fall below the critical angle threshold",
        "Phase changes produce destructive interference between forward and backward waves"
      ],
      "a": 2,
      "e": "<strong>Bending losses and critical angle violation:</strong> In a straight optical fiber, rays within the acceptance cone strike the core-cladding interface at glancing angles exceeding $\\theta_c$. However, when the fiber is bent around a tight radius, the local surface normal tilts relative to the guided ray path. At the outer curvature radius, the angle of incidence $\\theta$ decreases. When $\\theta < \\theta_c$, total internal reflection fails and light refracts across the interface into the cladding and outer jacket (macrobending loss).<br><br><em>Distractor Traps:</em><br>&bull; A falsely asserts the core index increases enough to force $\\theta_c = 90^\\circ$; photoelastic index changes are negligible compared to geometry changes.<br>&bull; B is incorrect because elastic mechanical bending does not alter electronic bandgap physics in silica.<br>&bull; D confuses geometric leakage across a dielectric boundary with standing wave destructive interference."
    },
    {
      "q": "When monochromatic light (wavelength 600 nm in air) enters the core of Fib-A (n = 1.50), how do its frequency, speed, and wavelength change?",
      "ch": [
        "Frequency remains constant, wave speed decreases, and wavelength decreases",
        "Frequency increases, wave speed remains constant, and wavelength decreases",
        "Frequency decreases, wave speed decreases, and wavelength remains constant",
        "Frequency remains constant, wave speed increases, and wavelength increases"
      ],
      "a": 0,
      "e": "<strong>Wavelength, wave speed, and frequency invariance across media:</strong> The frequency ($f$) of an electromagnetic wave is established by the oscillating source and remains invariant as light crosses any dielectric boundary. Within a medium of refractive index $n = 1.50$, the phase velocity slows to $v = \\frac{c}{n} = \\frac{3.00 \\times 10^8\\text{ m/s}}{1.50} = 2.00 \\times 10^8\\text{ m/s}$. Because wave speed is $v = f \\lambda_n$, the wavelength must compress proportionally: $\\lambda_n = \\frac{\\lambda_0}{n} = \\frac{600\\text{ nm}}{1.50} = 400\\text{ nm}$.<br><br><em>Distractor Traps:</em><br>&bull; B incorrectly posits that frequency varies while speed stays constant across media.<br>&bull; C incorrectly assumes frequency drops while wavelength remains frozen.<br>&bull; D directionally inverts both speed and wavelength changes, describing a transition into a less dense medium ($n < 1$)."
    }
  ]
}

# =========================================================================
# PASSAGE 4
# =========================================================================
p4 = {
  "id": "exam_cp90_7_p4",
  "sec": "C/P",
  "topic": "Thin Lens Equation, Linear Magnification & Ocular Accommodative Power",
  "sheet": 4,
  "label": "Chemical and Physical Foundations of Biological Systems",
  "examId": "cp90_7",
  "passage": """<div class="ttl">Passage 4 (Questions 19&ndash;24)</div>
<p>The human eye functions as a compound converging optical system that refracts incoming light to form real, inverted images on the photoreceptor layer of the retina. Refraction is partitioned between two primary structures: the anterior cornea, which provides fixed refractive power ($P_{cornea} \\approx +40.0\\text{ to }+43.0\\text{ D}$), and the crystalline lens, which provides adjustable power ($P_{lens} \\approx +15.0\\text{ to }+25.0\\text{ D}$) via ciliary muscle contraction. Total ocular optical power $P_{total}$ is measured in diopters ($\\text{D} = \\text{m}^{-1}$), defined as the reciprocal of focal length:</p>
$$P = \\frac{1}{f}$$
<p>For thin lenses in contact, total power is additive: $P_{total} = P_{cornea} + P_{lens}$.</p>
<p>The thin lens equation relates object distance ($d_o$), image distance ($d_i$), and focal length ($f$):</p>
$$\\frac{1}{f} = \\frac{1}{d_o} + \\frac{1}{d_i} \\implies P_{total} = \\frac{1}{d_o} + \\frac{1}{d_i}$$
<p>In an emmetropic eye, the anterior-posterior globe length from the corneal vertex to the retinal fovea is fixed at $d_i \\approx 16.7\\text{ mm}$ ($0.0167\\text{ m}$). When viewing an object at optical infinity ($d_o \\to \\infty$), $1/d_o = 0$, requiring a baseline unaccommodated power $P_{total} = 1/0.0167\\text{ m} \\approx +60.0\\text{ D}$. When viewing nearby objects (e.g., $d_o = 25.0\\text{ cm}$), the ciliary muscle contracts, relaxing the zonular tension on the lens capsule. This allows the lens to assume a more rounded, convex profile, increasing $P_{lens}$ by $+4.0\\text{ D}$ to maintain sharp retinal focus.</p>
<p>Linear magnification ($m$) relates image height ($h_i$) to object height ($h_o$):</p>
$$m = \\frac{h_i}{h_o} = -\\frac{d_i}{d_o}$$
<p>where the negative sign indicates inverted orientation relative to the object.</p>
<p>Ophthalmic bioengineers evaluated optical image formation in an anatomical optomechanical model eye equipped with an artificial cornea ($P_{cornea} = +42.0\\text{ D}$) and an electronically deformable silicone crystalline lens across various object distances (Table 4).</p>
<table class="tbl">
  <caption>Table 4 Accommodative power metrics and image formation parameters in optomechanical eye model</caption>
  <thead>
    <tr><th>Viewing Condition</th><th>Object Distance $d_o$ (m)</th><th>Corneal Power $P_{cornea}$ (D)</th><th>Lens Power $P_{lens}$ (D)</th><th>Total Power $P_{total}$ (D)</th><th>Image Distance $d_i$ (mm)</th><th>Magnification $m$</th></tr>
  </thead>
  <tbody>
    <tr><td>Condition 1 (Infinity)</td><td>&infin;</td><td>+42.0</td><td>+18.0</td><td>+60.0</td><td>16.67</td><td>0.0000</td></tr>
    <tr><td>Condition 2 (Distant)</td><td>5.00</td><td>+42.0</td><td>+18.2</td><td>+60.2</td><td>16.67</td><td>&minus;0.0033</td></tr>
    <tr><td>Condition 3 (Intermediate)</td><td>1.00</td><td>+42.0</td><td>+19.0</td><td>+61.0</td><td>16.67</td><td>&minus;0.0167</td></tr>
    <tr><td>Condition 4 (Near)</td><td>0.50</td><td>+42.0</td><td>+20.0</td><td>+62.0</td><td>16.67</td><td>&minus;0.0333</td></tr>
    <tr><td>Condition 5 (Reading close)</td><td>0.25</td><td>+42.0</td><td>+22.0</td><td>+64.0</td><td>16.67</td><td>&minus;0.0667</td></tr>
  </tbody>
</table>""",
  "qs": [
    {
      "q": "When the model eye focuses parallel light rays from an object at infinity onto the retina at d_i = 16.67 mm, what is its effective focal length and total optical power?",
      "ch": [
        "Focal length of 25.0 mm with optical power of +40.0 D",
        "Focal length of 16.7 mm with optical power of +60.0 D",
        "Focal length of 12.5 mm with optical power of +80.0 D",
        "Focal length of 50.0 mm with optical power of +20.0 D"
      ],
      "a": 1,
      "e": "<strong>Relationship between focal length and dioptric optical power:</strong> When an object is at infinity ($d_o \\to \\infty$), parallel incident rays converge at the focal point of the optical system, meaning image distance equals focal length: $f = d_i = 16.67\\text{ mm} = 0.01667\\text{ m}$. Optical power in diopters is the reciprocal of focal length in meters: $P = \\frac{1}{f} = \\frac{1}{0.01667\\text{ m}} \\approx +60.0\\text{ D}$. This total power represents the sum of corneal power ($+42.0\\text{ D}$) and unaccommodated lens power ($+18.0\\text{ D}$).<br><br><em>Distractor Traps:</em><br>&bull; A accounts only for corneal power ($+42.0\\text{ D} \\approx +40.0\\text{ D}$), omitting the lens contribution.<br>&bull; C calculates $P = 1/0.0125 = +80.0\\text{ D}$, overestimating ocular power.<br>&bull; D accounts only for the unaccommodated crystalline lens power ($+20.0\\text{ D} \\approx 1/0.050\\text{ m}$), omitting the cornea."
    },
    {
      "q": "When shifting focus from infinity to a near reading distance of 25.0 cm, by how many diopters must the crystalline lens increase its optical power?",
      "ch": [
        "+1.0 D",
        "+2.0 D",
        "+8.0 D",
        "+4.0 D"
      ],
      "a": 3,
      "e": "<strong>Accommodative amplitude calculation via the thin lens formula:</strong> At optical infinity, $1/d_o = 0$, so $P_{total} = 1/d_i = +60.0\\text{ D}$. When viewing an object at reading distance $d_o = 25.0\\text{ cm} = 0.25\\text{ m}$, the vergence required from the object is $\\frac{1}{d_o} = \\frac{1}{0.25\\text{ m}} = +4.0\\text{ D}$. To keep image distance fixed at the retina ($d_i = 0.01667\\text{ m}$), total power must become $P_{new} = \\frac{1}{d_o} + \\frac{1}{d_i} = 4.0\\text{ D} + 60.0\\text{ D} = +64.0\\text{ D}$. Because corneal power is fixed ($+42.0\\text{ D}$), the lens must increase from $+18.0\\text{ D}$ to $+22.0\\text{ D}$, an accommodative increase of exactly $+4.0\\text{ D}$.<br><br><em>Distractor Traps:</em><br>&bull; A computes $1 / 1.0\\text{ m} = +1.0\\text{ D}$, which corresponds to viewing at 1 meter.<br>&bull; B computes $1 / 0.50\\text{ m} = +2.0\\text{ D}$, corresponding to an intermediate distance of 50 cm.<br>&bull; C doubles the required accommodation ($2 \\times 4.0\\text{ D} = 8.0\\text{ D}$)."
    },
    {
      "q": "A person views a 1.80-m tall clinical Snellen chart stand positioned 6.00 m from the eye. Assuming d_i = 16.67 mm, what is the height of the retinal image?",
      "ch": [
        "-5.00 mm (inverted)",
        "+5.00 mm (upright)",
        "-15.0 mm (inverted)",
        "+15.0 mm (upright)"
      ],
      "a": 0,
      "e": "<strong>Linear magnification and image height calculation:</strong> Linear magnification is given by $m = -\\frac{d_i}{d_o}$. Converting units: $d_i = 16.67\\text{ mm} = 0.01667\\text{ m}$, and $d_o = 6.00\\text{ m}$. Thus, $m = -\\frac{0.01667\\text{ m}}{6.00\\text{ m}} = -0.002778$. The image height is $h_i = m \\times h_o = (-0.002778)(1.80\\text{ m}) = -0.00500\\text{ m} = -5.00\\text{ mm}$. The negative sign indicates an inverted retinal image.<br><br><em>Distractor Traps:</em><br>&bull; B forgets the negative sign in the linear magnification equation ($m = -d_i/d_o$), falsely stating the image is upright.<br>&bull; C divides $1.80\\text{ m}$ by $6.00\\text{ m}$ without multiplying by $d_i$, or makes an order-of-magnitude arithmetic error.<br>&bull; D omits the negative sign and introduces a 3-fold calculation error."
    },
    {
      "q": "Which statement correctly characterizes the real image formed on the retina by the eye's converging optical refracting system?",
      "ch": [
        "Real, upright, and magnified relative to the original physical object",
        "Virtual, upright, and reduced relative to the original physical object",
        "Real, inverted, and reduced relative to the original physical object",
        "Virtual, inverted, and magnified relative to the original physical object"
      ],
      "a": 2,
      "e": "<strong>Optics of retinal image formation by converging lenses:</strong> The ocular optical system (cornea and crystalline lens) functions as a positive converging lens system. For any real object located beyond the focal point ($d_o > f$), light rays physically converge at the retinal plane ($d_i > 0$), forming a real image. Because light rays cross the principal optical axis, the formed image is inverted ($m < 0$). Furthermore, because the object distance ($d_o \\ge 25\\text{ cm}$) vastly exceeds the image distance ($d_i \\approx 1.7\\text{ cm}$), $|m| = d_i/d_o \\ll 1$, meaning the image is substantially reduced in size.<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly identifies the image as upright and magnified; real images from single converging lenses are inverted when $d_o > f$.<br>&bull; B confuses retinal images with virtual images formed by magnifying glasses or diverging lenses.<br>&bull; D combines contradictory optical terms; virtual images cannot be cast onto a physical screen like the retina."
    },
    {
      "q": "During physiological accommodation for near vision, what biomechanical events occur in the ciliary body and crystalline lens?",
      "ch": [
        "Ciliary muscle relaxes, zonular tension increases, and the lens flattens",
        "Ciliary muscle contracts, zonular tension decreases, and the lens rounds",
        "Ciliary muscle contracts, zonular tension increases, and the lens flattens",
        "Ciliary muscle relaxes, zonular tension decreases, and the lens rounds"
      ],
      "a": 1,
      "e": "<strong>Helmholtz mechanism of ocular accommodation:</strong> The ciliary body contains a circular sphincter-like smooth muscle surrounding the crystalline lens. In the resting, unaccommodated state for distant vision, the ciliary muscle is relaxed, which holds the suspensory zonular fibers under high tension, pulling the elastic lens capsule taut and flat (lower curvature, lower power). For near vision accommodation, the ciliary muscle contracts, moving the ciliary ring inward toward the optical axis. This relaxes tension on the zonules, allowing the intrinsic elasticity of the lens capsule to bulge into a more steeply curved, convex shape (smaller radius of curvature, shorter focal length, higher optical power).<br><br><em>Distractor Traps:</em><br>&bull; A describes distant vision relaxation, which flattens the lens and decreases power.<br>&bull; C incorrectly assumes ciliary contraction pulls the zonules tighter, confusing a sphincter muscle with a radial muscle.<br>&bull; D pairs muscle relaxation with decreased tension, which contradicts annular sphincter geometry."
    },
    {
      "q": "The convex anterior corneal surface acts as a reflective spherical mirror with radius R = 7.8 mm. What type of reflected image does it form?",
      "ch": [
        "Real, inverted, and magnified image located 3.9 mm in front of cornea",
        "Real, inverted, and reduced image located 7.8 mm behind the cornea",
        "Virtual, inverted, and magnified image located 7.8 mm behind cornea",
        "Virtual, upright, and reduced image located 3.9 mm behind the cornea"
      ],
      "a": 3,
      "e": "<strong>Convex spherical mirror reflection and Purkinje image I:</strong> The outward-curving anterior corneal tear film functions as a convex spherical mirror. By sign convention, the center of curvature lies behind the reflecting surface, giving a negative radius ($R = -7.8\\text{ mm}$) and negative focal length: $f = \\frac{R}{2} = -\\frac{7.8\\text{ mm}}{2} = -3.9\\text{ mm}$. A convex mirror always forms an image with $d_i = \\left(\\frac{1}{f} - \\frac{1}{d_o}\\right)^{-1} < 0$. Because $d_i$ is negative, the image is virtual, located behind the corneal vertex. Linear magnification is $m = -d_i/d_o > 0$ and $|m| < 1$, producing an upright, reduced reflection (clinically observed as Purkinje image I during keratometry).<br><br><em>Distractor Traps:</em><br>&bull; A describes image formation by a concave mirror ($f > 0$), which can form real inverted images in front of the mirror.<br>&bull; B confuses convex mirrors with converging optical elements and sets focal length equal to $R$ instead of $R/2$.<br>&bull; C claims the virtual image is inverted and magnified, violating the universal optical behavior of convex mirrors."
    }
  ]
}

# =========================================================================
# PASSAGE 5
# =========================================================================
p5 = {
  "id": "exam_cp90_7_p5",
  "sec": "C/P",
  "topic": "Refractive Vision Defects: Myopia, Hyperopia, Astigmatism & Presbyopia",
  "sheet": 5,
  "label": "Chemical and Physical Foundations of Biological Systems",
  "examId": "cp90_7",
  "passage": """<div class="ttl">Passage 5 (Questions 25&ndash;30)</div>
<p>Ametropias (optical refractive errors) develop when the focal length of the resting ocular refracting elements fails to coincide with the axial length of the eye globe. In an emmetropic eye, parallel rays from distant objects converge precisely onto the foveal retina ($d_i \\approx 23.5\\text{ mm}$ total globe length).</p>
<p>In <strong>axial myopia</strong> (nearsightedness), excessive anterior-posterior elongation of the globe causes parallel rays from distant objects to focus anterior to the retina, producing a blurred circle of confusion. The myopic eye possesses a finite far point ($FP$); objects beyond this point cannot be brought into focus. Optical correction requires a <strong>diverging (concave) lens</strong> of negative power ($P < 0$). To view objects at optical infinity ($d_o \\to \\infty$), the corrective lens must form a virtual image of the distant object at the patient's far point:</p>
$$f_{lens} = -FP \\implies P_{lens} = -\\frac{1}{FP}$$
<p>where $FP$ is measured in meters from the lens.</p>
<p>In <strong>hyperopia</strong> (farsightedness), the eyeball is axially too short, or the refractive power of the cornea and lens is insufficient, causing parallel rays to converge toward a virtual focal point behind the retina. The near point ($NP$) recedes beyond the standard reading distance ($d_{near} = 0.25\\text{ m}$). Hyperopia is corrected using a <strong>converging (convex) lens</strong> of positive power ($P > 0$) that forms a virtual image of an object at $0.25\\text{ m}$ at the patient's actual near point:</p>
$$P_{lens} = \\frac{1}{d_{near}} - \\frac{1}{NP} = 4.0\\text{ D} - \\frac{1}{NP}$$
<p>In <strong>astigmatism</strong>, non-spherical (toric) corneal curvature produces unequal refractive powers along orthogonal meridians, corrected by cylindrical lenses. In <strong>presbyopia</strong>, age-related nuclear sclerosis and biochemical stiffening of crystalline lens fibers reduce accommodative amplitude without changing globe length, requiring positive reading power additions.</p>
<p>An ophthalmology clinic analyzed ocular biometric measurements across 5 adult patient groups presenting for refractive evaluation (Table 5).</p>
<table class="tbl">
  <caption>Table 5 Ocular biometric parameters, focal metrics, and refractive lens corrections</caption>
  <thead>
    <tr><th>Patient Group</th><th>Axial Length (mm)</th><th>Far Point $FP$ (m)</th><th>Near Point $NP$ (cm)</th><th>Corneal Astigmatism (D)</th><th>Lens Correction (Diopters)</th><th>Corrective Lens Geometry</th></tr>
  </thead>
  <tbody>
    <tr><td>Emmetropia</td><td>23.5</td><td>&infin;</td><td>25</td><td>0.00</td><td>0.00 D</td><td>None (Plano)</td></tr>
    <tr><td>Axial Myopia</td><td>25.5</td><td>0.50</td><td>15</td><td>0.00</td><td>&minus;2.00 D</td><td>Concave (diverging)</td></tr>
    <tr><td>Severe Hyperopia</td><td>21.5</td><td>&infin;</td><td>100</td><td>0.00</td><td>+3.00 D</td><td>Convex (converging)</td></tr>
    <tr><td>Presbyopia (Age 55)</td><td>23.5</td><td>&infin;</td><td>67</td><td>0.00</td><td>+2.50 D add</td><td>Convex reading add</td></tr>
    <tr><td>Corneal Astigmatism</td><td>23.5</td><td>&infin;</td><td>25</td><td>2.50 at 90&deg;</td><td>&minus;2.50 Cyl at 180&deg;</td><td>Toric cylindrical</td></tr>
  </tbody>
</table>""",
  "qs": [
    {
      "q": "For the axial myopic patient in Table 5 with a far point of 0.50 m, what focal length and optical power must a corrective spectacle lens possess?",
      "ch": [
        "Focal length of +0.50 m and optical power of +2.00 D",
        "Focal length of +0.25 m and optical power of +4.00 D",
        "Focal length of -0.50 m and optical power of -2.00 D",
        "Focal length of -0.25 m and optical power of -4.00 D"
      ],
      "a": 2,
      "e": "<strong>Spectacle lens power calculation for myopia:</strong> To correct myopia, a diverging lens is placed before the eye so that light coming from an object at infinity ($d_o \\to \\infty$) forms a virtual image at the patient's far point ($d_i = -FP = -0.50\\text{ m}$). Applying the thin lens formula: $P_{lens} = \\frac{1}{f} = \\frac{1}{d_o} + \\frac{1}{d_i} = 0 + \\frac{1}{-0.50\\text{ m}} = -2.00\\text{ D}$. The negative sign indicates a concave, diverging lens with focal length $f = -0.50\\text{ m}$.<br><br><em>Distractor Traps:</em><br>&bull; A prescribes a converging convex lens ($+2.00\\text{ D}$), which would increase ocular vergence and worsen myopic blurring.<br>&bull; B prescribes a $+4.00\\text{ D}$ convex lens, confusing the near point with the far point.<br>&bull; D doubles the required power to $-4.00\\text{ D}$ ($f = -0.25\\text{ m}$), overcorrecting the refractive error."
    },
    {
      "q": "In an uncorrected hyperopic patient viewing a nearby book at 25 cm without accommodation, where does the refracted light converge relative to the retina?",
      "ch": [
        "Directly on the fovea because the eye's axial length is elongated",
        "In front of the retina because the cornea refracts light too strongly",
        "On the optic disc, bypassing the retinal fovea and photoreceptors",
        "Behind the retina because the eye's converging power is insufficient"
      ],
      "a": 3,
      "e": "<strong>Ray convergence in uncorrected hyperopia:</strong> In hyperopia (farsightedness), the eyeball is axially too short relative to the optical power of the cornea and lens, or the refractive power is insufficient to focus diverging rays from nearby objects. Rays from an object at 25 cm diverge strongly; because the uncorrected hyperopic optical system cannot provide enough positive vergence, the rays reach the retinal surface before converging to a focal point, striking the retina as a blurred blur circle while converging toward a virtual focal point behind the retina.<br><br><em>Distractor Traps:</em><br>&bull; A describes an emmetropic eye or an accommodated eye, while falsely asserting the hyperopic eye is elongated.<br>&bull; B describes myopia, where rays converge in front of the retina.<br>&bull; C describes an anatomical blind spot misalignment rather than an axial optical focus error."
    },
    {
      "q": "The hyperopic patient in Table 5 has a near point of 100 cm (1.00 m). What lens power is required to enable clear reading at 25 cm (0.25 m)?",
      "ch": [
        "+3.00 D",
        "+5.00 D",
        "-3.00 D",
        "-1.00 D"
      ],
      "a": 0,
      "e": "<strong>Calculation of corrective lens power for hyperopia:</strong> The corrective lens must take an object located at standard reading distance ($d_o = 0.25\\text{ m}$) and form an upright virtual image at the patient's actual near point ($d_i = -NP = -1.00\\text{ m}$). Applying the thin lens formula: $P = \\frac{1}{d_o} + \\frac{1}{d_i} = \\frac{1}{0.25\\text{ m}} + \\frac{1}{-1.00\\text{ m}} = +4.00\\text{ D} - 1.00\\text{ D} = +3.00\\text{ D}$. A converging convex lens of $+3.00\\text{ D}$ provides the supplementary vergence needed.<br><br><em>Distractor Traps:</em><br>&bull; B adds the two values ($4.00 + 1.00 = +5.00\\text{ D}$), failing to use the negative sign for a virtual image ($d_i = -1.00\\text{ m}$).<br>&bull; C prescribes a diverging lens of $-3.00\\text{ D}$, which would push the near point even further away.<br>&bull; D accounts only for the near point vergence ($-1.00\\text{ D}$), omitting the required reading distance."
    },
    {
      "q": "How does the underlying pathophysiological mechanism of presbyopia differ fundamentally from that of axial hyperopia?",
      "ch": [
        "Presbyopia involves progressive globe shortening due to posterior scleral shrinkage",
        "Presbyopia stems from loss of lens compliance rather than an abnormally short globe",
        "Presbyopia is caused by excessive ciliary muscle hypercontraction and spasm",
        "Presbyopia results from asymmetric corneal toricity along the vertical meridian"
      ],
      "a": 1,
      "e": "<strong>Physiological basis of presbyopia vs anatomical hyperopia:</strong> Axial hyperopia is a structural refractive error present from birth or youth caused by an anatomically short eyeball ($< 23.5\\text{ mm}$). In contrast, presbyopia is an age-related physiological degeneration that affects individuals regardless of axial length (axial length remains normal, e.g. 23.5 mm in Table 5). Presbyopia results from non-enzymatic cross-linking of crystallin proteins, nuclear sclerosis, and decreased elasticity of the lens capsule, preventing the lens from deforming into a rounded convex shape during ciliary muscle contraction.<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly claims presbyopia shortens the physical eye globe.<br>&bull; C claims ciliary muscle spasm occurs, whereas presbyopia involves loss of lens tissue responsiveness despite normal ciliary effort.<br>&bull; D describes corneal astigmatism, not presbyopia."
    },
    {
      "q": "Why does a cylindrical lens correct corneal astigmatism without distorting image focus along the patient's normal perpendicular meridian?",
      "ch": [
        "Cylindrical lenses rotate the polarization axis of light by ninety degrees",
        "Cylindrical lenses filter out blue wavelengths that cause severe chromatism",
        "Cylindrical lenses possess curvature and refractive power in only one meridian",
        "Cylindrical lenses act as concave mirrors that invert retinal image wavefronts"
      ],
      "a": 2,
      "e": "<strong>Optics of cylindrical lenses in astigmatism correction:</strong> Astigmatism arises from an aspherical (toric) cornea that has different radii of curvature along orthogonal axes (like the side of a football). A cylindrical lens is formed by slicing a cylinder parallel to its axis: it has curvature and optical power along the meridian perpendicular to its cylinder axis, but zero curvature and plano power parallel to its cylinder axis. By aligning the cylindrical power axis with the defective corneal meridian, the refractive error is neutralized without altering the refraction of the normal perpendicular axis.<br><br><em>Distractor Traps:</em><br>&bull; A confuses cylindrical refractive lenses with polarizing filters.<br>&bull; B describes chromatic filtering, having no relevance to astigmatic meridian focus.<br>&bull; D confuses transmitting lenses with reflective mirrors and misstates wave inversion."
    },
    {
      "q": "When a -2.00 D concave spectacle lens corrects myopia for a distant star, what type of image does the lens form at the patient's far point?",
      "ch": [
        "A real, inverted image located 50 cm behind the spectacle lens",
        "A real, upright image located 50 cm in front of the spectacle lens",
        "A virtual, inverted image located 50 cm behind the spectacle lens",
        "A virtual, upright image located 50 cm in front of the spectacle lens"
      ],
      "a": 3,
      "e": "<strong>Virtual image formation by diverging corrective lenses:</strong> A diverging (concave) lens ($P = -2.00\\text{ D}$, $f = -0.50\\text{ m} = -50\\text{ cm}$) refracts incoming parallel rays from an object at infinity ($d_o \\to \\infty$) so that they diverge as if they originated from the anterior focal point. Because the refracted rays diverge on the exit side, they never physically converge; their virtual backward projections intersect at $d_i = -50\\text{ cm}$ in front of the lens (on the same side as the object). All virtual images produced by single thin lenses from real objects are upright ($m = -d_i/d_o > 0$).<br><br><em>Distractor Traps:</em><br>&bull; A describes a real inverted image formed by a converging convex lens behind the lens.<br>&bull; B is contradictory because real images form on the side opposite the object (behind a transmitting lens).<br>&bull; C incorrectly asserts the virtual image is inverted and located behind the lens."
    }
  ]
}

# =========================================================================
# PASSAGE 6
# =========================================================================
p6 = {
  "id": "exam_cp90_7_p6",
  "sec": "C/P",
  "topic": "Single-Slit & Double-Slit Diffraction Patterns in Biomedical Lasers",
  "sheet": 6,
  "label": "Chemical and Physical Foundations of Biological Systems",
  "examId": "cp90_7",
  "passage": """<div class="ttl">Passage 6 (Questions 31&ndash;36)</div>
<p>Laser wave optics provides high-precision diagnostic tools in flow cytometry, cell sizing, and optical micromanipulation. When a monochromatic, spatially coherent laser beam encounters a narrow aperture or a single biological cell suspended in a fluidic stream, wavelets emanating from across the wavefront interfere constructively and destructively, producing characteristic diffraction fringe patterns on a projection detector screen.</p>
<p>In <strong>Fraunhofer single-slit diffraction</strong>, dark fringe minima arise where wavelets from different sections of an aperture of width $a$ cancel destructively. The angular position $\\theta$ of the $m$-th order dark fringe satisfies:</p>
$$a \\sin\\theta = m \\lambda \\quad (m = \\pm 1, \\pm 2, \\pm 3, \\dots)$$
<p>where $\\lambda$ is laser wavelength and $m \\neq 0$. Under the paraxial small-angle approximation ($\\sin\\theta \\approx y/L$), the linear distance $y_m$ from the central bright peak to the $m$-th minimum on a screen at distance $L$ is:</p>
$$y_m = \\frac{m \\lambda L}{a}$$
<p>The bright central maximum spans between the first minima on either side ($m = \\pm 1$), giving it a total physical width twice that of any secondary bright fringe:</p>
$$W_{central} = 2 y_1 = \\frac{2 \\lambda L}{a}$$
<p>In <strong>Young's double-slit interference</strong>, two identical parallel slits separated by center-to-center distance $d$ act as coherent secondary sources. Bright constructive interference maxima occur where optical path length differences equal integer multiples of wavelength ($d \\sin\\theta = m \\lambda$), producing evenly spaced fringes separated by:</p>
$$\\Delta y = \\frac{\\lambda L}{d}$$
<p>According to Babinet's principle, the diffraction envelope generated by an opaque microscopic obstacle (such as an erythrocyte of diameter $d_{cell}$) is identical in fringe spacing to that generated by an aperture of equal dimensions.</p>
<p>Bioengineers calibrated a laser diffraction cytometer using He-Ne red ($\\lambda = 632.8\\text{ nm}$) and diode green ($\\lambda = 532.0\\text{ nm}$) lasers across precision slits, double apertures, and fixed human erythrocytes on a detector screen placed at $L = 1.50\\text{ m}$ (Table 6).</p>
<table class="tbl">
  <caption>Table 6 Laser diffraction and interference metrics across optical configurations and cell targets</caption>
  <thead>
    <tr><th>Optical Setup</th><th>Laser Wavelength $\\lambda$ (nm)</th><th>Slit Width $a$ ($\\mu$m)</th><th>Slit Spacing $d$ ($\\mu$m)</th><th>First Minimum $y_1$ (mm)</th><th>Fringe Spacing $\\Delta y$ (mm)</th><th>Central Width $W_{central}$ (mm)</th></tr>
  </thead>
  <tbody>
    <tr><td>Setup 1 (Single Slit)</td><td>632.8</td><td>25.0</td><td>&mdash;</td><td>38.0</td><td>&mdash;</td><td>76.0</td></tr>
    <tr><td>Setup 2 (Single Slit)</td><td>632.8</td><td>50.0</td><td>&mdash;</td><td>19.0</td><td>&mdash;</td><td>38.0</td></tr>
    <tr><td>Setup 3 (Single Slit)</td><td>532.0</td><td>50.0</td><td>&mdash;</td><td>16.0</td><td>&mdash;</td><td>32.0</td></tr>
    <tr><td>Setup 4 (Double Slit)</td><td>632.8</td><td>10.0</td><td>100.0</td><td>&mdash;</td><td>9.50</td><td>190.0 (envelope)</td></tr>
    <tr><td>Setup 5 (Double Slit)</td><td>532.0</td><td>10.0</td><td>100.0</td><td>&mdash;</td><td>7.98</td><td>159.6 (envelope)</td></tr>
    <tr><td>Setup 6 (Erythrocyte disc)</td><td>632.8</td><td>7.5 ($d_{cell}$)</td><td>&mdash;</td><td>126.6</td><td>&mdash;</td><td>253.1</td></tr>
  </tbody>
</table>""",
  "qs": [
    {
      "q": "In Setup 1 of Table 6, a single slit of width 25.0 um is illuminated by a 632.8-nm laser with L = 1.50 m. What is the distance from the central axis to the first dark minimum?",
      "ch": [
        "38.0 mm",
        "19.0 mm",
        "76.0 mm",
        "9.50 mm"
      ],
      "a": 0,
      "e": "<strong>Calculation of first minimum in single-slit diffraction:</strong> In Fraunhofer single-slit diffraction, the first destructive interference minimum occurs when $a \\sin\\theta = 1 \\cdot \\lambda$. Using the small-angle approximation $\\sin\\theta \\approx \\frac{y_1}{L}$, this yields $y_1 = \\frac{\\lambda L}{a}$. Substituting $\\lambda = 632.8\\text{ nm} = 6.328 \\times 10^{-7}\\text{ m}$, $L = 1.50\\text{ m}$, and $a = 25.0\\ \\mu\\text{m} = 2.50 \\times 10^{-5}\\text{ m}$: $y_1 = \\frac{(6.328 \\times 10^{-7}\\text{ m})(1.50\\text{ m})}{2.50 \\times 10^{-5}\\text{ m}} = \\frac{9.492 \\times 10^{-7}}{2.50 \\times 10^{-5}} = 0.03797\\text{ m} \\approx 38.0\\text{ mm}$.<br><br><em>Distractor Traps:</em><br>&bull; B doubles the slit width in the denominator or computes $y_1$ for $a = 50.0\\ \\mu\\text{m}$ ($19.0\\text{ mm}$).<br>&bull; C computes the total central maximum width $W = 2y_1 = 76.0\\text{ mm}$ rather than the distance from the central axis to the first minimum.<br>&bull; D divides by 4, confusing the single-slit formula with double-slit fringe spacing."
    },
    {
      "q": "When the slit width is doubled from 25.0 um (Setup 1) to 50.0 um (Setup 2) while keeping wavelength and screen distance constant, how does the central maximum change?",
      "ch": [
        "Central maximum width doubles and peak light intensity decreases by half",
        "Central maximum width halves and peak light intensity increases notably",
        "Central maximum width remains unchanged but interference fringes disappear",
        "Central maximum width quadruples and diffracted light shifts toward blue"
      ],
      "a": 1,
      "e": "<strong>Inverse relationship between slit width and diffraction spreading:</strong> The physical width of the central diffraction peak is $W_{central} = \\frac{2 \\lambda L}{a}$. Because slit width $a$ appears in the denominator, the angular spread of the diffraction pattern is inversely proportional to $a$. When $a$ is doubled from $25.0\\ \\mu\\text{m}$ to $50.0\\ \\mu\\text{m}$, the central peak width is cut in half (from $76.0\\text{ mm}$ to $38.0\\text{ mm}$). Furthermore, a wider slit transmits more total optical power while concentrating that energy into a narrower spatial area, significantly increasing peak central intensity.<br><br><em>Distractor Traps:</em><br>&bull; A directly inverts the geometric relationship, claiming width scales proportionally with $a$.<br>&bull; C incorrectly assumes diffraction spread is independent of aperture dimensions.<br>&bull; D confuses slit width variation with Doppler wavelength shifts."
    },
    {
      "q": "In Setup 4, laser light passes through double slits separated by d = 100 um with L = 1.50 m. What is the linear spacing between adjacent bright interference fringes?",
      "ch": [
        "38.0 mm",
        "19.0 mm",
        "9.50 mm",
        "4.75 mm"
      ],
      "a": 2,
      "e": "<strong>Young's double-slit fringe spacing calculation:</strong> In double-slit interference, constructive interference peaks occur when $d \\sin\\theta = m \\lambda$. The linear spacing $\\Delta y$ between adjacent bright maxima ($m$ and $m+1$) is given by $\\Delta y = \\frac{\\lambda L}{d}$. Substituting $\\lambda = 632.8\\text{ nm} = 6.328 \\times 10^{-7}\\text{ m}$, $L = 1.50\\text{ m}$, and slit separation $d = 100.0\\ \\mu\\text{m} = 1.00 \\times 10^{-4}\\text{ m}$: $\\Delta y = \\frac{(6.328 \\times 10^{-7}\\text{ m})(1.50\\text{ m})}{1.00 \\times 10^{-4}\\text{ m}} = \\frac{9.492 \\times 10^{-7}}{1.00 \\times 10^{-4}} = 9.492 \\times 10^{-3}\\text{ m} \\approx 9.50\\text{ mm}$.<br><br><em>Distractor Traps:</em><br>&bull; A uses the single-slit width $a = 25.0\\ \\mu\\text{m}$ instead of slit spacing $d = 100.0\\ \\mu\\text{m}$.<br>&bull; B uses $a = 50.0\\ \\mu\\text{m}$ instead of $d = 100.0\\ \\mu\\text{m}$.<br>&bull; D introduces an extraneous factor of 2 in the denominator, computing $\\Delta y / 2$."
    },
    {
      "q": "Comparing Setup 2 (632.8 nm) and Setup 3 (532.0 nm), why does the green laser produce a narrower central maximum than the red laser across an identical slit?",
      "ch": [
        "Green photons have lower energy and therefore undergo greater refraction",
        "Green light has a longer wavelength, compressing the diffraction angles",
        "Green light propagates slower in air, reducing wavefront phase divergence",
        "Green light has a shorter wavelength, causing destructive interference earlier"
      ],
      "a": 3,
      "e": "<strong>Wavelength dependency of diffraction spreading:</strong> The position of the first diffraction minimum is $y_1 = \\frac{\\lambda L}{a}$. Diffraction spreading is directly proportional to wavelength $\\lambda$. Green light has a shorter wavelength ($\\\\lambda = 532.0\\text{ nm}$) than red light ($\\lambda = 632.8\\text{ nm}$). Because wavelets from opposite edges of the slit accumulate a phase difference of $\\lambda / 2$ over a smaller angular deviation, destructive interference occurs at a smaller angle $\\theta$, compressing the central maximum width from $38.0\\text{ mm}$ down to $32.0\\text{ mm}$ (a ratio of $532.0 / 632.8 \\approx 0.84$).<br><br><em>Distractor Traps:</em><br>&bull; A falsely asserts green photons have lower energy; by $E = hc/\\lambda$, shorter wavelength means higher photon energy.<br>&bull; B falsely claims green light has a longer wavelength than red light.<br>&bull; C incorrectly assumes light propagation velocity in air varies substantially across the visible spectrum."
    },
    {
      "q": "According to Babinet's principle, why can the forward diffraction pattern produced by an individual erythrocyte (Setup 6) accurately determine its cellular diameter?",
      "ch": [
        "An opaque obstacle produces an identical diffraction pattern to an aperture of equal size",
        "Cellular cytoplasm acts as a diverging concave lens that magnifies interference fringe spacing",
        "Erythrocyte membrane hemoglobin undergoes stimulated emission when excited by 633 nm lasers",
        "Biological cell membranes completely absorb all diffracted light except at normal incidence"
      ],
      "a": 0,
      "e": "<strong>Babinet's principle and optical particle sizing:</strong> Babinet's principle states that the Fraunhofer diffraction pattern produced by an opaque planar obstacle (such as an individual circular red blood cell disk) is identical in angular intensity distribution and fringe geometry (outside the unscattered central beam) to that produced by a clear aperture of identical shape and dimensions. Thus, an erythrocyte with diameter $d_{cell} = 7.5\\ \\mu\\text{m}$ produces diffraction minima according to $d_{cell} \\sin\\theta = m \\lambda$, allowing precise cell sizing in flow cytometers.<br><br><em>Distractor Traps:</em><br>&bull; B incorrectly treats the opaque biconcave cell as a transparent diverging lens.<br>&bull; C describes laser gain media and stimulated emission, which do not occur in physiological hemoglobin.<br>&bull; D falsely claims biological membranes absorb light completely."
    },
    {
      "q": "In a single-slit diffraction experiment, what is the optical path length difference between wavelets from the top edge and the center of the slit at the first dark minimum?",
      "ch": [
        "Exactly one full wavelength, producing total constructive wave interference",
        "Exactly one-half wavelength, producing complete destructive wave cancellation",
        "Exactly one-fourth wavelength, causing a ninety-degree wave phase deviation",
        "Exactly zero path difference, because paraxial laser rays travel along identical paths"
      ],
      "a": 1,
      "e": "<strong>Wavelet pairing and destructive interference in single-slit diffraction:</strong> In Fraunhofer single-slit diffraction, the condition for the first dark minimum across a slit of width $a$ is $a \\sin\\theta = \\lambda$. To understand why darkness occurs, we divide the slit into two equal halves of width $a/2$. For every wavelet originating from a point in the top half of the slit, there is a corresponding wavelet originating from a point exactly $a/2$ lower in the bottom half. The path length difference between this paired set of wavelets is $\\Delta x = \\frac{a}{2} \\sin\\theta = \\frac{1}{2}(a \\sin\\theta) = \\frac{\\lambda}{2}$. A path difference of $\\lambda/2$ corresponds to a phase difference of $\\pi$ radians ($180^\\circ$), causing complete pair-wise destructive interference.<br><br><em>Distractor Traps:</em><br>&bull; A identifies the path difference between the extreme top and bottom edges ($a \\sin\\theta = \\lambda$), but fails to recognize that wavelets from the center are shifted by $\\lambda/2$.<br>&bull; C proposes $\\lambda/4$, which produces a $90^\\circ$ quadrature phase shift rather than complete cancellation.<br>&bull; D describes the central bright maximum ($\\\\theta = 0$) where path difference is zero."
    }
  ]
}

# =========================================================================
# PASSAGE 7
# =========================================================================
p7 = {
  "id": "exam_cp90_7_p7",
  "sec": "C/P",
  "topic": "Circular Dichroism (CD) & FRET Spectroscopy of Protein Folding",
  "sheet": 7,
  "label": "Chemical and Physical Foundations of Biological Systems",
  "examId": "cp90_7",
  "passage": """<div class="ttl">Passage 7 (Questions 37&ndash;42)</div>
<p>Biophysical spectroscopy provides sensitive structural and dynamic probes of macromolecular folding and conformational transitions. Two complementary spectroscopic techniques widely employed in structural biology are Circular Dichroism (CD) and F&ouml;rster Resonance Energy Transfer (FRET).</p>
<p><strong>Circular Dichroism</strong> measures the differential absorption of left-circularly polarized ($A_L$) and right-circularly polarized ($A_R$) light by optically active, chiral chromophores: $\\Delta A = A_L - A_R$. In proteins, peptide backbone amide bonds absorb in the far-UV spectrum ($190\\text{--}260\\text{ nm}$). Secondary structural motifs display pathognomonic CD spectral signatures when expressed as mean residue molar ellipticity ($[\\theta]$, $\\text{deg}\\cdot\\text{cm}^2/\\text{dmol}$). An $\\alpha$-helix exhibits two characteristic negative minima at $208\\text{ nm}$ ($\\pi \\to \\pi^*$ transition) and $222\\text{ nm}$ ($n \\to \\pi^*$ transition), with a strong positive band near $193\\text{ nm}$. Antiparallel $\\beta$-sheets display a single negative minimum at $218\\text{ nm}$ and a positive peak near $195\\text{ nm}$, whereas disordered random coils exhibit a pronounced negative minimum near $198\\text{ nm}$.</p>
<p><strong>F&ouml;rster Resonance Energy Transfer (FRET)</strong> is a non-radiative process in which an excited donor fluorophore transfers energy through long-range dipole-dipole resonance coupling to an acceptor fluorophore without photon emission. FRET efficiency ($E$) depends inversely on the sixth power of the donor-acceptor separation distance ($r$):</p>
$$E = \\frac{R_0^6}{R_0^6 + r^6}$$
<p>where $R_0$ is the F&ouml;rster distance (typically $2\\text{--}6\\text{ nm}$) at which energy transfer is exactly $50\\%$ ($E = 0.50$). This steep $r^{-6}$ dependency enables FRET to serve as a "spectroscopic ruler" capable of detecting sub-nanometer conformational shifts.</p>
<p>Biochemists investigated the calcium-dependent activation and domain collapse of human calmodulin (CaM). Recombinant CaM was engineered with an EDANS donor fluorophore at its N-terminus and a DABCYL acceptor chromophore at its C-terminus ($R_0 = 4.0\\text{ nm}$). Molar ellipticity at $222\\text{ nm}$, calculated $\\alpha$-helical content, donor fluorescence intensity ($I_D$), and FRET efficiency were monitored across various calcium concentrations, target peptide binding, and thermal unfolding (Table 7).</p>
<table class="tbl">
  <caption>Table 7 CD spectroscopic parameters and FRET conformational metrics of calmodulin</caption>
  <thead>
    <tr><th>Conformational State</th><th>Free [Ca$^{2+}$] ($\\mu$M)</th><th>Target Peptide</th><th>$[\\theta]_{222}$ ($10^3\\ \\text{deg}\\cdot\\text{cm}^2/\\text{dmol}$)</th><th>Calculated $\\alpha$-Helix (%)</th><th>FRET Efficiency $E$</th><th>Inter-terminal Distance $r$ (nm)</th></tr>
  </thead>
  <tbody>
    <tr><td>Apo-CaM (unliganded)</td><td>0.0</td><td>Absent</td><td>&minus;14.2</td><td>34%</td><td>0.12</td><td>5.6</td></tr>
    <tr><td>Low Calcium</td><td>0.5</td><td>Absent</td><td>&minus;19.5</td><td>48%</td><td>0.28</td><td>4.7</td></tr>
    <tr><td>Calcium-Saturated</td><td>100.0</td><td>Absent</td><td>&minus;26.0</td><td>65%</td><td>0.50</td><td>4.0</td></tr>
    <tr><td>Target-Bound Complex</td><td>100.0</td><td>Present (M13)</td><td>&minus;31.2</td><td>78%</td><td>0.89</td><td>2.8</td></tr>
    <tr><td>Thermally Denatured ($90^\\circ$C)</td><td>100.0</td><td>Absent</td><td>&minus;3.1</td><td>6%</td><td>0.02</td><td>7.7</td></tr>
  </tbody>
</table>""",
  "qs": [
    {
      "q": "A researcher isolates a novel bacterial toxin and observes negative CD ellipticity peaks at 208 nm and 222 nm, along with a positive peak at 193 nm. What secondary structure predominates?",
      "ch": [
        "Parallel beta-pleated sheets",
        "Disordered random coil loops",
        "Right-handed alpha-helices",
        "Triple-helical collagen ropes"
      ],
      "a": 2,
      "e": "<strong>Circular dichroism spectral signatures of protein secondary structures:</strong> The far-UV CD spectrum of peptide backbones provides direct structural identification. An $\\alpha$-helix is uniquely characterized by two distinct negative minima at $208\\text{ nm}$ (originating from the amide $\\pi \\to \\pi^*$ parallel electronic transition) and $222\\text{ nm}$ (from the $n \\to \\pi^*$ transition), alongside a strong positive Cotton effect near $193\\text{ nm}$. This signature reflects the regular helical arrangement of chiral peptide backbone hydrogen bonds.<br><br><em>Distractor Traps:</em><br>&bull; A exhibits a single negative minimum near $218\\text{ nm}$ and a positive peak near $195\\text{ nm}$.<br>&bull; B exhibits a prominent negative minimum near $198\\text{ nm}$ with near-zero ellipticity above $215\\text{ nm}$.<br>&bull; D exhibits a characteristic weak negative band near $200\\text{ nm}$ and a small positive peak near $228\\text{ nm}$."
    },
    {
      "q": "In Table 7, when calmodulin binds saturating calcium, the inter-terminal distance r equals the Förster radius R_0 (4.0 nm). What is the theoretical FRET efficiency E?",
      "ch": [
        "0.10 (10%)",
        "0.25 (25%)",
        "0.95 (95%)",
        "0.50 (50%)"
      ],
      "a": 3,
      "e": "<strong>Definition and calculation of Förster radius in FRET:</strong> The Förster distance $R_0$ is fundamentally defined as the donor-acceptor separation distance at which the resonance energy transfer efficiency is exactly $50\\%$ ($E = 0.50$). Mathematically, substituting $r = R_0$ into the FRET efficiency equation yields: $E = \\frac{R_0^6}{R_0^6 + r^6} = \\frac{R_0^6}{R_0^6 + R_0^6} = \\frac{R_0^6}{2 R_0^6} = \\frac{1}{2} = 0.50$. This confirms the measured experimental value in Table 7 for the calcium-saturated state.<br><br><em>Distractor Traps:</em><br>&bull; A confuses $E = 0.50$ with the unliganded apo-state efficiency ($0.12$).<br>&bull; B evaluates $\\frac{1}{2^2} = 0.25$, erroneously applying an inverse-square relationship.<br>&bull; C evaluates the target-bound complex efficiency ($0.89 \\approx 0.95$) instead of $r = R_0$."
    },
    {
      "q": "When calmodulin unfolds from its calcium-saturated state (r = 4.0 nm) to a denatured state where r = 8.0 nm, by what factor does the rate of dipole-dipole energy transfer decrease?",
      "ch": [
        "64-fold",
        "16-fold",
        "32-fold",
        "8-fold"
      ],
      "a": 0,
      "e": "<strong>Sixth-power distance dependency of dipole-dipole energy transfer:</strong> Non-radiative Förster energy transfer occurs via dipole-dipole coupling, which scales inversely with the sixth power of distance: $k_{FRET} \\propto \\frac{1}{r^6}$. When the distance between fluorophores doubles from $4.0\\text{ nm}$ to $8.0\\text{ nm}$ (a 2-fold expansion, $r_2 / r_1 = 2$), the rate of energy transfer decreases by a factor of: $\\left(\\frac{r_2}{r_1}\\right)^6 = 2^6 = 64$. This sixth-power sensitivity makes FRET an exceptionally sensitive molecular distance gauge.<br><br><em>Distractor Traps:</em><br>&bull; B computes $2^4 = 16$, erroneously applying a fourth-power relationship.<br>&bull; C computes $2^5 = 32$, missing one factor of 2.<br>&bull; D computes $2^3 = 8$, erroneously applying an inverse-cube relationship."
    },
    {
      "q": "Why do alpha-helical protein backbones exhibit circular dichroism, whereas a racemic mixture of free D- and L-alanine does not?",
      "ch": [
        "Racemic mixtures absorb infrared rather than ultraviolet electromagnetic radiation",
        "Alpha-helices possess asymmetric chiral dipoles that absorb circularly polarized light unequally",
        "Free amino acids lack covalent peptide bonds required to polarize incident visible light",
        "Racemic alanine solutions undergo total internal reflection, preventing light transmission"
      ],
      "a": 1,
      "e": "<strong>Biophysical origin of optical activity and circular dichroism:</strong> Circular dichroism requires molecular chirality (optical asymmetry). In an $\\alpha$-helix, chiral L-amino acids are organized into a regular right-handed helical geometry. This asymmetric spatial distribution of peptide bond electric dipole transition moments creates differential absorption of left- versus right-circularly polarized light ($\\Delta A = A_L - A_R \\neq 0$). In contrast, a racemic mixture contains equal numbers of D- and L-enantiomers whose opposite chiral rotations cancel out identically, resulting in net zero circular dichroism ($\\Delta A = 0$).<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because amino acids absorb UV light via electronic transitions regardless of chirality.<br>&bull; C is false because individual chiral amino acids do exhibit CD; it is the equal racemic cancellation that zeroes the signal.<br>&bull; D is nonsensical because dilute solutions transmit light rather than undergoing TIR."
    },
    {
      "q": "Based on Table 7, what structural transition occurs when the calmodulin-calcium complex binds its target skeletal muscle myosin light-chain kinase peptide (M13)?",
      "ch": [
        "Alpha-helices unfold into beta-sheets, causing donor and acceptor to move apart",
        "Calmodulin completely denatures, decreasing FRET efficiency and molar ellipticity",
        "The protein forms an extended rod, increasing inter-terminal distance to 6 nm",
        "Helical content increases and the terminal domains collapse around the target"
      ],
      "a": 3,
      "e": "<strong>Structural interpretation of CD and FRET data:</strong> In Table 7, the transition from calcium-saturated CaM to target-bound CaM causes molar ellipticity at $222\\text{ nm}$ to become more negative (from $-26.0$ to $-31.2 \\times 10^3\\text{ deg}\\cdot\\text{cm}^2/\\text{dmol}$), indicating an increase in $\\alpha$-helical content from $65\\%$ to $78\\%$. Simultaneously, the FRET efficiency rises dramatically from $0.50$ to $0.89$, and the calculated distance between the N- and C-terminal fluorophores contracts from $4.0\\text{ nm}$ down to $2.8\\text{ nm}$. This confirms that calmodulin wraps its globular domains tightly around the target peptide.<br><br><em>Distractor Traps:</em><br>&bull; A contradicts the data; helical content increases and inter-terminal distance contracts rather than expands.<br>&bull; B describes thermal denaturation, which causes loss of ellipticity ($-3.1$) and loss of FRET ($0.02$).<br>&bull; C describes an extension transition, which would decrease FRET efficiency rather than increase it to 0.89."
    },
    {
      "q": "Which physical requirement is strictly necessary for efficient non-radiative Förster resonance energy transfer between a donor and an acceptor fluorophore?",
      "ch": [
        "Overlap between donor emission spectrum and acceptor absorption spectrum",
        "Emission of an intermediate ultraviolet photon by the excited donor molecule",
        "Direct covalent bonding and continuous electron orbital overlap between tags",
        "Inter-fluorophore separation distances exceeding fifty nanometers in solution"
      ],
      "a": 0,
      "e": "<strong>Spectral overlap requirement for non-radiative resonance energy transfer:</strong> For Förster dipole-dipole resonance energy transfer to take place, the quantum transition energy of donor de-excitation must match the transition energy of acceptor excitation. This resonance condition is experimentally satisfied when the fluorescence emission spectrum of the donor fluorophore significantly overlaps with the ground-state absorbance (excitation) spectrum of the acceptor chromophore (spectral overlap integral $J$). Energy is transferred non-radiatively through electromagnetic dipole coupling without the intermediate generation of an actual photon.<br><br><em>Distractor Traps:</em><br>&bull; B contradicts the definition of FRET; it is an entirely non-radiative resonance process involving no photon emission.<br>&bull; C describes Dexter electron exchange transfer, which requires orbital contact ($< 1\\text{ nm}$), whereas FRET operates via long-range dipoles ($1\\text{--}10\\text{ nm}$).<br>&bull; D is incorrect because FRET efficiency is virtually zero at distances exceeding $10\\text{ nm}$ due to the $r^{-6}$ dependency."
    }
  ]
}

# =========================================================================
# STANDALONE DISCRETES (Q43-Q52)
# =========================================================================
disc = {
  "id": "exam_cp90_7_disc",
  "sec": "C/P",
  "topic": "C/P Standalone Discrete Questions",
  "sheet": 8,
  "label": "Chemical and Physical Foundations of Biological Systems",
  "examId": "cp90_7",
  "passage": """<div class=\"ttl\">Item Set (Questions 43&ndash;52)</div>\n<p><strong>Directions:</strong> Questions 43&ndash;52 are standalone questions that are not based on a passage. Select the single best answer to each question.</p>""",
  "qs": [
    {
      "d": True,
      "q": "When white light passes through a flint glass prism, violet light (400 nm) is refracted through a greater angle of deviation than red light (700 nm). What explains this optical dispersion?",
      "ch": [
        "Glass has a higher refractive index for shorter wavelengths, causing violet light to travel slower and refract more",
        "Red light possesses greater photon energy than violet light, allowing it to resist refractive bending at the interface",
        "Flint glass selectively absorbs violet light, converting electromagnetic wave energy into non-radiative phonon modes",
        "Violet light undergoes constructive interference within the glass, increasing its speed relative to incoming red light"
      ],
      "a": 0,
      "e": "<strong>Prismatic dispersion and wavelength-dependent refractive index (Topic 333):</strong> In transparent dielectric media such as glass, optical dispersion occurs because the refractive index $n(\\lambda)$ depends on wavelength. For normal dispersion, the refractive index increases as wavelength decreases ($n_{violet} > n_{red}$). Because phase velocity is $v = c / n$, violet light travels slower through the glass than red light. By Snell's law ($n_1 \\sin\\theta_1 = n_2 \\sin\\theta_2$), a larger refractive index results in greater angular deviation at both the entering and exiting faces of the prism, bending violet light more sharply toward the prism base.<br><br><em>Distractor Traps:</em><br>&bull; B is false because photon energy is $E = hc/\\lambda$; violet photons have greater energy than red photons, and energy does not govern classical refraction.<br>&bull; C describes optical absorption rather than elastic refractive dispersion.<br>&bull; D falsely claims violet light travels faster, which violates $v = c/n$ when $n_{violet} > n_{red}$."
    },
    {
      "d": True,
      "q": "Chromatic aberration in a single converging glass lens causes color fringing in microscopy. Which color light focuses closest to the lens, and how is this defect corrected?",
      "ch": [
        "Red light focuses closest to the lens; the aberration is corrected by adding a planar dielectric beam splitter",
        "Blue light focuses closest to the lens; the aberration is corrected by combining it with a diverging lens doublet",
        "Green light focuses closest to the lens; the aberration is corrected by placing an opaque spatial aperture filter",
        "Violet light focuses farthest from lens; the aberration is corrected by coating surfaces with magnesium fluoride"
      ],
      "a": 1,
      "e": "<strong>Chromatic aberration and achromatic doublets (Topic 340):</strong> Chromatic aberration arises from dispersion in the lens material. Because glass has a higher index of refraction for short wavelengths ($n_{blue} > n_{red}$), blue light bends more sharply than red light according to the Lensmaker's equation: $\\frac{1}{f} = (n - 1)\\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right)$. A higher $n$ yields a shorter focal length ($f_{blue} < f_{red}$), causing blue light to converge closer to the lens. To eliminate this defect, optical systems employ an achromatic doublet, combining a low-dispersion crown glass converging lens with a high-dispersion flint glass diverging lens to bring both colors to a common focus.<br><br><em>Distractor Traps:</em><br>&bull; A directionally inverts focal length, claiming red light focuses closer than blue light.<br>&bull; C describes spatial aperture filtering, which reduces spherical aberration and depth of field but cannot correct wavelength dispersion.<br>&bull; D claims violet light focuses farthest (a directional inversion) and confuses achromatic correction with anti-reflective coating."
    },
    {
      "d": True,
      "q": "In an X-ray crystallography experiment on a crystallized metalloenzyme, first-order constructive interference (n = 1) is observed at a glancing angle of theta = 30.0 degrees using monochromatic X-rays of wavelength lambda = 0.154 nm. What is the interplanar lattice spacing d of the crystal planes?",
      "ch": [
        "0.308 nm",
        "0.077 nm",
        "0.154 nm",
        "0.616 nm"
      ],
      "a": 2,
      "e": "<strong>Bragg's law of X-ray diffraction (Topic 343):</strong> Constructive interference from parallel atomic crystal planes occurs when the path difference between reflected X-rays equals an integer multiple of wavelengths: $n \\lambda = 2 d \\sin\\theta$. Solving for interplanar lattice spacing $d$: $d = \\frac{n \\lambda}{2 \\sin\\theta}$. Substituting $n = 1$, $\\lambda = 0.154\\text{ nm}$, and $\\theta = 30.0^\\circ$ (where $\\sin 30.0^\\circ = 0.500$): $d = \\frac{1(0.154\\text{ nm})}{2(0.500)} = \\frac{0.154\\text{ nm}}{1.000} = 0.154\\text{ nm}$. This corresponds to $1.54\\text{ \\AA}$, typical for bond and lattice spacings in macromolecular crystals.<br><br><em>Distractor Traps:</em><br>&bull; A forgets the factor of 2 in the denominator, computing $d = \\lambda / \\sin\\theta = 0.308\\text{ nm}$.<br>&bull; B divides by an extraneous factor of 2, computing $0.154 / 2 = 0.077\\text{ nm}$.<br>&bull; D multiplies by 4, confusing the Bragg equation with an open-closed pipe quarter-wavelength relationship."
    },
    {
      "d": True,
      "q": "An unpolarized laser beam with initial intensity I_0 = 120 W/m^2 passes through an ideal linear polarizer, and then through a second polarizer oriented at 60.0 degrees relative to the first. What is the final transmitted light intensity?",
      "ch": [
        "30.0 W/m^2",
        "15.0 W/m^2",
        "45.0 W/m^2",
        "60.0 W/m^2"
      ],
      "a": 1,
      "e": "<strong>Intensity transmission via Malus's law and unpolarized light rule (Topic 344):</strong> When unpolarized light passes through the first linear polarizer, half of the incident intensity is transmitted, and the light becomes linearly polarized: $I_1 = \\frac{I_0}{2} = \\frac{120\\text{ W/m}^2}{2} = 60.0\\text{ W/m}^2$. When this linearly polarized light encounters the second polarizer (analyzer) oriented at angle $\\theta = 60.0^\\circ$, the transmitted intensity is governed by Malus's law: $I_2 = I_1 \\cos^2\\theta$. Substituting $I_1 = 60.0\\text{ W/m}^2$ and $\\cos(60.0^\\circ) = 0.500$: $I_2 = (60.0\\text{ W/m}^2)(0.500)^2 = (60.0)(0.250) = 15.0\\text{ W/m}^2$.<br><br><em>Distractor Traps:</em><br>&bull; A forgets to square the cosine term, computing $I_2 = 60 \\times 0.50 = 30.0\\text{ W/m}^2$.<br>&bull; C computes $I_2 = I_1 \\sin^2(60^\\circ) = 60 \\times 0.75 = 45.0\\text{ W/m}^2$.<br>&bull; D gives the intensity after the first polarizer ($60.0\\text{ W/m}^2$), failing to account for the analyzer."
    },
    {
      "d": True,
      "q": "In confocal laser scanning fluorescence microscopy, what optical mechanism enables optical sectioning and high axial resolution in thick biological specimens?",
      "ch": [
        "A high-power pulsed infrared laser that completely eliminates out-of-focus fluorophore photobleaching",
        "A pair of polarizing prisms that cancel out all unpolarized fluorescence emissions from the sample",
        "A conjugate detector pinhole aperture that spatially rejects out-of-focus background fluorescence",
        "A cylindrical lens array that refocuses scattered fluorescent photons directly onto the objective"
      ],
      "a": 2,
      "e": "<strong>Optical sectioning and spatial filtering by confocal pinholes (Topic 346):</strong> In conventional widefield fluorescence microscopy, illumination excites fluorophores throughout the entire specimen thickness, and out-of-focus light blurs the focal plane. Confocal microscopy achieves optical sectioning by placing an adjustable spatial pinhole aperture conjugate to the specimen focal plane in front of the photomultiplier tube (PMT). In-focus fluorescence rays converge precisely through the pinhole to reach the detector, whereas out-of-focus rays originating from above or below the focal plane are defocused and physically blocked by the pinhole edges.<br><br><em>Distractor Traps:</em><br>&bull; A describes multiphoton excitation microscopy, not confocal pinhole spatial filtering.<br>&bull; B confuses spatial pinhole filtering with polarization cross-filtering.<br>&bull; D describes light sheet illumination optics rather than confocal descanning detection."
    },
    {
      "d": True,
      "q": "Total Internal Reflection Fluorescence (TIRF) microscopy restricts fluorophore excitation to within 100 nm of the coverslip interface because:",
      "ch": [
        "Only fluorophores directly bound to glass can absorb propagating transverse electromagnetic waves",
        "Refraction at the coverslip surface focuses the laser into a diffraction-limited pinhole spot",
        "Fluorescent antibodies undergo stimulated emission depletion when illuminated by angled lasers",
        "Total internal reflection generates a non-propagating evanescent wave that decays exponentially"
      ],
      "a": 3,
      "e": "<strong>Evanescent wave generation in TIRF microscopy (Topic 348):</strong> When a laser beam propagating through a high-index glass coverslip ($n_1 \\approx 1.52$) strikes an aqueous biological medium ($n_2 \\approx 1.33$) at an incident angle exceeding the critical angle ($\\theta > \\theta_c$), total internal reflection occurs. Although all energy is reflected, boundary conditions require continuity of the electromagnetic field across the interface, generating an evanescent electromagnetic wave. This evanescent field propagates along the interface but decays exponentially with penetration depth: $I(z) = I_0 e^{-z / d_p}$, where $d_p \\approx 100\\text{ nm}$. As a result, fluorophores deeper in the cell cytoplasm are not excited, eliminating background fluorescence.<br><br><em>Distractor Traps:</em><br>&bull; A falsely asserts only glass-bound fluorophores can absorb light.<br>&bull; B describes standard lens focusing, which does not produce sub-diffraction axial confinement.<br>&bull; C describes STED (Stimulated Emission Depletion) super-resolution microscopy, not TIRF."
    },
    {
      "d": True,
      "q": "Firefly luciferase bioluminescence differs fundamentally from green fluorescent protein (GFP) fluorescence because the bioluminescent emission of light:",
      "ch": [
        "Derives from chemical oxidation of luciferin with ATP rather than absorption of an excitation photon",
        "Requires continuous excitation by high-energy ultraviolet radiation to sustain electronic singlet states",
        "Involves non-radiative dipole-dipole energy transfer to an acceptor chromophore via Förster coupling",
        "Operates as an endergonic process that cools surrounding tissue by absorbing thermal kinetic energy"
      ],
      "a": 0,
      "e": "<strong>Thermodynamic and photophysical distinction between bioluminescence and fluorescence (Topic 350):</strong> Fluorescence (such as that of GFP) is a photoluminescent process wherein a fluorophore absorbs an incoming excitation photon of higher energy (shorter wavelength) and subsequently re-emits a photon of lower energy (longer wavelength) after vibrational relaxation. Bioluminescence, in contrast, requires zero excitation photons. Instead, the enzyme luciferase catalyzes an exergonic biochemical reaction combining D-luciferin, ATP, and $\\text{O}_2$ via an adenylylated intermediate to produce electronically excited oxyluciferin, which emits a visible photon upon relaxation to its ground state.<br><br><em>Distractor Traps:</em><br>&bull; B describes photoluminescence (fluorescence/phosphorescence), which contradicts photon-independent bioluminescence.<br>&bull; C describes FRET (Förster Resonance Energy Transfer), which transfers energy between two fluorophores.<br>&bull; D falsely characterizes bioluminescence as endergonic and cooling; it is an exergonic chemical reaction with an exceptionally high quantum yield."
    },
    {
      "d": True,
      "q": "In a medical Nd:YAG surgical laser, what physical condition within the active gain medium is fundamentally required to sustain coherent stimulated emission?",
      "ch": [
        "Complete thermal equilibrium where ground-state atoms outnumber atoms in all higher excited energy levels",
        "A population inversion where more active atoms occupy an excited meta-stable state than lower energy levels",
        "Total destructive interference of all emitted photons to prevent excessive heating of the laser cavity",
        "Dielectric breakdown of the laser rod material to release free electrons into conduction band orbitals"
      ],
      "a": 1,
      "e": "<strong>Population inversion and stimulated emission physics (Topic 352):</strong> Under normal thermal equilibrium governed by the Boltzmann distribution ($N_2 / N_1 = e^{-\\Delta E / k_B T}$), the lower ground state always has a higher population than an excited state ($N_1 > N_2$). Incident photons are therefore predominantly absorbed. To achieve laser amplification (Light Amplification by Stimulated Emission of Radiation), external optical or electrical energy ('pumping') must create a population inversion ($N_2 > N_1$), where more atoms reside in a long-lived meta-stable excited state than in the ground state. An incident photon then triggers stimulated de-excitation, producing identical, in-phase, coherent photons.<br><br><em>Distractor Traps:</em><br>&bull; A describes thermal equilibrium, where absorption dominates and laser amplification cannot occur.<br>&bull; C claims destructive interference occurs; lasers require constructive interference inside the resonator cavity.<br>&bull; D describes dielectric laser breakdown and damage, which destroys the crystalline gain medium."
    },
    {
      "d": True,
      "q": "During clinical Doppler sonography of the femoral artery, if the transducer insonation angle relative to blood flow changes from 60 degrees to 30 degrees at constant blood velocity, what happens to the detected Doppler shift?",
      "ch": [
        "It decreases by a factor of 0.50 because smaller angles reduce ultrasound beam penetration",
        "It remains completely unchanged because blood velocity and center frequency are constant",
        "It increases by a factor of 1.73 because the cosine of the insonation angle increases",
        "It doubles exactly because the insonation angle is reduced by fifty percent in radians"
      ],
      "a": 2,
      "e": "<strong>Cosine dependency of Doppler frequency shift (Topic 356):</strong> The Doppler frequency shift is directly proportional to the cosine of the insonation angle: $\\Delta f = \\frac{2 f_0 v \\cos\\theta}{c}$. Evaluating the cosines: at $\\theta_1 = 60.0^\\circ$, $\\cos(60.0^\\circ) = 0.500$. At $\\theta_2 = 30.0^\\circ$, $\\cos(30.0^\\circ) = \\frac{\\sqrt{3}}{2} \\approx 0.866$. The ratio of the detected Doppler shifts is $\\frac{\\Delta f_{30}}{\\Delta f_{60}} = \\frac{\\cos 30.0^\\circ}{\\cos 60.0^\\circ} = \\frac{0.866}{0.500} = 1.732$. Thus, decreasing the insonation angle from $60^\\circ$ to $30^\\circ$ increases the detected Doppler frequency shift by a factor of approximately 1.73.<br><br><em>Distractor Traps:</em><br>&bull; A directionally inverts the cosine trend, claiming the shift decreases.<br>&bull; B ignores the angular dependency of the Doppler equation, assuming shift depends only on speed.<br>&bull; D assumes a linear relationship with angle ($\\Delta f \\propto \\theta$), computing a 2-fold change because $60/30 = 2$, ignoring non-linear trigonometric cosine behavior."
    },
    {
      "d": True,
      "q": "A clinical pulse oximeter non-invasively calculates arterial oxygen saturation (SpO_2) by comparing optical absorbance at 660 nm and 940 nm because:",
      "ch": [
        "Oxygenated hemoglobin absorbs 660 nm light more strongly than deoxygenated hemoglobin",
        "Deoxygenated hemoglobin absorbs both 660 nm and 940 nm light equally due to heme symmetry",
        "Oxygenated hemoglobin completely reflects 940 nm light while transmitting all 660 nm light",
        "Deoxygenated hemoglobin absorbs 660 nm red light more strongly than 940 nm infrared light"
      ],
      "a": 3,
      "e": "<strong>Differential optical absorption of hemoglobin in pulse oximetry (Topic 360):</strong> Pulse oximetry utilizes spectrophotometric absorption differences between oxyhemoglobin ($\\text{HbO}_2$) and deoxyhemoglobin ($\\text{Hb}$). Deoxygenated hemoglobin exhibits a significantly higher molar extinction coefficient at $660\\text{ nm}$ (visible red light) than at $940\\text{ nm}$. Conversely, oxygenated hemoglobin absorbs more strongly at $940\\text{ nm}$ (near-infrared light) than at $660\\text{ nm}$. By calculating the ratio of pulsatile (arterial) absorbances at these two wavelengths ($R = \\frac{A_{660}}{A_{940}}$), the microchip accurately calculates the percentage of arterial hemoglobin saturation ($\\text{SpO}_2$).<br><br><em>Distractor Traps:</em><br>&bull; A directionally inverts the absorbance profiles; deoxy-Hb absorbs 660 nm more strongly than oxy-Hb.<br>&bull; B is false because deoxy-Hb has an asymmetric electronic structure with distinct absorbances at 660 nm and 940 nm.<br>&bull; C incorrectly asserts hemoglobin reflects light rather than absorbing it."
    }
  ]
}

exam_cp90_7 = [p1, p2, p3, p4, p5, p6, p7, disc]

# Build exam_cp60_7
# Contains Passages 1 through 5 (with ids exam_cp60_7_p1 to p5, examId: cp60_7)
# + first 3 discrete questions from exam_cp90_7_disc (id: exam_cp60_7_disc, examId: cp60_7)
exam_cp60_7 = []
for p in [p1, p2, p3, p4, p5]:
    p_copy = json.loads(json.dumps(p))
    p_copy["id"] = p_copy["id"].replace("cp90_7", "cp60_7")
    p_copy["examId"] = "cp60_7"
    exam_cp60_7.append(p_copy)

disc_60_copy = json.loads(json.dumps(disc))
disc_60_copy["id"] = "exam_cp60_7_disc"
disc_60_copy["examId"] = "cp60_7"
disc_60_copy["qs"] = disc_60_copy["qs"][:3]
exam_cp60_7.append(disc_60_copy)

# =========================================================================
# VALIDATIONS
# =========================================================================
print("=== VALIDATING EXAM_CP90_7 ===")
assert len(exam_cp90_7) == 8, f"Expected 8 sections, got {len(exam_cp90_7)}"
total_90_q = 0
key_counts_90 = {0: 0, 1: 0, 2: 0, 3: 0}
letters = ["A", "B", "C", "D"]

for s_idx, sec in enumerate(exam_cp90_7):
    q_list = sec["qs"]
    total_90_q += len(q_list)
    if s_idx < 7:
        assert len(q_list) == 6, f"Passage {s_idx+1} expected 6 Qs, got {len(q_list)}"
        words = prose_words(sec["passage"])
        print(f"Passage {s_idx+1} prose words: {words}")
        assert 200 <= words <= 380, f"Passage {s_idx+1} word count {words} out of range [200, 380]"
        assert "<table class=\"tbl\">" in sec["passage"], f"Passage {s_idx+1} missing table"
    else:
        assert len(q_list) == 10, f"Discretes expected 10 Qs, got {len(q_list)}"
        for q in q_list:
            assert q.get("d") is True, "Discrete question missing d: True"

    for q_idx, q in enumerate(q_list):
        ans = q["a"]
        key_counts_90[ans] += 1
        ch = q["ch"]
        assert len(ch) == 4, f"Question {q['q']} has {len(ch)} choices"
        lens = [len(c) for c in ch]
        ratio = max(lens) / min(lens)
        assert ratio <= 1.25, f"Length ratio {ratio:.3f} > 1.25 for Q: {q['q'][:30]} lens={lens}"
        # check explanation
        exp = q["e"]
        assert exp.startswith("<strong>"), f"Exp missing strong header: {exp[:30]}"
        assert "<em>Distractor Traps:</em>" in exp, f"Exp missing distractor traps: {exp[:30]}"
        bullets = exp.count("&bull;")
        assert bullets == 3, f"Expected 3 distractor bullets, got {bullets} in Q: {q['q'][:30]}"
        # verify bullet letters match the 3 incorrect options
        correct_letter = letters[ans]
        wrong_letters = [l for l in letters if l != correct_letter]
        for wl in wrong_letters:
            assert f"&bull; {wl} " in exp or f"&bull; {wl} is" in exp or f"&bull; {wl} describes" in exp or f"&bull; {wl} computes" in exp or f"&bull; {wl} evaluates" in exp or f"&bull; {wl} refers" in exp or f"&bull; {wl} accounts" in exp or f"&bull; {wl} confuses" in exp or f"&bull; {wl} prescribes" in exp or f"&bull; {wl} doubles" in exp or f"&bull; {wl} claims" in exp or f"&bull; {wl} directionally" in exp or f"&bull; {wl} incorrectly" in exp or f"&bull; {wl} fails" in exp or f"&bull; {wl} falsely" in exp or f"&bull; {wl} introduces" in exp or f"&bull; {wl} assumes" in exp or f"&bull; {wl} inverts" in exp or f"&bull; {wl} provides" in exp or f"&bull; {wl} gives" in exp or f"&bull; {wl} uses" in exp, f"Missing bullet for {wl} in {exp}"

print(f"Total CP90 questions: {total_90_q}")
assert total_90_q == 52, f"Expected 52 Qs, got {total_90_q}"
print(f"CP90 Key counts: A={key_counts_90[0]}, B={key_counts_90[1]}, C={key_counts_90[2]}, D={key_counts_90[3]}")
assert key_counts_90[0] == 13 and key_counts_90[1] == 13 and key_counts_90[2] == 13 and key_counts_90[3] == 13, "Answer keys not exactly 13 each!"

print("\n=== VALIDATING EXAM_CP60_7 ===")
assert len(exam_cp60_7) == 6, f"Expected 6 sections, got {len(exam_cp60_7)}"
total_60_q = 0
key_counts_60 = {0: 0, 1: 0, 2: 0, 3: 0}
for s_idx, sec in enumerate(exam_cp60_7):
    q_list = sec["qs"]
    total_60_q += len(q_list)
    for q in q_list:
        key_counts_60[q["a"]] += 1
print(f"Total CP60 questions: {total_60_q}")
assert total_60_q == 33, f"Expected 33 Qs, got {total_60_q}"
print(f"CP60 Key counts: A={key_counts_60[0]}, B={key_counts_60[1]}, C={key_counts_60[2]}, D={key_counts_60[3]}")
assert key_counts_60[0] == 8 and key_counts_60[1] == 8 and key_counts_60[2] == 9 and key_counts_60[3] == 8, "CP60 answer keys not 8, 8, 9, 8!"

# Write out Javascript files
cp90_js_content = f"""/* ---- exam_cp90_7.js ---- */
/* Full 90-minute Chem/Physical Practice Exam 7: 7 passages (42 Qs) + 10 discrete Qs = 52 Qs */
const EXAM_CP90_7 = {json.dumps(exam_cp90_7, indent=2)};

if (typeof window !== 'undefined') {{
  window.EXAM_CP90_7 = EXAM_CP90_7;
}}
if (typeof globalThis !== 'undefined') {{
  globalThis.EXAM_CP90_7 = EXAM_CP90_7;
}}
"""

cp60_js_content = f"""/* ---- exam_cp60_7.js ---- */
/* 60-minute Chem/Physical Practice Exam 7: 5 passages (30 Qs) + 3 discrete Qs = 33 Qs */
const EXAM_CP60_7 = {json.dumps(exam_cp60_7, indent=2)};

if (typeof window !== 'undefined') {{
  window.EXAM_CP60_7 = EXAM_CP60_7;
}}
if (typeof globalThis !== 'undefined') {{
  globalThis.EXAM_CP60_7 = EXAM_CP60_7;
}}
"""

with open("/home/cgslinde/DrillRoom/DrillRoom/exam_cp90_7.js", "w", encoding="utf-8") as f:
    f.write(cp90_js_content)

with open("/home/cgslinde/DrillRoom/DrillRoom/exam_cp60_7.js", "w", encoding="utf-8") as f:
    f.write(cp60_js_content)

print("\nFiles exam_cp90_7.js and exam_cp60_7.js written successfully!")
