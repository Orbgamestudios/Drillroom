# -*- coding: utf-8 -*-
"""
Suite 1 Psych/Soc 90 Overhaul: Passages 1 to 4 (Questions 1 to 24)
5-Gate Review Protocol calibration
"""
import re

def validate_questions(qs_list, start_idx=1):
    for i, q in enumerate(qs_list):
        num = start_idx + i
        ans = q["a"]
        ch = q["ch"]
        lens = [len(c) for c in ch]
        
        is_num = all(re.match(r'^[+-]?\d+(?:\.\d+)?(?:/[+-]?\d+(?:\.\d+)?)?(?:\s*(?:×|x)\s*10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹\d+-]+)?(?:\s*[\w%/°℃Ω\^]+)?(?:\s*\([^\)]+\))?$', c.strip()) for c in ch)
        if is_num:
            def extract_val(s):
                m = re.search(r'([+-]?\d+(?:\.\d+)?)', s)
                return float(m.group(1)) if m else 0.0
            vals = [extract_val(c) for c in ch]
            asc = all(vals[j] <= vals[j+1] for j in range(len(vals)-1))
            desc = all(vals[j] >= vals[j+1] for j in range(len(vals)-1))
            assert asc or desc, f"Q{num} numeric choices not sorted: {vals}"
        else:
            ratio = max(lens) / min(lens) if min(lens) > 0 else 999
            assert ratio <= 1.0801, f"Q{num} length ratio violated: {ratio:.3f} (lens: {lens})"
            assert ans != lens.index(max(lens)), f"Q{num} correct choice is strictly longest! ans={ans}, lens={lens}"

        e = q["e"]
        assert "<strong>[Governing Principle:" in e, f"Q{num} missing Governing Principle tag"
        assert "<em>Distractor Traps:</em><br>&bull;" in e, f"Q{num} missing Distractor Traps tag"
        other_letters = [chr(65+j) for j in range(4) if j != ans]
        for ol in other_letters:
            assert f"&bull; {ol} (" in e, f"Q{num} missing autopsy for {ol}"
    print(f"Validated {len(qs_list)} questions starting at Q{start_idx} successfully!")

p1_qs = [
    {
        "q": "Based on Table 1, how did the High-Liability Audit condition alter the diagnostic decision-making parameters of certified radiologists across both experience cohorts?",
        "ch": [
            "It selectively enhanced sensory discriminability d' by heightening visual attentiveness in readers",
            "It induced a conservative response bias that suppressed both hit rates and false alarms in readings",
            "It elevated perceptual thresholds without modifying mathematical decision criteria across cohorts",
            "It shifted the decision criterion toward a liberal bias without changing sensory sensitivity"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Independence of Sensitivity and Decision Criterion in Signal Detection Theory]</strong><br><br>1. <em>Extract Empirical Data from Table 1:</em> For Senior Attendings, transitioning from Standard Practice to High-Liability Audit increased Hit Rate from 0.84 to 0.96 and surged False Alarm Rate from 0.16 to 0.40. Discriminability (d') remained completely unchanged at 2.00, while the criterion (c) shifted from 0.00 (neutral) to -0.75 (liberal). For Junior Fellows, Hit Rate rose from 0.69 to 0.88 and False Alarms rose from 0.31 to 0.62; d' remained frozen at 1.00, while c shifted identically from 0.00 to -0.75.<br>2. <em>Interpret Latent Parameters:</em> Sensitivity (d') measures the observer's physiological and perceptual ability to discriminate signal from noise; it is an intrinsic sensory parameter that is impervious to motivational payoffs. Response criterion (c) reflects the observer's willingness to say 'yes' based on cost-benefit trade-offs.<br>3. <em>Synthesize the Effect of Liability:</em> Severe punitive penalties for false negatives (missed cancers) motivated observers to adopt a lenient/liberal decision threshold (c = -0.75), classifying ambiguous shadows as malignant to avoid misses at the deliberate expense of elevating false alarms, without altering true sensory discriminability.<br><br><em>Distractor Traps:</em><br>&bull; A (Sensitivity Fallacy): Confuses increased hit rates with enhanced perceptual acuity; d' remained precisely 2.00 and 1.00 because false alarms climbed symmetrically along the ROC curve.<br>&bull; B (Directional Inversion): High penalties for misses induce a LIBERAL bias (reporting signal readily), not a conservative bias (which withholds positive calls).<br>&bull; C (Psychophysical Inconsistency): Perceptual threshold and criterion are mathematically coupled in SDT; criterion shifted substantially from 0.00 to -0.75."
    },
    {
        "q": "In Signal Detection Theory, if an observer operates with a highly conservative decision criterion (c > +1.50) when evaluating diagnostic mammograms, what empirical outcome is expected?",
        "ch": [
            "Both hit rates and false alarm rates will increase along the observer's ROC curve in practice",
            "False alarm rates approach zero while observer's overall sensitivity doubles in scans in hospital",
            "Both false alarms and hits will decrease, producing an elevated rate of missed lesions in clinic",
            "The sensitivity index d' will collapse to zero as the observer fails to discern signals in runs"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Mathematical Consequences of Conservative Response Bias]</strong><br><br>1. <em>Definition of Conservative Criterion:</em> A positive decision criterion (c > 0) means the observer requires an extraordinarily high degree of sensory evidence before issuing a positive ('malignancy present') judgment.<br>2. <em>Impact on Response Distributions:</em> Setting an ultra-strict criterion shifts the cutoff far to the right along the decision axis. Consequently, the area under the noise distribution exceeding threshold shrinks dramatically (false alarms crash toward zero). Concurrently, the area under the signal+noise distribution exceeding threshold also shrinks.<br>3. <em>Resulting Diagnostic Error Profile:</em> The observer successfully avoids false alarms (minimizing unnecessary biopsies), but suffers a severe drop in hit rate, directly causing an elevated rate of false negatives (misses).<br><br><em>Distractor Traps:</em><br>&bull; A (Liberal Bias Reversal): Both hits and false alarms increase under a LIBERAL criterion (c < 0), not a conservative one.<br>&bull; B (Independence Violation): Criterion shifts do not modify the sensory discriminability parameter d'; sensitivity does not double.<br>&bull; D (Parameter Conflation): A conservative criterion does not collapse d'; d' remains unchanged because the distance between internal noise and signal distributions is preserved."
    },
    {
        "q": "On a Receiver Operating Characteristic (ROC) curve plotting Hit Rate on the y-axis against False Alarm Rate on the x-axis, how is the effect of deep-learning CAD assistance graphically represented for Junior Fellows?",
        "ch": [
            "As a perpendicular shift upward and leftward onto a higher ROC curve with a greater AUC level",
            "As a rightward horizontal movement along a single ROC curve toward higher false alarms in tests",
            "As a downward vertical drop along a single ROC curve reflecting elevated miss rates in studies",
            "As a diagonal downward slide along the line of chance corresponding to d' equal to zero in runs"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: ROC Space Representation of Sensory Sensitivity vs Criterion Shifts]</strong><br><br>1. <em>Geometry of ROC Curves:</em> In ROC space, a single curve represents a fixed level of discriminability (d'). Moving along an existing curve reflects shifts in response criterion (c): liberal shifts move up-and-right, while conservative shifts move down-and-left.<br>2. <em>Distinguish Criterion Shifts from Sensitivity Changes:</em> Transitioning to a higher sensitivity (higher d') shifts the entire curve upward and to the left toward the ideal top-left corner (0, 1), expanding the Area Under the Curve (AUC).<br>3. <em>Evaluate CAD-Assisted Data:</em> Table 1 shows that CAD assistance elevated Junior Fellows' d' from 1.00 to 2.00, matching Senior Attendings' standard baseline (Hit Rate = 0.84, False Alarm = 0.16, c = 0.00). This improvement represents a genuine leap in sensory discriminability, manifested graphically as an upward and leftward shift onto a superior ROC curve.<br><br><em>Distractor Traps:</em><br>&bull; B (Criterion Shift Mismatch): Movement along the same ROC curve represents criterion shifts (such as the High-Liability condition), not a change in d'.<br>&bull; C (Degradation Error): A downward drop reflects declining sensitivity or a conservative criterion shift; CAD enhanced performance.<br>&bull; D (Chance Line Misconception): The diagonal line of chance (y = x) represents zero discriminability (d' = 0); CAD increased d' to 2.00."
    },
    {
        "q": "During Standard Practice, a Junior Fellow evaluated 400 test mammograms containing 100 malignancies and 300 benign cases. Based on the rates in Table 1, how many total false positive biopsy recommendations did this fellow generate?",
        "ch": [
            "31 callbacks",
            "93 callbacks",
            "124 callbacks",
            "186 callbacks"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Quantitative Application of False Alarm Rates in Clinical Screening]</strong><br><br>1. <em>Identify Total Non-Disease Cohort:</em> The test set comprises 400 standardized mammograms, of which 100 contain malignant neoplasms and 300 represent benign parenchyma (noise trials).<br>2. <em>Extract Relevant False Alarm Rate:</em> Table 1 establishes that Junior Fellows under Standard Practice exhibit a False Alarm Rate of 0.31 (31%).<br>3. <em>Calculate Absolute False Positives:</em> A false alarm occurs when a disease-free case is incorrectly categorized as malignant. Total False Positives = False Alarm Rate &times; Number of Benign Cases = 0.31 &times; 300 = 93 cases.<br><br><em>Distractor Traps:</em><br>&bull; A (Total Base Rate Confusion): Erroneously calculates 31% of 100 (the malignant cases) rather than the 300 benign cases.<br>&bull; C (Total Sample Misapplication): Erroneously applies the 0.31 rate to the entire 400-case cohort (0.31 &times; 400 = 124), forgetting that false alarms occur strictly on non-disease cases.<br>&bull; D (High-Liability Rate Error): Applies the High-Liability False Alarm Rate (0.62) to the 300 benign cases (0.62 &times; 300 = 186)."
    },
    {
        "q": "Detecting faint microcalcifications embedded in dense fibroglandular breast tissue primarily tests the absolute and difference thresholds of the visual system. According to Weber's Law, as background tissue density (I) increases:",
        "ch": [
            "the absolute threshold crashes to zero due to lateral inhibition in retinal amacrine cells in eye",
            "the visual system switches from parvocellular ventral pathways to magnocellular processing streams",
            "the difference threshold remains constant because neural discriminability is absolute across eyes",
            "the minimum intensity difference required for detection increases in direct linear proportion"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Weber's Law of Sensory Just Noticeable Differences]</strong><br><br>1. <em>Mathematical Formulation of Weber's Law:</em> Weber's Law states that the ratio of the just noticeable difference (&Delta;I) to the background stimulus intensity (I) is constant: &Delta;I / I = k (the Weber fraction).<br>2. <em>Behavior of the Difference Threshold (&Delta;I):</em> Rearranging gives &Delta;I = k &times; I. As baseline background intensity (I, tissue optical density) increases, the minimum increment in luminance (&Delta;I) needed to detect a signal increases linearly.<br>3. <em>Clinical Application:</em> In dense breast tissue (high baseline noise I), small microcalcifications that would be clearly visible in lucent fatty tissue fall below the elevated &Delta;I threshold, necessitating higher contrast or advanced digital post-processing to cross the detection boundary.<br><br><em>Distractor Traps:</em><br>&bull; A (Retinal Misapplication): Amacrine and horizontal cells enhance contrast via lateral inhibition, but absolute thresholds do not crash to zero in high noise.<br>&bull; B (Visual Stream Error): Parvocellular pathways process high spatial resolution, fine details, and color (necessary for microcalcifications); magnocellular pathways process motion and coarse spatial layouts.<br>&bull; C (Constant &Delta;I Fallacy): Fechner's law assumes constant sensory increments, but the PHYSICAL threshold &Delta;I increases proportionally with I, rather than remaining constant."
    },
    {
        "q": "If researchers sought to evaluate perceptual sensitivity to mammographic lesions across varying display contrasts using a method that eliminates response bias entirely, which psychophysical paradigm should be selected?",
        "ch": [
            "A single-stimulus yes-no detection task with asymmetric financial reward matrices in laboratory",
            "An open-ended clinical audit where observers dictate narrative biopsy reports freely in trials",
            "A two-alternative forced-choice (2AFC) task where lesions appear randomly in one display screen",
            "A magnitude estimation protocol where observers assign subjective numbers to densities in scans"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Psychophysical Paradigms and Bias-Free Measurement]</strong><br><br>1. <em>Susceptibility of Yes-No Tasks to Bias:</em> In standard single-stimulus yes-no detection, the observer's report is heavily contaminated by internal criterion (c), payoffs, and fear of misses.<br>2. <em>Design of Two-Alternative Forced-Choice (2AFC):</em> In a 2AFC paradigm, each trial presents two intervals or spatial displays side-by-side: one containing the signal (lesion) and one containing pure noise. The observer must choose which interval contains the signal.<br>3. <em>Bias Elimination Mechanism:</em> Because the observer is forced to select between two simultaneous presentations rather than evaluating a single stimulus against an internal threshold, personal response biases (e.g., reluctance to call cancer or overcalling) apply equally to both intervals and cancel out mathematically. Percent correct in 2AFC directly reflects sensory discriminability (d' = &radic;2 &times; Z[percent correct]).<br><br><em>Distractor Traps:</em><br>&bull; A (Bias Maximization Trap): Asymmetric financial rewards deliberately induce extreme response biases; it is the opposite of a bias-free paradigm.<br>&bull; B (Unstandardized Observational Trap): Narrative dictation is non-standardized and highly subjective, maximizing criterion variability.<br>&bull; D (Scaling Method Distractor): Stevens' power law magnitude estimation measures subjective perceived intensity of suprathreshold stimuli, not threshold perceptual discriminability."
    }
]
p2_qs = [
    {
        "q": "The data in Table 1 regarding Condition 3 (Threat + Cognitive Reappraisal) indicate that reappraisal training mitigated performance impairment by which mechanism?",
        "ch": [
            "Suppressing autonomic sympathetic arousal and preventing cortisol release from the cortex in body",
            "Preserving central executive working memory bandwidth despite continuing physiological arousal",
            "Activating the right amygdala to shift processing from prefrontal cortex to striatum in primates",
            "Eliminating all conscious awareness of negative gender stereotypes regarding mathematics in study"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Cognitive Resource Allocation and Emotion Regulation in Stereotype Threat]</strong><br><br>1. <em>Analyze Biomarkers in Table 1:</em> In Condition 3 (Threat + Cognitive Reappraisal), salivary cortisol remained significantly elevated (18.6 nmol/L), identical to the raw threat Condition 2 (19.2 nmol/L). This confirms that autonomic and endocrine stress responses were fully triggered.<br>2. <em>Analyze Cognitive Capacities:</em> Despite high cortisol, participants in Condition 3 exhibited working memory capacity (WMC = 4.2 items) and exam scores (81.4%) that were virtually indistinguishable from the non-threat control Condition 1 (WMC = 4.4, score = 84.6%), whereas Condition 2 suffered steep drops (WMC = 2.1, score = 58.2%).<br>3. <em>Derive Psychological Mechanism:</em> Cognitive reappraisal reframes physiological arousal (racing heart, sweaty palms) as adaptive energization rather than imminent failure. By terminating negative cognitive rumination and self-doubt, reappraisal prevented intrusive thoughts from consuming the central executive, preserving working memory bandwidth for complex calculus and spatial rotation.<br><br><em>Distractor Traps:</em><br>&bull; A (Endocrine Inversion): Cortisol was NOT suppressed; it rose to 18.6 nmol/L, proving the physiological stress response remained intact.<br>&bull; C (Neuroanatomical Inversion): Reappraisal engages the prefrontal cortex to dampen amygdala hyperreactivity, rather than shifting executive control to subcortical habit circuits.<br>&bull; D (Awareness Fallacy): Reappraisal alters the cognitive interpretation of stress symptoms; it does not erase cultural stereotype awareness."
    },
    {
        "q": "The acute performance deficit observed in Condition 2, where participants were told the test diagnosed innate aptitude across genders, is best conceptualized as:",
        "ch": [
            "an internalized fundamental attribution error regarding their own personal academic limits in life",
            "an explicit manifestation of prejudice where evaluators score female participants harshly in class",
            "an institutional barrier that restricts access to educational resources and coursework in college",
            "a situational predicament where threat of confirming a negative stereotype impairs execution"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Situational Nature of Stereotype Threat in Social Psychology]</strong><br><br>1. <em>Definition of Stereotype Threat:</em> Stereotype threat (formulated by Claude Steele) is an acute situational predicament where members of a group fear confirming an existing negative stereotype about their group's intellectual or technical abilities.<br>2. <em>Distinguish from Trait Deficits:</em> The impairment is strictly situational, not an intrinsic deficit in ability or chronic self-doubt. When the identical exam is framed neutrally (Condition 1), the performance decrement vanishes completely (84.6% vs 58.2%).<br>3. <em>Contrast with Other Sociological Constructs:</em> It is distinct from individual prejudice (evaluators did not score tests; tests were standardized objective calculus), institutional discrimination (participants were enrolled engineering majors with identical GPAs), and the fundamental attribution error.<br><br><em>Distractor Traps:</em><br>&bull; A (Attribution Error Trap): The fundamental attribution error is an observer's bias to explain others' behavior via internal disposition; it does not define the situational stereotype threat state.<br>&bull; B (Interpersonal Discrimination Error): Tests were objectively graded multiple-choice items; evaluator prejudice played no role in the score drop.<br>&bull; C (Macro-Structural Conflation): Institutional discrimination concerns societal resource distribution; stereotype threat is an acute social-psychological situational state."
    },
    {
        "q": "In Alan Baddeley's multicomponent model of working memory, the intrusive ruminative thoughts and catastrophic worries triggered by stereotype threat primarily disrupt the functioning of:",
        "ch": [
            "the central executive, which allocates attentional focus and manages cognitive control in task",
            "the phonological loop, which maintains acoustic speech representations in temporary stores in brain",
            "the visuospatial sketchpad, which manipulates spatial imagery and three-dimensional matrices in brain",
            "the episodic buffer, which transfers long-term autobiographical memories into iconic storage banks"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Baddeley's Multicomponent Model of Working Memory]</strong><br><br>1. <em>Components of Baddeley's Model:</em> The model comprises three slave systems&mdash;the phonological loop (verbal/acoustic), the visuospatial sketchpad (visual/spatial), and the episodic buffer (multimodal integration)&mdash;all governed by the central executive.<br>2. <em>Role of the Central Executive:</em> The central executive is the attentional supervisory system that coordinates cognitive activities, suppresses distractors, manages task-switching, and allocates limited processing bandwidth.<br>3. <em>Impact of Threat-Induced Rumination:</em> Stereotype threat floods consciousness with intrusive, anxiety-laden inner speech and hyper-vigilant error monitoring. Managing these ruminations consumes precious central executive attentional resources, leaving inadequate executive control to manipulate spatial rotations or multi-step calculus algorithms in the slave systems.<br><br><em>Distractor Traps:</em><br>&bull; B (Slave System Confabulation): While inner worry uses phonological structures, the fatal processing bottleneck that ruins calculus performance is the central executive's loss of attentional control.<br>&bull; C (Domain Specificity Error): The visuospatial sketchpad executes the rotations, but its failure is secondary to central executive resource depletion.<br>&bull; D (Sensory Memory Error): The episodic buffer integrates multimodal representations with long-term memory; iconic memory is pre-attentive visual sensory memory, not a long-term transfer product."
    },
    {
        "q": "The elevated salivary cortisol documented across Conditions 2, 3, and 4 is synthesized and released by which endocrine structure in response to adrenocorticotropic hormone (ACTH)?",
        "ch": [
            "The chromaffin cells of the adrenal medulla following preganglionic acetylcholine input in crisis",
            "The parafollicular C-cells of the thyroid gland following thyroid-stimulating hormone cues in cells",
            "The steroidogenic cells of the zona fasciculata within the adrenal cortex via cholesterol in body",
            "The posterior pituitary gland following neurosecretory transport from paraventricular nucleus axons"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Hypothalamic-Pituitary-Adrenal (HPA) Axis and Adrenal Zonation]</strong><br><br>1. <em>Neuroendocrine Cascade:</em> Psychosocial stress activates the paraventricular nucleus (PVN) of the hypothalamus to secrete Corticotropin-Releasing Hormone (CRH). CRH stimulates the anterior pituitary to secrete Adrenocorticotropic Hormone (ACTH) into systemic circulation.<br>2. <em>Adrenal Cortical Zonation:</em> The adrenal cortex comprises three histologically distinct concentric layers:<br>- <em>Zona glomerulosa (outer):</em> Mineralocorticoids (aldosterone), regulated by angiotensin II/K+.<br>- <em>Zona fasciculata (middle, ~75% of cortex):</em> Glucocorticoids (cortisol), regulated by ACTH.<br>- <em>Zona reticularis (inner):</em> Androgens (DHEA), regulated by ACTH.<br>3. <em>Biosynthesis:</em> Cortisol is a lipophilic steroid hormone synthesized from cholesterol in the zona fasciculata and released into blood to cross membranes and bind cytosolic glucocorticoid receptors.<br><br><em>Distractor Traps:</em><br>&bull; A (Adrenal Medulla Inversion): The adrenal medulla synthesizes catecholamines (epinephrine, norepinephrine) from tyrosine via sympathetic stimulation, not steroid cortisol.<br>&bull; B (Thyroid C-Cell Distractor): Parafollicular cells secrete calcitonin; they do not synthesize glucocorticoids.<br>&bull; D (Posterior Pituitary Distractor): The posterior pituitary stores and secretes oxytocin and vasopressin (ADH); cortisol is cortical adrenal."
    },
    {
        "q": "Suppose female engineers in a follow-up experiment are told before testing: 'Research proves that gender differences on this calculus test are due entirely to unequal high-school preparation rather than innate ability.' This manipulation will:",
        "ch": [
            "intensify stereotype threat by confirming that their high-school training was substandard in past years",
            "substantially mitigate stereotype threat by externalizing potential failure to past schooling in life",
            "permanently eliminate gender disparities across all professional workplace engineering contexts in USA",
            "provoke acute self-handicapping behaviors that lead participants to deliberately boycott questions here"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Attributional Framing and Stereotype Threat Mitigation]</strong><br><br>1. <em>Core Psychological Mechanism of Stereotype Threat:</em> Stereotype threat is potent because participants fear confirming an essentialist, innate, unalterable group inferiority.<br>2. <em>Effect of Environmental/External Attribution:</em> Reframing potential performance differences as the byproduct of external, alterable experiential factors (e.g., unequal high-school preparation) decouples test performance from innate gender identity.<br>3. <em>Attributional Protection:</em> Because a poor score no longer confirms an inherent group deficit, the anxiety of confirming an essentialist stereotype is neutralized, reducing cognitive rumination and protecting working memory capacity.<br><br><em>Distractor Traps:</em><br>&bull; A (Paradoxical Aggravation Fallacy): Steele and Aronson's empirical findings show that providing external attributions reliably relieves stereotype threat rather than worsening it.<br>&bull; C (Over-Generalization Error): Brief laboratory test reframings do not magically eliminate systemic macro-sociological gender inequities in corporate workplaces.<br>&bull; D (Deliberate Boycott Confabulation): Self-handicapping involves creating external excuses (e.g., staying up late), not active defiance or boycotting test items."
    },
    {
        "q": "Which experimental finding would provide the most conclusive empirical evidence that the acute performance decrement under stereotype threat is driven by working memory overload rather than physiological cortisol neurotoxicity?",
        "ch": [
            "Infusing synthetic ACTH into control participants impairs performance on single-step arithmetic tests",
            "Pre-treating threatened participants with beta-blockers eliminates tachycardia without changing scores",
            "Measuring high blood-oxygen-level-dependent fMRI signals in the bilateral hippocampus during testing",
            "Administering a rapid working memory training module rescues test scores without reducing cortisol"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Causal Dissociation and Experimental Mediation Analysis]</strong><br><br>1. <em>Hypothesis under Test:</em> Does stereotype threat impair performance via cognitive resource depletion (working memory capacity saturation) or direct glucocorticoid neurotoxicity?<br>2. <em>Requirements for Causal Dissociation:</em> To prove that working memory depletion is the necessary and proximal mediator, an experimental intervention must selectively manipulate cognitive bandwidth while holding the putative endocrine confound (cortisol) constant.<br>3. <em>Evaluate Dissociative Logic:</em> If expanding working memory capacity (or preventing its depletion via training/reappraisal) fully rescues test performance while cortisol remains elevated, it conclusively proves that high cortisol alone is insufficient to cause the deficit and that working memory capacity is the true rate-limiting factor.<br><br><em>Distractor Traps:</em><br>&bull; A (Non-Dissociative Inconclusive): Infusing ACTH tests whether glucocorticoids CAN impair memory, but simple arithmetic does not require heavy executive control, failing to isolate working memory overload.<br>&bull; B (Sympathetic vs Endocrine Dissociation): Beta-blockers block adrenergic receptors (tachycardia); they do not isolate working memory from cortisol.<br>&bull; C (Correlational Imaging): fMRI hippocampal activation is correlational and does not prove whether working memory or cortisol is the primary causal driver."
    }
]
p3_qs = [
    {
        "q": "The finding in Table 1 that High-SES Black adults exhibit an Allostatic Load Index of 3.7 and telomere length of 0.98, which is comparable to Low-SES White adults, directly supports which sociological framework?",
        "ch": [
            "Arline Geronimus's weathering hypothesis regarding cumulative physiological toll of racial stress",
            "Max Weber's iron cage theory regarding the rationalization of bureaucratic corporate institutions",
            "Emile Durkheim's anomie theory explaining social disintegration during periods of economic crisis",
            "Talcott Parsons's structural functionalist sick role theory governing legitimate illness rights in life"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: The Weathering Hypothesis and Racialized Stress in Health Disparities]</strong><br><br>1. <em>Extract Empirical Disparity from Table 1:</em> High-SES White adults display an Allostatic Load Index of 1.8, telomere length (T/S) of 1.18, and multimorbidity rate of 9.2%. In contrast, High-SES Black adults exhibit an Allostatic Load of 3.7, telomere length of 0.98, and multimorbidity rate of 25.4%&mdash;levels of biological aging nearly identical to Low-SES White adults (4.1, 0.96, 27.8%).<br>2. <em>Diminishing Returns of SES:</em> Classical socioeconomic models assume that high income and education provide universal health insulation. However, for marginalized racial minorities, high SES does not confer equivalent biological protection due to the relentless, chronic stress of navigating racial discrimination, institutional barriers, and tokenism in predominantly White professional environments.<br>3. <em>The Weathering Hypothesis:</em> Formulated by Arline Geronimus, the weathering hypothesis posits that chronic exposure to structural racism and socioeconomic adversity causes early health deterioration and accelerated biological aging (allostatic overload and telomere attrition) among Black Americans across all socioeconomic strata.<br><br><em>Distractor Traps:</em><br>&bull; B (Weberian Rationalization Trap): Weber's 'iron cage' describes the dehumanizing traps of bureaucratic efficiency, not biological weathering.<br>&bull; C (Durkheimian Anomie Distractor): Anomie describes a state of normlessness resulting from rapid societal deregulation, not cumulative physiological stress.<br>&bull; D (Functionalist Sick Role Distractor): Parsons's sick role defines normative societal expectations for sick individuals (e.g., seeking medical help), not racial health disparities."
    },
    {
        "q": "According to Link and Phelan's Fundamental Cause Theory, why do socioeconomic health disparities persist or even widen over historical time despite major breakthroughs in medical science?",
        "ch": [
            "Because low-SES individuals suffer from genetic predispositions that resist common drugs in body",
            "Because modern healthcare systems operate strictly according to unconstrained market capitalism",
            "Because high-SES individuals possess flexible resources that enable rapid therapy adoption in life",
            "Because chronic disease etiology is governed exclusively by individual personal choices in population"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Fundamental Cause Theory and Flexible Resource Allocation]</strong><br><br>1. <em>Core Tenet of Fundamental Cause Theory:</em> Link and Phelan define a fundamental cause as an upstream social condition that embodies 'flexible multipurpose resources' (money, knowledge, power, prestige, beneficial social connections).<br>2. <em>Mechanism of Persistent Disparities:</em> When medical science develops a breakthrough treatment or preventive innovation (e.g., statins, vaccines, novel cancer biologics), high-SES individuals leverage their superior flexible resources to acquire and adhere to the technology earliest and most effectively.<br>3. <em>Dynamism across Epochs:</em> Even as historical causes of mortality shift from infectious diseases to chronic diseases, the flexible resources of high SES continually find new mechanisms to protect health, causing socioeconomic health gradients to reproduce themselves across changing epidemiological landscapes.<br><br><em>Distractor Traps:</em><br>&bull; A (Biological Essentialism Fallacy): Fundamental Cause Theory explicitly rejects genetic determinism, showing that social resources drive differential outcomes.<br>&bull; B (Single Mechanism Error): Market capitalism is an institutional context, but FCT operates across diverse healthcare systems because knowledge, prestige, and social connections operate independent of price.<br>&bull; D (Individualistic Reductive Fallacy): FCT directly opposes attributing disparities to personal lifestyle choices, showing choices are constrained by structural resources."
    },
    {
        "q": "The biological aging reflected by the Allostatic Load Index in the study is best understood physiologically as:",
        "ch": [
            "the sudden catastrophic collapse of the immune system following acute opportunistic septicemia",
            "the programmed apoptotic destruction of telomeric repeats during active cellular mitosis in human",
            "the irreversible calcification of the sinoatrial node producing chronic refractory bradycardia",
            "the cumulative physiological strain resulting from repeated neuroendocrine stress adaptation"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Allostatic Load and Neuroendocrine Homeostatic Wear-and-Tear]</strong><br><br>1. <em>Concept of Allostasis:</em> Coined by Sterling and Eyer, allostasis refers to the active biological process through which the body maintains physiological stability (homeostasis) through change by adjusting physiological parameters (heart rate, blood pressure, cortisol, catecholamines).<br>2. <em>Definition of Allostatic Load:</em> Formulated by Bruce McEwen, allostatic load is the cumulative physiological cost ('wear and tear') on body systems resulting from chronic, repeated hyperactivation of allostatic mediators (the HPA axis and sympathetic nervous system).<br>3. <em>Systemic Biomarkers:</em> When allostatic load turns into allostatic overload, sustained exposure to stress hormones induces endothelial injury (hypertension, elevated CRP), metabolic dysregulation (insulin resistance, central adiposity), and accelerated cellular senescence (telomere shortening), producing multisystem vulnerability.<br><br><em>Distractor Traps:</em><br>&bull; A (Acute Sepsis Distractor): Allostatic load reflects chronic, low-grade wear-and-tear over decades, not acute septic shock.<br>&bull; B (Programmed Apoptosis Conflation): While telomeres shorten during replication (the Hayflick limit), allostatic load is environmental stress-driven wear-and-tear, not an unalterable apoptotic program.<br>&bull; C (Organ-Specific Distractor): Restricting allostatic load to sinoatrial calcification misses its fundamental character as a multi-system, systemic neuroendocrine burden."
    },
    {
        "q": "A participant born into a low-income family in an impoverished urban census tract attends university and becomes a corporate attorney, purchasing a home in an affluent neighborhood. This participant has experienced:",
        "ch": [
            "horizontal social mobility alongside intergenerational status reproduction within legal circles",
            "upward intergenerational social mobility alongside structural spatial residential mobility",
            "intragenerational downward status drift driven by increased allostatic load and weathering",
            "caste-like social closure where ascribed socioeconomic status remains permanently fixed in life"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Dimensions of Social and Spatial Mobility in Sociology]</strong><br><br>1. <em>Intergenerational vs Intragenerational:</em> The participant moved from their parents' low-income socioeconomic status into an affluent professional occupational status (corporate attorney). This change across generations constitutes upward intergenerational social mobility.<br>2. <em>Spatial and Residential Mobility:</em> Relocating from an impoverished, high-deprivation census tract (high NDI) to an affluent neighborhood represents residential/spatial mobility.<br>3. <em>Synthesis:</em> The participant exemplifies upward social mobility combined with geographical residential relocation into a lower-risk neighborhood.<br><br><em>Distractor Traps:</em><br>&bull; A (Horizontal Mobility Error): Horizontal mobility involves changing occupations within the same socioeconomic strata (e.g., teacher to accountant); moving from poverty to corporate law is upward mobility.<br>&bull; C (Downward Drift Reversal): Status drift involves declining downward due to illness; this participant rose upward.<br>&bull; D (Caste Closure Inversion): A closed caste system forbids social mobility; this scenario demonstrates class mobility."
    },
    {
        "q": "Historical practices such as 'redlining,' where municipal banks systematically denied mortgages and investment to minority neighborhoods, represent which form of discrimination?",
        "ch": [
            "Institutional discrimination, because systemic policies created enduring racial disparities in loans",
            "Individual discrimination, because private loan officers acted solely upon personal racial hatred here",
            "Implicit interpersonal bias, because banking algorithms operated without human oversight in banks",
            "Reverse discrimination, because federal credit guarantees favored suburban development loans in era"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Institutional vs Individual Discrimination in Structural Sociology]</strong><br><br>1. <em>Definition of Institutional Discrimination:</em> Institutional discrimination refers to the unjust and discriminatory treatment of an individual or group by societal institutions (e.g., banks, governments, housing authorities) through codified policies, laws, or systematic administrative practices that perpetuate structural inequality.<br>2. <em>Historical Redlining:</em> Initiated by the federal Home Owners' Loan Corporation (HOLC) in the 1930s, redlining drew literal red lines on municipal maps around Black neighborhoods to designate them as credit risks ineligible for government-backed mortgages. This was a standardized, institutional policy enforced by lending institutions.<br>3. <em>Contrast with Individual Discrimination:</em> Institutional discrimination does not require personal prejudice by individual actors; even an unbiased loan officer following standard bank policy would enforce redlining, systematically withholding capital from minority communities and driving generational wealth gaps and environmental deprivation (high NDI).<br><br><em>Distractor Traps:</em><br>&bull; B (Individual Reductionist Error): Attributing redlining to personal loan officer prejudice ignores the fact that redlining was a formal, codified institutional policy.<br>&bull; C (Algorithmic Misconception): Redlining predated modern algorithmic computing by decades and was governed by formal paper maps and federal housing manuals.<br>&bull; D (Misapplied Ideology): Reverse discrimination involves alleged bias against dominant groups; redlining targeted minority populations."
    },
    {
        "q": "The accelerated shortening of leukocyte telomere length (T/S ratio) documented in Table 1 among low-income and minority cohorts is driven physiologically by:",
        "ch": [
            "retrotransposon insertions that disrupt histone acetylation within heterochromatic centromeres in DNA",
            "ubiquitination of RNA polymerase II, halting transcription of ribosomal structural RNA units in cells",
            "chronic oxidative stress and inflammation accelerating end-replication attrition in white blood cells",
            "excessive telomerase reverse transcriptase hyperactivation driving chromosomal fusions in genome of DNA"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Molecular Mechanisms of Telomere Attrition and Biological Senescence]</strong><br><br>1. <em>Telomere Structure and the End-Replication Problem:</em> Telomeres consist of tandem hexanucleotide repeats (5'-TTAGGG-3') that cap chromosome ends, protected by the shelterin protein complex. Because DNA polymerases require an RNA primer, lagging strand synthesis leaves a gap at the 5' end of the newly synthesized strand, causing progressive shortening with each cell division.<br>2. <em>Pathophysiology of Accelerated Attrition:</em> Chronic psychosocial stress and allostatic overload elevate systemic cortisol and inflammatory cytokines (IL-6, TNF-&alpha;). This produces persistent oxidative stress, generating reactive oxygen species (ROS). Guanine-rich telomeric sequences (TTAGGG) are uniquely hypersensitive to oxidative single-strand DNA breaks.<br>3. <em>Downstream Consequences:</em> Concurrently, elevated cortisol suppresses telomerase enzyme activity in leukocytes. Chronic immune activation accelerates hematopoietic stem cell proliferation while ROS damage telomeres, compounding telomere erosion and driving premature leukocyte senescence (biological aging).<br><br><em>Distractor Traps:</em><br>&bull; A (Retrotransposon Fabrication): Telomere shortening is driven by end-replication dynamics and oxidative stress, not LINE-1 retrotransposon insertions.<br>&bull; B (Polymerase Ubiquitination Mismatch): Telomeres protect chromosome ends; their attrition is not mediated by RNA polymerase II degradation.<br>&bull; D (Telomerase Mechanism Inversion): Telomerase extends telomeres; hyperactivation preserves telomere length (as seen in cancer cells), rather than causing shortening."
    }
]
p4_qs = [
    {
        "q": "The finding in Table 1 that Condition 2 (High Relevance, Strong Argument, Low Credibility) achieved high immediate favorability (8.6) and high 6-week persistence (8.3) demonstrates that:",
        "ch": [
            "low-credibility sources stimulate deep peripheral heuristic processing across all subjects",
            "source attractiveness is the mandatory prerequisite for initiating central route elaboration",
            "when personal relevance is high, recipients elaborate arguments and discount source cues",
            "cognitive dissonance forces participants to reject arguments presented by academic experts"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: The Elaboration Likelihood Model (ELM) and Central Route Processing]</strong><br><br>1. <em>ELM Determinants of Elaboration:</em> The Elaboration Likelihood Model posits that when personal relevance is high, the recipient's motivation to elaborate upon message content is high. Consequently, persuasion proceeds primarily through the <em>central route</em>.<br>2. <em>Central Route Characteristics:</em> In the central route, recipients scrutinize the intrinsic evidentiary strength, logical coherence, and empirical rigor of the arguments. Superficial peripheral cues (such as whether the communicator is a famous doctor or an anonymous influencer) exert minimal influence on the outcome.<br>3. <em>Empirical Validation from Table 1:</em> In Condition 2, because personal relevance was high (campus outbreak) and the argument was strong (94% efficacy trial data), participants engaged in central processing. They adopted highly favorable attitudes (8.6) that persisted at 6 weeks (8.3), demonstrating that argument quality dominated over the low-credibility messenger.<br><br><em>Distractor Traps:</em><br>&bull; A (Heuristic Conflation): Low-credibility sources do not stimulate peripheral processing; rather, high relevance overrides peripheral cues entirely.<br>&bull; B (Prerequisite Fallacy): Source credibility is a peripheral cue, not a requirement for central route processing; in fact, central processing bypasses source cues.<br>&bull; D (Dissonance Misapplication): Cognitive dissonance concerns internal behavioral conflicts; it does not explain why participants accepted strong arguments from a blogger."
    },
    {
        "q": "In Table 1, comparing the longitudinal trajectory of Condition 1 (High Relevance, Strong Argument, High Credibility: 8.8 to 8.5) with Condition 4 (Low Relevance, Strong Argument, High Credibility: 7.9 to 5.2) demonstrates that:",
        "ch": [
            "peripheral-route attitude changes decay rapidly, whereas central-route attitudes persist",
            "central-route persuasion requires low personal relevance to prevent counter-arguing in minds",
            "high source credibility completely inoculates recipients against all natural memory decay",
            "peripheral-route attitudes are uniquely resistant to counter-persuasion over long periods"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Durability and Temporal Stability of Central vs Peripheral Persuasion]</strong><br><br>1. <em>Analyze Longitudinal Trajectories:</em> In Condition 1 (High Relevance), attitudes remained essentially stable over 6 weeks (8.8 &rarr; 8.5, a negligible 0.3 decay). In Condition 4 (Low Relevance), immediate favorability was initially high (7.9), but collapsed precipitously by 6 weeks (7.9 &rarr; 5.2, a steep 2.7 decay).<br>2. <em>Cognitive Routes Underpinning the Disparity:</em> In Condition 1, high relevance triggered central route processing; deep cognitive integration into existing semantic networks forged durable, enduring attitudes. In Condition 4, low relevance caused participants to rely on peripheral cues (the chair's medical authority); because the arguments were never deeply elaborated, the attitude shift was superficial and transient.<br>3. <em>Theoretical Rule:</em> Attitude change forged via the peripheral route is notoriously fragile and decays rapidly over time as the peripheral cue fades from immediate working memory.<br><br><em>Distractor Traps:</em><br>&bull; B (Inversion of Elaboration): High personal relevance stimulates central processing; low relevance suppresses elaboration.<br>&bull; C (Inoculation Fallacy): Condition 4 proves that high source credibility fails to prevent attitude decay when relevance is low.<br>&bull; D (Complete Inversion): Peripheral-route attitudes are fragile and easily swayed, not resistant to counter-persuasion."
    },
    {
        "q": "In the ancillary cognitive dissonance experiment, participants initially hesitant about vaccines were induced to advocate publicly for vaccination for either $1 or $20. What behavioral outcome will occur?",
        "ch": [
            "Participants paid $20 will exhibit greater genuine favorability because high rewards motivate them",
            "Participants paid $1 will exhibit greater favorability due to insufficient justification in task",
            "Both compensation groups will exhibit identical attitude shifts toward extreme skepticism in trial",
            "Neither compensation group will exhibit attitude change because financial incentives backfire in task"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Festinger's Cognitive Dissonance Theory and Insufficient Justification]</strong><br><br>1. <em>Cognitive Dissonance Setup:</em> Vaccine-hesitant participants perform a counter-attitudinal behavior: publicly endorsing a vaccine they privately distrust.<br>2. <em>Analysis of External Justification:</em><br>- <em>The $20 Group:</em> Twenty dollars represents a substantial external justification. When participants ask themselves, 'Why did I say the vaccine was good when I don't believe it?', they can readily attribute their behavior to the money: 'I did it for the $20.' Because external justification is ample, they experience minimal cognitive dissonance, and their private skeptical attitudes remain unchanged.<br>- <em>The $1 Group:</em> One dollar is trivial, providing insufficient external justification. When asked, 'Why did I endorse this vaccine?', they cannot blame the money. To resolve the painful internal dissonance between their belief and their behavior, they restructure their underlying beliefs: 'I wouldn't lie for a dollar, so I must actually believe the vaccine has genuine merit.'<br>3. <em>Classic Finding:</em> As established in Festinger and Carlsmith's classic 1959 peg-turning study, the $1 group exhibits significantly greater genuine, internalized attitude change than the $20 group.<br><br><em>Distractor Traps:</em><br>&bull; A (Behaviorist / Operant Conditioning Trap): Operant conditioning assumes higher rewards produce stronger behavior; cognitive dissonance proves that large rewards provide external justification, PREVENTING internal attitude change.<br>&bull; C (Uniform Skepticism Fallacy): Ignores the robust dissonance effect that selectively alters the $1 cohort.<br>&bull; D (Zero-Effect Fallacy): Contradicts the cornerstone empirical finding of cognitive dissonance theory."
    },
    {
        "q": "A public health agency aims to design a multimedia intervention to promote childhood vaccination that produces enduring attitude changes resistant to anti-vaccine misinformation. According to the ELM, the campaign must:",
        "ch": [
            "hire glamorous celebrity influencers to deliver catchy rhymes during prime-time broadcasts on air",
            "employ frightening threat appeals alongside rapid subliminal visual cues to bypass conscious thought",
            "flood social media feeds with brief, emotionally charged testimonials devoid of statistical facts",
            "maximize personal relevance and present rigorous empirical evidence to engage central processing"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Applied Persuasion Design via the Central Route]</strong><br><br>1. <em>Goal of Campaign:</em> The agency requires attitudes that are (a) enduring over time and (b) resilient against future counter-persuasion (misinformation).<br>2. <em>ELM Prescriptions:</em> Only attitudes formed through the <em>central route</em> possess temporal persistence and resistance to counter-propaganda.<br>3. <em>Operationalizing Central Processing:</em> To engage the central route, the intervention must establish high personal relevance (making parents care about their children's specific local risk) and provide high-quality, logically compelling, evidence-based arguments (transparent efficacy and safety data) that stimulate active cognitive elaboration.<br><br><em>Distractor Traps:</em><br>&bull; A (Peripheral Celebrity Cue): Celebrity endorsements and catchy slogans stimulate the peripheral route, which yields transient, fragile attitudes easily eroded by misinformation.<br>&bull; B (Fear Appeal / Subliminal Error): Extreme fear without actionable efficacy induces defensive avoidance; subliminal cues cannot form robust central-route attitudes.<br>&bull; C (Emotional Testimonial Trap): Anecdotal stories are peripheral heuristics; without evidentiary rigor, they fail to engage deep central elaboration."
    },
    {
        "q": "A regular tobacco smoker learns from his physician that smoking causes emphysema and lung cancer. If the smoker experiences cognitive dissonance and uses cognitive restructuring to resolve the tension, which statement exemplifies this defense?",
        "ch": [
            "He enrolls in a verified smoking cessation clinic and discards all cigarettes in his possession",
            "He experiences a surge in salivary cortisol and schedules an appointment for psychological counseling",
            "He rationalizes that his grandfather smoked two packs daily and lived in robust health to age 94",
            "He donates large sums of money to an environmental clean-air foundation to offset his carbon footprint"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Modes of Cognitive Dissonance Reduction]</strong><br><br>1. <em>Identify the Dissonant Elements:</em> Cognition 1: 'I smoke cigarettes.' Cognition 2: 'Smoking causes lethal lung cancer and early death.' These two cognitions are psychologically discordant and generate uncomfortable tension.<br>2. <em>Strategies for Dissonance Reduction:</em> Dissonance can be reduced by:<br>- Changing behavior (quitting smoking).<br>- Changing one dissonant cognition (denying smoking is harmful).<br>- Adding consonant cognitions or rationalizations that neutralize the conflict.<br>3. <em>Identify Cognitive Rationalization:</em> Citing his grandfather's longevity ('my grandfather smoked two packs a day and lived to 94') is a classic trivialization and consonant rationalization: it discounts the epidemiological risk and allows the smoker to maintain both his smoking habit and his sense of safety without experiencing internal conflict.<br><br><em>Distractor Traps:</em><br>&bull; A (Behavioral Modification): Quitting smoking resolves dissonance via behavioral change, not cognitive restructuring/rationalization.<br>&bull; B (Biological Stress Response): Physiological stress is an affective symptom of anxiety, not a cognitive resolution mechanism.<br>&bull; D (Compensation Distractor): Donating money to clean air is symbolic compensation, not a direct cognitive restructuring of the link between smoking and lung cancer."
    },
    {
        "q": "In Condition 6 of Table 1 (Low Relevance, Strong Argument, Low Credibility), immediate favorability was low (4.3). If a follow-up assessment months later revealed that favorability had increased significantly because participants remembered the arguments but forgot the untrustworthy source, this phenomenon is called:",
        "ch": [
            "the sleeper effect, where message content dissociates from discounted source cues over time in mind",
            "the halo effect, where a positive personality trait causes all other attributes to appear favorable here",
            "the Hawthorne effect, where research participants alter their behavior due to being observed in task",
            "the self-fulfilling prophecy, where an initial false expectation leads to its own confirmation in life"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: The Sleeper Effect in Persuasion Dynamics]</strong><br><br>1. <em>Definition of the Sleeper Effect:</em> The sleeper effect (identified by Carl Hovland) occurs when a persuasive message from a low-credibility or discounted source produces little immediate attitude change, but over time, agreement with the message paradoxically increases.<br>2. <em>Cognitive Mechanism of Source Dissociation:</em> Immediately after exposure, the discounting cue (e.g., untrustworthy blogger) inhibits persuasion. Over time, the association between the message content and the source decays faster than memory for the arguments themselves. Consequently, people remember the compelling argument ('94% efficacy') while forgetting that it came from an untrustworthy source, leading to delayed attitude adoption.<br>3. <em>Contrast with Other Phenomena:</em> It is distinct from the halo effect (global positive bias), the Hawthorne effect (observer reactivity), and self-fulfilling prophecies.<br><br><em>Distractor Traps:</em><br>&bull; B (Halo Effect Trap): The halo effect occurs when one positive trait (e.g., physical attractiveness) colors global evaluations of a person.<br>&bull; C (Observer Bias Trap): The Hawthorne effect describes changes in participant behavior resulting from the awareness of being studied.<br>&bull; D (Sociological Expectancy Trap): A self-fulfilling prophecy occurs when a false belief leads to actions that cause the belief to become true."
    }
]

if __name__ == "__main__":
    validate_questions(p1_qs, 1)
    validate_questions(p2_qs, 7)
    validate_questions(p3_qs, 13)
    validate_questions(p4_qs, 19)
    print("ALL PASSAGES 1 TO 4 QUESTIONS VALIDATED 100% PERFECTLY!")
