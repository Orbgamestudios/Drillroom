# Passage 5: Topic 778 — Theories of Color Vision: Trichromatic vs Opponent-Process Theory
# Keys: 0, 1, 2, 3, 0, 1

p5_data = {
    "id": "exam_ps90_3_p5",
    "sec": "P/S",
    "topic": "Theories of Color Vision: Trichromatic vs Opponent-Process Theory",
    "sheet": 5,
    "label": "Psychological, Social, and Biological Foundations of Behavior",
    "examId": "ps90_3",
    "passage": """<div class="ttl">Passage 5 (Questions 25&ndash;30)</div>
<p>The human visual system's capacity to discriminate wavelengths across the visible spectrum ($380\\text{ to }740\\text{ nm}$) was historically explained by two competing frameworks: Thomas Young and Hermann von Helmholtz's Trichromatic Theory, and Ewald Hering's Opponent-Process Theory. Modern sensory neurobiology has synthesized these models into a unified dual-stage architecture: trichromacy operates at the primary photoreceptor receptor level, while opponent-process coding governs post-receptoral neural integration across retinal ganglion cells, the lateral geniculate nucleus (LGN), and extrastriate visual cortex.</p>
<p>At the receptoral stage, color vision is initiated by three distinct cone photoreceptor populations expressing unique photopsin apoproteins: S-cones (short-wavelength sensitive, $\\lambda_{\\text{max}} \\approx 420\\text{ nm}$), M-cones (medium-wavelength sensitive, $\\lambda_{\\text{max}} \\approx 530\\text{ nm}$), and L-cones (long-wavelength sensitive, $\\lambda_{\\text{max}} \\approx 560\\text{ nm}$). Because of the <i>principle of univariance</i>&mdash;which establishes that a photoreceptor's hyperpolarization signal encodes only the total number of absorbed photons, discarding photon wavelength&mdash;a single cone class cannot differentiate wavelength from intensity. Wavelength computation strictly requires comparing relative excitation ratios across the three cone types.</p>
<p>At the post-receptoral stage, retinal bipolar and ganglion cells compare cone inputs to establish three mutually antagonistic chromatic and achromatic channels: (1) Red-Green ($+L/-M$ or $+M/-L$), (2) Blue-Yellow ($+S/-[L+M]$ or $+[L+M]/-S$), and (3) Luminance/Achromatic ($+L+M$). Because neurons in an opponent channel fire above baseline to one color and below baseline to its complementary pair, the visual system cannot perceive combinations such as \"reddish-green\" or \"yellowish-blue.\" Continuous exposure to a saturated chromatic stimulus induces receptor adaptation and neural fatigue in that pathway, generating complementary negative afterimages upon viewing an achromatic neutral field. Electrophysiologists recorded extracellular spike rates from primate parvocellular LGN units, while psychophysicists tested color perceptions in trichromatic and protanopic human observers across spectral flashes before and after chromatic adaptation, as shown in Table 1.</p>
<table class="tbl">
  <caption>Table 1 Parvocellular LGN single-unit firing rates and human psychophysical color percepts across spectral flashes and chromatic adaptation</caption>
  <thead>
    <tr><th>Optical Flash Condition</th><th>LGN Unit 1 Firing (Hz)</th><th>LGN Unit 2 Firing (Hz)</th><th>Trichromat Percept (Normal)</th><th>Protanope Percept (L-Cone Absent)</th></tr>
  </thead>
  <tbody>
    <tr><td>Baseline (Darkness)</td><td>12.2</td><td>10.4</td><td>Black</td><td>Black</td></tr>
    <tr><td>440-nm Monochromatic Flash (Blue)</td><td>11.8 (Baseline)</td><td>68.4 (Strong excitation)</td><td>Vivid Blue</td><td>Vivid Blue</td></tr>
    <tr><td>530-nm Monochromatic Flash (Green)</td><td>1.8 (Strong inhibition)</td><td>8.9 (Slight inhibition)</td><td>Vivid Green</td><td>Achromatic Gray/Yellow</td></tr>
    <tr><td>650-nm Monochromatic Flash (Red)</td><td>74.6 (Strong excitation)</td><td>9.1 (Slight inhibition)</td><td>Vivid Red</td><td>Dim Achromatic Gray</td></tr>
    <tr><td>Achromatic White (Pre-Adaptation)</td><td>12.5 (Baseline)</td><td>10.6 (Baseline)</td><td>Neutral White</td><td>Neutral White</td></tr>
    <tr><td>Achromatic White (Post-650-nm Adaptation)</td><td>1.2 (Suppressed below baseline)</td><td>10.2 (Baseline)</td><td>Vivid Green (Afterimage)</td><td>Indistinct Neutral Gray</td></tr>
  </tbody>
</table>""",
    "qs": [
      {
        "q": "Based on the electrophysiological responses in Table 1, what specific opponent-process chromatic channels are represented by LGN Unit 1 and LGN Unit 2, respectively?",
        "ch": [
          "Unit 1 represents a Red-On/Green-Off (+L/-M) channel; Unit 2 represents a Blue-On/Yellow-Off (+S/-[L+M]) channel.",
          "Unit 1 represents a Green-On/Red-Off (+M/-L) channel; Unit 2 represents an Achromatic Luminance (+L+M) channel.",
          "Unit 1 represents an Achromatic Luminance (+L+M) channel; Unit 2 represents a Red-On/Green-Off (+L/-M) channel.",
          "Unit 1 represents a Yellow-On/Blue-Off channel; Unit 2 represents a Black-White non-opponent inhibitory channel."
        ],
        "a": 0,
        "e": "<strong>Electrophysiological identification of opponent channels:</strong> Opponent neurons respond with excitation (increased spike frequency above baseline) to one region of the spectrum and inhibition (decreased spike frequency below baseline) to another region:<br>&bull; <i>Unit 1</i>: Exhibits a resting baseline of $12.2\\text{ Hz}$. A $650\\text{-nm}$ (red) flash strongly excites it ($74.6\\text{ Hz}$), while a $530\\text{-nm}$ (green) flash strongly suppresses it ($1.8\\text{ Hz}$), with no change at $440\\text{ nm}$ ($11.8\\text{ Hz}$). This is the diagnostic profile of a <strong>Red-On/Green-Off ($+L/-M$)</strong> opponent neuron.<br>&bull; <i>Unit 2</i>: Exhibits a resting baseline of $10.4\\text{ Hz}$. A $440\\text{-nm}$ (blue) flash strongly excites it ($68.4\\text{ Hz}$), while both $530\\text{-nm}$ and $650\\text{-nm}$ flashes slightly inhibit it ($8.9\\text{ Hz}$ and $9.1\\text{ Hz}$, representing yellow inhibition via $L+M$). This identifies Unit 2 as a <strong>Blue-On/Yellow-Off ($+S/-[L+M]$)</strong> opponent neuron.<br><br><em>Distractor Traps:</em><br>&bull; B reverses Unit 1 (+M/-L would be excited by green and inhibited by red) and misidentifies Unit 2.<br>&bull; C misidentifies Unit 1 as an achromatic luminance channel (which would be excited by both red and green).<br>&bull; D invents non-existent channel configurations inconsistent with the firing data."
      },
      {
        "q": "Why does sudden presentation of an achromatic white stimulus immediately following 90 seconds of continuous exposure to a saturating 650-nm red light evoke a vivid green afterimage in normal observers?",
        "ch": [
          "Retinal guanylyl cyclase is irreversibly blocked in M-cones, causing spontaneous depolarization of all green cone pedicles.",
          "L-cone pathways undergo neural adaptation and fatigue, allowing unadapted M-cone signals to dominate the red-green opponent channel.",
          "Red photons remain physically trapped within the vitreous humor, selectively activating inhibitory glycinergic amacrine cells.",
          "Prolonged red exposure causes the visual cortex to permanently alter its orientation columns into horizontal color stripes."
        ],
        "a": 1,
        "e": "<strong>Physiological basis of negative afterimages:</strong> Prolonged adaptation to a continuous $650\\text{-nm}$ red stimulus causes photopigment bleaching, arrestin binding, and neural adaptation in the L-cone pathway and its downstream $+L/-M$ opponent neurons. The red excitatory component becomes fatigued, elevating its response threshold. When the observer suddenly views an achromatic white surface (which reflects all visible wavelengths equally), neutral white light stimulates L-cones, M-cones, and S-cones with equal intensity. However, because the L-cone pathway is adapted/fatigued, the unadapted, fresh M-cone pathway generates a far stronger signal. In the $+L/-M$ opponent channel, this imbalance causes unopposed M-cone inhibitory drive onto Unit 1, driving its firing rate far below its baseline ($1.2\\text{ Hz}$ in Table 1). The cortex decodes firing below baseline in a red-green channel as the complementary color: <strong>green</strong>.<br><br><em>Distractor Traps:</em><br>&bull; A erroneously attributes changes to M-cone guanylyl cyclase blockage.<br>&bull; C invents physical trapping of photons in vitreous humor.<br>&bull; D claims orientation column destruction in cortex, which is permanent damage rather than transient perceptual afterimages."
      },
      {
        "q": "The principle of univariance dictates that an individual who expresses only a single functional cone photopigment class (monochromacy) is completely colorblind because:",
        "ch": [
          "a single cone opsin cannot absorb photons whose wavelengths deviate by more than 5 nm from its peak absorption maximum.",
          "action potential amplitudes along the optic nerve vary linearly with the physical wavelength of the stimulating electromagnetic light.",
          "a photoreceptor's hyperpolarization depends solely on photon absorption rate, rendering wavelength and light intensity indistinguishable.",
          "single cone outer segments lack the cyclic nucleotide-gated channels required to produce hyperpolarizing electrical responses."
        ],
        "a": 2,
        "e": "<strong>Principle of univariance in photoreception:</strong> Formulated by Rushton, the principle of univariance states that once a photon is absorbed by a photoreceptor photopigment, all information regarding its physical wavelength (frequency/energy) is lost. The electrical output of the photoreceptor (the degree of outer segment hyperpolarization and reduction in glutamate release) is governed strictly by a single scalar variable: the total number of photons isomerizing 11-<i>cis</i>-retinal per unit time. For an individual with only a single functional cone class (a cone monochromat), any given receptor output can be produced either by a high-intensity light at a wavelength where absorption probability is low, or by a low-intensity light at the peak absorption wavelength. Because the brain receives only a single channel of information without a reference comparator, it is impossible to separate changes in color (wavelength) from changes in brightness (intensity). Thus, monochromats perceive the world exclusively in shades of gray.<br><br><em>Distractor Traps:</em><br>&bull; A is false: cone opsin absorption curves are broad bell curves spanning $>100\\text{ nm}$.<br>&bull; B is false: action potentials are all-or-none events whose amplitude never encodes wavelength.<br>&bull; D is biologically false: monochromats possess fully functional CNG channels and phototransduction cascades."
      },
      {
        "q": "Why are red-green color vision deficiencies (protanopia and deuteranopia) dramatically more prevalent in biological males than in biological females?",
        "ch": [
          "The genes encoding both L- and M-opsins reside on the Y chromosome, where homologous genetic recombination occurs continuously.",
          "Mitochondrial DNA mutations specifically target retinal pigment epithelium cells in males while sparing female cone photoreceptors.",
          "Females produce higher systemic levels of estrogen, which upregulates cone arrestin-1 expression to prevent photopigment loss.",
          "The genes encoding L- and M-cone photopsins are situated in tandem on the X chromosome, conferring X-linked recessive inheritance."
        ],
        "a": 3,
        "e": "<strong>Genetics of red-green color deficiency:</strong> The genes encoding the L-cone opsin (<i>OPN1LW</i>) and M-cone opsin (<i>OPN1MW</i>) are located in close head-to-tail proximity on the long arm of the X chromosome ($Xq28$). They share $96\\%$ sequence homology, making them highly susceptible to unequal homologous recombination during meiosis, leading to gene deletions, duplications, or hybrid opsin genes. Because red-green opsin defects are inherited in an <strong>X-linked recessive</strong> pattern, biological males ($XY$) are hemizygous: inheriting a single mutated X chromosome causes full clinical manifestation of the deficiency ($\sim 8\\%$ prevalence in males). Biological females ($XX$) must inherit mutated alleles on <i>both</i> X chromosomes to express the phenotype ($<0.5\\%$ prevalence), as a single normal X chromosome is sufficient to provide normal color vision.<br><br><em>Distractor Traps:</em><br>&bull; A erroneously places opsin genes on the Y chromosome.<br>&bull; B invents mitochondrial DNA mutations.<br>&bull; C invents hormonal estrogen protection mechanisms."
      },
      {
        "q": "When an identical neutral gray square is positioned against a large, saturated red background, the square is perceived as having a distinct greenish hue. What neural mechanism accounts for this simultaneous color contrast?",
        "ch": [
          "Spatial lateral inhibition within receptive field surrounds of red-green opponent ganglion cells enhances complementary green responses.",
          "Parasympathetic pupillary miosis blocks long-wavelength red light from entering the marginal zones of the crystalline lens.",
          "Rapid breakdown of 11-cis-retinal into toxic rhodopsin metabolites within the peripheral retinal pigment epithelium.",
          "Top-down cognitive expectations from the prefrontal cortex overriding lower-level sensory inputs from the striate cortex."
        ],
        "a": 0,
        "e": "<strong>Simultaneous color contrast and spatial opponency:</strong> Simultaneous color contrast is a perceptual phenomenon where the appearance of a neutral or chromatic target is altered by the surrounding color context, shifting toward the surrounding color's opponent complement (e.g., gray on a red background looks greenish; gray on a yellow background looks bluish). This is mediated by <i>double-opponent cells</i> in primary visual cortex (V1 blobs) and concentric color-opponent retinal ganglion cells. These neurons possess spatially antagonistic receptive fields (e.g., center excited by red, surround inhibited by red / excited by green). When the large surround is stimulated by vivid red light, it delivers strong lateral inhibition to the red channel and lateral excitation to the green channel. In the central gray area (which provides balanced, uncolored photon input), the surround-induced inhibition of red disinhibits the opponent green pathway, causing the cortex to compute a net green signal for the gray square.<br><br><em>Distractor Traps:</em><br>&bull; B describes pupillary miosis, which affects optical depth of field, not local color contrast.<br>&bull; C describes toxic metabolite accumulation, which is pathological and irrelevant.<br>&bull; D invents top-down prefrontal overriding for what is fundamentally an early, bottom-up sensory neurobiological computation."
      },
      {
        "q": "How does modern visual neuroscience resolve the historical debate between the Young-Helmholtz trichromatic theory and Hering's opponent-process theory?",
        "ch": [
          "Opponent-process theory accurately describes the initial cone photoreceptor layer, whereas trichromatic theory operates in cortex.",
          "Trichromatic theory operates at the photoreceptor stage, while opponent-process mechanisms emerge at post-receptoral neural stages.",
          "Both theories are entirely incorrect, as color perception is determined exclusively by psychological memory and semantic schemas.",
          "Trichromatic mechanisms operate under dim starlight (scotopic), whereas opponent mechanisms operate solely in bright daylight (photopic)."
        ],
        "a": 1,
        "e": "<strong>Dual-stage synthesis of color vision:</strong> Historically, Helmholtz argued that color vision relies on three primary receptor types (trichromacy), while Hering argued that color relies on three opposing pairs (red vs green, blue vs yellow, black vs white). Electrophysiological recordings proved that both theories are correct, but describe different sequential stages of the visual processing hierarchy. The <strong>Young-Helmholtz trichromatic theory</strong> correctly describes the primary receptor stage in the retina, where three distinct cone photoreceptor populations (S, M, and L cones) with distinct spectral absorption peaks initiate transduction. The <strong>Hering opponent-process theory</strong> correctly describes the post-receptoral neural stages, beginning with retinal bipolar and ganglion cells and extending through the LGN to visual cortex, where cone signals are subtracted and added to form antagonistic opponent channels ($L-M$, $S-[L+M]$, and $L+M$).<br><br><em>Distractor Traps:</em><br>&bull; A inverts the two stages, placing opponent processing at the photoreceptor layer and trichromacy in cortex.<br>&bull; C dismisses both theories, which are proven empirical foundations of visual neuroscience.<br>&bull; D confuses rod scotopic vision with cone photopic vision."
      }
    ]
}
