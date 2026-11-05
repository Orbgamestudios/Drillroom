import sys
from validator import validate_passage

passage_data = {
    "id": "exam_cars90_7_p2",
    "sec": "CARS",
    "topic": "Oral Poetic Form vs Print Epistemology (Walter Ong)",
    "sheet": None,
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_7",
    "passage": """<div class=\"ttl\">Passage 2 (Questions 7&ndash;12)</div>
<p>Modern literate humans inhabit a cognitive universe shaped so comprehensively by the written word that they reflexively conceptualize thought itself as an intrinsically visual artifact. We visualize texts as spatial architectures, sentences as linear tracks, and vocabulary as discrete lexical tokens cataloged in static dictionaries and repositories. In his seminal 1982 treatise <i>Orality and Literacy</i>, cultural theorist Walter J. Ong argued that this print-conditioned perspective fundamentally distorts our understanding of human intellectual history. For Ong, writing is not an inert, transparent technology that merely records pre-existing speech; rather, it represents a radical cognitive restructuring that transforms the human sensorium, dismantling the psycho-dynamics of &ldquo;primary orality&rdquo;&mdash;cultures untouched by any knowledge of script or typography&mdash;and replacing them with an internalized epistemology of spatialized, typographic silence.</p>
<p>In a primary oral culture, thought is inseparable from the fleeting materiality of sound. Because spoken sound exists only at the precise instant of its disappearance, an oral culture faces an existential challenge: how to effectively preserve and transmit hard-won cultural knowledge from instantaneous oblivion without an external physical archive. Ong, building on the groundbreaking Homeric studies of Milman Parry and Albert Lord, demonstrated that oral societies solve this preservation crisis through highly specialized mnemonic psychodynamics. Knowledge must be embedded in rhythmic, formulaic patterns: recurring metric epithets such as &ldquo;swift-footed Achilles&rdquo; or &ldquo;wine-dark sea,&rdquo; standardized thematic schemas, and heavily aggregative rather than analytical phrasing. An oral narrator does not assemble sentences through isolated conceptual abstraction, but through pre-fabricated thematic clusters. Furthermore, oral discourse is inherently redundant and copious, continually looping back on previously spoken motifs to ensure that neither the speaker nor the listening audience loses track of the evanescent auditory thread.</p>
<p>Moreover, Ong observed that primary orality anchors thought in the communal, agonistic reality of lived human struggle. Without writing to detach concepts from human actors, oral tradition remains participatory, dramatic, and situational, eschewing abstract syllogisms in favor of vividly personalized narrative confrontations. The historical advent of the printing press decisively shattered this acoustic commons. Print definitively spatialized language, translating dynamic, ephemeral auditory events into static, geometric layouts upon a paper page. Through movable alphabetic type cases, exact typographical repeatability, and visual indexation, print created what Ong termed the &ldquo;closure&rdquo; of the text: a printed work appears complete, autonomous, and self-contained, divorcing author from reader and encouraging private, solitary contemplation. Freed from the exhausting cognitive labor of formulaic memorization, the literate mind could divert its energies toward original analytic taxonomy, relentless skepticism, and detached philosophical introspection.</p>
<p>Nevertheless, Ong&rsquo;s paradigm has drawn sharp methodological objections from anthropologists and cultural historians. Critics such as Ruth Finnegan have challenged Ong&rsquo;s &ldquo;Great Divide&rdquo; model, arguing that it posits an excessively rigid, binary chasm between oral and literate cultures. Ethnographic field studies reveal that oral bards frequently engage in profound individual poetic innovation and subtle conceptual critique, disputing the assumption that primary oral thought is purely conservative and formula-bound. Other critics contend that Ong romanticizes the auditory community, overlooking how oral tradition can enforce tribal conformity and hierarchical domination just as ruthlessly as written bureaucratic law. Furthermore, the modern rise of digital telecommunications has ushered in what Ong termed &ldquo;secondary orality&rdquo;&mdash;a contemporary electronic acoustics that blends oral spontaneity with typographic discipline. Despite these necessary scholarly qualifications, Ong&rsquo;s central insight endures: the technologies of communication do not simply convey our ideas; they fundamentally determine how the human mind constructs, organizes, and experiences reality.</p>""",
    "qs": [
        {
            # Q7 (Q1 of P2) - Key: B (1)
            "q": "The primary thesis of the passage is that:",
            "ch": [
                "alphabetic writing systems are inherently superior to oral traditions because they preserve historical facts with flawless empirical accuracy.",
                "literacy and print are cognitive technologies that fundamentally restructure human consciousness rather than mere tools recording speech.",
                "the emergence of secondary digital orality has rendered traditional print epistemologies and analytical introspection completely obsolete.",
                "primary oral poets relied exclusively on repetitive formulaic epithets because their cognitive faculties lacked capacity for innovation."
            ],
            "a": 1,
            "e": "<strong>The passage focuses on Ong's central insight that writing and print are not neutral recording mechanisms, but transformative cognitive technologies that restructure the human sensorium and consciousness, transitioning from primary orality to spatialized typographic thought. Choice B precisely reflects this thesis.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): The passage avoids declaring alphabetic literacy hierarchically superior, portraying it instead as a different cognitive structure with distinct trade-offs.<br>&bull; C (Overgeneralization/Extreme): Paragraph 4 states that secondary orality blends oral spontaneity with typographic discipline, not that print is rendered completely obsolete.<br>&bull; D (Overgeneralization/Extreme): Paragraph 4 refutes the idea that oral bards lacked capacity for innovation, noting they engaged in profound individual poetic creativity."
        },
        {
            # Q8 (Q2 of P2) - Key: D (3)
            "q": "According to the passage, primary oral cultures rely on metric epithets and thematic redundancy primarily because:",
            "ch": [
                "tribal authorities actively mandated standardized vocabulary to enforce rigid political conformity upon performers.",
                "oral audiences lacked the sophisticated intellectual patience required to comprehend complex linear story narratives.",
                "spoken words were considered sacred metaphysical incantations that lost spiritual efficacy if phrased differently.",
                "auditory speech vanishes instantaneously, requiring patterned mnemonic structures to preserve communal knowledge."
            ],
            "a": 3,
            "e": "<strong>Paragraph 2 explains that spoken sound exists only at the moment of disappearance, facing an 'existential challenge: how to effectively preserve and transmit hard-won cultural knowledge from instantaneous oblivion without an external physical archive,' which oral societies solve via metric epithets, schemas, and redundancy.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Misattribution of Viewpoint): Political conformity is discussed in paragraph 4 as a critique of romanticizing oral societies, not as the primary cognitive reason for mnemonic formulas.<br>&bull; B (Plausible Extrapolation Not in Passage): The passage does not claim oral listeners lacked patience for complex narratives, but that sound is evanescent.<br>&bull; C (Plausible Extrapolation Not in Passage): Mnemonic formulas were functional cognitive necessities for memory retrieval, not justified in the text by sacred incantatory taboos."
        },
        {
            # Q9 (Q3 of P2) - Key: A (0)
            "q": "Based on paragraph 3, the \"closure\" of the text brought about by print technology refers to the perception that:",
            "ch": [
                "a printed book is a self-contained, finalized artifact that exists independently of immediate social interaction.",
                "censorship laws in early modern Europe prevented authors from releasing revised second editions of controversial works.",
                "reading should remain a communal vocal activity strictly controlled by religious authorities and scholastic guilds.",
                "human intellectual history reached its final evolutionary stage once mechanical movable type was widely commercialized."
            ],
            "a": 0,
            "e": "<strong>Paragraph 3 defines 'closure' as the condition where 'a printed work appears complete, autonomous, and self-contained, divorcing author from reader and encouraging private, solitary contemplation' due to physical layout and typographical repeatability.</strong><br><br><em>Distractor Traps:</em><br>&bull; B (Plausible Extrapolation Not in Passage): Closure refers to the spatial and epistemological autonomy of the printed object, not legal censorship banning revisions.<br>&bull; C (Directional Inversion): Print fostered solitary, private, silent reading, rather than communal vocal reading controlled by authorities.<br>&bull; D (Overgeneralization/Extreme): Closure describes the material and formal boundary of a printed volume, not the final termination of human intellectual history."
        },
        {
            # Q10 (Q4 of P2) - Key: C (2)
            "q": "Which of the following findings from cultural anthropology, if verified, would lend the strongest support to Ruth Finnegan's critique of Ong?",
            "ch": [
                "Archaeological excavations uncover ancient printing presses in civilizations previously categorized as pre-literate.",
                "Linguistic studies show that modern readers retain printed technical prose significantly longer than spoken audio lectures.",
                "Fieldwork reveals an illiterate oral society where poets compose highly idiosyncratic verses that intentionally break metric formulas.",
                "Cognitive neuroscientists identify identical hemispheric brain activation during both silent text reading and oral storytelling."
            ],
            "a": 2,
            "e": "<strong>Paragraph 4 states that Finnegan challenged Ong's 'Great Divide' by arguing that oral cultures are not merely formula-bound and conservative, citing ethnographic evidence of 'profound individual poetic innovation and subtle conceptual critique.' An illiterate society where poets intentionally break formulas directly corroborates her critique.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Plausible Extrapolation Not in Passage): Finding printing presses in pre-literate societies is historically nonsensical and does not address the poetic mechanics of oral tradition.<br>&bull; B (True Fact Wrong Question): Demonstrating greater retention from print supports Ong's claim about text permanence rather than Finnegan's critique of the oral-literate dichotomy.<br>&bull; D (Plausible Extrapolation Not in Passage): Neurological activation does not evaluate Finnegan's specific anthropological claim regarding individual poetic innovation vs. formulaic tradition."
        },
        {
            # Q11 (Q5 of P2) - Key: B (1)
            "q": "How would Ong most likely characterize a contemporary live audio podcast hosted by two political journalists?",
            "ch": [
                "As an unmediated manifestation of primary orality that functions completely free from typographic and literate logic.",
                "As an example of secondary orality that unites the conversational immediacy of sound with literate analytic research.",
                "As an inferior rhetorical format that degrades the intellectual capacity for sustained linear skepticism and inquiry.",
                "As an archaic survival of tribal mnemonic chanting that relies on formulaic metric epithets to communicate news."
            ],
            "a": 1,
            "e": "<strong>Paragraph 4 describes 'secondary orality' as 'a contemporary electronic acoustics that blends oral spontaneity with typographic discipline.' A modern live audio podcast by journalists perfectly illustrates this hybrid of spoken spontaneity informed by literate, analytical research.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Contemporary broadcasting is secondary orality, not primary orality; it is produced by literate minds and informed by written scripts and digital texts.<br>&bull; C (Misattribution of Viewpoint): Ong viewed communication technologies analytically rather than dismissing modern electronic acoustic media as inferior.<br>&bull; D (Directional Inversion): Podcasts do not rely on Homeric metric epithets to survive memory loss; their hosts are literate and live in an archived digital world."
        },
        {
            # Q12 (Q6 of P2) - Key: D (3)
            "q": "The author's tone toward Walter Ong's scholarly contribution can best be characterized as:",
            "ch": [
                "scathingly dismissive of his binary models and historical oversimplifications of non-Western verbal art.",
                "patronizingly amused by his nostalgic idealization of pre-literate communal storytelling environments.",
                "unconditionally enthusiastic, defending his original theoretical tenets against all modern empirical rebuttals.",
                "respectfully appreciative, acknowledging substantive counterarguments while validating his fundamental insights."
            ],
            "a": 3,
            "e": "<strong>Throughout the passage, the author treats Ong's work with serious scholarly appreciation ('seminal 1982 treatise,' 'central insight endures'), while also transparently articulating serious critiques (Finnegan's critique of the Great Divide, romanticization of community), characterizing them as 'necessary scholarly qualifications.' This balances respect with critical nuance.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): The author does not dismiss Ong scathingly; on the contrary, the conclusion affirms that his central insight endures.<br>&bull; B (Misattribution of Viewpoint): The author's tone is serious and scholarly, without patronizing amusement or mockery.<br>&bull; C (Overgeneralization/Extreme): The author does not defend Ong 'unconditionally'; the passage explicitly outlines legitimate anthropological counterarguments."
        }
    ]
}

wc, errs = validate_passage(passage_data, 6)
print(f"Validation: wc={wc}, errors={len(errs)}")
for e in errs:
    print(" ", e)
