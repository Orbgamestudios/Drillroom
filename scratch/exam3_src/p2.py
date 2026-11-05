# Passage 2: Topic 775 — Retinal Circuitry: Photoreceptors to Retinal Ganglion Cells
# Keys: 2, 3, 0, 1, 2, 3

p2_data = {
    "id": "exam_ps90_3_p2",
    "sec": "P/S",
    "topic": "Retinal Circuitry: Photoreceptors to Retinal Ganglion Cells",
    "sheet": 2,
    "label": "Psychological, Social, and Biological Foundations of Behavior",
    "examId": "ps90_3",
    "passage": """<div class="ttl">Passage 2 (Questions 7&ndash;12)</div>
<p>Visual information processing begins within the complex microcircuitry of the retina, a five-layered neural structure lining the posterior interior of the globe. Vertebrate photoreceptors (rods and cones) absorb incident photons using photopigment molecules composed of a transmembrane opsin apoprotein covalently coupled via a protonated Schiff base to the chromophore 11-<i>cis</i>-retinal. In complete darkness, high basal activity of retinal guanylyl cyclase maintains elevated cytosolic concentrations of cyclic guanosine monophosphate (cGMP) in the photoreceptor outer segment. cGMP binds to cyclic nucleotide-gated (CNG) cation channels, permitting a tonic inward influx of $\\text{Na}^+$ and $\\text{Ca}^{2+}$ (the \"dark current\"). This maintains the photoreceptor resting membrane potential at a partially depolarized state ($\\sim -40\\text{ mV}$), driving continuous exocytosis of the amino acid neurotransmitter L-glutamate from the synaptic terminal.</p>
<p>Absorption of a photon triggers the photochemical isomerization of 11-<i>cis</i>-retinal to <i>all-trans</i>-retinal, inducing a conformational transition into active Metarhodopsin II. This intermediate activates the visual G-protein transducin ($\\text{G}_t$), which in turn stimulates cGMP phosphodiesterase-6 (PDE6). Active PDE6 rapidly hydrolyzes cGMP to 5'-GMP, precipitating CNG channel closure. Unopposed outward leak $\\text{K}^+$ currents hyperpolarize the photoreceptor membrane toward $-70\\text{ mV}$, closing voltage-gated calcium channels and shutting down synaptic glutamate release.</p>
<p>Photoreceptor terminals synapse onto bipolar cells and horizontal cells within the outer plexiform layer. Horizontal cells mediate widespread lateral inhibition via gamma-aminobutyric acid (GABA) release, creating antagonistic center-surround receptive field geometries. Bipolar cells split the visual stream into parallel ON and OFF pathways. ON-center bipolar cells express metabotropic glutamate receptors (mGluR6) coupled to $\\text{G}_o$, which close TRPM1 cation channels in the dark; reduction of glutamate in light disinhibits TRPM1, causing inward current and cell depolarization (a sign-inverting synapse). Conversely, OFF-center bipolar cells express ionotropic AMPA/kainate receptors that depolarize in the dark and hyperpolarize in the light (a sign-conserving synapse). Neurophysiologists recorded whole-cell potentials and action potential discharge rates from retinal explants exposed to focal and annular optical stimuli under pharmacological perturbations, as detailed in Table 1.</p>
<table class="tbl">
  <caption>Table 1 Electrophysiological responses of photoreceptors, bipolar cells, and ganglion cells under optical and pharmacological stimulation</caption>
  <thead>
    <tr><th>Stimulus / Perfusion Condition</th><th>Center Photoreceptor $\\Delta V_m$ (mV)</th><th>Horizontal Cell Potential ($V_m$)</th><th>ON Bipolar Potential ($V_m$)</th><th>ON Ganglion Spikes (Hz)</th><th>OFF Ganglion Spikes (Hz)</th></tr>
  </thead>
  <tbody>
    <tr><td>Darkness (Resting)</td><td>0 (Resting: $-40\\text{ mV}$)</td><td>Depolarized ($-35\\text{ mV}$)</td><td>Hyperpolarized ($-62\\text{ mV}$)</td><td>3.2</td><td>4.1</td></tr>
    <tr><td>Center Spot Only</td><td>$-26$ (Hyperpolarized)</td><td>Depolarized ($-36\\text{ mV}$)</td><td>Depolarized ($-38\\text{ mV}$)</td><td>68.4</td><td>1.8</td></tr>
    <tr><td>Center Spot + Annular Surround</td><td>$-26$ (Hyperpolarized)</td><td>Hyperpolarized ($-58\\text{ mV}$)</td><td>Intermediate ($-51\\text{ mV}$)</td><td>18.1</td><td>24.6</td></tr>
    <tr><td>Center Spot + Gabazine (GABA$_A$ Antagonist)</td><td>$-26$ (Hyperpolarized)</td><td>Hyperpolarized ($-57\\text{ mV}$)</td><td>Depolarized ($-34\\text{ mV}$)</td><td>84.7</td><td>1.2</td></tr>
    <tr><td>Center Spot + L-AP4 (mGluR6 Agonist)</td><td>$-26$ (Hyperpolarized)</td><td>Depolarized ($-36\\text{ mV}$)</td><td>Hyperpolarized ($-65\\text{ mV}$)</td><td>0.4</td><td>2.1</td></tr>
  </tbody>
</table>""",
    "qs": [
      {
        "q": "In Table 1, adding an annular surround light stimulus to the center spot stimulus reduced ON ganglion cell firing from 68.4 Hz to 18.1 Hz. What synaptic mechanism is responsible for this surround suppression?",
        "ch": [
          "Depolarized horizontal cells release glutamate directly onto ganglion cells, shunting action potential propagation down the optic nerve.",
          "Hyperpolarized amacrine cells release glycine to activate chloride channels directly on the center cone photoreceptor outer segments.",
          "Hyperpolarized horizontal cells disinhibit presynaptic photoreceptors in the center, reducing net sign-inverting bipolar depolarization.",
          "Hyperpolarized bipolar cells release acetylcholine onto inhibitory interneurons, selectively uncoupling electrical gap junction networks."
        ],
        "a": 2,
        "e": "<strong>Lateral inhibition and center-surround antagonism:</strong> The concentric center-surround architecture of retinal receptive fields is generated at the first visual synapse in the outer plexiform layer by horizontal cells. When light strikes the annular surround, the surround photoreceptors hyperpolarize, decreasing their glutamate release onto horizontal cells. Because horizontal cells receive sign-conserving ionotropic inputs, reduced glutamate causes horizontal cells to hyperpolarize (from $-35\\text{ mV}$ to $-58\\text{ mV}$ in Table 1). In the dark or unilluminated surround, horizontal cells continuously release inhibitory GABA (and maintain feedback hemichannels) back onto the synaptic terminals of center photoreceptors. Hyperpolarization of horizontal cells relieves this presynaptic inhibition (disinhibition), causing the center photoreceptor terminal to depolarize slightly relative to the light-induced hyperpolarization. This partially restores glutamate release from the center cone terminal, which re-engages mGluR6 receptors on the ON bipolar cell, muting its depolarization (from $-38\\text{ mV}$ to $-51\\text{ mV}$) and suppressing ON ganglion cell spike frequency (from 68.4 Hz to 18.1 Hz).<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly claims horizontal cells release glutamate directly onto ganglion cells in the inner retina.<br>&bull; B erroneously places glycinergic amacrine action onto outer segments rather than inner plexiform layers.<br>&bull; D invents cholinergic gap junction uncoupling as the basis of receptive field surrounds."
      },
      {
        "q": "When the pharmacological agent L-AP4 (an mGluR6 receptor agonist) was added, center spot illumination produced photoreceptor hyperpolarization, but the ON bipolar cell remained hyperpolarized and ON ganglion cell spiking dropped to 0.4 Hz. What explains this observation?",
        "ch": [
          "L-AP4 irreversibly destroys cGMP phosphodiesterase-6 within photoreceptor outer segment disks, preventing cation channel closure.",
          "L-AP4 competitively inhibits ionotropic AMPA receptors on bipolar cells, blocking sodium influx during light exposure.",
          "L-AP4 binds to rhodopsin apoprotein to permanently prevent photoisomerization of 11-cis-retinal to all-trans-retinal.",
          "L-AP4 persistently activates mGluR6 receptors on ON bipolar dendrites, keeping TRPM1 cation channels closed despite light."
        ],
        "a": 3,
        "e": "<strong>mGluR6 receptor pharmacology and sign-inversion:</strong> ON-center bipolar cells express metabotropic glutamate receptors (mGluR6) on their dendritic tips in the outer plexiform layer. In darkness, glutamate released by photoreceptors binds mGluR6, activating a $G_o$ heterotrimeric G-protein cascade that maintains downstream TRPM1 non-selective cation channels in a closed state, keeping the ON bipolar cell tonicly hyperpolarized. In normal physiological conditions, light shuts down photoreceptor glutamate release, relieving mGluR6 activation, which allows TRPM1 channels to open and depolarize the cell. L-2-amino-4-phosphonobutyric acid (L-AP4) is a potent, selective agonist for mGluR6 receptors. Bath application of L-AP4 mimics the continuous presence of high glutamate specifically at the mGluR6 receptor. Even though light successfully hyperpolarizes the photoreceptor (Table 1: $-26\\text{ mV}$), L-AP4 continues to bind and stimulate mGluR6, locking TRPM1 channels shut. As a result, the ON bipolar cell cannot depolarize (stays at $-65\\text{ mV}$), releasing no excitatory transmitter onto ON ganglion cells and silencing their spikes ($0.4\\text{ Hz}$).<br><br><em>Distractor Traps:</em><br>&bull; A describes destruction of PDE6, which would occur in photoreceptors, but the table shows photoreceptor hyperpolarization is intact ($-26\\text{ mV}$).<br>&bull; B describes ionotropic AMPA receptors, which mediate OFF bipolar pathways, not ON bipolar pathways.<br>&bull; C falsely places L-AP4's site of action on rhodopsin."
      },
      {
        "q": "Why does the foveal cone visual pathway exhibit markedly superior spatial resolution compared to the peripheral rod visual pathway under daylight conditions?",
        "ch": [
          "Foveal cones demonstrate near 1:1 synaptic convergence with midget bipolar and ganglion cells, preserving spatial locus.",
          "Foveal cones possess vastly larger receptive fields that pool synaptic input over several millimeters of pigment epithelium.",
          "Peripheral rods synthesize specialized visual arrestin isoforms that accelerate transducin deactivation at high photon fluxes.",
          "Peripheral rods bypass intermediate bipolar cell relays to synapse directly on large magnocellular ganglion dendrites."
        ],
        "a": 0,
        "e": "<strong>Synaptic convergence and visual acuity trade-offs:</strong> Visual acuity (the capacity to resolve two distinct spatial points as separate) is governed by the degree of neural convergence in the retinal circuitry. In the central fovea (specifically the foveola), there is a dedicated \"private line\" architecture: a single cone photoreceptor synapses onto a single ON or OFF midget bipolar cell, which in turn synapses onto a single midget ganglion cell (a 1:1:1 convergence ratio). This minimal pooling ensures that photons originating from adjacent points in visual space activate distinct, independent ganglion cell axons, preserving precise spatial details. In contrast, in the peripheral retina, hundreds of rod photoreceptors converge onto a few rod bipolar cells, which converge via amacrine cells onto a single ganglion cell. This high convergence maximizes spatial summation, granting rods extraordinary sensitivity to detect dim light (scotopic vision), but destroys spatial resolution because the ganglion cell cannot determine which of the hundreds of rods absorbed the photon.<br><br><em>Distractor Traps:</em><br>&bull; B erroneously attributes large receptive fields and broad pooling to foveal cones (which is the exact opposite of reality).<br>&bull; C describes adaptation biochemistry unrelated to convergence geometry.<br>&bull; D falsely claims rods bypass bipolar cells and connect directly to ganglion cells."
      },
      {
        "q": "Following light-induced hyperpolarization of a rod photoreceptor, which sequence of molecular events is strictly required to terminate the signaling cascade and reopen CNG channels?",
        "ch": [
          "Guanylyl cyclase inhibition, transducin GTPase activation, and permanent uncoupling of 11-cis-retinal from the opsin pocket.",
          "Rhodopsin phosphorylation by GRK1, arrestin-1 binding, transducin GTP hydrolysis, and cGMP synthesis by guanylyl cyclase.",
          "Rapid calcium influx through open CNG channels, activation of protein kinase C, and degradation of cyclic GMP phosphodiesterase.",
          "Direct binding of beta-arrestin to cyclic AMP, open sodium channel gating, and thermal reconversion of trans-retinal to cis-retinal."
        ],
        "a": 1,
        "e": "<strong>Termination of the visual phototransduction cascade:</strong> To return a light-activated photoreceptor to its dark resting state (repolarizing/depolarizing to $-40\\text{ mV}$), the active phototransduction enzymes must be rapidly deactivated and cytoplasmic cGMP levels restored. First, rhodopsin kinase (GRK1) phosphorylates the intracellular C-terminal serine and threonine residues of active Metarhodopsin II. Visual arrestin-1 then binds the phosphorylated opsin, sterically blocking any further activation of transducin ($G_t$). Second, the intrinsic GTPase activity of transducin's $\\alpha$-subunit ($G\\alpha_t$) hydrolyzes bound GTP to GDP, accelerated by the RGS9-1 GTPase-activating protein complex, causing $G\\alpha_t$ to dissociate from and deactivate PDE6. Third, because CNG channel closure during light prevents $\\text{Ca}^{2+}$ entry while the $\\text{Na}^+/\\text{Ca}^{2+}\\text{-K}^+$ exchanger continues pumping $\\text{Ca}^{2+}$ out, intracellular $[\\text{Ca}^{2+}]$ falls. This drop in calcium disinhibits guanylyl cyclase-activating proteins (GCAPs), which strongly stimulate retinal guanylyl cyclase (retGC) to synthesize new cGMP from GTP. The rising cGMP re-binds CNG channels, reopening them and restoring the inward dark current.<br><br><em>Distractor Traps:</em><br>&bull; A suggests guanylyl cyclase inhibition, which would suppress cGMP and prevent channel reopening.<br>&bull; C incorrectly states that termination begins with calcium influx through open channels, whereas calcium drops during illumination.<br>&bull; D conflates cAMP with cGMP and invents non-existent direct beta-arrestin-cAMP interactions."
      },
      {
        "q": "When a person transitions from brilliant outdoor sunlight into a pitch-dark room, their visual detection threshold decreases over 30 minutes in a characteristic two-phase curve. What explains this biphasic recovery?",
        "ch": [
          "Bipolar cells initially amplify rod signals through electrical gap junctions before horizontal cells switch on GABAergic inhibition.",
          "Pupillary dilation occurs rapidly during the first 5 minutes, followed by a slow 25-minute increase in corneal refractive index.",
          "Cones regenerate photopigments rapidly but plateau at moderate sensitivity, whereas rods regenerate slowly to reach maximum sensitivity.",
          "The central fovea completely degenerates in darkness, requiring peripheral ganglion cells to synthesize new rhodopsin de novo."
        ],
        "a": 2,
        "e": "<strong>Dark adaptation curve and duplex retina theory:</strong> In bright sunlight (photopic vision), rhodopsin in rods is almost completely bleached (photoisomerized and uncoupled), rendering rods saturated and unresponsive. When entering total darkness, dark adaptation begins. The human detection threshold curve exhibits two distinct kinetic phases separated by the \"rod-cone break\" at $\\sim 7\\text{ to }10\\text{ minutes}$. During the first 5 to 7 minutes, cone photopigments (photopsins) rapidly regenerate, lowering the perceptual threshold by $\\sim 2\\text{ to }3\\text{ log units}$, at which point cone sensitivity plateaus (the cone branch). Meanwhile, rhodopsin regeneration through the visual cycle in the retinal pigment epithelium (RPE) proceeds much more slowly. At $\\sim 10\\text{ minutes}$, the accumulating unbleached rhodopsin causes rod sensitivity to overtake cone sensitivity; the rod branch takes over, continuing to increase sensitivity over the next 20 to 30 minutes until reaching the absolute visual threshold (a total sensitivity gain of $10^5\\text{ to }10^6\\text{-fold}$).<br><br><em>Distractor Traps:</em><br>&bull; A invents gap junction switches unrelated to photopigment regeneration kinetics.<br>&bull; B falsely claims corneal refractive index changes during dark adaptation.<br>&bull; D is biologically absurd, claiming foveal destruction occurs in the dark."
      },
      {
        "q": "Based on the data in Table 1, what was the electrophysiological consequence of applying the GABA_A receptor antagonist gabazine during center spot illumination?",
        "ch": [
          "It suppressed ON bipolar cell depolarization by blocking inward sodium entry through voltage-gated channels.",
          "It hyperpolarized the center photoreceptor beyond the maximum theoretical equilibrium potential of potassium.",
          "It completely prevented the exocytosis of glutamate from presynaptic photoreceptor terminal active zones.",
          "It eliminated baseline lateral inhibition, producing supranormal ON bipolar depolarization and elevated ganglion spiking."
        ],
        "a": 3,
        "e": "<strong>Pharmacological blockade of lateral inhibition by gabazine:</strong> In the retina, horizontal cells provide tonic and feedback inhibitory GABAergic input onto photoreceptor synaptic pedicles and bipolar cell dendrites. When gabazine (a competitive GABA$_A$ receptor antagonist) is applied, it blocks ionotropic GABA$_A$ receptors, eliminating this lateral inhibitory tone. As seen in Table 1, under center spot illumination alone, ON bipolar cells depolarized to $-38\\text{ mV}$ and ON ganglion cells fired at $68.4\\text{ Hz}$. When gabazine was co-applied, the removal of resting inhibitory GABAergic tone allowed the ON bipolar cell to depolarize even further (to $-34\\text{ mV}$), which elicited supranormal glutamate release onto the ON ganglion cell, elevating its firing rate to $84.7\\text{ Hz}$.<br><br><em>Distractor Traps:</em><br>&bull; A is refuted by the data: ON bipolar depolarization increased (to $-34\\text{ mV}$), not suppressed.<br>&bull; B is false: photoreceptor potential was unchanged at $-26\\text{ mV}$.<br>&bull; C contradicts the mechanism: glutamate exocytosis was enhanced, as demonstrated by the heightened downstream ganglion spike rate."
      }
    ]
}
