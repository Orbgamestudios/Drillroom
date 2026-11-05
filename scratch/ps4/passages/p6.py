import sys
import os

passage_data = {
  "id": "exam_ps90_4_p6",
  "sec": "P/S",
  "topic": "Perceptual Set, Expectancy Effects & Context Effects",
  "sheet": None,
  "label": "Psychological, Social, and Biological Foundations of Behavior",
  "examId": "ps90_4",
  "passage": "<div class=\"ttl\">Passage 6 (Questions 31&ndash;36)</div>\n<p>Perception is not an objective registration of physical reality; rather, it is actively constructed by an observer's internal cognitive state. A central psychological framework formalizing this phenomenon is the concept of a perceptual set&mdash;a temporary mental predisposition or cognitive readiness to perceive certain aspects of available sensory data while completely ignoring others. Perceptual sets are established and modulated by an intricate convergence of prior expectations, environmental contexts, cultural socialization, affective states, and internal motivational drives.</p>\n<p>The potent influence of expectations was famously demonstrated by Bugelski and Alampay (1961) using the ambiguous \"rat-man\" figure. Participants exposed to a preceding series of animal drawings overwhelmingly perceived the ambiguous graphic as a rodent, whereas those exposed to human portrait line drawings perceived the identical physical stimulus as a bald man wearing spectacles. Beyond semantic priming, physiological drive states also exert profound top-down control over perception. Jerome Bruner's \"New Look\" psychology posited that subjective value and physiological need states warp sensory interpretation, lowering perceptual thresholds for drive-relevant stimuli. For instance, hungry observers display an involuntary perceptual set that categorizes ambiguous visual contours as food items.</p>\n<p>To quantify how internal homeostatic deprivation interacts with external contextual priming, researchers conducted a 2 &times; 2 randomized controlled experiment with 80 healthy volunteers. Participants were assigned to either a 12-hour fasting condition or a recently satiated condition, followed by exposure to either food-related or animal-related semantic primes. Observers subsequently classified tachistoscopically presented ambiguous drawings. Behavioral categorization percentages, response latencies, and signal detection decision criteria ($\\beta$, where $\\beta < 1$ denotes a liberal bias toward food categorization) are recorded in Table 1.</p>\n<table class=\"tbl\">\n  <caption>Table 1 Ambiguous figure categorization percentages, response latencies, and signal detection criterion metrics across physiological states and semantic contexts</caption>\n  <thead>\n    <tr><th>Experimental Cohort</th><th>Homeostatic State</th><th>Preceding Semantic Context</th><th>Food Categorization (%)</th><th>Animal Categorization (%)</th><th>Categorization Latency (ms)</th><th>Decision Criterion ($\\beta$)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Cohort 1 ($n=20$)</td><td>12-Hour Fasted (Hungry)</td><td>Food-Related Semantic Prime</td><td>84.5%</td><td>15.5%</td><td>410 ms</td><td>0.58 (Liberal)</td></tr>\n    <tr><td>Cohort 2 ($n=20$)</td><td>12-Hour Fasted (Hungry)</td><td>Animal-Related Semantic Prime</td><td>46.8%</td><td>53.2%</td><td>585 ms</td><td>0.94 (Neutral)</td></tr>\n    <tr><td>Cohort 3 ($n=20$)</td><td>Satiated Baseline (Fed)</td><td>Food-Related Semantic Prime</td><td>58.2%</td><td>41.8%</td><td>495 ms</td><td>0.88 (Neutral)</td></tr>\n    <tr><td>Cohort 4 ($n=20$)</td><td>Satiated Baseline (Fed)</td><td>Animal-Related Semantic Prime</td><td>18.4%</td><td>81.6%</td><td>425 ms</td><td>1.42 (Conservative)</td></tr>\n  </tbody>\n</table>",
  "qs": [
    {
      "q": "Which formal definition best captures the psychological construct of a \"perceptual set\" as described in the passage?",
      "ch": [
        "A temporary loss of retinal cone photoreceptor sensitivity following prolonged daylight exposure.",
        "A mental predisposition or cognitive readiness to perceive sensory stimuli in a particular manner.",
        "A neurological disconnection syndrome segregating primary striate cortex from temporal networks.",
        "An automated subcortical motor reflex that realigns the fovea toward moving peripheral targets."
      ],
      "a": 1,
      "e": "<strong>Definition and nature of a perceptual set:</strong> A perceptual set refers to a cognitive readiness, mental posture, or predisposition to perceive sensory information in a particular way while ignoring competing interpretations. It illustrates that perception is a top-down, active, hypothesis-driven construction rather than passive sensory recording. Perceptual sets are dynamically shaped by contextual primes (e.g., surrounding words or images), prior experience, cultural learning, current emotional mood, and internal physiological drives (such as hunger or thirst).<br><br><em>Distractor Traps:</em><br>&bull; A (Mismatched Concept): Photoreceptor desensitization describes physiological sensory adaptation, not a cognitive perceptual set.<br>&bull; C (Pathological Misattribution): Cortical disconnections describe neurological agnosias or visual disconnections, not normal psychological set formation.<br>&bull; D (Motor Reflex): Realigning the fovea via saccades or the optokinetic reflex is an oculomotor motor response, not a cognitive perceptual set."
    },
    {
      "q": "In Table 1, 12-hour fasted participants exposed to food primes exhibited a decision criterion of $\\beta = 0.58$. What does this metric indicate in Signal Detection Theory?",
      "ch": [
        "The participants exhibited extreme sensory degradation resulting in near-zero visual acuity.",
        "The participants exhibited complete inability to discriminate signal distributions from noise.",
        "The participants adopted a highly conservative criterion requiring extreme sensory certainty.",
        "The participants adopted a liberal decision bias, requiring minimal evidence to report food."
      ],
      "a": 3,
      "e": "<strong>Signal Detection Theory criterion shifts ($\\beta$):</strong> In Signal Detection Theory, the decision criterion ($\\beta$ or $c$) reflects an observer's internal threshold or bias for deciding whether a target stimulus is present. A neutral criterion sits at $\\beta = 1.0$ (or $c = 0$). When $\\beta < 1.0$ (as in Cohort 1 with $\\beta = 0.58$), the observer adopts a \"liberal\" response criterion, meaning they require very little sensory evidence before endorsing the presence of the target (in this case, categorizing the ambiguous drawing as food). This demonstrates that biological hunger shifts cognitive response thresholds, predisposing observers to \"see\" drive-relevant food objects even in ambiguous visual noise.<br><br><em>Distractor Traps:</em><br>&bull; A (Mismatched SDT Metric): Sensory degradation and visual acuity affect sensory sensitivity ($d'$), not the response criterion threshold ($\\beta$).<br>&bull; B (Mismatched SDT Metric): Inability to discriminate signal from noise corresponds to a sensitivity of $d' = 0$, not a criterion shift.<br>&bull; C (Directional Inversion): A conservative criterion requires strong sensory certainty and is represented by $\\beta > 1.0$ (as seen in Cohort 4, $\\beta = 1.42$)."
    },
    {
      "q": "Through which cognitive mechanism does preceding exposure to animal words facilitate the rapid perception of an ambiguous drawing as a rodent?",
      "ch": [
        "Spreading activation through semantic networks pre-activates related conceptual schemas in memory.",
        "Permanent synaptic depression across primary visual simple cells suppresses all contour detection.",
        "Excitotoxic dopamine release in the basolateral amygdala produces transient auditory hallucinations.",
        "Lateral inhibition within retinal ganglion cells physically reshapes incoming optical photon waves."
      ],
      "a": 0,
      "e": "<strong>Spreading activation and semantic priming in perceptual sets:</strong> In cognitive network models of memory (such as Collins and Loftus' spreading activation theory), concepts are represented as interconnected nodes within a semantic network. When a participant reads animal-related prime words (e.g., 'forest', 'rabbit', 'paws'), activation spreads along associative links, pre-activating related animal schemas in semantic memory. When an ambiguous visual stimulus (such as the Bugelski rat-man figure) is immediately presented, these pre-activated animal concepts provide top-down predictive hypotheses, causing the visual system to assimilate ambiguous features into the pre-activated 'rat' schema.<br><br><em>Distractor Traps:</em><br>&bull; B (Severe Neurotoxic Error): Semantic priming does not induce permanent long-term depression or suppress V1 simple cell contour extraction.<br>&bull; C (Pathological Misattribution): Reading words does not cause excitotoxic dopamine surges or induce auditory hallucinations in healthy participants.<br>&bull; D (Physiological Nonsense): Retinal ganglion lateral inhibition enhances edge contrast, but does not physically reshape external photon waves."
    },
    {
      "q": "How does the \"Carpentered World Hypothesis\" explain cross-cultural variations in susceptibility to geometric visual illusions like the M&uuml;ller-Lyer illusion?",
      "ch": [
        "Genetic polymorphisms in retinal opsins alter photopigment absorption among rural populations.",
        "Living in rural environments eliminates binocular retinal disparity and depth accommodation.",
        "Lifelong exposure to rectangular architecture creates perceptual sets for interpreting corners.",
        "Non-Western individuals experience congenital apperceptive visual agnosias from poor nutrition."
      ],
      "a": 2,
      "e": "<strong>The Carpentered World Hypothesis and cultural perceptual sets:</strong> The Carpentered World Hypothesis (Segall, Campbell, & Herskovits) explains why people living in industrialized Western societies are far more susceptible to the Müller-Lyer illusion (two identical lines ending in inward-pointing vs. outward-pointing arrowheads appearing to be different lengths) than individuals from non-industrialized rural cultures. Westerners grow up in a \"carpentered world\" dominated by rectilinear architecture, right angles, and rectangular walls. In this environment, humans develop a strong perceptual set: an arrowhead pointing outward represents an outside corner that is closer to the viewer, while an inward-pointing arrowhead represents an inside corner that is farther away. In rural cultures with circular huts and few right angles, this perceptual set is not reinforced, making people virtually immune to the illusion.<br><br><em>Distractor Traps:</em><br>&bull; A (Biological Fallacy): Susceptibility to geometric illusions is culturally and experientially mediated, not dictated by retinal cone opsin genetics.<br>&bull; B (Physiological Contradiction): Retinal disparity and accommodation are universal binocular physiological processes, intact in all sighted human populations.<br>&bull; D (Offensive/Pathological Misattribution): Healthy individuals in non-industrial societies do not suffer from brain damage or agnosias."
    },
    {
      "q": "In Table 1, why did Cohort 2 (12-hour fasted, animal prime) exhibit the longest categorization latency (585 ms) and an evenly split categorization rate (46.8% vs 53.2%)?",
      "ch": [
        "Fasting triggered hypoglycemia that produced acute bilateral occipital lobe cellular necrosis.",
        "Top-down semantic animal priming clashed with bottom-up motivational food drive, causing conflict.",
        "Animal prime words actively fatigued language comprehension networks located within Broca's area.",
        "Signal detection sensitivity ($d'$) dropped to zero because participants fell asleep during testing."
      ],
      "a": 1,
      "e": "<strong>Cognitive conflict between motivational drive and contextual priming:</strong> In Cohort 2, participants were subject to two competing, antagonistic top-down forces: their internal physiological state (12-hour fasting) generated a powerful motivational bias to detect food items, while the external experimental context (animal-related prime words) primed animal schemas. Because these two top-down influences exerted opposing pulls on the ambiguous sensory data, participants experienced high cognitive conflict and decision uncertainty. Resolving this interference required additional cognitive processing time, resulting in the longest response latency (585 ms) and an evenly divided categorization rate (46.8% food vs. 53.2% animal).<br><br><em>Distractor Traps:</em><br>&bull; A (Extreme Medical Exaggeration): An overnight 12-hour fast does not cause occipital lobe infarction or brain tissue necrosis.<br>&bull; C (Incorrect Functional Anatomy): Semantic prime words do not induce neural fatigue in Broca's motor speech area.<br>&bull; D (False Assertion): Healthy awake subjects in a controlled 150 ms tachistoscopic task do not fall asleep or exhibit zero sensitivity."
    },
    {
      "q": "How does acute fear or emotional arousal establish a rapid perceptual set that prioritizes the detection of threatening stimuli like snakes or angry faces?",
      "ch": [
        "By permanently suppressing parasympathetic vagal nerve tone across all peripheral viscera.",
        "By inducing immediate dark adaptation through rapid bilateral pupillary constriction (miosis).",
        "By routing visual signals through a fast subcortical colliculo-pulvinar-amygdalar pathway.",
        "By blocking dorsal stream spatial calculations to concentrate visual attention entirely on V1."
      ],
      "a": 2,
      "e": "<strong>Subcortical \"low road\" and threat-related perceptual set:</strong> Joseph LeDoux and colleagues demonstrated that visual information travels via two distinct routes: a cortical \"high road\" (retina $\\rightarrow$ LGN $\\rightarrow$ V1 $\\rightarrow$ ventral stream $\\rightarrow$ amygdala) that is slow, detailed, and conscious, and a subcortical \"low road\" (retina $\\rightarrow$ superior colliculus $\\rightarrow$ pulvinar nucleus of the thalamus $\\rightarrow$ amygdala) that is rapid, crude, and automatic. Acute emotional arousal or threat primes this subcortical pathway, allowing low-spatial-frequency threat cues (such as the silhouette of a snake or an aggressive facial expression) to trigger amygdala activation within ~50 ms. The amygdala then sends widespread neuromodulatory feedback to sensory cortices, establishing an immediate perceptual set that biases visual attention toward danger.<br><br><em>Distractor Traps:</em><br>&bull; A (Irrelevant Peripheral Autonomics): Vagal nerve modulation affects heart rate and digestion, but does not directly establish sensory perceptual sets in visual pathways.<br>&bull; B (Physiological Inversion): Sympathetic fear arousal triggers pupillary dilation (mydriasis, via radial dilator muscle), not constriction (miosis).<br>&bull; D (Incorrect Functional Anatomy): The dorsal stream is vital for calculating spatial location and escape trajectories, not blocked during fear."
    }
  ]
}
