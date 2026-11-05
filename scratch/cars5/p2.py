# /home/cgslinde/DrillRoom/DrillRoom/scratch/cars5/p2.py
import json
from validator import validate_passage

passage_text = """<div class="ttl">Passage 2 (Questions 7&ndash;12)</div>
<p>In the mid-1950s, a cadre of iconoclastic critics writing for the Parisian film journal <i>Cahiers du Cin&eacute;ma</i> launched an intellectual insurgency that permanently altered the aesthetic evaluation of motion pictures. Spearheaded by Fran&ccedil;ois Truffaut, whose seminal 1954 manifesto &ldquo;A Certain Tendency of the French Cinema&rdquo; fiercely attacked the prevailing &ldquo;tradition of quality,&rdquo; these critics indicted mainstream European cinema as an ossified, bourgeois enterprise. Drawing theoretical inspiration from Alexandre Astruc&rsquo;s notion of the <i>cam&eacute;ra-stylo</i>&mdash;the concept that the camera should function as flexibly and personally as a writer&rsquo;s pen&mdash;they argued that post-war studios had reduced filmmaking to a sterile, academic exercise. In these industrial productions, self-effacing technicians merely illustrated prestigious literary screenplays with slick, predictable psychological realism. In response, Truffaut and his cohort&mdash;including Jean-Luc Godard, &Eacute;ric Rohmer, and Claude Chabrol&mdash;formulated <i>la politique des auteurs</i> (the auteur policy). They asserted that cinema was not a subsidiary branch of literature or theater, but an autonomous fine art whose true creator was the director, whose distinct personality and visual signature should govern every frame.</p>
<p>The philosophical core of auteurism was the primacy of <i>mise-en-sc&egrave;ne</i>&mdash;the expressive staging of visual elements, encompassing camera placement, lighting, blocking, temporal rhythm, and spatial composition. For the <i>Cahiers</i> theorists, a filmmaker&rsquo;s artistic identity was revealed not in the ostensible literary prestige of the plot, but in how formal visual choices transformed dramatic material. This conceptual leap allowed critics to champion American studio directors who had previously been dismissed as commercial hirelings. Figures such as Alfred Hitchcock, Howard Hawks, and Nicholas Ray were re-evaluated as visionary artists because, despite working under rigid Hollywood studio contracts and standard genre formulas, they consistently imprinted an unmistakable philosophical worldview and stylistic grammar across their filmographies. As Truffaut famously contended, there were no good or bad themes, only good or bad directors.</p>
<p>When these theorists transitioned from film criticism to directing in the late 1950s, inaugurating the French New Wave (<i>La Nouvelle Vague</i>), their diverging aesthetic strategies exposed fundamental tensions within auteurist modernism. Truffaut, in works such as <i>The 400 Blows</i> (1959), cultivated a lyrical, humanistic realism. Utilizing lightweight portable equipment, Parisian street locations, and poignant autobiographical themes, he achieved an intimate, emotionally resonant cinema that refreshed classical narrative forms, culminating in the famous ambiguous freeze-frame of young Antoine Doinel staring at the sea. In contrast, Jean-Luc Godard launched a radical deconstructive assault on conventional film grammar. In <i>Breathless</i> (1960) and <i>Contempt</i> (1963), Godard weaponized abrasive jump cuts, disjointed elliptical editing, asynchronous audio, and direct addresses to the audience. By shattering Hollywood&rsquo;s cherished illusion of spatio-temporal continuity, Godard deliberately dismantled the spectator&rsquo;s passive immersion, forcing the viewer to confront the cinematic medium as an ideological and formal construction.</p>
<p>Notwithstanding its triumph in establishing film as a legitimate subject of scholarly aesthetics, auteur theory provoked fierce critical opposition. American critic Pauline Kael vehemently contested the doctrine, arguing that it promulgated a romantic mythology of solitary genius that ignored the intrinsically collaborative, industrial nature of filmmaking. In Kael&rsquo;s assessment, elevating the director as sole author blinded critics to the vital contributions of screenwriters, cinematographers, actors, and editors, while arbitrarily excusing mediocre films by favored directors as expressions of personal style. Subsequent structuralist theorists similarly argued that auteurism fetishized individual subjectivity at the expense of analyzing the economic structures and semiotic codes that govern visual culture. Nonetheless, by relocating cinematic meaning from scripted dialogue to visual syntax, the New Wave permanently emancipated cinema from literary subservience.</p>"""

# Questions for Passage 2:
# Target answers: Q7: B, Q8: D, Q9: A, Q10: C, Q11: D, Q12: B
# Parity strictly within 20%!

qs = [
    {
        "q": "The primary objective of the passage is to:",
        "ch": [
            "demonstrate that Truffaut's cinematic technique was intellectually superior to Godard's formal experiments.",
            "trace the emergence of auteur theory, its artistic manifestations, and the theoretical critiques it encountered.",
            "prove that Hollywood studio directors were completely free from corporate constraints and commercial formulas.",
            "explain why contemporary film scholars have entirely abandoned visual mise-en-sc&egrave;ne in favor of script analysis."
        ],
        "a": 1,
        "e": "<strong>The passage traces the origins of auteur theory in <em>Cahiers du Cinéma</em>, explains the concept of <em>mise-en-scène</em>, explores the contrasting New Wave practices of Truffaut and Godard, and examines the counterarguments raised by critics like Pauline Kael and structuralists before reaffirming its legacy.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Misattribution of Viewpoint): The author presents Truffaut and Godard as exhibiting different, contrasting approaches to auteurism without declaring one inherently superior to the other.<br>&bull; C (Directional Inversion): Paragraph 2 states that Hitchcock and others created visionary work \"despite working under rigid Hollywood studio contracts and standard genre formulas,\" not that they were completely free.<br>&bull; D (Overgeneralization/Extreme): The passage concludes that the New Wave permanently emancipated cinema from literary subservience, rather than stating scholars abandoned visual analysis."
    },
    {
        "q": "According to the passage, the <i>Cahiers du Cin&eacute;ma</i> critics condemned post-war French cinema primarily because it:",
        "ch": [
            "depended excessively on improvised street acting rather than trained theatrical performers.",
            "relied on disorienting jump cuts that confused audiences and alienated commercial investors.",
            "refused to adapt classic literary masterpieces due to an obsession with cheap popular genres.",
            "treated filmmaking as a mechanical transcription of literary scripts rather than a visual art."
        ],
        "a": 3,
        "e": "<strong>Paragraph 1 explains that the critics attacked the \"tradition of quality\" because studios \"had reduced filmmaking to a sterile, academic exercise in which self-effacing technicians merely illustrated prestigious literary screenplays,\" failing to treat cinema as an autonomous visual art.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Lightweight equipment and location shooting were introduced by the New Wave itself, not the traditional cinema they attacked.<br>&bull; B (Directional Inversion): Jump cuts were Godard's radical innovation, not a feature of the traditional French cinema under attack.<br>&bull; C (Directional Inversion): The traditional cinema was obsessed with prestigious literary adaptations; the critics criticized them for this literary subservience."
    },
    {
        "q": "Based on the discussion of <i>mise-en-sc&egrave;ne</i> in paragraph 2, an auteurist critic evaluating a new film would be most interested in:",
        "ch": [
            "the visual coherence achieved through lighting, camera movement, and framing across the director's body of work.",
            "the historical accuracy and literary fidelity of the screenwriter's adaptation of a classic theatrical play.",
            "the box office revenue generated by the film during its opening commercial weekend in mainstream theaters.",
            "the degree to which the lead actors memorized dialogue without deviating from the printed script instructions."
        ],
        "a": 0,
        "e": "<strong>Paragraph 2 defines <em>mise-en-scène</em> as the \"expressive staging of visual elements, encompassing camera placement, lighting, blocking, temporal rhythm, and spatial composition\" through which a filmmaker imprints a consistent philosophical worldview and stylistic signature across their filmography.</strong><br><br><em>Distractor Traps:</em><br>&bull; B (Directional Inversion): Auteurism explicitly shifted value away from the literary prestige of the script to visual choices.<br>&bull; C (Plausible Extrapolation Not in Passage): Commercial box office performance is an industrial metric, not an auteurist aesthetic criterion.<br>&bull; D (Misattribution of Viewpoint): Focusing on strict actor obedience to a printed script prioritizes literary theater over the director's visual authorship."
    },
    {
        "q": "The passage suggests that the fundamental difference between Truffaut's and Godard's New Wave films lies in Godard's:",
        "ch": [
            "unwavering dedication to polished Hollywood lighting techniques and traditional continuity editing.",
            "complete rejection of contemporary political topics in favor of sentimental historical costume dramas.",
            "deliberate disruption of narrative continuity to make audiences conscious of cinema as a constructed medium.",
            "preference for high-budget studio sets over authentic location shooting in the residential streets of Paris."
        ],
        "a": 2,
        "e": "<strong>Paragraph 3 contrasts Truffaut's lyrical, emotionally resonant realism with Godard's radical assault on continuity: \"By shattering Hollywood's cherished illusion of spatio-temporal continuity, Godard deliberately dismantled the spectator's passive immersion, forcing the viewer to confront the cinematic medium as an ideological and formal construction.\"</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Godard explicitly attacked traditional Hollywood continuity editing by using abrasive jump cuts and asynchronous sound.<br>&bull; B (Directional Inversion): Godard dismantled Hollywood illusions rather than retreating to sentimental costume dramas.<br>&bull; D (Directional Inversion): Both filmmakers utilized lightweight equipment outside traditional studios; Godard did not prefer high-budget studio sets."
    },
    {
        "q": "Which of the following scenarios presents the strongest challenge to the central premises of auteur theory as described in the passage?",
        "ch": [
            "A director uses handheld cameras and natural ambient light to film a personal drama in an urban neighborhood.",
            "A film critic identifies recurrent visual motifs in five consecutive mystery movies produced by the same filmmaker.",
            "An independent director rewrites an assigned studio script to better express their idiosyncratic worldview.",
            "A celebrated movie's visual style is proven to have been entirely designed by its cinematographer and art director."
        ],
        "a": 3,
        "e": "<strong>Paragraph 4 details Pauline Kael's critique that auteur theory promotes a \"romantic mythology of solitary genius that ignored the intrinsically collaborative, industrial nature of filmmaking\" and credited the director for contributions actually made by cinematographers, screenwriters, and designers. Proving a film's style came entirely from the cinematographer directly undermines the auteurist claim that the director is the sole visual author.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (True Fact Wrong Question): Handheld cameras and location shooting embody New Wave techniques rather than challenging auteur theory.<br>&bull; B (True Fact Wrong Question): Identifying recurring visual motifs across multiple films is the hallmark method of auteurist criticism.<br>&bull; C (True Fact Wrong Question): A director imposing their worldview onto a studio script exemplifies auteurist practice (as with Hitchcock and Hawks)."
    },
    {
        "q": "The author quotes François Truffaut's assertion that \"there were no good or bad themes, only good or bad directors\" (paragraph 2) primarily to:",
        "ch": [
            "condemn directors who chose to work in popular genres such as Westerns and psychological murder thrillers.",
            "emphasize that artistic merit in cinema derives from formal visual execution rather than narrative subject matter.",
            "argue that screenwriters deserve greater remuneration and public credit than technical film directors.",
            "suggest that European art cinema should avoid exploring complex psychological or ethical dilemmas in plots."
        ],
        "a": 1,
        "e": "<strong>Paragraph 2 explains that for auteurists, artistic identity was revealed not in the ostensible literary prestige of the plot, but in how visual staging transformed dramatic material. Truffaut's dictum underscores that aesthetic value resides in the director's formal visual treatment (<em>mise-en-scène</em>) rather than the intrinsic nobility of the narrative topic.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Auteurists explicitly championed directors working in commercial genres like Westerns and thrillers.<br>&bull; C (Directional Inversion): The quote reinforces the supremacy of the director over the screenwriter, not the reverse.<br>&bull; D (Overgeneralization/Extreme): Truffaut was not advising cinema to avoid complex dilemmas, but arguing that any subject can be made great through visionary direction."
    }
]

passage_data = {
    "id": "exam_cars90_5_p2",
    "sec": "CARS",
    "topic": "Auteur Theory & Mise-en-Scène in French New Wave Cinema",
    "sheet": None,
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_5",
    "passage": passage_text,
    "qs": qs
}

if __name__ == "__main__":
    errs, wc = validate_passage(passage_data, 2, 6)
    if errs:
        print("ERRORS in P2:")
        for e in errs:
            print(" -", e)
    else:
        print(f"P2 PASSED VALIDATION! Word count: {wc}")
