# /home/cgslinde/DrillRoom/DrillRoom/scratch/cars5/p9.py
import json
from validator import validate_passage

passage_text = """<div class="ttl">Passage 9 (Questions 49&ndash;53)</div>
<p>Few theoretical interventions by the Frankfurt School of critical theory have incited as much enduring controversy as Theodor W. Adorno&rsquo;s scathing semiotic and sociological dissection of mass commercial jazz. In polemical essays such as &ldquo;On Jazz&rdquo; (1936) and &ldquo;Perennial Fashion&mdash;Jazz&rdquo; (1953), the German philosopher and musicologist mounted a ferocious, uncompromising assault against what was widely celebrated as the most vibrant, democratically liberating musical genre of the twentieth century. While progressive enthusiasts, liberal intellectuals, and commercial promoters lauded jazz for its spontaneous vitality, syncopated liberation from academic European rigidity, and rebellious spirit, Adorno perceived a sinister ideological trap. In his theoretical architecture, commercial jazz was not an authentic expression of human freedom, but the consummate commodity of the &ldquo;Culture Industry&rdquo;&mdash;an industrialized entertainment apparatus that manufactures standardized cultural artifacts designed to pacify the working class, stifle genuine critical consciousness, and train the human sensorium for psychological compliance with modern capitalist discipline.</p>
<p>The semiotic engine of Adorno&rsquo;s critique rested on the dialectic between standardization and what he termed &ldquo;pseudo-individualization.&rdquo; Adorno observed that despite its apparent exuberance and improvisational energy, commercial jazz was anchored to an inflexible, formulaic harmonic framework&mdash;most visibly the predictable thirty-two-bar song form, standard diatonic cadences, and rigid, mechanical metric beats inherited from commercial popular sheet music publishing. What was celebrated as spontaneous improvisation was, in Adorno&rsquo;s analysis, merely a cosmetic illusion. The syncopated accent, the ornamental instrumental flourish, and the improvised solo did not subvert the underlying metric grid; rather, they were pre-packaged, standardized deviations that inevitably resolved back into the dominant rhythmic and harmonic order. For Adorno, pseudo-individualization endowed the commercial commodity with a superficial halo of personal uniqueness and spontaneity, tricking listeners into believing they were experiencing idiosyncratic personal freedom when they were actually consuming interchangeable mass-produced goods designed for passive consumption.</p>
<p>Contemporary ethnomusicologists, African American studies scholars, and cultural theorists have mounted devastating critiques of Adorno&rsquo;s jazz writings, exposing fundamental empirical and cultural blind spots in his theoretical analysis. Critics note that Adorno&rsquo;s perspective was irrevocably distorted by an elitist Eurocentric bias that held the avant-garde twelve-tone serialism of the Second Viennese School (most notably Arnold Schoenberg) as the sole legitimate model of musical autonomy, authentic dialectical negation, and resistance to reification. More egregiously, writing primarily from exile in Frankfurt and the United States, Adorno formed his musical impressions largely from sanitized, commercial European dance-band swing and commodified radio broadcasts, failing to distinguish between white commercial packaging and the rich, subversive vernacular traditions of genuine African American jazz. Theorists such as Amiri Baraka and Henry Louis Gates Jr. demonstrated that in Black musical semiotics, polyrhythms, syncopation, and blues improvisation are not subservient decorative ornaments, but complex modes of counter-hegemonic cultural resistance and communal affirmation forged under systemic racial oppression.</p>
<p>Yet, despite Adorno&rsquo;s undeniable cultural chauvinism and his historical deaf-ear to the liberatory power of Black vernacular music, his broader semiotic critique retains an unsettling prophetic power. In an era dominated by algorithmic streaming platforms that optimize audio tracks for rapid digital consumption, formulaic pop hooks engineered for viral video snippets, and calculated branding that equates consumer novelty with authentic artistic rebellion, Adorno&rsquo;s diagnosis of the Culture Industry feels prescient. By exposing how commercial capital harnesses the illusion of nonconformity to sell standardized commodities, Adorno bequeathed a vital warning regarding the ease with which market imperatives can colonize the human imagination.</p>"""

# Questions for Passage 9:
# Target answers: Q49: A, Q50: B, Q51: C, Q52: D, Q53: B
# Parity strictly within 20%!

qs = [
    {
        "q": "Which of the following statements best summarizes the central thesis of the passage?",
        "ch": [
            "Adorno's critique of commercial jazz revealed commodified standardization, despite his cultural blind spots.",
            "Adorno successfully proved that Arnold Schoenberg's twelve-tone serialism is the only music with aesthetic merit.",
            "Commercial jazz was entirely free from capitalist marketing until algorithmic digital streaming platforms emerged.",
            "African American jazz musicians intentionally designed the thirty-two-bar song structure to pacify white listeners."
        ],
        "a": 0,
        "e": "<strong>The passage evaluates Theodor Adorno's critique of commercial jazz as an ideological product of the Culture Industry characterized by standardization and pseudo-individualization, examines the valid criticisms of his Eurocentric bias and misunderstanding of Black vernacular traditions, and concludes by recognizing the enduring relevance of his critique of commodification.</strong><br><br><em>Distractor Traps:</em><br>&bull; B (Misattribution of Viewpoint): While Adorno personally favored Schoenberg, the author does not endorse this view as the central thesis, explicitly labeling it an \"elitist Eurocentric bias.\"<br>&bull; C (Directional Inversion): Adorno's entire 1930s-1950s critique was that commercial jazz was already heavily commodified by the Culture Industry.<br>&bull; D (Plausible Extrapolation Not in Passage): The passage states that the 32-bar form came from commercial popular publishing, not that Black musicians designed it to pacify white audiences."
    },
    {
        "q": "According to the passage, Adorno used the term \"pseudo-individualization\" to describe:",
        "ch": [
            "the authentic psychological liberation experienced by working-class laborers attending live jazz concerts.",
            "superficial stylistic deviations that create an illusion of personal freedom while obeying standard formulas.",
            "the complete abolition of all metric rhythms and harmonic chord progressions in modern serialist music.",
            "the collaborative process whereby an entire orchestra improvises together without a designated conductor."
        ],
        "a": 1,
        "e": "<strong>Paragraph 2 defines pseudo-individualization as the phenomenon whereby syncopated accents, instrumental flourishes, and improvised solos act as \"standardized deviations that inevitably resolved back into the dominant rhythmic and harmonic order,\" endowing the commodity with a \"superficial halo of personal uniqueness\" while remaining fundamentally standardized.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Adorno viewed the experience of liberation as an ideological illusion, not authentic liberation.<br>&bull; C (Misattribution of Viewpoint): Abolishing metric rhythm describes avant-garde serialism, not pseudo-individualization in commercial jazz.<br>&bull; D (Plausible Extrapolation Not in Passage): Collective improvisation without a conductor is free jazz, not Adorno's definition of commercial pseudo-individualization."
    },
    {
        "q": "Based on paragraph 3, subsequent critics challenged Adorno's analysis of jazz primarily because he:",
        "ch": [
            "praised commercial radio swing bands while ignoring the radical twelve-tone compositions of Arnold Schoenberg.",
            "claimed that European classical traditions were completely devoid of intellectual discipline and formal rigor.",
            "conflated sanitized commercial dance music with the subversive vernacular traditions of Black jazz musicians.",
            "argued that listening to recorded music on the radio was superior to attending unamplified live performances."
        ],
        "a": 2,
        "e": "<strong>Paragraph 3 points out that Adorno formed his impressions from sanitized European swing and commercial broadcasts, \"failing to distinguish between white commercial packaging and the rich vernacular traditions of genuine African American jazz,\" where improvisation and polyrhythms functioned as counter-hegemonic cultural resistance.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Adorno championed Schoenberg and attacked commercial swing, not the other way around.<br>&bull; B (Directional Inversion): Adorno championed European high-modernist classical rigor.<br>&bull; D (Plausible Extrapolation Not in Passage): Adorno did not claim radio listening was superior to live performance."
    },
    {
        "q": "Which of the following musical phenomena best exemplifies Adorno's concept of the \"Culture Industry\" as described in the passage?",
        "ch": [
            "An underground avant-garde ensemble performing atonality for ten people in an abandoned industrial warehouse.",
            "A traditional folk singer performing unrecorded ancestral lullabies passed down orally through centuries.",
            "A solitary pianist composing complex experimental counterpoint exclusively for personal spiritual study.",
            "A record label releasing dozens of pop songs with identical chord progressions and minor cosmetic variations."
        ],
        "a": 3,
        "e": "<strong>The Culture Industry mass-produces standardized cultural goods with minor, calculated stylistic variations (pseudo-individualization) to ensure mass market consumption. Releasing dozens of pop songs sharing identical chord progressions with minor cosmetic tweaks is the definitive manifestation of this concept.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Misattribution of Viewpoint): Underground atonal ensembles performing for tiny audiences resist commercial commodification, resembling Schoenbergian high modernism.<br>&bull; B (Misattribution of Viewpoint): Unrecorded oral ancestral lullabies exist entirely outside commercial mass production.<br>&bull; C (Misattribution of Viewpoint): Solitary non-commercial composition is private aesthetic practice, not industrial culture."
    },
    {
        "q": "The author's discussion of algorithmic streaming platforms in the final paragraph serves primarily to:",
        "ch": [
            "prove that contemporary digital streaming services have completely eliminated capitalist monopolies in music.",
            "demonstrate that Adorno's warnings regarding commodification and engineered conformity remain relevant today.",
            "urge modern consumers to abandon popular commercial music in favor of mid-century German twelve-tone serialism.",
            "refute the claims made by African American studies scholars regarding the counter-hegemonic power of the blues."
        ],
        "a": 1,
        "e": "<strong>Paragraph 4 connects Adorno's critique to contemporary algorithmic streaming platforms and viral marketing to argue that despite his historical blind spots, \"Adorno's diagnosis of the Culture Industry feels prescient\" and serves as a vital warning about how market imperatives colonize the human imagination.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Streaming platforms optimize tracks for rapid consumption and commercial profit, exemplifying commodification rather than eliminating monopolies.<br>&bull; C (Overgeneralization/Extreme): The author does not instruct consumers to listen only to twelve-tone serialism.<br>&bull; D (Directional Inversion): The author agrees with African American scholars that Adorno had serious cultural blind spots; the discussion of streaming does not refute their claims."
    }
]

passage_data = {
    "id": "exam_cars90_5_p9",
    "sec": "CARS",
    "topic": "Musical Semiotics: Theodor Adorno's Critique of Mass Jazz",
    "sheet": None,
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_5",
    "passage": passage_text,
    "qs": qs
}

if __name__ == "__main__":
    errs, wc = validate_passage(passage_data, 9, 5)
    if errs:
        print("ERRORS in P9:")
        for e in errs:
            print(" -", e)
    else:
        print(f"P9 PASSED VALIDATION! Word count: {wc}")
