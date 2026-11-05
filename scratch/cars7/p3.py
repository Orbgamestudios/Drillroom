import sys
from validator import validate_passage

passage_data = {
    "id": "exam_cars90_7_p3",
    "sec": "CARS",
    "topic": "Environmental Aesthetics: The Scenic Sublime vs Ecological Value",
    "sheet": None,
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_7",
    "passage": """<div class=\"ttl\">Passage 3 (Questions 13&ndash;18)</div>
<p>For much of Western cultural history, the aesthetic evaluation of the natural world was tethered to the visual conventions of the scenic sublime and the picturesque. Popularized by eighteenth-century European philosophers such as Edmund Burke and Immanuel Kant, and immortalized by Romantic landscape painters, nature was judged almost exclusively as a static theatrical spectacle. Landscapes were deemed worthy of appreciation and preservation only if they displayed monumental grandeur&mdash;towering alpine peaks, yawning granite chasms, or thunderous waterfalls&mdash;or charming pictorial harmony that mirrored a framed oil painting. In his revolutionary 1949 conservation manifesto <i>A Sand County Almanac</i>, forester and ecologist Aldo Leopold mounted a profound philosophical challenge to this pictorial paradigm. Leopold argued that judging nature solely through the lens of scenic spectacle is not merely superficial; it actively distorts human environmental ethics by prioritizing human visual pleasure over ecological vitality.</p>
<p>To dismantle this scenic prejudice, Leopold proposed a radical reorientation of environmental valuation: the &ldquo;land ethic.&rdquo; Leopold famously declared that a thing is right when it tends to preserve the integrity, stability, and beauty of the biotic community, and wrong when it tends otherwise. Crucially, Leopold fused aesthetics with ecology, arguing that genuine natural beauty cannot be apprehended through uneducated retinal sensation alone. A pristine peat bog, a stagnant alkaline wetland, or a wind-scoured tallgrass prairie may appear drab, monotonous, or even visually repulsive to a casual tourist accustomed to dramatic postcards of the Rocky Mountains. Yet when viewed through the prism of ecological literacy, these humble habitats reveal an astonishing, intricate beauty: dynamic nutrient cycles, hyper-diverse invertebrate food webs, and millennia of evolutionary adaptation. For Leopold, perceiving the beauty of the land requires &ldquo;thinking like a mountain&rdquo;&mdash;cultivating an ecological literacy that comprehends invisible biological interdependencies.</p>
<p>Contemporary environmental philosopher Allen Carlson expanded Leopold&rsquo;s vision into what is now termed the &ldquo;cognitive&rdquo; or scientific model of environmental aesthetics. Carlson argues that just as the proper aesthetic appreciation of an artwork requires knowledge of its historical genre, artistic medium, and stylistic traditions, the proper appreciation of nature demands scientific knowledge supplied by geology, evolutionary biology, and ecology. Without scientific cognition, human admiration of the wilderness remains trivial, anthropocentric, and patronizing. Historically, this scenic bias produced disastrous conservation outcomes. Governments enthusiastically established national parks in high-altitude, rocky mountain terrains because their dramatic vistas enchanted affluent sightseers, while ecologically indispensable wetlands, grasslands, and marshes were systematically drained, plowed, or paved because they lacked dramatic scenic topography.</p>
<p>Nevertheless, the cognitive approach to environmental aesthetics has met with significant philosophical resistance. Non-cognitive aestheticians, such as Emily Brady, contend that Carlson and Leopold over-intellectualize what should remain a visceral, direct encounter with the living world. Brady maintains that aesthetic experience is fundamentally rooted in sensory perception, bodily emotion, and creative imagination; compelling an observer to consult ecological textbooks before judging a forest beautiful reduces aesthetic appreciation to a sterile academic exercise in applied biology. Furthermore, evolutionary psychologists point out that human aesthetic preferences for panoramic vistas with clear sightlines and water features are deep-seated evolutionary adaptations rooted in ancestral survival strategies, rather than arbitrary cultural prejudices that can be easily discarded through intellectual re-education. Despite these ongoing debates, Leopold&rsquo;s fundamental premise remains indispensable for contemporary conservation. By unshackling natural beauty from the narrow tyranny of the postcard vista, ecological aesthetics transforms aesthetic admiration into an urgent moral obligation to defend the planetary web of life.</p>""",
    "qs": [
        {
            # Q13 (Q1 of P3) - Key: C (2)
            "q": "The primary purpose of the passage is to:",
            "ch": [
                "argue that traditional eighteenth-century landscape paintings accurately captured the ecological complexity of wilderness.",
                "demonstrate that evolutionary psychology has definitively disproven the cognitive model of nature appreciation.",
                "examine how ecological aesthetics challenges the scenic paradigm and evaluate the philosophical debate surrounding it.",
                "advocate for the complete abolition of national park systems in mountainous regions to reallocate conservation funds."
            ],
            "a": 2,
            "e": "<strong>The passage traces the historical domination of the scenic sublime/picturesque, explains Leopold and Carlson's ecological/cognitive aesthetic alternative, details how the scenic bias damaged conservation, addresses counterarguments (Brady, evolutionary psychology), and concludes by defending the necessity of ecological aesthetics. Choice C accurately summarizes this comprehensive objective.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Paragraph 1 asserts that eighteenth-century painting reduced nature to a superficial static spectacle rather than capturing ecological complexity.<br>&bull; B (Overgeneralization/Extreme): Evolutionary psychology is cited as one philosophical/scientific challenge, not a definitive disproof that dismantles the cognitive model.<br>&bull; D (Overgeneralization/Extreme): While the passage critiques prioritizing scenic mountains over wetlands, it never advocates abolishing mountainous national parks."
        },
        {
            # Q14 (Q2 of P3) - Key: A (0)
            "q": "According to the passage, Aldo Leopold's concept of \"thinking like a mountain\" requires an observer to:",
            "ch": [
                "comprehend the complex, invisible ecological interdependencies that sustain the biotic community over time.",
                "ascend to high alpine summits to experience the overwhelming emotional terror associated with the sublime.",
                "ignore scientific explanations of wildlife behavior in order to cultivate unmediated mystical contemplation.",
                "view natural landscapes through the compositional framing techniques perfected by European oil painters."
            ],
            "a": 0,
            "e": "<strong>Paragraph 2 states that for Leopold, perceiving the beauty of the land requires 'thinking like a mountain'—which it defines as 'cultivating an ecological literacy that comprehends invisible biological interdependencies' such as nutrient cycles, food webs, and evolutionary adaptation.</strong><br><br><em>Distractor Traps:</em><br>&bull; B (True Fact Wrong Question): Experiencing terror on alpine summits refers to the traditional scenic sublime of Burke and Kant, which Leopold specifically sought to transcend.<br>&bull; C (Directional Inversion): Leopold argued that ecological literacy and scientific understanding are essential to perceive beauty, rather than ignoring them.<br>&bull; D (Directional Inversion): Leopold's approach is designed to dismantle the pictorial framing conventions derived from landscape painting."
        },
        {
            # Q15 (Q3 of P3) - Key: D (3)
            "q": "Based on paragraph 3, which of the following was a concrete historical consequence of the \"scenic bias\" in conservation?",
            "ch": [
                "Industrial logging corporations were prohibited from harvesting timber in ecologically fragile lowland floodplains.",
                "Eighteenth-century philosophers successfully lobbied European monarchs to preserve vast alkaline salt marshes.",
                "Scientists refused to conduct biological field research in high-altitude alpine regions lacking scenic waterfalls.",
                "Visually dramatic rocky mountain peaks were protected while ecologically vital but flat wetlands were destroyed."
            ],
            "a": 3,
            "e": "<strong>Paragraph 3 explicitly details that governments established national parks in rocky mountain terrains because dramatic vistas pleased tourists, while 'ecologically indispensable wetlands, grasslands, and marshes were systematically drained, plowed, or paved because they lacked dramatic scenic topography.'</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Lowland habitats were neglected and destroyed, not strictly protected from commercial exploitation.<br>&bull; B (Directional Inversion): Philosophers of that era valued dramatic or picturesque scenery, and flat marshes were routinely ignored or drained rather than preserved.<br>&bull; C (Plausible Extrapolation Not in Passage): The passage discusses political and public conservation priorities, not an academic boycott of alpine research by scientists."
        },
        {
            # Q16 (Q4 of P3) - Key: B (1)
            "q": "In Allen Carlson's cognitive model of environmental aesthetics, the appreciation of nature is directly analogous to:",
            "ch": [
                "the purely intuitive, immediate pleasure a child feels when gazing at brightly colored floral blossoms.",
                "the scholarly appreciation of art, which requires understanding an artwork's genre, medium, and history.",
                "the commercial valuation of pristine real estate based on scenic unobstructed views and recreational utility.",
                "the spiritual reverence experienced during religious worship of a transcendent and omnipotent deity."
            ],
            "a": 1,
            "e": "<strong>Paragraph 3 explains that Carlson draws an explicit analogy: 'just as the proper aesthetic appreciation of an artwork requires knowledge of its historical genre, artistic medium, and stylistic traditions, the proper appreciation of nature demands scientific knowledge supplied by geology, evolutionary biology, and ecology.'</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Carlson's cognitive model explicitly rejects uneducated, purely intuitive sensory appreciation as trivial and inadequate.<br>&bull; C (Directional Inversion): Carlson critiques commercial and anthropocentric visual enjoyment of scenery as superficial.<br>&bull; D (Plausible Extrapolation Not in Passage): Carlson's framework is grounded in secular natural sciences, not theological reverence for an omnipotent deity."
        },
        {
            # Q17 (Q5 of P3) - Key: C (2)
            "q": "Which of the following points represents Emily Brady's primary philosophical objection to Carlson's cognitive model?",
            "ch": [
                "Scientific explanations of ecological systems are fundamentally inaccurate and corrupted by corporate bias.",
                "Only professionally trained biologists possess the intellectual right to evaluate the aesthetic worth of nature.",
                "It excessively intellectualizes nature appreciation, ignoring direct sensory emotion and creative imagination.",
                "It fails to recognize that dramatic mountain vistas are more biologically productive than stagnant peat bogs."
            ],
            "a": 2,
            "e": "<strong>Paragraph 4 states that non-cognitive aestheticians like Emily Brady contend Carlson and Leopold 'over-intellectualize what should remain a visceral, direct encounter with the living world,' reducing aesthetic experience to an academic exercise while neglecting sensory perception, bodily emotion, and imagination.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Plausible Extrapolation Not in Passage): Brady does not claim science is corrupted by corporate bias, but that aesthetic experience should not depend strictly on scientific cognition.<br>&bull; B (Directional Inversion): Brady opposes the notion that one must be a trained scientist or consult ecology textbooks to legitimately experience natural beauty.<br>&bull; D (Directional Inversion): The premise that mountain vistas are more productive than peat bogs is biologically false and contradicts the passage's ecological claims."
        },
        {
            # Q18 (Q6 of P3) - Key: A (0)
            "q": "Suppose a regional government considers draining a muddy, odoriferous tidal salt marsh to construct an ornamental lake with white sand beaches. How would Leopold most likely evaluate this proposal?",
            "ch": [
                "He would strongly oppose it because destroying a functioning biotic community for visual scenery violates the land ethic.",
                "He would endorse the project because creating an aesthetically pleasing white sand beach elevates public appreciation of nature.",
                "He would remain indifferent provided that the new ornamental lake incorporates recreational boating and fishing concessions.",
                "He would support it only if the newly created ornamental lake attracts high volumes of affluent international tourists."
            ],
            "a": 0,
            "e": "<strong>Under Leopold's land ethic, 'a thing is right when it tends to preserve the integrity, stability, and beauty of the biotic community, and wrong when it tends otherwise.' Replacing a vital, intact wetland with an artificial scenic lake purely for human visual pleasure is a textbook violation of ecological integrity and the land ethic.</strong><br><br><em>Distractor Traps:</em><br>&bull; B (Directional Inversion): Leopold explicitly opposed sacrificing ecological health for superficial scenic or picturesque human pleasure.<br>&bull; C (Directional Inversion): Commercial and recreational concessions represent anthropocentric exploitation, which Leopold's land ethic directly repudiated.<br>&bull; D (Directional Inversion): Tourist revenue and scenic spectacle are the very mechanisms Leopold blamed for the historical destruction of crucial wetlands."
        }
    ]
}

wc, errs = validate_passage(passage_data, 6)
print(f"Validation: wc={wc}, errors={len(errs)}")
for e in errs:
    print(" ", e)
