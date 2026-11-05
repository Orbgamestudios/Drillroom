# /home/cgslinde/DrillRoom/DrillRoom/scratch/cars5/p7.py
import json
from validator import validate_passage

passage_text = """<div class="ttl">Passage 7 (Questions 37&ndash;42)</div>
<p>In the physical and economic devastation following the Second World War, European architecture underwent a radical ideological reckoning. Confronted with the monumental task of rebuilding shattered cities, a vanguard of progressive architects rejected both the nostalgic historicism of neoclassical facades and the slick, sanitized corporate glass of the burgeoning International Style. From this post-war crucible emerged Architectural Brutalism. Marking a dramatic rupture from the pristine, smooth white stucco of his pre-war villas, Le Corbusier embraced <i>b&eacute;ton brut</i>&mdash;raw, unadorned concrete that proudly bore the rough grain, knots, and imperfections of the timber shuttering into which it was poured, as exemplified in his monumental Unit&eacute; d&rsquo;Habitation in Marseille. The movement was subsequently theorized in Britain by Alison and Peter Smithson and championed by architectural historian Reyner Banham under the aesthetic ethos of &ldquo;as found.&rdquo; Crucially, the movement&rsquo;s moniker derived not from colloquial connotations of savagery or cruelty, but from the French term for raw concrete, signaling an uncompromising dedication to material truth.</p>
<p>At its core, Brutalism was less an ephemeral aesthetic style than a fierce moral philosophy. Its practitioners subscribed to an ethic of radical structural transparency and material honesty. In contrast to bourgeois traditions that masked structural engineering behind expensive marble veneers, ornate plaster, or synthetic decorative paneling, Brutalist buildings flaunted their raw ingredients&mdash;poured concrete, rough brick, heavy steel, and unpolished glass&mdash;without cosmetic apology. The textured surfaces of board-marked concrete served as an indexical record of the manual labor performed by the carpenters who built the wooden molds. Load-bearing pillars, expansive cantilevered forms, interior ventilation ducts, and sculptural exterior stair towers were deliberately foregrounded, rendering the mechanical and structural logic of the building immediately legible to the spectator. To conceal the structural reality of a building was, in the ethical lexicon of Brutalism, an act of civic deception and bourgeois superficiality.</p>
<p>Equally vital was Brutalism&rsquo;s intrinsic entanglement with the post-war social democratic welfare state. Brutalist architects were utopian modernists dedicated to creating egalitarian public infrastructure. Rather than serving corporate finance or private aristocratic luxury, the movement was commissioned to erect municipal social housing complexes (such as London&rsquo;s Robin Hood Gardens with its wide elevated &ldquo;streets in the sky&rdquo;), public universities, secondary schools, performing arts centers, and civic libraries. Concrete was inexpensive, durable, and abundant, allowing governments to construct heroic civic spaces that offered working-class populations dignified, sunlit domesticity and communal solidarity. The massive, sculptural forms were envisioned as permanent democratic monuments, embodying collective civic resilience and a forward-looking socialist optimism.</p>
<p>Tragically, Brutalism succumbed to a fierce public and political backlash in the closing decades of the twentieth century. In temperate northern European climates, untreated concrete proved uniquely vulnerable to persistent atmospheric dampness, accumulating dark rainwater streaks, aggressive lichen, and mineral efflorescence that left once-striking facades looking grim, weathered, and neglected. Furthermore, as neo-liberal governance dismantled post-war welfare budgets and curtailed municipal spending, local councils systematically neglected routine structural maintenance, allowing communal social housing to deteriorate into crime-ridden decay. The public and media conflated the socioeconomic consequences of municipal austerity with the architecture itself, demonizing Brutalist structures as cold, totalitarian monstrosities that bred urban despair. In recent years, however, architectural historians have led a passionate reassessment. Stripping away reactionary prejudices, scholars recognize that Brutalism&rsquo;s raw monumentalism was an unyielding ethical defense of public life, standing as a heroic contrast to the disposable, speculative glass towers of contemporary hyper-capitalism.</p>"""

# Questions for Passage 7:
# Target answers: Q37: B, Q38: C, Q39: D, Q40: A, Q41: D, Q42: C
# Parity strictly within 20%!

qs = [
    {
        "q": "The primary purpose of the passage is to:",
        "ch": [
            "argue that contemporary glass-curtain skyscrapers are structurally superior to concrete housing estates.",
            "trace the ideological origins, ethical tenets, and historical trajectory of Architectural Brutalism.",
            "prove that Le Corbusier designed post-war housing complexes solely to generate private corporate profits.",
            "demonstrate that rain-induced efflorescence is the sole cause of urban criminality in European cities."
        ],
        "a": 1,
        "e": "<strong>The passage examines Architectural Brutalism's origins in post-war reconstruction and Le Corbusier's <em>béton brut</em>, outlines its ethical commitments to material honesty and social welfare infrastructure, analyzes the reasons behind its public backlash, and concludes with its contemporary reassessment.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): The author contrasts Brutalism's ethical monumentalism favorably against today's \"disposable, speculative glass towers.\"<br>&bull; C (Directional Inversion): Paragraph 3 states that Brutalist architecture served egalitarian public housing and municipal welfare, not private corporate profits.<br>&bull; D (Overgeneralization/Extreme): Rain streaks are cited as an aesthetic weathering issue, while urban decay is attributed to socioeconomic austerity, not efflorescence causing crime."
    },
    {
        "q": "According to the passage, the term \"Brutalism\" originated primarily from:",
        "ch": [
            "the severe and aggressive criminal behavior exhibited by residents inside public housing complexes.",
            "the totalitarian military regimes of Eastern Europe that commissioned monumental stone monuments.",
            "the French phrase <i>b&eacute;ton brut</i>, referring to unfinished concrete bearing the texture of its wooden formwork.",
            "the violent critiques launched by conservative British politicians against public welfare spending."
        ],
        "a": 2,
        "e": "<strong>Paragraph 1 explicitly clarifies that \"the movement's moniker derived not from colloquial connotations of savagery or cruelty, but from the French term for raw concrete [<em>béton brut</em>], signaling an uncompromising dedication to material truth.\"</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): The passage explicitly denies that the name came from cruelty or criminal behavior.<br>&bull; B (Misattribution of Viewpoint): Eastern European regimes did not invent the name; it originated from Le Corbusier and British critics like Reyner Banham.<br>&bull; D (Plausible Extrapolation Not in Passage): Conservative critiques came decades later; the term was derived directly from French architectural terminology."
    },
    {
        "q": "Based on the passage, the Brutalist commitment to \"material honesty\" required architects to:",
        "ch": [
            "disguise industrial structural materials behind imported Italian marble panels and classical moldings.",
            "rely exclusively on hand-carved decorative woodwork to celebrate medieval artisanal guild traditions.",
            "incorporate tinted reflective mirror glass so that exterior walls mirror the surrounding natural landscape.",
            "expose structural concrete, mechanical ventilation ducts, and load-bearing pillars without cosmetic veneers."
        ],
        "a": 3,
        "e": "<strong>Paragraph 2 states that Brutalism's ethic of material honesty meant that \"buildings flaunted their raw ingredients—concrete, brick, steel, and glass—without cosmetic apology. Load-bearing pillars, expansive cantilevered cantons, interior service ducts, and sculptural stair towers were deliberately foregrounded.\"</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Brutalists vehemently rejected masking engineering behind expensive marble veneers and ornamental plaster.<br>&bull; B (Misattribution of Viewpoint): Hand-carved decorative woodwork reflects the Arts and Crafts movement or historicism, not Brutalism.<br>&bull; C (Misattribution of Viewpoint): Reflective glass characterizes the corporate International Style that Brutalists opposed."
    },
    {
        "q": "It can be inferred from paragraph 3 that post-war European governments favored Brutalism for civic projects because concrete was:",
        "ch": [
            "inexpensive, structurally resilient, and well-suited for constructing egalitarian civic facilities at scale.",
            "traditionally associated with aristocratic royal palaces and classical Renaissance cathedrals.",
            "easily covered with decorative baroque plaster to placate conservative municipal building inspectors.",
            "completely immune to atmospheric moisture, weathering streaks, and long-term chemical degradation."
        ],
        "a": 0,
        "e": "<strong>Paragraph 3 notes that Brutalist architects built for the welfare state and that \"Concrete was cheap, durable, and abundant, allowing governments to construct heroic civic spaces that offered working-class populations dignified, sunlit domesticity and communal solidarity.\"</strong><br><br><em>Distractor Traps:</em><br>&bull; B (Directional Inversion): Concrete was used for egalitarian public welfare, directly contrasting with aristocratic luxury and neoclassical historicism.<br>&bull; C (Directional Inversion): Brutalists refused to cover concrete with decorative plaster, considering veneers deceptive.<br>&bull; D (Directional Inversion): Paragraph 4 explicitly points out that concrete was vulnerable to persistent dampness and rainwater streaks."
    },
    {
        "q": "Which of the following scenarios best reflects the social philosophy of Architectural Brutalism as articulated by the author?",
        "ch": [
            "A luxury resort developer builds private seaside villas with synthetic stucco resembling Greek temples.",
            "A multinational investment bank erects a commercial skyscraper clad in mirrored corporate glass walls.",
            "A private real estate firm renovates an old hospital into high-priced condominiums with antique molding.",
            "A municipal city council commissions an unadorned concrete community library and public child care center."
        ],
        "a": 3,
        "e": "<strong>Brutalism combined unadorned raw materials with democratic, egalitarian public welfare purposes (libraries, schools, social housing). An unadorned concrete municipal library and public child care center commissioned by city government perfectly captures both the material and ethical spirit of Brutalism.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Private luxury villas with synthetic historicist stucco represent the bourgeois deception and private luxury Brutalism rejected.<br>&bull; B (Directional Inversion): Corporate mirrored skyscrapers exemplify the International Style that Brutalism fought against.<br>&bull; C (Misattribution of Viewpoint): High-priced private condominiums with antique molding represent commercial gentrification and historicist veneers."
    },
    {
        "q": "The passage implies that the public demonization of Brutalist buildings in the late twentieth century was largely unfair because it:",
        "ch": [
            "ignored the fact that Brutalist architects were secretly funded by international banking conglomerates.",
            "failed to realize that the movement's primary objective was to reproduce ancient Roman imperial monuments.",
            "attributed the consequences of government disinvestment and neglected maintenance to the architectural style.",
            "assumed that untreated concrete would remain pristine and gleaming white in wet northern European climates."
        ],
        "a": 2,
        "e": "<strong>Paragraph 4 explains that as neo-liberal austerity dismantled welfare budgets, councils neglected routine maintenance, and \"The public and media conflated the socioeconomic consequences of austerity with the architecture itself, demonizing Brutalist structures as cold, totalitarian monstrosities that bred urban despair.\"</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Brutalism was funded by public welfare municipal programs, not secret international bankers.<br>&bull; B (Directional Inversion): Brutalism rejected classical imperial monumentality in favor of modern democratic civic purpose.<br>&bull; D (Misattribution of Viewpoint): The public didn't assume concrete would stay pristine; the weathering contributed to the public's negative reaction, but the unfair demonization was blaming the architecture for austerity's decay."
    }
]

passage_data = {
    "id": "exam_cars90_5_p7",
    "sec": "CARS",
    "topic": "Architectural Brutalism & The Ethics of Exposed Concrete",
    "sheet": None,
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_5",
    "passage": passage_text,
    "qs": qs
}

if __name__ == "__main__":
    errs, wc = validate_passage(passage_data, 7, 6)
    if errs:
        print("ERRORS in P7:")
        for e in errs:
            print(" -", e)
    else:
        print(f"P7 PASSED VALIDATION! Word count: {wc}")
