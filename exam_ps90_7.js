/* ---- exam_ps90_7.js ---- */
/* Full 90-minute Psych/Soc Practice Exam 7: 7 passages (42 Qs) + 10 discrete Qs = 52 Qs */
const EXAM_PS90_7 = [
  {
    "id": "exam_ps90_7_p1",
    "sec": "P/S",
    "topic": "Altered States: Hypnotic Dissociation, Hilgard's Neodissociation Theory & DMN Attenuation",
    "sheet": 1,
    "label": "Psychological, Social, and Biological Foundations of Behavior",
    "examId": "ps90_7",
    "passage": "<div class=\"ttl\">Passage 1 (Questions 1&ndash;6)</div>\n<p>Hypnosis is a distinctive cognitive state characterized by focused sustained attention, heightened suggestibility, imaginative absorption, and diminished peripheral awareness. Theoretical frameworks explaining hypnotic phenomenology diverge between state and non-state models. Ernest Hilgard's <em>neodissociation theory</em> posits that hypnotic induction causes an executive division in conscious awareness into two simultaneous streams: one stream responds directly to the hypnotist's suggestions (executing analgesia or involuntary motor behaviors), while a second, detached cognitive stream termed the <em>hidden observer</em> continues to monitor objective sensory reality without conscious distress. Conversely, the <em>social cognitive (role) theory</em> contends that hypnosis does not represent a unique neurobiological state of consciousness, but rather emerges from ordinary socio-psychological mechanisms: role enactment, compliance, demand characteristics, and participant expectations.</p>\n<p>Modern functional neuroimaging (fMRI) and electroencephalography (EEG) elucidate the neurocircuitry of hypnotic absorption. Hypnotic induction consistently attenuates functional connectivity within the <em>Default Mode Network</em> (DMN)&mdash;comprising the posterior cingulate cortex (PCC), precuneus, and medial prefrontal cortex (mPFC)&mdash;a network active during internal self-referential thought and mind-wandering. Concurrently, hypnosis induces functional decoupling between the central executive network (dorsolateral prefrontal cortex, dlPFC) and the salience network (dorsal anterior cingulate cortex, dACC), impairing top-down conflict monitoring and reality testing while permitting effortless executive control surrender.</p>\n<p>Cognitive neuroscientists evaluated 48 healthy volunteers stratified by the Stanford Hypnotic Susceptibility Scale: Form C (SHSS-C) into High Susceptibility (SHSS-C score 9&ndash;12) and Low Susceptibility (SHSS-C score 0&ndash;3) cohorts. Participants underwent a standardized cold-pressor pain paradigm (4&deg;C water immersion for 60 seconds) across three conditions: Baseline Waking, Hypnotic Analgesia Suggestion (\"glove anesthesia\"), and Active Role-Simulation Control (instructed to actively simulate hypnotic analgesia). Physiological skin conductance response (SCR, reflecting sympathetic arousal), subjective pain intensity (0&ndash;100 Visual Analog Scale), and resting-state DMN functional connectivity (<em>z</em>-score) were quantified (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Cold-pressor pain metrics and neurofunctional connectivity across experimental conditions</caption>\n  <thead>\n    <tr><th>Cohort &amp; Experimental Condition</th><th>Mean Subjective Pain (0&ndash;100 VAS)</th><th>Peak SCR (&mu;S)</th><th>DMN Functional Connectivity (<em>z</em>-score)</th><th>dlPFC-dACC Coherence (<em>r</em>)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Low Susceptibility &ndash; Baseline Waking</td><td>82.4 &plusmn; 4.2</td><td>4.85 &plusmn; 0.32</td><td>1.42 &plusmn; 0.08</td><td>0.68 &plusmn; 0.04</td></tr>\n    <tr><td>Low Susceptibility &ndash; Hypnotic Analgesia</td><td>79.1 &plusmn; 3.9</td><td>4.68 &plusmn; 0.28</td><td>1.38 &plusmn; 0.07</td><td>0.65 &plusmn; 0.05</td></tr>\n    <tr><td>Low Susceptibility &ndash; Role Simulation</td><td>34.5 &plusmn; 3.1</td><td>4.72 &plusmn; 0.30</td><td>1.40 &plusmn; 0.09</td><td>0.66 &plusmn; 0.04</td></tr>\n    <tr><td>High Susceptibility &ndash; Baseline Waking</td><td>84.1 &plusmn; 3.8</td><td>4.91 &plusmn; 0.29</td><td>1.45 &plusmn; 0.07</td><td>0.70 &plusmn; 0.05</td></tr>\n    <tr><td>High Susceptibility &ndash; Hypnotic Analgesia</td><td>18.6 &plusmn; 2.4</td><td>4.52 &plusmn; 0.31</td><td>0.46 &plusmn; 0.05</td><td>0.18 &plusmn; 0.03</td></tr>\n    <tr><td>High Susceptibility &ndash; Role Simulation</td><td>22.1 &plusmn; 2.8</td><td>4.88 &plusmn; 0.33</td><td>1.39 &plusmn; 0.08</td><td>0.67 &plusmn; 0.04</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "Which core postulate of Ernest Hilgard's neodissociation theory of hypnosis is most directly demonstrated during hypnotic analgesia?",
        "ch": [
          "An executive cognitive division isolates conscious pain awareness while physiological sensory monitoring persists",
          "Hypnotic responsiveness is governed solely by social expectations, demand characteristics, and role conformity",
          "Complete sensory blockades occur at the peripheral nociceptors, preventing spinal pain transmission entirely",
          "The central nervous system enters a state of slow-wave sleep that completely eliminates autonomic responses"
        ],
        "a": 0,
        "e": "<strong>Hilgard's neodissociation theory and the hidden observer (Topic 842):</strong> Ernest Hilgard proposed the neodissociation theory of hypnosis, positing that hypnotic induction causes a functional split or division in executive cognitive control. One stream of consciousness is hypnotically suggested and executes subjective analgesia or altered perception, while a separate, dissociated stream&mdash;termed the 'hidden observer'&mdash;remains aware of objective reality and continues to monitor background physiological stimuli. In Table 1, highly susceptible subjects under hypnotic analgesia reported dramatically reduced subjective pain (18.6 vs 84.1), yet their autonomic skin conductance response remained robust (4.52 &mu;S), directly demonstrating this conscious dissociation.<br><br><em>Distractor Traps:</em><br>&bull; B describes the social cognitive (role enactment) theory of hypnosis, which rejects an altered neurobiological state.<br>&bull; C describes local anesthesia, whereas hypnotic analgesia occurs via central cognitive dissociation while peripheral nociceptors fire normally.<br>&bull; D describes deep N3 slow-wave sleep; hypnosis is an awake state characterized by focused attention rather than delta-wave sleep."
      },
      {
        "q": "In Table 1, what critical finding distinguishes true hypnotic analgesia in highly susceptible subjects from active role simulation?",
        "ch": [
          "Role simulation abolished both subjective pain ratings and sympathetic skin conductance responses completely",
          "Hypnotic analgesia selectively decoupled frontoparietal connectivity and attenuated DMN network coherence",
          "Role simulation produced marked neurofunctional decoupling between executive and salience brain networks",
          "Hypnotic analgesia completely eliminated all autonomic sympathetic arousal during the cold-pressor immersion"
        ],
        "a": 1,
        "e": "<strong>Distinguishing hypnotic state from role simulation via neuroimaging (Topic 842):</strong> In Table 1, while both hypnotic analgesia (VAS 18.6) and role simulation (VAS 22.1) in high-susceptibility subjects yielded low subjective pain ratings, they exhibited stark neurobiological differences. True hypnotic analgesia elicited profound neurofunctional decoupling between the executive control network and salience network (dlPFC-dACC coherence dropped to 0.18 vs 0.70 baseline) as well as substantial attenuation of the default mode network (DMN connectivity fell to 0.46 vs 1.45 baseline). In contrast, role-simulating subjects retained normal baseline network connectivity (DMN 1.39, dlPFC-dACC 0.67), proving that role simulation does not reproduce the altered neurofunctional state of hypnosis.<br><br><em>Distractor Traps:</em><br>&bull; A is contradicted by Table 1; role simulation left peak SCR elevated at 4.88 &mu;S and subjective pain at 22.1.<br>&bull; C inverts the experimental finding; role simulation maintained high dlPFC-dACC coherence (0.67), whereas hypnotic analgesia caused decoupling (0.18).<br>&bull; D is contradicted by Table 1; peak SCR remained elevated (4.52 &mu;S) during hypnotic analgesia, confirming autonomic responsiveness."
      },
      {
        "q": "The functional decoupling between the dorsolateral prefrontal cortex (dlPFC) and the dorsal anterior cingulate cortex (dACC) observed during hypnosis contributes to which subjective phenomenon?",
        "ch": [
          "An irreversible loss of episodic memory consolidation mediated by bilateral hippocampal necrosis",
          "A hyperactive focus on somatic threat evaluation that triggers generalized autonomic panic attacks",
          "A marked reduction in critical conflict monitoring that facilitates uncritical acceptance of suggestions",
          "A selective sensory amplification of ambient environmental noise that impairs sustained attention"
        ],
        "a": 2,
        "e": "<strong>Functional neuroanatomy of hypnotic suggestibility (Topic 842):</strong> The dorsal anterior cingulate cortex (dACC) is a central hub of the salience network responsible for error detection, conflict monitoring, and evaluating discrepancies between expectations and sensory input, whereas the dorsolateral prefrontal cortex (dlPFC) mediates top-down executive planning. Functional decoupling between the dlPFC and dACC during hypnosis attenuates conflict detection and critical evaluation, allowing individuals to uncritically accept suggestions (such as tactile numbness or perceptual distortions) without triggering cognitive skepticism or corrective reality testing.<br><br><em>Distractor Traps:</em><br>&bull; A describes severe anterograde amnesia caused by structural hippocampal lesions, not transient hypnotic functional modulation.<br>&bull; B describes acute panic disorder with excessive amygdalar and dACC hyperactivation, the opposite of hypnotic tranquility.<br>&bull; D describes sensory distractibility; hypnosis is characterized by high focal absorption and suppression of peripheral environmental noise."
      },
      {
        "q": "An investigator adhering strictly to the social cognitive perspective of hypnosis would interpret the low subjective pain scores during role simulation as evidence that:",
        "ch": [
          "Hypnosis represents a distinct, evolutionarily conserved altered state of cortical consciousness",
          "Subcortical nociceptive gating mechanisms are entirely bypassed through neurochemical inhibition",
          "Deep hypnotic trances induce irreversible functional disconnection within the primary sensory cortex",
          "Observed hypnotic effects are driven by situational compliance, demand cues, and social role enactment"
        ],
        "a": 3,
        "e": "<strong>Social cognitive role theory of hypnosis (Topic 842):</strong> The social cognitive (or role enactment) theory, championed by researchers such as Nicholas Spanos, asserts that hypnotic behaviors do not reflect a special, altered state of consciousness or dissociated neural stream. Instead, hypnotic responsiveness is driven by everyday socio-cognitive processes: conformity to social expectations, responsiveness to demand characteristics (subtle cues in the experimental setting indicating what behavior is expected), motivation to perform well, and active enactment of the social role of a 'hypnotized subject.' Proponents point to the fact that simulating controls can mimic the behavioral outcomes of hypnosis (e.g., low pain reports) without entering a trance.<br><br><em>Distractor Traps:</em><br>&bull; A defines the state/neodissociation perspective, which social cognitive theorists explicitly reject.<br>&bull; B describes physiological analgesia mediated by endorphinergic or spinothalamic gating mechanisms.<br>&bull; C describes permanent structural or functional disconnection in primary sensory cortex, which is untrue for hypnosis."
      },
      {
        "q": "Mindfulness-based meditation and hypnotic induction both modulate default mode network (DMN) activity. How does the neurophysiology of mindfulness meditation differ from hypnotic absorption?",
        "ch": [
          "Mindfulness meditation enhances frontal alpha and theta oscillatory coherence while sustaining open monitoring",
          "Mindfulness meditation completely suppresses bilateral motor cortex excitability to induce catatonic rigidity",
          "Mindfulness meditation relies exclusively on external verbal prompts to produce passive cognitive trance states",
          "Mindfulness meditation selectively destroys serotonergic projecting pathways arising from the raphe nuclei"
        ],
        "a": 0,
        "e": "<strong>Neurobiology of meditation versus hypnosis (Topic 842):</strong> While both mindfulness meditation and hypnosis downregulate default mode network (DMN) activity (reducing mind-wandering and self-referential rumination), their neurocognitive architectures differ significantly. Mindfulness meditation involves self-directed, non-judgmental present-moment awareness and sustained open monitoring, typically accompanied by enhanced frontal alpha (8&ndash;13 Hz) and theta (4&ndash;8 Hz) oscillatory synchrony and heightened metacognitive awareness. In contrast, hypnosis is characterized by narrowed absorption, focused suggestibility, and functional surrender of executive control, often guided by external verbal cues.<br><br><em>Distractor Traps:</em><br>&bull; B describes catatonia or severe neurological paralysis; meditation produces relaxed muscular tone without motor rigidity.<br>&bull; C describes externally guided hypnosis; mindfulness meditation is typically self-generated and cultivates active cognitive monitoring.<br>&bull; D describes neurotoxic chemical ablation of the dorsal raphe nuclei, not physiological meditation."
      },
      {
        "q": "If researchers failed to include the role-simulation control group in this experimental design, which methodological limitation would most severely undermine their conclusions?",
        "ch": [
          "The inability to measure peripheral sympathetic skin conductance responses during noxious thermal stimulation",
          "The inability to distinguish genuine hypnotic dissociation from conscious behavioral compliance and demand cues",
          "The complete failure to calibrate noxious thermal immersion temperatures across the experimental cohorts",
          "The inability to administer standardized psychometric assessments of hypnotic susceptibility before testing"
        ],
        "a": 1,
        "e": "<strong>Experimental design and demand characteristics in hypnosis research (Topic 842):</strong> In hypnosis research, demand characteristics (subtle environmental cues that inform subjects of the experimenter's hypothesis) pose a profound confounding threat. Subjects might verbally report reduced pain simply to please the researcher or conform to social expectations of how a hypnotized person should act. Martin Orne pioneered the use of the 'real-simulating' paradigm: unhypnotizable subjects are instructed to feign or simulate hypnosis. If 'real' hypnotized subjects differ from simulators only in subjective reports, demand characteristics explain the results; however, if real subjects exhibit distinct physiological or neurofunctional markers (e.g., DMN attenuation and dlPFC-dACC decoupling in Table 1) that simulators cannot replicate, researchers can conclude a genuine altered state exists.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because sympathetic skin conductance is measured directly using galvanic skin electrodes regardless of the control group.<br>&bull; C is incorrect because water immersion temperature is controlled physically by a refrigerated circulating water bath.<br>&bull; D is incorrect because standardized susceptibility scales (SHSS-C) are administered prior to group assignment."
      }
    ]
  },
  {
    "id": "exam_ps90_7_p2",
    "sec": "P/S",
    "topic": "Psychoactive Depressants: GABA-A Receptor Positive Allosteric Modulation & Delirium Tremens",
    "sheet": 1,
    "label": "Psychological, Social, and Biological Foundations of Behavior",
    "examId": "ps90_7",
    "passage": "<div class=\"ttl\">Passage 2 (Questions 7&ndash;12)</div>\n<p>Central nervous system (CNS) depressants, including ethanol, barbiturates, and benzodiazepines, primarily exert their sedative, anxiolytic, anticonvulsant, and motor-depressant actions through modulation of the &gamma;-aminobutyric acid type A (GABA-A) receptor complex. The GABA-A receptor is a heteropentameric ligand-gated chloride (Cl<sup>&minus;</sup>) ion channel typically composed of two &alpha;, two &beta;, and one &gamma; subunit. Endogenous GABA binds at the interface of the &alpha; and &beta; subunits, triggering conformational opening of the central ionophoric pore and facilitating an influx of Cl<sup>&minus;</sup> down its electrochemical gradient. The resulting membrane hyperpolarization shifts the neuronal resting potential further away from the threshold required for action potential firing, dampening overall cortical and subcortical excitability.</p>\n<p>Benzodiazepines and barbiturates act as positive allosteric modulators (PAMs) at distinct, non-overlapping allosteric binding pockets on the GABA-A receptor complex. Benzodiazepines (e.g., diazepam, lorazepam) bind specifically at the junction between the &alpha; and &gamma; subunits, augmenting receptor affinity for GABA and increasing the <em>frequency</em> of channel opening events without altering channel conductance or mean open duration. In contrast, barbiturates (e.g., phenobarbital, thiopental) increase the <em>mean duration</em> of channel opening events; at supratherapeutic concentrations, barbiturates can directly gate open the chloride channel in the complete absence of GABA, imparting a narrow therapeutic index and high mortality risk from medullary respiratory depression. Ethanol exhibits positive allosteric modulation at GABA-A receptors while concurrently inhibiting excitatory <em>N</em>-methyl-D-aspartate (NMDA) glutamate receptors.</p>\n<p>Chronic ethanol administration induces homeostatic neuroadaptations: downregulation and synaptic internalization of GABA-A receptors paired with compensatory transcriptional upregulation of postsynaptic NMDA receptor subunits. Abrupt cessation of ethanol unmasks massive uninhibited glutamatergic neurotransmission and sympathetic hyperactivity, precipitating withdrawal seizures and <em>delirium tremens</em> (DTs). Because ethanol, benzodiazepines, and barbiturates share positive allosteric actions on GABA-A signaling, cross-tolerance emerges, establishing long-acting benzodiazepines as frontline pharmacotherapy for alcohol withdrawal syndrome.</p>\n<p>Neurophysiologists examined rodent cortical slices using whole-cell patch-clamp electrophysiology alongside in vivo electroshock seizure threshold testing across acute and chronic drug exposure conditions (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 In vitro electrophysiological parameters and in vivo seizure thresholds in cortical neurons</caption>\n  <thead>\n    <tr><th>Experimental Treatment Condition</th><th>Normalized Cl<sup>&minus;</sup> Current (<em>I</em>/<em>I</em><sub>0</sub>)</th><th>Mean Open Duration (&tau;, ms)</th><th>Channel Opening Frequency (Hz)</th><th>NMDA EPSC Amplitude (pA)</th><th>Seizure Threshold (mA)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Control (10 &mu;M GABA alone)</td><td>1.00 &plusmn; 0.05</td><td>3.2 &plusmn; 0.2</td><td>12.4 &plusmn; 0.8</td><td>245 &plusmn; 12</td><td>18.2 &plusmn; 0.9</td></tr>\n    <tr><td>GABA + Diazepam (1 &mu;M)</td><td>2.42 &plusmn; 0.11</td><td>3.3 &plusmn; 0.2</td><td>30.8 &plusmn; 1.5</td><td>240 &plusmn; 14</td><td>28.5 &plusmn; 1.4</td></tr>\n    <tr><td>GABA + Phenobarbital (50 &mu;M)</td><td>3.15 &plusmn; 0.14</td><td>9.8 &plusmn; 0.6</td><td>13.1 &plusmn; 0.9</td><td>238 &plusmn; 11</td><td>32.1 &plusmn; 1.6</td></tr>\n    <tr><td>GABA + Ethanol (50 mM)</td><td>1.85 &plusmn; 0.09</td><td>4.1 &plusmn; 0.3</td><td>18.6 &plusmn; 1.1</td><td>112 &plusmn; 8</td><td>24.8 &plusmn; 1.2</td></tr>\n    <tr><td>GABA + Diazepam + Flumazenil (10 &mu;M)</td><td>1.04 &plusmn; 0.06</td><td>3.2 &plusmn; 0.2</td><td>12.9 &plusmn; 0.7</td><td>242 &plusmn; 13</td><td>18.6 &plusmn; 0.8</td></tr>\n    <tr><td>Chronic Ethanol Withdrawal (48 h abstinent)</td><td>0.48 &plusmn; 0.04</td><td>2.8 &plusmn; 0.2</td><td>6.5 &plusmn; 0.5</td><td>485 &plusmn; 22</td><td>8.4 &plusmn; 0.5</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "At typical resting neuronal membrane potentials (approx -70 mV), opening of the GABA-A receptor channel produces an inhibitory postsynaptic potential (IPSP) because:",
        "ch": [
          "Positively charged potassium ions rush rapidly into the intracellular space down their chemical gradient",
          "Positively charged sodium ions are actively exported against their electrochemical gradient by ATP hydrolysis",
          "Negatively charged chloride ions enter the neuron down their concentration gradient, causing hyperpolarization",
          "Negatively charged organic anions diffuse across the lipid bilayer into the surrounding extracellular space"
        ],
        "a": 2,
        "e": "<strong>Biophysics of GABA-A receptor chloride influx and hyperpolarization (Topic 843):</strong> In mammalian central neurons, the intracellular chloride concentration ([Cl<sup>&minus;</sup>]<sub>in</sub> &approx; 5&ndash;10 mM) is substantially lower than extracellular concentration ([Cl<sup>&minus;</sup>]<sub>out</sub> &approx; 110&ndash;120 mM), yielding a chloride equilibrium potential (<em>E</em><sub>Cl</sub>) around &minus;75 to &minus;80 mV. When GABA binds to the GABA-A receptor and opens its ligand-gated ion channel at a resting membrane potential of &minus;70 mV, negatively charged chloride ions (Cl<sup>&minus;</sup>) flow down their chemical concentration gradient into the intracellular fluid. The accumulation of negative anions inside the cell hyperpolarizes the membrane (drives <em>V</em><sub>m</sub> closer to &minus;80 mV), moving it farther away from the threshold for voltage-gated sodium channel activation (&minus;55 mV) and thereby generating an inhibitory postsynaptic potential (IPSP).<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because potassium efflux (out of the cell), not influx, hyperpolarizes neurons.<br>&bull; B describes the continuous primary active transport mediated by the Na<sup>+</sup>/K<sup>+</sup>-ATPase, not ligand-gated channel flux.<br>&bull; D is incorrect because large organic anions (proteins, nucleic acids) are membrane-impermeant and cannot diffuse across the lipid bilayer."
      },
      {
        "q": "According to the electrophysiological recordings presented in Table 1, what fundamental biophysical mechanism distinguishes diazepam from phenobarbital?",
        "ch": [
          "Diazepam blocks NMDA receptor currents, whereas phenobarbital exclusively blocks voltage-gated calcium flux",
          "Diazepam acts as a competitive antagonist at GABA sites, while phenobarbital acts as an irreversible agonist",
          "Diazepam prolongs the mean duration of channel opening, while phenobarbital increases opening frequency",
          "Diazepam increases the frequency of channel openings, whereas phenobarbital prolongs channel open duration"
        ],
        "a": 3,
        "e": "<strong>Electrophysiological distinction between benzodiazepines and barbiturates (Topic 843):</strong> A classic neuropharmacological principle (frequently tested on the MCAT) is that benzodiazepines and barbiturates modulate GABA-A receptors via distinct biophysical mechanisms: (1) <em>Benzodiazepines (diazepam)</em> act by increasing the <em>frequency</em> of chloride channel opening (frenzy = frequency = 'benZodiazepines open with greater frenZy'); in Table 1, diazepam jumped opening frequency from 12.4 Hz to 30.8 Hz without altering mean open duration (3.3 ms vs 3.2 ms control); (2) <em>Barbiturates (phenobarbital)</em> act primarily by increasing the <em>duration</em> of channel opening ('barbiDURATes increase DURATion'); in Table 1, phenobarbital extended mean open duration threefold from 3.2 ms to 9.8 ms while channel frequency remained unchanged (13.1 Hz vs 12.4 Hz).<br><br><em>Distractor Traps:</em><br>&bull; A is contradicted by Table 1; neither diazepam nor phenobarbital blocked NMDA currents (240 and 238 pA vs 245 pA control).<br>&bull; B misclassifies both drugs; diazepam is a positive allosteric modulator, not a competitive antagonist, and phenobarbital is not an irreversible agonist.<br>&bull; C inverts the mechanisms between the two drug classes."
      },
      {
        "q": "What pharmacological phenomenon explains why administering a long-acting benzodiazepine such as chlordiazepoxide successfully mitigates severe alcohol withdrawal?",
        "ch": [
          "Cross-tolerance and shared positive allosteric modulation at GABA-A receptors substitute for absent ethanol",
          "Direct competitive displacement of ethanol molecules from NMDA receptors permanently arrests glutamate flux",
          "Covalent inactivation of hepatic alcohol dehydrogenase prevents toxic buildup of endogenous acetaldehyde",
          "Complete down-regulation of post-synaptic dopamine D2 receptors immediately terminates autonomic tremors"
        ],
        "a": 0,
        "e": "<strong>Cross-tolerance and benzodiazepine pharmacotherapy in alcohol withdrawal (Topic 843):</strong> Cross-tolerance occurs when chronic exposure to one pharmacological agent produces tolerance to another agent that shares the same receptor, intracellular signaling pathway, or cellular mechanism of action. Because ethanol, benzodiazepines, and barbiturates all act as positive allosteric modulators at GABA-A receptors to facilitate chloride-mediated neuronal hyperpolarization, cross-tolerance exists among them. In severe alcohol withdrawal, the sudden removal of ethanol leaves the brain with downregulated GABA-A receptors and upregulated NMDA receptors, causing severe hyperexcitability. Administering a long-acting benzodiazepine (e.g., chlordiazepoxide or diazepam) substitutes for the missing ethanol at the GABA-A receptor, restoring inhibitory tone and preventing life-threatening seizures and delirium tremens.<br><br><em>Distractor Traps:</em><br>&bull; B is incorrect because benzodiazepines bind to GABA-A allosteric sites and do not bind to NMDA receptors.<br>&bull; C describes the mechanism of fomepizole (alcohol dehydrogenase inhibitor) or disulfiram (aldehyde dehydrogenase inhibitor), not benzodiazepines.<br>&bull; D is incorrect because benzodiazepines do not cause immediate down-regulation of dopamine D2 receptors, nor would that treat withdrawal seizures."
      },
      {
        "q": "In a patient experiencing severe delirium tremens during acute alcohol withdrawal, what underlying neurochemical imbalance responsible for this life-threatening state is reflected in Table 1?",
        "ch": [
          "Profound suppression of NMDA glutamate currents combined with supranormal GABA-A chloride hyperpolarization",
          "Excessive glutamatergic excitation via upregulated NMDA receptors paired with impaired GABAergic inhibition",
          "Selective destruction of locus coeruleus noradrenergic cell bodies that paralyzes the sympathetic system",
          "Massive accumulation of inhibitory acetylcholine in the brainstem causing fatal respiratory depression"
        ],
        "a": 1,
        "e": "<strong>Pathophysiology of delirium tremens (Topic 843):</strong> Delirium tremens (DTs) is a severe, life-threatening complication of alcohol withdrawal characterized by autonomic instability (hyperthermia, diaphoresis, tachycardia, severe hypertension), profound agitation, disorientation, visual/tactile hallucinations (formication), and generalized tonic-clonic seizures. In Table 1, 48-hour chronic ethanol withdrawal is characterized neurochemically by: (1) marked reduction in GABA-evoked chloride current (<em>I</em>/<em>I</em><sub>0</sub> dropped to 0.48 and frequency to 6.5 Hz) due to GABA-A receptor downregulation; and (2) nearly a doubling of excitatory NMDA receptor EPSC amplitude (485 pA vs 245 pA baseline). The unmasking of this massive glutamatergic excess in the absence of adequate GABAergic inhibition severely lowers the seizure threshold (from 18.2 mA down to 8.4 mA) and drives runaway autonomic sympathetic hyperactivity.<br><br><em>Distractor Traps:</em><br>&bull; A completely reverses the neurochemical reality; NMDA currents are dramatically increased, not suppressed, and GABA currents are depleted.<br>&bull; C is incorrect because locus coeruleus noradrenergic neurons are massively hyperactive during withdrawal, not destroyed or paralyzed.<br>&bull; D describes organophosphate cholinergic toxidrome, whereas delirium tremens is characterized by sympathomimetic hyperarousal."
      },
      {
        "q": "In Table 1, co-administering flumazenil with diazepam restores chloride current to baseline without affecting phenobarbital or ethanol. This indicates flumazenil functions as:",
        "ch": [
          "A non-competitive irreversible inhibitor that destroys the central pore of the GABA-A receptor complex",
          "A broad-spectrum glutamate receptor agonist that overrides all postsynaptic inhibitory hyperpolarization",
          "A competitive antagonist specifically targeting the benzodiazepine allosteric binding site on GABA-A",
          "A selective serotonin reuptake inhibitor that rapidly clears monoamines from the cortical synaptic cleft"
        ],
        "a": 2,
        "e": "<strong>Pharmacodynamics of flumazenil (Topic 843):</strong> Flumazenil is a selective, competitive antagonist at the benzodiazepine allosteric binding site located at the &alpha;/&gamma; subunit interface of the GABA-A receptor. It occupies the benzodiazepine binding pocket without altering channel conformation or enhancing GABA affinity, thereby competitively displacing benzodiazepine agonists (such as diazepam) and neutralizing their positive allosteric effect. Because barbiturates and ethanol act at distinct, separate allosteric binding sites on the receptor complex, flumazenil does not reverse barbiturate or alcohol toxicity, perfectly matching the electrophysiological data in Table 1.<br><br><em>Distractor Traps:</em><br>&bull; A describes non-competitive pore blockers such as picrotoxin, which non-specifically block all GABA-A currents.<br>&bull; B describes a glutamate agonist, which flumazenil is not.<br>&bull; D describes an SSRI (such as fluoxetine), which acts on the serotonin transporter (SERT) rather than GABA-A receptors."
      },
      {
        "q": "How do the clinical autonomic manifestations of acute barbiturate intoxication contrast with the clinical signs of acute barbiturate withdrawal?",
        "ch": [
          "Intoxication produces severe hyperthermia and tachycardia, whereas withdrawal produces profound hypothermia",
          "Intoxication produces pupillary dilation and hypertension, while withdrawal causes pupillary constriction",
          "Intoxication produces generalized hyperreflexia and tremors, whereas withdrawal causes flaccid paralysis",
          "Intoxication causes respiratory depression and hypotension, whereas withdrawal causes autonomic hyperactivity"
        ],
        "a": 3,
        "e": "<strong>Autonomic manifestations of depressant overdose versus withdrawal (Topic 843):</strong> Acute depressant intoxication (barbiturates, benzodiazepines, ethanol) causes generalized central nervous system depression characterized by: hypoventilation / respiratory depression (decreased medullary sensitivity to CO<sub>2</sub>), bradycardia, hypotension, hypothermia, slurred speech, ataxia, and somnolence/coma. Conversely, acute depressant withdrawal represents an uninhibited autonomic rebound state caused by loss of GABAergic inhibition and unmasked glutamatergic excess: severe autonomic hyperactivity (tachycardia, diaphoresis, severe hypertension, hyperthermia), hyperreflexia, tremors, agitation, insomnia, and tonic-clonic seizures.<br><br><em>Distractor Traps:</em><br>&bull; A inverts temperature and cardiovascular signs; intoxication lowers body temperature and heart rate, while withdrawal elevates them.<br>&bull; B reverses the blood pressure profile and incorrectly attributes hypertension to acute intoxication.<br>&bull; C inverts neuromuscular findings; hyperreflexia and tremors characterize acute withdrawal, while flaccidity/ataxia characterizes overdose."
      }
    ]
  },
  {
    "id": "exam_ps90_7_p3",
    "sec": "P/S",
    "topic": "Psychoactive Stimulants: Monoamine Transporter Reversal (Cocaine, Amphetamines & Adenosine Antagonism)",
    "sheet": 1,
    "label": "Psychological, Social, and Biological Foundations of Behavior",
    "examId": "ps90_7",
    "passage": "<div class=\"ttl\">Passage 3 (Questions 13&ndash;18)</div>\n<p>Central nervous system (CNS) stimulants enhance psychomotor arousal, alertness, vigilance, and locomotor activity by augmenting extracellular monoamine concentrations&mdash;specifically dopamine (DA), norepinephrine (NE), and serotonin (5-HT)&mdash;within forebrain target regions including the nucleus accumbens (NAc) and prefrontal cortex (PFC). Despite producing convergent behavioral phenotypes, stimulants operate via fundamentally divergent molecular mechanisms at the presynaptic terminal.</p>\n<p>Cocaine functions as a classical competitive reuptake inhibitor, binding directly to the external substrate-binding pocket of the presynaptic dopamine transporter (DAT), norepinephrine transporter (NET), and serotonin transporter (SERT). By blocking monoamine clearance from the synaptic cleft, cocaine prolongs and amplifies action potential-dependent monoaminergic signaling. In contrast, amphetamines (e.g., D-amphetamine, methamphetamine) act as substrate analogs. Amphetamine is transported into the presynaptic cytoplasm via DAT, where it disrupts the vesicular proton gradient and reverses the vesicular monoamine transporter 2 (VMAT2), causing massive redistribution of dopamine from intravesicular storage pools into the cytoplasm. Accumulating cytoplasmic DA promotes phosphorylation and conformational reversal of DAT, actively pumping non-vesicular dopamine outward into the synaptic cleft independent of action potential generation or extracellular calcium.</p>\n<p>Other stimulants modulate monoaminergic transmission indirectly. Caffeine is a non-selective competitive antagonist at purinergic adenosine A<sub>1</sub> and A<sub>2A</sub> G-protein coupled receptors. Under basal conditions, extracellular adenosine binds to A<sub>2A</sub> receptors on striatopallidal neurons to exert tonic inhibitory control over dopaminergic neurotransmission; caffeine antagonism removes this brake, promoting wakefulness and disinhibiting dopamine D<sub>2</sub> receptor signaling.</p>\n<p>Pharmacologists monitored extracellular monoamines in the rat nucleus accumbens using in vivo microdialysis alongside open-field locomotor testing across various stimulant and pharmacological pretreatment conditions (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Extracellular monoamines and locomotor activity in rodent nucleus accumbens following stimulant administration</caption>\n  <thead>\n    <tr><th>Experimental Treatment Group</th><th>Extracellular DA (% Baseline)</th><th>Extracellular NE (% Baseline)</th><th>Locomotor Activity (m/30 min)</th><th>Striatal DAT Occupancy (%)</th><th>Dependent on Intact Vesicular Stores?</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Saline Vehicle Control</td><td>100 &plusmn; 4%</td><td>100 &plusmn; 5%</td><td>14.2 &plusmn; 1.8</td><td>0.0 &plusmn; 0.0%</td><td>Yes (basal exocytosis)</td></tr>\n    <tr><td>Cocaine (10 mg/kg)</td><td>320 &plusmn; 15%</td><td>290 &plusmn; 14%</td><td>88.5 &plusmn; 5.2</td><td>78.4 &plusmn; 3.2%</td><td>Yes (exocytosis-dependent)</td></tr>\n    <tr><td>D-Amphetamine (2 mg/kg)</td><td>860 &plusmn; 34%</td><td>510 &plusmn; 22%</td><td>142.6 &plusmn; 8.1</td><td>62.1 &plusmn; 2.8%</td><td>No (VMAT reversal)</td></tr>\n    <tr><td>Caffeine (20 mg/kg)</td><td>145 &plusmn; 8%</td><td>130 &plusmn; 7%</td><td>42.4 &plusmn; 3.1</td><td>1.2 &plusmn; 0.4%</td><td>Yes (disinhibition)</td></tr>\n    <tr><td>Reserpine Pretreatment + D-Amphetamine</td><td>165 &plusmn; 11%</td><td>140 &plusmn; 9%</td><td>36.8 &plusmn; 2.9</td><td>61.5 &plusmn; 2.9%</td><td>No (stores depleted)</td></tr>\n    <tr><td>Reserpine Pretreatment + Cocaine</td><td>110 &plusmn; 6%</td><td>108 &plusmn; 5%</td><td>18.4 &plusmn; 2.1</td><td>77.9 &plusmn; 3.1%</td><td>Yes (stores depleted)</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "What fundamental molecular mechanism distinguishes the synaptic action of amphetamine from that of cocaine?",
        "ch": [
          "Amphetamine reverses the direction of DAT and disrupts VMAT2, while cocaine blocks DAT reuptake",
          "Amphetamine directly activates postsynaptic D2 receptors, whereas cocaine degrades presynaptic MAO",
          "Amphetamine irreversibly destroys dopamine transporters, while cocaine accelerates vesicular storage",
          "Amphetamine acts as a pure adenosine receptor antagonist, whereas cocaine mimics endogenous acetylcholine"
        ],
        "a": 0,
        "e": "<strong>Molecular mechanisms of amphetamine versus cocaine (Topic 844):</strong> The key molecular distinction between cocaine and amphetamine lies in how they elevate synaptic monoamines: (1) <em>Cocaine</em> is a pure reuptake inhibitor that binds competitively to the external pocket of DAT, NET, and SERT, blocking clearance so that normally exocytosed monoamines accumulate in the synaptic cleft; (2) <em>Amphetamine</em> is a transportable substrate that enters the presynaptic terminal, disrupts the vesicular proton gradient, inhibits/reverses VMAT2 to release dopamine into the cytoplasm, and reverses DAT conformation, actively pumping dopamine outward into the synapse independent of action potentials.<br><br><em>Distractor Traps:</em><br>&bull; B is incorrect because neither drug is a direct postsynaptic dopamine receptor agonist, and cocaine does not degrade monoamine oxidase.<br>&bull; C is incorrect because amphetamine does not destroy transporters (it reverses their transport direction), and cocaine does not accelerate vesicular uptake.<br>&bull; D describes the mechanism of caffeine (adenosine antagonism) and nicotine (nicotinic acetylcholine receptor agonism)."
      },
      {
        "q": "Pretreatment with reserpine (which irreversibly blocks VMAT2 and depletes vesicular monoamines) almost completely abolished cocaine's dopaminergic elevation, whereas D-amphetamine still produced a modest elevation. Why did reserpine abolish cocaine's effect?",
        "ch": [
          "Cocaine requires VMAT2 to directly phosphorylate and open ligand-gated postsynaptic chloride ion channels",
          "Cocaine relies on ongoing action potential-driven vesicular exocytosis to supply synaptic cleft dopamine",
          "Cocaine acts as a competitive substrate that must enter intravesicular pools before binding to DAT",
          "Cocaine binds irreversibly to presynaptic alpha-2 adrenergic autoreceptors to stimulate exocytosis"
        ],
        "a": 1,
        "e": "<strong>Vesicular dependence of cocaine versus amphetamine (Topic 844):</strong> Because cocaine is strictly a reuptake blocker, it does not generate new dopamine release on its own; it merely prevents the clearance of dopamine that has already been released via action potential-evoked, calcium-dependent vesicular exocytosis. When reserpine depletes vesicular monoamine stores by blocking VMAT2, vesicular exocytosis yields negligible dopamine release; thus, blocking DAT reuptake with cocaine produces no meaningful elevation in synaptic dopamine (110% vs 100% control in Table 1). In contrast, amphetamine can synthesize and reverse-transport newly synthesized cytoplasmic dopamine even when vesicular stores are depleted.<br><br><em>Distractor Traps:</em><br>&bull; A describes a fictitious mechanism; cocaine does not phosphorylate postsynaptic chloride channels.<br>&bull; C describes amphetamine's substrate behavior; cocaine is a blocker, not a transported substrate that enters vesicles.<br>&bull; D describes alpha-2 autoreceptors, which inhibit (rather than stimulate) exocytosis, and cocaine does not act as an irreversible alpha-2 agonist."
      },
      {
        "q": "Caffeine promotes alertness and elevates wakefulness without directly binding dopamine transporters. According to the passage, through which receptor mechanism does caffeine exert its behavioral stimulant effects?",
        "ch": [
          "Direct agonism at central nicotinic acetylcholine receptors located on postganglionic sympathetic fibers",
          "Positive allosteric modulation of GABA-A chloride channels within the ventral tegmental projection area",
          "Competitive antagonism at purinergic adenosine A1 and A2A G-protein coupled neurochemical receptors",
          "Irreversible inhibition of monoamine oxidase B preventing enzymatic degradation of synaptic dopamine"
        ],
        "a": 2,
        "e": "<strong>Mechanism of action of caffeine (Topic 844):</strong> Caffeine (1,3,7-trimethylxanthine) is the most widely consumed CNS stimulant. Its primary mechanism of action at physiological doses is non-selective competitive antagonism of purinergic adenosine A<sub>1</sub> and A<sub>2A</sub> G-protein coupled receptors. Throughout prolonged wakefulness, extracellular adenosine progressively accumulates in the basal forebrain and cortex, binding to A<sub>1</sub> receptors to inhibit wake-promoting cholinergic/monoaminergic neurons and to A<sub>2A</sub> receptors on striatopallidal GABAergic neurons. By competitively occupying and blocking these adenosine receptors without activating them, caffeine prevents adenosine-mediated sleep drive, promoting cortical desynchronization and disinhibiting striatal dopamine transmission (Table 1 shows caffeine produced only 1.2% DAT occupancy but elevated DA to 145%).<br><br><em>Distractor Traps:</em><br>&bull; A describes nicotine, an agonist at nicotinic acetylcholine receptors.<br>&bull; B describes sedative depressants (benzodiazepines/barbiturates), which enhance GABA-A currents.<br>&bull; D describes selegiline, an MAO-B inhibitor used in Parkinson's disease."
      },
      {
        "q": "Marked pharmacological elevation of systemic norepinephrine and dopamine produces which constellation of peripheral physiological signs in human stimulant users?",
        "ch": [
          "Bradycardia, miosis, bronchoconstriction, and accelerated gastrointestinal peristaltic contractions",
          "Profound central hypothermia, urinary incontinence, systemic vasodilation, and skeletal muscle atonia",
          "Excessive salivation, lacrimation, pupillary constriction, and marked bradycardic cardiac deceleration",
          "Mydriasis, tachycardia, peripheral vasoconstriction, elevated arterial blood pressure, and diaphoresis"
        ],
        "a": 3,
        "e": "<strong>Sympathomimetic toxidrome of CNS stimulants (Topic 844):</strong> Elevating extracellular norepinephrine and dopamine activates the sympathetic branch of the autonomic nervous system via &alpha;<sub>1</sub>, &beta;<sub>1</sub>, and &beta;<sub>2</sub> adrenergic receptors: (1) &alpha;<sub>1</sub> activation on vascular smooth muscle causes peripheral vasoconstriction and elevated systemic blood pressure (hypertension); (2) &alpha;<sub>1</sub> activation on the pupillary dilator muscle causes pupillary dilation (<em>mydriasis</em>); (3) &beta;<sub>1</sub> activation on the cardiac SA node and myocardium causes increased heart rate (tachycardia) and inotropy; (4) sympathetic activation of sweat glands stimulates diaphoresis (sweating); and (5) &beta;<sub>2</sub> activation promotes bronchodilation.<br><br><em>Distractor Traps:</em><br>&bull; A describes parasympathetic excess or opioid intoxication (miosis, bradycardia).<br>&bull; B describes acute sedative-hypnotic overdose or general anesthetic collapse.<br>&bull; C describes the classic cholinergic toxidrome (SLUDGE: salivation, lacrimation, urination, defecation, gastrointestinal distress, emesis)."
      },
      {
        "q": "Following chronic daily administration of high-dose cocaine, individuals typically require progressively larger doses to achieve the same euphoric high. What cellular neuroadaptation primarily accounts for this pharmacodynamic tolerance?",
        "ch": [
          "Upregulation of postsynaptic dopamine D2 receptors to compensate for deficient endogenous ligand levels",
          "Proliteration of unmyelinated axons within the ascending reticular activating system of the brainstem",
          "Downregulation and desensitization of postsynaptic dopamine receptors following chronic synaptic flooding",
          "Permanent structural enlargement of the lateral ventricles leading to widespread loss of cerebral cortex"
        ],
        "a": 2,
        "e": "<strong>Pharmacodynamic tolerance and dopamine receptor downregulation (Topic 844):</strong> Pharmacodynamic tolerance involves homeostatic changes in drug receptors or downstream intracellular signaling cascades in response to chronic drug exposure. Repeated cocaine administration causes chronic flooding of the synaptic cleft with supranormal levels of dopamine. In response to this persistent overstimulation, target medium spiny neurons homeostatically downregulate, internalize, and desensitize postsynaptic dopamine receptors (particularly D<sub>2</sub> receptors) and uncouple them from downstream G-protein second messenger systems. As a consequence, the same dose of cocaine produces a diminished biological response, compelling the user to consume escalating doses to recapture the initial euphoric effect.<br><br><em>Distractor Traps:</em><br>&bull; A inverts the homeostatic response; receptor upregulation occurs during chronic receptor blockade (antagonism) or chronic deprivation, not chronic agonist overstimulation.<br>&bull; B describes non-specific axonal sprouting, which does not mediate pharmacodynamic tolerance.<br>&bull; D describes ventricular enlargement and cortical gray matter atrophy, classic anatomical correlates of chronic schizophrenia."
      },
      {
        "q": "In contrast to pharmacodynamic tolerance, repeated intermittent administration of stimulants can elicit 'behavioral sensitization' (reverse tolerance). This phenomenon is clinically manifested as:",
        "ch": [
          "A progressive diminution of psychomotor agitation requiring escalating drug doses to induce alertness",
          "An accelerated rate of hepatic cytochrome P450 enzymatic clearance that shortens drug plasma half-life",
          "A complete suppression of drug craving accompanied by sustained aversion to drug-paired environments",
          "An augmented locomotor and stereotypic behavioral response to the same or lower stimulant test dose"
        ],
        "a": 3,
        "e": "<strong>Behavioral sensitization / reverse tolerance (Topic 844):</strong> While continuous daily stimulant use typically drives pharmacodynamic tolerance (diminished hedonic response), repeated <em>intermittent</em> exposure to psychostimulants (cocaine, amphetamines) produces <em>behavioral sensitization</em> (also termed reverse tolerance). Sensitization is defined as an augmented, progressive increase in behavioral (locomotor hyperactivity, stereotypy) and neurochemical (dopamine release in the nucleus accumbens) responsiveness to the exact same or even a lower stimulant dose. Sensitization is driven by neuroplastic remodeling in the ventral tegmental area and nucleus accumbens, and is believed to underpin the progressive escalation of drug craving and stimulant-induced paranoid psychosis.<br><br><em>Distractor Traps:</em><br>&bull; A describes classical behavioral and pharmacodynamic tolerance, the exact opposite of sensitization.<br>&bull; B describes pharmacokinetic (metabolic) tolerance, such as enzyme induction by carbamazepine or chronic ethanol.<br>&bull; C describes conditioned taste or place aversion, whereas sensitization intensifies drug seeking and conditioned place preference."
      }
    ]
  },
  {
    "id": "exam_ps90_7_p4",
    "sec": "P/S",
    "topic": "Opiates & Opioids: Mu-Opioid GPCR Activation, Endorphinergic Signaling & Naloxone Reversal",
    "sheet": 1,
    "label": "Psychological, Social, and Biological Foundations of Behavior",
    "examId": "ps90_7",
    "passage": "<div class=\"ttl\">Passage 4 (Questions 19&ndash;24)</div>\n<p>Opioids constitute an essential class of analgesic compounds encompassing natural opiates (e.g., morphine, codeine), semi-synthetic derivatives (e.g., heroin, oxycodone), and fully synthetic agents (e.g., fentanyl, methadone). These substances mimic endogenous opioid neuropeptides (&beta;-endorphins, enkephalins, dynorphins) by activating opioid G-protein coupled receptors, predominantly the mu-opioid receptor (&mu;OR, encoded by the <em>OPRM1</em> gene). The &mu;OR couples to the inhibitory heterotrimeric G<sub>i/o</sub> protein complex.</p>\n<p>Receptor activation by an agonist triggers the dissociation of the G<sub>&alpha;i/o</sub> subunit from the G<sub>&beta;&gamma;</sub> dimer. G<sub>&alpha;i</sub> directly inhibits adenylyl cyclase, reducing intracellular cyclic adenosine monophosphate (cAMP) levels and attenuating protein kinase A (PKA) signaling. Concurrently, free G<sub>&beta;&gamma;</sub> subunits promote the opening of G-protein coupled inwardly rectifying potassium (GIRK) channels, driving K<sup>+</sup> efflux and postsynaptic membrane hyperpolarization, while presynaptically closing voltage-gated N-type calcium (Ca<sup>2+</sup>) channels. In the dorsal horn of the spinal cord (substantia gelatinosa), this dual mechanism suppresses the exocytosis of nociceptive neurotransmitters (substance P and glutamate) from primary afferent terminals. Supraspinally, opioids inhibit local GABAergic interneurons within the periaqueductal gray (PAG) and rostral ventromedial medulla (RVM), disinhibiting descending serotonergic and noradrenergic pathways that extinguish spinal pain transmission.</p>\n<p>Beyond analgesia, &mu;OR activation in the medullary pre-B&ouml;tzinger complex blunts chemoreceptor sensitivity to arterial hypercapnia (elevated PaCO<sub>2</sub>), precipitating lethal respiratory depression. Acute opioid overdose is diagnosed by the classic clinical triad: profound central nervous system depression/coma, pupillary miosis (pinpoint pupils via disinhibition of the parasympathetic Edinger-Westphal nucleus), and respiratory depression. Naloxone is a pure competitive opioid receptor antagonist with high &mu;OR affinity that rapidly displaces agonists from the orthosteric binding pocket, restoring spontaneous respiratory drive within minutes.</p>\n<p>Pharmacologists characterized opioid receptor binding affinities, second-messenger inhibition, tail-flick antinociceptive latency, and minute ventilation across various opioid ligands in a rodent model (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Receptor binding affinities, intracellular signaling efficacy, antinociception, and respiratory depression</caption>\n  <thead>\n    <tr><th>Ligand Compound</th><th>Pharmacological Classification</th><th>&mu;OR Affinity (<em>K</em><sub>i</sub>, nM)</th><th>cAMP Inhibition (EC<sub>50</sub>, nM)</th><th>Tail-Flick Latency (s)</th><th>Minute Ventilation (<em>V</em><sub>E</sub>, mL/min)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Vehicle Control</td><td>Placebo Control</td><td>N/A</td><td>N/A</td><td>2.4 &plusmn; 0.2</td><td>182 &plusmn; 9</td></tr>\n    <tr><td>Morphine</td><td>Full &mu;OR Agonist</td><td>1.8 &plusmn; 0.1</td><td>4.2 &plusmn; 0.3</td><td>9.8 &plusmn; 0.6</td><td>92 &plusmn; 6</td></tr>\n    <tr><td>Fentanyl</td><td>High-Potency Full Agonist</td><td>0.09 &plusmn; 0.01</td><td>0.15 &plusmn; 0.02</td><td>10.0 &plusmn; 0.5 (cutoff)</td><td>41 &plusmn; 4</td></tr>\n    <tr><td>Buprenorphine</td><td>Partial &mu;OR Agonist</td><td>0.21 &plusmn; 0.02</td><td>1.1 &plusmn; 0.1</td><td>8.2 &plusmn; 0.5</td><td>138 &plusmn; 8</td></tr>\n    <tr><td>Naloxone</td><td>Pure Competitive Antagonist</td><td>0.85 &plusmn; 0.05</td><td>&gt;10,000 (inactive)</td><td>2.3 &plusmn; 0.2</td><td>184 &plusmn; 10</td></tr>\n    <tr><td>Fentanyl + Naloxone (1 mg/kg)</td><td>Competitive Displacement</td><td>0.85 &plusmn; 0.06</td><td>&gt;10,000 (displaced)</td><td>2.5 &plusmn; 0.2</td><td>176 &plusmn; 9</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "At the subcellular level, what immediate intracellular signaling events follow mu-opioid receptor activation by an agonist?",
        "ch": [
          "Inhibition of adenylyl cyclase, opening of GIRK potassium channels, and closure of presynaptic calcium channels",
          "Stimulation of adenylate cyclase, mobilization of IP3 calcium stores, and opening of postsynaptic sodium channels",
          "Direct activation of receptor tyrosine kinases, phosphorylation of MAP kinase, and transcription of opioid genes",
          "G-protein coupling to Gs alpha subunits, elevated cyclic AMP levels, and depolarization of primary afferents"
        ],
        "a": 0,
        "e": "<strong>Mu-opioid GPCR intracellular signaling cascade (Topic 845):</strong> The mu-opioid receptor is a 7-transmembrane G-protein coupled receptor linked to the pertussis toxin-sensitive heterotrimeric G<sub>i/o</sub> protein complex. Upon agonist binding: (1) The G<sub>&alpha;i</sub> subunit inhibits adenylyl cyclase, decreasing cAMP synthesis and reducing protein kinase A (PKA) activity; (2) The dissociated G<sub>&beta;&gamma;</sub> subunits bind directly to G-protein coupled inwardly rectifying potassium (GIRK) channels to stimulate K<sup>+</sup> efflux, causing membrane hyperpolarization of postsynaptic pain transmission neurons; and (3) G<sub>&beta;&gamma;</sub> subunits directly inhibit voltage-gated N-type Ca<sup>2+</sup> channels presynaptically, preventing Ca<sup>2+</sup> influx and halting vesicle fusion and exocytosis of substance P and glutamate.<br><br><em>Distractor Traps:</em><br>&bull; B describes G<sub>q</sub> (phospholipase C / IP3 / DAG) or G<sub>s</sub> second messenger signaling, which stimulate rather than inhibit neuronal firing.<br>&bull; C describes receptor tyrosine kinase (RTK) growth factor cascades, not GPCR opioid signaling.<br>&bull; D describes G<sub>s</sub>-mediated adenylyl cyclase activation, which would depolarize rather than hyperpolarize primary afferents."
      },
      {
        "q": "A 28-year-old unresponsive patient is brought to the emergency department. Which classic clinical triad definitively suggests acute opioid toxicity?",
        "ch": [
          "Hyperpyrexia, marked pupillary mydriasis, and persistent dry flushed skin with urinary retention",
          "Severe central nervous system depression, pinpoint pupillary miosis, and profound respiratory depression",
          "Sustained tonic-clonic motor seizures, visual hallucinations, and severe hypertensive cardiovascular crisis",
          "Massive watery diarrhea, lacrimation, diaphoresis, and uncontrolled involuntary gastrointestinal emesis"
        ],
        "a": 1,
        "e": "<strong>Classic clinical triad of acute opioid toxicity (Topic 845):</strong> Acute opioid overdose is diagnosed clinically by the hallmark triad of: (1) <em>Profound CNS depression</em> (stupor or unarousable coma); (2) <em>Pinpoint pupillary miosis</em> (extreme pupillary constriction caused by opioid-mediated disinhibition of the parasympathetic nucleus of Edinger-Westphal / cranial nerve III); and (3) <em>Severe respiratory depression</em> (markedly reduced respiratory rate and tidal volume due to blunted sensitivity of the medullary pre-B&ouml;tzinger complex to hypercapnia). Hypoxemia from respiratory depression can eventually lead to secondary brain injury and death if not reversed promptly with naloxone.<br><br><em>Distractor Traps:</em><br>&bull; A describes the anticholinergic toxidrome ('hot as a hare, blind as a bat [mydriasis], dry as a bone, red as a beet, mad as a hatter').<br>&bull; C describes severe psychostimulant toxicity or acute delirium tremens.<br>&bull; D describes the acute cholinergic toxidrome (SLUDGE) or severe opioid withdrawal (rhinorrhea, lacrimation, diarrhea, emesis)."
      },
      {
        "q": "In Table 1, buprenorphine exhibits submaximal antinociception and a higher minute ventilation (138 mL/min) than morphine or fentanyl, despite binding with high affinity. This reflects buprenorphine's status as a:",
        "ch": [
          "Pure competitive antagonist that completely blocks endogenous endorphin transmission",
          "Irreversible allosteric inhibitor that permanently inactivates mu-opioid receptors",
          "Partial agonist with a clinical ceiling effect on life-threatening respiratory depression",
          "Low-affinity prodrug that requires extensive hepatic conversion to active fentanyl"
        ],
        "a": 2,
        "e": "<strong>Pharmacodynamics of buprenorphine as a partial agonist (Topic 845):</strong> Buprenorphine is a partial agonist at the mu-opioid receptor characterized by very high binding affinity (<em>K</em><sub>i</sub> = 0.21 nM, binding more tightly than morphine at 1.8 nM) but low intrinsic efficacy (submaximal receptor activation). Because of its partial agonism, buprenorphine exhibits a crucial pharmacological 'ceiling effect' for respiratory depression: even at escalating doses, it does not completely extinguish respiratory drive (in Table 1, minute ventilation remained at 138 mL/min, compared to 41 mL/min for fentanyl). This favorable safety profile makes buprenorphine a cornerstone for outpatient treatment of opioid use disorder (medication-assisted treatment).<br><br><em>Distractor Traps:</em><br>&bull; A describes naloxone, a pure competitive antagonist with zero intrinsic efficacy.<br>&bull; B describes irreversible allosteric covalent inactivation, which does not characterize buprenorphine.<br>&bull; D describes codeine (which converts to morphine via CYP2D6); buprenorphine is not a prodrug for fentanyl."
      },
      {
        "q": "Naloxone effectively reverses fentanyl-induced respiratory arrest as shown in Table 1. However, patients administered naloxone often require repeat doses because:",
        "ch": [
          "Naloxone permanently alters blood-brain barrier permeability, allowing fentanyl molecules to cross faster",
          "Naloxone functions as a positive allosteric modulator that becomes depleted during cellular transcription",
          "Fentanyl binds irreversibly to presynaptic dopamine transporters, permanently resisting displacement",
          "Naloxone has a substantially shorter elimination half-life than most synthetic opioid receptor agonists"
        ],
        "a": 3,
        "e": "<strong>Pharmacokinetics of naloxone reversal (Topic 845):</strong> Naloxone is a pure, competitive antagonist with high affinity for the &mu;OR (<em>K</em><sub>i</sub> = 0.85 nM in Table 1). When administered parenterally, it rapidly crosses the blood-brain barrier and competitively displaces opioid agonists from the receptor pocket, completely reversing respiratory depression within 1&ndash;2 minutes. However, naloxone has a short plasma elimination half-life of approximately 30 to 90 minutes. Many synthetic opioids, such as fentanyl, methadone, or sustained-release oxycodone, possess much longer elimination half-lives (hours to days). When naloxone is metabolized and cleared, residual opioid molecules in the bloodstream re-bind to unoccupied mu-opioid receptors, precipitating renarcotization and recurrent respiratory arrest if repeat doses or a continuous infusion are not administered.<br><br><em>Distractor Traps:</em><br>&bull; A describes an unfounded alteration in blood-brain barrier permeability.<br>&bull; B misclassifies naloxone as a positive allosteric modulator and suggests it is consumed via transcription.<br>&bull; C incorrectly states fentanyl binds irreversibly to dopamine transporters; fentanyl binds reversibly to mu-opioid receptors."
      },
      {
        "q": "How does supraspinal opioid administration in the periaqueductal gray (PAG) initiate descending pain inhibition to suppress spinal dorsal horn nociception?",
        "ch": [
          "By inhibiting local GABAergic interneurons, thereby disinhibiting descending serotonergic and noradrenergic projections",
          "By directly activating thalamocortical sensory projections that accelerate nociceptive perception in the somatosensory cortex",
          "By selectively severing the arcuate fasciculus white matter tract that links receptive speech areas to motor speech centers",
          "By destroying substance P storage vesicles within postganglionic parasympathetic nerve terminals of the vagus nerve"
        ],
        "a": 0,
        "e": "<strong>Neuroanatomy of descending pain modulation (Topic 845):</strong> The periaqueductal gray (PAG) of the midbrain and the rostral ventromedial medulla (RVM) are critical supraspinal centers for endogenous opioid-mediated analgesia. Under basal conditions, tonic output from local inhibitory GABAergic interneurons suppresses projection neurons that descend to the spinal cord. When opioids bind to &mu;ORs on these GABAergic interneurons in the PAG, they hyperpolarize and silence them. This process&mdash;termed <em>disinhibition</em>&mdash;activates descending projection neurons to the RVM and locus coeruleus, which in turn project descending serotonergic (5-HT) and noradrenergic (NE) fibers into the dorsal horn of the spinal cord to inhibit spinothalamic nociceptive transmission.<br><br><em>Distractor Traps:</em><br>&bull; B describes sensory pain amplification, the exact opposite of analgesic pain gating.<br>&bull; C describes lesioning the arcuate fasciculus, which causes conduction aphasia rather than pain modulation.<br>&bull; D describes vagal nerve vesicle destruction, which does not mediate central analgesia."
      },
      {
        "q": "Chronic opioid therapy frequently leads to profound analgesic tolerance. Which two physiological effects of opioids typically show minimal or no tolerance over prolonged treatment?",
        "ch": [
          "Euphoria and respiratory depression",
          "Constipation and pupillary miosis",
          "Antinociception and sedation",
          "Pruritus and cognitive clouding"
        ],
        "a": 1,
        "e": "<strong>Differential tolerance to opioid effects (Topic 845):</strong> With repeated, chronic opioid administration, patients develop marked pharmacodynamic tolerance to many opioid effects, including analgesia (antinociception), euphoria, sedation, nausea, and respiratory depression. However, tolerance does not develop uniformly across all physiological responses. Crucially, <em>constipation</em> (gastrointestinal hypomotility mediated by mu-opioid receptors in the enteric myenteric plexus) and <em>pupillary miosis</em> (pinpoint pupils mediated by the Edinger-Westphal parasympathetic nucleus) exhibit minimal to no tolerance. Even long-term opioid-tolerant individuals continue to suffer from chronic opioid-induced constipation and display constricted pupils.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because patients develop substantial tolerance to both euphoria and respiratory depression.<br>&bull; C is incorrect because analgesia and sedation exhibit pronounced pharmacodynamic tolerance.<br>&bull; D is incorrect because histamine-mediated pruritus and cognitive sedation typically attenuate with chronic use."
      }
    ]
  },
  {
    "id": "exam_ps90_7_p5",
    "sec": "P/S",
    "topic": "Neurobiology of Substance Addiction: Mesolimbic Dopaminergic Circuitry (VTA to Nucleus Accumbens)",
    "sheet": 1,
    "label": "Psychological, Social, and Biological Foundations of Behavior",
    "examId": "ps90_7",
    "passage": "<div class=\"ttl\">Passage 5 (Questions 25&ndash;30)</div>\n<p>The neurobiology of substance use disorders is anchored in maladaptive neuroplasticity within the brain's reward circuitry, predominantly the <em>mesolimbic dopaminergic pathway</em>. Dopaminergic projection neurons originating in the <em>ventral tegmental area</em> (VTA) of the midbrain extend axonal projections via the medial forebrain bundle to terminate in the <em>nucleus accumbens</em> (NAc, specifically the NAc shell). The VTA also projects to the prefrontal cortex (PFC, mesocortical pathway), amygdala, and hippocampus, integrating reward signaling with executive decision-making, emotional conditioning, and contextual associative memory.</p>\n<p>Under baseline conditions, burst firing of VTA dopaminergic neurons conveys a reward prediction error that drives reinforcement learning. Addictive drugs hijack this circuit: while natural reinforcers (food, sex) produce modest, habituating dopamine elevations, drugs of abuse induce supraphysiological, non-habituating dopamine surges in the NAc. According to Robinson and Berridge's <em>incentive-sensitization theory</em>, addiction involves an enduring neurobiological dissociation between \"wanting\" (incentive salience, mediated by mesolimbic dopamine) and \"liking\" (subjective hedonic impact, mediated by discrete opioid and cannabinoid \"hedonic hotspots\" in the NAc and ventral pallidum). Repeated drug exposure sensitizes the mesolimbic dopamine system, transforming drug-associated conditioned stimuli into potent incentive magnets that provoke compulsive craving, even as hedonic \"liking\" declines due to pharmacodynamic tolerance.</p>\n<p>Chronic drug intake triggers long-lasting molecular alterations in striatal medium spiny neurons (MSNs). Sustained dopamine elevation leads to transcriptional accumulation of the stable, truncated transcription factor &Delta;FosB, which persists for weeks to months, remodeling dendritic spine architecture and locking in vulnerability to relapse. Concurrently, positron emission tomography (PET) imaging reveals marked downregulation of striatal dopamine D<sub>2</sub> receptor binding potential paired with prefrontal \"hypofrontality\" (reduced baseline metabolic activity in orbitofrontal and anterior cingulate cortices), impairing top-down behavioral inhibition.</p>\n<p>Neuroscientists monitored intravenous self-administration (IVSA) of cocaine in rodents across short-access (ShA, 1 h/day) and extended-access (LgA, 6 h/day) regimens alongside PET imaging and molecular assays (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Behavioral, neurochemical, and imaging metrics in rodent cocaine self-administration models</caption>\n  <thead>\n    <tr><th>Experimental Cohort &amp; Intervention</th><th>Daily Cocaine Infusions</th><th>Striatal D<sub>2</sub> Receptor Binding (<em>B</em><sub>max</sub>/<em>K</em><sub>d</sub>)</th><th>PFC Glucose Metabolism (&mu;mol/100g/min)</th><th>Striatal &Delta;FosB Protein (% Control)</th><th>Cue-Induced Reinstatement (Lever Presses)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Saline Control (1 h/day)</td><td>0 &plusmn; 0</td><td>3.45 &plusmn; 0.14</td><td>74.2 &plusmn; 3.1</td><td>100 &plusmn; 5%</td><td>4.2 &plusmn; 0.8</td></tr>\n    <tr><td>Short-Access Cocaine (ShA: 1 h/day)</td><td>18.4 &plusmn; 1.2</td><td>3.12 &plusmn; 0.12</td><td>68.5 &plusmn; 2.8</td><td>135 &plusmn; 7%</td><td>16.5 &plusmn; 1.4</td></tr>\n    <tr><td>Extended-Access Cocaine (LgA: 6 h/day)</td><td>84.6 &plusmn; 4.5</td><td>1.65 &plusmn; 0.08</td><td>42.1 &plusmn; 2.2</td><td>385 &plusmn; 18%</td><td>68.4 &plusmn; 4.2</td></tr>\n    <tr><td>LgA + Quinpirole (D<sub>2</sub> Agonist)</td><td>48.2 &plusmn; 3.1</td><td>2.45 &plusmn; 0.11</td><td>58.4 &plusmn; 2.6</td><td>320 &plusmn; 15%</td><td>34.2 &plusmn; 2.5</td></tr>\n    <tr><td>LgA + &Delta;FosB Antisense Oligo</td><td>82.1 &plusmn; 4.1</td><td>1.70 &plusmn; 0.09</td><td>44.5 &plusmn; 2.4</td><td>115 &plusmn; 6%</td><td>18.2 &plusmn; 1.6</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "Which anatomical pathway constitutes the primary neurobiological substrate of the mesolimbic dopamine reward system?",
        "ch": [
          "Dopaminergic neurons in the ventral tegmental area projecting axons directly to the nucleus accumbens shell",
          "Noradrenergic cell bodies in the locus coeruleus projecting axons exclusively to the lateral geniculate body",
          "Cholinergic interneurons located in the striatum projecting efferents to the primary somatosensory cortex",
          "Serotonergic projection neurons in the dorsal raphe projecting diffusely into the anterior pituitary gland"
        ],
        "a": 0,
        "e": "<strong>Anatomy of the mesolimbic dopamine pathway (Topic 847):</strong> The mesolimbic dopamine pathway is the principal reward and positive reinforcement circuit in the mammalian brain. It originates from dopaminergic A10 cell bodies located in the ventral tegmental area (VTA) of the ventral midbrain. These neurons send ascending axons through the medial forebrain bundle to innervate the ventral striatum, terminating predominantly within the shell and core of the nucleus accumbens (NAc). Natural rewards as well as all major drugs of abuse stimulate dopamine release from VTA terminals into the NAc, reinforcing goal-directed behaviors.<br><br><em>Distractor Traps:</em><br>&bull; B describes noradrenergic projections from the locus coeruleus, which mediate arousal and vigilance, and the lateral geniculate body is a visual relay.<br>&bull; C describes striatal cholinergic interneurons, which modulate motor striatal output, not the primary reward pathway.<br>&bull; D describes serotonergic raphe projections, which project throughout the forebrain rather than the anterior pituitary gland."
      },
      {
        "q": "According to the incentive-sensitization theory of addiction, what key neurochemical distinction explains escalating drug intake despite diminished pleasure?",
        "ch": [
          "Dopamine circuits generate hedonic liking, while endogenous opioid networks mediate compulsive drug craving",
          "Mesolimbic dopamine mediates incentive salience (wanting), whereas hedonic liking relies on opioid hotspots",
          "Both wanting and liking are controlled exclusively by GABAergic projections originating in the cerebellum",
          "Sensitization of serotonin 5-HT2A receptors causes hallucinations that replace all physical drug cravings"
        ],
        "a": 1,
        "e": "<strong>Incentive-sensitization theory: 'wanting' versus 'liking' (Topic 847):</strong> Robinson and Berridge's incentive-sensitization theory makes a fundamental neurobiological distinction between two reward components: (1) <em>'Wanting' (incentive salience)</em>: the motivational drive and craving to seek a reward, driven by the mesolimbic dopaminergic pathway (VTA to nucleus accumbens); and (2) <em>'Liking' (hedonic impact)</em>: the subjective pleasure or enjoyment experienced when consuming the reward, mediated by discrete opioid, cannabinoid, and GABAergic 'hedonic hotspots' in the nucleus accumbens and ventral pallidum. Chronic drug use produces neuroplastic sensitization of the dopaminergic 'wanting' system (causing pathological craving triggered by cues), while tolerance blunts the hedonic 'liking' system, leading to escalating consumption despite declining pleasure.<br><br><em>Distractor Traps:</em><br>&bull; A completely reverses the neurochemical roles of dopamine (wanting) and opioid circuits (liking).<br>&bull; C incorrectly attributes both processes to cerebellar GABAergic projections.<br>&bull; D refers to 5-HT<sub>2A</sub> hallucinogenic signaling, which does not mediate the core dissociation between wanting and liking in addiction."
      },
      {
        "q": "In Table 1, rats with extended daily cocaine access exhibited a 52% reduction in striatal D2 receptor binding potential. This neuroadaptation clinically correlates with:",
        "ch": [
          "Complete loss of autonomic cardiovascular reflexes accompanied by severe resting orthostatic hypotension",
          "Heightened sensitivity to natural rewards such as palatable foods and social companionship interactions",
          "Blunted reward sensitivity to non-drug stimuli and increased vulnerability to compulsive drug escalation",
          "Acute destruction of the substantia nigra pars compacta producing irreversible parkinsonian bradykinesia"
        ],
        "a": 2,
        "e": "<strong>Striatal D2 receptor downregulation and reward deficiency (Topic 847):</strong> In Table 1, extended cocaine access (LgA) drove a steep downregulation of striatal D<sub>2</sub> receptor binding (from 3.45 to 1.65). Human PET imaging studies (Volkow et al.) consistently demonstrate that chronic abusers of cocaine, alcohol, methamphetamine, and opioids exhibit marked downregulation of striatal D<sub>2</sub> receptors. This creates a hypodopaminergic 'reward deficiency state' characterized by anhedonia and blunted responsiveness to ordinary, natural biological reinforcers (food, social connection). To overcome this chronic anhedonic state, individuals compulsively escalate drug intake, as only drugs of abuse can evoke sufficient dopamine release to stimulate the depleted receptor pool.<br><br><em>Distractor Traps:</em><br>&bull; A describes severe autonomic neuropathy / orthostatic failure.<br>&bull; B is the exact opposite of reality; D<sub>2</sub> downregulation blunts sensitivity to natural rewards, causing anhedonia.<br>&bull; D describes Parkinson's disease, which involves structural degeneration of nigrostriatal dopaminergic neurons rather than down-regulation of mesolimbic D<sub>2</sub> receptors."
      },
      {
        "q": "Extended cocaine self-administration provoked marked prefrontal cortex hypometabolism in Table 1. In human addiction, prefrontal 'hypofrontality' accounts for which clinical symptom?",
        "ch": [
          "Selective degeneration of visual cortex neurons that causes profound cortical blindness and visual agnosia",
          "Complete loss of fine motor coordination due to destruction of anterior cerebellar Purkinje cell layers",
          "Inability to execute primary somatosensory tactile discrimination across distal dermatomal distributions",
          "Impaired executive inhibitory control and cognitive inflexibility that promote compulsive drug relapse"
        ],
        "a": 3,
        "e": "<strong>Prefrontal hypofrontality and loss of top-down inhibitory control (Topic 847):</strong> The prefrontal cortex (PFC), including the dorsolateral PFC, orbitofrontal cortex (OFC), and anterior cingulate cortex (ACC), provides essential 'top-down' executive inhibitory control over subcortical limbic impulses and habit-driven behavior. Chronic substance abuse induces 'hypofrontality'&mdash;characterized by reduced baseline glucose metabolism (shown in Table 1, where PFC metabolism fell from 74.2 to 42.1 &mu;mol/100g/min) and dendritic pruning in the PFC. Clinically, hypofrontality manifests as impaired impulse control, poor decision-making, cognitive inflexibility, and an inability to override intense subcortical drug cravings, driving compulsive relapse even when the patient consciously resolves to remain abstinent.<br><br><em>Distractor Traps:</em><br>&bull; A describes occipital lobe damage leading to cortical blindness or visual associative agnosia.<br>&bull; B describes cerebellar ataxia resulting from Purkinje cell loss (e.g., chronic alcohol cerebellar degeneration).<br>&bull; C describes primary somatosensory cortex (postcentral gyrus) damage."
      },
      {
        "q": "Treatment with DeltaFosB antisense oligonucleotides selectively reduced cue-induced drug-seeking reinstatement without reducing daily drug intake in Table 1. This finding confirms that DeltaFosB:",
        "ch": [
          "Functions as an acute ionotropic channel blocker that directly prevents cocaine entry across the blood-brain barrier",
          "Acts as a rapidly degraded immediate-early gene product that ceases expression within minutes of drug cessation",
          "Serves as a persistent molecular transcription factor mediating long-term structural plasticity and relapse vulnerability",
          "Mediates the acute lethal respiratory depression provoked by high-dose stimulants in mammalian animal models"
        ],
        "a": 2,
        "e": "<strong>Molecular role of DeltaFosB in addiction and relapse (Topic 847):</strong> &Delta;FosB is a uniquely stable, truncated splice variant of the Fos family of transcription factors. Unlike other immediate-early gene products (e.g., c-Fos) that degrade within hours, &Delta;FosB forms extraordinarily stable heterodimers with JunD and resists proteasomal degradation, persisting in striatal medium spiny neurons for weeks to months following repeated drug administration. &Delta;FosB drives downstream transcriptional programs (e.g., upregulating CDK5 and GluA2 AMPA subunits) that induce dendritic remodeling and increase spine density. In Table 1, blocking &Delta;FosB with antisense oligonucleotides selectively abolished cue-induced reinstatement (from 68.4 down to 18.2 lever presses), proving that &Delta;FosB is a critical molecular driver of enduring relapse vulnerability.<br><br><em>Distractor Traps:</em><br>&bull; A claims &Delta;FosB is an ionotropic channel blocker at the blood-brain barrier; it is an intracellular transcription factor.<br>&bull; B describes classic immediate-early genes like c-Fos; &Delta;FosB is uniquely characterized by high molecular persistence.<br>&bull; D describes acute opioid overdose lethality, not chronic striatal transcription factors."
      },
      {
        "q": "What clinical distinction differentiates physiological physical dependence from a substance use disorder (addiction) according to current diagnostic criteria?",
        "ch": [
          "Physical dependence involves compulsive craving, whereas addiction is characterized solely by tolerance",
          "Physical dependence requires legal incarceration, while substance use disorder requires genetic testing",
          "Physical dependence occurs only with illicit narcotics, whereas addiction develops only with alcohol",
          "Physical dependence involves tolerance and withdrawal, whereas addiction involves compulsive drug use despite harm"
        ],
        "a": 3,
        "e": "<strong>Distinction between physical dependence and addiction / substance use disorder (Topic 847):</strong> In modern psychiatric nosology (DSM-5), a vital distinction is maintained between: (1) <em>Physical dependence</em>: an expected neurobiological adaptation to chronic drug administration characterized by pharmacodynamic <em>tolerance</em> (needing higher doses for the same effect) and <em>withdrawal symptoms</em> upon cessation. Physical dependence can occur with non-addictive medications (e.g., beta-blockers, clonidine, corticosteroids) and with properly prescribed opioids without the presence of addiction; and (2) <em>Substance Use Disorder (addiction)</em>: a chronic behavioral syndrome characterized by compulsive drug seeking, loss of behavioral control, intense psychological craving, and continued drug use despite severe negative interpersonal, medical, occupational, or legal consequences.<br><br><em>Distractor Traps:</em><br>&bull; A inverts the two constructs; physical dependence involves tolerance/withdrawal, while addiction involves compulsive craving and behavioral impairment.<br>&bull; B references non-medical administrative or diagnostic criteria that play no role in DSM-5 substance use disorder definitions.<br>&bull; C is factually incorrect; physical dependence and addiction can occur across multiple classes of licit and illicit drugs."
      }
    ]
  },
  {
    "id": "exam_ps90_7_p6",
    "sec": "P/S",
    "topic": "Neural Substrates of Speech: Broca's Area, Wernicke's Area & Arcuate Fasciculus Tractography",
    "sheet": 1,
    "label": "Psychological, Social, and Biological Foundations of Behavior",
    "examId": "ps90_7",
    "passage": "<div class=\"ttl\">Passage 6 (Questions 31&ndash;36)</div>\n<p>Speech and language processing in the human brain are organized within a specialized network predominantly lateralized to the left cerebral hemisphere in over 95% of right-handed and approximately 70% of left-handed individuals. Classical aphasiology delineated two cortical epicenters: <em>Broca's area</em>, situated in the posterior inferior frontal gyrus (pars triangularis and pars opercularis, Brodmann areas 44 and 45), and <em>Wernicke's area</em>, localized to the posterior superior temporal gyrus (Brodmann area 22). In the classical Wernicke-Geschwind model, auditory speech representations decoded in Wernicke's area are relayed to Broca's area via the <em>arcuate fasciculus</em>, a prominent subcortical association white matter tract, where motor articulatory programs are planned and transferred to the primary motor cortex.</p>\n<p>Contemporary cognitive neuroscience has expanded this classical architecture into a dual-stream computational model (Hickok and Poeppel). The <em>ventral stream</em> (bilaterally organized along the middle and inferior temporal gyri) maps acoustic speech signals onto conceptual semantic representations (\"what\" the utterance means). Conversely, the <em>dorsal stream</em> (strongly left-lateralized, traversing the superior temporal sulcus, Sylvian parietal-temporal junction, and the arcuate fasciculus to the inferior frontal cortex) maps acoustic phonological representations onto frontal motor-articulatory programs (\"how\" to vocalize the utterance).</p>\n<p>Diffusion Tensor Imaging (DTI) allows in vivo tractography of the arcuate fasciculus by measuring <em>fractional anisotropy</em> (FA), an index of directional water diffusion reflecting white matter microstructural integrity and myelination. Investigators evaluated 40 participants: 20 neurologically intact controls and 20 stroke patients with focal left-perisylvian ischemic infarcts categorized by lesion site (focal Broca, focal Wernicke, or selective arcuate fasciculus deep white matter transection). Participants completed standardized language tasks under functional MRI (fMRI): a verbal repetition battery (repeating multisyllabic pseudowords) and a semantic decision task (determining whether paired words share categorical meaning) (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 DTI tractography, fMRI BOLD activation, and language performance across experimental cohorts</caption>\n  <thead>\n    <tr><th>Cohort &amp; Lesion Profile</th><th>Arcuate Fasciculus FA</th><th>Left IFG BOLD Activation (% change)</th><th>Left STG BOLD Activation (% change)</th><th>Verbal Repetition Accuracy (%)</th><th>Auditory Comprehension Accuracy (%)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Neurologically Intact Controls</td><td>0.54 &plusmn; 0.03</td><td>+1.42 &plusmn; 0.08%</td><td>+1.38 &plusmn; 0.07%</td><td>98.4 &plusmn; 1.2%</td><td>97.8 &plusmn; 1.4%</td></tr>\n    <tr><td>Focal Broca Lesion (Left IFG)</td><td>0.48 &plusmn; 0.03</td><td>+0.12 &plusmn; 0.02%</td><td>+1.35 &plusmn; 0.08%</td><td>44.2 &plusmn; 3.1%</td><td>89.5 &plusmn; 3.2%</td></tr>\n    <tr><td>Focal Wernicke Lesion (Left STG)</td><td>0.47 &plusmn; 0.02</td><td>+1.39 &plusmn; 0.07%</td><td>+0.15 &plusmn; 0.03%</td><td>38.6 &plusmn; 2.8%</td><td>32.4 &plusmn; 2.6%</td></tr>\n    <tr><td>Selective Arcuate Fasciculus Transection</td><td>0.21 &plusmn; 0.02</td><td>+1.38 &plusmn; 0.06%</td><td>+1.34 &plusmn; 0.07%</td><td>24.5 &plusmn; 2.1%</td><td>92.6 &plusmn; 2.9%</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "Which functional division correctly matches Broca's area and Wernicke's area with their primary linguistic specializations?",
        "ch": [
          "Broca's area mediates motor speech production and syntax, while Wernicke's area mediates semantic comprehension",
          "Broca's area mediates phonological sound decoding, while Wernicke's area controls somatic vocal cord movements",
          "Broca's area translates visual text into auditory imagery, while Wernicke's area generates affective vocal prosody",
          "Broca's area stores episodic vocabulary memories, whereas Wernicke's area coordinates grammatical tense syntax"
        ],
        "a": 0,
        "e": "<strong>Functional specialization of Broca's versus Wernicke's areas (Topic 849):</strong> In the left perisylvian language network: (1) <em>Broca's area</em> (posterior inferior frontal gyrus, Brodmann areas 44 and 45) is specialized for motor speech planning, articulatory programming, and syntactic sentence construction; (2) <em>Wernicke's area</em> (posterior superior temporal gyrus, Brodmann area 22) is specialized for auditory speech comprehension, phonological decoding, and accessing the semantic mental lexicon.<br><br><em>Distractor Traps:</em><br>&bull; B completely reverses their functions, assigning receptive sound decoding to Broca's and motor vocalization to Wernicke's.<br>&bull; C describes the angular gyrus (visual-phonological translation) and the contralateral right hemisphere (affective prosody).<br>&bull; D incorrectly attributes episodic memory storage (hippocampus/temporal cortex) to Broca's and grammatical syntax to Wernicke's."
      },
      {
        "q": "In Table 1, patients with selective arcuate fasciculus transection exhibited a profound drop in repetition accuracy (24.5%) while maintaining high comprehension (92.6%). This dissociation occurs because:",
        "ch": [
          "Auditory inputs are completely blocked at the level of the inner ear cochlear hair cells",
          "Wernicke's area has undergone massive cellular apoptosis that permanently abolishes speech perception",
          "Motor execution neurons in the primary precentral gyrus are completely paralyzed bilaterally",
          "Phonological input processed in the temporal lobe cannot be transferred to frontal speech motor networks"
        ],
        "a": 3,
        "e": "<strong>Disconnection syndrome and the arcuate fasciculus (Topic 849):</strong> The arcuate fasciculus is the primary white matter association tract that monosynaptically connects the temporal auditory comprehension hub (Wernicke's area) with the frontal motor speech planning hub (Broca's area). Selective damage or transection of this tract constitutes a classic 'disconnection syndrome' (conduction aphasia). The temporal lobe decodes auditory input normally (preserving comprehension at 92.6% in Table 1), and Broca's area can spontaneously generate speech, but acoustic phonological representations cannot be relayed directly to the motor articulatory system for verbatim repetition, collapsing repetition accuracy to 24.5%.<br><br><em>Distractor Traps:</em><br>&bull; A describes peripheral sensorineural hearing loss, which would destroy both comprehension and repetition.<br>&bull; B is contradicted by Table 1; Wernicke's area (left STG) activation (+1.34%) and comprehension (92.6%) were preserved.<br>&bull; C describes bilateral motor paralysis (corticospinal/corticobulbar damage), which would cause mutism or severe dysarthria rather than isolated repetition failure."
      },
      {
        "q": "According to the dual-stream neuroanatomical model of speech perception described in the passage, what functional task is primarily handled by the left-lateralized dorsal stream?",
        "ch": [
          "Decoding the conceptual and contextual semantic meaning of spoken phrases",
          "Mapping acoustic speech signals onto frontal motor articulatory networks",
          "Modulating emotional affective vocal inflections and musical cadence rhythm",
          "Storing long-term episodic memories of historical conversational narratives"
        ],
        "a": 1,
        "e": "<strong>The dual-stream model of speech processing (Topic 849):</strong> In Hickok and Poeppel's dual-stream model: (1) The <em>dorsal stream</em> is strongly left-hemisphere dominant and links the posterior superior temporal cortex with frontal premotor regions via the arcuate fasciculus, performing sensorimotor integration by translating acoustic auditory speech signals into frontal articulatory motor representations ('sound-to-action'); (2) The <em>ventral stream</em> is bilaterally distributed along temporal lobes and maps acoustic speech signals onto lexical and semantic conceptual representations ('sound-to-meaning').<br><br><em>Distractor Traps:</em><br>&bull; A describes the role of the ventral stream.<br>&bull; C describes prosodic and musical processing, which is primarily mediated by the non-dominant right hemisphere.<br>&bull; D describes episodic declarative memory, which is mediated by medial temporal lobe structures (hippocampus)."
      },
      {
        "q": "While left perisylvian networks govern syntactic structure and lexical semantics in most adults, what linguistic capability is predominantly mediated by the contralateral right hemisphere?",
        "ch": [
          "Motor execution of fine phonemic articulatory movements during vocalization",
          "Syntactic rule computation and grammatical agreement between nouns and verbs",
          "Comprehension of emotional vocal prosody, pragmatic sarcasm, and metaphor",
          "Phonological segmentation of rapid auditory pseudowords into morphemic roots"
        ],
        "a": 2,
        "e": "<strong>Right-hemisphere linguistic contributions: prosody and pragmatics (Topic 849):</strong> Although the left cerebral hemisphere is specialized for categorical language processing (phonology, syntax, lexical semantics) in the vast majority of individuals, the contralateral right hemisphere plays an essential role in pragmatic and paralinguistic communication. The right hemisphere mediates: (1) <em>Emotional prosody</em>: decoding and producing tone of voice, cadence, and affective inflections (e.g., distinguishing an angry demand from a gentle request); (2) <em>Pragmatics and figurative language</em>: understanding humor, irony, sarcasm, metaphors, and narrative cohesion. Right-hemisphere strokes frequently produce 'aprosodia' (flat, monotone speech and inability to detect vocal emotion).<br><br><em>Distractor Traps:</em><br>&bull; A describes motor speech articulation governed by the left inferior frontal gyrus (Broca's area) and precentral motor strip.<br>&bull; B describes syntactic processing, which is heavily left-lateralized to Broca's area.<br>&bull; D describes phonological decoding, which is localized to the left superior temporal gyrus."
      },
      {
        "q": "A lesion extending into the left angular gyrus (Brodmann area 39), situated at the junction of temporal, parietal, and occipital lobes, typically results in which clinical deficit?",
        "ch": [
          "Impaired reading and writing (alexia and agraphia) due to disrupted visual-phonological cross-modal translation",
          "Complete loss of autonomic cardiovascular homeostasis accompanied by severe peripheral vasodilatory shock",
          "Bilateral loss of thermal and pain sensation across all somatic dermatomes due to spinothalamic transection",
          "Permanent destruction of primary motor neurons producing flaccid hemiplegia across the ipsilateral extremity"
        ],
        "a": 0,
        "e": "<strong>Role of the angular gyrus in cross-modal linguistic translation (Topic 849):</strong> The angular gyrus (Brodmann area 39) is an anatomical convergence zone located in the inferior parietal lobule at the junction of visual (occipital), auditory (temporal), and somatosensory (parietal) association cortices. It is critical for cross-modal integration, specifically translating visually perceived orthographic symbols (written words) into auditory phonological codes that can be processed by Wernicke's area. Consequently, focal lesions of the left angular gyrus produce <em>alexia</em> (inability to read) and <em>agraphia</em> (inability to write), and form the anatomical core of Gerstmann syndrome (agraphia, acalculia, finger agnosia, left-right disorientation).<br><br><em>Distractor Traps:</em><br>&bull; B describes acute medullary/brainstem trauma or spinal shock.<br>&bull; C describes complete spinal cord spinothalamic tract transection.<br>&bull; D describes primary motor cortex or corticospinal tract infarction causing contralateral hemiplegia."
      },
      {
        "q": "In Diffusion Tensor Imaging (DTI), the fractional anisotropy (FA) value of the arcuate fasciculus decreased from 0.54 in controls to 0.21 following deep white matter injury. Biophysically, this reduction indicates:",
        "ch": [
          "An absolute increase in directional water diffusion parallel to intact longitudinal neurofilaments",
          "A total cessation of neuronal glucose consumption within the cell bodies of the striatum",
          "A sudden proliferation of mature oligodendrocytes that markedly thickens the myelin sheath",
          "A loss of structural fiber coherence, axonal degeneration, or disruption of myelin integrity"
        ],
        "a": 3,
        "e": "<strong>Biophysics of DTI fractional anisotropy in white matter pathology (Topic 849):</strong> Diffusion Tensor Imaging (DTI) measures the directionality of water molecule Brownian motion within biological tissues. In healthy, tightly bundled, heavily myelinated white matter tracts (like the arcuate fasciculus), water diffusion is strongly constrained along the longitudinal axis of the axons, resulting in high <em>anisotropy</em> (FA approaching 1.0; 0.54 in controls in Table 1). When axonal injury, demyelination, or ischemic transection occurs, directional constraints are degraded and water diffuses more isotropically in all directions, causing a sharp drop in fractional anisotropy (FA falling to 0.21).<br><br><em>Distractor Traps:</em><br>&bull; A describes high anisotropy, which indicates intact healthy white matter.<br>&bull; B describes FDG-PET metabolic measurement, not magnetic resonance water diffusion.<br>&bull; C describes remyelination, which would increase rather than decrease FA."
      }
    ]
  },
  {
    "id": "exam_ps90_7_p7",
    "sec": "P/S",
    "topic": "Clinical Aphasias: Expressive vs Receptive vs Conduction vs Global Aphasia",
    "sheet": 1,
    "label": "Psychological, Social, and Biological Foundations of Behavior",
    "examId": "ps90_7",
    "passage": "<div class=\"ttl\">Passage 7 (Questions 37&ndash;42)</div>\n<p>Aphasias are acquired impairments in the comprehension, production, or repetition of language caused by focal brain damage, most commonly thromboembolic occlusion of branches of the left middle cerebral artery (MCA). Clinical aphasiology differentiates aphasic syndromes based on three diagnostic axes: spontaneous speech <em>fluency</em>, auditory <em>comprehension</em>, and verbal <em>repetition</em>.</p>\n<p><em>Broca's aphasia</em> (motor/expressive aphasia) results from infarction within the territory of the superior division of the left MCA involving the inferior frontal gyrus. Patients exhibit non-fluent, halting, effortful speech characterized by agrammatism, simplified syntax, and telegraphic output (omission of grammatical morphemes such as prepositions, articles, and auxiliary verbs). Auditory comprehension is relatively preserved for colloquial conversational speech, although comprehension of syntactically complex, non-canonical sentences (e.g., passive-voice constructions like \"The boy was kicked by the horse\") is compromised. Crucially, patients retain intact metacognitive awareness of their communicative impairments, frequently demonstrating emotional distress, insight, and frustration.</p>\n<p>Conversely, <em>Wernicke's aphasia</em> (sensory/receptive aphasia) arises from occlusion of the inferior division of the left MCA supplying the posterior superior temporal gyrus. Patients exhibit fluent, effortless, melodic speech with normal prosody and phrase length; however, utterances are devoid of communicative meaning&mdash;characterized by neologisms (invented non-words), phonemic and semantic paraphasias, and rambling output termed \"word salad.\" Auditory comprehension and repetition are profoundly impaired. Unlike patients with Broca's aphasia, Wernicke's patients exhibit marked <em>anosognosia</em> (lack of awareness of their deficit), remaining oblivious to their communicative failure. <em>Conduction aphasia</em> preserves both spontaneous fluency and auditory comprehension, but presents with a disproportionate deficit in verbatim repetition and prominent phonemic approximations (<em>conduite d'approche</em>). <em>Global aphasia</em>, resulting from proximal MCA trunk occlusion, devastates all language modalities.</p>\n<p>Speech-language pathologists administered the Boston Diagnostic Aphasia Examination (BDAE-3) to four distinct patient groups recovering from acute ischemic stroke (Table 1).</p>\n<table class=\"tbl\">\n  <caption>Table 1 Psychometric language profiles and awareness ratings across post-stroke patient cohorts</caption>\n  <thead>\n    <tr><th>Clinical Cohort</th><th>Mean Phrase Length (Words/Utterance)</th><th>Auditory Comprehension (%ile)</th><th>Verbatim Repetition Accuracy (%)</th><th>Paraphasic Errors (per 100 words)</th><th>Deficit Insight Rating (0&ndash;4 Scale)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Healthy Controls</td><td>11.4 &plusmn; 0.8</td><td>98.5 &plusmn; 1.2</td><td>99.1 &plusmn; 0.6%</td><td>0.2 &plusmn; 0.1</td><td>4.0 &plusmn; 0.0 (complete)</td></tr>\n    <tr><td>Patient Group 1</td><td>3.1 &plusmn; 0.4</td><td>88.4 &plusmn; 3.1</td><td>32.4 &plusmn; 2.8%</td><td>4.2 &plusmn; 0.6</td><td>3.8 &plusmn; 0.2 (high insight)</td></tr>\n    <tr><td>Patient Group 2</td><td>12.2 &plusmn; 0.9</td><td>18.2 &plusmn; 2.2</td><td>19.5 &plusmn; 2.1%</td><td>28.6 &plusmn; 2.4</td><td>0.4 &plusmn; 0.1 (anosognosia)</td></tr>\n    <tr><td>Patient Group 3</td><td>10.8 &plusmn; 0.7</td><td>91.5 &plusmn; 2.8</td><td>21.2 &plusmn; 2.3%</td><td>18.4 &plusmn; 1.8</td><td>3.6 &plusmn; 0.3 (high insight)</td></tr>\n    <tr><td>Patient Group 4</td><td>1.2 &plusmn; 0.3</td><td>12.1 &plusmn; 1.8</td><td>6.8 &plusmn; 1.1%</td><td>3.1 &plusmn; 0.5</td><td>0.8 &plusmn; 0.2 (minimal)</td></tr>\n  </tbody>\n</table>",
    "qs": [
      {
        "q": "Based on the psychometric profiles in Table 1, which clinical classifications correctly identify Patient Group 1 and Patient Group 2?",
        "ch": [
          "Group 1 represents Wernicke's aphasia, while Group 2 represents conduction aphasia",
          "Group 1 represents Broca's aphasia, whereas Group 2 represents Wernicke's aphasia",
          "Group 1 represents global aphasia, while Group 2 represents transcortical aphasia",
          "Group 1 represents conduction aphasia, while Group 2 represents expressive aphasia"
        ],
        "a": 1,
        "e": "<strong>Differential diagnosis of Broca's versus Wernicke's aphasia (Topic 850):</strong> In Table 1: (1) <em>Patient Group 1</em> displays severely reduced phrase length (3.1 words/utterance, non-fluent), relatively preserved auditory comprehension (88.4 percentile), poor repetition (32.4%), and high insight/awareness (3.8 rating), which is the classic diagnostic signature of <em>Broca's (expressive) aphasia</em>; (2) <em>Patient Group 2</em> displays fluent phrase length (12.2 words/utterance), severely impaired auditory comprehension (18.2 percentile), impaired repetition (19.5%), high paraphasic error rate (28.6 per 100 words), and profound anosognosia (0.4 rating), which is the definitive profile of <em>Wernicke's (receptive) aphasia</em>.<br><br><em>Distractor Traps:</em><br>&bull; A completely reverses the two diagnoses.<br>&bull; C misclassifies Group 1 as global aphasia (which corresponds to Group 4 with severe impairment across all axes).<br>&bull; D misidentifies Group 1 as conduction aphasia (conduction aphasia is fluent with intact comprehension, matching Group 3)."
      },
      {
        "q": "Patient Group 3 demonstrated fluent phrase length (10.8) and preserved auditory comprehension (91.5%), yet suffered severely impaired repetition (21.2%) with frequent phonemic paraphasias. This syndrome (conduction aphasia) typically results from damage to:",
        "ch": [
          "The primary visual cortex within the calcarine sulcus of the occipital lobe",
          "The ventral tegmental area and the ascending medial forebrain bundle in the midbrain",
          "The arcuate fasciculus connecting temporal receptive areas to frontal motor speech areas",
          "The anterior descending corticospinal tract within the anterior funiculus of the spinal cord"
        ],
        "a": 2,
        "e": "<strong>Neuroanatomy and clinical profile of conduction aphasia (Topic 850):</strong> Conduction aphasia is characterized by fluent spontaneous speech, intact auditory comprehension, and a disproportionate, severe impairment in verbatim repetition, accompanied by frequent phonemic paraphasias and unsuccessful attempts to self-correct (<em>conduite d'approche</em>). This syndrome is classically caused by a lesion in the deep perisylvian white matter that interrupts the <em>arcuate fasciculus</em> (or the supramarginal gyrus), disconnecting Wernicke's area from Broca's area without destroying either cortical hub. Patients comprehend spoken words normally because Wernicke's area is intact, and speak fluently because Broca's area is intact, but cannot relay auditory representations forward for repetition.<br><br><em>Distractor Traps:</em><br>&bull; A describes calcarine cortex lesions, which cause homonymous hemianopia or cortical blindness.<br>&bull; B describes the mesolimbic dopamine pathway, which mediates reward and reinforcement.<br>&bull; D describes corticospinal motor pathways, which mediate somatic motor movement rather than language repetition."
      },
      {
        "q": "In Table 1, Patient Group 2 exhibited severe anosognosia (awareness rating 0.4), while Patient Group 1 exhibited high insight (3.8). What cognitive explanation accounts for this disparity?",
        "ch": [
          "Expressive aphasia preserves self-monitoring feedback networks, allowing patients to recognize speech errors",
          "Receptive deficits prevent patients from monitoring and detecting errors in their own auditory speech output",
          "Receptive aphasia induces psychogenic denial mechanisms rather than neuroanatomical perisylvian damage",
          "Expressive aphasia selectively damages auditory hair cells, rendering individuals oblivious to sound"
        ],
        "a": 1,
        "e": "<strong>Anosognosia in receptive versus expressive aphasia (Topic 850):</strong> Anosognosia (lack of awareness or insight into one's own neurological deficit) is a prominent and defining clinical characteristic of Wernicke's (receptive) aphasia. Self-monitoring of speech requires auditory feedback to be decoded and checked against communicative intentions in Wernicke's area and adjacent temporoparietal networks. Because Wernicke's area is damaged, patients are unable to decode their own auditory output and thus remain oblivious to their paraphasias, neologisms, and nonsensical 'word salad.' In contrast, Broca's patients have preserved receptive auditory comprehension and self-monitoring networks; they hear their own halting, agrammatic speech and recognize its errors, which frequently causes profound frustration and reactive depression.<br><br><em>Distractor Traps:</em><br>&bull; A is a true statement about Broca's aphasia, but the question specifically asks why receptive aphasia patients exhibit anosognosia (the lack of awareness).<br>&bull; C describes psychogenic denial; anosognosia in Wernicke's aphasia is a direct organic neurocognitive consequence of perisylvian temporoparietal damage.<br>&bull; D is factually incorrect; Broca's aphasia does not damage peripheral cochlear hair cells."
      },
      {
        "q": "Patient Group 4 exhibited severe non-fluency (1.2 words/utterance), near-total loss of comprehension (12.1%), and absent repetition (6.8%). This global aphasia presentation is typically precipitated by:",
        "ch": [
          "A small lacunar infarction confined strictly to the posterior limb of the internal capsule",
          "Selective degeneration of cerebellar Purkinje cells caused by chronic dietary thiamine deficiency",
          "Massive occlusion of the left middle cerebral artery trunk devastating anterior and posterior speech zones",
          "Occlusion of the posterior inferior cerebellar artery producing Wallenberg lateral medullary syndrome"
        ],
        "a": 2,
        "e": "<strong>Pathophysiology and vascular etiology of global aphasia (Topic 850):</strong> Global aphasia is the most severe form of aphasia, characterized by profound deficits across all three primary language axes: non-fluent speech (often restricted to stereotyped utterances or mutism), severely impaired auditory comprehension, and absent repetition. This devastating clinical presentation is classically caused by a massive thromboembolic occlusion of the proximal stem (main trunk) of the left middle cerebral artery (MCA). This compromises blood supply to both the superior division (supplying Broca's area in the frontal lobe) and the inferior division (supplying Wernicke's area and the arcuate fasciculus in the temporal and parietal lobes), infarcating the entire perisylvian language apparatus.<br><br><em>Distractor Traps:</em><br>&bull; A describes a pure motor lacunar stroke, which produces contralateral hemiparesis without cortical aphasia.<br>&bull; B describes Wernicke-Korsakoff encephalopathy and cerebellar vermis degeneration.<br>&bull; D describes lateral medullary syndrome (PICA stroke), causing vertigo, dysphagia, ataxia, and Horner syndrome, without aphasia."
      },
      {
        "q": "A patient presents with non-fluent, halting speech and impaired comprehension following systemic hypoperfusion, but demonstrates an uncanny ability to repeat complex sentences verbatim without error. This transcortical aphasia occurs because:",
        "ch": [
          "Watershed zone infarcts isolate the perisylvian language arc while leaving the Broca-Wernicke arcuate pathway intact",
          "The corpus callosum has been surgically severed, preventing communication between the cerebral hemispheres",
          "Complete bilateral destruction of the primary motor cortex has selectively paralyzed the tongue and larynx",
          "The patient is consciously feigning speech deficits while relying on intact subcortical basal ganglia reflexes"
        ],
        "a": 0,
        "e": "<strong>Transcortical aphasias and watershed infarctions (Topic 850):</strong> The definitive hallmark of transcortical aphasias (transcortical motor, transcortical sensory, and mixed transcortical) is the <em>preservation of verbatim repetition</em> despite severe deficits in spontaneous fluency, comprehension, or both. These syndromes occur following watershed (border-zone) infarctions&mdash;areas at the vulnerable junctions between the terminal territories of the anterior, middle, and posterior cerebral arteries, often during profound systemic hypotension or cardiac arrest. Watershed infarcts isolate the central perisylvian language zone from surrounding cortex, but leave the core perisylvian language arc (Broca's area, Wernicke's area, and the connecting arcuate fasciculus) structurally intact, allowing repetition to occur automatically.<br><br><em>Distractor Traps:</em><br>&bull; B describes split-brain syndrome resulting from corpus callosotomy, which impairs interhemispheric transfer without producing transcortical aphasia.<br>&bull; C describes severe bilateral bulbar/motor paralysis (pseudobulbar palsy), which prevents speech repetition.<br>&bull; D describes malingering or factitious disorder, whereas transcortical aphasia is an established neurological condition."
      },
      {
        "q": "Although patients with Broca's aphasia typically perform well on simple comprehension tests, they fail when presented with semantically reversible passive-voice sentences (e.g., 'The cow was kicked by the horse'). This deficit reveals that Broca's area is necessary for:",
        "ch": [
          "Storing the foundational auditory phonemic representations of individual consonants and vowels",
          "Regulating the autonomic homeostatic reflexes that coordinate diaphragm and respiratory airflow",
          "Modulating emotional affective vocal prosody and interpreting humorous conversational irony",
          "Decoding complex hierarchical grammatical syntax and processing non-canonical thematic roles"
        ],
        "a": 3,
        "e": "<strong>Syntactic comprehension deficits in Broca's aphasia / agrammatism (Topic 850):</strong> While Broca's aphasia was historically considered a purely expressive/motor disorder, modern cognitive aphasiology recognizes that Broca's area (Brodmann areas 44/45) is also critically involved in syntactic computation during comprehension. In active sentences with canonical English word order (Subject-Verb-Object: 'The horse kicked the cow'), patients can deduce meaning purely from semantic word order. However, in semantically reversible passive-voice sentences ('The cow was kicked by the horse'), where either noun could plausibly perform the action, semantic heuristic guessing fails; patients must parse the non-canonical grammatical syntax ('was [verb]-ed by') to identify who kicked whom. Broca's patients fail at these tasks, proving Broca's area is necessary for processing complex hierarchical syntax.<br><br><em>Distractor Traps:</em><br>&bull; A describes Wernicke's area and primary auditory cortex (Heschl's gyrus).<br>&bull; B describes brainstem autonomic respiratory centers in the medulla and pons.<br>&bull; C describes right hemisphere paralinguistic and prosodic processing."
      }
    ]
  },
  {
    "id": "exam_ps90_7_disc",
    "sec": "P/S",
    "topic": "Psychological, Social, and Biological Foundations of Behavior \u2014 Discrete Questions",
    "sheet": 1,
    "label": "Psychological, Social, and Biological Foundations of Behavior",
    "examId": "ps90_7",
    "qs": [
      {
        "d": true,
        "q": "Classic serotonergic hallucinogens, such as lysergic acid diethylamide (LSD) and psilocybin, induce profound perceptual distortions, synesthesia, and altered consciousness primarily by acting as:",
        "ch": [
          "Agonists at cortical pyramidal 5-HT2A receptors that disrupt thalamocortical sensory gating mechanisms",
          "Competitive antagonists at dopamine D2 receptors within the tuberoinfundibular endocrine projection tract",
          "Positive allosteric modulators at GABA-A ligand-gated chloride ion channels throughout the brainstem",
          "Irreversible inhibitors of the enzyme acetylcholinesterase within the parasympathetic nervous system"
        ],
        "a": 0,
        "e": "<strong>Neuropharmacology of classic hallucinogens (Topic 846):</strong> Classic hallucinogens (LSD, psilocybin, mescaline) are structural analogs of serotonin that act primarily as partial or full agonists at serotonin 5-HT<sub>2A</sub> G-protein coupled receptors. These receptors are densely expressed on the apical dendrites of layer V pyramidal glutamatergic neurons in the prefrontal cortex and the reticular nucleus of the thalamus. Activation of 5-HT<sub>2A</sub> receptors disrupts normal thalamocortical sensory gating&mdash;the filter that normally screens out irrelevant sensory stimuli. This breakdown in sensory filtering floods the cerebral cortex with unconstrained sensory signals, inducing perceptual distortions, visual hallucinations, cross-modal synesthesia, and ego dissolution.<br><br><em>Distractor Traps:</em><br>&bull; B describes first-generation antipsychotics (haloperidol), which cause hyperprolactinemia via tuberoinfundibular D<sub>2</sub> blockade.<br>&bull; C describes sedative-hypnotic depressants (benzodiazepines and barbiturates).<br>&bull; D describes organophosphate toxins and anticholinesterases (donepezil, pyridostigmine)."
      },
      {
        "d": true,
        "q": "When a dinner guest says 'Can you pass the salt?', a listener interprets this utterance as a polite request rather than a literal inquiry into their physical capability. This interpretive skill relies primarily on:",
        "ch": [
          "Phonology, which governs the acoustic structure and vocal articulation of individual phonemes",
          "Pragmatics, which governs how social context and communicative intent shape the meaning of speech",
          "Syntax, which establishes the formal rules for ordering nouns and auxiliary verbs into sentences",
          "Morphology, which dictates how minimal grammatical morphemes are combined into complex words"
        ],
        "a": 1,
        "e": "<strong>Components of language: Pragmatics versus Semantics and Syntax (Topic 848):</strong> Human language comprises five foundational components: (1) <em>Phonology</em>: the rules governing the structure and sequence of speech sounds (phonemes); (2) <em>Morphology</em>: the rules governing the composition of words from minimal units of meaning (morphemes); (3) <em>Syntax</em>: the grammatical rules governing sentence structure and word order; (4) <em>Semantics</em>: the literal meaning of words and sentences; and (5) <em>Pragmatics</em>: the rules governing the practical, social use of language in context, including understanding non-literal communicative intent, indirect requests, politeness norms, sarcasm, and conversational implicature. Understanding that 'Can you pass the salt?' is an indirect request rather than a literal yes/no question of motor ability is an application of pragmatics.<br><br><em>Distractor Traps:</em><br>&bull; A describes phonology, which deals with speech sounds.<br>&bull; C describes syntax, which deals with grammatical word order.<br>&bull; D describes morphology, which deals with word-formation units (roots, prefixes, suffixes)."
      },
      {
        "d": true,
        "q": "A researcher tests native speakers of two languages with differing color vocabularies. Speakers of Language X (distinguishing blue from green) discriminate shades faster than speakers of Language Y (using one term for both). This finding supports:",
        "ch": [
          "Universal Grammar, which claims language categories are innate and genetically hardwired at birth",
          "Linguistic determinism, which claims thought is strictly constrained and bounded by vocabulary",
          "Linguistic relativity, which posits that language categories influence and bias cognitive perception",
          "Dual-coding theory, which asserts that verbal and non-verbal information are stored separately"
        ],
        "a": 2,
        "e": "<strong>The Sapir-Whorf hypothesis: Linguistic relativity versus determinism (Topic 851):</strong> The Sapir-Whorf hypothesis addresses the relationship between language and thought: (1) <em>Weak version (Linguistic Relativity)</em>: proposes that the structure and vocabulary of a language influence, shape, and bias cognitive processes, memory, and perceptual discrimination speeds. The finding that possessing discrete lexical color categories facilitates perceptual discrimination times between color shades is a classic empirical validation of linguistic relativity; (2) <em>Strong version (Linguistic Determinism)</em>: claims that language strictly determines and completely constrains thought, asserting that humans are utterly incapable of thinking about or perceiving concepts for which their language lacks words (a claim largely refuted by cognitive science).<br><br><em>Distractor Traps:</em><br>&bull; A describes Chomsky's nativist theory of Universal Grammar, which emphasizes biological universality across all human languages.<br>&bull; B describes linguistic determinism, which would predict that speakers of Language Y could not perceive the difference between green and blue at all.<br>&bull; D describes Paivio's dual-coding theory of memory (verbal vs visual representations)."
      },
      {
        "d": true,
        "q": "A 30-month-old child who previously said 'held' and 'went' begins producing utterances such as 'I holded the kitty' and 'Daddy goed to work.' In developmental psycholinguistics, this phenomenon is termed:",
        "ch": [
          "Semantic underextension, where a categorical noun is applied to a single specific object",
          "Canonical infant babbling, where repetitive consonant-vowel syllable clusters are vocalized",
          "Telegraphic speech, where non-essential prepositions and grammatical morphemes are omitted",
          "Overregularization, where standard grammatical rules are inappropriately applied to irregular verbs"
        ],
        "a": 3,
        "e": "<strong>Overregularization in child language development (Topic 852):</strong> Language acquisition follows a predictable developmental chronology: (1) Cooing (2&ndash;4 months); (2) Canonical babbling (6&ndash;9 months); (3) One-word / holophrastic stage (10&ndash;14 months); (4) Two-word / telegraphic speech (18&ndash;24 months); and (5) Grammatical explosion and <em>overregularization</em> (24&ndash;36 months). Overregularization occurs when a child internalizes a regular grammatical rule (such as adding '-ed' to form past-tense verbs or '-s' to form plural nouns) and overapplies it to irregular words that they previously memorized as exceptions ('goed', 'holded', 'foots', 'mouses'). This demonstrates that language acquisition is rule-governed rather than pure behavioral imitation.<br><br><em>Distractor Traps:</em><br>&bull; A describes underextension, where a child uses a general categorical word (e.g., 'dog') to refer strictly to their own pet.<br>&bull; B describes infant babbling (e.g., 'ba-ba-ba'), which occurs between 6 and 9 months.<br>&bull; C describes telegraphic speech (e.g., 'want milk', 'car go'), which consists of two-word content phrases lacking syntax."
      },
      {
        "d": true,
        "q": "Psycholinguistic research demonstrates that bilingual individuals consistently outperform monolinguals on tasks requiring executive inhibitory control (e.g., the Stroop task). What cognitive mechanism underlies this bilingual advantage?",
        "ch": [
          "Constant suppression of the non-target language during speech recruits and strengthens executive frontoparietal networks",
          "Bilingualism leads to permanent atrophy of the temporal lobes, which frees up greater metabolic capacity for frontal processing",
          "Bilingual speakers possess two anatomically distinct and non-overlapping Broca's areas within the left frontal lobe",
          "Simultaneous acquisition of two languages permanently eliminates all susceptibility to proactive interference"
        ],
        "a": 0,
        "e": "<strong>Cognitive mechanisms of the bilingual executive advantage (Topic 853):</strong> In fluent bilinguals, both linguistic systems remain continuously active and accessible in the brain, even when communicating in only one language. Whenever a bilingual speaks, reads, or listens, lexical candidates from the non-target language compete for selection. To avoid catastrophic cross-language interference, the individual must constantly recruit domain-general executive control networks&mdash;specifically the dorsolateral prefrontal cortex (dlPFC) and anterior cingulate cortex (ACC)&mdash;to actively inhibit and suppress the competing language. Decades of this continuous, implicit inhibitory exercise physically strengthens frontoparietal executive circuits, conferring a generalized cognitive advantage in non-linguistic tasks requiring conflict resolution, task-switching, and selective attention (e.g., the Stroop and Flanker tasks) and enhancing cognitive reserve against neurodegenerative decline.<br><br><em>Distractor Traps:</em><br>&bull; B describes neurodegenerative atrophy, which does not occur as a consequence of bilingualism.<br>&bull; C describes anatomically duplicate Broca's areas; both languages recruit shared, overlapping perisylvian neural architecture.<br>&bull; D is factually incorrect; bilingual individuals remain susceptible to both proactive and retroactive memory interference."
      },
      {
        "d": true,
        "q": "A linguist observes that children across diverse cultures master complex syntactic grammar rapidly and without formal instruction, producing novel sentences they have never heard. This observation most strongly supports which theoretical model?",
        "ch": [
          "Skinner's behaviorist theory, which attributes syntax acquisition to operant conditioning and differential reinforcement",
          "Chomsky's nativist theory, which posits an innate, biologically predetermined Language Acquisition Device (LAD)",
          "Pavlov's classical conditioning framework, where grammatical structures serve as conditioned auditory stimuli",
          "Social cognitive learning theory, where language emerges solely from passive observation of parental role models"
        ],
        "a": 1,
        "e": "<strong>Theories of language development: Chomsky's nativism versus Skinner's behaviorism (Topic 854):</strong> Noam Chomsky formulated the <em>nativist (biological) theory</em> of language acquisition, arguing against B.F. Skinner's behaviorist model. Chomsky pointed to the 'poverty of the stimulus': children are exposed to limited, fragmented, and error-prone speech, yet they effortlessly deduce complex, abstract syntactic rules without formal tutoring, during a critical/sensitive developmental window. Chomsky posited that humans are born with an innate biological capacity for language&mdash;termed the <em>Language Acquisition Device (LAD)</em>&mdash;which contains an inherent blueprint of universal grammar shared across all human languages.<br><br><em>Distractor Traps:</em><br>&bull; A describes B.F. Skinner's behaviorist model, which fails to explain the generation of novel, unreinforced grammatical sentences.<br>&bull; C describes classical conditioning (stimulus-stimulus associations), which does not account for combinatorial syntax.<br>&bull; D describes Bandura's observational learning, which does not account for innate universal grammar or critical periods."
      },
      {
        "d": true,
        "q": "A four-year-old child struggling to assemble a jigsaw puzzle speaks softly to herself ('The blue piece goes here next to the edge') before successfully placing it. According to Lev Vygotsky, this self-directed vocalization represents:",
        "ch": [
          "Egocentric speech reflecting cognitive immaturity that must be eradicated before formal abstract thought can emerge",
          "Semantic paraphasia resulting from delayed myelination within the arcuate fasciculus connecting temporal regions",
          "Private speech functioning as a cognitive self-regulation tool that will eventually internalize into silent verbal thought",
          "Operant verbal behavior maintained solely by immediate external schedules of continuous physical reinforcement"
        ],
        "a": 2,
        "e": "<strong>Vygotsky's sociocultural theory: Private speech and the ZPD (Topic 855):</strong> Lev Vygotsky's sociocultural theory emphasized that cognitive development is deeply mediated by social interactions and cultural tools, particularly language. Vygotsky viewed <em>private speech</em> (self-directed audible speech used by young children during challenging tasks) not as a flaw, but as a critical cognitive tool for self-regulation, planning, problem-solving, and guiding goal-directed behavior. Around ages 6 to 7, overt private speech gradually internalizes, transforming into covert <em>inner speech</em> (silent verbal thought). Vygotsky also introduced the <em>Zone of Proximal Development (ZPD)</em>: the difference between what a child can achieve independently versus what they can achieve with guidance (scaffolding) from a More Knowledgeable Other (MKO).<br><br><em>Distractor Traps:</em><br>&bull; A describes Jean Piaget's view, who regarded self-talk as 'egocentric speech' reflecting cognitive immaturity that fades as the child becomes socialized.<br>&bull; B describes aphasic pathology; self-directed speech in young children is a normal developmental milestone, not a white matter defect.<br>&bull; D describes Skinner's behaviorism, which fails to appreciate the metacognitive self-regulatory function of private speech."
      },
      {
        "d": true,
        "q": "Paul Ekman's cross-cultural research in pre-industrial, non-literate societies (such as the Fore tribe of Papua New Guinea) provided foundational empirical evidence that:",
        "ch": [
          "Facial expressions of emotion are entirely arbitrary cultural conventions acquired exclusively through social learning",
          "Emotional feelings are caused solely by cognitive appraisals of situational context without any physiological arousal",
          "Autonomic nervous system activation patterns are identical across every discrete emotional experience in humans",
          "A discrete set of basic emotional facial expressions is biologically universal and recognized across all human cultures"
        ],
        "a": 3,
        "e": "<strong>Paul Ekman's universal basic emotions (Topic 856):</strong> Paul Ekman conducted landmark cross-cultural studies demonstrating that facial expressions corresponding to primary basic emotions are evolutionarily conserved and biologically universal, rather than culturally learned. By testing isolated, non-literate individuals in Papua New Guinea who had no exposure to Western media or culture, Ekman demonstrated that people worldwide accurately identify and display the same facial muscle configurations for six primary emotions: <em>Happiness, Sadness, Fear, Anger, Surprise, and Disgust</em> (with Contempt often included as a seventh). While cultural 'display rules' dictate when and where it is socially appropriate to express these emotions, the foundational facial motor patterns are innate and universal.<br><br><em>Distractor Traps:</em><br>&bull; A reflects extreme cultural relativism (Margaret Mead's hypothesis), which Ekman's cross-cultural data directly refuted.<br>&bull; B describes cognitive mediational theories of emotion (Lazarus), not Ekman's facial expression research.<br>&bull; C contradicts autonomic psychophysiology; Ekman demonstrated distinct autonomic profiles (e.g., heart rate and skin temperature) between anger, fear, and sadness."
      },
      {
        "d": true,
        "q": "A hiker walking through a forest abruptly encounters a roaring grizzly bear. The hiker's heart races and breathing quickens, and she subsequently thinks, 'My heart is pounding, so I must be terrified.' This sequence illustrates which theory of emotion?",
        "ch": [
          "The James-Lange theory, which posits that conscious emotional experience is produced by physiological arousal feedback",
          "The Cannon-Bard theory, which posits that physiological arousal and conscious emotional feelings occur simultaneously",
          "The Schachter-Singer two-factor theory, which requires cognitive appraisal of environmental cues to label vague arousal",
          "The Lazarus cognitive-mediational theory, which posits that cognitive appraisal must precede physiological responses"
        ],
        "a": 0,
        "e": "<strong>Classical theories of emotion: James-Lange versus alternatives (Topic 857):</strong> The MCAT heavily tests the distinction between classical theories of emotion: (1) <em>James-Lange Theory</em>: Event &rarr; Physiological arousal &rarr; Conscious emotional feeling ('I am trembling, therefore I am afraid'). Emotion is the brain's direct perception of visceral and somatic feedback; (2) <em>Cannon-Bard Theory</em>: Event &rarr; Simultaneous and independent physiological arousal and conscious emotional feeling via parallel thalamocortical pathways ('I see a bear, my heart races and I feel afraid at the exact same instant'); (3) <em>Schachter-Singer Two-Factor Theory</em>: Event &rarr; Physiological arousal &rarr; Cognitive appraisal / labeling based on environmental context &rarr; Conscious emotion ('My heart is racing, I see a dangerous bear, so I label this arousal as fear'); (4) <em>Lazarus Cognitive-Mediational Theory</em>: Event &rarr; Cognitive appraisal &rarr; Simultaneous emotion and physiological arousal.<br><br><em>Distractor Traps:</em><br>&bull; B describes Cannon-Bard, which posits simultaneous independent emergence of arousal and feeling.<br>&bull; C describes Schachter-Singer, which requires contextual cognitive appraisal to interpret ambiguous physiological arousal.<br>&bull; D describes Lazarus, where cognitive appraisal must precede physiological changes."
      },
      {
        "d": true,
        "q": "In Richard Lazarus's cognitive-mediational theory of emotion, what sequential relationship governs the emergence of subjective emotional feelings and physiological arousal upon encountering a stimulus?",
        "ch": [
          "Physiological arousal occurs first, and the brain subsequently monitors visceral sensations to experience emotion",
          "Cognitive appraisal of the stimulus occurs first, which subsequently mediates both emotional and physiological responses",
          "Physiological arousal and conscious emotional experience are triggered simultaneously via parallel thalamic relays",
          "Facial muscle contractions reflexively trigger emotional feelings before any higher cortical processing can occur"
        ],
        "a": 1,
        "e": "<strong>Lazarus's cognitive-mediational theory of emotion (Topic 858):</strong> Richard Lazarus formulated the cognitive-mediational theory of emotion, asserting that cognitive appraisal is the indispensable prerequisite that mediates and dictates the emotional experience. According to Lazarus: Stimulus &rarr; <em>Cognitive Appraisal</em> &rarr; Emotional experience and physiological response. The appraisal process involves two stages: (1) <em>Primary appraisal</em>: evaluating whether the stimulus is irrelevant, benign-positive, or stressful (harm/loss, threat, or challenge); and (2) <em>Secondary appraisal</em>: evaluating one's coping resources and ability to manage the stressor. If an event is appraised as a threat without adequate coping resources, negative emotion (fear/anxiety) and sympathetic arousal emerge simultaneously as downstream consequences of that initial appraisal.<br><br><em>Distractor Traps:</em><br>&bull; A describes the James-Lange theory of emotion.<br>&bull; C describes the Cannon-Bard theory of emotion.<br>&bull; D describes the facial feedback hypothesis (Tomkins/Izard)."
      }
    ]
  }
];

if (typeof window !== 'undefined') {
  window.EXAM_PS90_7 = EXAM_PS90_7;
}
if (typeof globalThis !== 'undefined') {
  globalThis.EXAM_PS90_7 = EXAM_PS90_7;
}
