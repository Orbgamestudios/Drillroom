import sys
from validator import validate_passage

passage_data = {
    "id": "exam_cars90_7_p4",
    "sec": "CARS",
    "topic": "Graphic Novels & The Visual Grammar of the Gutter (McCloud)",
    "sheet": None,
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_7",
    "passage": """<div class=\"ttl\">Passage 4 (Questions 19&ndash;24)</div>
<p>For much of the twentieth century, literary critics and art historians routinely dismissed comic books as a trivial, juvenile medium&mdash;an impoverished hybrid of truncated text and crude commercial melodrama. In his groundbreaking 1993 theoretical work <i>Understanding Comics: The Invisible Art</i>, cartoonist and theorist Scott McCloud dismantled this elitist prejudice by articulating a rigorous formalist poetics of sequential art. McCloud defined comics as juxtaposed pictorial and other images in deliberate sequence, intended to convey information and produce an aesthetic response in the viewer. Rather than serving as an inferior offshoot of painting or literature, comics constitute an autonomous artistic vocabulary with unique cognitive demands. At the core of McCloud&rsquo;s formal theory is a striking aesthetic paradox: the defining narrative engine of comics is located not within the drawn panels themselves, but in the empty white void that separates them&mdash;a liminal zone termed the &ldquo;gutter.&rdquo;</p>
<p>To grasp the unique cognitive nature of the gutter, McCloud contrasts comics directly with cinema. In film, the illusion of continuous motion is an involuntary optical phenomenon: through persistence of vision and the phi phenomenon, the spectator&rsquo;s retina passively stitches twenty-four discrete frames per second into a seamless illusion of kinetic realism. In comics, by contrast, time and space are fundamentally fractured. A comic strip presents a series of frozen, disconnected moments separated by blank bands of page. If panel A depicts an assailant raising a bludgeon and panel B depicts a scream echoing over a nocturnal city skyline, the physical strike itself is never drawn. Instead, the reader must bridge this perceptual abyss through what McCloud terms &ldquo;closure&rdquo;&mdash;the active, imaginative synthesis of fractured visual data into a coherent, continuous reality. In the gutter, the reader ceases to be a passive consumer and becomes an indispensable accomplice, supplying the motion, the sound, and the emotional resonance that the static drawings withhold.</p>
<p>McCloud further systematized this cognitive dynamic by classifying panel-to-panel transitions into six distinct categories, ranging from micro-temporal &ldquo;moment-to-moment&rdquo; shifts to radical &ldquo;non-sequitur&rdquo; juxtapositions. He observed that mainstream Western comics overwhelmingly privilege &ldquo;action-to-action&rdquo; transitions, driving the narrative forward through efficient, plot-centered causality. Conversely, traditional Japanese manga frequently employ &ldquo;aspect-to-aspect&rdquo; transitions, lingering on ambient environmental details&mdash;a dripping faucet, a stray cherry blossom, a distant cloud&mdash;to establish temporal suspension, contemplative mood, and spatial atmosphere. These aesthetic divergences demonstrate that the gutter is not merely a technical seam, but a sophisticated cultural grammar through which diverse societies encode temporal experience and psychological interiority.</p>
<p>Despite its undeniable influence, McCloud&rsquo;s framework has faced rigorous critique from comic semioticians and media scholars. Theorist Thierry Groensteen, in <i>The System of Comics</i>, contends that McCloud&rsquo;s linear focus on the gutter oversimplifies the visual mechanics of the medium. Groensteen argues that reading a comic is never a strictly linear, panel-to-panel progression; rather, it is a &ldquo;tabular&rdquo; experience where the eye wanders across the entire page, engaging in complex network resonances&mdash;what he terms &ldquo;arthrology&rdquo;&mdash;connecting distant panels across spatial layouts, color motifs, and page architecture. Other literary theorists point out that closure is not unique to comics, as prose readers routinely perform cognitive closure between sentences and chapter breaks. Nevertheless, McCloud&rsquo;s central theoretical breakthrough remains vital. By identifying the gutter as an active cognitive threshing floor, sequential art demonstrates that meaning in visual storytelling is produced not merely by what is shown, but by the creative agency required to illuminate what remains unseen.</p>""",
    "qs": [
        {
            # Q19 (Q1 of P4) - Key: D (3)
            "q": "The primary purpose of the passage is to:",
            "ch": [
                "prove that Japanese manga is structurally superior to Western graphic novels in pacing and characterization.",
                "demonstrate that cinema and sequential art employ identical physiological optical mechanisms to depict motion.",
                "reconcile the literary disputes between traditional prose novelists and modern graphic novel illustrators.",
                "examine McCloud's theory of the gutter and closure in comics while evaluating scholarly perspectives and critiques."
            ],
            "a": 3,
            "e": "<strong>The passage establishes McCloud's formal defense of comics, explicates the gutter and cognitive closure, compares cinematic optical illusions with comics, contrasts Western and Japanese panel transitions, reviews Groensteen's critique of linear reading, and affirms McCloud's conceptual impact. Choice D captures this comprehensive analytical trajectory.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): The passage contrasts Western and Japanese panel transitions as differing cultural aesthetic choices, not declaring one superior to the other.<br>&bull; B (Directional Inversion): Paragraph 2 explicitly contrasts comics with cinema, showing film uses passive retinal illusions while comics require active cognitive closure across fractured panels.<br>&bull; C (Misattribution of Viewpoint): The passage focuses on sequential art theory and comic semiotics, not a reconciliation between prose novelists and graphic novel artists."
        },
        {
            # Q20 (Q2 of P4) - Key: B (1)
            "q": "According to the passage, comics differ fundamentally from cinema in that sequential art:",
            "ch": [
                "relies upon rapid retinal persistence of vision to deceive the spectator into perceiving physical kinetic movement.",
                "requires the spectator to actively supply missing temporal and causal connections across fractured static panels.",
                "eliminates all narrative causality and emotional resonance in order to maintain absolute documentary realism.",
                "restricts its storytelling exclusively to linear verbal dialogue rather than visual pictorial representation."
            ],
            "a": 1,
            "e": "<strong>Paragraph 2 explains that unlike cinema (where continuous motion is an involuntary retinal phenomenon), comics present fractured time and space where 'the reader must bridge this perceptual abyss through what McCloud terms \"closure\"—the active, imaginative synthesis of fractured visual data into a coherent, continuous reality.'</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Misattribution of Viewpoint): Retinal persistence of vision is the physiological mechanism of cinema, not sequential art.<br>&bull; C (Directional Inversion): Comics do not eliminate causality or emotional resonance; the reader actively constructs them across the gutter.<br>&bull; D (Directional Inversion): Comics are fundamentally visual sequential art, not restricted exclusively to verbal text."
        },
        {
            # Q21 (Q3 of P4) - Key: C (2)
            "q": "Based on paragraph 3, traditional Japanese manga frequently utilizes \"aspect-to-aspect\" transitions in order to:",
            "ch": [
                "accelerate narrative momentum and emphasize explosive physical action during dramatic battle sequences.",
                "eliminate the need for the gutter so that panels blend together into an uninterrupted optical continuum.",
                "cultivate contemplative mood, environmental atmosphere, and temporal suspension through ambient details.",
                "mimic the efficient plot-centered causality that characterizes mainstream Western superhero narratives."
            ],
            "a": 2,
            "e": "<strong>Paragraph 3 states that traditional Japanese manga frequently employ aspect-to-aspect transitions, 'lingering on ambient environmental details—a dripping faucet, a stray cherry blossom, a distant cloud—to establish temporal suspension, contemplative mood, and spatial atmosphere.'</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Aspect-to-aspect transitions suspend temporal progression rather than accelerating plot-driven physical action.<br>&bull; B (Directional Inversion): Manga still utilizes the gutter; aspect-to-aspect transitions represent a specific way of bridging the gutter, not its elimination.<br>&bull; D (Misattribution of Viewpoint): Efficient plot-centered causality is attributed to mainstream Western comics, not the aspect-to-aspect transitions of manga."
        },
        {
            # Q22 (Q4 of P4) - Key: A (0)
            "q": "In McCloud's theoretical framework, \"closure\" is best characterized as:",
            "ch": [
                "an active cognitive process where the reader synthesizes fragmented visual depictions into a unified whole.",
                "the formal conclusion of a graphic novel where all unresolved thematic plot conflicts are neatly resolved.",
                "a printing defect where the physical boundaries between adjacent illustrative panels bleed into each other.",
                "an involuntary optical reflex governed entirely by biological persistence of vision within the human retina."
            ],
            "a": 0,
            "e": "<strong>Paragraph 2 defines closure as 'the active, imaginative synthesis of fractured visual data into a coherent, continuous reality,' transforming the reader from a passive spectator into an indispensable co-creator of narrative meaning.</strong><br><br><em>Distractor Traps:</em><br>&bull; B (True Fact Wrong Question): This defines narrative closure in traditional literary criticism, not McCloud's specific visual-cognitive concept of bridging panel gaps.<br>&bull; C (Plausible Extrapolation Not in Passage): Closure is a mental cognitive act performed by the reader, not a mechanical printing defect.<br>&bull; D (Misattribution of Viewpoint): Involuntary retinal reflexes describe cinematic perception, which McCloud explicitly contrasts with the active mental closure of comics."
        },
        {
            # Q23 (Q5 of P4) - Key: D (3)
            "q": "Which of the following statements represents Thierry Groensteen's central theoretical challenge to McCloud?",
            "ch": [
                "Comics are fundamentally an inferior offshoot of traditional painting that lacks any distinct visual grammar.",
                "Scott McCloud failed to recognize that Japanese manga relies on action-to-action transitions instead of mood.",
                "Cinematic film editing requires greater active cognitive participation from spectators than sequential print art.",
                "Focusing solely on linear panel transitions ignores holistic, non-linear page architectures and resonances."
            ],
            "a": 3,
            "e": "<strong>Paragraph 4 explains Groensteen's critique: McCloud's focus on linear adjacent gutters oversimplifies reading, which is a 'tabular' experience where the eye takes in the entire page through 'arthrology'—connecting distant panels across layouts, color motifs, and page architecture.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Groensteen is a comic semiotician who defends the artistic legitimacy and formal complexity of comics, not someone who dismisses them as inferior.<br>&bull; B (Misattribution of Viewpoint): Groensteen's critique centers on linear vs. tabular reading architecture, not contesting manga's transition types.<br>&bull; C (Directional Inversion): Groensteen does not argue that cinema demands more cognitive participation than sequential art."
        },
        {
            # Q24 (Q6 of P4) - Key: B (1)
            "q": "Suppose a graphic artist publishes a page showing a woman looking at an old photograph in panel 1, a teapot whistling on a stove in panel 2, and autumn leaves blowing past a window in panel 3. How would McCloud classify this panel sequence?",
            "ch": [
                "As an action-to-action sequence that accelerates narrative momentum toward an imminent dramatic confrontation.",
                "As an aspect-to-aspect sequence that suspends narrative action to evoke a contemplative, melancholic mood.",
                "As a moment-to-moment sequence that tracks the precise millisecond physical progression of a single motion.",
                "As a non-sequitur sequence that deliberately destroys all thematic coherence and reader comprehension."
            ],
            "a": 1,
            "e": "<strong>In paragraph 3, McCloud defines aspect-to-aspect transitions as those that linger on ambient environmental and domestic details to establish temporal suspension, contemplative mood, and atmosphere. Showing a photograph, a whistling teapot, and falling leaves without causal plot action directly exemplifies this atmospheric transition.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): There is no progressive kinetic action driving toward confrontation; the panels explore atmospheric elements of a single setting/moment.<br>&bull; C (Misattribution of Viewpoint): Moment-to-moment transitions depict tiny chronological steps of the same action (e.g., an eye blinking), not different atmospheric objects.<br>&bull; D (Overgeneralization/Extreme): The panels share a clear atmospheric, emotional, and domestic coherence, so they are not an incomprehensible non-sequitur."
        }
    ]
}

wc, errs = validate_passage(passage_data, 6)
print(f"Validation: wc={wc}, errors={len(errs)}")
for e in errs:
    print(" ", e)
