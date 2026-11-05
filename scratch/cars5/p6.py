# /home/cgslinde/DrillRoom/DrillRoom/scratch/cars5/p6.py
import json
from validator import validate_passage

passage_text = """<div class="ttl">Passage 6 (Questions 31&ndash;36)</div>
<p>In 1916, amidst the mechanized slaughter of the First World War, an international cadre of exiled poets, painters, and performers gathered at the Cabaret Voltaire in Zurich to launch Dada&mdash;an explosive, nihilistic counter-cultural revolt. Convinced that the catastrophic carnage of the trenches was the direct, monstrous culmination of Western rationalism, Enlightenment positivism, and bourgeois morality, the Dadaists declared war on European civilization itself. Traditional bourgeois art, with its celebration of aesthetic beauty, formal harmony, and humanistic virtue, was denounced as an ideological smoke screen that cosmetically masked the brutal barbarism of imperialist war. If rational civilization had produced industrial butchery, Dadaists reasoned, then logic, order, and traditional aesthetic decorum were fundamentally complicit. In response, Dada unleashed a chaotic assault of phonetic sound poems, chance collages, and abrasive cabaret provocations designed not to create a new aesthetic style, but to abolish the sacred institutional category of art altogether.</p>
<p>The most philosophically profound manifestation of this anti-art insurgency was orchestrated by the French-American iconoclast Marcel Duchamp. By the mid-1910s, Duchamp had grown contemptuous of what he derisively termed &ldquo;retinal art&rdquo;&mdash;painting and sculpture designed merely to stimulate the physical eye through exquisite brushwork, color harmony, or decorative craft. For Duchamp, retinal art, whether academic salon painting or modern Impressionism, reduced the artist to an unthinking manual laborer and the spectator to a passive consumer of sensory pleasure. Duchamp sought to emancipate art from this optical servitude, declaring that art should once again be put at the service of the intellect, operating as a conceptual interrogation rather than a physical commodity.</p>
<p>This radical conviction culminated in Duchamp&rsquo;s invention of the &ldquo;readymade,&rdquo; epitomized by his submission of <i>Fountain</i> to the 1917 exhibition of the Society of Independent Artists in New York. Duchamp purchased an ordinary commercial porcelain urinal from a plumbing supply manufacturer, rotated it ninety degrees onto its back, titled it <i>Fountain</i>, and signed it with the fictitious pseudonym &ldquo;R. Mutt 1917.&rdquo; Although the Society had pledged to exhibit any submitted work upon payment of an entry fee, the board suppressed <i>Fountain</i>, deeming it obscene and an insult to fine art. Defending the work in the avant-garde journal <i>The Blind Man</i>, Duchamp clarified his conceptual thesis: &ldquo;Whether Mr. Mutt with his own hands made the fountain or not has no importance. He CHOSE it. He took an ordinary article of life, placed it so that its useful significance disappeared under the new title and point of view&mdash;created a new thought for that object.&rdquo; By severing artistic legitimacy from artisanal skill and manual fabrication, Duchamp demonstrated that an artwork is essentially an act of intellectual nomination, defined by its institutional framing.</p>
<p>Yet the subsequent history of Dadaism and the readymade is defined by a profound, tragic irony. Conceived as an aggressive anti-art gesture meant to dynamite bourgeois aesthetic institutions, the readymade was eventually absorbed, tamed, and sacralized by the very museum apparatus it sought to subvert. By the late twentieth century, replicas of Duchamp&rsquo;s urinal were reverently displayed on pedestal vitrines in prestigious institutions like the Tate Modern and the Museum of Modern Art, insured for tens of millions of dollars and analyzed with pious scholarly solemnity. This institutional co-optation underscores the boundless capacity of the capitalist art market to neutralize radical rebellion, converting the absolute negation of art into its most lucrative and canonized commodity.</p>"""

# Questions for Passage 6:
# Target answers: Q31: C, Q32: B, Q33: A, Q34: D, Q35: C, Q36: D
# Parity strictly within 20%!

qs = [
    {
        "q": "The primary purpose of the passage is to:",
        "ch": [
            "prove that European academic salon painting was technically superior to American Dadaist collages.",
            "trace how World War I military trench tactics inspired the engineering of commercial porcelain urinals.",
            "examine Dada's anti-art revolt and Marcel Duchamp's conceptual disruption through the readymade.",
            "argue that contemporary museums should deaccession and destroy all conceptual twentieth-century art."
        ],
        "a": 2,
        "e": "<strong>The passage traces the emergence of Dadaism as an anti-art revolt against World War I rationalism, analyzes Marcel Duchamp's critique of \"retinal art\" and creation of the readymade (especially <em>Fountain</em>), and explores the institutional paradox of its eventual commodification.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): The passage describes Dadaists and Duchamp repudiating academic salon painting, not asserting its superiority.<br>&bull; B (Plausible Extrapolation Not in Passage): The passage connects WWI to the philosophical revolt of Dada, not to the literal industrial engineering of plumbing fixtures.<br>&bull; D (Overgeneralization/Extreme): The author notes the historical irony of institutional co-optation, but does not advocate the destruction of conceptual art."
    },
    {
        "q": "According to the passage, the Zurich Dadaists rejected traditional European aesthetic conventions primarily because they:",
        "ch": [
            "believed that commercial advertising offered a superior method for educating working-class laborers.",
            "viewed Western rationalism and bourgeois culture as morally bankrupt after the catastrophe of World War I.",
            "wished to restore medieval religious painting as the sole legitimate form of human creative expression.",
            "sought to increase the retail auction value of their personal oil paintings in international markets."
        ],
        "a": 1,
        "e": "<strong>Paragraph 1 explains that Dadaists were convinced that the mechanized carnage of WWI was the \"direct, monstrous culmination of Western rationalism, Enlightenment positivism, and bourgeois morality,\" concluding that reason, order, and traditional aesthetic decorum were fundamentally complicit.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Misattribution of Viewpoint): Commercial advertising was not the inspiration for Dada's nihilistic revolt against rationalism.<br>&bull; C (Directional Inversion): Dadaists sought to dismantle traditional categories of art, not restore medieval religious painting.<br>&bull; D (Directional Inversion): Dadaists launched an anti-art revolt aimed at abolishing art, not maximizing personal auction values."
    },
    {
        "q": "Marcel Duchamp's critique of \"retinal art\" (paragraph 2) centered on his belief that such art:",
        "ch": [
            "appealed merely to optical sensory pleasure while failing to engage the intellectual faculty.",
            "demanded excessive mathematical training that alienated ordinary museum visitors and patrons.",
            "neglected the physical craft of oil painting in favor of mechanical industrial manufacturing.",
            "depended too heavily on political slogans to advance socialist and communist government agendas."
        ],
        "a": 0,
        "e": "<strong>Paragraph 2 explains that Duchamp derided \"retinal art\" because it was \"designed merely to stimulate the physical eye through exquisite brushwork, color harmony, or decorative craft,\" reducing the spectator to a passive consumer of sensory pleasure rather than engaging the intellect.</strong><br><br><em>Distractor Traps:</em><br>&bull; B (Plausible Extrapolation Not in Passage): Duchamp criticized retinal art for being mindlessly physical, not for being excessively mathematical.<br>&bull; C (Directional Inversion): Retinal art prioritized physical manual craft and exquisite brushwork, which is what Duchamp rejected in favor of readymades.<br>&bull; D (Misattribution of Viewpoint): Retinal art was criticized for sensory superficiality, not for promoting communist slogans."
    },
    {
        "q": "Based on Duchamp's defense of <i>Fountain</i> in <i>The Blind Man</i>, an object qualifies as an artwork primarily through:",
        "ch": [
            "the laborious manual dexterity and anatomical precision demonstrated by the sculptor during fabrication.",
            "the intrinsic monetary value and geological rarity of the raw physical materials utilized in its creation.",
            "the consensus of a government-appointed regulatory committee approving its public moral decency.",
            "the artist's conceptual choice and recontextualization that endows an object with a new thought."
        ],
        "a": 3,
        "e": "<strong>Paragraph 3 quotes Duchamp's defense: \"Whether Mr. Mutt with his own hands made the fountain or not has no importance. He CHOSE it. He took an ordinary article of life, placed it so that its useful significance disappeared under the new title and point of view—created a new thought for that object.\" Art is thus an act of conceptual nomination.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Duchamp explicitly severed artistic legitimacy from manual dexterity and fabrication.<br>&bull; B (Plausible Extrapolation Not in Passage): Duchamp used an ordinary, mass-produced porcelain urinal, not rare geological materials.<br>&bull; C (Directional Inversion): The Society's board suppressed the work on moral grounds; Duchamp rejected moralistic committee approvals."
    },
    {
        "q": "Which of the following actions represents the closest contemporary equivalent to Duchamp's presentation of the \"readymade\"?",
        "ch": [
            "A painter spends five years painstakingly applying thousands of microscopic oil glazes to a historic portrait.",
            "A musician composes a complex four-part fugue using traditional seventeenth-century counterpoint harmony.",
            "An artist places an unedited commercial cardboard shipping box inside a gallery and titles it <i>The Container</i>.",
            "A graphic designer creates a corporate trademark logo for an international industrial manufacturing conglomerate."
        ],
        "a": 2,
        "e": "<strong>Duchamp's readymade involves taking a standard mass-produced utilitarian object, stripping its function, giving it a title/concept, and exhibiting it in an art space. Placing an unedited commercial shipping box in a gallery with a title perfectly mirrors the readymade.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Painstaking manual oil glazing represents the artisanal \"retinal art\" craft that Duchamp repudiated.<br>&bull; B (Directional Inversion): Traditional contrapuntal composition relies on classic formal craft rather than conceptual readymade nomination.<br>&bull; D (Misattribution of Viewpoint): Designing a commercial trademark is applied graphic design for industry, not an anti-art provocation in a gallery."
    },
    {
        "q": "The final paragraph discusses the display of Duchamp's urinals in modern museums primarily to illustrate:",
        "ch": [
            "the complete aesthetic failure of conceptual artworks to survive past their initial exhibition year.",
            "the technical superiority of twentieth-century plumbing manufacturing over ancient Greek pottery.",
            "the triumph of working-class laborers over bourgeois academic museum curators and wealthy collectors.",
            "the paradox whereby a radical anti-art provocation is co-opted and commodified by the establishment."
        ],
        "a": 3,
        "e": "<strong>Paragraph 4 highlights the \"profound, tragic irony\" that an aggressive anti-art gesture intended to dismantle bourgeois institutions was absorbed, canonized, and insured for millions, underscoring \"the boundless capacity of the capitalist art market to neutralize radical rebellion, converting the absolute negation of art into its most lucrative and canonized commodity.\"</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): The urinals survived and were canonized into celebrated museum centerpieces, not forgotten.<br>&bull; B (Plausible Extrapolation Not in Passage): The passage makes no comparison between modern plumbing and ancient Greek pottery.<br>&bull; C (Directional Inversion): The establishment art market co-opted the rebellion; it was not a triumph of working-class laborers over collectors."
    }
]

passage_data = {
    "id": "exam_cars90_5_p6",
    "sec": "CARS",
    "topic": "Dadaism & The Anti-Art Provocation of Marcel Duchamp",
    "sheet": None,
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_5",
    "passage": passage_text,
    "qs": qs
}

if __name__ == "__main__":
    errs, wc = validate_passage(passage_data, 6, 6)
    if errs:
        print("ERRORS in P6:")
        for e in errs:
            print(" -", e)
    else:
        print(f"P6 PASSED VALIDATION! Word count: {wc}")
