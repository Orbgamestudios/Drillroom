# make_exam7.py
import json
import re
import sys

def prose_words(html_str):
    text = re.sub(r'<table[\s\S]*?</table>', ' ', html_str)
    text = re.sub(r'<div class="ttl">[\s\S]*?</div>', ' ', text)
    text = re.sub(r'<[^>]+>', ' ', text)
    # remove math
    text = re.sub(r'\$\$[\s\S]*?\$\$', ' ', text)
    text = re.sub(r'\$[^\$]*\$', ' ', text)
    # clean punctuation
    words = [w for w in re.split(r'\s+', text) if len(w.strip()) > 0]
    return len(words)

# Passage 1
p1_passage = """<div class="ttl">Passage 1 (Questions 1&ndash;6)</div>
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
</table>"""

p1_qs = [
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

print("P1 prose words:", prose_words(p1_passage))
