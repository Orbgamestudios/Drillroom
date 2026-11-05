import sys
from validator import validate_passage

passage_data = {
    "id": "exam_cars90_7_p6",
    "sec": "CARS",
    "topic": "Surrealism & Automatism in 20th-Century Painting",
    "sheet": None,
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_7",
    "passage": """<div class=\"ttl\">Passage 6 (Questions 31&ndash;36)</div>
<p>In the traumatic aftermath of the First World War, a vanguard cadre of Parisian writers and visual artists concluded that the catastrophic slaughter of European trench warfare was the logical culmination of Western civilization&rsquo;s obsession with bourgeois rationality, technocratic positivism, and utilitarian logic. Emerging from the anarchic disillusionment of Dada, French poet and theorist Andr&eacute; Breton sought to construct an enduring revolutionary alternative. In his historic 1924 <i>Manifesto of Surrealism</i>, Breton formulated an audacious definition that would permanently reshape modern visual art: &ldquo;Surrealism, noun, masc. Pure psychic automatism, by which one proposes to express&mdash;verbally, by means of the written word, or in any other manner&mdash;the actual functioning of thought. Dictated by thought, in the absence of any control exercised by reason, exempt from any aesthetic or moral concern.&rdquo; Heavily influenced by Sigmund Freud&rsquo;s psychoanalytic investigations into dream symbolism and the repressed unconscious, Breton envisioned automatism not as an ornamental artistic style, but as an emancipatory technology designed to liberate human desire from the repressive straightjacket of rationalist civilization.</p>
<p>When transposed into the realm of visual painting, however, the doctrine of psychic automatism fractured into two fundamentally divergent aesthetic methodologies. The first branch embraced &ldquo;pure&rdquo; or gestural automatism, championed by artists such as Andr&eacute; Masson and Joan Mir&oacute;. Masson applied glue directly to raw canvas in spontaneous, uncalculated sweeps, scattering sand across the wet adhesive and letting unconscious motor impulses dictate biomorphic contours without conscious premeditation. Similarly, Max Ernst invented mechanical techniques such as <i>frottage</i> (rubbing graphite over textured wooden floorboards) and <i>grattage</i> (scraping pigment across uneven surfaces) to bypass deliberate composition, discovering hallucinatory imagery latent within random textures. For these painters, true automatism required completely relinquishing artistic ego and allowing the physical hand to function as a direct, uninhibited seismograph of the subterranean human unconscious.</p>
<p>Conversely, a second faction developed &ldquo;veristic&rdquo; or illusionistic Surrealism, exemplified by Salvador Dal&iacute; and Ren&eacute; Magritte. Rather than relying on gestural spontaneity, Dal&iacute; perfected an obsessively detailed, hyper-academic painting technique to depict impossible, hallucinatory dreamscapes with forensic clarity. Dal&iacute; termed his approach the &ldquo;paranoiac-critical method,&rdquo; systematically cultivating active delirium to transfigure ordinary objects into fluid, metamorphic symbols&mdash;such as melting pocket watches draped across desolate shorelines. Dal&iacute; argued that irrational dream states could be rendered intelligible only through rigorous photographic naturalism, presenting the absurd with such meticulous spatial precision and optical fidelity that the spectator&rsquo;s rational defenses completely collapsed.</p>
<p>Nevertheless, Surrealism&rsquo;s claim to direct psychic transparency provoked profound theoretical skepticism. Sigmund Freud himself remained notoriously cool toward the movement; during a famous 1938 meeting with Dal&iacute;, Freud observed that while classical art conceals the conscious ego to reveal unconscious mysteries, Surrealist paintings appeared overwhelmingly calculated, exhibiting conscious intent masquerading as unconscious revelation. Psychoanalytic theorists argued that genuine psychic impulses cannot bypass the ego&rsquo;s censorship mechanisms through voluntary artistic resolve alone; the moment an artist selects a brush or arranges a canvas, aesthetic deliberation inevitably intrudes. Furthermore, political theorists such as Walter Benjamin questioned whether Breton&rsquo;s fetishization of dream logic risked lapsing into mystical escapism rather than sparking concrete anti-capitalist mobilization. Breton&rsquo;s authoritarian dogmatism&mdash;manifested in recurring purges of dissidents like Georges Bataille&mdash;further exposed the paradox of mandating institutional orthodoxy in a movement dedicated to absolute psychic liberty. Despite these internal contradictions, Surrealism permanently shattered the hegemony of rationalism, proving that beneath the polished veneer of waking consciousness lies a boundless realm of poetic wonder.</p>""",
    "qs": [
        {
            # Q31 (Q1 of P6) - Key: B (1)
            "q": "The primary purpose of the passage is to:",
            "ch": [
                "demonstrate that gestural automatism is the only valid visual expression of Freudian psychoanalytic theory.",
                "examine the philosophical origins, divergent techniques, and theoretical criticisms of Surrealist automatism.",
                "condemn Salvador Dalí for betraying the revolutionary political principles established in Breton's manifesto.",
                "prove that Sigmund Freud's clinical discoveries were largely derived from Parisian avant-garde painters."
            ],
            "a": 1,
            "e": "<strong>The passage introduces Breton's definition of psychic automatism in reaction to WWI and rationalism, traces its division into gestural and veristic/illusionistic painting, discusses Dalí's paranoiac-critical method, presents Freud's and Benjamin's critiques, and evaluates Breton's legacy. Choice B encapsulates this comprehensive analysis.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Overgeneralization/Extreme): The passage outlines two distinct branches (gestural and veristic) without declaring gestural automatism the only valid method.<br>&bull; C (Misattribution of Viewpoint): The passage evaluates Dalí's technique and Freud's meeting objectively rather than condemning Dalí's politics.<br>&bull; D (Directional Inversion): Freud influenced Breton and the Surrealists, not the reverse; Freud was skeptical of the painters' claims."
        },
        {
            # Q32 (Q2 of P6) - Key: C (2)
            "q": "According to the passage, artists practicing \"pure\" gestural automatism sought to access the unconscious primarily by:",
            "ch": [
                "mastering hyper-realistic Renaissance oil painting techniques to replicate nocturnal dreamscapes with spatial accuracy.",
                "conducting structured clinical psychoanalytic interviews with psychiatric patients before designing geometric compositions.",
                "employing spontaneous motor sweeps and randomized physical textures to bypass deliberate conscious composition.",
                "submitting draft canvas sketches to an elected committee of political theorists for ideological and moral approval."
            ],
            "a": 2,
            "e": "<strong>Paragraph 2 explains that Masson used spontaneous sweeps of glue and sand, while Ernst used frottage and grattage over random textures 'to bypass deliberate composition, discovering hallucinatory imagery latent within random textures' and letting the hand act as an uninhibited seismograph of the unconscious.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Misattribution of Viewpoint): Hyper-realistic painting techniques belong to veristic Surrealists like Dalí, not gestural automatists.<br>&bull; B (Plausible Extrapolation Not in Passage): Gestural painters relied on immediate physical reflexes and textured rubbings, not clinical interviews.<br>&bull; D (Misattribution of Viewpoint): Gestural automatism rejected deliberate control and moral/political vetting, operating without rational interference."
        },
        {
            # Q33 (Q3 of P6) - Key: A (0)
            "q": "In paragraph 3, the author suggests that Salvador Dalí deployed rigorous photographic naturalism in order to:",
            "ch": [
                "disarm the viewer's rational defenses by rendering absurd dream phenomena with meticulous visual plausibility.",
                "conform to conservative French academic painting standards so that his canvases would command high gallery prices.",
                "demonstrate that mechanical photography was incapable of capturing the metaphysical essence of human consciousness.",
                "reassure bourgeois audiences that modern avant-garde art posed no genuine threat to established socio-political norms."
            ],
            "a": 0,
            "e": "<strong>Paragraph 3 states that Dalí argued irrational dream states 'could be rendered intelligible only through rigorous photographic naturalism, presenting the absurd with such meticulous spatial precision and optical fidelity that the spectator's rational defenses completely collapsed.'</strong><br><br><em>Distractor Traps:</em><br>&bull; B (Plausible Extrapolation Not in Passage): While Dalí later became commercially successful, the passage explains his academic technique as a method to shatter rational defenses, not mere market pandering.<br>&bull; C (Misattribution of Viewpoint): Dalí used photographic painting to render the unconscious credible, not to critique mechanical photography.<br>&bull; D (Directional Inversion): Dalí sought to collapse rational defenses and disrupt conventional perceptions of reality, not reassure bourgeois conservatism."
        },
        {
            # Q34 (Q4 of P6) - Key: D (3)
            "q": "Which of the following statements most accurately reflects Sigmund Freud's reported reaction to Surrealist painting?",
            "ch": [
                "He celebrated it as an infallible diagnostic instrument that rendered clinical psychoanalysis entirely obsolete.",
                "He condemned the movement for failing to adopt the political tenets of historical materialism and Marxism.",
                "He praised gestural automatism while declaring veristic dream paintings to be devoid of psychological interest.",
                "He suspected that the paintings reflected conscious, calculated deliberation rather than genuine unconscious revelation."
            ],
            "a": 3,
            "e": "<strong>Paragraph 4 states that Freud remained cool toward the movement, noting to Dalí that 'Surrealist paintings appeared overwhelmingly calculated, exhibiting conscious intent masquerading as unconscious revelation' because artistic selection inevitably involves conscious ego filtering.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Freud was skeptical and critical of Surrealism, never claiming it replaced clinical analysis.<br>&bull; B (Misattribution of Viewpoint): Critiques regarding historical materialism were raised by political theorists like Walter Benjamin, not Freud.<br>&bull; C (Plausible Extrapolation Not in Passage): Freud made a general observation about calculated conscious intent in Surrealist art, not an endorsement of gestural over veristic painting."
        },
        {
            # Q35 (Q5 of P6) - Key: B (1)
            "q": "Based on paragraph 4, Walter Benjamin's political critique of Surrealism suggested that the movement:",
            "ch": [
                "overemphasized rigorous economic analysis at the expense of liberating individual artistic spontaneity.",
                "risked lapsing into mystical escapism instead of galvanizing practical mobilization against capitalist injustice.",
                "lacked sufficient technical academic polish to convince working-class citizens of its revolutionary legitimacy.",
                "was excessively obedient to bourgeois legal institutions because of Breton's strict moral requirements."
            ],
            "a": 1,
            "e": "<strong>Paragraph 4 states that 'political theorists such as Walter Benjamin questioned whether Breton's fetishization of dream logic risked lapsing into mystical escapism rather than sparking concrete anti-capitalist mobilization.'</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Benjamin argued Surrealism focused too much on dream mystique and too little on concrete political-economic mobilization.<br>&bull; C (Plausible Extrapolation Not in Passage): Benjamin's critique focused on ideological escapism vs. political action, not academic craftsmanship.<br>&bull; D (Directional Inversion): Breton explicitly declared Surrealism exempt from moral concern; the critique was escapism, not bourgeois legal obedience."
        },
        {
            # Q36 (Q6 of P6) - Key: D (3)
            "q": "The author identifies a fundamental irony in the history of the Surrealist movement, namely that:",
            "ch": [
                "Dadaists embraced rationalist commercial advertising despite their declared philosophical nihilism.",
                "Freud derived his entire theory of the unconscious mind from examining Masson's sand compositions.",
                "its most famous painters completely abandoned visual art in favor of writing dogmatic manifestos.",
                "a movement dedicated to total psychic liberty was governed by rigid authoritarian dogmatism and purges."
            ],
            "a": 3,
            "e": "<strong>Paragraph 4 concludes by highlighting 'the paradox of mandating institutional orthodoxy in a movement dedicated to absolute psychic liberty,' citing Breton's recurring dogmatic purges of dissidents like Georges Bataille.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (True Fact Wrong Question): This relates to Dada, not the specific central irony of Surrealism described in paragraph 4.<br>&bull; B (Directional Inversion): Freud was skeptical of Masson and the Surrealists; he did not base his psychoanalysis on their paintings.<br>&bull; C (Directional Inversion): Surrealist artists continued painting profusely; they did not abandon visual art for manifestos."
        }
    ]
}

wc, errs = validate_passage(passage_data, 6)
print(f"Validation: wc={wc}, errors={len(errs)}")
for e in errs:
    print(" ", e)
