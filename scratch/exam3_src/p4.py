# Passage 4: Topic 777 — Visual Cortex Architecture: Feature Detection & Receptive Fields
# Keys: 2, 3, 0, 1, 2, 3

p4_data = {
    "id": "exam_ps90_3_p4",
    "sec": "P/S",
    "topic": "Visual Cortex Architecture: Feature Detection & Receptive Fields",
    "sheet": 4,
    "label": "Psychological, Social, and Biological Foundations of Behavior",
    "examId": "ps90_3",
    "passage": """<div class="ttl">Passage 4 (Questions 19&ndash;24)</div>
<p>Primary visual cortex (striate cortex, Area 17 or V1) transforms concentric center-surround thalamic inputs into representations of oriented contours, moving edges, and complex geometric features. In their foundational work, David Hubel and Torsten Wiesel established that striate cortex is organized into a modular functional architecture composed of orientation columns, ocular dominance columns, and cytochrome oxidase-rich metabolic patches termed \"blobs.\" Within this modular network, cortical neurons are classified into a hierarchical continuum based on receptive field physiology: simple cells, complex cells, and hypercomplex (end-stopped) cells.</p>
<p>Simple cells reside predominantly in cortical input layers (layer $4\\text{B}$ and layer 6). They possess distinct, spatially segregated subregions of excitation (ON) and inhibition (OFF) arranged in parallel rectilinear bands. A simple cell fires maximally to a stationary or moving bar of light at a specific orientation positioned precisely over its ON zone; shifting the stimulus slightly into the adjacent OFF zone abolishes firing. Hubel and Wiesel proposed a feedforward model wherein the receptive field of a simple cell is constructed from the convergent excitatory input of a row of LGN relay neurons whose circular receptive field centers align along a spatial axis. Complex cells reside predominantly in layers 2, 3, and 5. They respond robustly to an oriented bar of light anywhere within their receptive field (exhibiting spatial phase/position invariance) and frequently display direction selectivity, firing vigorously when an edge moves in a preferred direction but remaining silent when it moves in the reverse (null) direction. Complex cells are built from the convergent input of multiple simple cells sharing identical orientation preferences.</p>
<p>Hypercomplex (end-stopped) cells exhibit orientation and direction tuning, but their firing rate decreases precipitously when the length of the stimulus bar extends beyond an optimal boundary, mediated by flanking inhibitory zones. Neurophysiologists recorded extracellular action potentials from four cortical units (Units 1&ndash;4) in cat striate cortex while presenting oriented light bars under varying spatial, length, and directional configurations, as reported in Table 1.</p>
<table class="tbl">
  <caption>Table 1 Extracellular spike discharge rates (Hz) of striate cortical units under varied optical stimulus configurations</caption>
  <thead>
    <tr><th>Cortical Unit</th><th>Spontaneous Baseline (Hz)</th><th>Stimulus 1: Optimal Bar at Center</th><th>Stimulus 2: 1.5&deg; Shifted Bar</th><th>Stimulus 3: Elongated Bar (2&times; Length)</th><th>Stimulus 4: Preferred Direction Sweep</th><th>Stimulus 5: Null Direction Sweep</th></tr>
  </thead>
  <tbody>
    <tr><td>Unit 1</td><td>2.1</td><td>54.6 (Robust response)</td><td>1.8 (No response)</td><td>53.8 (Robust response)</td><td>28.4</td><td>27.1</td></tr>
    <tr><td>Unit 2</td><td>3.4</td><td>48.2 (Robust response)</td><td>47.6 (Robust response)</td><td>49.0 (Robust response)</td><td>82.5 (High discharge)</td><td>4.1 (Suppressed)</td></tr>
    <tr><td>Unit 3</td><td>1.9</td><td>42.1 (Robust response)</td><td>41.5 (Robust response)</td><td>4.8 (Inhibited)</td><td>76.3 (High discharge)</td><td>3.9 (Suppressed)</td></tr>
    <tr><td>Unit 4</td><td>5.2</td><td>5.8 (No selectivity)</td><td>5.4 (No selectivity)</td><td>5.1 (No selectivity)</td><td>5.5</td><td>5.2</td></tr>
  </tbody>
</table>""",
    "qs": [
      {
        "q": "Based on the electrophysiological responses in Table 1, which functional cell classifications correctly identify Unit 1, Unit 2, and Unit 3, respectively?",
        "ch": [
          "Unit 1 is an end-stopped cell; Unit 2 is a simple cell; Unit 3 is a complex cell.",
          "Unit 1 is a complex cell; Unit 2 is an end-stopped cell; Unit 3 is a simple cell.",
          "Unit 1 is a simple cell; Unit 2 is a complex cell; Unit 3 is an end-stopped cell.",
          "Unit 1 is a simple cell; Unit 2 is an end-stopped cell; Unit 3 is a complex cell."
        ],
        "a": 2,
        "e": "<strong>Functional classification of V1 cortical receptive fields:</strong><br>&bull; <i>Unit 1</i> is a <strong>simple cell</strong>: It responds robustly to an oriented bar at the center of its receptive field ($54.6\\text{ Hz}$), but shifting the stimulus by $1.5^\\circ$ completely silences it ($1.8\\text{ Hz}$), demonstrating strict position/phase sensitivity and lack of position invariance. Elongating the bar does not suppress firing ($53.8\\text{ Hz}$), ruling out end-stopping.<br>&bull; <i>Unit 2</i> is a <strong>complex cell</strong>: It fires vigorously to the oriented bar both at the center ($48.2\\text{ Hz}$) and when shifted $1.5^\\circ$ ($47.6\\text{ Hz}$), demonstrating classic spatial position invariance. Furthermore, it displays strong direction selectivity ($82.5\\text{ Hz}$ in preferred vs $4.1\\text{ Hz}$ in null direction) and is not inhibited by elongation ($49.0\\text{ Hz}$).<br>&bull; <i>Unit 3</i> is an <strong>end-stopped (hypercomplex) cell</strong>: Like a complex cell, it shows position invariance ($42.1\\text{ Hz}$ vs $41.5\\text{ Hz}$), but when the stimulus bar is elongated past the receptive field boundaries, its firing rate plummets from $42.1\\text{ Hz}$ down to $4.8\\text{ Hz}$ due to flanking end-inhibition.<br><br><em>Distractor Traps:</em><br>&bull; A, B, and D misassign these distinctive physiological properties."
      },
      {
        "q": "According to the classic Hubel and Wiesel hierarchical feedforward model, how does the oriented, linear ON/OFF receptive field of a V1 simple cell originate?",
        "ch": [
          "From recurrent horizontal collateral excitation between thousands of direction-selective complex cells in cortical layer 2/3.",
          "From direct descending inhibitory feedback projecting from the frontal eye fields down to the primary visual cortex input layer.",
          "From diffuse paracrine release of acetylcholine across ocular dominance columns activating muscarinic receptors on stellate cells.",
          "From the convergent excitatory alignment of multiple LGN relay cells whose circular center receptive fields share a linear spatial axis."
        ],
        "a": 3,
        "e": "<strong>Hubel and Wiesel feedforward model of simple cell receptive fields:</strong> Individual lateral geniculate nucleus (LGN) relay neurons have concentric, non-oriented, center-surround receptive fields (circular ON-center or OFF-center). Hubel and Wiesel proposed that the orientation tuning of a V1 simple cell emerges structurally from the convergent feedforward wiring of multiple LGN afferents. Specifically, several LGN neurons whose receptive field centers are arranged along a straight line in visual space project their axons to converge monosynaptically onto a single simple cell in layer 4B. The simultaneous activation of these aligned circular centers by an oriented bar of light produces cooperative spatial summation that depolarizes the simple cell to threshold. The simple cell's antagonistic flanking OFF subregions are generated by the flanking inhibitory surrounds of the aligned LGN inputs or feedforward inhibitory interneurons.<br><br><em>Distractor Traps:</em><br>&bull; A reverses the hierarchy: complex cells receive input from simple cells, not vice versa.<br>&bull; B describes frontal descending motor feedback.<br>&bull; C invents diffuse cholinergic paracrine mechanisms that cannot account for precise retinotopic orientation tuning."
      },
      {
        "q": "Unit 3 in Table 1 fired robustly to a stationary oriented bar (42.1 Hz) but its firing rate plummeted to 4.8 Hz when the bar was elongated beyond the receptive field. What perceptual feature is this neuron specialized to detect?",
        "ch": [
          "Corners, line terminations, and curvature boundaries where oriented contours end or bend sharply within the visual scene.",
          "Infinite uniform surfaces of homogeneous luminance that extend across the entire peripheral visual field without contrast.",
          "High-frequency chromatic flicker and rapid whole-field luminance oscillations generated by high-speed stroboscopic flashes.",
          "Absolute horizontal retinal disparity between corresponding points on the retinas used to compute stereoscopic depth cues."
        ],
        "a": 0,
        "e": "<strong>End-stopping and contour boundary detection:</strong> Hypercomplex or end-stopped cells are characterized by length summation followed by end-inhibition. While a simple or complex cell fires progressively more or maintains its plateau as a stimulus bar is lengthened, an end-stopped cell fires maximally only when the stimulus fits within its optimal excitatory length. If the bar extends beyond this length into flanking inhibitory regions, the cell's firing is suppressed (in Table 1, dropping from $42.1\\text{ Hz}$ to $4.8\\text{ Hz}$). Consequently, end-stopped cells do not respond well to continuous straight lines extending across space. Instead, they fire selectively when an edge terminates, turns, or bends within their receptive field. This makes them the primary feature detectors for line terminations, sharp angles, corners, intersections, and surface curvature—critical elementary primitives for visual object parsing and shape segmentation.<br><br><em>Distractor Traps:</em><br>&bull; B describes the exact opposite of what end-stopped cells detect (they are completely silenced by broad surfaces).<br>&bull; C describes temporal flicker detection mediated by magnocellular neurons.<br>&bull; D describes binocular disparity-tuned stereoscopic neurons."
      },
      {
        "q": "If a newborn kitten undergoes unilateral monocular eyelid suture (monocular deprivation) for several months during early postnatal development, what physiological outcome is observed in primary visual cortex?",
        "ch": [
          "Equal binocular representation is preserved because ocular dominance column architecture is genetically fixed and resistant to visual input.",
          "Cortical neurons become almost exclusively responsive to the non-deprived open eye, as open-eye axon terminals expand into deprived territory.",
          "Striate cortex completely degenerates into scar tissue, resulting in total permanent bilateral blindness across all cortical layers.",
          "Deprived-eye ocular dominance columns quadruple in physical surface area due to compensatory homeostatic sprouting of inhibitory synapses."
        ],
        "a": 1,
        "e": "<strong>Critical periods and ocular dominance plasticity:</strong> In normal adult primary visual cortex, layer 4 consists of alternating bands of inputs called ocular dominance columns, with neurons in layers 2/3 and 5/6 receiving binocular inputs driven equally by both eyes. Hubel and Wiesel demonstrated that the development and maintenance of these binocular columns depend strictly on patterned visual experience during a well-defined postnatal <i>critical period</i>. When an animal undergoes monocular deprivation during this critical window, active competition between afferents ensues. Because the closed eye transmits only random noise while the open eye transmits patterned, correlated visual signals, the thalamocortical axon terminals representing the open eye sprout and expand into adjacent territory. Concurrently, the axonal branches representing the deprived eye retract and atrophy. As a result, the deprived-eye ocular dominance columns shrink dramatically, and almost all cortical neurons in V1 become exclusively responsive to stimulation of the open eye (ocular dominance shift). The deprived eye becomes permanently functionally blind (amblyopic) at the cortical level even though its retinal anatomy remains normal.<br><br><em>Distractor Traps:</em><br>&bull; A is false: ocular dominance columns are highly plastic and dependent on visual experience.<br>&bull; C is exaggerated: only the deprived eye loses cortical driving, while open-eye vision is intact or enhanced.<br>&bull; D claims the deprived columns expand, which is the exact reverse of reality."
      },
      {
        "q": "Unit 2 demonstrated robust firing to a rightward sweep of an oriented bar (82.5 Hz) but was nearly silent to a leftward sweep (4.1 Hz). What neurobiological mechanism generates this direction selectivity?",
        "ch": [
          "Slower photopigment regeneration in nasal photoreceptors creating an asymmetric delay in retinal ganglion cell axonal conduction.",
          "Retrograde nitric oxide gas diffusion from postsynaptic pyramidal dendrites selectively inactivating presynaptic glutamate vesicles.",
          "Spatially asymmetric feedforward inhibition from GABAergic cortical interneurons that vetoes excitation during motion in the null direction.",
          "Selective opening of voltage-gated sodium channels that only activate when light photons enter the cornea at perpendicular angles."
        ],
        "a": 2,
        "e": "<strong>Direction selectivity and asymmetric feedforward inhibition:</strong> Direction-selective cortical neurons (such as Unit 2, which fires at $82.5\\text{ Hz}$ in the preferred direction and drops to $4.1\\text{ Hz}$ in the null direction) respond to motion in one direction while suppressing responses to motion in the opposite direction. The prevailing neurobiological model for cortical direction selectivity relies on spatially and temporally asymmetric feedforward inhibition (the Barlow-Levick veto model adapted for cortex). As a stimulus moves across the receptive field, it activates sensory inputs sequentially. For preferred-direction motion, excitatory inputs arrive first and depolarize the cell to threshold before any delayed inhibition can catch up. Conversely, during null-direction motion, the leading edge of the stimulus first activates GABAergic inhibitory interneurons located on the flank of the receptive field. These inhibitory interneurons deliver powerful, shunting GABAergic inhibition to the postsynaptic pyramidal cell just before or simultaneously with the excitatory inputs, vetoing action potential generation.<br><br><em>Distractor Traps:</em><br>&bull; A invents asymmetrical nasal photopigment delays.<br>&bull; B describes retrograde nitric oxide signaling (involved in LTP, not millisecond direction vetoing).<br>&bull; D is optical/biophysical nonsense (photons strike the retina, not voltage-gated channels directly)."
      },
      {
        "q": "Histological staining of primary visual cortex layers 2 and 3 reveals periodic cylindrical patches rich in cytochrome oxidase (blobs). What functional characteristic distinguishes blob neurons from interblob neurons?",
        "ch": [
          "Blob neurons exhibit sharp orientation tuning and direction selectivity, but possess no chromatic opponency or sensitivity.",
          "Blob neurons process high spatial frequency textures and stereoscopic depth disparities, but lack mitochondrial metabolic enzymes.",
          "Blob neurons receive exclusive magnocellular afferents from LGN layer 1 and project directly to posterior parietal cortex.",
          "Blob neurons display unoriented, wavelength-selective chromatic sensitivity, whereas interblob neurons show sharp orientation tuning."
        ],
        "a": 3,
        "e": "<strong>Cytochrome oxidase blobs vs interblob compartments:</strong> In layers 2 and 3 of primary visual cortex, staining for the mitochondrial metabolic enzyme cytochrome oxidase reveals a repeating lattice of peg-like cylindrical pillars termed <i>blobs</i>, separated by <i>interblob</i> regions. Blob and interblob compartments serve distinct functional roles in early visual processing:<br>&bull; <strong>Blobs:</strong> Contain neurons that are metabolically hyperactive and receive koniocellular and parvocellular inputs (via layer $4\\text{C}\\beta$). They exhibit <i>no orientation selectivity</i> (unoriented receptive fields), but display rich, circular color opponency (red-green and blue-yellow). Blobs project to the thin stripes of extrastriate area V2, feeding the ventral color stream.<br>&bull; <strong>Interblobs:</strong> Contain neurons with high spatial resolution and <i>sharp orientation selectivity</i>, responding to edges and borders while exhibiting little to no chromatic sensitivity. Interblobs project to the pale (interstripe) zones of V2, subserving form and shape analysis.<br><br><em>Distractor Traps:</em><br>&bull; A describes interblob neurons, not blobs.<br>&bull; B is contradictory because blobs are defined by their high concentration of cytochrome oxidase.<br>&bull; C describes magnocellular/layer 4B pathways projecting to thick stripes of V2 and MT."
      }
    ]
}
