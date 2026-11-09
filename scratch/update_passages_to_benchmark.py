import re, json

with open("scratch/expand_cars_passages.py", "r", encoding="utf-8") as f:
    text = f.read()

# Additions to reach 550-580 words:

# P3 (Aristotle): currently 513 words. Add ~45 words
p3_add = """<p>Crucially, Aristotle emphasized that virtue cannot be cultivated in solitary isolation. Because human beings are fundamentally civic animals (<i>politikon zoon</i>), eudaimonia requires the communal scaffolding of a just political community and the enduring bond of character-friendships (<i>philia</i>). Through shared civic life and mutual moral elevation, friends act as mirrors, enabling one another to perceive, refine, and sustain virtuous activity over the full arc of human existence.</p>"""

# P4 (Burke & Kant): currently 495 words. Add ~65 words
p4_add = """<p>Ultimately, this philosophical evolution mirrors a profound cultural transition from British empiricism to German idealism. Where Burke observed the biological shudder of the human animal confronting mortal danger, Kant celebrated the awakening of moral consciousness. The sublime, in Kant's critical system, functions as a bridge between the sensory and the intelligible, reassuring humanity that despite our material insignificance, our moral agency remains absolute.</p>"""

# P5 (Holmes): currently 499 words. Add ~60 words
p5_add = """<p>Holmes's radical skepticism regarding deductive certainty transformed American jurisprudence throughout the twentieth century. By unmasking the subjective policy preferences embedded within seemingly objective doctrines, legal realism inspired judicial skepticism of laissez-faire economic orthodoxy. Law ceased to be worshipped as a sacred relic of timeless geometry; instead, it became an active laboratory of social experimentation, evaluated by its pragmatic capacity to promote the public good.</p>"""

# P6 (Zuboff): currently 445 words. Add ~115 words
p6_add = """<p>This extractive logic extends far beyond targeted commercial advertising; it infiltrates the intimate spaces of the domestic home through connected smart devices, wearable biosensors, and ambient acoustic monitors. By embedding corporate surveillance into the physical artifacts of everyday life, technology monopolies erect an invisible architecture of behavioral modification. Human users are nudged into predictable lifestyle routines, algorithmic consuming patterns, and compliant civic postures. In Zuboff's grim diagnosis, surveillance capitalism threatens to replace the unpredictable, authentic spontaneity of human culture with a deterministic, machine-managed hive mind, wherein human unpredictability is systematically extinguished in the quest for total commercial certitude.</p>"""

# P7 (Mauss): currently 460 words. Add ~100 words
p7_add = """<p>Mauss drew crucial evidence from Bronislaw Malinowski's ethnographic documentation of the <i>Kula</i> ring among the Trobriand Islanders of the western Pacific. In this vast inter-island maritime network, men undertook perilous canoe voyages across open ocean not to acquire utilitarian commodities, but to exchange ritualized shell necklaces and armbands of no practical use. These sacred heirlooms circulated ceaselessly between trading partners, weaving an enduring fabric of international peace, mutual trust, and reciprocal alliance across hostile cultural boundaries. The Kula ring demonstrated that the circulation of objects is fundamentally the circulation of human souls, cementing social bonds that purely commercial contracts could never sustain.</p>"""

# P8 (Bourdieu): currently 468 words. Add ~90 words
p8_add = """<p>This institutional alchemy is most visibly perfected in standardized admissions testing and elite university credentials. By evaluating candidates through abstract, culturally laden metrics that reward polished rhetorical ease and elite scholastic socialization, higher education institutions effectively launder class privilege into the objective currency of academic brilliance. The credentialed elite can celebrate their professional supremacy as the rightful reward of natural intellectual merit, while the dispossessed internalize their own subordination as the just outcome of personal cognitive failure, inoculating the unequal social order against revolutionary challenge.</p>"""

# P9 (Jacobs vs Le Corbusier): currently 432 words. Add ~125 words
p9_add = """<p>This ideological clash reached its dramatic political climax in mid-century New York, where master builder Robert Moses attempted to slice expressways through historic residential neighborhoods. Mobilizing local residents to defeat the proposed Lower Manhattan Expressway, Jane Jacobs proved that urban neighborhoods are not blight to be cleared by bureaucratic bulldozer, but intricate webs of social capital that take generations to mature. When urban renewal projects tore down tenements to construct isolated high-rise public housing projects, they inadvertently created crime-ridden transit deserts devoid of spontaneous community vigilance. Jacobs's victory established a enduring urbanist principle: genuine civil security and vibrant street culture require preservation of the human-scale street grid, where casual sidewalk interactions foster spontaneous neighborly trust.</p>"""

# P5 Silk Road: currently 454 words. Add ~105 words
p5_silk_add = """<p>Furthermore, pastoral nomadic confederations were the indispensable catalysts of transcontinental technological diffusion. By establishing horse-breeding stations, mountain passes, and well-watered river corridors across the Central Asian deserts, nomadic horsemen ensured the safe passage of Sogdian merchants, Buddhist pilgrims, Nestorian Christian monks, and Islamic scholars. Great oasis cosmopolitan emporiums such as Samarkand, Bukhara, and Dunhuang flourished under nomadic patronage, functioning as dynamic intellectual melting pots where Hellenistic artistic forms, Persian administrative customs, and Chinese papermaking technology cross-pollinated to generate a truly unified Eurasian cultural ecumene.</p>"""

print("Applying additions...")

def insert_before_last_p(text, addition):
    parts = text.split("</p>")
    # insert before the last closing p
    if len(parts) >= 2:
        return "</p>".join(parts[:-2]) + "</p>\n" + addition + "\n" + parts[-2] + "</p>" + parts[-1]
    return text + "\n" + addition

# Update p3
p3_m = re.search(r'(p3_text\s*=\s*""")(.*?)(<div class="ttl">Passage 3.*?)(</p>\s*""")\n', text, re.DOTALL)
if p3_m:
    old_p3 = p3_m.group(3)
    new_p3 = insert_before_last_p(old_p3, p3_add)
    text = text.replace(old_p3, new_p3)
    print("p3 updated")

# Update p4
p4_m = re.search(r'(p4_text\s*=\s*""")(.*?)(<div class="ttl">Passage 4.*?)(</p>\s*""")\n', text, re.DOTALL)
if p4_m:
    old_p4 = p4_m.group(3)
    new_p4 = insert_before_last_p(old_p4, p4_add)
    text = text.replace(old_p4, new_p4)
    print("p4 updated")

# Update p5
p5_m = re.search(r'(p5_text\s*=\s*""")(.*?)(<div class="ttl">Passage 5.*?)(</p>\s*""")\n', text, re.DOTALL)
if p5_m:
    old_p5 = p5_m.group(3)
    new_p5 = insert_before_last_p(old_p5, p5_add)
    text = text.replace(old_p5, new_p5)
    print("p5 updated")

# Update p6
p6_m = re.search(r'(p6_text\s*=\s*""")(.*?)(<div class="ttl">Passage 6.*?)(</p>\s*""")\n', text, re.DOTALL)
if p6_m:
    old_p6 = p6_m.group(3)
    new_p6 = insert_before_last_p(old_p6, p6_add)
    text = text.replace(old_p6, new_p6)
    print("p6 updated")

# Update p7
p7_m = re.search(r'(p7_text\s*=\s*""")(.*?)(<div class="ttl">Passage 7.*?)(</p>\s*""")\n', text, re.DOTALL)
if p7_m:
    old_p7 = p7_m.group(3)
    new_p7 = insert_before_last_p(old_p7, p7_add)
    text = text.replace(old_p7, new_p7)
    print("p7 updated")

# Update p8
p8_m = re.search(r'(p8_text\s*=\s*""")(.*?)(<div class="ttl">Passage 8.*?)(</p>\s*""")\n', text, re.DOTALL)
if p8_m:
    old_p8 = p8_m.group(3)
    new_p8 = insert_before_last_p(old_p8, p8_add)
    text = text.replace(old_p8, new_p8)
    print("p8 updated")

# Update p9
p9_m = re.search(r'(p9_text\s*=\s*""")(.*?)(<div class="ttl">Passage 9.*?)(</p>\s*""")\n', text, re.DOTALL)
if p9_m:
    old_p9 = p9_m.group(3)
    new_p9 = insert_before_last_p(old_p9, p9_add)
    text = text.replace(old_p9, new_p9)
    print("p9 updated")

# Update p5_silkroad
p5s_m = re.search(r'(p5_silkroad_text\s*=\s*""")(.*?)(<div class="ttl">Passage 5.*?)(</p>\s*""")\n', text, re.DOTALL)
if p5s_m:
    old_p5s = p5s_m.group(3)
    new_p5s = insert_before_last_p(old_p5s, p5_silk_add)
    text = text.replace(old_p5s, new_p5s)
    print("p5_silkroad updated")

with open("scratch/expand_cars_passages.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Saved updated expand_cars_passages.py")
