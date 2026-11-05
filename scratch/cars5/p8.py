# /home/cgslinde/DrillRoom/DrillRoom/scratch/cars5/p8.py
import json
from validator import validate_passage

passage_text = """<div class="ttl">Passage 8 (Questions 43&ndash;48)</div>
<p>In 1981, when an anonymous national competition jury selected the design submitted by twenty-one-year-old architectural student Maya Lin for the Vietnam Veterans Memorial in Washington, D.C., it ignited a ferocious cultural battle that fundamentally revolutionized the philosophy of public commemorative art. For centuries, Western civic memorialization had been governed by the heroic paradigm of the classical monument. From Roman triumphal arches to nineteenth-century equestrian bronzes and neoclassical obelisks, traditional monuments were emphatically vertical, allegorical, and celebratory. Their ideological function was unambiguous: to sanctify martial violence, legitimize sovereign state power, and absorb the tragic reality of individual slaughter into a consoling, triumphalist national mythology. Death in service of the nation-state was framed as noble, purposeful sacrifice, safely insulated from ethical ambiguity or political doubt.</p>
<p>In radical contrast to this tradition of monumental verticality and martial pomp, Maya Lin conceived what cultural theorists have termed a &ldquo;counter-monument.&rdquo; Sunk deep into the rolling grass of the National Mall, Lin&rsquo;s memorial consists of two polished black gabbro granite walls meeting at a 125-degree angle, cutting into the earth like an unhealed psychological incision. The walls slope downward toward a central vertex over ten feet high, then rise back toward ground level, creating a subterranean sanctuary of somber quietude. Rather than featuring figurative soldiers wielding rifles or allegorical figures of Liberty, the walls are inscribed solely with the names of over 58,000 fallen and missing service members, arranged not alphabetically or hierarchically by military rank, but chronologically by the date of casualty. By ordering the names chronologically, Lin structured the memorial as an experiential narrative of time, where the war begins at the center, recedes into history, and loops back to the beginning.</p>
<p>The phenomenological brilliance of Lin&rsquo;s design lies in its reflective materiality and somatic intimacy. The mirror-like black granite reflects the living visitor&rsquo;s face directly superimposed onto the etched names of the dead, collapsing the temporal barrier between the living observer and the deceased. Mourners do not gaze passively up at an idealized bronze hero perched on a distant pedestal; instead, they walk downward into the earth, touching the physical incisions of names with their fingertips, leaving personal mementos, and seeing their own reflections entangled with historical loss. Crucially, Lin&rsquo;s design refuses didactic prescription. It neither glorifies the geopolitical goals of the war nor explicitly condemns them, providing no patriotic homilies, nationalistic slogans, or ideological justifications for a conflict that had deeply fractured American society. By creating an open, non-prescriptive space, the memorial democratized mourning, allowing individual grief and collective historical trauma to coexist without enforced national consensus.</p>
<p>Predictably, this radical departure from traditional monumentality provoked a fierce political firestorm. Traditionalist veterans and conservative critics vehemently denounced the memorial as a &ldquo;black gash of shame,&rdquo; an &ldquo;insulting ditch,&rdquo; and a defeatist anti-war polemic. To pacify critics, a political compromise resulted in the subsequent placement of Frederick Hart&rsquo;s traditional, figurative bronze statue, <i>The Three Soldiers</i>, situated nearby. Yet this juxtaposition only accentuated the aesthetic and emotional gulf between the two modes: while Hart&rsquo;s figurative soldiers offered conventional martial representation, it was Lin&rsquo;s subterranean scar that became one of the most visited and emotionally resonant shrines in the world. Lin established a new global paradigm for memorializing collective trauma, profoundly influencing later sacred spaces such as Berlin&rsquo;s Memorial to the Murdered Jews of Europe and the National September 11 Memorial.</p>"""

# Questions for Passage 8:
# Target answers: Q43: D, Q44: A, Q45: C, Q46: B, Q47: A, Q48: C
# Parity strictly within 20%!

qs = [
    {
        "q": "The primary purpose of the passage is to:",
        "ch": [
            "argue that Frederick Hart's figurative sculpture was aesthetically superior to Maya Lin's abstract design.",
            "document the military tactics and casualty statistics that characterized the protracted Vietnam conflict.",
            "prove that nineteenth-century neoclassical equestrian monuments successfully comforted grieving families.",
            "analyze Maya Lin's revolutionary departure from traditional civic monuments in memorializing trauma."
        ],
        "a": 3,
        "e": "<strong>The passage examines Maya Lin's Vietnam Veterans Memorial as a radical \"counter-monument\" that overturned traditional celebratory civic monumentality, analyzing its chronological organization, reflective materiality, political controversies, and global influence on trauma memorialization.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): The author views Lin's design as emotionally resonant and revolutionary, whereas Hart's statue is characterized as conventional and compromise-driven.<br>&bull; B (True Fact Wrong Question): Casualty statistics are cited as part of the memorial's chronological inscription, not as an analysis of military tactics.<br>&bull; C (Misattribution of Viewpoint): Traditional monuments are described as state-legitimizing mythologies, not analyzed for whether they comforted families."
    },
    {
        "q": "According to the passage, traditional nineteenth-century civic monuments functioned primarily to:",
        "ch": [
            "sanctify martial violence and absorb individual deaths into a celebratory national mythology.",
            "encourage citizens to interrogate the ethical ambiguities and geopolitical failures of war.",
            "provide subterranean reflective spaces where mourners could grieve without government interference.",
            "subvert state authority by listing the names of fallen soldiers in strict chronological order."
        ],
        "a": 0,
        "e": "<strong>Paragraph 1 states that traditional monuments were vertical, allegorical, and celebratory, and that \"Their ideological function was unambiguous: to sanctify martial violence, legitimize sovereign state power, and absorb the tragic reality of individual slaughter into a consoling, triumphalist national mythology.\"</strong><br><br><em>Distractor Traps:</em><br>&bull; B (Directional Inversion): Traditional monuments insulated deaths from ethical ambiguity or doubt; it is Lin's monument that invites open-ended reflection.<br>&bull; C (Directional Inversion): Traditional monuments were vertical and above-ground, not subterranean spaces.<br>&bull; D (Misattribution of Viewpoint): Chronological listing without ranks was Lin's innovation, not a feature of traditional 19th-century monuments."
    },
    {
        "q": "Based on paragraph 2, Maya Lin's decision to organize the names on the wall chronologically rather than alphabetically had the effect of:",
        "ch": [
            "guaranteeing that high-ranking military generals received greater visual prominence than private soldiers.",
            "concealing the true number of casualties to prevent political demonstrations near the National Mall.",
            "structuring the memorial as an experiential temporal narrative reflecting the historical course of the war.",
            "forcing surviving family members to consult commercial military historians before locating loved ones."
        ],
        "a": 2,
        "e": "<strong>Paragraph 2 states that the names were arranged \"not alphabetically or hierarchically by military rank, but chronologically by the date of casualty. By ordering the names chronologically, Lin structured the memorial as an experiential narrative of time, where the war begins at the center, recedes into history, and loops back to the beginning.\"</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Lin explicitly rejected hierarchical organization by military rank.<br>&bull; B (Directional Inversion): The wall inscribed all 58,000+ names, refusing concealment.<br>&bull; D (Plausible Extrapolation Not in Passage): The passage does not claim family members were forced to hire commercial historians."
    },
    {
        "q": "The author suggests that the reflective quality of the polished black granite walls (paragraph 3) was significant because it:",
        "ch": [
            "prevented visitors from touching or leaving personal physical mementos beneath the engraved names.",
            "superimposed the living observer's image onto the names of the dead, creating an intimate encounter.",
            "reinforced conventional patriotic slogans by displaying illuminated governmental mottos across the stone.",
            "eliminated all emotional grief by dazzling the viewer's eyes with intense outdoor solar glare."
        ],
        "a": 1,
        "e": "<strong>Paragraph 3 explains that \"The mirror-like black granite reflects the living visitor's face directly superimposed onto the etched names of the dead, collapsing the temporal barrier between the living observer and the deceased\" into an intimate somatic encounter.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Visitors regularly touch the names and leave mementos; the reflection does not prevent this.<br>&bull; C (Directional Inversion): The memorial provides no patriotic slogans or illuminated governmental mottos.<br>&bull; D (Overgeneralization/Extreme): The reflection creates quiet, emotional communion, not sensory blinding to eliminate grief."
    },
    {
        "q": "Which of the following designs for a public memorial would most closely adhere to Maya Lin's philosophy of the \"counter-monument\"?",
        "ch": [
            "A recessed pedestrian plaza featuring sunken granite benches inscribed with historical eyewitness testimonies.",
            "A bronze statue of an armed infantry squad charging forward atop a forty-foot gilded marble victory arch.",
            "A colossal equestrian bronze of a triumphant general flanked by classical stone allegories of Glory and Fame.",
            "A military museum gift shop selling miniature replicas of fighter aircraft to raise municipal revenues."
        ],
        "a": 0,
        "e": "<strong>Lin's counter-monument philosophy emphasizes non-heroic, non-vertical, introspective, somatic, and recessed public spaces that honor collective experience without celebratory martial pomp. A recessed pedestrian plaza with sunken benches inscribed with eyewitness testimonies mirrors this design.</strong><br><br><em>Distractor Traps:</em><br>&bull; B (Directional Inversion): A 40-foot victory arch with an armed squad charging forward exemplifies traditional martial triumphalism.<br>&bull; C (Directional Inversion): A colossal equestrian bronze of a general with allegories of Glory and Fame is the classic 19th-century heroic monument Lin rejected.<br>&bull; D (Misattribution of Viewpoint): A commercial gift shop selling fighter plane toys is retail merchandising, not commemorative architecture."
    },
    {
        "q": "The author mentions the addition of Frederick Hart's figurative sculpture <i>The Three Soldiers</i> (paragraph 4) primarily to:",
        "ch": [
            "argue that Lin's memorial was architecturally incomplete and required traditional sculptures to stand upright.",
            "prove that conservative veterans successfully forced the federal government to tear down Lin's granite walls.",
            "illustrate the ideological tension between traditional heroic monuments and Lin's abstract memorialization.",
            "demonstrate that figurative bronze statuary is universally more durable than polished black gabbro granite."
        ],
        "a": 2,
        "e": "<strong>Paragraph 4 notes that Hart's statue was added as a political compromise, but \"this juxtaposition only accentuated the aesthetic and emotional gulf between the two modes: while Hart's figurative soldiers offered conventional martial representation, it was Lin's subterranean scar that became one of the most visited and emotionally resonant shrines.\"</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): The author does not regard Lin's work as incomplete or requiring physical support.<br>&bull; B (Directional Inversion): Lin's walls were never torn down; they remain the primary, celebrated shrine.<br>&bull; D (Plausible Extrapolation Not in Passage): The passage compares their aesthetic and emotional paradigms, not physical material durability."
    }
]

passage_data = {
    "id": "exam_cars90_5_p8",
    "sec": "CARS",
    "topic": "Civic Monuments & The Memorialization of Historical Trauma / Maya Lin",
    "sheet": None,
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_5",
    "passage": passage_text,
    "qs": qs
}

if __name__ == "__main__":
    errs, wc = validate_passage(passage_data, 8, 6)
    if errs:
        print("ERRORS in P8:")
        for e in errs:
            print(" -", e)
    else:
        print(f"P8 PASSED VALIDATION! Word count: {wc}")
