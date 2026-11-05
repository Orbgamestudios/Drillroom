import sys
import os

passage_data = {
  "id": "exam_ps90_4_disc",
  "sec": "P/S",
  "topic": "P/S Standalone Discrete Questions",
  "sheet": None,
  "label": "Psychological, Social, and Biological Foundations of Behavior",
  "examId": "ps90_4",
  "passage": "",
  "qs": [
    {
      "q": "After gazing at a continuously descending waterfall for 60 seconds, an observer looks at a stationary rock face and perceives the rocks drifting upward. What neurobiological mechanism explains this motion aftereffect?",
      "ch": [
        "Involuntary microscopic saccadic eye movements induce continuous illusory upward retinal slip.",
        "Direction-selective neurons in cortical area MT adapt, creating an upward population firing imbalance.",
        "Rhodopsin bleaching across inferior retinal photoreceptors impairs downward luminance processing.",
        "Spontaneous endolymph flow in the semicircular canals activates upward vestibular ocular reflexes."
      ],
      "a": 1,
      "e": "<strong>Neural basis of the motion aftereffect (waterfall illusion):</strong> The motion aftereffect (MAE) is mediated by direction-selective neurons located in the middle temporal visual area (area MT or V5). Under baseline conditions with a stationary stimulus, neurons tuned to opposite directions (downward vs. upward) fire at identical, balanced spontaneous resting rates. Prolonged exposure (60 seconds) to continuous downward motion causes selective neural fatigue and adaptation specifically among downward-tuned neurons, suppressing their baseline firing rate. When the observer suddenly views a stationary rock wall, the unadapted upward-tuned neurons fire at their normal resting rate, which now significantly exceeds the suppressed firing rate of the adapted downward neurons. The visual cortex decodes this population imbalance as net upward physical movement.<br><br><em>Distractor Traps:</em><br>&bull; A (Inversion / Mechanical Error): The motion aftereffect is a central cortical perceptual phenomenon that persists even during rigorous eye fixation or optical stabilization.<br>&bull; C (Peripheral Photoreceptor Error): Rhodopsin bleaching causes dark adaptation changes, but does not encode direction-selective motion vectors.<br>&bull; D (Mismatched Vestibular System): The semicircular canals transduce physical head rotation; gazing at a visual waterfall does not induce physical endolymph fluid flow."
    },
    {
      "q": "In dichotic listening tasks, listeners occasionally hear their own name spoken in the unattended ear. How does Treisman's Attenuation Model explain this phenomenon, where Broadbent's Early Filter Model fails?",
      "ch": [
        "Unattended stimuli are attenuated rather than blocked, and personally salient signals have low activation thresholds.",
        "The early sensory filter completely blocks all unattended inputs, but the auditory nerve conducts names via bone pathways.",
        "Information from the unattended ear bypasses the thalamus to directly activate lexical semantic representations in Broca's area.",
        "Attention alternates randomly between ears on every syllable, ensuring that all unattended auditory signals are fully decoded."
      ],
      "a": 0,
      "e": "<strong>Treisman's Attenuation Model and the Cocktail Party Effect:</strong> Donald Broadbent's original Early Filter Model proposed an all-or-none bottleneck: unattended sensory inputs are completely blocked immediately after elementary physical analysis, which made it impossible to explain why listeners in dichotic listening experiments frequently notice personally meaningful stimuli (such as their own name) spoken softly in the unattended ear (the Cocktail Party Effect). Anne Treisman resolved this by proposing an attenuation filter. Instead of completely blocking unattended inputs, the attenuator simply turns down their signal volume. Word detectors in the mental lexicon have variable activation thresholds: while neutral, unexpected words require strong acoustic signals to cross threshold, personally salient or emotionally charged words (like one's name or 'fire') have permanently low thresholds, allowing even an attenuated whisper to trigger conscious recognition.<br><br><em>Distractor Traps:</em><br>&bull; B (Theoretical Contradiction): Broadbent's model cannot explain hearing one's name; invoking bone conduction is biologically baseless in headphone experiments.<br>&bull; C (Anatomical Nonsense): All auditory signals must pass through the cochlear nuclei, superior olive, inferior colliculus, and medial geniculate thalamic nucleus before cortex.<br>&bull; D (Incorrect Model): Treisman's model relies on continuous attenuation and threshold modulation, not rapid random syllable-by-syllable ear switching."
    },
    {
      "q": "According to Kahneman's capacity model of attention and multiple resource theory, why does engaging in a complex phone conversation impair driving performance even when utilizing a hands-free device?",
      "ch": [
        "Auditory phone conversations physically paralyze descending corticospinal motor tracts controlling leg reflexes.",
        "Speaking into a wireless hands-free microphone induces rapid sensory adaptation across middle ear hair cells.",
        "Both tasks draw upon a limited central executive capacity, producing severe cognitive resource competition.",
        "Divided attention causes temporary bilateral visual field scotomas that extinguish peripheral retinal vision."
      ],
      "a": 2,
      "e": "<strong>Kahneman's cognitive capacity model and divided attention:</strong> Daniel Kahneman's capacity model of attention posits that the human brain possesses a finite, pool of general cognitive processing resources. When performing two cognitively demanding tasks concurrently (such as actively navigating unpredictable highway traffic while processing complex verbal dialogue on a hands-free phone), the aggregate resource demands exceed total available cognitive capacity. Furthermore, under Multiple Resource Theory (Wickens), engaging in mental visualization or complex verbal decision-making diverts central executive attention away from visual scene analysis, causing delayed braking response times, missed traffic signals, and inattentional blindness, regardless of whether hands remain on the steering wheel.<br><br><em>Distractor Traps:</em><br>&bull; A (Extreme Neurological Fallacy): Conversation does not induce physical paralysis of corticospinal motor pathways.<br>&bull; B (Peripheral Inaccuracy): Speaking hands-free does not paralyze or desensitize hair cells within the organ of Corti.<br>&bull; D (Pathological Misattribution): Divided attention creates cognitive inattentional blindness, not physical blindness or anatomical visual scotomas."
    },
    {
      "q": "In classic dichotic listening shadowing experiments (Cherry, 1953), what specific alteration in the unattended auditory channel do listeners consistently fail to notice, supporting early acoustic filtering?",
      "ch": [
        "A sudden shift in acoustic pitch from a deep masculine voice to a high-pitched feminine voice.",
        "A transition in the spoken speech from English to German, or an abrupt switch to backwards speech.",
        "The complete replacement of the spoken speech stream with a continuous loud sinusoidal tone.",
        "A dramatic increase in the physical volume and acoustic sound pressure level of the spoken stream."
      ],
      "a": 1,
      "e": "<strong>Dichotic shadowing findings and early selection:</strong> In Colin Cherry's foundational dichotic listening experiments, participants shadowed (repeated aloud verbatim) a continuous spoken message delivered to one ear while ignoring an unattended message in the opposite ear. When tested on what occurred in the unattended ear, listeners easily detected gross physical acoustic changes—such as the voice changing from male to female (pitch shift), the voice being replaced by a loud 400 Hz pure tone, or sound stopping entirely. However, they were completely oblivious to semantic linguistic modifications, such as the speech transitioning from English to German, or the speech being played completely backwards. This finding provided cornerstone evidence for early selection models, demonstrating that unattended inputs are processed for basic physical features but not automatically decoded for linguistic syntax or semantics.<br><br><em>Distractor Traps:</em><br>&bull; A (Opposite Empirical Finding): Observers easily and consistently detect shifts in vocal pitch and gender in the unattended ear.<br>&bull; C (Opposite Empirical Finding): Participants immediately notice when human speech is replaced by a loud pure tone.<br>&bull; D (Opposite Empirical Finding): Participants readily detect dramatic increases or decreases in physical volume."
    },
    {
      "q": "How does the cognitive failure known as inattentional blindness differ fundamentally from the phenomenon of change blindness?",
      "ch": [
        "Inattentional blindness occurs only in auditory domains, whereas change blindness occurs exclusively in visual domains.",
        "Change blindness involves damage to the fusiform face area, whereas inattentional blindness is caused by retinal lesions.",
        "Inattentional blindness involves failing to detect modifications across flickers, whereas change blindness ignores novel objects.",
        "Inattentional blindness misses a visible novel item during focused tasks, whereas change blindness misses differences across flickers."
      ],
      "a": 3,
      "e": "<strong>Distinguishing inattentional blindness from change blindness:</strong> Both represent striking failures of visual awareness, but their experimental paradigms and operational definitions differ. Inattentional blindness occurs when an observer fails to notice a fully visible, unexpected, novel object or event that appears in plain sight (such as the gorilla walking through a basketball game in Simons & Chabris, 1999) because their focal spatial attention is intensely occupied with an ongoing task. In contrast, change blindness occurs when an observer fails to notice a substantial visual modification between two successive versions of a visual scene separated by a brief visual disruption (such as a visual flicker mask, screen blank, blink, or saccade in Rensink's flicker paradigm).<br><br><em>Distractor Traps:</em><br>&bull; A (Modality Error): Both inattentional blindness and change blindness are quintessential visual attentional phenomena.<br>&bull; B (Pathological Fallacy): Both phenomena occur reliably in healthy neurotypical observers; neither is caused by focal brain damage or retinal lesions.<br>&bull; C (Directional Inversion): This completely swaps the definitions: inattentional blindness misses unexpected novel objects, while change blindness misses modifications across flickers."
    },
    {
      "q": "According to Anne Treisman's Feature Integration Theory, what behavioral visual search pattern uniquely characterizes a conjunction search?",
      "ch": [
        "Search reaction times increase linearly as distractor set size grows, requiring serial focused attention.",
        "Search reaction times remain strictly flat and constant across set sizes, mediated by rapid pop-out effects.",
        "Target identification occurs in a pre-attentive stage that processes both color and orientation in parallel.",
        "Targets are identified significantly faster when surrounded by large numbers of visually similar distractors."
      ],
      "a": 0,
      "e": "<strong>Conjunction searches in Feature Integration Theory (FIT):</strong> According to Anne Treisman's Feature Integration Theory, visual processing occurs in two successive stages. In the pre-attentive stage, individual primary features (e.g., color, shape, line orientation) are analyzed automatically, rapidly, and in parallel across the entire visual field, producing instantaneous \"pop-out\" effects with flat search slopes ($O(1)$) when searching for a single unique feature (e.g., a red circle among green circles). However, in a conjunction search, the target is defined by a unique combination of two or more shared features (e.g., searching for a red circle among red squares and green circles). In the focused attention stage, the observer must deploy focal spatial attention serially to each individual item location to bind its features together, causing reaction time to increase in direct linear proportion ($O(N)$) to the number of distractors.<br><br><em>Distractor Traps:</em><br>&bull; B (Describes Single-Feature Pop-Out): Flat search slopes across set sizes characterize pre-attentive single-feature searches, not conjunction searches.<br>&bull; C (Theoretical Contradiction): In FIT, the pre-attentive stage processes features in parallel feature maps, but cannot bind conjunctions without serial focal attention.<br>&bull; D (Contradicted by Empirical Search Data): Increasing the number of distractors slows conjunction searches; it never accelerates identification."
    },
    {
      "q": "Why does an ischemic stroke in the right inferior parietal lobule frequently cause severe contralateral hemispatial neglect, whereas left-sided parietal lesions rarely do?",
      "ch": [
        "The left parietal cortex lacks all neurovascular collateral circulation, causing immediate tissue death.",
        "The left parietal cortex is dedicated exclusively to processing fine motor control of both upper limbs.",
        "The right parietal cortex directs attention bilaterally, whereas the left cortex attends only to right space.",
        "The right parietal cortex contains all primary tonotopic mappings for auditory and vestibular sensation."
      ],
      "a": 2,
      "e": "<strong>Hemispheric asymmetry in spatial attention (Mesulam's model):</strong> Hemispatial neglect (spatial inattention) is profoundly asymmetric. According to Marcel Mesulam's attentional matrix model, the right cerebral hemisphere is dominant for spatial attention: the right inferior parietal lobule / temporoparietal junction contains neural representations that direct attention across both the left and right hemispaces. In contrast, the left hemisphere contains neural representations that attend almost exclusively to the contralateral right hemispace. Consequently, when the right hemisphere is damaged, the left hemisphere cannot compensate for the neglected left hemispace, resulting in severe left hemispatial neglect. When the left hemisphere is damaged, the intact right hemisphere continues to direct attention to both hemispaces, preventing severe right neglect.<br><br><em>Distractor Traps:</em><br>&bull; A (Vascular Inaccuracy): Both hemispheres receive equivalent arterial blood supply from the middle cerebral arteries and circle of Willis collaterals.<br>&bull; B (Mismatched Function): The left motor strip (precentral gyrus) controls right limb movement; it is not the explanation for spatial attentional asymmetry.<br>&bull; D (Incorrect Anatomical Locus): Primary tonotopic auditory maps reside in Heschl's gyrus of the superior temporal lobe (BA 41), not the inferior parietal lobule."
    },
    {
      "q": "In an experiment investigating subliminal perception, a prime word is flashed for 20 ms followed by a pattern mask. What experimental evidence demonstrates implicit semantic priming?",
      "ch": [
        "Participants consciously describe the semantic meaning of the prime word with high confidence.",
        "Reaction times to classify semantically related targets are accelerated despite zero conscious awareness.",
        "Pupillary constriction occurs selectively in response to unprimed, novel, non-associated targets.",
        "Visual acuity limens tested with Snellen charts improve by two lines following masked prime exposure."
      ],
      "a": 1,
      "e": "<strong>Subliminal semantic priming and implicit cognition:</strong> Subliminal perception occurs when sensory stimuli are presented below an observer's subjective threshold of conscious awareness (e.g., using tachistoscopic presentation for 20 ms followed immediately by a high-contrast pattern mask). Although participants report that they saw only a flash of light and cannot report the identity of the prime, Anthony Marcel and subsequent researchers demonstrated implicit semantic priming: when asked to perform a lexical decision task on a subsequent suprathreshold target word (e.g., deciding whether 'DOCTOR' is a word), reaction times are significantly faster when preceded by a semantically related masked prime (e.g., 'NURSE') compared to an unrelated prime ('BREAD'). This proves that semantic meaning was decoded and activated in memory without conscious awareness.<br><br><em>Distractor Traps:</em><br>&bull; A (Contradicts Subliminal Definition): If participants consciously describe the prime, it was supraliminal (above threshold), not subliminal.<br>&bull; C (Irrelevant Metric): Pupil constriction is an autonomic pupillary light reflex, not an established index of lexical decision semantic priming.<br>&bull; D (Physiological Nonsense): Brief semantic primes do not alter physical optical refractive power or Snellen visual acuity thresholds."
    },
    {
      "q": "In free-recall tasks evaluating the Atkinson-Shiffrin multi-store model, what experimental manipulation selectively abolishes the recency effect while sparing the primacy effect?",
      "ch": [
        "Presenting list words at an accelerated rate of four words per second instead of one word.",
        "Displaying list items visually on a screen rather than reading them aloud over headphones.",
        "Using abstract low-frequency nouns instead of highly concrete, easily visualizable nouns.",
        "Requiring participants to count backward by threes for 30 seconds immediately prior to recall."
      ],
      "a": 3,
      "e": "<strong>The serial position effect in the Atkinson-Shiffrin model:</strong> The serial position effect demonstrates the distinction between short-term memory (STM) and long-term memory (LTM). The primacy effect (superior recall of items from the beginning of the list) occurs because early items receive more attentional maintenance rehearsal and are successfully transferred into consolidated LTM. The recency effect (superior recall of items from the end of the list) occurs because the final items remain immediately accessible within the limited-capacity short-term buffer. Introducing a 30-second distracter task (such as counting backward by threes, the Peterson and Peterson distractor technique) occupies working memory rehearsal buffers, causing terminal items to decay and completely abolishing the recency effect, while leaving the consolidated primacy items in LTM completely unaffected.<br><br><em>Distractor Traps:</em><br>&bull; A (Affects Primacy, Not Recency): Presenting items faster impairs rehearsal time and suppresses the primacy effect, while leaving the recency effect intact.<br>&bull; B (Modality Shift): Switching from auditory to visual presentation modulates the modality effect in recency, but does not selectively abolish recency.<br>&bull; C (Affects Overall Memorability): Word concreteness influences depth of processing and LTM encoding, but does not selectively extinguish recency."
    },
    {
      "q": "In George Sperling's (1960) tachistoscopic matrix experiments, how did the partial-report technique demonstrate that iconic sensory memory has a vast storage capacity?",
      "ch": [
        "Participants retained all twelve letters indefinitely if they rehearsed them using the phonological loop.",
        "Observers recalled entire matrices flawlessly when auditory retrieval cues were delayed by ten seconds.",
        "Observers cued to recall a specific row immediately after display offset recalled nearly all of its letters.",
        "Participants demonstrated equal recall accuracy regardless of whether the visual matrix was masked or unmasked."
      ],
      "a": 2,
      "e": "<strong>Sperling's partial-report paradigm and iconic memory:</strong> George Sperling flashed a $3 \\times 4$ array of 12 letters for 50 milliseconds. Under traditional whole-report conditions, participants could recall only 4 to 5 letters (~35&ndash;40%), suggesting that sensory memory was severely capacity-limited. However, Sperling introduced the partial-report technique: immediately after the visual display disappeared, an auditory tone (high, medium, or low pitch) signaled which specific row (top, middle, or bottom) the subject had to report. Because participants did not know which row would be cued until after the display vanished, and they consistently scored nearly 100% accuracy on whichever row was cued (multiplying out to ~9&ndash;12 letters available), Sperling proved that iconic sensory memory captures virtually the entire visual scene with massive capacity, but this iconic trace decays rapidly within 250 to 500 milliseconds.<br><br><em>Distractor Traps:</em><br>&bull; A (Mismatched Memory Store): Phonological rehearsal maintains items in working/short-term memory, whereas Sperling's experiment measured pre-categorical visual iconic memory.<br>&bull; B (Directly Contradicted): When the cue was delayed by even 1 second, recall dropped to whole-report levels (~4 items), proving iconic memory decays in under a second.<br>&bull; D (Directly Contradicted): Visual masking destroys the iconic trace, severely impairing partial-report performance."
    }
  ]
}

for q in passage_data["qs"]:
    q["d"] = True
