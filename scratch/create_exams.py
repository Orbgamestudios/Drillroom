# create_exams.py
import json
import re
import os
import sys

def prose_words(html_str):
    text = re.sub(r'<table[\s\S]*?</table>', ' ', html_str)
    text = re.sub(r'<div class="ttl">[\s\S]*?</div>', ' ', text)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\$\$[\s\S]*?\$\$', ' ', text)
    text = re.sub(r'\$[^\$]*\$', ' ', text)
    words = [w for w in re.split(r'\s+', text) if len(w.strip()) > 0]
    return len(words)

# --- PASSAGE 1 ---
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

# --- PASSAGE 2 ---
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

print("P1 prose:", prose_words(p1["passage"]))
print("P2 prose:", prose_words(p2["passage"]))
