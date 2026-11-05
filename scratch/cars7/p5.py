import sys
from validator import validate_passage

passage_data = {
    "id": "exam_cars90_7_p5",
    "sec": "CARS",
    "topic": "Camp Aesthetics: Susan Sontag & The Triumph of Stylistic Irony",
    "sheet": None,
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_7",
    "passage": """<div class=\"ttl\">Passage 5 (Questions 25&ndash;30)</div>
<p>In 1964, cultural critic Susan Sontag published &ldquo;Notes on &lsquo;Camp,&rsquo;&rdquo; an intellectual bombshell that catapulted a hitherto clandestine sensibility into mainstream critical discourse. Sontag recognized that sensibility is notoriously resistant to systematic codification; to capture Camp, she composed fifty-eight numbered jottings that sketched the elusive contours of a taste that revels in artifice, stylistic excess, and theatricality. For Sontag, the essence of Camp is its unapologetic love of the unnatural&mdash;of exaggeration, flamboyant performance, and the decisive triumph of style over content, texture over substance, and aestheticism over moral earnestness. Rather than judging human expression through the rigid binary of good versus bad art, Camp offers an affectionate, ironic lens that discovers aesthetic ecstasy precisely where conventional bourgeois taste discerns only failure, triviality, or vulgarity. In doing so, it directly challenged the solemn, puritanical high modernism that had dominated mid-century Western literary criticism.</p>
<p>Central to Sontag&rsquo;s taxonomy is the distinction between &ldquo;pure&rdquo; or &ldquo;naive&rdquo; Camp and its self-conscious, &ldquo;deliberate&rdquo; counterpart. Naive Camp, which Sontag regarded as the supreme and most authentic manifestation, is marked by dead seriousness. It arises when an ambitious creator undertakes an extravagant, passionate project with utter sincerity, only to fail spectacularly due to excessive grandiosity. Examples abound in the ornate, organic extravagances of Art Nouveau, Tiffany lamps, and Busby Berkeley&rsquo;s synchronized Hollywood musicals. The beauty of naive Camp lies in its earnest innocence: the artist intended to create sublime tragedy or monumental elegance, but produced an unintentional monument to artifice. Deliberate Camp, by contrast, is calculated and premeditated; by intentionally trying to be campy, it sacrifices the authentic tension of heroic failure and often descends into sterile kitsch. For Sontag, genuine Camp cannot be merely cynical; it is a &ldquo;seriousness that fails&rdquo;&mdash;an aesthetic that views the world through theatrical quotation marks, perceiving not a lamp, but a &ldquo;lamp,&rdquo; not a woman, but a &ldquo;woman.&rdquo;</p>
<p>Furthermore, Sontag illuminated the psychological and social mechanisms that underpin Camp. Dedicated to the dandyism of Oscar Wilde, the essay located Camp&rsquo;s historical roots in metropolitan queer subcultures. For these marginalized communities, Camp functioned as a sophisticated survival strategy and a coded linguistic fraternity, allowing individuals to navigate hostile social terrain through protective irony, flamboyant parody, and self-fashioning. Yet Sontag argued that Camp also operates as a democratizing solvent of moralism. By transmuting moral outrage into stylistic amusement, Camp neutralizes moral indignation, allowing the sophisticated connoisseur to relish vulgar pop culture, melodrama, and gaudy ephemera without guilty condescension. Camp provides a tender, generous sensibility that refuses to judge the world through harsh Puritanical righteousness, celebrating human vulnerability and theatricality through the redemptive power of aesthetic delight.</p>
<p>Nevertheless, Sontag&rsquo;s essay provoked vehement backlash from subsequent cultural and queer theorists. Critics such as Moe Meyer accused Sontag of politically castrating Camp by aestheticizing and universalizing it. In Meyer&rsquo;s view, Sontag stripped Camp of its radical, queer oppositional politics, packaging a subversive anti-heteronormative critique into a palatable bourgeois plaything for the Manhattan intellectual elite. Other theorists argued that Camp&rsquo;s celebratory detachment breeds cynical political apathy: by aestheticizing all human experience into harmless theatrical spectacle, Camp risks trivializing real suffering, poverty, and structural oppression. Despite these sharp polemics, Sontag&rsquo;s analysis remains a foundational text in modern aesthetics. By daring to take the trivial seriously, Sontag revealed that the mask of artifice often illuminates deeper truths about human culture than the solemn face of unexamined sincerity.</p>""",
    "qs": [
        {
            # Q25 (Q1 of P5) - Key: A (0)
            "q": "The primary purpose of the passage is to:",
            "ch": [
                "explicate Sontag's taxonomy of Camp aesthetics, its cultural dynamics, and subsequent theoretical criticisms.",
                "demonstrate that high modernist literary criticism remains the only valid framework for evaluating visual art.",
                "prove that deliberate Camp is aesthetically superior to naive Camp because of its calculated artistic irony.",
                "condemn mid-century queer subcultures for adopting frivolous aesthetic poses instead of militant direct action."
            ],
            "a": 0,
            "e": "<strong>The passage introduces Sontag's landmark essay, defines Camp's core qualities (artifice, style over content), details the naive vs. deliberate Camp taxonomy, explores its queer subcultural roots and anti-moralistic function, evaluates critiques by Moe Meyer and others, and affirms its lasting intellectual legacy. Choice A captures this entire conceptual scope.</strong><br><br><em>Distractor Traps:</em><br>&bull; B (Directional Inversion): Paragraph 1 notes that Camp successfully challenged the puritanical solemnity of high modernism, rather than validating high modernism as the only valid standard.<br>&bull; C (Directional Inversion): Sontag regarded naive Camp (marked by earnest failure), not deliberate Camp, as the supreme and most authentic manifestation.<br>&bull; D (Directional Inversion): The passage describes Camp respectfully as a sophisticated survival strategy and coded fraternity, rather than condemning queer subcultures."
        },
        {
            # Q26 (Q2 of P5) - Key: D (3)
            "q": "According to Sontag, \"pure\" or \"naive\" Camp is distinguished from \"deliberate\" Camp primarily by:",
            "ch": [
                "a strict adherence to minimalist architectural principles that reject excessive decorative ornamentation.",
                "an aggressive political desire to dismantle corporate capitalist advertising through socialist agitprop.",
                "a total absence of passion that deliberately mocks the emotional vulnerability of tragic theater heroes.",
                "an earnest, uncalculated commitment to grandeur whose very excess results in unintentional artifice."
            ],
            "a": 3,
            "e": "<strong>Paragraph 2 states that naive Camp is 'marked by dead seriousness' and arises when an ambitious creator undertakes an extravagant project with utter sincerity, only to fail spectacularly due to excessive grandiosity, producing an 'unintentional monument to artifice.'</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Naive Camp revels in ornate excess and organic extravagances (e.g., Art Nouveau, Tiffany lamps), the polar opposite of minimalism.<br>&bull; B (Misattribution of Viewpoint): Political agitation was not the defining motive of naive Camp creators, who were passionately attempting serious art.<br>&bull; C (Directional Inversion): Naive Camp is marked by dead seriousness, intense passion, and earnest innocence, rather than an absence of passion or cynical mockery."
        },
        {
            # Q27 (Q3 of P5) - Key: B (1)
            "q": "The author asserts that Camp acts as a \"democratizing solvent of moralism\" because it:",
            "ch": [
                "forces spectators to confront the grim material consequences of urban industrial capitalist exploitation.",
                "neutralizes puritanical indignation by transforming moral judgment into generous stylistic appreciation.",
                "proves that popular mass commercial culture possesses greater literary depth than classical ancient poetry.",
                "demands that political institutions enforce absolute aesthetic equality across diverse religious communities."
            ],
            "a": 1,
            "e": "<strong>Paragraph 3 explains that 'by transmuting moral outrage into stylistic amusement, Camp neutralizes moral indignation, allowing the sophisticated connoisseur to relish vulgar pop culture, melodrama, and gaudy ephemera without guilty condescension,' thereby offering a generous refusal of puritanical righteousness.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Camp aestheticizes experience into amusement rather than forcing confrontations with grim material exploitation.<br>&bull; C (Overgeneralization/Extreme): Camp does not claim pop culture has greater literary depth than classical poetry; it allows one to enjoy ephemera stylistically.<br>&bull; D (Plausible Extrapolation Not in Passage): Camp is an informal aesthetic sensibility, not a government policy enforcing aesthetic equality."
        },
        {
            # Q28 (Q4 of P5) - Key: C (2)
            "q": "Based on paragraph 4, theorist Moe Meyer's core objection to Sontag's work is that she:",
            "ch": [
                "overestimated the artistic significance of Art Nouveau lamps and synchronized Hollywood movie musicals.",
                "failed to realize that deliberate Camp produces more authentic emotional catharsis than naive art forms.",
                "sanitized Camp by depoliticizing a radical queer survival strategy for consumption by the bourgeois elite.",
                "inadvertently strengthened the puritanical high modernism that had long suppressed avant-garde writers."
            ],
            "a": 2,
            "e": "<strong>Paragraph 4 states that Meyer accused Sontag of 'politically castrating Camp by aestheticizing and universalizing it,' stripping it of its 'radical, queer oppositional politics' to turn a subversive anti-heteronormative critique into a palatable bourgeois plaything.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (True Fact Wrong Question): Meyer's critique concerned political sanitization and erasure of queer subcultural resistance, not the decorative merit of lamps.<br>&bull; B (Misattribution of Viewpoint): Meyer did not argue in favor of deliberate Camp; his objection was political and historical.<br>&bull; D (Directional Inversion): Sontag challenged high modernism rather than strengthening it, though Meyer argued she tamed Camp's radical politics."
        },
        {
            # Q29 (Q5 of P5) - Key: A (0)
            "q": "The passage implies that viewing a cultural object through \"theatrical quotation marks\" involves:",
            "ch": [
                "perceiving the object as a stylized, self-conscious performance rather than an unmediated natural essence.",
                "quoting verbatim dialogue from classical theatrical plays to elevate mundane daily conversation into art.",
                "placing physical warning placards around artworks to prevent museum visitors from touching delicate surfaces.",
                "censoring offensive dramatic scenes in modern films to protect impressionable adolescent audience members."
            ],
            "a": 0,
            "e": "<strong>Paragraph 2 explains that viewing the world through theatrical quotation marks means perceiving 'not a lamp, but a \"lamp,\" not a woman, but a \"woman\"'—which paragraph 1 and 2 define as understanding things in terms of artifice, performance, and stylized roles rather than essential natural facts.</strong><br><br><em>Distractor Traps:</em><br>&bull; B (True Fact Wrong Question): Quotation marks are used metaphorically to denote perceptual irony and stylized staging, not literal quotation of dramatic scripts.<br>&bull; C (Plausible Extrapolation Not in Passage): Placards describe museum signage or Brechtian staging, not Sontag's conceptual quotation marks.<br>&bull; D (Directional Inversion): Camp relishes vulgarity and excess; quotation marks represent aesthetic enjoyment of artifice, not moralistic censorship."
        },
        {
            # Q30 (Q6 of P5) - Key: C (2)
            "q": "Consider a 1950s science fiction film made on a shoestring budget, featuring actors passionately reciting apocalyptic scientific monologues while attacking a monster visibly made of papier-mâché and rubber bands. How would Sontag most likely classify this film?",
            "ch": [
                "As deliberate Camp, because the director cynically manufactured an absurd product to generate box-office mockery.",
                "As an unredeemable artistic failure that lacks any legitimate aesthetic value or redeeming cultural interest.",
                "As pure naive Camp, because the filmmakers' dead earnestness clashes gloriously with the extravagant cheapness of the monster.",
                "As high modernist tragedy, because the apocalyptic scientific monologues demonstrate profound philosophical insight."
            ],
            "a": 2,
            "e": "<strong>Paragraph 2 explains that pure, naive Camp arises when an ambitious creator undertakes an extravagant project with utter seriousness and passion, only to fail due to excessive ambition, producing an unintentional monument to artifice. A sincere, low-budget sci-fi film with passionate apocalyptic monologues and a visible rubber monster is a quintessential example of pure naive Camp.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): The prompt notes the actors recite monologues 'passionately' and sincerely, which reflects naive Camp rather than cynical deliberate Camp.<br>&bull; B (Directional Inversion): Sontag's whole point is that Camp discovers aesthetic ecstasy and affection precisely where conventional taste sees only failure.<br>&bull; D (Misattribution of Viewpoint): The visible rubber monster and disproportionate grandiosity place it squarely in the realm of Camp, not solemn high modernist tragedy."
        }
    ]
}

wc, errs = validate_passage(passage_data, 6)
print(f"Validation: wc={wc}, errors={len(errs)}")
for e in errs:
    print(" ", e)
