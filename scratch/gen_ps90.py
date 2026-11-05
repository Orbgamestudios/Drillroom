import json

# ==============================================================================
# PASSAGE 1: Signal Detection Theory in Radiology Mammography
# ==============================================================================
p1_html = """<div class="ttl">Passage 1 (Questions 1&ndash;6)</div>
<p>Screening mammography requires radiologists to discern faint microcalcifications and subtle architectural parenchymal distortions (signal) against dense, heterogeneous fibroglandular stroma (noise). Signal Detection Theory (SDT) models such perceptual decisions by isolating two independent latent parameters: sensory discriminability (sensitivity index, <i>d&prime;</i>) and response bias (decision criterion, <i>c</i> or &beta;). Sensitivity reflects physiological visual acuity and neural processing efficiency, calculated as <i>d&prime;</i> = <i>Z</i>(Hit Rate) &minus; <i>Z</i>(False Alarm Rate). In contrast, the decision criterion reflects an observer's internal threshold for reporting a signal, influenced by prior probabilities, expected payoffs, and error penalties.</p>
<p>To examine the impact of clinical experience and institutional liability incentives on diagnostic accuracy, investigators presented 400 standardized digital mammograms (100 confirmed malignant neoplasms, 300 verified benign parenchyma) to certified radiologists. Observers were stratified by experience: Junior Fellows (&lt;2 years post-residency) and Senior Attendings (&gt;10 years subspecialty practice). Each group read the test set under two conditions:</p>
<ul>
  <li><b>Standard Practice:</b> Observers evaluated cases under normal clinical parameters with neutral incentive instructions.</li>
  <li><b>High-Liability Audit:</b> Observers were instructed that false negative readings (misses) would incur a 10-fold regulatory and medico-legal audit penalty relative to false positive callbacks.</li>
  <li><b>CAD-Assisted:</b> A third condition was administered to Junior Fellows, where deep-learning computer-aided detection (CAD) algorithms highlighted suspicious regions of interest on the digital images.</li>
</ul>
<table>
<tr><th>Observer Cohort</th><th>Condition</th><th>Hit Rate (Sensitivity)</th><th>False Alarm Rate</th><th>Discriminability (<i>d&prime;</i>)</th><th>Decision Criterion (<i>c</i>)</th></tr>
<tr><td>Senior Attendings</td><td>Standard Practice</td><td class="n">0.84</td><td class="n">0.16</td><td class="n">2.00</td><td class="n">0.00</td></tr>
<tr><td>Senior Attendings</td><td>High-Liability Audit</td><td class="n">0.96</td><td class="n">0.40</td><td class="n">2.00</td><td class="n">&minus;0.75</td></tr>
<tr><td>Junior Fellows</td><td>Standard Practice</td><td class="n">0.69</td><td class="n">0.31</td><td class="n">1.00</td><td class="n">0.00</td></tr>
<tr><td>Junior Fellows</td><td>High-Liability Audit</td><td class="n">0.88</td><td class="n">0.62</td><td class="n">1.00</td><td class="n">&minus;0.75</td></tr>
<tr><td>Junior Fellows</td><td>CAD-Assisted</td><td class="n">0.84</td><td class="n">0.16</td><td class="n">2.00</td><td class="n">0.00</td></tr>
</table>
<p class="cap"><b>Table 1</b> Signal detection parameters across experimental conditions. Note: <i>c</i> = 0 denotes neutral criterion, <i>c</i> &lt; 0 denotes liberal/lenient bias, and <i>c</i> &gt; 0 denotes conservative bias.</p>"""

p1_qs = [
    {
        "q": "According to Table 1, the high-liability audit condition influenced diagnostic decisions across both observer cohorts primarily by:",
        "ch": [
            "increasing sensory discriminability (d&prime;) to compensate for heightened diagnostic scrutiny.",
            "shifting the decision criterion (c) in the liberal direction without altering sensory discriminability (d&prime;).",
            "shifting the decision criterion (c) in the conservative direction to minimize unnecessary recalls.",
            "selectively depressing the false alarm rate while holding the hit rate invariant."
        ],
        "a": 1,
        "e": "<strong>Incentive matrices alter decision criteria without changing sensory sensitivity.</strong> In both Attendings and Fellows, shifting from Standard Practice to High-Liability Audit decreased <em>c</em> from 0.00 to &minus;0.75 (a liberal shift, lowering the threshold to report malignancy), which elevated Hit Rate at the expense of substantially more False Alarms. Discriminability (<em>d&prime;</em>) remained exactly constant (2.00 for Attendings, 1.00 for Fellows). Trap A assumes high motivation sharpens sensory vision; Trap C inverts liberal and conservative criteria; Trap D contradicts the observed elevation in false alarms."
    },
    {
        "q": "In Signal Detection Theory, an observer operating with a highly conservative decision criterion (<i>c</i> &gt; 0 or &beta; &gt; 1) will typically demonstrate:",
        "ch": [
            "a high hit rate accompanied by a high false alarm rate.",
            "a low false alarm rate accompanied by an increased miss rate.",
            "a substantial increase in d&prime; independent of sensory background noise.",
            "an equal probability of committing type I and type II classification errors."
        ],
        "a": 1,
        "e": "<strong>Conservative criteria require overwhelming evidence before signaling 'yes.'</strong> A conservative observer (<em>c</em> &gt; 0) sets a stringent evidentiary threshold, minimizing False Alarms (saying 'tumor' when none exists) but inevitably causing a high Miss rate (failing to detect existing tumors, lowering Hit Rate). Choice A describes a liberal criterion (<em>c</em> &lt; 0). Choice C conflates criterion with sensory discriminability. Choice D is false because a biased criterion skews error types asymmetric to one another."
    },
    {
        "q": "On a Receiver Operating Characteristic (ROC) curve plotting Hit Rate (y-axis) versus False Alarm Rate (x-axis), how is the transition from Standard Practice to CAD-Assisted reading in Junior Fellows graphically represented?",
        "ch": [
            "A shift of the operating point downward and to the right along a single existing curve",
            "A shift of the operating point upward and to the right along a single existing curve",
            "An outward shift of the entire curve toward the upper-left corner, increasing the area under the curve",
            "A downward collapse of the curve toward the diagonal line of chance performance"
        ],
        "a": 2,
        "e": "<strong>Changes in d&prime; alter the ROC curve itself, whereas changes in criterion move along the curve.</strong> CAD assistance elevated the Fellows' discriminability index from <em>d&prime;</em> = 1.00 to <em>d&prime;</em> = 2.00 while maintaining a neutral criterion (<em>c</em> = 0.00). An increase in <em>d&prime;</em> expands the area under the curve (AUC), shifting the entire curve toward the top-left vertex (100% hits, 0% false alarms). In contrast, choices A and B describe criterion shifts along a fixed ROC curve."
    },
    {
        "q": "During the Standard Practice condition, a Junior Fellow evaluated the complete 400-case mammography dataset (100 malignant, 300 benign). Based on the rates in Table 1, how many total mammograms were classified as &ldquo;normal / benign&rdquo; by this fellow?",
        "ch": [
            "93",
            "207",
            "238",
            "300"
        ],
        "a": 2,
        "e": "<strong>Account for both Misses and Correct Rejections:</strong><br>For 100 malignant cases: Hit Rate = 0.69 &rArr; 69 Hits, leaving 31 Misses (classified as normal).<br>For 300 benign cases: False Alarm Rate = 0.31 &rArr; 93 False Alarms, leaving 300 &minus; 93 = 207 Correct Rejections (classified as normal).<br>Total mammograms classified as normal = 31 Misses + 207 Correct Rejections = 238 images. Trap B (207) ignores false negatives (misses); Trap A (93) is the number of false alarms."
    },
    {
        "q": "Detecting fine, punctate microcalcifications embedded in dense breast parenchyma requires high visual acuity and fine spatial resolution. This visual information is predominantly transduced by:",
        "ch": [
            "peripheral rod photoreceptors projecting through the magnocellular pathway.",
            "foveal cone photoreceptors projecting through the parvocellular pathway.",
            "retinal ganglion cells projecting directly to the superior colliculus.",
            "amacrine interneurons modulating horizontal receptive fields in the optic chiasm."
        ],
        "a": 1,
        "e": "<strong>The parvocellular ('P') pathway mediates high-resolution color and fine detail.</strong> Cones concentrated in the fovea centralis possess small receptive fields and 1:1 ganglion cell convergence, routing through the parvocellular layers of the lateral geniculate nucleus (LGN) to process static spatial detail. The magnocellular ('M') pathway (Choice A) specializes in motion and transient luminance. The superior colliculus (Choice C) controls reflexive saccades, not conscious high-acuity discrimination."
    },
    {
        "q": "If researchers sought to evaluate perceptual sensitivity to mammographic lesions while experimentally eliminating subjective response bias (criterion variability), which psychophysical methodology should they employ?",
        "ch": [
            "Method of limits with ascending signal intensities",
            "Two-alternative forced-choice (2AFC) task",
            "Unconstrained magnitude estimation protocol",
            "Continuous single-interval yes/no detection paradigm"
        ],
        "a": 1,
        "e": "<strong>Two-alternative forced-choice (2AFC) designs neutralize response criteria.</strong> In a 2AFC paradigm, observers view two side-by-side or sequential images (one containing a lesion, one normal) and must select which interval contains the signal. Because observers merely compare the two sensory impressions rather than setting an arbitrary internal boundary for 'tumor vs no tumor,' criterion bias is mathematically minimized or eliminated. A yes/no paradigm (Choice D) is precisely what is susceptible to criterion shifts."
    }
]

# ==============================================================================
# PASSAGE 2: Stereotype Threat, Working Memory, and Cortisol Biomarkers
# ==============================================================================
p2_html = """<div class="ttl">Passage 2 (Questions 7&ndash;12)</div>
<p>Stereotype threat is an acute psychosocial state characterized by heightened apprehension that one's performance will confirm a negative stereotype about one's social group. According to cognitive resource models, stereotype threat imposes an extraneous cognitive load on working memory capacity (WMC): intrusive worries about failure and active monitoring of performance consume the attentional bandwidth of the central executive. Simultaneously, psychological distress stimulates the hypothalamic-pituitary-adrenal (HPA) axis, elevating glucocorticoids that can disrupt prefrontal synaptic plasticity.</p>
<p>To evaluate these psychophysiological pathways, researchers recruited 160 female undergraduate engineering majors with comparable baseline mathematics GPA. Participants were randomized into four experimental conditions prior to completing a standardized 30-item spatial rotation and advanced calculus examination:</p>
<ul>
  <li><b>Condition 1 (Neutral Control):</b> The examination was introduced as a &ldquo;problem-solving task to evaluate the clarity of test items.&rdquo;</li>
  <li><b>Condition 2 (Stereotype Threat):</b> The examination was explicitly introduced as a &ldquo;diagnostic test of innate visuospatial and mathematical engineering aptitude across gender groups.&rdquo;</li>
  <li><b>Condition 3 (Threat + Cognitive Reappraisal):</b> Participants received the identical threat prime as Condition 2, but were instructed that physiological arousal (e.g., racing pulse, sweating) is an adaptive bodily response that mobilizes cognitive energy and enhances focus.</li>
  <li><b>Condition 4 (Threat + Working Memory Preload):</b> Participants received the threat prime while concurrently performing a continuous phonological loop suppression task (rehearsing random 6-letter consonant strings during test items).</li>
</ul>
<p>Investigators measured test accuracy, automated Operation-Span (O-SPAN) working memory score (0&ndash;60), salivary free cortisol elevation from baseline (&Delta;Cortisol, nmol/L), and intrusive thought frequency using intermittent retrospective probes (1&ndash;7 Likert scale).</p>
<table>
<tr><th>Condition</th><th>Test Score (%)</th><th>O-SPAN Score</th><th>&Delta;Cortisol (nmol/L)</th><th>Intrusive Thoughts</th></tr>
<tr><td>1: Neutral Control</td><td class="n">81.4</td><td class="n">47.2</td><td class="n">+0.6</td><td class="n">1.9</td></tr>
<tr><td>2: Stereotype Threat</td><td class="n">62.1</td><td class="n">32.5</td><td class="n">+4.8</td><td class="n">5.7</td></tr>
<tr><td>3: Threat + Reappraisal</td><td class="n">79.5</td><td class="n">45.1</td><td class="n">+4.6</td><td class="n">2.2</td></tr>
<tr><td>4: Threat + Preload</td><td class="n">51.8</td><td class="n">24.3</td><td class="n">+5.1</td><td class="n">5.9</td></tr>
</table>
<p class="cap"><b>Table 1</b> Cognitive performance and physiological markers across experimental cohorts.</p>"""

p2_qs = [
    {
        "q": "The data in Table 1 regarding Condition 3 (Threat + Cognitive Reappraisal) most directly indicate that:",
        "ch": [
            "cognitive reappraisal completely inhibits HPA axis activation, preventing cortisol release.",
            "reappraisal preserves executive working memory and test accuracy by suppressing intrusive thoughts despite sustained physiological arousal.",
            "reappraisal eliminates the cognitive vulnerability of the phonological loop to concurrent verbal load.",
            "arousal reappraisal converts stereotype threat into a self-fulfilling prophecy."
        ],
        "a": 1,
        "e": "<strong>Cognitive reappraisal decouples physiological arousal from cognitive impairment.</strong> In Condition 3, &Delta;Cortisol remained substantially elevated (+4.6 nmol/L, nearly identical to Condition 2's +4.8 nmol/L), proving the physiological stress response was not silenced. However, intrusive thoughts dropped from 5.7 to 2.2, rescuing O-SPAN (45.1) and test performance (79.5%) back toward control levels. This proves reappraisal alters the cognitive interpretation of somatic arousal, buffering executive working memory."
    },
    {
        "q": "The acute performance decline observed in Condition 2 is best categorized as stereotype threat rather than a self-fulfilling prophecy because:",
        "ch": [
            "the performance impairment was caused by an external evaluator's biased behavior directly altering participant actions.",
            "the impairment was driven by an internal cognitive-affective process triggered by situational stereotype salience, without requiring interpersonal interaction.",
            "the participants held a conscious, deep-seated belief in their group's innate mathematical inferiority prior to the experiment.",
            "the decline was solely mediated by peripheral neuromuscular fatigue rather than cognitive processing."
        ],
        "a": 1,
        "e": "<strong>Stereotype threat is an internal cognitive state; self-fulfilling prophecy is an interpersonal cycle.</strong> Stereotype threat occurs when awareness of a negative stereotype induces situational anxiety and working memory depletion in the individual, even without anyone treating them poorly. A self-fulfilling prophecy requires an external perceiver whose preconceived expectations lead them to treat the target differently, which in turn causes the target to confirm the original expectation. Pre-existing internal endorsement of the stereotype (Choice C) is not required for stereotype threat."
    },
    {
        "q": "In Baddeley's multicomponent model of working memory, the intrusive ruminative thoughts reported by participants in Condition 2 primarily deplete the resources of the:",
        "ch": [
            "episodic buffer, preventing the retrieval of long-term procedural motor programs.",
            "visuospatial sketchpad, directly degrading basic photoreceptor transduction.",
            "phonological loop, by causing mechanical paralysis of the subvocal articulatory rehearsal apparatus.",
            "central executive, restricting its capacity to direct attention and manage strategic problem solving."
        ],
        "a": 3,
        "e": "<strong>Intrusive worries deplete the central executive's attentional capacity.</strong> The central executive is responsible for focusing attention, switching cognitive sets, inhibiting task-irrelevant ruminations, and allocating processing resources to subordinate slave systems. Intrusive evaluative worries hijack central executive control, leaving insufficient bandwidth for solving complex multi-step calculus problems."
    },
    {
        "q": "The elevated salivary cortisol observed in Conditions 2, 3, and 4 is synthesized and released through which neuroendocrine cascade?",
        "ch": [
            "CRH from the hypothalamus &rarr; ACTH from the anterior pituitary &rarr; Cortisol from the adrenal cortex",
            "GnRH from the hypothalamus &rarr; LH from the posterior pituitary &rarr; Cortisol from the adrenal medulla",
            "TRH from the anterior pituitary &rarr; TSH from the hypothalamus &rarr; Cortisol from the thyroid gland",
            "Epinephrine from the adrenal medulla &rarr; ACTH from the anterior pituitary &rarr; Cortisol from the adrenal cortex"
        ],
        "a": 0,
        "e": "<strong>HPA axis cascade: CRH &rarr; ACTH &rarr; Cortisol.</strong> Psychosocial stress prompts the paraventricular nucleus of the hypothalamus to secrete Corticotropin-Releasing Hormone (CRH) into the hypophyseal portal system. CRH stimulates corticotropes in the anterior pituitary to release Adrenocorticotropic Hormone (ACTH) into systemic circulation, which binds MC2 receptors in the zona fasciculata of the adrenal cortex to stimulate cortisol synthesis. The adrenal medulla synthesizes catecholamines (epinephrine/norepinephrine), not glucocorticoids."
    },
    {
        "q": "Suppose that in a follow-up experiment, female engineers are told before testing that &ldquo;women consistently demonstrate superior multi-angle spatial reasoning compared to men.&rdquo; If their scores rise significantly above the neutral control baseline, this phenomenon is termed:",
        "ch": [
            "stereotype threat.",
            "stereotype lift.",
            "the bystander effect.",
            "fundamental attribution error."
        ],
        "a": 1,
        "e": "<strong>Stereotype lift (or stereotype boost) is a performance boost from positive stereotypes.</strong> When awareness of an in-group positive stereotype (or an out-group negative stereotype) enhances self-efficacy, lowers evaluative anxiety, and improves cognitive performance above baseline, it is known as stereotype lift/boost. Stereotype threat refers exclusively to the performance deficit."
    },
    {
        "q": "Which experimental result would provide the strongest evidence that the performance drop in Condition 2 was mediated by working memory depletion rather than low generalized task motivation?",
        "ch": [
            "Participants in Condition 2 spent more time persisting on unsolvable math items than Control participants.",
            "Condition 2 participants exhibited impaired performance on high-working-memory math tasks but completely preserved performance on automatic, retrieval-based arithmetic.",
            "Condition 2 participants reported identical levels of self-efficacy compared to Condition 1 participants.",
            "Condition 2 participants showed a flat line on pupillometry dilation throughout the examination."
        ],
        "a": 1,
        "e": "<strong>Selective impairment of high-WMC tasks isolates executive working memory load.</strong> If low motivation were the cause, performance would drop uniformly across all tasks, whether simple or complex. Preserved performance on automatic, well-rehearsed arithmetic (which does not depend on central executive working memory) paired with deficits restricted to novel, complex spatial tasks (which strictly demand WMC) proves that working memory bandwidth—not effort or motivation—was the critical limiting factor."
    }
]

# Write out Passage 1 and 2 tests
print("Passages 1 & 2 defined.")

# ==============================================================================
# PASSAGE 3: Fundamental Cause Theory, Residential Segregation, and Weathering
# ==============================================================================
p3_html = """<div class="ttl">Passage 3 (Questions 13&ndash;18)</div>
<p>Epidemiological research consistently identifies a robust socioeconomic status (SES) gradient across morbidity and all-cause mortality. Link and Phelan's <i>Fundamental Cause Theory</i> (FCT) posits that SES operates as a fundamental cause because it encompasses flexible, multipurpose resources&mdash;including wealth, knowledge, prestige, power, and beneficial social connections&mdash;that allow individuals to avoid biological risks and adopt protective health behaviors regardless of which proximate disease mechanisms or medical treatments predominate in a particular era.</p>
<p>Concurrently, Arline Geronimus proposed the <i>Weathering Hypothesis</i>, asserting that chronic, cumulative exposure to structural socioeconomic disadvantage and institutionalized racism imposes continuous physiological stress, resulting in accelerated biological aging and premature health deterioration among marginalized racial groups. This wear-and-tear is clinically quantified as <i>allostatic load</i>, representing the systemic dysregulation of cardiovascular, metabolic, and neuroendocrine homeostatic systems. Furthermore, racial residential segregation reinforces these disparities by concentrating environmental toxins, substandard housing, and food deserts within disinvested municipalities.</p>
<p>A 25-year prospective cohort study tracked 1,600 non-Hispanic Black and non-Hispanic White adults from age 20 to 45. Participants were categorized by educational attainment and household income into Low-SES or High-SES strata. At age 45, investigators assessed:</p>
<ul>
  <li><b>Allostatic Load Index (ALI):</b> A composite score (0&ndash;10) evaluating 10 physiological biomarkers: systolic and diastolic blood pressure, waist-to-hip ratio, fasting serum glucose, HbA1c, total/HDL cholesterol ratio, resting pulse, serum C-reactive protein (CRP), and overnight urinary cortisol and norepinephrine.</li>
  <li><b>Leukocyte Telomere Length (LTL):</b> Quantified as the telomere-to-single-copy-gene ratio (T/S ratio) via quantitative PCR, serving as a cellular biomarker of biological senescence.</li>
  <li><b>Multimorbidity Rate:</b> Proportion of participants diagnosed with &ge;2 chronic conditions (e.g., essential hypertension, type 2 diabetes, coronary artery disease).</li>
  <li><b>Neighborhood Deprivation Index (NDI):</b> Standardized census-tract measure of spatial segregation, poverty density, and commercial food availability (scale 1.0&ndash;5.0, where 5.0 denotes maximum deprivation).</li>
</ul>
<table>
<tr><th>Demographic Cohort</th><th>SES Category</th><th>Allostatic Load Index (0&ndash;10)</th><th>Mean Telomere Length (T/S)</th><th>Multimorbidity Rate (%)</th><th>Mean NDI</th></tr>
<tr><td>White Adults</td><td>High SES</td><td class="n">1.8</td><td class="n">1.18</td><td class="n">9.2</td><td class="n">1.4</td></tr>
<tr><td>White Adults</td><td>Low SES</td><td class="n">4.1</td><td class="n">0.96</td><td class="n">27.8</td><td class="n">3.1</td></tr>
<tr><td>Black Adults</td><td>High SES</td><td class="n">3.7</td><td class="n">0.98</td><td class="n">25.4</td><td class="n">2.7</td></tr>
<tr><td>Black Adults</td><td>Low SES</td><td class="n">6.3</td><td class="n">0.76</td><td class="n">47.2</td><td class="n">4.5</td></tr>
</table>
<p class="cap"><b>Table 1</b> Biomarkers of biological aging and health outcomes at chronological age 45.</p>"""

p3_qs = [
    {
        "q": "The finding in Table 1 that High-SES Black adults have an Allostatic Load Index (3.7) and multimorbidity rate (25.4%) comparable to Low-SES White adults (4.1 and 27.8%) provides the strongest empirical evidence against which theoretical premise?",
        "ch": [
            "The weathering hypothesis of cumulative physiological wear-and-tear",
            "A purely income-reductionist model asserting that racial health disparities are entirely explained by differences in socioeconomic resources",
            "The concept that chronic psychosocial stressors alter autonomic homeostatic setpoints",
            "Fundamental Cause Theory's premise that flexible resources confer health advantages"
        ],
        "a": 1,
        "e": "<strong>Racial disparities persist across identical socioeconomic strata due to structural racism.</strong> If health disparities were solely an artifact of income and educational differences (a pure economic determinism model), High-SES Black individuals would exhibit allostatic load and morbidity rates identical to High-SES White individuals. Instead, High-SES Black adults experience biological weathering on par with Low-SES White adults, demonstrating that racialized social stressors, discrimination, and residential segregation exert an independent, toxic effect on physiology that high income cannot fully eliminate."
    },
    {
        "q": "According to Link and Phelan's Fundamental Cause Theory, if medical science develops a revolutionary gene therapy that completely eliminates mortality from coronary artery disease, what pattern will most likely emerge across socioeconomic strata?",
        "ch": [
            "The mortality gap between High-SES and Low-SES populations will permanently close.",
            "Low-SES populations will adopt the therapy first due to disproportionate disease burden.",
            "High-SES populations will rapidly access and benefit from the therapy, reproducing the relative mortality gradient.",
            "Health disparities will invert, causing higher allostatic load among wealthy individuals."
        ],
        "a": 2,
        "e": "<strong>Fundamental causes reproduce disparities by monopolizing new protective resources.</strong> Fundamental Cause Theory emphasizes that when new medical innovations, technologies, or health information emerge, high-SES individuals leverage their flexible resources (money, health literacy, insurance coverage, professional connections) to obtain early and complete access. Consequently, health gradients persist or widen even as the overall burden of specific diseases shifts."
    },
    {
        "q": "The biological aging reflected by the Allostatic Load Index in the study is best understood physiologically as:",
        "ch": [
            "acute, reversible sympathetic activation that resolves without long-term anatomical changes.",
            "the cumulative pathological cost of chronic neuroendocrine and autonomic adaptations to persistent psychosocial stressors.",
            "an inevitable genetic program of cellular senescence entirely detached from environmental adversity.",
            "a protective downregulation of basal metabolic rate to conserve somatic glycogen reserves."
        ],
        "a": 1,
        "e": "<strong>Allostatic load represents cumulative multisystem physiological strain.</strong> While allostasis is the adaptive process of maintaining stability (homeostasis) through physiological or behavioral change, allostatic load is the 'wear-and-tear' resulting from chronic, unremitting overactivity or dysregulation of the sympathetic-adrenal-medullary (SAM) axis, HPA axis, and inflammatory cytokines (elevated CRP, cortisol, hypertension), damaging cardiovascular and metabolic tissues over decades."
    },
    {
        "q": "A participant born into a low-income family in an impoverished urban census tract attends university on scholarship, earns a medical degree, and achieves a top-quintile household income by age 40. Sociologists designate this trajectory as:",
        "ch": [
            "downward intergenerational mobility.",
            "upward intragenerational mobility.",
            "horizontal structural mobility.",
            "vertical social reproduction."
        ],
        "a": 1,
        "e": "<strong>Intragenerational mobility refers to socioeconomic shifts within a single individual's lifespan.</strong> Because the participant moved upward from lower SES in early life to upper-quintile SES in adulthood, it is upward intragenerational mobility. Intergenerational mobility (Choice A) compares social standing across different generations (e.g., child compared to parents). Social reproduction (Choice D) is the transmission of social inequality from one generation to the next without mobility."
    },
    {
        "q": "Historical practices such as &ldquo;redlining,&rdquo; where municipal mortgage lenders and federal agencies systematically denied capital investment and home loans to minority neighborhoods, represent which form of social inequality?",
        "ch": [
            "Individual prejudice",
            "Institutional discrimination manifesting as spatial inequality",
            "Interpersonal microaggression",
            "Self-selected cultural enclavization"
        ],
        "a": 1,
        "e": "<strong>Institutional discrimination is embedded within organizational and governmental policies.</strong> Redlining was an institutionalized, systemic policy encoded into official lending guidelines and zoning laws, rather than an isolated, personal act of bias by an individual loan officer. This policy produced enduring spatial inequality—segregating minority communities into geographic areas with disinvested infrastructure, toxic environmental exposures, and food deserts."
    },
    {
        "q": "The accelerated shortening of leukocyte telomere length (T/S ratio) documented in the Low-SES Black cohort reflects which fundamental molecular process of cellular senescence?",
        "ch": [
            "Inability of DNA polymerase to replicate the 5&prime; terminal ends of linear lagging strands, accelerated by oxidative DNA damage",
            "Excessive elongation of mitochondrial circular plasmid DNA during repeated binary fission",
            "Hypermethylation of promoter regions driving non-stop transcription of histone deacetylases",
            "Apoptotic destruction of the nuclear envelope mediated by telomerase reverse transcriptase overactivity"
        ],
        "a": 0,
        "e": "<strong>The end-replication problem causes telomere erosion during cellular division.</strong> Because DNA polymerase requires an RNA primer and can only synthesize 5&prime; to 3&prime;, removal of the distal primer leaves an unreplicated gap at the 5&prime; end of the daughter lagging strand. In somatic leukocytes lacking telomerase, chromosomes shorten with every cell cycle. Chronic physiological stress, glucocorticoid exposure, and reactive oxygen species (ROS) accelerate this erosion, triggering premature cellular senescence."
    }
]

# ==============================================================================
# PASSAGE 4: Elaboration Likelihood Model (ELM) & Cognitive Dissonance
# ==============================================================================
p4_html = """<div class="ttl">Passage 4 (Questions 19&ndash;24)</div>
<p>The Elaboration Likelihood Model (ELM) of persuasion posits that attitude change occurs via two distinct cognitive routes depending on a recipient's motivation and ability to elaborate upon message content. The <i>central route</i> involves deep, systematic cognitive processing of the intrinsic merits, evidentiary rigor, and logical coherence of arguments; attitude changes forged through the central route are durable, highly predictive of future behavior, and resilient against counter-persuasion. Conversely, the <i>peripheral route</i> operates when motivation or cognitive bandwidth is constrained; recipients rely on superficial heuristic cues&mdash;such as source attractiveness, formal credentials, emotional music, or message length&mdash;producing fragile, transient shifts in attitude.</p>
<p>In parallel, Leon Festinger's <i>Cognitive Dissonance Theory</i> posits that holding inconsistent cognitions or engaging in behavior discordant with one's core attitudes generates an aversive psychological tension (dissonance) that drives cognitive restructuring. When individuals perform a counter-attitudinal behavior under conditions of <i>insufficient external justification</i>, they resolve the internal conflict by altering their underlying attitudes to align with the enacted behavior.</p>
<p>Investigators examined these persuasive dynamics in a public health intervention designed to address vaccine hesitancy regarding a novel mucosal influenza vaccine among 480 undergraduate students. Participants were randomized into a 2 &times; 2 &times; 2 factorial protocol manipulating:</p>
<ul>
  <li><b>Personal Relevance:</b> High (informed the outbreak is actively spreading on their home campus) vs. Low (informed the outbreak is localized to a remote overseas region).</li>
  <li><b>Argument Quality:</b> Strong (comprehensive epidemiological trial data demonstrating 94% efficacy and favorable risk ratios) vs. Weak (anecdotal subjective testimonials and emotional rhetoric).</li>
  <li><b>Source Credibility:</b> High (presented by the university's Chair of Infectious Diseases in clinical attire) vs. Low (presented by an anonymous social media lifestyle influencer).</li>
</ul>
<p>Immediately post-intervention and at a 6-week follow-up, participants rated their vaccine favorability on a standardized scale (1.0 = highly negative, 10.0 = highly positive). In an ancillary dissonance experiment, vaccine-hesitant participants were induced to record a pro-vaccine public service announcement in exchange for either nominal compensation ($1) or substantial compensation ($20).</p>
<table>
<tr><th>Condition</th><th>Personal Relevance</th><th>Argument Quality</th><th>Source Credibility</th><th>Immediate Attitude (1&ndash;10)</th><th>6-Week Attitude (1&ndash;10)</th></tr>
<tr><td>1</td><td>High</td><td>Strong</td><td>High</td><td class="n">8.8</td><td class="n">8.5</td></tr>
<tr><td>2</td><td>High</td><td>Strong</td><td>Low</td><td class="n">8.6</td><td class="n">8.3</td></tr>
<tr><td>3</td><td>High</td><td>Weak</td><td>High</td><td class="n">4.1</td><td class="n">3.9</td></tr>
<tr><td>4</td><td>Low</td><td>Strong</td><td>High</td><td class="n">7.9</td><td class="n">5.2</td></tr>
<tr><td>5</td><td>Low</td><td>Weak</td><td>High</td><td class="n">7.7</td><td class="n">4.8</td></tr>
<tr><td>6</td><td>Low</td><td>Strong</td><td>Low</td><td class="n">4.3</td><td class="n">4.0</td></tr>
</table>
<p class="cap"><b>Table 1</b> Immediate and longitudinal attitude favorability scores following persuasive communication.</p>"""

p4_qs = [
    {
        "q": "The finding in Table 1 that Condition 2 (High Relevance, Strong Argument, Low Credibility) yielded an immediate favorability score of 8.6, whereas Condition 3 (High Relevance, Weak Argument, High Credibility) yielded only 4.1, demonstrates that under high personal relevance:",
        "ch": [
            "peripheral cues dominate information processing and supersede factual argument strength.",
            "recipients process messages via the central route, making argument validity the primary determinant of persuasion.",
            "source credibility interacts synergistically with weak arguments to produce cognitive dissonance.",
            "attitude change decays completely within 6 weeks regardless of cognitive elaboration."
        ],
        "a": 1,
        "e": "<strong>High personal relevance engages the central route, prioritizing argument strength over peripheral cues.</strong> Under high relevance, participants scrutinized the substance of the message: strong arguments produced high persuasion (8.6&ndash;8.8) even with a low-credibility influencer, whereas weak arguments failed (4.1) despite an expert source. In contrast, under low relevance (Conditions 4 and 5), the expert source produced high immediate ratings regardless of argument quality, the hallmark of the peripheral route."
    },
    {
        "q": "In Table 1, comparing the longitudinal trajectory of Condition 1 with Condition 5 between post-test and 6 weeks illustrates which fundamental prediction of the Elaboration Likelihood Model?",
        "ch": [
            "Central-route attitude change demonstrates enduring temporal persistence, whereas peripheral-route attitude change decays rapidly.",
            "Peripheral-route attitude change produces permanent neural remodeling within the limbic system.",
            "Weak arguments processed through the central route undergo spontaneous recovery over time.",
            "Personal relevance reduces the cognitive capacity required to evaluate peripheral cues."
        ],
        "a": 0,
        "e": "<strong>Central route changes endure; peripheral route changes fade.</strong> In Condition 1 (central route: high relevance + strong argument), attitude scores remained virtually identical after 6 weeks (8.8 &rarr; 8.5). In Condition 5 (peripheral route: low relevance + weak argument + high credibility cue), immediate attitude was initially high (7.7) due to superficial prestige bias, but collapsed over 6 weeks down to 4.8. Peripheral shifts are superficial and transient unless continuously reinforced."
    },
    {
        "q": "In the ancillary cognitive dissonance experiment, participants initially opposed to vaccination who recorded a pro-vaccine video for $1 demonstrated significantly greater genuine positive attitude change than those paid $20. Why?",
        "ch": [
            "The $20 payment created severe cognitive dissonance by overwhelming executive working memory.",
            "The $1 payment provided insufficient external justification, compelling participants to resolve internal dissonance by modifying their attitudes.",
            "The $1 payment activated classical conditioning, transforming the video task into a primary reinforcer.",
            "The $20 payment triggered reactance, causing participants to intentionally sabotage their performance."
        ],
        "a": 1,
        "e": "<strong>The insufficient justification effect forces internal attitude alignment.</strong> When individuals engage in counter-attitudinal behavior (advocating for a vaccine they dislike), they experience dissonance. If paid $20, they have ample external justification ('I only said it for the substantial payment'), resolving the contradiction without altering their beliefs. If paid only $1, external justification is insufficient, leaving acute internal dissonance that can only be resolved by internally convincing themselves that they actually agree with the pro-vaccine message."
    },
    {
        "q": "A public health campaign aims to maximize enduring, counter-persuasion-resistant seatbelt compliance among adolescents. Based on the ELM, the campaign creators should prioritize:",
        "ch": [
            "featuring popular celebrity actors performing humorous comedic skits while driving.",
            "presenting vivid statistics and logical causal arguments highlighting direct, personal vulnerability and survival outcomes.",
            "playing fast-paced, high-tempo pop music in the background of brief 5-second advertisements.",
            "increasing the number of advertisements without altering message clarity or factual content."
        ],
        "a": 1,
        "e": "<strong>Central route processing requires personal relevance and strong, logical evidence.</strong> Highlighting direct personal vulnerability (elevating motivation/relevance) and presenting sound, logical arguments about crash biomechanics and survival engages central route processing, fostering deep cognitive elaboration and producing durable behavioral change resistant to peer counter-persuasion. Choices A, C, and D are peripheral heuristic cues."
    },
    {
        "q": "A regular cigarette smoker is informed by his physician that tobacco use causes emphysema and lung cancer. If the smoker responds by stating, &ldquo;My grandfather smoked two packs a day and lived to age 94, so medical statistics on smoking are completely exaggerated,&rdquo; Festinger's theory characterizes this defense as:",
        "ch": [
            "altering the core addictive behavior to achieve behavioral consonance.",
            "reducing cognitive dissonance by trivializing the threat and seeking consonant rationalizations.",
            "experiencing spontaneous recovery of an unconditioned sensory response.",
            "succumbing to the fundamental attribution error regarding his physician's motives."
        ],
        "a": 1,
        "e": "<strong>Dissonance is often alleviated through trivialization or rationalizing cognitions.</strong> When individuals cannot or will not change an entrenched dissonant behavior (smoking), they reduce psychological distress by discounting the validity of contradictory information, seeking outlier anecdotes (the grandfather who lived to 94), or trivializing the risk, thereby restoring perceived internal consistency."
    },
    {
        "q": "If participants who listened to the anonymous lifestyle blogger in Condition 6 dismissed the health advice by concluding, &ldquo;Social media influencers are vain, lazy, and morally bankrupt narcissists,&rdquo; while completely ignoring the rigorous clinical data presented, they committed:",
        "ch": [
            "the actor-observer bias.",
            "the fundamental attribution error.",
            "the self-serving bias.",
            "the halo effect."
        ],
        "a": 1,
        "e": "<strong>The fundamental attribution error overemphasizes internal disposition over situational context.</strong> The fundamental attribution error (FAE) is the pervasive tendency for observers to attribute another person's actions or standing to internal personality traits or moral character (vanity, laziness) while overlooking situational factors, external evidence, or environmental constraints. Actor-observer bias (Choice A) requires comparing an attribution of oneself to an attribution of another."
    }
]

print("Passages 3 & 4 defined.")

# ==============================================================================
# PASSAGE 5: Operant Conditioning Schedules & Incentive-Sensitization
# ==============================================================================
p5_html = """<div class="ttl">Passage 5 (Questions 25&ndash;30)</div>
<p>Substance use disorders involve complex interactions between operant reinforcement schedules, Pavlovian associative conditioning, and neural circuit adaptations. Robinson and Berridge's <i>Incentive-Sensitization Theory</i> dissociates the neurobiological substrates of drug &ldquo;wanting&rdquo; (incentive salience, mediated by the mesolimbic dopamine projection) from drug &ldquo;liking&rdquo; (hedonic pleasure, mediated by discrete opioid and endocannabinoid receptor hotspots within the nucleus accumbens shell and ventral pallidum). While tolerance blunts hedonic liking over repeated administrations, neuroplastic sensitization hyper-activates mesolimbic dopamine pathways, producing pathological craving and compulsive seeking when confronted with drug-associated conditioned stimuli (cues).</p>
<p>Operant reinforcement schedules fundamentally dictate the acquisition rate, terminal response vigor, and extinction resistance of drug self-administration. To quantify these parameters, 48 adult male Sprague-Dawley rats were implanted with chronic intravenous jugular catheters and trained in operant chambers equipped with an active lever (delivering intravenous cocaine + paired audiovisual cue: cue light illumination and a 2.5-kHz tone) and an inactive lever (recorded presses without programmed consequences).</p>
<p>Rats were assigned to one of four reinforcement schedules for 21 days:</p>
<ul>
  <li><b>Group 1 (FR-1):</b> Continuous reinforcement; every active lever press triggered an infusion.</li>
  <li><b>Group 2 (FR-15):</b> Fixed ratio; exactly 15 active lever presses yielded one infusion.</li>
  <li><b>Group 3 (VR-15):</b> Variable ratio; an unpredictable number of active lever presses (averaging 15, range 3&ndash;27) yielded an infusion.</li>
  <li><b>Group 4 (FI-60s):</b> Fixed interval; the first active lever press following a 60-second elapsed interval yielded an infusion.</li>
</ul>
<p>Following acquisition, animals underwent 10 days of extinction testing (infusions replaced with isotonic saline, audiovisual cue withheld). On day 11, animals were evaluated in a cue-induced reinstatement session (audiovisual cue presented non-contingently) paired with in vivo microdialysis measuring extracellular dopamine in the nucleus accumbens (NAc).</p>
<table>
<tr><th>Experimental Group</th><th>Schedule</th><th>Terminal Acquisition Rate (presses/min)</th><th>Cumulative Extinction Responses (10 Days)</th><th>Reinstatement Responses (Day 11)</th><th>NAc Extracellular Dopamine (% Baseline)</th></tr>
<tr><td>Group 1</td><td>FR-1</td><td class="n">14.2</td><td class="n">175</td><td class="n">48</td><td class="n">170%</td></tr>
<tr><td>Group 2</td><td>FR-15</td><td class="n">51.6</td><td class="n">710</td><td class="n">122</td><td class="n">255%</td></tr>
<tr><td>Group 3</td><td>VR-15</td><td class="n">106.8</td><td class="n">2,680</td><td class="n">355</td><td class="n">420%</td></tr>
<tr><td>Group 4</td><td>FI-60s</td><td class="n">24.5</td><td class="n">430</td><td class="n">84</td><td class="n">215%</td></tr>
</table>
<p class="cap"><b>Table 1</b> Operant responding parameters and neurochemical cue reactivity across schedules.</p>"""

p5_qs = [
    {
        "q": "Based on Table 1, which reinforcement schedule generated the highest terminal response rate and the greatest persistence during extinction, matching the behavioral pattern characteristic of human electronic gambling and substance addiction?",
        "ch": [
            "Fixed Ratio (FR-15)",
            "Variable Ratio (VR-15)",
            "Fixed Interval (FI-60s)",
            "Continuous Reinforcement (FR-1)"
        ],
        "a": 1,
        "e": "<strong>Variable ratio schedules generate the highest response rates and maximal resistance to extinction.</strong> In VR schedules, reinforcement occurs after an unpredictable, variable number of responses. Because any individual press could be the one that triggers the reward, subjects maintain an extraordinarily high, steady rate of output (106.8 presses/min) with no post-reinforcement pause. This schedule is notoriously resistant to extinction (2,680 cumulative responses), underlying the powerful behavioral persistence of slot machines, gambling, and addictive seeking."
    },
    {
        "q": "Cumulative response records for Group 4 (FI-60s) during the final days of acquisition would exhibit which distinctive graphical pattern between consecutive drug deliveries?",
        "ch": [
            "A completely flat horizontal line indicating behavioral extinction",
            "A constant, unbroken steep linear slope with zero pause after reinforcement",
            "A scalloped curve featuring a post-reinforcement pause followed by accelerating response rates as the end of the interval approaches",
            "A staircase pattern with massive bursts of responding immediately following each reward delivery"
        ],
        "a": 2,
        "e": "<strong>Fixed interval schedules produce a characteristic 'scalloped' response curve.</strong> In an FI schedule, reward delivery is determined purely by elapsed time; pressing during the interval yields nothing. Consequently, the animal pauses immediately following reinforcement (the post-reinforcement pause) and then gradually accelerates its response rate as the 60-second mark nears, creating an upward-curving 'scallop' on cumulative records."
    },
    {
        "q": "According to the incentive-sensitization theory of addiction, as chronic drug consumption progresses toward dependence, what dissociation occurs between &ldquo;wanting&rdquo; and &ldquo;liking&rdquo;?",
        "ch": [
            "Mesolimbic dopamine-mediated craving ('wanting') sensitizes and intensifies, while opioid-mediated hedonic pleasure ('liking') blunts due to tolerance.",
            "Hedonic pleasure ('liking') sensitizes exponentially, while motivational craving ('wanting') drops to zero.",
            "Both 'wanting' and 'liking' undergo identical down-regulation due to mu-opioid receptor internalization.",
            "Craving becomes solely governed by the prefrontal cortex while the nucleus accumbens undergoes complete atrophy."
        ],
        "a": 0,
        "e": "<strong>Incentive-sensitization decouples 'wanting' (sensitized) from 'liking' (tolerated).</strong> Robinson and Berridge showed that repeated drug exposure produces hypersensitivity (sensitization) in the mesolimbic dopamine system, amplifying the incentive salience or 'wanting' triggered by drug cues. In contrast, the neural circuits mediating the subjective pleasure or 'liking' (hedonic hotspots in the nucleus accumbens shell and ventral pallidum mediated by opioids) exhibit tolerance, leading individuals to compulsively crave and seek a drug even when it produces minimal pleasure."
    },
    {
        "q": "In the reinstatement phase of the experiment, the paired audiovisual stimulus (light + 2.5-kHz tone) that rekindled vigorous lever-pressing and dopamine release functions as a:",
        "ch": [
            "primary unconditioned reinforcer.",
            "conditioned stimulus triggering cue reactivity.",
            "negative punisher suppressing alternative behaviors.",
            "discriminative stimulus for operant extinction."
        ],
        "a": 1,
        "e": "<strong>The paired light/tone cue acts as a conditioned stimulus (CS).</strong> Through repeated classical conditioning pairings with cocaine (unconditioned stimulus, US), the previously neutral light/tone compound becomes a conditioned stimulus (CS) capable of eliciting conditioned dopamine release and operant drug-seeking (conditioned response, CR), a phenomenon known clinically as cue reactivity."
    },
    {
        "q": "The elevated extracellular dopamine measured in the nucleus accumbens during cue-induced reinstatement is delivered by dopaminergic axons originating in the:",
        "ch": [
            "locus coeruleus.",
            "substantia nigra pars compacta.",
            "ventral tegmental area (VTA).",
            "raphe nuclei."
        ],
        "a": 2,
        "e": "<strong>The mesolimbic dopamine pathway projects from the VTA to the nucleus accumbens.</strong> The ventral tegmental area (VTA) in the midbrain sends dopaminergic projections along the mesolimbic pathway to the nucleus accumbens (ventral striatum), playing a central role in reward, reinforcement, and incentive salience. In contrast, the substantia nigra (Choice B) projects to the dorsal striatum (nigrostriatal pathway for motor control); the locus coeruleus (Choice A) synthesizes norepinephrine; and the raphe nuclei (Choice D) synthesize serotonin."
    },
    {
        "q": "During the very first 30 minutes of the extinction phase (when lever pressing yielded only saline for the first time), the rats exhibited an immediate, temporary surge in active lever-pressing frequency before responding steadily declined. This phenomenon is known as:",
        "ch": [
            "an extinction burst.",
            "spontaneous recovery.",
            "stimulus generalization.",
            "instinctive drift."
        ],
        "a": 0,
        "e": "<strong>An extinction burst is a brief, intense spike in responding upon removal of reinforcement.</strong> When a previously reinforced operant behavior suddenly fails to produce the expected reinforcer, the organism temporarily increases the frequency, variability, and intensity of the response before beginning the gradual decline toward extinction. Spontaneous recovery (Choice B) occurs after a delay/rest interval following complete extinction."
    }
]

# ==============================================================================
# PASSAGE 6: Schizophrenia Neurobiology, Dopaminergic Pathways, & Antipsychotics
# ==============================================================================
p6_html = """<div class="ttl">Passage 6 (Questions 31&ndash;36)</div>
<p>The classical dopamine hypothesis of schizophrenia posited generalized dopaminergic hyperactivity. Contemporary neurobiological models refine this view by mapping symptom dimensions to distinct anatomical pathways with opposing neurochemical states:</p>
<ul>
  <li><b>Mesolimbic Pathway (VTA &rarr; Nucleus Accumbens / Ventral Striatum):</b> Dopamine hyperfunction drives <i>positive symptoms</i>, including auditory hallucinations, persecutory delusions, and disorganized thought.</li>
  <li><b>Mesocortical Pathway (VTA &rarr; Dorsolateral Prefrontal Cortex):</b> Dopamine hypofunction underlies <i>negative symptoms</i> (flat affect, avolition, alogia, anhedonia) and executive cognitive impairments.</li>
  <li><b>Nigrostriatal Pathway (Substantia Nigra &rarr; Dorsal Striatum / Caudate-Putamen):</b> Regulates extrapyramidal motor coordination; unintended D2 receptor antagonism here produces extrapyramidal symptoms (EPS), such as acute dystonia, pseudoparkinsonism, and tardive dyskinesia.</li>
  <li><b>Tuberoinfundibular Pathway (Hypothalamus &rarr; Anterior Pituitary):</b> Dopamine acts as prolactin-inhibiting factor (PIF); D2 antagonism removes this tonic inhibition, causing hyperprolactinemia.</li>
</ul>
<p>Typical (first-generation) antipsychotics act primarily as high-affinity D2 receptor antagonists, effectively resolving positive symptoms but often exacerbating negative symptoms and inducing severe EPS. Atypical (second-generation) antipsychotics combine moderate D2 antagonism with potent serotonin 5-HT<sub>2A</sub> receptor antagonism, facilitating dopamine release in the prefrontal cortex and striatum to mitigate negative symptoms and reduce motor side effects. Third-generation agents function as D2 partial agonists.</p>
<p>A 16-week randomized, double-blind clinical trial compared three pharmacotherapies in 180 adults with chronic schizophrenia:</p>
<ul>
  <li><b>Arm 1 (Haloperidol, 10 mg/day):</b> Typical D2 antagonist.</li>
  <li><b>Arm 2 (Risperidone, 6 mg/day):</b> Atypical 5-HT<sub>2A</sub> / D2 antagonist.</li>
  <li><b>Arm 3 (Aripiprazole, 15 mg/day):</b> Atypical D2 partial agonist / 5-HT<sub>2A</sub> antagonist.</li>
</ul>
<p>Investigators monitored striatal D2 receptor occupancy (%) using [<sup>11</sup>C]-raclopride PET imaging, percentage reduction in PANSS positive score (&Delta;PANSS+), percentage reduction in PANSS negative score (&Delta;PANSS&minus;), Simpson-Angus Scale (SAS) for extrapyramidal motor signs (0&ndash;40, higher = worse motor impairment), and fasting serum prolactin (ng/mL; normal reference: &lt;20 ng/mL).</p>
<table>
<tr><th>Pharmacotherapy</th><th>Drug Mechanism</th><th>Striatal D2 Occupancy (%)</th><th>&Delta;PANSS+ (%)</th><th>&Delta;PANSS&minus; (%)</th><th>Mean SAS Score</th><th>Serum Prolactin (ng/mL)</th></tr>
<tr><td>Arm 1: Haloperidol</td><td>High-affinity D2 antagonist</td><td class="n">83%</td><td class="n">&minus;48.5%</td><td class="n">&minus;6.2%</td><td class="n">8.4</td><td class="n">68.5</td></tr>
<tr><td>Arm 2: Risperidone</td><td>Dual 5-HT<sub>2A</sub> / D2 antagonist</td><td class="n">74%</td><td class="n">&minus;47.1%</td><td class="n">&minus;23.5%</td><td class="n">2.2</td><td class="n">54.2</td></tr>
<tr><td>Arm 3: Aripiprazole</td><td>D2 partial agonist / 5-HT<sub>2A</sub> antagonist</td><td class="n">86%</td><td class="n">&minus;45.8%</td><td class="n">&minus;29.1%</td><td class="n">0.5</td><td class="n">12.1</td></tr>
</table>
<p class="cap"><b>Table 1</b> Clinical efficacy and neuropharmacological parameters across treatment arms.</p>"""

p6_qs = [
    {
        "q": "Why does haloperidol achieve robust efficacy against positive symptoms (&minus;48.5%) while producing virtually no meaningful improvement in negative symptoms (&minus;6.2%)?",
        "ch": [
            "Haloperidol selectively upregulates dopamine synthesis exclusively in the prefrontal cortex.",
            "Non-selective D2 receptor antagonism successfully dampens hyperactive mesolimbic signaling but fails to reverse, and may worsen, pre-existing hypodopaminergic tone in the mesocortical pathway.",
            "Positive symptoms are mediated by serotonin 5-HT2A receptors, which haloperidol irreversibly blocks.",
            "Negative symptoms stem entirely from demyelination of the corpus callosum unaffected by monoamines."
        ],
        "a": 1,
        "e": "<strong>Pathology-specific dopamine mismatch: mesolimbic hyperfunction vs mesocortical hypofunction.</strong> Positive symptoms arise from hyperdopaminergic activity in the mesolimbic pathway, so blocking D2 receptors relieves hallucinations and delusions. However, negative symptoms stem from hypodopaminergic activity in the mesocortical pathway (prefrontal cortex). Haloperidol indiscriminately blocks D2 receptors across the entire brain, providing no benefit—and often worsening—prefrontal dopamine deficit."
    },
    {
        "q": "The elevated Simpson-Angus Scale (SAS) motor score observed in Arm 1 (8.4) indicates extrapyramidal symptoms resulting directly from dopamine receptor antagonism in which neural tract?",
        "ch": [
            "Mesocortical pathway",
            "Nigrostriatal pathway",
            "Tuberoinfundibular pathway",
            "Spinothalamic tract"
        ],
        "a": 1,
        "e": "<strong>The nigrostriatal pathway controls involuntary motor circuitry.</strong> Dopaminergic neurons originating in the substantia nigra pars compacta project to the dorsal striatum (caudate and putamen) to facilitate motor initiation. Blocking >80% of striatal D2 receptors (as haloperidol does) mimics Parkinsonian dopamine depletion, producing extrapyramidal motor side effects (pseudoparkinsonism, rigidity, resting tremor, acute dystonia)."
    },
    {
        "q": "What neuroendocrine mechanism explains the pronounced hyperprolactinemia observed in Arm 1 (68.5 ng/mL) and Arm 2 (54.2 ng/mL)?",
        "ch": [
            "D2 receptor blockade in the tuberoinfundibular pathway lifts dopamine's tonic inhibitory suppression of prolactin secretion from anterior pituitary lactotropes.",
            "Dopamine agonism in the posterior pituitary triggers the immediate exocytosis of prolactin and oxytocin.",
            "Haloperidol stimulates TRH release from the paraventricular nucleus, directly inducing adrenal galactorrhea.",
            "Blockade of 5-HT2A receptors in the pineal gland prevents melatonin synthesis, disinhibiting prolactin."
        ],
        "a": 0,
        "e": "<strong>Dopamine is the primary prolactin-inhibiting factor (PIF) via the tuberoinfundibular pathway.</strong> Dopaminergic neurons in the hypothalamic arcuate nucleus project to the median eminence and deliver dopamine through portal vessels to lactotropes in the anterior pituitary. Dopamine binds D2 receptors to tonically suppress prolactin exocytosis. High-affinity D2 antagonism (Arms 1 and 2) disinhibits lactotropes, driving serum prolactin up."
    },
    {
        "q": "Aripiprazole achieves 86% striatal D2 receptor occupancy yet yields an extrapyramidal score near zero (0.5) and normal prolactin levels (12.1 ng/mL). What pharmacological property accounts for this profile?",
        "ch": [
            "It is an irreversible suicide inhibitor of tyrosine hydroxylase.",
            "It functions as a partial D2 agonist with ~30% intrinsic activity, providing sufficient basal stimulation in the striatum and pituitary while dampening hyperactive mesolimbic firing.",
            "It completely avoids crossing the blood-brain barrier, exerting all effects through peripheral autonomic ganglia.",
            "It selectively destroys dopamine transporters exclusively within the ventral tegmental area."
        ],
        "a": 1,
        "e": "<strong>Partial agonists act as functional antagonists in hyperactive areas and functional agonists in hypoactive areas.</strong> Aripiprazole binds D2 receptors with high affinity (86% occupancy) but possesses modest intrinsic efficacy (~30%). In the mesolimbic tract where endogenous dopamine is excessively high, it acts as a functional antagonist, reducing overall signaling to alleviate positive symptoms. In the striatum and tuberoinfundibular tracts where basal dopamine is normal, its intrinsic activity provides sufficient baseline signaling to prevent extrapyramidal motor symptoms and avoid hyperprolactinemia."
    },
    {
        "q": "Which clinical constellation represents exclusively NEGATIVE symptoms of schizophrenia according to the Diagnostic and Statistical Manual of Mental Disorders (DSM-5)?",
        "ch": [
            "Auditory hallucinations, somatic delusions, and pressured speech",
            "Avolition, blunted affect, alogia, and asociality",
            "Catatonic posturing, thought broadcasting, and flight of ideas",
            "Depersonalization, hypervigilance, and obsessive-compulsive checking"
        ],
        "a": 1,
        "e": "<strong>Negative symptoms reflect deficits or absence of normal behavioral functions.</strong> Negative symptoms are characterized by the '5 As': Avolition (lack of motivation), Affective flattening/blunted affect, Alogia (poverty of speech), Asociality (social withdrawal), and Anhedonia (inability to experience pleasure). Hallucinations, delusions, and disorganized motor behavior (Choices A and C) are positive symptoms (pathological additions to normal behavior)."
    },
    {
        "q": "Twin studies consistently demonstrate a concordance rate for schizophrenia of approximately 48% in monozygotic twins and 17% in dizygotic twins. This evidence provides strongest support for which etiological model?",
        "ch": [
            "The diathesis-stress model, indicating that substantial genetic vulnerability requires environmental stressors for phenotypic clinical expression",
            "The social drift hypothesis, asserting that psychological illness solely causes downward economic mobility without biological factors",
            "A pure Mendelian autosomal dominant inheritance model with complete penetrance",
            "The psychoanalytic drive model of repressed infantile intrapsychic trauma"
        ],
        "a": 0,
        "e": "<strong>A 48% monozygotic concordance rate proves a powerful genetic diathesis interacting with environment.</strong> If schizophrenia were purely genetic (Mendelian with 100% penetrance), monozygotic twin concordance would be 100%. If it were purely environmental, MZ and DZ twins would share identical concordance rates (~17%). A 48% MZ vs 17% DZ concordance demonstrates a strong hereditary predisposition (diathesis) that requires secondary environmental triggers (stress, birth complications, cannabis use) to manifest clinically."
    }
]

print("Passages 5 & 6 defined.")

# ==============================================================================
# PASSAGE 7: Dramaturgical Perspective & Impression Management in Healthcare
# ==============================================================================
p7_html = """<div class="ttl">Passage 7 (Questions 37&ndash;42)</div>
<p>Erving Goffman's <i>dramaturgical perspective</i> analyzes social interaction through the theatrical metaphor of performance, dividing human behavior into front-stage and back-stage regions. In healthcare environments, clinicians constantly engage in <i>impression management</i> on the <b>front stage</b> (e.g., patient rooms, outpatient clinics, surgical suites) before an audience of patients, families, and evaluators. Clinicians utilize formal sign-vehicles&mdash;such as white lab coats, stethoscopes, and technical anatomical vocabulary&mdash;while maintaining an affective demeanor of calm clinical competence, diagnostic infallibility, and professional empathy.</p>
<p>Conversely, the <b>back stage</b> comprises private institutional sanctuaries (e.g., locked physician call rooms, staff lounges, scrub alcoves) where the performance is suspended. Here, clinicians can drop the professional facade, openly acknowledge diagnostic uncertainty, vent emotional exhaustion, and employ dark coping humor among peers without undermining patient trust or compromising the institutional legitimacy of medicine.</p>
<p>Navigating these settings introduces complex role dynamics:</p>
<ul>
  <li><b>Role Strain:</b> Contradictory tensions, expectations, or demands experienced within a <i>single</i> social status (e.g., a resident physician struggling to simultaneously conduct rapid clinical throughput, complete extensive electronic charting, and deliver compassionate bedside care).</li>
  <li><b>Role Conflict:</b> Incompatible obligations arising from <i>two or more separate</i> statuses occupied by the same individual (e.g., an intensivist balancing mandatory overnight critical care duties with parental responsibilities for a hospitalized dependent child).</li>
</ul>
<p>A sociological investigation surveyed 240 hospital clinicians across three academic intensive care units (ICUs): Postgraduate Year 1 Interns (PGY-1), Postgraduate Year 3 Senior Residents (PGY-3), Attending Intensivists, and ICU Registered Nurses (RNs). Researchers quantified weekly clinical hours, front-stage impression management effort (1.0&ndash;5.0 scale), frequency of back-stage emotional venting (episodes per 12-hour shift), standardized indices of role strain and role conflict (1.0&ndash;10.0 scale), and emotional depersonalization scores from the Maslach Burnout Inventory (MBI, 0&ndash;30 scale).</p>
<table>
<tr><th>Professional Cohort</th><th>Mean Weekly Hours</th><th>Impression Management Effort (1&ndash;5)</th><th>Back-Stage Venting (episodes/shift)</th><th>Role Strain Index (1&ndash;10)</th><th>Role Conflict Index (1&ndash;10)</th><th>MBI Depersonalization (0&ndash;30)</th></tr>
<tr><td>PGY-1 Interns</td><td class="n">78.5</td><td class="n">4.7</td><td class="n">5.4</td><td class="n">8.6</td><td class="n">7.8</td><td class="n">18.4</td></tr>
<tr><td>PGY-3 Senior Residents</td><td class="n">67.0</td><td class="n">4.4</td><td class="n">4.1</td><td class="n">6.4</td><td class="n">6.8</td><td class="n">15.2</td></tr>
<tr><td>Attending Intensivists</td><td class="n">54.0</td><td class="n">4.1</td><td class="n">2.0</td><td class="n">4.2</td><td class="n">5.0</td><td class="n">9.5</td></tr>
<tr><td>ICU Registered Nurses</td><td class="n">39.5</td><td class="n">4.3</td><td class="n">4.8</td><td class="n">5.9</td><td class="n">4.1</td><td class="n">11.4</td></tr>
</table>
<p class="cap"><b>Table 1</b> Sociological indices of workplace performance, role stress, and burnout in intensive care staff.</p>"""

p7_qs = [
    {
        "q": "A PGY-1 intern experiences intense distress while attempting to simultaneously execute emergency bedside arterial lines, answer urgent clinical nurse pages, and document detailed electronic discharge summaries before sign-out. This experience is best designated as:",
        "ch": [
            "role conflict.",
            "role strain.",
            "role exit.",
            "status inconsistency."
        ],
        "a": 1,
        "e": "<strong>Role strain occurs when conflicting demands exist within a single social role.</strong> The intern is occupying a single social status (that of medical intern / resident physician) and struggling to satisfy multiple competing expectations built into that specific role (procedural tasks vs administrative charting vs communication). Role conflict (Choice A) requires a clash between two or more entirely different social statuses (e.g., physician vs parent). Role exit (Choice C) is disengaging from a role permanently."
    },
    {
        "q": "According to Goffman's dramaturgical framework, the high frequency of emotional venting and dark humor observed in the staff breakroom (5.4 episodes/shift among interns) serves what sociological function?",
        "ch": [
            "A front-stage performance intended to intimidate subordinate healthcare technicians",
            "A back-stage coping mechanism that allows actors to release emotional strain and cultivate group solidarity without compromising the front-stage clinical illusion",
            "A pathological manifestation of the bystander effect within institutional hierarchies",
            "An attempt to induce cognitive dissonance in senior attending supervisors"
        ],
        "a": 1,
        "e": "<strong>The back stage provides a sanctuary to drop performance facades without audience scrutiny.</strong> According to Goffman, back-stage regions allow social actors to shed their rehearsed characters, vent authentic anxieties, express dark humor, and decompress among peers. This protects the front-stage performance (the illusion of calm omnipotence presented to patients and families) while maintaining interpersonal solidarity and preventing psychological collapse."
    },
    {
        "q": "An attending physician is scheduled to lead a life-or-death multi-organ transplant surgery at the exact time her elderly parent suffers a stroke requiring immediate legal power-of-attorney medical decisions. Her profound psychological anguish stems directly from:",
        "ch": [
            "role strain.",
            "role conflict.",
            "social facilitation.",
            "group polarization."
        ],
        "a": 1,
        "e": "<strong>Role conflict arises from competing demands between two distinct social roles.</strong> Here, the individual occupies two separate social statuses simultaneously: surgeon/physician and adult child/family caregiver. The non-negotiable obligations of these two roles directly collide in time and emotional priority, exemplifying classic role conflict."
    },
    {
        "q": "When a junior resident intentionally drapes a cardiology-grade stethoscope over her neck, buttons a clean white coat embroidered with an academic insignia, and speaks with authoritative medical jargon to soothe a skeptical patient, she is utilizing:",
        "ch": [
            "sign-vehicles to execute front-stage impression management.",
            "deindividuation to escape personal clinical responsibility.",
            "the fundamental attribution error to blame institutional administrators.",
            "informational social influence to conform to patient demands."
        ],
        "a": 0,
        "e": "<strong>Sign-vehicles are physical props and appearance cues used in impression management.</strong> In dramaturgical sociology, individuals manage the impressions others form of them by utilizing 'sign-vehicles'—including setting, appearance (white coat, stethoscope, badge), and manner (confident clinical tone, professional jargon)—to communicate social status, establish competence, and secure the audience's compliance and trust."
    },
    {
        "q": "During interdisciplinary ICU rounds, resident physicians and nurses view hospital financial administrators as an adversarial &ldquo;out-group&rdquo; interested only in reducing bed-days, while viewing fellow bedside clinicians as a cohesive &ldquo;in-group&rdquo; dedicated to patient welfare. This division is best explained by:",
        "ch": [
            "Social Identity Theory.",
            "Drive-Reduction Theory.",
            "The James-Lange Theory of emotion.",
            "Differential Association Theory."
        ],
        "a": 0,
        "e": "<strong>Social Identity Theory explains in-group favoritism and out-group derogation.</strong> Henri Tajfel's Social Identity Theory posits that individuals categorize themselves and others into social groups ('in-groups' vs 'out-groups') to bolster self-esteem and social cohesion. Group members perceive in-group peers with positive bias and solidarity, while viewing out-group members (here, administrative budget managers) with skepticism, stereotypes, and perceived competition."
    },
    {
        "q": "A structural functionalist sociologist examining Table 1 would argue that the steep hierarchy, high work hours, and intense role strain of residency training exist primarily because:",
        "ch": [
            "capitalist hospital boards exploit vulnerable trainee labor to extract surplus monetary value.",
            "hierarchical stratification ensures that the most functionally vital societal roles are filled by the most rigorously trained and competent individuals.",
            "micro-level symbolic interactions construct arbitrary medical realities detached from biological health.",
            "patriarchal institutional norms systematically disadvantage female caregivers."
        ],
        "a": 1,
        "e": "<strong>Structural functionalism views institutional stratification as socially adaptive (Davis-Moore thesis).</strong> Functionalism (Emile Durkheim, Kingsley Davis, Wilbert Moore) asserts that societal institutions operate in equilibrium, with social stratification serving a vital purpose: grueling training, high demands, and substantial prestige/rewards motivate the most capable individuals to endure sacrificial preparation to fill the most functionally critical roles in society (such as physicians). Choice A is Conflict Theory; Choice C is Symbolic Interactionism; Choice D is Feminist Theory."
    }
]

# ==============================================================================
# SET 8: 10 Standalone Discrete Questions (d: true)
# ==============================================================================
ps_discretes = [
    {
        "q": "In a psychophysical experiment testing Weber's Law, a participant can just barely distinguish between an 80-gram weight and an 84-gram weight. If the experimenter subsequently presents a 240-gram weight, what is the minimum additional weight that must be added for the participant to perceive a just-noticeable difference (JND)?",
        "d": True,
        "ch": [
            "4 grams",
            "8 grams",
            "12 grams",
            "16 grams"
        ],
        "a": 2,
        "e": "<strong>Weber's Law states that the difference threshold is a constant fraction of the initial stimulus intensity: &Delta;I / I = k.</strong><br>From the first trial: &Delta;I = 84 g &minus; 80 g = 4 g. Weber's constant <em>k</em> = 4 / 80 = 0.05 (5%).<br>For the 240-gram stimulus: &Delta;I = <em>k</em> &times; I = 0.05 &times; 240 g = 12 grams.<br>Trap A (4 grams) makes the common error of assuming the JND is a constant absolute quantity rather than a constant proportion."
    },
    {
        "q": "A 50-year-old physician devotes her weekends to founding a free community clinic to train pre-medical students and provide preventative care to underserved families, stating that she derives deep meaning from nurturing the next generation of healthcare leaders. According to Erik Erikson's stages of psychosocial development, which crisis is she successfully resolving?",
        "d": True,
        "ch": [
            "Intimacy vs. Isolation",
            "Generativity vs. Stagnation",
            "Integrity vs. Despair",
            "Identity vs. Role Confusion"
        ],
        "a": 1,
        "e": "<strong>Generativity vs. Stagnation is Erikson's crisis of middle adulthood (ages ~40&ndash;65).</strong> Generativity involves contributing productively to society, guiding and mentoring younger generations, and establishing a positive enduring legacy. Failure to resolve this stage leads to stagnation (feeling unproductive, self-absorbed, and unfulfilled). Intimacy vs. Isolation (Choice A) occurs in young adulthood (20&ndash;40); Integrity vs. Despair (Choice C) occurs in late adulthood (65+)."
    },
    {
        "q": "In Lawrence Kohlberg's Heinz dilemma, a participant argues that Heinz was morally obligated to steal the unaffordable cancer medication for his dying wife because: &ldquo;Universal human rights and the inherent sanctity of human life transcend civil property laws and institutional legal statutes.&rdquo; This reasoning exemplifies which stage of moral development?",
        "d": True,
        "ch": [
            "Pre-conventional morality (Stage 1: Obedience and punishment orientation)",
            "Pre-conventional morality (Stage 2: Instrumental relativist orientation)",
            "Conventional morality (Stage 4: Law and order social obedience)",
            "Post-conventional morality (Stage 6: Universal ethical principles)"
        ],
        "a": 3,
        "e": "<strong>Post-conventional morality bases ethical decisions on abstract, universal human rights.</strong> In Stage 6, individuals recognize that laws and social rules are valid only to the extent that they ground justice; when institutional laws conflict with universal human rights (such as the right to life), ethical conscience supersedes civil law. Conventional Stage 4 (Choice C) would argue stealing is wrong because maintaining societal order requires strict obedience to statutory law."
    },
    {
        "q": "In Study A, researchers observed that athletes asked to pull on a rope as part of a 6-person tug-of-war team exerted 22% less individual mechanical force than when pulling alone. In Study B, participants seated in an auditorium failed to evacuate or notify authorities when smoke billowed from an air vent because each assumed other attendees would take action. Which pair of social psychological phenomena is demonstrated in Study A and Study B, respectively?",
        "d": True,
        "ch": [
            "Social facilitation and Groupthink",
            "Social loafing and Bystander effect",
            "Deindividuation and Group polarization",
            "Bystander effect and Social loafing"
        ],
        "a": 1,
        "e": "<strong>Social loafing involves reduced effort in pooled tasks; the bystander effect involves failure to intervene due to diffusion of responsibility.</strong> In Study A, individual physical output decreased when performance was pooled and unidentifiable (classic social loafing). In Study B, presence of inactive peers caused diffusion of responsibility and pluralistic ignorance, inhibiting intervention during an emergency (the bystander effect). Choice D inverts the two phenomena."
    },
    {
        "q": "A driver observes another motorist swerve erratically across lanes and furiously yells, &ldquo;That person is an aggressive, reckless jerk who has no regard for safety!&rdquo; Ten minutes later, when the same driver swerves abruptly to avoid a pothole, she thinks, &ldquo;I had to swerve because the road was damaged and the city never repairs it.&rdquo; The discrepancy between these two attributions illustrates:",
        "d": True,
        "ch": [
            "the fundamental attribution error.",
            "the actor-observer bias.",
            "the self-serving bias.",
            "the optimism bias."
        ],
        "a": 1,
        "e": "<strong>The actor-observer bias compares attributions made for oneself versus others.</strong> The fundamental attribution error (FAE, Choice A) is strictly an observer effect: overattributing *another person's* behavior to internal disposition while ignoring external situations. However, when a person simultaneously attributes *someone else's* behavior to internal character flaws (observer role) but their *own* identical behavior to external situational pressures (actor role), the comparative phenomenon is specifically the actor-observer bias."
    },
    {
        "q": "On a computer display, an array of visual stimuli is presented where alternating vertical columns of black squares and white circles are immediately perceived as vertical stripes rather than horizontal rows. In another quadrant, a broken circular contour with three small missing gaps is instantaneously perceived as a complete circle. Which Gestalt principles govern these two perceptual phenomena, respectively?",
        "d": True,
        "ch": [
            "Principle of Proximity and Principle of Continuity",
            "Principle of Similarity and Principle of Closure",
            "Principle of Symmetry and Principle of Common Fate",
            "Principle of Closure and Principle of Similarity"
        ],
        "a": 1,
        "e": "<strong>Similarity groups items that share physical attributes; Closure completes incomplete visual boundaries.</strong> The visual system organizes items sharing color and shape (black squares vs white circles) into distinct columnar units via the Law of Similarity. The perceptual tendency to fill in gaps and perceive broken contours as an intact, continuous geometric object is the Law of Closure. Choice D inverts the order."
    },
    {
        "q": "A clinical patient experiences sudden diaphoresis and tachycardia following an injection of epinephrine. The patient glances at the physician calmly reviewing lab results and concludes, &ldquo;My pulse is elevated, but the doctor is completely calm, so I am merely feeling mild medication side effects rather than experiencing a panic attack.&rdquo; Which theory of emotion best accounts for the patient's emotional interpretation?",
        "d": True,
        "ch": [
            "James-Lange theory",
            "Cannon-Bard theory",
            "Schachter-Singer two-factor theory",
            "Lazarus cognitive-mediational theory"
        ],
        "a": 2,
        "e": "<strong>The Schachter-Singer two-factor theory requires physiological arousal PLUS cognitive appraisal of context.</strong> Schachter and Singer demonstrated that emotional experience is not determined by physiological arousal alone (as James-Lange posits), but requires an explicit cognitive label derived from evaluating the environmental context. Here, somatic arousal (tachycardia) paired with situational appraisal of the calm physician leads the patient to label the state as a benign physical side effect rather than fear/panic."
    },
    {
        "q": "According to George Herbert Mead's sociological theory of the social self and symbolic interactionism, how do the &ldquo;I&rdquo; and the &ldquo;Me&rdquo; interact when an exhausted medical student considers skipping a mandatory morning rounds presentation?",
        "d": True,
        "ch": [
            "The 'I' represents the spontaneous, impulsive desire to sleep, while the 'Me' represents the internalized professional norms and expectations of the healthcare community.",
            "The 'Me' represents the impulsive, uncoordinated biological drive, while the 'I' acts as the socialized moral censor.",
            "Both the 'I' and the 'Me' represent internalized societal expectations, while the biological Id represents the self.",
            "The 'I' is formed during the game stage through the generalized other, whereas the 'Me' is present at birth."
        ],
        "a": 0,
        "e": "<strong>Mead's 'I' is the spontaneous, acting self; the 'Me' is the socialized, reflective self.</strong> In Mead's framework, the 'Me' is the organized set of attitudes, expectations, and societal norms internalized from the 'generalized other' (the socialized self: 'A professional physician does not abandon rounds'). The 'I' is the spontaneous, creative, autonomous, and individual response to the 'Me' (the impulsive desire: 'I am exhausted and want to sleep'). The 'Me' constrains and socializes the 'I.'"
    },
    {
        "q": "Which scenario represents institutional discrimination rather than individual discrimination?",
        "d": True,
        "ch": [
            "An individual landlord refuses to lease an apartment to an immigrant family due to personal xenophobic prejudice.",
            "A municipal banking algorithm automatically disqualifies mortgage applicants lacking a 5-year unbroken history of residential address stability, disproportionately rejecting low-income minority renters despite loan officers holding no racial bias.",
            "A retail store cashier deliberately gives incorrect change to customers whose religious attire differs from her own.",
            "A physician unconsciously spends less time listening to an elderly patient due to personal ageist stereotypes."
        ],
        "a": 1,
        "e": "<strong>Institutional discrimination is systemic and encoded into policies, regulations, or algorithms.</strong> Individual discrimination (Choices A, C, and D) involves isolated, interpersonal biased actions executed by specific individuals based on personal prejudice. Institutional discrimination refers to organizational, governmental, or algorithmic policies that systematically disadvantage a protected group, operating independently of the personal prejudices of individual employees."
    },
    {
        "q": "Which example best captures the fundamental physiological distinction between sensory adaptation and habituation?",
        "d": True,
        "ch": [
            "Sensory adaptation involves central nervous system cognitive disengagement, whereas habituation involves mechanical fatigue of somatic skeletal muscles.",
            "Sensory adaptation involves a decrease in peripheral receptor sensitivity to an unvarying physical stimulus, whereas habituation involves a central cognitive decrease in behavioral responsiveness to a repeated stimulus.",
            "Sensory adaptation occurs exclusively within the autonomic sympathetic nervous system, whereas habituation occurs only in the retina.",
            "Habituation requires surgical ablation of the thalamus, whereas sensory adaptation occurs spontaneously in all glial cells."
        ],
        "a": 1,
        "e": "<strong>Sensory adaptation is peripheral receptor attenuation; habituation is central cognitive learning.</strong> Sensory adaptation occurs at the level of sensory receptors (e.g., skin thermoreceptors firing fewer action potentials after remaining submerged in warm water). Habituation is a central, cognitive/behavioral form of non-associative learning where the brain learns to ignore a repeated, non-threatening stimulus (e.g., ceasing to notice the loud hum of a ventilation unit while studying), though the peripheral sensory receptors are still transducing the physical waves."
    }
]

# Assemble all 7 passages + discretes
all_sets = [
    {
        "id": "exam_ps90_p1",
        "sec": "P/S",
        "topic": "Signal Detection Theory in radiology mammography",
        "sheet": 51,
        "label": "Psychological, Social, and Biological Foundations of Behavior",
        "examId": "ps90",
        "passage": p1_html,
        "qs": p1_qs
    },
    {
        "id": "exam_ps90_p2",
        "sec": "P/S",
        "topic": "Stereotype threat, working memory capacity, and cortisol biomarkers",
        "sheet": 53,
        "label": "Psychological, Social, and Biological Foundations of Behavior",
        "examId": "ps90",
        "passage": p2_html,
        "qs": p2_qs
    },
    {
        "id": "exam_ps90_p3",
        "sec": "P/S",
        "topic": "Fundamental Cause Theory, residential segregation, and weathering",
        "sheet": 61,
        "label": "Psychological, Social, and Biological Foundations of Behavior",
        "examId": "ps90",
        "passage": p3_html,
        "qs": p3_qs
    },
    {
        "id": "exam_ps90_p4",
        "sec": "P/S",
        "topic": "Elaboration Likelihood Model and cognitive dissonance in persuasion",
        "sheet": 59,
        "label": "Psychological, Social, and Biological Foundations of Behavior",
        "examId": "ps90",
        "passage": p4_html,
        "qs": p4_qs
    },
    {
        "id": "exam_ps90_p5",
        "sec": "P/S",
        "topic": "Operant conditioning schedules and incentive-sensitization in addiction",
        "sheet": 54,
        "label": "Psychological, Social, and Biological Foundations of Behavior",
        "examId": "ps90",
        "passage": p5_html,
        "qs": p5_qs
    },
    {
        "id": "exam_ps90_p6",
        "sec": "P/S",
        "topic": "Schizophrenia neurobiology, dopaminergic pathways, and antipsychotics",
        "sheet": 58,
        "label": "Psychological, Social, and Biological Foundations of Behavior",
        "examId": "ps90",
        "passage": p6_html,
        "qs": p6_qs
    },
    {
        "id": "exam_ps90_p7",
        "sec": "P/S",
        "topic": "Dramaturgical perspective, impression management, and role dynamics",
        "sheet": 60,
        "label": "Psychological, Social, and Biological Foundations of Behavior",
        "examId": "ps90",
        "passage": p7_html,
        "qs": p7_qs
    },
    {
        "id": "exam_ps90_discretes",
        "sec": "P/S",
        "topic": "P/S Standalone Discrete Questions",
        "sheet": None,
        "label": "Psychological, Social, and Biological Foundations of Behavior",
        "examId": "ps90",
        "passage": "",
        "qs": ps_discretes
    }
]

total_qs = sum(len(s["qs"]) for s in all_sets)
print(f"Total P/S questions assembled: {total_qs}")

# Write to /home/cgslinde/DrillRoom/DrillRoom/exam_ps90.js
js_content = "/* ---- exam_ps90.js ---- */\n/* Full 90-minute Psych/Soc practice section: 7 passages (42 Qs) + 10 discrete Qs = 52 Qs */\nconst EXAM_PS90 = " + json.dumps(all_sets, indent=2) + ";\n"
with open("/home/cgslinde/DrillRoom/DrillRoom/exam_ps90.js", "w") as f:
    f.write(js_content)

print("exam_ps90.js written successfully!")
