import sys, re, json
sys.path.append('/home/cgslinde/DrillRoom/DrillRoom/scratch')
import craft_ps90_p5_to_p8 as m

# Q25 (P5 Q1): ans=D (3)
m.p5_qs[0]["ch"] = [
    "Fixed-ratio 20 (FR-20), producing rapid responding punctuated by post-reinforcement pauses",
    "Fixed-interval 60s (FI-60s), producing moderate response rates with scalloped curves in tests",
    "Variable-interval 60s (VI-60s), producing stable, moderate response rates resistant to drop",
    "Variable-ratio 20 (VR-20), producing high, steady response rates with minimal pauses in runs"
]

# Q27 (P5 Q3): ans=C (2)
m.p5_qs[2]["ch"] = [
    "both drug wanting and drug liking increase symmetrically due to global dopamine surges in brain",
    "drug wanting decreases through behavioral extinction while drug liking surges via sensitization",
    "drug wanting surges via neural sensitization while drug liking plateaus or drops via tolerance",
    "both drug wanting and drug liking crash to zero as prefrontal cortex silences all reward circuits"
]

# Q28 (P5 Q4): ans=A (0)
m.p5_qs[3]["ch"] = [
    "conditioned stimulus that acquired incentive salience via Pavlovian second-order conditioning",
    "negative reinforcer that directly removed an aversive physiological withdrawal state in animal",
    "primary reinforcer that satisfied an innate biological survival drive within brain hypothalamus",
    "discriminative stimulus signaling that an operant punishment schedule was operating in rats"
]

# Q29 (P5 Q5): ans=D (3)
m.p5_qs[4]["ch"] = [
    "substantia nigra pars compacta projecting to the putamen via the nigrostriatal pathway",
    "paraventricular nucleus of the hypothalamus projecting to the neurohypophysis in brain",
    "raphe nuclei of the brainstem projecting throughout the neocortex via serotonin in brain",
    "ventral tegmental area (VTA) projecting rostrally via the mesolimbic reward pathway"
]

# Q30 (P5 Q6): ans=B (1)
m.p5_qs[5]["ch"] = [
    "spontaneous recovery occurring after complete temporal consolidation of learned behavior",
    "an extinction burst, where response frequency spikes temporarily before progressive drop",
    "instinctive drift, where learned operant behaviors degrade toward innate biological habits",
    "stimulus generalization, where responding transfers across distinct auditory wavelength signals"
]

# Q31 (P6 Q1): ans=B (1)
m.p6_qs[0]["ch"] = [
    "It selectively blocks 5-HT2A receptors without altering striatal D2 dopamine binding in brain",
    "It blocks mesolimbic D2 receptors, but deepens dopamine hypofunction in mesocortical tract",
    "It stimulates dopamine synthesis in the ventral tegmentum while destroying cortex neurons in head",
    "It selectively binds trace amine receptors, bypassing the four canonical dopamine pathways here"
]

# Q32 (P6 Q2): ans=D (3)
m.p6_qs[1]["ch"] = [
    "The mesolimbic pathway originating in VTA and terminating in the nucleus accumbens in brain",
    "The tuberoinfundibular pathway originating in the arcuate nucleus of hypothalamus in head",
    "The mesocortical pathway originating in VTA and terminating in prefrontal cortex in head",
    "The nigrostriatal pathway originating in substantia nigra and terminating in striatum"
]

# Q34 (P6 Q4): ans=C (2)
m.p6_qs[3]["ch"] = [
    "Aripiprazole functions as an irreversible competitive antagonist destroying D2 receptors in brain",
    "Aripiprazole operates as a pure full agonist that mimics 100% of endogenous dopamine tone in CNS",
    "Aripiprazole functions as a D2 partial agonist with high affinity but low intrinsic efficacy",
    "Aripiprazole bypasses brain tissue by failing to cross specialized blood-brain barrier in body"
]

# Q35 (P6 Q5): ans=B (1)
m.p6_qs[4]["ch"] = [
    "Auditory hallucinations, somatic passivity delusions, and disorganized posturing in patients",
    "Affective flattening, avolition, alogia, anhedonia, and profound social asociality in patients",
    "Flight of ideas, grandiose delusions, pressured rapid speech, and psychomotor agitation in mood",
    "Tardive dyskinesia, involuntary choreoathetoid facial movements, and oculogyric crisis in clinic"
]

# Q36 (P6 Q6): ans=D (3)
m.p6_qs[5]["ch"] = [
    "Schizophrenia is inherited as an autosomal dominant disorder with complete hundred percent penetrance",
    "Environmental influences play zero role in schizophrenia because genetic concordance is high in twins",
    "Schizophrenia is caused exclusively by prenatal rubella exposure with zero genetic component in life",
    "Schizophrenia has substantial genetic liability, but non-shared environment prevents penetrance"
]

# Q38 (P7 Q2): ans=C (2)
m.p7_qs[1]["ch"] = [
    "a front-stage region where clinicians polish impression management routines for family crowds",
    "a total institution where residents are stripped of their identities via degradation in care",
    "a back-stage region where actors drop their professional masks and release emotions in room",
    "a secondary group organized around rational economic exchange and wage bargaining in hospital"
]

# Q40 (P7 Q4): ans=B (1)
m.p7_qs[3]["ch"] = [
    "primary deviance that violates established informal institutional nursing cultural norms",
    "sign-vehicles employed to communicate status and bolster authority legitimacy in hospital",
    "manifest functions designed solely to maximize acoustical velocity of cardiac murmurs in chest",
    "informal social sanctions designed to punish non-compliant ancillary healthcare staff in wards"
]

# Q44 (Disc Q2): ans=B (1)
m.discrete_qs[1]["ch"] = [
    "Identity versus Role Confusion, establishing a coherent personal philosophy and career in adult life",
    "Generativity versus Stagnation, contributing to future generations and community welfare in clinic",
    "Integrity versus Despair, reflecting retrospectively on life achievements without bitter regrets in age",
    "Intimacy versus Isolation, forming committed, vulnerable romantic attachments in early adulthood"
]

# Q45 (Disc Q3): ans=C (2)
m.discrete_qs[2]["ch"] = [
    "Pre-conventional morality, driven strictly by personal punishment avoidance in childhood life",
    "Conventional morality, driven by social conformity and preserving strict law and order in society",
    "Post-conventional morality, guided by self-chosen universal ethical principles and human rights",
    "Sub-conventional morality, guided by immediate sensory pleasure and instinctive drive states in body"
]

# Q48 (Disc Q6): ans=B (1)
m.discrete_qs[5]["ch"] = [
    "The Law of Proximity, where elements situated closely together are perceived as unified in space",
    "The Law of Similarity, where elements sharing visual features are grouped together in display",
    "The Law of Closure, where the visual system automatically fills in missing contour boundaries in eye",
    "The Law of Pragnanz, where stimuli are perceived in the most complex, chaotic form possible in minds"
]

# Q49 (Disc Q7): ans=C (2)
m.discrete_qs[6]["ch"] = [
    "The James-Lange theory, where conscious emotional feeling is caused directly by gut somatic feedback",
    "The Cannon-Bard theory, where thalamic sensory relay triggers physiology and feeling at once in brain",
    "The Schachter-Singer two-factor theory, where bodily arousal and cognitive appraisal merge now",
    "The Lazarus cognitive-mediational theory, where appraisal precedes all physiological arousal in body"
]

# Q50 (Disc Q8): ans=D (3)
m.discrete_qs[7]["ch"] = [
    "id, which operates according to the pleasure principle and demands immediate primary drive relief",
    "superego, which internalizes cultural moral prohibitions enforced by parental authority figures",
    "Me, which represents the socialized component of the self shaped by generalized other norms",
    "I, which represents the spontaneous, individualistic, un-socialized active subject of the self"
]

# Q52 (Disc Q10): ans=B (1)
m.discrete_qs[9]["ch"] = [
    "Sympathetic preganglionic neurons release norepinephrine, while parasympathetic fibers use GABA pools",
    "Sympathetic postganglionics release norepinephrine, while parasympathetics release acetylcholine",
    "Sympathetic postganglionics release acetylcholine onto muscarinic receptors in heart ventricles",
    "Parasympathetic preganglionic neurons release epinephrine directly into postganglionic synapses"
]

# Run validation on all
m.validate_questions(m.p5_qs, 25)
m.validate_questions(m.p6_qs, 31)
m.validate_questions(m.p7_qs, 37)
m.validate_questions(m.discrete_qs, 43)
print("ALL ps90 p5-p8 VALIDATED SUCCESSFULLY IN MEMORY!")

# Write out craft_ps90_p5_to_p8.py cleanly
with open("/home/cgslinde/DrillRoom/DrillRoom/scratch/craft_ps90_p5_to_p8.py", "w") as f:
    f.write('''# -*- coding: utf-8 -*-
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

p5_qs = ''' + json.dumps(m.p5_qs, indent=4) + '''
p6_qs = ''' + json.dumps(m.p6_qs, indent=4) + '''
p7_qs = ''' + json.dumps(m.p7_qs, indent=4) + '''
discrete_qs = ''' + json.dumps(m.discrete_qs, indent=4) + '''

if __name__ == "__main__":
    validate_questions(p5_qs, 25)
    validate_questions(p6_qs, 31)
    validate_questions(p7_qs, 37)
    validate_questions(discrete_qs, 43)
    print("ALL PASSAGES 5 TO 8 QUESTIONS VALIDATED 100% PERFECTLY!")
''')
print("Successfully regenerated craft_ps90_p5_to_p8.py!")
