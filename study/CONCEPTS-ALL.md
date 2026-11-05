# FL1 — EVERY CONCEPT

**283 concepts.** Built from the 66 questions missed on AAMC Practice Exam 1 (503, 58th
percentile, 164/230) and the topics adjacent to them. Format governed by `../TEACH-SPEC.md`;
study method by `../PROTOCOL.md`.

Four angles on every concept, because three different representational routes into one idea is
what worked:

- **Structure** — schematic. One line, usually a table.
- **Concrete** — episodic. A situation you can picture. *(C/P computational concepts use
  **Worked example** + **Faded example** instead — backward fading, per the PROTOCOL amendment.)*
- **Claims** — propositional. What it asserts, and what it **denies**.
- **Predicts** — the forward inference. AAMC names the theory and asks you to run it.

Each cluster ends with **Discriminators** — one separating question per confusable pair, held
adjacent, never split across days — and a single-axis **Compression** table.

## How to use this

**Do not read it.** Reading is the one use that does nothing. Cover the block, say the four
angles from the concept name alone, then uncover. Closed vs open book is d = 0.46–0.50; prose vs
any prettier format is d = 0.09–0.19.

One rotation through all of it, not topic blocks — deck size *is* the spacing parameter (massed
26% vs long spacing 75% at one week). Retire a concept only after a **cold-start** success in a
later session, never on two right in a row in one sitting.

| section | concepts | |
|---|---|---|
| **PSYCHOLOGY / SOCIOLOGY** | 180 | 19 misses · ~40% of remaining time · biggest pool, closed vocabulary |
| **PHYSICS** | 36 | worst discipline at 57% · small pool but it is a floor |
| **GENERAL & ORGANIC CHEMISTRY** | 32 | gen chem is 30% of C/P — the largest single discipline on the exam |
| **CARS** | 14 | not content — a rejection grammar and seven stem families |
| **BIOLOGY / BIOCHEMISTRY** | 21 | 84th percentile already · maintenance only, do not overspend here |

*697 tables. Generated 2026-09-05 by `tools/stitch_concepts.py` from the five source documents — edit those, not this.*


---

# PSYCHOLOGY / SOCIOLOGY

## CONCEPTS — Psych/Soc
**FL1: 125 · 44th percentile · 40/59. Skill 1 (Knowledge) 55% — the worst cell on the exam.
Skill 3 90%, Skill 4 100%.** You reason fine. You do not have the words.

Nineteen misses, clustered by content category, not by passage or position. A bounded
vocabulary problem; the seven clusters below are the whole of it.

### How to use this

The skill is **discrimination, not recognition.** AAMC names the theory in the stem, asks
what it predicts, and builds the wrong answers from the term's three nearest neighbours.

Run every **Discriminator** both ways: scenario → term, then term → a scenario tempting to
call its neighbour. One direction alone produces a learner who recognizes X and also calls Y
"X." Every concept ends in **Predicts** — the form the question takes.

---

### THE NEGATIVE-STEM PROCEDURE — run this before everything else

**56% on NOT / LEAST / EXCEPT items against 71% overall. Four of the nineteen P/S misses were
negative-stem: Q201 (LEAST likely), Q206 (does NOT identify), Q209 (all of the following
EXCEPT), and one more.** Stem processing, not knowledge — a procedure, fixable in a week.

**Why it fails.** "Which is LEAST likely" makes you hold *not likely* while judging *is this
likely*, four times over — and the better you know the topic, the harder each true statement
pulls. Recognizing "yes, that IS an effect of gentrification" feels like finding the answer.
On a negative stem, recognition is the trap.

**All four steps before you read a single option.**

1. **Find the marker.** NOT · LEAST · EXCEPT · ALL OF THE FOLLOWING · WOULD NOT ·
   INCONSISTENT WITH. Mark it on the screen.
2. **Rewrite the stem positive.** "Which effect is LEAST likely with gentrification?" →
   "Which effects ARE likely with gentrification?"
3. **State the count: "Three of these are. One is not."** Ranking becomes verification — the
   step that stops you picking the first option you recognize as true.
4. **Score every option T/F on the positive question,** in order. Not "is this least likely" —
   only "is this likely, yes or no." The answer is the single F.

**Two come out F** → your predicate is looser than the stem's; re-read its exact noun (Q206
asked for an aspect of *assimilation*, not something true about immigration). **Zero come out
F** → too loose the other way; the key is the weakest T.

Half-knowledge is what a negative stem punishes: three true-sounding options, no clear false
one. Q201, Q206 and Q209 are taught below with their false statements attached — there, the
false statements are the answer.

---

### CLUSTER 1 — MEMORY

**FL1: Q173, Q174 · CC6B.** Both Skill 2 — you inferred because nothing was there to
retrieve.

*Shared scene:* **Maya, a nursing student. Every morning she parks in the hospital garage.
Every evening she works a list of beta-blockers: metoprolol, atenolol, propranolol.**

#### Semantic networks and spreading activation
FL1: Q173 · CC6B · Skill 2 · knowledge absent

**Structure.** Concepts are nodes, related concepts linked; activating one spreads activation
outward, pre-activating neighbours below awareness; retrieval returns the most-activated node.

**Concrete.** Maya reads *metoprolol*; activation runs to *atenolol*, *propranolol*, *-olol*,
*beta-blocker*, *blood pressure*, *asthma*. An hour later she writes the list from memory and
adds **nadolol** — never on it, one link from everything that was.

**Claims.** Organized by **semantic relatedness**, not by when or where you learned it. Denies
retrieval-as-lookup: the winning node wins on activation, not on having been presented.

**Evidence.** Study *bed, rest, pillow, night, dream* and people falsely recall *sleep* at
rates matching real list items. AAMC uses the logic without naming the paradigm.

**Predicts.** Stem names spreading activation → the error is an **intrusion of a semantically
related item never presented**: false recall or recognition of a category neighbour. Not a
blank, not transposed order, not a distortion of an item that *was* present.

#### The forgetting taxonomy — where in the pipeline it failed
FL1: Q173 · CC6B · knowledge absent

**Structure.** Encoding → storage → retrieval: three failure sites, plus two corruption errors where retrieval *succeeds* and returns the wrong thing.

| Failure | Where it acts | What happened |
|---|---|---|
| **Encoding failure** | encoding | never got in; nothing was attended |
| **Decay** | storage | trace faded with time; no competitor introduced |
| **Interference — proactive** | storage → retrieval | a competitor blocks it; old blocks new (*pro* = forward in time, old material pushing forward) |
| **Interference — retroactive** | storage → retrieval | a competitor blocks it; new blocks old |
| **Retrieval failure** | retrieval | stored and intact, inaccessible now. Tip-of-the-tongue; a cue restores it |
| **Source-monitoring error** | retrieval succeeds, returns the wrong thing | right content, wrong origin |
| **Misinformation effect** | retrieval succeeds, returns the wrong thing | post-event information rewrote the content |

**Concrete.** Maya cannot find her car. (a) On the phone walking in, never registered the level
— *encoding failure*. (b) Not parked there since June — *decay*. (c) Parked on 5 all last month,
keeps walking to 5 — *proactive interference*. (d) Tip of her tongue until she sees the stairwell
— *retrieval failure*. (e) Sure a nurse said 4; she read a sign — *source-monitoring error*.
(f) A friend says "we were on 4, right?" — *misinformation effect*.

**Claims.** Forgetting is not one process. Retrieval failure denies the storehouse view where
forgetting equals erasure: a trace can be intact and unreachable, which is why a cue restores
what a minute of effort could not.

**Predicts.** The stem's cue is **what happened in the interval.** Only time passed → decay.
Competing material learned → interference, then check direction. A cue brought it back →
retrieval failure. Never attended → encoding failure. Memory *present but wrong* → not
forgetting at all: source monitoring or misinformation.

#### Proactive interference
FL1: Q173 · CC6B · knowledge absent — Sep 5 cold: label produced inverted, stage called *encoding*

**Structure.** Two traces both got in; at retrieval the **older** one wins the cue and the newer
is blocked. *Pro-* = forward — old material pushing forward onto new.
**Concrete.** Maya parked on level 5 every day in August. It is September and her spot is on 3.
She walks to 5. She *saw* the 3 this morning and can picture the sign — but when the cue "my
level" fires, August answers first.
**Claims.** It acts at **storage and retrieval. Never at encoding.** The proof is inside the
word: interference is a competition, a competition needs two competitors, so both items must
have been encoded — if the new one never got in there is nothing to block, and the diagnosis is
encoding failure instead. Denies decay, which requires that *nothing* was learned in the interval.
**Predicts.** Stem gives an old set and a new set and tests the **new** one → proactive. Options
reading "was never encoded," "attention was divided during learning," or "the trace faded" are
each one stage or one mechanism off, and the first of those is the trap. A distinctive cue for
the new item recovers it — which would be impossible if encoding had failed.

#### Retroactive interference
FL1: Q173 · CC6B · knowledge absent

**Structure.** The same two encoded traces, reverse direction: the **newer** one wins the cue and
the older is blocked. *Retro-* = backward — new material reaching back onto old.
**Concrete.** Same garage, opposite question. By late September Maya parks on 3 without thinking
and cannot tell you which level she used in August. Level 5 was solid for a month; the new habit
overwrote *access* to it, not the trace.
**Claims.** Same stage as proactive — **storage and retrieval, not encoding** — and the same
requirement that both sets were learned. Denies erasure: hand her the August parking receipt and
level 5 comes straight back.
**Predicts.** Stem gives an old set and a new set and tests the **old** one → retroactive. Read
the direction off *what the question asks you to recall*, not off which was learned first — both
scenarios contain both sets, and the tested item is the one being blocked. Sleep or an empty
interval between learning and test **reduces** retroactive interference; more new learning in
that interval increases it.

#### Source-monitoring error
FL1: Q173 · CC6B · knowledge absent — Sep 5 cold: looped four times, never closed, produced "memory monitering"

**Structure.** A memory arrives in two parts — **content**, and a **source tag** (who said it,
where you read it, whether you did it or watched it, whether you perceived it or imagined it).
Retrieval returns the content correctly, the tag is missing or wrong, and you supply one. The
verb inside the label is *check where this came from*; the error is skipping the check.
**Concrete.** Maya is certain the charge nurse told her propranolol is dangerous in asthma. The
fact is true and she did encounter it — on the break-room poster. The content is intact; only
its origin is invented.
**Claims.** **Nothing failed.** Content was encoded, stored, and retrieved correctly; the whole
error is in attribution. Denies that this is forgetting — she has *more* available than a person
who forgot, not less. Denies misinformation: nobody fed her a false detail, she mis-filed a true
one she already had. And the label is **source**-monitoring — the thing being monitored is the
origin, not the memory.
**Predicts.** Stem describes someone confident whose **content is accurate** while the origin is
wrong → source monitoring. Same for "I'm sure I read that" about something they were told,
remembering an imagined action as performed, or producing a phrase believing it original. AAMC's
distractors here are the two stage-failures, encoding and retrieval — both wrong, because
nothing is missing.

#### Misinformation effect
FL1: Q173 · CC6B · knowledge absent

**Structure.** Information supplied **after** the event enters the memory *of* the event and is
later recalled as part of what was originally experienced. Post-event input → altered content.
**Concrete.** A classmate quizzing Maya says "the lecture said atenolol is the lipid-soluble one,
right?" It was not in the lecture and it is not true. A week later Maya recalls the lecturer
saying it, and would sit an exam on it.
**Claims.** The record is not fixed — it is edited by whatever arrives afterwards, including the
wording of a question. Denies source monitoring's signature: here the **content itself is wrong**,
and it is wrong because something outside the event supplied it. Denies that confidence tracks
accuracy — the edited memory feels exactly like the real one.
**Evidence.** People shown a filmed collision and asked how fast the cars were going when they
*smashed* rather than *hit* give higher speed estimates, and a week later falsely report broken
glass in a film that contained none. The verb in the question changed the memory.
**Predicts.** Stem contains a leading question, a co-witness's remark, or a later news report →
misinformation. One move separates it from source monitoring: **was there a post-event input
carrying the wrong detail?** Yes → misinformation. No, the detail is correct and only its origin
is misplaced → source monitoring.

#### Automatic vs effortful encoding
FL1: Q174 · CC6B · Skill 2 · knowledge absent

**Structure.** *Space, time, frequency* and well-learned material encode **without intention
and without attentional cost**; everything else needs effortful processing — rehearsal,
elaboration, deliberate strategy.

**Concrete.** No plan, no rehearsal, and Maya walks straight to her car. She also knows without
counting that she has seen *propranolol* more often than *nadolol*: frequency, free. The drug
list costs her effort on every item.

**Claims.** Location memory is **automatic and incidental**. Denies that encoding requires
intent, and denies "I wasn't trying to remember it, so it wasn't encoded" — hence reporting
*where on the page* a fact appeared.

**Predicts.** "Memory for locations" wants: encoded automatically, without effort or intention,
therefore relatively **spared under divided attention** and relatively spared in normal aging.
Any option requiring rehearsal, deliberate strategy, or conscious intent is wrong. Spatial
memory is also the hippocampus's job — see Cluster 3B.

#### The memory-type taxonomy
FL1: Q174 option set · CC6B · knowledge absent

**Structure.** Two crossing partitions — *by stage* (**sensory → short-term → long-term**) and *by access* (**explicit/declarative** vs **implicit/nondeclarative**).

| Type | Duration | Capacity | Content |
|---|---|---|---|
| **Sensory — iconic** (visual) | ~0.5 s | raw trace | unprocessed visual image |
| **Sensory — echoic** (auditory) | ~3–4 s | raw trace | unprocessed sound |
| **Short-term** | ~20–30 s without rehearsal | ~7±2 items | held passively |
| **Working memory** | while manipulation continues | limited | STM *manipulated* — phonological loop, visuospatial sketchpad, central executive. **Working memory ≠ short-term memory:** STM passively holds, working memory actively manipulates |
| **Long-term — explicit/declarative, episodic** | durable | unlimited | statable: a personally experienced event |
| **Long-term — explicit/declarative, semantic** | durable | unlimited | statable: a context-free fact |
| **Long-term — implicit/nondeclarative, procedural** | durable | unlimited | not statable: skills |
| **Long-term — implicit/nondeclarative, other** | durable | unlimited | not statable: priming, conditioned responses |

**Concrete.** Maya, one morning: the parking sign still visible half a second after she looks
away (iconic); "level three, level three" to the elevator (STM); metoprolol is a beta-blocker
(semantic); the morning she locked her keys in the car (episodic); driving home without
thinking about the clutch (procedural).

**Claims.** Denies a single unitary store. The dissociation is the argument: dense anterograde
amnesia destroys new *explicit* memory while *procedural* learning continues — the patient
improves at mirror-tracing across days and denies ever having done it.

**Predicts.** AAMC completes the taxonomy in the options — all four types offered. Sort on
content: personally experienced event → episodic; context-free fact → semantic; skill →
procedural; brief raw sensory trace → sensory. "Without awareness," "cannot verbalize," "shown
by performance rather than report" → implicit.

#### Iconic memory
FL1: Q174 option set · CC6B · knowledge absent

**Structure.** A raw, unprocessed **visual** trace of the whole field, held about **half a
second** — everything, before anything is selected.
**Concrete.** Maya glances at the level sign and turns away. For a fraction of a second the 3 is
still there, complete — and gone well before she reaches the elevator.
**Claims.** Capacity is essentially the entire display; **duration is the limit, not capacity.**
Denies that the bottleneck between seeing and remembering is how much you can take in — you take
in nearly all of it and lose almost all of it before it can be used.
**Evidence.** Cue people to report one row of a briefly flashed grid *after* the grid is gone and
they report almost any row perfectly, though from the whole grid they can name only a handful.
Everything was there; it faded during the reporting.
**Predicts.** "Approximately how long" for a visual sensory store → **under a second (~0.5 s).**
Any stem describing an image persisting after the stimulus stops, or a cue delivered after the
display ends, is iconic. If the stem's modality is sound, this row is wrong and the duration is
several times longer.

#### Echoic memory
FL1: Q174 option set · CC6B · knowledge absent

**Structure.** The same raw unprocessed trace for **sound**, held roughly **3–4 seconds** — long
enough to be replayed.
**Concrete.** The garage attendant calls "bay 3B" as Maya walks past and she is not listening.
Two seconds later she plays it back off the tail of the sound and hears it, having never attended
when it was said.
**Claims.** Modality sets the duration, and the auditory store is the long one. Denies parity with
vision, and the reason is structural: speech arrives spread out over time, so a store that faded
in half a second could not hold a spoken word long enough for it to be a word. Denies that "what
did you say?" followed by answering yourself is a failure of memory — it is the echoic store
being read.
**Predicts.** Same stem, ear instead of eye → seconds, not milliseconds. AAMC's error option pairs
the modality with the wrong duration, so answer on which sense the stem names: **iconic ≈ 0.5 s,
echoic ≈ 3–4 s.**

#### Priming — the implicit/nondeclarative "other"
FL1: Q174 option set · CC6B · knowledge absent

**Structure.** Prior exposure to a stimulus changes how a later related stimulus is processed —
faster, likelier, more available — with no awareness that the exposure is doing it. Sharing this
row: conditioned responses, also implicit, also visible only in behaviour.
**Concrete.** Maya passes a chart listing propranolol at noon. That evening, handed the fragment
PRO____, she completes it faster than ATE____ and, asked why, says it just came to mind.
**Claims.** Memory here is demonstrated by **performance, not by report.** Denies that remembering
requires knowing you remember — the category is defined by influence without recollection, which
is what *nondeclarative* means: not "hard to declare," but nothing to declare.
**Evidence.** Amnesic patients who cannot recognize a study list at all show the same
word-completion advantage from it as controls — the dissociation the container's argument rests on.
**Predicts.** Stem measures **speed, completion, or preference** rather than accuracy of recall →
implicit. Person says they do not remember while their performance says they do → priming.
Against spreading activation it is *effect vs mechanism*: if the item asks what the facilitation
**is called**, priming; if it asks what **causes** it, spreading activation.

#### Depth of processing and rehearsal
FL1: Q174 support · CC6B

**Structure.** Retention scales with **depth of semantic processing**, not time on task; the levels-of-processing ladder runs structural (how it looks) < phonemic (how it sounds) < semantic (what it means).

| Rehearsal | Operation | Where the material lands | Depth |
|---|---|---|---|
| **Maintenance rehearsal** | repetition | holds in STM | shallow |
| **Elaborative rehearsal** | connects to existing knowledge | moves material to LTM | deep |

**Concrete.** Maya saying "metoprolol, metoprolol" for ten minutes, versus Maya noting it is
β1-selective and picturing the asthmatic patient who can therefore take it. Same ten minutes; a
week out the second wins, and not narrowly.

**Claims.** Denies that repetition is the engine of long-term memory. Time-on-task does not
predict retention; the *kind* of processing does.

**Predicts.** Of two study methods, the one connecting to prior knowledge wins on delayed
recall. On a serial-position curve a filled delay wipes out the **recency** end (STM) and leaves
**primacy** intact (LTM). Study/test mismatch → a decrement: context-dependent (external
environment) and state-dependent (mood, intoxication) memory.

**Discriminators**
- **Decay vs interference** — was a competing item introduced, or did only time pass?
- **Proactive vs retroactive interference** — is OLD blocking NEW, or NEW blocking OLD?
- **Encoding failure vs retrieval failure** — was it ever attended to?
- **Source-monitoring error vs misinformation effect** — right content with wrong origin, or
  content altered by later information?
- **Priming vs spreading activation** — the *effect* of prior exposure, or the *mechanism*?
- **Episodic vs semantic** — did you personally experience it, or do you just know it?
- **Short-term vs working memory** — passive holding, or active manipulation?
- **Maintenance vs elaborative rehearsal** — repeat it, or connect it?
- **Flashbulb vs eidetic** — vivid emotional event memory (often wrong), or photographic detail?
- **Anterograde vs retrograde amnesia** — cannot form new, or lost old?

**Compression — where in the pipeline the process acts**

| Process | ENCODE | STORE | RETRIEVE |
|---|---|---|---|
| Attention / divided attention | ✓ | | |
| Automatic encoding (space, time, frequency) | ✓ | | |
| Maintenance vs elaborative rehearsal | ✓ | | |
| Levels of processing | ✓ | | |
| Chunking | ✓ | | |
| Decay | | ✓ | |
| Long-term potentiation, consolidation | | ✓ | |
| Interference (pro- and retroactive) | | ✓ | ✓ |
| Retrieval cues, context/state dependence | | | ✓ |
| Tip-of-the-tongue | | | ✓ |
| Spreading activation → intrusion errors | | | ✓ |
| Recognition vs recall vs relearning | | | ✓ |
| Source monitoring, misinformation | | | ✓ |

Read the column off the stem first. The stem always names the stage.

---

### CLUSTER 2 — SENSATION

**FL1: Q182, Q183 · CC6A.** Both Skill 1, both tagged BIO. The cheapest cluster here: pure
structure-to-function lookup.

*Shared scene:* **one patient in clinic. His eyelid margins are inflamed and flaking, and a
fire alarm this morning left his ears ringing.**

#### Structure and function of the eye
FL1: Q182 · CC6A · Skill 1 · knowledge absent

**Structure.** Follow the photon: **cornea → aqueous humor → pupil → lens → vitreous humor → retina → optic nerve → optic chiasm → LGN of the thalamus → V1, occipital lobe.**

| Stop | Structure | What it does |
|---|---|---|
| 1 | **Cornea** | transparent front surface; **does most of the refraction**; avascular; the tissue in contact with the eyelid |
| 2 | **Aqueous humor** | the fluid the photon crosses next |
| 3 | **Pupil** | the aperture, sized by the **iris** |
| 4 | **Lens** | **accommodation** — the *adjustable* focus, pulled thin or fat by the ciliary muscle |
| 5 | **Vitreous humor** | the fluid of the posterior chamber |
| 6 | **Retina** | light passes *through* the ganglion and bipolar layers before reaching the photoreceptors at the back: **rods and cones → bipolar cells → ganglion cells** |
| 6a | **Optic disc** | where the nerve exits; no photoreceptors — the blind spot |
| 6b | **Fovea** | cones only, maximum acuity |
| 7 | **Optic nerve → optic chiasm** | ganglion-cell axons; nasal fibres cross at the chiasm |
| 8 | **LGN of the thalamus → V1, occipital lobe** | thalamic relay, then primary visual cortex |

**Concrete.** Flakes from the inflamed lid margin sit on the front of the eye and abrade it with
every blink. What the eyelid touches, and what gets scratched, is the **cornea** — avascular, so
it heals slowly and scars opaque. Nothing behind the pupil is reachable from an eyelid.

**Claims.** Cornea does most of the bending, lens only the variable part — denies that the lens
is the main refractive element; it is the tuner. Fixes the geometry: **outside insult → cornea
or conjunctiva; distance focus → lens or globe shape; signal → retina or beyond.**

**Predicts.** Localize by *kind* of insult and *kind* of deficit. External/physical/surface →
cornea. Cannot focus near → lens or ciliary muscle. Poor night and peripheral vision → rods.
Poor colour and fine detail → cones and fovea. Whole field lost in one eye → that optic nerve.
Matched half-field in both → behind the chiasm. Nothing on an eyelid keys to retina, optic
nerve, or lens.

*Also here:* **rods** (low light, periphery, achromatic, high sensitivity) vs **cones** (bright
light, fovea, colour, acuity). **Trichromatic theory** (three cone types, at the retina) vs
**opponent-process theory** (red–green, blue–yellow, black–white channels, *after* the retina;
explains afterimages) — not rivals, successive stages of one pathway.

#### The lens and accommodation

**Structure.** Ciliary muscle **contracts** → the suspensory zonules **slacken** → the elastic
lens springs **rounder** → refractive power rises → near objects focus. Relax the muscle and the
zonules pull taut, the lens flattens, and focus returns to distance.
**Concrete.** Hand the patient his discharge instructions. At arm's length the print is sharp;
brought to reading distance it blurs. His ciliary muscle is contracting on cue — the lens has
stiffened with age and will not round up. The motor works; the spring is gone.
**Claims.** The lens supplies only the **variable** part of the focus; the cornea did the bulk
before the light arrived. Denies the intuitive mechanics — the muscle does not pull the lens fat.
Contraction *releases* tension and lets it fatten, so near work is the **contracted** state and
distance is the resting one.
**Predicts.** "Cannot focus on near objects" → lens or ciliary apparatus; never cornea, never
retina. Paralyse the ciliary muscle with cycloplegic drops → near focus lost, distance kept. A
stem crediting the lens with most of the refraction is the distractor built off the cornea.
Nothing on an eyelid reaches this stop.

#### The retina

**Structure.** Light crosses the ganglion-cell and bipolar-cell layers first and reaches the
photoreceptors **last**, at the very back. The signal then travels back out the way the light came
in: **rods and cones → bipolar cells → ganglion cells → optic nerve.**
**Concrete.** The clinician shines an ophthalmoscope in. The beam passes through two transparent
sheets of neurons before it touches a single rod or cone, and the answer comes back out through
those same sheets to the disc.
**Claims.** The retina is wired backwards, and the backwards wiring is *why* there is a blind
spot: the ganglion axons have to gather on the inner surface and then dive through the sheet to
leave the eye. Denies that the retina is a screen an image lands on — it is three layers of
neurons that begin processing before anything reaches the brain.
**Predicts.** "Which cells transduce light" → rods and cones, never bipolar, never ganglion.
"Which cells send axons to the brain" → ganglion cells only, and a stem asking what the optic
nerve is made of wants exactly that. Damage confined to the receptor layer spares the rest of the
pathway; damage at the ganglion layer takes out everything behind it.

#### The optic disc

**Structure.** The point where ganglion axons converge and exit the eye. No photoreceptors sit
there, so anything falling on it is not seen — the blind spot.
**Concrete.** Cover one of the patient's eyes and have him fix on the wall clock. About fifteen
degrees out toward his ear there is a patch of his visual field reaching no receptor at all, and
he reports nothing missing. The field looks continuous because it is filled in.
**Claims.** A real, permanent hole in the sensory sheet that is never experienced. Denies that
perception is a readout of the receptor surface — what he sees includes territory no receptor
ever reported.
**Predicts.** "Why does the blind spot exist" → the nerve's exit point, no receptors there. "Why
is it not noticed" → filling-in from surrounding context, i.e. top-down completion, not a second
set of receptors. Run it against the fovea below: one spot with **no** receptors and one with the
**densest**, a few millimetres apart.

#### The fovea

**Structure.** A pit at the centre of the retina: **cones only, no rods**, near one-to-one wiring
onto ganglion cells, overlying neural layers swept aside so light reaches the receptors more
directly. Maximum acuity, minimum sensitivity.
**Concrete.** Same patient, same chart. He reads the smallest line only by looking straight at it.
Slide the letters ten degrees off centre and they dissolve — out there it is rods, and rods do
not resolve detail.
**Claims.** Acuity is bought with cones and one-to-one wiring; sensitivity is bought with rods and
convergence; one patch of retina cannot have both. Denies uniform resolution across the visual
field — nearly all the detail he believes he sees comes from a region about the width of a
thumbnail at arm's length, moved around by saccades.
**Predicts.** "Poor colour vision and poor fine detail" → cones and fovea. "Poor night and
peripheral vision" → rods. A dim star visible only when you look slightly away → the fovea has no
rods; that is the forward inference AAMC wants out of "cones only." Central loss vs peripheral
loss localizes on the same axis.

#### Sensory reception by hair cells — the cochlea
FL1: Q183 · CC6A · Skill 1 · knowledge absent

**Structure.** Follow the pressure wave from air to cortex; the two tested steps are 5 and 6.

| Step | Where | What happens |
|---|---|---|
| 1 | pinna → auditory canal → **tympanic membrane** | sound reaches and moves the drum |
| 2 | **ossicles** (malleus, incus, stapes) | amplify and impedance-match air to fluid |
| 3 | **oval window** | stapes drives a fluid wave into the cochlea |
| 4 | **basilar membrane** | travelling wave; its motion shears the **stereocilia** against the tectorial membrane |
| 5 | stereocilia tips | the shear **mechanically pulls open gated K⁺ channels** |
| 6 | hair cell body | **K⁺ flows IN** from the K⁺-rich endolymph → the cell **depolarizes** |
| 7 | hair cell base | voltage-gated **Ca²⁺** channels open |
| 8 | **cochlear (spiral ganglion) nerve** | neurotransmitter release onto it |
| 9 | brainstem → **medial geniculate nucleus of the thalamus** → **A1, temporal lobe** | relay, then primary auditory cortex |

**Concrete.** The alarm drives the stapes into the oval window like a piston. Cochlear fluid is
incompressible with nowhere to go, so it bulges the basilar membrane; the bulge bends the hair
bundle sideways and physically yanks a gate open — no messenger, no ligand, no binding.

**Claims.** Two things, and AAMC traps on both.
1. The gating is **mechanical** — the stimulus opens the channel by pulling on it, denying the
   default that a sensory receptor works by chemical binding.
2. The depolarizing ion is **K⁺ entering the cell**, backwards from every other cell you have
   studied. Endolymph is uniquely high in K⁺, so potassium influx, not sodium influx, is the
   depolarizing current.

**Predicts.** "Sound-induced vibrations depolarize hair cells by opening which channels?" →
**mechanically gated (stretch-activated) potassium channels.** Kill the distractors by *position
in the sequence*: voltage-gated Na⁺ = axon, downstream; ligand-gated = synapse, downstream;
**voltage-gated Ca²⁺ sits at the hair cell's own base and is the most attractive wrong answer,
genuinely there but one step too late.** Only one channel type is opened by the vibration.

*Pitch and loudness:* **place theory** — position along the basilar membrane codes frequency
(base stiff and narrow → high; apex wide and floppy → low), accounting for high pitches.
**Frequency/temporal theory** — firing rate matches the wave, accounting for low pitches, with
the volley principle covering the middle. **Loudness** = how many hair cells fire and how fast,
not which ones.

#### The ossicles and impedance matching

**Structure.** Malleus → incus → stapes, a three-bone lever between eardrum and oval window.
Their job is **impedance matching**: air moves easily and cochlear fluid does not, so pressure
that moved the drum would reflect off the fluid unless it were first concentrated.
**Concrete.** The fire alarm's energy is collected across the whole area of the patient's eardrum
and delivered onto the oval window, roughly twenty times smaller. Same force, a twentieth of the
area — pressure rises by that factor, and the fluid finally moves.
**Claims.** The gain is **geometric and mechanical** — a large area feeding a small one, plus a
small lever advantage across three bones — not amplification in any electronic sense. Denies that
the middle ear is a convenience the cochlea could do without: without it most airborne energy
reflects at the fluid boundary and never enters at all.
**Predicts.** Fault in the outer or middle ear (wax, perforated drum, fixed stapes) → the signal
never reaches the cochlea and the receptors are intact. Fault in hair cells or cochlear nerve →
transduction or transmission failed. The question is asking for **location in the chain**, not
severity. The stapes is the last mechanical stage: everything downstream of it is fluid, not air.

#### The basilar membrane

**Structure.** A tapered strip running the length of the cochlea — **narrow and stiff at the base**
by the oval window, **wide and floppy at the apex**. Each frequency peaks at one place along it,
high at the base and low at the apex, and that motion shears the stereocilia against the tectorial
membrane.
**Concrete.** The alarm is a high, piercing tone. Its travelling wave peaks within the first few
millimetres of the cochlea, right where the wave enters, and it is those basal hair cells that are
still ringing this afternoon. The apex, which handles low pitches, barely moved.
**Claims.** Frequency is coded by **place**, and place is fixed by mechanics — width and stiffness
— before any receptor is involved. Denies that hair cells distinguish pitch: they are the same
cell all along the strip, and each one reports only *that my patch moved*. The membrane does the
sorting.
**Predicts.** A loud high tone loads the base → **high frequencies are lost before low ones**,
which is the pattern after noise exposure and the pattern in aging. "Which region responds to a
100 Hz tone" → the apex. Place theory covers high pitches; firing rate (frequency/temporal theory,
volley principle in the middle) covers low ones, because no neuron fires fast enough to track a
high tone one-for-one. Loudness is *how many* cells and *how fast* — never *which*.

#### The sensory pathway template
FL1: Q182, Q183 · CC6A · knowledge absent

**Structure.** One pipeline for every modality: **stimulus → receptor → transduction into a graded receptor potential → afferent nerve → thalamic relay → primary sensory cortex → association cortex.**

| Modality | Receptor class | Relay | Cortex |
|---|---|---|---|
| Vision | **photoreceptors** (rods, cones) | LGN | occipital |
| Hearing, balance | **mechanoreceptors** (cochlear and vestibular hair cells) | MGN | temporal |
| Touch / pain | mechanoreceptors (Pacinian corpuscles, proprioceptors), **thermoreceptors**, **nociceptors** | VPN | postcentral gyrus, parietal |
| Taste | **chemoreceptors** (taste buds) | thalamus | gustatory cortex |
| Smell | chemoreceptors (olfactory cells) | **none — olfaction bypasses the thalamus entirely** | olfactory bulb → piriform cortex and limbic structures directly |

**Smell is the exception**, which is why smell hooks emotion and memory so hard.

**Concrete.** One patient, two complaints. What reaches his thalamus from the scratched cornea
and what reaches it from the ringing ear are indistinguishable trains of action potentials —
LGN for one, MGN for the other. Swap the wires and he would see the alarm.

**Claims.** The signal does not carry the modality — every modality is the same action
potential, carried by **which line it arrives on** (labelled lines). Denies that anything about
the impulse in the optic nerve is "visual."

**Predicts.** "Which structure transduces X" → the receptor, never the nerve, never the cortex.
A lesion → a modality-specific deficit localizing to a pathway stage. Smell → do not route
through the thalamus. Constant unchanging stimulus → **sensory adaptation** at the receptor,
not attention.

#### Nociceptors and pain perception

**Structure.** Free nerve endings responding to tissue-damaging stimuli — mechanical, thermal,
chemical — running the standard template: receptor → afferent → thalamus (VPN) → postcentral
gyrus. What is different sits downstream: the signal is **modulated** before it becomes pain.
**Concrete.** Grit from the patient's flaking lid margin scrapes the cornea with every blink. The
corneal nociceptors do not quieten the way his skin quietens into his shirt — the damage is still
there and so is the pain. He presses and rubs the lid, and while he is rubbing it eases.
**Claims.** Pain is not a straight readout of receptor firing. Large-fibre touch input and
descending signals from the brain **close a gate** on nociceptive traffic at the spinal cord, so
identical tissue damage can produce different pain. Denies the simplest form of the labelled-line
story — the line is right about *which modality*, wrong to imply intensity survives the trip
unedited. And denies that all receptors adapt: nociceptors **sensitize** instead, which is the
whole point of a damage signal.
**Predicts.** "Why does rubbing an injury help" → competing large-fibre input closing the gate;
not distraction, not endorphins alone. Constant unchanging *pressure* that stops being felt →
sensory adaptation at a mechanoreceptor. Constant unchanging *injury* that keeps hurting →
nociceptors, which do not adapt. Any stem where expectation, attention, or emotion changes
reported pain is asking for descending modulation — spinal cord or above, not the receptor.

#### Psychophysics — thresholds, Weber, and signal detection
FL1: none missed · CC6A · included because it completes the 6A option pool

**Structure.** Two thresholds, one law, and one theory that splits detection into ability and willingness.

| Term | What it is |
|---|---|
| **Absolute threshold** | smallest stimulus detectable 50% of the time |
| **Difference threshold (JND)** | smallest detectable *change* |
| **Weber's law** | the JND is a constant *proportion* of the standard, not a constant amount |
| **Signal detection theory** | detection under noise, split into sensitivity and criterion |
| **Sensitivity (d′)** | how well you tell signal from noise |
| **Response criterion (bias)** | how willing you are to say "yes" |

Signal detection's 2×2 — signal present/absent × response yes/no:

| | Response "yes" | Response "no" |
|---|---|---|
| **Signal present** | **hit** | **miss** |
| **Signal absent** | **false alarm** | **correct rejection** |

**Concrete.** Asked whether he hears a tone: move the patient to a quiet room and *sensitivity*
improves; tell him a missed tone means another hour of testing and his *criterion* shifts —
more hits and more false alarms, no change in his ears.

**Claims.** Detection is a decision, not a measurement. Denies a fixed threshold: one ear
yields different "thresholds" under different payoffs, expectations, motivation.

**Predicts.** Hits AND false alarms moving the same direction → the **criterion** moved. Hits up
while false alarms down → **sensitivity** improved. Motivation, payoff, expectation move the
criterion; the stimulus, the noise, or the observer's ability move d′.

#### Absolute threshold

**Structure.** Position 1 on the axis that orders this whole cluster — *how much of the intensity
scale the claim is about.* Absolute threshold is a single **point**: the smallest intensity
detected **50% of the time**, with nothing to compare it against.
**Concrete.** Audiometry on the patient whose ears are ringing. The tone steps down until he stops
raising his hand, then back up until he starts again, and the level written down is the one he
catches on half the trials — not the quietest he ever caught.
**Claims.** The 50% is definitional, not sloppy measurement. Detection near threshold is
probabilistic: there is no intensity below which he never hears and above which he always does.
Denies a hard floor — and in denying it, hands the argument to signal detection theory at the
bottom of the table.
**Predicts.** A stem asking for "the minimum stimulus that can be detected" wants the 50% criterion
in the answer. An option describing a comparison against a stimulus already present is the
difference threshold, not this. And because the criterion is probabilistic, motivation and
expectation move the measured value — which is why the last two rows exist at all.

#### Difference threshold (JND)

**Structure.** Position 2: a single **step**, taken anywhere on the scale. The smallest change
from an already-present standard that is noticed 50% of the time.
**Concrete.** Two tones for the same patient, the second slightly louder. Raise the second until
he first calls them different. That increment is the just-noticeable difference **for that
starting level.**
**Claims.** The comparison is against something already there — the entire difference from the row
above, and the reason "absolute" means *against nothing*. Denies that the JND is a fixed quantity:
it is always measured at a standard, and the standard is part of the answer.
**Predicts.** Two stimuli in the stem, asking whether a change is noticed → difference threshold.
One stimulus with nothing to compare it to → absolute. The moment the stem hands you a **starting
intensity** and asks how much must be added, it has stopped being a threshold question and become
Weber's — the next row.

#### Weber's law

**Structure.** Position 3: what happens to that step as you move **up the scale**. The JND is a
constant **proportion** of the standard, never a constant amount: **ΔI / I = k.** Bigger standard,
bigger increment, same ratio.
**Concrete.** The patient's difference threshold is taken twice. In the quiet room, against a soft
standard, a small increase is enough. Out at the nurses' station against the ward's background,
that same small increase is invisible and the increment has to grow in step with the background.
His ears did not change. The standard did.
**Claims.** Sensory discrimination is **relative** — the system reports ratios, not absolute
increments. Denies a fixed detectable step. And denies its own universality: *k* holds through the
middle of a range and breaks down at the extremes.
**Evidence.** Each sense has its own *k* — roughly 2% for lifted weight, larger for loudness and
brightness. The constant characterizes the modality; the increment does not.
**Predicts.** This is the section's only routine calculation and it always runs the same way:
solve *k* from the pair you are given, then apply it to the new standard. "A 100 g weight needs
102 g to be noticed — what does 500 g need?" → k = 0.02, so 510 g. If a stem offers a **constant
increment** across different standards, it is checking whether you will accept a violation of the
law. Do not.

#### Fechner's law
*Off-outline. Weber's law is the outline term; this is the neighbour AAMC builds Weber's
distractors from, and it is position 4 on the same axis.*

**Structure.** Add the steps up. If every JND is one equal unit of felt change, then stacking them
makes **sensation grow as the logarithm of intensity** — S = k log I. Each further multiplication
of the physical stimulus adds the same, and therefore shrinking, slice of experience.
**Concrete.** Take the alarm from one unit of intensity to ten and the patient reports a large
jump. Take it from ten to a hundred — a far larger physical change — and he reports about the same
jump again. Equal ratios, equal felt steps.
**Claims.** Fechner is Weber **integrated**: a claim about the whole scale, where Weber's is a
claim about one step of it. Denies proportionality between physical intensity and experience —
which is why the decibel scale is logarithmic. Stevens later denied Fechner in turn, arguing
sensation is a power function with a modality-specific exponent. The three are **positions on one
line**, not three interchangeable names: Weber measured the step, Fechner integrated the steps
into a scale, Stevens threw out the integration and measured the scale directly.
**Predicts.** A stem about the just-noticeable **step** → Weber. A stem about how loud or bright
something **feels** across a wide range → a compressive relation, so large physical increases give
diminishing perceptual returns. A distractor reading "sensation is proportional to intensity" is
wrong under all three laws, which makes it the safest thing on the page to eliminate.

**Discriminators**
- **Sensation vs perception** — detection and transduction, or interpretation and organization?
- **Cornea vs lens** — the fixed bulk of the refraction, or the adjustable focus?
- **Rods vs cones** — low light and periphery, or colour and acuity?
- **Trichromatic vs opponent-process** — at the retina, or after it?
- **Place vs frequency theory** — *which* fibres fire (high pitch), or *how fast* (low pitch)?
- **Mechanically gated vs voltage-gated channels** — opened by physical force, or by a change in
  membrane potential?
- **Sensory adaptation vs selective attention** — the receptor stopped responding, or the brain
  stopped selecting?
- **Absolute vs difference threshold** — smallest detectable stimulus, or smallest detectable
  change?
- **Sensitivity (d′) vs response bias** — can he tell them apart, or is he just willing to say
  yes?
- **Kinesthetic vs vestibular** — where my limbs are, or which way is up?
- **Bottom-up vs top-down processing** — driven by the stimulus, or by expectation and context?

**Compression — how far along stimulus → cortex the concept sits**

| Stage | Vision | Hearing | The concepts that live here |
|---|---|---|---|
| Optics / conduction | cornea, pupil, lens | pinna, canal, ossicles | refraction, amplification, impedance matching |
| Receptor + transduction | rods, cones | cochlear hair cells | mechanically gated K⁺ channels, photopigment bleaching, sensory adaptation, absolute threshold |
| First-order coding | bipolar, ganglion cells | spiral ganglion | opponent processing, place vs frequency coding |
| Nerve | optic nerve, chiasm | cochlear nerve | field defects localize here |
| Thalamic relay | LGN | MGN | *smell skips this step* |
| Primary cortex | V1 occipital | A1 temporal | feature detection, parallel processing |
| Association / interpretation | — | — | perception, Gestalt grouping, constancy, top-down processing, signal-detection criterion |

Every 6A question asks about one row. Find it from the stem's verb — *transduce, depolarize,
refract, relay, interpret*.

---

### CLUSTER 3 — MOTIVATION AND BIOLOGICAL BASES OF BEHAVIOR (CC7A)

**FL1: Q176, Q188, Q195, Q211, Q212 · 4/9 on CC7A · 44%.** Your most expensive category: 7A is
one of AAMC's four largest, roughly **13–14 items on a real form**. Five misses, four passages —
content, not fatigue. Two things here share no axis, so 7A is split; Q176 sits in Cluster 4 with
its passage.

*Shared scene for 3A and 3B:* **Jordan runs cross-country. A researcher straps a heart-rate and
skin-conductance monitor to him before a race and hands him a questionnaire after. Midseason,
his coach starts paying him $20 a race.**

---

#### 3A — MOTIVATION AND HOW IT GETS MEASURED

#### Intrinsic vs extrinsic motivation, and overjustification
FL1: Q212 · CC7A · Skill 2 · knowledge absent

**Structure.** Two sources of motivation and one interaction between them.

| Term | Where the reward sits | Instances |
|---|---|---|
| **Intrinsic** | the activity *is* the reward | interest, enjoyment, curiosity, mastery |
| **Extrinsic** | the reward is separable from the activity | money, grades, trophies, praise, deadlines, avoiding punishment, an audience |
| **Overjustification effect** | an extrinsic reward *displaces* the intrinsic one | reward something already done for its own sake and the external reason displaces the internal one; when the reward stops, the behaviour drops *below* its original baseline |

**Concrete.** Jordan runs because he likes running; his coach pays $20 a race and now he runs
for the money. Payments stop in October and he runs less than in August, before any money
existed. His teammate, who only ever showed up for the money, shows no drop.

**Claims.** Extrinsic reward is **not additive** with intrinsic; it substitutes. Denies the
naive incentive view that more reward yields more behaviour, and denies that motivation is a
single quantity you can top up.

**Predicts.** "Which **extrinsic** factor accounts for the difference in motivation?" → the
option naming something **outside the activity and outside the person, functioning as a reward
or consequence**: payment, grade, deadline, competition, audience, supervisor, praise, avoiding
a penalty. **Not** enjoyment, interest, curiosity, values, perceived competence, personality,
self-efficacy — intrinsic or dispositional, and one will be phrased attractively.

**The trap.** "Extrinsic" and "situational" both mean *outside the person*, and both will be in
the option set. Extrinsic requires the factor to be a **motivator** — a reward or consequence
attached to the behaviour. Weather, room temperature, task difficulty are situational, not
extrinsic. If the stem says *motivational* differences, the factor must motivate.

#### Intrinsic motivation

**Structure.** The reward has no location outside the activity — stop the activity and the
reward stops with it.
**Concrete.** August, no money anywhere in the picture: Jordan runs the Tuesday long loop
alone, unwatched, uncounted, and comes back saying it felt good. Nothing was handed to him
at the end.
**Claims.** Asserts the doing is itself the payoff — interest, curiosity, mastery, enjoyment.
Denies that behaviour requires a deliverable consequence: there is nothing to withhold, so
nothing can be withheld to stop it. Also denies that "internal" means "biological" — a drive
is internal too, and a drive is not intrinsic motivation.
**Predicts.** Strip out every external consequence and intrinsically motivated behaviour
continues at rate. On the exam an option is intrinsic only if deleting the reward would
delete the activity: enjoyment, interest, curiosity, challenge, mastery, personal values.

#### Extrinsic motivation
FL1: Q212 · CC7A · Skill 2 · knowledge absent

**Structure.** The reward is a separable object delivered *for* the behaviour — you could hand
it over with no activity happening at all.
**Concrete.** Midseason: a $20 bill in Jordan's hand in the finish chute. The bill exists
independently of the 5K; the coach could hand him $20 in the parking lot without a race
being run.
**Claims.** Asserts the motivator is a consequence attached to the behaviour from outside —
money, grades, trophies, praise, deadlines, an audience, escape from punishment. Denies that
"outside the person" is sufficient: the wind, the course profile, the temperature are all
outside Jordan and motivate nothing. Extrinsic requires reward-or-consequence, not mere
externality.
**Predicts.** "Which extrinsic factor accounts for the difference?" → the option that is both
outside the person *and* functioning as a payoff. The situational-but-not-reward option
(weather, task difficulty, time of day) is the built distractor and will read attractively.

#### Overjustification effect

**Structure.** Reward an already-intrinsic behaviour → the person re-attributes the behaviour
to the reward → withdraw the reward and behaviour falls *below* its pre-reward baseline.
**Concrete.** $20 a race from September. In October the money stops, and Jordan runs fewer
voluntary miles than he did in August, before any money existed. The teammate who only ever
came for the $20 shows no drop — he had no interest to displace.
**Claims.** Asserts extrinsic reward substitutes for intrinsic rather than adding to it.
Denies the additive incentive picture — more reward, more behaviour — and denies that the
harm is merely losing the reward: the net loss *below baseline* is the effect. Requires
pre-existing interest; with none, there is no effect at all.
**Predicts.** Look for two things: a drop below the original baseline, and an unaffected
comparison person who never had the interest. Behaviour merely returning to baseline after
reward withdrawal is ordinary extinction, not overjustification. If the stem never
establishes prior interest, overjustification is the wrong answer.

#### The four factors and the three theories of motivation
FL1: Q212 · CC7A · knowledge absent

**Structure.** AAMC's outline names exactly four factors — **instinct, arousal, drives, needs** — and three theories.

| Account | What drives the behaviour | Direction | The detail AAMC tests |
|---|---|---|---|
| **Drive-reduction** | a physiological need creates a **drive**, an aversive state of tension; behaviour reduces it | **push, from inside** | behaviour restores homeostasis |
| **Incentive** | the value of an external goal, need or no need | **pull, from outside** | works with no internal deficit at all |
| **Arousal (Yerkes–Dodson)** | an **optimal level** of arousal, not zero | toward a set-point | inverted-U: performance peaks in the middle; the optimum is **lower for difficult or novel tasks and higher for simple, well-learned ones** |
| **Need-based (Maslow)** | physiological → safety → love and belonging → **esteem** → self-actualization | up the hierarchy | lower **deficiency needs** must be reasonably met before **growth needs** are pursued. Esteem = respect, achievement, recognition; self-actualization = fulfilling one's potential |
| **Instinct** | innate, species-typical, unlearned fixed patterns | innate release | it cannot explain most human behaviour, which is why the other theories exist |

**Concrete.** Jordan eating the kitchen after a race — deficit made the drive, eating removed
it: *drive reduction*. Racing for a medal he cannot eat: *incentive*. Fastest when moderately
keyed up, falling apart before a huge crowd at conference finals where the tactics are
complicated: *arousal*, optimum shifted left because the task is hard. Quitting the month his
family loses housing: *Maslow*, safety outranking esteem.

**Claims.** Drive-reduction denies goal-pull without an internal deficit — which is why it
**fails** on curiosity, thrill-seeking, and dessert after a full meal, and why incentive theory
exists. Arousal theory denies that the target state is zero tension.

**Predicts.** Deficit → behaviour → deficit gone = **drive reduction**. No deficit, attractive
external goal = **incentive**. Best in the middle, worse at both ends = **arousal /
Yerkes–Dodson**; complex task → peak at *lower* arousal. Behaviour appearing only once a lower
need is met = **Maslow**. Innate, species-wide, no learning = **instinct**.

**One axis orders all five, and it is the only thing you need to hold: *what level of internal
tension is the behaviour aiming at?*** Instinct — the question does not apply, there is no
regulator. Drive-reduction — zero. Maslow — zero, but taken in a fixed queue, lowest unmet
first. Arousal — a nonzero middle. Incentive — no internal target at all; the pull is outside
and tension may rise.

**Yerkes–Dodson carries nothing in its name.** It does not have to: it is the account that
sits in the *middle* of this axis, and "the middle is best" is its entire content. Position
and claim are the same fact, so rebuilding the axis rebuilds the theory. The blocks below run
in axis order rather than table order for this reason.

#### Instinct

**Structure.** Position 0 — no set-point at all. An innate, species-typical, unlearned fixed
pattern; a releasing stimulus starts it and it runs to completion whether or not it helps.
**Concrete.** A stone kicks off a spike toward Jordan's eye and his hand is already up. No
deficit preceded it, no goal follows it, no coach taught it, and every runner in the pack
would do the same.
**Claims.** Asserts some behaviour is genetically pre-written and needs neither an internal
state nor a learning history. Denies that this scales to humans: it cannot explain running
for a medal, quitting the team, or dessert after a full meal — which is precisely why the
other accounts exist. Denies modifiability; a drive is learnable and adjustable, an instinct
is not.
**Predicts.** Stem markers: innate, species-typical, present from birth, no learning history,
identical across members. If the stem gives a *current bodily state* as the cause, it is
drive, not instinct.

#### Drive-reduction

**Structure.** Position 1 — set-point zero. Physiological need → drive, an aversive tension →
behaviour → tension removed → behaviour stops. Motivation is subtraction.
**Concrete.** Jordan eats the kitchen after the Saturday race, then stops mid-sandwich when
the deficit is gone. Nothing outside pulled him; any food would have served.
**Claims.** Asserts the target is zero tension and the goal object is interchangeable. Denies
that behaviour can be pulled by an attractive goal in the absence of a deficit — which is
exactly where it visibly fails: curiosity, thrill-seeking, and dessert on a full stomach
reduce nothing.
**Predicts.** Deficit → behaviour → deficit gone → behaviour stops. If the stem's person is
already satisfied and acts anyway, drive-reduction is the distractor and incentive is the key.

#### Need-based motivation (Maslow's hierarchy)

**Structure.** Position 2 — set-point still zero, but the deficits are queued: physiological →
safety → love and belonging → esteem → self-actualization, and the lowest unmet one owns the
behaviour. The bottom four are **deficiency needs** (they arise from a lack and go quiet when
filled); the top is a **growth need** (no lack, never fills).
**Concrete.** October: Jordan's family loses housing and he quits three weeks before
conference, where he was going to place. Safety is unmet, so esteem — the medal, the
recognition — stops motivating anything.
**Claims.** Asserts a fixed *priority*, not a fixed importance: unmet lower needs preempt
higher ones. Denies that growth needs behave like deficiency needs — self-actualization is
pursued at zero deficit and does not switch off on satisfaction, which is the point at which
the hierarchy stops being drive-reduction.
**Predicts.** Behaviour appearing only once a lower need is met, or vanishing when a lower one
is threatened → Maslow. Esteem vs self-actualization: recognition *from others* is esteem;
fulfilling your own potential with no audience is self-actualization.

#### Arousal theory (Yerkes–Dodson)

**Structure.** Position 3, the middle of the axis — and that position *is* the theory. The
set-point is a nonzero optimum, so performance traces an inverted U and too little arousal
hurts as much as too much. The optimum slides: **lower for difficult or novel tasks, higher
for simple, well-learned ones.**
**Concrete.** Jordan runs his best 5K moderately keyed up. At conference finals — huge crowd,
tactics he has never run before — he is far past his optimum and falls apart, at an arousal
level that would have been fine on a familiar time trial. On an easy warm-up jog he is under
his optimum and runs it sloppily.
**Claims.** Asserts organisms *seek* arousal when under-aroused, so the target is a level, not
a floor. Denies drive-reduction's zero-tension target head-on: the two make opposite
predictions about a bored, comfortable, need-free person — drive-reduction says nothing
happens, arousal theory says he goes looking for stimulation.
**Predicts.** Best in the middle, worse at both ends → arousal. Given a *hard or new* task the
peak moves left, so high arousal now hurts; given an easy or overlearned one, high arousal
still helps. The exam version holds arousal constant, varies task difficulty, and asks why
the outcomes differ.

#### Incentive theory

**Structure.** Position 4 — no internal set-point. The cause sits entirely outside, in the
value of a goal object, and it operates at zero deficit, so tension can rise in pursuit of it.
**Concrete.** Jordan sprints the last 400 for a medal he cannot eat, drink, or sleep in, on a
day nothing in his body is lacking. He crosses the line more depleted than he started — the
opposite of restoring anything.
**Claims.** Asserts pull, not push: a goal's attractiveness is sufficient and no need is
required. Denies drive-reduction's claim that every motivated act reduces a deficit — the
medal and the $20 create no deficit and remove none. Note the overlap deliberately: extrinsic
motivation is incentive theory's mechanism seen from the individual's side.
**Predicts.** No deficit plus an attractive external goal → incentive. If the goal's *value*
is manipulated and behaviour changes with it, incentive. If the stem establishes the person
was fed, rested, and safe and acted anyway, incentive.

#### Subjective vs objective measurement
FL1: Q211 · CC7A · Skill 2 · knowledge absent

**Structure.** The cut is whether the datum passes through a judgment.

| | The datum is | Instances |
|---|---|---|
| **Subjective** | a **judgment or report of an internal state** | self-report scale, questionnaire, interview, an observer's rating of how someone seems |
| **Objective** | **observable and countable without passing through anyone's judgment** | behaviour counts, latencies, physiological signals, task performance, administrative records |

**Concrete.** Motivation in Jordan, four ways. (a) He rates "how motivated do you feel, 1–7" —
**subjective**. (b) His coach rates how motivated Jordan *seems* — still **subjective**; someone
else's judgment is still a judgment. (c) Minutes trained voluntarily, unobserved —
**objective**, behavioural. (d) Heart rate at the line — **objective**, physiological, and a poor
*operationalization*, which is a separate criticism.

**Claims.** The split turns on **whether the measure passes through someone's judgment** — not
on whether it produces numbers, not on who supplies it. A 7-point Likert scale is quantitative
and subjective. Denies the conflation with reliability: subjective ≠ unreliable, objective ≠
valid.

**Predicts.** "Which assessment represents a **subjective** measure of motivation?" → the option
where a person **reports or rates a state**. Two reports → take the one reporting an *internal
state* over a *fact*. Counts, latencies, physiological traces, records are objective. Watch for
the reverse version: asks for the objective measure, offers three self-reports.

*Attached vocabulary:* self-report vs behavioural vs implicit measures; **social desirability
bias** is the standing threat to self-report; **operationalization** = how the construct was
measured *in this study*, as opposed to what it means.

**Discriminators — 3A**
- **Intrinsic vs extrinsic** — is the reward the activity itself, or separable from it?
- **Overjustification vs plain extrinsic motivation** — did an external reward *undermine*
  pre-existing interest, or was there never any interest?
- **Extrinsic vs situational** — is the outside factor a *reward*, or just an outside
  circumstance?
- **Drive-reduction vs incentive** — pushed by an internal deficit, or pulled by an external
  goal?
- **Drive vs instinct** — homeostatic and learnable, or innate and fixed?
- **Arousal theory vs drive-reduction** — an optimal *level*, or always toward zero?
- **Esteem vs self-actualization** — recognition from others, or fulfilling your own potential?
- **Deficiency vs growth needs** — does the need arise from a lack?
- **Subjective vs objective** — does the datum pass through anyone's judgment?
- **Objective vs valid** — countable without judgment, versus actually measuring the construct.

**Compression — what initiates the behaviour**

| | PUSH (internal deficit) | PULL (external goal) | SET-POINT (optimal level) |
|---|---|---|---|
| Drive-reduction | ✓ | | |
| Needs / Maslow deficiency needs | ✓ | | |
| Instinct | ✓ (innate release) | | |
| Incentive theory | | ✓ | |
| Extrinsic motivation | | ✓ | |
| Overjustification | | ✓ replaces internal | |
| Intrinsic motivation | | ✓ the activity itself | |
| Arousal / Yerkes–Dodson | | | ✓ |
| Maslow growth needs | | | ✓ (toward potential) |

One question orders the table: **does the behaviour stop when something inside is restored
(push), something outside is obtained (pull), or a level is reached (set-point)?**

---

#### 3B — BIOLOGICAL BASES OF BEHAVIOR

#### The nervous system's two different partitions
FL1: Q188 · CC7A · Skill 1 · knowledge absent

**Structure.** Three nested cuts, which AAMC's distractors mix deliberately.

| Cut | One side | The other side |
|---|---|---|
| 1 | **CNS** — brain + spinal cord | **PNS** — everything else |
| 2, inside the PNS | **somatic** — voluntary skeletal muscle, plus afferent sensory | **autonomic** — involuntary, viscera and glands |
| 3, inside the autonomic | **sympathetic** — mobilize | **parasympathetic** — conserve |

| Effector | **Sympathetic** | **Parasympathetic** (the reverse, largely via the **vagus**) |
|---|---|---|
| Heart | ↑ heart rate and contractility | ↓ heart rate |
| Airways | bronchodilation | — |
| Pupil | **pupil dilation** | pupil constriction |
| Sweat glands | **↑ sweating** — and the one exception to the rule: sympathetic postganglionic fibres to eccrine sweat glands are **cholinergic** (ACh), not adrenergic | — |
| Digestion, salivation | ↓ digestion and salivation | ↑ digestion and salivation |
| Skin and gut vessels | vasoconstriction | — |
| Liver | glycogenolysis | — |
| Adrenal medulla | releases **epinephrine** | — |

**Concrete.** Jordan on the start line: palms wet, pupils wide, mouth dry, heart at 140, stomach
shut down — each one a branch of a subdivision of a half of the nervous system.

**Claims.** "Sympathetic" is a branch of the autonomic, itself a branch of the peripheral.
Denies that CNS/PNS and somatic/autonomic are alternatives to sympathetic/parasympathetic —
**different levels of one tree**, so "central nervous system" against "sympathetic" is not a
wrong branch but a wrong partition.

**Predicts.** When options mix levels (CNS, somatic, sympathetic, parasympathetic), fix **which
partition the stem is asking about** first, then choose within it. An involuntary visceral
response eliminates two options on level alone.

**Every block below opens by naming its level, because the level is what the item tests.**
Level 1 cuts by *location* (CNS / PNS). Level 2 cuts the PNS by *what is innervated* (somatic
/ autonomic). Level 3 cuts the autonomic by *direction of effect* (sympathetic /
parasympathetic). A stem that offers terms from two levels is not asking you to pick a branch.

#### Central nervous system (CNS)

**Structure.** Level 1 of 3, cut by location: brain plus spinal cord — everything encased in
skull and vertebrae. Integration happens here; nothing leaves except as a peripheral nerve.
**Concrete.** Jordan on the start line: the decision to hold pace for the first 400, and the
reflex arc that yanks his foot off a sharp rock, both close inside the skull or the cord.
Neither the sensor in his sole nor the muscle in his calf is CNS.
**Claims.** Asserts this cut asks only *where the tissue sits*, not what the signalling does.
Denies that CNS is an alternative to "sympathetic" — a sympathetic preganglionic neuron has
its cell body in the spinal cord (CNS) and its axon in the periphery (PNS); the two cuts
slice the same neuron. Offering CNS against sympathetic is a wrong *partition*, not a wrong
branch.
**Predicts.** Fix the level before choosing. A stem naming a location (brain, cord, nerve,
ganglion) is level 1; naming voluntariness is level 2; naming mobilize/conserve is level 3.

#### Peripheral nervous system (PNS)

**Structure.** Level 1 of 3, the other side of the location cut: every neuron, axon, and
ganglion outside skull and spine — cranial and spinal nerves, sensory receptors, autonomic
ganglia.
**Concrete.** The stretch receptors in Jordan's Achilles, the motor axons running to his
quadriceps, and the ganglion chain beside his spine that will dump norepinephrine on his
heart — all PNS, on the location question alone.
**Claims.** Asserts the PNS is the *container* for both level-2 branches: somatic and
autonomic are subdivisions of it, not siblings of it. Denies that PNS means "sensory" or
"involuntary" — it carries both directions and both voluntary and involuntary traffic.
**Predicts.** Every remaining term in this concept lives inside the PNS. If the option pair is
CNS vs PNS, the stem is asking about location; when the stem is about a *response*, that pair
is usually there to absorb an unread option.

#### Somatic nervous system

**Structure.** Level 2 of 3, inside the PNS, cut by what is innervated: skeletal muscle under
voluntary control, plus the sensory afferents coming back. One motor neuron, cell body in the
CNS, no ganglion, ACh at the neuromuscular junction, always excitatory.
**Concrete.** Jordan choosing to lengthen his stride over the last 200: a single axon from
cord to quadriceps, ACh released, the fibre contracts — and he can stop it by deciding to.
**Claims.** Asserts a one-neuron, always-excitatory, voluntary path to skeletal muscle. Denies
the shorthand "somatic = motor": sensory afferents are somatic too. Denies that
somatic/autonomic is the same cut as CNS/PNS — this one asks what the *target tissue* is, not
where the neuron lives.
**Predicts.** Skeletal muscle under intentional control → somatic. If the effector named is a
gland, smooth muscle, or cardiac muscle, you are on the wrong branch of the right level.

#### Autonomic nervous system

**Structure.** Level 2 of 3, inside the PNS, the involuntary half: smooth muscle, cardiac
muscle, glands. Two neurons in series with a ganglion between them, preganglionic always ACh,
and the target can be excited *or* inhibited.
**Concrete.** While Jordan is deliberately choosing his stride, his gut motility, pupil width
and sweat rate are being set without him. He cannot will his salivary glands back on at the
line no matter how dry his mouth is.
**Claims.** Asserts the two-neuron chain and bidirectional control as the structural
signature. Denies that "involuntary" means unnoticed — he feels the dry mouth and the
pounding heart perfectly well, he simply cannot command them. Denies that autonomic is a
level-3 term: sympathetic and parasympathetic live *inside* it.
**Predicts.** A viscus or gland in the stem → autonomic, which alone kills the somatic option
and both level-1 options. Only then choose sympathetic vs parasympathetic.

#### Sympathetic division
FL1: Q188 · CC7A · Skill 1 · knowledge absent

**Structure.** Level 3 of 3, inside the autonomic: mobilize. Thoracolumbar outflow, short
preganglionic (ACh) → paravertebral chain ganglion → long postganglionic releasing
**norepinephrine**. Diffuse by construction — one preganglionic fibre reaches many ganglionic
neurons, so it fires as a system.
**Concrete.** Jordan at the gun: heart at 140, pupils wide, palms soaking the electrodes,
mouth dry, gut shut down, airways open, liver dumping glucose, adrenal medulla dumping
epinephrine into the blood — one command, eight organs.
**Claims.** Asserts a coordinated whole-body mobilization, predominantly adrenergic. Denies
being "the stress system" — that conflates it with the HPA axis, which is hormonal and about
twenty times slower. Two structural breaks in the adrenergic rule: sympathetic postganglionic
fibres to **eccrine sweat glands** release ACh, and the **adrenal medulla** has no
postganglionic fibre at all — a preganglionic fibre synapses directly onto chromaffin cells
(ACh, nicotinic), which then release epinephrine into the blood.
**Predicts.** Coordinated multi-organ mobilization → sympathetic, at level 3. If the option
set mixes CNS, somatic and sympathetic, the level question is being tested and two options
die before you read them.

#### Parasympathetic division

**Structure.** Level 3 of 3, the other side: conserve — rest and digest. Craniosacral outflow,
long preganglionic (ACh) → ganglion sitting *on or in* the target organ → very short
postganglionic releasing ACh. Discrete by construction — one fibre reaches few targets, so it
acts organ by organ.
**Concrete.** Jordan an hour later on the team bus: heart back to 55, pupils small, saliva
back, gut working on the sandwich. Not one coordinated surge — each organ came back on its
own schedule.
**Claims.** Asserts organ-specific, cholinergic, restorative control. Denies symmetry with the
sympathetic: they are not mirror images. Airways, sweat glands, most blood vessels, liver and
adrenal medulla receive sympathetic input with **no parasympathetic opposition** — which is
why a sweat gland can index one branch cleanly and the heart cannot.
**Predicts.** "The reverse of sympathetic" is right for heart, pupil, digestion and
salivation, and wrong for the unopposed effectors. Asked what parasympathetic activation does
to sweating or bronchi, the answer is *nothing*; the trap option says "decreases it."

#### The vagus nerve

**Structure.** Cranial nerve X, carrying the majority of parasympathetic outflow — heart,
lungs, and gut as far as the splenic flexure. Its tonic firing, *vagal tone*, brakes the heart
continuously.
**Concrete.** Jordan's resting heart rate of 48 is not a slow pacemaker: his sinoatrial node
would run near 100 on its own. The vagus holds it down all day. At the gun the first thing
that happens is the brake coming off, before any sympathetic surge arrives.
**Claims.** Asserts heart rate is set by two opposing inputs on the same node, one of them
tonically active. Denies that a rising heart rate means sympathetic activation — it can be
pure **vagal withdrawal** with no change in sympathetic outflow at all. This is the mechanism
behind heart rate being a contaminated index.
**Predicts.** Any measure of heart rate reports the net of two branches, never one. A stem
that says heart rate rose and asks what happened autonomically has at least two mechanistically
valid answers — expect an added discriminator, or expect the key to be a cleaner measure.

#### The eccrine sweat gland exception

**Structure.** The one place a sympathetic *postganglionic* fibre is cholinergic: it releases
ACh onto muscarinic receptors on eccrine sweat glands. Sympathetic in origin, cholinergic in
transmitter, and with no parasympathetic input whatsoever.
**Concrete.** The skin-conductance electrodes on Jordan's palm. Atropine — a muscarinic
blocker, the drug you would expect to touch only parasympathetic targets — abolishes his
palmar sweating; propranolol, a β-blocker, does not.
**Claims.** Asserts that transmitter identity and divisional identity are separate facts.
Denies the tidy rule "sympathetic = adrenergic, parasympathetic = cholinergic" as a
universal — it is a strong tendency with two named breaks, this one and the adrenal medulla.
It does *not* deny that sweating is sympathetic: the gland is sympathetically and only
sympathetically driven, which is exactly what makes it the clean index.
**Predicts.** If a stem reports a cholinergic agent increasing sweating, do not conclude
parasympathetic. And because the gland is singly innervated, a change in skin conductance has
exactly one possible source — which is what makes it rank 1 in the next concept.

#### Measuring sympathetic activation
FL1: Q188 · CC7A · Skill 1 · knowledge absent

**Structure.** The best index is an effector with **only sympathetic innervation**; ranked for AAMC's usual option pool.

| Rank | Measure | Why it reads sympathetic tone |
|---|---|---|
| 1 | **Skin conductance / galvanic skin response / electrodermal activity** | sweat glands are effectively purely sympathetic. **Cleanest single index. If it is an option, it is the answer.** |
| 2 | **Pupil diameter** | dilation is sympathetic; constriction is parasympathetic |
| 3 | **Circulating or urinary epinephrine / norepinephrine** | the sympathetic-adrenal-medullary (SAM) axis, fast, seconds to a minute |
| 4 | **Heart rate** | usable but **contaminated**: the heart is dually innervated, so a rise can be sympathetic activation *or* vagal withdrawal. It measures the net, not the branch |
| 5 | **Cortisol** | **wrong axis and wrong timescale.** HPA axis (hypothalamus CRH → anterior pituitary ACTH → adrenal cortex), peaking roughly 20 minutes after the stressor. Indexes *stress*, not *sympathetic tone* |
| 6 | **Self-reported anxiety** | not a physiological measure at all |

**Concrete.** Jordan at the start line: skin conductance spikes within seconds, pupils dilate,
heart hits 140. His cortisol peaks twenty minutes later, in the parking lot, after the race is
over.

**Claims.** Two axes leave the brain under stress, not interchangeable: **SAM, neural, seconds,
epinephrine** and **HPA, hormonal, tens of minutes, cortisol.** Denies equating "stress
response" with "sympathetic activation."

**Predicts.** "Most useful measure of **sympathetic** activation?" → skin conductance if
offered; else pupil dilation or circulating epinephrine; heart rate only if nothing cleaner is
present; **never cortisol** (wrong axis, wrong timescale); never a questionnaire. If the stem
says *stress* or *HPA*, cortisol becomes correct — the stem's noun decides.

**The rank order is derivable, not memorized. One question generates it: *how many branches
act on the effector you are measuring, and can you tell them apart?*** One branch → clean.
Two branches on separate effectors → direction disambiguates. Two branches on one effector →
you read the net, never the branch. Wrong axis entirely → not a sympathetic measure at all.

#### Skin conductance / galvanic skin response / electrodermal activity
FL1: Q188 · CC7A · Skill 1 · knowledge absent

**Structure.** Three names, one measure: a small current across two palm electrodes whose
resistance drops as eccrine sweat fills the ducts. **One branch, one effector** — sweat glands
have sympathetic innervation and no parasympathetic input, so every change has exactly one
possible cause. Onset in one to three seconds.
**Concrete.** The gun goes and Jordan's trace jumps inside two seconds, then steps up again
each time the pack surges. Nothing in his body can drive that line down except sympathetic
outflow easing off.
**Claims.** Asserts the cleanest available single index of sympathetic tone, and asserts it on
the argument from *single innervation* — not from being electrical, and not from being fast.
Denies that it measures emotion, stress, or deception: it measures sympathetic outflow, which
many states produce.
**Predicts.** If skin conductance, GSR, or electrodermal activity appears in the option set
for a *sympathetic* question, it is the answer. "Galvanic" carries no information; the fact
worth binding to the name is single innervation.

#### Pupil diameter

**Structure.** Rank 2. Dually innervated, but through *two different muscles*: sympathetic α1
contracts the radial dilator and the pupil widens; parasympathetic CN III contracts the
sphincter and it narrows. Because the branches act through separate effectors, the direction
of change names the branch.
**Concrete.** The researcher photographs Jordan's eyes at the line and again on the bus. Wide
at the line, small on the bus, and no ambiguity about which system did which.
**Claims.** Asserts that direction disambiguates a dually innervated organ *when the two
branches use separate effectors*. Denies that dual innervation automatically ruins a measure —
it ruins heart rate because both branches converge on one node, and leaves the pupil usable.
**Predicts.** Pupil *dilation* is the sympathetic answer; constriction is parasympathetic and
will be offered somewhere as though it were sympathetic. With skin conductance absent from the
options, dilation is usually the key.

#### Circulating epinephrine and norepinephrine (the SAM axis)

**Structure.** Rank 3. Sympathetic preganglionic fibres drive the adrenal medulla directly and
chromaffin cells release epinephrine into the blood: neural trigger, hormonal readout, seconds
to a minute, sampled in plasma or urine.
**Concrete.** Blood drawn from Jordan's arm at the line already carries the epinephrine spike.
The same assay run on a urine sample after the race integrates the whole hour and tells you
nothing about the start.
**Claims.** Asserts a valid sympathetic index — the same branch, one step downstream. Denies
that it is as clean in practice as skin conductance: it lags the neural signal, it is diluted
by clearance and blood volume, and the needle used to sample it drives the variable being
measured.
**Predicts.** When the stem wants a *sympathetic* measure and offers a catecholamine, take it
over heart rate and over cortisol. Epinephrine and cortisol are the pair AAMC offers together;
epinephrine is seconds and sympathetic, cortisol is tens of minutes and is not.

#### Heart rate

**Structure.** Rank 4, and contaminated for a structural reason: both branches act on the same
sinoatrial node, so a rise can be sympathetic activation, vagal withdrawal, or any mixture. It
reports the net, never the branch.
**Concrete.** Jordan's chest strap reads 140 at the gun. That number is equally compatible
with a large sympathetic surge and with the vagal brake simply coming off — the trace cannot
distinguish them.
**Claims.** Asserts heart rate is a legitimate *arousal* measure and an illegitimate *branch*
measure. Denies that faster necessarily means more sympathetic. Where the pupil escapes dual
innervation by using two muscles, the heart does not.
**Predicts.** Heart rate is the key only when nothing cleaner is offered, or when the stem
asks about arousal or exertion rather than about the sympathetic branch specifically. Placed
next to skin conductance, it is the distractor.

#### Cortisol (the HPA axis)

**Structure.** Rank 5, wrong on both axis and clock. Hypothalamic CRH → anterior pituitary
ACTH → adrenal **cortex** → cortisol, peaking roughly twenty minutes after the stressor and
staying up for hours. A hormonal cascade, not a nerve.
**Concrete.** Jordan's cortisol peaks in the parking lot twenty minutes after he finished, by
which point his skin conductance has been back at baseline for a quarter of an hour. Two
curves, two systems, one gun.
**Claims.** Asserts a slow, sustained endocrine stress response running in parallel with the
fast neural one. Denies that "stress response" and "sympathetic activation" name the same
thing — the standing conflation this whole option pool is built on. Cortex, not medulla;
ACTH, not a nerve; minutes, not seconds.
**Predicts.** Never the answer to a *sympathetic* question. Always in contention for a
*stress*, *chronic*, *HPA*, or *twenty-minutes-later* question. The stem's noun decides, and
AAMC changes the noun rather than the options.

#### Brain structures by the behaviour their damage changes
FL1: Q195 · CC7A · Skill 1 · knowledge absent

**Structure.** Indexed by deficit, not anatomy.

| Structure | The behaviour it owns | Damage → |
|---|---|---|
| **Amygdala** | fear, threat detection, emotional salience, aggression, emotional memory | blunted fear, failure to recognize threat (especially in faces), tameness |
| **Hippocampus** | consolidating **new declarative** memories; spatial memory | anterograde amnesia; old memories and skills intact |
| **Hypothalamus** | homeostasis and drives: hunger (**lateral** initiates eating; **ventromedial** signals satiety), thirst, temperature, sexual behaviour, circadian rhythm (SCN), endocrine control through the pituitary | drives unregulated — lateral lesion stops eating, ventromedial lesion never stops |
| **Thalamus** | sensory relay for every modality **except smell** | modality-general sensory loss |
| **Prefrontal cortex** | executive function, planning, working memory, impulse inhibition, personality | disinhibition, poor planning, intact intelligence with ruined judgment |
| **Basal ganglia** (with substantia nigra) | movement initiation, procedural learning, reward | nigrostriatal dopamine loss → Parkinson's |
| **Cerebellum** | balance, coordination, motor learning, timing | ataxia — cannot stay upright or time a movement |
| **Medulla** | breathing, heart rate, blood pressure | loss of vital autonomic control |
| **Pons** | sleep, arousal, respiratory relay | disrupted sleep and arousal |
| **Reticular formation** | arousal and the sleep–wake cycle | coma, disrupted sleep–wake cycle |
| **Broca's area** (frontal) | speech **production** | non-fluent aphasia, comprehension preserved |
| **Wernicke's area** (temporal) | **comprehension** | fluent but meaningless speech |
| **Limbic system** | amygdala, hippocampus, hypothalamus, cingulate cortex, septal nuclei — emotion, memory, and drive together | the component deficits above, combined |

**Concrete.** Jordan's race, taken apart by lesions. No **amygdala**: the starting gun stops
frightening him. No **hypothalamus**: he stops eating, or never stops. No **hippocampus**: he
runs the course from habit but cannot tell you afterward that he ran it. No **prefrontal
cortex**: he starts before the gun and does not care. No **cerebellum**: he cannot stay upright.

**Claims.** The real structure–function map is many-to-many; the *tested* map is one-to-one.
Use the tested one, knowing its denial: no region does one thing, and "the amygdala is the fear
centre" is a simplification AAMC still keys on.

**Predicts.** **Read the behaviour in the stem, not the structures in the options** — invert the
list. Fear → amygdala. New declarative or spatial → hippocampus. Eating, drinking, temperature,
hormones, circadian → hypothalamus. Impulse control, planning, judgment → PFC. Initiating
movement → basal ganglia. Coordination, balance → cerebellum. Vital autonomic → medulla. Sensory
relay → thalamus. Producing speech → Broca. Understanding speech → Wernicke.

#### Amygdala

**Structure.** Threat detection and emotional salience — the tag that says *this matters, and
it is dangerous*. Damage: blunted fear, failure to read threat in faces, tameness, emotional
memories that no longer feel charged.
**Concrete.** With no amygdala the starting gun does not startle Jordan. He hears it, turns
his head, and steps off the line late, because nothing in him flagged it.
**Claims.** Asserts a salience tagger sitting upstream of the autonomic and endocrine
responses. Denies being a memory-forming structure: it makes memories emotional, the
hippocampus makes them at all. Denies "the fear centre" as literally true — but that
simplification is what AAMC keys.
**Predicts.** Fear, threat, aggression, the emotional intensity of a memory, recognizing a
fearful face → amygdala. If the stem is about *retaining* what happened rather than how it
felt, switch to hippocampus.

#### Hippocampus

**Structure.** Consolidates new declarative (explicit) memories and holds spatial maps.
Damage: anterograde amnesia — old memories, skills and procedural learning intact, nothing
new stored.
**Concrete.** With no hippocampus Jordan runs the whole 5K course correctly from habit — his
legs know it — and afterwards cannot tell the researcher he raced today.
**Claims.** Asserts a consolidation gateway, not a storage vault: memories live in cortex, and
the deficit is in getting them there. Denies that declarative and procedural memory share a
route, which is why the skill survives and the fact does not.
**Predicts.** Cannot form new memories, disoriented in a new place, childhood recall intact →
hippocampus. Cannot *hold and manipulate* information over seconds → prefrontal cortex, a
different structure and a different kind of memory.

#### Hypothalamus

**Structure.** Homeostasis, drives, and the endocrine bridge: hunger (**lateral** initiates
eating, **ventromedial** terminates it), thirst, temperature, sexual behaviour, circadian
timing via the SCN, and control of the pituitary. Damage: the regulated variable runs
open-loop.
**Concrete.** Lateral lesion and Jordan will not touch the post-race food and wastes away
mid-season. Ventromedial lesion and he eats through the whole team meal and keeps going.
**Claims.** Asserts a bank of set-point controllers, each with a start and a stop. Denies
relaying sensation — that is the thalamus, one prefix away and a completely different job.
Denies being purely neural: it is the one structure here that also secretes.
**Predicts.** Eating, drinking, temperature, sex, circadian rhythm, hormone release →
hypothalamus. Derive the lesion result rather than recalling it: a lesion removes the function
the nucleus performs, so killing the initiator stops eating and killing the terminator means
eating never stops.

#### Thalamus

**Structure.** Sensory relay: every modality except smell synapses here before reaching
cortex. Damage: modality-general sensory loss, and impaired arousal, because everything routes
through one place.
**Concrete.** With no thalamus Jordan cannot see the finish banner, hear the crowd, or feel the
track under his spikes — but he can still smell the wet grass, because olfaction bypasses the
relay entirely.
**Claims.** Asserts a single obligatory waystation for sensation. Denies that smell obeys it —
the one exception, and the one AAMC asks about. Denies confusion with the hypothalamus: this
one passes information along, it does not regulate a drive.
**Predicts.** "Which structure would disrupt several senses at once" → thalamus. "Which sense
survives" → smell. A stem about hunger or temperature sitting next to a thalamus option is
testing whether you read the prefix.

#### Prefrontal cortex

**Structure.** Executive function: planning, working memory, impulse inhibition, and the
personality that rests on them. Damage: disinhibition, ruined judgment, intact measured
intelligence.
**Concrete.** With no prefrontal cortex Jordan breaks before the gun fires, goes out at a pace
he cannot hold, and when the coach pulls him he is neither embarrassed nor deterred. His
treadmill test scores are unchanged.
**Claims.** Asserts a control layer sitting over intact capacities. Denies that failed
judgment implies failed intelligence — the dissociation between preserved IQ and destroyed
decision-making is the whole point. Denies memory *formation*: PFC manipulates and inhibits,
hippocampus stores.
**Predicts.** Impulsivity, no planning, socially inappropriate behaviour with intact
intellect → prefrontal cortex. "Working memory" in the stem → PFC, never hippocampus.

#### Basal ganglia

**Structure.** Initiating and gating voluntary movement, plus procedural learning and reward.
With the substantia nigra: nigrostriatal dopamine loss → Parkinson's — resting tremor,
rigidity, bradykinesia, difficulty *starting* a movement.
**Concrete.** With basal ganglia damage Jordan stands at the line knowing exactly what to do
and cannot begin. Once a teammate pushes him and he is moving, the stride itself is fine.
**Claims.** Asserts a start/stop gate on movements planned elsewhere. Denies a coordination
role — a well-coordinated movement that cannot be started is basal ganglia; a started movement
that arrives wrong is cerebellum.
**Predicts.** Difficulty initiating, resting tremor, habit and skill learning → basal ganglia.
Add "dopamine" and "substantia nigra" and it is Parkinson's — the low-dopamine half of the
dopamine trap.

#### Cerebellum

**Structure.** Balance, coordination, motor learning, and the timing of movement. Damage:
ataxia — wide unsteady gait, intention tremor, dysmetria, movements that start correctly and
arrive wrong.
**Concrete.** With no cerebellum Jordan starts crisply on the gun and then cannot hold the
line: he weaves off the course, overshoots the turn at the creek, and goes down at the
barriers.
**Claims.** Asserts an error-correcting timer running alongside movement. Denies weakness —
strength is normal, sequencing is not. Denies being the initiator; that is basal ganglia, the
confusable neighbour.
**Predicts.** Balance, coordination, smooth timing, learned motor sequences → cerebellum.
"Cannot start" is basal ganglia; "cannot control once started" is cerebellum.

#### Medulla

**Structure.** The vital autonomic centres: breathing, heart rate, blood pressure, plus
vomiting and swallowing reflexes. Damage: loss of the automatic control of functions that
cannot be sustained voluntarily.
**Concrete.** Jordan's breathing rate climbing over the last 800 without his deciding
anything — the medulla is reading CO₂ and setting it. Damage here does not change his race; it
ends his life.
**Claims.** Asserts involuntary control at the brainstem's lowest and oldest level. Denies
overlap with hypothalamic homeostasis: the hypothalamus sets hunger, thirst and temperature,
the medulla runs cardiac and respiratory output moment to moment.
**Predicts.** Breathing, heart rate, blood pressure, life-sustaining reflexes → medulla. If
the function in the stem can be lost without death — sleep, arousal — it is pons or reticular
formation instead.

#### Pons

**Structure.** The bridge between medulla and midbrain and between cortex and cerebellum:
sleep architecture (REM generation), arousal, and modulation of the respiratory rate the
medulla generates.
**Concrete.** Jordan's REM sleep the night before conference — the pontine cells that switch it
on also paralyse him so he does not run the race in his bed. Damage here fragments his sleep
while his breathing continues.
**Claims.** Asserts a sleep-and-arousal role over and above conduction. Denies duplicating the
medulla: the medulla generates the respiratory rhythm and its loss is immediately fatal, the
pons modulates it.
**Predicts.** REM sleep, sleep–wake regulation, respiratory *modulation* → pons. If the stem
is about the arousal continuum itself rather than a sleep stage, the answer is more likely
reticular formation.

#### Reticular formation

**Structure.** A diffuse net of nuclei running the length of the brainstem; as the reticular
activating system it sets the overall level of cortical arousal and gates the sleep–wake
cycle. Damage: coma.
**Concrete.** The reticular formation is why Jordan is alert on the 6 a.m. bus to the meet and
drowsy on the ride home, and why he sleeps through a teammate's alarm but not through his own
name.
**Claims.** Asserts arousal is a graded, brainstem-set global variable — a dial, not a switch.
Denies being a sleep centre: it sets whether and how much the cortex is on, and its loss
produces coma, not insomnia.
**Predicts.** Consciousness, general alertness, coma, filtering out irrelevant stimulation →
reticular formation. A specific sleep *stage* points to pons; a circadian *schedule* points to
the hypothalamic SCN.

#### Broca's area

**Structure.** Left frontal, adjacent to motor cortex: speech **production** — assembling and
articulating output. Damage: non-fluent aphasia, effortful telegraphic speech, comprehension
preserved, and the patient knows.
**Concrete.** After the race Jordan wants to tell the researcher he went out too fast. He
understands every question she asks. What comes out is "went... fast... too," halting, and he
is visibly frustrated by it.
**Claims.** Asserts a production/comprehension dissociation with an anatomical basis —
frontal, next to motor output. Denies that non-fluent implies not understanding. The
frustration is diagnostic: intact comprehension makes the deficit audible to the speaker.
**Predicts.** Effortful, sparse, grammatically stripped speech with intact understanding →
Broca. Frontal location and *production* are the same fact: output sits beside the motor strip.

#### Wernicke's area

**Structure.** Left temporal, near auditory cortex: **comprehension**. Damage: fluent aphasia —
normal rate and prosody, meaningless content, poor comprehension, and no awareness of the
deficit.
**Concrete.** Same moment, different lesion: Jordan answers the researcher at length, smoothly,
in confident well-formed sentences that mean nothing, and looks puzzled when she looks
confused.
**Claims.** Asserts comprehension and production are separable systems in separate lobes.
Denies that fluency signals intactness — this is the trap, since a Wernicke's patient sounds
far more normal for the first two seconds. Denies awareness: not knowing you are impaired is
part of the syndrome.
**Predicts.** Fluent but empty speech, poor comprehension, an untroubled patient → Wernicke.
Temporal location and *comprehension* are the same fact: input sits beside auditory cortex.

#### Limbic system

**Structure.** Not a structure but a set — amygdala, hippocampus, hypothalamus, cingulate
cortex, septal nuclei — handling emotion, memory and drive as one interconnected circuit.
**Concrete.** Jordan's whole start line at once: the gun frightening him (amygdala), last
year's finish replaying (hippocampus), his empty stomach (hypothalamus), and the conflict
between going out hard and holding back (cingulate).
**Claims.** Asserts emotion, memory and drive are anatomically interlocked rather than separate
faculties. Denies being the answer whenever a component is also on offer: if the stem
describes one specific deficit and both "amygdala" and "limbic system" appear, the specific one
is the key. Limbic system is correct only when the stem's function genuinely spans the set.
**Predicts.** A stem naming one deficit → name the component. A stem naming emotion *and*
memory *and* drive together, or asking which system contains the amygdala → limbic system.

#### Neurotransmitters, hormones, and the nervous-vs-endocrine split
FL1: Q188, Q195 support · CC7A

**Structure.** Nervous signalling is **fast, electrical, targeted, brief**; endocrine is **slow, blood-borne, diffuse, sustained**; the **hypothalamus is the bridge**, via the pituitary.

| Class | Agent | What it does |
|---|---|---|
| Transmitter | **Dopamine** | reward, movement, motivation — excess in mesolimbic → schizophrenia's positive symptoms; loss in nigrostriatal → Parkinson's; addiction |
| Transmitter | **Serotonin** | mood, sleep, appetite |
| Transmitter | **Acetylcholine** | muscle activation and memory (lost in Alzheimer's) |
| Transmitter | **Norepinephrine** | arousal, alertness, fight-or-flight |
| Transmitter | **GABA** | principal **inhibitory** |
| Transmitter | **Glutamate** | principal **excitatory**, substrate of LTP |
| Transmitter | **Endorphins** | pain suppression |
| Transmitter | **Substance P** | pain transmission |
| Hormone | **Cortisol** | chronic stress, HPA, slow |
| Hormone | **Epinephrine** | acute stress, SAM, fast |
| Hormone | **Oxytocin** | bonding |
| Hormone | **Melatonin** | circadian |
| Hormone | **Testosterone** | aggression, sex drive |
| Hormone | **Insulin / leptin / ghrelin** | hunger signalling to the hypothalamus |

**Concrete.** Jordan's start-line surge is epinephrine — seconds, gone in minutes. The grinding
fatigue in week nine of the season is cortisol — hours, days, weeks.

**Claims.** One stressor drives both axes at different speeds. Denies that hormones and
neurotransmitters name one system: the endocrine effect outlasts the stimulus, the neural one
does not.

**Predicts.** Seconds and targeted → neural. Minutes to hours and body-wide → endocrine. Given a
neurotransmitter and a disorder, check the *direction*: schizophrenia and Parkinson's are the
same transmitter with opposite signs, and that is an intentional trap.

**Discriminators — 3B**
- **Sympathetic vs parasympathetic** — mobilize, or conserve?
- **Somatic vs autonomic** — voluntary skeletal muscle, or involuntary viscera? (A *different
  cut* than CNS vs PNS.)
- **Skin conductance vs heart rate as an index** — is the effector singly or dually innervated?
- **SAM vs HPA axis** — epinephrine in seconds, or cortisol in tens of minutes?
- **Amygdala vs hippocampus** — emotional salience and fear, or forming new declarative
  memories?
- **Hypothalamus vs thalamus** — drives and homeostasis, or sensory relay?
- **Hippocampus vs prefrontal cortex** — forming the memory, or manipulating and inhibiting?
- **Broca vs Wernicke** — production and non-fluent, or comprehension and fluent-but-empty?
- **Schizophrenia vs Parkinson's dopamine** — too much where, or too little where?
- **Nervous vs endocrine** — fast, targeted, brief, or slow, diffuse, sustained?

**Compression — the level of the system at which the concept lives**

| Level | Concepts | The question that lands you here |
|---|---|---|
| Ion channel | mechanically gated K⁺, voltage-gated Na⁺/Ca²⁺, ligand-gated | what opens the gate? |
| Synapse | dopamine, serotonin, ACh, NE, GABA, glutamate, endorphins | which transmitter, and which direction? |
| Structure | amygdala, hippocampus, hypothalamus, thalamus, PFC, basal ganglia, cerebellum, medulla | what behaviour changed when it was damaged? |
| Branch | sympathetic vs parasympathetic; somatic vs autonomic; CNS vs PNS | which partition is the stem using? |
| Axis | SAM (epinephrine, seconds) vs HPA (cortisol, minutes) | how fast, and how long does it last? |
| Whole organism | drive, arousal, incentive, motivation | what does the behaviour accomplish? |

Every 7A biology item names a level in its stem. Fix the level first; it eliminates half the
options unread.

#### Dopamine

**Structure.** Transmitter — fast, synaptic, brief. Reward prediction, movement initiation,
motivation. Two pathways, opposite pathologies: mesolimbic excess → the positive symptoms of
schizophrenia; nigrostriatal loss → Parkinson's.
**Concrete.** The lift Jordan feels when the $20 lands in his hand is mesolimbic dopamine —
the same transmitter whose loss elsewhere in his brain would stop him getting off the start
line at all.
**Claims.** Asserts the effect is defined by *pathway*, not by molecule. Denies "the pleasure
chemical": it tracks wanting and prediction error more than liking, and in the striatum it is
a motor transmitter. Denies that a transmitter has one direction of dysfunction.
**Predicts.** Given dopamine and a disorder, check the *sign and the place* — this is the
intentional trap. Antipsychotics block D2 and produce parkinsonian side effects; L-DOPA
raises dopamine and can produce psychotic symptoms. Each is the other run backwards.

#### Serotonin

**Structure.** Transmitter, from the raphe nuclei: mood, sleep onset, appetite, and the
restraint of aggression. Low function is the target of SSRIs.
**Concrete.** Week nine of the season, Jordan is sleeping badly, eating erratically and flat
about racing at all — the three serotonin functions moving together.
**Claims.** Asserts one transmitter spanning mood, sleep and appetite, which is why depression
presents as all three at once. Denies the simple deficiency story: SSRIs raise synaptic
serotonin within hours and take weeks to work, so the level cannot be the whole mechanism.
**Predicts.** A stem pairing mood with sleep and appetite → serotonin. Melatonin is downstream
of serotonin and is circadian, not affective; do not swap them.

#### Acetylcholine

**Structure.** Transmitter with two exam-relevant jobs: skeletal muscle activation at the
neuromuscular junction (nicotinic) and memory in the CNS (degenerating in Alzheimer's). Also
every autonomic preganglionic fibre, every parasympathetic postganglionic fibre, and the
sympathetic fibres to eccrine sweat glands.
**Concrete.** The same molecule fires Jordan's quadriceps and soaks the electrodes on his
palm — one released onto a nicotinic receptor by a somatic neuron, the other onto a muscarinic
receptor by a sympathetic one.
**Claims.** Asserts that transmitter identity does not determine division or effect — receptor
type does. Denies that "cholinergic" means "parasympathetic," the error the sweat gland exists
to break.
**Predicts.** Memory loss plus a transmitter → ACh and Alzheimer's. Paralysis plus a
transmitter → ACh at the NMJ. Curare and botulinum act here; nerve agents block its breakdown
and produce continuous contraction.

#### Norepinephrine

**Structure.** A transmitter in the CNS (arousal, alertness, vigilance) and the sympathetic
postganglionic transmitter in the periphery — and, released into blood from the adrenal
medulla, a hormone. Same molecule, three contexts.
**Concrete.** Norepinephrine crosses the synapse onto Jordan's sinoatrial node at the gun and,
minutes earlier, was keeping him vigilant during the warm-up from locus coeruleus neurons.
**Claims.** Asserts the neurotransmitter/hormone boundary is about the *route* — synaptic cleft
versus bloodstream — not about the chemical. Denies that a molecule belongs to one system:
norepinephrine and epinephrine both cross the line.
**Predicts.** Arousal, alertness, fight-or-flight, stimulant mechanisms → norepinephrine. A
stem specifying bloodstream and body-wide is asking about the hormone role; synapse and
milliseconds, the transmitter role.

#### GABA

**Structure.** The principal **inhibitory** transmitter of the CNS. GABA-A is a ligand-gated
chloride channel: open it, Cl⁻ enters, the neuron hyperpolarizes and moves away from
threshold.
**Concrete.** The night before conference Jordan cannot stop rehearsing the race. A
benzodiazepine, alcohol and a barbiturate would all work at GABA-A, potentiating the same
inhibition — and all three would blunt his coordination in the morning.
**Claims.** Asserts inhibition is an active process with its own transmitter and its own ion.
Denies that "inhibitory" means inconsequential: losing GABA function produces seizure, not
calm.
**Predicts.** Anxiolytics, sedatives, alcohol, anticonvulsants → GABA. A transmitter question
mentioning hyperpolarization or Cl⁻ influx → GABA. Its opposite on every dimension is
glutamate.

#### Glutamate

**Structure.** The principal **excitatory** transmitter of the CNS and the substrate of
long-term potentiation through the NMDA receptor: depolarizes, Na⁺ and Ca²⁺ in, toward
threshold.
**Concrete.** Every course feature Jordan learned on his preview run — the sharp left at the
creek, the false flat at two miles — was potentiated at glutamatergic synapses, because
repeated firing strengthened exactly those connections.
**Claims.** Asserts learning has a specific synaptic mechanism and that mechanism is
excitatory. Denies that excitation is benign: excess glutamate is excitotoxic and kills
neurons in stroke.
**Predicts.** Learning, memory, LTP, NMDA, excitotoxicity → glutamate. Set against GABA in an
option list, the question is direction: depolarize or hyperpolarize.

#### Endorphins

**Structure.** Endogenous opioid peptides that *suppress* the pain signal — presynaptically
blocking the release of pain transmitters, and through descending pathways from the
periaqueductal grey.
**Concrete.** Jordan finishes and only notices in the parking lot that he tore a toenail off at
mile two. The signal was there during the race and was being suppressed.
**Claims.** Asserts pain is modulated, not merely detected — the nervous system has its own
brake. Denies that the injury signal was absent: transmission and suppression are separate
steps, which is why the pain arrives late rather than never.
**Predicts.** Runner's high, stress-induced analgesia, naloxone-reversible placebo analgesia,
opioid drugs → endorphins. If the stem is about the signal *arriving*, it is substance P.

#### Substance P

**Structure.** A neuropeptide that *transmits* nociceptive input from the primary afferent into
the dorsal horn — the message endorphins act to block.
**Concrete.** The torn toenail at mile two releasing substance P into Jordan's spinal cord, and
endorphins arriving at that same synapse to stop it getting through.
**Claims.** Asserts a dedicated transmitter for pain input. Denies that pain is one event:
transmission (substance P) and suppression (endorphins) are opposed processes at one synapse,
and felt pain is their difference. The name carries nothing — the fact to bind is that it sits
on the *sending* side.
**Predicts.** With both in the option set, ask which direction the stem describes: signal going
up → substance P, signal being damped → endorphins. Capsaicin depletes substance P, which is
why chilli burns and then numbs.

#### Cortisol

**Structure.** Hormone from the adrenal **cortex**, the end of the HPA cascade — slow,
bloodborne, sustained. Raises blood glucose by gluconeogenesis, mobilizes fat and protein,
suppresses immune function, and stays elevated for hours.
**Concrete.** The grinding fatigue in week nine: sleeping badly, catching every cold that goes
round the bus, not recovering between workouts. That is weeks of elevated cortisol, and it
looks nothing like the two-second jolt at a start line.
**Claims.** Asserts an endocrine stress response whose effects outlast the stimulus by hours to
weeks. Denies that the acute and chronic stress responses are one system at two intensities —
different axes, different messengers, different clocks.
**Predicts.** Chronic stress, immune suppression, raised blood glucose, hours-scale timing →
cortisol. Adrenal *cortex* rather than medulla is the structural discriminator against
epinephrine.

#### Epinephrine

**Structure.** Hormone from the adrenal **medulla**, the end of the SAM axis — neural trigger,
bloodborne delivery, seconds to onset and minutes to clear: heart rate and contractility up,
bronchi open, glycogenolysis, blood shunted to muscle.
**Concrete.** The gun goes and Jordan feels the surge inside three seconds, and it is gone
before the first mile. Same stressor, and his cortisol has not begun to rise.
**Claims.** Asserts one stressor drives two axes at different speeds through two different
tissues of the same gland. Denies that epinephrine and cortisol are interchangeable stress
markers: medulla vs cortex, neural vs pituitary trigger, seconds vs twenty minutes.
**Predicts.** Fast whole-body mobilization → epinephrine. Given a timescale, the timescale
alone separates it from cortisol; given a gland layer, the layer does.

#### Oxytocin

**Structure.** Hormone synthesized in the hypothalamus and released from the **posterior**
pituitary: social bonding, trust and pair-bonding, plus uterine contraction in labour and milk
letdown.
**Concrete.** The team huddle before the gun, arms across shoulders — driven by the same
molecule that delivers babies. Nothing in the name would let you guess the pairing.
**Claims.** Asserts a shared neurochemistry for attachment and reproduction. Denies "the love
hormone" as complete: it raises in-group trust and can raise out-group hostility, making it a
*social salience* signal rather than a positive-affect one.
**Predicts.** Bonding, trust, attachment, labour, nursing → oxytocin. Posterior pituitary means
made in the hypothalamus and stored downstream, not synthesized in the pituitary — that
distinction is itself tested.

#### Melatonin

**Structure.** Hormone from the **pineal** gland, released in darkness under control of the
hypothalamic suprachiasmatic nucleus. Signals night and promotes sleep onset; synthesized
downstream of serotonin.
**Concrete.** Jordan's 6 a.m. bus to a meet two time zones east: his melatonin is still peaking
when the gun goes, and he races on the wrong clock.
**Claims.** Asserts circadian timing is hormonally encoded with light as the input. Denies that
melatonin is a sedative or an affective hormone — it moves the clock, it does not create sleep
pressure or mood. Denies any relation to melanin, which is a pigment.
**Predicts.** Jet lag, shift work, seasonal light, sleep *timing* → melatonin; mood →
serotonin. Bright light suppresses melatonin, which is the mechanism behind screens at night.

#### Testosterone

**Structure.** Steroid hormone from the testes, with smaller contributions from adrenal cortex
and ovaries: sex drive, secondary sexual characteristics, muscle protein synthesis, and an
association with aggression and dominance behaviour.
**Concrete.** Jordan's testosterone is higher after he wins conference than after he places
eighth. The outcome moved the hormone, not only the other way round.
**Claims.** Asserts a bidirectional hormone–behaviour relationship. Denies the one-way causal
story that testosterone causes aggression: winner and loser effects show competition changes
testosterone, and the human aggression association is modest and correlational.
**Predicts.** Sex drive, dominance, competition, muscle mass → testosterone. If a stem asserts
a clean causal arrow from hormone to aggression, expect the key to be the more cautious
option.

#### Insulin

**Structure.** Hormone from pancreatic beta cells. Peripherally it drives glucose into cells
and lowers blood glucose; centrally it reaches the hypothalamus as a **satiety** signal
proportional to how well fed the body is.
**Concrete.** The bagel Jordan eats in the finish area spikes his insulin: glucose leaves his
blood into muscle, and the same insulin arriving at his hypothalamus is part of why the second
bagel appeals less than the first.
**Claims.** Asserts one hormone acting both metabolically and motivationally. Denies that the
hypothalamus reads stomach fullness alone — it reads circulating hormonal signals, which is
why hunger tracks energy state rather than stomach volume.
**Predicts.** Blood glucose falling after a meal → insulin. Hunger signalling to the
hypothalamus → insulin alongside leptin and ghrelin.

#### Ghrelin

**Structure.** Hormone from the empty **stomach**: rises before meals, acts on the hypothalamus
to *initiate* eating, falls after ingestion. The only major hunger-promoting signal in the set.
**Concrete.** Jordan's ghrelin climbs on the bus to the meet and peaks about forty minutes
before the gun, precisely when he cannot eat.
**Claims.** Asserts hunger is signalled positively rather than as the mere absence of satiety.
Denies that fullness alone regulates eating: without ghrelin's rise the meal is not initiated
at all.
**Predicts.** Rises with fasting, falls with feeding, short-term and meal-to-meal → ghrelin.
Its opposite on every dimension is leptin.

#### Leptin

**Structure.** Hormone from **adipose tissue**, proportional to fat mass: a long-term satiety
signal telling the hypothalamus how much energy is stored. More fat → more leptin → reduced
intake.
**Concrete.** Jordan in week nine at racing weight with low body fat: his leptin is low, so his
hypothalamus reads a depleted store and he is hungry at every meal regardless of what he just
ate.
**Claims.** Asserts a chronic, stores-based regulator sitting behind the meal-to-meal one.
Denies that it functions as an appetite switch in obesity — high leptin with continued eating
is leptin *resistance*, not deficiency, which is why administering it rarely helps.
**Predicts.** Long-term, fat-mass-proportional, satiety → leptin; short-term, stomach, hunger →
ghrelin. A timescale of days to months → leptin; hours → ghrelin.

---

### CLUSTER 4 — PSYCHOLOGICAL DISORDERS AND ATTITUDE CHANGE

**FL1: Q176 (CC7A), Q177 (CC7C), Q180 (CC6B).** Three misses off one passage — a maintenance
model of an anxiety disorder — all the same failure: the passage described a mechanism in
ordinary words and asked you to name it in the field's words.

*Shared scene:* **Ellis's heart speeds up in a grocery store. He reads it as a heart attack,
panics, and leaves. The fear drops within minutes. Next week he does not go in.**

#### The six approaches to psychological disorders
FL1: Q176 · CC7A · Skill 1 · knowledge absent

**Structure.** AAMC's six perspectives (listed as personality theories; they double as approaches to disorder), plus two models.

| | Approach | What it says the disorder is made of |
|---|---|---|
| Perspective | **Psychoanalytic / psychodynamic** | unconscious conflict, early experience, defense mechanisms |
| Perspective | **Humanistic** | blocked growth; incongruence between real and ideal self; conditions of worth |
| Perspective | **Trait** | stable dimensions; disorder is an extreme position on a normal dimension |
| Perspective | **Social cognitive** | reciprocal determinism among person, behaviour, and environment; expectancies, self-efficacy, observational learning. Where **cognitive** explanations (beliefs, appraisals, interpretations) sit on AAMC's map |
| Perspective | **Biological** | genes, neurotransmitters, brain structure, endocrine function |
| Perspective | **Behaviourist** | learned through classical and operant conditioning; only observable contingencies matter; **no appeal to internal states at all** |
| Model | **Biomedical** | disease is biological pathology |
| Model | **Biopsychosocial** | biology + psychology + social context together |

**Concrete.** Ellis's panic, six ways. *Psychoanalytic:* unconscious conflict about leaving
home. *Humanistic:* he cannot be his real self under his family's conditions of worth. *Trait:*
very high in neuroticism, always has been. *Social cognitive:* he believes he cannot cope, the
belief changes what he does, what he does confirms it. *Biological:* overactive amygdala, locus
coeruleus firing too readily. *Behaviourist:* sensations were paired with terror and now elicit
it; leaving was reinforced by relief.

**Claims.** Behaviourism **denies that you need to posit any internal cause** — contingencies
are the whole explanation, which is what separates it from social cognitive, whose entire
content is an internal belief. Biomedical denies social context is part of the disease;
biopsychosocial denies biology is sufficient.

**Predicts.** "Maintenance Factor X is most closely related to which approach?" — **read what
the factor is made of, not what it is about.** Learned association or reinforced behaviour →
**behaviourist**. Belief, expectancy, interpretation, appraisal → **cognitive / social
cognitive**. Neurotransmitter, structure, gene → **biological**. Unconscious conflict or defense
→ **psychoanalytic**. Thwarted self-actualization or incongruence → **humanistic**. Stable
lifelong disposition → **trait**. The topic is not the approach: on a panic passage, *pairing*
is behaviourist, *misinterpretation* is cognitive.

#### Psychoanalytic / psychodynamic
FL1: Q176 · CC7A · knowledge absent

**Structure.** The cause is a conflict the person cannot report — early experience, a wish set against a defence; the symptom is the compromise between them.
**Concrete.** Ellis's therapist asks what changed the month the attacks started. His father moved into a care home; Ellis handled the paperwork and felt nothing at the time. The grocery store is where the feeling comes out because it has nowhere else to go.
**Claims.** The stated reason is not the reason. Denies that the patient has access to his own cause — which is why the approach cannot be checked by asking him. Denies the behaviourist's sufficiency claim: contingencies are surface.
**Predicts.** A maintenance factor phrased as *unresolved conflict, defence, repression, displacement,* or something from childhood the patient does not connect to the symptom → psychoanalytic. If the passage lets the patient state his own cause accurately, it is not this one.

#### Humanistic
FL1: Q176 · CC7A · knowledge absent

**Structure.** Growth toward the real self is the default; disorder is what happens when acceptance is made conditional and the real self is forced apart from the ideal one.
**Concrete.** In Ellis's family fear was not something you said out loud, and he was the calm one — being the calm one was how he was loved. Thirty years on, the panic is the part of him that was never allowed a name.
**Claims.** Asserts the person is not broken but blocked: remove the conditions of worth and growth resumes. Denies that the disorder is a defect to be corrected, and denies psychoanalysis's picture of the interior as a battlefield — for the humanist it is a thwarted direction, not a fight.
**Predicts.** A maintenance factor about *self-acceptance, incongruence between who he is and who he must be, unconditional positive regard,* or thwarted self-actualization → humanistic. The tell is that the therapy removes an obstacle rather than adding a technique.

#### Trait
FL1: Q176 · CC7A · knowledge absent

**Structure.** Behaviour is generated by stable dimensions everyone sits somewhere on; the disorder is an extreme position on one, not a different kind of thing.
**Concrete.** Ellis checked the stove twice at nine years old and checks it twice now. Score him on neuroticism at fifteen and at forty and the number is the same high one; his whole family is on that scale, lower down.
**Claims.** Continuity — no categorical break between disordered and well. Denies the situational account, that circumstance carries the behaviour, and denies psychoanalysis's developmental story: the dimension was there before the events were.
**Predicts.** A factor described as *longstanding, characteristic, present before onset, stable across situations* → trait. If the passage measures it with an instrument that yields a **score** rather than a category, it is a trait account.

#### Social cognitive
FL1: Q176 · CC7A · knowledge absent

**Structure.** Person, behaviour and environment each cause the other two — reciprocal determinism — and the person's contribution is a statable belief: an expectancy, a self-efficacy judgement, something learned by watching.
**Concrete.** Ellis believes he could not cope with a racing heart in public. Believing it, he leaves the store. Leaving, he never finds out. The belief built the environment that proves the belief.
**Claims.** This is where AAMC files **cognitive** explanations — appraisal, interpretation, expectancy. Asserts an internal state does causal work, the exact thing behaviourism denies. Denies one-way causation: the environment is not simply given to the person.
**Predicts.** A factor made of *belief, expectation, interpretation, appraisal, self-efficacy* or observational learning → social cognitive. On a panic passage, **catastrophic misinterpretation of bodily sensations is this approach**, even though the sensations themselves are bodily.

#### Behaviourist
FL1: Q176 · CC7A · knowledge absent

**Structure.** Only observable contingencies — pairings and consequences. No internal term is permitted anywhere in the explanation.
**Concrete.** What a behaviourist writes in Ellis's file: entered store 10:14, heart rate rose, left at 10:18, fear fell. There is no line for what he thought it meant, and the account is finished without one.
**Claims.** Denies that you need to posit an internal cause at all — not that beliefs are hard to measure, that they are **unnecessary**. That is the entire distance to social cognitive, whose whole content is an internal belief.
**Predicts.** A factor made of *pairing, association, reinforcement, punishment, extinction* or avoidance → behaviourist. Same passage, same panic: **the pairing is behaviourist, the misinterpretation is cognitive.** The topic never decides; the material the factor is made of decides.

#### Biomedical model
FL1: Q176 · CC7A · knowledge absent

**Structure.** Disease is biological pathology. Everything else is context around the disease rather than part of it.
**Concrete.** Ellis's GP writes "panic disorder," starts an SSRI, and books a six-week review. The care home, the grocery store and the avoidance are background to the case, not entries in it.
**Claims.** Asserts one level of explanation is sufficient. Denies that social context is constitutive — it may trigger, but the disease sits in the tissue. Distinct from the **biological perspective**: the perspective says where to look, the model says that is the only place worth looking.
**Predicts.** An option saying the condition "is best understood as a disease of the brain," or that treatment should target pathology alone → biomedical. On an EXCEPT stem it is usually the one option that leaves the person's circumstances out.

#### Biopsychosocial model
FL1: Q176 · CC7A · knowledge absent

**Structure.** Three levels run at once and interact — biology, psychology, social context — and dropping any one leaves the case unexplained.
**Concrete.** Ellis's case conference fills three columns: a nervous system that fires early, a belief that a fast heart means death, and a night-shift job where he now sees nobody for eleven hours.
**Claims.** Asserts no level is sufficient alone, which denies the biomedical claim head-on. Denies as well that it is merely "biology plus some other factors" — the levels **interact**, so the social level can change the biological one.
**Predicts.** Given a passage listing a genetic loading, a cognitive style and an isolating job, the account covering all three is biopsychosocial; the option naming only the strongest single cause is the biomedical distractor. Where a stem asks which approach is most comprehensive, this is it.

#### Classical conditioning as a maintenance mechanism — interoceptive cues
FL1: Q177 · CC7C · Skill 1 · knowledge absent

**Structure.** A **US** produces a **UR** with no learning; pair a neutral stimulus with the US repeatedly and the **NS** becomes a **CS** eliciting a **CR**.

| | Stimulus | Response |
|---|---|---|
| **Unlearned** — effective before any pairing | **US** | **UR** |
| **Learned** — effective only after the pairing | **CS** (formerly the NS) | **CR** |

The CS can be **internal**, because a bodily sensation is a perfectly good stimulus.

**Concrete.** Ellis's first attack: the surge of terror is the **US**, the fear it produces the
**UR**. Just before it started his heart rate rose slightly — then, a neutral sensation. Now a
mild rise from stairs, coffee, or heat is a **CS** eliciting fear as a **CR**.

**Claims.** Denies that the panic needs an external trigger — it is inside. And denies the
sensation-as-*symptom* reading: in the maintenance loop it is a **cause**, having acquired a
signalling role it did not have before.

**Predicts.** "Mild changes in bodily sensations act as:" → **conditioned stimuli.** Run the
four-way check with one question: **was this stimulus effective before any learning happened?**
If no, it is a CS, and the response it now produces is the CR.

**The trap.** "Unconditioned stimulus" is attractive because the sensations are involuntary and
bodily. **Involuntary is not unconditioned.** *Unconditioned* means it did not have to be
learned; a racing heart did not produce panic before the pairing, so it cannot be the US.

#### Operant conditioning as a maintenance mechanism — negative reinforcement and avoidance
FL1: Q180 · CC6B · Skill 1 · knowledge absent

**Structure.** The 2×2. **Reinforcement** increases behaviour, **punishment** decreases it;
**positive** = a stimulus is *added*, **negative** = a stimulus is *removed*.

| | Behaviour ↑ (reinforcement) | Behaviour ↓ (punishment) |
|---|---|---|
| **Add** a stimulus | positive reinforcement | positive punishment |
| **Remove** a stimulus | **negative reinforcement** (escape, avoidance) | negative punishment |

**Concrete.** Ellis leaves the store and the fear drops within four minutes. Leaving was
**negatively reinforced** — an aversive state removed, so it comes faster and sooner next time:
**escape learning**. By next week he does not enter at all: **avoidance learning**. Never
staying, he never learns nothing happens, so **extinction never occurs.**

**Claims.** Negative reinforcement is **not punishment**. Denies "negative" as bad: it names
the operation (removal), and *reinforcement* always means the behaviour goes **up**. Avoidance
self-seals — a behaviour that prevents the disconfirming experience cannot be corrected by
experience.

**Predicts.** In a two-factor maintenance model of an anxiety disorder the two processes are
**classical conditioning** (a cue acquires the fear) and **operant conditioning through negative
reinforcement** (avoidance strengthened by relief). Exposure works by **blocking the avoidance
so extinction can happen.**

**When the passage's vocabulary is cognitive instead.** If it frames its maintenance factors as
*attention to bodily sensations* and *catastrophic interpretation of them*, the answer set is
the 6B lexicon — **selective attention / hypervigilance** and **top-down processing / cognitive
appraisal** — not the conditioning lexicon. **Match the answer to the words the passage used.**
Both readings are live on a panic passage; only one is in the passage.

#### Attitude and behaviour change — and which direction the item is asking about
FL1: Q177 context · CC7C

**Structure.** The outline lists the two directions as **separate bullets**, and AAMC writes items on the direction.

| Direction | Mechanism | What it says |
|---|---|---|
| **Attitudes → behaviour** | the four moderators | strong when the attitude is **specific to the behaviour**, formed by **direct experience**, strongly held, and when **situational pressure is weak** |
| **Behaviour → attitudes** | **Cognitive dissonance** | an act inconsistent with an attitude creates discomfort; the cheapest resolution is changing the attitude. **Dissonance is largest when the external justification is smallest.** |
| **Behaviour → attitudes** | **Self-perception** | with no strong prior attitude, you infer your attitude by observing your own behaviour. No discomfort involved |
| **Behaviour → attitudes** | **Foot-in-the-door** | a small compliance shifts self-image, making the large request succeed |
| **Compliance only — no attitude change** | **Door-in-the-face** | a large refused request then a small one; runs on reciprocal concession |
| **Compliance only — no attitude change** | **Lowball** | agreement first, cost revealed after; runs on commitment to the decision |
| **Behaviour → attitudes** | **Role-playing effects** | occupying a role reshapes the attitude |
| **Persuasion — elaboration likelihood model** | **Central route** | motivated and able to think → argument quality decides → durable, resistant change |
| **Persuasion — elaboration likelihood model** | **Peripheral route** | unmotivated or distracted → cues decide: attractiveness, credibility, number of arguments, mood → fragile change that decays |

**Concrete.** Ellis tells his therapy group that exposure works, before he believes it.
*Dissonance:* said for no reward, the mismatch resolves by his believing it more.
*Self-perception:* no prior opinion, heard himself say it, concluded he must think so. *ELM:*
the argument moves him only if he is well enough that day to attend to it; otherwise only the
speaker's confidence registers, and not for long.

**Claims.** Dissonance requires an **existing attitude contradicted** and produces
**arousal/discomfort**; self-perception requires **no prior attitude** and produces **no
discomfort**. That difference is the whole discriminator, and it is testable: only dissonance
predicts physiological arousal.

**Predicts.** **Small** incentive → **more** attitude change under dissonance (insufficient
justification). **Large** incentive → less; the behaviour is already explained. No prior attitude
→ dissonance predicts nothing, self-perception carries it. Distracted or unmotivated audience →
only peripheral cues move them, and the change decays. Strong argument, motivated audience →
central route, durable change.

#### When attitudes predict behaviour — the four moderators
FL1: Q177 context · CC7C

**Structure.** An attitude predicts behaviour when it is **specific to that behaviour**, formed by **direct experience**, **strongly held**, and when **situational pressure is weak**. Fail one and the correlation collapses.
**Concrete.** Ellis says he believes in exposure therapy, and does none of it. He says he will stand inside the corner shop for two minutes on Tuesday morning, and does. Same man, same week; the second attitude names the act.
**Claims.** Asserts that a weak attitude–behaviour correlation is a measurement mismatch, not evidence that attitudes are inert. Denies the folk assumption that a sincerely held general attitude should show up in specific conduct.
**Predicts.** Given a study where a general attitude fails to predict a specific act, the answer is that the attitude was measured at the wrong level of specificity — not that the participants were insincere. Strong situational pressure in the stem → the attitude will not predict; direct experience in the stem → it will.

#### Cognitive dissonance
FL1: Q177 context · CC7C

**Structure.** An act inconsistent with an existing attitude → discomfort → the attitude moves to match the act, because the act cannot be undone. **Less external justification, more attitude change.**
**Concrete.** Ellis tells the therapy group that exposure works, before he believes it. Nobody paid him and nobody made him. Walking to his car he notices he means it more than he did when he said it.
**Claims.** Requires a prior attitude to contradict, and asserts a real aversive arousal state. Denies that the change is cool inference — the discomfort is the engine — and denies the intuition that a bigger reward buys a bigger shift in belief.
**Evidence.** Give people a pill and tell them it causes tension and the attitude change disappears; the arousal is attributed to the pill instead. Nothing in self-perception predicts that result.
**Predicts.** **Small** incentive, weak pressure, free choice → large attitude change. **Large** incentive → little, because the act is already explained. If the stem says the person held no prior opinion, dissonance predicts nothing at all.

#### Self-perception
FL1: Q177 context · CC7C

**Structure.** No prior attitude → you read your own behaviour the way an outside observer would and infer what you must think. No conflict, no arousal.
**Concrete.** Ellis had no view about the breathing exercise either way. He hears himself recommending it to a new group member and thinks: apparently I rate that.
**Claims.** Asserts attitude change without discomfort, from observation alone. Denies dissonance's necessary condition — there was nothing there to contradict — and denies that arousal is required for an attitude to move.
**Predicts.** Weak, ambiguous or absent prior attitude → self-perception carries it; strong prior attitude contradicted → dissonance. One question splits them: **was there an attitude to violate, and is the person uncomfortable?**

#### Foot-in-the-door
FL1: Q177 context · CC7C

**Structure.** Small request accepted → self-image shifts to "someone who does this" → the large request now fits. The escalation runs **through the person's view of himself**.
**Concrete.** The therapist asks Ellis to stand in the shop doorway for thirty seconds. He does. Two weeks later she asks for twenty minutes of shopping and he agrees — the doorway made him a person who goes in.
**Claims.** Asserts the first act works by changing self-perception, so the effect survives a delay and a change of requester. Denies that compliance is bought by the size of the second request or by pressure at the moment of asking.
**Predicts.** Given "he agreed to something small first, then something large," the mechanism named is self-perception and the effect should **persist over time**. Remove the delay, or have him refuse the first request, and foot-in-the-door does not apply.

#### Door-in-the-face
FL1: Q177 context · CC7C

**Structure.** Large request refused → the smaller request reads as a concession → reciprocal concession plus contrast produce compliance. It runs **through the exchange, not the self**.
**Concrete.** The therapist opens with a full hour in the supermarket on Saturday. Ellis refuses. She says "then ten minutes in the corner shop" and he takes it — because she moved, so he moves.
**Claims.** Asserts compliance with **no attitude change at all**: he is not more favourable to exposure, he is answering a concession. Denies foot-in-the-door's mechanism outright — here the first request must be **refused**, from the same person, without delay.
**Predicts.** Insert a delay or swap the requester and this effect dies; do the same to foot-in-the-door and it survives. Expect compliance now and **nothing durable** — if the stem asks what the person believes six months later, this technique predicts no change.

#### Lowball
FL1: Q177 context · CC7C

**Structure.** Agreement obtained on favourable terms → the cost is raised **after** the commitment → the person stays, because the commitment attached to the decision rather than to the terms.
**Concrete.** The group leader signs Ellis up for a Saturday session and he agrees. Then she mentions it starts at seven and runs until noon. He goes.
**Claims.** Asserts the binding thing is the freely made decision itself. Denies that people re-evaluate when the terms change, and denies door-in-the-face's route — nothing was refused and no concession was offered.
**Predicts.** The order is the tell: **commitment first, bad news second.** Told the cost up front he declines; told after, he complies. If the stem removes his sense of free choice at the moment of agreeing, the effect disappears.

#### Central route
FL1: Q177 context · CC7C

**Structure.** Motivated **and** able to think → the message is elaborated → argument quality decides → change is durable, resistant to counterargument, and predicts behaviour.
**Concrete.** On a good day Ellis reads the handout on extinction, checks its claim against his own exposure log, finds it holds, and changes his mind. Six months later he still holds it.
**Claims.** Asserts that what persuaded him was the content. Denies that credibility or the sheer number of arguments mattered here — under elaboration a **weak** argument from a credible source backfires rather than helping.
**Predicts.** Given a motivated, undistracted, personally involved audience: strong arguments persuade, weak ones repel, and the attitude sticks. If a later item asks whose attitudes still predict behaviour, it is this group.

#### Peripheral route
FL1: Q177 context · CC7C

**Structure.** Unmotivated, distracted, or unable → no elaboration → cues decide: source credibility, attractiveness, mood, how many arguments there were. The change is fragile and decays.
**Concrete.** On a bad day Ellis cannot follow the argument at all. What registers is that the speaker was a consultant and sounded certain. He agrees, and by Thursday it has gone.
**Claims.** Asserts persuasion without processing. Denies that argument quality matters when elaboration is low — **counting** arguments is a peripheral cue, weighing them is central.
**Predicts.** Distraction, time pressure, low personal relevance or low ability in the stem → peripheral route, and the attitude is **temporary, vulnerable to counterargument, and a poor predictor of behaviour.** The discriminator is never what the message contained; it is whether the audience could work on it.

**Discriminators**
- **Behaviourist vs social cognitive** — is the factor a *contingency* or a *belief*?
- **Biomedical vs biopsychosocial** — is social context part of the disorder or outside it?
- **Psychoanalytic vs humanistic** — unconscious conflict, or blocked growth?
- **Trait vs situational approach** — a stable disposition, or the circumstances?
- **CS vs US** — was the stimulus effective *before* the pairing?
- **CR vs UR** — is the response to the learned cue, or to the natural one?
- **Negative reinforcement vs punishment** — does the behaviour go **up** or **down**?
- **Escape vs avoidance** — does the behaviour end the aversive state, or prevent it starting?
- **Extinction vs spontaneous recovery** — the CR fades with unreinforced exposure, or reappears
  after a rest interval.
- **Cognitive dissonance vs self-perception** — was there a prior attitude to contradict, and is
  there discomfort?
- **Cognitive dissonance vs foot-in-the-door** — the attitude shifts to match a *dissonant act*,
  or the behaviour escalates through *commitment*?
- **Central vs peripheral route** — did argument quality decide, or did a cue?
- **Positive vs negative punishment** — was something added, or taken away?

**Compression — what is claimed to do the causal work**

| Approach / mechanism | The cause it names | Where the cause sits |
|---|---|---|
| Psychoanalytic | unconscious conflict | inside, unavailable to report |
| Humanistic | thwarted growth, incongruence | inside, about the self |
| Trait | a stable dimension | inside, dispositional |
| Social cognitive / cognitive | a belief, expectancy, appraisal | inside, statable |
| Biological | transmitter, structure, gene | inside, physical |
| Behaviourist — classical conditioning | a stimulus that acquired meaning | outside, an association |
| Behaviourist — operant conditioning | a consequence that followed behaviour | outside, a contingency |
| Cognitive dissonance | an act contradicting an attitude | the mismatch between them |
| Self-perception | observation of one's own behaviour | outside, then inferred |
| ELM central / peripheral | argument quality / a surface cue | in the message and the audience |
| Biopsychosocial | all of the above plus context | across all levels |

One question orders the table: **when this account explains the behaviour, what does it point
at?** Behaviourist accounts point outside the person; cognitive at a belief; biological at
tissue. AAMC's item asks you to point.

---

### CLUSTER 5 — SOCIAL INTERACTION (CC8C)

**FL1: Q209, Q222, Q226 · 3/6 on CC8C · 50%.** One of the section's two largest categories —
roughly **8 items on a real form**. Q197 is tagged **CC7B**, carried into this cluster because
synchrony is socially situated. Q209 is a negative stem (EXCEPT); run the procedure at the top
first.

*Shared scene:* **Dr. Reyes sees Mr. Okonkwo. A cultural liaison begins joining the visits. Mr.
Okonkwo's sister drives him to dialysis and calls every night.**

#### Group size — dyad, triad, and what a third member changes
FL1: Q222 · CC8C · Skill 1 · knowledge absent

**Structure.** Adding one member changes the *kind* of group, not its size alone.

| | **Dyad** (2) | **Triad** (3) | Larger still |
|---|---|---|---|
| Survives a member leaving | no — either member's exit ends it | **yes** | yes |
| Coalitions | none possible — no majority | **possible** — two against one | subgroups form |
| Third party to mediate | none | **a mediator role appears** | formal roles |
| Responsibility | undivided | diffuses | diffusion deepens |
| Intimacy | **the most intimate group** | falls | lowest |
| Stability | **the most fragile** | greater | gains stability and formality |

**Concrete.** Physician and patient alone: a dyad — if either withdraws there is no encounter.
Add the liaison and it is a triad: she can translate a misunderstanding, and can also side with
Mr. Okonkwo against Dr. Reyes, structurally impossible the week before. Training Dr. Reyes
instead **adds no member**.

**Claims.** Caused by the **number of members**, not the third member's skill or intentions.
Denies reading a new participant as merely an added resource — the **type of relationship
changes**, and the changes follow from arithmetic, not from who the person is.

**Predicts.** On "liaison vs training the physician," the *structural* differences all follow
from dyad → triad: greater stability, a possible mediator, possible coalitions, **reduced
intimacy in the original dyad.** Training changes competence and leaves structure untouched. An
item contrasting adding a person against improving one is testing group size.

#### Coalition
FL1: Q222 · CC8C · knowledge absent — missed again cold, Sep 5

**Structure.** Two members act together against a third. It requires **three people**, because a group of two has no majority to form.
**Concrete.** In the room, the liaison and Mr. Okonkwo both say the transplant workup should wait. Dr. Reyes is outnumbered in her own clinic — an arrangement that was not merely unlikely the week before but structurally unavailable.
**Claims.** Asserts a coalition is created by arithmetic, not intention: nobody has to plan it, and no one need be hostile. Denies that a dyad can contain one — in a group of two every disagreement is one against one and there is no side to take.
**Predicts.** Any item contrasting a two-person relationship with a three-person one lists "coalitions become possible" among the correct structural consequences. If an option says two members sided against another, the group described has at least three.

#### The mediator role
FL1: Q222 · CC8C · knowledge absent — missed again cold, Sep 5

**Structure.** A third member can stand **outside** a disagreement between the other two and act on it — a position that does not exist in a dyad, whoever the person is.
**Concrete.** Dr. Reyes says "your clearance is falling." Mr. Okonkwo hears an accusation. The liaison restates the number in terms he can accept and restates his refusal in terms Reyes can act on. She occupies a place in the room that was empty when there were two chairs.
**Claims.** Asserts the role is made available by group size, and that the same position can be used to exploit the split rather than heal it — one structural fact, two uses. Denies that mediation is a skill one member of a dyad could simply supply: inside a dyad, every party to the dispute is a party to it.
**Predicts.** "What becomes possible when a third person joins?" → a mediator, a coalition, and survival of one member's departure. Expect the same item to offer **reduced intimacy** as a correct consequence, not as a distractor.

#### Adding a member vs improving a member
FL1: Q222 · CC8C · reasoning — read "train the physician instead" as being about difficulty rather than about structure. Missed again cold, Sep 5.

**Structure.** Two interventions, one goal, different arithmetic: hiring a third person **changes the kind of group**; training one of the two leaves a dyad with a better-trained member in it.
**Concrete.** The clinic can fund the cultural liaison, or send Dr. Reyes on a two-day course. After the course the room still holds two people — no coalition can form, nobody can mediate, and if either walks out there is no encounter. After the hire all three of those change, and nobody has become more skilled.
**Claims.** Asserts that structural properties follow from the **count of members** and from nothing else. Denies the reading that this choice is about how hard, how expensive or how effective each option is: the two options are **not two doses of the same thing**, and an item asking what differs *structurally* is not asking which works better.
**Predicts.** Whenever a stem offers "add a person" against "improve a person," the correct differences are the dyad→triad list — stability, mediation, coalitions, diffused responsibility, reduced intimacy. Any option framed in terms of competence, cost, difficulty or training time is on the wrong axis and is wrong.

#### The four types of social support
FL1: Q209 · CC8C · Skill 1 · knowledge absent · **negative stem (EXCEPT)**

**Structure.** Distinguished by **what is transferred.**

| Type | What is transferred | The act |
|---|---|---|
| **Emotional** | empathy, love, trust, caring | someone listens |
| **Instrumental (tangible)** | material aid, services, money, labour | someone drives you |
| **Informational** | advice, guidance, facts | someone explains what the nephrologist said |
| **Appraisal** | feedback useful for self-evaluation | someone tells you how you are doing |
| *(Companionship / belonging)* | sometimes listed fifth | someone is simply there |

**Concrete.** Mr. Okonkwo's sister in one week: listens when he says he is frightened
(**emotional**), drives him to dialysis (**instrumental**), explains what the doctor meant by
"clearance" (**informational**), tells him he is handling this better than he thinks
(**appraisal**). One person, four kinds.

**Claims.** Not one quantity. Denies that "amount of support" is the variable — the wrong type
does not substitute. Denies too that it is categorized by *who* provides it: items describe an
**act**, not a person.

**Predicts.** Match on the content of the act. Asked which support type a study measured, find
the verb: *listened / provided / explained / evaluated.*

#### Emotional support
FL1: Q209 · CC8C · knowledge absent · **negative stem (EXCEPT)** — blank on free recall, Sep 5

**Structure.** What is transferred is a **feeling** — empathy, love, trust, caring. Nothing is solved and nothing is taught.
**Concrete.** Nine at night, Mr. Okonkwo says he is frightened of the machine. His sister does not fix it, correct him, or explain it. She stays on the line.
**Claims.** Asserts the transfer is of regard itself, which is why it works when nothing about the problem can change. Denies that support must accomplish something — advice offered at this moment is a different type, and usually the wrong one.
**Predicts.** In the stem look for *listened, comforted, was there for him, expressed concern.* A study measuring "how much the patient felt cared about" is measuring emotional support, whatever else it also did.

#### Instrumental (tangible) support
FL1: Q209 · CC8C · knowledge absent · **negative stem (EXCEPT)** — blank on free recall, Sep 5

**Structure.** What is transferred is a **thing** — money, labour, transport, a service. Material aid, physically delivered.
**Concrete.** Twenty to six in the morning, three times a week, his sister's car is in the driveway and she drives him to dialysis.
**Claims.** Asserts the support **is** the resource, not the sentiment behind it: a paid taxi transfers the same thing. Denies that instrumental support requires closeness, which is why it is the type most easily replaced by a service.
**Predicts.** Look for *provided, gave, drove, paid, helped with.* If a concrete good or an hour of somebody's labour changes hands, the answer is instrumental — even when the giver is obviously devoted to the recipient.

#### Informational support
FL1: Q209 · CC8C · knowledge absent · **negative stem (EXCEPT)** — blank on free recall, Sep 5

**Structure.** What is transferred is a **fact** — advice, guidance, an explanation, a referral. The recipient still has to do the thing.
**Concrete.** Mr. Okonkwo asks what the nephrologist meant by "clearance." His sister reads the note back to him, tells him what number they want, and what happens if it keeps falling.
**Claims.** Asserts the resource is knowledge for solving the problem. Denies the instrumental reading — nobody did anything *for* him — and denies the appraisal reading: this is information about the **world**, not about **him**.
**Predicts.** Look for *explained, advised, suggested, told him how.* Where one person both explains a treatment and arranges it, the item will separate the two acts, and the explaining half is informational.

#### Appraisal support
FL1: Q209 · CC8C · knowledge absent · **negative stem (EXCEPT)** — blank on free recall, Sep 5

**Structure.** What is transferred is **feedback** — information the person uses to evaluate himself: affirmation, comparison, a verdict on how he is doing.
**Concrete.** His sister tells him he has missed one session in eight months and that this is better than he thinks he is doing. She is not comforting him and she is not explaining dialysis; she is handing him a measure of his own performance.
**Claims.** Asserts the content is **self-relevant evaluation**. Denies the emotional reading — what crossed was a judgement, not a feeling — and denies the informational reading, because the fact is about him rather than about the illness.
**Predicts.** Look for *evaluated, affirmed, gave feedback, helped him judge how he was doing.* Against emotional support the split is one question: **is the content about how he feels, or about how he is doing?** This is the type least likely to be on his list, which on an EXCEPT stem makes it the trap — unfamiliar is not the same as not a type.

#### Companionship (belonging) support
FL1: Q209 · CC8C · **negative stem (EXCEPT)**

**Structure.** What is transferred is **presence** — shared time and the sense of belonging, with no content at all.
**Concrete.** His sister sits in the dialysis waiting room for the full four hours with a magazine. They exchange perhaps ten sentences. She was there.
**Claims.** Asserts co-presence is itself a resource, distinct from the empathy that emotional support transmits. Claims nothing against the other four: the standard taxonomy names four types and some sources add this as a fifth.
**Predicts.** On "all of the following are types of social support EXCEPT," companionship is a **true option, not the key.** The keys on that item are things that are not support at all — financial strain, network size, obligation — or the assertion that more ties are always better.

#### The two models of how social support reaches health
FL1: Q209 · CC8C · **negative stem (EXCEPT)** · knowledge absent

**Structure.** Two competing accounts of the support→health link.

| Model | When support helps | Through what |
|---|---|---|
| **Direct (main) effect model** | **at every level of stress** | everyday social integration: better health behaviours, more health information, normative pressure to seek care, less loneliness, lower baseline physiological arousal, a sense of purpose and identity |
| **Stress-buffering model** | **mainly or only under stress** | **appraisal** — the threat looks manageable, coping resources look adequate — and dampening the physiological stress response |

| Mechanisms that are real — the true options on an EXCEPT item | Mechanisms that are not — therefore the keys |
|---|---|
| reduced cortisol and sympathetic reactivity | support does not remove the underlying pathology |
| improved immune function | it does not work through the person's genetic risk |
| better treatment adherence and health behaviour | it does not work by increasing obligations or demands |
| earlier care-seeking | **larger networks are not monotonically better** — support can be experienced as burden, criticism, or obligation |
| reduced depression and anxiety | it is not the *number* of ties but the perceived adequacy of them that predicts outcomes |
| buffered appraisal of threat | |
| increased sense of control | |

**Concrete.** Under the direct model the sister's nightly calls help whether or not anything is
wrong — he eats better and takes the phosphate binders. Under buffering they do nothing
measurable most weeks and everything on the day the biopsy result comes back.

**Claims.** Buffering asserts support acts *on the stress process itself*, therefore **denying
a uniform benefit**. The direct model asserts it works through everyday integration, therefore
denying that stress is required. Not two descriptions of one finding: they disagree about the
low-stress group.

**Evidence.** They make **different predictions in the low-stress group** and the same
prediction in the high-stress group — which is what makes them testable. Buffering predicts an
**interaction** between support and stress; the direct model predicts a **main effect** of
support with no interaction.

**Predicts.** Benefit only in the high-stress group → **buffering**. Benefit at all stress
levels → **direct effect**. On the EXCEPT item, convert first: *"Three of these ARE mechanisms by
which social support benefits health; which is not?"* The key is either a mechanism from a
different construct entirely, or the assertion that more ties are always better.

#### Direct (main) effect model
FL1: Q209 · CC8C · **negative stem (EXCEPT)** · knowledge absent

**Structure.** Being socially integrated benefits health **at every level of stress**, through everyday channels: better health behaviour, more health information, normative pressure to seek care, less loneliness, lower baseline arousal, a sense of purpose.
**Concrete.** Take two of Dr. Reyes's patients in an ordinary month with nothing wrong. The one whose sister calls every night is doing better than the one who lives alone — better adherence, earlier appointments, lower resting pressure. The model's whole content is that this gap exists **when nothing is happening.**
**Claims.** Asserts stress is not required for support to pay. Denies buffering's central claim that support acts on the stress process, and therefore denies that the unstressed have nothing to gain.
**Evidence.** Statistically this is a **main effect of support with no support × stress interaction**, and it is what network and social-integration measures typically produce.
**Predicts.** A study finding supported people healthier across the whole stress range → direct effect. On a graph of outcome against stress, this model is **two roughly parallel lines** — parallel lines *are* the absence of an interaction.

#### Stress-buffering model
FL1: Q209 · CC8C · **negative stem (EXCEPT)** · knowledge absent — answered correctly but unsure, Sep 5

**Structure.** Support acts **on the stress process itself**: it changes appraisal — the threat looks smaller, coping resources look adequate — and dampens the physiological response. Under low stress there is nothing to buffer.
**Concrete.** The same two patients on the day the biopsy result comes back. Now the one with the nightly calls is measurably steadier and the one who lives alone is not. Through the eleven ordinary weeks before it the two looked identical — and **that identical stretch is the model's real claim**, not the divergence.
**Claims.** Asserts a conditional benefit, therefore **denying a uniform one**. Denies that the two models are one finding described twice: they agree about the high-stress group and disagree about the low-stress group, and only the low-stress group can decide between them.
**Evidence.** This is an **interaction** between support and stress, and it appears with *perceived, functional* support — support matched to what the stressor actually demands — rather than with counts of ties.
**Predicts.** Benefit only in the high-stress group → buffering. Benefit at all levels → direct effect. **One question decides it: what happens in the low-stress group?** On a graph, buffering means lines that converge or cross; any separation at the left-hand end of the stress axis rules buffering out.

#### Synchronous behaviour
FL1: Q197 · CC7B/8C · Skill 2 · knowledge absent

**Structure.** Moving in time with others raises in-group bonding.

| | |
|---|---|
| **The acts** | chanting, marching, rowing, singing, clapping, dancing |
| **What it increases** | **group cohesion, rapport, liking, trust, perceived similarity, cooperation, prosocial behaviour toward the group, and conformity within it** |
| **Side effects** | blurs the self–other boundary; raises pain thresholds via endorphin release; can increase out-group derogation |

**Concrete.** A hospital waiting-room drumming session. Twenty minutes later the participants
sit closer together, say "we" about what happened, help a stranger from the group pick up
dropped papers, and rate the group's opinion as closer to their own than it is.

**Claims.** Affiliation **without any shared goal, belief, or communication.** Denies that
solidarity requires common interest or shared identity — temporal coordination suffices.
Durkheim's *collective effervescence* is the same claim at the level of ritual.

**Predicts.** "Engaging in synchronous behaviours is most likely to lead to:" → increased
**cohesion, affiliation, cooperation, trust, or conformity** within the group. **Not** individual
performance, creativity, or individuation. If **deindividuation** is offered, split on the stem:
*bonding and liking* → synchrony/cohesion; *lost self-awareness and restraint, often
antinormative* → deindividuation.

#### Status, role, and self-presentation — the 8C vocabulary
FL1: Q222 support · CC8C

**Structure.** Four families of terms: status, role, group, organization — plus self-presentation.

| Family | Term | What it means |
|---|---|---|
| Status | **achieved** | earned through action |
| Status | **ascribed** | assigned at birth or involuntarily |
| Status | **master status** | the one that dominates how others see you |
| Status | **status set** | all of them |
| Role | **role conflict** | tension **between two different roles** |
| Role | **role strain** | tension **within a single role** |
| Role | **role exit** | disengaging from a role and building a new identity |
| Group | **primary** | small, intimate, enduring, an end in itself |
| Group | **secondary** | large, impersonal, goal-directed |
| Group | **in-group vs out-group** | the group you belong to vs the one you do not |
| Group | **reference group** | whose standards you use for comparison — you need not be a member |
| Group | **aggregate** | co-located, no interaction |
| Group | **category** | shares a trait only |
| Organization | **formal organization** | deliberately structured |
| Organization | **bureaucracy** | the specific rational-legal hierarchical form |
| Organization | **iron law of oligarchy** | a perspective on bureaucracy: all organizations drift toward rule by a few |
| Organization | **McDonaldization** | a perspective on bureaucracy: efficiency, calculability, predictability, control |
| Self-presentation | **front stage vs back stage** | Goffman's dramaturgy |
| Self-presentation | **impression management** | controlling others' perceptions |
| Self-presentation | **self-monitoring** | the *trait* of adjusting self-presentation to the situation |

**Concrete.** Dr. Reyes is a physician — **achieved**. On call the night of her son's school
play: two roles, incompatible demands, **role conflict**. Inside the physician role alone,
deliver a devastating result gently *and* move on in eight minutes: **role strain**. Her manner
at the bedside versus the workroom: **front stage**, **back stage**. Her sister's family,
measured against without belonging to: a **reference group**.

**Claims.** Every term names a **position or a performance, not a person**: status is a
position, role is what it requires, strain is between requirements, not inside a personality.
Denies the dispositional distractor — that the conflict is about her character rather than the
structure she occupies.

**Predicts.** Role items resolve on a count: **how many roles?** Two → conflict, one → strain.
Group items on **intimacy and purpose**: intimate, an end in itself → primary; impersonal,
instrumental → secondary. Self-presentation items on **act or disposition**: controlling
perceptions → impression management; a trait of adjusting to context → self-monitoring.

#### Master status
FL1: Q222 support · CC8C

**Structure.** One status in the set overrides the rest and organizes how everyone else reads you. It can be achieved or ascribed, and you do not choose which one it is.
**Concrete.** Mr. Okonkwo is a machinist, a father, a deacon and a Tuesday–Thursday dialysis patient. On the ward he is the dialysis patient in bay 4, and the residents discussing him do not know the other three exist.
**Claims.** Asserts the dominance is conferred by the **audience**, not by the person's own ranking of his identities. Denies that it is simply the status that matters most to him — and against **status set**, which is merely all of them held at once with no hierarchy claimed.
**Predicts.** An item describing one characteristic that shapes how others treat him in every setting is asking for master status; an item listing several positions a person occupies is asking for status set. Illness, disability and a criminal record are the standard examples.

#### Primary group
FL1: Q222 support · CC8C

**Structure.** Small, face-to-face, enduring, emotionally involving — and it exists **for its own sake**. The relationships are the point.
**Concrete.** Mr. Okonkwo's sister and the household she drives from. Nobody joined it to accomplish anything, no member could be swapped for an equivalent, and it would carry on if the dialysis stopped tomorrow.
**Claims.** Asserts the defining feature is **purpose**, not size — a three-person work team is not a primary group. Denies that closeness is the criterion: a secondary group can contain a real friendship without becoming primary.
**Predicts.** A group described as intimate, long-lasting and an end in itself → primary. Expect the distractor to be a small group with a task attached; check whether the members exist for the group or the group exists for a job.

#### Secondary group
FL1: Q222 support · CC8C

**Structure.** Larger, impersonal, often time-limited, organized around a **goal**; members are interchangeable occupants of roles.
**Concrete.** The dialysis unit's staff. Mr. Okonkwo knows two of them by name; if either leaves, the chair is still filled at six on Tuesday and his treatment does not change. The unit exists to clear his blood, not to know him.
**Claims.** Asserts **interchangeability** is the diagnostic: the group survives replacement of any member because roles hold it together, not people. Denies that coldness or formality is what makes it secondary — the staff can be warm and it is still a means to an end.
**Predicts.** A group defined by its function with replaceable members → secondary. On an item contrasting the two, the split is one question: **is the group an end in itself, or a means to something else?**

#### Reference group
FL1: Q222 support · CC8C

**Structure.** The group whose standards you use to judge yourself. **Membership is not required** — comparison is.
**Concrete.** Mr. Okonkwo reads a forum of transplant recipients every night and has never posted. He is not one of them and he will measure this year against them anyway. The people he actually sits beside on Tuesdays are his in-group, and they are not the yardstick.
**Claims.** Asserts the **evaluative function** defines it, so a reference group can be one you are excluded from, aspire to, or have left. Denies the in-group reading: belonging and comparing are different relations and routinely point at different groups.
**Predicts.** Someone judging his situation against a group he does not belong to → reference group, and relative deprivation is what it produces. **One question: does he belong to it, or does he measure by it?** Belonging alone is in-group.

#### Bureaucracy

**Structure.** The rational-legal form of a formal organization: division of labour, a hierarchy of authority, explicit written rules, impersonality, and appointment by technical qualification.
**Concrete.** Mr. Okonkwo's transplant referral needs prior authorization. There is a form, a named reviewer, a stated appeal level above her, and a rule that decides the case. The form has no field for the fact that he is frightened, and adding one would break it.
**Claims.** Asserts impersonality is a **design feature**, not a failure — treating like cases alike requires ignoring the person. Denies that any organized group qualifies: a **formal organization** is any deliberately structured group, and bureaucracy is one specific form of it.
**Predicts.** A vignette emphasizing written rules, hierarchy, and identical treatment regardless of who applies → bureaucracy. Expect the item to offer the cost — rigidity, red tape, alienation, ritualism — as a **correct** consequence, because the same features produce both halves.

#### Iron law of oligarchy

**Structure.** Every organization, however democratic at founding, drifts toward rule by a small group — because running it requires delegation and expertise, and the delegates acquire interests of their own.
**Concrete.** The clinic starts a patient advisory council so patients have a voice. Two years on, three long-standing members set every agenda and know procedures nobody else has read; the remaining twelve vote on what those three bring.
**Claims.** Asserts the drift is **structural and therefore inevitable** — nobody seized anything. Denies the corruption reading: no bad actor is required, only the fact that organizing requires organizers.
**Predicts.** A democratic body concentrating power over time, with no misconduct anywhere in the stem → iron law of oligarchy. If the stem supplies a villain, the item is testing something else.

#### McDonaldization

**Structure.** Bureaucratic rationality spread through everyday life on four dimensions: **efficiency, calculability, predictability, control** — with control increasingly by technology rather than by people.
**Concrete.** Mr. Okonkwo's dialysis: a four-hour slot, a scripted intake, a target number that defines success, the identical protocol in every chair, and a machine that alarms rather than a nurse who notices. Any unit in the region would run him the same way.
**Claims.** Asserts these processes deliver real gains **and** produce irrational outcomes through rationality itself — the system optimizes what it can measure and loses what it cannot. Denies that this is a claim about restaurants or business: it is aimed at hospitals, universities and clinics.
**Predicts.** Standardization, quantified targets, scripted interaction or deskilling in the stem → McDonaldization, and the correct consequence is **loss of what the metrics do not capture.** If the stem is instead about power concentrating in a few hands, the answer is the iron law.

#### Front stage and back stage
FL1: Q222 support · CC8C

**Structure.** Goffman's dramaturgy: social life is performance, and behaviour splits by **region** — front stage where an audience is present, back stage where it is not and the performance is prepared.
**Concrete.** Dr. Reyes reads the biopsy number in the workroom, says something short and unrepeatable, arranges her face, and pushes the door open. The door is the region boundary, and nothing about her sincerity changed as she crossed it.
**Claims.** Asserts the split is about **where you are and who is watching**, not about a true self against a false one — the back region is another performance, for a different audience. Denies the cynical reading that the front stage is a lie.
**Predicts.** An item contrasting how someone behaves with patients against how they behave among colleagues is asking for front stage/back stage. The three self-presentation terms divide cleanly: **region** here, the **act** is impression management, the **trait** is self-monitoring.

#### Impression management
FL1: Q222 support · CC8C · **the pair he answered wrong cold, Sep 5**

**Structure.** The **act** of controlling the impression other people form of you — what you do, in this situation, to shape their perception.
**Concrete.** Dr. Reyes sits down instead of standing, slows her speech, and leaves the pager in her coat so Mr. Okonkwo will see someone unhurried. Three specific things done to produce one impression in one person.
**Claims.** Asserts the target of the management is **other people's minds**, never your own self-concept. Denies that it implies dishonesty — managing an accurate impression is still managing it — and denies that it is a personality variable: it is behaviour, and anyone can do it on a given afternoon.
**Predicts.** An item describing what someone **did** in order to be perceived a certain way → impression management. If the item instead describes how much a person characteristically varies from room to room, it has moved to self-monitoring.

#### Self-monitoring
FL1: Q222 support · CC8C · **answered wrong cold, Sep 5 — given as "managing how you see yourself"**

**Structure.** The **trait**: how much a person reads situational cues and adjusts self-presentation to fit them. High self-monitors change across rooms; low self-monitors behave the same everywhere, out of internal dispositions.
**Concrete.** The liaison speaks one way to Mr. Okonkwo's family, another to the nephrologist, another to the billing desk, and is fluent in all three — a high self-monitor. The senior resident uses one register with all three and does not notice the difference — a low self-monitor. Neither is thinking about their self-image; both are being read by other people.
**Claims.** **The "self" in the name is what gets adjusted, not what gets watched.** This is not self-awareness, not self-esteem, and not managing how you see yourself: exactly like impression management, it is about how **others** see you. What separates them is that impression management is an **act** and self-monitoring is a **stable disposition** to perform such acts sensitively.
**Predicts.** "Which construct explains why this person behaves differently in every room?" → self-monitoring. "Which names what she did in the room?" → impression management. **One question splits them: act, or trait?** Any option glossing self-monitoring as introspection, self-evaluation or self-concept is the distractor, and it is wrong.

**Discriminators**
- **Dyad vs triad** — can a coalition form, and does the group survive one member leaving?
- **Emotional vs appraisal support** — comfort about a feeling, or feedback about a performance?
- **Informational vs instrumental support** — was advice given, or was something done?
- **Direct effect vs stress-buffering** — does support help everyone, or only the stressed?
  (Main effect vs interaction.)
- **Synchrony vs deindividuation** — bonding and liking, or lost restraint?
- **Role conflict vs role strain** — two roles, or one?
- **Achieved vs ascribed status** — earned, or assigned?
- **Master status vs status set** — the one that overrides, or all of them?
- **Primary vs secondary group** — an end in itself, or a means to a goal?
- **Reference group vs in-group** — whose standards you use, or where you belong?
- **Impression management vs self-monitoring** — the behaviour, or the trait?
- **Formal organization vs bureaucracy** — any structured group, or the rational-legal form?
- **Altruism vs reciprocal altruism vs inclusive fitness** — no return, delayed return, or
  return through shared genes?

**Compression — how many people the concept requires**

| Number | Concepts |
|---|---|
| 1 | achieved/ascribed status, role exit, role strain |
| 2 | dyad, role conflict, a support tie, front stage/back stage, attraction, attachment, **master status**, **impression management**, **self-monitoring** |
| 3 | triad, coalition, mediator, the tertius role |
| small group | primary group, cohesion, synchrony, in-group/out-group, group size effects |
| large group | secondary group, formal organization, bureaucracy, network, diffusion of responsibility |
| population | iron law of oligarchy, McDonaldization, institutional discrimination |

**Reference group is the one entry that does not sort on this axis** — a family, a cohort, or an
entire profession all qualify. Size is not the constraint; what matters is that you measure
yourself against it and need not belong to it.

AAMC returns to dyad→triad because it is the only place where adding **one** person changes the
*kind* of thing the group is.

---

### CLUSTER 6 — SOCIAL STRUCTURE AND DEMOGRAPHICS (CC9A / CC9B)

**FL1: Q201, Q206, Q208, Q224 · CC9B was 1/4 — 25%, the worst content category on the exam.**
Two are negative stems (Q201 LEAST, Q206 NOT); sociology overall was your weakest discipline at
65%. This cluster plus the negative-stem procedure is the largest recoverable block in P/S.

*Shared scene:* **Riverside, one neighbourhood, forty years. Hmong families arrive in the 1980s.
The factory closes in 1996. Affluent buyers arrive after 2015. The people who stayed got old.**

#### Assimilation and its alternatives
FL1: Q206 · CC9A · Skill 1 · knowledge absent · **negative stem (does NOT identify)**

**Structure.** Four outcomes when a minority group meets a dominant culture, plus one opposite pole.

| Outcome | What happens to the minority group's distinct identity | Who changes |
|---|---|---|
| **Assimilation** | takes on the dominant culture's patterns; the distinct identity **fades**. A multi-generational *process* with two halves: **cultural** (language, dress, norms, food) and **structural** (entering mainstream institutions, occupations, neighbourhoods, intermarriage) | the minority only |
| **Acculturation** | adopts some traits of the new culture **while retaining the original identity**. The reversible first stage | the minority, partly and reversibly |
| **Amalgamation** | the two blend into something new. The "melting pot." | **both** |
| **Multiculturalism / pluralism** | distinct cultures persist side by side with mutual respect; the dominant culture does not absorb them | neither |
| **Segregation** | enforced separation. The opposite pole | neither — separation is imposed |

| Aspects of assimilation an item may name as true | Statements that are NOT assimilation — therefore the keys on a negative stem |
|---|---|
| loss of the heritage language across generations | keeping the heritage language while adding the new one (acculturation, bilingualism) |
| intermarriage with the dominant group | the **dominant** culture adopting minority practices (diffusion, or amalgamation) |
| dispersion out of ethnic enclaves | enforced separation (segregation) |
| adoption of dominant norms and dress | a genuinely new hybrid culture emerging (amalgamation) |
| declining ethnic self-identification | institutions funding and celebrating distinct traditions (multiculturalism) |
| entry into mainstream institutions and occupations | anything that **preserves** the group's distinct identity |
| **asymmetry** — the minority changes far more than the dominant group | |
| it may be voluntary or coerced | |

**Concrete.** Riverside's Hmong community, four ways. Grandchildren speak only English, marry
out, move to the suburbs: **assimilation.** Parents speak Hmong at home, English at work, and
identify as Hmong: **acculturation.** A food and festival culture emerges that is neither Hmong
nor what preceded it: **amalgamation.** The city funds a Hmong cultural center and the community
persists as itself: **multiculturalism.**

**Claims.** Asserts the **distinct identity disappears into the dominant one** and the change is
**one-directional** — the asymmetry that discriminates it from amalgamation, where both sides
change. Denies that maintaining identity while functioning in the dominant culture counts: that
is acculturation, the option AAMC uses as the trap.

**Predicts.** On "which does NOT identify an aspect of assimilation," convert to *"three of
these ARE aspects of assimilation."* Then score each on one question: **does the minority group's distinct identity
get smaller, and is the change one-directional?** The odd one out preserves the identity, or has
the dominant culture changing.

#### Assimilation
FL1: Q206 · CC9A · Skill 1 · knowledge absent · **negative stem (does NOT identify)**

**Structure.** The minority group's distinct identity shrinks across generations as it takes on the dominant culture's patterns — cultural first (language, dress, food), structural second (schools, jobs, neighbourhoods, intermarriage) — while the dominant group barely moves.
**Concrete.** Mai arrives in Riverside in 1984 speaking Hmong. Her son Tou speaks it to her and English everywhere else. Tou's daughter Chloe, born 2010, knows three words of it, will marry out, and lives in a suburb her grandmother could not have bought into. Three generations, one direction.
**Claims.** Asserts the change is **one-directional and cumulative**: what shrinks is the minority group's distinctness, and what it disappears into does not change to meet it. Denies that living successfully inside the dominant culture is itself assimilation — Tou does that while remaining Hmong, and that is acculturation. Denies that assimilation must be voluntary or must be coerced; it is defined by the outcome, not by the pressure.
**Predicts.** On a stem naming assimilation, the credited option has the minority group's distinctness getting smaller. On "which does NOT identify an aspect of assimilation," the key either **preserves** the distinct identity or has the **dominant** group doing the changing.

#### Cultural assimilation
FL1: Q206 · CC9A · supports

**Structure.** The first half, and the fast one: language, dress, food, holidays, accent, name — the visible surface of a way of life is replaced by the dominant one's, with no change in where the group lives or works.
**Concrete.** Tou's household by 2005: English at dinner, a Christmas tree beside the household spirit shelf, hotdish at the block potluck. Same house on the east side, same second-shift job, same friends. The surface converted; the position did not.
**Claims.** Asserts culture can convert while structure holds — often inside a single generation. Denies that speaking the language and eating the food proves a group has assimilated: the structural half can lag by two generations or never arrive.
**Predicts.** An item describing language loss, dress, or name changes and saying nothing about jobs, housing, or intermarriage is testing this half only. Expect a distractor calling it complete assimilation.

#### Structural assimilation
FL1: Q206 · CC9A · supports

**Structure.** The second half, and the slow one: the group enters the dominant society's institutions — schools, occupations, neighbourhoods, clubs, and finally its families through intermarriage — so that group membership stops predicting where a person ends up.
**Concrete.** Chloe at the state university, in a firm with no other Hmong employees, in a suburb under one percent Hmong, marrying out. Nothing about her position traces back to Mai's 1984 arrival.
**Claims.** Asserts this half requires the dominant society to **admit** the group, so it can be blocked from outside — by discrimination, by lending, by segregation — no matter how completely the cultural half has run. Denies that assimilation is something a minority does entirely to itself.
**Predicts.** Intermarriage and residential dispersion are AAMC's markers for this half, and it is the half a discrimination passage shows failing. **Cultural without structural** is the profile of a group that lost its language and still cannot get in.

#### Acculturation
FL1: Q206 · CC9A · **trap — the option AAMC builds against assimilation**

**Structure.** Take on traits of the new culture **and keep the original identity**: the group ends up holding two cultures rather than swapping one for the other, and the move is reversible.
**Concrete.** Tou exactly. Hmong at his mother's table, English at work; New Year at the community hall in November and the Fourth of July on the lake. Ask him what he is and he says Hmong. Nothing was traded away.
**Claims.** Asserts **addition, not replacement** — competence in the dominant culture without loss of the original. Denies that fluency in the dominant culture implies the distinct identity is going. It is also the *first stage of* assimilation in Gordon's sequence, which is why the two swap so easily: the same behaviour can be an endpoint or a way station, and only the identity question separates them.
**Predicts.** Any option with a group speaking the new language **while** keeping the old, or observing both sets of holidays, is acculturation. On "does NOT identify an aspect of assimilation," an option that preserves the heritage identity is the key; on a positive stem it is the trap.

#### Amalgamation
FL1: Q206 · CC9A · supports

**Structure.** Two cultures blend into a third that is neither parent — the melting pot — so **both** sides change and neither original survives intact.
**Concrete.** Riverside's summer street fair by 2005: egg rolls in a brat bun, a polka band with a qeej player sitting in, a dish nobody's grandmother in either country would recognize. What is on the table came from both sides and belongs to neither.
**Claims.** Asserts **symmetry** — the dominant group is altered too. Denies the one-directional picture that defines assimilation. Covers intermarriage producing a mixed population as well as the emergence of a new cultural form.
**Predicts.** Look for the word **both**, or for a new thing named that did not exist before. If the dominant culture is described as changing, the answer is amalgamation, never assimilation — and on a negative stem an amalgamation option is a live key.

#### Multiculturalism / pluralism
FL1: Q206 · CC9A · supports

**Structure.** Distinct cultures persist side by side with mutual recognition and equal standing; the dominant culture neither absorbs them nor pushes them out, and difference is treated as a public good.
**Concrete.** Riverside in 1998 funds a Hmong cultural center on Bell Street, prints ballots in Hmong, and puts the New Year on the city calendar. Mrs. Vang's grocery stays open because the community stays intact enough to shop there. Nobody merged with anybody.
**Claims.** Asserts distinctness **survives, by design and with institutional support**. Denies assimilation (identity survives) and denies amalgamation (no third culture forms). Denies that separateness implies inequality — which is exactly what separates it from segregation.
**Predicts.** Institutional support for distinct traditions — funding, bilingual services, official recognition — is the marker. On "does NOT identify an aspect of assimilation," this is the most common key, because it is the opposite outcome and still sounds like a good thing.

#### Segregation
FL1: Q206 · CC9A · supports

**Structure.** The groups are kept apart and the separation is **imposed** — by law, by lending, by zoning, by steering, by violence — so contact between them cannot produce any of the other four outcomes.
**Concrete.** Riverside's Hmong families landed on the east side in the 1980s and stayed there, because the banks would not write mortgages west of the tracks and the realtors did not show those houses. Not a preference. A boundary.
**Claims.** Asserts the separation is **coerced and unequal in power**, which distinguishes it from multiculturalism, where separateness is chosen and equal. Denies that residential clustering is by itself segregation — an enclave people choose is a different object. Denies that repealing the law ends it: **de facto** segregation persists through price and lending after **de jure** segregation is gone.
**Predicts.** Look for a named mechanism of enforcement — redlining, covenants, steering, school boundaries. If one is there, it is segregation. If the clustering is chosen and resourced, it is an enclave or multiculturalism.

#### Ethnic enclave
FL1: Q206 · CC9A · supports

**Structure.** A concentrated neighbourhood where a group's own institutions — shops, worship, language, credit, jobs — run at enough scale that a member can live a full life inside it; the clustering is **chosen** and functions as a resource.
**Concrete.** Bell Street in 1994: Mrs. Vang's grocery, a Hmong-language church, a clan association that lends toward a down payment, and two employers who hire on a cousin's word. Mai never needed English to get through a week.
**Claims.** Asserts concentration can be an **asset** — it lowers the cost of arrival and supplies capital and jobs the dominant economy withholds. Denies that living apart is always exclusion, and denies that leaving is always progress: dispersion out of the enclave is an assimilation marker and it costs the network.
**Predicts.** Enclave items turn on whether the clustering is chosen and resource-bearing (enclave) or imposed and resource-stripping (segregation). "Dispersion out of ethnic enclaves" in a list is a true aspect of assimilation — therefore a wrong answer on a negative stem.

#### Cultural diffusion
FL1: Q206 · CC9A · **trap — the arrow reverses**

**Structure.** A practice, object, or idea spreads **from** one culture **to** another; nothing about the sender's identity changes, and the borrower is frequently the dominant group.
**Concrete.** By 2018 the coffee roaster on the corner sells a Hmong sausage sandwich to buyers who moved in from three states away, and none of them will ever be Hmong. The trait crossed. Nobody was absorbed.
**Claims.** Asserts only that a **trait moved**, and says nothing about identity, power, or outcome. Denies that the dominant culture picking something up is evidence of assimilation — the arrow points the wrong way. Denies that it yields a blended culture; when both sides fuse into a third thing, that is amalgamation.
**Predicts.** Check the direction of the arrow before naming any term in this set. **Minority adopts dominant → assimilation or acculturation. Dominant adopts minority → diffusion.** On "does NOT identify an aspect of assimilation," an option with the dominant culture adopting a minority practice is a key.

#### Gentrification and urban change
FL1: Q201 · CC9B · Skill 2 · knowledge absent · **negative stem (LEAST likely)**

**Structure.** The arc AAMC uses, in order.

| Stage | What happens |
|---|---|
| **Urbanization** | industrialization concentrates population in cities |
| **Suburbanization and urban decline** | out-migration to the periphery, disinvestment, white flight |
| **Gentrification** | higher-income residents move into a disinvested urban neighbourhood; property values and rents rise; the built environment is upgraded |
| **Urban renewal** | the alternative endpoint: planned, often state-led redevelopment |

| Effects that ARE likely — the true options on a negative stem | Effects that are LEAST likely — the keys |
|---|---|
| rising property values, rents and property taxes | decreased property values or rents |
| **displacement** of lower-income and often minority long-term residents | increased affordable housing |
| changed racial and class composition | increased residential stability for the existing low-income residents |
| new retail aimed at the incoming population and closure of businesses serving the old one | improved circumstances for the displaced residents themselves |
| **falling measured poverty and crime rates in the tract** — because of who now lives there, not because anyone's circumstances improved | reduced segregation across the metro area (it typically relocates segregation rather than reducing it) |
| increased public and private investment | |
| reduced affordable housing supply | |
| cultural displacement and loss of community networks even for those who stay | |
| political conflict over development | |

**Concrete.** Riverside after 2015: a coffee roaster where the laundromat was; a two-flat at
four times its 2008 price; the Hmong grocery closed; median income up 40% — while most families
who lived there in 2008 are two miles west in worse housing, and out of the tract's statistics
entirely.

**Claims.** Improves the **place**, not **the people who were there**. Denies the
neighbourhood-effects optimism that reads improving tract statistics as improving resident
fortunes: the statistics changed because the denominator changed. **Place versus people answers
most gentrification items.**

**Predicts.** On a LEAST-likely item, convert, then run every option through one question:
**does this follow from richer people arriving and rents rising?** Anything requiring rents to
fall, housing to become more affordable, or the original residents to stay and prosper is the
answer.

#### Urbanization
FL1: Q201 · CC9B · supports

**Structure.** Population concentrates **into** cities from outside them, usually pulled by industrial jobs, so the urban share of a whole society's population rises.
**Concrete.** Riverside exists because of the factory. Between 1910 and 1950 farm families moved into the ward to work it, and blocks of two-flats went up to hold them. Nobody was displacing anybody; there was nothing here before.
**Claims.** Asserts a change in **where a society's population sits** — country to city. Denies that it says anything about which city-dwellers change places: urbanization moves people in from outside, gentrification rearranges people already inside. Denies the folk equation with sprawl; suburbanization runs the other way.
**Predicts.** Rural → urban at the scale of a country or region is urbanization. Richer resident → existing neighbourhood at the scale of a few blocks is gentrification. Urbanization and stage-2 demographic transition arrive together.

#### Urban decline (disinvestment)
FL1: Q201 · CC9B · supports

**Structure.** Capital leaves a neighbourhood — employers, mortgages, maintenance, tax base, services — the built environment deteriorates, and whoever can leave does.
**Concrete.** Riverside from 1996: the factory shuts, 1,400 jobs go, the bank stops writing mortgages on Bell Street, the city cuts the bus line, and by 2004 a third of the two-flats have absentee owners and bad roofs. The east side did not get poorer because its people changed. The money left.
**Claims.** Asserts the driver is **withdrawn investment**, not resident behaviour or culture. Denies the culture-of-poverty reading of a declining neighbourhood. Denies that decline is passive — redlining, disinvestment, and highway routing are decisions somebody made.
**Predicts.** Decline **precedes** gentrification and is what makes property cheap enough for it, so a passage can use both about one tract without contradiction. Lost jobs, lending, and services → decline. Who moved out, and their race → white flight.

#### White flight
FL1: Q201 · CC9B · supports

**Structure.** A racialized out-migration: white residents leave as Black or immigrant residents arrive, taking the tax base and the lending with them, and the neighbourhood's composition flips.
**Concrete.** Riverside's west side, 1984 to 1991. The Hmong families arrive on the east side; the white families on the west side sell within seven years and buy in the townships. The houses did not deteriorate first. The neighbours changed first.
**Claims.** Asserts the **trigger is who arrived**, not what happened to the housing — the causal order is the whole content. Denies the neutral economic story in which residents left because the neighbourhood declined; here the departure produced the decline. Denies that it requires individual animus: a tipping point needs only the expectation that others will go.
**Predicts.** Arrival by one group, departure by another, departure following arrival → white flight. Money leaving first with no racial trigger named → urban decline. White flight plus disinvestment is what makes a tract cheap; gentrification is the same tract twenty years later.

#### Gentrification
FL1: Q201 · CC9B · Skill 2 · knowledge absent · **negative stem (LEAST likely)**

**Structure.** Higher-income residents move **into** a disinvested urban neighbourhood; rents, prices, and taxes rise; buildings and retail are upgraded; and the lower-income residents who were there are pushed out.
**Concrete.** Riverside after 2015. Dana buys the two-flat on Bell Street for four times its 2008 price; the laundromat becomes a coffee roaster; Mrs. Vang's grocery closes because her customers left; median household income in the tract rises 40% — while most families who lived here in 2008 are two miles west in worse housing and out of the tract's statistics entirely.
**Claims.** Asserts the neighbourhood improves and **the people who were in it do not** — the tract's improving numbers are the arithmetic of who is now being counted. Denies the neighbourhood-effects reading of those numbers: the denominator changed. Denies that falling tract poverty and crime mean anyone's poverty or victimization fell.
**Predicts.** Every true option follows from *richer people arrive, rents rise*. On LEAST-likely, the key requires rents to fall, housing to become more affordable, the original residents to stay and prosper, or metro segregation to drop. **Place versus people answers most gentrification items.**

#### Urban renewal
FL1: Q201 · CC9B · supports

**Structure.** Planned, state-led redevelopment: a public authority designates an area, clears or rebuilds it, and finances the replacement — the change is decided in an office, not produced by a market of individual buyers.
**Concrete.** In 1998 Riverside's council votes the old factory parcel "blighted," condemns four blocks around it with federal money, and puts up a medical campus and a parking structure. The 200 households on those blocks got relocation notices, not rent increases.
**Claims.** Asserts the **agent is the state and the instrument is a plan** — eminent domain, designation, public financing. Denies that it is gentrification: displacement runs through condemnation rather than price, and it can happen with no higher-income buyers arriving at all. It produced the same outcome for the people cleared, which is why the two are confusable.
**Predicts.** Find the agent. Individual buyers and rising rents → gentrification. A city, an authority, a designation, a plan → urban renewal. Both displace; only one does it through the market.

#### Displacement
FL1: Q201 · CC9B · supports

**Structure.** The original residents are forced out — by rent, sale, non-renewal, tax increase, or condemnation — and because they leave the tract, they leave the data that describes it.
**Concrete.** The Yang family's rent on Bell Street goes from $650 to $1,400 between 2015 and 2019. They move two miles west into a worse unit with a longer bus ride to the same job. Riverside's poverty rate falls that year. Theirs went up.
**Claims.** Asserts that improvement measured **on a place** cannot be read as improvement **of the people** who were there, because the displaced are no longer in the sample. Denies the inference from a falling tract poverty rate to falling household poverty. This is the most-tested idea in the container.
**Predicts.** Whenever a gentrification item reports an improving tract statistic, ask **who is being counted now**. The credited option separates the place from the people; the trap reads the tract's number as the residents' outcome.

#### Cultural displacement
FL1: Q201 · CC9B · supports

**Structure.** The people stay but the neighbourhood stops being theirs: the shops, institutions, gathering places, and networks that served them are replaced by ones serving the newcomers.
**Concrete.** Mai still owns her house on Bell Street and is not going anywhere. But the grocery is a wine bar, the church rents its hall to a yoga studio, the two neighbours who drove her to appointments moved west, and the new residents have complained to the city about the New Year drumming.
**Claims.** Asserts displacement has a form that leaves the address unchanged — **loss of community and belonging without loss of housing**. Denies that staying means being unharmed, which is the assumption behind reading "residents who remained" as "residents who were fine."
**Predicts.** An option describing lost community networks, lost familiar businesses, or lost belonging among people who **did not move** is a true effect of gentrification, therefore a wrong answer on a LEAST-likely stem. Expect it as a distractor precisely because it sounds like a non-effect.

#### Residential segregation
FL1: Q201 · CC9B · supports

**Structure.** Groups live in separate areas within the same metro — a property measured **across the whole metro**, not inside one tract — produced by lending, zoning, steering, and price rather than by preference alone.
**Concrete.** Riverside's tract becomes more racially mixed after 2015; that is what Dana moving in does to the numbers. Meanwhile the Yangs and forty other families land in two far-west-side tracts that were 20% Hmong in 2010 and 55% Hmong in 2020. The metro's segregation did not fall. It moved.
**Claims.** Asserts segregation is a **metro-scale** property, so one tract's mixing tells you nothing about it. Denies that gentrification reduces segregation — it typically relocates it, which is why "reduced segregation across the metro area" is a key on a LEAST-likely stem. Denies that de jure repeal ended it.
**Predicts.** Watch the scale word in every option. "This neighbourhood became more mixed" can be true while "the metro became less segregated" is false, in the same passage, from the same facts.

#### Neighbourhood effects
FL1: Q201 · CC9B · **trap — the frame that hides the composition change**

**Structure.** The hypothesis that where you live causes your outcomes — that a better tract improves the health, schooling, and earnings of the people in it — which makes improving tract statistics look like improving lives.
**Concrete.** A 2021 city report shows Riverside's poverty down 12 points, crime down a third, test scores up, and concludes the redevelopment "lifted the neighbourhood's families." Every family it means is either still poor two miles west, or was never poor and arrived in 2017.
**Claims.** Asserts place causes outcomes: change the neighbourhood and you change the lives in it. Denies the compositional explanation — that a tract's numbers can move entirely by substitution of residents. That denial is what makes it the wrong answer here: after gentrification the compositional explanation is the correct one.
**Predicts.** When an item reports before-and-after tract statistics and offers a conclusion about residents, the credited answer names **composition** and the trap names the neighbourhood's effect on its residents. Same shape as the crude-rate trap in demographics — one is a neighbourhood, one is a population.

#### Demographic transition, population structure, and what "demographic" means
FL1: Q208 · CC9B · Skill 2 · knowledge absent

**Structure.** The four stages of the **demographic transition**, then the vocabulary that describes any point on it.

| Stage | Birth rate | Death rate | Population |
|---|---|---|---|
| 1. **Pre-industrial** | high | high | small and stable |
| 2. **Early industrializing** | stays high | **falls** — sanitation, food supply, medicine | **fastest population growth** |
| 3. **Maturing** | **falls** — urbanization, women's education and labour force participation, child survival improves so fewer births are needed, children shift from asset to cost, contraception | low | growth slows |
| 4. **Post-industrial** | low | low | stable or declining, and **aging** |

| Family | Term | What it means |
|---|---|---|
| Pyramid | **expansive** | wide base, high fertility — stage 2 |
| Pyramid | **constrictive** | base narrower than the middle, top-heavy — stage 4 with fertility **below** replacement |
| Pyramid | **stationary** | rectangular — stage 4 with fertility **at** replacement |
| Rate | **crude** rate | per 1,000 of the *total* population |
| Rate | **age-specific** rate | within one age band |
| Rate | **total fertility rate** | births per woman over a lifetime (~2.1 is replacement) |
| Rate | **fecundity** vs **fertility** | biological capacity vs actual births |
| Migration | **push** factors | drive people out of the origin — war, famine, unemployment, persecution |
| Migration | **pull** factors | attract them to the destination — jobs, safety, family, education |
| Migration | **immigration** vs **emigration** | in vs out — the same movement from two ends |
| Model | **Malthus** | population grows geometrically, food arithmetically, and the check is catastrophic — famine, war, disease |

**Concrete.** Riverside's crude death rate rose between 1996 and 2020 and **nobody got sicker.**
Young families left after the factory closed and were not replaced; median age went 28 → 44; more
old people, more deaths per 1,000 per year. The crude birth rate fell for the identical reason.
Every resident's risk could have improved and both rates would still have moved this way.

**Claims.** A **demographic explanation** attributes a rate change to the **composition of the
population** — who is in it — not to individual behaviour, risk, or policy. Denies the
behavioural reading of an aggregate statistic. The transition itself denies Malthus: fertility
fell **voluntarily**, with development, before any catastrophic check.

**Predicts.** Asked for a **demographic** explanation, pick the option about **who is in the
population** — age structure, migration, cohort size, fertility, mortality — not the one about
attitudes, motivation, effort, or policy. The **crude-rate trap** is the archetype: a crude rate
can move entirely because the age structure moved. Stage → pyramid; pyramid → stage.

#### Stage 1 — pre-industrial
FL1: Q208 · CC9B · Skill 2 · knowledge absent — the stage sequence

**Structure.** First of four positions on one axis — *which rate has fallen yet?* Neither. Birth rate high, death rate high, and the two cancel: the population is small and barely moves.
**Concrete.** Mai's mother, in a highland village in the 1940s: eight births, four children living at fifteen — the other four lost to fevers and a hungry spring. The village she died in had the same number of houses as the one she was born in.
**Claims.** Asserts that a high birth rate is what a high death rate *requires*: with half of children dying, seven or eight births is replacement, not excess. Denies that pre-industrial populations were growing — high fertility and zero growth are the same fact seen from two ends. Denies that the birth rate is the first thing to move; it is the last.
**Predicts.** A vignette with high fertility **and** high infant or child mortality **and** a stable total → stage 1. Its pyramid is wide at the base and tapers steeply, because death thins every age band. If the total is growing, you are already in stage 2.

#### Stage 2 — early industrializing
FL1: Q208 · CC9B · Skill 2 · knowledge absent — the stage sequence

**Structure.** Second position — *the death rate has fallen; the birth rate has not.* Sanitation, food supply and vaccination cut mortality within a generation while families keep having the number of children the old mortality demanded. The gap between the two rates is the fastest growth the population will ever see.
**Concrete.** Mai, in the camp clinic in 1979–84: a nurse, clean water, a vaccination card for each child. She has seven, like her mother — and all seven live. Nothing about how many children she wanted changed. What changed is that they stopped dying.
**Claims.** Asserts growth comes from mortality falling **first**, not from fertility rising — the birth rate in stage 2 is stage 1's birth rate. Denies that a population boom means people started having more children. Denies the Malthusian reading that this growth must end in catastrophe: in the next stage it ends in a decision.
**Predicts.** Falling death rate, unchanged birth rate, rapid growth, a very young population → stage 2. Its pyramid is the classic **expansive** triangle: a very wide base, each cohort bigger than the one above it. Asked why the population is growing, the credited option is about **mortality**, not fertility.

#### Stage 3 — maturing
FL1: Q208 · CC9B · Skill 2 · knowledge absent — the stage sequence

**Structure.** Third position — *now the birth rate falls*, because everything that made seven children rational has reversed: children survive, so fewer births reach the same family size; children cost (school, a bedroom) instead of earning (a field); women are in school and in the labour force; contraception is at the pharmacy. Growth slows.
**Concrete.** Tou and his wife, a hospital tech, stop at three. All three will live; each needs a car seat, a bedroom and eighteen years of school; and her shift is worth more than a fourth child's labour would ever have been. Nobody told them to stop. The arithmetic did.
**Claims.** Asserts fertility falls **voluntarily, with development** — the transition's central assertion and its denial of Malthus. Denies that a policy or campaign is required; the same drop occurs wherever child survival, women's education and urban life arrive. Denies that the population stops growing here: it is still growing, slower, on the momentum of stage 2's large young cohorts.
**Predicts.** Falling birth rate with an already-low death rate → stage 3. Its pyramid narrows at the base while the middle stays thick — the stage-2 cohorts moving up. Asked for the cause of the fertility decline, the credited option names **women's education, child survival, urbanization or the cost of children**, never a change in fecundity.

#### Stage 4 — post-industrial
FL1: Q208 · CC9B · Skill 2 · knowledge absent — the stage sequence

**Structure.** Fourth position — *both rates are low and they cancel again*, as in stage 1 but at the opposite corner: few births, few deaths, long lives. The population is stable or shrinking, and **aging**, because the big stage-2 cohorts are now old and nothing large is coming up behind them.
**Concrete.** Chloe's cohort, on current rates: one child, at thirty-three, if any. Her grandmother had seven. Nobody Chloe knows has buried a child and nobody has had many; at the 2020 New Year the hall is mostly Tou's generation and older.
**Claims.** Asserts stability at low rates is the endpoint of development, not a crisis. Denies that low birth plus low death means a young, healthy population — it means an **old** one, with a rising share of dependents over 65. Denies that stage 4 equals stage 1 because both are stable: one is stable at seven births and four survivors, the other at one birth and one survivor.
**Predicts.** Low birth, low death, median age rising, growth near zero or negative → stage 4. Its pyramid is **stationary** (a rectangle) if births hold at replacement, **constrictive** (base narrower than the middle, top-heavy) if they have fallen below it. An aging-population stem — pensions, dependency ratio, geriatric care — is a stage-4 stem.

#### Crude rate
FL1: Q208 · CC9B · supports — the archetype trap

**Structure.** Events per 1,000 of the **whole** population per year, everyone in the denominator regardless of age — so it moves whenever the age structure moves, even if no individual's risk changed.
**Concrete.** Riverside 1996 → 2020: the young families left after the factory closed, median age went 28 → 44, and deaths per 1,000 rose while nobody got sicker. The 70-year-olds died at the same rate as before; there were just more of them per thousand.
**Claims.** Asserts a crude rate is a fact about **who is in the population**, and only secondarily about how dangerous life is for them. Denies that a rising crude death rate means health worsened, or that a falling crude birth rate means women are having fewer children — either can be pure composition.
**Predicts.** A stem gives a crude rate moving and asks for a **demographic** explanation → the credited option is about age structure or migration, not behaviour or care. Two populations with identical age-specific risk show different crude rates if their age structures differ. That gap is the entire content of "crude."

#### Age-specific rate
FL1: Q208 · CC9B · supports

**Structure.** Events per 1,000 **within one age band** — 65–74, or 20–24 — so the age-structure confound is removed by construction, and what is left is the risk actually faced by people of that age.
**Concrete.** Riverside's deaths per 1,000 among 65–74-year-olds in 2020 were *lower* than in 1996 — the medical campus opened next door. The crude death rate rose over the same years. Both numbers are correct; they answer different questions.
**Claims.** Asserts this is the honest comparison across populations or across time: it isolates risk from composition. Denies that "the death rate rose" has any meaning until you know which rate. Denies that a crude and an age-specific rate must move together — they routinely move in opposite directions.
**Predicts.** When a passage reports both and they diverge, the age-specific rate describes **people's risk**; the crude rate describes **who lives there**. An option that reads a crude change as a change in individual risk is the trap; the key uses the age-specific figure, or says the crude change is compositional.

#### Total fertility rate
FL1: Q208 · CC9B · supports

**Structure.** The number of children **one woman** would bear over her lifetime if today's age-specific birth rates held — a per-woman number, not a count of births. About **2.1** replaces a generation.
**Concrete.** Mai's cohort, seven. Tou's wife's cohort, about three. Chloe's, on 2020 rates, about 1.6 — under the 2.1 that replaces itself. Riverside's crude birth rate fell over the same years for a different reason (fewer young women in the denominator); the TFR says what the women who *are* there are doing.
**Claims.** Asserts fertility is measured per woman, so the age structure cannot fake it — the opposite of the crude birth rate. Denies that a TFR below 2.1 means the population is shrinking *now*: large young cohorts keep births up for a generation after the rate drops. Denies that "total" means a total count.
**Predicts.** A question about whether a population will **replace itself** wants the TFR against 2.1. A question about births per 1,000 wants the crude birth rate. Stage 3 is the TFR falling; stage 4 is the TFR at or under 2.1.

#### Fertility
FL1: Q208 · CC9B · supports

**Structure.** **Actual** births — the realized number, whether counted per 1,000 (crude birth rate), per age band (age-specific rate) or per woman over a lifetime (TFR).
**Concrete.** Mai bore seven children. That is her fertility: a fact about what happened, in a camp, with a husband, with no pharmacy.
**Claims.** Asserts fertility is behaviour and circumstance, and therefore the thing that **moves** during the transition. Denies that it is a biological property; the biological property is the next term, and it did not move.
**Predicts.** "Birth rate," "number of children born," "births per woman" → fertility. Every fertility decline in the transition is a decline in this, with fecundity untouched.

#### Fecundity
FL1: Q208 · CC9B · supports

**Structure.** The **biological capacity** to reproduce — the ceiling on fertility, set by physiology, and far above any population's actual births.
**Concrete.** Chloe's body can carry as many children as Mai's could. Her fertility will be one-seventh of her grandmother's. Every bit of the difference is social — survival, school, work, the pharmacy — and none of it is fecundity.
**Claims.** Asserts fecundity is roughly constant across the transition and across societies. Denies that a falling birth rate says anything about anyone's ability to conceive. Denies the reverse reading too: a population can be highly fecund and have very low fertility, which is exactly stage 4.
**Predicts.** "Capacity," "ability to conceive," "biological potential" → fecundity. An option explaining a fertility decline by reduced fecundity is wrong unless the passage names a biological cause. Fecundity is always the higher number.

#### Push factors
FL1: Q208 · CC9B · supports

**Structure.** Conditions at the **origin** that make leaving better than staying — war, famine, persecution, a closed factory.
**Concrete.** 1996: the factory shuts, 1,400 jobs go, and the Xiong household leaves Bell Street within the year. Nothing new appeared anywhere else that month. Riverside pushed.
**Claims.** Asserts the cause of the move sits where the mover *was*. Denies that migration needs an attractive destination — refugees leave with nowhere good to go. Denies that push and pull are alternatives; most moves have both, and the item asks which one **the stated detail** is.
**Predicts.** A passage detail located at the origin → push. Same move, detail located at the destination → pull. The trap is the same fact described from the other end: "war at home" and "safety abroad" are one migration, and AAMC will list both.

#### Pull factors
FL1: Q208 · CC9B · supports

**Structure.** Conditions at the **destination** that draw people in — jobs, safety, family already there, schools.
**Concrete.** 1984: a Riverside church sponsors a family and the factory is hiring on a cousin's word. Mai's household lands on Bell Street because those two things were *here*, not because of anything in Riverside they were fleeing.
**Claims.** Asserts the cause sits where the mover is *going*. Denies that pull is the stronger or "real" cause — the same family had a war behind them. Denies that family already at the destination is anything but a pull factor.
**Predicts.** A passage detail about the destination — wages, sponsorship, relatives, safety → pull. If the stem describes the origin and the option describes the destination, the option has swapped ends; reject it.

#### Malthusian theory
FL1: Q208 · CC9B · supports — the transition's paired opposite

**Structure.** Population grows geometrically (2, 4, 8, 16), food supply arithmetically (1, 2, 3, 4), so population must outrun subsistence and be checked **catastrophically** — famine, disease, war — unless restrained earlier by late marriage and abstinence.
**Concrete.** What Malthus would have predicted for Mai's line: seven children who all live, then forty-nine grandchildren, then hunger. What happened: three, then one, chosen, with more food per person at every step. Riverside's births fell without a single hungry year.
**Claims.** Asserts the check on population is external and catastrophic. Denies — and this is where it fails — that fertility falls **voluntarily with development**, which is the demographic transition's whole content and the historical record's. The two are the outline's only named "theories of demographic change," so each is the other's distractor.
**Predicts.** A stem about resource exhaustion, carrying capacity, famine or collapse → Malthusian. A stem about death rates falling and then birth rates falling as a society industrializes → demographic transition, the keyed answer more often than not. An option that has fertility falling *because of* scarcity is Malthus wearing the transition's clothes.

#### The six sociological perspectives
FL1: Q206, Q208 context · CC9A · the highest-value set in the section

**Structure.** Split on level, then engine.

| Level | Perspective | The engine |
|---|---|---|
| **Macro** | **Functionalism** | parts serve functions; equilibrium; **manifest** = intended and recognized vs **latent** = unintended and unrecognized; dysfunction |
| **Macro** | **Conflict theory** | competition over scarce resources; power; class |
| **Macro** | **Feminist theory** | conflict theory with **gender** as the axis |
| **Micro** | **Symbolic interactionism** | meaning built and negotiated in face-to-face interaction; symbols; labels |
| **Micro** | **Social constructionism** | a category becomes real because it is collectively defined that way |
| **Micro** | **Exchange / rational choice** | cost–benefit calculation |

**Concrete.** Riverside's gentrification, six ways. *Functionalism:* displacement is a **latent
dysfunction** of a housing market whose manifest function is allocating housing. *Conflict:*
developers used capital and zoning power against people with less of both. *Symbolic
interactionism:* it became "up-and-coming" when enough people said so to each other and acted on
it. *Social constructionism:* "blighted" had to be a real category before anything could be
cleared under it. *Exchange:* each mover ran a rent-versus-commute calculation. *Feminist:* the
cost fell hardest on single mothers, whose housing and childcare networks were least portable.

**Claims.** Each asserts one engine and **denies the others are primary**. Functionalism: a
persisting arrangement does something for the system, and persistence does not require coercion.
Conflict theory, the reverse: it persists because someone with power benefits, and apparent
consensus is imposed. Symbolic interactionism denies either macro story explains anything until
you show it enacted between people. Rivals, not layers.

**Predicts.** The item's **level** (individuals interacting vs institutions and groups) picks the
half; its **engine** (function, power, meaning, definition, calculation, gender) picks the
member. If the stem is about *how a label or category came to exist*, you are in symbolic
interactionism or social constructionism, never functionalism.

#### Functionalism
FL1: Q206, Q208 context · CC9A · supports

**Structure.** Position 1 of 6 on the zoom axis — the six perspectives ordered by the **size of the unit that does the explaining**, from the whole society down to one person. Here the unit is *society as a system*: parts persist because they serve a function for the whole; disturbance is followed by re-equilibration; functions are **manifest** (intended, recognized) or **latent** (neither), and harms are **dysfunctions**.
**Concrete.** Riverside's forty years read as a system righting itself. The neighbourhood existed to house the factory's workers; the factory closed; the system withdrew (disinvestment) from a part that no longer served, then found it a new function — housing the medical campus and rebuilding the tax base. The 1998 blight designation: manifest function, clearing derelict blocks; latent function, lifting land values around them; latent dysfunction, two hundred households gone.
**Claims.** Asserts a persisting arrangement is doing something for the system, and that persistence does not require coercion. Denies that "who benefits" is the question — the system benefits. Denies conflict theory's reading of the same forty years as a transfer of land from the weak to the strong.
**Predicts.** An option phrased as what an arrangement **does for** society or an institution — *serves to, maintains, integrates, stabilizes, contributes to* — is functionalist. If the stem asks about an *unintended* consequence, it is asking for a latent function or dysfunction. The adjacent trap is conflict theory: same arrangement, described by who gains.

#### Conflict theory
FL1: Q206, Q208 context · CC9A · supports

**Structure.** Position 2 — the unit is *groups competing inside the society* over scarce resources: land, money, power. Arrangements persist because they benefit whoever has the power, and apparent consensus is something the winners produce.
**Concrete.** Riverside's forty years as one resource, land, moving to whoever held capital and zoning power. The bank redlined the east side in the 1980s; the council condemned four blocks in 1998; developers bought when prices bottomed; and the people with the least capital paid at every step. What functionalism calls re-equilibration, conflict theory calls the invoice.
**Claims.** Asserts inequality is the engine, not a by-product. Denies that persistence implies benefit to the whole — the arrangement persists because someone can enforce it. Denies functionalism's equilibrium: stability is the powerful holding what they took.
**Predicts.** The keyed option names **unequal access to a scarce resource** — AAMC's own example: the wealthy have better health outcomes *because they have access to better care*. Words: *power, resources, exploitation, whose interests*. The adjacent trap is feminist theory: the same sentence with gender as the axis instead of class.

#### Feminist theory
FL1: Q206, Q208 context · CC9A · supports

**Structure.** Position 3 — the unit is *gendered groups*: conflict theory's engine with **gender** as the axis of power. Institutions, work and family are organized so that men hold more of the resources, and that organization reproduces itself.
**Concrete.** Riverside's forty years with the sex column added. The 1996 layoffs hit the second-shift men; the 2015–19 displacement hit single mothers hardest, because their childcare was the block itself — a grandmother two doors down — and it did not move with them. The redevelopment plan was drafted by a council of nine men and assumed a two-earner household.
**Claims.** Asserts gender is a structural organizer of power, not a demographic footnote to class. Denies that class explains the whole pattern — two households at the same income, one headed by a woman, did not lose the same thing. Denies functionalism's reading of the gendered division of labour as "what works for the family."
**Predicts.** An option locating the mechanism in *gendered institutions, patriarchy, the gendered division of labour, or who does the unpaid work* is feminist. **Conflict vs feminist is one question: is the axis class or gender?** Both are macro; neither is about a face-to-face interaction.

#### Social constructionism
FL1: Q206, Q208 context · CC9A · supports

**Structure.** Position 4 — the unit is *a shared category*: race, gender, illness, deviance, blight. Things treated as natural or objective are real in their effects because a collectivity has agreed to treat them as real, and the item's tell is **"is not inherent but is defined by."**
**Concrete.** In 1997 Bell Street was a place with bad roofs. In 1998 it was "blighted" — a legal category the council voted into being — and only then could four blocks be condemned. Nothing about the roofs changed between those years. The category did, and it moved two hundred households. "Up-and-coming" in 2015 did the same job in the other direction.
**Claims.** Asserts the category precedes and enables the action: you cannot clear what has not been defined as clearable. Denies that the category was discovered in the object — blight, like race, is not a property of bricks or bodies. Denies symbolic interactionism's focus on the *moment of negotiation*: constructionism is about the definition once it has hardened and everyone acts on it.
**Predicts.** A stem about *how a category came to exist or came to count as real* → constructionism. The adjacent trap is symbolic interactionism: if the stem is about people negotiating meaning **in an interaction**, it is that one; if it is about a **category** treated as objective, it is this one. Never functionalism — the question is where the category came from, not what it does for the system.

#### Symbolic interactionism
FL1: Q206, Q208 context · CC9A · supports

**Structure.** Position 5 — the unit is *a face-to-face interaction*: society exists in the meanings people build, negotiate and act on with each other, through symbols and labels. Change how the situation is defined between two people and you change what happens.
**Concrete.** Riverside "turned" one conversation at a time — a realtor's word on a tour, the roaster's chalkboard, a neighbour saying "you got in before it changed." Twenty years earlier, a label the other way: "the Hmong side" shaped how officers, teachers and loan officers acted toward whoever lived there. Mai reads the new neighbour's face when the New Year drums start, and turns them down.
**Claims.** Asserts meaning is made in interaction and has effects because people respond to it. Denies that either macro story explains anything until you show it enacted between people — the redlining was a loan officer looking at a face. Denies constructionism's emphasis on the finished category; here the meaning is still being negotiated.
**Predicts.** Stem words *interpret, meaning, label, define the situation, symbols, face-to-face* → symbolic interactionism. AAMC's own Skill 2 item: use its premises in an observational study of **physician–patient interactions** to explain perceived compliance — the answer is about what the two parties signal to each other, not about either one's traits. Micro, always.

#### Exchange / rational choice
FL1: Q206, Q208 context · CC9A · supports

**Structure.** Position 6 — the unit is *one person's ledger*: people weigh costs against rewards and choose the larger payoff; social structure is the sum of those choices.
**Concrete.** Every Riverside move was arithmetic. Dana in 2015: a mortgage on a two-flat against a twelve-minute commute — worth it. The Yangs in 2019: $1,400 rent against a longer bus ride to the same job — not worth it, so they went. Mai stays: the house is paid off and the clan association is two blocks away, and leaving would cost more than staying.
**Claims.** Asserts incentives are sufficient to explain the pattern; meaning, function and power enter only as costs and rewards. Denies that people are moved by norms except as prices. Denies the other five perspectives' need for anything above the individual — the neighbourhood's fate is the aggregate of its ledgers.
**Predicts.** Cue words *incentive, payoff, reward, cost, benefit, weighed* → exchange/rational choice. An option explaining a social pattern as individuals each choosing the larger payoff is this one — and if the stem describes a person deciding whether a relationship or a move is "worth it," you are here, not in symbolic interactionism.

**Discriminators**
- **Assimilation vs acculturation** — did the distinct identity disappear, or is it retained
  alongside the new culture?
- **Assimilation vs amalgamation** — does one side change, or both?
- **Assimilation vs multiculturalism** — absorbed, or preserved side by side?
- **Gentrification vs urban renewal** — market-driven in-migration, or planned, often state-led
  redevelopment?
- **Gentrification vs urbanization** — who moves into an existing urban neighbourhood, or the
  overall concentration of population into cities?
- **Urban decline vs white flight** — general disinvestment, or the specific racialized
  out-migration?
- **Demographic explanation vs behavioural explanation** — did the population's composition
  change, or did people's behaviour change?
- **Crude vs age-specific rate** — per 1,000 of everybody, or within one age band?
- **Fertility vs fecundity** — actual births, or biological capacity?
- **Push vs pull factors** — driven out of the origin, or attracted to the destination?
- **Malthusian vs demographic transition** — a catastrophic check, or a voluntary fertility
  decline with development?
- **Culture lag vs culture shock** — nonmaterial culture failing to keep up with technological
  change, or an individual's disorientation entering a new culture?
- **Subculture vs counterculture** — distinct within the dominant culture, or actively opposing
  its values?
- **Manifest vs latent function** — intended and recognized, or unintended and unrecognized?
- **Latent function vs latent dysfunction** — unintended benefit, or unintended harm?
- **Conflict theory vs feminist theory** — class as the axis, or gender?
- **Symbolic interactionism vs social constructionism** — meaning negotiated in interaction, or
  a category defined into reality?
- **Relative deprivation vs absolute poverty** — a *perception* relative to a reference group
  (and the motor of social movements), or a *measure* against a fixed subsistence threshold?

**Compression — the scale of the thing that is changing**

| Scale | Concepts | The question that lands you here |
|---|---|---|
| A person's culture | acculturation, culture shock, socialization | what did this individual take on or lose? |
| A group's identity | assimilation, amalgamation, multiculturalism, subculture, counterculture | did the group's distinctness survive? |
| A neighbourhood | gentrification, urban renewal, white flight, residential segregation, suburbanization | who lives here now who did not before? |
| A society's rates | demographic transition, fertility and mortality rates, population pyramids, migration | did the composition of the population change? |
| A society's structure | the six perspectives, institutions, stratification, globalization | what arrangement of positions produced this? |

Place the stem's noun on this ladder before reading options. Almost every 9A/9B distractor set
offers the right concept from the **wrong rung**.

---

### CLUSTER 7 — RESEARCH DESIGN IN P/S

**FL1: Q211, Q224, Q226.** Skill 3 90%, Skill 4 **100%** — handed a research vignette you were
perfect. So this cluster is short and not about reasoning. What broke were **names**: what a
design is *called*, what a measure is *called*. Q224 asked "the research is best described as
a:" — a labelling question in a methods question's clothes.

**Scope warning.** AAMC's 108-page outline never uses *control group, randomization, blind,
placebo, sample size, statistical power, null hypothesis, standard error, t-test, ANOVA,
chi-square, regression, effect size,* or *confidence interval* — zero occurrences. **What is
absent is the abstract noun and the inferential-statistics vocabulary, not the concrete
phrases:** vignettes still say participants were *randomly assigned* or *randomly selected*, so
random assignment vs random sampling stays live below, while *randomization*, *t-test*, *ANOVA*,
*power*, and *confidence interval* never appear as such. An option in that vocabulary is not
from AAMC's deck. The deck it does use is about **thirty terms**, the highest points-per-minute
material in the section.

*Shared scene:* **the Riverside studies, and the clinic from Cluster 5.**

#### Naming the design
FL1: Q224 · CC9B · Skill 3 · knowledge absent (a label, not a judgment)

**Structure.** Three questions in order; the name is the **conjunction of all three answers**, not one word.

| Question | What was true of the study | The word it earns |
|---|---|---|
| **1. Was anything manipulated?** | nothing was | observational / descriptive / correlational |
| | yes, with participants assigned to conditions | **experimental** |
| | yes, but the groups pre-existed | **quasi-experimental** (including a natural experiment) |
| **2. How many time points, and in which direction?** | one | **cross-sectional** |
| | the same people measured repeatedly | **longitudinal** |
| | a defined group followed forward from exposure to outcome | **cohort** |
| | from the outcome backward to exposure | **case-control** |
| | existing records | **archival** |
| **3. What kind of data — and by what method?** | counts and numbers | **quantitative** |
| | meaning, description, open-ended | **qualitative** |
| | structured self-report at scale | **survey** |
| | immersive fieldwork | **ethnography / participant observation** |
| | watching without joining | **naturalistic observation** |
| | one unit in depth | **case study** |
| | systematic coding of existing texts or media | **content analysis** |

**Concrete.** Five Riverside studies, five names. 30 displaced families interviewed at length
about what moving cost them → **qualitative, cross-sectional interview study**. 2,000 residents
surveyed once → **cross-sectional survey**. The same 500 followed ten years → **longitudinal
cohort study**. Gentrified tracts compared with non-gentrified via census data → **observational
quasi-experiment**: nothing manipulated, nobody assigned. A researcher renting an apartment for
a year, keeping field notes → **ethnography, participant observation**.

**Claims.** Sophisticated analysis does not convert an observational study into an experiment.
Design is fixed by **what researchers did to the participants**, not to the data. Denies reading
a well-controlled statistical comparison as experimental.

**Predicts.** AAMC's option set usually varies exactly **one** of the three questions — find it
and answer only that. No manipulation → never "experiment," however elaborate. One time point →
no temporal order, no causal claim. **Random assignment** → internal validity, causal inference.
**Random sampling** → external validity, generalizability. The most-swapped pair in the section,
and the single most common methods error.

#### Experimental
FL1: Q224 · CC9B · supports

**Structure.** The researchers **manipulated** something and **assigned participants to conditions** — the two facts together. Assignment made at random is what lets the difference in outcome be attributed to the manipulation and to nothing else.
**Concrete.** Riverside's housing authority has 300 vouchers and 600 eligible displaced families. It allocates them by lottery, then measures blood pressure in both groups two years later. Whatever differs between the two groups, the lottery made sure it was not something about the families.
**Claims.** Asserts this is the only design that licenses a **causal** claim — within this sample. Denies that sophisticated analysis of unmanipulated data converts anything into an experiment. Denies that an experiment generalizes on its own: the 600 were eligible families in one city, and the lottery says nothing about anyone else.
**Predicts.** "Randomly assigned," "were placed in the condition," "the researchers manipulated" → experimental; the option set will offer *correlational* and *quasi-experimental* as the neighbours. If nothing was assigned by the researcher, it is not this, however many variables were measured.

#### Quasi-experimental
FL1: Q224 · CC9B · supports

**Structure.** Something varied between groups **but the groups pre-existed** — the researcher compared conditions that were already there rather than assigning anyone to them. A **natural experiment** is the case where an outside event (a policy, a closure, a disaster) did the sorting.
**Concrete.** Gentrified tracts compared with non-gentrified tracts on census health data. Nobody was assigned to a tract; people chose, or were priced into, where they live. The 1996 factory closure as a natural experiment: the workers laid off compared with workers at the plant across the river that stayed open.
**Claims.** Asserts a stronger comparison than a single-time survey — some alternative explanations are ruled out by the comparison group's existence. Denies clean causation: whatever sorted people into the groups could also have produced the outcome. Denies that "quasi" means "sloppy"; it means "without assignment."
**Predicts.** Groups defined by something that already happened — where people live, whether they were laid off, which school district → quasi-experimental. The credited claim is "a stronger association," never "caused." **Experiment vs quasi-experiment is one question: did the researcher assign, or did the groups pre-exist?**

#### Random assignment
FL1: Q224 · CC9B · supports · **added — not a table row; the cluster's flagship discriminator had no block**

**Structure.** Who goes into **which condition** is decided by chance, after they are already in the study. It equalizes the groups on everything not manipulated, so the manipulation is the only systematic difference — **internal validity**, the licence for a causal claim.
**Concrete.** The voucher lottery. The 600 families are already the sample; the coin decides which 300 get a voucher. Age, income, health and motivation are now spread evenly between the two groups on average, because the coin does not know them.
**Claims.** Asserts causation inside the sample. Denies generalization: random assignment says nothing about whether the 600 resemble anyone else. Denies that assignment of any kind is enough — assigning the sickest 300 to vouchers destroys the comparison.
**Predicts.** "Randomly assigned to" → the causal claim is licensed for this sample and only this sample. AAMC's own item keys on this: **only the option that randomly assigns a manipulated variable licenses a causal claim.** The adjacent trap swaps in random sampling, which buys the other thing.

#### Random sampling
FL1: Q224 · CC9B · supports · **added — not a table row; the cluster's flagship discriminator had no block**

**Structure.** Who gets **into the study** is decided by chance from a defined population. The sample then resembles that population, so results generalize to it — **external validity**.
**Concrete.** The 2,000-resident survey. Names drawn by lottery from the city's tax roll: the sample looks like Riverside, and its 34% reporting displacement worry generalizes to Riverside. The same survey posted at the coffee roaster returns the roaster's customers — a convenience sample that generalizes to nobody.
**Claims.** Asserts generalization to the population sampled. Denies causation: a perfectly representative sample measured once still cannot say what caused what. Denies that a large sample substitutes for a random one — 10,000 roaster customers are still roaster customers.
**Predicts.** "Randomly selected from," "a representative sample of" → generalization is licensed. **Assignment buys causation, sampling buys generalization, and neither buys the other.** A study can have both (a lottery-drawn sample, then a coin-flipped condition), either, or neither — score the two separately.

#### Cross-sectional
FL1: Q224 · CC9B · supports

**Structure.** **One time point.** Everyone measured once, at the same moment; differences are between people, never within a person over time.
**Concrete.** The 2,000 residents surveyed in spring 2020. Long-term residents report worse sleep than newcomers. Whether the neighbourhood's change wrecked their sleep, or poor sleepers were the ones who could not organize a move, or both, this design cannot say — it has one photograph.
**Claims.** Asserts association at a moment, and prevalence. Denies temporal order: with one photograph you cannot tell which came first, so you cannot tell cause from consequence. Denies that comparing age groups at one time point shows what happens as people age — a 60-year-old in 2020 is a different cohort from a 30-year-old, not the same person later.
**Predicts.** "Surveyed once," "at a single point in time," "compared 20-year-olds with 60-year-olds" → cross-sectional; the licensed claim is association and prevalence, never sequence or cause. **Cross-sectional vs longitudinal is one question: one time point, or the same people over time?**

#### Longitudinal
FL1: Q224 · CC9B · supports

**Structure.** **The same people measured repeatedly** over time, so change is observed *within* individuals and the order of events is known.
**Concrete.** The same 500 residents interviewed in 2010, 2015 and 2020. The ones displaced between waves show the drop in sleep quality *after* the move, not before. The photograph has become a film.
**Claims.** Asserts temporal order — and incidence, new cases appearing between waves. Denies causation still: whatever made a household displaceable could also have made it sleep worse. Denies that it is cheap or quick, which is why attrition — who dropped out between waves — is its standing threat.
**Predicts.** "Followed," "measured again in," "over ten years," "the same participants" → longitudinal; the licensed claim adds *temporal order* to association and still stops short of cause. If the stem also defines the group by an exposure, it is the next term.

#### Cohort
FL1: Q224 · CC9B · supports

**Structure.** A group **defined by exposure**, followed **forward** from exposure to outcome — a longitudinal design whose starting line is "who was exposed and who was not."
**Concrete.** The 500 enrolled in 2010, all free of hypertension. By 2016 the rent surge had displaced 140 of them and left 360 in place: two groups, defined by exposure. Follow both to 2020 and count new diagnoses — 19% of the displaced, 11% of the others. The design counted cases as they arose, in people whose exposure was known first.
**Claims.** Asserts incidence and temporal order: exposure was recorded before the outcome existed. Denies causation — confounders remain, and nobody assigned displacement. Denies that "cohort" means "age group" here: an age cohort is a demographic term; a cohort *study* is defined by shared exposure.
**Predicts.** "Followed exposed and unexposed," "from exposure to outcome," "incidence" → cohort. The direction of the arrow is the whole discriminator: **cohort runs exposure → outcome; case-control runs outcome → exposure.**

#### Case-control
FL1: Q224 · CC9B · supports

**Structure.** Start from the **outcome** — people who have it (cases) and matched people who do not — and look **backward** at who had the exposure.
**Concrete.** In 2020 the clinic pulls 80 Riverside patients newly diagnosed with hypertension and 80 matched patients without it, then asks each about displacement since 2015. 40% of the cases were displaced; 18% of the others were. The study started at the end and read the story in reverse.
**Claims.** Asserts association between an outcome and a prior exposure, efficiently — the design of choice for a rare outcome, because you begin with the people who have it. Denies incidence: you chose how many cases to include, so no rate can be computed from it. Denies temporal certainty: exposure is recalled, and people with the outcome remember exposures differently. "Case" here means a person with the outcome, not a single unit studied in depth (that is a case study).
**Predicts.** "Compared patients with the condition to those without," "asked about prior exposure," "looked back" → case-control. It can never answer "what proportion of the exposed developed the outcome" — that question belongs to a cohort.

#### Ethnography / participant observation
FL1: Q224 · CC9B · supports

**Structure.** The researcher **joins** the setting — lives in it, takes part, keeps field notes over months — to record what things mean from inside. Qualitative, one setting, in depth.
**Concrete.** A sociologist rents a Bell Street apartment for 2018, shops at Mrs. Vang's, goes to the block meetings about the New Year drumming, and writes it all down each night. By December she knows what "up-and-coming" costs from the inside of a household it is costing.
**Claims.** Asserts access to meaning that no survey item can reach. Denies frequency and generalization: one street, one year, one observer. Denies neutrality — the researcher's presence is part of the setting, and she says so.
**Predicts.** "Immersed," "lived among," "field notes," "participated in" → ethnography; the licensed claim is description of the case and hypotheses to test elsewhere. **Ethnography vs naturalistic observation is one question: did the researcher join, or only watch?**

#### Naturalistic observation
FL1: Q224 · CC9B · supports

**Structure.** The researcher **watches without joining or intervening**, in the setting where the behaviour occurs, and codes what she sees.
**Concrete.** A researcher sits at the roaster's window table three mornings a week and tallies who greets whom on Bell Street — old resident to old resident, newcomer to newcomer, across the line almost never. She orders coffee. She talks to nobody. The behaviour is untouched by the study.
**Claims.** Asserts behaviour as it actually occurs, without the distortions of a lab or a questionnaire. Denies access to meaning — she sees the missed greeting, not what either party thought it meant. Denies causation: nothing is manipulated, so nothing causal follows.
**Predicts.** "Observed," "recorded without interacting," "in their natural setting" → naturalistic observation; if the observer is described as a participant, it is ethnography instead. Both are observational; only one has an insider.

#### Subjective vs objective measurement — cross-reference
FL1: Q211 · taught in full in Cluster 3A

**Subjective means the datum passes through someone's judgment** — including someone else's, and
including a numeric rating scale. Objective means it is countable without one. Neither term says
anything about reliability or validity.

#### "If replicated, which hypothesis would be supported?"
FL1: Q226 · CC8C · Skill 2 · knowledge absent (the construct, not the logic)

**Structure.** Three steps; the test is entailment, not compatibility.

| Step | Do this |
|---|---|
| 1 | **Restate the finding as a directional sentence in your own words, before reading any option.** *Group A scored higher than group B, and the gap was larger under condition X.* |
| 2 | **For each hypothesis, ask whether it *entails* that exact pattern** — direction and comparison included. |
| 3 | A hypothesis that merely **permits** the result is not supported by it. Only the one that **requires** it is. |

**Concrete.** The clinic study: high social support meant lower cortisol, but only among those
reporting high stress; under low stress the groups were identical. The supported hypothesis is
**stress-buffering** — the only one that *requires* the effect to vanish in the low-stress group.
A main-effect hypothesis fits half the data and is contradicted by the rest.

**Claims.** Support is about entailment, not compatibility. Denies the natural reading of
"supported" as "not contradicted."

**Predicts.** A result with an **interaction** supports the hypothesis predicting the
interaction, never the one predicting a main effect. The wrong option is almost always **true,
and about a variable the study did not measure**, or the right direction on the wrong
comparison. Check the comparison before the direction.

#### The methods terms AAMC actually uses
FL1: supporting all of the above

**Variables.** **Independent** = what was assigned or set. **Dependent** = what was measured.
**Confounder** = causes both the IV and the DV, making the association spurious. **Mediator** =
the mechanism *through which* the IV affects the DV. **Moderator** = changes the *strength* of
the relation.
**Validity.** **Internal** = confidence the IV caused the DV *in this study*. **External** =
generalizability beyond it. **Reliability** = consistency. A measure can be reliable and
invalid; it can never be valid and unreliable.
**Threats to self-report and observation.** **Social desirability bias** (answering to look
good), **demand characteristics** (guessing the hypothesis and complying), **Hawthorne effect**
(changing behaviour because you know you are watched).
**Sampling.** **Selection bias** (who entered), **attrition bias** (who dropped out),
**non-response bias** (who declined).
**Ethics.** **Informed consent** before, **debriefing** after, **right to withdraw** throughout.
**Anonymity** (the researcher cannot link data to identity) vs **confidentiality** (can, but
will not disclose). **Deception** is permitted with debriefing; **coercion** never is.
**Epidemiology.** **Incidence** = new cases over a period. **Prevalence** = existing cases at a
point.
**Description.** **Mean vs median under skew** — income is right-skewed, so it is reported as a
median. **Operationalization** = how the construct was measured in this study.

**Claims.** The deck is **closed and small**; Skill 3 items are answerable from it without
tracking the study's specifics. Denies that methods questions require understanding the
particular experiment — they mostly require having the word.

**Predicts.** Given a variable AAMC calls a "third variable," decide among confounder, mediator,
and moderator by asking **where it sits relative to the arrow**: before both (confounder), on
the arrow (mediator), or bending the arrow (moderator).

**Discriminators**
- **Random sampling vs random assignment** — who got *into* the study, or who went into *which
  condition*?
- **Internal vs external validity** — did the IV cause the DV here, or does it hold elsewhere?
- **Reliability vs validity** — consistent, or measuring the right thing?
- **Experiment vs quasi-experiment** — was there assignment, or did the groups pre-exist?
- **Cross-sectional vs longitudinal** — one time point, or the same people over time?
- **Cohort vs case-control** — from exposure forward, or from outcome back?
- **Ethnography vs naturalistic observation** — did the researcher join, or only watch?
- **Confounder vs mediator vs moderator** — before the arrow, on it, or bending it?
- **Subjective vs objective measure** — does the datum pass through anyone's judgment?
- **Social desirability vs demand characteristics vs Hawthorne** — looking good, guessing the
  hypothesis, or knowing you are watched?
- **Incidence vs prevalence** — new cases, or all existing cases?
- **Anonymity vs confidentiality** — can the researcher link it to you at all?
- **Supported vs merely consistent** — does the hypothesis *require* this result?

**Compression — what the design licenses you to claim**

| The design | You may claim | You may NOT claim |
|---|---|---|
| Case study, ethnography | description of one case; hypotheses to test | frequency, generalization |
| Cross-sectional survey | association at one time; prevalence | temporal order, causation |
| Longitudinal / cohort | association plus **temporal order**; incidence | causation (confounders remain) |
| Case-control | association between an outcome and prior exposure | incidence, temporal certainty |
| Quasi-experiment | a stronger association; some alternatives ruled out | clean causation (groups pre-existed) |
| Experiment (random assignment) | **causation, within this sample** | generalization beyond the sample |
| Random *sampling*, any design | **generalization to the population sampled** | causation, on its own |

The bottom two rows are the whole game: **assignment buys causation, sampling buys
generalization, and neither buys the other.**

---

### THE SEVEN-DAY LOOP

1. **Negative-stem procedure on ten items every session**, regardless of topic — 56% → 71% on
   that stem type is roughly two questions, and it is a procedure, not knowledge.
2. **Drill every Discriminator in both directions.**
3. **Order of attack, by cost:** CC9B (25%, worst on the exam) → CC7A (44%, ~13 items per form)
   → CC8C (50%, ~8 items per form) → CC6A anatomy (two questions, pure lookup, cheapest points
   here) → CC6B memory.
4. **Close each concept by stating its Predicts line from memory.** Definition only = card not
   finished.

---

# PHYSICS

## CONCEPTS — C/P PHYSICS

Physics is the floor: **8/14, 57%**, worst discipline on FL1 — but not from ignorance. C/P Skill 2
ran **77% in the first half of the section and 43% in the second**, a 34-point collapse with
knowledge at 80%. Content present, schema absent under time pressure: the **worked-example
population** (research/11 §1.5). Worked examples beat problem-solving at g = 0.48;
**backward-faded** examples beat example–problem pairs at d ≈ 0.46–0.54, at zero extra study time.

Fifteen quantitative concepts carry a three-rung ladder, one per solvable move:

1. **Worked — full.** Every step shown. Read it; do not solve it.
2. **Faded — last step.** Everything but the final computation is given.
3. **Faded — last two.** Setup given, execution yours.

**Run it with the prompt.** Atkinson's effect came from naming the principle behind each step
*with feedback attached*. On rungs 2 and 3, say which equation the step comes from before you
compute. Then read `Check:` — that line is the feedback, and it names the principle, not just the
number. Skipping it throws away most of the effect.

**Time allocation.** Optics and fluids first — six of the ten misses, both genuine content gaps.
Circuits third. **Electrochemistry last and shortest**: Q53/54/55 are one passage in the final
third, taken with the clock gone — a pacing casualty wearing a content mask.

No calculator. Every number falls out clean. Trig only at 0/30/45/60/90.

---

## CLUSTER 1 — OPTICS
**FL1: Q15, Q45 · CC4D (4/6, 67%)**

**Shared scenario: one eye looking at a candle.** A 6 cm flame across the room. Light leaves it in
air, crosses the cornea, the aqueous humor, the lens, and the **vitreous humor**, and lands on the
retina as a real, inverted, tiny image. Each concept is one step further along that trip.

---

#### Index of refraction
FL1: **Q15** · CC4D · broke: reasoning — had the relation, didn't run it

**Structure.** `n = c/v`, the factor by which a medium slows light — dimensionless, always ≥ 1, since nothing outruns `c = 3.00 × 10⁸ m/s`.

**Concrete.** Light entering the vitreous humor slows from 3.00 × 10⁸ to about 2.24 × 10⁸ m/s — no
energy lost, no color change, just smaller steps through a medium whose electrons keep absorbing
and re-emitting it.

**Claims.** `n` is a **speed** ratio, nothing else. Denies that `n` is "how much a material bends light" —
bending is a *consequence* of `n` mismatch at a boundary, and at normal incidence a huge `n` bends
nothing. Denies any frequency change: **`f` is fixed by the source and survives every boundary;
`λ` shrinks**, `λ_medium = λ_vacuum/n`.

**Predicts.** Given `v`, `n = c/v`; given `n`, `v = c/n`; `λ_medium = λ_vacuum/n` with `f` unchanged. Higher `n`
→ slower → shorter `λ` → bends *toward* the normal.

**Worked — full.** *Light travels at 2.00 × 10⁸ m/s inside a lens implant. Find n.*
1. Principle: `n = c/v`, a speed ratio.
2. `n = (3.00 × 10⁸)/(2.00 × 10⁸)`.
3. Powers of ten cancel: `n = 1.50`.

**Faded — last step.** *The cornea has n = 1.38. How fast does light move in it?*
1. Principle: same relation the other way — `v = c/n`.
2. `v = (3.00 × 10⁸)/1.38`.
3. `v = ______`

**Faded — last two.** *Light in the vitreous humor moves at 2.24 × 10⁸ m/s; green light of vacuum
wavelength 500 nm enters. Find n, then λ inside the eye.*
1. Principle: `n = c/v`, then `λ_medium = λ_vacuum/n`.
2. `n = ______`
3. `λ_medium = ______`

**Check:** (2) `v ≈ 2.17 × 10⁸ m/s` — divide mantissas, keep the exponent; `v` must land below `c`. (3)
`n ≈ 1.34`, so `λ = 500/1.34 ≈ 373 nm`. Principle: *frequency is conserved across a boundary,
wavelength is not*.

---

#### Snell's law
FL1: — · CC4D · supports Q15

**Structure.** `n₁ sin θ₁ = n₂ sin θ₂`, angles **from the normal** — into higher `n` bends toward the normal, into lower `n` away.

**Concrete.** The candle's light hits the cornea at 45° off the perpendicular. Air is `n = 1.0`, cornea
`n = 1.41`; inside, the ray runs at 30°. Almost all of the eye's focusing happens here, not at the
lens.

**Claims.** The *product* `n sin θ` carries across a boundary. Denies that light always bends toward the normal
— it bends away entering a lower-`n` medium. Denies that a head-on ray bends: at `θ₁ = 0`,
`sin θ₁ = 0` forces `sin θ₂ = 0` for any media.

**Predicts.** Bigger `n` on your side → smaller angle on your side, so a shrinking angle means a slower medium.
Given three variables, solve the fourth; `θ` stays at 0/30/45/60/90.

**Worked — full.** *Light in air (n = 1.0) strikes the cornea (n = 1.41) at 45°. Find the
refracted angle.*
1. Principle: `n₁ sin θ₁ = n₂ sin θ₂`, angles from the normal.
2. `(1.0)(sin 45°) = (1.41)(sin θ₂)`.
3. `sin 45° = √2/2 ≈ 0.707`, so `0.707 = 1.41 sin θ₂`.
4. `sin θ₂ = 0.707/1.41 = 0.50`, so `θ₂ = 30°`.

**Faded — last step.** *Light inside glass (n = 2.0) hits the glass–water boundary (n = 1.33) at
30°. Find the refracted angle's sine.*
1. Principle: `n₁ sin θ₁ = n₂ sin θ₂`, glass as medium 1.
2. `(2.0)(sin 30°) = (1.33)(sin θ₂)`, `sin 30° = 0.50`.
3. `sin θ₂ = ______`, and the ray bends ______ the normal.

**Faded — last two.** *A ray passes from the aqueous humor (n = 1.33) into the lens (n = 1.41) at
0° incidence. Find the refracted angle and the speed inside the lens.*
1. Principle: Snell for the angle; `v = c/n` for the speed.
2. `θ₂ = ______`
3. `v = ______`

**Check:** (2) `sin θ₂ ≈ 0.75`, above `sin 30° = 0.50`, so the angle grew — bent **away from** the normal,
into the faster medium. (3) `θ₂ = 0°`, `v ≈ 2.13 × 10⁸ m/s`. Principle: `sin 0° = 0` forces
`sin θ₂ = 0`, whatever the indices.

---

#### Total internal reflection
FL1: — · CC4D · supports Q15

**Structure.** `sin θ_c = n₂/n₁`, valid **only when `n₁ > n₂`**; past `θ_c` nothing exits and 100% reflects back into the dense medium.

**Concrete.** Sit on the bottom of a pool and look up: overhead is a bright circular window onto
the sky, and past about 49° from vertical the surface goes silver, reflecting the pool floor. That
edge is `θ_c`.

**Claims.** TIR is Snell's law out of room: as `θ₁` grows, `sin θ₂` hits 1 while `θ₁` is under 90°, leaving no
transmitted ray. Denies that TIR is a material property — it is geometry, and **directional**: the
boundary that traps light dense→rare transmits perfectly rare→dense. Light entering glass from air
is never totally internally reflected.

**Predicts.** `θ_c = arcsin(n₂/n₁)`, landing on 30°, 45°, or 60°. Raising `n₁` *lowers* `θ_c` and traps more
light — why fiber cores are high-index. If `n₁ < n₂`, no angle has that sine, and the answer is "total internal reflection is impossible
here."

**Worked — full.** *A fiber core (n = 1.41) sits in air (n = 1.0). Find the critical angle.*
1. Principle: TIR needs dense→rare; `1.41 > 1.0`, satisfied.
2. `sin θ_c = n₂/n₁ = 1.0/1.41 = 0.707`.
3. `0.707 = √2/2`, so `θ_c = 45°`. Rays beyond 45° from the normal stay inside.

**Faded — last step.** *A diamond (n = 2.0) sits in air.*
1. Principle: `sin θ_c = n₂/n₁ = 1.0/2.0`.
2. `sin θ_c = 0.50`.
3. `θ_c = ______`, and compared with the fiber above, diamond traps ______ light.

**Faded — last two.** *Light travels from air (n = 1.0) toward the cornea (n = 1.41). Is there a
critical angle?*
1. Principle: check the direction of the index step first.
2. Ratio `n₂/n₁ = ______`
3. Conclusion: ______

**Check:** (2) `θ_c = 30°`; diamond traps **more** light — a smaller critical angle means more ray angles
exceed it. (3) `n₂/n₁ = 1.41 > 1`, and no sine exceeds 1, so **no critical angle exists**.
Principle: the directionality of the condition, not the arithmetic.

---

#### Thin lens and mirror equation, with sign conventions
FL1: — · CC4D · supports Q45

**Structure.** `1/o + 1/i = 1/f`, identical for thin lenses and spherical mirrors (`f = R/2` for mirrors); the rest is sign bookkeeping.

**Concrete.** The eye is this equation at `o ≫ f`: candle 5 m away, focal length about 2 cm, so `1/i ≈ 1/f` and
the image lands at the focal point on the retina. Bring the candle to 20 cm and `i` wants to sit
behind the retina, so the ciliary muscle fattens the lens to shorten `f` — accommodation, one
algebra step.

**Claims.** Image position is fixed entirely by object position and focal length; lens *size* and object
*brightness* are irrelevant. Denies "a stronger lens makes a bigger image": shorter `f` pulls the
image closer, which by `m = −i/o` makes it **smaller** for a distant object. Denies that a
converging lens always makes a real image — inside `f` it makes a **virtual, upright, magnified**
one, the magnifying glass.

**The sign table — memorize the logic, not the rows.** Positive means *where the light
actually goes.*

| | `f > 0` | `f < 0` | `i > 0` means | `i < 0` means |
|---|---|---|---|---|
| **Lens** | converging (convex) | diverging (concave) | real image, **opposite** side from object | virtual image, **same** side as object |
| **Mirror** | concave | convex | real image, **in front** (same side as object) | virtual image, **behind** the mirror |

`o > 0` always here. Diverging lenses and convex mirrors **can only** make virtual, upright,
minified images — no exceptions, no arithmetic needed.

**Predicts.** `i = of/(o − f)`. Converging with `o > f` → real, inverted; `o < f` → virtual, upright; `f < 0` →
`i < 0` always. **Real is always inverted; virtual always upright** — either identifies the other.

**Worked — full.** *A converging lens has f = +10 cm; an object sits 30 cm in front. Where is the
image?*
1. Principle: `1/o + 1/i = 1/f`; converging, `f` positive.
2. `1/i = 1/f − 1/o = 1/10 − 1/30`.
3. Common denominator: `3/30 − 1/30 = 2/30`.
4. Invert: `i = +15 cm` — real, on the far side, inverted.

**Faded — last step.** *Same lens, f = +10 cm, object now at 15 cm.*
1. Principle: `1/i = 1/f − 1/o = 1/10 − 1/15`.
2. Common denominator: `3/30 − 2/30 = 1/30`.
3. `i = ______`, which means the image is ______ and ______.

**Faded — last two.** *Same lens, f = +10 cm, object now at 5 cm — inside the focal length.*
1. Principle: `1/i = 1/f − 1/o`. Predict the sign before computing: the object is inside `f`.
2. `1/i = ______`
3. `i = ______`, image is ______ and ______.

**Check:** (2) `i = +30 cm`, real and inverted — halving `o` from 30 to 15 *doubled* `i`; the relation is
reciprocal, not linear. (3) `−1/10`, so `i = −10 cm`, **virtual, upright**, same side as the
object. Principle: a negative `i` reports rays that diverge and only *appear* to come from behind.

---

#### Magnification
FL1: **Q45** · CC4D · broke: reasoning — the ratio was computable from distances alone

**Structure.** `m = h_image/h_object = −i/o` — the middle expression is what is asked for, the right one is what you have, and the two heights are never both needed.

**Concrete.** The 6 cm candle at 5 m lands on your retina about 0.24 mm tall, smaller than a grain of salt, and
that is the whole visual world you have ever seen. The ratio `h_i/h_o` is 0.004, got by dividing
2 cm by 500 cm and signing it negative.

**Claims.** The height ratio equals the **distance ratio**, negated: "the ratio of image height to object
height" is answerable from `i` and `o` with no height information at all. Denies that a measured
object size is needed; denies that `m` is a size, since it is dimensionless. **`m < 0` means
inverted, hence real; `m > 0` means upright, hence virtual.**

**Predicts.** `|m| > 1` enlarged, `|m| < 1` reduced. Given `h_i`, `h_o = h_i·(o/i)`. Converging lens: beyond `2f`
reduced, at `2f` `|m| = 1`, between `f` and `2f` enlarged, inside `f` enlarged, upright, virtual.

**Worked — full.** *A 4 cm object sits 30 cm from a converging lens, f = +10 cm. Find the ratio of
image height to object height, and the image height.*
1. Principle: need `i` first — `1/i = 1/10 − 1/30 = 2/30`, `i = +15 cm`.
2. Principle: `m = −i/o`.
3. `m = −15/30 = −0.50`. That is `h_i/h_o`, the answer as asked.
4. `h_i = m · h_o = (−0.50)(4) = −2 cm`; negative height means inverted.

**Faded — last step.** *Same lens, object 2 cm tall at 15 cm; earlier we found i = +30 cm.*
1. Principle: `m = −i/o`.
2. `m = −30/15`.
3. `m = ______`, so the image is ______ and `h_i = ______`.

**Faded — last two.** *Same lens, object 3 cm tall at 5 cm; earlier we found i = −10 cm.*
1. Principle: `m = −i/o`, then `h_i = m · h_o`.
2. `m = ______`
3. Image is ______, ______, and `h_i = ______`.

**Check:** (2) `m = −2.0`, inverted and real, `h_i = −4 cm`. The object moved closer and the image got bigger
— outside `f`, approaching the focal point blows it up toward infinity. (3) `m = −(−10)/5 = +2.0`;
the double negative is where this is lost. **Upright and virtual**, `h_i = +6 cm`. Principle: the
sign decides orientation and image type together.

---

**Discriminators**

- **`n` vs Snell's law** — is there a boundary? One medium: `n = c/v`. Two media:
  `n₁ sin θ₁ = n₂ sin θ₂`.
- **Refraction vs total internal reflection** — is `n₁ > n₂`? Only then can a critical angle exist.
- **Converging lens vs concave mirror** — which side does a real image land on? Lens: the far side.
  Mirror: the object's side. Same equation.
- **Real vs virtual image** — is `i` positive? That one sign gives real/virtual, inverted/upright,
  and projectable-or-not.
- **Object outside `f` vs inside `f`** — is `1/o` bigger or smaller than `1/f`? Outside: real,
  inverted. Inside: virtual, upright, magnified.

**Compression** — the axis is **how far downstream of "light changed speed" the concept sits.**

| Concept | What the light changes | Governing relation |
|---|---|---|
| Index of refraction | **speed** (and wavelength; never frequency) | `n = c/v` |
| Snell's law | **direction** at a boundary | `n₁ sin θ₁ = n₂ sin θ₂` |
| Total internal reflection | direction, at its **limit** — no transmission | `sin θ_c = n₂/n₁`, needs `n₁ > n₂` |
| Thin lens / mirror equation | **where** rays reconverge | `1/o + 1/i = 1/f` |
| Magnification | **how big and which way up** the reconvergence is | `m = h_i/h_o = −i/o` |

---

## CLUSTER 2 — FLUIDS AND CIRCULATION
**FL1: Q18, Q21, Q26 · CC4B (2/4, 50%)**

**Shared scenario: one heartbeat's worth of blood.** The left ventricle squeezes, 70 mL leaves
through the aortic valve, and that bolus runs aorta → arteries → arterioles → capillary bed →
venules → veins → right heart → pulmonary artery → lung capillaries. Each concept is something
that happens to that same bolus at a different point.

---

#### Continuity equation — and why capillary flow is slow
FL1: **Q26** · CC4B · broke: **trap** — applied one-tube intuition to a branched bed

**Structure.** `Q = A·v = constant` for an incompressible fluid — and in a **branched** system `A` is the **summed** cross-section of every branch at that level.

**Concrete.** The aorta is one 4 cm² tube at about 30 cm/s, walking pace. Ten billion capillaries,
each so narrow a red cell folds through, total about 4000 cm², so blood slows to **0.03 cm/s** and
a red cell dwells about one second: exactly what gas exchange needs.

**Claims.** **Total** cross-section sets velocity, so branching pattern — not any single vessel's caliber —
determines local speed. Denies the garden-hose model this trap is built on: *narrow tube → faster
flow* holds only when the *same* tube narrows. Capillaries narrow and **multiply**, winning by
three orders of magnitude. Denies that friction or viscosity causes the slowness — resistance sets
the *pressure drop*, not the velocity.

**Predicts.** Velocity is **lowest** where total area is **highest**. `v = Q/A`; splitting area `A` into `n`
vessels of area `a` gives `v_new = v_old·A/(n·a)`. Rank by *inverse total area*: aorta > vena cava
> arterioles > capillaries.

**Worked — full.** *The aorta has area 4 cm² and blood moves at 30 cm/s; the capillary bed totals
4000 cm². Find capillary velocity.*
1. Principle: flow rate is conserved, `A₁v₁ = A₂v₂`.
2. `Q = (4)(30) = 120 cm³/s`.
3. `v₂ = Q/A₂ = 120/4000`.
4. `v₂ = 0.03 cm/s` — three orders slower, because the area is three orders larger.

**Faded — last step.** *A vessel of area 2 cm² carrying blood at 40 cm/s branches into 100
identical vessels of area 0.5 cm² each. Find the velocity in each branch.*
1. Principle: `A₁v₁ = A_total·v₂`, where `A_total` sums all branches.
2. `Q = (2)(40) = 80 cm³/s`; `A_total = 100 × 0.5 = 50 cm²`.
3. `v₂ = ______`

**Faded — last two.** *An artery of area 3 cm² carries blood at 20 cm/s; downstream total
cross-section is 300 cm². Find the downstream velocity, and whether a red cell spends more or less
time per centimeter there.*
1. Principle: `Q` is constant; `v = Q/A_total`.
2. `v_downstream = ______`
3. Time per centimeter: ______

**Check:** (2) `v₂ = 80/50 = 1.6 cm/s` — each branch (0.5 cm²) is *narrower* than the parent (2 cm²) and flow
still slowed, because 100 of them is 25× the parent's area. That is the Q26 trap. (3) `Q = 60
cm³/s`, `v = 0.2 cm/s`, so a red cell spends **100× longer** per centimeter.

---

#### Poiseuille flow and vascular resistance
FL1: — · CC4B · supports Q26, Q18

**Structure.** `Q = πΔP r⁴/(8ηL)`, i.e. `ΔP = Q·R` with `R = 8ηL/(π r⁴)` — resistance scales as **1/r⁴**, everything else linearly.

**Concrete.** Arterioles are the only vessels with real smooth muscle in the wall; blood enters at about 80 mmHg
and leaves at about 30. Constrict one to half its radius and resistance rises **sixteen-fold**:
one ring of muscle redirecting cardiac output between gut and muscle in seconds.

**Claims.** Resistance governs pressure drop, not velocity: `ΔP = QR`. Denies the conflation this cluster lives
or dies on — **resistance and velocity are different questions with different equations**:
continuity answers "how fast," Poiseuille "how much pressure does it cost." Capillaries have high
individual resistance *and* low velocity, and neither causes the other. Denies that halving radius
doubles resistance.

**Evidence.** Poiseuille assumes laminar, steady, Newtonian flow in a rigid cylinder; blood in
large arteries is pulsatile and non-Newtonian. The exam uses it anyway and expects `r⁴` scaling.

**Predicts.** Double the length → resistance × 2. Raise viscosity (polycythemia, dehydration) → proportional
rise. **Series resistances add; parallel total falls below the smallest** — why the capillary bed,
billions of tubes in parallel, contributes less total resistance than the arterioles.

**Worked — full.** *An arteriole constricts to half its radius; length, viscosity, and driving
pressure unchanged. What happens to flow?*
1. Principle: `Q ∝ r⁴` at fixed `ΔP`, `η`, `L`.
2. `(r/2)⁴ = r⁴/16`.
3. `Q_new = Q/16` — about 6% of baseline.

**Faded — last step.** *A vessel's radius is tripled; nothing else changes.*
1. Principle: `Q ∝ r⁴`.
2. `(3r)⁴ = 81 r⁴`.
3. Flow becomes ______ × baseline, and resistance becomes ______ × baseline.

**Faded — last two.** *Blood viscosity doubles (severe dehydration) and vessel radius falls by
half, at constant driving pressure.*
1. Principle: `Q = πΔP r⁴/(8ηL)` — track each factor separately, then multiply.
2. Factor from viscosity: ______; factor from radius: ______
3. Net flow: ______ × baseline.

**Check:** (2) Flow **× 81**, resistance **× 1/81** — reciprocal at fixed pressure, and reversing that is the
standard slip. (3) Viscosity `× 1/2`, radius `× 1/16`, net `Q = baseline/32`. Principle: the
factors are independent and multiply — do not add them.

---

#### Bernoulli's equation
FL1: — · CC4B · supports Q18

**Structure.** `P + ½ρv² + ρgh = constant` along a streamline — three energy densities, all in J/m³, trading against each other.

**Concrete.** Blood reaches a plaque narrowing the carotid to half its area. Continuity doubles its speed, so the
pressure term must fall: **pressure inside the stenosis is lower than on either side**, which lets
a diseased vessel collapse where it is already too narrow.

**Claims.** Energy per unit volume is conserved for an **ideal** fluid — no viscosity, no turbulence, steady
flow. Denies that fast fluid pushes harder sideways; the opposite is true, and that is the Venturi
effect. Denies its own universality: **Bernoulli does not explain the pressure drop from aorta to
vena cava** — that is viscous dissipation, Poiseuille's. A pressure drop at unchanged velocity and
height is never Bernoulli.

**Predicts.** At constant height, `v` up → `P` down by exactly `½ρ(v₂² − v₁²)`; at constant velocity, height up →
pressure down. Use the two laws **in that order, always**: continuity gives the velocity Bernoulli
needs. Draining from an open tank, `v = √(2gh)` — both pressures atmospheric, free-fall speed from
height `h`.

---

#### Hydrostatic pressure
FL1: — · CC4B · supports Q18

**Structure.** `P = P₀ + ρgh` — pressure in a static fluid depends only on depth, density, and `g`; not on container shape, volume, or surface area.

**Concrete.** Stand up. Your heart sits about 1.3 m above your feet, so ankle veins carry an extra
`ρgh = (1000)(10)(1.3) ≈ 1.3 × 10⁴ Pa` — about 100 mmHg of purely positional pressure, roughly
doubling what the heart supplies — and why a giraffe needs a 250 mmHg systolic. Lie down and `h`
goes to zero.

**Claims.** All points at the same depth in a connected static fluid are at the same pressure, whatever the
geometry (Pascal). Denies the volume intuition: a thin tube of water 10 m tall and a pool 10 m deep
have identical bottom pressure. Denies that pressure at depth pushes only downward — it is
isotropic.

**Predicts.** Every 10 m of water ≈ 1 atm. Standing → supine sends `ρgh` to zero for any body part. In a U-tube,
equal heights mean equal pressures at that level; a height difference `h` reports `ρgh`.
`1 mmHg = 133 Pa`; `760 mmHg = 1 atm = 1.01 × 10⁵ Pa`.

---

#### Systolic, diastolic, pulse, and mean pressure
FL1: **Q18** · CC4B · broke: reasoning — three named pressures, one relation, not retrieved

**Structure.** Four quantities, two definitions.
- `P_pulse = P_systolic − P_diastolic` — a **difference**, not a pressure level.
- `P_mean = P_diastolic + ⅓ P_pulse` — the time-weighted average over one cardiac cycle.

**Concrete.** A cuff reads 120/80. Pulse pressure is 40. Mean arterial pressure is **not** 100 — it
is `80 + 40/3 ≈ 93`, closer to diastolic because at rest the heart spends about **twice as long
relaxed as contracted**. The ⅓ is not a fudge factor: one-third systole, two-thirds diastole.

**Claims.** A strict ordering, `P_d < P_mean < P_s`, with `P_mean` **below the arithmetic midpoint**. Denies the
two reflexes AAMC builds distractors from: that mean pressure is `(P_s + P_d)/2`, and that pulse
pressure sits on the same axis as the others. `P_pulse` is a **span** — smaller than all three and
still correct. Any choice implying `P_mean ≥ (P_s + P_d)/2`, or ordering `P_pulse` among the
levels, is wrong on structure alone.

**Predicts.** Given any two of `P_s`, `P_d`, `P_pulse`, subtract for the third, then `P_mean = P_d + P_pulse/3`.
Stiff arteries (age, atherosclerosis) → **wider** pulse pressure at the same mean. Tachycardia
shortens diastole, drifting the ⅓ toward ½. On sight: `P_mean = (P_s + 2P_d)/3`,
`P_s = 3P_mean − 2P_d`.

**Worked — full.** *A pulmonary artery reads 25/8 mmHg. Find pulse pressure and mean pressure.*
1. Principle: pulse pressure is a difference. `P_pulse = 25 − 8 = 17 mmHg`.
2. Principle: mean sits one-third up the pulse from diastolic, `P_mean = P_d + P_pulse/3`.
3. `P_mean = 8 + 17/3 = 8 + 5.7`.
4. `P_mean ≈ 13.7 ≈ 14 mmHg`. Ordering check: `8 < 14 < 25`. Valid.

**Faded — last step.** *A systemic artery reads 140/90 mmHg.*
1. Principle: `P_pulse = P_s − P_d = 140 − 90 = 50 mmHg`.
2. Principle: `P_mean = P_d + P_pulse/3 = 90 + 50/3`.
3. `P_mean = ______`, and confirm it falls between ______ and ______.

**Faded — last two.** *A patient's mean arterial pressure is 100 mmHg and diastolic is 85 mmHg.
Find pulse pressure and systolic pressure.*
1. Principle: run `P_mean = P_d + P_pulse/3` backwards.
2. `P_pulse = ______`
3. `P_s = ______`

**Check:** (2) `P_mean ≈ 106.7 ≈ 107 mmHg`, between 90 and 140 and **below** the midpoint of 115 — landing on 115
means you used the arithmetic mean, the primary distractor. (3) `100 − 85 = 15 = P_pulse/3`, so
`P_pulse = 45`, `P_s = 130`. Principle: the relation is invertible, and AAMC gives you whichever
two are least convenient.

---

#### Work done by the heart
FL1: **Q21** · CC4B · broke: reasoning — didn't recognize `W = PΔV` as the applicable form

**Structure.** `W = P·ΔV`, straight from `W = F·d` with `F = P·A`; units confirm it, `Pa·m³ = N·m = J`. Power: `Power = W/t = P·Q`.

**Concrete.** Each beat the left ventricle pushes 70 mL against a mean arterial pressure of about 95 mmHg:
`(1.3 × 10⁴ Pa)(7 × 10⁻⁵ m³) ≈ 0.9 J`, the energy of dropping an apple 10 cm — roughly 1 watt at
70 beats a minute, all day, forever.

**Claims.** For fluid moved at roughly constant pressure, work is pressure times volume displaced, and **no
force, distance, or vessel dimension is needed** — the geometry already cancelled. Denies the
instinct to reach for `W = Fd` and hunt for an artery's length and cross-section. Denies that
velocity or flow rate is needed: those give *power*. Joules asked → a volume; watts asked → a rate.

**Predicts.** The product **once both are in SI**, and the conversion is where the question is lost:
`1 L = 10⁻³ m³`, `1 mmHg = 133 Pa`. Doubling volume or pressure doubles the work; nine liters at
the same pressure as 70 mL is 128× the work.

**Worked — full.** *How much work does the heart do pushing 5.0 L of blood at a mean pressure of
100 mmHg?*
1. Principle: fluid displaced against pressure, `W = PΔV`.
2. Pressure to SI: `100 × 133 = 1.33 × 10⁴ Pa`.
3. Volume to SI: `5.0 L = 5.0 × 10⁻³ m³`.
4. `W = (1.33 × 10⁴)(5.0 × 10⁻³) = 66.5 J ≈ 67 J`.

**Faded — last step.** *Find the work circulating 9.0 L of blood through an artery held at
1.3 × 10⁴ Pa.*
1. Principle: `W = PΔV`; pressure already in Pa.
2. Convert volume: `9.0 L = 9.0 × 10⁻³ m³`.
3. `W = ______`

**Faded — last two.** *Find the work circulating 9.0 L of blood at a mean pressure of 120 mmHg.*
1. Principle: `W = PΔV`, both quantities in SI first.
2. `P = ______ Pa`; `ΔV = ______ m³`
3. `W = ______ J`

**Check:** (2) `W = (1.3 × 10⁴)(9.0 × 10⁻³) = 117 ≈ 120 J` — multiply mantissas (`1.3 × 9.0 = 11.7`), add
exponents. (3)
`P ≈ 1.6 × 10⁴ Pa`, `ΔV = 9.0 × 10⁻³ m³`, `W ≈ 144 J`. Principle: the whole difficulty is unit
conversion, not physics — off by 1000 means you left volume in liters.

---

**Discriminators**

- **Continuity vs Poiseuille** — *speed* or *pressure cost*? Speed: `A·v = Q`. Pressure drop:
  `ΔP = QR`, `R ∝ 1/r⁴`. Q26 is a speed question and the `r⁴` reflex is the trap.
- **Continuity vs Bernoulli** — continuity gives the new velocity; Bernoulli converts it into a
  pressure. Always that order, never the reverse.
- **Bernoulli vs Poiseuille** — is the fluid ideal? Bernoulli only moves energy between terms;
  Poiseuille **dissipates** it. A pressure drop at unchanged velocity and height is viscous.
- **One tube narrowing vs a bed branching** — did total cross-section go down or up? Narrowing:
  velocity up. Branching: velocity down, though each branch is narrower.
- **Pulse pressure vs the other three** — level or span? `P_pulse` is the only difference; it never
  belongs in an ordering with `P_s`, `P_d`, `P_mean`.
- **Work vs power** — given a volume or a flow rate? Volume → `W = PΔV`, joules. Rate →
  `Power = PQ`, watts.

**Compression** — the axis is **what stays constant along the flow path.**

| Concept | What is conserved | What that forces |
|---|---|---|
| Continuity | **volume flow rate `Q`** | area up ⇒ velocity down (capillaries) |
| Bernoulli | **total energy density** `P + ½ρv² + ρgh` | velocity up ⇒ pressure down |
| Poiseuille | **nothing — energy is dissipated** | pressure falls along the tube, `ΔP = QR` |
| Hydrostatic `ρgh` | **no flow at all** | pressure set by depth alone |
| `P_s`, `P_d`, `P_pulse`, `P_mean` | the cycle's **time weighting** (⅓ systole) | `P_mean` sits below the midpoint |
| `W = PΔV` | **energy accounting** across the whole trip | joules per volume moved, geometry cancels |

---

## CLUSTER 3 — CIRCUITS
**FL1: Q56 · CC4C (2/5, 40% — worst C/P content category)**

**Shared scenario: one bench circuit.** A battery, wires, and one or two identical 60 Ω bulbs. Put
them in a line or side by side, insert a resistor, swap the battery. Every concept below is a
rearrangement of these same parts.

---

#### Ohm's law and resistance
FL1: **Q56** · CC4C · broke: reasoning + timing — final third, clock gone

**Structure.** `V = IR` — push, flow, obstruction — with `I = ΔQ/Δt` in amperes (coulombs per second) and resistance from geometry, `R = ρL/A`.

**Concrete.** A 12 V battery drives a 60 Ω bulb: `I = 12/60 = 0.2 A`, a fifth of a coulomb through the filament
every second. Swap in a 30 Ω bulb and current doubles to 0.4 A and it glows brighter. The battery
did not change; the obstruction did.

**Claims.** Two of the three quantities determine the third — but you must know **which one the circuit holds
fixed**: a battery fixes voltage, not current. Denies that a higher-resistance element always
carries less current *and* less power; both hold on fixed voltage, both reverse in **series**.
Denies that `R` depends on the current — it is material and geometry.

**Predicts.** Fixed `V`: `R` up → `I` down. Fixed `I` (series branch): `R` up → the voltage *across that element*
up. From `R = ρL/A`: double the length → double `R`; double the diameter → quarter the `R`.

---

#### Series and parallel
FL1: **Q56** · CC4C · broke: reasoning — reduction step skipped under time

**Structure.**
- **Series:** `R_eq = R₁ + R₂ + …`. **Current is the same everywhere; voltage divides.**
- **Parallel:** `1/R_eq = 1/R₁ + 1/R₂ + …`. **Voltage is the same across every branch; current
  divides.** Two resistors: `R_eq = R₁R₂/(R₁+R₂)`. `n` identical: `R_eq = R/n`.

**Concrete.** Both 60 Ω bulbs in a line on the 12 V battery: 120 Ω, 0.1 A through both, 6 V each, both dim. Side
by side: each sees 12 V, each pulls 0.2 A, the battery delivers 0.4 A, both bright — **four times
the power**. Unscrew one: in series everything goes dark; in parallel the other does not flicker.

**Claims.** Adding a resistor in **parallel always lowers** total resistance, below even the smallest branch,
because you added a path and not an obstacle. Denies the near-universal model that more components
means more resistance. Brightness is **power dissipated**, and the wiring decides which element
gets more: series shares current, so `P = I²R` and the **larger** resistance is brighter; parallel
shares voltage, so `P = V²/R` and the **smaller** is.

**Predicts.** Add a parallel branch → `R_eq` falls → total current rises → battery drains faster. Add a series
element → everything dims. In a series chain, `V₁ = V_total·R₁/R_total`. Short-circuiting something
in parallel drops that pair's resistance to zero.

---

#### Current division
FL1: **Q56** · CC4C · broke: reasoning

**Structure.** For two parallel branches carrying total `I`: `I₁ = I · R₂/(R₁ + R₂)` — proportional to the **other** branch's resistance; safer still, find the shared branch voltage and use `I₁ = V/R₁`.

**Concrete.** 12 V across a 60 Ω bulb in parallel with a 30 Ω bulb. Both see 12 V; the 60 Ω takes
0.2 A, the 30 Ω takes 0.4 A, total 0.6 A — **twice as much down the path with half the
resistance**, exactly what blood does at an arteriolar branch.

**Claims.** In parallel, current splits **inversely** with resistance and every branch sees the same voltage.
Denies the reflex of writing `I₁ = I·R₁/(R₁+R₂)` by analogy with the voltage divider — the
numerator is the *opposite* resistance. Denies that current is "used up": whatever enters a
junction leaves it, exactly like `Q = Av` at a vessel branch.

**Predicts.** More current takes the lower-resistance path, always; the split is `R₂ : R₁` — note the swap. For
one specific element, never use the divider formula: get `R_eq`, total current, the voltage across
the parallel section, then divide by that element's resistance.

**Worked — full.** *A household bulb is rated 60 W at 120 V. Find its current and resistance.*
1. Principle: power in a resistive element, `P = IV`.
2. `I = P/V = 60/120`.
3. `I = 0.5 A`.
4. Ohm's law: `R = V/I = 120/0.5 = 240 Ω`.

**Faded — last step.** *A 9 V battery drives a 30 Ω bulb in series with a 15 Ω resistor. How much
current passes through the bulb?*
1. Principle: series — resistances add, current is the same in both. `R_eq = 45 Ω`.
2. Principle: Ohm's law on the loop. `I = V/R_eq = 9/45`.
3. `I = ______ A`, and the current through the bulb is ______ than this.

**Faded — last two.** *A 12 V battery drives two 60 Ω bulbs in parallel. How much current passes
through one bulb, and how much leaves the battery?*
1. Principle: parallel branches share the full battery voltage; get one bulb's current from Ohm's
   law, then sum.
2. `I_one bulb = ______`
3. `I_total = ______`, and `R_eq = ______`

**Check:** (2) `I = 0.2 A`, and the bulb carries **exactly** that, not less — series is one path, so dividing
again imports a parallel rule. (3) Each bulb sees 12 V, so `I = 0.2 A`, `I_total = 0.4 A`,
`R_eq = 30 Ω`. Principle: in parallel, work per-branch and sum — never divide the voltage.

---

#### Power
FL1: **Q56** · CC4C · supports

**Structure.** `P = IV`, and with Ohm's law substituted, `P = I²R` and `P = V²/R` — three forms of one statement; watts = J/s, and `E = Pt`.

**Concrete.** The 60 Ω bulb on 12 V burns `V²/R = 144/60 = 2.4 W`. Add a second identical bulb in **series** and
each drops 6 V, burning `36/60 = 0.6 W` — the pair uses 1.2 W, *half* what one bulb used alone. Add
it in **parallel** and each still burns 2.4 W, total 4.8 W.

**Claims.** The three forms are algebraically identical but **not interchangeable in practice** — pick the one
whose variables the circuit holds constant. Denies that any single form settles "more resistance
means more power": `I²R` says it raises power, `V²/R` says it lowers it, both true of different
questions. **Use `I²R` when current is shared (series), `V²/R` when voltage is shared (parallel).**

**Predicts.** Series: the biggest resistor glows brightest. Parallel: the smallest does. Total battery power is
`P = I_total·V_battery` regardless of arrangement. A bulb's *rating* (60 W at 120 V) fixes its
resistance, not its power — run it at 60 V and it burns 15 W, because power goes as `V²`.

---

#### Capacitors
FL1: — · CC4C · supports; this category is 40% and capacitors are half of it

**Structure.** `C = Q/V`; parallel plate `C = κε₀A/d`; stored energy `U = ½CV² = ½QV = Q²/2C`. Combination rules **mirror** resistors: **parallel capacitors add** (`C_eq = C₁ + C₂`), **series add reciprocally** (`1/C_eq = 1/C₁ + 1/C₂`).

**Concrete.** Two metal plates 1 mm apart across a battery: charge piles on one face and drains off the other
until plate voltage matches the battery's, then current stops. Slide plastic between them and
capacitance jumps by `κ` — the slab polarizes, partly cancelling the field, so the same voltage
holds more charge. A defibrillator is this, scaled: 200 J into a chest in 5 ms.

**Claims.** A capacitor stores **charge and energy**, not current: at steady state nothing flows through it, so
in a DC circuit it is eventually an open circuit and a parallel wire carries everything. Denies
that capacitors combine like resistors — in series capacitance *falls*, because that effectively
widens the plate separation. Denies that a dielectric works by conducting; it polarizes, raising
`C` by exactly `κ`.

**Predicts.** Series capacitors: same **charge**, voltage divides. Parallel: same **voltage**, charge divides —
opposite to resistors. Dielectric in at fixed voltage → `C`, `Q`, `U` all up. Increase `d` at fixed
charge → `C` down, `V` up, `U` up (you did work pulling the plates apart).

---

**Discriminators**

- **Series vs parallel** — one path or several? One path: current shared, voltages add. Several:
  voltage shared, currents add.
- **`P = I²R` vs `P = V²/R`** — which quantity does the circuit hold constant? Series holds current
  → `I²R`. Parallel holds voltage → `V²/R`. This decides every "which bulb is brighter" item.
- **Voltage divider vs current divider** — same resistor in the numerator, or the other one?
  Voltage: `V₁ = V·R₁/(R₁+R₂)`, same. Current: `I₁ = I·R₂/(R₁+R₂)`, **other**.
- **Resistors vs capacitors in combination** — resistors add in series, capacitors add in parallel;
  the words tell you nothing. Anchor on one fact — *series capacitors are like one capacitor with
  wider plates* — and derive the rest.
- **Adding a component in series vs parallel** — an obstacle or a path? Series adds resistance and
  dims everything. Parallel lowers total resistance and raises battery current.

**Compression** — the axis is **what the elements share and what divides between them.**

| Arrangement | Shared | Divides | Equivalent | Bigger element gets |
|---|---|---|---|---|
| Resistors in **series** | current `I` | voltage `V` | `R₁ + R₂` | more voltage, more power (`I²R`) |
| Resistors in **parallel** | voltage `V` | current `I` | `R₁R₂/(R₁+R₂)` | less current, less power (`V²/R`) |
| Capacitors in **series** | charge `Q` | voltage `V` | `C₁C₂/(C₁+C₂)` | less voltage |
| Capacitors in **parallel** | voltage `V` | charge `Q` | `C₁ + C₂` | more charge |

---

## CLUSTER 4 — ELECTROCHEMISTRY
**FL1: Q53, Q54, Q55 · CC4C**

**Read the diagnosis before the content.** All three misses came from **one passage** in the
**final third** of C/P, where he finished with 0.6 minutes to spare and left Q39 blank.
Section-half Skill-2 accuracy was 77% → 43%. These were answered with the clock gone, not with the
concept missing. **This cluster gets the smallest share of study time.** Learn the procedure, run
the two ladders, move on.

**Shared scenario: two metal strips and a beaker.** A zinc strip and a copper strip. In separate
half-cells with a wire and a salt bridge, they are a battery. Drop either into hydrochloric acid
and one of them fizzes. Hook a power supply across them backwards and the whole thing runs uphill.
Same two metals, three outcomes, one number decides all of it.

---

#### Reduction potentials and cell potential
FL1: **Q54** · CC4C · broke: timing — procedure not run

**Structure.** Every half-reaction is tabulated as a **reduction** with `E°_red` in volts; the more positive `E°_red` is reduced (**cathode**), the other runs backwards as oxidation (**anode**), and `E°_cell = E°_cathode − E°_anode`, both read straight off the reduction table.

**Concrete.** Zinc reads −0.76 V, copper +0.34 V, so copper is reduced: `Cu²⁺ + 2e⁻ → Cu` at the cathode,
`Zn → Zn²⁺ + 2e⁻` at the anode, `E°_cell = 0.34 − (−0.76) = 1.10 V`. Drop zinc into copper sulfate
and it happens with no wire — the strip darkens as copper plates onto it and the blue drains away.

**Claims.** The table is a **ranking of oxidizing strength**: most positive = strongest oxidizing agents, most
negative (as reduced metal) = strongest reducing agents. Denies the most expensive error here —
**`E°` is intensive and is never multiplied by stoichiometric coefficients**; doubling a
half-reaction leaves `E°` alone and changes `ΔG`. Denies flipping the sign of `E°` on reversing a
half-reaction *and* subtracting: `E°_cathode − E°_anode` already handles the flip.

**Predicts.** Cathode is the more positive `E°_red`; subtract, read the sign. Positive `E°_cell` → the reaction
as written goes forward. Any species oxidizes anything **below** it on the table and nothing above.

---

#### Spontaneity
FL1: **Q55** · CC4C · broke: timing — one sign check

**Structure.** `ΔG° = −nFE°_cell` with `n` = moles of electrons and `F ≈ 96,500 C/mol`; the minus sign is the whole content — **positive `E°_cell` ⇔ negative `ΔG°` ⇔ spontaneous ⇔ `K > 1`.**

**Concrete.** The zinc–copper cell runs at +1.10 V with 2 electrons: `ΔG° = −(2)(96,500)(1.10) ≈ −212 kJ`,
enormously downhill, which is why it lights a bulb until the zinc is gone. Reverse the pairing and
`E°_cell` is −1.10 V, `ΔG°` is +212 kJ, and nothing happens.

**Claims.** The **sign of `E°_cell` alone** answers "will this occur spontaneously" — you need neither `ΔG` nor
`n` nor `F` unless the item asks for joules. Denies that a large `E°` means a *fast* reaction:
`E°` and `ΔG` are thermodynamic and say nothing about rate. Denies that `n` affects spontaneity —
it scales the magnitude of `ΔG°`, never its sign.

**Predicts.** Positive `E°_cell` → spontaneous, galvanic, `ΔG° < 0`, `K > 1`; negative → driven, electrolytic,
`ΔG° > 0`, `K < 1`. Concentration shifts `E` off `E°` (Nernst: more reactant or less product makes
`E` **more positive**) but never flips a strongly signed cell. A **concentration cell** is the
limiting case — identical electrodes, `E° = 0`, driven only by the concentration difference,
reaching zero when the sides equalize.

**Worked — full.** *Zn²⁺/Zn has E° = −0.76 V; Cu²⁺/Cu has E° = +0.34 V. Will Zn metal reduce Cu²⁺
spontaneously? Find `E°_cell` and `ΔG°`.*
1. Principle: the more positive `E°_red` is reduced. `+0.34 > −0.76`, so Cu²⁺ is the cathode and Zn
   the anode — matching the reaction as proposed.
2. Principle: `E°_cell = E°_cathode − E°_anode = 0.34 − (−0.76)`.
3. `E°_cell = +1.10 V`. Positive → spontaneous.
4. Principle: `ΔG° = −nFE°`, `n = 2`. `ΔG° = −(2)(96,500)(1.10) ≈ −2.1 × 10⁵ J = −212 kJ`.

**Faded — last step.** *Ag⁺/Ag has E° = +0.80 V; Fe²⁺/Fe has E° = −0.44 V. Will Fe metal reduce
Ag⁺?*
1. Principle: `+0.80 > −0.44`, so Ag⁺ is reduced (cathode) and Fe oxidized (anode).
2. Principle: `E°_cell = E°_cathode − E°_anode = 0.80 − (−0.44)`.
3. `E°_cell = ______ V`, therefore ______.

**Faded — last two.** *Balancing the silver reaction requires `2Ag⁺ + Fe → 2Ag + Fe²⁺`. Does
doubling the silver half-reaction change `E°_cell`? Find `ΔG°`.*
1. Principle: decide first whether `E°` is intensive or extensive, then apply `ΔG° = −nFE°` with the
   correct `n`.
2. `E°_cell` after doubling = ______
3. `ΔG° = ______`

**Check:** (2) `E°_cell = +1.24 V`, **spontaneous** — iron does displace silver. (3) `E°_cell` is **unchanged
at +1.24 V**; potential is intensive, like temperature. `n = 2`, so `ΔG° ≈ −2.4 × 10⁵ J = −239 kJ`.
Principle, the costliest in this category: **coefficients change `n` and therefore `ΔG`, and never
change `E°`.**

---

#### Galvanic vs electrolytic
FL1: — · CC4C · supports Q54, Q55

**Structure.** Both cells share the definitions — **oxidation at the anode, reduction at the cathode, electrons through the external wire from anode to cathode** — and differ only in the sign of `E°_cell`, hence which electrode is labeled + and −.

| | Galvanic (voltaic) | Electrolytic |
|---|---|---|
| `E°_cell` | positive | negative |
| `ΔG` | negative — spontaneous | positive — must be driven |
| Energy | chemical → electrical | electrical → chemical |
| **Anode** | oxidation, **negative** terminal | oxidation, **positive** terminal |
| **Cathode** | reduction, **positive** terminal | reduction, **negative** terminal |

**Concrete.** Run forward, the cell is a battery: zinc dissolves, electrons pour into the wire, and that
electrode is negative because it is the *source* of electrons. Force it backwards with a power
supply to replate the zinc: the chemistry at each electrode swaps, and the supply's positive
terminal now *pulls* electrons out of whichever electrode is oxidized, so the anode is labeled
positive. **The chemistry never moved; only the wiring did.**

**Claims.** Anode and cathode are defined by the **reaction**, not by charge, and are identical in both cell
types. Denies the widespread belief that the anode is always negative. Denies that recharging
reverses the definitions — it reverses which physical electrode plays which role. Anions migrate
toward the anode and cations toward the cathode in **both**.

**Predicts.** From `E°_cell` alone: cell type, `ΔG` sign, both terminal signs. On recharge, the discharge cathode
becomes the anode. **Faraday's law** for anything plated or evolved: `moles of electrons = It/F`,
divided by electrons per formula unit. Doubling current or time doubles the mass; a 3+ ion needs
1.5× the charge of a 2+ ion for the same moles.

---

#### Galvanic (voltaic) cell
FL1: — · CC4C · supports Q54, Q55

**Structure.** A **spontaneous** redox reaction split into two half-cells so its electrons must travel through a wire: `E°_cell > 0`, `ΔG < 0`, chemical energy → electrical. Electrons leave the anode (oxidation; the **negative** terminal, because that is where electrons are produced), cross the wire, and arrive at the cathode (reduction; **positive**). The salt bridge passes ions — anions toward the anode, cations toward the cathode — so neither beaker builds up charge and stalls the reaction.

**Concrete.** Zinc in zinc sulfate, copper in copper sulfate, a wire and a salt bridge between them. The bulb lights. Over the afternoon the zinc strip thins and roughens, the copper strip thickens, and the blue on the copper side pales as Cu²⁺ plates out. The meter reads 1.10 V at the start and drifts down as Zn²⁺ builds and Cu²⁺ is spent; pull the salt bridge and the bulb goes out at once.

**Claims.** Asserts the cell produces a voltage because the reaction *wants* to go — the voltage is the reaction's spontaneity expressed in volts. Denies that the terminal signs are a convention: the anode is negative *because* oxidation pumps electrons into it. Denies that the salt bridge carries electrons; it carries ions, and without it the anode beaker goes positive and the cathode beaker negative until nothing more can move. Every battery is one of these.

**Predicts.** Given two `E°_red` values, the more positive is the cathode; the meter reads `E°_cathode − E°_anode`. Anode loses mass if its metal is the species oxidized; cathode gains mass if the cation plates. Running the cell moves concentrations in the direction that lowers `E`, until `E = 0` — a dead battery is a cell at equilibrium. "Which electrode is negative" → the anode, in this cell type only.

---

#### Electrolytic cell
FL1: — · CC4C · supports Q54, Q55

**Structure.** A **non-spontaneous** redox reaction driven by an external source whose voltage exceeds `|E°_cell|`: `E°_cell < 0`, `ΔG > 0`, electrical energy → chemical. The supply's positive terminal *pulls* electrons out of one electrode — that one is oxidized, so it is the anode, and it is **positive**; its negative terminal *pushes* electrons into the other — reduction, cathode, **negative**. Same definitions as the galvanic cell, opposite signs.

**Concrete.** The same beakers, with a power supply set above 1.10 V clipped across them backwards. Now the zinc strip *grows* — Zn²⁺ is forced back onto it (cathode, on the supply's negative clip) — and the copper strip dissolves into blue (anode, on the positive clip). Recharging the lead-storage battery in a car is this exact operation: the alternator drives the discharge reaction in reverse.

**Claims.** Asserts oxidation is still at the anode and reduction still at the cathode — the labels follow the reaction, and the reaction at each physical electrode has been reversed. Denies "the anode is negative" as a rule; it is negative in a galvanic cell and positive here. Denies that the supply changes what is favorable: it does not make `ΔG` negative, it pays the positive `ΔG` in electrical work, and must supply at least `|E°_cell|` to do so. Denies that electrons travel through the solution — ions do, anions to the anode as always.

**Predicts.** `E°_cell` negative, or a stem with "a current is passed through," "electrolysis," "plating," "recharging" → electrolytic. The electrode clipped to the supply's positive terminal is the anode: write the oxidation there. On recharge, the electrode that was the cathode on discharge is now the anode — its *sign* has not changed, its *role* has. Minimum applied voltage = `|E°_cell|`; how much is deposited is Faraday's law, below.

---

#### Anode
FL1: — · CC4C · supports Q53, Q54

**Structure.** The electrode where **oxidation** happens: a species gives up electrons, and those electrons enter the external circuit from here. Anions migrate toward it — that is what "anion" means. Its *sign* depends on the cell: **negative** in a galvanic cell (electron source), **positive** in an electrolytic cell (the supply is pulling electrons out).

**Concrete.** In the battery, the zinc strip: it thins because `Zn → Zn²⁺ + 2e⁻` is eating it, and it is the negative post. Under the power supply, the copper strip: it thins because `Cu → Cu²⁺ + 2e⁻` is eating *it*, and it is on the positive clip. Two different pieces of metal, one name, because the same thing — metal dissolving, electrons leaving — happens at each.

**Claims.** Asserts the anode is defined by its chemistry and nothing else. Denies that it is the negative electrode by definition — the most-tested false belief in the container. Denies that it attracts cations; it attracts anions, in both cell types, because oxidation is making the electrolyte around it positive and negative ions move in to balance. Denies that the anode always loses mass: if the species oxidized is an ion or water (`2H₂O → O₂ + 4H⁺ + 4e⁻`), the electrode is inert and a gas comes off instead.

**Predicts.** "At the anode" → write the oxidation half-reaction. "Which electrode loses mass" → the anode, if its own metal is what oxidizes. "Which way do anions move" → toward the anode, in any cell. Sign: ask first which cell type you are in — galvanic, negative; electrolytic, positive. Electrons in the wire leave the anode; conventional current in the wire arrives at it.

---

#### Cathode
FL1: — · CC4C · supports Q53, Q54

**Structure.** The electrode where **reduction** happens: electrons arrive from the external circuit and are consumed by a species that gains them. Cations migrate toward it. Its sign: **positive** in a galvanic cell (electrons are being drawn in), **negative** in an electrolytic cell (the supply is pushing electrons in).

**Concrete.** In the battery, the copper strip: it thickens as `Cu²⁺ + 2e⁻ → Cu` plates on, the blue fades around it, and it is the positive post. Under the power supply, the zinc strip: it regrows as `Zn²⁺ + 2e⁻ → Zn`, on the negative clip. In acid, hydrogen bubbles off the cathode — `2H⁺ + 2e⁻ → H₂` — which is the fizz in the metal-plus-acid block.

**Claims.** Asserts the cathode is defined by reduction, so metal plating and hydrogen evolution are cathode events in every cell. Denies that it is the positive electrode by definition. Denies that a cation is reduced at the anode under any wiring. Denies that the electrode metal itself must react: a platinum or graphite cathode just hands electrons to whatever in the solution is most reducible.

**Predicts.** "At the cathode" → write the reduction half-reaction. "Metal deposited," "gas evolved at the negative electrode during electrolysis," "mass gained" → cathode, and the amount is Faraday's law. "Which way do cations move" → toward the cathode, in any cell. **Anode vs cathode is one question: are electrons leaving the species, or arriving?** Sign is a second question, answered by cell type.

---

#### Faraday's law
FL1: — · CC4C · supports Q53–Q55 · **added — not a table row; an outline bullet named in the container's Predicts and the trigger table with no ladder anywhere**

**Structure.** Charge is current times time, `Q = It`; **`F ≈ 96,500 C` is the charge on one mole of electrons**, so `mol e⁻ = It/F`; divide by the electrons each ion needs, multiply by molar mass. Four steps, one operation each.

**Concrete.** The copper strip under the power supply for 1930 s at 2.00 A gains 1.27 g. Run the current twice as long and it gains 2.54 g. Swap the solution for silver nitrate and the same charge deposits 4.32 g of silver — more than three times the mass, because each Ag⁺ needs one electron where each Cu²⁺ needs two, and silver is heavier.

**Claims.** Asserts the amount deposited or evolved is fixed by **charge and the ion's charge alone**. Denies that voltage matters once it clears the threshold — doubling the voltage does not double the mass; doubling the current or the time does. Denies that concentration or temperature enter (provided the ion does not run out). Denies that all ions plate equally per coulomb: per mole of electrons you get one mole of Ag, half a mole of Cu, a third of a mole of Al.

**Predicts.** Mass ∝ `It`, and at fixed charge mass ∝ molar mass ÷ electrons per ion. A 3+ ion needs 1.5× the charge of a 2+ ion for the same number of atoms. Gas: moles from the same ladder, then 22.4 L/mol at STP. Any "how much" stem in electrochemistry is this ladder and nothing else.

**Worked — full.** *A current of 2.00 A runs through CuSO₄ solution for 1930 s. What mass of copper (63.5 g/mol) deposits on the cathode?*
1. Principle: charge is current × time. `Q = It = (2.00)(1930) = 3860 C`.
2. Principle: one mole of electrons carries `F ≈ 96,500 C`. `mol e⁻ = 3860 / 96,500 = 0.0400 mol`.
3. Principle: read electrons per ion from the half-reaction. `Cu²⁺ + 2e⁻ → Cu`, so `mol Cu = 0.0400 / 2 = 0.0200 mol`.
4. `mass = (0.0200)(63.5) = 1.27 g`.

**Faded — last step.** *The same 3860 C passes through AgNO₃ solution. What mass of silver (108 g/mol) deposits?*
1. Principle: `mol e⁻ = 3860 / 96,500 = 0.0400 mol`.
2. Principle: `Ag⁺ + e⁻ → Ag`, one electron per atom, so `mol Ag = 0.0400 mol`.
3. `mass = ______ g`

**Faded — last two.** *A current of 3.00 A runs for 1930 s through a solution of Cr³⁺ (52 g/mol). Find the moles and mass of chromium deposited, and say why it is the same number of atoms as the copper above despite 1.5× the charge.*
1. Principle: `Q = It`, then `mol e⁻ = Q/F`, then divide by electrons per ion.
2. `mol Cr = ______`
3. `mass Cr = ______`; same atom count as copper because ______

**Check:** (3) `mass Ag = (0.0400)(108) = 4.32 g`. (2) `Q = 5790 C`, `mol e⁻ = 0.0600`, `mol Cr = 0.0600 / 3 = 0.0200 mol`. (3) `mass = (0.0200)(52) = 1.04 g`; the atom count matches copper's because a 3+ ion needs 1.5× the electrons of a 2+ ion, and the charge was 1.5×. Principle: **charge buys electrons; the ion's charge sets how many electrons buy one atom.**

---

#### Concentration cell
FL1: — · CC4C · supports Q55 · **added — not a table row; an outline bullet ("Concentration cell") that appears in this cluster only as a clause inside Spontaneity's Predicts**

**Structure.** Two half-cells with the **same** metal and the **same** ion at **different concentrations**: `E° = 0` because the half-reactions are identical, yet `E > 0` because equalizing the concentrations is downhill. The dilute side is the **anode** — its metal dissolves to raise its ion concentration; the concentrated side is the **cathode** — its ions plate out to lower theirs. Electrons flow dilute → concentrated, and `E` falls to zero as the two sides meet.

**Concrete.** Two copper strips, two copper sulfate beakers, one at 0.01 M and one at 1.0 M, wire and bridge. The meter reads a few hundredths of a volt — real, small — and all of it comes from the difference in blue. The pale beaker's strip thins; the dark beaker's strip thickens; the pale one darkens and the dark one pales until they match, and then the meter reads zero.

**Claims.** Asserts a voltage can exist with no difference in chemistry at all — only a difference in concentration — which is the Nernst equation's concentration term doing all the work with `E° = 0`. Denies that the concentrated side is the anode: the system moves to *equalize*, so the dilute side must gain ions (oxidation) and the concentrated side lose them (reduction). Denies that `E°_cell = 0` means nothing happens; it means the standard-state cell does nothing, and this cell is not at standard state.

**Predicts.** Identical electrodes, different concentrations → concentration cell; `E° = 0`; electrons flow **from the dilute half-cell to the concentrated one**; the cathode is in the concentrated beaker. A larger concentration ratio raises `E`; a tenfold ratio gives about 30 mV for a 2+ ion. A neuron's membrane potential is the same physics — one ion, two concentrations, a voltage — which is why the same equation appears on both sides of the exam.

---

#### Metal plus acid — the activity series
FL1: **Q53** · CC4C · broke: timing — one comparison against zero

**Structure.** With the standard hydrogen electrode `2H⁺ + 2e⁻ → H₂` at `E° = 0.00 V` **by definition**, a metal in strong acid evolves H₂ exactly when `E°_cell = 0.00 − E°_red(Mⁿ⁺/M) > 0`, i.e. when **`E°_red(Mⁿ⁺/M) < 0`** — the metals **above** hydrogen in the activity series.

**Concrete.** Drop a zinc strip in 1 M HCl and it fizzes: zinc is −0.76, so `0.00 − (−0.76) = +0.76 V`. Drop a
copper penny in the same beaker and **nothing happens, ever** — copper is +0.34, so `−0.34 V`. Move
the penny to nitric acid and it dissolves in brown gas, because nitrate (`NO₃⁻`, `E° ≈ +0.96 V`)
outranks H⁺ as an oxidant.

**Claims.** "Will this metal react with acid" is a **single comparison against zero**, needing no arithmetic
once you read `E°_red`. Denies that acid strength decides it: 12 M HCl will not touch copper,
silver, platinum, or gold, because H⁺ concentration does not change which species is the stronger
oxidant. Denies that all acids behave alike — HCl and dilute H₂SO₄ are **non-oxidizing**, H⁺ their
only oxidant, while HNO₃ and hot concentrated H₂SO₄ bring an oxidizing **anion** and dissolve
metals with positive `E°_red`.

**Predicts.** Negative `E°_red` + any strong acid → `Mⁿ⁺` in solution + H₂ gas. Positive `E°_red` + HCl → **no
reaction**. Gas from a non-oxidizing acid is always H₂. Metals below hydrogen (Cu, Ag, Pt, Au)
survive in coins, plumbing, and jewelry — the same fact stated as metallurgy.

**Worked — full.** *Will zinc metal (`E°_red = −0.76 V`) evolve H₂ gas in 1 M HCl?*
1. Principle: hydrogen reduced, metal oxidized. Cathode `2H⁺/H₂` at 0.00 V; anode `Zn²⁺/Zn` at
   −0.76 V.
2. `E°_cell = E°_cathode − E°_anode = 0.00 − (−0.76)`.
3. `E°_cell = +0.76 V`. Positive → **yes**, H₂ evolves and the zinc dissolves.

**Faded — last step.** *Will copper metal (`E°_red = +0.34 V`) evolve H₂ gas in 1 M HCl?*
1. Principle: same setup. Cathode `2H⁺/H₂` at 0.00 V; anode `Cu²⁺/Cu` at +0.34 V.
2. `E°_cell = 0.00 − 0.34`.
3. `E°_cell = ______ V`, therefore ______.

**Faded — last two.** *Nickel has `E°_red = −0.25 V` and silver has `E°_red = +0.80 V`. Which evolves
H₂ in 1 M HCl, and what single feature of the numbers told you?*
1. Principle: compare each metal's `E°_red` against the 0.00 V hydrogen reference.
2. Nickel: ______ ; Silver: ______
3. The deciding feature: ______

**Check:** (2) `E°_cell = −0.34 V`, so **no** — copper does not react with HCl at any concentration. (3)
Nickel is negative → `+0.25 V` → **evolves H₂**; silver is positive → `−0.80 V` → **no reaction**.
Principle: the deciding feature is the **sign of the metal's own reduction potential**; you never
had to subtract, and on a timed section you should not.

---

**Discriminators**

- **Which half-cell is the cathode?** — which `E°_red` is more positive? That one is reduced. There
  is no second criterion.
- **Galvanic vs electrolytic** — is `E°_cell` positive? Positive: runs itself, anode negative.
  Negative: must be driven, anode positive. The anode is the oxidation site in both.
- **`E°` vs `ΔG`** — did the coefficients change? `E°` never scales with coefficients; `ΔG` always
  does, through `n`.
- **Will it react with HCl vs with HNO₃?** — is the acid's anion an oxidant? HCl offers only H⁺
  (0.00 V); HNO₃ offers nitrate (+0.96 V) and dissolves copper and silver too.
- **Spontaneous vs fast** — `E°_cell` reports direction only. A +2 V reaction with a high activation
  barrier can sit unchanged for years.

**Compression** — the axis is **the sign of `E°_cell`**; everything here restates it.

| `E°_cell` | `ΔG°` | `K` | Cell type | Anode terminal | Happens on its own? |
|---|---|---|---|---|---|
| **positive** | negative | > 1 | galvanic | negative | yes |
| zero | zero | = 1 | at equilibrium (dead battery) | — | no net change |
| **negative** | positive | < 1 | electrolytic | positive | only if driven |

---

## CLUSTER 5A — NUCLEAR DECAY
**FL1: Q42 · CC4E (4/6, 67%)**

**Shared scenario: one atom of uranium-238 in a granite countertop.** Over four and a half billion
years it steps down a chain of fourteen decays to lead-206, changing identity every time something
leaves the nucleus. Each concept tracks one step.

---

#### Conservation of A and Z
FL1: **Q42** · CC4E · broke: reasoning — didn't run the two-line balance

**Structure.** In `ᴬ_Z X` — `A` = nucleons, `Z` = protons and therefore element identity — **`A` and `Z` balance separately**: two subtractions and a look at the provided periodic table.

**Concrete.** `²³⁸₉₂U → ⁴₂He + ?`. Mass: `238 − 4 = 234`. Charge: `92 − 2 = 90`. Element 90 is thorium, so the
atom is now `²³⁴₉₀Th` and a helium nucleus is flying off at 5% of light speed. **Two atoms where
there was one** — how "which two atoms form" wants you to think.

**Claims.** Identity is set by `Z` and nothing else — you never need thorium's properties, only that it is
element 90. Denies that decay chains or daughter products must be memorized: the table is supplied
and the arithmetic is two subtractions. Denies that mass is conserved in the ordinary sense — `A`,
the nucleon count, is; **mass is not**, the missing mass leaving as binding energy, which is what
makes the decay energetic.

**Predicts.** Parent plus one product determines the other: subtract `A`, subtract `Z`, read the element. Parent
plus daughter determines the particle — `ΔA = 4, ΔZ = 2` is alpha; `ΔA = 0, ΔZ = +1` is beta-minus.
**The electron carries `A = 0, Z = −1`**, written `⁰₋₁e`, and that `−1` is what drives `Z` *up*.

**Worked — full.** *Uranium-238 undergoes alpha decay. What two atoms result?*
1. Principle: alpha emits `⁴₂He`. Skeleton: `²³⁸₉₂U → ⁴₂He + ᴬ_Z X`.
2. Balance mass number: `A = 238 − 4 = 234`.
3. Balance atomic number: `Z = 92 − 2 = 90`.
4. Element 90 is thorium. Products: **`⁴₂He` and `²³⁴₉₀Th`.**

**Faded — last step.** *Thorium-234 undergoes beta-minus decay. What atom results?*
1. Principle: beta-minus emits `⁰₋₁e`. Skeleton: `²³⁴₉₀Th → ⁰₋₁e + ᴬ_Z X`.
2. Balance: `A = 234 − 0 = 234`; `Z = 90 − (−1) = 91`.
3. Element 91 is ______, so the product is ______.

**Faded — last two.** *Radium-226 decays into two atoms, one of which is radon-222 (`²²²₈₆Rn`).
Identify the other product and name the decay mode.*
1. Principle: `A` and `Z` each balance; find the difference and read what particle fits.
2. `ΔA = ______`, `ΔZ = ______`
3. The other product is ______, so the mode is ______.

**Check:** (2) Element 91 is protactinium, so `²³⁴₉₁Pa`. The subtlety is subtracting a negative: beta-minus
*raises* `Z` because the emitted electron carries `−1` and a neutron converts to a proton. (3)
`ΔA = 226 − 222 = 4`, `ΔZ = 88 − 86 = 2`, so `⁴₂He` and **alpha decay**. Principle, and Q42's exact shape: the question
names one product and makes you generate the other from two subtractions.

---

#### The decay modes
FL1: **Q42** · CC4E · supports

**Structure.** Five processes, defined entirely by what they do to `A` and `Z`.

| Mode | Emitted | `ΔA` | `ΔZ` | Nucleus was | Penetration |
|---|---|---|---|---|---|
| **Alpha** | `⁴₂He` | **−4** | **−2** | too heavy (`Z > 83`) | stopped by paper |
| **Beta-minus** | `⁰₋₁e` + antineutrino | 0 | **+1** | neutron-rich | stopped by aluminum |
| **Beta-plus** | `⁰₊₁e` (positron) | 0 | **−1** | proton-rich | — |
| **Electron capture** | a neutrino only — nothing charged leaves; the daughter's characteristic X-ray follows | 0 | **−1** | proton-rich | — |
| **Gamma** | photon | **0** | **0** | in an excited state | needs lead |

**Concrete.** Carbon-14 has 8 neutrons and 6 protons, two more than stable carbon can carry. One converts:
`n → p + e⁻`. Seven protons now, so it is **nitrogen**, still mass 14, and an electron shoots out
fast. Nothing orbiting left — the electron was **manufactured inside the nucleus**, which is why
`A` holds and `Z` climbs.

**Claims.** Beta particles are created in the nucleus, not stripped from the electron cloud. Denies the common
model that beta decay ejects an orbital electron — then `Z` would be unchanged and the atom merely
an ion. **Gamma changes neither `A` nor `Z`**, so a gamma-only step makes no new element and can
never answer "which two atoms form." Denies that beta-plus and electron capture are distinguishable
by bookkeeping — both give `ΔA = 0, ΔZ = −1`.

**Predicts.** Too heavy → alpha. Too many neutrons → beta-minus. Too many protons → beta-plus or electron
capture. Excited but otherwise fine → gamma. **The nucleus always moves toward the stable
neutron-to-proton band**, so which side the parent sits on names the mode before you read any
choice.

---

#### Alpha decay
FL1: **Q42** · CC4E · supports

**Structure.** The nucleus ejects two protons and two neutrons bound as one particle, `⁴₂He`: `ΔA = −4, ΔZ = −2`, a new element two places down the table. The mode of nuclei that are simply **too heavy** — every nuclide past bismuth (`Z > 83`) is unstable, and alpha is how the heavy ones shed mass.

**Concrete.** The uranium-238 atom in the countertop, step one of fourteen: `²³⁸₉₂U → ²³⁴₉₀Th + ⁴₂He`. The helium nucleus leaves at about 5% of light speed; the thorium recoils the other way, slowly, because momentum balances and it is sixty times heavier. The alpha crosses a few centimeters of air and is stopped by the dead outer layer of your skin — or by a sheet of paper.

**Claims.** Asserts the emitted particle is a helium *nucleus* — no electrons — so the atom left behind carries two surplus electrons and the alpha steals two from whatever it hits. Denies that alpha is the "weak" radiation because it is easily stopped: it is the most ionizing per centimeter, dumping all its energy in a few cells, which is why the alpha that matters is the one emitted **inside** you (radon-222, a gas in this same chain, in a lung). Denies that alpha alone can carry a heavy nucleus to stability: removing two protons and two neutrons from a nucleus with `N/Z ≈ 1.6` leaves the daughter *more* neutron-rich (`146/92 → 144/90`), so a heavy chain must interleave alphas with beta-minus steps.

**Predicts.** `ΔA = 4` between parent and product → alpha, the only common mode that moves `A`. Parent heavier than bismuth with no other cue → alpha first. After an alpha, expect a beta-minus soon — the U-238 chain runs eight alphas and six beta-minuses to reach lead-206. Shielding stem: paper or skin.

---

#### Beta-minus decay
FL1: **Q42** · CC4E · supports

**Structure.** A neutron becomes a proton inside the nucleus, `n → p + e⁻ + ν̄`; the electron is **manufactured there and ejected**: `ΔA = 0, ΔZ = +1`, one element *up*. The mode of a nucleus with **too many neutrons** for its protons.

**Concrete.** Step two on the countertop: `²³⁴₉₀Th → ²³⁴₉₁Pa + ⁰₋₁e`. Thorium-234 has 144 neutrons to 90 protons — more neutron-heavy than the uranium that made it. One neutron converts; the electron leaves at a good fraction of light speed with a spread of energies, the antineutrino carrying the rest; a few millimeters of aluminum stops it. Same 234 nucleons. Protactinium.

**Claims.** Asserts the electron came from the nucleus, not from the electron cloud — which is why `Z` climbs and the mass number holds. Denies the model where beta decay ejects an orbital electron; that would leave `Z` unchanged and make an ion, not a new element. Denies that ejecting a negative particle lowers the nucleus's charge: the nucleus *gained* a positive unit, and the atom as a whole is briefly a positive ion until it picks up an electron from its surroundings.

**Predicts.** `ΔA = 0, ΔZ = +1` → beta-minus, and the balancing move is subtracting `−1`: `Z_daughter = Z_parent + 1`. Carbon-14 → nitrogen-14; every neutron-rich fission product; every "became the next element with the same mass number" stem. **Beta-minus vs beta-plus is one question: did `Z` go up or down?** Up is this one.

---

#### Beta-plus decay
FL1: **Q42** · CC4E · supports

**Structure.** A proton becomes a neutron, `p → n + e⁺ + ν`, and the **positron** — the electron's antiparticle, `⁰₊₁e` — is ejected: `ΔA = 0, ΔZ = −1`, one element *down*. The mode of a nucleus with **too many protons**, and only available when the parent atom outweighs the daughter atom by at least **1.022 MeV** — two electron masses — because the products carry two particles the parent did not have to pay for before: the positron, and the orbital electron the daughter no longer needs.

**Concrete.** The countertop has none of these; the hospital next door makes thousands a second. Fluorine-18 in a PET tracer: `¹⁸₉F → ¹⁸₈O + ⁰₊₁e`. The positron travels about a millimeter through tissue, meets an electron, and both vanish into **two 511 keV photons flying in exactly opposite directions**. The detector ring catches both and draws the line between them. Fluorine became oxygen; the picture is made of annihilations.

**Claims.** Asserts something leaves the nucleus and is detectable at a distance — the positron, then its two photons. Denies that beta-plus is beta-minus run backwards at the same price: beta-minus needs only a positive mass difference, beta-plus needs it to exceed two electron masses, so a proton-rich nucleus with a small mass surplus **cannot** do this and must capture instead. Denies that the 511 keV photons are gamma decay — they come from annihilation outside the nucleus, after the decay is over.

**Predicts.** `ΔZ = −1` with a positron named, or **two back-to-back 511 keV photons**, or a PET stem → beta-plus. The daughter sits one element to the left. **Beta-plus vs electron capture is one question: did anything leave the nucleus?** Here, yes — a positron.

---

#### Electron capture
FL1: **Q42** · CC4E · supports

**Structure.** The nucleus pulls in one of the atom's own **inner-shell electrons** and a proton becomes a neutron, `p + e⁻ → n + ν`: `ΔA = 0, ΔZ = −1`, the same bookkeeping as beta-plus. Nothing charged leaves the nucleus; the neutrino carries the energy away unseen, and the only signal is atomic — the hole left in the inner shell is filled from above, emitting the **daughter element's characteristic X-ray**.

**Concrete.** An iodine-125 seed implanted in a prostate: `¹²⁵₅₃I + ⁰₋₁e → ¹²⁵₅₂Te`. The nucleus swallows a K-shell electron and is tellurium. An outer electron drops into the empty shell and a tellurium X-ray leaves the atom — those low-energy photons are the radiation doing the treating. Iodine-125's mass surplus over tellurium-125 is 0.19 MeV, nowhere near the 1.022 MeV a positron costs, so this nucleus **can decay no other way**. Back on the countertop: potassium-40 in the feldspar does this one time in nine, becoming argon that stays trapped in the crystal — the clock used to date the rock.

**Claims.** Asserts a capture is possible whenever the parent atom outweighs the daughter atom at all, because nothing new is created — the electron was already there. Denies that beta-plus and electron capture are one process with one condition: capture is available wherever beta-plus is, and also across the whole window from 0 to 1.022 MeV where beta-plus is forbidden. Denies that the X-ray is a gamma: it comes from the electron shell, not the nucleus, and it is the *daughter's* X-ray, because by the time the shell refills the atom is already the new element.

**Predicts.** `ΔZ = −1` with **no emitted particle**, or "characteristic X-rays of the daughter," or a stem describing an orbital electron entering the nucleus → electron capture. A proton-rich nuclide with a small mass difference → capture only; with a large one → both are open and beta-plus usually dominates. **Beta-plus vs electron capture is one question: did anything leave the nucleus?** Here, no — an electron went *in*.

---

#### Gamma decay
FL1: **Q42** · CC4E · supports

**Structure.** An **excited nucleus** drops to a lower energy state and emits the difference as a photon: `ΔA = 0, ΔZ = 0`. No new element. Usually the second half of another decay — the daughter of an alpha or beta step is often left excited and sheds the surplus within picoseconds — or, in a **metastable** nuclide, a delayed step of its own.

**Concrete.** The bone-scan isotope from the half-life block: the "m" in technetium-99m means the nucleus is holding 140 keV it has not yet released. It releases it as one photon, which passes out of the patient and into the gamma camera. Technetium before, technetium after. On the countertop, the gamma a counter hears is the same thing one step behind a beta: bismuth-214 beta-decays to polonium-214, and the newborn polonium nucleus, arriving excited, drops to its ground state by emitting a 609 keV photon.

**Claims.** Asserts a gamma-only step changes energy and nothing else — not `A`, not `Z`, not the element. Denies that gamma can ever answer "which two atoms form": it forms none. Denies that gamma is a particle in the alpha/beta sense; it is light, uncharged, undeflected by a magnetic field, and stopped only by centimeters of lead or thick concrete because it ionizes sparsely along a long path. Denies that every photon from a decaying atom is a gamma — an X-ray comes from the electron shell, a gamma from the nucleus.

**Predicts.** "Element unchanged, energy released," an asterisk or "m" on the parent, or a shielding stem answered by lead → gamma. Given `ΔA = 0, ΔZ = 0` between parent and product, the product is the same nuclide and the mode is gamma. **Gamma vs everything else is one question: did the element change?** Only gamma leaves it alone.

---

#### Half-life
FL1: — · CC4E · supports

**Structure.** `N = N₀(½)^(t/t½)`, so after `n` half-lives the fraction remaining is `1/2ⁿ` — first-order, independent of starting amount, temperature, pressure, and chemical form.

**Concrete.** A patient gets 80 mg of technetium-99m for a bone scan, half-life 6 hours. Six hours later, 40 mg;
twelve, 20; eighteen, 10; twenty-four, **5 mg** — one-sixteenth, because 24 hours is four
half-lives. Tc-99m is the workhorse isotope: long enough to image, short enough that the patient is clean by
morning.

**Claims.** The useful move is **counting half-lives, not exponentiating**: `t/t½` gives `n`, the answer is
`N₀/2ⁿ`. Denies that a decaying sample reaches zero. Denies that decay *rate* is constant — the
*fraction* per unit time is, so absolute rate falls as the sample shrinks. Denies that anything
done to a sample changes its half-life: heating, dissolving, ionizing do nothing, because chemistry
lives outside the nucleus.

**Evidence.** On a **semi-log plot** (log of remaining quantity vs. linear time) first-order decay is
a **straight line** — AAMC's diagnostic, slope proportional to `−1/t½`. A straight line on *linear*
axes would mean constant absolute rate, which decay is not.

**Predicts.** Count `n = t/t½` and halve `n` times. Given initial and final amounts, count the halvings and divide
elapsed time by that count. Recognize instantly: 1/2, 1/4, 1/8, 1/16, 1/32 → 1, 2, 3, 4, 5
half-lives.

**Worked — full.** *A patient receives 80 mg of an isotope with a 6-hour half-life. How much remains
after 24 hours?*
1. Principle: count half-lives. `n = t/t½ = 24/6 = 4`.
2. Principle: each half-life halves the amount, `N = N₀/2ⁿ`.
3. `N = 80/2⁴ = 80/16`.
4. `N = 5 mg`.

**Faded — last step.** *Iodine-131 has a half-life of 8 days; a 12 mg dose is given. How much remains
after 32 days?*
1. Principle: `n = 32/8 = 4` half-lives.
2. `N = 12/2⁴ = 12/16`.
3. `N = ______ mg`

**Faded — last two.** *A sample falls from 64 g to 4 g in 30 minutes. Find the half-life.*
1. Principle: run it backwards — count the halvings first, then divide the elapsed time.
2. Number of half-lives: ______
3. `t½ = ______`

**Check:** (2) `N = 0.75 mg`. (3) `64 → 32 → 16 → 8 → 4` is **4 halvings** (`64/4 = 16 = 2⁴`), so
`t½ = 30/4 = 7.5 minutes`. Principle: the ratio of amounts gives `n` directly, and on this exam
that ratio is always a clean power of two.

---

**Discriminators**

- **Alpha vs beta** — did the mass number change? Alpha is the only common mode that moves `A`.
- **Beta-minus vs beta-plus** — did `Z` go up or down? Up: a neutron became a proton. Down: a proton
  became a neutron.
- **Beta-plus vs electron capture** — *did anything leave the nucleus?* Positron out (then two back-to-back 511 keV photons) → beta-plus. Inner-shell electron *in*, nothing charged out, only the daughter's X-ray → capture. Same `A`, same `ΔZ = −1`; and a mass surplus under 1.022 MeV can only capture.
- **Gamma vs everything else** — did the element change? Gamma is the only mode producing no new
  element, so it can never answer "which two atoms form."
- **Nuclear vs chemical** — does the element's identity change? Only nuclear processes change `Z`,
  and no temperature, catalyst, or bond alters a half-life.

**Compression** — the axis is **what the emission does to `Z`** (and, secondarily, `A`).

| Mode | `Z` | `A` | Element changes? |
|---|---|---|---|
| Alpha | **−2** | −4 | yes, down two |
| Beta-plus / electron capture | **−1** | 0 | yes, down one |
| Gamma | **0** | 0 | **no** |
| Beta-minus | **+1** | 0 | yes, up one |

---

## CLUSTER 5B — ELECTRONIC STRUCTURE
**FL1: — · CC4E**

**Shared scenario: a pinch of table salt thrown into the candle flame from Cluster 1.** The flame
turns brilliant yellow. Sodium's outer electron absorbs heat, jumps to a higher orbital, falls back,
and emits a photon at exactly 589 nm — the yellow of a streetlight. Each concept is one part of why
that color and no other came out.

---

#### Electron configuration and the filling rules
FL1: — · CC4E · supports

**Structure.** Three rules in order — **Aufbau** (fill lowest first: `1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s`), **Pauli** (two per orbital, opposite spins; no two electrons share all four quantum numbers), **Hund** (one electron in each equal-energy orbital, spins parallel, before pairing) — capacities `s` = 2, `p` = 6, `d` = 10, `f` = 14.

**Concrete.** Iron, `Z = 26`: `1s²2s²2p⁶3s²3p⁶4s²3d⁶`. Five `3d` orbitals, six electrons, so Hund fills all five
singly and the sixth pairs: **four unpaired**, which is why an iron filing jumps to a magnet.
Oxidize to `Fe³⁺` and the **`4s` pair leaves first**, then one `3d`, giving `[Ar]3d⁵` — five
electrons in five orbitals, all unpaired.

**Claims.** `4s` fills **before** `3d` but empties **before** it too — once `3d` is occupied it drops below
`4s`, so `4s` is last in and first out. Denies the reflex of removing `d` electrons first from
transition metal ions, which changes the unpaired count and therefore the magnetic answer. Denies
that Aufbau order is a law: **chromium is `[Ar]4s¹3d⁵` and copper is `[Ar]4s¹3d¹⁰`**, a half-filled
or filled `d` shell beating the `s` pairing.

**Predicts.** Any unpaired electron → **paramagnetic**; all paired → **diamagnetic**, weakly repelled. Quantum
numbers: `n` = shell, `l` = 0…(n−1) naming s/p/d/f, `m_l` = −`l`…+`l` (`p` has 3 orbitals, `d` has
5), `m_s` = ±½. Across a period **effective nuclear charge rises**: radius shrinks, ionization
energy and electronegativity climb; down a group all three reverse. Cations are smaller than the
parent atom, anions larger.

**Worked — full.** *Give the configuration of Fe³⁺ and state whether it is paramagnetic.*
1. Principle: build neutral iron first, `Z = 26`: `1s²2s²2p⁶3s²3p⁶4s²3d⁶`, or `[Ar]4s²3d⁶`.
2. Principle: transition metals lose `4s` before `3d`. Remove both `4s` → `[Ar]3d⁶`.
3. That is two of three; remove one more, from `3d` → `[Ar]3d⁵`.
4. Principle: Hund. Five electrons in five `d` orbitals → all unpaired → **paramagnetic**.

**Faded — last step.** *Give the configuration of Zn²⁺ (`Z = 30`) and state its magnetism.*
1. Principle: neutral zinc is `[Ar]4s²3d¹⁰`.
2. Principle: remove the `4s` electrons first → `[Ar]3d¹⁰`.
3. Unpaired electrons: ______, so Zn²⁺ is ______.

**Faded — last two.** *How many unpaired electrons does neutral nitrogen (`Z = 7`) have, and is it
paramagnetic?*
1. Principle: write the configuration by Aufbau, then apply Hund to the outermost subshell.
2. Configuration: ______
3. Unpaired: ______ ; magnetism: ______

**Check:** (2) `3d¹⁰` is full, so **zero** unpaired and Zn²⁺ is **diamagnetic** — why zinc compounds are
colorless and iron compounds are not. (3) `1s²2s²2p³`; three `2p` electrons in three orbitals
singly, parallel spins, so **three unpaired**, **paramagnetic**. Principle: Hund's rule, not Pauli,
decides the unpaired count.

---

#### Photons, line spectra, and the photoelectric effect
FL1: — · CC4E · supports

**Structure.** `E = hf = hc/λ` with `h = 6.63 × 10⁻³⁴ J·s`; electron energies are **quantized**, so a photon is absorbed or emitted only when its energy matches a gap exactly. Photoelectric effect: `KE_max = hf − W`, `W` the work function.

**Concrete.** Sodium in the flame emits at 589 nm and nowhere else: through a prism, one bright yellow line on a
black field, not a rainbow, because its outer electron has one gap to fall across. Send the light
through cold sodium vapor and you get the mirror image — a full spectrum with a black gap at
589 nm.

**Claims.** Discrete lines are direct evidence of quantized levels: a continuous orbit model predicts a
continuous spectrum, and the line spectrum falsifies it. The photoelectric effect shows light
delivering energy in **individual packets** — below the threshold frequency **no electrons are
ejected at any intensity**, and above it more intensity gives more **electrons** while more
frequency gives more **kinetic energy**. Denies the wave prediction that a dim blue lamp eventually
accumulates enough to eject one; it never does, and a bright red one never does either.

**Predicts.** Shorter `λ` → higher `f` → higher `E`; an absorbed photon must match `ΔE` exactly. For hydrogen
`E_n = −13.6/n² eV`, so gaps shrink and emission lines crowd as `n` grows. Plot `KE_max` against
`f`: a straight line of slope `h`, x-intercept `W/h`; changing the metal shifts the intercept, never
the slope. AAMC supplies `hc ≈ 1240 eV·nm`, so a 620 nm photon carries 2 eV.

---

**Discriminators**

- **Aufbau order vs ionization order** — building the atom or taking it apart? `4s` fills before
  `3d`; `4s` empties before `3d`. Both are true.
- **Pauli vs Hund** — Pauli sets the *capacity* (2 per orbital), Hund the *arrangement* (spread
  before pairing). Only Hund decides how many are unpaired.
- **Paramagnetic vs diamagnetic** — is any electron unpaired? One is enough for paramagnetic.
- **Emission vs absorption spectrum** — bright lines on dark, or dark lines on bright? Same
  wavelengths either way; the atom emits exactly what it absorbs.
- **Intensity vs frequency in the photoelectric effect** — brighter light gives *more* electrons;
  bluer light gives *faster* ones. Neither substitutes for the other.
- **Nuclear energy scale vs electronic** — MeV or eV? Nuclear decay releases millions of
  electron-volts and changes the element; electronic transitions release a few and change the color.

**Compression** — the axis is **the energy of the state the electron occupies**, quantized.

| Concept | What quantization forces |
|---|---|
| Aufbau | electrons fill the **lowest available** energies first |
| Pauli | each energy state holds **at most two** electrons |
| Hund | equal-energy states fill **singly first**, maximizing unpaired spins |
| Paramagnetism | unpaired spins survive ⇒ the atom responds to a magnetic field |
| Line spectra | only **exact gaps** can be absorbed or emitted ⇒ lines, not a continuum |
| Photoelectric effect | one photon, one electron ⇒ a **threshold frequency**, not a threshold brightness |

---

## THE 60-SECOND TRIGGER TABLE

C/P Skill 2 fell from 77% to 43% across the section. The failure is not knowing which equation
applies — it is **finding it fast enough**. Read column-left, answer the question, take the
equation. Drill until the lookup is automatic; that is the schema the ladders are building.

| The stem says… | Ask | Take |
|---|---|---|
| speed of light in a material | one medium or two? | `n = c/v` |
| a light ray crosses a boundary | which `n` is bigger? | `n₁ sin θ₁ = n₂ sin θ₂` |
| light trapped, fiber, no light escapes | is `n₁ > n₂`? | `sin θ_c = n₂/n₁` |
| image, lens, mirror, focal length | is the object inside or outside `f`? | `1/o + 1/i = 1/f` |
| ratio of heights, how big, upright or inverted | do I have `i` and `o`? | `m = h_i/h_o = −i/o` |
| how fast is the fluid moving | did **total** area go up or down? | `A·v = Q` |
| pressure drop along a vessel, resistance | is radius changing? | `ΔP = QR`, `R ∝ 1/r⁴` |
| narrowing raises speed, what about pressure | ideal fluid? | `P + ½ρv² + ρgh = const` |
| depth, column, standing vs lying down | is anything flowing? | `P = ρgh` |
| systolic, diastolic, mean, pulse | level or span? | `P_pulse = P_s − P_d`; `P_mean = P_d + P_pulse/3` |
| work done by the heart, energy to pump | volume or rate? | `W = PΔV` (J) or `Power = PQ` (W) |
| current through an element | series or parallel? | `V = IR` after reducing `R_eq` |
| which bulb is brighter | shared current or shared voltage? | `P = I²R` (series) or `V²/R` (parallel) |
| will this reaction occur / is it spontaneous | which `E°_red` is more positive? | `E°_cell = E°_cat − E°_an > 0` |
| does H₂ gas evolve in acid | is the metal's `E°_red` negative? | sign check against 0.00 V |
| how much metal is plated | how many electrons per ion? | `mol e⁻ = It/F` |
| which atoms form, what particle was emitted | what are `ΔA` and `ΔZ`? | balance `A` and `Z` separately |
| how much is left after time `t` | how many halvings? | `N = N₀/2ⁿ`, `n = t/t½` |
| unpaired electrons, paramagnetic | did I remove `4s` before `3d`? | Aufbau, then Hund |
| photon energy, wavelength, threshold | energy per photon or number of photons? | `E = hc/λ`; `KE_max = hf − W` |

---

# GENERAL & ORGANIC CHEMISTRY

## CONCEPTS — Chem/Phys · CHEMISTRY

Chemistry on FL1 was 28/36 (78%), the strong half of the section. Organic was 9/12 cold. Eight
misses and the concepts under them.

| FL1 | Category | Skill | What broke |
|---|---|---|---|
| Q4 | CC5C | S4 | negative stem — picked a true statement on a NOT question |
| Q7 | CC5D | S2 | biologically relevant molecules |
| Q9 | CC5B | S2 | carbocation / Markovnikov |
| Q32 | CC5E | S1 | opsin absorption maxima |
| Q35 | CC5D | S2 | amino acid side-chain pKa, net charge |
| Q39 | CC5D | S1 | **left blank** — ran out of time |
| Q41 | CC5E | S3 | effect of adding an enzyme to a mixture |
| Q58 | CC5A | S2 | solution calculation, 0.078 mol |

C/P Skill 2 ran 77% in the first half of the section, 43% in the second: content present, killed by
time pressure. Every quantitative concept below is a worked example plus a faded one. Do the blank.

---

### Negative-stem procedure
FL1: Q4 · NOT/LEAST/EXCEPT accuracy 56% vs 71% overall · broke: trap

1. **Rewrite the stem positive in the margin.** "Which does NOT correctly describe X" becomes
   "three of these are TRUE; find the false one." Three words, written down, not thought.
2. **Verdict each option T or F.** Four independent judgments. Do not hunt for "the answer."
3. **The key is the minority verdict.** On a NOT stem, the single F.
4. **Two F's or zero F's means you misread the stem, not the options.** Re-read the stem, never
   the options — that is where the time goes.

Under pressure the negation drops out of working memory and the default policy — pick the true
statement — reasserts itself. That is Q4. Writing it out externalizes the negation.

---

## Cluster 1 — Carbocation chemistry
FL1: Q4, Q9

**The shared flask.** Three vessels of the same C5 skeleton: 2-methyl-2-butene,
2-methyl-2-butanol, 3-methyl-2-butanol. Plus the exam's own flask — malic acid
(HOOC–CHOH–CH2–COOH) in hot dilute sulfuric acid.

#### Where carbocations come from — three gates
FL1: Q9 · CC5B · broke: reasoning

**Structure.** (a) π bond attacks an electrophile, + on the other alkene carbon; (b) leaving group
ionizes off a 2° or 3° carbon; (c) alcohol protonated, water leaves.
**Concrete.** HBr into the 2-methyl-2-butene vessel. The π electrons grab H+; the carbon that
missed it is electron-deficient, sp2, flat.
**Claims.** Asserts a discrete cation step *before* the nucleophile arrives. Denies H and Br
arrive together. Denies cations form on primary or methyl carbons in solution — those go SN2, or
never go.
**Predicts.** Name the gate → planar center, racemization, rearrangement, Markovnikov
regiochemistry, Zaitsev mixture.

#### Stability order
FL1: Q9 · CC5B · broke: reasoning

**Structure.** Resonance-stabilized (allylic, benzylic, adjacent to O or N lone pair) > 3° > 2° > 1° > methyl,
by hyperconjugation from adjacent C–H sigma bonds into the empty p plus alkyl induction. Adjacent
electron-withdrawing groups (C=O, COOH, NO2, CF3, halogen) destabilize.
**Concrete.** In the malic acid flask the cation lands on C2, flanked by a COOH — a 2° cation
beside an electron-withdrawing carboxyl. A bad cation; hence the heat and concentrated acid.
**Claims.** Asserts stability is whatever donates density into the empty p. Denies "more
substituted" is the rule: an adjacent oxygen lone pair beats a 3° alkyl cation — full resonance, not
partial donation.
**Predicts.** Of two possible cations the reaction takes the more stable; that choice fixes the
product.

#### Planarity, and what it destroys
FL1: Q4 · CC5C · broke: trap

**Structure.** sp2, trigonal planar, empty p perpendicular to the plane. (1) Nucleophile attacks
either face equally → racemic. (2) Adjacent C–C rotates freely → alkene geometry set by whichever
rotamer eliminates → both geometries form.
**Concrete.** (S)-malic acid, one enantiomer, into the flask. Water leaves; the C2 cation is flat
and C2–C3 spins. A base pulls an H off C3 — the carboxyls end up same-side or opposite, depending
where the spin stopped. Out come both maleic acid (cis) and fumaric acid (trans), from one pure
enantiomer.
**Claims.** Asserts a planar intermediate erases the starting material's stereochemical information.
Denies one stereoisomer in guarantees one stereoisomer out. **This is the Q4 key.** The stem's true
statements described the reaction correctly; the false one claimed stereospecificity.
**Predicts.** No mechanism through a free carbocation is stereospecific. Single-enantiomer substrate
→ mixture means a carbocation was involved.

#### Stereospecific vs stereoselective
FL1: Q4 · CC5C · broke: trap

**Structure.** Stereospecific: the *starting material's* stereochemistry sets the product's — swap
the reactant stereoisomer, get a different product stereoisomer. Stereoselective: one product
stereoisomer predominates whatever went in.
**Concrete.** Same flask, two routes. Acid dehydration of malic acid gives mostly fumaric acid,
trans being less strained — stereoselective. Fumarase runs an anti elimination on (S)-malate and
gives fumarate only, never maleate — stereospecific: it holds the substrate in one conformation
and never lets it rotate.
**Claims.** Asserts two independent properties. Denies "mostly one product" means "stereospecific."
Every stereospecific reaction is stereoselective; the converse is false, and the converse is the
trap.
**Predicts.** Stereospecific → concerted, no free intermediate. Stereoselective only → planar
intermediate, mixture with a thermodynamic bias.

#### Markovnikov addition
FL1: Q9 · CC5B · broke: reasoning

**Structure.** H+ adds to the alkene carbon with more hydrogens → + lands where best stabilized →
nucleophile bonds that more substituted carbon. Regiochemistry follows from cation stability, not a
rule of its own.
**Concrete.** HBr into 2-methyl-2-butene. H goes to C3 (one H and a methyl), not C2 (two methyls),
landing where it makes the 3° cation at C2. Br finds C2. Product: 2-bromo-2-methylbutane.
**Claims.** Asserts one mechanistic cause for regiochemistry. Denies sterics or "which carbon is
bigger."
**Predicts.** Two anti-Markovnikov routes in AAMC scope. HBr **with peroxides** → radical, Br·
adding first to the less substituted carbon; HBr only, not HCl or HI. Hydroboration–oxidation (BH3,
then H2O2/NaOH) → OH on the less substituted carbon, H and OH syn, **no cation, therefore no
rearrangement**.

#### Rearrangement — 1,2-hydride and methyl shifts
FL1: Q9 · CC5B · broke: reasoning

**Structure.** If an H or methyl adjacent to the cation can shift over and give a more stable
cation, it shifts — faster than the nucleophile arrives. The product comes from the rearranged
cation.
**Concrete.** 3-methyl-2-butanol in acid. Water leaves C2 → 2° cation; the H on C3 slides over and
the + now sits on C3, which is 3°. Whatever adds, adds *there* — the product skeleton is not the
one you drew first.
**Claims.** Asserts the product reports the *most stable accessible* cation, not the one first
formed. Denies the leaving group's position fixes the product's position.
**Predicts.** Markovnikov product absent from the choices → the key is a rearranged skeleton. Look
for a 2° cation with a 3° carbon next door.

#### The unimolecular/bimolecular fork
FL1: Q4, Q9 · CC5B · broke: reasoning

**Structure.** Does the leaving group depart in its own step? Yes → SN1/E1: free cation,
racemization, rearrangement, Zaitsev mixture, rate on substrate only. No → SN2/E2: nucleophile or
base acts as C–LG breaks — backside inversion (SN2) or anti-periplanar geometry (E2), never
rearrangement, rate on both partners.
**Concrete.** 2-methyl-2-butanol + HBr, no base, protic solvent: C–OH ionizes, cation forms, Br
arrives late. Now a tosylated 1° alcohol with sodium ethoxide: ethoxide hits the back of the
carbon while tosylate is still leaving. Same flask, different fork, different stereochemistry.
**Claims.** Asserts stereochemical outcome is a *readout of mechanism*. Denies substrate structure
alone decides — solvent and the strength of the incoming species decide with it.
**Predicts.** Strong base or nucleophile + 1°/2° → bimolecular. Weak nucleophile or
solvent-as-nucleophile + 2°/3° + polar protic → unimolecular. Heat pushes toward elimination in both
branches.

**Discriminators**
- Stereospecific vs stereoselective — *does swapping the starting stereoisomer change which product stereoisomer forms?* Yes = specific.
- SN1 vs SN2 — *does the leaving group leave in its own step?*
- E1 vs E2 — *is a strong base present?* Strong base → E2, one concerted step, and it additionally requires the H and the leaving group anti-periplanar. Weak base or heat alone → E1 through a carbocation.
- Markovnikov vs anti-Markovnikov — *which carbon gets the H?* More-H carbon = Markovnikov.
- Hydroboration vs acid-catalyzed hydration — *is there a cation?* No cation = no rearrangement, and OH ends up on the other carbon.

**Compression** — the whole cluster on one axis.

| | Free carbocation? |
|---|---|
| SN1, E1, acid-catalyzed dehydration | **yes** |
| HX addition to an alkene (Markovnikov) | **yes** |
| Rearrangement occurs | only if yes |
| Racemization at the reacting center | only if yes |
| Loss of stereospecificity | only if yes |
| SN2, E2 | no |
| Hydroboration–oxidation | no |
| HBr + peroxides | no — radical, not cation |
| Enzymatic elimination (fumarase) | no — held rigid |

The left column is downstream of the right. Answer the right column first.

---

## Cluster 2 — Amino acid charge
FL1: Q35, Q7

**The shared peptide.** One hexapeptide on one titration bench, for every concept here:

**Asp–Gly–His–Lys–Ser–Glu** (D-G-H-K-S-E)

Free α-amino on the Asp end, free α-carboxyl on the Glu end. Three acidic groups, two basic, one
titrating right at physiological pH.

#### The pH-vs-pKa rule
FL1: Q35 · CC5D · broke: reasoning

**Structure.** pH below pKa → the group keeps its proton; above → it has lost it. Charge follows
from the *protonated* form: protonated N +1, deprotonated N 0; protonated O-acid 0, deprotonated −1.
**Concrete.** Hexapeptide in a beaker at pH 1; walk the pH up with NaOH. Each group flips exactly
once, in pKa order, lowest first: α-COOH 2.2, Asp 3.9, Glu 4.3, His 6.0, α-NH3+ 9.5, Lys 10.5. Six
flips, six equivalence points, one staircase.
**Claims.** Asserts protonation state is set by the *comparison* of pH to pKa, not by whether the
group is "an acid" or "a base." Denies acidic side chains are always negative — Asp at pH 2 is
neutral.
**Predicts.** pH = pKa → 50/50. One unit below → ~91% protonated; one above → ~91% deprotonated. Two
units either way → >99%, so treat anything two units off as fully one form.

#### The nine pKa values, and the pH-7 line that sorts them
FL1: Q35 · CC5D · broke: knowledge

**Structure.** Backbone: α-COOH ≈ 2, α-NH3+ ≈ 9.5. Side chains, low to high:
Asp 3.9 · Glu 4.3 · **His 6.0** · Cys 8.3 · Tyr 10.1 · Lys 10.5 · Arg 12.5.
**Concrete.** Draw the pH-7 line through that list. Above it, the oxygen acids (Asp, Glu): proton
gone, **−1**. Below it, the nitrogen bases (Lys, Arg): proton held, **+1**. Cys and Tyr are acids
with high pKa — still protonated, **0**. His at 6.0 sits just past the line, ~90% deprotonated:
**treat it as 0**, but it is the only side chain buffering at physiological pH.
**Claims.** Asserts only Asp, Glu, Lys, Arg carry charge at pH 7, plus His partially. Denies Cys and
Tyr are "acidic and therefore negative" — their pKa values sit on the protonated side of pH 7.
**Predicts.** Buffering, general acid-base catalysis, or a pH-sensitive conformational switch near
physiological pH → **histidine**; nothing else titrates there. Hemoglobin's Bohr effect, the
catalytic triad, and metal coordination all run through His.

#### Computing net charge — worked
FL1: Q35 · CC5D · broke: reasoning

**Worked example.** Net charge of Asp–Gly–His–Lys–Ser–Glu at pH 7.

| Group | pKa | pH vs pKa | State | Charge |
|---|---|---|---|---|
| α-NH3+ (N-terminus) | 9.5 | 7 < 9.5 | protonated | **+1** |
| Asp side chain | 3.9 | 7 > 3.9 | deprotonated | **−1** |
| Gly side chain | — | — | none | 0 |
| His side chain | 6.0 | 7 > 6.0 | deprotonated | **0** |
| Lys side chain | 10.5 | 7 < 10.5 | protonated | **+1** |
| Ser side chain | — | — | none | 0 |
| Glu side chain | 4.3 | 7 > 4.3 | deprotonated | **−1** |
| α-COO− (C-terminus) | 2.2 | 7 > 2.2 | deprotonated | **−1** |

Sum: (+1) + (−1) + 0 + (+1) + (−1) + (−1) = **−1**.

The two termini cancel at any pH between about 4 and 8, as they always do in a linear peptide. At
pH 7, skip both and count side chains: −1, 0, +1, −1 = **−1**. Four fewer lines.

**Faded example — Q35's exact shape.** Variant XI replaces His3 with Arg.
Arg side chain pKa = 12.5. pH 7 < 12.5, so Arg is protonated: **+1**.
Wild-type His3 contributed **0**.
Change in net charge = (+1) − (0) = ______
New net charge = (−1) + (that) = ______

**Faded again.** A second variant replaces Lys4 with Glu.
Lys contributed ____ . Glu contributes ____ . Change = ______ .

**Structure.** Substitution question → never recompute the whole molecule: charge of the residue
that left, charge of the one that arrived, subtract.
**Claims.** Asserts "how does the net charge change" is a two-term subtraction. Denies you need the
wild-type net charge at all — the question asks a difference, and every unchanged residue cancels.
**Predicts.** Delta method ≈ eight seconds; full recount ≈ ninety. Q35 was a Skill 2 miss in the
second half of the section — this is the version that survives.

#### Isoelectric point
FL1: Q35 · CC5D · broke: knowledge

**Structure.** pI = the pH at which net charge is zero. Start at pH 0, everything protonatable
protonated, count the charge, subtract 1 at each pKa passed. pI = the average of the two pKa values
bracketing the zero-charge species.
**Worked example.** The hexapeptide. At pH 0: α-NH3+ (+1), His (+1), Lys (+1), all acids neutral.
Charge = **+3**.
- past 2.2 (α-COOH): +2
- past 3.9 (Asp): +1
- past 4.3 (Glu): **0** ← zero-charge species lives here
- past 6.0 (His): −1

Zero sits between pKa 4.3 and pKa 6.0. pI = (4.3 + 6.0)/2 = **5.15**.

**Faded example.** Free lysine. pKa's: α-COOH 2.2, α-NH3+ 9.0, side chain 10.5.
At pH 0 the charge is +2. Past 2.2 → +1. Past 9.0 → 0. Past 10.5 → −1.
The zero species is bracketed by ______ and ______ . pI = ______

**Claims.** Asserts pI is a property of the *molecule*, from the two pKa values flanking neutrality
— not the average of all of them, not of the side chains. Denies pI alone gives charge at pH 7;
compare pI to the pH.
**Predicts.** **pH > pI → negative → anode (+ electrode).** pH < pI → positive → cathode. At pH = pI
it does not move and solubility is minimal, no charge repulsion holding molecules apart — why
proteins precipitate at their pI, and the basis of isoelectric focusing.

**Discriminators**
- Acidic side chain vs basic side chain — *is the ionizable atom oxygen or nitrogen?* Oxygen goes 0 → −1. Nitrogen goes +1 → 0.
- Cys/Tyr vs Asp/Glu — *is the pKa above or below 7?* Both groups are acids; only pKa placement decides the charge at pH 7.
- His vs everything — *does it titrate near pH 7?* Only His.
- pI vs pH — *which is larger?* pH larger → net negative.

**Compression** — the whole cluster on one axis: **side-chain pKa, with the pH-7 line drawn in.**

| Side chain | pKa | Charge at pH 7 |
|---|---|---|
| Asp | 3.9 | −1 |
| Glu | 4.3 | −1 |
| — α-COOH (2.2) — | | −1 |
| His | 6.0 | ~0 (only one that titrates here) |
| **— pH 7 line —** | | |
| Cys | 8.3 | 0 |
| — α-NH3+ (9.5) — | | +1 |
| Tyr | 10.1 | 0 |
| Lys | 10.5 | +1 |
| Arg | 12.5 | +1 |

Above the line and oxygen-based → −1. Below and nitrogen-based → +1. Below and oxygen-based → 0.

---

## Cluster 3 — Carbohydrate linkages
FL1: Q39 (**the only blank on the exam**), Q7

**The shared granule.** One glycogen particle in one hepatocyte, a branched tree of glucose. Every
enzyme below acts on this same object; they differ only in **which carbon of glucose they touch**.

**Q39 was not a knowledge failure — it was never attempted.** The stem gave the enzyme (glycogen
synthase), the substrate (UDP-glucose), and the leaving group (UDP), and asked the bond type: a
ten-second retrieval, the cheapest question in the section, scored zero. Fix: the object below, plus
the rule that any question naming an enzyme and asking "what bond" gets answered or guessed before
you move — never left blank.

#### The glycosidic bond is an acetal
FL1: Q39 · CC5D · broke: not attempted

**Structure.** Glucose closes into a ring: the C5 hydroxyl attacks the C1 aldehyde →
**hemiacetal**, one OR and one OH on the same
carbon. That C1–OH plus a second alcohol → **acetal**, two OR groups on C1, water expelled. The
second OR is another sugar; that C–O–C is the glycosidic bond.
**Concrete.** The outermost glucose on a branch of the granule: C1 bonded to two oxygens — the
ring oxygen and one leading to the C4 of the residue beneath. Two oxygens on one carbon, no OH:
acetal, locked.
**Claims.** Asserts a glycosidic bond is ordinary carbonyl chemistry — nucleophilic addition to a
carbonyl, twice. Denies a new bond type to memorize separately.
**Predicts.** Acetals are stable to base, hydrolyzed by aqueous acid → polysaccharides survive the
small intestine's pH but are cleaved in the stomach and by any glycosidase. A hemiacetal
equilibrates with the open-chain aldehyde and therefore **reduces** Tollens' or Benedict's reagent;
an acetal cannot open and does not.

#### Anomeric carbon, α vs β
FL1: Q39, Q7 · CC5D · broke: knowledge

**Structure.** **Anomeric carbon** = the former carbonyl carbon, C1 in an aldose, C2 in a ketose,
the only ring carbon with two oxygens. Ring closure makes a new stereocenter → two anomers. Haworth,
D-glucose: **α** = anomeric OH *down*, opposite C6; **β** = *up*, same side as C6.
**Concrete.** Dissolve pure α-D-glucopyranose in water and watch the optical rotation drift and
settle — mutarotation. The ring opens to the aldehyde, spins, recloses either way, settling at
~36% α / 64% β. β wins because in the chair its OH is equatorial.
**Claims.** Asserts α/β is a stereochemical descriptor of one carbon, fixed when the acetal forms
and unchangeable after. Denies anomers are epimers in general — anomers are epimers *at the anomeric
carbon specifically*.
**Predicts.** Once glycosidic, the configuration is locked and enzymes are absolutely specific to
it. Humans hydrolyze α-1,4 (starch, glycogen), cannot touch β-1,4 (cellulose). Same monomer, same
linkage position, opposite anomer — one food, one fiber.

#### UDP-glucose — the activated donor
FL1: Q39 · CC5D · broke: not attempted

**Structure.** Glucose-1-phosphate + UTP → UDP-glucose + PPi; inorganic pyrophosphatase hydrolyzes
PPi to 2 Pi, and that hydrolysis makes activation irreversible.
**Concrete.** The incoming glucose reaches the granule already carrying UDP on its C1; the
C1–O–UDP bond is a high-energy phosphoester. The C4 hydroxyl of the terminal residue attacks C1 and UDP leaves as a
stable, delocalized anion.
**Claims.** Asserts biological glycosyl transfer needs a good leaving group on the anomeric carbon,
a bare OH being terrible. Denies the sugar polymerizes by simple condensation in a cell — the
free-energy cost is paid up front by UTP, not at the bond-forming step.
**Predicts.** Every nucleotide sugar follows this: UDP-glucose for glycogen, UDP-glucuronate for
phase II conjugation in the liver, UDP-galactose for lactose, GDP-mannose and CDP-choline elsewhere.
"NDP-sugar" = an activated glycosyl donor.

#### Glycogen synthase makes α-1,4 · branching enzyme makes α-1,6
FL1: Q39 · CC5D · broke: not attempted — **this is the answer that was left blank**

**Structure.**
- **Glycogen synthase**: UDP-glucose + glycogen(n) → glycogen(n+1) + UDP. Bond formed:
  **α-1,4-glycosidic** — C1 of the new glucose to the C4-OH of the non-reducing end.
- **Branching enzyme** (amylo-4,6-transglycosylase): lifts a block of ~7 residues off a chain at
  least 11 long and reattaches it to a C6-OH further in. Bond formed: **α-1,6-glycosidic**.
- **Glycogenin** primes it, attaching the first glucose to one of its own tyrosine hydroxyls and
  extending to ~8 residues before synthase takes over.
**Concrete.** At the granule's outer edge, synthase walks outward along a linear chain, adding one
glucose at a time to the C4 end. Branching enzyme cuts a length off, swings it sideways, staples
it to a C6 — a new free end. Every branch doubles the places synthase and phosphorylase can act;
glycogen mobilizes fast.
**Claims.** Asserts linear extension and branching are two enzymes, two chemically different bonds,
two different carbons. Denies synthase makes branches.
**Predicts.** UDP released → **α-1,4 bond formed**. Free glucose released and no UDP → debranching
enzyme's α-1,6 glucosidase activity. Glucose-1-phosphate released → glycogen phosphorylase,
cleaving α-1,4 phosphorolytically.

#### Degradation runs the same map backward
FL1: Q39, Q7 · CC5D · broke: knowledge

**Structure.** **Glycogen phosphorylase** cleaves α-1,4 bonds with inorganic phosphate, not water,
releasing **glucose-1-phosphate**, and stalls four residues from a branch point. **Debranching
enzyme** is bifunctional: a transferase moves three of those four to a nearby C4 end, then an
α-1,6-glucosidase hydrolyzes the last one off as **free glucose**.
**Concrete.** Same granule, running down. Phosphorylase chews back from the outside until it hits
the four-residue stub at each branch. The stubs accumulate — a limit dextrin — and debranching
enzyme clears them.
**Claims.** Asserts phosphorolysis, not hydrolysis, is the main degradative step → ~90% of released
glucose leaves as G1P, no ATP to re-phosphorylate. Denies symmetry between synthesis and
degradation: different enzymes, different bonds broken vs made, different chemistry (phosphate vs
UDP).
**Predicts.** ~90% of breakdown yields G1P, 10% free glucose, matching the ~10% of residues in α-1,6
linkages. Muscle lacks glucose-6-phosphatase → muscle glycogen cannot raise blood glucose; liver has
it and can.

**Discriminators**
- α-1,4 vs α-1,6 — *which hydroxyl did C1 attack, C4 or C6?* Synthase = C4. Branching enzyme = C6.
- Glycogen synthase vs branching enzyme — *was UDP released?* Only synthase uses UDP-glucose.
- Phosphorylase vs debranching glucosidase — *is the product phosphorylated?* G1P = phosphorylase. Free glucose = debranching.
- Hemiacetal vs acetal — *does C1 still carry an OH?* OH = hemiacetal = reducing end.
- α vs β linkage — *is the anomeric OR down or up relative to C6?* Down = α (digestible). Up = β (cellulose).
- Anomer vs epimer — *is the differing carbon the anomeric one?* Yes = anomer.

**Compression** — the whole cluster on one axis: **what is bonded to C1 of glucose.**

| What C1 is bonded to | Name | Made or broken by |
|---|---|---|
| OH + ring O | hemiacetal — the reducing end | free in solution; mutarotates |
| O–UDP | activated donor | UDP-glucose pyrophosphorylase |
| O–C4 of the next glucose | **α-1,4-glycosidic** | **glycogen synthase** (makes) / phosphorylase (breaks) |
| O–C6 of a chain interior | **α-1,6-glycosidic** | **branching enzyme** (makes) / debranching (breaks) |
| O–Tyr of a protein | the primer | glycogenin, on itself |

Every question here is "what is on C1." Answer that and the bond name is automatic.

---

## Cluster 4 — Thermodynamics and kinetics
FL1: Q32, Q41

**The shared bench.** A spectrophotometer reading absorbance every second, beside a whiteboard
carrying one reaction-coordinate diagram. The cuvette holds Cluster 3's glycogen plus whatever enzyme
the passage adds. Everything here is either the **height of the hill** or the **difference in the
ground level**, and those are independent.

#### λmax reports an energy gap
FL1: Q32 · CC5E · broke: knowledge

**Structure.** A molecule absorbs the photon matching its HOMO–LUMO gap. E = hc/λ →
**large gap = short λmax; small gap = long λmax**. Conjugation adds π orbitals, raising HOMO and
lowering LUMO: narrower gap, longer λmax, red shift.
**Concrete.** Retinal in solvent absorbs around 380 nm, in the UV. Bind it to opsin through a
**protonated Schiff base** to a lysine: the positive charge pulls electron density along the
polyene, delocalization extends, λmax jumps to the visible. The opsin's own charged and polar
residues near the chromophore tune it further — S-cone ≈ 420 nm, rhodopsin ≈ 500, M-cone ≈ 530,
L-cone ≈ 560. **Same chromophore in all four. Only the protein differs.**
**Claims.** Asserts color vision is one molecule in four protein environments, λmax an
electronic-structure property. Denies four different pigments; denies absorbing the photon is the
signal — the signal is the 11-cis → all-trans **isomerization** the photon drives, which reshapes
retinal and activates the opsin.
**Predicts.** Longer λmax = lower photon energy = a receptor tuned redder. A polar residue mutated
in near the chromophore shifts λmax; one far away does not. Losing the L-opsin gene shifts red
sensitivity — red-green color deficiency.

**Worked example — photon energy.** Use **E(eV) = 1240 / λ(nm)**. Rhodopsin, λmax = 500 nm.
E = 1240/500 = **2.48 eV**.
**Faded.** The L-cone, λmax = 560 nm. E = 1240 / 560 = ______ eV.
Is that larger or smaller than rhodopsin's? ______

**Worked example — Beer's law.** A = εbc. A chromophore with ε = 5.0 × 10³ M⁻¹cm⁻¹ in a 1.0 cm
cuvette reads A = 0.40. c = A/(εb) = 0.40 / (5.0 × 10³) = **8.0 × 10⁻⁵ M**.
**Faded.** Same chromophore, same cuvette, A rises to 0.80. c = ______
Absorbance is linear in concentration, so this is a one-step ratio, not a recomputation.

#### Activation energy and ΔG are independent
FL1: Q41 · CC5E · broke: reasoning

**Structure.** **Ea** = height from reactants to the transition state, setting the *rate*. **ΔG** =
reactant-to-product level difference, setting the *equilibrium position*. Change one without the
other. ΔG = ΔH − TΔS; ΔG° = −RT ln Keq.
**Concrete.** Draw the hill on the whiteboard. Raise the peak: the reaction slows, the products sit
exactly where they sat. Lower the product well: more product at equilibrium, peak unmoved. Two
knobs, no linkage.
**Claims.** Asserts "spontaneous" and "fast" are unrelated words. Denies a very negative ΔG implies
a fast reaction — diamond → graphite has ΔG < 0 and an Ea so large the rate is unmeasurable.
**Predicts.** Temperature changes *both* — rate up via Arrhenius, equilibrium shifting per the sign
of ΔH. A catalyst changes only the first. Read which knob the stem turned.

**Worked example — ΔG° from Keq.** At 298 K, ΔG° = −2.303 RT log Keq, and 2.303 RT ≈ **5.7
kJ/mol**. So **ΔG° ≈ −5.7 × log Keq** in kJ/mol.
Keq = 100 → log Keq = 2 → ΔG° = −5.7 × 2 = **−11.4 kJ/mol**.
**Faded.** Keq = 1.0 × 10⁻³ → log Keq = ______ → ΔG° = ______ kJ/mol. Sign?
Anchor: **every factor of 10 in Keq is worth 5.7 kJ/mol.** Keq = 1 → ΔG° = 0, always.

#### What a catalyst does and does not do
FL1: Q41 · CC5E · broke: reasoning

**Structure.** An alternative path with a lower Ea, lowering the barrier forward and reverse **by
the same amount**; regenerated unchanged; absent from the stoichiometry and from the equilibrium
expression.
**Concrete.** Add the enzyme to the cuvette. The trace bends and reaches its plateau sooner. **The
plateau is at the same height it would have reached without the enzyme.** Faster arrival, same
place.
**Claims.** Asserts catalysis is purely kinetic. Denies four distractors: a catalyst shifts
equilibrium, changes ΔG or ΔH, increases yield at equilibrium, or is consumed. It changes ΔG‡ only.
**Predicts.** Add catalyst → forward rate up, reverse up by the same factor, Keq unchanged, plateau
unchanged, time-to-plateau shorter. Data showing the *final* level moving → the added species was
not a catalyst on the measured reaction.

#### Adding an enzyme to a mixture — the four-question schema
FL1: Q41 · CC5E · broke: reasoning (Skill 3, second half of section)

**Structure.** Enzyme added to a reaction mixture — run these in order:
1. **Does it catalyze the reaction being measured?** → rate up, position unchanged.
2. **Does it consume or produce one of the species in that equilibrium?** → the position shifts by
   Le Châtelier. Removing a product pulls the reaction forward. This is not catalysis.
3. **Does it covalently modify a different enzyme** (kinase adds phosphate, phosphatase removes
   it)? → *that* enzyme's activity changes; the thermodynamics of the measured reaction do not.
4. **Does it act on the substrate's physical state** — solubility, aggregation, accessibility? →
   the apparent rate changes because more substrate is reachable, not because Ea moved.
**Concrete.** Laforin, a **glucan phosphatase**, goes into the cuvette and hydrolyzes phosphate
esters off glycogen. Question 4, not question 1. Dephosphorylated glycogen is better branched, more
soluble, more accessible to phosphorylase and amylase — the downstream enzymes speed up though
laforin never touched their active sites.
**Claims.** Asserts "added enzyme" has four distinct meanings and the stem says which. Denies the
reflex "it's a catalyst, so nothing about equilibrium changes" — true only under branch 1.
**Predicts.** Lose laforin → glycogen accumulates hyperphosphorylated and poorly branched, forming
insoluble polyglucosan inclusions: Lafora bodies, progressive myoclonic epilepsy. Generally
**a phosphatase reverses whatever the corresponding kinase did** — inactivating if the kinase
activated, activating if it inactivated. Glycogen is the standard case of "vice versa":
phosphorylation activates phosphorylase and *inactivates* synthase, so a phosphatase there promotes
storage and blocks breakdown.

#### Rate-determining step and the rate law
FL1: Q41 · CC5E · broke: knowledge

**Structure.** The slowest elementary step — highest barrier on the diagram — sets the overall rate;
the rate law reads off that step's molecularity plus anything in equilibrium before it. Exponents
come from **experiment or from the mechanism**, never from balanced-equation coefficients.
**Concrete.** The whiteboard diagram has two humps. The taller one is the bottleneck. Lowering the
shorter hump does nothing to the measured rate.
**Claims.** Asserts overall kinetics report one step, not the whole path. Denies a balanced equation
predicts order.
**Predicts.** SN1's rate-determining step is ionization → rate = k[substrate], nucleophile
concentration absent from the rate law: the kinetic fingerprint separating SN1 from SN2, tying back
to Cluster 1. At [S] ≫ Km every enzyme is saturated, catalysis itself becomes rate-determining, rate
= Vmax, independent of [S].

**Discriminators**
- Ea vs ΔG — *does the change alter the height of the barrier or the depth of the well?*
- Catalyst vs product-removing enzyme — *did the final plateau move?* Moved = not catalysis.
- Kinetic vs thermodynamic control — *is the product the one over the lower barrier or the one in the lower well?* Low temperature and short times give kinetic; heat and time give thermodynamic.
- Temperature vs catalyst — *catalyst changes only rate; temperature changes rate and equilibrium.*
- Competitive vs noncompetitive inhibition — *can more substrate outcompete it?* Yes: Km up, Vmax unchanged. No: Vmax down, Km unchanged.
- λmax vs absorbance — *λmax is which photon energy is absorbed (a structure property); absorbance is how much (a concentration measurement).*

**Compression** — the whole cluster on one axis: **state-energy difference vs barrier height.**

| Quantity | What it measures | Path-dependent? | Changed by a catalyst? |
|---|---|---|---|
| λmax / HOMO–LUMO gap | difference between two electronic states | no | no |
| ΔH, ΔS, ΔG | difference between reactant and product states | no | **no** |
| Keq | the same difference, exponentiated | no | **no** |
| Ea (ΔG‡) | height of the barrier between them | **yes** | **yes — this one only** |
| Rate, Vmax, kcat | consequence of the barrier | **yes** | **yes** |

Top block: state functions, catalyst-proof. Bottom block: path properties, the only things a
catalyst touches. Sort the stem's quantity into a block before answering.

---

## Cluster 5 — Solutions
FL1: Q58

**The shared flask.** One 250 mL volumetric flask holding **0.078 mol** of NaCl — Q58's own number.
Every concept below is that flask read a different way. The whole cluster is one question: **what
is in the denominator?**

#### Molarity — moles per liter of solution
FL1: Q58 · CC5A · broke: reasoning

**Structure.** M = mol solute / L **solution**, not per liter of solvent; volume measured after
dissolving, because the solute occupies space.
**Concrete.** Weigh out 0.078 mol NaCl, tip it into the 250 mL volumetric flask, add water to the
etched line, invert. The line is the denominator.
**Claims.** Asserts molarity is defined on final volume. Denies adding solute to 250 mL of water
gives a 250 mL solution — it gives slightly more, and for concentrated solutions the difference is
real.
**Predicts.** Molarity is temperature-dependent, volume expanding with heat; molality is not. A
passage that heats a solution and asks which unit changed is asking this.

**Worked example — Q58's shape.** 0.078 mol of solute dissolved to a final volume of 250. mL.
1. Convert to liters: 250 mL × (1 L / 1000 mL) = **0.250 L**
2. M = mol / L = 0.078 / 0.250
3. Dividing by 0.25 is multiplying by 4: 0.078 × 4 = **0.312 M**

**Faded — dilution.** Take 25.0 mL of that 0.312 M solution and dilute to 100.0 mL.
M₁V₁ = M₂V₂, because **moles do not change when you add solvent**.
(0.312)(25.0) = M₂(100.0)
M₂ = ______

**Faded again — reverse direction.** You need 50.0 mL of 0.100 M solution from the 0.312 M stock.
What volume of stock? V₁ = ______

#### Molality, and when the denominator switches
FL1: Q58 · CC5A · broke: knowledge

**Structure.** m = mol solute / kg **solvent**. Mass, not volume; solvent, not solution. Used for
every colligative property because it does not change with temperature.
**Concrete.** Same 0.078 mol NaCl, now weighed into exactly 250. g of water rather than diluted to
a mark. Water being 1.00 g/mL, the number comes out the same — 0.312 — which is precisely why the
trap works. In any non-aqueous or concentrated system the two diverge.
**Claims.** Asserts the two answer different questions: molarity for stoichiometry and reaction
mixtures, molality for freezing point, boiling point, vapor pressure. Denies interchangeability
outside dilute aqueous solution.
**Predicts.** Dilute aqueous → M ≈ m, substitute freely. It breaks the moment a problem gives *grams
of solvent* rather than *volume of solution*, or changes temperature.

#### Colligative properties depend on particle count, not identity
FL1: Q58 · CC5A · broke: knowledge

**Structure.** Four properties, all scaling with the number of dissolved particles: vapor pressure
**lowering**, boiling point **elevation** (ΔTb = i·Kb·m), freezing point **depression**
(ΔTf = i·Kf·m), **osmotic pressure** (Π = i·M·R·T). The **van 't Hoff factor i** is the number of
particles one formula unit produces: glucose 1, NaCl 2, CaCl₂ 3, Na₂SO₄ 3. For water,
Kb = 0.512 °C/m and Kf = 1.86 °C/m.
**Concrete.** Two beakers, one 0.312 m glucose, one 0.312 m NaCl. The NaCl beaker freezes at twice
the depression, boils at twice the elevation, pulls twice the osmotic pressure — twice the
particles. Identity is irrelevant; count is everything.
**Claims.** Asserts chemical nature does not enter these four properties. Denies a "stronger" or
"heavier" solute has a larger effect.
**Predicts.** Rank solutes by i × m. A weak electrolyte gives i between 1 and 2, set by degree of
dissociation. Real ionic solutions run i slightly below ideal from ion pairing — why measured
depressions come out a few percent low.

**Worked example.** 0.078 mol NaCl in 250. g of water. Freezing point?
1. Molality: m = 0.078 mol / 0.250 kg = **0.312 m**
2. Particles: NaCl → Na⁺ + Cl⁻, so **i = 2**
3. ΔTf = i·Kf·m = 2 × 1.86 × 0.312 = 1.86 × 0.624 = **1.16 °C**
4. Freezing point = 0.00 − 1.16 = **−1.16 °C** (depression is always *down*)

**Faded.** The same 0.078 mol, but of CaCl₂, in the same 250. g of water.
i = ______ · ΔTf = ______ °C · new freezing point = ______

#### Osmotic pressure and tonicity
FL1: Q58 · CC5A · broke: knowledge

**Structure.** Π = iMRT, with R = 0.0821 L·atm/(mol·K). Osmolarity = i × M, the total particle
concentration; water moves toward the higher osmolarity. **Tonicity** counts only particles that
cannot cross the membrane.
**Concrete.** Drop a red cell into the 0.312 M NaCl flask. Osmolarity = 2 × 0.312 = 0.624 osmol/L,
roughly double plasma's ~0.30. Water leaves the cell and it crenates. Normal saline is 0.9% NaCl ≈
0.154 M, giving 0.308 osmol/L — isotonic by design.
**Claims.** Asserts osmotic pressure is colligative, set by particle count, and osmolarity is not
tonicity. Denies they are synonyms: urea raises osmolarity but crosses membranes freely, so a urea
solution can be iso-osmotic and hypotonic at once, and cells in it swell.
**Predicts.** Two compartments → compute i × M on each side; water flows toward the larger. A solute
that crosses the membrane is excluded from tonicity but kept in osmolarity.

#### The unit traps
FL1: Q58 · CC5A · broke: reasoning under time pressure

**Structure.** Six traps account for nearly every arithmetic-correct-but-wrong answer:
1. **mL not converted to L.** Off by 1000. Convert before anything else, on the page.
2. **Grams given, moles needed** — or the reverse. Divide by molar mass first.
3. **Molarity vs molality.** Check whether the denominator was a volume of solution or a mass of solvent.
4. **The van 't Hoff factor left out.** Every colligative calculation needs i.
5. **Dilution treated as addition.** M₁V₁ = M₂V₂ uses the *final* volume, not the volume added.
6. **Percent vs decimal.** 0.9% is 0.009, and 0.9 g per 100 mL is 9 g/L.
**Concrete.** Q58 gave 0.078 mol and a volume in milliliters. The chemistry is one division. The
only way to miss it is a unit.
**Claims.** Asserts these are unit errors, not concept errors, and the fix is procedural. Denies
more chemistry review helps.
**Predicts.** Write the units of the answer *before* computing. If the target is M, the expression
must end in mol/L, and any line whose units are not mol/L is wrong regardless of the arithmetic —
the check that survives the second half of the section, when Skill 2 dropped from 77% to 43%.

**Estimation without a calculator.** 0.078/0.25 → multiply by 4. Dividing by 0.5 → double. Dividing
by 0.2 → multiply by 5. MCAT answer choices are spread by factors, not decimals, so one significant
figure and a correct exponent pick the key.

**Discriminators**
- Molarity vs molality — *is the denominator a volume of solution or a mass of solvent?*
- Osmolarity vs tonicity — *can the solute cross the membrane?* If yes, it counts for osmolarity only.
- Colligative vs non-colligative — *would swapping the solute for a different one at the same particle count change the answer?* If no, it is colligative.
- Dilution vs mixing — *is solute being added, or only solvent?* Only solvent → moles conserved → M₁V₁ = M₂V₂.

**Compression** — the whole cluster on one axis: **what is in the denominator.**

| Unit | Numerator | Denominator | Temperature-dependent? |
|---|---|---|---|
| Molarity (M) | mol solute | **L of solution** | yes |
| Molality (m) | mol solute | **kg of solvent** | no |
| Mole fraction (χ) | mol solute | **total mol** | no |
| Mass percent | g solute | **g of solution** × 100 | no |
| Osmolarity | i × mol solute | **L of solution** | yes |
| Normality (N) | equivalents | L of solution | yes |

Read the denominator off the stem first. The arithmetic is then one division.

---

## Cluster 6 — Separations and purification
FL1: Q1–Q5 passage (Q4 the miss)

**The shared workup.** The malic acid flask from Cluster 1, cooled. In it: unreacted malic acid,
fumaric acid, maleic acid, sulfuric acid, water. Everything below pulls those four apart. **Every
separation is a partition between two phases, differing only in which property drives it.**

#### The partition principle
FL1: Q1–Q5 · CC5C · broke: reasoning

**Structure.** Two phases in contact; a compound distributes between them by one property; the
moving phase carries compounds in proportion to how little they favor the stationary phase. Mobile +
stationary + one discriminating property = a separation.
**Concrete.** In the workup funnel, ether and water, property polarity. On a TLC plate, solvent
front and silica, still polarity. In a gel, buffer and polyacrylamide, property size.
**Claims.** Asserts chromatography, extraction, distillation, and electrophoresis are one mechanism
with five faces. Denies separate techniques to memorize individually.
**Predicts.** Name the two phases and the property → elution order, without recalling the
technique's name. That is the only question the exam asks here.

#### Acid–base extraction
FL1: Q1–Q5 · CC5C · broke: knowledge

**Structure.** Charged species dissolve in water, neutral species in organic solvent; adjust pH to
switch a compound's charge and it moves between layers on command. NaHCO₃ (weak base) deprotonates
carboxylic acids only; NaOH deprotonates carboxylic acids *and* phenols; HCl protonates amines.
**Concrete.** Shake the cooled workup with ether and water. At pH 1 fumaric and maleic acid are
neutral diacids and go up into the ether. Add aqueous bicarbonate and shake: both deprotonate to
dianions and drop into the aqueous layer as sodium salts. Acidify with HCl and they precipitate
back out, free of everything neutral.
**Claims.** Asserts extraction is Cluster 2's pH-vs-pKa rule in a funnel. Denies it separates by
"how acidic" in the abstract — it separates by whether pH sits above or below each compound's pKa.
**Predicts.** Carboxylic acid from phenol: bicarbonate first (only the carboxylic acid, pKa ~5,
deprotonates; the phenol at pKa ~10 stays neutral in the organic layer), then NaOH to take the
phenol. Which layer sits on top is density: ether and hydrocarbons float on water, dichloromethane
and chloroform sink.

#### Thin-layer chromatography and Rf
FL1: Q1–Q5 · CC5C · broke: knowledge

**Structure.** Rf = (distance traveled by the spot) / (distance traveled by the solvent front),
always between 0 and 1, always measured from the same origin line. Normal-phase silica is a
**polar** stationary phase: polar compounds stick and travel little — **low Rf**; nonpolar
compounds ride with the solvent — **high Rf**.
**Concrete.** Spot the workup mixture on silica and run it. Maleic acid, cis and with a net dipole,
hydrogen-bonds hard to the silica and barely moves; fumaric acid, trans with its two dipoles
opposed, moves further. Two spots, one plate, one property.
**Claims.** Asserts Rf is a ratio of distances on one plate, comparable only within that plate and
solvent. Denies Rf is a physical constant — change the solvent polarity and every Rf changes.
**Predicts.** More polar solvent → everything moves further → all Rf values rise. Reverse-phase (C18
stationary phase, polar mobile phase) inverts the whole order: **nonpolar compounds stick, polar
ones elute first.** That inversion is a standard distractor.

**Worked example.** Solvent front travels 8.0 cm from the origin. A spot travels 2.0 cm.
Rf = 2.0 / 8.0 = **0.25**.
**Faded.** A second spot on the same plate travels 6.0 cm. Rf = ______
Which of the two compounds is more polar on normal-phase silica? ______

#### Column chromatography — the four sorting properties
FL1: Q1–Q5 · CC5C · broke: knowledge

**Structure.** One column, four possible stationary phases, four properties:
- **Size-exclusion (gel filtration)** — porous beads. **Large molecules elute FIRST**: they cannot
  enter the pores and take the short path around, while small molecules wander through the pores
  and are retarded.
- **Ion-exchange** — charged resin. A **cation** exchanger carries fixed negative groups and binds
  *positively* charged proteins; elute with rising salt or by shifting pH past the protein's pI.
- **Affinity** — an immobilized ligand, antibody, or His-tag/nickel pair. Binds one target
  specifically; everything else washes through; elute with free ligand or a competitor.
- **Gas chromatography** — vaporized sample; separates by boiling point and volatility. Requires a
  thermally stable, volatile analyte, so not for proteins.
**Concrete.** Pour one protein mixture down four columns: column 1 sorts by radius, column 2 by the
net charge you computed in Cluster 2, column 3 by whether a molecule binds one specific ligand.
Column 4 will not run at all — proteins do not vaporize.
**Claims.** Asserts size-exclusion elutes big first — the counterintuitive one. Denies a column
always retains the largest species longest.
**Predicts.** Tagged protein → affinity, the only one-step purity. Identical masses → ion-exchange
or isoelectric focusing, their pI values differing. Desalting → size-exclusion: protein out first,
salt last.

#### Electrophoresis
FL1: Q1–Q5 · CC5C · broke: knowledge

**Structure.** Charged molecules migrate through a gel toward the opposite electrode; the gel
retards by size. Three variants:
- **SDS-PAGE** — SDS denatures and coats every protein with negative charge in proportion to mass,
  so charge-to-mass ratio is uniform and separation is by **size alone**. Small runs far.
- **Native PAGE** — no denaturant, so migration reflects **size, shape, and native charge**
  together, and quaternary structure is preserved.
- **Isoelectric focusing** — a pH gradient; each protein migrates until pH = its **pI**, where its
  net charge is zero and it stops.
**Concrete.** Run the hexapeptide from Cluster 2 in an IEF gel. It stalls at pH 5.15. The variant
carrying Arg in place of His stalls further toward the basic end — a neutral residue replaced by a
positive one raises the pI.
**Claims.** Asserts SDS-PAGE deliberately destroys charge information to read size cleanly. Denies
SDS-PAGE mobility says anything about charge or oligomeric state — why SDS-PAGE and native PAGE give
different band counts for the same sample.
**Predicts.** **pH > pI → protein is negative → migrates to the anode.** pH < pI → to the cathode.
Two-dimensional gels combine IEF (by pI) with SDS-PAGE (by size) precisely because those two
properties are independent.

#### Distillation, recrystallization, and resolving enantiomers
FL1: Q4 · CC5C · broke: trap

**Structure.** Distillation sorts by **boiling point**, needing a gap of roughly 25 °C for simple
distillation and a fractionating column below that. Recrystallization sorts by **differential
solubility with temperature** — target soluble hot and insoluble cold, impurity soluble at both. Enantiomers have **identical** boiling points, melting points, solubilities, and
Rf values in every achiral environment, so they need a **chiral** one: a chiral resolving agent to
make diastereomeric salts, or a chiral chromatography column.
**Concrete.** Maleic acid is cis: COOH groups crowd, no tight lattice, ~79 g per 100 mL in water.
Fumaric acid is trans: packs efficiently, melts far higher, under 1 g per 100 mL. Cool the aqueous
workup — fumaric crystallizes out cleanly, maleic stays dissolved. The perfect recrystallization
pair.
**Claims.** Asserts cis/trans geometry controls lattice packing → melting point and solubility → the
separation. Denies a physical separation can resolve enantiomers: the racemic mixture from Cluster
1's planar carbocation cannot be separated by distillation, recrystallization, or ordinary
chromatography. **That was the shape of Q4's trap: statements about the products' physical
differences were true; the false statement was about stereochemistry.**
**Predicts.** Maleic acid's first pKa is ~1.9, its second ~6.1 — an unusually wide gap, the cis
monoanion being stabilized by an intramolecular hydrogen bond the second deprotonation must break.
Fumaric acid, trans and unable to form it, has pKa ~3.0 and ~4.4, closer together. Geometry predicts
acidity — exactly what a NOT stem builds an option out of.

**Discriminators**
- Size-exclusion vs every other column — *does the biggest species come out first or last?* First, only here.
- Normal-phase vs reverse-phase — *is the stationary phase polar or nonpolar?* Polar stationary → polar compounds have low Rf.
- SDS-PAGE vs native PAGE — *was the native charge destroyed?* SDS destroys it, leaving size alone.
- Native PAGE vs isoelectric focusing — *does migration stop at a position, or continue for the whole run?* IEF stops at pI.
- Bicarbonate vs hydroxide wash — *is the target's pKa below ~7 or above?* Bicarbonate takes carboxylic acids only.
- Diastereomers vs enantiomers — *do they differ in any achiral physical property?* Diastereomers do and separate normally; enantiomers do not and require a chiral environment.

**Compression** — the whole cluster on one axis: **the property being sorted on.**

| Method | Sorts on | Elutes/moves first |
|---|---|---|
| Liquid–liquid extraction | polarity, set by charge, set by pH | the layer you choose |
| Normal-phase TLC / column | polarity | least polar (highest Rf) |
| Reverse-phase HPLC | polarity, inverted | most polar |
| Size-exclusion | hydrodynamic size | **largest** |
| Ion-exchange | net charge (i.e. pI vs buffer pH) | the species not binding the resin |
| Affinity | specific binding | everything except the target |
| Gas chromatography | boiling point / volatility | lowest boiling |
| Distillation | boiling point | lowest boiling |
| Recrystallization | solubility vs temperature | impurity stays in solution |
| SDS-PAGE | size only | smallest travels farthest |
| Native PAGE | size + shape + charge | — |
| Isoelectric focusing | pI | stops where pH = pI |
| Chiral column / resolving agent | handedness | requires a chiral environment |

Identify the property in the first column and the elution order is determined. Every question in
this category is that one lookup.

---

## Cross-links

The six clusters share four objects; retrieval through the link beats retrieval through the concept
name.

- **pKa vs pH** is one rule used in three places: side-chain charge (Cluster 2), acid–base
  extraction (Cluster 6), and buffer behavior at physiological pH via histidine.
- **pI** is computed in Cluster 2 and *used* in Cluster 6 — ion-exchange binding and isoelectric
  focusing are the pI calculation with a gel attached.
- **The glycogen granule** carries Cluster 3 into Cluster 4: laforin acts on that object, and the
  bond glycogen synthase makes is the Q39 answer.
- **The planar carbocation** in Cluster 1 produces the racemic and geometric mixture that
  Cluster 6 then has to separate — and explains why one of those separations is impossible.

**The two procedures that matter most under time pressure**, both from second-half misses:
1. On a NOT/LEAST/EXCEPT stem, write the positive form in the margin before reading option A.
2. On any calculation, write the units of the target answer before the first line of arithmetic.

---

# CARS

## CONCEPTS — CARS

FL1: 124, 50th percentile, 35/53. Eighteen misses.
Decay: **82% first third → 59% middle → 58% final third** — that gradient, not any question type,
is the largest recoverable block of points here.

CARS has no content. What is learnable: **how AAMC builds a wrong answer**, and **what each stem
type actually demands.**

Sources: `research/07-cars-construction.md` (AAMC CARS outline + AAMC-labeled Road Map corpus,
n=181 stems), `study/CARS-AAMC-SETS.md` (14 AAMC/Khan passage sets, per-choice rationales in
AAMC's own voice), `results/FL1-ANALYSIS.md`.

---

### THE ONE FACT THAT ORGANIZES EVERYTHING

Count the AAMC rationales that reject an option for being **false**. Almost none:

> "this is not supported by the passage" · "there is no evidence in the passage for this"
> · "the passage does not discuss this" · "this is not the *best* answer" · "this is true of
> X but the question asks about Y"

**CARS is not a truth test. It is a warrant test.** Never "is this true?" — always
"did *this text* license this?" AAMC's standard: the key presents
*"the most likely and most reasonable outcome"* — a **superlative over a graded set**, not a
predicate. Three options can be true; one is licensed.

> **The key is the option you can defend in one move. The near-miss is the one you can defend
> in three.** If your justification has a "well, if you assume…" in it, you are on the wrong option.

---

## 1 · THE 14 REJECTION TEMPLATES

Every rejection sentence AAMC writes is one of fourteen moves. **Measured** across all 66 items in
`CARS-AAMC-SETS.md`:

| Rejection language | count |
|---|---:|
| "no evidence / no information / no mention / no discussion / no language / no suggestion" | 16 |
| "**Although** [option is true] …" — grant, then deny relevance | 17 |
| "the passage does not discuss / mention / state / assert / argue" | 8 |
| "… **rather than** …" — right proposition, wrong object | 11 |
| "is not related / not relevant / not central / not the main / not part of" | 7 |
| "the author never states / never claims / never argues" | 6 |
| "outside" / "not directly" / "irrelevant" | 12 |
| **"this option is false / untrue / inaccurate"** | **0** |

Zero: never once is a distractor rejected for being *false about the world*. All six occurrences of
"is wrong / is incorrect" name an option *number* ("option D is incorrect") or sit inside an
option's own text — never a verdict on truth.

**So the operative question is never "is this true?" It is "where is the sentence?"** No finger on
a sentence, no option — however sensible it is.

---

#### R1 · NO ANCHOR SENTENCE
*n ≈ 30 — the most common rejection by a wide margin*

**Structure.** Topically apt, plausible, often true, built from what an educated reader already
knows — and no passage sentence says it.

**Concrete.** *Ultimatum game*, Q2, on the significance of "the range of players remained limited."
Option B: "Limiting the range of players allowed the experimenters to better control the outcome" —
any methods course supplies "controlled sample" on reflex. AAMC: *"There is no evidence the
experimenters wanted to limit the range of players to better control the game (option B) or range
of variables (option D)."* It was limited **because** the subjects were Western university
students: suffered, not chosen.

**Claims.** Support is a **location**, not a property — you can put a finger on a sentence or the
option is dead. Denies the test you actually run, *does this sound right given what I know about
the topic?*, which measures your knowledge, not the passage's.

**Why it pulls.** You retrieve your own competence, not the passage. Knowing feels like reading.

**Disqualifier.** Point at the sentence. There isn't one.

**Predicts.** On a field you know — psychology, biology, medicine — R1 rate goes **up**: raise the
anchor bar, don't relax it.

---

#### R2 · SUPPORTED, BUT ANSWERS A DIFFERENT QUESTION
*n ≈ 11 · the near-miss slot on function and evidence items*

**Structure.** A proposition the passage genuinely asserts, from a different part of the argument:
truth untouched, relevance corrupted.

**Concrete.** *Tools for thought*, Q1: which assertion is presented **as evidence that computers
are affecting people's conception of the mind**? Option D is a real authorial claim. AAMC:
*"The passage does mention … that
evaluating the impact of technology on thinking will be a challenge in higher education
(option D), **but this is not related to the idea** that computers may be changing people's
conception of the mind."* A and B, also real passage content, die the same way:
*"These examples do not provide evidence that
computers are affecting people's thinking about the mind."*

**Claims.** An option must be **responsive to the stem's qualifier**, not merely true of the
passage. Denies *found it, done* — locating the sentence is necessary and not sufficient.

**Why it pulls.** You find the sentence, the confirmation click fires, you stop reading the stem.

**Disqualifier.** Restate the stem as a demand first: *"give me evidence for
the MIND claim, not the SKILL claim."*

**Predicts.** Any stem with a qualifier clause ("as evidence **that X**," "in order
**to Y**," "about **Z**") puts at least two true-of-the-passage options in play.

---

#### R3 · CONCESSION READ AS THESIS
*"Although" is the single most frequent opening word in AAMC's rejections — n = 17*

**Structure.** The author grants component C of an opponent's view before denying D; the option is
built from C — true, author-voiced, citable, not the thesis.

**Concrete.** *What is life?*, Q4. AAMC: *"**Although** the author mentions that these molecular
machines are spontaneously produced (option 4), **this is not central to the main argument**,
which is that they execute non-spontaneous processes essential to living organisms."* His own
voice, still wrong.

**Claims.** Author-voiced is not the author's point; arguing requires stating the thing you are
about to deny. Denies *if he wrote it, he means it as his position* — the most expensive false rule
in CARS.

**Why it pulls.** Every elimination heuristic returns *keep*. Only "does this answer the question."

**Disqualifier.** Conceded material sits **left** of a "but," "however," "yet," "although," or
"in fact." The thesis is on the right.

**Predicts.** Verbatim-traceable option plus relief → find the nearest contrastive conjunction; if
your sentence is upstream of it, drop the option.

---

#### R4 · MENTIONED, BUT NOT EVIDENCED
*the entire evidence/support archetype lives here — his Q75, Q77, Q85*

**Structure.** A claim the passage makes **and never supports**, on an item asking which claim
**is** supported.

**Concrete.** *Tools for thought*, Q4: "Which passage assertion is **most supported in the passage
by evidence or examples**?" AAMC: *"The potential downsides to calculator use she cites from past
conversations with colleagues are **anecdotal examples, not assertions that are further supported
by evidence** (options B and C). The author does assert that the invention of writing systems
brought about radical changes in thinking in the first paragraph, but **no evidence is offered for
this statement** (option D)."* Key A is the only claim with a worked example under it: the CS major
reinterpreting a Freudian slip.

**Claims.** "Supported" names a **relation between two sentences**, not a property of one. Denies
*supported = the passage asserts it*; a claim is not support for itself.

**Why it pulls.** All four are things the passage says; only *argumentative role* separates them.

**Disqualifier.** What sentence sits **beneath** this one? Nothing → premise, not "supported."

**Predicts.** Ignore truth; map the tree. The key is a node with children, distractors are leaves.

---

#### R5 · WRONG VOICE
**Structure.** A proposition the passage *contains* but does not *endorse* — cited scholar, reported
consensus, concession, entertained hypothesis — attached to the author; or his own thesis handed to
the cited figure.

**Concrete.** *Huns and Eurasian history*, Q6, on what would weaken **Pirenne's** explanation. AAMC:
*"The issue of the scale of the campaign being too large (option 3) **is part of the passage
author's alternative account and not part of Pirenne's explanation**."* Right paragraph, wrong owner.

**Counter-case you must hold.** *Does free will exist?* — Dennett and Libet are cited and
**endorsed**; the quantum-fluctuation people are cited and destroyed. "Cited therefore rejected" is
a false rule AAMC punishes.

**Claims.** Every proposition has an **owner**, and the owner is part of the proposition. Denies two
opposite errors at once: *it's in the passage so it's the author's*, and the overcorrection *cited
therefore rejected*.

**Why it pulls.** Attribution is invisible to keyword matching, and frames don't highlight.

**Disqualifier.** Find the sentence, then the *frame*: the subject of the reporting verb, and
whether the next sentence extends it or turns on it.

**Predicts.** Every passage has an item whose two survivors differ only in owner. Tag ownership on
the way in (§3) or pay for it here.

---

#### R6 · WRONG SCOPE
**Structure.** Right proposition, wrong quantity — a proper subset or superset of what the stem
asks about. The "rather than" family.

**Concrete.** *Maternal psychology*, Q3. AAMC: *"The passage specifically discusses **mothers and
their interactions with their infants** (options 2 and 4) **rather than women interacting with
children in general** (options 1 and 3)."* Two of four die on one noun. Also *Does free will
exist?*, Q1: *"the author doesn't state that **all** properties of the brain are
best studied by psychology, but that **some** properties of the brain may be emergent."*

**Claims.** Quantifiers and population nouns are **content**, not phrasing: `mothers` and `women`
are different claims, `some` and `all` are different claims. Denies *same idea, different wording*.

**Why it pulls.** The proposition is right, and scope reads as phrasing.

**Disqualifier.** Put the option's population word next to the passage's. `mothers` vs
`women`. `some` vs `all`. `this study` vs `the field`.

**Predicts.** When two survivors say the same thing the difference is a noun or a quantifier — find
it first, because reasoning cannot break a scope tie.

---

#### R7 · PASSAGE VOCABULARY, WRONG JOINT
**Structure.** Every content word kept, exactly one relation corrupted: cause↔effect,
necessary↔sufficient, correlation→causation, part↔whole, conditional direction, supersede↔refute.

**Concrete.** *Does free will exist?*, Q1, option C: "Free will is an emergent property that is
decoupled from the standard macroscopic laws of causality." Every phrase is lifted — but
"partial decoupling … from the standard macroscopic laws of causality" belongs to the
**quantum-fluctuation** paragraph the author calls *nonsense*, and "emergent property" to the
paragraph he endorses: the option splices two paragraphs across a rejection. AAMC:
*"The author doesn't talk about emergent properties being decoupled from the standard laws of
causality."*

**Claims.** The meaning sits in the **connective**, not the content words. Denies recognition as
evidence: matching vocabulary is not matching claims, and familiarity of wording is uncorrelated
with correctness.

**Why it pulls.** Word-level recognition fires on every phrase; the eye skips syntax.

**Disqualifier.** Diagram both survivors as `X —[relation]→ Y`, then find the passage's own
connective. AAMC builds deliberately fragile transitions for exactly this.

**Predicts.** The option that feels *maximally familiar* is the more suspect one.

---

#### R8 · ASSUMED, NOT ARGUED
**Structure.** The passage's *background premise*, on an item asking for its *purpose, question, or
point*. Setup mistaken for payload.

**Concrete.** *Maternal psychology*, Q3, on the new study's main purpose. AAMC:
*"Although the author asserts that infants' expressions of negative emotion will cause mothers to
experience stress reactions, **this effect is assumed and is not the main question that is being
studied** (option 4). Rather, it is presented as a potential problem for which the positive effects
… may be a solution."*

**Claims.** What a passage **assumes** and what it **argues** are different roles; only one is the
point. Denies *most repeated = most important* — frequency tracks the premise, which is what has to
be explained before the argument can start.

**Why it pulls.** The background is stated more often and more plainly than the thesis.

**Disqualifier.** What would the passage still need to prove if this option were granted? If
"everything," it is setup.

**Predicts.** On purpose and main-idea items the most-repeated content is the premise; the thesis
appears once, late, often hedged.

---

#### R9 · TRUE BUT INERT
**Structure.** On strengthen/weaken and incorporation items: a real fact about the subject with
**no contact with the specific link under attack**.

**Concrete.** *Understanding Thomas Hardy*, Q3, whose claim links *evolutionary theory* to
predeterminism. AAMC: *"the argument that Calvinists believe in both God and Predestination
(option 2) **would have no effect on the author's claim because it does not involve evolutionary
theory**."*

**Claims.** Strengthening and weakening are **local to one inference**, never to a topic. Denies
*relevant to the passage = relevant to the argument*, the reason three of four options survive your
first pass here.

**Why it pulls.** On-topic, true, in the passage's own vocabulary — just not about the joint.

**Disqualifier.** Name the link as `P → C` **before** options, then ask only: does this touch P→C?

**Predicts.** Most options will be about the passage and one about the inference. Find the arrow,
then check each option's *direction* against it.

---

#### R10 · REVERSAL IN FRESH WORDS
*floor-level trap — but it is re-lexicalized, so it never announces itself*

**Structure.** Negate the key, restate the negation positively in vocabulary the passage never used
for it. Never "the author denies X."

**Concrete.** *Deconstructionism*, Q4, option B: "To acknowledge its **existentialist principles**
in order to propose an extension of these principles." AAMC: *"The author does not portray
deconstructionism as having existentialist principles … in fact he **contrasts** deconstructionism
and existentialism in the final paragraph."* The option fuses the author's two poles.

**Claims.** The **sign** of a relation survives re-lexicalization — a negation can be stated
entirely in positive vocabulary. Denies that a reversal announces itself with a negation word; it
reads as a competent summary.

**Why it pulls.** Reversals read as *summaries* when you are tired.

**Disqualifier.** For any option asserting a relation between two named things, check the sign: same
side or opposite sides?

**Predicts.** This is the option you pick in the last third — cheap when fresh, nearly invisible when
depleted, which is precisely the §4 problem.

---

#### R11 · SILENCE READ AS SUPPORT
**Structure.** The passage raises a variable and never resolves it; the option asserts a resolution,
in either direction.

**Concrete.** *Designing courthouses*, Q1 ("people's reactions were independent of…"), option D:
peer influence. AAMC: *"There is limited information in the passage about peer influence. People
are asked to imagine themselves accompanying a friend to the courthouse, but based on the passage,
**it's unclear if people's reactions were dependent or independent of their peers**."* The passage
mentions the friend; mentioning is not measuring.

**Claims.** **Naming** a variable and **settling** it are different acts, and only the second
licenses an option. Denies the anchor test as sufficient — the mention exists, R1 passes, and the
option is still dead.

**Why it pulls.** The topic *is* there, so the R1 anchor test appears to pass.

**Disqualifier.** "The passage names this" versus "the passage settles this."

**Predicts.** On "independent of / unaffected by / regardless of" stems the key is the variable the
passage **explicitly measured and found null** — here attractiveness, where participants responded
to intimidation "rather than" beauty.

---

#### R12 · WRONG CATEGORY
**Structure.** Not the *kind of thing* the stem asked for. Not false — ineligible.

**Concrete.** *Designing courthouses*, Q3, on architectural features activating mental associations.
Option D: an unpopular grocery store has bad produce. AAMC, in one sentence:
*"Bad produce is **not an architectural design feature** of a grocery store."* B and C fail a second
category test — *function* (no drive-through, no play area) where the stem demands *association*.

**Claims.** The stem specifies a **kind**, and an option of the wrong kind is ineligible before its
truth is assessed at all. Denies that every option earns an evaluation on the merits — some are
answered by a noun, in two seconds.

**Why it pulls.** It matches the scenario's shape, and shape matching is fast.

**Disqualifier.** Say the stem's category noun before options: *architectural feature.
association, not function.* D is gone in two seconds.

**Predicts.** Category checks cost no rereading, so a category-ineligible option should never
survive to your two-option adjudication.

---

#### R13 · SURFACE ANALOGY, BROKEN RELATION
**Structure.** AAMC's most explicitly published recipe: the **key matches the relation and
mismatches the domain**; the trap matches the domain and mismatches the relation.

**Concrete.** *Tools for thought*, Q3, on "the tools we use to think change the ways in which we
think." Option D — an office manager installs accounting software — is the *tool* option: same
domain, technology, workplace. AAMC: *"**Although** new accounting software represents a
new tool, any benefit of increased productivity **may be a direct effect from the software, and may
not necessarily reflect fundamental changes in the thinking** of the humans who use it."* Key C:
someone appreciates abstract painting differently after learning a theory of complementary colors —
the *theory* is the tool, the *seeing* is the thought.

**Claims.** An analogy is a claim about a **relation**; the domain is scenery. Denies *same subject
matter = same structure* — the fastest signal your reader produces and, on these items, the
anti-correlated one.

**Why it pulls.** The distractor shares nouns with the passage.

**Disqualifier.** Strip the nouns and write the relation as a skeleton: *X alters the medium of
thought → thought itself changes.* Test options against the skeleton, not the scene.

**Predicts.** On "most like / LEAST analogous," expect the key in an unrelated field and the trap in
the passage's own.

---

#### R14 · NOT THE BEST
**Structure.** The residual class: supported, responsive, correctly scoped and attributed — and a
second option is *more so*. AAMC's standard is a superlative: the key presents
*"the most likely and most reasonable outcome."*

**Concrete.** *Censorship*, Q1. Option A says the new claim "provides an explanation for a
difficulty implied in the opening paragraph"; option C says it "**both contradicts and resolves**"
that difficulty. C captures both moves, A one. AAMC eliminates A in one clause: *"The new information
would not provide an explanation for the current conditions."*

**Claims.** The instruction is a **superlative**, so correctness here is comparative, not absolute.
Denies *I can defend it, therefore it's right* — defensibility is the wrong test precisely when both
survivors are defensible.

**Why it pulls.** Nothing is wrong with it. That is the entire problem.

**Disqualifier.** Count your justification steps. **The key is defensible in one move; the near-miss
takes three.** A defense containing "well, if you assume…" is on the near-miss.

**Predicts.** Two survivors → find the **one axis** they differ on (responsiveness, scope, strength,
attribution, relation) and ask which side of it the passage is on. Without naming the axis a 50/50
becomes a coin flip.

---

**Discriminators**

- **R1 vs R11** — R1: is the topic in the passage at all? R11: the topic is there; did the passage *settle* it?
- **R2 vs R3** — both are true and non-responsive. R2's sentence is in a different part of the argument; R3's sentence is on the left of a "but."
- **R4 vs R8** — R4: this claim has no evidence under it. R8: this claim is the floor the argument stands on.
- **R5 vs R7** — R5: right words, wrong owner. R7: right words, wrong connective.
- **R6 vs R14** — R6: the options differ by a quantifier or a noun. R14: they differ by degree of fit, with no single word to point at.
- **R10 vs R13** — R10 inverts a relation *inside* the passage. R13 preserves the passage's scenery and inverts the relation in a *new* one.

**Compression** — the one axis is **what the option is missing.**

| | what is absent |
|---|---|
| R1 | a sentence |
| R11 | a finding (the sentence exists, the result doesn't) |
| R4 | evidence under the sentence |
| R8 | argumentative load — it's a premise |
| R2 | responsiveness to this stem |
| R3 | thesis status — it's the conceded half |
| R5 | the right owner |
| R6 | the right quantity |
| R7 | the right connective |
| R9 | contact with the arrow under attack |
| R12 | category eligibility |
| R13 | the relation, under matching scenery |
| R10 | the sign |
| R14 | nothing — the other option just has more |

---

## 2 · THE SEVEN ARCHETYPES HE MISSED

Eighteen misses, seven stem families. Seventeen are placed below; **Q79** is not — AAMC's
skill and content tags came through blank for it in the score extract, so it has no archetype.

**Q98, Q99, Q100, Q101 were four consecutive misses** — main idea, apply, function, function. One
passage, and the composition says he never built its skeleton: main idea and function need the
argument's shape, apply needs the author's framework. Miss the shape and the set goes. See §4.

---

#### A · FUNCTION / PURPOSE
FL1: Q66, Q100, Q101 · *"why is X included," "the author explains his focus is different because"*
· broke: **trap (R2)**

**What is really being asked.** Not what the material *says* — what its inclusion *does for the
argument*. AAMC prints content and job as options every time.

**Where the answer lives.** Rarely in the cited sentence — function is conferred by a claim in a
**different paragraph**, usually one downstream.

**Concrete.** *Censorship*, Q4: "The author mentions both the legal right to speak our minds and our
lack of agreement about what we want our children to watch … most likely **in order to**:" — the
function of ¶3 opens ¶4, "One political solution is rating systems." AAMC:
*"this information serves to introduce and explain why the United States has adopted rating
systems."*

**Claims.** A unit's **content** and its **job** are separate facts, and function items ask only
about the job. Denies that the cited sentence contains its own purpose.

**The trap it attracts.** R2, every time. Constructed example in `research/07` (not AAMC): asked why
the author mentions the period's devotional literature, the trap says "to establish that viewers
sought consolation" — what the evidence **says**. The key is what deploying it **does**: undercut a
premise the opponent's account requires.

**Predicts.** Read one paragraph past the citation before choosing. Two survivors: one is content,
one is job — take the job.

---

#### B · EVIDENCE / SUPPORT
FL1: Q75, Q77, Q85 · *"which fact gives the strongest support," "which assertion does this support"*
· broke: **reasoning (argument roles never mapped)**

**What is really being asked.** Classify statements by **argumentative role** — premise, conclusion,
illustration, concession, unsupported assertion. All four options are usually true.

**Where the answer lives.** In the *relation between* two sentences: a claim with something
underneath it.

**Concrete.** *Tools for thought*, Q4 — worked in R4. Four true authorial assertions; the key is the
only one with a worked example under it. AAMC rejects two as *"anecdotal examples, not
assertions further supported by evidence"* and one because *"no evidence is offered for this
statement."* Q1 of the same set reads the tree upward: which assertion is presented **as evidence
for** a specific claim.

**Claims.** An argument is a **tree**; every statement occupies a node, and *supported* means having
children. Denies that reading for content can classify statements — role is invisible to content and
has to be recorded as you read.

**The trap it attracts.** R4 and R8. Vivid claims get asserted and boring claims get evidenced, so
the most memorable sentence is usually the unsupported one.

**Predicts.** Build two columns on the noteboard as you read: **CLAIM** / **what backs it**. Ten
seconds per paragraph, and it *is* the answer.

---

#### C · INFERENCE
FL1: Q73, Q78, Q95, Q103 · *"it may be inferred," "the most likely reason behind"* · broke:
**trap (R1 / R10)**

**What is really being asked.** What must be true **given only this text** — one step, not two.
AAMC's "It can be inferred" stems were labeled Foundations of Comprehension **100% of the time**
(n=4): a *local* skill.

**Where the answer lives.** The immediate sentence context, plus at most its neighbors.

**Concrete.** *Deconstructionism*, Q1: what does "America is deconstruction" mean? The answer is the
clause immediately before — America is a *"historically dissociated construction of random
meanings."* AAMC: *"This phrasing suggests that America and deconstructionism have in common a lack
of consistency in interpretation."* All three distractors need an added premise: US literature suits
the method (B), US critics built it (C), US universities are politically captured (D) — killed with
*"the passage does not discuss,"* *"it does
not assert,"* *"but does not assert."*

**Claims.** On AAMC, *infer* means **paraphrase plus one implication** — Foundations of
Comprehension, not reasoning. Denies the ordinary sense of inference as a chain of deduction. Chain
length is the discriminator, and longer is worse.

**The trap it attracts.** R1 above all — inference stems invite reasoning, and reasoning recruits
knowledge. Then R10, since a two-step inference can land on the author's opposite.

**Predicts.** **One step from a passage sentence = key. Two steps = distractor.**

---

#### D · APPLY TO A NEW SITUATION
FL1: Q89, Q92, Q99, Q109 · *"would probably," "which subject area would be," "the single change that
would most weaken"* · broke: **reasoning (framework not held)**

**What is really being asked.** Run the author's framework — not yours, not the world's — over
material the stem supplies. AAMC: *"rule out the options that do not fit or
are incongruent with the context (e.g., framework, perspective, scenario) created by the passage."*

**Where the answer lives.** Nowhere in the passage: the author's *principle*, one sentence, has to
be in your head before you read the options.

**Concrete.** *Deconstructionism*, Q3: how would this author review a stage production of *Julius
Caesar*? Every option is a defensible review, so AAMC selects on framework — writing is
*"an imaginative exploration of ideas"* and *"Literature is not a subordinate
category of social criticism"*, so the review assumes Shakespeare's presentation reflected
**artistic sensibility** (C). Option A, evidence the play served Shakespeare's gender and class, is
a competent modern review and *the deconstructionist framework the author spent five paragraphs
attacking*.

**Second instance, strengthen form.** *Understanding Thomas Hardy*, Q3, on the arrow
`evolutionary theory → predeterminism`. Two options *weaken* it (A — evolution predicts change over
deep time, not daily decision-making; C — evolution is scientific while predestination invokes
divine forces) and one is inert — *"the argument that
Calvinists believe in both God and Predestination (option 2) **would have no effect on the author's
claim because it does not involve evolutionary theory**."* Key D extends the arrow: *"All human
decisions are determined by the brain which is a byproduct of biological evolution."* Note the key
contains "All" — see §5.

**Claims.** The framework you run is **the author's**, and it may be one you think is wrong. Denies
that the best answer is the most defensible response — a competent modern reading issued from the
framework the author spent five paragraphs attacking is a distractor by construction.

**The trap it attracts.** R9 (true but inert) and framework-incongruence — a sensible response from
the *rejected* framework.

**Predicts.** Write the author's principle as one conditional first; each option is then a yes/no
test. **"The single change that would most weaken" means: name the arrow, then break that arrow.**

---

#### E · MAIN IDEA / CENTRAL THESIS
FL1: Q86, Q98 · broke: **trap (R3 / R8)**

**What is really being asked.** The synthesis. AAMC builds these so the thesis is **distributed** —
partly at the top, completed at the bottom — so no single sentence is liftable. A lift is a
distractor.

**Where the answer lives.** First paragraph plus last paragraph, combined. AAMC:
*"The beginning and ending of passages are two specific sections where the author often provides
important information about the general theme, message, or purpose."*

**Concrete.** *Deconstructionism*, Q2. Option A — "The true meaning of texts can never be decided" —
is the most prominent idea in the passage, stated three times, and belongs to the position the author
is destroying (R5+R8). Option B — "most literary criticism is now deconstructionism" — is a scope
overreach he never states (R6). Key D appears only in ¶6–7: writing is *"an existential
act,"* literature must be honored *"as a mode of radical discovery."*

**Claims.** The thesis is **distributed** and therefore not liftable from any one sentence. Denies
*the topic sentence is the main idea* — and denies that the idea you remember most clearly is the
author's, since the opponent's view got explained first and at length.

**The trap it attracts.** R8 (the setup, repeated most) and R3 (the concession).

**Predicts.** State the thesis as **"X, but really Y"** before looking: distractors are X, the key
is Y. A main-idea option with no adversary in it is almost never the key.

---

#### F · IRONY / RELATIONSHIP
FL1: Q112 · *"the passage describes an irony, namely that"* · broke: **reasoning**

**What is really being asked.** A **two-term structure with a reversal in it**: an expectation and
its violation, a means that defeats its end, an actor producing the opposite of the intent.

**Where the answer lives.** At a contrastive hinge — *yet, however, but, contrary to, despite,
astonishingly, ostensibly*. AAMC edits these in.

**Concrete — three, so the shape generalizes:**
- *Puritan society*: the townspeople *"had expected to behold her dimmed and obscured by a
  disastrous cloud, were astonished to perceive how her beauty shone out."* Expectation → violation,
  marked by "astonished."
- *Puritan society*, Q2: *"with a burning blush, **and yet** a haughty smile."* Shame and pride in
  one clause, joined by "yet." The item asks which image does **not** convey dignity: the left half
  of the "yet."
- *Deconstructionism*, ¶4: deconstruction *"presented itself as a supra-ideological mode of analysis,
  exposing the ideological aberrations of others while seemingly possessing none itself."* The method
  that unmasks ideology exempts itself — built from one "while."

**Claims.** Irony is a **two-term structure with a sign flip**. Denies that an accurate statement of
either pole alone can be the answer; an irony option with no opposition inside it is wrong before
you check the passage.

**The trap it attracts.** R2 — an option naming one term correctly and dropping the tension.

**Predicts.** The key contains **both poles**: scan for the option with two clauses pointing opposite
directions and check the passage supplies both.

---

#### G · ALTERNATIVE EXPLANATION
FL1: Q78, Q86 · *"could alternatively be explained as indicating"* · broke: **reasoning**

**What is really being asked.** Keep the **observation**, replace the **explanation**. An option that
changes the finding is out immediately.

**Where the answer lives.** Wherever the passage entertains a rival account — CARS passages are
selected for having one.

**Concrete.** *Designing courthouses* is built out of this. The author states a finding (discomfort
with the modern building only among familiar participants), then runs the move twice —
*"It is possible that photographs reduced the actual impact … **Another possibility** … those with
prior experience may have been exposed to the building from multiple angles."* — and again at the
end: mood-as-mediator versus *"another and more plausible possibility"*, activated associations. Q2
asks why he rejects the first; the answer is one sentence of disconfirming data:
*"building type affected perceived likelihood of conviction also for those participants who showed no
enhanced discomfort."*

**Claims.** The **observation is fixed**; only the mechanism attached to it moves. Denies that a
rival account may revise the finding — an option that alters the datum is not an alternative
explanation of it, it is a different datum.

**The trap it attracts.** R9 and R12 — options swapping the *finding* rather than the *explanation*,
or offering a mechanism the passage never put in play.

**Predicts.** Split the target sentence into `[observation] because [mechanism]` before reading
options: the key preserves the left bracket exactly and substitutes only the right.

---

**Discriminators**

- **Function vs Evidence** — Function: *why is this here?* Evidence: *what holds this up?* Function looks downstream; evidence looks underneath.
- **Inference vs Apply** — Inference: one step, no new material. Apply: the stem hands you new material and you run his framework on it.
- **Main idea vs Function** — Main idea: what the whole passage is for. Function: what one unit is for. Same question, different span — and the distractor for each is the other one's key.
- **Weaken vs Alternative explanation** — Weaken: break the arrow. Alternative: keep the observation, swap the arrow's source.
- **Irony vs Relationship** — Irony requires a *sign flip*. A relationship item without opposition is not irony, and an irony option without two poles is not the key.

**Compression** — the one axis is **how far from the passage the answer sits.**

| archetype | evidence span |
|---|---|
| Inference | one sentence + neighbors |
| Irony | one contrastive hinge |
| Function | the cited unit **+ a claim in another paragraph** |
| Evidence/support | two sentences and the link between them |
| Alternative explanation | one observation + two candidate mechanisms |
| Main idea | opening ∪ closing |
| Apply | the whole framework **× material not in the passage** |

---


## 3 · THE OWNERSHIP SYSTEM

The right tool for the R3/R5 family. It was not running from passage 1.

#### The three tags

At **each paragraph break**, one word in the margin. Not a summary — an owner.

| tag | means | markers |
|---|---|---|
| **HIS** | the author is committed to this | unmarked declarative, evaluative adverbs, "the point that needs to be reaffirmed," "more plausibly" |
| **THEIRS** | someone else holds it; the author is reporting | "Scholars have long treated," "X argued," direct quotation, "it is commonly held" |
| **GIVEN** | setup, data, definition, history — owned by nobody in the dispute | narrative past tense, study descriptions, glossed terms, numbers |

**The extension: THEIRS carries a sign.** `THEIRS−` rejected, `THEIRS+` endorsed. Without it,
"cited therefore wrong" becomes a rule: in *Does free will exist?* Dennett and Libet are cited and
**adopted** (the author's own position is Dennett's) while the quantum-fluctuation theorists are
called *"nonsense."* One character of ink prevents the whole error class.

#### The state sentence — with a mandatory "but"

After the last paragraph, before the first question: **one sentence, in your head, of the form
"X, but Y."**

The "but" is a forcing function — CARS passages are selected for holding two positions (AAMC:
*"multifaceted and focus on the relationships between ideas"*). No X → you never identified the
opponent. No Y → you have the opponent's view, not the author's: the R8/R3 miss on main-idea items.
X is what the distractors are built from; Y is the key.

#### Highlight only the left half of a concession

Concessions — *"There is something to this, **but** …"*, *"**Although** X, Y"*, *"X,
**and yet** Y"* — get marked on the **left** half only, stopping at the pivot word. The mark is a
**label**, not a memory aid: every marked span means
*"author-voiced, citable, true — and not the thesis."* R3 is AAMC's highest-frequency rejection
connective ("Although…" ×17).

- *Puritan society*, Q2, which image is **not** used to support dignity: *"with a
  **burning blush**, and yet a haughty smile."* The key is the left half of the "yet." AAMC:
  *"her 'blush' … is contrasted by the word 'yet' against her 'haughty smile.'"*
- *Censorship*, ¶2: *"**Censorship seems to be an answer** to the growing problem … **But** books are
  meant for exploration."* Highlight it whole and you have stored his position backwards.

---

#### Worked pass — *Deconstructionism and literature*

| ¶ | tag | content | why |
|---|---|---|---|
| 1 | **GIVEN** | what deconstructionism assumes; its Parisian origin, structuralist descent | definitional setup — but note the loaded verb *"prone to misread"* |
| 2 | **THEIRS−** | endless slippage of the subject; Derrida: *"America is deconstruction"* | quoted proponent, no endorsement |
| 3 | **GIVEN → HIS** | it filled the gap left by the new criticism; then *"Junior misreaders … like C.I.A. operatives, decoding false signals"* | history turns evaluative mid-paragraph; the simile is the author's |
| 4 | **THEIRS−** | *"As one academic critic exulted…"*; it presented itself as supra-ideological | reported boast; *"exulted"* marks the stance |
| 5 | **HIS** | demythologize, decanonize, dephallicize, **defame**; *"a few bare bones … and some tattered leather bindings"* | satire, therefore authorial |
| 6 | **HIS** | *"The point that needs to be reaffirmed is that writing is an existential act."* | explicit thesis marker |
| 7 | **HIS / THEIRS+** | we need an ambiance affirming creativity; **Sartre's** freedom-affirming existentialism | a cited figure the author **adopts** — the sign matters |

**State sentence.** *Deconstruction reads literature as undecidable social commentary and became the
academy's method — **but** writing is a moral and imaginative act, so criticism's first question is
creative merit.*

That closes all four items, four different archetypes:

| item | what the tags settle |
|---|---|
| **Q2, main idea** | A ("the true meaning of texts can never be decided") is X; D ("the most salient issue should be creative merit") is Y. **Keyed: D.** |
| **Q4, function of ¶3–5** | Key: *"denounce its triviality in order to strengthen the case for a contrasting vision."* B — *acknowledge its existentialist principles* — dies on the ¶7 tag, where Sartre is **THEIRS+** and set against deconstruction. AAMC: *"in fact he contrasts deconstructionism and existentialism in the final paragraph."* |
| **Q3, apply** | Run Y: artistic sensibility. A, evidence the play served Shakespeare's gender and class, is ¶4's **THEIRS−** content offered as his. |
| **Q1, inference** | *"America is deconstruction"* sits in the ¶2 THEIRS− block, so the item asks what Derrida's line **means**, not whether the author agrees. One step from the adjacent clause: *"historically dissociated construction of random meanings."* |

**Cost.** Seven tags ≈ 15 seconds, state sentence ≈ 10 — the half minute that makes the other nine
and a half work.

**Predicts.** An option restating a THEIRS− tag or a left-half highlight, on a stem asking for the
author's view, thesis, or purpose, is the near-miss. Cross it and move.

---

## 4 · THE DECAY

**82% → 59% → 58%.** The largest single loss in CARS and the only one that is pure procedure.

#### Read the shape before fixing it

A **step, not a slope** — 59 then 58, flat after the drop. Fatigue produces a slope, and his own
exam rules fatigue out: B/B went 74 → 84 → **86** and P/S 58 → 68 → **76**, later the same day. He
switched to skim-for-structure with 20–30 minutes left: *"it stopped the bleeding."* A late method
change plus a floor rather than a continued fall is a **regime change under clock debt** — time
overspent early, repaid at a worse exchange rate.

#### Where the points actually are

The back two-thirds is **35 of the 53 questions.** The first third is 18, already at 82%, and its
three remaining questions are the hardest three on the form.

| profile | correct |
|---|---|
| his FL1 (82 / 59 / 58) | 35 |
| flat 70% across | 37 |
| 82 first third, 70 after | 39 |
| 75 / 70 / 70 | 38 |

Each costs the first third nothing or almost nothing. **There is no scenario where more investment
in passages 1–3 pays** — the peak is bought with time the other 35 questions then do not have.

#### The clock rule

Nine passages, ninety minutes, countdown on screen. **At the end of passage N it must read
90 − 10N.** No arithmetic: glance, compare to a multiple of ten.

| after passage | clock reads |
|---|---|
| 1 | 80:00 |
| 2 | 70:00 |
| 3 | 60:00 |
| 4 | 50:00 |
| 5 | 40:00 |
| 6 | 30:00 |
| 7 | 20:00 |
| 8 | 10:00 |
| 9 | 0:00 |

**Debt is paid on the next passage, never the last one.** More than 2:00 behind at a checkpoint →
the *next* passage runs the compressed protocol. The rule that would have changed FL1: at 1:41 per
question against a 1:42 budget he never ran out of time — he carried a deficit forward and repaid it
in one lump near minute 60 — where his own account places the switch.

#### The per-passage procedure — same one from passage 1

| phase | budget | what happens |
|---|---|---|
| **Read** | 0:00 → 3:30 | One pass, tagging `HIS / THEIRS± / GIVEN` at each break and marking left-halves of concessions. **Never re-read a sentence** — AAMC edits passages to be self-sufficient and glosses its hard terms, so anything that didn't land is re-explained downstream. The most expensive habit available. |
| **Gate** | 3:30 → 3:45 | Say *"X, but Y."* A gate, not a formality — branch on it. |
| **Gate passed** | ~60 s / question | Full protocol, in the order given. No reordering; re-orientation costs more than it saves. |
| **Gate failed** | ~30 s / skeleton item | No skeleton → main-idea, function and apply items are two-minute coin flips. **Triage:** answer the locals (detail, meaning-in-context, one-step inference), 30 s each on the skeleton items, flag, move, bank the time. That set costs most of itself either way; the live question is whether it also costs the next passage. That was Q98–101. |
| **Commit** | ~45 s in | Down to two. Do not adjudicate: **the key is defensible in one step, the near-miss in three** — take the one-step option, flag, move. If both feel one-step you have not named the axis (R14). |
| **Flagged** | after passage 9 | Not revisited before then. Mid-section returns convert a small deficit into a regime change. |

#### The compressed protocol (his skim-for-structure, promoted to a standing tool)

Trigger: >2:00 behind at a checkpoint, or a first paragraph opaque on the first read.

- ¶1 in full · first and last sentence of each middle ¶ · last ¶ in full. Tag as you go.
- **State sentence still mandatory** — it is the whole point of the skim.
- Go to questions; return to the paragraph a stem points at and read that one properly.
- Budget 7:00 instead of 10:00. The 3:00 saved is the debt payment.

#### How to train it in seven days

The defect does not appear in passages 1–3, so **practicing passages 1–3 does not train it.**

1. **Never run a cold 3-passage block.** Run CARS *after* 30–45 minutes of other work, so the block's
   first passage is functionally passage 4 — where the data says he breaks.
2. **Score by thirds, every time.** First-third minus last-third accuracy. FL1 was **+24**; the
   target is single digits. Total percentage hides the fix, the gradient won't.

Volume: two full 9-passage timed sections in the seven days, plus daily 3-passage blocks under the
clock rule — the clock rule is what is being trained, not reading speed.

**Predicts.** If checkpoint discipline holds the gradient collapses first and total accuracy follows.
If accuracy rises but the gradient stays at +20, timing was not the mechanism and the read itself is
the next thing to test.

---

## 5 · WHAT TO STOP USING

#### Stop counting words

He learned it from a practice bank where **72% of keys were the longest option** against 25% by
chance — a 47-point signal. Rational there; also the bank teaching him a property of *itself*.

**AAMC does not have that property.** Over all 66 items in `CARS-AAMC-SETS.md`:

| | AAMC/Khan corpus (n=66) | chance | his old bank |
|---|---:|---:|---:|
| key is the **longest** option | **33%** | 25% | **72%** |
| key is the **shortest** option | **24%** | 25% | — |

Eight points over chance, inside the noise, worthless as a tiebreaker. Length is no accident on AAMC
material: NBME's item-writing rules, which AAMC's writers work inside, require options to be
*"homogeneous"* and name length asymmetry as a construct-irrelevant flaw to be removed in review.
AAMC length-balances on purpose.

**The cost is not neutral.** A heuristic with a 47-point signal in training and an 8-point signal on
the exam fires with training-level confidence on exam-level noise, hardest where he can least resist
it: a 50/50, late in the section. That is the R14 slot. **Delete it.**

#### Three more heuristics that are anti-correlated on AAMC material

Same corpus, same 66 items (264 options):

| | keys | distractors |
|---|---:|---:|
| contains an absolute (*all, every, always, never, only, must, cannot*) | **9%** | 5% |
| contains a hedge (*may, might, some, often, likely, suggests*) | **3%** | 7% |

Six occurrences versus nine — the honest reading is **"no usable signal,"** not
"reverse the rule." It still kills two heuristics outright — and a third dies on separate
evidence:

| heuristic | why it dies |
|---|---|
| **"Eliminate anything extreme."** | AAMC deliberately keys absolutes when the passage itself states one, precisely so this stops being a content-free winning strategy; the mirror trap, the *too-weak* distractor, farms examinees who select on safety, and under-describing what the author committed to is wrong for the same reason over-describing it is. **The modality is judged against the passage's own hedge, never in the abstract.** *Censorship* Q2 keys "general **disapproval**" over "cautious support" and "staunch neutrality" — the strong option wins because the author is strong. |
| **"The safe, hedged option is usually right."** | 3% vs 7% says the opposite here. Hedging is how the too-weak distractor is manufactured. |
| **"A cited view is never the author's."** | *Does free will exist?* cites Dennett, Libet, Wegner and the quantum theorists; the author's own thesis **is Dennett's**. *Deconstructionism* ends by endorsing Sartre. Attribution needs a sign (§3), not a rule. |

#### Stop defaulting to B

FL1: accuracy **81.7% when the key was B, 66.7% when it wasn't** — a 15-point gap, replicating the
same gap in his own bank (73% vs 63%). This form ran B-heavy at 30.9%, so the default paid. AAMC/Khan
key positions run **A 18 · B 15 · C 14 · D 19**: B is not modal, and there is no base rate to
exploit. When wrong on FL1 he over-picked C — 20 of the 65 misses he actually answered (66 missed, minus the Q39
blank), 31% — a position habit misfiring.

#### Stop asking "is this true?"

The whole of §1: zero of 198 distractors rejected for being false about the world; **textual
warrant** is the predicate. Costliest version — the true-and-informed option on a topic he knows.

#### What replaces all of it

One question, asked in this order:

1. **Where is the sentence?** No sentence → dead (R1).
2. **Does it answer *this* stem?** True but non-responsive → dead (R2, R3).
3. **Whose is it?** Tagged THEIRS− or a left-half → dead (R5, R3).
4. **Same quantity, same connective, same category?** (R6, R7, R12).
5. **Two survivors → name the axis** — responsiveness, scope, strength, attribution, relation — and
   take the option defensible in **one move**.

Nothing in that list looks at the option's shape. That is the point.

---

## EXAM-DAY CARD

**Clock.** End of passage N → clock reads 90 − 10N. Over by 2:00 → next passage compressed. Debt is
never deferred to the end.

**Read (3:30).** One pass, no re-reading a sentence. Tag each ¶: `HIS / THEIRS+ / THEIRS− / GIVEN`.
Highlight left-halves of concessions only.

**Gate (0:15).** *"X, but Y."* No sentence → triage the set: locals only, 30 s each on the skeleton
items, flag, bank the time.

**Per question (60 s).** Read the stem as a demand, not a topic. Anchor → responsive → owner →
quantity/connective/category. Two survivors: name the axis, take the one-move option, flag, go.

**Never.** Count words. Eliminate on "always." Prefer the hedge. Default to B. Ask whether it's true.
Re-read during the read. Return to a flagged item before passage 9 is done.

**The sentence.** *The key is the option you can defend in one move. The near-miss is the one you can
defend in three.*

---

# BIOLOGY / BIOCHEMISTRY

## CONCEPTS — Bio/Biochem

FL1 B/B: **128, 84th percentile, 48/59.** Skill 1 (knowledge) 91%. Skill 2 (reasoning) 74%.
Strongest section — a patch, not a rebuild. Eleven missed questions → 21 concepts, eight
clusters, then stop.

---

### Before the clusters: the negative stem

Q129 ("which does **NOT** measure...") and Q168 ("which is **LEAST** likely...").
**56% on negative stems vs 71% across the whole exam** (B/B itself was 81.4%) — procedural, not conceptual. A negative stem is four
true/false questions in one question's clothing, and read normally it hands you three attractive
right answers.

**The procedure. Scratch paper, before reading any option.**

1. **Find the negation word.** NOT, EXCEPT, LEAST, ALL BUT. Circle it.
2. **Rewrite the stem positive.** "Which does NOT measure Na⁺/K⁺ ATPase activity" becomes
   *"Three of these measure Na⁺/K⁺ ATPase activity. Which one fails?"*
3. **Mark each option T or F against the positive question.** Not better/worse. Binary.
4. **Pick the F.** One F, three Ts. Two Fs → you misread the positive form. Zero Fs → you're
   grading on quality, not truth.
5. **Expect the pull.** The three wrong answers are *true statements*. That feeling is the trap
   firing, not a signal. On LEAST stems the most obviously true option is guaranteed wrong.

**Budget.** Four evaluations, not one. ~2:00, not 1:33.

---

### Cluster 1 — Central dogma and gene expression
FL1: Q113, Q120, Q135

**The shared cell.** One **vascular smooth muscle cell** in an arteriole wall: transcribes
*AGTR1*, splices, translates the AT1 receptor, membranes it, and in Cluster 5 signals through it.

#### What survives into a mature mRNA
FL1: Q120 · CC2A · Skill 2 · broke: reasoning — "contains a sequence coding for" was read as "contains"

**Structure.** DNA (promoter, enhancers, exons, introns) → pre-mRNA (5′ cap added, introns
removed by the **spliceosome**, poly-A tail added) → mature mRNA = cap + 5′UTR + start codon +
**exonic coding sequence** + stop codon + 3′UTR + poly-A → protein.

**Concrete.** snRNPs cut each intron from the *AGTR1* pre-mRNA at its GU...AG boundaries and
ligate the exons. What exits the pore is shorter than the gene, carries a cap nothing templated
and ~200 A's no base specified, plus untranslated ends. The ribosome reads AUG to stop.

**Claims.** "Codes for" is about the **open reading frame**: the mRNA *contains* cap, UTRs, poly-A
but *codes for* only start-to-stop. Encoded, being amino acids: transmembrane domains, signal
peptides, leader sequences cleaved off later. Not encoded: sugars (N-/O-glycosylation), phosphate,
lipid anchors, bound metals, prosthetic groups. Denies "the mRNA is a copy of the gene" — introns,
promoters, enhancers stay behind.

**Predicts.** *Made of amino acids?* Yes → encoded, even if cleaved off later. No → not encoded,
however essential. *Between start and stop?* Present-in but not coding-for is the trap.

#### A transcription factor turns on a set, not a gene
FL1: Q135 · CC1B · Skill 2 · broke: reasoning — predicted one gene's product instead of a co-regulated group

**Structure.** Signal → **transcription factor** activated (phosphorylated, ligand-bound, or
released from an inhibitor) → enters nucleus → binds a **response element** in the
enhancer/promoter of *every gene carrying it* → all transcribed together.

**Concrete.** Sustained angiotensin II; one TF goes nuclear. It doesn't find "the hypertrophy
gene" — it finds its sequence in front of a contractile protein gene, a growth factor gene, a
matrix gene, and one unrelated to any of them. All four rise together. A liver cell turns on a
different list: different chromatin open.

**Claims.** Co-regulation is by **shared sequence**, not shared function — induced genes need not
share a pathway, a phenotype, or a chromosomal neighborhood. Denies "genes induced by stimulus X
are the X-response machinery." Second: the same TF in two cell types gives two lists, because
accessibility (chromatin state, methylation) gates which copies are reachable.

**Predicts.** Stimulus activates a TF → predict *genes sharing a promoter element, functionally
heterogeneous, cell-type-dependent.* "The induced genes all participate in [one process]" is an
overclaim unless the passage showed it; "they share a regulatory sequence" is usually right.

#### Describing an allele from a figure without overclaiming
FL1: Q113 · CC1B · Skill 4 · broke: data reasoning — stated more than the figure showed

**Structure.** Read axes and units → name what's compared → say the trend in your own words →
*then* read options → eliminate anything asserting what the figure didn't measure.

**Concrete.** The figure gives *HSP110* allele status across tumors: some wild-type, some the **E9
allele** (exon-9-skipped, from instability in the intron 8 repeat wrecking the splice signal —
Cluster 2 makes this). Bars show frequency or association with a tumor class. Nothing showed
function, causation, or outcome unless a panel did.

**Claims.** "Best describes" is scored against **the data, not the biology**. Four ways an option
overruns its evidence: reverses direction; inflates magnitude ("abolishes" for a partial drop);
asserts mechanism or causation from association; generalizes to a group, tissue, or timepoint
never included. Denies that the best answer is the most biologically true statement.

**Predicts.** *Best describes* + data → the trap is a correct-sounding mechanistic claim. Pick
the flattest option that says only what the axes say, even though it feels like it isn't
answering.

**Discriminators**
- Contains vs codes for — *is the sequence between the start and stop codon?*
- Exon vs coding sequence — *UTRs are exonic and non-coding; is every exon translated?* No.
- Encoded vs post-translational — *is it made of amino acids?*
- Best describes (data) vs is true (biology) — *did this figure measure that?*

**Compression — where each feature drops out of the pipeline**

| Feature | Last stage it exists in |
|---|---|
| Promoter, enhancer | DNA only |
| Intron | Pre-mRNA |
| 5′ cap, poly-A tail | Mature mRNA (never in DNA) |
| 5′/3′ UTR | Mature mRNA (never in protein) |
| Signal peptide | Nascent protein (cleaved before the mature protein) |
| Transmembrane domain | Mature protein — encoded |
| Glycan, phosphate, lipid anchor | Mature protein — **not** encoded |

---

### Cluster 2 — DNA repair and genome instability
FL1: Q115

**The shared cell.** One **colon crypt stem cell**, dividing every few days for decades — the
lineage that produced the tumors in the Q113 figure.

#### Mismatch repair — the proofreader's proofreader
FL1: Q115 · CC1C · Skill 2 · broke: knowledge — MMR's substrate and the strand-discrimination step

**Structure.** Polymerase inserts a wrong base or slips on a repeat → **MutSα** (MSH2+MSH6)
binds a base-base mismatch, **MutSβ** (MSH2+MSH3) binds a larger insertion/deletion loop →
**MutLα** (MLH1+PMS2) recruited, nicks the **new** strand → exonuclease chews back past the
error → pol δ resynthesizes → ligase seals.

**Concrete.** Pol δ runs onto seventeen consecutive A's; the strands re-anneal out of register and
the polymerase continues one A short, leaving a single unpaired bulge. Nothing is chemically wrong
— every base is a normal A or T. MutSβ finds the bulge by shape, MutLα cuts the strand with a free
end nearby.

**Claims.** MMR's substrate is **correctly-structured DNA in the wrong pairing** — normal bases,
wrong partner, or right bases in the wrong register. Not damage repair. Its hard problem is
knowing **which strand is wrong**, solved by cutting the one with a nearby nick or end. It acts
*after* the polymerase moved on, catching what 3′→5′ proofreading let through, and raising fidelity a further ~100–1000×.
Denies "repair enzymes recognize damaged bases."

**Predicts.** Lose MMR and errors proofreading missed become permanent: a **hypermutator**
phenotype of point mutations and, far more distinctively, **length changes at repetitive
sequences** — where slippage happens, and slippage is what MutSβ caught.

#### Microsatellite instability — the readout, not the lesion
FL1: Q115 · CC1C · Skill 2 · broke: reasoning — treated MSI as a cause rather than a marker

**Structure.** MMR lost → slippage at short tandem repeats goes unrepaired → each locus drifts
to a new length independently in each clone → PCR a panel of those loci in tumor and matched
normal → tumor lanes show bands the normal lanes don't. That band shift **is** microsatellite
instability.

**Concrete.** A **microsatellite** is a short tandem repeat — (A)₁₇, (CA)₂₀ — mostly noncoding. In
the MMR-dead clone one (A)₁₇ tract is 15 in one cell, 19 in another, 17 in a third: amplify from
the tumor and you get a ladder, from normal colon one clean band. The chromosomes look ordinary.

**Claims.** MSI is a **phenotype that reports MMR loss**; it does not cause MMR loss and is not a
synonym for genomic instability in general. Instability of **length at repeats** — hence a
repeat-length assay, hence a karyotype won't show it. Denies conflation with **chromosomal
instability** — aneuploidy, gross rearrangement, the other route to colorectal cancer. MSI tumors
are near-diploid, CIN tumors MMR-competent.

**Evidence.** Repeats inside genes frameshift when their length changes — an (A)₁₀ tract in
*TGFBR2*, a (G)₈ in *BAX*: premature stop, protein lost. A repeat in an **intron** near a splice
site frameshifts nothing; it destroys the splice signal and the exon is skipped — the *HSP110* E9
allele from Q113.

**Predicts.** "Tumor shows MSI" → MMR gene lost (MLH1 silenced by promoter methylation, or
germline mutation in Lynch syndrome), very high mutation burden, frameshifts at coding repeats,
near-normal chromosome number, abnormal splice products where the repeat was intronic. "MMR
intact" → MSI absent, however mutated the tumor is.

**Discriminators**
- Proofreading vs MMR — *has the polymerase moved on yet?*
- MMR vs BER/NER — *is the base chemically altered, or chemically fine and wrongly paired?*
  MMR takes normal bases; BER takes one damaged base (deaminated C, oxidized G); NER takes a
  bulky helix-distorting lesion (thymine dimer, adduct).
- MSI vs CIN — *is the instability in repeat length or in chromosome number?*
- Germline vs somatic MMR loss — *is the second hit inherited or acquired?* Lynch syndrome
  inherits one broken allele in every cell; the tumor arises where the second copy is lost.

**Compression — one axis: what kind of lesion**

| Lesion | System | Signature of losing it |
|---|---|---|
| Wrong base, caught instantly | Pol 3′→5′ proofreading | Elevated point mutation rate |
| Wrong base / slipped loop, after the fork passed | **Mismatch repair** | **MSI**, hypermutation, frameshifts at repeats |
| One chemically altered base | Base excision repair | Transition mutations from deamination/oxidation |
| Bulky helix-distorting adduct | Nucleotide excision repair | UV sensitivity (xeroderma pigmentosum) |
| Double-strand break | HR (BRCA1/2) or NHEJ | Translocations, gross rearrangement |

---

### Cluster 3 — Membrane transport: structure predicts route
FL1: Q133

**The shared cell.** One **proximal tubule epithelial cell**: apical (urine-facing) on top,
basolateral (blood-facing) below, tight junctions between neighbors. It carries Cluster 4 and
reappears in Cluster 7.

#### Reading a molecule's structure to pick its route
FL1: Q133 · CC2A · Skill 2 · broke: reasoning — chose a transporter for a molecule too large/charged for one

**Structure.** Three properties, in order: **size → charge → polarity.** Small + nonpolar +
uncharged → straight through the bilayer, no protein. Small + polar + uncharged → slow simple
diffusion, sometimes a channel. Charged, or large and polar → protein required; passive if
downhill, active if uphill. Macromolecule or particle → vesicle.

**Concrete.** Four things hit the apical membrane at once. **Cortisol**, small nonpolar steroid,
dissolves into the acyl core and is out the other side — no transporter, no saturation. **Na⁺**,
tiny but charged, can't touch that greasy interior. **Glucose**, big and hydroxyl-studded, needs
**SGLT2** — and only if Na⁺ comes along. **Albumin**, 66 kDa, fits nothing; a clathrin-coated pit
swallows it whole.

**Claims.** Permeability is whether the molecule can shed its water shell and enter a hydrocarbon
interior: charge is nearly disqualifying whatever the size, size disqualifies at the top end
whatever the chemistry. Denies "lipid-soluble things need special transporters" — they need none.
Denies "big charged molecules use pumps" — past a size it becomes **endocytosis**. Denies "a
highly cationic peptide will use an ion channel" — channels are ion-selective filters, not
size-blind holes.

**Predicts.** Count charges, estimate size, note hydrophobic stretches. **Cationic or amphipathic
peptide, protein, nucleic acid, lipoprotein particle** → **endocytosis**, and with a specific
cell-surface partner, **receptor-mediated endocytosis**. **Small uncharged lipophile** → simple
diffusion, rate linear in concentration forever, no Vmax.

#### Facilitated diffusion is passive; secondary active transport is not
FL1: Q133 · CC2A · broke: category confusion — "carrier protein" read as "active"

**Structure.** **Passive**: down the electrochemical gradient, no metabolic energy — simple
diffusion, **channels** (gated pore, no conformational cycle, fast, ion-selective), **carriers**
(bind, occlude, flip, release — slower, saturable, Vmax). **Primary active**: the transporter
hydrolyzes ATP. **Secondary active**: it spends a pre-existing ion gradient, touching no ATP.

**Concrete.** One glucose molecule's trip. Apically **SGLT2** carries it *uphill* — glucose is
already more concentrated inside than in the filtrate — powered entirely by Na⁺ falling down its
own gradient, no ATP bound. Basolaterally **GLUT2** lets it slide *downhill* into blood:
saturable, conformation-changing, completely passive. Two carriers, one active, one not.

**Claims.** "Uses a protein" and "uses energy" are independent axes: GLUT runs backwards the
moment the gradient reverses, SGLT never does while the Na⁺ gradient holds. Denies "carrier
protein = active transport." Denies "active transport = ATP binds this protein." Denies
"facilitated diffusion can concentrate a solute" — it equilibrates. Denies that ions move only
down their concentration gradient: the force is **electrochemical**, so a cation can climb its
concentration gradient passively if the voltage pulls.

**Predicts.** Poison ATP and secondary active transport keeps running — briefly, until the Na⁺
gradient it lives on decays. Primary stops immediately, secondary fades: that delay is the
fingerprint. "Accumulates against its gradient without ATP hydrolysis by the transporter" →
predict a coupled ion.

**Discriminators**
- Channel vs carrier — *does the protein undergo a conformational cycle per solute?* Carrier
  yes (saturable, Vmax); channel no (fast, still selective, still saturating at very high flux
  but treated as non-saturable).
- Facilitated vs active — *would it run in reverse if the gradient reversed?* Yes → passive.
- Primary vs secondary active — *does ATP bind this transporter?*
- Transport vs endocytosis — *is the cargo bigger than a protein channel's pore?*

**Compression — one axis: where the energy comes from**

| Route | Energy source | Saturable? | Can concentrate? |
|---|---|---|---|
| Simple diffusion | Gradient | No | No |
| Channel | Electrochemical gradient | Effectively no | No |
| Facilitated (carrier) | Gradient | Yes | No |
| Secondary active (SGLT, NCX) | Another ion's gradient | Yes | Yes |
| Primary active (Na⁺/K⁺ ATPase) | ATP, directly | Yes | Yes |
| Endocytosis | ATP, via vesicle machinery | — | Yes |

---

### Cluster 4 — The Na⁺/K⁺ ATPase and how activity is measured
FL1: Q129

#### The pump: stoichiometry, charge, and what it pays for
FL1: Q129 · CC1D · Skill 3 · broke: knowledge — what the pump does per cycle

**Structure.** Per cycle: **3 Na⁺ out, 2 K⁺ in, 1 ATP hydrolyzed.** A P-type ATPase — it
phosphorylates its own aspartate residue, changing conformation, then dephosphorylates to reset.
Net **+1 charge exported per cycle → electrogenic.**

**Concrete.** On the basolateral face the pump holds intracellular Na⁺ near 10 mM against 145 mM
outside. That gradient is the cell's stored energy: what SGLT2 spends to pull glucose in uphill,
the Na⁺/H⁺ exchanger to move acid out, the Na⁺/Ca²⁺ exchanger to hold cytosolic Ca²⁺ at 100 nM,
NKCC2 in the thick ascending limb. Add ouabain: each transporter stalls in sequence, water follows
Na⁺ in, the cell swells.

**Claims.** Direct job: a gradient. Economic job: the battery for secondary active transport
across the whole cell. Electrogenic, so worth a few millivolts of resting potential — but it
denies that the pump *sets* the resting potential, which is set mainly by K⁺ leak channels and the
K⁺ gradient. The pump's role there is **indirect**.

**Predicts.** Inhibit it and predict, in order: immediate few-mV depolarization → within minutes,
failure of every Na⁺-coupled cotransporter → rising intracellular Na⁺ and Ca²⁺ as NCX stalls,
which is how digoxin increases cardiac contractility → cell swelling, and slow further
depolarization as the gradients decay.

#### Measuring activity vs measuring abundance — the NOT question
FL1: Q129 · CC1D · Skill 3 · **negative stem** · broke: trap — picked a plausible assay without asking what it detects

**Structure.** An assay measures **activity** only if what it detects is produced **per catalytic
cycle** — ATP consumed (Pi released), ions moved, or charge moved. Run any of those three **±
ouabain**; the ouabain-sensitive component *is* the pump. (Tracer flux = ²²Na⁺ efflux or ⁸⁶Rb⁺
uptake, Rb⁺ substituting for K⁺.)

**Concrete.** Four tubes: Pi release ± ouabain, ⁸⁶Rb⁺ uptake ± ouabain, patch-clamp current that
vanishes with ouabain — and a Western blot for the α subunit giving a dark band, from cells that
sat in ouabain an hour with the pump frozen. The blot counted protein: same answer if every pump
were dead.

**Claims.** Abundance is not activity. Anything counting protein or transcript — Western blot,
immunofluorescence, ELISA, qPCR — reports how much machinery exists, not whether it turns. Ligand
*binding* counts sites, not cycles. A downstream steady state with many other causes ([Na⁺]ᵢ,
resting Vm) is confounded. Denies that a measurement "about the pump" measures "the pump's
activity."

**Predicts.** **Would this number change if every pump were present but frozen?** Unchanged →
abundance → that is the NOT/LEAST answer. Collapses → activity. On any "which does not measure
activity" item, the answer is the protein-quantification option.

**Discriminators**
- Activity vs abundance — *would the number change if the protein were present but frozen?*
- Direct vs downstream readout — *does anything other than this pump also produce this signal?*
- Na⁺/K⁺ ATPase vs Ca²⁺ ATPase vs H⁺/K⁺ ATPase — all P-type; *which ions, and is it
  electrogenic?* Of these three, only Na⁺/K⁺ moves net charge (3 out, 2 in). H⁺/K⁺
  (gastric parietal cell) is 1:1 and electroneutral. *(PMCA and SERCA are mildly electrogenic in
  full biochemistry; the AAMC-level contrast is Na⁺/K⁺ against the electroneutral H⁺/K⁺.)*

**Compression — one axis: what the assay actually detects**

| Assay | Detects | Measures activity? |
|---|---|---|
| Pi release ± ouabain | ATP hydrolyzed per cycle | Yes |
| ²²Na⁺ efflux / ⁸⁶Rb⁺ uptake | Ions moved per cycle | Yes |
| Ouabain-sensitive current | Net charge moved per cycle | Yes |
| Western blot / qPCR / immunostain | Protein or transcript present | **No — abundance** |
| Labeled-ouabain binding | Number of sites | **No — abundance** |
| Steady-state [Na⁺]ᵢ or resting Vm | Sum of every conductance and pump | **No — confounded** |

---

### Cluster 5 — Cell signaling and what "directly activates" means
FL1: Q134

**The shared cell.** Back to the **vascular smooth muscle cell** from Cluster 1, AT1 receptor now
in the membrane. Angiotensin II arrives.

#### The four receptor classes, sorted by what crosses the membrane
FL1: Q134 · CC1A · Skill 1 · broke: knowledge — the step order inside the cascade

**Structure.**
**GPCR** — 7 transmembrane passes → ligand binds → Gα swaps GDP for GTP → Gα-GTP separates
from Gβγ → effector. Gs → adenylyl cyclase ↑ → **cAMP** → PKA. Gi → adenylyl cyclase ↓.
Gq → phospholipase C → cleaves PIP₂ into **IP₃ + DAG** → IP₃ opens the ER Ca²⁺ channel;
DAG plus Ca²⁺ activates PKC.
**Receptor tyrosine kinase** — ligand → receptors dimerize → trans-autophosphorylation on
tyrosines → phosphotyrosines are docking sites → Ras/MAPK and PI3K/Akt.
**Ligand-gated ion channel** — ligand binds, pore opens, ions flow. Milliseconds. No second
messenger, no cascade.
**Intracellular receptor** — the ligand itself crosses the membrane (steroid, thyroid hormone,
vitamin D) → binds a cytoplasmic or nuclear receptor → chaperone released → dimer binds a
hormone response element → transcription. Hours.

**Concrete.** Angiotensin II — a peptide, therefore stuck outside — binds AT1, a **Gq**-coupled
GPCR. Gαq-GTP finds PLCβ; PLCβ cuts PIP₂ into IP₃ and DAG; IP₃ opens the sarcoplasmic reticulum's
Ca²⁺ channel; four Ca²⁺ bind **calmodulin**; Ca²⁺-calmodulin activates **myosin light chain
kinase**; MLCK phosphorylates the myosin regulatory light chain. Meanwhile cortisol has walked
through the membrane and is changing transcription.

**Claims.** Class follows ligand chemistry: **lipophilic → intracellular receptor; hydrophilic or
peptide → surface receptor**, and speed follows class because only the nuclear receptor has to
make protein. Denies that potency comes from the hormone — the cascade's **amplification** does:
one receptor activates many G proteins, one cyclase makes many cAMP, one PKA phosphorylates many
substrates.

**Predicts.** Ligand structure → receptor location and response latency. Slow response requiring
new protein → nuclear receptor, blocked by a transcription inhibitor. Millisecond response →
ligand-gated channel, untouched by one.

#### "Directly activates" is exactly one step
FL1: Q134 · CC1A · Skill 1 · broke: trap — named the upstream initiator instead of the immediate activator

**Structure.** In A → B → C → D, what *directly* activates C is **B**. Write the chain, find the
named target, take **one** step back, stop.

**Concrete.** What directly activates MLCK? Not angiotensin II — that activates AT1. Not IP₃ —
that opens an ER channel. Not Ca²⁺ alone — Ca²⁺ binds calmodulin. **Ca²⁺-calmodulin** does. Four
molecules answer loosely; one answers "directly."

**Claims.** "Directly" means physical contact or covalent modification **by that molecule**.
Denies the loose causal reading in which everything upstream counts. Two complications AAMC uses:
(1) **activation by relief of inhibition** — cAMP binds PKA's regulatory subunits and releases the
catalytic ones, still direct; (2) the famous molecule is a distractor — epinephrine, insulin,
angiotensin II are almost never the direct activator of anything but their own receptor.

**Predicts.** On "what directly activates / immediately precedes / is the proximal stimulus for
X," predict the least famous molecule in the option set — the intermediate, not the hormone. The
distractor is the pathway's initiator.

**Evidence.** Termination mirrors activation and is tested the same way: Gα's own GTPase
hydrolyzes its GTP and shuts the pathway off; phosphodiesterase degrades cAMP; phosphatases
reverse the kinases. Caffeine inhibits PDE — cAMP stays up. Cholera toxin locks Gs GTP-bound —
cAMP never comes down, intestinal Cl⁻ and water secretion never stops.

**Discriminators**
- Gs vs Gi vs Gq — *cAMP up, cAMP down, or IP₃/DAG and Ca²⁺?*
- Second messenger vs effector enzyme — *is it small and diffusible (cAMP, IP₃, DAG, Ca²⁺) or
  is it the protein that makes it (adenylyl cyclase, PLC)?*
- Surface vs intracellular receptor — *can the ligand cross a lipid bilayer on its own?*
- Directly vs ultimately activates — *do these two molecules touch?*

**Compression — one axis: time to effect**

| Receptor class | Route | Latency |
|---|---|---|
| Ligand-gated ion channel | Ligand → pore | Milliseconds |
| GPCR | Ligand → G protein → second messenger → kinase | Seconds |
| Receptor tyrosine kinase | Ligand → dimerize → autophosphorylate → cascade | Seconds–minutes |
| Intracellular / nuclear | Ligand crosses membrane → TF → transcription → translation | Hours |

---

### Cluster 6 — The action potential
FL1: Q159

**The shared cell.** One **myelinated axon**, resting at −70 mV, taking a depolarizing input at
the axon hillock.

#### Which conductance is open when
FL1: Q159 · CC3A · Skill 2 · broke: reasoning — the direction and consequence of Na⁺ influx

**Structure.** Rest (−70): K⁺ leak open, Vm near E_K (−90), pulled up by a small Na⁺ leak.
**Threshold (−55): voltage-gated Na⁺ channels open**, Vm climbing toward E_Na (+60). Peak (≈+35):
Na⁺ channels **inactivate** — a second, separate gate swings shut — while slow voltage-gated K⁺
channels open, and K⁺ efflux repolarizes, then undershoots toward E_K.

**Concrete.** The hillock reaches −55. One voltage-gated Na⁺ channel opens; Na⁺ enters pushed by
*both* forces — 145 mM outside against 10 mM inside, and a negative interior pulling a cation in.
That depolarizes the patch, opening more Na⁺ channels: **positive feedback**, spike unstoppable.
Milliseconds later the inactivation gates close, the slow K⁺ channels are wide open, and the
membrane crashes down. This happens only at the **nodes of Ranvier**; between them current runs
passively under myelin, so the spike jumps.

**Claims.** Na⁺ influx causes **depolarization** — the interior becomes less negative, then
positive. It denies the two reversals AAMC offers: that Na⁺ entry hyperpolarizes (that is Cl⁻
entry or K⁺ exit), and that the Na⁺/K⁺ ATPase drives the upstroke (the pump moves Na⁺ *out*,
slowly). Repolarization is **K⁺ efflux, not Na⁺ efflux** — Na⁺ channels close by inactivating, not
by running backwards, and that gate is the refractory period: the impulse only travels forward.

**Predicts.** "Na⁺ conductance rises" → Vm moves **toward E_Na**; "K⁺ conductance rises" →
**toward E_K**. That one rule generates every phase without memorizing them. Block inactivation →
prolonged spike; block the voltage-gated K⁺ channel → slowed repolarization.

#### Almost no sodium actually moves
FL1: Q159 · CC3A · Skill 2 · broke: trap — chose a bulk-concentration consequence over a voltage consequence

**Structure.** The membrane is a capacitor: charging it through 100 mV takes an extraordinarily
small number of ions relative to the cytosol's stock. **Voltage** changes enormously,
**concentration** barely at all.

**Concrete.** Intracellular Na⁺ was 10 mM before the spike; after it, to any measurement you would
make, still 10 mM. Poison that axon's Na⁺/K⁺ ATPase with ouabain and it fires hundreds of normal
action potentials before accumulated leak degrades the gradients.

**Claims.** The action potential is an **electrical** event running on a chemical gradient it does
not appreciably spend. It denies "Na⁺ influx raises intracellular sodium concentration" as what
the influx *causes* — true by an immeasurable amount, not the mechanism. It denies "the pump
restores the gradient after each action potential": it maintains it over minutes and hours.

**Predicts.** An option offering a bulk-concentration change as the consequence of an ion current
is the distractor; the answer is a **membrane-potential** change. Blocking the pump does not
abolish the next action potential.

#### All-or-none: intensity is frequency, not amplitude
FL1: Q159 · CC3A · Skill 1

**Structure.** Above threshold every action potential in a given axon has the same amplitude and
shape. A stronger stimulus makes **more spikes per second** and recruits more axons.

**Concrete.** Press a finger lightly: one mechanoreceptor axon fires at 10 Hz. Press hard: the
same axon fires at 100 Hz — identical spikes, ten times as often — and neighboring
higher-threshold axons start too. The brain reads intensity off the rate and the count.

**Claims.** Amplitude carries no information; frequency and population do. It denies the graded
model. **Graded potentials** — EPSPs, receptor potentials, end-plate potentials — are the opposite
on both counts: amplitude *does* scale with stimulus, and they *decay* with distance. Action
potentials arrive at the terminal at full size.

**Predicts.** Conduction velocity rises with **axon diameter** (less axial resistance) and
**myelination** (saltatory conduction). Demyelinate an axon — multiple sclerosis — and predict
slowed or failed conduction, not smaller spikes.

**Discriminators**
- Depolarize vs hyperpolarize — *does the entering/leaving ion make the inside more positive?*
- Na⁺ channel closed vs inactivated — *can the next stimulus open it?* Closed yes,
  inactivated no, until Vm repolarizes.
- Repolarization vs hyperpolarization — *is Vm returning to rest, or below it?*
- Graded potential vs action potential — *does amplitude vary with stimulus strength?*
- Absolute vs relative refractory — *is any stimulus sufficient, or just a larger one?*

**Compression — one axis: which conductance dominates**

| Phase | Vm | Dominant conductance | Direction of drift |
|---|---|---|---|
| Rest | −70 | K⁺ leak | toward E_K (−90) |
| Threshold → upstroke | −55 → +35 | Voltage-gated Na⁺ | toward E_Na (+60) |
| Peak | +35 | Na⁺ inactivating, K⁺ opening | turning over |
| Repolarization | +35 → −70 | Voltage-gated K⁺ | toward E_K |
| Undershoot | < −70 | K⁺ still open | toward E_K |
| Return | −70 | Leak; gradients held by the pump | rest |

---

### Cluster 7 — Renal concentration
FL1: Q127

**The shared cell.** The **proximal tubule cell from Cluster 3** is one station. Follow one volume
of filtrate from Bowman's capsule to the papilla, on a day the person is dehydrated and ADH is
maximal.

#### The nephron by osmolarity, segment by segment
FL1: Q127 · CC3B · Skill 1 · broke: knowledge — which segment does what to tubular osmolarity

**Structure.** Bowman's 300 → PCT reabsorbs ~2/3 of the volume **isosmotically** → descending limb
water-permeable and solute-impermeable, concentrating to **~1200** at the bend → ascending limb
**water-impermeable**, pumping NaCl out, diluting to **~100** → collecting duct permeability set
by ADH: final urine **50 (no ADH) to 1200 (max ADH).**

**Concrete.** The filtrate loses two-thirds of its volume in the proximal tubule — Na⁺ pumped out
basolaterally, glucose and amino acids dragged by SGLT and relatives, water through aquaporin-1 —
and exits *just as concentrated as it went in*. Into a medulla saltier with depth: water pours out
of the descending limb until the fluid at the bend is as concentrated as anything in the body.
Round the corner the wall is watertight, NKCC2 hauls Na⁺, K⁺, and 2 Cl⁻ out, water cannot follow,
and the fluid dilutes going up. Back down the collecting duct, where ADH's **aquaporin-2** lets
water leave until the urine equilibrates with the papilla.

**Claims.** The **thick ascending limb is the diluting segment**, output hypotonic — around 100
mOsm — **in every state, ADH or no ADH**. The **collecting duct is the only segment whose water
permeability is regulated**. Denies the model in which "making concentrated urine" changes the
loop's behavior: the loop builds the same gradient either way. Denies "the proximal tubule
concentrates the filtrate" — it moves the most volume and changes osmolarity not at all.

**Predicts.** *Most concentrated tubular fluid* → the **bend of the loop in the inner medulla**
(and, at maximal ADH, the terminal collecting duct). *Most dilute* → the **early distal tubule**,
always. *Where concentrated and dilute urine diverge* → the **collecting duct**. *Most
concentrated interstitium* → the **inner medulla/papilla**.

#### Countercurrent multiplication vs countercurrent exchange
FL1: Q127 · CC3B · Skill 1 · broke: knowledge — attributed gradient creation to the wrong structure

**Structure.** The ascending limb can only make the interstitium ~200 mOsm saltier than the fluid
beside it — the **single effect**. Because the two limbs run antiparallel and fluid keeps
flowing, that modest sideways step repeats at every level and stacks along the corticomedullary
axis, **multiplying** into a 300→1200 gradient.

**Concrete.** The loop is a hairpin standing in a column. NKCC2 pushes salt sideways at every
level; the descending limb, permeable to water, loses water and delivers *saltier* fluid round the
bend, so the ascending limb has saltier fluid to pump from. Each turn drives salt deeper.
Alongside, the **vasa recta** dives in and loops out — down it picks up solute and loses water, up
it gives them back — leaving nearly isosmotic, carrying off water without rinsing the salt out.

**Claims.** The loop of Henle is a **multiplier**: it spends ATP (indirectly, through the Na⁺/K⁺
ATPase powering NKCC2) and *creates* the gradient. The vasa recta is an **exchanger**: entirely
passive, *preserving* a gradient it did not make. Denies the common substitution of one for the
other. Second: **urea contributes**, not just NaCl — ADH also inserts urea transporters in the
inner medullary collecting duct. Third: only long-looped **juxtamedullary nephrons** reach deep
enough.

**Predicts.** A loop diuretic blocks NKCC2 → the gradient collapses, the ascending limb can no
longer dilute, the collecting duct has nothing to concentrate against: predict a large volume of
urine close to isotonic. Raise medullary blood flow sharply → washout, impaired concentrating
ability, no transporter touched.

#### ADH moves water; aldosterone moves sodium
FL1: Q127 · CC3B · Skill 1

**Structure.** **ADH**: rising plasma osmolarity (hypothalamic osmoreceptors, ~1%) or large volume
loss (baroreceptors, ~10%) → posterior pituitary → V2 receptor on collecting duct principal cells
→ Gs → cAMP → PKA → **aquaporin-2 in the apical membrane** → free water reabsorbed.
**Aldosterone**: low blood pressure/volume via renin–angiotensin, or hyperkalemia → adrenal cortex
→ principal cells → more ENaC and more Na⁺/K⁺ ATPase → **Na⁺ in, K⁺ out**, water follows
osmotically.

**Concrete.** The dehydrated person's plasma osmolarity is 295. ADH is high, the collecting duct
is soaked in aquaporins, urine comes out at 1200, plasma osmolarity falls back toward 290.
Meanwhile angiotensin II — the peptide that contracted the smooth muscle cell in Cluster 5 — has
driven aldosterone release, and the same principal cells reclaim Na⁺ and dump K⁺.

**Claims.** ADH reabsorbs **water without solute**, so it lowers plasma osmolarity and
concentrates the urine. Aldosterone reabsorbs **Na⁺ with water following**, so it raises volume
and blood pressure while barely moving plasma osmolarity. Denies "ADH reabsorbs salt" and denies
"aldosterone concentrates the urine."

**Predicts.** No ADH (central diabetes insipidus, or an unresponsive V2 receptor in nephrogenic
DI) → enormous volumes of **dilute** urine (~50 mOsm) with **normal blood glucose** — the classic
contrast with diabetes mellitus in Cluster 8, where the urine is also copious but loaded with
glucose.

**Discriminators**
- Multiplier vs exchanger — *does it spend energy to build the gradient, or passively preserve
  one?* Loop of Henle builds; vasa recta preserves.
- Descending vs ascending limb — *is this wall permeable to water or to solute?* Never both.
- ADH vs aldosterone — *is the stimulus osmolarity, or volume/pressure and K⁺?*
- Concentrated vs dilute urine — *which single segment differs?* Only the collecting duct.

**Compression — one axis: osmolarity of tubular fluid (mOsm)**

| Location | Osmolarity | Why |
|---|---|---|
| Bowman's capsule | 300 | Filtrate = plasma minus protein |
| End of proximal tubule | **300** | Isosmotic reabsorption — volume falls, osmolarity doesn't |
| Bend of loop, inner medulla | **~1200** | Water out, solute stays: maximum |
| Early distal tubule | **~100** | Solute out, water can't follow: minimum, always |
| Final urine, no ADH | 50 | Collecting duct impermeable |
| Final urine, max ADH | 1200 | AQP2 inserted; equilibrates with papilla |

---

### Cluster 8 — Glucose physiology and diabetes
FL1: Q165, Q168

**The shared patients.** Two people in one clinic waiting room. **T1**, nineteen, thin, diagnosed
at eleven, insulin pump. **T2**, fifty-four, heavy, diagnosed last year, metformin. Both at blood
glucose 260 this morning. Both about to go for a run.

#### Insulin's job is GLUT4 translocation — and only some tissues care
FL1: Q165 · CC3B · Skill 2 · broke: knowledge — which tissues need insulin to take up glucose

**Structure.** Blood glucose ↑ → β-cell takes up glucose through GLUT2 → glycolysis → ATP/ADP
↑ → **K_ATP channel closes** → β cell depolarizes → voltage-gated Ca²⁺ channel opens → Ca²⁺
in → insulin granules exocytose. Insulin → **receptor tyrosine kinase** on muscle and adipose
→ IRS → PI3K → Akt → **GLUT4-containing vesicles fuse with the plasma membrane** → glucose
uptake rises.

**Concrete.** T2 eats lunch. Her β cells read glucose like a fuel gauge — GLUT2's high Km means
uptake tracks blood glucose rather than saturating — and release plenty of insulin. At her thigh
muscle the receptor dimerizes and phosphorylates itself, then the signal weakens between IRS and
Akt: few GLUT4 vesicles move. Her **brain**, **liver**, **red cells**, and **kidney tubules** take
glucose up as always — GLUT1, GLUT2, GLUT3.

**Claims.** Insulin controls glucose uptake in **muscle and adipose tissue** — the GLUT4 tissues —
and does not gate uptake in brain, liver, RBC, or renal tubule. Denies the model in which insulin
is the body's only glucose key; explains why the brain does not starve in diabetes and *does* fail
immediately in hypoglycemia. It is the **fed-state signal**: glycogen synthesis on, glycogenolysis
and gluconeogenesis off, lipogenesis on, **lipolysis off**, protein synthesis on.

**Predicts.** Remove insulin entirely → not just hyperglycemia but **unrestrained lipolysis** →
free fatty acids to the liver → **ketogenesis** → ketoacidosis. Leave a little, as in T2 →
hyperglycemia **without** ketosis, because even a small amount suppresses lipolysis.

#### Exercise recruits GLUT4 without insulin
FL1: Q165 · CC3B · Skill 2 · broke: reasoning — did not identify which defect exercise bypasses

**Structure.** Muscle contraction → cytosolic Ca²⁺ ↑ and AMP/ATP ratio ↑ → **AMPK** activated
→ GLUT4 translocation, by a pathway **parallel to and independent of** insulin/PI3K/Akt.

**Concrete.** T2 runs. Nothing repairs IRS or Akt, but her contracting quadriceps pulls GLUT4 to
the surface through AMPK anyway and glucose leaves her blood, still leaving for hours as the
muscle refills glycogen. T1 runs too — same AMPK recruitment, but with almost no insulin nothing
restrains his liver: glucagon, epinephrine, and cortisol drive hepatic output up, so whether his
glucose falls or rises depends on how much insulin is circulating.

**Claims.** Exercise lowers glucose **by a route that does not require insulin signaling** — why
it works where insulin signaling is the broken part. In **Type 2** the defect is downstream of the
receptor, exercise bypasses it, and the effect compounds chronically because it also reduces the
adiposity and ectopic lipid driving the resistance. In **Type 1** there is no insulin at all and
the acute response is **unpredictable**. Denies "exercise lowers glucose equally in both types"
and denies "exercise works by increasing insulin secretion."

**Predicts.** "Which type of diabetes would regular exercise most likely reduce blood glucose in"
→ **Type 2**, whose broken step exercise routes around and whose underlying pathology exercise
partly reverses. Exercise does nothing to the autoimmune β-cell destruction in Type 1.

#### The symptoms, and the two things they all trace to
FL1: Q168 · CC1D · Skill 2 · **negative stem** · broke: trap — one true-sounding option was the opposite of the mechanism

**Structure.** Two generators, and every real symptom comes from one.
**(a) Glucose in the tubule.** Blood glucose exceeds the renal transport maximum (~180–200
mg/dL) → SGLT2 saturates → glucose stays in the filtrate → holds water there osmotically →
**osmotic diuresis** → polyuria → volume loss and rising plasma osmolarity → **polydipsia**.
**(b) Cells that cannot use the glucose.** Muscle and fat starving in a high-glucose bloodstream
→ **polyphagia**, fatigue, and — in Type 1 — **weight loss** from lipolysis, proteolysis, and
calories poured into the urine.

**Concrete.** T1 before diagnosis at eleven: up four times a night, drinking constantly, eating
everything and losing twelve pounds, exhausted, vision blurring as osmotic shifts swelled his
lenses, a cut on his shin that wouldn't close. Each is sugar dragging water out through his
kidney, or cells that couldn't get fuel. The LEAST list: never hypoglycemic (that came later, from
his insulin), never *reduced* urine output, no weight gain, never less thirsty.

**Claims.** Polyuria in diabetes is **osmotic diuresis**, not a hormone problem — a different
mechanism from diabetes insipidus, where ADH is the failure and the urine is dilute and
sugar-free. Weight change in untreated diabetes is **loss**, not gain; obesity is a risk factor
for Type 2, not a symptom. **Hypoglycemia is a complication of treatment**, not a feature of the
disease.

**Predicts.** On a LEAST-likely-symptom item, run the filter: **does this trace to glucose pulling
water out through the kidney, or to cells starving in a sea of sugar?** If neither, it is the
answer. The two reliable LEAST answers are **the reverse of a real symptom** (oliguria, decreased
thirst, weight gain) and **a treatment effect** (hypoglycemia).

#### Type 1 vs Type 2 — absent versus ignored
FL1: Q165, Q168 · CC1D/CC3B · Skill 1

**Structure.** **Type 1**: autoimmune T-cell destruction of β cells → **absolute insulin
deficiency**. **Type 2**: **insulin resistance** at the target tissue plus progressive β-cell
secretory failure → insulin present, often high early, and not obeyed.

**Concrete.** Measure **C-peptide** — cleaved from proinsulin, released 1:1 with endogenous
insulin, absent from injected insulin. T1's is near zero, his β cells gone; T2's is normal or
high, hers working hard. One lab separates them though both are hyperglycemic this morning.

**Claims.** The two share a number and almost nothing else — onset, ketosis-proneness, and whether
insulin is mandatory all differ (T2 decompensates into the hyperosmolar hyperglycemic state, not
DKA, because residual insulin blocks lipolysis). Denies "Type 2 is mild Type 1."

**Predicts.** Given a defect, predict the type. β-cell autoantibodies, low C-peptide,
ketoacidosis → Type 1. Normal insulin with poor tissue response, no ketosis, response to weight
loss or exercise → Type 2. Given an intervention, ask **which broken step does it touch** — that
is the whole of Q165.

**Discriminators**
- Type 1 vs Type 2 — *is insulin absent, or present and ignored?* (C-peptide answers it.)
- Diabetes mellitus vs diabetes insipidus — *is the polyuria driven by glucose in the tubule
  or by absent ADH?* Both make huge urine volumes; only one has glucose in it.
- Symptom of the disease vs effect of treatment — *would an untreated patient have this?*
- Insulin-stimulated vs contraction-stimulated GLUT4 — *does the pathway run through Akt or
  through AMPK?*

**Compression — one axis: which step is broken, and does the intervention touch it**

| | Type 1 | Type 2 |
|---|---|---|
| Broken step | β cell destroyed — no insulin made | Post-receptor signaling — insulin ignored |
| C-peptide | Low / absent | Normal / high |
| Ketosis-prone | Yes | No (HHS instead) |
| Weight at onset | Loss, lean | Typically obese |
| Insulin injection | Replaces the missing step — required | Overcomes resistance — optional |
| **Exercise (AMPK/GLUT4)** | **Bypasses nothing that's broken; hepatic output unopposed — unpredictable** | **Bypasses the broken step, and reverses its cause — reliable** |
