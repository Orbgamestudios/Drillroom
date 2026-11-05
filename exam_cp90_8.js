/* ---- exam_cp90_8.js ---- */
/* Full 90-minute Chem/Physical Practice Exam 8: 7 passages (42 Qs) + 10 discrete Qs = 52 Qs */
const EXAM_CP90_8 = [
  {
    "id": "exam_cp90_8_p1",
    "sec": "C/P",
    "topic": "Flow Cytometry Optical Layout: Forward Scatter (FSC), Side Scatter (SSC) & Fluorophore Spectral Compensation",
    "sheet": 1,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_8",
    "passage": "<div class=\"ttl\">Passage 1 (Questions 1&ndash;6)</div>\n<p>Immunologists and clinical biophysicists routinely employ multi-parametric flow cytometry to quantify leukocyte subpopulations in peripheral blood mononuclear cell (PBMC) isolations. In a modern flow cytometer, a cell suspension is injected into a laminar sheath fluid stream inside a quartz flow chamber. Hydrodynamic focusing forces the sample stream into a narrow coaxial core, aligning individual cells single-file as they traverse an optical interrogation point intersecting a focused 488-nm solid-state diode laser beam.</p>\n<p>When an incident laser photon strikes a passing cell, light is scattered in all directions. Light scattered at small forward angles ($0.5^\\circ$ to $10^\\circ$) is detected by a forward scatter (FSC) photodiode aligned with the laser axis. Forward scatter arises primarily from wave diffraction around the cell perimeter and correlates directly with cell cross-sectional surface area (cell size). Concurrently, light scattered orthogonally at $90^\\circ$ is collected by a side scatter (SSC) lens array and directed to a photomultiplier tube (PMT). Side scatter arises from optical reflection and refraction at internal intracellular interfaces, reflecting nuclear lobulation, cytoplasmic granularity, and organelle complexity.</p>\n<p>To differentiate T lymphocyte subsets and monocytes, cells were stained with fluorescein isothiocyanate (FITC)-conjugated anti-CD4 antibodies (excitation maximum $495\\text{ nm}$, emission peak $525\\text{ nm}$) and phycoerythrin (PE)-conjugated anti-CD14 antibodies (excitation $496/546\\text{ nm}$, emission peak $578\\text{ nm}$). Emitted fluorescence is separated using dichroic mirrors and bandpass filters. The FL1 detector (PMT1) collects FITC emission through a 530/30 nm bandpass filter, while the FL2 detector (PMT2) collects PE emission through a 585/40 nm bandpass filter. Because FITC's emission spectrum exhibits a wide spectral tail extending into the 585/40 nm bandpass, a spillover coefficient ($k = 0.18$) is subtracted via linear spectral matrix compensation:</p>\n$$F_{PE,\\text{comp}} = F_{PE,\\text{meas}} - k \\cdot F_{FITC,\\text{meas}}$$\n<p>Optical scatter and fluorescence metrics across major leukocyte populations were recorded (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Optical scatter characteristics, fluorophore spillover, and fluorescence intensity across leukocyte subsets</caption>\n  <thead>\n    <tr><th>Cell Population</th><th>Frequency (% Total)</th><th>Forward Scatter (FSC, a.u.)</th><th>Side Scatter (SSC, a.u.)</th><th>Uncompensated FL2 (PE, a.u.)</th><th>Compensated FL2 (PE, a.u.)</th><th>Nuclear & Granule Morphology</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Lymphocytes</td><td>32.4 &plusmn; 2.1</td><td>210 &plusmn; 15</td><td>85 &plusmn; 8</td><td>450 &plusmn; 22</td><td>90 &plusmn; 10</td><td>Agranular, single round nucleus</td></tr>\n    <tr><td>Monocytes</td><td>8.6 &plusmn; 0.9</td><td>540 &plusmn; 30</td><td>310 &plusmn; 25</td><td>2850 &plusmn; 110</td><td>2760 &plusmn; 105</td><td>Moderate lysosomal granules, indented nucleus</td></tr>\n    <tr><td>Neutrophils</td><td>54.2 &plusmn; 3.4</td><td>620 &plusmn; 35</td><td>780 &plusmn; 42</td><td>120 &plusmn; 14</td><td>102 &plusmn; 12</td><td>Dense azurophilic granules, multi-lobed nucleus</td></tr>\n    <tr><td>Cell Debris</td><td>4.8 &plusmn; 0.6</td><td>35 &plusmn; 6</td><td>28 &plusmn; 5</td><td>45 &plusmn; 8</td><td>38 &plusmn; 7</td><td>Amorphous membrane fragments</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "How do the primary physical optics principles underlying Forward Scatter (FSC) and Side Scatter (SSC) detection differ?",
        "ch": [
          "FSC relies on narrow-angle diffraction reflecting cell size, whereas SSC relies on orthogonal light reflection and refraction reflecting internal granularity",
          "FSC relies on wide-angle light refraction reflecting cell size, whereas SSC relies on axial light diffraction reflecting outer membrane thickness",
          "FSC relies on inelastic Raman scattering reflecting cell size, whereas SSC relies on elastic Rayleigh scattering reflecting cytoplasmic viscocity",
          "FSC relies on coherent stimulated emission reflecting cell size, whereas SSC relies on spontaneous fluorescence emission reflecting nuclear diameter"
        ],
        "a": 0,
        "e": "<strong>Physical optical mechanisms of FSC and SSC (Topic 370):</strong> Forward Scatter (FSC) is collected at small forward angles ($0.5^\\circ$ to $10^\\circ$) along the incident laser path, where light undergoes Fraunhofer/Mie diffraction around the cell perimeter; diffraction intensity scales with cross-sectional surface area, providing a readout of cell volume. Side Scatter (SSC) is collected at $90^\\circ$ perpendicular to the laser beam, where photons undergo reflection and refraction at internal boundaries with differing refractive indices (such as chromatin clumps, mitochondrial membranes, and cytoplasmic granules), providing an index of internal structural complexity.<br><br><em>Distractor Traps:</em><br>&bull; B directionally inverts optical scattering geometries and claims diffraction measures membrane thickness.<br>&bull; C misidentifies elastic Mie/Fraunhofer scattering as Raman scattering and misattributes SSC to cytoplasmic viscosity.<br>&bull; D confuses flow cytometric laser scattering with stimulated emission and fluorescence."
      },
      {
        "q": "In the flow cytometer interrogation cell, what fluid mechanical condition is established by the outer sheath fluid to ensure single-cell interrogation?",
        "ch": [
          "Turbulent vortex mixing that accelerates cells radially outward against the inner walls of the quartz interrogation chamber",
          "Laminar coaxial flow that hydrodynamically focuses the central sample stream into a single-file core along the laser axis",
          "High Reynolds number flow that creates acoustic standing waves to trap cells at pressure antinodes inside the quartz cell",
          "Electroosmotic fluid drive that electrophoretically separates individual leukocytes based on surface net negative charge"
        ],
        "a": 1,
        "e": "<strong>Hydrodynamic focusing and laminar fluid mechanics (Topic 370):</strong> Hydrodynamic focusing introduces the sample cell suspension into a rapidly flowing concentric sheath fluid. Because the Reynolds number is maintained well below the critical turbulent threshold ($Re < 2000$), the flow regime is strictly laminar. The faster-flowing sheath fluid accelerates and narrows the inner sample core stream, constraining suspended leukocytes into a single-file queue traversing the laser focal point, which prevents coincidental multi-cell optical events.<br><br><em>Distractor Traps:</em><br>&bull; A describes turbulent vortex mixing, which disrupts laminar core flow and causes sample clumping.<br>&bull; C describes acoustic standing wave focusing, which operates at lower flow velocities and does not utilize sheath fluid dynamics.<br>&bull; D describes capillary zone electrophoresis, confusing hydrodynamic sheath fluid drag with electric field mobility."
      },
      {
        "q": "For a lymphocyte subpopulation displaying a measured FITC signal of 2,000 a.u. and an uncompensated PE signal of 450 a.u., what is the compensated PE intensity?",
        "ch": [
          "Exactly 810 a.u.",
          "Exactly 450 a.u.",
          "Exactly 90 a.u.",
          "Exactly 18 a.u."
        ],
        "a": 2,
        "e": "<strong>Calculation of spectral compensation matrix subtraction (Topic 370):</strong> Spectral overlap occurs because the emission tail of FITC extends into the 585/40 nm bandpass filter of the PE channel. Using the compensation formula provided: $F_{PE,\\text{comp}} = F_{PE,\\text{meas}} - k \\cdot F_{FITC,\\text{meas}}$. Given $k = 0.18$, $F_{PE,\\text{meas}} = 450\\text{ a.u.}$, and $F_{FITC,\\text{meas}} = 2000\\text{ a.u.}$, the spillover contribution is $k \\cdot F_{FITC,\\text{meas}} = 0.18 \\times 2000 = 360\\text{ a.u.}$ Subtracting this spillover from the uncompensated PE intensity gives: $F_{PE,\\text{comp}} = 450 - 360 = 90\\text{ a.u.}$, matching Table 1.<br><br><em>Distractor Traps:</em><br>&bull; A forgets to subtract the spectral spillover correction, simply reporting the uncompensated PE signal (450 a.u.).<br>&bull; B computes the spillover correction alone ($0.18 \\times 2000 = 360\\text{ a.u.}$) rather than the net compensated intensity.<br>&bull; D divides by the spillover percentage or multiplies $0.18 \\times 100$, arriving at an order-of-magnitude error."
      },
      {
        "q": "Based on the data in Table 1, why do neutrophils exhibit significantly greater Side Scatter (SSC) signals than lymphocytes?",
        "ch": [
          "Neutrophils have larger overall cross-sectional surface areas that diffract incident light into the forward photodiode",
          "Neutrophils lack internal organelles, allowing unobstructed transmission of photons through the cytoplasm to the PMT",
          "Neutrophils possess higher surface expression of CD14 receptors, which intensely absorb and re-emit 488-nm laser light",
          "Neutrophils contain multi-lobed nuclei and dense cytoplasmic granules that cause extensive wide-angle light scattering"
        ],
        "a": 3,
        "e": "<strong>Cytoplasmic granularity and side scatter morphology (Topic 370):</strong> Side scatter is governed by internal structural heterogeneity. Mature neutrophils are polymorphonuclear granulocytes containing segmented multi-lobed nuclei and dense cytoplasmic granules (primary azurophilic and secondary specific granules). These internal organelles present abundant interfaces with differing refractive indices, causing extensive refraction and wide-angle ($90^\\circ$) reflection that produces high SSC ($780 \\pm 42\\text{ a.u.}$). In contrast, lymphocytes have a single round nucleus and scant agranular cytoplasm, generating low SSC ($85 \\pm 8\\text{ a.u.}$).<br><br><em>Distractor Traps:</em><br>&bull; A describes forward scatter (FSC) mechanics and misattributes cell cross-sectional area to orthogonal side scatter.<br>&bull; B falsely asserts neutrophils lack internal organelles; mature neutrophils are packed with dense primary and secondary granules.<br>&bull; C confuses immunophenotypic marker staining with label-free intrinsic optical scatter parameters."
      },
      {
        "q": "The FL1 channel utilizes a 530/30 nm bandpass optical filter. What wavelength range of light does this optical element transmit to the PMT1 detector?",
        "ch": [
          "515 nm to 545 nm",
          "500 nm to 530 nm",
          "530 nm to 560 nm",
          "485 nm to 515 nm"
        ],
        "a": 0,
        "e": "<strong>Bandpass filter specifications in optical spectroscopy (Topic 370):</strong> A bandpass filter designated as $\\lambda_0 / \\Delta \\lambda$ is characterized by its center wavelength $\\lambda_0$ and full-width half-maximum (FWHM) bandwidth $\\Delta \\lambda$. For a 530/30 nm filter, the transmitted band is symmetrically centered at $530\\text{ nm}$ with a total width of $30\\text{ nm}$ (i.e., $\\pm 15\\text{ nm}$ on either side of the center). Therefore, the transmitted wavelength range is: $530 - 15 = 515\\text{ nm}$ to $530 + 15 = 545\\text{ nm}$. This window captures the peak fluorescence emission of FITC ($525\\text{ nm}$) while blocking scattered 488-nm excitation laser light.<br><br><em>Distractor Traps:</em><br>&bull; B assumes a 30-nm asymmetrical lower bandpass extending from 500 to 530 nm.<br>&bull; C assumes a 30-nm asymmetrical upper bandpass extending from 530 to 560 nm.<br>&bull; D represents a bandpass centered at 500 nm rather than 530 nm."
      },
      {
        "q": "If an operator increases the supply voltage applied across the dynodes of the FL1 photomultiplier tube (PMT), what effect is observed?",
        "ch": [
          "The quantum yield of FITC fluorescence increases, causing fluorophores to emit more photons per absorbed excitation photon",
          "The secondary electron multiplication gain increases, yielding larger output current pulses for identical photon arrivals",
          "The wavelength sensitivity of the photocathode shifts, allowing PMT1 to detect longer wavelength infrared photons directly",
          "The transit time of electrons through the dynode chain decreases to zero, eliminating all background dark current noise"
        ],
        "a": 1,
        "e": "<strong>Photomultiplier tube electronic gain mechanics (Topic 370):</strong> In a photomultiplier tube, incident photons strike a photocathode to eject primary photoelectrons via the photoelectric effect. An applied high voltage establishes an electric field across a cascade of secondary dynodes. Increasing the PMT voltage increases the kinetic energy of electrons impacting each dynode, multiplying the number of secondary electrons ejected per stage. This elevates the overall multiplication gain ($G = \\delta^n$), resulting in larger output current pulses without altering the intrinsic quantum yield or optical emission properties of the fluorophore.<br><br><em>Distractor Traps:</em><br>&bull; A confuses detector electronic amplification with fluorophore intrinsic quantum yield, which is an invariant molecular property.<br>&bull; C falsely claims dynode voltage alters the optical bandgap and spectral sensitivity of the photocathode material.<br>&bull; D asserts dynode voltage eliminates electron transit time and thermal dark current, which is physically impossible."
      }
    ]
  },
  {
    "id": "exam_cp90_8_p2",
    "sec": "C/P",
    "topic": "Bohr Hydrogen Model, Quantized Rydberg Transitions & Transition Metal Anomalies (Cr, Cu)",
    "sheet": 2,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_8",
    "passage": "<div class=\"ttl\">Passage 2 (Questions 7&ndash;12)</div>\n<p>Analytical chemists and astrophysicists utilize atomic emission spectroscopy to investigate quantized electronic transitions in hydrogen and multielectron transition metal ions. According to the Bohr model of the hydrogen atom, an electron of mass $m_e$ and charge $e$ orbits a stationary nucleus in discrete circular trajectories with quantized orbital angular momentum:</p>\n$$L = m_e v r = \\frac{n h}{2\\pi} = n \\hbar \\quad (n = 1, 2, 3, \\dots)$$\n<p>Equating Coulombic electrostatic attraction to centripetal acceleration establishes quantized orbital radii ($r_n = n^2 a_0$, where $a_0 = 52.9\\text{ pm}$ is the Bohr radius) and discrete electronic energy states:</p>\n$$E_n = -\\frac{R_H}{n^2} = -\\frac{13.6\\text{ eV}}{n^2} = -\\frac{2.18 \\times 10^{-18}\\text{ J}}{n^2}$$\n<p>Relaxation from an excited principal state $n_i$ to a lower state $n_f$ results in the emission of a photon with quantized energy $\\Delta E = h c / \\lambda = R_H (1/n_f^2 - 1/n_i^2)$. Transitions terminating at the ground state ($n_f = 1$) form the high-energy ultraviolet Lyman series, transitions terminating at $n_f = 2$ form the visible Balmer series, and transitions terminating at $n_f = 3$ form the near-infrared Paschen series. In atomic hydrogen, these radiative decays obey the electric dipole selection rule $\\Delta l = \\pm 1$.</p>\n<p>In multielectron transition metal systems analyzed via inductively coupled plasma optical emission spectrometry (ICP-OES), an argon plasma sustained at temperatures between $6000\\text{ K}$ and $8000\\text{ K}$ atomizes and thermally excites injected metal ions. Subshell filling follows the Aufbau principle, Hund's rule, and the Pauli exclusion principle, but exhibits thermodynamic ground-state anomalies driven by electron exchange stabilization. Chromium ($Z = 24$) and copper ($Z = 29$) adopt half-filled ($3d^5$) and fully-filled ($3d^{10}$) configurations, respectively, rather than completing the $4s$ subshell. Quantized hydrogen transitions and transition metal electronic configurations were compiled for comparison (Table 2).</p>\n<table class=\"tbl\">\n  <caption>Table 2 Quantized hydrogen emission transitions and transition metal ground-state electronic configurations</caption>\n  <thead>\n    <tr><th>Species</th><th>Initial State ($n_i$)</th><th>Final State ($n_f$)</th><th>Calculated $\\Delta E$ (eV)</th><th>Emission $\\lambda$ (nm)</th><th>Spectral Series / Color</th><th>Ground State Configuration</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>H atom</td><td>$n = 3$</td><td>$n = 2$</td><td>1.89</td><td>656.3</td><td>Balmer ($H_\\alpha$) / Red</td><td>$1s^1$</td></tr>\n    <tr><td>H atom</td><td>$n = 4$</td><td>$n = 2$</td><td>2.55</td><td>486.1</td><td>Balmer ($H_\\beta$) / Cyan</td><td>$1s^1$</td></tr>\n    <tr><td>H atom</td><td>$n = 2$</td><td>$n = 1$</td><td>10.20</td><td>121.6</td><td>Lyman ($\\text{Ly}_\\alpha$) / Far UV</td><td>$1s^1$</td></tr>\n    <tr><td>H atom</td><td>$n = 4$</td><td>$n = 3$</td><td>0.66</td><td>1875.1</td><td>Paschen ($P_\\alpha$) / Infrared</td><td>$1s^1$</td></tr>\n    <tr><td>Cr$^0$ (neutral)</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>Ground State</td><td>[Ar] $4s^1 3d^5$</td></tr>\n    <tr><td>Cr$^{3+}$ (cation)</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>Ground State</td><td>[Ar] $3d^3$</td></tr>\n    <tr><td>Cu$^0$ (neutral)</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>Ground State</td><td>[Ar] $4s^1 3d^{10}$</td></tr>\n    <tr><td>Cu$^{+}$ (cation)</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>Ground State</td><td>[Ar] $3d^{10}$</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "When an electron in a hydrogen atom undergoes a transition from the n = 3 level to the n = 2 level, what is the emitted photon energy and spectral classification?",
        "ch": [
          "10.20 eV in the ultraviolet Lyman series",
          "2.55 eV in the cyan-colored Balmer series",
          "1.89 eV in the red-colored Balmer series",
          "0.66 eV in the infrared Paschen series"
        ],
        "a": 2,
        "e": "<strong>Bohr model transition energy and Balmer series calculation (Topic 371):</strong> The energy of a photon emitted during an electronic transition in hydrogen is given by the Rydberg equation: $\\Delta E = R_H (1/n_f^2 - 1/n_i^2) = 13.6\\text{ eV}(1/2^2 - 1/3^2) = 13.6\\text{ eV}(1/4 - 1/9) = 13.6\\text{ eV}(5/36) \\approx 1.89\\text{ eV}$. Wavelength is $\\lambda = \\frac{hc}{\\Delta E} = \\frac{1240\\text{ eV}\\cdot\\text{nm}}{1.89\\text{ eV}} \\approx 656\\text{ nm}$, which is the characteristic red $H_\\alpha$ line of the visible Balmer series ($n_f = 2$).<br><br><em>Distractor Traps:</em><br>&bull; A describes the $n = 2 \\to 1$ transition in the ultraviolet Lyman series ($\\Delta E = 10.20\\text{ eV}$, $\\lambda = 121.6\\text{ nm}$).<br>&bull; B describes the $n = 4 \\to 2$ transition in the visible Balmer series ($H_\\beta$, $\\Delta E = 2.55\\text{ eV}$, $\\lambda = 486.1\\text{ nm}$).<br>&bull; D describes the $n = 4 \\to 3$ transition in the infrared Paschen series ($\\Delta E = 0.66\\text{ eV}$, $\\lambda = 1875\\text{ nm}$)."
      },
      {
        "q": "When a neutral chromium atom is ionized to form the chromium(III) cation, Cr3+, what is its ground-state valence electron configuration?",
        "ch": [
          "[Ar] 4s2 3d1",
          "[Ar] 4s1 3d2",
          "[Ar] 4s0 3d4",
          "[Ar] 4s0 3d3"
        ],
        "a": 3,
        "e": "<strong>Transition metal ionization and electron removal sequence (Topics 372-373):</strong> Neutral chromium ($Z = 24$) has the ground-state electron configuration $[\\text{Ar}]\\,4s^1 3d^5$. When transition metals form cations, electrons are always removed first from orbitals with the highest principal quantum number ($n = 4$), because the $4s$ electrons are spatially more diffuse and experience lower nuclear penetration once the $3d$ subshell is occupied. To form $\\text{Cr}^{3+}$, three electrons must be removed: the single $4s$ electron is lost first, followed by two $3d$ electrons, leaving $[\\text{Ar}]\\,3d^3$ (or $[\\text{Ar}]\\,4s^0 3d^3$).<br><br><em>Distractor Traps:</em><br>&bull; A fails to remove $4s$ electrons first upon ionization, mistakenly treating $3d$ as more easily ionized than $4s$.<br>&bull; B only removes two electrons ($4s^1 3d^1$) rather than three, leaving a +2 oxidation state.<br>&bull; C removes two electrons from $4s$ and one from $3d$ based on the fictitious $[\\text{Ar}]\\,4s^2 3d^4$ neutral state."
      },
      {
        "q": "What thermodynamic and quantum mechanical factor accounts for the anomalous ground-state electron configuration of neutral copper ([Ar] 4s1 3d10)?",
        "ch": [
          "Complete shielding of nuclear charge by the single 4s electron, which eliminates all attractive forces acting on 3d orbitals",
          "Minimization of principal quantum number n, which requires all valence electrons to occupy the lowest possible angular shell",
          "Exchange energy stabilization and spherical charge symmetry associated with an entirely filled set of five degenerate 3d orbitals",
          "Relativistic expansion of the inner 1s and 2s core orbitals, which forces valence electrons outward into diffuse 4s configurations"
        ],
        "a": 2,
        "e": "<strong>Anomalous subshell stability and exchange energy in copper (Topic 373):</strong> In copper ($Z = 29$), the expected Aufbau configuration is $[\\text{Ar}]\\,4s^2 3d^9$. However, promoting one electron from the $4s$ orbital to the $3d$ subshell produces a completely filled $[\\text{Ar}]\\,4s^1 3d^{10}$ configuration. A filled $d^{10}$ subshell achieves complete spherical charge symmetry and maximizes quantum exchange energy ($K \\cdot \\frac{n(n-1)}{2}$), which minimizes electron-electron repulsion. The energetic stabilization gained by completing the $d^{10}$ subshell significantly exceeds the small energy required to promote an electron from $4s$ to $3d$.<br><br><em>Distractor Traps:</em><br>&bull; A falsely claims a single $4s$ electron completely shields nuclear charge from the inner $3d$ subshell.<br>&bull; B misinterprets quantum rules, as $3d$ ($n=3$) already has a lower principal quantum number than $4s$ ($n=4$).<br>&bull; D invokes relativistic core contraction, which only becomes dominant in very heavy elements like gold or mercury."
      },
      {
        "q": "Based on the Bohr model, how does the orbital radius of an electron in the n = 3 state of hydrogen compare to its orbital radius in the ground state (n = 1)?",
        "ch": [
          "It is 1.73 times larger because orbital radius scales with the square root of n",
          "It is 3.00 times larger because orbital radius scales linearly with quantum level n",
          "It is 6.00 times larger because orbital radius scales with the orbital diameter 2n",
          "It is 9.00 times larger because orbital radius scales with the square of quantum level n"
        ],
        "a": 3,
        "e": "<strong>Quadratic scaling of Bohr orbital radii (Topic 371):</strong> In the Bohr atom, equating centripetal acceleration ($m_e v^2 / r$) to Coulomb attraction ($k e^2 / r^2$) alongside quantized angular momentum ($m_e v r = n \\hbar$) gives the orbital radius equation: $r_n = \\frac{n^2 \\hbar^2}{k m_e e^2} = n^2 a_0$, where $a_0 \\approx 52.9\\text{ pm}$. Thus, orbital radius scales quadratically with principal quantum number ($r_n \\propto n^2$). For $n = 3$, $r_3 = 3^2 a_0 = 9 a_0$, which is exactly 9.00 times larger than the ground-state radius ($r_1 = 1^2 a_0 = a_0$).<br><br><em>Distractor Traps:</em><br>&bull; A assumes orbital radius scales with the square root of principal quantum number ($\\sqrt{n}$).<br>&bull; B assumes a linear scaling relationship between orbital radius and quantum number ($r_n \\propto n$).<br>&bull; C calculates orbital diameter scaling ($2n$) rather than the quadratic dependence ($n^2$)."
      },
      {
        "q": "Why do electronic transitions in the hydrogen Lyman series emit photons of strictly higher energy and frequency than transitions in the Balmer series?",
        "ch": [
          "Lyman transitions terminate at n = 1, which has a much larger energy gap to excited states than the n = 2 level",
          "Lyman transitions violate the Pauli exclusion principle, requiring higher kinetic energy to overcome core shielding",
          "Balmer transitions involve transitions to the ground state, which releases substantially less electrostatic energy",
          "Balmer transitions emit photons that undergo destructive wave interference, lowering their observed frequencies"
        ],
        "a": 0,
        "e": "<strong>Quantized energy level spacing and spectral series hierarchy (Topic 371):</strong> Hydrogen energy levels are governed by $E_n = -13.6\\text{ eV} / n^2$. The energy gap between $n = 1$ ($-13.6\\text{ eV}$) and $n = 2$ ($-3.4\\text{ eV}$) is $10.2\\text{ eV}$. Because all Lyman series transitions terminate at $n_f = 1$, the smallest possible Lyman transition ($n = 2 \\to 1$) releases $10.2\\text{ eV}$ (ultraviolet, $\\lambda = 121.6\\text{ nm}$). In contrast, Balmer transitions terminate at $n_f = 2$; even the highest-energy Balmer transition ($n = \\infty \\to 2$) releases only $3.4\\text{ eV}$ (visible/near-UV). Because $\\Delta E = h f$, Lyman photons strictly possess higher energy and frequency.<br><br><em>Distractor Traps:</em><br>&bull; B falsely asserts Lyman transitions violate the Pauli exclusion principle.<br>&bull; C directionally inverts ground state energetics; the $n=1$ state is the deepest electrostatic potential well.<br>&bull; D falsely attributes lower photon frequency to destructive interference rather than quantized energy differences."
      },
      {
        "q": "According to Hund's rule, why is the ground-state valence configuration of neutral chromium ([Ar] 4s1 3d5) characterized by six unpaired electrons?",
        "ch": [
          "Pairing electrons in the 4s subshell would violate the Heisenberg uncertainty principle by localizing electron positions",
          "Placing single electrons into separate degenerate orbitals with parallel spins minimizes inter-electronic Coulombic repulsion",
          "Unpaired electrons generate strong diamagnetic repulsions that lower the total effective nuclear charge of the nucleus",
          "Parallel spins decrease the orbital angular momentum quantum number l, allowing valence electrons to penetrate the nucleus"
        ],
        "a": 1,
        "e": "<strong>Hund's rule and spin multiplicity maximization (Topics 372-373):</strong> Hund's rule of maximum multiplicity states that for degenerate orbitals (such as the five $3d$ orbitals), the lowest-energy configuration is achieved by placing one electron into each orbital with parallel spins before any pairing occurs. This spatial separation keeps negatively charged electrons as far apart as possible, minimizing inter-electronic Coulombic repulsion. Furthermore, parallel spins allow quantum mechanical exchange stabilization. Neutral chromium features one electron in the $4s$ orbital and five unpaired electrons in the $3d$ subshell, resulting in six total unpaired spins ($S = 3$).<br><br><em>Distractor Traps:</em><br>&bull; A misapplies the Heisenberg uncertainty principle to electron pairing within degenerate subshells.<br>&bull; C confuses paramagnetism with diamagnetism and misrepresents nuclear charge effects.<br>&bull; D falsely claims parallel spins alter orbital angular momentum quantum number $l$."
      }
    ]
  },
  {
    "id": "exam_cp90_8_p3",
    "sec": "C/P",
    "topic": "Effective Nuclear Charge (Zeff), Core Shielding, Atomic/Ionic Radii & First vs Second Ionization Energy",
    "sheet": 3,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_8",
    "passage": "<div class=\"ttl\">Passage 3 (Questions 13&ndash;18)</div>\n<p>Bioinorganic chemists investigate how periodic atomic properties govern physiological metal cation selectivity and the cellular toxicity of heavy metals. In multielectron atoms, the net positive electrostatic attraction experienced by a valence electron is described by the effective nuclear charge ($Z_{\\text{eff}}$):</p>\n$$Z_{\\text{eff}} = Z - S$$\n<p>where $Z$ is the nuclear charge (atomic number) and $S$ represents the screening (shielding) constant exerted by intervening electrons. Core electrons occupy localized inner spherical orbitals that shield outer electrons with high efficiency ($S \\approx 1.0$ per core electron). In contrast, valence electrons in the same principal energy shell exhibit poor mutual shielding ($S \\approx 0.35$). Consequently, across any period from left to right, $Z_{\\text{eff}}$ increases systematically, drawing the valence electron cloud closer to the nucleus and causing a contraction in atomic radius.</p>\n<p>Removing an electron requires an input of energy termed the first ionization energy ($\\text{IE}_1$):</p>\n$$\\text{X}(g) \\to \\text{X}^+(g) + e^- \\quad (\\Delta H = \\text{IE}_1 > 0)$$\n<p>Subsequent removal of a second electron requires the second ionization energy ($\\text{IE}_2$). When an ionization process strips an electron from a stable, filled noble gas core, $\\text{IE}$ increases by nearly an order of magnitude due to the drop in principal quantum number $n$ and an abrupt increase in $Z_{\\text{eff}}$.</p>\n<p>Isoelectronic ions share identical electron configurations ($1s^2 2s^2 2p^6$) but possess differing nuclear charges. Quantitative measurements of nuclear shielding, atomic radii, ionic radii, and successive ionization energies were compiled for representative biological Period 3 and Group 1/2 elements (Table 3).</p>\n<table class=\"tbl\">\n  <caption>Table 3 Nuclear parameters, atomic and ionic radii, and successive ionization energies for Period 3 elements</caption>\n  <thead>\n    <tr><th>Element & Symbol</th><th>Atomic Number ($Z$)</th><th>Ground Configuration</th><th>Valence $Z_{\\text{eff}}$</th><th>Atomic Radius (pm)</th><th>Monatomic Ion</th><th>Ionic Radius (pm)</th><th>$\\text{IE}_1$ (kJ/mol)</th><th>$\\text{IE}_2$ (kJ/mol)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Sodium (Na)</td><td>11</td><td>[Ne] $3s^1$</td><td>+2.20</td><td>186</td><td>Na$^+$</td><td>102</td><td>496</td><td>4562</td></tr>\n    <tr><td>Magnesium (Mg)</td><td>12</td><td>[Ne] $3s^2$</td><td>+2.85</td><td>160</td><td>Mg$^{2+}$</td><td>72</td><td>738</td><td>1451</td></tr>\n    <tr><td>Aluminum (Al)</td><td>13</td><td>[Ne] $3s^2 3p^1$</td><td>+3.50</td><td>143</td><td>Al$^{3+}$</td><td>54</td><td>578</td><td>1817</td></tr>\n    <tr><td>Phosphorus (P)</td><td>15</td><td>[Ne] $3s^2 3p^3$</td><td>+4.80</td><td>110</td><td>P$^{3-}$</td><td>212</td><td>1012</td><td>1907</td></tr>\n    <tr><td>Sulfur (S)</td><td>16</td><td>[Ne] $3s^2 3p^4$</td><td>+5.45</td><td>104</td><td>S$^{2-}$</td><td>184</td><td>1000</td><td>2252</td></tr>\n    <tr><td>Potassium (K)</td><td>19</td><td>[Ar] $4s^1$</td><td>+2.20</td><td>227</td><td>K$^+$</td><td>138</td><td>419</td><td>3052</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "Across the isoelectronic series Na+, Mg2+, and Al3+, what accounts for the observed monotonic decrease in ionic radius (102 pm to 72 pm to 54 pm)?",
        "ch": [
          "Decreasing effective nuclear charge allows the valence shell to expand farther away from the atomic nucleus",
          "Increasing principal quantum number n forces the core electrons into higher energy degenerate subshells",
          "Increasing nuclear charge acts on an identical number of electrons, drawing the electron cloud inward",
          "Enhanced core electron shielding reduces Coulombic attraction between protons and inner-shell electrons"
        ],
        "a": 2,
        "e": "<strong>Isoelectronic radii and nuclear charge dependency (Topic 375):</strong> The ions $\\text{Na}^+$ ($Z = 11$), $\\text{Mg}^{2+}$ ($Z = 12$), and $\\text{Al}^{3+}$ ($Z = 13$) are isoelectronic, each possessing exactly 10 electrons with the closed-shell configuration $1s^2 2s^2 2p^6$. Because the number of electrons and core shielding are identical, the effective nuclear charge is determined solely by the number of nuclear protons. As atomic number increases from 11 to 13, the greater positive nuclear charge exerts a progressively stronger electrostatic Coulombic attraction on the same 10 electrons, pulling the electron cloud tighter toward the nucleus and causing a marked decrease in ionic radius.<br><br><em>Distractor Traps:</em><br>&bull; A directionally inverts effective nuclear charge, which increases rather than decreases across the series.<br>&bull; B claims principal quantum number increases, but all three ions share an identical $n=2$ valence configuration ($[\\text{Ne}]$).<br>&bull; D asserts core shielding increases, whereas the number of core electrons ($1s^2 = 2$) is identical across all three ions."
      },
      {
        "q": "Why is the second ionization energy of sodium (4562 kJ/mol) nearly ten times its first ionization energy (496 kJ/mol)?",
        "ch": [
          "Sodium's second electron is ejected from an unstable, diffuse 3p orbital experiencing negligible nuclear charge",
          "The second ionization requires breaking a covalent sigma bond between adjacent sodium nuclei in the gas phase",
          "Removing the second electron reverses the direction of the nuclear magnetic dipole, causing spin destabilization",
          "The second electron must be stripped from a stable noble-gas core orbital with a lower principal quantum number"
        ],
        "a": 3,
        "e": "<strong>Successive ionization energies and noble gas core removal (Topic 376):</strong> The first ionization of sodium removes its single valence electron from the $3s$ subshell ($[\\text{Ne}]\\,3s^1 \\to [\\text{Ne}]$), requiring a modest energy input of $496\\text{ kJ/mol}$. The second ionization requires removing an electron from the closed noble gas neon core ($1s^2 2s^2 2p^6$). Core $n = 2$ electrons occupy orbitals with a significantly smaller average radial distance from the nucleus and experience dramatically higher effective nuclear charge ($Z_{\\text{eff}}$) due to minimal intervening shielding. This electrostatic transition produces an enormous ~9.2-fold spike in ionization energy.<br><br><em>Distractor Traps:</em><br>&bull; A claims the second electron occupies a diffuse $3p$ orbital, whereas it is removed from a contracted $2p$ noble gas core.<br>&bull; B describes homolytic covalent bond cleavage in diatomic molecules rather than atomic gas-phase photoionization.<br>&bull; C misattributes ionization energy spikes to nuclear magnetic dipole flipping rather than electrostatic core attraction."
      },
      {
        "q": "Despite having a higher nuclear charge, aluminum exhibits a lower first ionization energy (578 kJ/mol) than magnesium (738 kJ/mol). Why?",
        "ch": [
          "Aluminum's single 3p electron is shielded by the completed 3s subshell and occupies a higher energy subshell",
          "Magnesium possesses half-filled 3p orbitals that confer extraordinary Hund's rule quantum exchange stability",
          "Aluminum has a smaller effective nuclear charge than magnesium due to severe valence electron-electron pairing",
          "Magnesium's 3s electrons experience zero core shielding from the underlying neon noble gas shell configuration"
        ],
        "a": 0,
        "e": "<strong>Subshell penetration and Period 3 ionization anomalies (Topic 376):</strong> Magnesium has the valence configuration $[\\text{Ne}]\\,3s^2$, whereas aluminum has $[\\text{Ne}]\\,3s^2 3p^1$. The $3p$ orbital has higher energy than the $3s$ orbital and has a node at the nucleus, making it less penetrating than the $3s$ orbital. Consequently, the lone $3p$ electron in aluminum is partially shielded from the nucleus by both the inner neon core and the completed $3s^2$ subshell. Because this electron occupies a higher energy level and is less tightly bound, less energy is required to remove it, making $\\text{IE}_1$ of aluminum ($578\\text{ kJ/mol}$) slightly lower than that of magnesium ($738\\text{ kJ/mol}$).<br><br><em>Distractor Traps:</em><br>&bull; B incorrectly claims magnesium has $3p$ electrons; neutral magnesium has a closed $3s^2$ subshell with no $3p$ occupancy.<br>&bull; C falsely claims aluminum has a lower effective nuclear charge; aluminum has 13 protons compared to magnesium's 12.<br>&bull; D ignores core electron shielding from the inner neon shell, which shields both atoms significantly."
      },
      {
        "q": "Which of the following periodic trends correctly describes the electron affinity and electronegativity of halogens relative to alkali metals?",
        "ch": [
          "Halogens exhibit more endothermic electron affinities and lower Pauling electronegativities than alkali metals",
          "Halogens exhibit more exothermic electron affinities and higher Pauling electronegativities than alkali metals",
          "Halogens exhibit identical electron affinities but significantly lower Pauling electronegativities than alkali metals",
          "Halogens exhibit positive electron affinities and completely zero electronegativities due to closed valence shells"
        ],
        "a": 1,
        "e": "<strong>Periodic trends in electron affinity and electronegativity (Topic 377):</strong> Across a period from left to right, effective nuclear charge ($Z_{\\text{eff}}$) increases significantly while atomic radius contracts. Halogens (Group 17) possess high $Z_{\\text{eff}}$ and valence configurations of $ns^2 np^5$; adding an electron completes a stable, noble gas octet, releasing substantial energy (highly exothermic electron affinity, $\\Delta H_{\\text{EA}} \\ll 0$). Halogens also exert a strong electrostatic pull on shared bonding electrons, resulting in high Pauling electronegativities (e.g., Fluorine = 4.0). In contrast, alkali metals (Group 1) have low $Z_{\\text{eff}}$, low electronegativity (0.8\u20131.0), and minimal electron affinity.<br><br><em>Distractor Traps:</em><br>&bull; A directionally inverts both trends, claiming halogens have endothermic electron affinities and lower electronegativity.<br>&bull; C erroneously states that electron affinity is identical across different periodic groups.<br>&bull; D describes noble gases (closed valence shells), which have positive/endothermic electron affinities and negligible electronegativity."
      },
      {
        "q": "Phosphorus exhibits a slightly higher first ionization energy (1012 kJ/mol) than sulfur (1000 kJ/mol). What quantum effect explains this anomaly?",
        "ch": [
          "Sulfur's valence electrons occupy a higher principal quantum shell (n = 4) than phosphorus's valence electrons",
          "Phosphorus possesses a completely filled valence octet that resists the loss of any outer valence electrons",
          "Sulfur has a paired electron in one 3p orbital, and the resulting Coulombic repulsion facilitates electron removal",
          "Phosphorus has a lower effective nuclear charge, which paradoxically increases electrostatic valence attraction"
        ],
        "a": 2,
        "e": "<strong>Electron pairing repulsion and Group 15/16 ionization anomalies (Topics 374, 376):</strong> Phosphorus has the valence configuration $3s^2 3p^3$, in which each of the three degenerate $3p$ orbitals contains a single unpaired electron with parallel spins, maximizing exchange stabilization according to Hund's rule. Sulfur has the configuration $3s^2 3p^4$, requiring two electrons to share one of the $3p$ orbitals. The inter-electronic Coulombic repulsion between the two paired electrons in the same spatial orbital increases electron energy and destabilizes the orbital, making it easier to remove one electron. As a result, $\\text{IE}_1$ of sulfur ($1000\\text{ kJ/mol}$) is slightly lower than that of phosphorus ($1012\\text{ kJ/mol}$).<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly assigns sulfur's valence electrons to $n=4$; both phosphorus and sulfur are Period 3 elements ($n=3$).<br>&bull; B claims phosphorus has a completed octet, but it only possesses a half-filled $3p^3$ valence subshell.<br>&bull; D asserts phosphorus has a lower effective nuclear charge and directionally inverts the relationship to ionization energy."
      },
      {
        "q": "Why do inner-shell core electrons shield valence electrons from nuclear charge much more effectively than valence electrons shield each other?",
        "ch": [
          "Core electrons possess opposite spin quantum numbers that completely cancel the nuclear magnetic dipole",
          "Valence electrons travel at relativistic speeds that prevent them from interacting with the atomic nucleus",
          "Core electrons have zero mass defect, allowing them to exert stronger repulsive forces on valence electrons",
          "Core electron probability densities lie between the nucleus and the valence shell, neutralizing nuclear charge"
        ],
        "a": 3,
        "e": "<strong>Radial probability distribution and core electron shielding (Topic 374):</strong> Electron shielding is governed by Gauss's law of electrostatics and quantum radial probability distribution functions. Core electrons (such as $1s$, $2s$, and $2p$) have radial probability distributions concentrated much closer to the nucleus than valence electrons. When a valence electron is situated at a radial distance $r$, inner core electrons lie entirely within a spherical surface of radius $r$, acting like a point negative charge at the nucleus that directly cancels part of the positive nuclear charge ($S \\approx 1.0$). In contrast, electrons in the same valence shell are located at similar radial distances and do not intervene between each other and the nucleus, providing very poor shielding ($S \\approx 0.35$).<br><br><em>Distractor Traps:</em><br>&bull; A invokes electron spin cancellation, which does not neutralize Coulombic electric monopoles.<br>&bull; B misapplies relativistic electron speeds to explain classical electrostatic shielding.<br>&bull; C claims core electrons have zero mass defect, which is physically meaningless in the context of atomic shielding."
      }
    ]
  },
  {
    "id": "exam_cp90_8_p4",
    "sec": "C/P",
    "topic": "Nuclear Binding Energy, Mass Defect, Alpha, Beta-Minus, Positron (PET) Decay & Electron Capture",
    "sheet": 4,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_8",
    "passage": "<div class=\"ttl\">Passage 4 (Questions 19&ndash;24)</div>\n<p>Nuclear medicine physicians and medical biophysicists utilize synthetic radioisotopes for diagnostic imaging and targeted radionuclide radiotherapy. Nuclear stability is governed by the strong nuclear force, which binds protons and neutrons into a compact nucleus against electrostatic Coulomb repulsion. The mass of any stable nucleus is strictly less than the sum of its individual constituent free nucleons. This difference is the mass defect ($\\Delta m$):</p>\n$$\\Delta m = [Z m_p + (A - Z) m_n] - m_{\\text{nucleus}}$$\n<p>According to Einstein's mass-energy equivalence ($E = \\Delta m \\cdot c^2$, where $1\\text{ amu} \\approx 931.5\\text{ MeV}$ ), mass defect is converted into nuclear binding energy ($E_b$) when nucleons assemble. The binding energy per nucleon ($E_b / A$) peaks near iron-56 ($^{56}\\text{Fe}$, $\\approx 8.8\\text{ MeV/nucleon}$); lighter nuclei release energy through nuclear fusion, while heavy actinide nuclei release energy through fission.</p>\n<p>Unstable radionuclides undergo spontaneous nuclear transmutations to achieve a stable neutron-to-proton ($N/Z$) ratio:</p>\n<ol>\n  <li><strong>Alpha decay ($\\alpha$):</strong> Heavy nuclei ($Z > 82$) eject a $^4_2\\text{He}$ nucleus, decreasing mass number $A$ by 4 and atomic number $Z$ by 2.</li>\n  <li><strong>Beta-minus decay ($\\beta^-$):</strong> Neutron-rich nuclei convert a neutron into a proton, emitting an electron and an electron antineutrino ($n \\to p^+ + e^- + \\bar{\\nu}_e$), increasing $Z$ by 1 while $A$ is unchanged.</li>\n  <li><strong>Beta-plus (positron) decay ($\\beta^+$):</strong> Proton-rich nuclei convert a proton into a neutron, emitting a positron and an electron neutrino ($p^+ \\to n + e^+ + \\nu_e$), decreasing $Z$ by 1 while $A$ is unchanged.</li>\n  <li><strong>Electron capture (EC):</strong> A proton captures an inner $K$-shell orbital electron ($p^+ + e^- \\to n + \\nu_e$), decreasing $Z$ by 1.</li>\n</ol>\n<p>In Positron Emission Tomography (PET), fluorine-18 ($^{18}\\text{F}$, $t_{1/2} = 110\\text{ min}$) labeled 2-deoxy-2-[$^{18}\\text{F}$]fluoro-D-glucose ($^{18}\\text{F}$-FDG) emits positrons that undergo matter-antimatter annihilation with ambient electrons, producing two collinear 511-keV gamma photons detected in coincidence (Table 4).</p>\n<table class=\"tbl\">\n  <caption>Table 4 Nuclear physical properties, decay pathways, and clinical applications of medical radioisotopes</caption>\n  <thead>\n    <tr><th>Radionuclide</th><th>Decay Mode</th><th>Half-Life ($t_{1/2}$)</th><th>Emitted Radiation</th><th>Daughter Isotope</th><th>Clinical Application</th><th>Mass Defect $\\Delta m$ (amu)</th><th>$E_b / A$ (MeV/nucleon)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Fluorine-18 ($^{18}_9\\text{F}$)</td><td>Positron ($\\beta^+$)</td><td>110 min</td><td>$\\beta^+$ ($0.63\\text{ MeV}$), $2\\times 511\\text{ keV } \\gamma$</td><td>$^{18}_8\\text{O}$</td><td>PET oncology staging</td><td>0.1477</td><td>7.65</td></tr>\n    <tr><td>Technetium-99m ($^{99\\text{m}}_{43}\\text{Tc}$)</td><td>Isomeric $\\gamma$</td><td>6.0 hr</td><td>$\\gamma$ ($140\\text{ keV}$)</td><td>$^{99}_{43}\\text{Tc}$</td><td>SPECT cardiac perfusion</td><td>0.9412</td><td>8.61</td></tr>\n    <tr><td>Iodine-131 ($^{131}_{53}\\text{I}$)</td><td>Beta-minus ($\\beta^-$)</td><td>8.0 days</td><td>$\\beta^-$ ($0.61\\text{ MeV}$), $\\gamma$ ($364\\text{ keV}$)</td><td>$^{131}_{54}\\text{Xe}$</td><td>Thyroid ablation therapy</td><td>1.1850</td><td>8.43</td></tr>\n    <tr><td>Radium-223 ($^{223}_{88}\\text{Ra}$)</td><td>Alpha ($\\alpha$)</td><td>11.4 days</td><td>$\\alpha$ ($5.78\\text{ MeV}$)</td><td>$^{219}_{86}\\text{Rn}$</td><td>Bone metastasis palliative therapy</td><td>1.9120</td><td>7.72</td></tr>\n    <tr><td>Thallium-201 ($^{201}_{81}\\text{Tl}$)</td><td>Electron capture</td><td>73 hr</td><td>X-rays ($68\\text{--}80\\text{ keV}$), $\\gamma$ ($167\\text{ keV}$)</td><td>$^{201}_{80}\\text{Hg}$</td><td>Myocardial viability imaging</td><td>1.7350</td><td>7.89</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "In PET oncology imaging using 18F-FDG, what physical process produces the two 511-keV photons detected by the circular detector array?",
        "ch": [
          "Annihilation of the emitted positron with an ambient tissue electron, converting mass into two collinear gamma rays",
          "Photoelectric absorption of emitted alpha particles by heavy tungsten collimators surrounding the patient gantry",
          "Bremsstrahlung deceleration of beta particles as they pass near dense hydroxyapatite crystals in skeletal bone",
          "Compton scattering of high-energy gamma rays emitted during the isomeric transition of the excited fluorine nucleus"
        ],
        "a": 0,
        "e": "<strong>Positron-electron annihilation physics in PET imaging (Topics 379, 382):</strong> In PET, fluorine-18 undergoes $\\beta^+$ decay, ejecting a positron ($e^+$). The positron travels a short distance (~1 mm in soft tissue), losing kinetic energy through inelastic collisions until it encounters an ambient atomic electron ($e^-$). The positron and electron undergo matter-antimatter annihilation ($e^+ + e^- \\to 2\\gamma$). Because both particles are nearly at rest, conservation of linear momentum requires the two resulting gamma photons to be emitted in opposite directions ($180^\\circ$ apart). By Einstein's mass-energy equivalence, the total rest mass converted is $2 m_e c^2 = 2(0.511\\text{ MeV}) = 1.022\\text{ MeV}$, giving each gamma photon an energy of exactly $511\\text{ keV}$.<br><br><em>Distractor Traps:</em><br>&bull; B describes photoelectric absorption of alpha particles, which do not produce 511 keV gamma pairs.<br>&bull; C describes continuous Bremsstrahlung X-ray production from decelerating beta particles.<br>&bull; D describes Compton scattering of nuclear gamma rays rather than electron-positron annihilation."
      },
      {
        "q": "When radium-223 (223Ra, Z = 88) undergoes alpha decay to deliver targeted radiotherapy in bone, what daughter nucleus is produced?",
        "ch": [
          "Actinium-223 with atomic number 89",
          "Radon-219 with an atomic number of 86",
          "Francium-219 with atomic number 87",
          "Thorium-227 with atomic number 90"
        ],
        "a": 1,
        "e": "<strong>Balancing alpha decay nuclear reactions (Topic 380):</strong> An alpha particle is a helium-4 nucleus ($^4_2\\text{He}$) containing 2 protons and 2 neutrons. In any nuclear transmutation, total nucleon mass number ($A$) and total electric charge ($Z$) must be conserved. For radium-223 ($^{223}_{88}\\text{Ra}$): $^{223}_{88}\\text{Ra} \\to ^A_Z\\text{Y} + ^4_2\\text{He}$. Conserving mass number: $A = 223 - 4 = 219$. Conserving atomic number: $Z = 88 - 2 = 86$. Element 86 on the periodic table is radon (Rn). Therefore, the daughter nucleus produced is radon-219 ($^{219}_{86}\\text{Rn}$).<br><br><em>Distractor Traps:</em><br>&bull; A represents a beta-minus decay transmutation where $Z$ increases to 89.<br>&bull; C miscalculates atomic number conservation ($88 - 2 = 86$, not 87).<br>&bull; D adds an alpha particle ($Z = 88 + 2 = 90$, $A = 223 + 4 = 227$), directionally inverting decay into nuclear fusion."
      },
      {
        "q": "During the beta-minus decay of iodine-131 into xenon-131, why is an electron antineutrino emitted alongside the high-energy electron?",
        "ch": [
          "To balance the decrease in mass number A between parent and daughter nuclei",
          "To neutralize positive electrostatic repulsions generated inside the nucleus",
          "To conserve lepton number and total angular momentum during the decay event",
          "To absorb excess kinetic energy that would otherwise trigger nuclear fission"
        ],
        "a": 2,
        "e": "<strong>Conservation of lepton number in beta-minus decay (Topic 381):</strong> In beta-minus decay, a neutron converts into a proton, an electron, and an antineutrino: $n \\to p^+ + e^- + \\bar{\\nu}_e$. Before decay, the neutron is a baryon with lepton number $L = 0$. After decay, the proton has $L = 0$, while the emitted electron has $L = +1$. To conserve total lepton number ($L_{\\text{initial}} = L_{\\text{final}} = 0$), an electron antineutrino possessing lepton number $L = -1$ must be simultaneously emitted ($+1 + (-1) = 0$). The antineutrino also carries intrinsic spin ($\\hbar/2$), ensuring the conservation of total angular momentum.<br><br><em>Distractor Traps:</em><br>&bull; A claims antineutrinos balance nucleon mass number, but $A$ is already strictly conserved ($131 \\to 131$).<br>&bull; B asserts antineutrinos possess electrical charge, but neutrinos and antineutrinos are electrically neutral leptons.<br>&bull; D misattributes antineutrino emission to preventing induced nuclear fission."
      },
      {
        "q": "Based on nuclear binding energy principles, why does nuclear fusion release energy for light nuclei while fission releases energy for heavy nuclei?",
        "ch": [
          "Heavy nuclei have higher mass defects per nucleon than iron-56, causing fission to consume thermal kinetic energy",
          "Light nuclei possess zero strong nuclear force, so combining them converts pure electromagnetic force into heat",
          "Both fusion and fission decrease total binding energy, driving reactions toward states of higher nuclear entropy",
          "Intermediate nuclei near iron-56 have the highest binding energy per nucleon, making transitions toward iron exothermic"
        ],
        "a": 3,
        "e": "<strong>Nuclear binding energy curve and reaction energetics (Topic 379):</strong> The curve of binding energy per nucleon ($E_b / A$) increases sharply for light elements, peaks near iron-56 ($^{56}\\text{Fe}$) at approximately $8.8\\text{ MeV/nucleon}$, and then decreases gradually for heavier actinide elements. When light nuclei combine (fusion) or heavy nuclei split (fission), the reaction products move closer to the iron-56 peak, resulting in higher binding energy per nucleon. Greater binding energy represents a greater mass defect (mass converted to energy via $E = \\Delta m \\cdot c^2$), which is released as kinetic energy and gamma radiation, making both pathways highly exothermic.<br><br><em>Distractor Traps:</em><br>&bull; A claims fission is endothermic and consumes thermal energy; nuclear fission of heavy actinide isotopes is highly exothermic.<br>&bull; B falsely asserts light nuclei lack strong nuclear forces.<br>&bull; C claims binding energy decreases; both fusion of light nuclei and fission of heavy nuclei increase binding energy per nucleon."
      },
      {
        "q": "What secondary emission process directly generates the characteristic X-rays observed during thallium-201 electron capture decay?",
        "ch": [
          "Pair production of electrons and positrons occurring in the Coulomb field of the daughter nucleus",
          "Spontaneous nuclear de-excitation from an isomeric spin state directly to the ground state",
          "Outer-shell orbital electrons dropping into the inner K-shell vacancy left by the captured electron",
          "Elastic nuclear scattering of incoming antineutrinos off peripheral valence electron shells"
        ],
        "a": 2,
        "e": "<strong>Atomic electron cascade following electron capture (Topic 383):</strong> In electron capture, the parent nucleus absorbs an inner atomic electron (typically from the $K$-shell, $n = 1$), converting a nuclear proton into a neutron ($p^+ + e^- \\to n + \\nu_e$). This process leaves a vacancy in the inner atomic electron shell of the daughter mercury atom ($^{201}\\text{Hg}$). An outer-shell electron (from the $L$ or $M$ shell) rapidly drops down to fill this vacancy, releasing the quantized energy difference between atomic subshells as a characteristic X-ray photon ($68\\text{--}80\\text{ keV}$) or ejecting an Auger electron.<br><br><em>Distractor Traps:</em><br>&bull; A describes electron-positron pair production, which requires high-energy gamma rays exceeding 1.022 MeV.<br>&bull; B describes isomeric gamma de-excitation, which releases nuclear gamma photons rather than atomic characteristic X-rays.<br>&bull; D describes hypothetical neutrino-electron scattering, which has an infinitesimal cross-section and does not generate X-rays."
      },
      {
        "q": "A patient receives an injection of 18F-FDG with an initial activity of 400 MBq. What is the remaining radioactivity after 330 minutes?",
        "ch": [
          "Approximately 200 MBq",
          "Approximately 100 MBq",
          "Approximately 75.0 MBq",
          "Approximately 50.0 MBq"
        ],
        "a": 3,
        "e": "<strong>Exponential radioactive decay kinetics and half-life (Topic 379):</strong> Radioactive decay follows first-order exponential kinetics: $A(t) = A_0 (1/2)^{t / t_{1/2}}$. From Table 4, the half-life of fluorine-18 is $t_{1/2} = 110\\text{ minutes}$. The elapsed time is $t = 330\\text{ minutes}$. Calculating the number of elapsed half-lives: $n = \\frac{330\\text{ min}}{110\\text{ min}} = 3.0$ half-lives. The remaining activity is: $A(330) = 400\\text{ MBq} \\times (1/2)^3 = 400 \\times \\frac{1}{8} = 50.0\\text{ MBq}$.<br><br><em>Distractor Traps:</em><br>&bull; A calculates remaining activity after only 1 half-life ($110\\text{ min}$): $400 / 2 = 200\\text{ MBq}$.<br>&bull; B calculates remaining activity after 2 half-lives ($220\\text{ min}$): $400 / 4 = 100\\text{ MBq}$.<br>&bull; C applies a linear decay rate ($400 - [3 \\times 108]$) rather than exponential half-life kinetics."
      }
    ]
  },
  {
    "id": "exam_cp90_8_p5",
    "sec": "C/P",
    "topic": "First Law of Thermodynamics (Delta U = Q - W), PV Work Diagrams & Thermodynamic Cycles",
    "sheet": 5,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_8",
    "passage": "<div class=\"ttl\">Passage 5 (Questions 25&ndash;30)</div>\n<p>Biomedical engineers designing pneumatic cardiopulmonary ventilators and artificial muscle actuators evaluate cyclic thermodynamic processes. According to the First Law of Thermodynamics, energy is conserved within any closed system:</p>\n$$\\Delta U = Q - W$$\n<p>where $\\Delta U$ is the change in internal energy, $Q$ is heat transferred to the system ($Q > 0$ for endothermic absorption, $Q < 0$ for exothermic release), and $W$ is mechanical work done by the system on its surroundings ($W = \\int P\\,dV$; $W > 0$ for expansion, $W < 0$ for compression). For an ideal monatomic gas, internal energy depends solely on absolute temperature: $U = \\frac{3}{2} n R T$.</p>\n<p>On a pressure-volume ($PV$) diagram:</p>\n<ul>\n  <li><strong>Isobaric path ($\\Delta P = 0$):</strong> Work done is $W = P(V_f - V_i)$ and $\\Delta U = Q - P\\Delta V$.</li>\n  <li><strong>Isochoric path ($\\Delta V = 0$):</strong> Work done is $W = 0$, so $\\Delta U = Q$.</li>\n  <li><strong>Isothermal path ($\\Delta T = 0$):</strong> Internal energy remains constant ($\\Delta U = 0$), so $Q = W$.</li>\n  <li><strong>Adiabatic path ($Q = 0$):</strong> No heat exchange occurs, yielding $\\Delta U = -W$. An adiabatic expansion ($W > 0$) results in gas cooling ($\\Delta T < 0$).</li>\n</ul>\n<p>A prototype pneumatic actuator operates on a closed rectangular four-stage cycle using $n = 0.50\\text{ mol}$ of an ideal gas (States $1 \\to 2 \\to 3 \\to 4 \\to 1$). State 1 begins at $P_1 = 100\\text{ kPa}$ and $V_1 = 10.0\\text{ L}$ ($T_1 \\approx 241\\text{ K}$). Step A ($1 \\to 2$) is an isochoric pressurization to $P_2 = 300\\text{ kPa}$. Step B ($2 \\to 3$) is an isobaric expansion to $V_3 = 30.0\\text{ L}$. Step C ($3 \\to 4$) is an isochoric depressurization back to $P_4 = 100\\text{ kPa}$. Step D ($4 \\to 1$) is an isobaric compression returning to $V_1 = 10.0\\text{ L}$.</p>\n<p>Because internal energy is a thermodynamic state function, traversing a complete closed cycle returns the working gas to its exact initial equilibrium state with zero net change in internal energy ($\\Delta U_{\\text{cycle}} = 0$). Over continuous operation, the enclosed geometric area on the $PV$ diagram represents the net mechanical work delivered to the ventilator bellows per cycle, while thermal efficiency characterizes how effectively absorbed heat is converted into usable mechanical work. Thermodynamic metrics were compiled (Table 5).</p>\n<table class=\"tbl\">\n  <caption>Table 5 Thermodynamic state parameters, heat transfers, and mechanical work across the actuator cycle</caption>\n  <thead>\n    <tr><th>Process Stage</th><th>Initial State ($P_i, V_i, T_i$)</th><th>Final State ($P_f, V_f, T_f$)</th><th>Process Type</th><th>Heat Added $Q$ (J)</th><th>Work Done $W$ (J)</th><th>Internal Energy $\\Delta U$ (J)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Step A ($1 \\to 2$)</td><td>100 kPa, 10.0 L, 241 K</td><td>300 kPa, 10.0 L, 722 K</td><td>Isochoric</td><td>+3000</td><td>0</td><td>+3000</td></tr>\n    <tr><td>Step B ($2 \\to 3$)</td><td>300 kPa, 10.0 L, 722 K</td><td>300 kPa, 30.0 L, 2165 K</td><td>Isobaric</td><td>+15000</td><td>+6000</td><td>+9000</td></tr>\n    <tr><td>Step C ($3 \\to 4$)</td><td>300 kPa, 30.0 L, 2165 K</td><td>100 kPa, 30.0 L, 722 K</td><td>Isochoric</td><td>&minus;9000</td><td>0</td><td>&minus;9000</td></tr>\n    <tr><td>Step D ($4 \\to 1$)</td><td>100 kPa, 30.0 L, 722 K</td><td>100 kPa, 10.0 L, 241 K</td><td>Isobaric</td><td>&minus;5000</td><td>&minus;2000</td><td>&minus;3000</td></tr>\n    <tr><td>Complete Cycle</td><td>100 kPa, 10.0 L, 241 K</td><td>100 kPa, 10.0 L, 241 K</td><td>Cyclic Loop</td><td>+4000</td><td>+4000</td><td>0</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "For the complete rectangular thermodynamic cycle (1 -> 2 -> 3 -> 4 -> 1), what is the net mechanical work done by the pneumatic actuator?",
        "ch": [
          "Exactly +4000 J of work",
          "Exactly +6000 J of work",
          "Exactly +2000 J of work",
          "Exactly zero net J of work"
        ],
        "a": 0,
        "e": "<strong>Enclosed area on a PV diagram and net cyclic work (Topic 385):</strong> The net work done by a system traversing a closed path on a $PV$ diagram is equal to the geometric area enclosed by the loop. For the rectangular cycle: $W_{\\text{net}} = \\Delta P \\times \\Delta V = (P_{\\text{high}} - P_{\\text{low}})(V_{\\text{high}} - V_{\\text{low}}) = (300\\text{ kPa} - 100\\text{ kPa})(30.0\\text{ L} - 10.0\\text{ L}) = (200\\text{ kPa})(20.0\\text{ L})$. Converting to SI units ($1\\text{ kPa} = 10^3\\text{ Pa}$, $1\\text{ L} = 10^{-3}\\text{ m}^3$): $W_{\\text{net}} = (2.00 \\times 10^5\\text{ Pa})(2.00 \\times 10^{-2}\\text{ m}^3) = +4000\\text{ J}$. Alternatively, summing the work across all four steps gives: $W_{\\text{net}} = 0 + 6000 + 0 + (-2000) = +4000\\text{ J}$.<br><br><em>Distractor Traps:</em><br>&bull; B calculates only the positive expansion work during Step B ($W = P \\Delta V = 300\\text{ kPa} \\times 20\\text{ L} = 6000\\text{ J}$), ignoring negative compression work.<br>&bull; C calculates work done during the compression stroke alone ($W = 100\\text{ kPa} \\times 20\\text{ L} = 2000\\text{ J}$).<br>&bull; D falsely assumes cyclic work is zero because internal energy change is zero ($\\Delta U = 0$)."
      },
      {
        "q": "During Step A (1 -> 2), why is the mechanical work performed by the gas strictly equal to zero?",
        "ch": [
          "The temperature of the ideal gas remains constant throughout the pressurization phase",
          "The volume of the chamber remains fixed, so no boundary displacement occurs (dV = 0)",
          "The external atmospheric pressure perfectly matches the internal cylinder pressure",
          "Heat added to the system is completely dissipated into frictional kinetic drag"
        ],
        "a": 1,
        "e": "<strong>Isochoric work definition in thermodynamics (Topics 384-385):</strong> Mechanical boundary work is defined as the integral of pressure over volume change: $W = \\int P\\,dV$. In an isochoric (isovolumetric) process such as Step A, the volume of the gas is rigidly held constant at $10.0\\text{ L}$, which means $dV = 0$. Because the system boundary does not translate or displace against the surroundings, no mechanical work is performed on or by the gas ($W = 0$). By the First Law ($\\Delta U = Q - W$), all heat absorbed during this step directly increases the internal energy of the gas: $\\Delta U = Q = +3000\\text{ J}$.<br><br><em>Distractor Traps:</em><br>&bull; A falsely claims temperature is constant; temperature triples from 241 K to 722 K during Step A.<br>&bull; C asserts chamber pressure matches atmospheric pressure, ignoring the rigid fixed boundary constraint.<br>&bull; D assumes mechanical work is lost to friction rather than being zero due to zero volume displacement ($dV = 0$)."
      },
      {
        "q": "If the actuator undergoes an adiabatic expansion where the gas performs 1,500 J of work on the piston, what is the change in internal energy and gas temperature?",
        "ch": [
          "Delta U = -1,500 J, and the gas temperature decreases",
          "Delta U = +1,500 J, and the gas temperature increases",
          "Delta U = 0 J, and the gas temperature remains constant",
          "Delta U = -1,500 J, and the gas temperature increases"
        ],
        "a": 0,
        "e": "<strong>Adiabatic expansion and the First Law of Thermodynamics (Topic 384):</strong> In an adiabatic process, the system is thermally insulated from its surroundings so that no heat is exchanged ($Q = 0$). Substituting $Q = 0$ into the First Law of Thermodynamics ($\\Delta U = Q - W$) yields: $\\Delta U = -W$. When the gas expands and performs positive work on the piston ($W = +1500\\text{ J}$), the internal energy change is $\\Delta U = -(+1500\\text{ J}) = -1500\\text{ J}$. Because the internal energy of an ideal gas is directly proportional to absolute temperature ($U = \\frac{3}{2} n R T$), a reduction in internal energy ($\\Delta U < 0$) causes a corresponding drop in gas temperature ($\\Delta T < 0$).<br><br><em>Distractor Traps:</em><br>&bull; B inverts the sign of internal energy, claiming expansion work increases internal energy in an adiabatic process.<br>&bull; C confuses adiabatic processes ($Q = 0$) with isothermal processes ($\\Delta U = 0$).<br>&bull; D correctly calculates $\\Delta U = -1500\\text{ J}$ but directionally inverts the temperature change, claiming temperature rises."
      },
      {
        "q": "On a pressure-volume (PV) diagram, what does clockwise traversal of a closed loop indicate regarding the thermodynamic nature of the system?",
        "ch": [
          "The system operates as a refrigeration heat pump requiring net external mechanical work input",
          "The system operates as a heat engine delivering net positive mechanical work to the surroundings",
          "The system undergoes irreversible entropy destruction, violating the second law of thermodynamics",
          "The system exhibits zero net heat exchange because all process stages are strictly isothermal"
        ],
        "a": 1,
        "e": "<strong>Directionality of thermodynamic PV cycles and heat engines (Topic 385):</strong> When a cyclic process traverses a closed $PV$ loop in a clockwise direction, the high-pressure upper curve represents positive expansion work ($W_{\\text{exp}} > 0$), while the low-pressure lower curve represents negative compression work ($W_{\\text{comp}} < 0$). Because expansion occurs at a higher pressure than compression, the positive work exceeds the magnitude of the negative work, resulting in net positive work done by the system ($W_{\\text{net}} > 0$). This constitutes a heat engine, which converts absorbed thermal energy into useful mechanical work. Conversely, counter-clockwise cycles require net work input ($W_{\\text{net}} < 0$), operating as refrigerators or heat pumps.<br><br><em>Distractor Traps:</em><br>&bull; A describes a counter-clockwise PV loop, which corresponds to a refrigerator or heat pump requiring net work input.<br>&bull; C claims clockwise cycles violate the second law of thermodynamics; standard heat engines operate clockwise with valid efficiencies.<br>&bull; D falsely asserts that all four stages of the cycle are isothermal."
      },
      {
        "q": "Why is the change in internal energy (Delta U) for the entire cycle (1 -> 2 -> 3 -> 4 -> 1) identically zero?",
        "ch": [
          "The mechanical work done during expansion exactly cancels the mechanical work done during isochoric heating",
          "Heat input during Step B is perfectly absorbed by latent phase changes of the working fluid inside the piston",
          "Internal energy is a thermodynamic state function that depends solely on the initial and final state variables",
          "The ideal gas undergoes adiabatic isolation, preventing any thermal or mechanical interaction with surroundings"
        ],
        "a": 2,
        "e": "<strong>State functions versus path functions in cyclic processes (Topic 384):</strong> Thermodynamic properties such as internal energy ($U$), enthalpy ($H$), entropy ($S$), pressure ($P$), volume ($V$), and temperature ($T$) are state functions: their values depend entirely on the current equilibrium state of the system, not on the path taken to reach that state. In any complete thermodynamic cycle, the working fluid returns to its exact initial state (State 1: $P_1 = 100\\text{ kPa}$, $V_1 = 10.0\\text{ L}$, $T_1 = 241\\text{ K}$). Therefore, the net change in any state function over one complete cycle is identically zero ($\\Delta U_{\\text{cycle}} = U_1 - U_1 = 0$). In contrast, heat ($Q$) and work ($W$) are path functions.<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly equates work during expansion with work during isochoric heating (where $W = 0$).<br>&bull; B asserts the ideal gas undergoes latent phase transitions, but the working fluid remains an ideal gas throughout.<br>&bull; D confuses cyclic state function behavior with adiabatic thermal isolation."
      },
      {
        "q": "What is the thermal efficiency (eta = W_net / Q_in) of the prototype pneumatic actuator over one complete cycle?",
        "ch": [
          "Approximately 50.0%",
          "Approximately 33.3%",
          "Approximately 26.7%",
          "Approximately 22.2%"
        ],
        "a": 3,
        "e": "<strong>Thermal efficiency calculation for a cyclic engine (Topic 385):</strong> Thermal efficiency is defined as the ratio of net mechanical work output to total heat input: $\\eta = \\frac{W_{\\text{net}}}{Q_{\\text{in}}}$. From Table 5, net mechanical work is $W_{\\text{net}} = +4000\\text{ J}$. Heat input occurs during the endothermic stages (Step A where $Q_A = +3000\\text{ J}$, and Step B where $Q_B = +15000\\text{ J}$ ), giving a total heat input of $Q_{\\text{in}} = 3000 + 15000 = 18000\\text{ J}$. Calculating thermal efficiency: $\\eta = \\frac{4000\\text{ J}}{18000\\text{ J}} = \\frac{4}{18} = \\frac{2}{9} \\approx 0.222$ (or $22.2\\%$).<br><br><em>Distractor Traps:</em><br>&bull; A divides net work by Step B work alone ($4000 / 6000 = 66.7\\%$) or assumes a Carnot limit of 50%.<br>&bull; B divides work by compression heat or computes $2000 / 6000 = 33.3\\%$.<br>&bull; C computes $4000 / 15000 = 26.7\\%$, omitting heat added during the isochoric Step A ($Q_A = 3000\\text{ J}$)."
      }
    ]
  },
  {
    "id": "exam_cp90_8_p6",
    "sec": "C/P",
    "topic": "Hess's Law, Standard Enthalpies of Formation & Bond Dissociation Energy (BDE) in Substrate Oxidation",
    "sheet": 6,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_8",
    "passage": "<div class=\"ttl\">Passage 6 (Questions 31&ndash;36)</div>\n<p>Exercise physiologists and nutritional biochemists study the bioenergetics of cellular respiration by measuring reaction enthalpies of metabolic fuels. In cellular metabolism, carbohydrate and fatty acid substrates undergo enzymatic oxidation to yield carbon dioxide, water, and ATP. The standard enthalpy of combustion ($\\Delta H_{\\text{comb}}^\\circ$) can be quantified experimentally using a bomb calorimeter or calculated theoretically from standard enthalpies of formation ($\\Delta H_f^\\circ$):</p>\n$$\\Delta H_{\\text{rxn}}^\\circ = \\sum n \\Delta H_f^\\circ(\\text{products}) - \\sum m \\Delta H_f^\\circ(\\text{reactants})$$\n<p>By international thermodynamic convention, the standard enthalpy of formation of any pure chemical element in its most stable allotropic form at $298\\text{ K}$ and $1\\text{ bar}$ is defined as zero ($\\Delta H_f^\\circ[\\text{O}_2(g)] = 0\\text{ kJ/mol}$). Because enthalpy is a state function, Hess's law dictates that the total enthalpy change for a chemical transformation is independent of the pathway.</p>\n<p>Reaction enthalpies can also be estimated from mean gas-phase bond dissociation energies (BDE):</p>\n$$\\Delta H_{\\text{rxn}} \\approx \\sum \\text{BDE}(\\text{bonds broken}) - \\sum \\text{BDE}(\\text{bonds formed})$$\n<p>Bond cleavage is strictly endothermic ($\\text{BDE} > 0$), while bond formation is exothermic.</p>\n<p>Researchers investigated the complete oxidation of glucose ($\\text{C}_6\\text{H}_{12}\\text{O}_6(s)$), palmitic acid ($\\text{C}_{16}\\text{H}_{32}\\text{O}_2(s)$), and lactate ($\\text{C}_3\\text{H}_6\\text{O}_3(s)$). Combustion reactions were conducted in a constant-volume bomb calorimeter surrounded by $2.00\\text{ kg}$ of water (total calorimeter heat capacity $C_{\\text{cal}} = 10.5\\text{ kJ/}^\\circ\\text{C}$). In bomb calorimetry, the sample is ignited in a pressurized pure oxygen atmosphere ($P \\approx 25\\text{--}30\\text{ atm}$) inside a rigid, heavy-walled steel bomb. Because the reaction occurs at strictly constant volume ($\\Delta V = 0$), no boundary displacement work is performed ($W = 0$), and the net heat released directly equals the internal energy of combustion ($\\Delta U_{\\text{comb}} = q_V$). Reaction enthalpy is subsequently determined via $\\Delta H = \\Delta U + \\Delta n_{\\text{gas}} R T$. Thermochemical properties were compiled (Table 6).</p>\n<table class=\"tbl\">\n  <caption>Table 6 Thermochemical properties, combustion enthalpies, and caloric energy densities of metabolic substrates</caption>\n  <thead>\n    <tr><th>Substrate</th><th>Molecular Formula</th><th>Molar Mass (g/mol)</th><th>$\\Delta H_f^\\circ$ (kJ/mol)</th><th>Combustion Stoichiometry</th><th>$\\Delta H_{\\text{comb}}^\\circ$ (kJ/mol)</th><th>Energy Density (kJ/g)</th><th>Caloric Density (kcal/g)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Glucose</td><td>C$_6$H$_{12}$O$_6(s)$</td><td>180.2</td><td>&minus;1274</td><td>C$_6$H$_{12}$O$_6$ + 6O$_2$ &rarr; 6CO$_2$ + 6H$_2$O</td><td>&minus;2802</td><td>15.6</td><td>3.73</td></tr>\n    <tr><td>Palmitic Acid</td><td>C$_{16}$H$_{32}$O$_2(s)$</td><td>256.4</td><td>&minus;892</td><td>C$_{16}$H$_{32}$O$_2$ + 23O$_2$ &rarr; 16CO$_2$ + 16H$_2$O</td><td>&minus;9978</td><td>38.9</td><td>9.30</td></tr>\n    <tr><td>Lactic Acid</td><td>C$_3$H$_6$O$_3(s)$</td><td>90.1</td><td>&minus;694</td><td>C$_3$H$_6$O$_3$ + 3O$_2$ &rarr; 3CO$_2$ + 3H$_2$O</td><td>&minus;1344</td><td>14.9</td><td>3.56</td></tr>\n    <tr><td>Carbon Dioxide</td><td>CO$_2(g)$</td><td>44.0</td><td>&minus;393.5</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>\n    <tr><td>Liquid Water</td><td>H$_2$O$(l)$</td><td>18.0</td><td>&minus;285.8</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "Using the standard enthalpies of formation in Table 6, what is the calculated standard enthalpy of combustion (Delta H_comb) for one mole of glucose?",
        "ch": [
          "-2802 kJ/mol",
          "-1954 kJ/mol",
          "-3476 kJ/mol",
          "-1274 kJ/mol"
        ],
        "a": 0,
        "e": "<strong>Enthalpy of combustion calculation from enthalpies of formation (Topic 386):</strong> The balanced combustion reaction of glucose is: $\\text{C}_6\\text{H}_{12}\\text{O}_6(s) + 6\\text{O}_2(g) \\to 6\\text{CO}_2(g) + 6\\text{H}_2\\text{O}(l)$. Applying Hess's law with $\\Delta H_f^\\circ[\\text{O}_2(g)] = 0$: $\\Delta H_{\\text{comb}}^\\circ = [6\\Delta H_f^\\circ(\\text{CO}_2) + 6\\Delta H_f^\\circ(\\text{H}_2\\text{O})] - [\\Delta H_f^\\circ(\\text{glucose}) + 6(0)]$. Substituting values from Table 6: $\\Delta H_{\\text{comb}}^\\circ = [6(-393.5) + 6(-285.8)] - [-1274] = [-2361.0 - 1714.8] + 1274 = -4075.8 + 1274 = -2801.8\\text{ kJ/mol} \\approx -2802\\text{ kJ/mol}$.<br><br><em>Distractor Traps:</em><br>&bull; B forgets to multiply the formation enthalpy of $\\text{CO}_2$ by its stoichiometric coefficient of 6.<br>&bull; C subtracts the formation enthalpy of products from reactants, inverting the sign of $\\Delta H_{\\text{rxn}}^\\circ$.<br>&bull; D reports the standard enthalpy of formation of glucose itself rather than the combustion enthalpy."
      },
      {
        "q": "Why does palmitic acid yield more than twice the caloric energy density per gram (9.30 kcal/g) compared to glucose (3.73 kcal/g)?",
        "ch": [
          "Palmitic acid contains more hydroxyl functional groups that form stabilizing intermolecular hydrogen bonds",
          "Fatty acid carbons exist in a more highly reduced oxidation state than the partially oxidized carbons of glucose",
          "The combustion of palmitic acid produces pure elemental hydrogen gas, which possesses an exceptionally high BDE",
          "Glucose requires enzyme activation that consumes two ATP equivalents, decreasing its intrinsic heat of combustion"
        ],
        "a": 1,
        "e": "<strong>Oxidation states and caloric density of metabolic fuels (Topics 386-387):</strong> The energy released during combustion originates from the oxidation of carbon atoms to carbon dioxide (where carbon has an oxidation state of +4). In palmitic acid ($\text{C}_{16}\text{H}_{32}\text{O}_2$), the long hydrocarbon tail consists predominantly of methylene groups ($-\\text{CH}_2-$) where carbon has a formal oxidation state of -2 (highly reduced). In contrast, glucose ($\text{C}_6\text{H}_{12}\text{O}_6$) is heavily oxygenated with multiple hydroxyl and carbonyl groups, where carbon has an average oxidation state of 0. Because fatty acid carbons are far more reduced, their complete oxidation transfers more electrons to oxygen per gram of substrate, releasing substantially more energy ($38.9\\text{ kJ/g} \\approx 9.30\\text{ kcal/g}$ vs $15.6\\text{ kJ/g} \\approx 3.73\\text{ kcal/g}$).<br><br><em>Distractor Traps:</em><br>&bull; A attributes high caloric density to hydroxyl groups; palmitic acid has only one carboxyl group and no hydroxyls, whereas glucose is heavily oxygenated.<br>&bull; C falsely claims combustion produces elemental hydrogen gas instead of liquid water.<br>&bull; D confuses cellular biochemical glycolysis ATP priming with standard bomb calorimeter combustion thermodynamics."
      },
      {
        "q": "Anaerobic glycolysis converts one mole of glucose into two moles of lactic acid (C6H12O6 -> 2 C3H6O3). Based on Table 6, what is Delta H_rxn for this conversion?",
        "ch": [
          "+2802 kJ/mol",
          "+114 kJ/mol",
          "-114 kJ/mol",
          "-1458 kJ/mol"
        ],
        "a": 2,
        "e": "<strong>Application of Hess's law to biochemical transformations (Topic 386):</strong> For the conversion $\\text{C}_6\\text{H}_{12}\\text{O}_6 \\to 2\\text{C}_3\\text{H}_6\\text{O}_3$, the reaction enthalpy can be calculated directly from formation enthalpies: $\\Delta H_{\\text{rxn}}^\\circ = 2\\Delta H_f^\\circ(\\text{lactic acid}) - \\Delta H_f^\\circ(\\text{glucose})$. Substituting values from Table 6: $\\Delta H_{\\text{rxn}}^\\circ = 2(-694\\text{ kJ/mol}) - (-1274\\text{ kJ/mol}) = -1388 + 1274 = -114\\text{ kJ/mol}$. Alternatively, using heats of combustion: $\\Delta H_{\\text{rxn}}^\\circ = \\Delta H_{\\text{comb}}^\\circ(\\text{glucose}) - 2\\Delta H_{\\text{comb}}^\\circ(\\text{lactic acid}) = -2802 - 2(-1344) = -2802 + 2688 = -114\\text{ kJ/mol}$. This exothermicity drives cellular ATP regeneration under hypoxic conditions.<br><br><em>Distractor Traps:</em><br>&bull; A reports the positive enthalpy of reverse glucose combustion.<br>&bull; B directionally inverts the enthalpy change, claiming anaerobic fermentation is endothermic (+114 kJ/mol).<br>&bull; D computes the difference between one mole of lactic acid combustion and glucose combustion."
      },
      {
        "q": "Why does calculating reaction enthalpies from average bond dissociation energies (BDE) yield slight discrepancies compared to bomb calorimetry?",
        "ch": [
          "Bond breaking is exothermic in the gas phase but endothermic in aqueous cellular solution",
          "Bond dissociation energies violate Hess's law because enthalpy is a path-dependent function",
          "Calorimetry measures free energy Delta G directly rather than standard enthalpy Delta H",
          "BDE values are gas-phase averages that do not account for condensed-phase intermolecular forces"
        ],
        "a": 3,
        "e": "<strong>Limitations of bond dissociation energy approximations (Topic 387):</strong> Bond dissociation energy (BDE) calculations rely on tabulations of average homolytic bond energies measured strictly for isolated molecules in the gas phase. In bomb calorimetry, reactants and products exist in condensed phases (solid glucose, liquid water), where substantial intermolecular forces (such as lattice energy and hydrogen bonding networks) and enthalpies of condensation contribute significantly to the overall heat of reaction. Furthermore, real chemical bonds have dissociation energies influenced by local resonance, hybridization, and steric environments, whereas BDE values use generalized cross-compound averages.<br><br><em>Distractor Traps:</em><br>&bull; A falsely claims bond breaking is exothermic in the gas phase; bond breaking is always endothermic regardless of phase.<br>&bull; B asserts BDE violates Hess's law and falsely characterizes enthalpy as path-dependent.<br>&bull; C claims bomb calorimetry measures free energy $\\Delta G$; constant-volume calorimetry directly measures $\\Delta U$ and enthalpy $\\Delta H$."
      },
      {
        "q": "Why is the standard enthalpy of formation (Delta H_f) of diatomic oxygen gas, O2(g), equal to 0 kJ/mol in thermodynamic tables?",
        "ch": [
          "By thermodynamic convention, elements in their standard reference states at 298 K and 1 bar are assigned Delta H_f = 0",
          "The double bond in O2 possesses zero bond dissociation energy due to symmetrical nonpolar electron sharing",
          "Diatomic oxygen cannot undergo combustion reactions because it serves exclusively as an oxidizing agent",
          "Oxygen gas possesses zero standard molar entropy at room temperature according to the Third Law of Thermodynamics"
        ],
        "a": 0,
        "e": "<strong>Thermodynamic reference state definitions for elements (Topic 386):</strong> The standard enthalpy of formation ($\\Delta H_f^\\circ$) is defined as the enthalpy change accompanying the formation of one mole of a compound from its pure constituent elements in their standard reference states at $298.15\\text{ K}$ ($25^\\circ\\text{C}$) and $1\\text{ bar}$. Because forming an element from itself involves zero chemical transformation, the standard enthalpy of formation of any pure element in its most stable physical and allotropic state at $298\\text{ K}$ and $1\\text{ bar}$ is defined by convention as identically zero: $\\Delta H_f^\\circ[\\text{O}_2(g)] = 0\\text{ kJ/mol}$, $\\Delta H_f^\\circ[\\text{C}(s,\\text{graphite})] = 0\\text{ kJ/mol}$, and $\\Delta H_f^\\circ[\\text{H}_2(g)] = 0\\text{ kJ/mol}$.<br><br><em>Distractor Traps:</em><br>&bull; B claims the $\\text{O}=\\text{O}$ double bond has zero BDE; diatomic oxygen has a high bond dissociation energy of $498\\text{ kJ/mol}$.<br>&bull; C confuses thermodynamic reference definitions with chemical reactivity as an oxidizer.<br>&bull; D misapplies the Third Law of Thermodynamics, which assigns zero entropy to perfect crystals at absolute zero ($0\\text{ K}$), not gases at $298\\text{ K}$."
      },
      {
        "q": "When a 0.500-g sample of glucose (Delta H_comb = -15.6 kJ/g) is burned completely in the bomb calorimeter (C_cal = 10.5 kJ/deg C), what is the temperature rise?",
        "ch": [
          "Exactly 1.48 deg C",
          "Exactly 0.74 deg C",
          "Exactly 0.37 deg C",
          "Exactly 2.96 deg C"
        ],
        "a": 1,
        "e": "<strong>Calorimetric heat capacity and temperature rise calculation (Topic 386):</strong> Combustion releases heat into the calorimeter vessel and surrounding water bath: $q_{\\text{cal}} = -q_{\\text{rxn}} = m \\cdot |\\Delta H_{\\text{comb}}|$. For a $0.500\\text{-g}$ sample of glucose with energy density $15.6\\text{ kJ/g}$: $q_{\\text{cal}} = (0.500\\text{ g})(15.6\\text{ kJ/g}) = 7.80\\text{ kJ}$. The temperature increase of the calorimeter system is related to its total heat capacity by $q_{\\text{cal}} = C_{\\text{cal}} \\Delta T$. Solving for $\\Delta T$: $\\Delta T = \\frac{q_{\\text{cal}}}{C_{\\text{cal}}} = \\frac{7.80\\text{ kJ}}{10.5\\text{ kJ/}^\\circ\\text{C}} \\approx 0.743^\\circ\\text{C} \\approx 0.74^\\circ\\text{C}$.<br><br><em>Distractor Traps:</em><br>&bull; A calculates $\\Delta T$ for a 1.00-g sample of glucose ($7.8 \\times 2 / 10.5 = 1.48^\\circ\\text{C}$).<br>&bull; C divides the temperature rise by an extraneous factor of 2 ($0.74 / 2 = 0.37^\\circ\\text{C}$).<br>&bull; D multiplies by a factor of 4 or miscalculates sample mass as 2.00 g."
      }
    ]
  },
  {
    "id": "exam_cp90_8_p7",
    "sec": "C/P",
    "topic": "Heating Curves, Latent Heats of Fusion/Vaporization & Lyophilization Phase Boundaries",
    "sheet": 7,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_8",
    "passage": "<div class=\"ttl\">Passage 7 (Questions 37&ndash;42)</div>\n<p>Pharmaceutical formulation scientists utilize lyophilization (freeze-drying) to stabilize therapeutic monoclonal antibodies (mAbs) and vaccines against hydrolytic and thermal degradation. Lyophilization exploits water's thermodynamic phase boundaries, sublimating solid ice directly into water vapor under reduced chamber pressure without passing through the intermediate liquid phase.</p>\n<p>On a temperature-versus-heat ($T$ vs $q$) heating curve:</p>\n<ul>\n  <li><strong>Single-phase heating regions:</strong> Temperature increases linearly with heat input according to sensible heat transfer ($q = m c \\Delta T$), where $c$ is specific heat capacity. The slope of the curve ($\\Delta T / q = 1 / m c$) is inversely proportional to $c$; substances with higher specific heat display shallower temperature warming slopes.</li>\n  <li><strong>Phase transition plateaus:</strong> During melting or boiling, added heat disrupts intermolecular hydrogen bonds without changing temperature ($q = m \\Delta H_{\\text{fus}}$ or $q = m \\Delta H_{\\text{vap}}$), yielding horizontal plateaus.</li>\n</ul>\n<p>Water's triple point occurs at $T_t = 0.01^\\circ\\text{C}$ ($273.16\\text{ K}$) and $P_t = 0.006\\text{ atm}$ ($4.58\\text{ mmHg} = 0.61\\text{ kPa}$). At pressures below $P_t$, liquid water cannot exist in thermodynamic equilibrium. Lyophilization proceeds in three distinct stages:</p>\n<ol>\n  <li><strong>Freezing:</strong> The formulation is frozen below its glass transition temperature ($T_g' \\approx -32^\\circ\\text{C}$) to form crystalline ice.</li>\n  <li><strong>Primary Drying:</strong> Chamber pressure is evacuated to $0.10\\text{ mbar}$ ($0.075\\text{ mmHg} \\ll 4.58\\text{ mmHg}$), and shelf temperature is slowly raised while remaining below the collapse temperature ($T_c \\approx -30^\\circ\\text{C}$), driving endothermic sublimation ($\\Delta H_{\\text{sub}} = \\Delta H_{\\text{fus}} + \\Delta H_{\\text{vap}}$).</li>\n  <li><strong>Secondary Drying:</strong> Shelf temperature is warmed to $+25^\\circ\\text{C}$ under high vacuum to desorb residual bound water.</li>\n</ol>\n<p>Beyond the critical point ($T_c = 374^\\circ\\text{C}$, $P_c = 218\\text{ atm}$), water enters the supercritical fluid regime. Thermodynamic phase parameters were compiled (Table 7).</p>\n<table class=\"tbl\">\n  <caption>Table 7 Thermodynamic parameters, latent heats of phase transition, and operational states for lyophilization</caption>\n  <thead>\n    <tr><th>Phase / Transition</th><th>Specific Heat $c$ [J/(g&middot;&deg;C)]</th><th>Enthalpy $\\Delta H$ (kJ/mol)</th><th>Enthalpy $\\Delta H$ (J/g)</th><th>Transition Temp ($T$)</th><th>Operating Pressure ($P$)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Solid Ice</td><td>2.09</td><td>&mdash;</td><td>&mdash;</td><td>&minus;45&deg;C to 0&deg;C</td><td>1.00 atm</td></tr>\n    <tr><td>Melting (Fusion)</td><td>&mdash;</td><td>6.01</td><td>334</td><td>0&deg;C (273.15 K)</td><td>1.00 atm</td></tr>\n    <tr><td>Liquid Water</td><td>4.18</td><td>&mdash;</td><td>&mdash;</td><td>0&deg;C to 100&deg;C</td><td>1.00 atm</td></tr>\n    <tr><td>Vaporization (Boiling)</td><td>&mdash;</td><td>40.7</td><td>2260</td><td>100&deg;C (373.15 K)</td><td>1.00 atm</td></tr>\n    <tr><td>Sublimation</td><td>&mdash;</td><td>46.7</td><td>2594</td><td>&minus;30&deg;C (Primary Drying)</td><td>0.10 mbar (0.075 mmHg)</td></tr>\n    <tr><td>Desorption</td><td>&mdash;</td><td>52.0</td><td>2889</td><td>+25&deg;C (Secondary Drying)</td><td>0.05 mbar (0.038 mmHg)</td></tr>\n    <tr><td>Triple Point</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>+0.01&deg;C</td><td>4.58 mmHg (0.61 kPa)</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "How much total heat is required to warm 10.0 g of pure solid ice from -20.0 deg C to liquid water at +20.0 deg C at 1.00 atm?",
        "ch": [
          "Exactly 3760 J",
          "Exactly 4180 J",
          "Exactly 4590 J",
          "Exactly 5010 J"
        ],
        "a": 2,
        "e": "<strong>Multi-step heat calculation across sensible and latent phase transitions (Topic 388):</strong> Heating across a phase boundary requires summing sensible heat and latent heat: (1) Warming ice from $-20.0^\\circ\\text{C}$ to $0.0^\\circ\\text{C}$: $q_1 = m c_{\\text{ice}} \\Delta T = (10.0\\text{ g})(2.09\\text{ J/(g}\\cdot^\\circ\\text{C)})(20.0^\\circ\\text{C}) = 418\\text{ J}$. (2) Melting ice at $0.0^\\circ\\text{C}$: $q_2 = m \\Delta H_{\\text{fus}} = (10.0\\text{ g})(334\\text{ J/g}) = 3340\\text{ J}$. (3) Warming liquid water from $0.0^\\circ\\text{C}$ to $+20.0^\\circ\\text{C}$: $q_3 = m c_{\\text{water}} \\Delta T = (10.0\\text{ g})(4.18\\text{ J/(g}\\cdot^\\circ\\text{C)})(20.0^\\circ\\text{C}) = 836\\text{ J}$. Total heat input is: $q_{\\text{total}} = q_1 + q_2 + q_3 = 418 + 3340 + 836 = 4594\\text{ J} \\approx 4590\\text{ J}$.<br><br><em>Distractor Traps:</em><br>&bull; A calculates only the heat of fusion plus liquid warming ($3340 + 836 = 4176\\text{ J}$), omitting the sensible heat to warm ice from $-20^\\circ\\text{C}$ to $0^\\circ\\text{C}$.<br>&bull; B forgets the sensible heat to warm liquid water from $0^\\circ\\text{C}$ to $+20^\\circ\\text{C}$ ($418 + 3340 = 3758\\text{ J}$).<br>&bull; D uses the specific heat capacity of liquid water ($4.18\\text{ J/g}\\cdot^\\circ\\text{C}$) for both ice and water segments, overestimating sensible heat."
      },
      {
        "q": "Why must the chamber pressure during primary drying in lyophilization be maintained strictly below water's triple point pressure (4.58 mmHg)?",
        "ch": [
          "Pressures below 4.58 mmHg induce turbulent convective heat transfer that accelerates protein denaturation",
          "Lowering the pressure reduces the latent heat of sublimation to zero, eliminating external energy needs",
          "Pressures below 4.58 mmHg raise the boiling point of liquid water above the critical point of steam",
          "At pressures below 4.58 mmHg, liquid water cannot exist at equilibrium, ensuring direct solid-to-vapor sublimation"
        ],
        "a": 3,
        "e": "<strong>Triple point pressure boundary and lyophilization sublimation (Topics 388-389):</strong> On the pressure-temperature phase diagram of water, the triple point represents the unique thermodynamic condition ($T_t = 0.01^\\circ\\text{C}$, $P_t = 4.58\\text{ mmHg} = 0.61\\text{ kPa}$) where solid, liquid, and gas phases coexist in equilibrium. At any pressure below $4.58\\text{ mmHg}$, the liquid phase is thermodynamically unstable and cannot exist. Therefore, as heat is added to the frozen cake during primary drying under deep vacuum ($0.075\\text{ mmHg}$ ), solid ice sublimates directly into water vapor. If the chamber pressure were allowed to rise above $4.58\\text{ mmHg}$, the ice would melt into liquid water, causing cake collapse and protein denaturation.<br><br><em>Distractor Traps:</em><br>&bull; A asserts low pressure increases convective heat transfer, whereas vacuum diminishes convective gas heat transfer.<br>&bull; B falsely asserts lowering pressure reduces the latent heat of sublimation to zero.<br>&bull; C claims low pressure elevates the boiling point; reducing ambient pressure decreases boiling points."
      },
      {
        "q": "On a heating curve of water, why is the slope of the liquid water region shallower than the slope of the solid ice region?",
        "ch": [
          "Liquid water has a higher specific heat capacity than ice, requiring more heat input per degree of temperature increase",
          "Ice has stronger covalent O-H bonds than liquid water, allowing ice to absorb heat without changing temperature",
          "Liquid water undergoes continuous sublimation during heating, dissipating thermal energy as latent work",
          "Ice molecules possess greater translational degrees of freedom, facilitating rapid kinetic energy transfer"
        ],
        "a": 0,
        "e": "<strong>Heating curve slope and inverse heat capacity relationship (Topic 388):</strong> On a heating curve plotting temperature ($T$) on the vertical axis versus heat added ($q$) on the horizontal axis, the slope during a single-phase warming segment is given by: $\\text{Slope} = \\frac{\\Delta T}{q} = \\frac{1}{m c}$. Because slope is inversely proportional to specific heat capacity ($c$), a substance with a higher specific heat capacity exhibits a shallower slope. From Table 7, liquid water has a specific heat capacity of $4.18\\text{ J/(g}\\cdot^\\circ\\text{C)}$, which is twice as large as that of solid ice ($2.09\\text{ J/(g}\\cdot^\\circ\\text{C)}$). Liquid water requires twice as much heat energy per gram to achieve each degree Celsius of temperature rise, resulting in a slope that is half as steep.<br><br><em>Distractor Traps:</em><br>&bull; B confuses intramolecular covalent $\\text{O}-\\text{H}$ bonds with intermolecular hydrogen bonds and misinterprets specific heat.<br>&bull; C claims sublimation occurs in the liquid phase; sublimation is strictly the solid-to-gas transition.<br>&bull; D claims ice molecules have greater translational degrees of freedom; solid ice molecules are locked in a rigid lattice with vibrational modes only."
      },
      {
        "q": "By applying Hess's law to phase change enthalpies, what relationship governs the latent heat of sublimation (Delta H_sub)?",
        "ch": [
          "Delta H_sub = Delta H_vap - Delta H_fus",
          "Delta H_sub = Delta H_fus + Delta H_vap",
          "Delta H_sub = (Delta H_fus + Delta H_vap) / 2",
          "Delta H_sub = Delta H_fus x Delta H_vap"
        ],
        "a": 1,
        "e": "<strong>Hess's law of latent phase transitions (Topics 386, 388):</strong> Enthalpy is a thermodynamic state function, meaning the enthalpy change for a process depends only on the initial and final states, not the pathway. Direct sublimation from solid ice to water vapor ($\text{H}_2\text{O}(s) \\to \text{H}_2\text{O}(g)$) can be expressed as a two-step sequence: (1) melting ice to liquid water ($\text{H}_2\text{O}(s) \\to \text{H}_2\text{O}(l)$, $\\Delta H_{\\text{fus}} = 6.01\\text{ kJ/mol}$), followed by (2) vaporizing liquid water to gas ($\text{H}_2\text{O}(l) \\to \text{H}_2\text{O}(g)$, $\\Delta H_{\\text{vap}} = 40.7\\text{ kJ/mol}$). By Hess's law, the total enthalpy of sublimation is the exact sum of the two transitions: $\\Delta H_{\\text{sub}} = \\Delta H_{\\text{fus}} + \\Delta H_{\\text{vap}} = 6.01 + 40.7 = 46.7\\text{ kJ/mol}$ ($2594\\text{ J/g}$).<br><br><em>Distractor Traps:</em><br>&bull; A subtracts the heat of fusion from vaporization, directionally inverting Hess's law.<br>&bull; C averages the latent heats rather than summing them.<br>&bull; D takes the ratio of fusion to vaporization enthalpies."
      },
      {
        "q": "During the melting of ice at 0 deg C, heat is continuously added yet the measured temperature does not rise. What accounts for this behavior?",
        "ch": [
          "Heat added to the system is converted entirely into expanding the volume of water against atmospheric pressure",
          "The thermal energy is absorbed by surrounding air molecules via radiation rather than entering the ice crystal",
          "Added thermal energy is used to disrupt intermolecular hydrogen bonds rather than increasing molecular kinetic energy",
          "The enthalpy of fusion is an exothermic parameter that releases cooling waves to counteract heating elements"
        ],
        "a": 2,
        "e": "<strong>Microscopic kinetic versus potential energy during phase plateaus (Topic 388):</strong> Temperature is a macroscopic measure of the average translational kinetic energy of molecules in a system ($\\langle KE \\rangle = \\frac{3}{2} k_B T$). During a first-order phase change such as melting, the temperature remains strictly constant at the melting point ($0^\\circ\\text{C}$) because added thermal energy is not used to increase the kinetic velocity of the molecules. Instead, the heat energy (latent heat of fusion) does work against intermolecular forces, partially disrupting the rigid, open hexagonal hydrogen-bonding network of the ice lattice. This energy is stored as intermolecular potential energy as molecules transition from an ordered crystalline lattice to a disordered liquid state.<br><br><em>Distractor Traps:</em><br>&bull; A attributes the plateau to $PV$ work of expansion; volume changes during melting are tiny and account for negligible work.<br>&bull; B claims heat radiates into surrounding air rather than melting the ice sample.<br>&bull; D asserts the enthalpy of fusion is exothermic; melting is an endothermic process requiring continuous heat input."
      },
      {
        "q": "Above the thermodynamic critical point (T_c = 374 deg C, P_c = 218 atm), what unique physical property characterizes supercritical water?",
        "ch": [
          "It exhibits infinite surface tension, forming spherical droplets that completely resist mechanical shear",
          "It solidifies into a high-pressure crystalline ice lattice that is significantly denser than liquid water",
          "It separates into two distinct immiscible phases consisting of ionized hydrogen gas and oxygen radicals",
          "It expands to fill its container like a gas while possessing the high density and solvating power of a liquid"
        ],
        "a": 3,
        "e": "<strong>Supercritical fluid physical properties and phase boundaries (Topic 389):</strong> The critical point marks the terminal boundary of the liquid-gas coexistence curve. Above the critical temperature ($T_c$) and critical pressure ($P_c$), the meniscus separating liquid and gas disappears, merging into a single homogenous supercritical fluid phase. A supercritical fluid expands to fill the entire volume of its container and possesses gas-like transport properties (negligible surface tension, low viscosity, and high molecular diffusion rates), while maintaining a liquid-like density and high solvating power. This hybrid nature makes supercritical fluids exceptionally effective mobile phases in chromatography and green extraction processes.<br><br><em>Distractor Traps:</em><br>&bull; A falsely claims supercritical fluids exhibit infinite surface tension; supercritical fluids have zero surface tension.<br>&bull; B asserts supercritical water solidifies into crystalline ice; it exists at temperatures far above ambient boiling.<br>&bull; C claims water dissociates into elemental gases; supercritical water remains intact $\text{H}_2\text{O}$ molecules with altered dielectric properties."
      }
    ]
  },
  {
    "id": "exam_cp90_8_disc",
    "sec": "C/P",
    "topic": "C/P Standalone Discrete Questions",
    "sheet": 8,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_8",
    "passage": "<div class=\"ttl\">Item Set (Questions 43&ndash;52)</div>\n<p><strong>Directions:</strong> Questions 43&ndash;52 are standalone questions that are not based on a passage. Select the single best answer to each question.</p>",
    "qs": [
      {
        "d": true,
        "q": "In two-photon excitation microscopy of deep cerebral cortical neurons, why does using near-infrared pulsed lasers (e.g., 800 nm) permit imaging at greater depths than conventional single-photon confocal microscopy (e.g., 400 nm)?",
        "ch": [
          "Infrared light experiences significantly less Rayleigh scattering in tissue, and excitation is localized to the focal volume",
          "Infrared photons carry greater energy than ultraviolet photons, allowing them to penetrate dense cell membranes easily",
          "Infrared wavelengths cause continuous stimulated emission that eliminates out-of-focus background fluorescence entirely",
          "Two-photon absorption occurs uniformly along the entire illumination cone, maximizing the total fluorescence collected"
        ],
        "a": 0,
        "e": "<strong>Two-photon excitation physics and wavelength-dependent Rayleigh scattering (Topic 351):</strong> Biological tissues scatter light extensively due to microscopic refractive index variations between lipid membranes and aqueous cytosol. Elastic scattering follows Rayleigh and Mie regimes; Rayleigh scattering intensity is inversely proportional to the fourth power of wavelength ($I_{\\text{scatter}} \\propto 1/\\lambda^4$). Near-infrared light ($800\\text{ nm}$) scatters up to 16 times less than violet/blue light ($400\\text{ nm}$), allowing photons to penetrate $>1\\text{ mm}$ into deep brain tissue without loss of ballistic coherence. Furthermore, two-photon absorption probability depends quadratically on incident photon flux ($I^2$), confining fluorophore excitation strictly to the diffraction-limited focal volume and eliminating out-of-focus photobleaching and background autofluorescence.<br><br><em>Distractor Traps:</em><br>&bull; B claims infrared photons have greater energy than UV photons; by $E = hc/\\lambda$, longer IR wavelengths have lower photon energy.<br>&bull; C describes stimulated emission depletion (STED), which uses a second laser to quench fluorescence, not two-photon excitation.<br>&bull; D asserts excitation occurs along the entire illumination cone; two-photon excitation probability depends on $I^2$, confining excitation strictly to the focal volume."
      },
      {
        "d": true,
        "q": "During an abdominal ultrasound examination, why does the acoustic beam fail to penetrate deeply into cortical bone, creating an acoustic shadow behind the ribs?",
        "ch": [
          "Cortical bone has an acoustic impedance identical to soft tissue, allowing the ultrasound wave to transmit without reflection",
          "Bone exhibits a high acoustic attenuation coefficient and severe impedance mismatch, causing extensive reflection and absorption",
          "Sound waves travel much slower through bone than through soft tissue, which inverts the phase of transmitted ultrasound pulses",
          "Bone completely polarizes longitudinal sound waves into transverse shear waves that cannot be detected by piezoelectric crystals"
        ],
        "a": 1,
        "e": "<strong>Acoustic impedance mismatch and attenuation in bone (Topic 354):</strong> Acoustic reflection at a tissue boundary depends on the difference in acoustic impedance ($Z = \\rho v$). Soft tissue has an impedance of $Z \\approx 1.63 \\times 10^6\\text{ Rayls}$, whereas cortical bone has $Z \\approx 7.8 \\times 10^6\\text{ Rayls}$. The reflection coefficient at the soft tissue-bone interface is high ($R = [Z_2 - Z_1]^2 / [Z_2 + Z_1]^2 \\approx 43\\%$), reflecting a substantial portion of the incident ultrasound beam. Furthermore, bone possesses an exceptionally high acoustic attenuation coefficient ($\\alpha \\approx 20\\text{--}30\\text{ dB/cm at 5 MHz}$, compared to $0.5\\text{--}1.0\\text{ dB/(cm}\\cdot\\text{MHz)}$ for soft tissue), rapidly absorbing the transmitted mechanical acoustic energy as heat and casting an acoustic shadow beneath bone structures.<br><br><em>Distractor Traps:</em><br>&bull; A asserts cortical bone has acoustic impedance identical to soft tissue; bone has an impedance nearly 5-fold greater than soft tissue.<br>&bull; C claims acoustic velocity in bone is slower; sound propagates much faster in dense bone ($\\approx 3500\\text{ m/s}$) than in soft tissue ($\\approx 1540\\text{ m/s}$).<br>&bull; D claims bone completely polarizes longitudinal sound waves into shear waves that cannot be detected by ultrasound transducers."
      },
      {
        "d": true,
        "q": "Photoacoustic imaging combines optical contrast with ultrasonic spatial resolution. What primary physical mechanism generates the acoustic signal detected by the transducer?",
        "ch": [
          "Continuous laser irradiation induces photochemical ionization that releases high-frequency sound waves from biological tissue",
          "Fluorescent emission from endogenous chromophores undergoes destructive interference, producing detectable pressure fluctuations",
          "Short laser pulses are absorbed by chromophores, inducing transient thermoelastic expansion that launches ultrasonic pressure waves",
          "Coherent laser light reflects elastically off cell boundaries, creating standing shear waves that resonate inside tissue cavities"
        ],
        "a": 2,
        "e": "<strong>Thermoelastic expansion in photoacoustic ultrasound generation (Topic 358):</strong> Photoacoustic imaging (PAI) hybridizes optical excitation with acoustic detection. A biological specimen is illuminated with short nanosecond laser pulses ($t < 10\\text{ ns}$, satisfying thermal and stress confinement conditions). Endogenous light-absorbing chromophores (such as hemoglobin, melanin, or lipids) absorb the optical energy, producing a localized, rapid rise in temperature (on the order of millikelvins). This rapid temperature jump causes instantaneous thermoelastic expansion of the absorbing volume, launching transient mechanical acoustic pressure waves (ultrasound) that propagate through tissue with minimal scattering and are detected by piezoelectric ultrasonic transducers to reconstruct high-resolution optical absorption maps.<br><br><em>Distractor Traps:</em><br>&bull; A claims continuous lasers induce photochemical ionization; photoacoustic imaging uses non-ionizing nanosecond pulsed light.<br>&bull; B misattributes ultrasound generation to optical fluorescence interference.<br>&bull; D claims coherent optical reflection generates acoustic waves, ignoring optical absorption and thermoelastic expansion."
      },
      {
        "d": true,
        "q": "Stimulated Emission Depletion (STED) microscopy achieves super-resolution imaging beyond the classical Abbe diffraction limit. How does the STED donut beam function?",
        "ch": [
          "It suppresses fluorescence at the periphery of the focal spot via stimulated emission, leaving a sub-diffraction central emitting area",
          "It selectively excites fluorophores in the outer ring while photobleaching fluorophores located within the central coordinate null",
          "It increases the numerical aperture of the objective lens by altering the physical refractive index of the immersion oil medium",
          "It forces fluorophores into long-lived triplet states, allowing single-molecule stochastic blinking across sequential camera frames"
        ],
        "a": 0,
        "e": "<strong>Stimulated Emission Depletion (STED) super-resolution mechanics (Topic 362):</strong> In STED microscopy, a standard diffraction-limited circular excitation laser pulse is spatially overlaid with a red-shifted, doughnut-shaped depletion laser beam that features a central zero-intensity coordinate null. Fluorophores at the periphery of the diffraction spot are intercepted by the high-intensity STED doughnut beam before they can spontaneously fluoresce, forcing them to undergo stimulated emission down to the ground state at the longer depletion wavelength (which is spectrally filtered out). Only fluorophores situated within the sub-diffraction central null can emit spontaneous fluorescence, effectively shrinking the fluorescence point spread function (PSF) and yielding lateral resolutions below $20\\text{ nm}$, breaking Abbe's diffraction barrier.<br><br><em>Distractor Traps:</em><br>&bull; B confuses STED depletion with outer-ring excitation and center-spot photobleaching.<br>&bull; C asserts STED increases objective lens numerical aperture; STED modulates fluorophore emission states without altering physical lens optics.<br>&bull; D describes single-molecule localization microscopy (STORM/PALM) photo-switching rather than STED stimulated depletion."
      },
      {
        "d": true,
        "q": "In a Fourier Transform Infrared (FTIR) spectrometer, what optical component produces the interference pattern (interferogram) that is converted into an absorbance spectrum?",
        "ch": [
          "A diffraction grating that angularly separates polychromatic infrared light into distinct discrete monochromatic wavelengths",
          "A Michelson interferometer with a beam splitter and a moving mirror that systematically modulates the optical path difference",
          "A cylindrical glass lens that focuses transmitted infrared radiation onto a photodiode array to eliminate spherical aberration",
          "A polarizing crystal that selectively filters out transverse electric field vectors perpendicular to the biological sample axis"
        ],
        "a": 1,
        "e": "<strong>Michelson interferometer optics in FTIR spectroscopy (Topic 363):</strong> Unlike dispersive infrared spectrometers that use diffraction gratings to isolate individual wavelengths sequentially, an FTIR spectrometer utilizes a Michelson interferometer. A collimated broadband infrared beam strikes a 50:50 beam splitter, dividing into two perpendicular beams: one reflects off a stationary fixed mirror, while the other reflects off a moving mirror translating at a constant velocity. When recombined at the beam splitter, an optical path difference ($\\delta = 2x$) is established, causing constructive and destructive wave interference across all wavelengths simultaneously. This yields an interferogram in the spatial domain, which is converted into a frequency/wavenumber absorption spectrum via the mathematical Fourier transform.<br><br><em>Distractor Traps:</em><br>&bull; A describes dispersive infrared spectrometers that use diffraction gratings or prisms, not FTIR interferometers.<br>&bull; C describes refractive lens focusing to reduce spherical aberration, which does not generate an optical interferogram.<br>&bull; D describes linear polarization filters used in circular dichroism or ellipsometry."
      },
      {
        "d": true,
        "q": "In a clinical gamma camera used for nuclear scintigraphy, what sequence of physical events converts an incident gamma photon into a detectable electronic signal?",
        "ch": [
          "The gamma photon directly ionizes dynode plates, which generate an avalanche of secondary gamma rays detected by a photocathode",
          "The gamma photon undergoes Bragg diffraction within a collimator, which reflects polarized electrons into a semiconductor diode",
          "The gamma photon creates an acoustic pressure wave in a piezoelectric crystal, which discharges a measurable capacitive current",
          "The gamma photon excites a NaI(Tl) crystal to emit visible photons, which release photoelectrons amplified across a dynode chain"
        ],
        "a": 3,
        "e": "<strong>Scintillation crystals and PMT amplification in gamma cameras (Topic 365):</strong> A gamma camera detects high-energy photons (e.g., $140\\text{ keV}$ gammas from $^{99\\text{m}}\\text{Tc}$) through a two-step scintillation and electron multiplication cascade. First, the incident gamma photon passes through a lead collimator and deposits its energy into a thallium-doped sodium iodide [$\\text{NaI(Tl)}$] scintillation crystal via photoelectric or Compton interactions, producing a localized flash of thousands of visible light photons. These visible photons strike the photocathode of a photomultiplier tube (PMT), releasing primary electrons via the photoelectric effect. An accelerating electric field directs these photoelectrons through a series of secondary dynodes, where secondary electron emission amplifies the signal $10^6$-fold into a measurable electronic voltage pulse.<br><br><em>Distractor Traps:</em><br>&bull; A claims gamma rays directly ionize dynodes to emit secondary gamma rays, omitting the scintillation crystal and photocathode.<br>&bull; B confuses gamma ray scintillation with X-ray Bragg crystal diffraction.<br>&bull; C confuses scintillation detection with piezoelectric acoustic pressure transducers."
      },
      {
        "d": true,
        "q": "According to the Abbe diffraction limit (d = lambda / [2 NA]), what is the minimum resolvable lateral distance for a microscope using violet light (lambda = 420 nm) and an oil-immersion objective (NA = 1.40)?",
        "ch": [
          "Exactly 150 nm",
          "Exactly 300 nm",
          "Exactly 420 nm",
          "Exactly 588 nm"
        ],
        "a": 0,
        "e": "<strong>Calculation of Abbe diffraction limit of lateral optical resolution (Topic 366):</strong> Ernst Abbe's diffraction limit describes the smallest lateral separation distance ($d$) between two point light sources that can still be distinguished as distinct entities: $d = \\frac{\\lambda}{2\\,\\text{NA}} = \\frac{\\lambda}{2 n \\sin\\alpha}$, where $\\lambda$ is the illumination wavelength in vacuum and $\\text{NA}$ is the numerical aperture of the objective lens. Substituting the given values ($\\lambda = 420\\text{ nm}$ and $\\text{NA} = 1.40$): $d = \\frac{420\\text{ nm}}{2(1.40)} = \\frac{420\\text{ nm}}{2.80} = 150\\text{ nm}$. Structures separated by less than $150\\text{ nm}$ merge into a single diffraction-blurred spot due to wave diffraction.<br><br><em>Distractor Traps:</em><br>&bull; B omits the factor of 2 in the Abbe denominator, computing $d = 420 / 1.40 = 300\\text{ nm}$.<br>&bull; C reports the illumination wavelength itself (420 nm).<br>&bull; D multiplies the wavelength by $\\text{NA}$ ($420 \\times 1.40 = 588\\text{ nm}$), inverting the Abbe equation."
      },
      {
        "d": true,
        "q": "In clinical laboratory testing for immunoglobulins, how does nephelometry differ fundamentally from turbidimetry in its optical measurement geometry?",
        "ch": [
          "Nephelometry measures the reduction in light intensity transmitted directly in line with the incident beam (180 degree detection)",
          "Nephelometry measures light scattered at an angle to the incident beam, providing superior sensitivity for dilute complexes",
          "Nephelometry requires radioactive isotopic labeling of proteins, whereas turbidimetry relies entirely on fluorescent antibody dyes",
          "Nephelometry measures refracted light along the axial path, whereas turbidimetry measures light absorption at right angles"
        ],
        "a": 1,
        "e": "<strong>Geometric optical distinction between nephelometry and turbidimetry (Topic 368):</strong> Both nephelometry and turbidimetry quantify macromolecular immune complexes (e.g., antigen-antibody aggregates) suspended in solution, but they employ distinct optical detection geometries. Turbidimetry aligns the photodetector directly on-axis with the incident light source ($180^\\circ$), measuring the reduction in transmitted light caused by particle scattering and absorption (governed by the Beer-Lambert relationship). In contrast, nephelometry places the photodetector at an angle (typically $70^\\circ$ to $90^\\circ$) off-axis from the incident beam, measuring scattered light against a zero-background field. Because it detects light against a dark background, nephelometry offers substantially higher signal-to-noise ratio and sensitivity for low-concentration serum proteins.<br><br><em>Distractor Traps:</em><br>&bull; A describes turbidimetry, which measures transmitted light attenuation in the forward direction ($180^\\circ$ detection).<br>&bull; C claims nephelometry requires radioactive isotopes; nephelometry is a label-free optical scattering assay.<br>&bull; D claims nephelometry measures refracted light along the axial path and turbidimetry measures light absorption at right angles."
      },
      {
        "d": true,
        "q": "Optical tissue clearing methods (such as CLARITY) render intact biological organs transparent for deep 3D fluorescence microscopy primarily by:",
        "ch": [
          "Dissolving all intracellular proteins and nucleic acids, leaving behind an empty scaffold of transparent lipid membranes",
          "Increasing the numerical aperture of objective lenses so that light rays undergo total internal reflection within the coverslip",
          "Removing scatter-inducing membrane lipids and equilibrating tissue with a high-refractive-index solution matching structural proteins",
          "Applying intense electrical fields that polarize water molecules, preventing them from absorbing visible excitation photons"
        ],
        "a": 2,
        "e": "<strong>Refractive index matching in tissue clearing for 3D microscopy (Topic 369):</strong> Biological tissue opacity is caused primarily by optical scattering, which occurs when light encounters repeated interfaces between materials of differing refractive indices ($n$). In native tissue, lipid membranes have high refractive indices ($n \\approx 1.46\\text{--}1.50$), whereas the aqueous cytosol has a much lower refractive index ($n \\approx 1.33$). In tissue clearing protocols (e.g., CLARITY, BABB, 3DISCO), scatter-inducing membrane lipids are extracted while preserving structural proteins and fluorophores inside a hydrogel mesh. The tissue is then infused with a clearing agent whose refractive index matches that of protein and glass ($n \\approx 1.45\\text{--}1.52$). Eliminating refractive index mismatches abolishes internal light scattering, rendering whole organs optically transparent.<br><br><em>Distractor Traps:</em><br>&bull; A asserts that clearing dissolves proteins and nucleic acids, which would destroy cellular architecture and fluorescent antibodies.<br>&bull; B confuses objective lens numerical aperture with tissue clearing specimen preparation.<br>&bull; D claims tissue clearing applies electrical fields to polarize water, confusing clearing with gel electrophoresis."
      },
      {
        "d": true,
        "q": "Transition metal complex [Fe(CN)6]4- is diamagnetic, whereas [Fe(H2O)6]2+ is paramagnetic with four unpaired electrons. What explains this difference?",
        "ch": [
          "Cyanide is a weak-field ligand that creates a small crystal field splitting energy, favoring a high-spin electron configuration",
          "Water is a strong-field ligand that forces all d-electrons into higher-energy eg orbitals to minimize core electron shielding",
          "Iron exists in the +3 oxidation state in the hexacyano complex, but exists in the +1 oxidation state in the hydrated complex",
          "Cyanide is a strong-field ligand causing large d-orbital splitting that forces all six d-electrons to pair in lower t2g orbitals"
        ],
        "a": 3,
        "e": "<strong>Crystal field theory and spin states in transition metal complexes (Topic 378):</strong> Both $[\\text{Fe(CN)}_6]^{4-}$ and $[\\text{Fe(H}_2\\text{O)}_6]^{2+}$ contain iron in the $+2$ oxidation state with a $d^6$ electron configuration ($[\\text{Ar}]\\,3d^6$). In an octahedral crystal field, the five degenerate $d$ orbitals split into lower $t_{2g}$ and higher $e_g$ energy levels separated by crystal field splitting energy $\\Delta_o$. Cyanide ($\\text{CN}^-$) is a classic strong-field ligand high in the spectrochemical series, inducing a large splitting energy ($\\Delta_o > P$, where $P$ is electron pairing energy). This forces all six $d$-electrons to pair up in the lower $t_{2g}$ orbitals ($t_{2g}^6 e_g^0$), yielding zero unpaired electrons and a diamagnetic state (weakly repelled by a magnetic field). In contrast, water is a weak-field ligand ($\\Delta_o < P$), resulting in a high-spin configuration ($t_{2g}^4 e_g^2$) with four unpaired electrons, creating strong paramagnetism (attraction to magnetic fields).<br><br><em>Distractor Traps:</em><br>&bull; A claims cyanide is a weak-field ligand; cyanide ($\text{CN}^-$) is a classic strong-field ligand near the top of the spectrochemical series.<br>&bull; B claims water is a strong-field ligand that forces electrons into $e_g$ orbitals; water is a weak-field ligand and $e_g$ is higher in energy than $t_{2g}$.<br>&bull; C claims iron is in the +3 oxidation state in the hexacyano complex; iron is in the +2 oxidation state in both complexes ($\text{Fe}^{2+}$)."
      }
    ]
  }
];

if (typeof window !== 'undefined') {
  window.EXAM_CP90_8 = EXAM_CP90_8;
}
if (typeof globalThis !== 'undefined') {
  globalThis.EXAM_CP90_8 = EXAM_CP90_8;
}
