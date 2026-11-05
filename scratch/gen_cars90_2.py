import json

# Define the 9 CARS passages and questions for Exam 2
passages = []

# ==============================================================================
# PASSAGE 1: Bioethics & Crisis Standards of Care
# ==============================================================================
p1_html = """<div class="ttl">Passage 1 (Questions 1&ndash;6)</div>
<p>During catastrophic public health emergencies, acute shortages of critical medical infrastructure&mdash;such as mechanical ventilators, hemodialysis machines, and extracorporeal membrane oxygenation (ECMO) circuits&mdash;compel health systems to transition from standard patient-centered clinical care to population-based crisis standards of care. In ordinary clinical medicine, deontological principles predominate: physicians maintain a fiduciary obligation to advocate exclusively for the best interests of the individual patient before them, strictly bound by duties of non-maleficence and autonomy. In contrast, crisis triage frameworks mandate a utilitarian reallocation, where the moral imperative shifts to maximizing aggregate population survival, quantified as life-years saved or post-discharge long-term survivability.</p>
<p>To operationalize this transition without subjecting bedside clinicians to moral injury, bioethicists advocate establishing independent triage committees that employ objective scoring algorithms, such as the Sequential Organ Failure Assessment (SOFA). However, the uncritical deployment of organ-failure scoring metrics has precipitated severe ethical critiques from disability rights advocates and critical race theorists. Algorithms that incorporate baseline comorbidities or projected long-term life expectancy systematically disadvantage individuals with preexisting chronic disabilities and marginalized racial populations who bear a disproportionate burden of structural health inequities. Consequently, an algorithm designed to be mathematically neutral frequently codifies and amplifies historical systemic disadvantage under the veneer of clinical objectivity.</p>
<p>In response, revisionist triage frameworks propose multi-principle allocation schemes that balance the utilitarian preservation of life-years with egalitarian correctives, such as weighted lottery systems or "area deprivation index" priority adjustments. Furthermore, bioethicists invoke the classical philosophical <i>Doctrine of Double Effect</i> to navigate the withdrawal of life-sustaining treatment from deteriorating patients to reallocate equipment to patients with higher prognostic utility. This doctrine holds that an action with foreseeable harmful consequences (e.g., patient demise following ventilator extubation) is morally permissible if the primary intention is achieving a proportionate good (saving a viable life), the harmful effect is not the chosen means to the good end, and no less injurious alternative exists.</p>"""

p1_qs = [
    {
        "q": "The primary purpose of the passage is to:",
        "ch": [
            "advocate for the immediate abolition of organ-failure scoring metrics in emergency critical care triage.",
            "analyze the ethical shift from deontological patient advocacy to utilitarian triage and the challenges of equitable allocation.",
            "prove that the Doctrine of Double Effect is unworkable in acute intensive care environments.",
            "demonstrate that bedside physicians should make all triage decisions without administrative interference."
        ],
        "a": 1,
        "e": "<strong>Paragraphs 1&ndash;3 trace the systemic transition from deontological individual care to utilitarian population allocation, evaluate algorithmic equity concerns, and examine proposed bioethical compromises.</strong> Choice A is too extreme (the author examines reform frameworks rather than urging total abolition). Choice C asserts the exact opposite of paragraph 3. Choice D contradicts paragraph 2, which emphasizes establishing independent triage teams to shield bedside clinicians from moral distress."
    },
    {
        "q": "Based on the passage, the ethical tension between ordinary clinical practice and crisis standards of care arises primarily because:",
        "ch": [
            "physicians in crisis scenarios abandon all ethical codes in favor of arbitrary clinical decisions.",
            "bedside physicians refuse to follow institutional protocols during emergency shortages.",
            "crisis triage shifts the core ethical mandate from individual fiduciary duty to aggregate population utility.",
            "organ-failure scoring algorithms fail to assess physiological parameters with mathematical reliability."
        ],
        "a": 2,
        "e": "<strong>Paragraph 1 explicitly identifies the fundamental ethical divergence:</strong> ordinary care operates under a deontological, individual fiduciary duty, whereas crisis care subordinates individual advocacy to the utilitarian goal of maximizing aggregate population survival. Choice A and B invent unprofessional behavior unmentioned in the text. Choice D misidentifies the criticism: critics challenge the equity and social bias of the metrics, not their basic mathematical scoring consistency."
    },
    {
        "q": "According to the passage, disability rights advocates object to utilizing long-term life expectancy projections in triage algorithms because such metrics:",
        "ch": [
            "undermine the authority of independent triage committees to modify clinical scoring systems.",
            "systematically convert existing socioeconomic and chronic physiological disadvantages into lower priority scores.",
            "prevent clinicians from administering palliative comfort measures to terminally ill patients.",
            "violate the requirements of the Doctrine of Double Effect by intending patient harm."
        ],
        "a": 1,
        "e": "<strong>Paragraph 2 states that incorporating baseline comorbidities and life expectancy systematically disadvantages patients with preexisting disabilities and structural inequities,</strong> transforming preexisting health disparities into institutional deprioritization. Choice A is an irrelevant administrative distraction. Choice C is contradicted by standard palliative protocols. Choice D misapplies the Doctrine of Double Effect, which governs withdrawal rather than the algorithm's disability critique."
    },
    {
        "q": "Which of the following scenarios best exemplifies an application of the Doctrine of Double Effect as described in paragraph 3?",
        "ch": [
            "A physician administers lethal potassium chloride to a patient to free up a hospital bed for an incoming trauma victim.",
            "A triage team reallocates an ECMO circuit to a patient with higher prognostic survival, foreseeing the donor patient's death without intending it as the means.",
            "An administrator selects triage candidates using an unweighted lottery to avoid evaluating clinical comorbidities.",
            "A clinician ignores organ failure scores to prioritize personal acquaintances during an equipment shortage."
        ],
        "a": 1,
        "e": "<strong>The Doctrine of Double Effect allows an action where harm is a foreseen side effect but not the intended means or end.</strong> In Choice B, extubating a non-surviving patient to save a viable patient foresees death as an unavoidable outcome, whereas the intent is preserving viable life. Choice A represents active intentional euthanasia (harm as direct means), which the doctrine strictly forbids. Choices C and D do not involve the double-effect framework."
    },
    {
        "q": "The author's reference to 'area deprivation index' priority adjustments in paragraph 3 serves primarily to illustrate:",
        "ch": [
            "a mechanism designed to counterbalance structural disparities embedded in conventional clinical scoring systems.",
            "a method for eliminating the necessity of human decision-making in hospital crisis committees.",
            "a historical justification for preserving pure utilitarian allocation schemes during pandemics.",
            "an empirical proof that socioeconomic factors determine individual genetic susceptibility to trauma."
        ],
        "a": 0,
        "e": "<strong>Paragraph 3 introduces egalitarian correctives (like area deprivation index adjustments) as tools to mitigate the disproportionate disadvantage that purely physiological/utilitarian metrics impose on marginalized communities.</strong> Choice B overstates the tool into fully autonomous automation. Choice C inverts the author's logic: it modifies rather than preserves pure utilitarian allocation. Choice D introduces an unfounded biological genetic claim."
    },
    {
        "q": "If a hospital implemented a triage protocol that relied exclusively on chronological age cutoffs, the author of the passage would most likely view this policy as:",
        "ch": [
            "an optimal fulfillment of deontological bedside advocacy principles.",
            "a flawed heuristic that exacerbates equity concerns by substituting an arbitrary demographic proxy for nuanced prognostic evaluation.",
            "the only legally defensible application of the classical Doctrine of Double Effect.",
            "a scientifically rigorous methodology that completely eliminates disparate racial outcomes."
        ],
        "a": 1,
        "e": "<strong>Throughout paragraph 2, the author criticizes crude proxy variables that disproportionately penalize vulnerable cohorts.</strong> A rigid chronological age cutoff functions as a blunt heuristic that magnifies structural discrimination without evaluating nuanced individualized recovery potential. Choice A confuses deontological care with age-based restriction. Choice C misapplies double effect. Choice D is contradicted by epidemiological evidence on health disparities."
    }
]

passages.append({
    "id": "exam_cars90_2_p1",
    "sec": "CARS",
    "topic": "Bioethics & Crisis Standards of Care",
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_2",
    "passage": p1_html,
    "qs": p1_qs
})

print("Passage 1 defined.")

# ==============================================================================
# PASSAGE 2: Ludwig Wittgenstein — Language Games & Private Language
# ==============================================================================
p2_html = """<div class="ttl">Passage 2 (Questions 7&ndash;12)</div>
<p>In his early philosophical treatise, the <i>Tractatus Logico-Philosophicus</i>, Ludwig Wittgenstein championed the "picture theory of language," asserting that meaningful propositions mirror empirical reality through logical isomorphism. Under this early paradigm, language serves as an exact symbolic calculus: words denote discrete worldly objects, and propositional syntax maps the spatial and logical configurations of facts. However, in his mature posthumous masterpiece, the <i>Philosophical Investigations</i>, Wittgenstein dramatically repudiated this rigid referential model, diagnosing it as a seductive philosophical illusion rooted in our craving for metaphysical unity.</p>
<p>In its stead, the later Wittgenstein introduced the concept of the <i>Sprachspiel</i> or "language-game." Language, he argued, is not a unified formal calculus anchored in transcendental logic; rather, it is an open-ended multiplicity of dynamic human activities, interwoven into shared cultural forms of life (<i>Lebensformen</i>). Meaning is not a mysterious metaphysical essence that an ethereal mind attaches to a phonetic token, nor is it merely the material object to which a noun points. Instead, Wittgenstein famously proclaimed: "the meaning of a word is its use in the language." Asking for the meaning of a word in the abstract is as futile as asking for the universal value of a chess piece detached from the programmed rules, tactical objectives, and physical moves of a game of chess.</p>
<p>To dismantle Cartesian mentalism once and for all, Wittgenstein constructed the celebrated <i>Private Language Argument</i>. Traditional epistemologies, from Descartes to the British empiricists, posited that mental states (such as acute physical pain or sensory perceptions) are privileged, private interior objects immediately accessible only to the solitary introspective subject, who subsequently invents private linguistic tokens to label them. Wittgenstein demonstrated that a purely private language&mdash;whose words refer to what only the solitary speaker can experience and whose meanings cannot be communicated to another&mdash;is logically impossible. Language fundamentally requires a distinction between <i>being right</i> and merely <i>thinking one is right</i>. A solitary private linguist possess no external public criterion of correctness, no independent benchmark to verify that a private sensation experienced today is identical to the sensation labeled yesterday. Lacking a public grammar established through shared social interaction, the private linguist is reduced to an individual who purchases several copies of the morning newspaper to verify the accuracy of the front-page headline.</p>"""

p2_qs = [
    {
        "q": "The primary shift from Wittgenstein's early philosophy in the Tractatus to his later philosophy in the Investigations can best be characterized as a transition from:",
        "ch": [
            "an empirical theory of physical perception to a solipsistic doctrine of private introspection.",
            "a formal referential model of language to a pragmatic, socially embedded theory of linguistic usage.",
            "an ethical defense of religious mysticism to an analytical verification of biological sciences.",
            "a psychological investigation of inner emotion to an algorithmic analysis of formal grammar."
        ],
        "a": 1,
        "e": "<strong>Paragraphs 1 and 2 explicitly contrast the early referential 'picture theory' (words denotatively mirroring worldly objects via formal logic) with the later 'language-game' model (meaning defined by contextual usage within shared human forms of life).</strong> Choice A is backward (the later philosophy explicitly refutes private introspection). Choices C and D introduce irrelevant disciplines unaddressed in the text."
    },
    {
        "q": "The author introduces the analogy of a chess piece in paragraph 2 primarily in order to emphasize that:",
        "ch": [
            "linguistic rules are rigidly codified and cannot evolve across cultural contexts.",
            "the significance of a word is determined entirely by its function within an interactive system of rules.",
            "intellectual debate resembles competitive game play rather than cooperative communication.",
            "spoken vocabulary must be taught through formal didactic instruction rather than natural imitation."
        ],
        "a": 1,
        "e": "<strong>Paragraph 2 explains that words, like chess pieces, lack inherent meaning when isolated; their value and meaning arise solely from their functional role within the governing rules of the game.</strong> Choice A contradicts the passage's characterization of language as an open-ended multiplicity. Choice C introduces competitive rivalry not supported by the analogy. Choice D is an extrapolation unsupported by the text."
    },
    {
        "q": "According to the passage, the Private Language Argument refutes Cartesian mentalism primarily by demonstrating that:",
        "ch": [
            "private sensory sensations are purely imaginary and do not possess biological reality.",
            "solitary introspective speakers always misdiagnose their physiological neurological states.",
            "a genuine standard of linguistic correctness requires public criteria and shared social grammar.",
            "introspective meditation weakens an individual's capacity to master complex grammatical syntax."
        ],
        "a": 2,
        "e": "<strong>Paragraph 3 argues that a private language is impossible because it lacks an independent, external standard to distinguish between 'being right' and merely 'thinking one is right'; genuine meaning requires public criteria established through social interaction.</strong> Choice A is a false extrapolation (Wittgenstein does not deny that people feel pain). Choices B and D introduce unfounded cognitive claims."
    },
    {
        "q": "The closing metaphor of an individual purchasing multiple copies of the morning newspaper (paragraph 3) serves to illustrate:",
        "ch": [
            "the redundant, circular nature of attempting to validate an internal rule without an independent public benchmark.",
            "the economic dependence of mass communication media on repetitive consumer purchasing habits.",
            "the vulnerability of democratic institutions to coordinated journalistic misinformation campaigns.",
            "the human tendency to seek cognitive confirmation when evaluating political controversies."
        ],
        "a": 0,
        "e": "<strong>The metaphor illustrates the absurdity of self-verification:</strong> buying multiple copies of the same newspaper does not independently confirm the story, just as checking one's private memory against another private memory provides no independent validation of a linguistic rule. Choices B, C, and D misread the philosophical epistemological metaphor as literal media commentary."
    },
    {
        "q": "Which of the following linguistic practices best exemplifies a 'language-game' as conceived by the later Wittgenstein?",
        "ch": [
            "A dictionary editor recording the etymological origins of ancient Latin prefixes.",
            "A carpenter calling out 'Slab!' to an assistant who retrieves and positions a stone in a building site.",
            "A solitary hermit recording invented numerical symbols in a private diary to denote private mood shifts.",
            "A software engineer writing binary code that executes exclusively on an isolated mainframe computer."
        ],
        "a": 1,
        "e": "<strong>Wittgenstein's classic example of a language-game is a builder calling out commands ('Slab!', 'Block!') where language is directly interwoven into collaborative physical action within a shared form of life.</strong> Choice C represents the exact private language model Wittgenstein refutes. Choices A and D represent abstract or isolated coding rather than socially embedded linguistic usage."
    },
    {
        "q": "Based on the passage, the author would most likely AGREE with which of the following assertions regarding language?",
        "ch": [
            "Philosophical confusion frequently arises when words are abstracted from their active functional contexts.",
            "All human languages share an innate, immutable logical structure embedded in human neuroanatomy.",
            "The primary objective of linguistic philosophy is to construct an ideal, flawless mathematical vocabulary.",
            "Sensory perceptions provide the only legitimate epistemological foundation for empirical truth."
        ],
        "a": 0,
        "e": "<strong>Paragraphs 1 and 2 emphasize that philosophical illusions arise when language is detached from its contextual use in human life and treated as an abstract metaphysical calculus.</strong> Choice B represents Chomskyan nativism, which contrasts with Wittgenstein's contextual pluralism. Choice C reflects the early Tractarian goal that Wittgenstein explicitly repudiated. Choice D represents classic British empiricism, which Wittgenstein critiqued."
    }
]

passages.append({
    "id": "exam_cars90_2_p2",
    "sec": "CARS",
    "topic": "Ludwig Wittgenstein — Language Games & Private Language",
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_2",
    "passage": p2_html,
    "qs": p2_qs
})

print("Passage 2 defined.")

# ==============================================================================
# PASSAGE 3: Aristotle — Virtue Ethics & Eudaimonia
# ==============================================================================
p3_html = """<div class="ttl">Passage 3 (Questions 13&ndash;18)</div>
<p>Modern moral philosophy is largely polarized between two dominant normative architectures: Kantian deontology, which grounds ethics in universalizable duties and categorical imperatives, and Benthamite utilitarianism, which evaluates the moral worth of actions solely by their aggregated hedonic consequences. Despite their profound theoretical antagonisms, both frameworks share an underlying modern prejudice: they conceptualize ethics as an external algorithmic decision procedure. Both ask: <i>"What act is it my duty to perform right now?"</i> In doing so, both reduce moral life to episodic, courtroom-like adjudications of isolated dilemmas, detaching moral evaluation from the lifelong development of human character.</p>
<p>In sharp contrast, the classical virtue ethics of Aristotle begins not with discrete dilemmas, but with a foundational teleological inquiry: <i>"What constitutes a life well-lived?"</i> For Aristotle, all human activities aim at some perceived good, and this hierarchy of ends culminates in <i>eudaimonia</i>&mdash;a term inadequately translated as "happiness," but more accurately denoting holistic human flourishing, active self-realization, and objective excellence. Eudaimonia is not a fleeting emotional state of subjective pleasure, nor is it a static credential one acquires. It is an enduring, structured activity of the soul (<i>energeia</i>) in accordance with rational virtue (<i>arete</i>) over a complete life.</p>
<p>Aristotle posited that moral virtues are not innate biological endowments, nor are they abstract intellectual formulas acquired through book study. Rather, virtues of character (such as courage, temperance, and justice) are stable behavioral dispositions (<i>hexeis</i>) cultivated through habituation (<i>ethismos</i>). We become just by repeatedly performing just acts, just as an apprentice becomes an accomplished harpist by practicing the harp. Central to this moral architecture is the doctrine of the <i>golden mean</i>: virtue is a harmonious mean between the vices of deficiency and excess, tailored to the specific agent and context. Courage, for example, is the calibrated mean between the reckless excess of foolhardiness and the paralyzing deficiency of cowardice. Determining this mean requires <i>phronesis</i>&mdash;practical wisdom&mdash;a seasoned perceptual capacity that cannot be codified into rigid rulebooks, but is honed through lived experience, moral mentorship, and reflective deliberation.</p>"""

p3_qs = [
    {
        "q": "According to the author, a fundamental flaw shared by both Kantian deontology and utilitarianism is that they:",
        "ch": [
            "completely reject the concept of objective moral truth in favor of cultural relativism.",
            "reduce ethical deliberation to an episodic, rule-based algorithm detached from enduring character development.",
            "overemphasize the role of emotional habituation at the expense of rational analysis.",
            "refuse to apply moral standards to complex political and legal institutions."
        ],
        "a": 1,
        "e": "<strong>Paragraph 1 explicitly asserts that despite their differences, both deontology and utilitarianism share the flaw of conceptualizing ethics as an external algorithmic decision procedure for isolated dilemmas, ignoring the lifelong cultivation of human character.</strong> Choice A is false (both Kant and Bentham are strong moral objectivists). Choice C inverts the argument. Choice D is an extrapolation unsupported by the text."
    },
    {
        "q": "The author contrasts the modern understanding of 'happiness' with the Greek concept of eudaimonia primarily to show that eudaimonia:",
        "ch": [
            "refers to an objective state of flourishing realized through virtuous activity rather than transient subjective pleasure.",
            "is an unachievable utopian ideal that ancient philosophers used solely for rhetorical debate.",
            "can be acquired instantly through an intense intellectual revelation without habituation.",
            "is identical to the utilitarian maximization of hedonic gratification across a population."
        ],
        "a": 0,
        "e": "<strong>Paragraph 2 clarifies that eudaimonia is not a fleeting emotional feeling or subjective pleasure, but an enduring, objective state of active self-realization and human flourishing achieved through rational virtue over a complete life.</strong> Choice B is contradicted by Aristotle's practical framework. Choice C contradicts the emphasis on lifelong habituation. Choice D contradicts the distinction between Aristotelian flourishing and utilitarian hedonic calculation."
    },
    {
        "q": "The analogy of learning to play the harp in paragraph 3 is used to illustrate the idea that moral virtue:",
        "ch": [
            "is an inherent genetic talent possessed only by an artistic aristocracy.",
            "requires rigid obedience to immutable religious scriptures.",
            "is developed through repeated practice and active habituation rather than passive intellectual study.",
            "depends entirely on emotional catharsis and spontaneous impulse."
        ],
        "a": 2,
        "e": "<strong>Paragraph 3 explicitly uses the harpist analogy to explain habituation: 'We become just by repeatedly performing just acts, just as an apprentice becomes an accomplished harpist by practicing the harp.'</strong> Choice A introduces genetic determinism refuted by Aristotle's habituation model. Choice B introduces religious dogma unmentioned in the text. Choice D contradicts rational habituation."
    },
    {
        "q": "Which of the following scenarios best demonstrates the Aristotelian concept of the 'golden mean' regarding financial generosity?",
        "ch": [
            "An individual gives away all personal savings without regard for family sustenance, resulting in bankruptcy.",
            "A wealthy donor gives proportioned donations to verified community charities while maintaining stable personal reserves.",
            "An individual hoards all surplus capital in offshore accounts, refusing to contribute to public welfare.",
            "A citizen delegates all charitable decisions to an automated lottery algorithm."
        ],
        "a": 1,
        "e": "<strong>The golden mean represents a harmonious balance between excess and deficiency:</strong> generosity is the mean between prodigality/recklessness (giving away everything heedlessly, Choice A) and stinginess/miserliness (hoarding everything, Choice C). Choice B represents the calibrated, virtuous mean. Choice D represents algorithmic detachment."
    },
    {
        "q": "According to the passage, phronesis (practical wisdom) differs from abstract moral rules because phronesis:",
        "ch": [
            "operates as a rigid, universal formula applicable to all situations without modification.",
            "is an intuitive perceptual capacity developed through lived experience and contextual deliberation.",
            "rejects any distinction between noble virtues and destructive vices.",
            "can be fully codified into elementary educational handbooks."
        ],
        "a": 1,
        "e": "<strong>Paragraph 3 describes phronesis as a seasoned perceptual capacity honed through lived experience and mentorship that cannot be reduced to rigid rulebooks or codified formulas.</strong> Choices A and D assert the exact opposite of what the passage states. Choice C is a mischaracterization of virtue ethics."
    },
    {
        "q": "Based on the passage, if a modern healthcare organization wanted to structure its clinical training around Aristotelian virtue ethics, it would prioritize:",
        "ch": [
            "requiring medical students to memorize utilitarian mathematical optimization algorithms.",
            "fostering longitudinal mentorship, reflective bedside practice, and the habituation of clinical empathy and prudence.",
            "relying exclusively on automated artificial intelligence diagnostic scoring to eliminate physician discretion.",
            "imposing severe legal financial penalties for minor procedural documentation deviations."
        ],
        "a": 1,
        "e": "<strong>An Aristotelian training model focuses on habituation through practice, moral mentorship, and developing phronesis (practical wisdom and sound clinical judgment) over time.</strong> Choice A reflects the utilitarian algorithmic approach critiqued in paragraph 1. Choices C and D represent detached technocratic and punitive models that ignore character development."
    }
]

passages.append({
    "id": "exam_cars90_2_p3",
    "sec": "CARS",
    "topic": "Aristotle — Virtue Ethics & Eudaimonia",
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_2",
    "passage": p3_html,
    "qs": p3_qs
})

print("Passage 3 defined.")

# ==============================================================================
# PASSAGE 4: Edmund Burke & Kant — The Aesthetic Sublime
# ==============================================================================
p4_html = """<div class="ttl">Passage 4 (Questions 19&ndash;24)</div>
<p>In eighteenth-century aesthetic theory, a decisive intellectual revolution occurred when thinkers decoupled the concept of aesthetic appreciation from mere harmony, symmetry, and classical beauty. In his landmark 1757 treatise, <i>A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful</i>, Edmund Burke established a foundational psychological dichotomy. Beauty, Burke argued, is grounded in feelings of affection, tenderness, and pleasure, evoked by objects that are comparatively small, smooth, polished, and gently curved. In diametrical contrast, the <i>sublime</i> is rooted in the visceral passion of terror&mdash;specifically, our instinct for self-preservation aroused by sensations of vastness, infinity, obscurity, power, and overwhelming magnitude.</p>
<p>Burke emphasized that the sublime does not evoke unmitigated, paralyzing dread, but rather a paradoxical emotional phenomenon he termed "delightful horror." This complex aesthetic transport occurs exclusively when an observer perceives a terrifying spectacle&mdash;such as a violent oceanic tempest, a sheer precipice, or a catastrophic volcanic eruption&mdash;from a vantage of physical safety. When danger presses too closely, terror is simply noxious and incapacitating; but when experienced at a psychological remove, the contemplation of overwhelming danger produces an intense physiological dilation of the nerves, purging the mind through sublime awe.</p>
<p>Three decades later, in the <i>Critique of Judgment</i>, Immanuel Kant radically internalized and intellectualized Burke's empirical psychology. For Kant, the sublime does not reside in the physical object itself&mdash;the tempest or the abyss is merely raw chaotic nature. Rather, the sublime is an extraordinary intellectual confrontation occurring within human consciousness. Kant distinguished between the <i>mathematical sublime</i> (provoked by infinite magnitude, such as the starry heavens) and the <i>dynamical sublime</i> (provoked by overwhelming physical power, such as raging avalanches). When confronted with vast nature, our sensory imagination collapses, overwhelmed by its inability to synthesize the infinite totality. Yet, in that precise moment of sensory defeat, human reason awakens, discovering within itself a transcendent, supersensible moral capacity that exceeds anything in sensible nature. The sublime is thus our revelation of human intellectual and moral supremacy over the material universe.</p>"""

p4_qs = [
    {
        "q": "The primary distinction between the beautiful and the sublime according to Edmund Burke is that:",
        "ch": [
            "the beautiful is an illusion created by modern society, whereas the sublime reflects divine scripture.",
            "the beautiful is grounded in pleasure and tenderness, whereas the sublime is rooted in self-preservation and terror experienced safely.",
            "the beautiful requires mathematical measurement, whereas the sublime is evaluated through commercial market value.",
            "the beautiful belongs exclusively to the fine arts, whereas the sublime is restricted to architectural structures."
        ],
        "a": 1,
        "e": "<strong>Paragraph 1 explicitly outlines Burke's dichotomy: beauty is grounded in affection, smoothness, and pleasure, while the sublime is rooted in terror, vastness, and the instinct for self-preservation. Paragraph 2 adds that it occurs from a position of safety.</strong> Choices A, C, and D invent theological, economic, and medium distinctions unsupported by the text."
    },
    {
        "q": "Burke's concept of 'delightful horror' (paragraph 2) is dependent upon which of the following conditions?",
        "ch": [
            "The observer must actively engage in physical combat against the threatening natural force.",
            "The threatening spectacle must be observed from a threshold of psychological and physical safety.",
            "The artistic representation must completely eliminate all realistic depictions of danger.",
            "The natural phenomenon must be verified through quantitative scientific instrumentation."
        ],
        "a": 1,
        "e": "<strong>Paragraph 2 states that delightful horror occurs exclusively when the observer perceives an overwhelming or dangerous spectacle from a position of safety, because unmediated proximity produces pure, noxious terror.</strong> Choice A would cause raw panic. Choice C contradicts the requirement of perceived vast danger. Choice D is an irrelevant scientific distraction."
    },
    {
        "q": "According to the passage, Kant's philosophical revision of Burke's theory of the sublime primarily involved:",
        "ch": [
            "shifting the locus of the sublime from the external physical object to the internal faculties of human consciousness and reason.",
            "rejecting all distinction between mathematical magnitude and dynamical physical power.",
            "arguing that natural catastrophes prove the complete futility of human intellectual endeavors.",
            "subordinating moral reasoning to the involuntary physiological responses of the nervous system."
        ],
        "a": 0,
        "e": "<strong>Paragraph 3 explains that Kant internalized the sublime: nature is not inherently sublime in itself; rather, the sublime is an intellectual drama in which the failure of sensory imagination reveals the supremacy of human reason and moral capacity over the sensible world.</strong> Choice B is false (Kant explicitly distinguished between the mathematical and dynamical sublime). Choices C and D invert Kant's conclusion regarding human intellectual supremacy."
    },
    {
        "q": "Which of the following scenarios best illustrates Kant's concept of the 'dynamical sublime'?",
        "ch": [
            "A mathematician contemplating the non-terminating decimal expansion of pi while seated at a desk.",
            "A traveler viewing a violent volcanic eruption from a secure cliff, feeling physical vulnerability alongside moral awe.",
            "A museum visitor admiring a smoothly carved marble bust of a classical Roman senator.",
            "A mountaineer experiencing fatal hypothermia and panic during an unpredicted blizzard."
        ],
        "a": 1,
        "e": "<strong>The dynamical sublime involves overwhelming physical power in nature (like volcanic eruptions or avalanches) observed from a safe vantage point where sensory intimidation triggers the realization of human moral reason.</strong> Choice A is closer to the mathematical sublime (infinite magnitude). Choice C represents Burkean/classical beauty. Choice D represents raw unmediated trauma without aesthetic distance."
    },
    {
        "q": "The author's tone in describing the historical development from Burke to Kant can best be described as:",
        "ch": [
            "scornful and dismissive of pre-modern psychological inquiries.",
            "analytical, appreciative, and intellectually nuanced.",
            "dogmatic and rigidly partisan in defense of empirical reductionism.",
            "skeptical of the capacity of philosophical aesthetics to elucidate human emotion."
        ],
        "a": 1,
        "e": "<strong>The author traces the intellectual evolution with precision, objective framing, and clear structural distinctions, highlighting the merits of Burke's empirical psychology and Kant's transcendental internalization.</strong> Choices A and C attribute hostile bias unsupported by the text. Choice D is contradicted by the author's respectful, thorough analysis."
    },
    {
        "q": "Based on the passage, both Burke and Kant would agree that an aesthetic encounter with the sublime:",
        "ch": [
            "transcends ordinary passive pleasure and involves an encounter with overwhelming magnitude or power.",
            "can be fully explained by the mechanical laws of Newtonian classical optics.",
            "is accessible only to professional painters and academic art historians.",
            "requires the complete suppression of human emotional sensitivity."
        ],
        "a": 0,
        "e": "<strong>Both Burke (terror, vastness, delightful horror) and Kant (sensory imagination overwhelmed by vast magnitude or physical power) agree that the sublime is not ordinary comfortable pleasure, but an encounter with overwhelming magnitude or force.</strong> Choices B, C, and D contradict the psychological and transcendental universality argued by both thinkers."
    }
]

passages.append({
    "id": "exam_cars90_2_p4",
    "sec": "CARS",
    "topic": "Edmund Burke & Kant — The Aesthetic Sublime",
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_2",
    "passage": p4_html,
    "qs": p4_qs
})

print("Passage 4 defined.")

# ==============================================================================
# PASSAGE 5: Oliver Wendell Holmes — Legal Realism & The Common Law
# ==============================================================================
p5_html = """<div class="ttl">Passage 5 (Questions 25&ndash;30)</div>
<p>For centuries, classical legal formalism dominated Anglo-American jurisprudence. Formalists conceived of the law as an autonomous, self-contained deductive science. Under this orthodox vision, legal decisions are geometric operations: judges serve as dispassionate intellectual technicians who deduce inevitable verdicts from pre-existing, immutable statutory axioms through formal deductive logic. Law was thought to inhabit a celestial heaven of pure legal concepts, entirely insulated from the messy contingencies of economic struggle, political ideology, and social change.</p>
<p>In 1881, Oliver Wendell Holmes Jr. shattered this conceptual fortress with his revolutionary opening lecture in <i>The Common Law</i>: "The life of the law has not been logic: it has been experience." Holmes argued that judicial decisions are not mechanical syllogisms dictated by pure reason. Rather, legal doctrine reflects the evolving moral prejudices, economic necessities, and social intuitions of dominant political classes across historical epochs. When courts adjudicate novel disputes, judges do not discover eternal truths hidden within precedent; instead, they make pragmatic legislative policy choices, which are subsequently dressed in the respectable vestments of formal deduction to maintain institutional legitimacy.</p>
<p>To demystify moralistic rhetoric in the courtroom, Holmes formulated his famous heuristic: the <i>"bad man theory of law."</i> If one wishes to comprehend what the law actually is, Holmes asserted, one must view it not through the pious eyes of the ethical philosopher, but through the cynical eyes of the bad man. The bad man cares nothing for abstract moral duties, natural rights, or ethical virtue; he cares exclusively for material consequences. To the bad man, a legal duty is nothing more or less than a prediction that if he commits a particular act, the public sovereign force will impose an imprisonment or exact a fine. By stripping legal concepts down to predictive prophecies of state coercion, Holmes inaugurated American Legal Realism, compelling jurists to evaluate legal rules not by their conceptual elegance, but by their empirical social consequences.</p>"""

p5_qs = [
    {
        "q": "The primary purpose of the passage is to:",
        "ch": [
            "prove that all common law judicial decisions are corrupt and devoid of moral value.",
            "contrast classical legal formalism with Holmesian legal realism and its predictive theory of law.",
            "advocate for the complete replacement of human judges with algorithmic decision-making models.",
            "demonstrate that legal education should abandon historical precedent in favor of pure mathematics."
        ],
        "a": 1,
        "e": "<strong>The passage establishes the contrast between the formalist model (law as a deductive, autonomous science) and Holmes's legal realist revolution (law as historical experience, pragmatic policy choice, and predictive coercion).</strong> Choice A overstates Holmes's critique into an accusation of pure corruption. Choices C and D invent proposals unmentioned in the text."
    },
    {
        "q": "According to the passage, legal formalists viewed judicial decisions primarily as:",
        "ch": [
            "pragmatic policy adjustments responsive to socioeconomic inequality.",
            "subconscious manifestations of class bias and economic interest.",
            "deductive, mechanical operations derived logically from established legal axioms.",
            "arbitrary impositions of sovereign power lacking logical coherence."
        ],
        "a": 2,
        "e": "<strong>Paragraph 1 explicitly describes the formalist paradigm: judges act as dispassionate technicians who deduce inevitable verdicts from pre-existing statutory axioms through formal deductive logic.</strong> Choices A and B represent Holmes's realist counter-argument, not the formalist view. Choice D contradicts formalist doctrine."
    },
    {
        "q": "Holmes's assertion that 'The life of the law has not been logic: it has been experience' (paragraph 2) implies that:",
        "ch": [
            "legal doctrine is continually shaped by historical necessities, social beliefs, and political conflict.",
            "judges should disregard all statutory legislation in favor of immediate personal whims.",
            "formal logic has no legitimate application in mathematics or physical sciences.",
            "the common law will inevitably disintegrate as human societies become more complex."
        ],
        "a": 0,
        "e": "<strong>Paragraph 2 explains Holmes's famous aphorism: judicial doctrine reflects evolving moral prejudices, economic necessities, and social intuitions across historical eras rather than abstract syllogistic deduction.</strong> Choice B mischaracterizes realism as pure lawless caprice. Choices C and D are irrelevant extrapolations."
    },
    {
        "q": "The author introduces the 'bad man theory of law' in paragraph 3 primarily to:",
        "ch": [
            "urge courts to impose harsher criminal sentences to deter immoral behavior.",
            "illustrate a functional heuristic that separates legal realities from abstract moralizing.",
            "argue that criminal behavior is an inevitable consequence of socioeconomic stratification.",
            "demonstrate that ethical philosophers make superior trial judges in criminal courts."
        ],
        "a": 1,
        "e": "<strong>Paragraph 3 explains that the 'bad man' perspective strips away pious moral language to reveal what law actually is: an empirical prediction of how the state's coercive force will be deployed.</strong> Choice A mistakes an analytical heuristic for a penal policy proposal. Choice C introduces sociological etiology not discussed. Choice D is contradicted by Holmes's rejection of moralistic jurisprudence."
    },
    {
        "q": "Based on the passage, how would Oliver Wendell Holmes Jr. most likely interpret a judge's citation of centuries-old precedent in a modern economic dispute?",
        "ch": [
            "As definitive proof that the legal dispute was decided by eternal natural laws.",
            "As a rhetorical strategy designed to confer institutional legitimacy upon what is fundamentally a contemporary policy choice.",
            "As an accidental error resulting from the judge's ignorance of contemporary financial markets.",
            "As an unconstitutional violation of the principle of judicial independence."
        ],
        "a": 1,
        "e": "<strong>Paragraph 2 explicitly states that when judges make pragmatic policy choices, they dress them in the respectable vestments of formal deduction and precedent to maintain institutional legitimacy.</strong> Choice A represents the formalist view Holmes rejected. Choices C and D introduce irrelevant criticisms."
    },
    {
        "q": "Which of the following modern legal reforms is most consistent with the tenets of American Legal Realism as presented in the passage?",
        "ch": [
            "Mandating that all judicial rulings cite Latin legal maxims to ensure semantic purity.",
            "Conducting empirical econometric studies to evaluate the actual social consequences of antitrust regulations before revising legal standards.",
            "Requiring trial judges to strictly deduce corporate tax liabilities from seventeenth-century maritime codes.",
            "Banning the introduction of sociological and economic evidence in appellate court arguments."
        ],
        "a": 1,
        "e": "<strong>Legal realism insists that law must be judged by its empirical social and economic consequences rather than conceptual elegance (paragraph 3). Conducting empirical studies on antitrust outcomes directly aligns with this principle.</strong> Choices A, C, and D reflect formalist obsession with rigid deduction and exclusionary doctrine."
    }
]

passages.append({
    "id": "exam_cars90_2_p5",
    "sec": "CARS",
    "topic": "Oliver Wendell Holmes — Legal Realism & The Common Law",
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_2",
    "passage": p5_html,
    "qs": p5_qs
})

print("Passage 5 defined.")

# ==============================================================================
# PASSAGE 6: Shoshana Zuboff — Surveillance Capitalism & Behavioral Modification
# ==============================================================================
p6_html = """<div class="ttl">Passage 6 (Questions 31&ndash;36)</div>
<p>Throughout the industrial era, capitalism expanded by commodifying the tangible world: nature was transformed into real estate, raw materials into manufactured commodities, and human physical labor into an hourly wage. In her monumental critique, <i>The Age of Surveillance Capitalism</i>, social theorist Shoshana Zuboff argues that the digital epoch has inaugurated a radical mutation of market logic. Rather than merely digitalizing conventional commerce, dominant technology conglomerates have pioneered a rogue economic species: surveillance capitalism. This mutation claims human private experience as free raw material for translation into behavioral data.</p>
<p>Under this regime, the foundational digital feedback loop has been subverted. In the early internet era, behavioral data was collected primarily to improve online services (e.g., refining search engine indexing or speeding up page rendering). Zuboff labels this the "behavioral value reinvestment cycle." Today, however, user data is siphoned into a vast, opaque "behavioral surplus" that far exceeds service enhancement. This surplus is channeled into advanced machine-learning pipelines to fabricate "prediction products"&mdash;computational models that forecast what users will click, buy, feel, and do. These prediction products are subsequently traded in lucrative <i>behavioral futures markets</i> to business customers seeking certainty in consumer behavior.</p>
<p>Crucially, Zuboff demonstrates that surveillance capitalism does not terminate at passive prediction; its inexorable economic logic demands <i>behavioral modification</i>. The most profitable prediction is one that is guaranteed. To achieve this, digital architectures deploy automated nudges, algorithmic feeds, variable-ratio psychological conditioning, and targeted social engineering to steer human behavior toward commercial objectives. In doing so, surveillance capitalism expropriates not merely surplus labor, but the foundational bedrock of human freedom: the "right to the future tense" and the sanctuary of individual autonomy. Where totalitarianism aimed to conquer the state and psyche through physical terror, surveillance capitalism conquers society through ubiquitous digital architectures of behavioral modification, transforming democratic citizens into predictable consumer nodes.</p>"""

p6_qs = [
    {
        "q": "The primary thesis of the passage is that surveillance capitalism:",
        "ch": [
            "has democratized global commerce by providing free search engines and communication platforms to all citizens.",
            "represents an unprecedented mutation of market logic that extracts human experience as behavioral surplus to predict and modify behavior.",
            "is simply traditional industrial capitalism accelerated by faster computer microprocessors.",
            "will inevitably collapse because consumers refuse to use digital communication technologies."
        ],
        "a": 1,
        "e": "<strong>Paragraphs 1&ndash;3 establish that surveillance capitalism is a novel mutation that commodifies private experience as behavioral surplus, trades prediction products in futures markets, and actively modifies human behavior.</strong> Choice A reflects the corporate marketing narrative that Zuboff refutes. Choice C contradicts paragraph 1, which distinguishes it from industrial capitalism. Choice D is an unfounded speculation."
    },
    {
        "q": "According to paragraph 2, the transition from early internet data collection to surveillance capitalism occurred when user data was:",
        "ch": [
            "used exclusively to improve user interface design and software operational speed.",
            "diverted beyond service improvement into a behavioral surplus used to manufacture prediction products.",
            "made completely accessible to public government regulatory oversight committees.",
            "deleted permanently every 24 hours to comply with international privacy treaties."
        ],
        "a": 1,
        "e": "<strong>Paragraph 2 explains the shift from the 'behavioral value reinvestment cycle' (improving service) to the extraction of 'behavioral surplus' channeled into machine learning to fabricate prediction products traded in futures markets.</strong> Choice A describes the early cycle. Choices C and D describe protective practices that do not exist under surveillance capitalism."
    },
    {
        "q": "Zuboff asserts that the ultimate economic trajectory of surveillance capitalism requires 'behavioral modification' (paragraph 3) because:",
        "ch": [
            "software algorithms cannot process raw sensory data without physical hardware adjustments.",
            "guaranteeing behavioral outcomes delivers maximal certainty and profitability in prediction markets.",
            "technology firms are morally committed to eliminating criminal activity across urban centers.",
            "advertisers refuse to purchase data unless consumers explicitly consent to behavioral experiments."
        ],
        "a": 1,
        "e": "<strong>Paragraph 3 explicitly states: 'The most profitable prediction is one that is guaranteed. To achieve this, digital architectures deploy automated nudges... to steer human behavior toward commercial objectives.'</strong> Choice A is a technical distraction. Choice C attributes altruistic motives refuted by the text. Choice D contradicts the passage's emphasis on opaque, non-consensual extraction."
    },
    {
        "q": "The phrase 'the right to the future tense' in paragraph 3 refers to:",
        "ch": [
            "the legal privilege of commercial enterprises to execute speculative financial contracts.",
            "the essential human capacity to act autonomously, make uncoerced choices, and shape one's destiny.",
            "the grammatical ability of artificial intelligence models to conjugate future verb forms.",
            "the constitutional mandate that elections occur on predetermined chronological dates."
        ],
        "a": 1,
        "e": "<strong>Paragraph 3 links the 'right to the future tense' directly to the sanctuary of individual autonomy and human freedom, which is eroded when behavioral modification predetermines and engineers human actions.</strong> Choice A inverts the victim and perpetrator. Choices C and D are literal, nonsensical misreadings."
    },
    {
        "q": "How does Zuboff distinguish surveillance capitalism from historical totalitarianism in paragraph 3?",
        "ch": [
            "Totalitarianism relied on physical violence and state terror, whereas surveillance capitalism operates through ubiquitous, automated digital architectures of behavioral modification.",
            "Totalitarianism operated exclusively in digital spaces, whereas surveillance capitalism controls physical agriculture.",
            "Totalitarianism respected individual consumer privacy, whereas surveillance capitalism abolishes all property.",
            "Totalitarianism was universally profitable for private corporations, whereas surveillance capitalism operates at a financial deficit."
        ],
        "a": 0,
        "e": "<strong>Paragraph 3 states: 'Where totalitarianism aimed to conquer the state and psyche through physical terror, surveillance capitalism conquers society through ubiquitous digital architectures of behavioral modification.'</strong> Choices B, C, and D assert historically and textually absurd claims."
    },
    {
        "q": "Based on the passage, the author would most likely support which of the following policy initiatives?",
        "ch": [
            "Providing subsidies to tech corporations to accelerate algorithmic user behavioral tracking.",
            "Prohibiting the commercial trade of behavioral prediction products and outlawing non-consensual behavioral modification architectures.",
            "Requiring consumers to pay a subscription fee while leaving surveillance tracking systems fully intact.",
            "Eliminating all algorithmic search engines and returning exclusively to printed card catalogs."
        ],
        "a": 1,
        "e": "<strong>Given the severe critique of behavioral surplus extraction, futures markets, and behavioral modification in paragraphs 2 and 3, the author would logically endorse banning the commercial trade of prediction products and algorithmic manipulation.</strong> Choices A and C preserve the exploitative architecture. Choice D is an extreme reactionary overreaction."
    }
]

passages.append({
    "id": "exam_cars90_2_p6",
    "sec": "CARS",
    "topic": "Shoshana Zuboff — Surveillance Capitalism & Behavioral Modification",
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_2",
    "passage": p6_html,
    "qs": p6_qs
})

print("Passages 4, 5, 6 defined.")

# ==============================================================================
# PASSAGE 7: Marcel Mauss — The Gift Economy & Reciprocal Obligation
# ==============================================================================
p7_html = """<div class="ttl">Passage 7 (Questions 37&ndash;42)</div>
<p>In classical and neoclassical economics, the founding myth of human exchange posits <i>Homo economicus</i>: an isolated, hyper-rational individual calculating material self-interest, who initially engages in barter and subsequently invents currency to overcome the friction of the double coincidence of wants. In his foundational 1925 anthropological essay, <i>The Gift</i> (<i>Essai sur le don</i>), French sociologist Marcel Mauss fundamentally shattered this utilitarian myth. Drawing upon extensive ethnographic field accounts from Melanesia, Polynesia, and the Pacific Northwest, Mauss demonstrated that archaic economic systems were never founded upon spot-barter or detached contractual market exchange. Rather, they were organized around systems of competitive, compulsory, and deeply ceremonial gift exchange.</p>
<p>Central to Mauss's analysis is the revelation that the archaic gift is never truly "free" or disinterested. On the contrary, gift exchange is governed by an iron, threefold social obligation: <i>the obligation to give</i>, <i>the obligation to receive</i>, and <i>the obligation to reciprocate</i>. To refuse a proffered gift is to reject the social bond itself, signaling hostile estrangement or an implicit declaration of war. Furthermore, the gift is not an inert physical commodity detached from its donor. In Maori cosmology, for instance, goods possess a vital spiritual power called <i>hau</i>&mdash;the "spirit of the gift"&mdash;which demands return to its origin. To retain another's gift without reciprocating is to risk severe spiritual retribution and social dishonor.</p>
<p>Nowhere was this dynamic more visible than in the <i>potlatch</i> ceremonies of the Kwakiutl and Haida peoples of the Pacific Northwest. In these competitive feasts, rival chiefs vied for social rank, prestige, and political authority by giving away or spectacularly destroying colossal quantities of wealth (such as copper shields, cedar blankets, and canoes). In the potlatch, wealth was not accumulated to store purchasing power, as in Western capitalism; rather, wealth existed solely to be surrendered. The chief who distributed or destroyed the most property established crushing moral and political superiority over rivals, who were bound to reciprocate with interest at a future feast or submit to subservience. Mauss termed this a <i>total social phenomenon</i> (<i>fait social total</i>): an institution that simultaneously fuses economic, legal, religious, kinship, and aesthetic dimensions, proving that economy is fundamentally embedded within human social relations.</p>"""

p7_qs = [
    {
        "q": "The primary objective of Marcel Mauss's analysis in The Gift as presented in the passage is to:",
        "ch": [
            "prove that Western free-market capitalism is the only historically viable economic framework.",
            "refute the utilitarian myth of Homo economicus by demonstrating that archaic exchange is ceremonial, compulsory, and socially embedded.",
            "encourage modern industrial governments to adopt the potlatch as a method of currency regulation.",
            "demonstrate that gift giving in pre-modern societies was entirely voluntary and motivated by pure altruism."
        ],
        "a": 1,
        "e": "<strong>Paragraph 1 explicitly establishes Mauss's purpose: refuting the neoclassical myth of the isolated, utility-maximizing barterer by showing that archaic economies were structured around compulsory, competitive, and socially embedded gift exchanges.</strong> Choice A is backward. Choice C is an absurd policy extrapolation. Choice D contradicts paragraph 2, which explicitly stresses that the gift was never free, disinterested, or purely voluntary."
    },
    {
        "q": "According to paragraph 2, refusal to receive a proffered gift in archaic societies was interpreted primarily as:",
        "ch": [
            "an astute economic calculation to preserve personal material resources.",
            "a violation of religious vows of personal poverty.",
            "a rejection of the social relationship itself, signaling hostility or conflict.",
            "a standard bargaining tactic in competitive trade negotiations."
        ],
        "a": 2,
        "e": "<strong>Paragraph 2 explicitly states: 'To refuse a proffered gift is to reject the social bond itself, signaling hostile estrangement or an implicit declaration of war.'</strong> Choices A and D misapply modern commercial bargaining motives that Mauss explicitly rejects. Choice B introduces irrelevant religious vows."
    },
    {
        "q": "The concept of hau in Maori cosmology is discussed in paragraph 2 primarily to show that:",
        "ch": [
            "archaic gift items were viewed as spiritually bonded to the donor and carried an inherent demand for reciprocity.",
            "Polynesian tribes had developed sophisticated paper currency systems prior to European contact.",
            "material trade was conducted exclusively between immediate biological family members.",
            "religious leaders exercised total dictatorial control over agricultural production."
        ],
        "a": 0,
        "e": "<strong>Paragraph 2 explains hau as the 'spirit of the gift'—a vital force linking the gift to the donor that demands return and punishes failure to reciprocate.</strong> Choices B, C, and D are factual and historical fabrications."
    },
    {
        "q": "Based on the passage, the potlatch ceremonies of the Pacific Northwest (paragraph 3) differed most fundamentally from Western capitalism in that in the potlatch:",
        "ch": [
            "property was exchanged exclusively through anonymous digital banking networks.",
            "wealth derived its primary value from its ceremonial distribution or destruction to gain social prestige rather than its accumulation.",
            "social status was determined solely by the possession of precious metal coinage.",
            "all members of the community maintained perfectly equal material resources."
        ],
        "a": 1,
        "e": "<strong>Paragraph 3 explicitly contrasts the two: in the potlatch, wealth existed solely to be given away or destroyed to establish rank and prestige, whereas in Western capitalism wealth is accumulated to store purchasing power.</strong> Choice A is historically anachronistic. Choice C contradicts the emphasis on non-coin goods (blankets, copper). Choice D is false (the potlatch created intense hierarchy, not equality)."
    },
    {
        "q": "Mauss's characterization of gift exchange as a 'total social phenomenon' (paragraph 3) means that gift exchange:",
        "ch": [
            "operates as an isolated commercial transaction separate from religious or familial ties.",
            "simultaneously integrates economic, legal, religious, kinship, and moral dimensions of society.",
            "is found exclusively among Pacific island populations and nowhere else in human history.",
            "requires the complete elimination of political authority and central leadership."
        ],
        "a": 1,
        "e": "<strong>Paragraph 3 defines 'total social phenomenon' as an institution that simultaneously fuses economic, legal, religious, kinship, and aesthetic dimensions, showing that economy is inseparable from total social fabric.</strong> Choice A states the exact opposite. Choices C and D are refuted by Mauss's comparative cross-cultural approach."
    },
    {
        "q": "If a modern economist argued that all corporate charitable donations are merely calculated public relations moves to boost net profits, Mauss's framework would most likely view this claim as:",
        "ch": [
            "a confirmation that modern charity reflects an ongoing, disguised form of reciprocal social obligation and prestige competition.",
            "absolute proof that classical Homo economicus has always accurately described all human history.",
            "an irrelevant observation that has no connection to institutional social behavior.",
            "a refutation of the concept of the total social phenomenon."
        ],
        "a": 0,
        "e": "<strong>Mauss's core insight is that gifts are never purely disinterested; they are inextricably tied to prestige, social power, and reciprocal obligation. Viewing corporate donations as investments in prestige and obligation aligns with this framework.</strong> Choice B misses Mauss's historical critique. Choices C and D misunderstand the universality of Mauss's social theory."
    }
]

passages.append({
    "id": "exam_cars90_2_p7",
    "sec": "CARS",
    "topic": "Marcel Mauss — The Gift Economy & Reciprocal Obligation",
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_2",
    "passage": p7_html,
    "qs": p7_qs
})

print("Passage 7 defined.")

# ==============================================================================
# PASSAGE 8: Pierre Bourdieu — Cultural Reproduction & Meritocracy
# ==============================================================================
p8_html = """<div class="ttl">Passage 8 (Questions 43&ndash;48)</div>
<p>Modern democratic societies celebrate educational meritocracy as their supreme egalitarian engine. Under this official ideology, the school system functions as an impartial, universal sorting mechanism: students enter an open arena of scholastic competition, and academic credentials are distributed solely on the basis of innate intellectual talent and personal effort. Academic success is celebrated as the personal triumph of the meritorious individual, while scholastic failure is framed as a fair, self-inflicted deficit of ambition or aptitude. By decoupling socioeconomic attainment from the ancestral hereditary titles of feudalism, the meritocratic school legitimizes modern class stratification as natural, rational, and just.</p>
<p>In his landmark sociological works, <i>The Inheritors</i> and <i>Reproduction in Education, Society and Culture</i>, French sociologist Pierre Bourdieu dismantled this meritocratic illusion. Bourdieu argued that the education system does not overcome social inequality; rather, it functions as the primary modern institutional mechanism for <i>cultural reproduction</i>&mdash;the covert intergenerational transmission of class privilege. Central to Bourdieu's critique is his expansion of the concept of capital beyond mere financial wealth. He identified <i>cultural capital</i>: non-financial social assets that exist in three distinct states: <i>embodied</i> (long-lasting dispositions of the mind and body, linguistic fluency, aesthetic taste, and ease of manner), <i>objectified</i> (cultural goods such as books, art, and instruments), and <i>institutionalized</i> (academic credentials and degrees from elite academies).</p>
<p>Crucially, Bourdieu demonstrated that the school curriculum is not culturally neutral. It explicitly presumes and rewards the specific linguistic codes, cultural references, and intellectual mannerisms (the <i>habitus</i>) of the dominant socioeconomic classes. Children from privileged families absorb this embodied cultural capital through effortless, osmotic immersion from birth within the domestic sphere. When these children enter school, their familiar domestic culture is consecrated by educators as natural academic "brilliance" or "talent." Conversely, working-class children arrive at school having to master an alien cultural code. Because the school treats all students as if they started from a position of cultural equality, it converts inherited social privilege into individual academic merit, thereby performing an act of <i>symbolic violence</i>: convincing the disadvantaged that their subordinate position is the legitimate consequence of their own natural intellectual inferiority.</p>"""

p8_qs = [
    {
        "q": "The primary thesis of the passage is that the educational system:",
        "ch": [
            "has successfully eliminated social stratification by awarding degrees strictly on individual merit.",
            "acts as an instrument of cultural reproduction that legitimizes inherited social privilege as natural talent.",
            "fails to teach basic literacy and numeracy due to underfunding in public institutions.",
            "should be abolished and replaced with informal home-based apprenticeship models."
        ],
        "a": 1,
        "e": "<strong>The entire passage develops Bourdieu's argument that the educational system covertly reproduces class privilege by rewarding inherited cultural capital and disguising inherited social advantage as innate individual academic merit.</strong> Choice A describes the meritocratic myth that the passage refutes. Choices C and D introduce irrelevant policy issues unaddressed by Bourdieu."
    },
    {
        "q": "Which of the following best exemplifies 'embodied cultural capital' as defined in paragraph 2?",
        "ch": [
            "A portfolio of municipal bonds inherited from a grandparent.",
            "An effortless command of refined vocabulary, formal cadence, and classical references acquired during childhood.",
            "A framed master's degree certificate hanging in a professional office.",
            "A collection of rare oil paintings stored in a secure gallery vault."
        ],
        "a": 1,
        "e": "<strong>Paragraph 2 defines embodied cultural capital as long-lasting dispositions of the mind and body, linguistic fluency, ease of manner, and aesthetic taste. An effortless command of refined vocabulary and cadence acquired at home is the textbook example.</strong> Choice A is financial capital. Choice C is institutionalized cultural capital. Choice D is objectified cultural capital."
    },
    {
        "q": "According to paragraph 3, the school system commits 'symbolic violence' against working-class children primarily by:",
        "ch": [
            "subjecting them to physical corporal punishment during formal examinations.",
            "consecrating the culture of privileged classes as neutral merit while convincing disadvantaged students that failure reflects personal inferiority.",
            "refusing to allow working-class students to enroll in introductory literacy courses.",
            "requiring all students to wear identical institutional uniforms."
        ],
        "a": 1,
        "e": "<strong>Paragraph 3 explicitly defines symbolic violence in education: by treating culturally privileged domestic habits as natural 'talent' while demanding working-class students decode an alien culture, the school convinces disadvantaged students that their lower academic standing is the legitimate outcome of natural intellectual inferiority.</strong> Choice A is a literal misinterpretation of 'violence'. Choices C and D are factual fabrications."
    },
    {
        "q": "The author contrasts the official meritocratic ideology (paragraph 1) with Bourdieu's sociological critique (paragraphs 2&ndash;3) in order to demonstrate that:",
        "ch": [
            "feudal hereditary titles were morally superior to modern academic credentialing systems.",
            "educational institutions function to disguise the intergenerational transmission of inequality behind a veneer of fairness.",
            "working-class students naturally possess superior artistic instincts compared to wealthy students.",
            "academic standardized testing should be expanded to evaluate physical athletics."
        ],
        "a": 1,
        "e": "<strong>The passage establishes that while the official ideology claims school is an impartial sorting mechanism, it actually functions to obscure and legitimize the transmission of inherited class inequality.</strong> Choice A is an unfounded distortion. Choices C and D introduce baseless claims unmentioned in the text."
    },
    {
        "q": "Based on Bourdieu's theory of cultural reproduction, which of the following admissions policies would most effectively challenge the reproduction of privilege in higher education?",
        "ch": [
            "Increasing the weight given to interviews assessing 'poise, conversational ease, and cultural polish.'",
            "Evaluating applicants exclusively through unadjusted standardized vocabulary and etiquette exams.",
            "Actively recognizing and crediting the experiential competencies, overcoming of adversity, and contextual habitus of marginalized applicants.",
            "Granting automatic admission to descendants of university donors and alumni."
        ],
        "a": 2,
        "e": "<strong>Since Bourdieu argues that standard tests and subjective interviews reward privileged embodied habitus, actively valuing contextual resilience and non-traditional competencies counteracts the systemic bias of cultural reproduction.</strong> Choices A, B, and D reinforce cultural and institutional reproduction of privilege."
    },
    {
        "q": "The author's reference to the habitus in paragraph 3 implies that an individual's cultural tastes and linguistic style are:",
        "ch": [
            "deeply ingrained behavioral and cognitive dispositions acquired through early immersion in one's social environment.",
            "random intellectual quirks that change unpredictably from week to week.",
            "rigid genetic traits mapped to specific chromosomal loci.",
            "purely superficial mannerisms that have no influence on academic evaluations."
        ],
        "a": 0,
        "e": "<strong>Paragraph 3 describes habitus as the internalized cultural codes, mannerisms, and linguistic practices absorbed through early immersion in the domestic environment.</strong> Choice B contradicts its deep durability. Choice C falsely biologizes a sociological construct. Choice D is refuted by the passage's evidence that educators mistake habitus for natural intelligence."
    }
]

passages.append({
    "id": "exam_cars90_2_p8",
    "sec": "CARS",
    "topic": "Pierre Bourdieu — Cultural Reproduction & Meritocracy",
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_2",
    "passage": p8_html,
    "qs": p8_qs
})

print("Passage 8 defined.")

# ==============================================================================
# PASSAGE 9: Le Corbusier vs Jane Jacobs — Urbanism and Human Scale
# ==============================================================================
p9_html = """<div class="ttl">Passage 9 (Questions 49&ndash;53)</div>
<p>In mid-twentieth-century architectural theory, a profound ideological civil war erupted over the destiny of the modern industrial city. At one pole stood the high-modernist doctrine of the Swiss-French architect Le Corbusier, whose 1925 <i>Ville Radieuse</i> (Radiant City) sought to eradicate the historical, tangled urban core in favor of total rationalist planning. Le Corbusier viewed the traditional street as an obsolete, disease-ridden relic of the medieval past. In its place, he envisioned monumental geometric towers raised on stilts, separated by vast superblocks of manicured lawns and high-speed arterial freeways. Urban functions were rigidly segregated into sterile monocultures: residential zones, commercial zones, and industrial sectors. For the high modernists, the city was a machine to be mastered from above through geometric symmetry and technocratic efficiency.</p>
<p>In 1961, urban activist Jane Jacobs mounted a devastating counter-revolution with <i>The Death and Life of Great American Cities</i>. Writing from the vantage of her Greenwich Village neighborhood, Jacobs exposed high-modernist urban renewal as an arrogant pseudo-science that destroyed the intricate social ecology of living cities. Urban vitality, Jacobs argued, does not stem from geometric purity or isolated towers in a park; rather, it emerges from complex, spontaneous diversity at the human scale. A healthy city requires short street blocks, mixed aged buildings, dense concentrations of diverse populations, and, above all, the mutual co-presence of multiple commercial and residential uses that activate sidewalks throughout the day and night.</p>
<p>Jacobs's most celebrated conceptual contribution was her theory of <i>"eyes on the street."</i> Public safety and civil order in urban environments, she demonstrated, are not maintained primarily by police patrols or top-down surveillance; rather, they are sustained by an unconscious, voluntary network of casual public surveillance provided by local residents, shopkeepers, and pedestrians. When sidewalks are lined with small groceries, laundromats, and street cafes, the constant flow of people creates natural, mutual vigilance that deters crime and fosters spontaneous community solidarity. By severing street-level retail and isolating residents in vertical monoliths, modernist planning eliminated eyes on the street, replacing dynamic civic life with desolate, dangerous urban canyons.</p>"""

p9_qs = [
    {
        "q": "The primary conflict analyzed in the passage is between:",
        "ch": [
            "classical agrarian nostalgia and modern suburban commercial development.",
            "top-down, geometric high-modernist urban planning and organic, human-scale sidewalk ecology.",
            "privatized mass transit systems and municipal highway construction initiatives.",
            "the aesthetic preservation of religious cathedrals and commercial real estate speculation."
        ],
        "a": 1,
        "e": "<strong>The passage contrasts Le Corbusier's high-modernist, geometric, zoned planning with Jane Jacobs's defense of complex, organic, human-scale street life and mixed-use density.</strong> Choices A, C, and D identify conflicts outside the core architectural debate of the passage."
    },
    {
        "q": "According to paragraph 1, Le Corbusier's 'Radiant City' model sought to reform urban architecture primarily by:",
        "ch": [
            "preserving historic cobblestone alleyways and small independent retail shops.",
            "rigidly segregating urban functions and replacing traditional street grids with vertical towers and freeways.",
            "delegating all zoning authority to local neighborhood block associations.",
            "banning mechanical automobiles in favor of horse-drawn carriages."
        ],
        "a": 1,
        "e": "<strong>Paragraph 1 explicitly outlines Le Corbusier's model: eradicating traditional streets, raising towers on stilts, surrounding them with freeways, and strictly segregating residential, commercial, and industrial zones.</strong> Choice A is what Le Corbusier sought to demolish. Choices C and D are historical inversions."
    },
    {
        "q": "Jane Jacobs's concept of 'eyes on the street' (paragraph 3) suggests that public safety in dense urban neighborhoods is most effectively maintained by:",
        "ch": [
            "armed military checkpoints stationed at every major intersection.",
            "continuous, casual public surveillance generated naturally by pedestrians, shopkeepers, and mixed sidewalk use.",
            "installing centralized closed-circuit television cameras on all building rooftops.",
            "curfew regulations requiring citizens to remain indoors after twilight."
        ],
        "a": 1,
        "e": "<strong>Paragraph 3 explicitly defines 'eyes on the street': casual, unconscious public surveillance provided by residents, pedestrians, and shopkeepers whose activities activate the sidewalk throughout the day.</strong> Choices A, C, and D represent top-down, authoritarian interventions that Jacobs contrasted with organic street vigilance."
    },
    {
        "q": "Based on paragraph 2, which of the following urban conditions would Jane Jacobs view as essential for fostering a vital city neighborhood?",
        "ch": [
            "Vast, isolated superblocks containing purely residential luxury towers.",
            "Short blocks, buildings of varying ages, and mixed commercial and residential uses.",
            "Extensive suburban highways that prevent pedestrians from crossing streets.",
            "Rigid municipal zoning laws that ban street cafes and retail shops near apartments."
        ],
        "a": 1,
        "e": "<strong>Paragraph 2 states that a healthy city requires short street blocks, mixed-age buildings, high concentration of population, and multiple simultaneous commercial and residential uses.</strong> Choices A, C, and D represent the exact modernist features that Jacobs criticized."
    },
    {
        "q": "The author's depiction of modernist planning projects that eliminated street-level retail as producing 'desolate, dangerous urban canyons' (paragraph 3) serves to:",
        "ch": [
            "praise high-modernist aesthetics for reducing air pollution in central business districts.",
            "illustrate the counterproductive real-world consequence of technocratic planning that ignores human-scale social interaction.",
            "demonstrate that violent crime is an inevitable biological trait of dense human populations.",
            "advocate for the total abandonment of municipal building safety codes."
        ],
        "a": 1,
        "e": "<strong>The concluding sentence underscores Jacobs's critique: well-intentioned technocratic planning that severed street life ended up destroying the natural mechanisms of safety and community, creating desolate spaces.</strong> Choice A contradicts the critical tone. Choices C and D are baseless extrapolations."
    }
]

passages.append({
    "id": "exam_cars90_2_p9",
    "sec": "CARS",
    "topic": "Le Corbusier vs Jane Jacobs — Urbanism and Human Scale",
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_2",
    "passage": p9_html,
    "qs": p9_qs
})

print("Passage 9 defined.")

total_qs = sum(len(p["qs"]) for p in passages)
print(f"Total CARS Exam 2 questions: {total_qs}")

# Output to exam_cars90_2.js
js_content = "/* ---- exam_cars90_2.js ---- */\n/* Full 90-minute CARS Practice Exam 2: 9 passages (53 Qs) */\nconst EXAM_CARS90_2 = " + json.dumps(passages, indent=2) + ";\n"
with open("/home/cgslinde/DrillRoom/DrillRoom/exam_cars90_2.js", "w") as f:
    f.write(js_content)

print("exam_cars90_2.js written successfully!")
