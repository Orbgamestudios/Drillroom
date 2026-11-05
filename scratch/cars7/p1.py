import sys
from validator import validate_passage

passage_data = {
    "id": "exam_cars90_7_p1",
    "sec": "CARS",
    "topic": "Avant-Garde Theater: Bertolt Brecht & The Alienation Effect (Verfremdungseffekt)",
    "sheet": None,
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_7",
    "passage": """<div class=\"ttl\">Passage 1 (Questions 1&ndash;6)</div>
<p>For centuries, Western dramatic tradition was governed by the Aristotelian imperative of catharsis: the theater functioned as an emotional crucible wherein audiences achieved psychological purge through uncritical identification with tragic protagonists. In this classical framework, the dramatic stage operates as an illusory mirror of immutable human destiny, enticing spectators to surrender their critical faculties to the seductive sweep of narrative inevitability. In the tumultuous political landscape of Weimar Germany, playwright and theorist Bertolt Brecht launched a radical counter-assault against this hypnotic theatrical paradigm. Brecht argued that Aristotelian drama lulls bourgeois spectators into a tranquilizing stupor, presenting contingent socio-economic hierarchies as unalterable natural laws. To shatter this pacifying spell, Brecht pioneered what he termed &ldquo;epic theater,&rdquo; an avant-garde aesthetic designed to replace passive emotional immersion with detached, analytical interrogation through the deliberate deployment of the <i>Verfremdungseffekt</i>, or alienation effect.</p>
<p>The alienation effect operates by systematically rendering the familiar strange, denaturalizing everyday social rituals so that spectators perceive them as historically constructed rather than biologically ordained. Rather than concealing the physical apparatus of performance behind naturalistic set dressings and seamless illusionism, Brechtian staging intentionally lays bare the mechanics of production. Stage lanterns and harsh floodlights are left exposed in full view of the audience, dispelling any illusion of organic daylight; half-curtains allow spectators to witness stagehands repositioning scenery; and austere placards or projected slides announce scene synopses in advance, deliberately sabotaging dramatic suspense so that viewers focus on how events unfold rather than what happens next. Furthermore, Brecht demanded that actors abandon the psychological naturalism popularized by Konstantin Stanislavsky. Instead of completely dissolving into their roles, Brechtian performers are instructed to maintain a perceptible distance from their characters&mdash;effectively demonstrating a social behavior or &ldquo;gestus&rdquo; while subtly commenting upon it from the outside, occasionally even breaking the fourth wall to interrogate the audience directly.</p>
<p>By preventing the spectator from drowning in unreflective empathy, epic theater seeks to transform theatrical observation into an act of ideological critique. When a character makes a ruinous decision in an epic drama, the audience is not meant to sigh fatalistically at the cruelty of fate; rather, they are provoked to ask what concrete structural conditions compelled that choice, and how collective political action might alter those conditions. In <i>Mother Courage and Her Children</i>, for instance, Brecht resists sentimentalizing Courage as a noble, enduring matriarch. Her tragic inability to comprehend that war is an exploitative capitalist transaction that devours her own children is presented with clinical, unsentimental detachment, forcing the spectator to supply the critical historical judgment that the protagonist tragically lacks.</p>
<p>Yet Brecht&rsquo;s theoretical architecture has provoked vigorous contestation. Critical theorist Theodor Adorno argued that Brecht&rsquo;s overt didacticism frequently compromised aesthetic autonomy, reducing art to a didactic instrument that risks substituting authoritarian ideological instruction for genuine emancipatory consciousness. Adorno maintained that by explicitly dictating what audiences ought to conclude, epic theater inadvertently mimics the pedagogical coerciveness of the totalitarian regimes it sought to oppose. Later theater theorists have pointed out a practical paradox in Brechtian performance: spectators often experience profound emotional resonance in spite of alienation devices, suggesting that affective identification cannot be excised from theatrical reception by technical mandate alone. Nonetheless, Brecht&rsquo;s legacy remains monumental. By unmasking the ideological constructedness of dramatic reality, the alienation effect permanently disrupted theatrical complacency, proving that the stage could serve not as an opiate of cathartic solace, but as a laboratory for revolutionary social cognition.</p>""",
    "qs": [
        {
            # Q1 - Key: A (0)
            "q": "The primary purpose of the passage is to:",
            "ch": [
                "explicate the theoretical principles, staging devices, and scholarly critiques of Brechtian epic theater.",
                "demonstrate that classical Aristotelian catharsis remains the superior method for evoking moral reform.",
                "prove that psychological immersion in dramatic roles is essential to achieving socio-political consciousness.",
                "reconcile the pedagogical disputes between Adorno's aesthetic theory and Stanislavskian naturalistic acting."
            ],
            "a": 0,
            "e": "<strong>The passage introduces Brecht's critique of Aristotelian catharsis, details the mechanics of epic theater and the alienation effect (lighting, placards, gestus), illustrates this via <em>Mother Courage</em>, addresses criticisms by Adorno and performance scholars, and affirms its lasting intellectual legacy. Choice A captures this entire conceptual scope.</strong><br><br><em>Distractor Traps:</em><br>&bull; B (Directional Inversion): The passage contrasts Brecht's theater against Aristotelian catharsis, which Brecht criticized as tranquilizing rather than morally reforming.<br>&bull; C (Directional Inversion): Brecht explicitly sought to dismantle psychological immersion in favor of detached critical observation.<br>&bull; D (Misattribution of Viewpoint): The passage discusses disputes between Brecht and Adorno, not a reconciliation between Adorno and Stanislavsky."
        },
        {
            # Q2 - Key: C (2)
            "q": "According to the passage, Brechtian staging employs exposed lanterns and scene placards primarily to:",
            "ch": [
                "evoke a nostalgic historical atmosphere that mirrors the authentic production conditions of antiquity.",
                "heighten dramatic suspense by keeping the audience uncertain regarding upcoming tragic character deaths.",
                "subvert naturalistic theatrical illusion so spectators analyze socio-political causes rather than narrative plot.",
                "demonstrate the material poverty of Weimar theaters while honoring traditional Stanislavskian techniques."
            ],
            "a": 2,
            "e": "<strong>Paragraph 2 explains that exposed floodlights dispel organic illusions and placards deliberately sabotage suspense so that viewers focus on 'how events unfold rather than what happens next,' preventing passive immersion and stimulating socio-political critique.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Plausible Extrapolation Not in Passage): The exposed mechanics were designed to make the contemporary medium visible, not to simulate classical ancient performance.<br>&bull; B (Directional Inversion): Paragraph 2 explicitly states that placards 'deliberately sabotag[e] dramatic suspense' rather than heightening it.<br>&bull; D (Misattribution of Viewpoint): Exposed mechanics were deliberate aesthetic choices to counter Stanislavsky's naturalism, not responses to poverty honoring naturalism."
        },
        {
            # Q3 - Key: B (1)
            "q": "The author's description of \"gestus\" implies that a Brechtian actor differs from a Stanislavskian actor by:",
            "ch": [
                "completely internalizing the character's subconscious psyche to achieve profound emotional catharsis on stage.",
                "maintaining a critical intellectual distance from the role to exhibit and scrutinize social behavior externally.",
                "refusing to deliver scripted dialogue in order to prioritize spontaneous improvisations with the audience.",
                "surrendering all political intent so that the dramatic performance remains strictly neutral and non-judgmental."
            ],
            "a": 1,
            "e": "<strong>Paragraph 2 states that unlike Stanislavskian performers who dissolve into their roles, Brechtian actors maintain a 'perceptible distance from their characters—effectively demonstrating a social behavior or \"gestus\" while subtly commenting upon it from the outside.'</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Internalizing the subconscious psyche to achieve catharsis defines Stanislavsky's naturalism, which Brecht explicitly rejected.<br>&bull; C (Overgeneralization/Extreme): Brechtian actors broke the fourth wall and commented on their roles, but the passage never states that they refused to deliver scripted dialogue.<br>&bull; D (Directional Inversion): Brechtian acting was overtly ideological and political, never neutral or detached from social critique."
        },
        {
            # Q4 - Key: D (3)
            "q": "Based on the passage, the characterization of Mother Courage is intended to produce which response in the spectator?",
            "ch": [
                "Overwhelming pity for a grieving mother struggling against arbitrary and unavoidable cosmic tragedies.",
                "Immediate personal admiration for an unyielding businesswoman whose resilience models moral fortitude.",
                "Unconscious psychological identification that reconciles the spectator to the harsh realities of wartime survival.",
                "Critical intellectual awareness of how commercial exploitation renders individuals complicit in their own ruin."
            ],
            "a": 3,
            "e": "<strong>Paragraph 3 notes that Brecht resists sentimentalizing Courage, showing her inability to grasp that war is an exploitative capitalist transaction devouring her children, thereby 'forcing the spectator to supply the critical historical judgment that the protagonist tragically lacks.'</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Misattribution of Viewpoint): Pitying Courage as a victim of cosmic fate represents the Aristotelian response that Brecht deliberately opposed.<br>&bull; B (Directional Inversion): Brecht avoids sentimentalizing her as a noble or admirable figure; her commercial worldview is shown to be self-destructive.<br>&bull; C (Directional Inversion): Epic theater specifically combats unconscious psychological identification and fatalistic acceptance of war."
        },
        {
            # Q5 - Key: A (0)
            "q": "Which of the following scenarios in modern contemporary media most closely embodies the core critique raised by Adorno against Brechtian theater?",
            "ch": [
                "A heavy-handed political documentary that explicitly commands viewers how to vote, suppressing open inquiry.",
                "A realistic Hollywood war film that uses visceral sensory effects to immerse viewers in tragic personal grief.",
                "An experimental improvisational drama where audience members vote via smartphone to decide the play's ending.",
                "A minimalist comedy where actors repeatedly step out of character to deliver satirical jokes about modern life."
            ],
            "a": 0,
            "e": "<strong>Paragraph 4 states that Adorno criticized Brecht for an 'overt didacticism' that compromised aesthetic autonomy by 'explicitly dictating what audiences ought to conclude,' thereby mimicking pedagogical coerciveness. A political documentary that commands viewers what to conclude directly illustrates Adorno's concern regarding dogmatic pedagogical enforcement.</strong><br><br><em>Distractor Traps:</em><br>&bull; B (True Fact Wrong Question): A visceral Hollywood drama exemplifies Aristotelian emotional immersion, which Brecht opposed, rather than Adorno's critique of Brecht.<br>&bull; C (Plausible Extrapolation Not in Passage): Smartphone polling allows spectator agency, which contradicts Adorno's critique of top-down didactic coercion.<br>&bull; D (True Fact Wrong Question): Breaking character for satirical jokes exemplifies Brecht's alienation effect itself, rather than Adorno's warning against heavy-handed ideological lecturing."
        },
        {
            # Q6 - Key: C (2)
            "q": "The passage implies that the ultimate significance of Brecht's epic theater lies in its ability to:",
            "ch": [
                "eradicate all emotional resonance from live stage performance through technical staging interventions.",
                "prove that art cannot alter political structures and must therefore retreat into formal aesthetic purity.",
                "expose the malleability of human social institutions by reframing dramatic staging as an instrument of inquiry.",
                "reestablish classical Greek dramatic structures as the universal benchmark of modern avant-garde playwrighting."
            ],
            "a": 2,
            "e": "<strong>The concluding paragraph emphasizes that Brecht's monumental legacy lies in 'unmasking the ideological constructedness of dramatic reality' and transforming the stage into a 'laboratory for revolutionary social cognition,' proving social conditions can be altered.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Overgeneralization/Extreme): Paragraph 4 acknowledges that emotional resonance often persists despite technical devices, and total eradication was neither fully realized nor the ultimate theoretical value.<br>&bull; B (Directional Inversion): Brecht explicitly rejected retreating into formal aesthetic purity, insisting that theater actively engage and stimulate social change.<br>&bull; D (Directional Inversion): Brecht sought to dismantle classical Greek (Aristotelian) theatrical benchmarks rather than reestablish them."
        }
    ]
}

wc, errs = validate_passage(passage_data, 6)
print(f"Validation: wc={wc}, errors={len(errs)}")
for e in errs:
    print(" ", e)
