# Passage 7: Topic 780 — Visual Perceptual Constancies: Size, Shape & Color Constancy
# Keys: 0, 1, 2, 3, 0, 1

p7_data = {
    "id": "exam_ps90_3_p7",
    "sec": "P/S",
    "topic": "Visual Perceptual Constancies: Size, Shape & Color Constancy",
    "sheet": 7,
    "label": "Psychological, Social, and Biological Foundations of Behavior",
    "examId": "ps90_3",
    "passage": """<div class="ttl">Passage 7 (Questions 37&ndash;42)</div>
<p>Visual perceptual constancies refer to the cognitive mechanisms by which the brain maintains stable, invariant perceptions of an object's intrinsic physical properties&mdash;such as its size, geometric shape, color, and achromatic lightness&mdash;despite continuous, drastic fluctuations in the proximal sensory stimuli reaching the retina. These constancies reflect top-down inferential neurocomputations that integrate raw retinal input with contextual spatial depth and illumination cues.</p>
<p><i>Size constancy</i> maintains stable object size perception across varying viewing distances, governed by the size-distance invariance hypothesis: perceived physical size is computed as the product of retinal image size and perceived distance ($S_{\\text{perceived}} = k \\times [S_{\\text{retina}} \\times D_{\\text{perceived}}]$). When an object recedes, its retinal projection shrinks linearly ($S_{\\text{retina}} \\propto 1/D$), but an increase in perceived distance compensates, preserving size constancy. A related psychophysical phenomenon is <i>Emmert's Law</i>: the perceived physical size of an afterimage (which has a fixed, invariant physical footprint on the retina) scales in direct linear proportion to the physical distance of the projection plane onto which it is viewed ($S_{\\text{afterimage}} \\propto D_{\\text{surface}}$). Similarly, <i>shape constancy</i> preserves the perceived true geometry of an object (e.g., a rectangular tabletop or doorway) even when viewed at an oblique slant that casts an acute trapezoidal or elliptical projection onto the retinal photoreceptor mosaic.</p>
<p><i>Color constancy</i> allows surface colors to appear invariant despite dramatic shifts in ambient spectral illumination (e.g., viewing a red apple under midday sun vs fluorescent bulbs). In his Retinex theory, Edwin Land demonstrated that color constancy cannot be explained by local cone excitations alone; instead, cortical area V4 compares reflectance ratios across surrounding spatial surfaces within three independent wavebands. Similarly, Hans Wallach's ratio rule governs <i>lightness constancy</i>: perceived surface lightness (black, gray, white) is determined not by absolute physical photon flux (luminance), but by the contrast ratio between the surface and its immediate surroundings. Cognitive scientists evaluated size and color constancies in healthy adult controls and neurological patients with focal bilateral lesions to extrastriate area V4, as summarized in Table 1.</p>
<table class="tbl">
  <caption>Table 1 Afterimage diameter scaling and psychophysical color matching accuracy under varying ambient illuminants across subject cohorts</caption>
  <thead>
    <tr><th>Subject Cohort</th><th>Afterimage Projection Plane (m)</th><th>Perceived Afterimage Diameter (cm)</th><th>Ambient Illuminant Condition</th><th>Target Color Matching Accuracy (%)</th><th>V4 fMRI BOLD (% of baseline)</th></tr>
  </thead>
  <tbody>
    <tr><td>Healthy Controls</td><td>1.0 m</td><td>4.2 cm</td><td>Illuminant A (Daylight, 6500 K)</td><td>96.4%</td><td>100%</td></tr>
    <tr><td>Healthy Controls</td><td>2.0 m</td><td>8.3 cm</td><td>Illuminant B (Tungsten, 2800 K)</td><td>94.2%</td><td>144%</td></tr>
    <tr><td>Healthy Controls</td><td>4.0 m</td><td>16.7 cm</td><td>Illuminant B (Tungsten, 2800 K)</td><td>93.9%</td><td>146%</td></tr>
    <tr><td>Area V4 Lesion Cohort</td><td>1.0 m</td><td>4.1 cm</td><td>Illuminant A (Daylight, 6500 K)</td><td>88.6% (Near normal)</td><td>&mdash; (Ablated)</td></tr>
    <tr><td>Area V4 Lesion Cohort</td><td>2.0 m</td><td>8.4 cm</td><td>Illuminant B (Tungsten, 2800 K)</td><td>25.4% (Severe deficit)</td><td>&mdash; (Ablated)</td></tr>
    <tr><td>Area V4 Lesion Cohort</td><td>4.0 m</td><td>16.6 cm</td><td>Illuminant B (Tungsten, 2800 K)</td><td>24.8% (Severe deficit)</td><td>&mdash; (Ablated)</td></tr>
  </tbody>
</table>""",
    "qs": [
      {
        "q": "Based on the afterimage data in Table 1, what mathematical relationship describes the perceived diameter of the afterimage as the projection distance increases from 1.0 m to 4.0 m?",
        "ch": [
          "Perceived size scales in direct linear proportion to projection distance, adhering strictly to Emmert's Law (S &prop; D).",
          "Perceived size follows an inverse square law relative to projection distance, shrinking exponentially (S &prop; 1/D^2).",
          "Perceived size remains completely invariant regardless of projection distance due to absolute retinal photoreceptor locking.",
          "Perceived size oscillates randomly depending on whether the observer blinks, reflecting irregular pupillary diameter shifts."
        ],
        "a": 0,
        "e": "<strong>Emmert's Law and afterimage scaling:</strong> Emmert's Law states that the perceived physical size of an afterimage of constant retinal dimensions is directly proportional to the physical distance of the projection surface upon which it is cast ($S \\propto D$). Because an afterimage is generated by bleached photopigments within a fixed patch of retinal photoreceptors, its angular retinal image size ($S_{\\text{retina}}$) remains identical at all times. In Table 1, when the afterimage is projected onto a surface at $1.0\\text{ m}$, its perceived diameter is $4.2\\text{ cm}$. When the projection plane is doubled to $2.0\\text{ m}$, its perceived diameter doubles to $8.3\\text{ cm}$. When quadrupled to $4.0\\text{ m}$, its perceived diameter quadruples to $16.7\\text{ cm}$ ($4.2 \\times 4 = 16.8\\text{ cm}$). This exact 1:1 linear scaling demonstrates that the visual brain automatically multiplies the fixed retinal afterimage signal by perceived distance to compute physical size.<br><br><em>Distractor Traps:</em><br>&bull; B describes inverse square attenuation, which applies to physical light intensity, not afterimage scaling.<br>&bull; C describes total failure of size scaling.<br>&bull; D invents random blinking oscillations."
      },
      {
        "q": "Why did neurological patients with bilateral lesions to cortical area V4 achieve normal color matching under Illuminant A (daylight) but fail severely under Illuminant B (tungsten)?",
        "ch": [
          "Area V4 lesions destroy S-cones in the peripheral retina, abolishing short-wavelength phototransduction under artificial bulbs.",
          "Area V4 performs spatial reflectance ratio calculations across the scene, which are indispensable when ambient illumination changes.",
          "Tungsten incandescent bulbs emit ionizing ultraviolet radiation that selectively damages parvocellular layers of the lateral geniculate.",
          "V4 lesion patients suffer from complete optic nerve demyelination that prevents transmission of long-wavelength red action potentials."
        ],
        "a": 1,
        "e": "<strong>Retinex theory, Area V4, and color constancy:</strong> In standard daylight (Illuminant A, $6500\\text{ K}$), the spectrum of ambient light is broad and balanced; standard cone ratios directly match canonical color categories, allowing even V4-lesioned patients to perform relatively well ($88.6\\%$ accuracy) via intact striate (V1) wavelength coding. However, tungsten incandescent illumination (Illuminant B, $2800\\text{ K}$) is heavily skewed toward long, red-orange wavelengths and impoverished in short-wavelength blue light. Under Illuminant B, every object in the room reflects significantly more long-wavelength photons into the eye than it would under daylight. To achieve color constancy and recognize that a white paper is still white and a green apple is still green, the visual cortex must discount the illuminant. As demonstrated by Edwin Land's Retinex theory, <strong>extrastriate area V4</strong> carries out this operation by computing the spatial ratios of reflectance across surrounding surfaces across independent wavebands. Because the V4-lesioned patients lack this specialized computational area, they cannot discount the illuminant; their color perception falls prey to the raw, altered wavelength distribution, causing matching accuracy to collapse to $\\sim 25\\%$.<br><br><em>Distractor Traps:</em><br>&bull; A is false: V4 lesions are in extrastriate cortex, leaving retinal S-cones completely intact.<br>&bull; C is physically false: tungsten bulbs emit long-wavelength infrared, not ionizing UV.<br>&bull; D invents optic nerve demyelination."
      },
      {
        "q": "According to the size-distance invariance hypothesis, why does the horizon moon appear substantially larger to a human observer than the zenith moon high overhead?",
        "ch": [
          "Atmospheric ozone at the horizon acts as a giant optical convex lens, physically magnifying the image cast on the cornea.",
          "The horizon moon reflects long-wavelength red light that directly depolarizes foveal horizontal cells to double retinal image size.",
          "Rich terrestrial depth cues make the horizon moon appear farther away, prompting the cortex to scale up its perceived physical size.",
          "Binocular disparity neurons in striate cortex shut off when gazing upwards, causing the zenith moon to physically shrink on the retina.",
        ],
        "a": 2,
        "e": "<strong>The Moon Illusion and size-distance invariance:</strong> The Moon Illusion—where the moon appears up to $50\\%$ larger when resting on the horizon than when overhead at its zenith—is an optical illusion explained by the size-distance invariance hypothesis (the apparent-distance theory). The physical angular size of the moon subtended at the cornea is completely identical ($0.52^\\circ$) in both positions; its retinal image size ($S_{\\text{retina}}$) does not change. However, when the moon is at the horizon, it is viewed across an intervening terrestrial terrain filled with rich monocular depth cues (trees, buildings, roads, linear perspective, and texture gradients). These cues cause the visual system to interpret the horizon moon as being situated at a great physical distance ($D_{\\text{perceived}}$ is large). Conversely, the zenith moon sits in an empty, cues-absent sky, leading the brain to perceive it as closer. Applying the size-distance formula ($S_{\\text{perceived}} \\propto S_{\\text{retina}} \\times D_{\\text{perceived}}$), because $S_{\\text{retina}}$ is identical, the greater perceived distance of the horizon moon forces the visual cortex to scale up its perceived physical size.<br><br><em>Distractor Traps:</em><br>&bull; A is physically false: atmospheric refraction flattens the moon slightly vertically rather than magnifying it.<br>&bull; B describes atmospheric Rayleigh scattering causing reddish color, which does not expand retinal image dimensions.<br>&bull; D falsely claims disparity neurons shut off."
      },
      {
        "q": "A piece of black coal in direct sunlight reflects more physical photons per second into the eye than a piece of white paper in dim candlelight. Why does an observer still perceive the coal as black and the paper as white?",
        "ch": [
          "Cone photoreceptors undergo complete metabolic apoptosis under sunlight, reducing coal brightness to zero.",
          "The cornea undergoes dynamic polarization changes that selectively block photons reflected from carbon-rich surfaces.",
          "Action potentials along the optic nerve encode the absolute physical luminance (lux) rather than relative contrast ratios.",
          "Perceived lightness is determined by the ratio of luminance between an object and its immediate surround (Wallach's ratio rule)."
        ],
        "a": 3,
        "e": "<strong>Lightness constancy and Wallach's ratio rule:</strong> Lightness constancy refers to the visual system's capacity to perceive the intrinsic achromatic reflectance of a surface (whether it is white, gray, or black) regardless of the absolute level of ambient illumination. Physical luminance (the total number of photons entering the pupil) is the product of surface reflectance (percentage of light reflected) and illumination intensity. Under direct sunlight ($100,000\\text{ lux}$), a piece of black coal with $5\\%$ reflectance reflects $5,000\\text{ units}$ of light. Under dim candlelight ($10\\text{ lux}$), a piece of white paper with $90\\%$ reflectance reflects only $9\\text{ units}$ of light. Despite the coal reflecting over 500 times more physical photons than the white paper, the coal is perceived as jet black and the paper as bright white. As established by Hans Wallach's ratio rule, the visual system does not evaluate absolute luminance; instead, lateral inhibitory circuits in the retina and cortex compute the <i>luminance contrast ratio</i> between an object and its immediate background. Because the coal reflects far less light than the sunlit ground surrounding it (ratio $\\sim 1:20$), it is perceived as black. Because the paper reflects far more light than the dim room surrounding it (ratio $\\sim 9:1$), it is perceived as white.<br><br><em>Distractor Traps:</em><br>&bull; A describes apoptosis under sunlight, which is medically absurd.<br>&bull; B invents corneal polarization that recognizes carbon.<br>&bull; C states the exact opposite of reality: optic nerve fibers encode relative contrast, not absolute lux."
      },
      {
        "q": "An observer views an inclined rectangular playing card through a narrow reduction peephole that eliminates all ambient depth and distance cues. What shape will the observer perceive?",
        "ch": [
          "A trapezoid corresponding directly to the geometric outline of the card projected onto the retina.",
          "A perfect rectangle, because shape constancy operates independently of any depth or context cues.",
          "An expanding concentric circle, due to spontaneous oscillations of ciliary muscle accommodation.",
          "A pulsating three-dimensional cube, generated by involuntary saccadic microsaccades of the fovea."
        ],
        "a": 0,
        "e": "<strong>Shape constancy breakdown in reduction conditions:</strong> Shape constancy allows an observer to perceive an object as retaining its true physical geometry (e.g., a rectangular card) even when tilted at an angle that casts a distorted projective outline (a trapezoid) onto the retina. To achieve shape constancy, the visual system relies on depth, slant, and surface orientation cues (such as linear perspective, texture gradients, and stereopsis) to discount the tilt angle. When an observer views the card through a reduction screen or monocular peephole that strips away all depth and slant cues, the visual system is deprived of the context needed to compute the tilt correction. Consequently, shape constancy collapses: the observer perceives the proximal stimulus literally as it is cast on the retina—an acute <strong>trapezoid</strong>.<br><br><em>Distractor Traps:</em><br>&bull; B is incorrect because shape constancy strictly requires spatial depth cues and breaks down under reduction conditions.<br>&bull; C and D invent bizarre perceptual distortions (circles, pulsating cubes) unrelated to geometric projective optics."
      },
      {
        "q": "In Table 1, Area V4 lesion patients exhibited preserved size scaling according to Emmert's Law but severe deficits in color constancy. What neuroanatomical conclusion is best supported by this dissociation?",
        "ch": [
          "Size constancy and color constancy are both processed exclusively within the primary visual striate cortex (V1).",
          "Size constancy relies on parietal dorsal stream spatial scaling, whereas color constancy requires extrastriate ventral area V4.",
          "Extrastriate area V4 is the primary convergence center for all monocular, binocular, and somatosensory depth calculations.",
          "Perceptual constancies are non-localized epiphenomena that cannot be mapped to distinct cortical processing streams."
        ],
        "a": 1,
        "e": "<strong>Neuroanatomical segregation of visual constancies:</strong> The data in Table 1 reveal that patients with bilateral lesions to extrastriate area V4 display normal size constancy (their afterimage size scaling adheres perfectly to Emmert's Law, doubling from $4.1\\text{ cm}$ at $1\\text{ m}$ to $8.4\\text{ cm}$ at $2\\text{ m}$ and $16.6\\text{ cm}$ at $4\\text{ m}$, matching healthy controls), yet their color constancy is completely devastated under shifted illuminants ($25.4\\%$ vs $94.2\\%$ in controls). This functional dissociation demonstrates that different perceptual constancies are executed by anatomically distinct cortical streams. <strong>Color constancy</strong> requires extrastriate area V4 within the ventral (\"what\") visual stream to compute spatial reflectance ratios. In contrast, <strong>size constancy</strong> requires scaling retinal dimensions by spatial depth and distance representations, which are computed primarily within the dorsal (\"where/how\") stream and posterior parietal cortex before modulating striate representations.<br><br><em>Distractor Traps:</em><br>&bull; A is false: if both were mediated exclusively by V1, a V4 lesion would not spare size constancy while destroying color constancy.<br>&bull; C is false: V4 is a ventral color/form area, not a somatosensory/depth convergence hub.<br>&bull; D contradicts the fundamental modularity of the brain."
      }
    ]
}
