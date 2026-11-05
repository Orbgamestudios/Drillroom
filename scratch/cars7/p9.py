import sys
from validator import validate_passage

passage_data = {
    "id": "exam_cars90_7_p9",
    "sec": "CARS",
    "topic": "The Flâneur & The Sensory Shock of the Modern Metropolis (Baudelaire)",
    "sheet": None,
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_7",
    "passage": """<div class=\"ttl\">Passage 9 (Questions 49&ndash;53)</div>
<p>In mid-nineteenth-century Paris, the radical urban renovations overseen by Baron Georges-Eug&egrave;ne Haussmann systematically demolished ancient medieval alleyways, replacing tangled working-class quarters with monumental stone boulevards, gaslit department stores, and glass-canopied commercial shopping arcades. Amid this rapid architectural metamorphosis, French poet and essayist Charles Baudelaire identified an emergent human archetype who personified the psychological condition of modernity: the <i>fl&acirc;neur</i>. In his seminal 1863 essay &ldquo;The Painter of Modern Life,&rdquo; written about graphic artist Constantin Guys, Baudelaire immortalized the fl&acirc;neur as a solitary, aristocratic stroller who wanders the bustling urban avenues with leisurely detachment. For Baudelaire, the fl&acirc;neur is a passionate spectator who takes a metaphorical &ldquo;bath of the crowd,&rdquo; plunging into the surging human ocean of the city streets while preserving strict intellectual aloofness. In a famous aesthetic formulation, Baudelaire defined modernity as &ldquo;the ephemeral, the fugitive, the contingent, the half of art whose other half is the eternal and the immutable.&rdquo; The fl&acirc;neur&rsquo;s heroic aesthetic vocation was to distill eternal beauty from the transient, fleeting spectacle of metropolitan street life.</p>
<p>The fl&acirc;neur&rsquo;s leisurely strolling represented a deliberate aesthetic resistance against the frantic, regimented temporality of early industrial capitalism. In the Parisian arcades, dandy strollers famously walked pet turtles on leashes, ostentatiously allowing the reptile&rsquo;s sluggish pace to dictate their own movements in mocking defiance of bourgeois efficiency and factory clock-time. Yet this leisurely posture was perpetually threatened by the terrifying sensory shock of the modern industrial metropolis. As sociologist Georg Simmel observed in his classic 1903 treatise &ldquo;The Metropolis and Mental Life,&rdquo; the dense, chaotic concentration of street traffic, flashing shop windows, and teeming crowds assaulted the human nervous system with an unprecedented intensification of nervous stimulation. To survive this relentless sensory bombardment, the urbanite was compelled to cultivate a &ldquo;blas&eacute; attitude&rdquo;&mdash;an emotional numbness, intellectual reservation, and protective psychological indifference that shielded the fragile individual ego from catastrophic cognitive overload.</p>
<p>Decades later, German Marxist critic Walter Benjamin repositioned Baudelaire&rsquo;s fl&acirc;neur at the ideological center of his monumental <i>Arcades Project</i>. For Benjamin, the fl&acirc;neur was far from a sovereign, disinterested aesthetic aristocrat; rather, he was an acutely alienated figure standing precariously on the historical threshold of late commodity capitalism. Benjamin observed that the fl&acirc;neur who &ldquo;goes botanizing on the asphalt&rdquo; is ultimately an accomplice to the commercial commodity spectacle. Intoxicated by the dazzling vitrines of the glass-roofed arcades, the fl&acirc;neur&rsquo;s visual connoisseurship directly mirrors the gaze of the prospective buyer. In Benjamin&rsquo;s tragic formulation, the fl&acirc;neur is an intellectual whose artisanal labor has been rendered superfluous, wandering the consumer dreamscape as a commodity seeking a purchaser.</p>
<p>Feminist cultural historians, most notably Janet Wolff, have further unmasked the socio-historical exclusivity of the fl&acirc;neur. Wolff demonstrated that the freedom to stroll anonymously through the nocturnal metropolis, observing without being accosted, was a privilege reserved strictly for affluent bourgeois men. In the rigidly gendered urban geography of the nineteenth century, an unchaperoned woman walking leisurely through urban streets was not celebrated as a poetic fl&acirc;neuse, but was immediately pathologized as a streetwalker or fallen woman. The fl&acirc;neur&rsquo;s celebratory detachment thus depended upon an invisible matrix of patriarchal dominance, economic privilege, and sexual surveillance. Despite these necessary critiques, Baudelaire&rsquo;s archetype retains hypnotic resonance. The fl&acirc;neur stands as modern civilization&rsquo;s first native citizen&mdash;a solitary consciousness suspended between the thrilling enchantment of the metropolitan crowd and the desolate abyss of urban alienation.</p>""",
    "qs": [
        {
            # Q49 (Q1 of P9) - Key: A (0)
            "q": "The primary purpose of the passage is to:",
            "ch": [
                "trace Baudelaire's concept of the flâneur, its psychological dynamics, and subsequent critical revisions.",
                "demonstrate that Haussmann's renovations successfully eliminated social alienation among Parisian laborers.",
                "prove that strolling with pet turtles was an economically viable protest that repealed industrial factory laws.",
                "argue that modern urban environments are psychologically healthier than pre-industrial agrarian villages."
            ],
            "a": 0,
            "e": "<strong>The passage introduces Baudelaire's concept of the flâneur during the Haussmannization of Paris, examines the sensory shock analyzed by Simmel (blasé attitude), explores Benjamin's Marxist reinterpretation of the flâneur as commodified spectator, details Wolff's feminist critique, and concludes with an assessment of the archetype's enduring significance. Choice A accurately captures this complete trajectory.</strong><br><br><em>Distractor Traps:</em><br>&bull; B (Directional Inversion): Haussmann demolished working-class quarters and paved the way for consumer spectacle and alienation, rather than eliminating alienation.<br>&bull; C (Overgeneralization/Extreme): Walking turtles was an eccentric symbolic gesture of aesthetic defiance by dandies, not an economically viable protest that repealed labor laws.<br>&bull; D (Directional Inversion): The passage emphasizes the terrifying sensory shock, nervous intensification, and emotional numbness produced by the metropolis."
        },
        {
            # Q50 (Q2 of P9) - Key: B (1)
            "q": "According to the passage, nineteenth-century Parisian dandies walked pet turtles in public arcades primarily to:",
            "ch": [
                "conduct empirical zoological experiments on the behavioral adaptations of captive reptiles to gas lighting.",
                "mock bourgeois standards of industrial productivity and resist the regimented pace of factory clock-time.",
                "intimidate working-class pedestrians who attempted to enter private luxury shopping arcades after hours.",
                "demonstrate that mechanical street sweepers had made urban thoroughfares safe for fragile domestic animals."
            ],
            "a": 1,
            "e": "<strong>Paragraph 2 explains that dandies walked pet turtles on leashes, 'ostentatiously allowing the reptile's sluggish pace to dictate their own movements in mocking defiance of bourgeois efficiency and factory clock-time.'</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Plausible Extrapolation Not in Passage): The practice was a flamboyant social pose and protest against industrial speed, not a zoological scientific experiment.<br>&bull; C (Plausible Extrapolation Not in Passage): The turtle was an emblem of slowness, not a guard animal used to intimidate or exclude pedestrians.<br>&bull; D (Plausible Extrapolation Not in Passage): The behavior had nothing to do with demonstrating the safety or efficacy of municipal street sweepers."
        },
        {
            # Q51 (Q3 of P9) - Key: A (0)
            "q": "Based on paragraph 2, Georg Simmel's concept of the \"blasé attitude\" is best described as:",
            "ch": [
                "a protective psychological detachment adopted by urbanites to endure overwhelming sensory stimulation.",
                "a state of hyper-aesthetic euphoria where the spectator perceives divine spiritual presence in crowd noise.",
                "an aggressive political agitation aimed at organizing labor strikes against department store owners.",
                "a medical disease caused by breathing toxic chemical fumes emitted by nineteenth-century gas lanterns."
            ],
            "a": 0,
            "e": "<strong>Paragraph 2 states that Simmel identified the 'blasé attitude' as 'an emotional numbness, intellectual reservation, and protective psychological indifference that shielded the fragile individual ego from catastrophic cognitive overload' provoked by urban sensory bombardment.</strong><br><br><em>Distractor Traps:</em><br>&bull; B (Directional Inversion): The blasé attitude is characterized by emotional numbness and indifference, the exact opposite of ecstatic religious euphoria.<br>&bull; C (Misattribution of Viewpoint): Simmel's concept is psychological and defensive, not an organized political labor strike.<br>&bull; D (Plausible Extrapolation Not in Passage): The blasé attitude is a psychological coping mechanism, not a toxicological respiratory disease."
        },
        {
            # Q52 (Q4 of P9) - Key: D (3)
            "q": "Which of the following points encapsulates Walter Benjamin's primary theoretical revision of Baudelaire's flâneur?",
            "ch": [
                "The flâneur was a heroic proletarian revolutionary who actively organized factory workers against capitalism.",
                "Baudelaire invented the flâneur as a fictional literary satire that bore no relationship to historical Paris.",
                "The flâneur successfully escaped the influence of commercial advertising by retreating into private gardens.",
                "Rather than a sovereign artist, the flâneur is an alienated figure complicit in the commodity spectacle."
            ],
            "a": 3,
            "e": "<strong>Paragraph 3 states that for Benjamin, 'the flâneur was far from a sovereign, disinterested aesthetic aristocrat; rather, he was an acutely alienated figure standing precariously on the historical threshold of late commodity capitalism' whose connoisseurship mirrors that of a buyer and whose own labor has been commodified.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Benjamin saw the flâneur as an accomplice to commodity spectacle and an intellectual whose labor was superfluous, not an active proletarian leader.<br>&bull; B (Plausible Extrapolation Not in Passage): Benjamin treated the flâneur as an essential historical archetype embodying nineteenth-century capitalism, not a fictional satire.<br>&bull; C (Directional Inversion): Benjamin argued the flâneur was intoxicated by arcade shopping vitrines, not someone who escaped to private gardens."
        },
        {
            # Q53 (Q5 of P9) - Key: C (2)
            "q": "Janet Wolff's feminist critique challenges Baudelaire's account of metropolitan strolling by demonstrating that:",
            "ch": [
                "nineteenth-century female artists composed more celebrated urban poetry than their male contemporaries.",
                "Baron Haussmann's architectural plans were designed specifically to promote equal gender integration.",
                "uninhibited urban strolling was a gendered privilege denied to women, who were pathologized if unchaperoned.",
                "wealthy bourgeois women were the primary financial investors funding the Parisian shopping arcades."
            ],
            "a": 2,
            "e": "<strong>Paragraph 4 explains that Wolff demonstrated that anonymous urban strolling 'was a privilege reserved strictly for affluent bourgeois men,' whereas an unchaperoned woman walking leisurely through city streets 'was not celebrated as a poetic flâneuse, but was immediately pathologized as a streetwalker or fallen woman.'</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Plausible Extrapolation Not in Passage): Wolff's critique emphasized the structural exclusion and marginalization of women from the public urban realm.<br>&bull; B (Directional Inversion): The urban geography was rigidly gendered and patriarchal, not designed for equal integration.<br>&bull; D (Plausible Extrapolation Not in Passage): Financial investment by women is not discussed; the focus is on the restriction of bodily movement and public presence."
        }
    ]
}

wc, errs = validate_passage(passage_data, 5)
print(f"Validation: wc={wc}, errors={len(errs)}")
for e in errs:
    print(" ", e)
