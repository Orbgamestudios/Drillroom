import sys
from validator import validate_passage

passage_data = {
    "id": "exam_cars90_7_p8",
    "sec": "CARS",
    "topic": "Iconoclasm & The Destruction of Religious Art / Byzantine Iconoclasm",
    "sheet": None,
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_7",
    "passage": """<div class=\"ttl\">Passage 8 (Questions 43&ndash;48)</div>
<p>Between the eighth and ninth centuries, the Byzantine Empire was convulsed by a theological and political crisis that threatened the very foundations of Christian art: the Iconoclastic Controversy. In 726 CE, following a devastating volcanic eruption in the Aegean Sea and catastrophic territorial losses to expanding Islamic caliphates, Emperor Leo III ordered the public removal of a monumental icon of Christ from the Chalke Gate of the imperial palace in Constantinople. Leo and his successors&mdash;most notably Constantine V&mdash;interpreted military defeats not as geopolitical failures, but as manifestations of divine wrath provoked by the widespread veneration of painted wooden panels. For more than a century, imperial decrees mandated the systematic whitewashing of church walls, the burning of sacred portraits, and the persecution of monks who defended religious imagery. This violent episode, known as Byzantine Iconoclasm (&ldquo;image-breaking&rdquo;), unmasked profound anxieties regarding the metaphysical nature of representation, the limits of the sacred, and the institutional locus of imperial authority.</p>
<p>The iconoclastic position was rooted in rigorous christological dogma and the Old Testament prohibition against idolatry. Iconoclasts contended that attempting to depict Jesus Christ in material pigments posed an insurmountable theological dilemma. Christ possessed two undivided natures: divine and human. An artist attempting to paint Christ could only depict His physical, human flesh, thereby separating His humanity from His divinity&mdash;the grave heresy of Nestorianism. Alternatively, if the artist claimed that the icon captured both natures, the artist attempted to circumscribe the infinite, uncontainable divinity within finite physical matter&mdash;the heresy of Monophysitism. Consequently, iconoclasts insisted that the only true, uncorrupted image of Christ authorized by Scripture was the Eucharistic bread and wine, which miraculously becomes His substance without depicting His sensory likeness.</p>
<p>In response, iconodule (&ldquo;image-venerating&rdquo;) theologians, led by the Syrian monk John of Damascus and Theodore the Studite, formulated an ingenious counter-theology that rescued Western and Eastern Christian art from annihilation. John of Damascus argued that the historical event of the Incarnation decisively revolutionized the status of physical matter. By willingly taking on human flesh, God sanctified material creation: &ldquo;I do not worship matter; I worship the Creator of matter who became matter for my sake.&rdquo; Furthermore, John drew a vital semiotic distinction between <i>latreia</i> (the absolute adoration due exclusively to God) and <i>proskynesis</i> (the respectful veneration offered to an image, which passes directly to the sacred prototype depicted). An icon was not an idol harboring magical divinity within wood and egg tempera; rather, it functioned as a transparent spiritual window directing the believer&rsquo;s contemplation toward the divine archetype in heaven.</p>
<p>Modern Byzantine historians, such as Peter Brown, have demonstrated that beneath these esoteric theological disputes lay a fierce socio-political struggle for institutional hegemony. Throughout the early Middle Ages, monastic communities had accumulated enormous agrarian wealth, fiscal independence, and immense popular influence, largely derived from their guardianship of miracle-working icons. By outlawing icons, the Isaurian soldier-emperors sought to dismantle the rival authority of the monasteries, consolidating ideological power and civic loyalty under the singular aegis of the imperial throne and military hierarchy. When the Empress Theodora finally restored icon veneration in 843 CE&mdash;a celebration commemorated as the &ldquo;Triumph of Orthodoxy&rdquo;&mdash;the victory permanently established the theological legitimacy of religious imagery while subordinating it to standardized ecclesiastical guidelines. Byzantine iconoclasm thus exposed a profound cultural paradox: the ferocious impulse to destroy images does not diminish their potency, but rather serves as the ultimate testament to their undeniable ideological power.</p>""",
    "qs": [
        {
            # Q43 (Q1 of P8) - Key: D (3)
            "q": "The primary purpose of the passage is to:",
            "ch": [
                "prove that Emperor Leo III was secretly a religious pagan who sought to restore Roman polytheism.",
                "demonstrate that the Nestorian heresy was historically accurate regarding the dual natures of Christ.",
                "reconcile Islamic theological prohibitions on idolatry with the artistic practices of medieval Rome.",
                "examine the theological arguments, political struggles, and cultural paradoxes of Byzantine iconoclasm."
            ],
            "a": 3,
            "e": "<strong>The passage introduces Byzantine Iconoclasm, details the christological dilemmas argued by iconoclasts, analyzes the counter-theology of John of Damascus (the Incarnation, latreia vs. proskynesis), examines the socio-political power struggle with monasteries (Brown), and highlights the cultural paradox of image destruction. Choice D encapsulates this full scope.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Plausible Extrapolation Not in Passage): Leo III was an Orthodox Christian emperor who interpreted military defeats as divine punishment for idolatry, not a pagan attempting to restore polytheism.<br>&bull; B (Misattribution of Viewpoint): The passage discusses the Nestorian heresy as a theological trap raised by iconoclasts, not as an empirically validated doctrine.<br>&bull; C (Misattribution of Viewpoint): Islamic expansion is mentioned as historical context prompting imperial anxiety, not the subject of a reconciliation with Rome."
        },
        {
            # Q44 (Q2 of P8) - Key: A (0)
            "q": "According to the passage, Byzantine iconoclasts argued that representing Christ in visual paintings was heretical because it:",
            "ch": [
                "either separated His two natures or attempted to circumscribe His uncontainable divinity in finite matter.",
                "demanded that artists use expensive imported pigments that depleted the imperial military defense treasury.",
                "required monks to abandon their monastic vows of perpetual silence to recite secular painting guild oaths.",
                "violated civic Roman legal traditions by depicting emperors in subservient poses beside biblical prophets."
            ],
            "a": 0,
            "e": "<strong>Paragraph 2 explains the theological dilemma: depicting only Christ's human flesh separated His humanity from His divinity (Nestorianism), while claiming to depict both attempted to 'circumscribe the infinite, uncontainable divinity within finite physical matter' (Monophysitism).</strong><br><br><em>Distractor Traps:</em><br>&bull; B (Plausible Extrapolation Not in Passage): The economic argument against icons in the passage relates to monastic land wealth and power, not the cost of imported pigments.<br>&bull; C (Plausible Extrapolation Not in Passage): Monks defending icons is mentioned, but vows of silence and guild oaths are entirely fabricated.<br>&bull; D (Misattribution of Viewpoint): Iconoclasts objected to depictions of Christ and divine figures on theological grounds, not imperial portraits beside biblical figures."
        },
        {
            # Q45 (Q3 of P8) - Key: C (2)
            "q": "Based on paragraph 3, John of Damascus's distinction between latreia and proskynesis served to establish that:",
            "ch": [
                "worshipping physical matter was completely acceptable provided the icon was blessed by an imperial bishop.",
                "only the Byzantine Emperor possessed the spiritual authority to receive true sacrificial worship from citizens.",
                "venerating a painted icon is not idolatry because the honor paid to the image passes to the divine archetype.",
                "wooden icons possessed independent magical consciousness capable of performing miraculous physical healings."
            ],
            "a": 2,
            "e": "<strong>Paragraph 3 states that John distinguished between <em>latreia</em> (adoration due exclusively to God) and <em>proskynesis</em> (respectful veneration offered to an image, which 'passes directly to the sacred prototype depicted'), showing the icon was not an idol harboring magic, but a window to heaven.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): John explicitly stated 'I do not worship matter'; matter itself is not worshipped, only the Creator is given latreia.<br>&bull; B (Directional Inversion): Latreia belongs exclusively to God, never to an earthly emperor.<br>&bull; D (Directional Inversion): John specifically refuted the idea that icons harbored independent magical divinity within their wood and tempera."
        },
        {
            # Q46 (Q4 of P8) - Key: B (1)
            "q": "Historian Peter Brown's interpretation suggests that the Isaurian emperors banned religious icons primarily to:",
            "ch": [
                "encourage international trade with Western European merchants who preferred illuminated codex manuscripts.",
                "dismantle the economic wealth and rival political influence concentrated in independent monastic communities.",
                "comply with democratic referendums organized by rural peasant populations who rejected urban ecclesiastical taxes.",
                "convert the entire population of the Byzantine Empire to the strict theological doctrines of early Calvinism."
            ],
            "a": 1,
            "e": "<strong>Paragraph 4 explains Peter Brown's thesis: monastic communities had accumulated enormous agrarian wealth, fiscal independence, and influence through guardianship of icons; emperors outlawed icons to 'dismantle the rival authority of the monasteries, consolidating ideological power and civic loyalty under the singular aegis of the imperial throne.'</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Plausible Extrapolation Not in Passage): The dispute was internal to Byzantine imperial power and monastic institutions, not a trade strategy for Western European illuminated manuscripts.<br>&bull; C (Plausible Extrapolation Not in Passage): The ban was an autocratic imperial decree by soldier-emperors, not a response to peasant democratic referendums.<br>&bull; D (Plausible Extrapolation Not in Passage): Calvinism arose in the sixteenth-century Protestant Reformation, eight centuries after Byzantine iconoclasm."
        },
        {
            # Q47 (Q5 of P8) - Key: D (3)
            "q": "According to paragraph 2, iconoclasts viewed the Eucharistic bread and wine as the only legitimate image of Christ because:",
            "ch": [
                "the elements were harvested from imperial royal estates managed directly by the Byzantine military hierarchy.",
                "the consecrated elements remained completely invisible to the eyes of lay worshippers during holy communion.",
                "the wine and bread were physically imported from Jerusalem rather than manufactured by local urban craftspeople.",
                "they miraculously become Christ's true substance without attempting to portray His physical sensory likeness."
            ],
            "a": 3,
            "e": "<strong>Paragraph 2 concludes by stating that iconoclasts insisted 'the only true, uncorrupted image of Christ authorized by Scripture was the Eucharistic bread and wine, which miraculously becomes His substance without depicting His sensory likeness.'</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Plausible Extrapolation Not in Passage): The legitimacy was strictly theological/metaphysical (substance without pictorial likeness), not based on imperial farm management.<br>&bull; B (Directional Inversion): The bread and wine were visible physical elements consumed during the liturgy, not invisible objects.<br>&bull; C (Plausible Extrapolation Not in Passage): The geographic provenance of wheat or wine had no bearing on the iconoclastic christological argument."
        },
        {
            # Q48 (Q6 of P8) - Key: C (2)
            "q": "The final sentence of the passage implies that the act of violently destroying images is culturally significant because it:",
            "ch": [
                "demonstrates that visual artistic representations have virtually no enduring influence over human civilization.",
                "proves that secular democratic institutions invariably triumph over conservative ecclesiastical authorities.",
                "paradoxically acknowledges and confirms the immense, formidable ideological power of the destroyed symbols.",
                "reveals that physical matter is inherently evil and incapable of conveying transcendent spiritual meaning."
            ],
            "a": 2,
            "e": "<strong>The passage concludes with the paradox: 'the ferocious impulse to destroy images does not diminish their potency, but rather serves as the ultimate testament to their undeniable ideological power.' One does not mobilize armies and imperial decrees to destroy something perceived as inert or meaningless; the violence itself confirms the symbol's supreme efficacy.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): The passage argues the exact opposite: iconoclasm confirms images possess overwhelming power, rather than proving they have no influence.<br>&bull; B (Misattribution of Viewpoint): The passage discusses medieval imperial autocracies and monastic churches, not modern secular democracies.<br>&bull; D (Misattribution of Viewpoint): Viewing matter as inherently evil was rejected by the triumphant iconodules who affirmed the Incarnation."
        }
    ]
}

wc, errs = validate_passage(passage_data, 6)
print(f"Validation: wc={wc}, errors={len(errs)}")
for e in errs:
    print(" ", e)
