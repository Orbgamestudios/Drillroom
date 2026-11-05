# CONCEPTS — Bio/Biochem

FL1 B/B: **128, 84th percentile, 48/59.** Skill 1 (knowledge) 91%. Skill 2 (reasoning) 74%.
Strongest section — a patch, not a rebuild. Eleven missed questions → 21 concepts, eight
clusters, then stop.

---

## Before the clusters: the negative stem

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

## Cluster 1 — Central dogma and gene expression
FL1: Q113, Q120, Q135

**The shared cell.** One **vascular smooth muscle cell** in an arteriole wall: transcribes
*AGTR1*, splices, translates the AT1 receptor, membranes it, and in Cluster 5 signals through it.

### What survives into a mature mRNA
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

### A transcription factor turns on a set, not a gene
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

### Describing an allele from a figure without overclaiming
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

## Cluster 2 — DNA repair and genome instability
FL1: Q115

**The shared cell.** One **colon crypt stem cell**, dividing every few days for decades — the
lineage that produced the tumors in the Q113 figure.

### Mismatch repair — the proofreader's proofreader
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

### Microsatellite instability — the readout, not the lesion
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

## Cluster 3 — Membrane transport: structure predicts route
FL1: Q133

**The shared cell.** One **proximal tubule epithelial cell**: apical (urine-facing) on top,
basolateral (blood-facing) below, tight junctions between neighbors. It carries Cluster 4 and
reappears in Cluster 7.

### Reading a molecule's structure to pick its route
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

### Facilitated diffusion is passive; secondary active transport is not
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

## Cluster 4 — The Na⁺/K⁺ ATPase and how activity is measured
FL1: Q129

### The pump: stoichiometry, charge, and what it pays for
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

### Measuring activity vs measuring abundance — the NOT question
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

## Cluster 5 — Cell signaling and what "directly activates" means
FL1: Q134

**The shared cell.** Back to the **vascular smooth muscle cell** from Cluster 1, AT1 receptor now
in the membrane. Angiotensin II arrives.

### The four receptor classes, sorted by what crosses the membrane
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

### "Directly activates" is exactly one step
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

## Cluster 6 — The action potential
FL1: Q159

**The shared cell.** One **myelinated axon**, resting at −70 mV, taking a depolarizing input at
the axon hillock.

### Which conductance is open when
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

### Almost no sodium actually moves
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

### All-or-none: intensity is frequency, not amplitude
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

## Cluster 7 — Renal concentration
FL1: Q127

**The shared cell.** The **proximal tubule cell from Cluster 3** is one station. Follow one volume
of filtrate from Bowman's capsule to the papilla, on a day the person is dehydrated and ADH is
maximal.

### The nephron by osmolarity, segment by segment
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

### Countercurrent multiplication vs countercurrent exchange
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

### ADH moves water; aldosterone moves sodium
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

## Cluster 8 — Glucose physiology and diabetes
FL1: Q165, Q168

**The shared patients.** Two people in one clinic waiting room. **T1**, nineteen, thin, diagnosed
at eleven, insulin pump. **T2**, fifty-four, heavy, diagnosed last year, metformin. Both at blood
glucose 260 this morning. Both about to go for a run.

### Insulin's job is GLUT4 translocation — and only some tissues care
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

### Exercise recruits GLUT4 without insulin
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

### The symptoms, and the two things they all trace to
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

### Type 1 vs Type 2 — absent versus ignored
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
