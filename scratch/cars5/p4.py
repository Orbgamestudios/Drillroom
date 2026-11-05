# /home/cgslinde/DrillRoom/DrillRoom/scratch/cars5/p4.py
import json
from validator import validate_passage

passage_text = """<div class="ttl">Passage 4 (Questions 19&ndash;24)</div>
<p>During the middle decades of the twentieth century, Anglo-American literary scholarship was fundamentally revolutionized by the ascendancy of New Criticism. Reacting against the nineteenth-century philological tradition that treated literary works as mere biographical artifacts or historical documents, formalist theorists sought to establish literary criticism as an autonomous, rigorous, and disciplined academic enterprise. The philosophical foundation of this formalist revolt was articulated in a pair of landmark essays by literary theorist W. K. Wimsatt Jr. and aesthetic philosopher Monroe Beardsley: &ldquo;The Intentional Fallacy&rdquo; (1946) and &ldquo;The Affective Fallacy&rdquo; (1949). Together, these essays mounted a systematic defense of the literary text as an autonomous ontological entity&mdash;what Cleanth Brooks memorably termed a &ldquo;verbal icon&rdquo;&mdash;whose aesthetic meaning and structural integrity reside strictly within its own formal verbal boundaries, untethered from external circumstance.</p>
<p>In &ldquo;The Intentional Fallacy,&rdquo; Wimsatt and Beardsley directly challenged the pervasive romantic assumption that the true meaning of a poem is identical to the psychological intention of its creator. They argued that an author&rsquo;s private intentions, biographical struggles, or psychological motivations are neither accessible nor desirable standards for judging the success or meaning of a work of literary art. Once a poem is composed and released into the world, it is detached from its author at birth; it becomes an autonomous public object governed by the shared linguistic conventions of the culture. To reconstruct authorial design through private letters, diary entries, or post-hoc authorial commentary is to commit an epistemological error. As Wimsatt and Beardsley famously asserted, judging a poem by its author&rsquo;s intended design confuses the poem with its psychological origins, treating literature as an exercise in amateur psychoanalysis rather than an aesthetic artifact.</p>
<p>To operationalize their theory, Wimsatt and Beardsley established a rigorous distinction between internal and external evidence. Internal evidence is discovered through the close examination of the text itself: the semantic interplay of words, grammatical syntax, meter, imagery, and the historical lexicon available to the author&rsquo;s linguistic community. This evidence is public, verifiable, and structurally grounded. Conversely, external evidence consists of private revelations regarding why or how an author composed the work&mdash;statements in private correspondence, anecdotal confessions, or political manifestos. For the New Critics, external evidence is irrelevant to critical interpretation. If an author&rsquo;s intended meaning is successfully realized within the poem, the text itself will demonstrate it; if the intention is not realized in the verbal fabric, consulting external biography cannot supply the deficiency. Meaning is generated through the formal harmonization of paradox, irony, and ambiguity, not biographical intent.</p>
<p>This rigorous formalism was paired with the repudiation of the &ldquo;Affective Fallacy,&rdquo; which warningly proscribed evaluating a literary work based on its emotional impact upon the reader. To judge a poem by whether it makes a reader weep, swoon, or experience catharsis, the New Critics argued, is to dissolve objective criticism into impressionistic subjectivism and psychological relativism. Predictably, New Criticism attracted severe backlash from later theoretical paradigms. Historicists, Marxists, and feminist scholars indicted New Criticism for enclosing literature within an ahistorical vacuum, systematically severing texts from the socioeconomic realities of race, class, and gender oppression. Furthermore, post-structuralists demonstrated that linguistic signs are inherently unstable, undermining the New Critical ideal of organic, self-contained textual harmony. Nevertheless, by banishing biographical gossip and establishing the primacy of rigorous close reading, New Criticism permanently elevated textual scrutiny to the foundational methodology of modern literary analysis.</p>"""

# Questions for Passage 4:
# Target answers: Q19: D, Q20: B, Q21: C, Q22: A, Q23: B, Q24: D
# Parity strictly within 20%!

qs = [
    {
        "q": "Which of the following statements most accurately expresses the central thesis of the passage?",
        "ch": [
            "Wimsatt and Beardsley proved that authorial psychology is the only reliable guide to literary interpretation.",
            "The Affective Fallacy successfully demonstrated that emotional responses are more objective than verbal syntax.",
            "Post-structuralist theory adopted New Criticism's belief in organic textual unity to discredit biographical gossip.",
            "New Criticism established textual autonomy by rejecting both authorial intention and subjective emotional reaction."
        ],
        "a": 3,
        "e": "<strong>The central thesis of the passage is that New Criticism revolutionized literary study by asserting the ontological autonomy of the text (as a \"verbal icon\") and banishing both authorial intent (the intentional fallacy) and reader emotion (the affective fallacy) in favor of rigorous close reading of internal formal structures.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Wimsatt and Beardsley argued the exact opposite—that authorial psychology is neither accessible nor desirable as a standard.<br>&bull; B (Directional Inversion): The Affective Fallacy argued that emotional responses dissolve objective criticism into impressionistic subjectivism.<br>&bull; C (Misattribution of Viewpoint): Post-structuralists undermined rather than adopted New Criticism's belief in organic textual unity."
    },
    {
        "q": "According to Wimsatt and Beardsley, committing the \"Intentional Fallacy\" involves:",
        "ch": [
            "evaluating a poem based on the sociological and economic status of its intended working-class readers.",
            "confusing the internal aesthetic meaning of an artwork with the psychological motivations of its creator.",
            "relying solely on the public linguistic lexicon and grammar of an era to decipher metaphorical ambiguities.",
            "insisting that a poem's structural balance must evoke a specific psychological catharsis in the audience."
        ],
        "a": 1,
        "e": "<strong>Paragraph 2 explains that the Intentional Fallacy occurs when critics judge a poem by its author's intended design, which \"confuses the poem with its psychological origins, treating literature as an exercise in amateur psychoanalysis rather than an aesthetic artifact.\"</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Misattribution of Viewpoint): Evaluating a text based on the socio-economic status of readers describes Marxist/sociological criticism, not the Intentional Fallacy.<br>&bull; C (Directional Inversion): Relying on the public linguistic lexicon is what New Critics endorse as valid internal evidence.<br>&bull; D (Misattribution of Viewpoint): Judging a work by audience catharsis is the Affective Fallacy, not the Intentional Fallacy."
    },
    {
        "q": "Based on the distinction between internal and external evidence in paragraph 3, a New Critic would consider which of the following valid evidence for interpreting a poem?",
        "ch": [
            "A confidential diary entry in which the poet discloses their secret romantic longing for a distant neighbor.",
            "A letter written to a publisher explaining the philosophical symbolism the author intended to communicate.",
            "The grammatical relationships, recurring metaphors, and historical definitions of words used in the verse.",
            "A recorded interview in which the author discusses how their political disillusionment inspired the work."
        ],
        "a": 2,
        "e": "<strong>Paragraph 3 explicitly identifies internal evidence as that \"discovered through the close examination of the text itself: the semantic interplay of words, grammatical syntax, meter, imagery, and the historical lexicon available to the author's linguistic community.\"</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Misattribution of Viewpoint): A private diary entry is external evidence explicitly barred by New Critics.<br>&bull; B (Misattribution of Viewpoint): A letter to a publisher stating authorial intent is classic external evidence.<br>&bull; D (Misattribution of Viewpoint): An interview discussing political inspiration constitutes external biographical evidence."
    },
    {
        "q": "It can be inferred from the passage that New Critics viewed a published poem as an object that is:",
        "ch": [
            "publicly owned and governed by shared linguistic conventions rather than private authorial intentions.",
            "continually rewritten and redefined by the fluctuating emotional impressions of successive generations of readers.",
            "inseparable from the economic class relations and material modes of production operating during its creation.",
            "inherently incomplete until the author issues an authoritative commentary clarifying its paradoxical themes."
        ],
        "a": 0,
        "e": "<strong>Paragraph 2 states that once a poem is published, it \"is detached from its author at birth; it becomes an autonomous public object governed by the shared linguistic conventions of the culture,\" rather than remaining tied to authorial intention.</strong><br><br><em>Distractor Traps:</em><br>&bull; B (Misattribution of Viewpoint): Fluctuating emotional reader responses represent reader-response theory and the Affective Fallacy, which New Critics rejected.<br>&bull; C (Misattribution of Viewpoint): Inseparability from economic class relations reflects Marxist criticism, not New Criticism.<br>&bull; D (Directional Inversion): New Critics held that authorial commentary cannot supply missing meaning and is irrelevant to the autonomous text."
    },
    {
        "q": "Suppose a newly discovered letter by John Keats explicitly states that his \"Ode on a Grecian Urn\" was composed as an allegory celebrating Victorian industrial machinery. How would Wimsatt and Beardsley most likely evaluate this discovery?",
        "ch": [
            "They would immediately revise all critical readings of the poem to reflect Keats's newly revealed political allegory.",
            "They would dismiss the letter as external evidence that cannot alter the meaning established by the poem's own text.",
            "They would argue that the letter proves the poem is an aesthetic failure that should be excluded from the literary canon.",
            "They would praise the discovery as definitive empirical proof that biographical intent determines literary meaning."
        ],
        "a": 1,
        "e": "<strong>Paragraph 3 states that for New Critics, statements in private correspondence are external evidence that is \"irrelevant to critical interpretation. If an author's intended meaning is successfully realized within the poem, the text itself will demonstrate it; if the intention is not realized in the verbal fabric, consulting external biography cannot supply the deficiency.\"</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Revising interpretation based on authorial letters directly commits the Intentional Fallacy.<br>&bull; C (Overgeneralization/Extreme): Discovering an external letter does not render the poem itself an aesthetic failure; the poem is evaluated on its internal text.<br>&bull; D (Directional Inversion): New Critics vehemently denied that biographical intent determines meaning."
    },
    {
        "q": "The passage suggests that later historicist and Marxist theorists criticized New Criticism primarily because it:",
        "ch": [
            "placed excessive pedagogical emphasis on the private psychological confessions of nineteenth-century poets.",
            "rejected objective textual analysis in favor of subjective, highly impressionistic emotional reactions.",
            "denied that literature possessed any meaningful formal structure or metaphorical coherence whatsoever.",
            "isolated literary texts from the social, political, and material conditions in which they were produced."
        ],
        "a": 3,
        "e": "<strong>Paragraph 4 notes that historicists, Marxists, and feminists \"indicted New Criticism for enclosing literature within an ahistorical vacuum, systematically severing texts from the socioeconomic realities of race, class, and gender oppression.\"</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): New Criticism banished private psychological confessions; it did not emphasize them.<br>&bull; B (Misattribution of Viewpoint): New Criticism championed objective textual analysis and rejected impressionistic emotional reactions (via the Affective Fallacy).<br>&bull; C (Directional Inversion): New Critics placed paramount emphasis on formal structure, paradox, and metaphorical coherence."
    }
]

passage_data = {
    "id": "exam_cars90_5_p4",
    "sec": "CARS",
    "topic": "New Criticism & The Intentional Fallacy / Wimsatt & Beardsley",
    "sheet": None,
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_5",
    "passage": passage_text,
    "qs": qs
}

if __name__ == "__main__":
    errs, wc = validate_passage(passage_data, 4, 6)
    if errs:
        print("ERRORS in P4:")
        for e in errs:
            print(" -", e)
    else:
        print(f"P4 PASSED VALIDATION! Word count: {wc}")
