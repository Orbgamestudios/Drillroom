# /home/cgslinde/DrillRoom/DrillRoom/scratch/cars5/p1.py
import json
from validator import validate_passage

passage_text = """<div class="ttl">Passage 1 (Questions 1&ndash;6)</div>
<p>In his landmark 1925 anthology <i>The New Negro: An Interpretation</i>, philosopher and cultural critic Alain Locke announced a profound metamorphosis in African American intellectual and artistic life. Locke argued that the Black American had historically been treated not as an autonomous human subject, but as a sociological problem, an ideological abstraction, or a sentimental ward of philanthropic pity. The &ldquo;Old Negro&rdquo; was a defensive figure, encumbered by the burden of Victorian respectability politics and anxious apologetics designed to placate white sensibilities and disprove racist pseudoscientific stereotypes. In contrast, Locke proclaimed that the burgeoning cultural flowering in Harlem represented a spiritual coming of age. The New Negro was shedding the psychology of passive grievance in favor of dynamic self-direction, transitioning from social subservience to expressive sovereignty. For Locke, this psychological liberation could not be achieved primarily through political lobbying or economic accommodation; it required a cultural renaissance that asserted Black modernism on its own terms.</p>
<p>Central to Locke&rsquo;s aesthetic doctrine was the systematic repudiation of nineteenth-century minstrel caricatures that had reduced Black expressive culture to comical buffoonery or primitive spectacle. However, rather than fleeing from racial idioms to mimic the sterile academic conventions of European classicism, Locke urged Black creators to excavate their distinct ancestral and vernacular traditions. He identified Negro spirituals, the secular blues, colloquial folklore, and ancestral African plastic arts as profound repositories of formal aesthetic sophistication. Locke envisioned a reciprocal dialogue between ancient African design and contemporary American modernism. He encouraged visual artists like Aaron Douglas to synthesize ancestral geometric motifs with dynamic cubist silhouettes, and lauded writers such as Langston Hughes and Zora Neale Hurston for transmuting the syncopated idioms of jazz and Southern folk speech into sophisticated literary forms. In Locke&rsquo;s estimation, authentic Black folk culture possessed an intrinsic vitality capable of reinvigorating an exhausted Western modernist aesthetic.</p>
<p>This theoretical stance ignited an intense debate over the relationship between art and politics, crystallizing in a famous ideological dispute between Locke and W. E. B. Du Bois. In his 1926 address &ldquo;Criteria of Negro Art,&rdquo; Du Bois championed an unapologetically instrumentalist philosophy, famously declaring that &ldquo;all art is propaganda and ever must be, despite the wailing of the purists.&rdquo; For Du Bois, aesthetic endeavor was subordinate to the paramount struggle for civil rights, voting access, and racial justice; an artwork was judged by its efficacy in refuting white supremacy and advancing political enfranchisement. Locke resisted this didactic prescription. He warned that subordinating creative expression to political utility trapped Black artists in reactive, defensive postures, chaining their imaginations to the very racial pathology they sought to overcome. By treating art as sociological propaganda, Locke argued, one sacrificed formal nuance, complex interiority, and authentic psychological depth. True emancipation lay in artistic autonomy&mdash;the freedom to depict Black life in its rich contradictions without bearing the constant burden of racial ambassadorship.</p>
<p>Subsequent cultural theorists have raised pertinent questions regarding the political vulnerabilities of Locke&rsquo;s aestheticism. Critics such as Harold Cruse noted that the New Negro movement was precarious because it relied heavily on white philanthropic patrons who often commodified Black exoticism, while remaining largely aloof from the material, unionized struggles of the Black industrial proletariat. When the Great Depression devastated Harlem, cultural acclaim proved incapable of shielding Black communities from structural economic collapse. Nonetheless, Locke&rsquo;s enduring achievement was epistemological. By rejecting both the assimilationist impulse to imitate white artistic canons and the utilitarian impulse to reduce creative literature to sociological polemics, Locke established the philosophical foundation for modern Black cultural self-determination.</p>"""

# Questions for Passage 1:
# Target answers: Q1: A, Q2: C, Q3: B, Q4: D, Q5: A, Q6: C
# Check answer parity strictly for each!

qs = [
    {
        "q": "Which of the following best expresses the primary purpose of the passage?",
        "ch": [
            "To analyze Alain Locke's formulation of the New Negro aesthetic and its debates regarding cultural autonomy.",
            "To argue that W. E. B. Du Bois's concept of racial propaganda was inherently superior to modernist aestheticism.",
            "To document how white philanthropic patronage ultimately caused the total socioeconomic collapse of Harlem.",
            "To contrast nineteenth-century minstrel caricatures with the geometric innovations introduced by Aaron Douglas."
        ],
        "a": 0,
        "e": "<strong>The passage comprehensively analyzes Alain Locke's philosophical articulation of the \"New Negro\" aesthetic, contrasting it with the defensive \"Old Negro,\" exploring his debate with Du Bois regarding aesthetic autonomy versus political propaganda, and evaluating both its material critiques and lasting intellectual legacy.</strong><br><br><em>Distractor Traps:</em><br>&bull; B (Directional Inversion): The author presents Locke's defense of artistic autonomy as a legitimate and profound alternative to Du Bois's instrumentalism, rather than asserting Du Bois was inherently superior.<br>&bull; C (Overgeneralization/Extreme): Paragraph 4 notes that reliance on white patrons was a vulnerability noted by critics and that the Great Depression devastated Harlem, but does not claim patronage caused the total economic collapse.<br>&bull; D (True Fact Wrong Question): While minstrelsy and Douglas are discussed in paragraph 2, this is supporting detail rather than the overarching primary purpose of the passage."
    },
    {
        "q": "According to the passage, Alain Locke characterized the \"Old Negro\" primarily as an entity that:",
        "ch": [
            "embraced avant-garde European cubism while completely abandoning traditional African folk materials.",
            "subordinated cultural expression to aggressive industrial labor strikes and socialist union organizing.",
            "operated defensively within respectability politics to soothe white prejudices and disprove racial stereotypes.",
            "rejected philanthropic assistance from white patrons in favor of militant political self-determination."
        ],
        "a": 2,
        "e": "<strong>Paragraph 1 explicitly describes the \"Old Negro\" as \"a defensive figure, encumbered by the burden of Victorian respectability politics and anxious apologetics designed to placate white sensibilities and disprove racist pseudoscientific stereotypes.\"</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Plausible Extrapolation Not in Passage): The Old Negro did not embrace avant-garde cubism; Locke encouraged New Negro artists like Aaron Douglas to synthesize ancestral motifs with modern techniques.<br>&bull; B (Directional Inversion): Industrial labor agitation is associated in paragraph 4 with the Black industrial proletariat that the movement supposedly overlooked, not the Victorian apologetics of the Old Negro.<br>&bull; D (Directional Inversion): The passage states the Old Negro was treated as a \"sentimental ward of philanthropic pity\" rather than rejecting philanthropic assistance."
    },
    {
        "q": "Based on the passage, Locke would most likely agree with which of the following statements concerning Black artistic creation?",
        "ch": [
            "True artistic excellence requires Black authors to master European classicism before consulting folk idioms.",
            "Creative expression achieves its deepest social significance when freed from the imperative of direct propaganda.",
            "Visual and literary representations must prioritize didactic political arguments to overturn racial disenfranchisement.",
            "Authentic cultural modernism can flourish only if artists completely sever connections to ancestral traditions."
        ],
        "a": 1,
        "e": "<strong>Paragraph 3 explains that Locke resisted didactic prescriptions and argued that true emancipation lay in artistic autonomy, warning that subordinating art to political utility trapped Black artists in reactive, defensive postures and compromised psychological depth and formal nuance.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Directional Inversion): Paragraph 2 explicitly notes that Locke opposed \"fleeing from racial idioms to mimic the sterile academic conventions of European classicism.\"<br>&bull; C (Misattribution of Viewpoint): This represents W. E. B. Du Bois's instrumentalist perspective (\"all art is propaganda\"), which Locke directly contested.<br>&bull; D (Directional Inversion): Locke explicitly urged creators to \"excavate their distinct ancestral and vernacular traditions,\" identifying African plastic arts as vital."
    },
    {
        "q": "The author mentions W. E. B. Du Bois's 1926 address \"Criteria of Negro Art\" in paragraph 3 primarily to:",
        "ch": [
            "demonstrate that Black intellectuals were universally opposed to incorporating folk traditions into literature.",
            "prove that Alain Locke failed to understand the urgent legal dangers confronting African Americans in the South.",
            "expose the ideological consensus that unified Harlem Renaissance figures against modernist experimentation.",
            "illuminate a fundamental theoretical divergence regarding whether art should serve immediate political ends."
        ],
        "a": 3,
        "e": "<strong>Paragraph 3 introduces Du Bois's famous declaration that \"all art is propaganda\" to highlight the central ideological conflict in the Harlem Renaissance between Du Bois's utilitarian view of art as a weapon for civil rights and Locke's defense of aesthetic autonomy.</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Overgeneralization/Extreme): Neither Locke nor Du Bois opposed folk traditions; the dispute concerned whether art must function strictly as political propaganda.<br>&bull; B (Plausible Extrapolation Not in Passage): The passage notes Locke was \"deeply committed to racial justice\" and does not introduce Du Bois to prove Locke was ignorant of racial dangers.<br>&bull; C (Directional Inversion): Rather than showing an ideological consensus, the citation highlights an \"intense debate\" and \"ideological dispute\" between two opposing philosophies."
    },
    {
        "q": "Which of the following situations most closely parallels Locke's recommended approach to cultural modernism?",
        "ch": [
            "An Indigenous composer incorporates tribal chants and rhythms into an avant-garde orchestral symphony.",
            "A labor union leader commissions a series of informational pamphlets detailing corporate workplace violations.",
            "A classical violinist abandons regional folk ballads to perform only traditional eighteenth-century sonatas.",
            "An academic committee bans all non-canonical literature from a university's foundational history curriculum."
        ],
        "a": 0,
        "e": "<strong>Paragraph 2 describes Locke's model: synthesizing distinct ancestral and vernacular materials (spirituals, blues, African plastic motifs) with modern artistic forms (cubism, jazz literature, avant-garde design). An Indigenous composer blending ancestral tribal chants with modern orchestral forms perfectly mirrors this dynamic synthesis.</strong><br><br><em>Distractor Traps:</em><br>&bull; B (Misattribution of Viewpoint): Commissioning purely informational political/labor pamphlets exemplifies Du Bois's instrumental propaganda model rather than Locke's aesthetic synthesis.<br>&bull; C (Directional Inversion): Abandoning folk ballads to mimic European classical conventions is precisely the sterile mimicry Locke cautioned against.<br>&bull; D (Directional Inversion): Enforcing rigid traditionalist canons directly contradicts Locke's innovative, pluralistic modernism."
    },
    {
        "q": "The critique raised by Harold Cruse in the final paragraph suggests that the New Negro movement was vulnerable because it:",
        "ch": [
            "relied exclusively on governmental subsidies that were terminated after the stock market crash of 1929.",
            "rejected modern aesthetic techniques in favor of an obsolete Victorian standard of artistic decorum.",
            "depended on external financial patrons while remaining disconnected from working-class labor realities.",
            "focused so intensely on socialist labor organizing that it alienated mainstream African American churches."
        ],
        "a": 2,
        "e": "<strong>Paragraph 4 states that Cruse noted the movement \"relied heavily on white philanthropic patrons who often commodified Black exoticism, while remaining largely aloof from the material, unionized struggles of the Black industrial proletariat.\"</strong><br><br><em>Distractor Traps:</em><br>&bull; A (Plausible Extrapolation Not in Passage): The passage cites reliance on \"white philanthropic patrons,\" not governmental subsidies.<br>&bull; B (Directional Inversion): The movement championed modern aesthetic techniques; it was the \"Old Negro\" that was encumbered by Victorian standards.<br>&bull; D (Directional Inversion): Cruse's critique was precisely that the movement remained aloof from labor struggles, not that it engaged in excessive socialist organizing."
    }
]

passage_data = {
    "id": "exam_cars90_5_p1",
    "sec": "CARS",
    "topic": "Harlem Renaissance: Alain Locke & The New Negro Aesthetic",
    "sheet": None,
    "label": "Critical Analysis and Reasoning Skills",
    "examId": "cars90_5",
    "passage": passage_text,
    "qs": qs
}

if __name__ == "__main__":
    errs, wc = validate_passage(passage_data, 1, 6)
    if errs:
        print("ERRORS in P1:")
        for e in errs:
            print(" -", e)
    else:
        print(f"P1 PASSED VALIDATION! Word count: {wc}")
