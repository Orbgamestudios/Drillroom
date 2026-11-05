# /home/cgslinde/DrillRoom/DrillRoom/scratch/cars5/p5.py
import json
from validator import validate_passage

passage_text = """<div class="ttl">Passage 5 (Questions 25&ndash;30)</div>
<p>In the late twentieth century, American literary theorist Stanley Fish orchestrated an epistemological revolution that fundamentally destabilized the foundations of Anglo-American criticism. In landmark works culminating in <i>Is There a Text in This Class? The Authority of Interpretive Communities</i> (1980), Fish mounted a dual assault against two entrenched, opposing theoretical camps. On one side was the formalist orthodoxy of New Criticism, which reified the literary text as an autonomous, self-contained verbal icon possessing objective, determinate meanings embedded in the words on the page. On the other side was naive reader-response subjectivism, which celebrated reading as an unconstrained, idiosyncratic psychological adventure wherein each sovereign individual constructs their own solipsistic meaning. Fish radically rejected both poles, asserting that meaning does not reside statically within the printed marks on a page, nor does it originate ex nihilo from an isolated, autonomous consciousness.</p>
<p>Instead, Fish argued that meaning is an active, temporal performance generated through the reading process, and that this performance is entirely governed and enabled by &ldquo;interpretive communities.&rdquo; An interpretive community is not merely a social club or an organized guild of scholars; it is an internalized network of shared cultural assumptions, linguistic conventions, interpretive strategies, and institutional norms. These communal strategies precede the individual reader, systematically shaping what a reader can perceive, recognize, and articulate in any verbal sequence. According to Fish, texts do not possess intrinsic formal properties that compel a particular interpretation; rather, it is the interpretive strategy deployed by a community that actively brings those textual properties into existence. In Fish&rsquo;s provocative formulation, interpreters do not decode poems; rather, communal interpretive strategies create poems.</p>
<p>To substantiate this radical anti-foundationalist claim, Fish frequently recounted a famous experiment from his university teaching. Upon entering a classroom, Fish drew a frame around a list of surnames remaining on the blackboard from a previous linguistics lecture&mdash;Jacobs-Rosenbaum, Levin, Thorne&mdash;and informed his incoming literature students that the list was a seventeenth-century religious devotional poem. Trained in the conventions of Christian metaphysical poetry, the students immediately &ldquo;discovered&rdquo; intricate allegorical meanings, discerning references to the Hebrew Scriptures, the New Jerusalem, and sacramental theology within the syllables of the names. For Fish, this episode demonstrated that the students were not projecting subjective fantasies onto an objective text, nor were they discovering properties latent within the names. Rather, they were applying a shared institutional strategy for reading religious verse, and that strategy itself generated the poem&rsquo;s formal characteristics, themes, and aesthetic unity.</p>
<p>Fish&rsquo;s framework elicited vehement resistance from traditionalists and progressive theorists alike, who warned that his model collapsed into nihilistic relativism or institutional authoritarianism. If textual meaning is entirely determined by communal conventions without any objective anchor in the verbal artifact, critics argued, then there is no independent, neutral standard by which to evaluate competing interpretations or correct erroneous readings. Furthermore, if individuals are entirely products of their interpretive communities, genuine critical dissent and paradigm shifts would appear impossible, reducing scholarship to the self-perpetuating dogma of whoever controls institutional power. In response, Fish maintained that solipsistic relativism is an impossible phantom because no reader ever exists outside of an interpretive community; within any given community, standards of evidence and validity are experienced as fully binding and objective. Disagreements are settled not by appealing to a mythical &ldquo;text-in-itself,&rdquo; but through the rhetorical art of persuasion operating within institutional discourse.</p>"""

# Questions for Passage 5:
# Target answers: Q25: A, Q26: D, Q27: B, Q28: C, Q29: A, Q30: B
# Parity strictly within 20%!

qs = [
    {
        "q": "The primary purpose of the passage is to:",
        "ch": [
            "explicate Stanley Fish's concept of interpretive communities and examine its theoretical implications.",
            "demonstrate that seventeenth-century religious verse contains superior aesthetic qualities to modern poetry.",
            "defend New Critical formalism against the relativistic excesses of contemporary reader-response theorists.",
            "prove that classroom students cannot distinguish between linguistic surnames and genuine works of literature."
        ],
        "a": 0,
        "e": "<strong>The passage analyzes Stanley Fish's reader-response philosophy, detailing how his concept of \"interpretive communities\" dismantles both formalist textual autonomy and individual subjectivism, illustrating this through his classroom experiment, and addressing counterarguments concerning relativism and institutional authority.</strong><br><br><em>Distractor Traps:</em><br>&bull; B (True Fact Wrong Question): Religious verse is discussed as an illustrative example in paragraph 3, not to establish its aesthetic superiority.<br>&bull; C (Directional Inversion): Fish attacks New Critical formalism; the passage does not defend New Criticism against Fish.<br>&bull; D (Misattribution of Viewpoint): The classroom anecdote illustrates how interpretive strategies produce textual features, not that students lack basic intelligence or discernment."
    },
    {
        "q": "According to the passage, an \"interpretive community\" is best understood as:",
        "ch": [
            "a formal legal board that licenses professional literary critics and authors before publication.",
            "an informal collection of isolated individuals who harbor completely random subjective opinions.",
            "a commercial publishing conglomerate that determines the retail price of printed literature.",
            "a shared framework of institutional conventions and strategies that governs reading practices."
        ],
        "a": 3,
        "e": "<strong>Paragraph 2 explicitly defines an interpretive community as \"an internalized network of shared cultural assumptions, linguistic conventions, interpretive strategies, and institutional norms\" that shapes what readers perceive, recognize, and articulate.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Plausible Extrapolation Not in Passage): An interpretive community is an internalized network of conventions, not a formal legal licensing board.<br>&bull; B (Directional Inversion): Fish explicitly rejects naive subjectivism and random individual opinion, emphasizing shared communal constraints.<br>&bull; C (Misattribution of Viewpoint): Commercial publishing conglomerates relate to economic book production, not Fish's epistemological interpretive strategies."
    },
    {
        "q": "In paragraph 3, Fish's classroom experiment with the list of linguistics professors' surnames is cited primarily to show that:",
        "ch": [
            "students will uncritically accept any false biographical statement made by an authority figure.",
            "the deployment of a communal interpretive strategy actively generates the formal features of a text.",
            "seventeenth-century Christian poets deliberately disguised their verses using complex anagrams.",
            "linguistics professors routinely publish sacred religious allegories under cryptic pseudonyms."
        ],
        "a": 1,
        "e": "<strong>Paragraph 3 explains that the classroom episode demonstrated that students \"were applying a shared institutional strategy for reading religious verse, and that strategy itself generated the poem's formal characteristics, themes, and aesthetic unity.\"</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Misattribution of Viewpoint): Fish's point was epistemological (how interpretive strategies create text properties), not a psychological claim about student gullibility.<br>&bull; C (Plausible Extrapolation Not in Passage): The surnames were from modern linguistics professors, not 17th-century anagrams.<br>&bull; D (Plausible Extrapolation Not in Passage): The list was ordinary names left on a board, not cryptic religious allegories."
    },
    {
        "q": "Based on the passage, how would Stanley Fish most likely respond to a New Critic who asserts that a poem's meaning is permanently fixed within its internal verbal structure?",
        "ch": [
            "By agreeing that the physical paper and typography dictate an unalterable, universal aesthetic interpretation.",
            "By asserting that every individual reader creates completely private meanings that cannot be evaluated by others.",
            "By arguing that what the New Critic considers \"fixed textual evidence\" is itself an artifact of interpretive rules.",
            "By conceding that scientific linguistic analysis can objectively prove the true psychological intent of the author."
        ],
        "a": 2,
        "e": "<strong>Paragraphs 1 and 2 explain that Fish rejects the idea that texts possess intrinsic properties that compel an interpretation, arguing that the interpretive strategies deployed by a community bring those textual properties into existence. Therefore, what the New Critic calls \"objective verbal evidence\" is actually produced by the New Critic's interpretive methodology.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Fish directly denies that the physical text or typography dictates meaning.<br>&bull; B (Misattribution of Viewpoint): This is naive reader subjectivism, which Fish specifically rejects alongside formalism.<br>&bull; D (Misattribution of Viewpoint): Fish rejects both objective textual determinism and authorial psychological intent."
    },
    {
        "q": "Which of the following scenarios best exemplifies the operation of an \"interpretive community\" as described in the passage?",
        "ch": [
            "A group of trained patent attorneys examining a document and identifying identical legal claims and ambiguities.",
            "A hermit who invents a completely private, unwritten language that is indecipherable to any other human being.",
            "A computer programmer who uses an automated algorithm to count the total syllable length of random words.",
            "An eccentric collector who buys rare manuscripts solely based on the monetary value of their leather bindings."
        ],
        "a": 0,
        "e": "<strong>Paragraph 2 defines an interpretive community as a group sharing internalized conventions, institutional norms, and interpretive strategies. Patent attorneys sharing specialized legal training, institutional norms, and reading strategies that govern how they interpret patent documents perfectly exemplifies an interpretive community.</strong><br><br><em>Distractor Traps:</em><br>&bull; B (Directional Inversion): A hermit with an idiosyncratic private language represents radical solipsism, which Fish explicitly rejects.<br>&bull; C (Plausible Extrapolation Not in Passage): Mechanical syllable counting is an automated physical tally, not an interpretive strategy generating meaning.<br>&bull; D (Misattribution of Viewpoint): Valuing leather bindings is commercial commodity collecting, not textual interpretation."
    },
    {
        "q": "The passage implies that critics who accused Fish of promoting \"nihilistic relativism\" failed to appreciate his belief that:",
        "ch": [
            "all written literature possesses an immutable core of grammatical truth that resists subjective distortion.",
            "readers are always already constrained by communal norms that provide binding standards of validity.",
            "individual readers have the sovereign power to invent new interpretive methods completely on their own.",
            "institutional academic power will inevitably be overthrown by spontaneous grassroots reader rebellions."
        ],
        "a": 1,
        "e": "<strong>Paragraph 4 states that critics feared relativism, but \"Fish maintained that solipsistic relativism is an impossible phantom because no reader ever exists outside of an interpretive community; within any given community, standards of evidence and validity are experienced as fully binding and objective.\"</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Fish completely denies that literature has an immutable core of objective truth.<br>&bull; C (Directional Inversion): Fish argues that individuals cannot invent methods outside communal structures; readers are always shaped by pre-existing communal strategies.<br>&bull; D (Plausible Extrapolation Not in Passage): Fish does not predict grassroots overthrow of institutions; he analyzes how institutional persuasion functions."
    }
]

passage_data = {
    "id": "exam_cars90_5_p5",
    "sec": "CARS",
    "topic": "Reader-Response Theory & Interpretive Communities / Stanley Fish",
    "sheet": None,
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_5",
    "passage": passage_text,
    "qs": qs
}

if __name__ == "__main__":
    errs, wc = validate_passage(passage_data, 5, 6)
    if errs:
        print("ERRORS in P5:")
        for e in errs:
            print(" -", e)
    else:
        print(f"P5 PASSED VALIDATION! Word count: {wc}")
