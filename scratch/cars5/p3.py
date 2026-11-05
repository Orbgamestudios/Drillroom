# /home/cgslinde/DrillRoom/DrillRoom/scratch/cars5/p3.py
import json
from validator import validate_passage

passage_text = """<div class="ttl">Passage 3 (Questions 13&ndash;18)</div>
<p>For over a century, orthodox Anglo-American literary scholarship operated under the liberal humanist assumption that great literature constitutes a timeless repository of universal human truths. In the traditionalist vision championed by figures such as Matthew Arnold in the Victorian era and later F. R. Leavis in the twentieth century, literary masterpieces were conceived as transcendent aesthetic monuments that rise above the sordid, transient contingencies of historical conflict, offering spiritual sustenance and moral refinement. However, in seminal works such as <i>Marxism and Literary Criticism</i> (1976) and <i>Literary Theory: An Introduction</i> (1983), the British cultural theorist Terry Eagleton launched a devastating assault on this foundational mystification. Drawing upon historical materialism, Eagleton insisted that &ldquo;Literature&rdquo; with a capital &ldquo;L&rdquo; is neither an autonomous metaphysical realm nor an immutable category of natural genius. Rather, it is a historically contingent ideological construct, deeply entangled in the material relations of production, class hegemony, institutional gatekeeping, and political power.</p>
<p>To demystify the sacred status of the literary canon, Eagleton traced the institutional genealogy of English studies in nineteenth-century Britain. As the Industrial Revolution deepened class antagonisms and widespread secularization eroded the pacifying authority of the Church, the British ruling classes confronted an urgent crisis of social cohesion and political legitimacy. Religion, historically the primary ideological mechanism for instilling moral obedience, patience, and social deference among the working classes, was visibly losing its institutional grip. In response, Eagleton demonstrated, the Victorian state and educational reformers consciously elevated the study of English literature as a secular substitute for religion. By steeping working-class and colonial subjects in the moral contemplation of national literary masterworks, bourgeois authorities sought to foster a synthetic national identity, diffuse radical political agitation, and cultivate docile social sensibilities without resorting to overt military coercion.</p>
<p>Yet Eagleton&rsquo;s Marxist aesthetics sharply distinguishes itself from the crude, reductive economic determinism often associated with &ldquo;vulgar&rdquo; Marxism. Crude determinists treated literary texts as mere passive reflections&mdash;superstructural mirrors that mechanically reproduced the economic base of their historical era, directly reflecting class interests. Rejecting this mechanical reflection theory, Eagleton drew upon Louis Althusser&rsquo;s structural Marxism and Pierre Macherey&rsquo;s influential concept of literary production. According to Macherey, an author does not merely transcribe a pre-existing ideological worldview; instead, the literary text actively works upon ideology, transmuting raw ideological materials into aesthetic form. In doing so, the artwork often reveals the fissures, silences, and internal contradictions of the very ideology it ostensibly seeks to legitimize. Great literature, Eagleton argued, is significant not because it offers a seamless ideological doctrine, but because its formal complexities inadvertently dramatize what ideology cannot say, rendering visible the ideological boundaries that imprison human consciousness.</p>
<p>Traditionalist critics have responded to Eagleton with fierce indignation, accusing Marxist literary theory of reductive cynicism and ideological vandalism. Aesthetic purists contend that by reducing literary masterpieces to ideological instruments of social control or class conflict, Eagleton strips literature of its unique affective power, subjective wonder, and transcendent aesthetic pleasure. They argue that readers throughout history have found authentic existential meaning in Shakespeare or Keats that cannot be explained away by bourgeois class interests. To this charge, Eagleton replied that acknowledging literature&rsquo;s ideological lineage does not require denying its formal brilliance. On the contrary, demystifying the myth of pure aesthetic autonomy frees criticism from sentimental illusions, enabling readers to appreciate literature as a dynamic, contested social practice embedded in human history.</p>"""

# Questions for Passage 3:
# Target answers: Q13: C, Q14: A, Q15: D, Q16: B, Q17: C, Q18: A
# Parity strictly within 20%!

qs = [
    {
        "q": "The primary purpose of the passage is to:",
        "ch": [
            "prove that Victorian educational reforms were solely intended to suppress working-class literacy.",
            "defend traditional liberal humanism against the ideological critiques launched by Terry Eagleton.",
            "examine Terry Eagleton's Marxist critique of literature as a historically conditioned ideological construct.",
            "demonstrate that crude economic determinism provides the most accurate method for analyzing poetry."
        ],
        "a": 2,
        "e": "<strong>The passage focuses on Terry Eagleton's Marxist theoretical framework, analyzing how he demystifies the liberal humanist concept of \"Literature,\" investigates the Victorian genealogy of English studies, contrasts sophisticated Marxist aesthetics with crude determinism, and addresses traditionalist counterarguments.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Overgeneralization/Extreme): Paragraph 2 discusses how English literature was used to diffuse political agitation, not that reforms were solely designed to suppress literacy.<br>&bull; B (Directional Inversion): The author presents Eagleton's critiques as a powerful demystification of liberal humanism, not a defense of humanism against Eagleton.<br>&bull; D (Directional Inversion): Paragraph 3 explicitly rejects crude economic determinism (\"vulgar Marxism\") in favor of a nuanced Althusserian/Machereyan model of literary production."
    },
    {
        "q": "According to the passage, the Victorian establishment promoted the study of English literature primarily because it:",
        "ch": [
            "served as a secular instrument for moral pacification and social cohesion when religious influence waned.",
            "guaranteed higher industrial productivity by providing factory laborers with technical and scientific skills.",
            "encouraged the working classes to organize radical political unions against bourgeois factory owners.",
            "eliminated all class distinctions across Britain by fostering widespread artistic and theatrical patronage."
        ],
        "a": 0,
        "e": "<strong>Paragraph 2 states that as secularization eroded the Church's pacifying authority during the Industrial Revolution, Victorian authorities consciously elevated English literature as a secular substitute for religion to \"diffuse radical political agitation, and cultivate docile social sensibilities without resorting to overt military coercion.\"</strong><br><br><em>Distractor Traps:</em><br>&bull; B (Plausible Extrapolation Not in Passage): The passage emphasizes moral contemplation and docile social sensibilities, not technical or scientific workplace skills.<br>&bull; C (Directional Inversion): The institution was promoted to \"diffuse radical political agitation,\" not encourage unionization.<br>&bull; D (Overgeneralization/Extreme): The promotion was designed to preserve ruling-class hegemony and deference, not eliminate all class distinctions."
    },
    {
        "q": "Based on the passage, how does Eagleton's Marxist aesthetic differ from \"vulgar\" Marxist literary criticism?",
        "ch": [
            "Eagleton asserts that literature possesses an absolute, timeless autonomy completely divorced from economics.",
            "Eagleton restricts his critical analysis exclusively to nineteenth-century British industrial poetry and drama.",
            "Eagleton claims that an author's personal psychological neuroses are more important than class structures.",
            "Eagleton rejects the notion that literature is merely a passive, mechanical mirror of the economic base."
        ],
        "a": 3,
        "e": "<strong>Paragraph 3 explicitly contrasts Eagleton with \"crude, reductive economic determinism often associated with 'vulgar' Marxism,\" which treated texts as mere superstructural mirrors of the economic base, explaining that Eagleton views the literary text as actively working upon ideology and exposing its internal contradictions.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Misattribution of Viewpoint): Autonomy divorced from economics is the liberal humanist view that Eagleton vehemently rejects.<br>&bull; B (Plausible Extrapolation Not in Passage): Eagleton does not restrict his analysis only to 19th-century industrial poetry.<br>&bull; C (Misattribution of Viewpoint): Focus on personal psychological neuroses characterizes psychoanalytic criticism, not Eagleton's historical materialism."
    },
    {
        "q": "It can be inferred from the passage that Pierre Macherey's concept of \"literary production\" implies that an effective critique of a text should:",
        "ch": [
            "celebrate the author as an unconstrained genius who possesses complete mastery over ideological biases.",
            "interrogate what the text omits or cannot say to expose the underlying contradictions of its historical era.",
            "evaluate an artwork solely by calculating the commercial royalties earned by its publishing syndicate.",
            "condemn any literary work whose characters do not explicitly endorse revolutionary socialist politics."
        ],
        "a": 1,
        "e": "<strong>Paragraph 3 explains that Macherey's concept shows how an artwork \"reveals the fissures, silences, and internal contradictions of the very ideology it ostensibly seeks to legitimize\" and \"inadvertently dramatize[s] what ideology cannot say.\" Thus, effective critique focuses on these ideological silences and fractures.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Macherey rejects the liberal humanist myth of the author as an autonomous, unconstrained genius.<br>&bull; C (Plausible Extrapolation Not in Passage): Analyzing royalties is crude commercial calculation, not Macherey's focus on formal ideological contradictions.<br>&bull; D (Overgeneralization/Extreme): Macherey and Eagleton do not require characters to voice socialist slogans; they analyze how formal tensions reveal ideological limits."
    },
    {
        "q": "Which of the following literary analyses best exemplifies Eagleton's theoretical approach as described in the passage?",
        "ch": [
            "Examining how a Renaissance sonnet's strict rhyming scheme achieves universal, transcendent spiritual harmony.",
            "Analyzing a modern novel strictly through the documented childhood trauma and private journals of its author.",
            "Investigating how an eighteenth-century novel's narrative silences reveal tensions regarding colonial plantation wealth.",
            "Surveying readers in multiple countries to record their subjective emotional tears while reading an epic tragedy."
        ],
        "a": 2,
        "e": "<strong>Paragraph 3 emphasizes that literary production reveals the \"fissures, silences, and internal contradictions of the very ideology it ostensibly seeks to legitimize,\" exposing ideological entanglements in material relations of production (colonialism, class hegemony). Investigating how narrative silences conceal or expose colonial plantation wealth directly reflects this methodology.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Misattribution of Viewpoint): Celebrating \"universal, transcendent spiritual harmony\" reflects the liberal humanism of Matthew Arnold that Eagleton attacks.<br>&bull; B (Misattribution of Viewpoint): Focusing on authorial childhood trauma reflects biographical/psychoanalytic criticism rather than Marxist historical materialism.<br>&bull; D (Misattribution of Viewpoint): Measuring subjective emotional tears exemplifies affective reader response, not ideological demystification."
    },
    {
        "q": "Traditionalist critics mentioned in paragraph 4 would most likely challenge Eagleton by asserting that:",
        "ch": [
            "great literature possesses an enduring aesthetic and affective value that transcends socio-economic origins.",
            "nineteenth-century British educational reformers were secretly dedicated to promoting socialist revolutions.",
            "literary texts are purely commercial commodities that have no capacity to evoke personal emotional feelings.",
            "the study of English literature should be completely abolished in favor of theological religious doctrine."
        ],
        "a": 0,
        "e": "<strong>Paragraph 4 notes that traditionalist aesthetic purists argue Eagleton \"strips literature of its unique affective power, subjective wonder, and transcendent aesthetic pleasure\" and assert that readers \"have found authentic existential meaning in Shakespeare or Keats that cannot be explained away by bourgeois class interests.\"</strong><br><br><em>Distractor Traps:</em><br>&bull; B (Directional Inversion): Traditionalists would not claim Victorian reformers were secret socialists; Victorian reformers sought to diffuse radical agitation.<br>&bull; C (Directional Inversion): Traditionalists argue the exact opposite—that literature is transcendent and affective, not merely a commercial commodity.<br>&bull; D (Overgeneralization/Extreme): Traditionalists champion the study of great literature rather than advocating its abolition."
    }
]

passage_data = {
    "id": "exam_cars90_5_p3",
    "sec": "CARS",
    "topic": "Marxist Aesthetics: Terry Eagleton & The Ideology of Literature",
    "sheet": None,
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_5",
    "passage": passage_text,
    "qs": qs
}

if __name__ == "__main__":
    errs, wc = validate_passage(passage_data, 3, 6)
    if errs:
        print("ERRORS in P3:")
        for e in errs:
            print(" -", e)
    else:
        print(f"P3 PASSED VALIDATION! Word count: {wc}")
