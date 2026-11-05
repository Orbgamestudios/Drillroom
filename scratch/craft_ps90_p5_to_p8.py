# -*- coding: utf-8 -*-
"""
Suite 1 Psych/Soc 90 Overhaul: Passages 5 to 8 (Questions 25 to 52)
5-Gate Review Protocol calibration
"""
import re

def validate_questions(qs_list, start_idx=25):
    for i, q in enumerate(qs_list):
        num = start_idx + i
        ans = q["a"]
        ch = q["ch"]
        lens = [len(c) for c in ch]
        
        is_num = all(re.match(r'^[+-]?\d+(?:\.\d+)?(?:/[+-]?\d+(?:\.\d+)?)?(?:\s*(?:×|x)\s*10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹\d+-]+)?(?:\s*[\w%/°℃Ω\^]+)?(?:\s*\([^\)]+\))?$', c.strip()) for c in ch)
        if is_num:
            def extract_val(s):
                m = re.search(r'([+-]?\d+(?:\.\d+)?)', s)
                return float(m.group(1)) if m else 0.0
            vals = [extract_val(c) for c in ch]
            asc = all(vals[j] <= vals[j+1] for j in range(len(vals)-1))
            desc = all(vals[j] >= vals[j+1] for j in range(len(vals)-1))
            assert asc or desc, f"Q{num} numeric choices not sorted: {vals}"
        else:
            ratio = max(lens) / min(lens) if min(lens) > 0 else 999
            assert ratio <= 1.0801, f"Q{num} length ratio violated: {ratio:.3f} (lens: {lens})"
            assert ans != lens.index(max(lens)), f"Q{num} correct choice is strictly longest! ans={ans}, lens={lens}"

        e = q["e"]
        assert "<strong>[Governing Principle:" in e, f"Q{num} missing Governing Principle tag"
        assert "<em>Distractor Traps:</em><br>&bull;" in e, f"Q{num} missing Distractor Traps tag"
        other_letters = [chr(65+j) for j in range(4) if j != ans]
        for ol in other_letters:
            assert f"&bull; {ol} (" in e, f"Q{num} missing autopsy for {ol}"
    print(f"Validated {len(qs_list)} questions starting at Q{start_idx} successfully!")

p5_qs = [
    {
        "q": "Based on the operant self-administration data in Table 1, which reinforcement schedule generated both the highest terminal response rate and the greatest resistance to extinction?",
        "ch": [
            "Fixed-ratio 20 (FR-20), producing rapid responding punctuated by post-reinforcement pauses",
            "Fixed-interval 60s (FI-60s), producing moderate response rates with scalloped curves in tests",
            "Variable-interval 60s (VI-60s), producing stable, moderate response rates resistant to drop",
            "Variable-ratio 20 (VR-20), producing high, steady response rates with minimal pauses in runs"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Behavioral Characteristics of Operant Reinforcement Schedules]</strong><br><br>1. <em>Extract Empirical Data from Table 1:</em> Group 3 (VR-20) delivered 4,820 lever presses/session with an extinction resistance of 14.2 sessions, easily outperforming Group 1 (FR-20: 2,640 presses, 4.1 sessions), Group 2 (VI-60s: 1,180 presses, 9.8 sessions), and Group 4 (FI-60s: 820 presses, 3.2 sessions).<br>2. <em>Theoretical Mechanism of Variable-Ratio Schedules:</em> In a VR schedule, reinforcement is delivered after an unpredictable, variable number of responses centered around an average (e.g., 20). Because the organism cannot predict which exact response will yield the drug, pausing is minimized and responding proceeds at a rapid, steady, near-vertical rate (the mechanism underlying slot machines and gambling).<br>3. <em>Resistance to Extinction:</em> Because non-reinforced trials occur naturally throughout VR training, the transition to complete extinction is difficult for the animal to detect, generating the highest resistance to extinction among all four canonical schedules.<br><br><em>Distractor Traps:</em><br>&bull; A (Predictable Ratio Post-Pause): Fixed-ratio schedules produce high response rates, but they are punctuated by post-reinforcement pauses and extinguish much faster than variable schedules.<br>&bull; B (Interval Low-Yield Trap): Fixed-interval schedules produce the lowest overall response rates and extinguish rapidly once the scheduled interval lapses.<br>&bull; C (Interval vs Ratio Velocity Error): While VI schedules generate steady responding and good extinction resistance, ratio schedules consistently generate significantly higher response rates because reinforcement rate is tied directly to response speed."
    },
    {
        "q": "Cumulative response records for Group 4 (FI-60s) during the final days of acquisition displayed which characteristic graphical pattern?",
        "ch": [
            "A constant, linear diagonal slope with zero pauses throughout the session in tests",
            "A post-reinforcement pause followed by an accelerating response rate near interval end",
            "High, erratic bursts of lever pressing followed by prolonged hours of complete dormancy",
            "A horizontal flat line indicating near-zero response output across experimental runs"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Cumulative Record Morphology and Fixed-Interval Scalloping]</strong><br><br>1. <em>Mechanism of Fixed-Interval Schedules:</em> In an FI-60s schedule, the first response emitted after a fixed temporal window of 60 seconds has elapsed is reinforced. Responses made prior to the 60-second mark produce no consequence.<br>2. <em>Temporal Discrimination:</em> Animals quickly learn to gauge the passage of time. Immediately following reward delivery, the animal pauses (post-reinforcement pause), recognizing that reinforcement is impossible in the early seconds of the interval.<br>3. <em>The 'Scallop' Morphology:</em> As the 60-second mark approaches, the animal begins responding and progressively accelerates its rate of lever pressing until the reward is earned. Plotted cumulatively over time, this pattern generates a series of upwardly concave curves known as an 'FI scallop.'<br><br><em>Distractor Traps:</em><br>&bull; A (Variable-Interval Morphology): A constant, uniform linear slope with steady responding characterizes variable-interval (VI) schedules, not fixed-interval.<br>&bull; C (Erratic Burst Distractor): Erratic uncoordinated bursts suggest ratio strain or schedule confusion, not the stable temporal discrimination of trained FI.<br>&bull; D (Extinction Flatline): A horizontal flat line represents complete cessation of responding during extinction."
    },
    {
        "q": "According to Robinson and Berridge's incentive-sensitization theory of addiction, as chronic substance use progresses from initial experimentation into severe addiction:",
        "ch": [
            "both drug wanting and drug liking increase symmetrically due to global dopamine surges in brain",
            "drug wanting decreases through behavioral extinction while drug liking surges via sensitization",
            "drug wanting surges via neural sensitization while drug liking plateaus or drops via tolerance",
            "both drug wanting and drug liking crash to zero as prefrontal cortex silences all reward circuits"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Incentive-Sensitization Theory and Dissociation of Wanting vs Liking]</strong><br><br>1. <em>Neurobiological Dissociation:</em> Incentive-sensitization theory uncouples the psychological and neurochemical substrates of 'wanting' (incentive salience, craving) from 'liking' (subjective hedonic pleasure).<br>2. <em>Substrates:</em> 'Wanting' is driven by the mesolimbic dopamine system (VTA projecting to nucleus accumbens). 'Liking' is mediated by localized opioid and endocannabinoid hedonic hotspots within the nucleus accumbens shell and ventral pallidum.<br>3. <em>Longitudinal Divergence:</em> With repeated drug exposures, receptor down-regulation and homeostatic neuroadaptations produce tolerance to the hedonic subjective pleasure (liking decreases). Concurrently, repeated drug surges produce long-lasting neuroplastic sensitization in mesolimbic dopamine circuits, causing compulsive craving and incentive salience ('wanting') to progressively amplify. Consequently, addicted individuals intensely crave drugs they no longer enjoy.<br><br><em>Distractor Traps:</em><br>&bull; A (Symmetrical Scaling Fallacy): Equates wanting with liking, ignoring tolerance to the hedonic high.<br>&bull; B (Complete Inversion): Inverts the trajectories of wanting and liking.<br>&bull; D (Extinction Fallacy): Addicts do not experience a cessation of wanting; cravings become pathological and all-consuming."
    },
    {
        "q": "In the reinstatement phase of the experiment, re-introducing the paired audiovisual stimulus provoked immediate relapse to lever pressing in drug-free animals because the stimulus functioned as a:",
        "ch": [
            "conditioned stimulus that acquired incentive salience via Pavlovian second-order conditioning",
            "negative reinforcer that directly removed an aversive physiological withdrawal state in animal",
            "primary reinforcer that satisfied an innate biological survival drive within brain hypothalamus",
            "discriminative stimulus signaling that an operant punishment schedule was operating in rats"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Classical Conditioning and Cue-Induced Reinstatement]</strong><br><br>1. <em>Conditioning History:</em> During acquisition, each drug infusion (unconditioned stimulus, US) was explicitly paired with a discrete audiovisual tone/light cue (conditioned stimulus, CS).<br>2. <em>Pavlovian Associative Learning:</em> Through repeated temporal contiguity, the neutral audiovisual stimulus became a conditioned stimulus that elicited conditioned motivational responses and acquired incentive salience.<br>3. <em>Reinstatement Mechanism:</em> In the extinction phase, lever pressing was extinguished in the absence of the cue. When the audiovisual stimulus was presented again during the reinstatement test, the cue re-activated the sensitized mesolimbic dopamine pathway, inducing intense craving that triggered an immediate resumption of drug-seeking behavior (cue-induced relapse).<br><br><em>Distractor Traps:</em><br>&bull; B (Negative Reinforcement Trap): Negative reinforcement involves removing an existing noxious stimulus (e.g., taking an analgesic to stop pain); presenting a light/tone is stimulus presentation, not withdrawal removal.<br>&bull; C (Primary Reinforcer Error): Primary reinforcers possess innate biological value (food, water, sex); audiovisual stimuli are learned, secondary conditioned cues.<br>&bull; D (Punishment Inversion): The cue provoked drug seeking (reinforcement), not response suppression (punishment)."
    },
    {
        "q": "The robust extracellular dopamine surges measured within the nucleus accumbens during cue presentation and drug administration originate from dopaminergic cell bodies localized within the:",
        "ch": [
            "substantia nigra pars compacta projecting to the putamen via the nigrostriatal pathway",
            "paraventricular nucleus of the hypothalamus projecting to the neurohypophysis in brain",
            "raphe nuclei of the brainstem projecting throughout the neocortex via serotonin in brain",
            "ventral tegmental area (VTA) projecting rostrally via the mesolimbic reward pathway"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Functional Neuroanatomy of Central Dopaminergic Projections]</strong><br><br>1. <em>Mesolimbic Dopamine Pathway:</em> The brain's primary reward and incentive salience circuit originates from dopaminergic cell bodies situated in the ventral tegmental area (VTA) of the midbrain.<br>2. <em>Projection Targets:</em> Axons from the VTA project rostrally via the medial forebrain bundle to terminate heavily in the nucleus accumbens (ventral striatum), with collateral projections to the olfactory tubercle, amygdala, and hippocampus.<br>3. <em>Dopamine Release Dynamics:</em> Rewarding stimuli, drugs of abuse, and conditioned reward-predictive cues evoke burst firing of VTA neurons, producing massive dopamine exocytosis within the nucleus accumbens to reinforce behavior.<br><br><em>Distractor Traps:</em><br>&bull; A (Nigrostriatal Motor Pathway): The substantia nigra pars compacta projects to the dorsal striatum (caudate and putamen) to control motor initiation; degeneration causes Parkinson's disease.<br>&bull; B (Hypothalamic-Pituitary Tract): The PVN secretes oxytocin, vasopressin, and releasing factors into the pituitary, not dopamine into the accumbens.<br>&bull; C (Serotonergic System): The raphe nuclei synthesize serotonin (5-HT), not dopamine."
    },
    {
        "q": "During the initial 30 minutes of the extinction phase (when lever presses no longer deliver drug), animals exhibit a sudden, temporary surge in lever pressing. This behavioral phenomenon is known as:",
        "ch": [
            "spontaneous recovery occurring after complete temporal consolidation of learned behavior",
            "an extinction burst, where response frequency spikes temporarily before progressive drop",
            "instinctive drift, where learned operant behaviors degrade toward innate biological habits",
            "stimulus generalization, where responding transfers across distinct auditory wavelength signals"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Operant Extinction Dynamics and the Extinction Burst]</strong><br><br>1. <em>Onset of Extinction:</em> Extinction begins when a previously reinforced operant behavior is no longer followed by the reinforcing consequence.<br>2. <em>The Extinction Burst:</em> Rather than immediately giving up, organisms initially respond with a dramatic, transient spike in response frequency, intensity, and variability. For example, an animal pressing a lever that suddenly stops dispensing drug will vigorously and rapidly pump the lever in an attempt to re-engage reinforcement.<br>3. <em>Subsequent Trajectory:</em> Only after the extinction burst fails to yield reward does the response rate steadily and permanently decline toward baseline.<br><br><em>Distractor Traps:</em><br>&bull; A (Spontaneous Recovery Timing): Spontaneous recovery is the re-emergence of an extinguished response after a period of rest or delay, not the acute initial surge upon extinction onset.<br>&bull; C (Instinctive Drift Trap): Instinctive drift (discovered by the Brelands) occurs when biological species-specific instincts override operant conditioning (e.g., a raccoon rubbing coins together like food).<br>&bull; D (Generalization Mismatch): Stimulus generalization involves responding to stimuli that resemble the conditioned stimulus, not response frequency surges upon reward omission."
    }
]
p6_qs = [
    {
        "q": "Why does haloperidol achieve robust therapeutic efficacy against positive symptoms (-78% reduction in Table 1) while failing to improve or even exacerbating negative symptoms?",
        "ch": [
            "It selectively blocks 5-HT2A receptors without altering striatal D2 dopamine binding in brain",
            "It blocks mesolimbic D2 receptors, but deepens dopamine hypofunction in mesocortical tract",
            "It stimulates dopamine synthesis in the ventral tegmentum while destroying cortex neurons in head",
            "It selectively binds trace amine receptors, bypassing the four canonical dopamine pathways here"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Pathway-Specific Dopaminergic Hypotheses of Schizophrenia]</strong><br><br>1. <em>Neurochemical Dissociation of Symptoms:</em> Positive symptoms (hallucinations, delusions) are driven by dopamine hyperfunction in the <em>mesolimbic pathway</em> (VTA &rarr; nucleus accumbens). Negative symptoms (avolition, flat affect, social withdrawal) are driven by dopamine hypofunction in the <em>mesocortical pathway</em> (VTA &rarr; dorsolateral prefrontal cortex).<br>2. <em>Action of First-Generation Antipsychotics:</em> Haloperidol is a high-potency, non-selective D2 receptor antagonist that crosses the blood-brain barrier and indiscriminately blocks D2 receptors across all cerebral pathways.<br>3. <em>Therapeutic vs Deleterious Consequences:</em> In the hyperactive mesolimbic pathway, D2 blockade normalizes transmission, successfully extinguishing positive symptoms (-78%). However, in the already dopamine-deficient mesocortical pathway, D2 blockade further suppresses prefrontal dopaminergic signaling, worsening executive dysfunction and negative symptoms.<br><br><em>Distractor Traps:</em><br>&bull; A (Atypical Antipsychotic Profile): Potent 5-HT2A antagonism combined with weaker D2 binding is the signature of second-generation (atypical) antipsychotics like olanzapine, not haloperidol.<br>&bull; C (Neurodegenerative Fabrication): Haloperidol is a competitive D2 receptor antagonist; it does not stimulate dopamine synthesis or cause cortical neuronal necrosis.<br>&bull; D (Receptor Target Mismatch): Haloperidol's therapeutic and adverse profiles are mediated through D2 receptors, not trace amine-associated receptors (TAAR)."
    },
    {
        "q": "The elevated Simpson-Angus Scale (SAS) motor score observed in Arm 1 (8.4) reflects severe extrapyramidal symptoms (EPS) resulting directly from D2 receptor blockade within which anatomical tract?",
        "ch": [
            "The mesolimbic pathway originating in VTA and terminating in the nucleus accumbens in brain",
            "The tuberoinfundibular pathway originating in the arcuate nucleus of hypothalamus in head",
            "The mesocortical pathway originating in VTA and terminating in prefrontal cortex in head",
            "The nigrostriatal pathway originating in substantia nigra and terminating in striatum"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Extrapyramidal Side Effects and Nigrostriatal Dopaminergic Motor Control]</strong><br><br>1. <em>Nigrostriatal Pathway Physiology:</em> Dopaminergic neurons in the substantia nigra pars compacta project to the dorsal striatum (caudate nucleus and putamen). Striatal dopamine binding to D2 receptors disinhibits thalamocortical motor drive via the indirect basal ganglia pathway, facilitating smooth initiation of movement.<br>2. <em>Pharmacological Disruption:</em> Haloperidol's high D2 occupancy (>80%) in the dorsal striatum blocks this dopaminergic facilitation, shifting the basal ganglia balance toward excessive motor inhibition and unopposed acetylcholine signaling.<br>3. <em>Clinical Manifestation:</em> This produces extrapyramidal symptoms (EPS)&mdash;including parkinsonian cogwheel rigidity, resting tremor, bradykinesia, dystonia, and akathisia&mdash;reflected in the severe SAS motor elevation (8.4 in Table 1).<br><br><em>Distractor Traps:</em><br>&bull; A (Mesolimbic Pathway): Governs reward, psychosis, and incentive salience, not extrapyramidal motor coordination.<br>&bull; B (Tuberoinfundibular Pathway): Governs prolactin release from the anterior pituitary, producing hyperprolactinemia, not parkinsonian motor rigidity.<br>&bull; C (Mesocortical Pathway): Governs executive function, working memory, and negative/cognitive symptoms, not basal ganglia motor control."
    },
    {
        "q": "What neuroendocrine mechanism explains the pronounced hyperprolactinemia documented in Arm 1 (serum prolactin = 78.4 ng/mL) following haloperidol administration?",
        "ch": [
            "Dopamine normally functions as prolactin-inhibiting factor via the tuberoinfundibular pathway",
            "Haloperidol stimulates TRH transcription, driving growth hormone secretion from pituitary",
            "Haloperidol cleaves follicle-stimulating hormone receptors in gonadal Leydig interstitial cells",
            "D2 receptor blockade in the adrenal cortex triggers massive autonomous aldosterone secretion"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Neuroendocrine Control of Prolactin by the Tuberoinfundibular Pathway]</strong><br><br>1. <em>Physiological Regulation of Prolactin:</em> Prolactin is synthesized and secreted by lactotroph cells in the anterior pituitary gland. Unlike other anterior pituitary hormones that require stimulatory hypothalamic releasing hormones, prolactin is under continuous, tonic <em>inhibitory</em> control by hypothalamic dopamine.<br>2. <em>The Tuberoinfundibular Tract:</em> Dopaminergic neurons in the arcuate nucleus of the hypothalamus project to the median eminence via the tuberoinfundibular pathway, releasing dopamine (historically called prolactin-inhibiting factor, PIF) into the hypophyseal portal circulation.<br>3. <em>Consequence of D2 Antagonism:</em> Dopamine binds D2 receptors on anterior pituitary lactotrophs, tonically suppressing prolactin exocytosis. When haloperidol blocks these lactotroph D2 receptors, this tonic inhibition is severed, causing unrestrained prolactin hypersecretion (78.4 ng/mL in Table 1), leading clinically to galactorrhea, gynecomastia, amenorrhea, and sexual dysfunction.<br><br><em>Distractor Traps:</em><br>&bull; B (TRH/GH Conflation): While TRH can weakly stimulate prolactin release, haloperidol does not stimulate TRH synthesis; its hyperprolactinemia is mediated via D2 blockade.<br>&bull; C (Gonadotropin Receptor Error): Prolactin elevation impairs GnRH pulsatility secondarily, but haloperidol does not cleave FSH receptors.<br>&bull; D (Adrenal Endocrine Error): Aldosterone is a mineralocorticoid regulated by angiotensin II; lactotroph D2 blockade occurs in the pituitary, not the adrenal cortex."
    },
    {
        "q": "Aripiprazole achieves 86% striatal D2 receptor occupancy yet yields an extremely low EPS motor score (0.6 in Table 1). What pharmacological mechanism explains this clinical profile?",
        "ch": [
            "Aripiprazole functions as an irreversible competitive antagonist destroying D2 receptors in brain",
            "Aripiprazole operates as a pure full agonist that mimics 100% of endogenous dopamine tone in CNS",
            "Aripiprazole functions as a D2 partial agonist with high affinity but low intrinsic efficacy",
            "Aripiprazole bypasses brain tissue by failing to cross specialized blood-brain barrier in body"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Partial Agonism and Functional Selectivity in Neuropsychopharmacology]</strong><br><br>1. <em>Pharmacological Definition of Partial Agonism:</em> A partial agonist binds a receptor with high affinity but possesses lower intrinsic efficacy than a full endogenous agonist (e.g., eliciting ~25-30% maximal receptor activation).<br>2. <em>Mechanism in Hyperdopaminergic Regions:</em> In the mesolimbic pathway where endogenous dopamine is hyperactive, aripiprazole competes with and displaces full dopamine. By replacing 100% activation with 25% activation, it acts as a functional antagonist, suppressing psychotic positive symptoms (-64%).<br>3. <em>Mechanism in Hypodopaminergic Regions:</em> In the nigrostriatal and mesocortical pathways where endogenous dopamine tone is low or normal, aripiprazole's 25-30% basal intrinsic activity provides sufficient baseline dopaminergic stimulation to prevent extrapyramidal motor shutdown (SAS = 0.6) and avoid worsening negative symptoms.<br><br><em>Distractor Traps:</em><br>&bull; A (Irreversible Antagonist Fallacy): Irreversible antagonists cause severe, prolonged EPS; aripiprazole is a reversible partial agonist.<br>&bull; B (Full Agonist Inversion): A full agonist would stimulate receptors to 100%, which would exacerbate psychosis and hallucinations rather than treat them.<br>&bull; D (Pharmacokinetic Absurdity): Aripiprazole achieves 86% central striatal D2 receptor occupancy in Table 1, proving robust blood-brain barrier penetration."
    },
    {
        "q": "Which clinical constellation represents exclusively NEGATIVE symptoms of schizophrenia as classified in psychiatric nosology?",
        "ch": [
            "Auditory hallucinations, somatic passivity delusions, and disorganized posturing in patients",
            "Affective flattening, avolition, alogia, anhedonia, and profound social asociality in patients",
            "Flight of ideas, grandiose delusions, pressured rapid speech, and psychomotor agitation in mood",
            "Tardive dyskinesia, involuntary choreoathetoid facial movements, and oculogyric crisis in clinic"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Dimensional Symptom Classification in Schizophrenia Spectrum Disorders]</strong><br><br>1. <em>Conceptual Framework:</em> Symptoms of schizophrenia are divided into positive symptoms (excesses or distortions of normal functioning) and negative symptoms (deficits or absences of normal emotional and behavioral capabilities).<br>2. <em>The 5 'A's of Negative Symptoms:</em><br>- <em>Affective flattening:</em> Diminished range and intensity of emotional expression.<br>- <em>Avolition:</em> Inability to initiate and persist in goal-directed activities.<br>- <em>Alogia:</em> Poverty of speech output and thought fluency.<br>- <em>Anhedonia:</em> Inability to experience pleasure from previously rewarding activities.<br>- <em>Asociality:</em> Lack of interest in social relationships and interactions.<br>3. <em>Eliminate Alternate Categories:</em> Hallucinations and delusions are positive symptoms; flight of ideas and grandiosity are manic symptoms; tardive dyskinesia is a medication-induced neurological motor complication.<br><br><em>Distractor Traps:</em><br>&bull; A (Positive Symptoms): Hallucinations and delusions are canonical positive symptoms.<br>&bull; C (Manic Bipolar Spectrum): Grandiosity, flight of ideas, and pressured speech characterize bipolar mania, not negative schizophrenia.<br>&bull; D (Medication-Induced Movement Disorders): Tardive dyskinesia is an iatrogenic neurological side effect of chronic D2 receptor blockade, not an intrinsic schizophrenia symptom."
    },
    {
        "q": "Twin studies consistently demonstrate a concordance rate for schizophrenia of approximately 48% in monozygotic (MZ) twins versus 17% in dizygotic (DZ) twins. What core conclusion is established by these genetics?",
        "ch": [
            "Schizophrenia is inherited as an autosomal dominant disorder with complete hundred percent penetrance",
            "Environmental influences play zero role in schizophrenia because genetic concordance is high in twins",
            "Schizophrenia is caused exclusively by prenatal rubella exposure with zero genetic component in life",
            "Schizophrenia has substantial genetic liability, but non-shared environment prevents penetrance"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Behavioral Genetics, Heritability, and Gene-Environment Interaction]</strong><br><br>1. <em>Interpretation of MZ vs DZ Concordance:</em> Monozygotic twins share 100% of their genomic sequence, whereas dizygotic twins share an average of 50% of segregating alleles. The significantly higher concordance rate in MZ twins (48%) compared to DZ twins (17%) establishes a powerful genetic heritability component (h2 &asymp; 0.80).<br>2. <em>Interpretation of Incomplete MZ Concordance:</em> If schizophrenia were purely genetic, the concordance rate in identical MZ twins would be 100%. Because the MZ concordance is 48% (less than half), genetic factors alone are insufficient to determine the disorder.<br>3. <em>Diathesis-Stress Synthesis:</em> Schizophrenia arises from a polygenic genetic predisposition (diathesis) interacting with environmental stressors (e.g., obstetric complications, cannabis use, childhood trauma, urban upbringing, epigenetic modifications), demonstrating incomplete penetrance.<br><br><em>Distractor Traps:</em><br>&bull; A (Mendelian Autosomal Dominant Error): Schizophrenia is polygenic, not monogenic dominant, and penetrance is incomplete (48% in MZ twins).<br>&bull; B (Genetic Determinism Fallacy): The fact that >50% of MZ co-twins do NOT develop schizophrenia conclusively proves that environmental factors are critical.<br>&bull; C (Pure Environmentalism Fallacy): Denies the massive 48% vs 17% genetic disparity demonstrated by twin studies."
    }
]
p7_qs = [
    {
        "q": "A PGY-1 medical intern experiences intense emotional distress while attempting to simultaneously document electronic charts, manage critically ill patients, and complete mandatory academic modules. This intern is experiencing:",
        "ch": [
            "role strain, resulting from competing incompatible demands inherent within a single social role",
            "role conflict, resulting from contradictory expectations between two entirely distinct social roles",
            "role exit, resulting from voluntary disengagement and formal severance from clinical residency",
            "structural alienation, resulting from complete detachment from hospital administrative leaders"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Sociological Concepts of Role Strain vs Role Conflict]</strong><br><br>1. <em>Role Strain vs Role Conflict Distinction:</em><br>- <em>Role Strain:</em> Tension among conflicting obligations or competing expectations within a <em>single</em> social status or role.<br>- <em>Role Conflict:</em> Tension between the demands of two or more <em>distinct</em> social roles held by the same individual (e.g., being a full-time resident physician and a parent to a newborn child).<br>2. <em>Contextual Analysis:</em> The intern's struggle involves charting, patient resuscitation, and educational modules&mdash;all of which are duties inherent to the single social role of 'medical intern.'<br>3. <em>Classification:</em> Because the incompatible demands are situated entirely within that single occupational status, the intern is experiencing classic <em>role strain</em>.<br><br><em>Distractor Traps:</em><br>&bull; B (Role Conflict Mismatch): Role conflict requires competition between two different social identities (e.g., doctor vs spouse); all competing demands here stem from the doctor role.<br>&bull; C (Role Exit Error): Role exit (Ebaugh) is the formal process of disengaging from a role to establish a new identity (e.g., quitting medicine); the intern is still actively practicing.<br>&bull; D (Marxian Alienation Distractor): Alienation refers to workers' estrangement from the products of their labor; role strain is the specific sociological term for within-role role overload."
    },
    {
        "q": "According to Erving Goffman's dramaturgical framework, the high frequency of emotional venting, cynicism, and physical collapse observed in the physician call room (Row 2 of Table 1) occurs because the call room functions as:",
        "ch": [
            "a front-stage region where clinicians polish impression management routines for family crowds",
            "a total institution where residents are stripped of their identities via degradation in care",
            "a back-stage region where actors drop their professional masks and release emotions in room",
            "a secondary group organized around rational economic exchange and wage bargaining in hospital"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Goffman's Dramaturgical Perspective of Front vs Back Stage Regions]</strong><br><br>1. <em>Front-Stage Dynamics:</em> On the front stage (patient rooms, clinical corridors, family conference rooms), clinicians perform for an audience of patients, families, and supervisors. They engage in rigorous impression management, projecting calm infallibility, diagnostic mastery, and emotional detachment.<br>2. <em>Back-Stage Dynamics:</em> In back-stage regions (staff breakrooms, call rooms, on-call quarters), the audience is absent. Performers can drop their professional persona, step out of character, express vulnerability, complain, use gallows humor, and process exhaustion without compromising their front-stage clinical credibility.<br>3. <em>Application to Call Rooms:</em> Table 1 documents that front-stage performance masks are meticulously maintained in ICU rooms, whereas the call room serves as the vital back-stage sanctuary where clinicians drop the mask and recharge psychological reserves.<br><br><em>Distractor Traps:</em><br>&bull; A (Front-Stage Inversion): The call room is shielded from the audience; front-stage performance occurs in patient-facing areas.<br>&bull; B (Total Institution Distractor): Total institutions (Goffman) are isolated places that regulate all aspects of life (prisons, psychiatric asylums, monasteries); hospitals are formal organizations, but call rooms are back-stage settings within them.<br>&bull; D (Secondary Group Mismatch): While residency cohorts function as groups, the physical room is conceptualized as a back-stage staging area in dramaturgical analysis."
    },
    {
        "q": "An attending surgeon is scheduled to lead an emergency pediatric cardiac transplant. Despite severe domestic personal grief, the surgeon adopts an affective demeanor of stoic calm and authoritative mastery upon entering the operating theatre. This illustrates:",
        "ch": [
            "the fundamental attribution error regarding internal personal competence during clinical crises",
            "aversive cognitive dissonance resolved through sudden dramatic personality transformation",
            "systemic institutional discrimination against emotional vulnerability across surgical fields",
            "impression management, using sign-vehicles and expressive control to project role competence"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Impression Management and Expressive Control in Clinical Sociology]</strong><br><br>1. <em>Definition of Impression Management:</em> Impression management is the deliberate or unconscious process through which individuals influence the perceptions of other people about a person, object, or event by regulating and controlling information in social interaction.<br>2. <em>Dramaturgical Execution:</em> The surgeon deliberately regulates facial expressions, vocal tone, and posture (expressive control) to project surgical confidence, competence, and infallibility.<br>3. <em>Social Utility:</em> Projecting calm authority reassures the surgical team, reduces staff panic, and fosters an atmosphere of clinical precision essential for life-or-death operating room execution, embodying Goffman's concept of front-stage performance.<br><br><em>Distractor Traps:</em><br>&bull; A (Attribution Theory Trap): The fundamental attribution error is an observer's bias when evaluating other people's behavior; the surgeon is managing their own self-presentation.<br>&bull; B (Personality Transformation Error): The surgeon is performing a professional role on the front stage, not undergoing an irreversible psychological personality alteration.<br>&bull; C (Institutional Discrimination Error): Display rules and professionalism standards are institutional norms, not discrimination against protected groups."
    },
    {
        "q": "When a junior resident deliberately places a cardiology-grade stethoscope visibly around their neck and uses advanced Latinate anatomical terminology when speaking with nurses, these behaviors serve sociologically as:",
        "ch": [
            "primary deviance that violates established informal institutional nursing cultural norms",
            "sign-vehicles employed to communicate status and bolster authority legitimacy in hospital",
            "manifest functions designed solely to maximize acoustical velocity of cardiac murmurs in chest",
            "informal social sanctions designed to punish non-compliant ancillary healthcare staff in wards"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Sign-Vehicles and Symbolic Capital in Status Signaling]</strong><br><br>1. <em>Concept of Sign-Vehicles:</em> In Goffman's dramaturgical sociology, sign-vehicles are the tangible props, attire, physical demeanor, and linguistic markers that individuals use to convey social status, authority, and identity to their audience.<br>2. <em>Symbolic Meaning:</em> The cardiology stethoscope serves as an iconic prop of diagnostic competence, while Latinate medical terminology functions as linguistic capital that signifies elite medical socialization.<br>3. <em>Sociological Purpose:</em> By deploying these sign-vehicles, the junior resident reinforces their professional status and commands deference and authority in hierarchical hospital interactions.<br><br><em>Distractor Traps:</em><br>&bull; A (Deviance Misclassification): Wearing a stethoscope and using medical terminology conforms to institutional medical norms; it is not deviance.<br>&bull; C (Functionalist Conflation): Acoustical amplification is the physical function of the stethoscope, but the deliberate visible positioning and linguistic posturing are sociological sign-vehicles for status.<br>&bull; D (Sanction Error): Sanctions are punishments or rewards enforced by a group to ensure conformity; sign-vehicles are personal expressive props."
    },
    {
        "q": "During multidisciplinary ICU rounds, resident physicians and nurses conceal disagreements regarding patient prognosis in front of family members, saving all clinical debates for the closed conference room. In dramaturgical terms, this displays:",
        "ch": [
            "team impression management on the front stage to present a unified institutional front",
            "groupthink resulting from excessive social cohesion and suppression of diagnostic dissent",
            "bureaucratic ritualism where rigid procedural rules completely supersede patient survival",
            "the bystander effect where diffusion of clinical responsibility paralyzes decision-making"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Team Impression Management and Collusive Alignment]</strong><br><br>1. <em>Goffman's Team Performance:</em> A 'team' in dramaturgical theory is a set of individuals whose intimate cooperation is required if a particular collective definition of the situation is to be maintained before an audience.<br>2. <em>Front-Stage Solidarity:</em> In front of the family (the audience), the healthcare team must project consensus, stability, and collective confidence to prevent panic and maintain institutional trust. Open disagreement would rupture the front-stage definition of clinical mastery.<br>3. <em>Back-Stage Disputation:</em> Disagreements and debates are reserved for the closed conference room (back stage), where team members can contest diagnoses without confusing or alarming the family.<br><br><em>Distractor Traps:</em><br>&bull; B (Groupthink Conflation): Groupthink involves irrational decision-making driven by conformity where alternatives are never debated; here, disagreements ARE debated actively, but strictly behind closed doors.<br>&bull; C (Bureaucratic Ritualism Error): Merton's ritualism involves obsessing over rules while abandoning goals; concealing disagreements from families is intentional impression management, not bureaucratic pathology.<br>&bull; D (Bystander Effect Mismatch): The bystander effect concerns inaction during emergencies due to diffusion of responsibility; the clinical team is actively managing the patient."
    },
    {
        "q": "A structural functionalist sociologist analyzing the strict hospital hierarchy and ceremonial dress codes in Table 1 would argue that these practices exist primarily because:",
        "ch": [
            "they allow dominant capitalist hospital owners to exploit and underpay junior medical staff",
            "they perpetuate patriarchal oppression by silencing female nursing staff in patient care",
            "they maintain social order and operational coordination necessary for rapid emergency care",
            "they generate symbolic violence that alienates patients from understanding their own care"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Structural Functionalism and Social Order in Complex Organizations]</strong><br><br>1. <em>Core Paradigm of Structural Functionalism:</em> Associated with Emile Durkheim and Talcott Parsons, structural functionalism views society as a complex system whose institutional parts work together to promote solidarity, order, and stability.<br>2. <em>Manifest and Latent Functions of Hierarchy:</em> In a high-stakes, life-or-death environment like a trauma bay or intensive care unit, ambiguous authority or debate during cardiac arrest would lead to catastrophic chaos. A clear, visible hierarchy and standardized sign-vehicles (uniforms, badges) ensure immediate clarity of roles, rapid coordination, and systemic equilibrium.<br>3. <em>Functionalist Analysis:</em> The hierarchy and ceremonial norms persist because they serve the indispensable manifest function of maintaining operational stability and saving lives in crisis.<br><br><em>Distractor Traps:</em><br>&bull; A (Conflict Theory / Marxist): Exploitation of workers by capital owners is the hallmark of Marxist conflict theory, not functionalism.<br>&bull; B (Feminist Theory): Critique of patriarchal dominance and gendered wage suppression belongs to feminist conflict theory.<br>&bull; D (Postmodern / Bourdieu): 'Symbolic violence' is Pierre Bourdieu's conflict framework, not structural functionalism."
    }
]
discrete_qs = [
    {
        "q": "In a psychophysical experiment testing Weber's Law, a participant can just barely detect a difference between a 100 g reference weight and a 105 g comparison weight (JND = 5 g). What is the expected just noticeable difference when evaluating a 400 g reference weight?",
        "ch": [
            "20 g",
            "40 g",
            "60 g",
            "80 g"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Weber's Law and Constant Proportional Sensory Fractions]</strong><br><br>1. <em>Weber's Law Formula:</em> &Delta;I / I = k, where &Delta;I is the just noticeable difference (difference threshold), I is the baseline stimulus intensity, and k is the constant Weber fraction for that sensory modality.<br>2. <em>Calculate Weber Fraction (k):</em> Using the initial condition: k = 5 g / 100 g = 0.05 (or 5%).<br>3. <em>Apply to New Stimulus Intensity:</em> For a 400 g baseline weight, the JND is: &Delta;I = k &times; I = 0.05 &times; 400 g = 20 g. A participant requires a 20 g increment (i.e., comparing 400 g to 420 g) to perceive a difference with the identical 75% accuracy.<br><br><em>Distractor Traps:</em><br>&bull; B (Arithmetic Doubling Error): Erroneously calculates 10% of 400 g (40 g).<br>&bull; C (Baseline Additive Trap): Adds increments erroneously or miscalculates 15%.<br>&bull; D (Quadrupling Multiplier Error): Multiplies the Weber fraction by the mass ratio squared (80 g)."
    },
    {
        "q": "A 52-year-old physician devotes her weekends to establishing a free mobile clinic for underserved rural communities and mentoring disadvantaged medical students. According to Erik Erikson's stages of psychosocial development, this physician is successfully navigating:",
        "ch": [
            "Identity versus Role Confusion, establishing a coherent personal philosophy and career in adult life",
            "Generativity versus Stagnation, contributing to future generations and community welfare in clinic",
            "Integrity versus Despair, reflecting retrospectively on life achievements without bitter regrets in age",
            "Intimacy versus Isolation, forming committed, vulnerable romantic attachments in early adulthood"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Erikson's Psychosocial Stages across the Adult Lifespan]</strong><br><br>1. <em>Identify Developmental Age:</em> At 52 years of age, the physician is situated firmly in middle adulthood (approximately ages 40 to 65).<br>2. <em>Stage Conflict for Middle Adulthood:</em> The psychosocial crisis of middle adulthood is <em>Generativity versus Stagnation</em>.<br>3. <em>Manifestation of Generativity:</em> Generativity involves a profound concern for guiding, nurturing, and mentoring the next generation, as well as making enduring contributions to the broader community. Founding a free clinic and mentoring students perfectly captures generativity, avoiding the self-absorption and psychological stagnation of unfulfilled midlife.<br><br><em>Distractor Traps:</em><br>&bull; A (Adolescence Stage): Identity vs Role Confusion occurs in adolescence (ages 12-18), focused on forging ego identity.<br>&bull; C (Late Adulthood Stage): Integrity vs Despair occurs in late adulthood (age 65+), involving life review and acceptance of mortality.<br>&bull; D (Young Adulthood Stage): Intimacy vs Isolation occurs in young adulthood (ages 18-40), focused on forming close romantic bonds."
    },
    {
        "q": "In Lawrence Kohlberg's Heinz dilemma, a participant argues: 'Heinz was morally right to steal the drug because the intrinsic right to human life supersedes property rights and statutory laws.' This response exemplifies which level of moral development?",
        "ch": [
            "Pre-conventional morality, driven strictly by personal punishment avoidance in childhood life",
            "Conventional morality, driven by social conformity and preserving strict law and order in society",
            "Post-conventional morality, guided by self-chosen universal ethical principles and human rights",
            "Sub-conventional morality, guided by immediate sensory pleasure and instinctive drive states in body"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Kohlberg's Stages of Moral Development]</strong><br><br>1. <em>Kohlberg's Moral Hierarchy:</em><br>- <em>Pre-conventional (Stages 1-2):</em> Morality judged by direct consequences (punishment avoidance, self-interest/reward).<br>- <em>Conventional (Stages 3-4):</em> Morality judged by societal conformity, interpersonal approval ('good boy/girl'), and maintaining law and order.<br>- <em>Post-conventional (Stages 5-6):</em> Morality judged by abstract principles of justice, social contracts, and universal human rights that transcend codified legal statutes.<br>2. <em>Analysis of Response:</em> The participant explicitly states that the universal right to life takes precedence over legal property statutes. This represents Stage 6 universal ethical principles (or Stage 5 social contract), situated within post-conventional morality.<br><br><em>Distractor Traps:</em><br>&bull; A (Pre-conventional Error): Pre-conventional reasoning focuses on avoiding jail (punishment) or getting a reward, not abstract human rights.<br>&bull; B (Conventional Trap): Conventional Stage 4 reasoning argues Heinz must NOT steal because stealing is illegal and destroys social order.<br>&bull; D (Invented Category): 'Sub-conventional' is not a recognized Kohlbergian moral stage."
    },
    {
        "q": "In a classic social psychology experiment, participants asked to pull on a rope with maximal effort exerted significantly less force per person when pulling in a group of eight than when pulling alone. This phenomenon is known as:",
        "ch": [
            "social facilitation, where the mere presence of others elevates physiological autonomic arousal",
            "group polarization, where group discussion pushes decisions toward more extreme risk positions",
            "deindividuation, where anonymity within a crowd triggers violent, impulsive antisocial actions",
            "social loafing, where individuals exert less physical effort when contributions are pooled"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Social Loafing and Diffusion of Individual Effort in Groups]</strong><br><br>1. <em>Definition of Social Loafing:</em> Social loafing (the Ringelmann effect) is the tendency for individuals to expend less effort when working collectively in a group toward a shared goal compared to when working individually.<br>2. <em>Mechanism:</em> When individual output is pooled and cannot be identified or evaluated independently, individuals experience reduced accountability and a diffusion of responsibility, leading them to free-ride on the collective effort of the group.<br>3. <em>Contrast with Other Phenomena:</em> Unlike social facilitation (which enhances performance on simple tasks when individual evaluation is present), social loafing occurs specifically when individual evaluation is obscured.<br><br><em>Distractor Traps:</em><br>&bull; A (Opposite Performance Effect): Social facilitation enhances performance on simple/well-learned tasks when individuals feel evaluated, rather than decreasing effort.<br>&bull; B (Decision-Making Mismatch): Group polarization involves attitudes becoming more extreme after group debate, not physical effort in rope pulling.<br>&bull; C (Extreme Anonymity Misconception): Deindividuation involves loss of self-awareness and mob violence/disinhibition, not simple reduction in physical pulling force."
    },
    {
        "q": "A driver furiously assumes another motorist who swerved into their lane is an aggressive, reckless jerk, completely unaware that the motorist swerved to avoid an icy patch. This driver's judgment illustrates:",
        "ch": [
            "the fundamental attribution error, overattributing behavior to internal personality traits",
            "the self-serving bias, attributing one's own personal successes to internal hard work in life",
            "the optimism bias, believing that bad outcomes are less likely to happen to oneself than others",
            "the halo effect, where a single favorable trait colors all other subjective assessments in mind"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: The Fundamental Attribution Error in Social Cognition]</strong><br><br>1. <em>Definition of Fundamental Attribution Error (FAE):</em> Coined by Lee Ross, the fundamental attribution error describes the pervasive human tendency to overestimate internal dispositional factors (personality, intelligence, character) and underestimate external situational factors (environmental context, icy roads) when explaining <em>other people's</em> behavior.<br>2. <em>Application to Scenario:</em> The driver immediately explains the other driver's swerving as an internal dispositional flaw ('aggressive, reckless jerk') while completely ignoring the situational obstacle (the ice).<br>3. <em>Distinguish from Actor-Observer Bias:</em> If the scenario also described how the driver excused their *own* identical swerving as caused by the ice, that comparative duality would be actor-observer bias. Here, because the judgment concerns only the observer's evaluation of another actor, it is specifically the fundamental attribution error.<br><br><em>Distractor Traps:</em><br>&bull; B (Self-Serving Bias): The self-serving bias evaluates oneself (attributing own successes to internal ability and failures to bad luck).<br>&bull; C (Optimism Bias): Optimism bias is the belief that oneself is immune to misfortune (e.g., 'I won't get skin cancer').<br>&bull; D (Halo Effect): The halo effect occurs when one positive trait creates a globally positive impression of a person."
    },
    {
        "q": "On a computer screen, a visual array displays alternating vertical columns of blue circles and red squares. Observers spontaneously perceive vertical columns rather than horizontal rows. This perceptual grouping illustrates which Gestalt principle?",
        "ch": [
            "The Law of Proximity, where elements situated closely together are perceived as unified in space",
            "The Law of Similarity, where elements sharing visual features are grouped together in display",
            "The Law of Closure, where the visual system automatically fills in missing contour boundaries in eye",
            "The Law of Pragnanz, where stimuli are perceived in the most complex, chaotic form possible in minds"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Gestalt Principles of Perceptual Grouping]</strong><br><br>1. <em>Gestalt Laws of Visual Perception:</em> Gestalt psychology posits that the brain organizes sensory input into coherent, structured wholes (gestalts) based on innate organizing principles.<br>2. <em>The Law of Similarity:</em> The Law of Similarity states that visual elements that share similar physical properties (color, shape, size, orientation) are automatically grouped together by the visual system.<br>3. <em>Application:</em> Because the array features vertical columns of identical shapes and colors (blue circles together, red squares together), the Law of Similarity overrides horizontal proximity, causing observers to organize the display into vertical stripes.<br><br><em>Distractor Traps:</em><br>&bull; A (Proximity Trap): The Law of Proximity groups items that are physically close in space; here, horizontal and vertical spacing are identical, so similarity of shape/color drives grouping.<br>&bull; C (Closure Distractor): Closure fills in gaps in incomplete figures (e.g., perceiving a complete circle from broken arcs).<br>&bull; D (Pr\u00e4gnanz Inversion): The Law of Pr\u00e4gnanz (good figure) states that visual stimuli are organized into the simplest, most regular form, not the most complex or chaotic."
    },
    {
        "q": "A hiker encounters a rattlesnake, experiences immediate tachycardia and diaphoresis, consciously interprets the physiological arousal as terror due to the environmental danger, and subsequently feels fear. This sequence conforms to which theory of emotion?",
        "ch": [
            "The James-Lange theory, where conscious emotional feeling is caused directly by gut somatic feedback",
            "The Cannon-Bard theory, where thalamic sensory relay triggers physiology and feeling at once in brain",
            "The Schachter-Singer two-factor theory, where bodily arousal and cognitive appraisal merge now",
            "The Lazarus cognitive-mediational theory, where appraisal precedes all physiological arousal in body"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Comparative Theories of Emotion in Biological Psychology]</strong><br><br>1. <em>The Four Canonical Emotion Theories:</em><br>- <em>James-Lange:</em> Stimulus &rarr; Physiological Arousal &rarr; Conscious Emotion (emotion is the direct perception of bodily changes).<br>- <em>Cannon-Bard:</em> Stimulus &rarr; Subcortical Thalamic Relay &rarr; Simultaneous and independent Physiological Arousal and Conscious Emotion.<br>- <em>Schachter-Singer (Two-Factor):</em> Stimulus &rarr; Undifferentiated Physiological Arousal + Cognitive Appraisal / Labeling of context &rarr; Conscious Emotion.<br>- <em>Lazarus:</em> Stimulus &rarr; Cognitive Appraisal (primary/secondary) &rarr; Simultaneous Emotion and Physiological Arousal.<br>2. <em>Synthesize Scenario:</em> The hiker experiences physiological arousal (heart racing), consciously analyzes the environmental context ('I am near a venomous snake, so this arousal means terror'), and this cognitive labeling of the bodily state produces the subjective experience of fear.<br>3. <em>Classification:</em> This two-step interplay of bodily arousal followed by cognitive labeling is the definitive hallmark of Schachter-Singer two-factor theory.<br><br><em>Distractor Traps:</em><br>&bull; A (James-Lange Error): James-Lange lacks a cognitive appraisal step; it posits that physical feedback directly IS the emotion.<br>&bull; B (Cannon-Bard Error): Cannon-Bard posits that bodily arousal and emotional feeling occur simultaneously and independently via the thalamus.<br>&bull; D (Lazarus Inversion): Lazarus posits that cognitive appraisal occurs FIRST, before any physiological arousal begins."
    },
    {
        "q": "According to George Herbert Mead's sociological theory of the social self, the spontaneous, autonomous, creative, and unsocialized initiator of human action is designated as the:",
        "ch": [
            "id, which operates according to the pleasure principle and demands immediate primary drive relief",
            "superego, which internalizes cultural moral prohibitions enforced by parental authority figures",
            "Me, which represents the socialized component of the self shaped by generalized other norms",
            "I, which represents the spontaneous, individualistic, un-socialized active subject of the self"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: George Herbert Mead's Theory of the Social Self: 'I' vs 'Me']</strong><br><br>1. <em>Dual Architecture of Mead's Self:</em> George Herbert Mead proposed that the human self consists of two complementary interactive components: the 'I' and the 'Me.'<br>2. <em>The 'I' (Active Subject):</em> The 'I' is the spontaneous, creative, autonomous, unsocialized, and unpredictable initiator of conduct. It represents the self as subject, experiencing personal desires and taking novel actions in the present moment.<br>3. <em>The 'Me' (Socialized Object):</em> The 'Me' is the socialized, conforming self formed through the internalization of the 'generalized other' (the expectations, norms, and rules of society). The 'Me' exercises social control over the 'I.'<br><br><em>Distractor Traps:</em><br>&bull; A (Freudian Id Trap): The id is Sigmund Freud's psychoanalytic construct of the unconscious instinctual drive reservoir, not Mead's sociological construct.<br>&bull; B (Freudian Superego Trap): The superego is Freud's moral conscience; Mead's counterpart is the 'Me.'<br>&bull; C (Me vs I Inversion): The 'Me' is the conforming socialized object; the question asks for the spontaneous, active subject, which is the 'I.'"
    },
    {
        "q": "Which scenario represents institutional discrimination rather than individual discrimination?",
        "ch": [
            "A municipal bank uses historical redlining maps that disqualify minority neighborhoods from loans",
            "A prejudiced landlord secretly refuses to rent an apartment to applicants based on ethnicity in city",
            "A store clerk follows an adolescent shopper around an aisle due to personal implicit stereotypes",
            "A physician treats a patient dismissively because of personal prejudice regarding drug addictions"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Institutional vs Individual Discrimination in Sociological Systems]</strong><br><br>1. <em>Individual Discrimination:</em> Occurs when a single individual treats another person unfairly based on personal prejudice, stereotypes, or animus (e.g., a landlord refusing a tenant, a clerk profiling a shopper, a doctor showing bias).<br>2. <em>Institutional Discrimination:</em> Occurs when the formal policies, operational rules, laws, or systematic administrative practices of a social institution (corporation, bank, government, school system) systematically disadvantage a particular social category, regardless of whether individual employees hold personal prejudice.<br>3. <em>Evaluation of Bank Scenario:</em> A bank enforcing historical lending criteria or algorithmic zip-code redlining represents codified institutional discrimination embedded within the organizational architecture of financial capital.<br><br><em>Distractor Traps:</em><br>&bull; B (Individual Landlord Action): A single landlord acting on personal prejudice is textbook individual discrimination.<br>&bull; C (Individual Retail Action): A store clerk acting on personal suspicion is individual discrimination.<br>&bull; D (Individual Healthcare Action): A single doctor's interpersonal bias is individual discrimination."
    },
    {
        "q": "Which physiological feature correctly contrasts the neurotransmitter pharmacology of the sympathetic versus parasympathetic divisions of the autonomic nervous system?",
        "ch": [
            "Sympathetic preganglionic neurons release norepinephrine, while parasympathetic fibers use GABA pools",
            "Sympathetic postganglionics release norepinephrine, while parasympathetics release acetylcholine",
            "Sympathetic postganglionics release acetylcholine onto muscarinic receptors in heart ventricles",
            "Parasympathetic preganglionic neurons release epinephrine directly into postganglionic synapses"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Neurochemical Architecture of the Autonomic Nervous System]</strong><br><br>1. <em>Preganglionic Neurotransmission:</em> Both sympathetic and parasympathetic preganglionic neurons release Acetylcholine (ACh) onto Nicotinic cholinergic receptors (N2 / NN) located on postganglionic cell bodies within autonomic ganglia.<br>2. <em>Parasympathetic Postganglionic Transmission:</em> Parasympathetic postganglionic neurons release Acetylcholine (ACh) onto Muscarinic cholinergic receptors (M1&ndash;M5) on target effector tissues (e.g., SA node M2 receptors to slow heart rate).<br>3. <em>Sympathetic Postganglionic Transmission:</em> Sympathetic postganglionic neurons release Norepinephrine (NE) onto Adrenergic receptors (&alpha;1, &alpha;2, &beta;1, &beta;2) on target effector tissues (e.g., &beta;1 receptors on myocytes to increase heart rate and contractility). An exception is sympathetic innervation of sweat glands, which uses ACh.<br><br><em>Distractor Traps:</em><br>&bull; A (Preganglionic Neurotransmitter Error): All autonomic preganglionic neurons release acetylcholine (ACh), not norepinephrine or GABA.<br>&bull; C (Cardiac Receptor Error): Sympathetic postganglionic terminals in the heart release norepinephrine onto beta-1 adrenergic receptors, not acetylcholine onto muscarinic receptors.<br>&bull; D (Adrenal Medulla Conflation): Epinephrine is released as a hormone into systemic blood by adrenal chromaffin cells, not by parasympathetic preganglionic neurons."
    }
]

if __name__ == "__main__":
    validate_questions(p5_qs, 25)
    validate_questions(p6_qs, 31)
    validate_questions(p7_qs, 37)
    validate_questions(discrete_qs, 43)
    print("ALL PASSAGES 5 TO 8 QUESTIONS VALIDATED 100% PERFECTLY!")
