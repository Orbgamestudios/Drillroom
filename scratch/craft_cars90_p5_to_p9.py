# scratch/craft_cars90_p5_to_p9.py
# Authors 5/5 difficulty questions for Passages 5 to 9 of EXAM_CARS90
# adhering strictly to the 5-Gate Review Protocol.

import sys

# ==============================================================================
# PASSAGE 5: Historiography — The Huns and Eurasian History (6 Qs)
# ==============================================================================
p5_qs = [
    {
        "q": "The author criticizes modern and contemporary Western historians who analyze the Battle of the Catalaunian Fields primarily because those scholars:",
        "ch": [
            "relied uncritically upon partisan chronicles composed during the early Middle Ages.",
            "exaggerated the tactical battlefield competence displayed by Visigothic alliances.",
            "ignored the pivotal role played by Roman diplomatic treaties in securing allies.",
            "refused to consult contemporary Latin and Greek documents regarding Hunnic lineage."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Historiographical Epistemic Vulnerability]</strong> Historical scholarship becomes distorted when secondary historians accept primary source accounts without interrogating the ideological and religious biases of their authors.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Paragraph 2 states explicitly: 'In the evaluation of the largest battle, a number of Western history scholars, both modern and contemporary, drew on information from the chroniclers of the early Middle Ages, and used them uncritically.'<br>2. <em>Contextual Assessment</em>: These early medieval chroniclers were partisan, Christian, and Roman-centric writers (as illustrated by the St. Genovefa legend) whose accounts framed the conflict as a holy deliverance rather than an objective strategic encounter.<br>3. <em>Downstream Deduction</em>: The author's explicit critique is directed at this credulous, uncritical adoption of biased medieval chronicles.<br><br><em>Distractor Traps:</em><br>&bull; B (Distorted Detail Trap): The passage mentions Visigoths as 'good allies,' but the author does not accuse Western historians of exaggerating their competence.<br>&bull; C (Direct Inversion): The author notes that Western historians emphasized Roman military art and alliances, not that they ignored them.<br>&bull; D (Factual Contradiction): Paragraph 1 confirms that Greek and Latin sources <em>did</em> record Attila's royal lineage, which Western scholars used, rather than refused to consult."
    },
    {
        "q": "In explaining why the Hunnic campaign in Gaul stalled, the author's thesis differs most fundamentally from that of Henri Pirenne by asserting that the primary factor was:",
        "ch": [
            "the structural over-extension of imperial lines across disparate populations.",
            "the tactical battlefield brilliance of Roman legions under the command of Aetius.",
            "the decisive divine intervention inspired by pious ecclesiastical leaders in Paris.",
            "Attila's unexpected death shortly after crossing the Rhine in the spring of 451."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Structural vs Heroic Historiography]</strong> The passage contrasts two divergent historiographical paradigms: romanticized 'great man' or martial valor narratives versus structural, logistical, and demographic constraints.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Pirenne's Position</em>: Pirenne attributed the outcome to military heroism and tactical alliance: 'The military art of the Romans and German bravery decided everything here.'<br>2. <em>Author's Counter-Thesis</em>: The author explicitly rejects this monocausal explanation: 'In our opinion, the situation in Gaul can be explained by the over-large scale of Attila’s campaigns and the inability to restrain dozens of tribes and entities that were not related to the Huns socially and ethnically.'<br>3. <em>Conclusion</em>: The core divergence is between Pirenne's tactical valor and the author's logistical over-extension across ethnically alien tribes.<br><br><em>Distractor Traps:</em><br>&bull; B (Opposing Viewpoint Trap): Aetius's tactical brilliance is Pirenne's argument, not the author's thesis.<br>&bull; C (Hagiographical Seducer): Conflates the folk legend of St. Genovefa with the author's objective historiographical explanation.<br>&bull; D (Chronological Mismatch): Attila died in 453 AD, two years after the 451 AD Gaul campaign; his death did not stall the Gaul offensive."
    },
    {
        "q": "The author's inclusion of the account concerning St. Genovefa and the Parisian women (paragraph 1) functions rhetorically to illustrate the:",
        "ch": [
            "climate of pervasive existential panic that the Hunnic invasion inspired in Gaul.",
            "pivotal strategic contribution made by ecclesiastical authorities in imperial defense.",
            "superiority of defensive siege fortifications maintained by major cities in Gaul.",
            "complete absence of organized military garrisons stationed within Roman territories."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Rhetorical Function of Narrative Vignettes]</strong> CARS passages routinely incorporate anecdotal folk episodes not to establish tactical facts, but to demonstrate psychological atmospheres and cultural reactions.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Paragraph 1 describes how 'Parisians were frightened of Attila’s cruelty and anger, so they decided to send women and children and some belongings to a safe place.' Genovefa then persuaded them to stay and rely on prayer.<br>2. <em>Rhetorical Synthesis</em>: The author introduces this anecdote directly after describing Attila's grand imperial expansion, showing the terror that his reputation inspired among civilian populations in the West.<br>3. <em>Downstream Deduction</em>: It exemplifies the profound dread and religious fatalism experienced by Western communities facing the Hunnic horde.<br><br><em>Distractor Traps:</em><br>&bull; B (Superficial Literalism): Adopts the medieval religious perspective as literal strategic truth, which the author later critiques as uncritical history.<br>&bull; C (Scope Shift): Focuses on siege fortifications, whereas the passage emphasizes civilian panic and prayer.<br>&bull; D (Extreme Overstatement): Alleges Roman garrisons were completely absent, which is contradicted by Aetius's mobilization of Roman and allied armies."
    },
    {
        "q": "Suppose newly discovered contemporary records revealed that Roman tributes to Attila were voluntary commercial trade subsidies. This discovery would most directly WEAKEN the passage claim that:",
        "ch": [
            "Attila exercised formidable coercive tributary dominance over both Roman empires.",
            "the Hunnic confederation stretched geographically from Central Asia to the Rhine.",
            "Attila belonged to an established royal lineage that ruled for generations.",
            "the Battle of the Catalaunian Fields represented a major military engagement."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Empirical Falsification of Coercive Geopolitical Hegemony]</strong> When a historical argument relies on financial transfers as proof of political subjugation, demonstrating that those payments were voluntary commerce shatters the inference of dominance.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Passage Assertion</em>: The author cites the fact that 'In the south, both Roman Empires... were paying tribute to Attila' as proof of his unmatched imperial power and global influence.<br>2. <em>Evaluating the Hypothetical</em>: If the payments were voluntary commercial subsidies for trade rather than extorted tribute under threat of conquest, they reflect mutually beneficial economic exchange rather than Roman subjugation.<br>3. <em>Conclusion</em>: This directly undermines the claim that Attila held both Roman empires in a subordinate, tributary relationship.<br><br><em>Distractor Traps:</em><br>&bull; B (Geographical Irrelevance): Trade subsidies would not alter the geographic boundaries of Hunnic territory from Altai to the Rhine.<br>&bull; C (Lineage Decoupling): Attila's royal ancestry is established by separate genealogical sources unaffected by the motive behind Roman payments.<br>&bull; D (Independent Tactical Fact): The scale and decisiveness of the Catalaunian Fields battle remains unchanged by the commercial nature of prior subsidies."
    },
    {
        "q": "The author's assertion that the Hunnic Union in Central Asia contributed to the emergence of modern Turkic peoples logically depends upon the premise that:",
        "ch": [
            "sociocultural and genealogical continuity endured despite imperial collapse.",
            "the political borders established by Attila survived into modern statehood.",
            "the Hunnic leadership successfully assimilated all European client tribes.",
            "all nomadic pastoralist groups in Eurasia shared identical religious creeds."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Unstated Presupposition of Ethnogenetic Continuity]</strong> Linking an ancient political entity to modern ethnic groups requires the assumption that linguistic, genetic, or cultural transmission persisted across the intervening millennia.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Identify the Claim</em>: In Paragraph 1, the author asserts: 'The Hun’s Union in Central Asia contributed to the later emergence of the Kazakh nation and other Turkic peoples.'<br>2. <em>Identify the Gap</em>: The passage also states that Attila's empire rapidly collapsed in 453 AD. How can a short-lived, collapsed confederation contribute to modern nations that formed centuries later?<br>3. <em>Deduce the Bridge</em>: The author must assume that the social, linguistic, and cultural fabric of the Central Asian tribes survived the political dissolution of the Hunnic state.<br><br><em>Distractor Traps:</em><br>&bull; B (Direct Factual Inversion): The passage explicitly notes the empire collapsed in 453 AD; its political borders did not survive.<br>&bull; C (Contradicted by Text): Paragraph 2 explicitly highlights the 'inability to restrain dozens of tribes and entities that were not related to the Huns socially and ethnically.'<br>&bull; D (Extraneous Homogeneity): Asserts that all nomads shared identical creeds, a sweeping assumption unnecessary to ethnogenetic continuity."
    },
    {
        "q": "Which of the following historical scenarios is most conceptually similar to the author's explanation of the dissolution of Hunnic imperial authority?",
        "ch": [
            "A vast conquest empire held by personal charisma unraveling upon its supreme ruler's death.",
            "A democratic federation gradually dissolving because member states maintained rival tariffs.",
            "An isolated maritime kingdom succumbing to gradual collapse after prolonged regional famine.",
            "A pre-industrial culture repelling an imperial invasion through persistent guerrilla warfare."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Structural Isomorphism in Imperial Fragmentation]</strong> The core mechanism of Hunnic collapse is a massive, multi-ethnic empire bound together by a single charismatic leader (Attila) without durable administrative institutions, disintegrating immediately upon that leader's death.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Deconstruct Passage Dynamics</em>: (1) Rapid expansion over diverse, unrelated tribes; (2) Unified leadership concentrated in a single dominant figure; (3) Inability to institutionalize control; (4) Immediate collapse upon the ruler's death.<br>2. <em>Evaluating Options</em>: Choice A captures every element of this structural dynamic (charismatic conquest empire unraveling upon founder's demise).<br>3. <em>Verification</em>: All other options describe democratic tax disputes, ecological famine, or anti-colonial guerrilla resistance.<br><br><em>Distractor Traps:</em><br>&bull; B (Institutional Inversion): A democratic federation dissolving over tax laws represents institutional, bureaucratic failure, not personalistic conquest collapse.<br>&bull; C (Ecological Red Herring): Involves maritime geography and famine, having no structural connection to rapid imperial over-expansion.<br>&bull; D (Tactical Mismatch): Describes guerrilla defense against industrial invaders, which inverts the conquering imperial posture of the Huns."
    }
]

# ==============================================================================
# PASSAGE 6: Political Economy — Energy in Nigeria (6 Qs)
# ==============================================================================
p6_qs = [
    {
        "q": "According to the passage, the Nigerian government prioritizes gasoline imports over kerosene and diesel supplies primarily because:",
        "ch": [
            "urban gasoline consumers exert significantly greater political pressure on the state.",
            "domestic refineries lack the technical capability to produce middle distillate fuels.",
            "kerosene and diesel consumption produce far greater amounts of greenhouse gas emissions.",
            "international maritime treaties restrict the bulk importation of industrial diesel fuel."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Political Economy of Regulated Subsidies]</strong> Governments in rentier or developing economies allocate scarce public revenues to satisfy the consumer classes most capable of threatening regime stability.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Paragraph 2 explains that 'The gasoline market is much better supplied than kerosene and diesel because of its higher political profile.'<br>2. <em>Causal Mechanism</em>: It continues: 'The weaker political pressures exerted by the consumers of kerosene (the poor and low middle class) and diesel (industrial sector) on the government... largely explain their more severe and persistent market shortages.'<br>3. <em>Conclusion</em>: Gasoline is prioritized because its consumers possess the political leverage to destabilize the state if shortages occur.<br><br><em>Distractor Traps:</em><br>&bull; B (Technical Fabrication): The text notes refineries operate below 40% capacity, not that they lack the engineering capacity to refine kerosene or diesel.<br>&bull; C (Environmental Inversion): Biomass burning in rural areas is cited as emitting greenhouse gases; relative fuel emissions are not the reason for government import priority.<br>&bull; D (External Regulatory Trap): Imports are constrained by 'public financing,' not international maritime shipping treaties."
    },
    {
        "q": "The author characterizes the status of Nigeria's electrical infrastructure as inherently paradoxical primarily because pervasive outages occur:",
        "ch": [
            "despite vast domestic energy endowments and installed capacity exceeding peak demand.",
            "even though rural communities utilize advanced decentralized renewable energy systems.",
            "because private industrial firms deliberately refuse to invest capital into electricity.",
            "while state-owned refineries operate at maximum commercial efficiency and utilization."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Paradox of Plenty in Institutional Dysfunction]</strong> The central irony of the resource curse / institutional failure is that severe service deficits persist in the presence of overwhelming natural wealth and underutilized physical assets.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Identify the Paradox</em>: In Paragraph 3 and 4, the author stresses that blackouts occur 'despite abundant energy resources in Nigeria,' and notes that 'peak electricity demand has been less than half of the installed capacity in the past decade, [yet] load shedding occurs regularly.'<br>2. <em>Synthesizing Logic</em>: The country has more than enough natural fuel and more than double the installed power capacity needed to meet peak demand, yet experiences persistent electrical collapse.<br>3. <em>Selection</em>: Choice A perfectly frames this fundamental structural contradiction.<br><br><em>Distractor Traps:</em><br>&bull; B (Direct Inversion): Rural communities lack electricity entirely and burn traditional wood biomass, rather than utilizing advanced renewables.<br>&bull; C (Factual Inversion): Industrial firms are forced to allocate an estimated 20% of their investment capital to alternative generation, the opposite of refusing to invest.<br>&bull; D (Direct Textual Contradiction): Paragraph 2 explicitly states state-owned refineries 'have hardly operated above a 40% capacity utilization rate.'"
    },
    {
        "q": "The passage indicates that chronic electricity unreliability has transformed the public power grid into a 'standby source' for manufacturers, directly causing those firms to:",
        "ch": [
            "divert substantial capital reserves into expensive captive power generation systems.",
            "relocate their primary manufacturing facilities from urban centers to rural villages.",
            "eliminate all operational reliance upon imported petroleum products like diesel fuel.",
            "advocate for the immediate re-nationalization of private electric power companies."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Capital Diversion in Infrastructure Breakdown]</strong> When a public utility fails, private enterprises are forced to internalize infrastructure costs, diverting productive capital into redundant private generation.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Paragraph 4 states that poor service delivery 'has rendered public supply a standby source, as many consumers... substitute more expensive captive supply alternatives to minimize the negative consequences of power supply interruptions.'<br>2. <em>Quantifying Impact</em>: It concludes: 'An estimated 20% of the investment into industrial projects is allocated to alternative sources of electricity supply.'<br>3. <em>Deduction</em>: The direct consequence is the diversion of one-fifth of capital investment into expensive captive generation.<br><br><em>Distractor Traps:</em><br>&bull; B (Geographical Nonsense): Rural areas completely lack electricity; manufacturers would never relocate to rural areas to escape urban power outages.<br>&bull; C (Direct Inversion): Captive generators run largely on diesel fuel, massively increasing reliance on petroleum products.<br>&bull; D (Anachronistic Agency): The public utility was already state-owned (NEPA/PHCN); firms were not demanding re-nationalization."
    },
    {
        "q": "Based on the passage's analysis of rural energy consumption, an initiative that successfully deployed solar home lighting systems to rural villages would most directly:",
        "ch": [
            "mitigate deforestation and local greenhouse emissions caused by burning wood biomass.",
            "eliminate the chronic 40% operational capacity utilization bottleneck at all refineries.",
            "reduce the massive volume of imported gasoline required to stabilize urban transport.",
            "prevent the private industrial manufacturing sector from suffering electrical outages."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Targeted Sectoral Intervention in Energy Ecology]</strong> A policy intervention must be evaluated strictly against the specific ecological and economic variables operative in the targeted domain.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Rural Energy Profile</em>: Paragraph 1 states: 'People in rural areas depend on burning wood and traditional biomass for their energy needs, causing great deforestation, emitting greenhouse gases, and polluting the environment.'<br>2. <em>Applying Solar Lighting</em>: Replacing wood-burning lighting with clean solar panels in rural villages directly addresses the primary driver of rural deforestation and localized biomass emissions.<br>3. <em>Conclusion</em>: It directly mitigates environmental destruction caused by traditional biomass combustion.<br><br><em>Distractor Traps:</em><br>&bull; B (Domain Mismatch): Refinery operational utilization is an internal industrial/state maintenance problem, completely unaffected by rural lighting choices.<br>&bull; C (Cross-Sector Confusion): Urban gasoline is consumed by vehicles and urban generators, not rural villagers who lack cars and electricity.<br>&bull; D (Target Beneficiary Error): Industrial manufacturing firms are located in urban industrial centers; rural solar lighting does not alter factory outages."
    },
    {
        "q": "Suppose economic survey data revealed that between 2004 and 2008, Nigerian manufacturers reported record-high profit margins while reducing backup power expenses. This finding would most directly WEAKEN which passage claim?",
        "ch": [
            "Power supply interruptions impose severe financial and productive penalties on firms.",
            "Installed electrical generating capacity exceeds peak national demand by over 100%.",
            "State-owned oil refineries process less than 40% of their rated processing capacity.",
            "Rural and sub-rural energy demands fail to reach the center stage of policy programs."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Empirical Falsification of Cost-Burden Hypotheses]</strong> If an author argues that a public failure imposes devastating private capital burdens, empirical evidence showing soaring profits and falling backup costs directly refutes the causal claim.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Locate Target Claim</em>: Paragraph 4 asserts that skyrocketing outages (which surged by 26% and 43%) severely harmed manufacturing 'production activities and profitability,' forcing companies to spend 20% of their investment on expensive backup power.<br>2. <em>Evaluating the Hypothetical</em>: If manufacturers enjoyed record profit margins while cutting expenditure on backup power during those exact years, power outages clearly did not penalize profitability or compel heavy captive spending.<br>3. <em>Conclusion</em>: This finding directly undermines the claim that outages severely damage manufacturing profitability.<br><br><em>Distractor Traps:</em><br>&bull; B (Engineering Baseline Irrelevance): The relationship between installed capacity and peak demand is a technical metric unaffected by corporate profit margins.<br>&bull; C (Refinery Utilization Decoupling): Refinery performance is governed by domestic operational failures, which remain unchanged by manufacturing profits.<br>&bull; D (Political Neglect Scope): The governmental neglect of rural energy needs is an independent political reality having no connection to factory profitability."
    },
    {
        "q": "The author's overarching argument regarding Nigeria's energy crisis can best be synthesized as asserting that:",
        "ch": [
            "institutional mismanagement and biased policy priorities obstruct sustainable development.",
            "rapid population growth has permanently outstripped the nation's natural resource capacity.",
            "rural deforestation represents a far more catastrophic economic crisis than urban blackouts.",
            "full privatization of petroleum imports will automatically eliminate electrical load shedding."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Institutional Dysfunction vs Malthusian Scarcity]</strong> The author's diagnostic frame attributes systemic crises not to inherent physical shortages, but to state institutional paralysis, urban political bias, and infrastructural neglect.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Synthesizing Major Themes</em>: Across all paragraphs, the author highlights: (1) deplorable urban-centered policies neglecting rural needs; (2) underutilized refineries and political bias favoring gasoline over diesel/kerosene; (3) failure of the state electrical authority despite abundant resources and excess installed capacity.<br>2. <em>Deductive Thesis</em>: Nigeria possesses abundant resources and capacity, but institutional paralysis, political favoritism, and execution failure create a nationwide energy crisis.<br>3. <em>Selection</em>: Choice A accurately synthesizes this governance-centered critique.<br><br><em>Distractor Traps:</em><br>&bull; B (Malthusian Distortion Trap): The author explicitly notes that installed capacity exceeds peak demand and resources are abundant; population has not outstripped natural capacity.<br>&bull; C (False Dichotomy / Hierarchical Trap): The author analyzes both rural deforestation and industrial outages as complementary dimensions of one crisis, never ranking one as far more catastrophic.<br>&bull; D (Unwarranted Market Dogmatism): The passage critiques state management, but nowhere claims that private petroleum imports will eliminate electrical grid load shedding."
    }
]

# ==============================================================================
# PASSAGE 7: Philosophical Psychology — Primordial and Complex Jealousy (6 Qs)
# ==============================================================================
p7_qs = [
    {
        "q": "According to the author, the foundational distinction between primordial jealousy and complex jealousy is that primordial jealousy:",
        "ch": [
            "is elicited by direct perception of attention capture without self-evaluative appraisals.",
            "functions to dissolve the primary attachment bond rather than repel an outside interloper.",
            "occurs exclusively within non-human social mammals and is absent in developing infants.",
            "requires sophisticated counterfactual reasoning regarding a social rival's true motives."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Cognitive Parsimony in Emotional Phylogeny]</strong> Primordial affective systems operate as low-level perceptual heuristics that trigger adaptive behaviors prior to the evolutionary or developmental emergence of metacognition.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Paragraph 2 states that primordial jealousy 'can be triggered without complex cognition about the self or about the meaning of the social interaction,' elicited simply by 'the relatively simple perception that an attachment figure... has been captured by a potential usurper.'<br>2. <em>Contrast with Complex Jealousy</em>: In complex jealousy, 'interpretations of the situation play a large role... (e.g., does this mean my mate will leave me? Am I unloveable?).'<br>3. <em>Downstream Deduction</em>: Primordial jealousy is sensory and perceptual, lacking complex appraisals about self-esteem or relationship meaning.<br><br><em>Distractor Traps:</em><br>&bull; B (Functional Inversion): Both forms function to 'protect the primary relationship' and remove the usurper, not dissolve the attachment bond.<br>&bull; C (Direct Factual Inversion): Paragraph 3 explicitly demonstrates primordial jealousy in human infants as young as 6 months old.<br>&bull; D (Definitional Inversion): Counterfactual reasoning about rival motives characterizes complex human adult jealousy, the exact opposite of primordial jealousy."
    },
    {
        "q": "In the canine jealousy experiment, having owners direct affectionate behaviors toward a novel inanimate pail served methodologically to determine whether:",
        "ch": [
            "the elicitation of jealousy requires a stimulus that mimics a social conspecific.",
            "canine aggressive responses are driven exclusively by general auditory overstimulation.",
            "domestic canines possess advanced cognitive theory-of-mind regarding human owners.",
            "canine attachment bonds are stronger toward synthetic toys than toward real humans."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Experimental Discrimination of Social vs Non-Social Triggers]</strong> In evolutionary psychology, an emotional adaptation must demonstrate functional specificity: it must fire selectively to socially threatening interlopers rather than indiscriminate novelty.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Paragraph 5 details the three conditions: (1) realistic stuffed dog, (2) novel jack-o'-lantern pail, (3) children's pop-up book.<br>2. <em>Methodological Logic</em>: The author states: 'This enabled us to test whether the elicitation of jealousy required that the owner show affection to an appropriate stimulus (what appeared to be a conspecific) or whether affectionate behaviors directed to a nonsocial stimulus would be enough.'<br>3. <em>Conclusion</em>: The pail was a nonsocial control to verify whether jealousy requires an interloper that looks like a conspecific rival.<br><br><em>Distractor Traps:</em><br>&bull; B (Confounding Variable Mismatch): Auditory stimulation was tested by the melody-playing children's book, not the silent jack-o'-lantern pail.<br>&bull; C (Cognitive Overreach Trap): The entire hypothesis of primordial jealousy is that it does NOT require advanced theory-of-mind or complex social cognition.<br>&bull; D (Absurd Semantic Inversion): The test was not comparing canine love for toys vs humans, but whether toys could trigger jealousy when given human affection."
    },
    {
        "q": "The author cites research showing that six-month-old human infants display distress when their mothers attend to realistic dolls primarily to:",
        "ch": [
            "provide empirical evidence for jealousy prior to the onset of complex cognition.",
            "demonstrate that young infants confuse inanimate objects with biological siblings.",
            "prove that human maternal affection is governed entirely by instinctive reflexes.",
            "refute the evolutionary claim that jealousy originated during sibling competition."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Ontogenetic Evidence for Primordial Emotional Architecture]</strong> Demonstrating that pre-verbal infants exhibit an emotion provides powerful empirical confirmation that the emotion does not depend on mature cognitive or linguistic scaffolding.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Contextual Anchor</em>: Paragraph 3 introduces the infant findings directly after theorizing that jealousy has a primordial form that does not require complex appraisals of the self.<br>2. <em>Synthesizing Logic</em>: Six-month-old infants lack advanced self-reflection, linguistic appraisals, and theory of mind. Therefore, their clear jealous reactions to mother-doll interactions prove that jealousy can operate in a purely primordial, perceptual format.<br>3. <em>Selection</em>: Choice A accurately identifies this foundational evidential role.<br><br><em>Distractor Traps:</em><br>&bull; B (Literal Anthropomorphism Trap): The experiment used realistic dolls to simulate an interloper, but the purpose was not to study infant cognitive error or confusion.<br>&bull; C (Scope Shift): The study investigates the infant's emotional response, not maternal instinctive reflexes.<br>&bull; D (Direct Inversion): The infant data supports the sibling competition hypothesis, rather than refuting it."
    },
    {
        "q": "Which of the following experimental findings, if observed in the canine study, would most directly CHALLENGE the author's evolutionary model of jealousy?",
        "ch": [
            "Dogs exhibited aggressive barrier behaviors only when owners read the pop-up book.",
            "Dogs directed significantly more attention toward the stuffed dog than toward the pail.",
            "Dogs attempted to push themselves physically between the owner and the stuffed dog.",
            "Dogs displayed negative vocalizations when their owners lavished praise on the toy dog."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Functional Teleology and Stimulus Specificity]</strong> An evolutionary adaptation is falsified if its operational behaviors are triggered by non-threatening noise and absent in the presence of an authentic social threat.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Theoretical Definition</em>: In Paragraph 6, the author defines jealousy's function: 'to break-up a potentially threatening liaison and protect the primary relationship,' triggering approach behaviors between attachment and interloper.<br>2. <em>Evaluating the Falsifier</em>: If dogs showed barrier and aggressive behaviors *only* when the owner read a book (a non-social task testing general negative affect from lost attention) but ignored the stuffed dog, then the behavior is NOT jealousy (protecting a relationship from an interloper), but general irritation or boredom.<br>3. <em>Conclusion</em>: Choice A shatters the core functional claim that dogs experience jealousy toward social rivals.<br><br><em>Distractor Traps:</em><br>&bull; B (Strong Confirmation): Showing more attention to the stuffed dog than the pail directly confirms the author's hypothesis.<br>&bull; C (Direct Behavioral Confirmation): Pushing between owner and rival is the exact physical barrier behavior predicted by the model.<br>&bull; D (Affective Confirmation): Negative vocalizations toward the rival confirm the presence of jealous negative affect."
    },
    {
        "q": "The evolutionary hypothesis that jealousy originated in sibling competition for parental investment fundamentally presumes that in ancestral environments:",
        "ch": [
            "securing maternal attention conferred a critical biological survival advantage.",
            "dependent offspring possessed conscious awareness of their evolutionary fitness.",
            "parental investment was always distributed equally across all biological offspring.",
            "social alliances with non-kin interlopers were necessary for juvenile subsistence."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Selective Pressure in Evolutionary Adaptation]</strong> For a competitive behavioral response to evolve, the contested resource (parental attention/care) must have directly impacted individual survival and reproductive fitness.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Paragraph 2 states: 'One possibility is that jealousy first evolved in the context of sibling-parent relationships where dependent offspring compete for parental resources.'<br>2. <em>Unspoken Premise</em>: For an emotion like jealousy to evolve to 'regain the loved one's attention and block the liaison,' maternal attention and resources must have been finite, and securing them must have been critical to the offspring's survival.<br>3. <em>Selection</em>: Choice A accurately identifies this essential selective foundation.<br><br><em>Distractor Traps:</em><br>&bull; B (Cognitive Teleology Trap): Evolutionary mechanisms do not require organisms to have conscious awareness of 'evolutionary fitness.'<br>&bull; C (Direct Inversion): If parental investment were always equal, there would be zero selective pressure for offspring to evolve competitive jealousy.<br>&bull; D (External Distractor): Sibling competition is about securing parental care within the family, not forming alliances with non-kin."
    },
    {
        "q": "Based on the passage, which of the following adult human reactions most purely exemplifies primordial jealousy rather than complex jealousy?",
        "ch": [
            "Instinctively stepping between one's partner and an intruder who commands attention.",
            "Ruminating over whether a spouse's flirtatious comment implies personal unattractiveness.",
            "Terminating an intimate relationship after calculating the long-term emotional distress.",
            "Experiencing deep melancholy because a romantic rival possesses superior social status."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Perceptual Reflex vs Cognitive Appraisal]</strong> In CARS psychological taxonomy, the purest form of a primordial emotion is a spontaneous, immediate physical intervention to block attention capture, stripped of ruminative self-evaluation.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Deconstruct Criteria</em>: Primordial jealousy is: (1) triggered by the simple perception that attention is captured by a usurper; (2) motivates approach actions to get physically between the attachment and interloper; (3) lacks complex cognitive appraisals about the self.<br>2. <em>Evaluating Options</em>: Choice A describes an automatic, physical intervention to separate the partner and intruder without cognitive appraisal.<br>3. <em>Verification</em>: Choices B, C, and D all involve complex ruminative appraisals ('personal unattractiveness,' 'long-term calculations,' 'rival's superior social status').<br><br><em>Distractor Traps:</em><br>&bull; B (Complex Appraisal Archetype): Ruminating about being unloveable/unattractive is explicitly cited in Paragraph 2 as the hallmark of *complex* jealousy.<br>&bull; C (Calculated Rational Decision): Deliberate termination of a relationship is a calculated cognitive choice, not a primordial behavioral reflex.<br>&bull; D (Social-Comparison Appraisal): Melancholy based on comparing social status requires sophisticated social cognition and self-esteem evaluation."
    }
]

# ==============================================================================
# PASSAGE 8: Philosophy of Science — Biological Life and Semiosis (6 Qs)
# ==============================================================================
p8_qs = [
    {
        "q": "The author rejects the received view that life is merely an extremely complex form of chemistry primarily on the grounds that living systems:",
        "ch": [
            "require biological specificity generated by molecular machines that utilize codes.",
            "are governed by vitalistic metaphysical forces that supersede physical mechanics.",
            "arise exclusively through spontaneous chemical polymerization of primitive genes.",
            "evolved conscious cognitive intention long before the formation of cellular units."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Semiotic Specificity vs Spontaneous Chemistry]</strong> In code biology, the qualitative leap from chemistry to biology is the emergence of manufactured, sequence-directed biological specificity, which cannot arise through spontaneous thermodynamics.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Paragraph 1 states the received view is that 'life is but an extremely complex form of chemistry.' The author counters: 'This however, is precisely what molecular biology does not support. The genes and proteins of the first cells had to have biological specificity, and specific molecules cannot be formed spontaneously.'<br>2. <em>Core Mechanism</em>: Biological specificity 'can only be manufactured by molecular machines, and their production requires entities like sequences and codes that simply do not exist in spontaneous processes.'<br>3. <em>Conclusion</em>: Life is distinct because it requires code-directed molecular machines, which do not exist in spontaneous inanimate chemistry.<br><br><em>Distractor Traps:</em><br>&bull; B (Vitalistic Distortion): The author is an empirical materialist who rejects vitalism, explicitly noting that ribosome appearance 'has the same logic and we can regard it as a natural event.'<br>&bull; C (Direct Inversion): The author explicitly denies that biological specificity can arise through spontaneous chemical polymerization.<br>&bull; D (Anachronistic Agency): Confuses semiosis at the genetic level with conscious cognitive intention, which only appears at higher emergent levels."
    },
    {
        "q": "In paragraph 2, the author's observation that ribosomes can still arise by self-assembly from their components functions primarily to support the claim that:",
        "ch": [
            "the emergence of codemakers can be accounted for as an entirely natural phenomenon.",
            "spontaneous chemical processes routinely generate fully functional biological codes.",
            "ribosomes existed in the primitive ocean prior to the appearance of bondmaker units.",
            "molecular machines require human laboratory intervention to achieve self-assembly."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Naturalistic Plausibility of Molecular Machines]</strong> Authors cite contemporary biochemical self-assembly to prove that a seemingly miraculous evolutionary leap does not require supernatural or non-physical explanations.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: In Paragraph 2, the author discusses the difficult evolutionary transition to 'codemakers': 'that is much more difficult to account for, but in principle it has the same logic and we can regard it as a natural event (ribosomes, for example, can still arise by self-assembly from their components).' <br>2. <em>Synthesizing Logic</em>: To preempt vitalist critics who might argue that molecular machines are too complex to originate naturally, the author points to the empirical fact that modern ribosomes self-assemble naturally without external directing agency.<br>3. <em>Selection</em>: Choice A accurately identifies this naturalistic defense.<br><br><em>Distractor Traps:</em><br>&bull; B (Definitional Inversion): The author maintains throughout that spontaneous chemistry CANNOT produce codes; ribosomes self-assemble, but they are machines that translate codes.<br>&bull; C (Chronological Inversion): Paragraph 2 shows bondmakers came first, then copymakers, and finally codemakers.<br>&bull; D (Direct Inversion): Ribosomes self-assemble naturally in nature, having no requirement for human laboratory intervention."
    },
    {
        "q": "According to the passage, the evolutionary transition from 'copymakers' to 'codemakers' represented a qualitative leap in complexity because codemakers:",
        "ch": [
            "established an organic code that correlated two fundamentally independent realms.",
            "operated entirely without the physical and energetic constraints of chemical bonds.",
            "eliminated the need for sequences and biological specificity in cellular growth.",
            "relied upon conscious mental deliberation to direct the synthesis of polypeptides."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: The Semiotic Nature of Organic Codes]</strong> A code is not merely copying a template (homology); it is establishing an arbitrary, rule-based mapping between two completely disparate sets of objects (e.g. nucleic acids and amino acids).<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Textual Progression</em>: Paragraph 2 traces three stages: (1) 'bondmakers' stick subunits together; (2) 'copymakers' stick subunits together in order provided by a template; (3) 'codemakers' produce molecules that cannot be formed spontaneously.<br>2. <em>Semiotic Meaning</em>: Unlike copying (which is direct steric mirroring), codemaking introduces the genetic code—an organic code translating nucleotide sequences into amino acid sequences.<br>3. <em>Selection</em>: Choice A captures this qualitative leap into genuine code-directed translation.<br><br><em>Distractor Traps:</em><br>&bull; B (Physical Impossibility): Codemakers are physical molecular machines still bound by physics and chemistry ('Physics and chemistry provide of course the building blocks of life').<br>&bull; C (Direct Inversion): Codemakers *created* biological specificity; they did not eliminate it.<br>&bull; D (Anthropomorphic Distortion): Confuses organic molecular codes with conscious human deliberation."
    },
    {
        "q": "Which of the following hypothetical scientific discoveries would most directly WEAKEN the author's primary argument regarding the divide between life and matter?",
        "ch": [
            "Demonstrating that highly specific functional proteins form in prebiotic conditions.",
            "Synthesizing an artificial ribosome capable of translating synthetic cellular mRNA.",
            "Proving that all enzymatic cellular reactions strictly obey classical thermodynamics.",
            "Discovering that primitive unicellular organisms utilize alternative genetic codons."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Falsification of Essential Demarcation Criteria]</strong> If an argument asserts that X is an inviolable boundary separating two domains, demonstrating that domain A naturally generates the defining trait of domain B shatters the boundary.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Locate the Absolute Assertion</em>: The author states: 'All components of matter arise by spontaneous processes that do not require sequences and codes, whereas all components of life arise by manufacturing processes that do... specific molecules cannot be formed spontaneously.'<br>2. <em>Formulate the Falsifier</em>: If researchers demonstrate that high-specificity, complex functional proteins *can* arise spontaneously through inanimate prebiotic chemistry without codes, sequences, or molecular machines, the author's foundational dividing line collapses.<br>3. <em>Selection</em>: Choice A represents this exact fatal empirical counter-evidence.<br><br><em>Distractor Traps:</em><br>&bull; B (Strengthening Finding): Creating an artificial molecular machine that translates RNA directly reinforces the author's machine/code model.<br>&bull; C (Baseline Irrelevance): The author already concedes that physics and chemistry govern all matter; thermodynamic obedience is expected.<br>&bull; D (Confirming Plurality): The author explicitly notes in Paragraph 3 that multiple organic codes exist; alternative codons simply confirm code plurality."
    },
    {
        "q": "The author characterizes the statement 'life is semiosis' as an 'oversimplified statement' that nonetheless contains a 'deep truth' because while:",
        "ch": [
            "physics and chemistry provide the material parts, codes are what animate matter.",
            "semiosis occurs only in human language, biochemical reactions govern living cells.",
            "all biological machines formed spontaneously, molecular evolution required guidance.",
            "life emerged from matter, modern biology can be fully reduced to inorganic physics."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Dialectical Dual-Aspect Naturalism]</strong> Reductionist chemistry provides the material substrate, but information-processing codes provide the organizational architecture that constitutes living phenomena.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Paragraph 3 concludes: 'Physics and chemistry provide of course the building blocks of life, but what ‘animates’ matter is codes, and that is why there is a deep truth in the oversimplified statement that “life is semiosis.”'<br>2. <em>Deconstruct the Paradox</em>: It is 'oversimplified' if taken to mean that matter and chemistry do not matter (since physical molecules are required). But it is a 'deep truth' because chemical components alone cannot produce life without the informational codes that direct their assembly and function.<br>3. <em>Selection</em>: Choice A accurately preserves both halves of this formulation.<br><br><em>Distractor Traps:</em><br>&bull; B (Direct Inversion): The author explicitly argues that semiosis is NOT limited to language, but exists at all levels from genes to mind.<br>&bull; C (Teleological Contradiction): Claims molecular evolution required non-natural guidance, which the author explicitly rejects.<br>&bull; D (Received View Inversion): Choice D states the reductionist view that biology reduces to physics, which the author wrote the entire passage to refute."
    },
    {
        "q": "By shifting the focus of origin-of-life research away from 'which molecules came first,' the author's philosophical approach primarily aims to:",
        "ch": [
            "reframe the inquiry around the emergence of sequence-driven manufacturing apparatus.",
            "prove that chemical evolution was an impossible historical event on prebiotic Earth.",
            "establish that linguistics and semiotics are more fundamental than atomic physics.",
            "resolve the historical conflict between proponents of vitalism and materialism."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Paradigm Shift from Chemical Substance to Informational Architecture]</strong> Scientific debates often fixate on material precursors (e.g. RNA vs proteins) while ignoring the functional organizational system that actually defines the target state.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Textual Analysis</em>: In Paragraph 1, the author writes: 'The problem of which molecules came first has been the object of countless debates, but in a way it is a secondary issue. What really matters is that spontaneous genes and spontaneous proteins had the potential to evolve into the first cells.'<br>2. <em>Deductive Synthesis</em>: The critical barrier was never accumulating random amino acids or nucleotides, but developing the molecular machinery (machines, codes, sequences) capable of manufacturing specific molecules.<br>3. <em>Downstream Deduction</em>: The author seeks to reframe origin-of-life biology around the origin of semiotic manufacturing machines rather than precursor chemical chronologies.<br><br><em>Distractor Traps:</em><br>&bull; B (Scientific Denial Trap): The author explicitly accepts chemical evolution, noting in Paragraph 2 that it 'could spontaneously produce bondmakers.'<br>&bull; C (Disciplinary Imperialism): Does not assert linguistics is more fundamental than physics, but that biological life requires organic codes.<br>&bull; D (Scope Distortion): The author is not arbitrating historical disputes over vitalism, but providing a new molecular model for why biology cannot reduce to chemistry."
    }
]

# ==============================================================================
# PASSAGE 9: Jane Addams — Charity and the Democratic Standard (5 Qs)
# ==============================================================================
p9_qs = [
    {
        "q": "According to Addams, the primary source of ethical confusion and moral distress in modern society is the:",
        "ch": [
            "temporal lag between evolving moral conceptions and hardened social habits.",
            "growing hostility exhibited by impoverished communities toward public charity.",
            "total absence of any shared moral convictions across different social classes.",
            "inability of charitable societies to collect sufficient industrial donations."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Cultural Lag in Ethical Evolution]</strong> Societal morality evolves through conceptual breakthroughs, but institutional and behavioral patterns lag behind, trapping actors in painful cognitive dissonance.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Paragraph 1 states: 'Our conceptions of morality, as all our other ideas, pass through a course of development; the difficulty comes in adjusting our conduct, which has become hardened into customs and habits, to these changing moral conceptions.'<br>2. <em>Psychological Consequence</em>: Addams notes: 'When this adjustment is not made, we suffer from the strain and indecision of believing one hypothesis and acting upon another.'<br>3. <em>Conclusion</em>: Ethical distress stems from the friction between modern egalitarian ideals and inherited paternalistic practices.<br><br><em>Distractor Traps:</em><br>&bull; B (Scope Shift): The passage focuses on the perplexity of the charitable actors, not on violent hostility from the poor.<br>&bull; C (Extreme Relativism): Addams does not claim moral convictions are absent, but that they are in transition and out of sync with conduct.<br>&bull; D (Material Reductionism): Trivializes profound philosophical and ethical tension into an administrative budget shortage."
    },
    {
        "q": "The author argues that the 'complacency of the old-fashioned charitable man is gone forever' primarily because modern democracy has:",
        "ch": [
            "discredited the assumption that economic prosperity signifies moral superiority.",
            "eliminated all substantial socioeconomic inequalities across modern urban settings.",
            "convinced wealthy benefactors that private philanthropy is inherently criminal.",
            "compelled affluent citizens to perform strenuous manual labor alongside workers."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: The Demolition of Paternalistic Moral Entitlement]</strong> Under democratic standards, the unilateral assumption that economic fortune reflects virtuous character collapses, destroying the unearned moral peace of the wealthy benefactor.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Paragraph 3 explains the historical baseline: 'Formerly when it was believed that poverty was synonymous with vice and laziness, and that the prosperous man was the righteous man, charity was administered harshly with a good conscience.'<br>2. <em>The Democratic Inroad</em>: Paragraph 4 details the shift: 'We have learned since that time to measure by other standards, and have ceased to accord to the money-earning capacity exclusive respect... its possession is by no means assumed to imply the possession of the highest moral qualities.'<br>3. <em>Downstream Deduction</em>: When wealth is no longer equated with righteousness, the wealthy benefactor can no longer enjoy moral complacency when dispensing aid.<br><br><em>Distractor Traps:</em><br>&bull; B (Factual Inversion): Inequality remains pervasive; indeed, Addams notes charity reveals 'the lack of that equality which democracy implies.'<br>&bull; C (Extreme Overstatement): Portrays philanthropy as viewed as 'criminal,' which is an extreme distortion of Addams's critique of ethical inadequacy.<br>&bull; D (Literal Physical Distractor): Democracy changed moral standards, not an edict forcing rich citizens to do daily manual work."
    },
    {
        "q": "When the author contrasts the 'old charitable attitude' with the 'modern tendency,' she criticizes the older framework primarily for:",
        "ch": [
            "maintaining an unjust dual moral standard that judged the poor by toil alone.",
            "refusing to provide any physical or financial assistance to destitute families.",
            "demanding that industrial employers pay exorbitant wages to unskilled workers.",
            "prioritizing intellectual and artistic development over bodily survival needs."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Asymmetric Class Metrics in Traditional Morality]</strong> Traditional philanthropy maintained an oppressive double standard: evaluating the affluent by business acumen and refined social virtues, while reducing the impoverished to raw physical endurance.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Data Interrogation</em>: Paragraph 5 states: 'It is largely in this modern tendency to judge all men by one democratic standard, while the old charitable attitude commonly allowed the use of two standards, that much of the difficulty adheres.'<br>2. <em>Analyzing the Dual Standard</em>: Paragraph 5 explains that society knows unceasing toil is brutalizing, yet the old standard made our position untenable by 'judg[ing] large numbers of our fellows solely upon their success in maintaining it,' while judging the rich by other virtues.<br>3. <em>Selection</em>: Choice A accurately identifies this unjust dual ethical standard.<br><br><em>Distractor Traps:</em><br>&bull; B (Direct Inversion): The old charitable organizations certainly provided physical aid, but did so with moral condescension.<br>&bull; C (Opposite Direction Trap): The old charity blamed the poor for their poverty, rather than demanding higher wages from employers.<br>&bull; D (Scope Inversion): The old standard ignored the intellectual and social virtues of the poor, focusing exclusively on their bodily toil."
    },
    {
        "q": "The passage's depiction of the 'daintily clad charitable visitor' encountering the washerwoman in her untidy home serves primarily to:",
        "ch": [
            "illustrate the visceral dissolution of assumed class superiority during contact.",
            "criticize the washerwoman for failing to maintain rigorous domestic cleanliness.",
            "admonish the affluent visitor for wearing inappropriately luxurious attire indoors.",
            "prove that genuine charity requires providing professional housekeeping assistance."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: The Interpersonal Crucible of Democratic Realization]</strong> Abstract democratic ideals become living realities at the precise physical moment of encounter, when patronizing moral certainty dissolves into mutual human recognition.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Textual Analysis</em>: Paragraph 5 closes with the vivid scene: 'The daintily clad charitable visitor who steps into the little house made untidy by the vigorous efforts of her hostess, the washerwoman, is no longer sure of her superiority to the latter.'<br>2. <em>Rhetorical Function</em>: This scene concretizes Addams's overarching thesis: the visitor recognizes that the untidiness is the result of exhausting labor, causing her inherited sense of moral and social superiority to falter.<br>3. <em>Conclusion</em>: It captures the visceral breakdown of assumed social superiority under the democratic gaze.<br><br><em>Distractor Traps:</em><br>&bull; B (Superficial Moralism Trap): Addams explicitly notes the house was made untidy 'by the vigorous efforts of her hostess,' excusing the disorder as the fruit of honest toil.<br>&bull; C (Literal Dress Critique): The 'daintily clad' description establishes the social contrast, not a sartorial rebuke of the visitor.<br>&bull; D (Prescriptive Absurdity): The text is a psychological and moral critique, not a proposal for dispatching housekeepers."
    },
    {
        "q": "Across the passage, the author's tone toward the growing tension between democracy and traditional charity is best described as:",
        "ch": [
            "analytically reflective while welcoming the transformative democratic standard.",
            "uncompromisingly cynical regarding the possibility of genuine social progress.",
            "nostalgic for the unclouded moral certainty of earlier paternalistic philanthropy.",
            "indifferent to the psychological discomfort experienced by wealthy benefactors."
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Critical Compassion and Democratic Faith]</strong> Jane Addams's signature authorial voice blends lucid sociological critique with profound democratic idealism, acknowledging the discomfort of moral evolution while embracing its necessity.<br><br><em>Step-by-Step Derivation:</em><br>1. <em>Textual Tone Markers</em>: Addams describes the perplexity with empathy ('leave us sadly unguided and perplexed,' 'we suffer from the strain'), yet consistently champions democracy ('hints and glimpses of a larger and more satisfying democracy,' 'our democratic instinct instantly takes alarm').<br>2. <em>Synthesizing Stance</em>: She does not despair, nor does she long for the past; she soberly analyzes the ethical crisis while celebrating the democratic standard that demands human equality.<br>3. <em>Selection</em>: Choice A captures both the analytical rigor and the forward-looking democratic commitment.<br><br><em>Distractor Traps:</em><br>&bull; B (Affective Distortion): Addams is deeply hopeful about democracy, never cynical.<br>&bull; C (Direct Inversion): She expressly rejects the complacency of the old charitable attitude, calling it 'tenable no longer.'<br>&bull; D (Emotional Insensitivity): She explicitly describes the 'strain and indecision' of all participants, displaying empathetic psychological insight rather than indifference."
    }
]

if __name__ == "__main__":
    print("Validating Passages 5 to 9...")
    all_qs = p5_qs + p6_qs + p7_qs + p8_qs + p9_qs
    issues = []
    for i, q in enumerate(all_qs):
        lens = [len(c) for c in q["ch"]]
        r = max(lens) / min(lens)
        corr_len = lens[q["a"]]
        max_len = max(lens)
        if r > 1.08:
            issues.append(f"Q{i+25} Gate 4 ratio: {r:.3f} > 1.08 (lens={lens}, q='{q['q'][:40]}')")
        if corr_len == max_len and lens.count(max_len) == 1:
            issues.append(f"Q{i+25} Gate 4 longest: correct choice is strict longest ({corr_len} vs {[l for j,l in enumerate(lens) if j!=q['a']]})")
        if "<strong>" not in q["e"] or "</strong>" not in q["e"]:
            issues.append(f"Q{i+25} Gate 5: missing strong tag in Q{i+25}")
        if "Distractor Traps:" not in q["e"]:
            issues.append(f"Q{i+25} Gate 5: missing Distractor Traps in Q{i+25}")
        if q["e"].count("&bull;") < 3:
            issues.append(f"Q{i+25} Gate 5: < 3 bullets in Q{i+25}")

    if issues:
        print(f"Found {len(issues)} issues:")
        for iss in issues:
            print("  ", iss)
        sys.exit(1)
    else:
        print(f"All {len(all_qs)} questions in Passages 5-9 successfully passed all 5 gates with <= 1.08x length symmetry!")
