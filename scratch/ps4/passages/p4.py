import sys
import os

passage_data = {
  "id": "exam_ps90_4_p4",
  "sec": "P/S",
  "topic": "Auditory Agnosia, Pure Word Deafness & Amusia",
  "sheet": None,
  "label": "Psychological, Social, and Biological Foundations of Behavior",
  "examId": "ps90_4",
  "passage": "<div class=\"ttl\">Passage 4 (Questions 19&ndash;24)</div>\n<p>Central auditory processing requires the transformation of acoustic waveforms from primary auditory cortex (A1, located in Heschl's transverse gyrus within Brodmann area 41) into complex perceptual representations within secondary auditory association cortices (BA 42 and BA 22). When cortical pathology spares the peripheral hearing apparatus yet disrupts central acoustic processing networks, patients present with distinct auditory agnosias. These neuropsychological syndromes exhibit striking modular dissociations between phonological linguistic decoding, environmental sound recognition, and musical contour discrimination.</p>\n<p>A classic cortical dissociation is pure word deafness (auditory verbal agnosia). Individuals afflicted with pure word deafness exhibit a profound inability to comprehend or repeat spoken speech, frequently remarking that spoken language sounds like an unintelligible foreign tongue or static noise. Remarkably, their spontaneous speech is fluent and articulate, their writing is grammatical, and their reading comprehension remains completely intact. This syndrome typically stems from bilateral or deep left superior temporal lobe lesions that isolate intact language comprehension networks (Wernicke's area, BA 22) from bilateral auditory input. In contrast, environmental sound agnosia impairs the recognition of familiar non-verbal acoustic signals (e.g., ringing telephones, thunder, barking dogs) while sparing linguistic comprehension. Furthermore, congenital amusia (tone deafness) represents a lifelong neurodevelopmental deficit in fine-grained musical pitch perception and melodic contour tracking, linked to disrupted connectivity along the right frontotemporal auditory tract.</p>\n<p>Audiologists and cognitive neurologists evaluated cohorts of patients exhibiting focal auditory processing deficits alongside healthy controls using standardized diagnostic batteries. Protocols evaluated pure-tone hearing thresholds, verbal repetition, written text comprehension, non-verbal sound identification, and Montreal Battery of Evaluation of Amusia (MBEA) scores, as reported in Table 1.</p>\n<table class=\"tbl\">\n  <caption>Table 1 Audiometric limens, linguistic processing, environmental sound identification, and musical pitch scores across auditory cohorts</caption>\n  <thead>\n    <tr><th>Clinical Evaluation Cohort</th><th>Pure-Tone Threshold (dB HL)</th><th>Spoken Speech Repetition (%)</th><th>Written Text Comprehension (%)</th><th>Environmental Sound ID (%)</th><th>MBEA Pitch Contour (%)</th><th>Spontaneous Speech (wpm)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Pure Word Deafness ($n=10$)</td><td>16.4 dB</td><td>12.8%</td><td>98.2%</td><td>89.5%</td><td>88.0%</td><td>124 wpm</td></tr>\n    <tr><td>Environmental Sound Agnosia ($n=10$)</td><td>15.2 dB</td><td>96.4%</td><td>97.5%</td><td>21.3%</td><td>84.6%</td><td>126 wpm</td></tr>\n    <tr><td>Congenital Amusia ($n=16$)</td><td>14.8 dB</td><td>97.8%</td><td>98.6%</td><td>92.1%</td><td>48.2%</td><td>128 wpm</td></tr>\n    <tr><td>Healthy Matched Controls ($n=20$)</td><td>13.5 dB</td><td>98.5%</td><td>98.9%</td><td>95.8%</td><td>93.4%</td><td>130 wpm</td></tr>\n  </tbody>\n</table>",
  "qs": [
    {
      "q": "Which diagnostic finding from Table 1 provides the strongest evidence that pure word deafness is an input-disconnection syndrome rather than a central language aphasia?",
      "ch": [
        "Normal pure-tone audiometry thresholds demonstrating preserved cochlear transduction mechanics.",
        "Impaired spoken repetition scores matching the severe loss observed in global language aphasias.",
        "Preserved environmental sound identification proving that left temporal cortex is fully operational.",
        "Completely preserved written comprehension and fluent spontaneous speech despite speech deafness."
      ],
      "a": 3,
      "e": "<strong>Pure word deafness as an auditory input-disconnection syndrome:</strong> In pure word deafness (auditory verbal agnosia), patients score catastrophically low on spoken speech repetition (12.8% in Table 1) and spoken comprehension. However, their written text comprehension is virtually flawless (98.2%) and their spontaneous speech is fluent and articulate (124 words per minute). In true language aphasias (such as Wernicke's or global aphasia), central lexical-semantic networks are damaged, which inevitably impairs both spoken comprehension and written reading comprehension. The selective failure of spoken comprehension in the presence of immaculate reading and writing confirms that central language faculties are fully intact, and that the disorder is an auditory-verbal disconnection between Heschl's gyrus and Wernicke's area.<br><br><em>Distractor Traps:</em><br>&bull; A (True Fact Wrong Question): Normal audiometry proves peripheral hearing is intact, but does not distinguish central aphasia from an auditory input disconnection.<br>&bull; B (Supports Competing Claim): Low spoken repetition is shared with several aphasias; it does not isolate the input-disconnection nature of the disorder.<br>&bull; C (Incomplete Rationale): Spared environmental sound identification shows preserved acoustic analysis, but spared reading/writing is the direct proof of intact central language."
    },
    {
      "q": "What specific neuroanatomical disruption produces pure word deafness while sparing reading comprehension and spontaneous verbal articulation?",
      "ch": [
        "Bilateral disconnection of primary auditory cortex input from the left posterior superior temporal gyrus.",
        "Focal infarction of the arcuate fasciculus disconnecting Broca's motor speech area from the hippocampus.",
        "Total bilateral destruction of Heschl's transverse gyrus eliminating all primary acoustic representations.",
        "Degenerative atrophy of the left angular gyrus abolishing cross-modal phonetic-to-graphemic conversions."
      ],
      "a": 0,
      "e": "<strong>Neuroanatomical basis of pure word deafness:</strong> Pure word deafness occurs when primary auditory signals cannot reach Wernicke's area in the left posterior superior temporal gyrus (BA 22). This typically results from either bilateral subcortical lesions in the temporal acoustic radiations or a unilateral left subcortical lesion that simultaneously cuts ipsilateral projections from the left Heschl's gyrus and transcallosal fibers arriving from the right Heschl's gyrus. Because Wernicke's area itself is structurally undamaged, it can still receive visual linguistic inputs from the angular gyrus (enabling reading) and project to Broca's area via the arcuate fasciculus (enabling fluent speech).<br><br><em>Distractor Traps:</em><br>&bull; B (Mismatched Syndrome): Disconnection of the arcuate fasciculus between Wernicke's and Broca's areas causes conduction aphasia (impaired repetition with intact comprehension), not pure word deafness.<br>&bull; C (Extreme / Incorrect Syndrome): Bilateral destruction of Heschl's transverse gyrus produces cortical deafness (loss of all conscious hearing), which would elevate pure-tone thresholds and eliminate environmental sound recognition.<br>&bull; D (Mismatched Syndrome): Damage to the angular gyrus causes alexia with agraphia (inability to read and write), directly contradicting the intact reading found in pure word deafness."
    },
    {
      "q": "The behavioral dissociation between pure word deafness and environmental sound agnosia in Table 1 supports which theoretical model of acoustic cognition?",
      "ch": [
        "A unitary cognitive processing system where acoustic complexity alone dictates perceptual recognition.",
        "Dual modular cortical streams segregating verbal linguistic decoding from non-verbal sound processing.",
        "A hierarchical serial bottleneck where non-verbal sounds must be categorized before phonological decoding.",
        "An equipotential cortical model wherein all temporal lobe subregions process all acoustic signals identically."
      ],
      "a": 1,
      "e": "<strong>Modular processing of speech versus environmental acoustics:</strong> Table 1 reveals a classic double dissociation: patients with pure word deafness cannot process speech (12.8% repetition) but excel at environmental sounds (89.5%), whereas patients with environmental sound agnosia cannot recognize non-verbal sounds (21.3%) but understand and repeat spoken speech normally (96.4%). A double dissociation provides gold-standard neuropsychological proof that the brain utilizes distinct, functionally autonomous cognitive modules or neural processing pathways: one dedicated to linguistic phonological analysis (predominantly left-lateralized superior temporal) and another dedicated to complex acoustic environmental patterns (bilateral or right-lateralized temporoparietal).<br><br><em>Distractor Traps:</em><br>&bull; A (Contradicted by Double Dissociation): If a single unitary system existed governed only by complexity, one group could not fail on speech while sparing sounds, while the other failed on sounds while sparing speech.<br>&bull; C (Contradicted by Data): If environmental recognition were a prerequisite bottleneck for speech, patients with environmental agnosia could not exhibit 96.4% speech repetition.<br>&bull; D (Directly Contradicted): Equipotentiality argues that all cortical regions share identical functions, which is refuted by functional localization and modularity."
    },
    {
      "q": "Which neural tract pathology is most strongly implicated in the selective deficit in pitch contour and melodic discrimination observed in congenital amusia?",
      "ch": [
        "Unilateral demyelination of the corticospinal tract impairing fine vocal motor chord control.",
        "Bilateral calcification of the stria vascularis disrupting endocochlear electrical potentials.",
        "Reduced white matter connectivity in the right superior longitudinal fasciculus and arcuate fasciculus.",
        "Excitotoxic glutamate damage to the medial geniculate nucleus abolishing auditory signal relays."
      ],
      "a": 2,
      "e": "<strong>Frontotemporal tract connectivity in congenital amusia:</strong> Neuroimaging studies (using diffusion tensor imaging and resting-state fMRI) have demonstrated that congenital amusia is not a peripheral ear disease (pure-tone thresholds are normal: 14.8 dB in Table 1). Instead, amusia is linked to microstructural abnormalities and reduced white matter tract connectivity in the right hemisphere's auditory-frontal feedback loop—specifically the right superior longitudinal fasciculus and the right arcuate fasciculus connecting the right superior temporal gyrus (auditory cortex) with the right inferior frontal gyrus (BA 44/47). This pathway is crucial for fine-grained pitch discrimination, tonal contour tracking, and musical working memory.<br><br><em>Distractor Traps:</em><br>&bull; A (Wrong Pathway): The corticospinal tract mediates voluntary motor control of spinal skeletal muscles, not auditory or musical perception.<br>&bull; B (Peripheral Pathology): The stria vascularis maintains the endocochlear potential in the cochlea; its dysfunction causes sensorineural hearing loss (elevated pure-tone thresholds), not amusia.<br>&bull; D (Extreme Subcortical Deficit): Severe damage to the medial geniculate nucleus of the thalamus would abolish auditory input entirely, causing profound sensorineural deafness."
    },
    {
      "q": "A neurologist evaluates a stroke patient who cannot understand spoken language. Which clinical feature decisively differentiates pure word deafness from Wernicke's aphasia?",
      "ch": [
        "The patient exhibits severe sensorineural hearing loss on standard pure-tone audiometry.",
        "The patient speaks fluently without paraphasias and displays normal reading comprehension.",
        "The patient communicates solely through manual gestures due to bilateral vocal fold paralysis.",
        "The patient exhibits fluent speech characterized by neologisms and profound reading comprehension deficits."
      ],
      "a": 1,
      "e": "<strong>Distinguishing pure word deafness from Wernicke's aphasia:</strong> Both patients with pure word deafness and patients with Wernicke's aphasia have severe difficulty understanding spoken speech. However, their spontaneous speech and written reading comprehension are starkly opposite. Wernicke's aphasia involves damage to the lexical-semantic storage in Wernicke's area itself; therefore, patients exhibit fluent but nonsensical speech filled with phonemic and semantic paraphasias, word substitutions, and neologisms (\"word salad\"), along with severely impaired reading comprehension. In contrast, pure word deafness leaves Wernicke's area intact; patients speak flawlessly, fluently, and meaningfully, and can read and write with perfect comprehension.<br><br><em>Distractor Traps:</em><br>&bull; A (Diagnostic Contradiction): Neither pure word deafness nor Wernicke's aphasia is characterized by peripheral sensorineural hearing loss on audiometry.<br>&bull; C (Motor Symptom): Vocal cord paralysis is a peripheral vagus nerve (CN X) lesion, not a cortical auditory or language disorder.<br>&bull; D (Describes Wernicke's Aphasia): Neologistic speech and impaired reading characterize Wernicke's aphasia itself, which is what pure word deafness is being contrasted against."
    },
    {
      "q": "The normal pure-tone thresholds across all cohorts in Table 1 (13.5&ndash;16.4 dB HL) demonstrate that which physiological acoustic mechanism is fully preserved?",
      "ch": [
        "High-level semantic categorization within bilateral anterior superior temporal sulci.",
        "Feedback efferent modulation of middle ear ossicles by the tensor tympani and stapedius muscles.",
        "Tonotopic mechanical frequency dispersion along the cochlear basilar membrane and auditory nerve.",
        "Frontoparietal top-down attentional filtering of competing acoustic dichotic speech streams."
      ],
      "a": 2,
      "e": "<strong>Tonotopic cochlear transduction and pure-tone audiometry:</strong> Pure-tone audiometry measures the minimal sound pressure level required to detect single-frequency sinusoidal acoustic waves across the human audible spectrum (typically 250 to 8000 Hz). Detecting these tones relies on peripheral mechanics: sound waves vibrate the tympanic membrane and ossicles, transferring fluid waves through the perilymph to displace the basilar membrane. The basilar membrane is tonotopically organized (stiff and narrow at the base for high frequencies; wide and compliant at the apex for low frequencies). Hair cell stereocilia deflection depolarizes the auditory nerve (CN VIII), transmitting signals to the cochlear nucleus and primary auditory cortex. Intact thresholds (<20 dB HL) prove this peripheral tonotopic apparatus is completely preserved.<br><br><em>Distractor Traps:</em><br>&bull; A (Cortical Language Function): Semantic categorization occurs in higher-order association cortices, which are damaged or disconnected in auditory agnosias.<br>&bull; B (Middle Ear Reflex): The acoustic reflex dampens loud sounds (>80 dB) to protect against acoustic trauma, but is not the mechanism measured by threshold audiometry.<br>&bull; D (Attentional Executive Function): Top-down dichotic filtering is a frontal-executive selective attention process, not the peripheral mechanism verified by pure-tone limens."
    }
  ]
}
