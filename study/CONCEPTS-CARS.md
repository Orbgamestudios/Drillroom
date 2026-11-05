# CONCEPTS — CARS

FL1: 124, 50th percentile, 35/53. Eighteen misses.
Decay: **82% first third → 59% middle → 58% final third** — that gradient, not any question type,
is the largest recoverable block of points here.

CARS has no content. What is learnable: **how AAMC builds a wrong answer**, and **what each stem
type actually demands.**

Sources: `research/07-cars-construction.md` (AAMC CARS outline + AAMC-labeled Road Map corpus,
n=181 stems), `study/CARS-AAMC-SETS.md` (14 AAMC/Khan passage sets, per-choice rationales in
AAMC's own voice), `results/FL1-ANALYSIS.md`.

---

## THE ONE FACT THAT ORGANIZES EVERYTHING

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

# 1 · THE 14 REJECTION TEMPLATES

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

### R1 · NO ANCHOR SENTENCE
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

### R2 · SUPPORTED, BUT ANSWERS A DIFFERENT QUESTION
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

### R3 · CONCESSION READ AS THESIS
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

### R4 · MENTIONED, BUT NOT EVIDENCED
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

### R5 · WRONG VOICE
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

### R6 · WRONG SCOPE
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

### R7 · PASSAGE VOCABULARY, WRONG JOINT
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

### R8 · ASSUMED, NOT ARGUED
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

### R9 · TRUE BUT INERT
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

### R10 · REVERSAL IN FRESH WORDS
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

### R11 · SILENCE READ AS SUPPORT
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

### R12 · WRONG CATEGORY
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

### R13 · SURFACE ANALOGY, BROKEN RELATION
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

### R14 · NOT THE BEST
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

# 2 · THE SEVEN ARCHETYPES HE MISSED

Eighteen misses, seven stem families. Seventeen are placed below; **Q79** is not — AAMC's
skill and content tags came through blank for it in the score extract, so it has no archetype.

**Q98, Q99, Q100, Q101 were four consecutive misses** — main idea, apply, function, function. One
passage, and the composition says he never built its skeleton: main idea and function need the
argument's shape, apply needs the author's framework. Miss the shape and the set goes. See §4.

---

### A · FUNCTION / PURPOSE
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

### B · EVIDENCE / SUPPORT
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

### C · INFERENCE
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

### D · APPLY TO A NEW SITUATION
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

### E · MAIN IDEA / CENTRAL THESIS
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

### F · IRONY / RELATIONSHIP
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

### G · ALTERNATIVE EXPLANATION
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


# 3 · THE OWNERSHIP SYSTEM

The right tool for the R3/R5 family. It was not running from passage 1.

### The three tags

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

### The state sentence — with a mandatory "but"

After the last paragraph, before the first question: **one sentence, in your head, of the form
"X, but Y."**

The "but" is a forcing function — CARS passages are selected for holding two positions (AAMC:
*"multifaceted and focus on the relationships between ideas"*). No X → you never identified the
opponent. No Y → you have the opponent's view, not the author's: the R8/R3 miss on main-idea items.
X is what the distractors are built from; Y is the key.

### Highlight only the left half of a concession

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

### Worked pass — *Deconstructionism and literature*

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

# 4 · THE DECAY

**82% → 59% → 58%.** The largest single loss in CARS and the only one that is pure procedure.

### Read the shape before fixing it

A **step, not a slope** — 59 then 58, flat after the drop. Fatigue produces a slope, and his own
exam rules fatigue out: B/B went 74 → 84 → **86** and P/S 58 → 68 → **76**, later the same day. He
switched to skim-for-structure with 20–30 minutes left: *"it stopped the bleeding."* A late method
change plus a floor rather than a continued fall is a **regime change under clock debt** — time
overspent early, repaid at a worse exchange rate.

### Where the points actually are

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

### The clock rule

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

### The per-passage procedure — same one from passage 1

| phase | budget | what happens |
|---|---|---|
| **Read** | 0:00 → 3:30 | One pass, tagging `HIS / THEIRS± / GIVEN` at each break and marking left-halves of concessions. **Never re-read a sentence** — AAMC edits passages to be self-sufficient and glosses its hard terms, so anything that didn't land is re-explained downstream. The most expensive habit available. |
| **Gate** | 3:30 → 3:45 | Say *"X, but Y."* A gate, not a formality — branch on it. |
| **Gate passed** | ~60 s / question | Full protocol, in the order given. No reordering; re-orientation costs more than it saves. |
| **Gate failed** | ~30 s / skeleton item | No skeleton → main-idea, function and apply items are two-minute coin flips. **Triage:** answer the locals (detail, meaning-in-context, one-step inference), 30 s each on the skeleton items, flag, move, bank the time. That set costs most of itself either way; the live question is whether it also costs the next passage. That was Q98–101. |
| **Commit** | ~45 s in | Down to two. Do not adjudicate: **the key is defensible in one step, the near-miss in three** — take the one-step option, flag, move. If both feel one-step you have not named the axis (R14). |
| **Flagged** | after passage 9 | Not revisited before then. Mid-section returns convert a small deficit into a regime change. |

### The compressed protocol (his skim-for-structure, promoted to a standing tool)

Trigger: >2:00 behind at a checkpoint, or a first paragraph opaque on the first read.

- ¶1 in full · first and last sentence of each middle ¶ · last ¶ in full. Tag as you go.
- **State sentence still mandatory** — it is the whole point of the skim.
- Go to questions; return to the paragraph a stem points at and read that one properly.
- Budget 7:00 instead of 10:00. The 3:00 saved is the debt payment.

### How to train it in seven days

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

# 5 · WHAT TO STOP USING

### Stop counting words

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

### Three more heuristics that are anti-correlated on AAMC material

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

### Stop defaulting to B

FL1: accuracy **81.7% when the key was B, 66.7% when it wasn't** — a 15-point gap, replicating the
same gap in his own bank (73% vs 63%). This form ran B-heavy at 30.9%, so the default paid. AAMC/Khan
key positions run **A 18 · B 15 · C 14 · D 19**: B is not modal, and there is no base rate to
exploit. When wrong on FL1 he over-picked C — 20 of the 65 misses he actually answered (66 missed, minus the Q39
blank), 31% — a position habit misfiring.

### Stop asking "is this true?"

The whole of §1: zero of 198 distractors rejected for being false about the world; **textual
warrant** is the predicate. Costliest version — the true-and-informed option on a topic he knows.

### What replaces all of it

One question, asked in this order:

1. **Where is the sentence?** No sentence → dead (R1).
2. **Does it answer *this* stem?** True but non-responsive → dead (R2, R3).
3. **Whose is it?** Tagged THEIRS− or a left-half → dead (R5, R3).
4. **Same quantity, same connective, same category?** (R6, R7, R12).
5. **Two survivors → name the axis** — responsiveness, scope, strength, attribution, relation — and
   take the option defensible in **one move**.

Nothing in that list looks at the option's shape. That is the point.

---

# EXAM-DAY CARD

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
