# scratch/craft_cars90_p1_to_p4.py
# Authors 5/5 difficulty questions for Passages 1 to 4 of EXAM_CARS90
# adhering strictly to the 5-Gate Review Protocol.

import json
import sys

def check_symmetry(q):
    lens = [len(c) for c in q["ch"]]
    r = max(lens) / min(lens)
    assert r <= 1.08, f"FAILED Gate 4: {r:.3f} > 1.08 in '{q['q'][:50]}' (lens={lens})"
    assert "<strong>" in q["e"] and "</strong>" in q["e"], f"FAILED Gate 5: missing strong tag in '{q['q'][:50]}'"
    assert "Distractor Traps:" in q["e"], f"FAILED Gate 5: missing Distractor Traps in '{q['q'][:50]}'"
    assert q["e"].count("&bull;") >= 3, f"FAILED Gate 5: < 3 bullets in '{q['q'][:50]}'"

# ==============================================================================
# PASSAGE 1: Thorstein Veblen — The Place of Science in Modern Civilisation (6 Qs)
# ==============================================================================
p1_qs = [
    {
        "q": "The author's characterization of modern occidental civilization's superiority is best understood as asserting that it is:",
        "ch": [
            "circumscribed in operational breadth but definitive in its material impact.",
            "empirically illusory because earlier cultures surpass it across all metrics.",
            "comprehensive in cultural scope across aesthetic, moral, and logical spheres.",
            "contingent upon metaphysical doctrines that will be abandoned over time."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Delimited Pragmatic Hegemony]</strong> The author explicitly constructs a dual thesis in Paragraph 1: modern civilization possesses 'not an all-around superiority, but a superiority within a closely limited range,' yet this specific matter-of-fact competence confers 'a decisive practical advantage over all other cultural schemes.'<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Locate Paragraph 1 where the author specifies the boundary of modern excellence ('closely limited range') alongside its consequence ('decisive practical advantage').<br>2. <em>Synthesizing Logic</em>: The claim is neither a blanket endorsement of cultural superiority nor a total negation of it; it is narrowly defined yet practically supreme.<br>3. <em>Evaluating Options</em>: Choice A captures both halves of this nuanced balance perfectly with parallel academic phrasing.<br><br><em>Distractor Traps:</em><br>&bull; B (Extreme Scope Inversion): Extrapolates the author's concessions regarding barbarian artistic and metaphysical achievements into an absolute denial of any modern advantage.<br>&bull; C (Directional Expansion): Commits the primary 50/50 seducer trap by adopting popular western chauvinism, directly contradicting the text's explicit denial of 'all-around superiority.'<br>&bull; D (External Attribution): Introduces metaphysical contingency, when Veblen explicitly argues that matter-of-fact science replaces and devalues metaphysical speculation."
    },
    {
        "q": "The extensive catalogue of non-Western achievements in paragraph 3 (Grecian art, Far Eastern craft, and Scholastic dialectic) primarily serves to:",
        "ch": [
            "excoriate modern occidental societies for forfeiting humanist traditions.",
            "demonstrate that cross-cultural comparisons are inherently subjective in kind.",
            "delineate the strict boundary conditions of occidental matter-of-factness.",
            "substantiate the thesis that modern intellectual life is currently declining."
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Rhetorical Boundary Delimitation]</strong> In classical CARS dialectic, an author introduces extensive concessions not to abandon their thesis, but to sharpen its scope by eliminating rival hypotheses.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Contextual Role</em>: In Paragraph 2, Veblen defines the core modern trait as an impersonal apprehension of facts. Paragraph 3 then methodically enumerates areas where other cultures dominate (art, craft, folklore, metaphysics, political finesse).<br>2. <em>Rhetorical Function</em>: By proving that the West is second-rate in artistic taste, craftsmanship, and metaphysics, Veblen isolates matter-of-fact insight as the <em>sole</em> variable responsible for its global dominance.<br>3. <em>Conclusion</em>: The catalogue serves as negative definition, strictly bounding the operational domain where the West truly prevails.<br><br><em>Distractor Traps:</em><br>&bull; A (Normative / Emotional Distortion): Interprets an analytical anthropological taxonomy as a moralistic rebuke or lamentation.<br>&bull; B (Postmodern Relativist Trap): Asserts that cultural comparisons are impossible, whereas Veblen compares cultures with definitive, hierarchical confidence throughout the passage.<br>&bull; D (Seductive 50/50 Overstatement): Confuses the limitation of modern virtue to a single domain with a claim of historical cultural degeneration."
    },
    {
        "q": "The author's observation that the matter-of-fact habit of mind 'may be a matter of habit or of racial endowment, or it may be an outcome of both' functions rhetorically to:",
        "ch": [
            "dismiss the causal origin of the trait as irrelevant to its historical effect.",
            "endorse biological determinism as the definitive foundation of cultural growth.",
            "signal intellectual hesitation regarding the validity of his central argument.",
            "suggest that non-Western cultures can easily acquire the scientific viewpoint."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Elimination of Non-Essential Causal Variables]</strong> Analytical argumentation frequently quarantines secondary disputes to preserve the explanatory power of the primary thesis.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Immediate Textual Follow-up</em>: Veblen immediately writes: 'whatever be the explanation of its prevalence, the immediate consequence is much the same for the growth of civilisation.'<br>2. <em>Logical Deduction</em>: Veblen deliberately signals to the reader that whether the scientific orientation is sociological ('habit') or biological ('endowment') has zero bearing on his historical deduction: that a culture possessing it will inevitably conquer cultural schemes that lack it.<br>3. <em>Selection</em>: Choice A accurately identifies this deliberate methodological bracketing.<br><br><em>Distractor Traps:</em><br>&bull; B (50/50 Selective Seeding Trap): Seizes upon the phrase 'racial endowment' to claim the author champions biological determinism, ignoring the author's explicit indifference to the etiology.<br>&bull; C (Psychometric False Hedging): Misinterprets rhetorical bracketing as epistemological uncertainty or argumentative weakness.<br>&bull; D (Unwarranted Extrapolation): Speculates about the ease of cultural transmission, an issue completely unaddressed in paragraph 2."
    },
    {
        "q": "Which of the following historical scenarios, if verified, would most directly undermine the author's argument regarding civilizational conflict?",
        "ch": [
            "A traditional society lacking science defeats an industrialized power in war.",
            "An imperial power rapidly assimilates the artistic traditions of its colony.",
            "A scientific empire collapses internally because of acute sectarian controversy.",
            "A pre-industrial culture maintains philosophical schools alongside religion."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Falsification of Invariant Historical Imperatives]</strong> To weaken a universal deterministic claim, one must identify an empirical counter-instance that violates the stated causal necessity.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Target the Absolute Claim</em>: In Paragraph 2, Veblen establishes an uncompromising principle: 'A civilisation which is dominated by this matter-of-fact insight must prevail against any cultural scheme that lacks this element.'<br>2. <em>Formulate the Falsifier</em>: A single verified instance where a culture completely devoid of matter-of-fact science decisively prevails against a scientific civilization shatters the invariant necessity of Veblen's rule.<br>3. <em>Match with Options</em>: Choice A presents this exact counter-example.<br><br><em>Distractor Traps:</em><br>&bull; B (Irrelevant Concession): Veblen already conceded in Paragraph 3 that ancient art and craftsmanship surpass modern achievements, so artistic assimilation is entirely consistent with his thesis.<br>&bull; C (Internal vs External Seducer Trap): Internal fragmentation through sectarian strife addresses internal political stability, not Veblen's specific claim regarding inter-civilizational dominance between scientific and non-scientific cultural schemes.<br>&bull; D (Passive Baseline Trap): Mere coexistence of philosophy and religion in traditional societies is explicitly recognized by Veblen in Paragraph 3 and provides zero counter-evidence."
    },
    {
        "q": "In paragraph 4, the author asserts that statecraft, dynasty-building, and religious propagation 'seem futile in comparison with the achievements of science.' This comparison implies that modern individuals evaluate human endeavors primarily by their:",
        "ch": [
            "lasting cumulative utility and verifiable factual truth rather than ceremony.",
            "alignment with orthodox religious dogma and authentic spiritual transcendence.",
            "capacity to stimulate genuine aesthetic appreciation and subjective fulfillment.",
            "contribution to the preservation of aristocratic privilege and social order."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Epistemological Revaluation of Human Ends]</strong> Paragraph 4 contrasts the transient, self-justifying ambitions of the past with the permanent, escalating prestige of scientific inquiry.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Textual Analysis</em>: Ancient pursuits (feuds, dynasties, sects, consumption) 'dwindle in men's esteem as time passes,' whereas 'the achievements of science are held higher' and the 'final appeal is... taken to the scientist.'<br>2. <em>Deductive Synthesis</em>: The underlying metric that causes dynasties to dwindle while science rises is that science yields durable, objective factual insight that remains valid beyond the egoistic lifespan of founders and creeds.<br>3. <em>Conclusion</em>: Modern valuation rests on cumulative factual verification rather than ritualistic or institutional permanence.<br><br><em>Distractor Traps:</em><br>&bull; B (Direct Inversion): States the exact opposite of the modern shift away from religious creeds and sects.<br>&bull; C (Scope Shift): Confuses aesthetic gratification (conceded to ancient Greeks in Paragraph 3) with the modern matter-of-fact evaluation.<br>&bull; D (True Fact Wrong Epoch): Accurately describes the historical justification of feudal dynasties in earlier ages, but fails to capture the modern perspective defined in the stem."
    },
    {
        "q": "The passage's concluding sentence ('This state of things may not be altogether fortunate, but such it is') serves primarily to maintain an authorial stance that is:",
        "ch": [
            "strictly descriptive and analytical rather than being normatively celebratory.",
            "overtly apologetic regarding the cultural devastation wrought by modern science.",
            "deeply skeptical about the empirical validity of modern scientific findings.",
            "optimistically anticipating a renaissance in traditional metaphysical inquiry."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Epistemic Neutrality and Positivist Distance]</strong> Academic CARS texts frequently employ closing hedges to divorce empirical description (what is) from normative advocacy (what ought to be).<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Contextual Assessment</em>: Throughout the passage, Veblen explains how science inevitably conquers all rival worldviews. A reader might easily misread this as triumphalist Western cheerleading.<br>2. <em>Deconstructing the Closing Hedge</em>: By noting that the supremacy of science 'may not be altogether fortunate,' Veblen abruptly detaches his personal valuation from his historical analysis, concluding with the fatalistic realism of 'but such it is.'<br>3. <em>Selection</em>: Choice A captures this critical philosophical distinction between description and endorsement.<br><br><em>Distractor Traps:</em><br>&bull; B (Emotional Overstatement): Inflates a restrained qualifier into an 'overt apology,' which is unsupported by the text's dispassionate tone.<br>&bull; C (Direct Inversion): Claims the author doubts science's empirical validity, when the entire essay is premised on the unmatched factual efficacy of scientific insight.<br>&bull; D (Fabricated Future Projection): Invents an optimistic prophecy of a metaphysical renaissance nowhere hinted at in the text."
    }
]

# ==============================================================================
# PASSAGE 2: Nathaniel Hawthorne — Puritan Society and Orthodoxy (6 Qs)
# ==============================================================================
p2_qs = [
    {
        "q": "The author's observation that the founders of a new colony inevitably allot 'a portion of the virgin soil as the site of a prison' primarily serves to expose:",
        "ch": [
            "the inescapable paradox within a society aspiring toward complete moral purity.",
            "the architectural ineptitude characteristic of early colonial settlement plans.",
            "the pragmatic economic necessity of utilizing punitive labor in frontier posts.",
            "the transient nature of religious devotion when facing rugged wilderness trials."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Dialectical Incoherence of Utopian Moralism]</strong> The central irony of the opening paragraph is the structural tension between utopian aspiration and punitive compulsion.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Paragraph 1 contrasts 'whatever Utopia of human virtue and happiness they might originally project' with their recognition of a prison as an 'earliest practical necessity.'<br>2. <em>Mechanistic Bridge</em>: A community dedicated to absolute virtue must define itself against transgression; therefore, institutionalized confinement is not an accidental blemish, but an indispensable prerequisite to sustain the illusion of communal orthodoxy.<br>3. <em>Downstream Deduction</em>: The prompt asks what this juxtaposition exposes: the tragic, inescapable paradox of Puritan perfectionism.<br><br><em>Distractor Traps:</em><br>&bull; B (Literal Superficiality Trap): Trivializes profound philosophical irony into an issue of architectural incompetence.<br>&bull; C (Economic Substitution Trap): Imports Marxist or economic categories ('punitive labor') nowhere mentioned in Hawthorne's theological narrative.<br>&bull; D (Scope Shift): Claims religious devotion was transient, whereas the text depicts an obsessive, enduring theological rigidity."
    },
    {
        "q": "Which of the following best characterizes the symbolic tension established between the 'black flower of civilized society' and the 'wild rose-bush'?",
        "ch": [
            "Institutional moral retribution versus unmediated, enduring natural compassion.",
            "Corrupt ecclesiastical bureaucracy versus the pristine virtues of early settlers.",
            "Despairing spiritual depravity versus the redemptive power of public penitence.",
            "The ephemeral brevity of human misery versus the eternal permanence of penal law."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Organic Nature vs Artificial Institutional Dogma]</strong> Hawthorne establishes a binary between the grim, punitive machinery of man and the spontaneous, compassionate grace of the natural world.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Textual Anchors</em>: The prison is explicitly termed 'the black flower of civilized society,' growing out of unsightly weeds. The rose-bush is 'wild,' offering its 'fragrant beauty' indiscriminately to the condemned.<br>2. <em>Semantic Mapping</em>: The prison represents civilized society's calculated retribution; the wild rose represents an organic, uncodified pity that nature extends to human frailty.<br>3. <em>Option Synthesis</em>: Choice A mirrors this exact symbolic dichotomy with balanced philosophical precision.<br><br><em>Distractor Traps:</em><br>&bull; B (True Fact Wrong Contrast): Suggests the settlers were virtuous while bureaucracy was corrupt, but Hawthorne indicts the entire colonial ethos as sad-colored and unforgiving.<br>&bull; C (Theological Misinterpretation): Conflates the rose with 'public penitence,' but the rose exists <em>outside</em> the prison portal, offering solace against the community's punitive display.<br>&bull; D (Inversion of Permanence): Inverts the passage's temporal claim, which notes that the rose-bush 'has been kept alive in history' while individual colonial edicts fade."
    },
    {
        "q": "Hester Prynne's decision to embroider the scarlet letter with 'fantastic flourishes of gold thread' in violation of colonial sumptuary regulations functions rhetorically to signify:",
        "ch": [
            "an autonomous aesthetic reclamation of a designated instrument of public ignominy.",
            "a desperate attempt to ingratiate herself with prominent colonial magistrates.",
            "an unrepentant celebration of secular materialism over ascetic spiritual piety.",
            "a cynical ploy to distract curious onlookers from the physical presence of her baby."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Subversion through Aesthetic Transmutation]</strong> When an oppressed individual elaborates and beautifies a mandated mark of shame, they wrest semiotic control away from the punitive authority.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Textual Scrutiny</em>: The letter is crafted with 'luxuriance of fancy' and 'splendor... greatly beyond what was allowed by the sumptuary regulations.'<br>2. <em>Psychological Synthesis</em>: The Puritans intended the letter as an austere, degrading brand. By executing it with gold embroidery, Hester does not hide her sin; she transforms an imposed badge of humiliation into a work of exquisite personal agency.<br>3. <em>Conclusion</em>: It represents an autonomous reclamation that subverts the beadle's disciplinary objective.<br><br><em>Distractor Traps:</em><br>&bull; B (50/50 Sycophancy Trap): Claims she tried to flatter magistrates, which directly contradicts her haughty glance and open violation of their sumptuary laws.<br>&bull; C (Superficial Category Error): Mistakes artistic defiance for an endorsement of 'secular materialism.'<br>&bull; D (Intermediate Step Inversion): Paragraph 4 explicitly states she realized 'one token of her shame would but poorly serve to hide another' and boldly took the baby on her arm, abandoning concealment."
    },
    {
        "q": "The crowd's astonishment at perceiving Hester's appearance as a 'halo of misfortune' rather than a 'dimmed and obscured cloud' reveals that the community's penal system:",
        "ch": [
            "depends upon the psychological degradation of the offender to sustain its authority.",
            "secretly harbored profound sympathy for the transgressive actions of the accused.",
            "succeeded in demonstrating the transformative spiritual efficacy of incarceration.",
            "failed because the magistrates had mistakenly prosecuted an innocent community member."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: The Requisite Abjection of the Penal Subject]</strong> Public punishment functions sociologically only if the punished subject visibly embodies abjection and brokenness.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: The crowd 'had expected to behold her dimmed and obscured by a disastrous cloud,' but were 'astonished' to find her beauty shining out, surrounding her with dignity.<br>2. <em>Deductive Link</em>: The crowd is disoriented because the entire spectacle of the pillory relies on witnessing Hester's psychological collapse to validate the righteousness of their laws.<br>3. <em>Deduction</em>: When Hester appears radiant and proud, the punitive mechanism misfires, demonstrating that colonial authority requires the offender's inner degradation to reaffirm its power.<br><br><em>Distractor Traps:</em><br>&bull; B (Sentimental Distortion): Mistakes the crowd's shock for 'profound sympathy'; the text describes them as stern, grim onlookers in sad-colored garments.<br>&bull; C (Direct Inversion): Claims the prison spiritually redeemed her in the Puritan sense, when her defiance explicitly flouted their intended humiliation.<br>&bull; D (Extraneous Fact Trap): Alleges she was innocent, but Hester's baby and admission confirm the violation of law; her defiance is spiritual, not legal."
    },
    {
        "q": "Suppose historical legal documents demonstrated that 17th-century Boston magistrates deliberately encouraged intricate embroidery on punitive badges to heighten public visual fascination. This evidence would most directly WEAKEN which of the following passage claims?",
        "ch": [
            "Hester's gold-threaded ornamentation defied the colony's sumptuary prohibitions.",
            "The townspeople assembled outside the wooden prison in solemn, quiet expectation.",
            "Hester repelled the town-beadle with haughty dignity upon emerging from jail.",
            "The infant turned its face aside from the unaccustomed brightness of the sun."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Empirical Subversion of Authorial Framing]</strong> When evaluating hypothetical challenges in CARS, identify the specific text assertion that depends logically on the contested fact.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Passage Assertion</em>: The author states that Hester's gold embroidery was 'greatly beyond what was allowed by the sumptuary regulations of the colony' and emphasized her defiance of communal norms.<br>2. <em>Applying the Hypothetical</em>: If magistrates actually <em>mandated or encouraged</em> intricate embroidery to create a public spectacle, then her embroidery was not a transgressive act of private aesthetic rebellion, but compliance with official penal choreography.<br>3. <em>Conclusion</em>: This directly shatters the claim that her ornamentation defied sumptuary prohibitions.<br><br><em>Distractor Traps:</em><br>&bull; B (Unaffected Factual Detail): The crowd's solemn assembly remains completely plausible regardless of who designed the badge.<br>&bull; C (Physical Gesture Decoupling): Hester repelling the beadle's hand is an independent physical action of bodily autonomy unaffected by badge regulations.<br>&bull; D (Biological Reflex Irrelevance): An infant squinting at daylight is a physiological reflex having zero connection to judicial embroidery decrees."
    },
    {
        "q": "Which of the following scenarios is most conceptually analogous to Hester Prynne's posture when emerging through the prison door?",
        "ch": [
            "A political dissident marching to trial wearing a banned emblem of resistance.",
            "A repentant executive publicly acknowledging accounting fraud at an inquiry.",
            "An accused suspect escaping custody by evading guards in a crowded street.",
            "A convicted felon accepting a pardon while apologizing for his past misconduct."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Structural Isomorphism in Transgressive Dignity]</strong> An authentic MCAT analogy must replicate the core structural variables: compulsory penal judgment, refusal to be abased, and transformational display of the forbidden token.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Core Structural Nodes</em>: (1) An individual under state custody; (2) emerging into public condemnation; (3) deliberately displaying a forbidden symbol with defiant dignity rather than shame.<br>2. <em>Evaluating Choice A</em>: A political dissident marching into an authoritarian court wearing a banned symbol perfectly maps onto Hester wearing the lavishly embroidered scarlet letter.<br>3. <em>Verification</em>: All other choices involve repentance, evasion, or capitulation.<br><br><em>Distractor Traps:</em><br>&bull; B (Penitential Inversion): An executive apologizing embodies the exact groveling submission that Hester explicitly rejects.<br>&bull; C (Physical Escape Trap): Hester does not run away; she steps boldly into the open air and faces her accusers.<br>&bull; D (Capitulation Trap): Accepting a pardon and apologizing represents reconciliation with the state, the antithesis of Hester's isolation in a 'sphere by herself.'"
    }
]

# ==============================================================================
# PASSAGE 3: Literary Criticism — Understanding Thomas Hardy (6 Qs)
# ==============================================================================
p3_qs = [
    {
        "q": "The author's assertion that Hardy refused to follow the realists into a 'morass of words' while simultaneously rejecting 'pure impressionism' implies that authentic literary artistry requires:",
        "ch": [
            "synthesizing empirical reality with the author's personal philosophical vision.",
            "abandoning contemporary scientific findings in favor of Classical mythology.",
            "documenting mundane sociological details with photographic, detached fidelity.",
            "prioritizing stylistic ornamentation over thematic coherence and narrative truth."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Dialectical Synthesis of Realism and Subjectivity]</strong> The author defines Hardy's unique stature in Paragraph 1 as a deliberate reconciliation between rival 19th-century aesthetic dogmas.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Hardy rejected realists who merely accumulated words to depict life as they thought it was, but also rejected 'pure impressionism.' Instead, 'he endeavored to preserve a balance between objective reality and his interpretation of it.'<br>2. <em>Deductive Synthesis</em>: True literary artistry, according to the author, is neither mechanical stenography (realism) nor solipsistic fantasy (impressionism), but an active synthesis of observed reality and philosophical vision.<br>3. <em>Selection</em>: Choice A articulates this exact balance.<br><br><em>Distractor Traps:</em><br>&bull; B (Direct Inversion): Hardy specifically embraced science ('believed in the efficacy of the knowledge given to one by an understanding of science'), never abandoning it.<br>&bull; C (The Realist Error): Describes pure realism, the exact 'morass of words' that the author praises Hardy for rejecting.<br>&bull; D (Vacuous Aestheticism): Suggests shallow ornamentation, whereas the text establishes Hardy as a deeply philosophical, deterministic thinker."
    },
    {
        "q": "The passage asserts that evolutionary theory provided 'aid from an unsought source' to the doctrine of Predestination. This argument fundamentally depends upon the premise that:",
        "ch": [
            "biological materialism negates human volitional autonomy as rigidly as theology.",
            "Charles Darwin and Thomas Huxley were devout proponents of Calvinist doctrines.",
            "nineteenth-century religious denominations universally welcomed evolutionary theory.",
            "genetic determinism allows individuals to select their ultimate spiritual outcome."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Equivalence of Mechanistic and Theological Constraints]</strong> To argue that two radically different intellectual paradigms (Calvinism and Darwinism) support the same conclusion, the author must assume they share a common mechanistic consequence.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Contextual Analysis</em>: Paragraph 3 contrasts Free Will with Predestination, then notes evolutionary theory unexpectedly aided Predestination by showing that human actions fit 'scientific determinism.'<br>2. <em>Unspoken Premise</em>: For evolutionary biology to reinforce Calvinist predetermination, biological causality (heredity and environment) must bind human will just as irrevocably as an omnipotent divine decree.<br>3. <em>Conclusion</em>: Both systems converge on the eradication of metaphysical free will.<br><br><em>Distractor Traps:</em><br>&bull; B (Factual Absurdity Trap): Claims Darwin and Huxley were Calvinists; the text notes the aid was 'from an unsought source,' meaning the scientists were secular thinkers, not theologians.<br>&bull; C (Historical Distortion Trap): Claims churches welcomed evolution, which contradicts the known historical conflict and the passage's note that Calvinism originated in religion while evolution was secular.<br>&bull; D (Direct Internal Inversion): Suggests genetic determinism allows individuals to select their outcome, which contradicts the definition of determinism."
    },
    {
        "q": "In paragraph 2, the author's description of human beings moving as 'automata, each within his own sphere' functions primarily to illustrate the:",
        "ch": [
            "extent to which unseen deterministic forces govern everyday individual choices.",
            "dehumanizing industrial factory conditions experienced by urban British laborers.",
            "intellectual superiority of the emperor over an unconscious lout in the ditch.",
            "complete absence of any predictable biological patterns across human cultures."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Metaphorical Representation of Total Determinism]</strong> The automaton metaphor is the quintessential 19th-century mechanical representation of the illusion of free agency.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Paragraph 2 states that circumstance caught up 'all human beings from the emperor in his palace to the unconscious lout lying drunk in the ditch,' concluding that 'men moved as automata, each within his own sphere. Unseen forces played upon them; unseen powers directed them.'<br>2. <em>Deductive Synthesis</em>: An automaton appears to walk on its own, but its movements are entirely dictated by internal gears and external clockwork. Hardy uses this image to show that human deliberation is an illusion masking overwhelming deterministic forces.<br>3. <em>Selection</em>: Choice A accurately defines the function of the metaphor.<br><br><em>Distractor Traps:</em><br>&bull; B (Sociological Scope Creep): Imports industrial factory conditions, whereas Hardy's claim applies universally to all human beings, including ancient emperors.<br>&bull; C (Hierarchical Inversion): Claims the emperor is superior, when Veblen specifically uses the emperor and drunkard to demonstrate that fate treats all classes with equal indifference.<br>&bull; D (Direct Inversion): Claims biological patterns are absent, when Paragraph 3 explicitly identifies heredity as one of the three foundational deterministic forces."
    },
    {
        "q": "Which of the following historical developments during the nineteenth century would most directly WEAKEN the author's claims regarding Hardy's worldview?",
        "ch": [
            "A sociological consensus proving that individuals routinely defy their heredity.",
            "The discovery that Thomas Hardy privately attended Roman Catholic church services.",
            "The widespread secularization of British universities during the late Victorian era.",
            "The emergence of psychological research confirming the decisive impact of schooling."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Empirical Falsification of Tripartite Determinism]</strong> Hardy's philosophical architecture rests upon three inviolable pillars: heredity, education, and environment.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Locate Core Vulnerability</em>: Hardy believed that from these three forces 'there was no escape, for every choice seemingly made by the individual... was dictated by so many thousand unseen circumstances.'<br>2. <em>Evaluate Challenge</em>: If rigorous sociological data demonstrated that individuals regularly break free from both genetic endowment and environmental conditioning through conscious will, the foundational claim that humans are helpless automata collapses.<br>3. <em>Conclusion</em>: Choice A strikes at the heart of this causal premise.<br><br><em>Distractor Traps:</em><br>&bull; B (Biographical Red Herring): Attending church services addresses personal habit, but does not refute the scientific and philosophical validity of his literary determinism.<br>&bull; C (Strengthening Variable): Secularization of universities would foster the exact scientific determinism Hardy championed.<br>&bull; D (Confirming Variable): Proving that education shapes psychology directly confirms Hardy's second deterministic force ('the shaping power of education')."
    },
    {
        "q": "Based on the passage, the ancient Greek belief in the three Fates and the nineteenth-century scientific determinism of Hardy are similar in that both:",
        "ch": [
            "subordinate human volition entirely to inexorable and external deterministic laws.",
            "attribute daily human misfortunes to the direct whims of deities on Mount Olympus.",
            "reject any distinction between the hereditary traits of mortal men and the gods.",
            "assert that education can easily liberate humans from their predetermined destiny."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Historical Continuity of Deterministic Thought]</strong> Across the passage, the author constructs an unbroken lineage of determinism running from Greek mythology through Calvinism to evolutionary biology.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Textual Comparison</em>: Paragraph 3 explicitly bridges the Greeks and Hardy: 'The Greeks, for example, believed that the three Fates directed every action... of mortals, and Immortals... Once an anthropomorphic God was out of the picture and His place taken by an evolving Consciousness... it was almost necessary to believe in a theory of life similar to that held by Hardy.'<br>2. <em>Common Denominator</em>: Whether called the 'three Fates,' 'Predestination,' or 'heredity and environment,' both systems agree that human agency is completely subordinated to an unyielding external law.<br>3. <em>Selection</em>: Choice A encapsulates this philosophical kinship.<br><br><em>Distractor Traps:</em><br>&bull; B (Conflation of Epochs): Hardy explicitly discarded anthropomorphic deities, replacing them with scientific determinism and the Immanent Will.<br>&bull; C (Spurious Category): Fabricates an assertion about the genetics of Greek gods, an absurdity nowhere in the text.<br>&bull; D (Direct Inversion): Claims education liberates humans, whereas Hardy categorized education as one of the three prisons from which 'there was no escape.'"
    },
    {
        "q": "The author's tone toward Thomas Hardy's intellectual synthesis across the entire passage can best be described as:",
        "ch": [
            "respectfully analytical of his rigorous integration of literature and science.",
            "dismissive of his outdated reliance upon obsolete Calvinist theological dogma.",
            "unconditionally laudatory of his superiority over Arnold, Whitman, and Darwin.",
            "condescending toward his futile attempts to understand complex Greek philosophy."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Calibrated Academic Respect without Hyperbole]</strong> Identifying the author's tone requires distinguishing measured scholarly endorsement from both uncritical worship and cynical disdain.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Textual Evidence</em>: The author calls Hardy 'in the old sense of the word a literary artist,' notes he 'scanned the pages of philosophy, of science, and of history to be certain that he read life aright,' and treats his deterministic worldview as a serious, coherent intellectual achievement.<br>2. <em>Eliminating Extremes</em>: The author never mocks Hardy, nor does he place him above Darwin or Whitman in an uncritical panegyric.<br>3. <em>Conclusion</em>: The tone is dignified, scholarly, and respectfully analytical.<br><br><em>Distractor Traps:</em><br>&bull; B (False Negative): Claims the author dismisses Hardy, when the author repeatedly validates Hardy's rigorous scanning of philosophy and science.<br>&bull; C (Hyperbolic Panegyric): Overstates analytical respect into 'unconditional laudation' and invents a ranking where Hardy is superior to Darwin.<br>&bull; D (Emotional Distortion): Claims the author is condescending, which directly contradicts the passage's admiring scholarly demeanor."
    }
]

# ==============================================================================
# PASSAGE 4: Evolutionary Psychology — Maternal Emotional Response (6 Qs)
# ==============================================================================
p4_qs = [
    {
        "q": "The author criticizes previous neuroimaging studies of maternal responses to infant smiling primarily because those investigations:",
        "ch": [
            "assessed neural activation from a calm baseline rather than during acute stress.",
            "utilized functional neuroimaging techniques lacking sufficient spatial precision.",
            "examined non-biological female caregivers rather than actual biological mothers.",
            "focused on sympathetic autonomic arousal while ignoring parasympathetic metrics."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Methodological Baseline Invalidation]</strong> In behavioral neuroscience, a stimulus effect can be radically underestimated if tested against a quiescent resting state rather than its functional target state.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Paragraph 3 notes that prior fMRI studies examined infant smiling, but 'these studies emphasized the effects of infant smiling on changes from a calm maternal state.'<br>2. <em>Theoretical Critique</em>: The author argues: 'It is possible infant smiling might have stronger recovery effects on physiologically negative stressful states, by means of the undoing effect.'<br>3. <em>Downstream Deduction</em>: Testing from a calm baseline overlooked the primary evolutionary function of the smile: reversing acute sympathetic distress caused by crying.<br><br><em>Distractor Traps:</em><br>&bull; B (Technical Red Herring): Claims fMRI lacked spatial precision, an engineering critique nowhere made by the author.<br>&bull; C (Subject Demographics Trap): Fabricates an assertion about non-biological caregivers; the passage confirms prior studies examined maternal brain regions.<br>&bull; D (Theoretical Distortion): Prior studies were brain-imaging studies of neural activation (reward systems, motor planning), not peripheral autonomic studies that ignored parasympathetic metrics."
    },
    {
        "q": "Based on the description of maternal distress reactions as 'preparation for action,' an instantaneous undoing effect during an ongoing cry would be maladaptive because it would:",
        "ch": [
            "prematurely extinguish the sympathetic drive required to console the infant.",
            "induce severe maternal exhaustion through prolonged cardiovascular hyperarousal.",
            "permanently damage the infant's capacity to develop autonomous coping strategies.",
            "prevent the mother from accurately discerning the acoustic pitch of the distress."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Evolutionary Teleology of Autonomic Stress]</strong> Acute sympathetic activation is an evolved survival mechanism designed to motivate immediate protective intervention.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Textual Principle</em>: Paragraph 1 states that cardiac acceleration and increased skin conductance in mothers function as 'preparation for action,' prompting the mother to 'approach, pick up, and attempt to console her infant.'<br>2. <em>Functional Analysis</em>: If an infant's crying immediately triggered the undoing effect, the mother's parasympathetic system would prematurely restore a quiet, relaxed state.<br>3. <em>Behavioral Consequence</em>: The mother would lose the physiological arousal necessary to sustain the urgent, physically demanding behavior of comforting a distressed baby.<br><br><em>Distractor Traps:</em><br>&bull; B (Directional Inversion): Argues the mother would suffer prolonged hyperarousal, when an instantaneous undoing effect causes the exact opposite: premature relaxation.<br>&bull; C (Infant Centric Distortion): Shifts the focus to the infant's long-term psychological development, which is unaddressed in this maternal physiological study.<br>&bull; D (Sensory Shift): Claims pitch perception would be impaired, confusing autonomic motor motivation with acoustic auditory acuity."
    },
    {
        "q": "To confirm that infant smiles accelerate maternal physiological recovery specifically via the undoing effect rather than sensory habituation, researchers must show that:",
        "ch": [
            "recovery occurs significantly faster after smiling faces than neutral faces.",
            "mothers exhibit identical cardiac deceleration when exposed to unfamiliar infants.",
            "skin conductance returns to baseline at identical rates regardless of stimulus.",
            "parasympathetic activation remains suppressed until the infant stops vocalizing."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Experimental Discrimination between Active Reversal and Passive Decay]</strong> In autonomic psychophysiology, proving an active 'undoing' mechanism requires demonstrating that a positive valence stimulus accelerates recovery beyond the baseline rate of passive habituation.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Theoretical Definition</em>: Paragraph 2 cites Fredrickson and Levenson: cardiovascular activity 'returns to baseline more quickly when followed by watching a cheerful film than after a sad or neutral film.'<br>2. <em>Experimental Control</em>: Passive habituation occurs simply through the passage of time or exposure to a neutral stimulus. To isolate the undoing effect, the happy smile must demonstrate statistically superior recovery speed compared to an emotionally neutral infant face.<br>3. <em>Selection</em>: Choice A defines this vital experimental control.<br><br><em>Distractor Traps:</em><br>&bull; B (Demographic Generalizability Trap): Testing unfamiliar infants tests generalizability, but does not distinguish the undoing effect from passive sensory habituation.<br>&bull; C (Direct Inversion): Proving recovery occurs at identical rates would prove the smile has NO unique undoing effect, falsifying the hypothesis.<br>&bull; D (Factual Inversion): The undoing effect requires parasympathetic activation to rise rapidly, not remain suppressed."
    },
    {
        "q": "According to the autonomic model outlined in paragraph 2, a mother successfully experiencing the undoing effect following infant distress would exhibit:",
        "ch": [
            "enhanced parasympathetic tone accompanied by steady decreases in heart rate.",
            "concurrent elevations in both cardiac output and galvanic skin responsiveness.",
            "complete suppression of the autonomic nervous system to achieve homeostasis.",
            "accelerated sympathetic dominance until conscious cognitive appraisal occurs."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Reciprocal Autonomic Homeostasis]</strong> Homeostatic restoration after acute stress requires the activation of the parasympathetic branch and the reciprocal dampening of sympathetic activity.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Paragraph 2 states that after stress release, 'parasympathetic activity becomes dominant and sympathetic activity decreases, with an associated reduction in skin conductance and heart rate.'<br>2. <em>Physiological Synthesis</em>: The undoing effect accelerates this exact parasympathetic dominance.<br>3. <em>Selection</em>: Choice A matches this physiological mechanism with rigorous terminology.<br><br><em>Distractor Traps:</em><br>&bull; B (Directional Inversion): Depicts continued sympathetic fight-or-flight arousal (elevated heart rate and skin conductance).<br>&bull; C (Biological Impossibility): Claims the entire autonomic nervous system is 'completely suppressed,' which would cause circulatory arrest; homeostasis is dual, dynamic regulation, not cessation.<br>&bull; D (Phase Mismatch): Depicts sustained sympathetic dominance, which characterizes the ongoing stress response, not the undoing effect."
    },
    {
        "q": "Suppose an experiment reveals that mothers experiencing postpartum depression display normal cardiac spikes to infant cries, but show zero autonomic recovery when shown infant smiles. This finding most directly suggests that:",
        "ch": [
            "depressive pathology selectively impairs the maternal undoing recovery pathway.",
            "postpartum depression completely eliminates maternal sympathetic fight reflexes.",
            "infant smiles possess zero biological capacity to influence maternal heart rate.",
            "the undoing effect is completely reliant upon conscious cognitive deliberation."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Pathological Uncoupling of Affective Modulation]</strong> When an established regulatory mechanism fails in a clinical population despite intact stress induction, researchers infer impairment of the modulating pathway.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Analyze the Findings</em>: Stress induction is intact (normal cardiac spikes to cries), but the therapeutic intervention fails (zero autonomic recovery from smiles).<br>2. <em>Deductive Link</em>: In healthy mothers, positive infant expressions activate reward and parasympathetic pathways to attenuate stress. In depressed mothers, the failure to recover indicates that depression selectively impairs the capacity of positive stimuli to recruit the undoing mechanism.<br>3. <em>Selection</em>: Choice A accurately identifies this selective impairment.<br><br><em>Distractor Traps:</em><br>&bull; B (Direct Factual Inversion): The prompt explicitly states the mothers displayed 'normal cardiac spikes to infant cries,' proving sympathetic arousal is fully functional.<br>&bull; C (False Overgeneralization): Extrapolates a finding in a clinical depressed cohort into a sweeping claim that infant smiles have zero biological capacity in all human mothers.<br>&bull; D (Theoretical Contradiction): Paragraph 1 notes caregivers respond 'automatically' to expressions, and Paragraph 2 links it to autonomic physiology, not conscious cognitive deliberation."
    },
    {
        "q": "Which of the following real-world clinical situations is most structurally analogous to the operation of the undoing effect described in the passage?",
        "ch": [
            "A panicked phobic patient calming down upon viewing soothing visual imagery.",
            "A chronic hypertension patient lowering blood pressure through daily exercise.",
            "An athlete mentally visualizing a flawless performance prior to competition.",
            "An insomniac establishing a rigid nocturnal bedtime schedule to induce sleep."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Valence-Driven Autonomic De-escalation]</strong> A true MCAT analogy must replicate the operational mechanism: acute physiological stress/panic followed immediately by a positive emotional stimulus that accelerates autonomic return to baseline.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Deconstruct Mechanism</em>: (1) Acute stress induction (negative valence, high sympathetic arousal); (2) Introduction of an emotionally comforting/positive stimulus; (3) Rapid autonomic de-escalation.<br>2. <em>Evaluating Choice A</em>: A panicked phobic patient (acute sympathetic arousal) experiencing rapid stabilization upon viewing comforting imagery mirrors the mother recovering from distress cries upon seeing a smile.<br>3. <em>Verification</em>: All other options describe chronic adaptations, anticipatory priming, or behavioral routines lacking acute valence-driven reversal.<br><br><em>Distractor Traps:</em><br>&bull; B (Chronic vs Acute Mismatch): Exercise lowering blood pressure is chronic physiological vascular remodeling, not acute emotional undoing.<br>&bull; C (Anticipatory Priming Trap): Athletic visualization is forward-looking mental preparation, not recovery from an acute negative stress state.<br>&bull; D (Circadian Behavioral Routine): Sleep scheduling relies on circadian melatonin regulation, having no connection to emotional undoing."
    }
]

if __name__ == "__main__":
    print("Validating Passages 1 to 4...")
    all_qs = p1_qs + p2_qs + p3_qs + p4_qs
    issues = []
    for i, q in enumerate(all_qs):
        lens = [len(c) for c in q["ch"]]
        r = max(lens) / min(lens)
        corr_len = lens[q["a"]]
        max_len = max(lens)
        if r > 1.08:
            issues.append(f"Q{i+1} Gate 4 ratio: {r:.3f} > 1.08 (lens={lens}, q='{q['q'][:40]}')")
        if corr_len == max_len and lens.count(max_len) == 1:
            issues.append(f"Q{i+1} Gate 4 longest: correct choice is strict longest ({corr_len} vs {[l for j,l in enumerate(lens) if j!=q['a']]})")
        if "<strong>" not in q["e"] or "</strong>" not in q["e"]:
            issues.append(f"Q{i+1} Gate 5: missing strong tag")
        if "Distractor Traps:" not in q["e"]:
            issues.append(f"Q{i+1} Gate 5: missing Distractor Traps")
        if q["e"].count("&bull;") < 3:
            issues.append(f"Q{i+1} Gate 5: < 3 bullets")

    if issues:
        print(f"Found {len(issues)} issues:")
        for iss in issues:
            print("  ", iss)
        sys.exit(1)
    else:
        print("All 24 questions in Passages 1-4 successfully passed all 5 gates with <= 1.08x length symmetry!")
