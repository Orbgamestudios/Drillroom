import sys
from validator import validate_passage

passage_data = {
    "id": "exam_cars90_7_p7",
    "sec": "CARS",
    "topic": "Digital Literature & The Hypertextual Dissolution of Linearity",
    "sheet": None,
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_7",
    "passage": """<div class=\"ttl\">Passage 7 (Questions 37&ndash;42)</div>
<p>For more than five centuries, the physical technology of the printed codex exerted an undisputed monopoly over the Western literary imagination. Bound between rigid covers and organized into sequential, numbered pages, the traditional book institutionalized an epistemology of uninterrupted linearity: narratives advanced inexorably from an authorially dictated beginning, through causal complications, to a definitive and immutable conclusion. In the late twentieth century, the emergence of personal computing and digital networks mounted the first radical structural challenge to this typographic hegemony. Anticipated by visionary computer pioneer Theodor Nelson&mdash;who coined the term &ldquo;hypertext&rdquo; in the 1960s to describe non-sequential electronic writing&mdash;literary scholars such as George Landow hailed electronic literature as the practical realization of post-structuralist theory. Hypertext promised nothing less than the dissolution of authorial tyranny, fracturing the monolithic spine of the codex into a democratized, open-ended web of infinite interpretive pathways.</p>
<p>In early electronic hypertext fiction, exemplified by Michael Joyce&rsquo;s groundbreaking <i>afternoon, a story</i> (1987) and Shelley Jackson&rsquo;s <i>Patchwork Girl</i> (1995), the traditional passivity of the reader was decisively shattered. Instead of turning printed pages along a predetermined track, the reader encounters a computer screen of prose composed of discrete textual nodes or &ldquo;lexias&rdquo; embedded with interactive hyperlinks. Clicking a highlighted phrase branches the narrative along divergent thematic pathways, rendering every reading session a unique, idiosyncratic voyage through a multilinear labyrinth. Theorist Espen Aarseth classified such works as &ldquo;ergodic literature&rdquo;&mdash;texts wherein &ldquo;non-trivial effort&rdquo; is actively demanded of the reader to traverse the cybernetic textual landscape. In this digital matrix, the boundary separating author and audience becomes fluid and permeable. The reader ceases to be a receptive consumer of a closed, &ldquo;readerly&rdquo; artifact and transforms into what cyber-theorists termed a &ldquo;wreader&rdquo;&mdash;an active co-creator who dynamically stitches a bespoke narrative architecture out of fragmented textual possibilities.</p>
<p>Early cyber-utopian critics celebrated hypertext as an inherently emancipatory, anti-hierarchical medium that mirrored the associative, non-linear architecture of human consciousness. Post-structuralists argued that by dismantling fixed chronological causality, hypertext instantiated Roland Barthes&rsquo;s famous prophecy of the &ldquo;death of the author,&rdquo; dispersing narrative authority across a decentralized web of interconnected signifiers. In Jackson&rsquo;s <i>Patchwork Girl</i>, a feminist reimagining of Mary Shelley&rsquo;s <i>Frankenstein</i>, the fragmented hypertext format served as a direct formal metaphor for female embodiment and identity assembled from disparate historical scraps, subverting patriarchal narrative coherence through radical aesthetic discontinuity.</p>
<p>Yet this euphoria soon encountered fierce resistance from literary traditionalists and cognitive scientists alike. Critics such as Sven Birkerts, in <i>The Gutenberg Elegies</i>, argued that the dissolution of narrative linearity induces chronic cognitive disorientation, replacing sustained, contemplative immersion with superficial skimming and navigational anxiety. In a text where every sentence offers multiple branching exits, the reader expends cognitive bandwidth deciding where to click next rather than absorbing emotional resonance or thematic depth. Without an authorially engineered conclusion, narrative momentum dissipates into an aimless, anticlimactic maze devoid of dramatic catharsis. Furthermore, media historians observe that standalone hypertext fiction largely withered as a commercial genre; the interactive link was quickly co-opted by corporate web browsers and algorithmic platforms to maximize consumer distraction and advertising revenue rather than aesthetic contemplation. Nonetheless, digital literature permanently altered literary consciousness. By demonstrating that linear progression is merely a contingent mechanical artifact of the printing press, hypertext exposed the printed book as just one possible technological container for the enduring human impulse to weave stories.</p>""",
    "qs": [
        {
            # Q37 (Q1 of P7) - Key: C (2)
            "q": "The primary purpose of the passage is to:",
            "ch": [
                "prove that digital computing has rendered traditional physical libraries and printed novels totally obsolete.",
                "demonstrate that early hypertext fiction failed because authorial control is biologically necessary for comprehension.",
                "examine the theoretical promises, artistic techniques, and cognitive critiques of non-linear digital literature.",
                "advocate for replacing corporate internet search engines with open-source feminist electronic hypertexts."
            ],
            "a": 2,
            "e": "<strong>The passage introduces hypertext's challenge to the codex, examines early hypertext works and ergodic theory (Aarseth, Landow, Jackson), explains theoretical claims regarding the 'death of the author,' evaluates cognitive and literary critiques (Birkerts, commercial co-optation), and summarizes its conceptual impact on literary form. Choice C accurately encapsulates this scope.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Overgeneralization/Extreme): Paragraph 4 explicitly notes that standalone hypertext fiction withered commercially, and the printed book was not completely eradicated.<br>&bull; B (Directional Inversion): The passage explores cognitive challenges, but does not claim authorial control is biologically necessary or that digital literature was a complete failure.<br>&bull; D (Plausible Extrapolation Not in Passage): The passage discusses the co-optation of hyperlinks by corporate platforms as a historical observation, not an activist advocacy campaign."
        },
        {
            # Q38 (Q2 of P7) - Key: B (1)
            "q": "According to the passage, the term \"wreader\" was coined by cyber-theorists to signify that in hypertext literature:",
            "ch": [
                "the author retains absolute tyrannical control over the sequence in which each discrete digital lexia is revealed.",
                "the reader actively participates in constructing the narrative structure by choosing among branching hyperlink paths.",
                "readers must write extensive computer programming code before accessing the introductory chapters of electronic novels.",
                "traditional typographic punctuation marks are replaced by automated algorithmic voice recognition software."
            ],
            "a": 1,
            "e": "<strong>Paragraph 2 explains that in hypertext, 'the reader ceases to be a receptive consumer of a closed, \"readerly\" artifact and transforms into what cyber-theorists termed a \"wreader\"—an active co-creator who dynamically stitches a bespoke narrative architecture out of fragmented textual possibilities' by selecting hyperlinks.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): The concept of the wreader specifically highlights the dismantling of authorial control and reader empowerment.<br>&bull; C (Plausible Extrapolation Not in Passage): 'Non-trivial effort' refers to navigational choices among lexias, not writing raw computer code.<br>&bull; D (Plausible Extrapolation Not in Passage): The passage does not discuss voice recognition or punctuation elimination."
        },
        {
            # Q39 (Q3 of P7) - Key: D (3)
            "q": "Based on paragraph 3, post-structuralist theorists viewed hypertext as an instantiation of the \"death of the author\" because:",
            "ch": [
                "authors of electronic literature invariably published their interactive stories anonymously under fake pseudonyms.",
                "computer algorithms completely eliminated human novelists from writing digital fiction by generating prose automatically.",
                "the physical components of personal computers deteriorated rapidly, destroying digital manuscripts upon publication.",
                "narrative authority was dispersed across a decentralized network of links rather than originating from a singular voice."
            ],
            "a": 3,
            "e": "<strong>Paragraph 3 states that post-structuralists argued that 'by dismantling fixed chronological causality, hypertext instantiated Roland Barthes's famous prophecy of the \"death of the author,\" dispersing narrative authority across a decentralized web of interconnected signifiers' rather than centering on an authoritative voice.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Plausible Extrapolation Not in Passage): Hypertext authors (like Joyce and Jackson) were named and known, not anonymous; the 'death of the author' is a theoretical concept about authority.<br>&bull; B (Misattribution of Viewpoint): Early hypertext was written by human authors using interactive software, not automated generative algorithms.<br>&bull; C (Plausible Extrapolation Not in Passage): The 'death of the author' is not related to hardware obsolescence or file degradation."
        },
        {
            # Q40 (Q4 of P7) - Key: A (0)
            "q": "Which of the following points reflects Sven Birkerts's primary criticism of hypertext in The Gutenberg Elegies?",
            "ch": [
                "Branching choices fragment reader concentration and replace deep contemplation with navigational anxiety.",
                "Electronic literature relies excessively on patriarchal narrative archetypes that restrict feminist self-fashioning.",
                "Computer screens emit electromagnetic radiation that damages the neurological architecture of the visual cortex.",
                "Hypertext fiction requires expensive specialized hardware that prevents working-class citizens from reading."
            ],
            "a": 0,
            "e": "<strong>Paragraph 4 states that Birkerts argued 'the dissolution of narrative linearity induces chronic cognitive disorientation, replacing sustained, contemplative immersion with superficial skimming and navigational anxiety,' as readers expend cognitive energy deciding where to click rather than absorbing thematic depth.</strong><br><br><em>Distractor Traps:</em><br>&bull; B (Misattribution of Viewpoint): Subverting patriarchal archetypes is praised in paragraph 3 regarding Jackson's feminist hypertext, not Birkerts's critique.<br>&bull; C (Plausible Extrapolation Not in Passage): Birkerts's critique is cognitive and literary, not focused on physical radiation.<br>&bull; D (Plausible Extrapolation Not in Passage): Birkerts focused on aesthetic and psychological loss, not economic hardware affordability."
        },
        {
            # Q41 (Q5 of P7) - Key: C (2)
            "q": "In paragraph 3, the author discusses Shelley Jackson's Patchwork Girl primarily to illustrate how:",
            "ch": [
                "technological limitations in early computer software prevented female authors from publishing complex electronic novels.",
                "hypertext fiction was rejected by feminist scholars for imitating the linear conventions of nineteenth-century gothic horror.",
                "non-linear digital form can serve as an aesthetic metaphor for fragmented personal identity and female embodiment.",
                "interactive digital literature quickly surpassed traditional print fiction in global commercial bookstore sales."
            ],
            "a": 2,
            "e": "<strong>Paragraph 3 explains that in <em>Patchwork Girl</em>, 'the fragmented hypertext format served as a direct formal metaphor for female embodiment and identity assembled from disparate historical scraps, subverting patriarchal narrative coherence through radical aesthetic discontinuity.'</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Jackson successfully published and achieved acclaim for <em>Patchwork Girl</em>; it is cited as a triumph of formal innovation.<br>&bull; B (Directional Inversion): The work is praised for subverting linear gothic conventions through aesthetic discontinuity, not rejected.<br>&bull; D (Directional Inversion): Paragraph 4 notes that hypertext fiction withered commercially, rather than surpassing print bookstore sales."
        },
        {
            # Q42 (Q6 of P7) - Key: B (1)
            "q": "The passage implies that the historical trajectory of the hyperlink in modern digital culture resulted in:",
            "ch": [
                "the complete destruction of corporate social media networks by underground avant-garde hypertext novelists.",
                "the commercial co-optation of interactive links into mechanisms for attention extraction and advertising revenue.",
                "the total disappearance of printed codex books from contemporary educational institutions and universities.",
                "the universal adoption of ergodic literature as the mandatory format for all digital legal and medical texts."
            ],
            "a": 1,
            "e": "<strong>Paragraph 4 states that 'the interactive link was quickly co-opted by corporate web browsers and algorithmic platforms to maximize consumer distraction and advertising revenue rather than aesthetic contemplation.' Choice B directly reflects this outcome.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Corporate platforms co-opted the link, while standalone hypertext fiction withered, the opposite of destroying corporate platforms.<br>&bull; C (Directional Inversion): Paragraph 4 affirms that the printed book survived and that standalone hypertext fiction withered.<br>&bull; D (Overgeneralization/Extreme): Ergodic literature was an avant-garde artistic form, never a mandated format for legal and medical documentation."
        }
    ]
}

wc, errs = validate_passage(passage_data, 6)
print(f"Validation: wc={wc}, errors={len(errs)}")
for e in errs:
    print(" ", e)
