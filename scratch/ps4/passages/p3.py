import sys
import os

passage_data = {
  "id": "exam_ps90_4_p3",
  "sec": "P/S",
  "topic": "Visual Agnosias & The Ventral Stream: Prosopagnosia",
  "sheet": None,
  "label": "Psychological, Social, and Biological Foundations of Behavior",
  "examId": "ps90_4",
  "passage": "<div class=\"ttl\">Passage 3 (Questions 13&ndash;18)</div>\n<p>Visual sensory information exiting the primary visual cortex (striate cortex, V1) bifurcates into two distinct cortical processing pathways: the dorsal \"where/how\" pathway projecting to the posterior parietal cortex, and the ventral \"what\" pathway traversing V2 and V4 to terminate in the inferior temporal (IT) cortex. The ventral stream is specialized for high-level object representation, shape constancy, and category-selective visual recognition. Focal lesions along this occipitotemporal axis precipitate distinct visual agnosias&mdash;severe impairments in visual recognition that cannot be attributed to elementary sensory deficits, language aphasias, or generalized intellectual decline.</p>\n<p>Neuropsychologists classically distinguish between apperceptive and associative visual agnosias. Apperceptive agnosia arises from disruptions in early structural feature integration; affected individuals cannot perceive coherent object forms, copy simple drawings, or match identical geometric shapes, despite intact visual acuity and field boundaries. Conversely, in associative agnosia, perceptual structural binding is preserved&mdash;patients can copy complex drawings accurately and match identical shapes&mdash;yet the intact visual representation is disconnected from semantic memory, rendering them unable to name or identify objects by sight. A profoundly selective ventral stream deficit is prosopagnosia, characterized by an inability to recognize familiar human faces, typically resulting from lesions to the fusiform gyrus (Brodmann area 37), particularly the fusiform face area (FFA).</p>\n<p>To investigate the functional modularity of ventral stream substructures, cognitive neurologists tested three clinical cohorts with focal vascular lesions alongside healthy controls on a computerized visual battery and functional magnetic resonance imaging (fMRI) task. Standardized behavioral accuracies and FFA BOLD signal contrasts (Faces > Common Objects) are detailed in Table 1.</p>\n<table class=\"tbl\">\n  <caption>Table 1 Behavioral accuracy across visual recognition tasks, drawing ability, and fusiform face area fMRI activation</caption>\n  <thead>\n    <tr><th>Clinical Participant Cohort</th><th>Primary Anatomical Lesion Site</th><th>Upright Face Accuracy (%)</th><th>Inverted Face Accuracy (%)</th><th>Common Object Accuracy (%)</th><th>Object Copying Accuracy (%)</th><th>FFA BOLD Activation ($\\Delta \\%$)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Acquired Prosopagnosia ($n=12$)</td><td>Right / Bilateral Fusiform Gyrus</td><td>41.2%</td><td>40.8%</td><td>94.5%</td><td>96.2%</td><td>+0.12%</td></tr>\n    <tr><td>Apperceptive Agnosia ($n=8$)</td><td>Bilateral Lateral Occipital Complex</td><td>38.5%</td><td>36.9%</td><td>42.1%</td><td>32.4%</td><td>+0.28%</td></tr>\n    <tr><td>Associative Agnosia ($n=10$)</td><td>Anterior Inferior Temporal Cortex</td><td>52.4%</td><td>48.0%</td><td>46.2%</td><td>95.0%</td><td>+0.35%</td></tr>\n    <tr><td>Healthy Matched Controls ($n=20$)</td><td>Intact (No Neurological Lesion)</td><td>93.8%</td><td>64.2%</td><td>96.8%</td><td>97.4%</td><td>+2.45%</td></tr>\n  </tbody>\n</table>",
  "qs": [
    {
      "q": "Based on the neuropsychological findings in Table 1, which diagnostic dissociation best distinguishes apperceptive visual agnosia from associative visual agnosia?",
      "ch": [
        "Apperceptive agnosics recognize upright faces normally, whereas associative agnosics display profound face blindness.",
        "Associative agnosics exhibit severe primary visual field scotomas, whereas apperceptive agnosics retain full visual fields.",
        "Associative agnosics successfully copy drawings of objects, whereas apperceptive agnosics cannot assemble structural forms.",
        "Apperceptive agnosics easily name objects upon visual presentation, whereas associative agnosics rely entirely on tactile cues."
      ],
      "a": 2,
      "e": "<strong>Dissociation between apperceptive and associative agnosia:</strong> Apperceptive agnosia results from damage to earlier visual integration areas (such as the lateral occipital complex, LOC). Patients cannot bind individual sensory features (lines, edges, contours) into a coherent perceptual gestalt; consequently, their object copying score is severely impaired (32.4% in Table 1). In contrast, associative agnosia stems from damage to anterior inferior temporal regions or disconnections between perception and semantic memory. Associative agnosics have intact early perceptual integration and can therefore copy complex drawings with meticulous accuracy (95.0% in Table 1), but they cannot attach semantic meaning to what they have drawn, failing to identify or name the object visually.<br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Neither agnosia cohort recognizes upright faces normally (both score ~38&ndash;52%), and prosopagnosia is the specific condition of face blindness.<br>&bull; B (Medical Diagnostic Error): Visual agnosias are by definition higher-order cortical recognition deficits that occur in the absence of primary visual field cuts (scotomas).<br>&bull; D (Directional Inversion): Apperceptive agnosics cannot name visually presented objects because they cannot even perceive the structural form, let alone name it."
    },
    {
      "q": "In Table 1, healthy controls display a marked accuracy reduction when faces are inverted (93.8% to 64.2%), whereas prosopagnosic patients show no significant difference (41.2% to 40.8%). What accounts for this discrepancy?",
      "ch": [
        "Inversion impairs early retinal ganglion receptive fields in healthy controls but selectively spares damaged cortical tissue.",
        "Prosopagnosic patients possess enhanced dorsal stream motion processing that actively compensates for static image inversion.",
        "Healthy controls utilize piecemeal analytical processing for upright faces, whereas prosopagnosic patients utilize configural processing.",
        "Healthy controls process upright faces configurally, whereas prosopagnosic patients rely on impaired piecemeal feature processing."
      ],
      "a": 3,
      "e": "<strong>The Face Inversion Effect and configural face processing:</strong> In neurotypical individuals, upright human faces are processed holistically or configurally—meaning the brain automatically integrates the spatial relations among facial features (interocular distance, nose-to-mouth proportions). Inversion disrupts this specialized configural processing, forcing healthy observers to switch to slower, less accurate piecemeal analysis, causing a steep drop in accuracy (the Face Inversion Effect, dropping from 93.8% to 64.2%). In contrast, prosopagnosic individuals have damaged FFA circuitry and cannot process faces holistically even when upright; they already rely exclusively on slow, error-prone piecemeal feature analysis. Consequently, turning the face upside down causes no additional performance drop (41.2% vs. 40.8%).<br><br><em>Distractor Traps:</em><br>&bull; A (Incorrect Anatomical Locus): The face inversion effect is a high-level cortical perceptual phenomenon, not a peripheral retinal ganglion cell deficit.<br>&bull; B (Irrelevant Mechanism): The dorsal stream processes spatial motion and visually guided action; it does not compensate for static face inversion.<br>&bull; C (Directional Inversion): Healthy controls process upright faces holistically/configurally (not piecemeal), whereas prosopagnosics rely on piecemeal processing."
    },
    {
      "q": "If a patient with severe acquired prosopagnosia also preserves full function of their dorsal visual processing stream, which behavior will remain completely intact?",
      "ch": [
        "Accurately reaching out to grasp a moving coffee cup whose visual identity they cannot consciously recognize.",
        "Identifying a close friend from a photograph by rapidly synthesizing their holistic facial configuration.",
        "Naming a familiar household tool immediately upon viewing its static line drawing on a computer display.",
        "Copying a complex geometric landscape drawing while simultaneously explaining its cultural significance."
      ],
      "a": 0,
      "e": "<strong>Dorsal versus ventral visual stream dissociation:</strong> According to the Goodale and Milner dual-stream model, the ventral stream (V1 to inferior temporal cortex) mediates conscious visual perception and object identification (\"vision-for-perception\"), while the dorsal stream (V1 to posterior parietal cortex) mediates online visuomotor control and spatial coordination (\"vision-for-action\"). A patient with isolated ventral stream damage (such as prosopagnosia or visual form agnosia) cannot identify what an object is. However, because their dorsal occipitoparietal stream is intact, they can seamlessly calibrate their hand grip aperture, orientation, and trajectory to reach out and grasp a moving or stationary object.<br><br><em>Distractor Traps:</em><br>&bull; B (Directly Contradicted): Recognizing a friend from a photograph requires an intact ventral stream and fusiform face area, which are damaged in prosopagnosia.<br>&bull; C (Ventral Stream Function): Visual identification of tools from static drawings is a ventral stream semantic recognition task.<br>&bull; D (Confounded Ventral/Semantic Task): Explaining the cultural significance of visual art requires ventral semantic integration."
    },
    {
      "q": "What do the fMRI BOLD activation findings in Table 1 demonstrate regarding the functional specialization of the fusiform face area (FFA)?",
      "ch": [
        "The FFA undergoes uniform bilateral atrophy whenever an individual develops any clinical category of visual agnosia.",
        "The FFA exhibits category-selective neural activation for faces over objects that is abolished in prosopagnosic patients.",
        "The FFA operates strictly as an early general-purpose edge detector that projects equally to ventral and dorsal streams.",
        "The FFA exhibits identical BOLD signal increases regardless of whether visual stimuli are upright faces or common objects."
      ],
      "a": 1,
      "e": "<strong>Category-selective FFA activation in fMRI:</strong> In neurotypical controls, functional MRI demonstrates robust category-selective responses in the fusiform face area (FFA) of the fusiform gyrus, displaying a pronounced positive BOLD contrast when viewing faces compared to common objects (+2.45% in Table 1). In patients with acquired prosopagnosia due to fusiform gyrus lesions, this selective activation is virtually extinguished (+0.12%), demonstrating that the FFA is functionally specialized for face processing and that its focal disruption underlies selective face recognition failure.<br><br><em>Distractor Traps:</em><br>&bull; A (Overgeneralization): Patients with apperceptive or associative agnosias have primary lesions in the lateral occipital complex or anterior temporal cortex, not uniform FFA atrophy.<br>&bull; C (Incorrect Function): Early edge detection is mediated by simple and complex cells in V1 (striate cortex), not the high-level fusiform face area.<br>&bull; D (Directly Contradicted): Healthy controls show significant BOLD divergence (+2.45% contrast) between faces and objects, proving activation is not identical."
    },
    {
      "q": "Which experimental finding would provide the strongest support for the \"visual expertise hypothesis\" regarding the evolutionary function of the fusiform face area?",
      "ch": [
        "Car experts exhibiting robust FFA BOLD activation when discriminating visually homogeneous antique automobile models.",
        "Congenitally blind individuals demonstrating normal FFA activation in response to auditory human speech phonemes.",
        "Prosopagnosic individuals successfully discriminating vocal pitch contours despite complete loss of facial vision.",
        "Infants displaying an innate preference for schematic face-like paddles within thirty minutes of physical birth."
      ],
      "a": 0,
      "e": "<strong>The visual expertise hypothesis of the FFA:</strong> The domain-specificity hypothesis posits that the FFA is an innately dedicated module evolved exclusively for human facial processing. In contrast, the visual expertise hypothesis (championed by Isabel Gauthier and colleagues) posits that the FFA is a general-purpose cortical processor optimized for making fine-grained subordinate-level distinctions among visually homogeneous members of any object category for which the observer has acquired extensive expertise. Demonstrating that car experts or bird experts exhibit significant FFA activation when identifying subtle differences among cars or birds provides direct empirical support for the expertise hypothesis.<br><br><em>Distractor Traps:</em><br>&bull; B (Irrelevant to Visual Expertise): FFA activation to non-visual speech phonemes in blind individuals reflects cross-modal plasticity, not acquired visual perceptual expertise.<br>&bull; C (Sensory Modality Dissociation): Intact vocal recognition in prosopagnosia illustrates multi-sensory sparing, but does not address the visual expertise debate.<br>&bull; D (Supports Competing Hypothesis): Neonatal face preferences support the innate face-module hypothesis (domain-specificity), directly opposing the acquired expertise hypothesis."
    },
    {
      "q": "When a prosopagnosic patient fails to recognize their spouse visually but instantly recognizes them upon hearing them speak, which cognitive architecture is demonstrated?",
      "ch": [
        "A generalized semantic dementia that selectively spares low-level auditory frequency discrimination limens.",
        "A severe anterograde episodic memory deficit that impairs consolidation across all visual sensory domains.",
        "A global failure of symbolic language comprehension that selectively spares nonverbal social emotional cues.",
        "A modality-specific visual recognition deficit that leaves auditory person-identity nodes entirely intact."
      ],
      "a": 3,
      "e": "<strong>Modality-specific perceptual deficit versus multimodal semantic loss:</strong> Prosopagnosia is not a loss of person knowledge or semantic memory; patients have not forgotten who their spouse is, what their name is, or their shared life history. Instead, the deficit is strictly unimodal: the visual input pathway cannot access the intact person identity node (PIN). When the spouse speaks, acoustic signals are transduced through the auditory system to the superior temporal voice area and Wernicke's region, which successfully activate the person identity node and allow instant recognition. This double dissociation proves that the core deficit is perceptual and modality-specific rather than a generalized semantic or episodic memory impairment.<br><br><em>Distractor Traps:</em><br>&bull; A (Misdiagnosis): Semantic dementia is a progressive neurodegenerative loss of conceptual knowledge across all sensory modalities, not a spared-voice visual deficit.<br>&bull; B (Misdiagnosis): Anterograde episodic memory failure (e.g., hippocampal amnesia) prevents forming new episodic memories, but does not prevent recognizing a long-term spouse.<br>&bull; C (Misdiagnosis): The patient exhibits normal spoken language and auditory recognition, directly contradicting global language failure."
    }
  ]
}
