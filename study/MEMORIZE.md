# MEMORIZE — the always-tested arbitrary set

**What this is.** The bounded set of MCAT facts that cannot be derived and must be known cold. Everything derivable was deliberately left out. Scope-locked to the AAMC content outline (`research/08-content-outline.md`): Algebra II ceiling, no calculus, no dot/cross products, trig only at 0/90/180 and 30-45-60, periodic table provided, no calculator.

**How to use it.** One sitting, morning of Sept 11. Read the tables, not the notes. Notes exist so a fact you half-know snaps back; they are not for first learning.

**Status:** built 2026-09-04.

---

**Contents**

1. [The 20 amino acids](#1-the-20-amino-acids) — table, catalytic His, essential, keto/glucogenic, A280, pI
2. [Hormones](#2-hormones) — releasing hormones, pituitary, peripheral glands, the trap pairings, signaling class
3. [The nephron](#3-the-nephron-segment-by-segment) — segment table, countercurrent, clearance
4. [Metabolic regulation points](#4-metabolic-regulation-points-only) — glycolysis, PDH, TCA, ox-phos, gluconeogenesis bypasses, phosphate hierarchy
5. [Formula sheet](#5-formula-sheet) — 12 domains, units, and the standard error for each
6. [Lab techniques](#6-lab-techniques) — gels, chromatography, blots, PCR, ELISA, decision table
7. [Genetics](#7-genetics) — ratios, pedigree one-step IDs, Hardy-Weinberg, linkage
8. [Vitamins and cofactors](#8-vitamins-and-cofactors) — coenzyme forms, reaction-type table, the three discriminators

---

## 1. THE 20 AMINO ACIDS

### 1.1 The table

Side-chain pKa column: blank = not ionizable. Values are Lehninger free-amino-acid values; in a folded protein they shift, and AAMC passages will tell you when they have.

| Name | 3 | 1 | Class | SC pKa | Distinguishing structural feature |
|---|---|---|---|---|---|
| Glycine | Gly | **G** | nonpolar | — | Side chain is a single **H**. Only achiral AA. Maximum backbone flexibility → found where the chain must turn hard (collagen Gly-X-Y every 3rd residue). |
| Alanine | Ala | **A** | nonpolar | — | Methyl. The reference "small hydrophobe"; the residue mutagenesis scans to (Ala scanning). |
| Valine | Val | **V** | nonpolar | — | Isopropyl, **β-branched** → disfavors α-helix. The Glu6→Val substitution is sickle-cell. |
| Leucine | Leu | **L** | nonpolar | — | Isobutyl (branch at γ). Leucine zipper. **Ketogenic only.** |
| Isoleucine | Ile | **I** | nonpolar | — | *sec*-butyl. **β-branched AND two stereocenters** (with Thr, the only two). |
| Proline | Pro | **P** | nonpolar | — | **Secondary amine** — side chain bonds back to α-N (pyrrolidine ring). No amide H to donate → **helix breaker / found in turns**; the only residue with an appreciable *cis* peptide bond. |
| Methionine | Met | **M** | nonpolar | — | **Thioether** (S but no thiol, cannot form disulfides). **AUG = start codon**, so N-terminal residue of every nascent chain. |
| Phenylalanine | Phe | **F** | aromatic, nonpolar | — | Benzyl. Purely hydrocarbon aromatic. λmax ≈ 257 nm — **negligible at 280**. |
| Tryptophan | Trp | **W** | aromatic, nonpolar | — | **Indole** — bicyclic, largest side chain, has an N–H. Dominates A280 (ε ≈ 5500). |
| Tyrosine | Tyr | **Y** | aromatic, polar | **10.07** | **Phenol**. Only aromatic that ionizes. Phosphorylation target of receptor tyrosine kinases. Second contributor to A280 (ε ≈ 1490). |
| Serine | Ser | **S** | polar | — | –CH2OH. Nucleophile of the **serine protease catalytic triad**; principal O-phosphorylation site. |
| Threonine | Thr | **T** | polar | — | –CH(OH)CH3. **β-branched, two stereocenters.** Phosphorylation + O-linked glycosylation site. |
| Cysteine | Cys | **C** | polar | **8.18** | **Thiol.** Only residue that forms a covalent crosslink — 2 Cys oxidize to **cystine** (disulfide). Thiolate is the nucleophile in Cys proteases. |
| Asparagine | Asn | **N** | polar | — | Amide of Asp (uncharged, cannot titrate). **N-linked glycosylation** at the Asn-X-Ser/Thr sequon (X ≠ Pro). |
| Glutamine | Gln | **Q** | polar | — | Amide of Glu; one CH2 longer than Asn. Blood ammonia carrier. |
| Aspartate | Asp | **D** | acidic | **3.65** | Shortest carboxylate (one CH2). Second member of the catalytic triad. |
| Glutamate | Glu | **E** | acidic | **4.25** | Carboxylate, one CH2 longer → slightly weaker acid. Principal excitatory neurotransmitter. |
| Lysine | Lys | **K** | basic | **10.53** | Straight-chain **ε-amino**. Site of histone acetylation/methylation; forms Schiff bases with PLP and retinal. |
| Arginine | Arg | **R** | basic | **12.48** | **Guanidinium** — resonance-delocalized over 3 N, so it is the **most basic** and stays protonated at every physiological pH. |
| Histidine | His | **H** | basic, aromatic | **6.00** | **Imidazole.** The one side chain that titrates near pH 7. |

### 1.2 The catalytic-residue question (asked every form)

**Histidine, pKa ≈ 6.0, is the only side chain with a pKa near physiological pH.**

Why that makes it the catalytic residue: at pH 7.4 the imidazole sits near its pKa, so a meaningful fraction of the population is protonated and a meaningful fraction is not. It can therefore **accept a proton in one step of the mechanism and donate it back in the next, within a single turnover** — general acid *and* general base catalysis from one residue, with no energetic penalty for switching. Every other ionizable side chain is locked: Asp/Glu are >99.9% deprotonated at pH 7, Lys/Arg >99.9% protonated. Locked residues can stabilize charge (electrostatic catalysis, transition-state stabilization) but cannot shuttle protons.

Consequences you can be asked to predict:
- **Serine protease triad Ser-His-Asp.** His pulls the proton off Ser-OH, generating the alkoxide nucleophile; Asp orients His and stabilizes the resulting imidazolium. Asp does not touch the substrate.
- **pH-rate profiles with a bell shape near pH 6–7** implicate His. A profile that turns over near pH 4 implicates Asp/Glu; near pH 10, Lys/Tyr/Cys.
- **Hemoglobin's Bohr effect** runs through His146 (β) — protonation at low pH stabilizes T state.
- His is also the near-universal **metal-coordinating residue** (Zn in carbonic anhydrase, Fe in heme) because the unprotonated imidazole N is a good lone-pair donor.

### 1.3 Essential

**PVT TIM HaLL** — **P**he, **V**al, **T**hr, **T**rp, **I**le, **M**et, **H**is, **L**eu, **L**ys. That is 9. Add **Arg** = conditionally essential (children, injury, growth — synthesis rate is below demand). Total commonly quoted as 9 or 10; both appear in answer keys, so read the stem.

Non-essential (11): Ala, Asn, Asp, Cys, Gln, Glu, Gly, Pro, Ser, Tyr, + Arg if the stem counts it non-essential.

Two conditional dependencies worth knowing: **Tyr is made from Phe** (phenylalanine hydroxylase; PKU blocks it → Tyr becomes essential), and **Cys is made from Met** (Met donates the sulfur).

### 1.4 Ketogenic vs glucogenic

| Category | Members | Mnemonic / logic |
|---|---|---|
| **Purely ketogenic** | **Leu, Lys** | "the two L's." Carbon skeletons enter only as acetyl-CoA / acetoacetyl-CoA → cannot make net glucose. |
| **Both** | **Ile, Phe, Thr, Trp, Tyr** | "**I** **P**ut **T**hree **T**ires **T**ogether." |
| **Purely glucogenic** | the other 13 | Default. Skeletons reach pyruvate, OAA, α-KG, succinyl-CoA, or fumarate. |

The load-bearing derivation: **acetyl-CoA cannot become glucose in animals** (PDH is irreversible; the two carbons are lost as CO2 in the TCA turn). So "ketogenic" = "enters at acetyl-CoA or acetoacetate."

### 1.5 A280 absorbance

**Trp >> Tyr >> Phe.** Trp and Tyr are the practical contributors; Phe is essentially invisible at 280 nm. Trp and Tyr are the only two with an extended/heteroatom-bearing aromatic system; Phe's benzene absorbs at shorter wavelength.

Use: **protein concentration by A280** is the standard readout. A protein with no Trp or Tyr will read near zero and be missed — that is the trap. Nucleic acid contamination shows as **A260 > A280**; pure DNA has A260/A280 ≈ 1.8, pure RNA ≈ 2.0, pure protein ≈ 0.6.

### 1.6 Charge, pI, and titration — the arbitrary anchors

| Group | pKa | State at pH 7.4 |
|---|---|---|
| α-carboxyl | ≈ 2.0 (1.8–2.4) | deprotonated, **–1** |
| α-amino | ≈ 9.5 (8.8–10.6) | protonated, **+1** |

- **pI = average of the two pKas that flank the neutral (zwitterionic) species.**
- Neutral side chain → pI ≈ (2.0 + 9.5)/2 ≈ **5.7–6.1**
- Acidic side chain (Asp, Glu) → average the **two lowest** → pI ≈ **3**
- Basic side chain (His, Lys, Arg) → average the **two highest** → pI ≈ **7.6 (His), 9.7 (Lys), 10.8 (Arg)**
- **pH < pI → net positive → migrates to cathode. pH > pI → net negative → migrates to anode.** At pH = pI, no migration and **minimum solubility** (why proteins precipitate at their pI).

### 1.7 Stereochemistry

All 19 chiral amino acids in proteins are **L**. L = **S** at the α-carbon **for every one except cysteine**, which is **R** — nothing about the geometry changed; the sulfur simply outranks nitrogen under CIP priority. Glycine is achiral. Ile and Thr have a second stereocenter in the side chain.

---

## 2. HORMONES

### 2.1 Hypothalamus — the releasing hormones

All travel the **hypophyseal portal system** to the anterior pituitary. Portal = they reach the pituitary at high concentration without systemic dilution; that is why hypothalamic hormones are essentially undetectable in peripheral blood.

| Hormone | Target | Action | Axis |
|---|---|---|---|
| **GnRH** | gonadotropes | ↑ FSH, LH — **pulsatile release required**; continuous GnRH *suppresses* gonadotropins (basis of leuprolide) | HPG |
| **TRH** | thyrotropes (+ lactotropes) | ↑ TSH, and ↑ prolactin as a side effect | HPT |
| **CRH** | corticotropes | ↑ ACTH | HPA |
| **GHRH** | somatotropes | ↑ GH | GH/IGF-1 |
| **Somatostatin (GHIH)** | somatotropes, thyrotropes | ↓ GH, ↓ TSH | GH/IGF-1 (brake) |
| **Dopamine (PIF)** | lactotropes | **↓ prolactin — tonic, continuous inhibition** | prolactin (inverted) |
| *ADH, oxytocin* | *(made here, not released here)* | synthesized in supraoptic/paraventricular nuclei, carried down axons, **released from posterior pituitary** | — |

### 2.2 Pituitary

**Anterior (adenohypophysis)** — true glandular tissue, makes its own hormones. Mnemonic **FLAT PiG**: FSH, LH, ACTH, TSH (the four **tropic**) + **P**rolactin, **G**H (the two **direct**).

**Posterior (neurohypophysis)** — neural tissue, a nerve terminal, **synthesizes nothing.** ADH and oxytocin only.

| Gland | Hormone | Target | Action | Axis |
|---|---|---|---|---|
| Ant. pit. | **FSH** | ♀ granulosa / ♂ Sertoli | ♀ follicle maturation, aromatase → estrogen; ♂ spermatogenesis support | HPG |
| Ant. pit. | **LH** | ♀ theca + whole follicle / ♂ Leydig | ♀ androgen precursor, **surge triggers ovulation**, maintains corpus luteum; ♂ testosterone | HPG |
| Ant. pit. | **ACTH** | adrenal **cortex** (fasciculata) | ↑ cortisol; also ↑ melanin (POMC-derived → hyperpigmentation in Addison's) | HPA |
| Ant. pit. | **TSH** | thyroid follicular cells | ↑ T3/T4 synthesis + release; ↑ gland size | HPT |
| Ant. pit. | **Prolactin** | mammary gland | milk **production** (not ejection) | inhibited by dopamine |
| Ant. pit. | **GH** | liver → IGF-1; also direct on muscle/bone/fat | ↑ linear growth, ↑ protein synthesis, **↑ lipolysis, ↓ glucose uptake (diabetogenic)** | GH/IGF-1 |
| Post. pit. | **ADH (vasopressin)** | collecting duct principal cells (V2), vascular smooth muscle (V1) | **inserts aquaporin-2 → water reabsorption only**; V1 vasoconstriction | osmolarity |
| Post. pit. | **Oxytocin** | uterine smooth muscle, myoepithelial cells | uterine contraction (**positive feedback** in labor), **milk let-down** | positive-feedback loop |

### 2.3 Peripheral glands

| Gland | Hormone | Target | Action | Axis |
|---|---|---|---|---|
| Thyroid (follicular) | **T3 / T4** | nearly all cells; **intracellular nuclear receptor** | ↑ basal metabolic rate, ↑ Na/K-ATPase, ↑ heat, permissive for GH and catecholamines. T4 is the reservoir; **T3 is the active form** (deiodinase converts peripherally) | HPT |
| Thyroid (parafollicular C) | **Calcitonin** | osteoclasts, kidney | ↓ plasma Ca2+ (inhibits osteoclasts, ↑ renal Ca excretion). **Minor in humans** | Ca-PO4 |
| Parathyroid (chief) | **PTH** | bone, kidney, (gut indirectly) | **↑ plasma Ca2+, ↓ plasma phosphate.** ↑ osteoclast resorption (via osteoblast RANKL), ↑ Ca reabsorption in DCT, ↑ phosphate *excretion* in PCT, ↑ 1α-hydroxylase → calcitriol | Ca-PO4 |
| Kidney | **Calcitriol** (1,25-(OH)2-D3) | small intestine | ↑ absorption of **both Ca2+ and phosphate** | Ca-PO4 |
| Adrenal **cortex** — glomerulosa | **Aldosterone** | DCT/collecting-duct principal cells | **↑ Na+ reabsorption (water follows isotonically), ↑ K+ and H+ secretion** | RAAS |
| Adrenal cortex — fasciculata | **Cortisol** | liver, muscle, adipose, immune | ↑ gluconeogenesis, ↑ proteolysis, ↑ lipolysis, **immunosuppression**, permissive for catecholamines | HPA |
| Adrenal cortex — reticularis | **DHEA / androgens** | peripheral tissue | weak androgens; the main androgen source in women | HPA-ish |
| Adrenal **medulla** | **Epi (~80%) / NE** | α and β adrenergic GPCRs | fight-or-flight: ↑ HR, ↑ contractility, bronchodilation, glycogenolysis, vasoconstriction. **A modified sympathetic ganglion — preganglionic sympathetic fibers release ACh onto nicotinic receptors here** | sympathetic |
| Pancreas α | **Glucagon** | **liver only** | ↑ glycogenolysis, ↑ gluconeogenesis, ↑ ketogenesis | fuel |
| Pancreas β | **Insulin** | liver, muscle, adipose (**GLUT4**) | ↑ glucose uptake, glycogenesis, lipogenesis, protein synthesis; ↓ everything catabolic. **Also drives K+ into cells** | fuel |
| Pancreas δ | **Somatostatin** | neighboring islet cells, GI | ↓ insulin, ↓ glucagon, ↓ GI secretion/motility | brake |
| Kidney (JG cells) | **Renin** (an enzyme) | angiotensinogen | released on ↓ renal perfusion, ↓ NaCl at macula densa, or β1 sympathetic input. Starts RAAS | RAAS |
| Lung endothelium | **ACE** | angiotensin I → II | AT-II: vasoconstriction, ↑ aldosterone, ↑ ADH, ↑ thirst, ↑ PCT Na reabsorption | RAAS |
| Kidney | **EPO** | bone marrow | ↑ RBC production; released on hypoxia | O2 delivery |
| Heart — atria / ventricles | **ANP / BNP** | kidney, vessels | **the anti-aldosterone**: ↑ Na and water excretion, vasodilation, ↓ renin/aldosterone. Released on **stretch** = volume overload | volume (opposes RAAS) |
| Liver | **IGF-1 (somatomedin)** | bone, cartilage, muscle | mediates most of GH's growth effect | GH/IGF-1 |
| Pineal | **Melatonin** | SCN, body | circadian phase; **released in darkness** | circadian |
| Thymus | **Thymosin** | T cells | T-cell maturation | immune |
| Adipose | **Leptin** | hypothalamus | **satiety** — decreases appetite; rises with fat mass | appetite |
| Stomach | **Ghrelin** | hypothalamus | **hunger** — rises before meals | appetite |
| Stomach G cells | **Gastrin** | parietal cells | ↑ HCl secretion | GI |
| Duodenum S cells | **Secretin** | pancreas, stomach | ↑ **bicarbonate** from pancreas, ↓ gastric acid. Released by **acid** in duodenum | GI |
| Duodenum I cells | **CCK** | gallbladder, pancreas, stomach | gallbladder contraction, ↑ pancreatic **enzymes**, ↓ gastric emptying, satiety. Released by **fat and protein** | GI |
| Testes (Leydig) | **Testosterone** | wide | male secondary characteristics, spermatogenesis support, anabolic | HPG |
| Testes (Sertoli) | **Inhibin** | ant. pituitary | **selectively ↓ FSH only** | HPG |
| Ovary (granulosa) | **Estrogen** | wide | follicular phase; endometrial **proliferation**; feedback sign flips (below) | HPG |
| Corpus luteum | **Progesterone** | endometrium, uterus | luteal phase; endometrial **maintenance/secretion**, ↓ uterine contractility | HPG |
| Placenta | **hCG** | corpus luteum | LH-mimic — rescues the corpus luteum until the placenta takes over (~wk 8–12). Basis of pregnancy tests | HPG |

### 2.4 The trap pairings — memorize the discriminator, not the pair

| Pair | The one-line discriminator |
|---|---|
| **ADH vs aldosterone** | **ADH moves water alone → volume up, osmolarity DOWN (serum Na falls).** **Aldosterone moves Na with water isotonically → volume up, osmolarity UNCHANGED.** ADH answers to osmoreceptors; aldosterone answers to angiotensin II and to **hyperkalemia**. ADH acts on aquaporin-2; aldosterone on ENaC + Na/K-ATPase. |
| **PTH vs calcitonin** | Both touch Ca2+; **PTH raises it, calcitonin "tones it down."** But the real discriminator is phosphate: **PTH raises Ca and LOWERS phosphate** (it wastes PO4 in the PCT). **Calcitriol raises BOTH.** A stem with high Ca + high PO4 is vitamin D, not PTH. |
| **Insulin vs glucagon** | **Glucagon has no muscle receptors** — it is a liver hormone. And **only liver has glucose-6-phosphatase**, so only liver exports free glucose; muscle glycogen serves muscle alone. |
| **Oxytocin vs ADH** | Both are posterior-pituitary nonapeptides differing by two residues. Oxytocin = the only classic **positive-feedback** loop (with the LH surge). Prolactin makes milk; **oxytocin ejects it.** |
| **Cortisol vs epinephrine** | Same stressor, different clock. Epi = seconds, GPCR, transient. Cortisol = hours, **nuclear receptor, transcriptional**, and **permissive** — it does not itself vasoconstrict, it lets catecholamines do so. |
| **Estrogen's feedback sign** | **Negative** at low/moderate levels, **POSITIVE** when high and sustained for ~2 days late in the follicular phase → the **LH surge → ovulation**. This sign flip is the single most tested endocrine fact. |
| **Inhibin vs estrogen** | Inhibin suppresses **FSH only**; estrogen/progesterone suppress both. |
| **Prolactin** | The **only** anterior-pituitary hormone under net **inhibitory** control (dopamine). Cut the stalk → every other pituitary hormone falls, prolactin **rises**. |
| **T3/T4 and cortisol are the receptor traps** | Thyroid hormone is **amino-acid derived but binds an intracellular nuclear receptor** (like a steroid). Catecholamines are amino-acid derived and bind **surface GPCRs**. Do not sort by chemical class; sort by receptor location. |
| **Aldosterone vs ANP** | Exact opposites. Aldosterone retains Na; ANP dumps it. ANP is released by **stretch**. |
| **Somatostatin** | Appears in three places — hypothalamus (↓GH, ↓TSH), pancreatic δ cells (↓insulin, ↓glucagon), gut. Always a brake. |
| **GH's glucose effect** | GH is **anabolic for protein but ANTI-insulin for glucose** — it raises blood glucose. Counterintuitive; tested. |
| **FSH/LH by sex** | FSH → the **support cell** (Sertoli / granulosa). LH → the **steroid-making cell** (Leydig / theca) and the ovulation trigger. |

### 2.5 Signaling class — decides speed, transport, and duration

| Class | Examples | Receptor | Blood transport | Onset / duration |
|---|---|---|---|---|
| **Peptide** | insulin, glucagon, GH, ACTH, ADH, PTH, all releasing hormones | **cell surface**, → cAMP / IP3-DAG / RTK | free (water-soluble) | fast / short |
| **Steroid** | cortisol, aldosterone, estrogen, progesterone, testosterone, calcitriol | **intracellular / nuclear** → alters transcription | **carrier protein required** | slow / long |
| **Amino-acid derived** | T3/T4 → **nuclear**; epi/NE → **surface GPCR** | split — see above | T3/T4 carrier-bound; catecholamines free | split |

Two derivations that answer most signaling questions: only the **free** fraction of a carrier-bound hormone is active (so albumin changes shift total but not free levels), and **steroid effects cannot be fast** because they require transcription and translation.

---

## 3. THE NEPHRON, SEGMENT BY SEGMENT

**Scope note:** AAMC's list names the segments, transport, the counter-current multiplier, and osmoregulation. It does **not** name diuretics. They are included because MCAT passages routinely supply a drug and expect you to place its site — treat the diuretic column as passage-decoding, not as recall AAMC will test bare.

### 3.1 The table

| Segment | Reabsorbed | Secreted | Transporters | H2O permeability | Diuretic acting here |
|---|---|---|---|---|---|
| **Glomerulus / Bowman's** | *(nothing — bulk filtration)* ~20% of plasma filtered | — | no transporters; a **size + charge sieve**: fenestrated endothelium → **negatively charged** basement membrane → podocyte slit diaphragms | free | — |
| **Proximal convoluted tubule** | **~65–67% of Na+ and water; 100% glucose; 100% amino acids; ~85–90% HCO3−;** phosphate, K+, urea, Cl− | **H+**; organic acids and bases — **drugs, PAH, penicillin, creatinine** | **SGLT2** (glucose, Na-coupled), **NHE3** (Na+/H+ exchange), Na-amino-acid and Na-phosphate cotransport, basolateral **Na+/K+-ATPase**, **carbonic anhydrase**. Brush border, most mitochondria in the nephron | **high — freely permeable.** Reabsorption is **isosmotic**: filtrate leaves at the same 300 mOsm it entered | **Acetazolamide** (carbonic-anhydrase inhibitor) → HCO3− wasting, metabolic acidosis. **Mannitol** (osmotic) |
| **Descending thin limb** | **water only** | — | **aquaporin-1**; essentially no active transport | **high to water, impermeable to solute** → filtrate **concentrates** to ~1200 mOsm at the hairpin | **Mannitol** |
| **Thin ascending limb** | NaCl, passively | — | passive paracellular/transcellular NaCl | **impermeable to water** | — |
| **Thick ascending limb (TAL)** | **Na+, K+, Cl−** actively; **Ca2+ and Mg2+ paracellularly** | small K+ backleak into lumen | **NKCC2** (Na-K-2Cl symporter), **ROMK** (K+ recycles to lumen → **lumen-positive** potential that drives Ca2+/Mg2+ paracellular reabsorption), basolateral Na+/K+-ATPase | **impermeable to water.** The **"diluting segment"** — filtrate exits **hypotonic (~100 mOsm)** | **Loop diuretics — furosemide** (blocks NKCC2). Most potent; also wastes Ca2+ and Mg2+ and **destroys the medullary gradient** |
| **Distal convoluted tubule (early)** | **Na+, Cl−; Ca2+ under PTH control** | — | **NCC** (Na-Cl symporter); **TRPV5** Ca2+ channel (PTH-upregulated) | **impermeable to water** | **Thiazides** (block NCC) |
| **Collecting duct — principal cells** | **Na+ (aldosterone-dependent); water (ADH-dependent); urea (inner medulla)** | **K+** | **ENaC** (Na+ entry; aldosterone ↑), **ROMK** (K+ out), **aquaporin-2** (ADH inserts it), **UT-A1** urea transporter (ADH ↑) | **variable — the only ADH-controlled segment.** No ADH → dilute urine (~50 mOsm); max ADH → concentrated (~1200 mOsm) | **K+-sparing: amiloride / triamterene** (block ENaC); **spironolactone / eplerenone** (mineralocorticoid-receptor antagonists). **ADH V2 antagonists** (-vaptans) |
| **Collecting duct — intercalated cells** | **HCO3− (α-type)** | **H+ (α-type); HCO3− (β-type)** | **H+-ATPase**, **H+/K+-ATPase**, band-3 Cl−/HCO3− exchanger, carbonic anhydrase | n/a | — (indirectly: loops/thiazides cause **contraction alkalosis** via this cell) |

### 3.2 The facts that get tested off this table

**The filtration barrier is charge-selective as well as size-selective.** Albumin (~66 kDa, **negatively charged**) is excluded twice over. Damage that neutralizes the basement membrane's fixed negative charge produces proteinuria **at unchanged pore size** — that is the standard passage twist.

**Arteriole logic.** Constrict the **afferent** → GFR **falls**. Constrict the **efferent** → GFR **rises** (backs pressure up into the glomerulus). **Angiotensin II preferentially constricts the efferent arteriole**, which is how RAAS defends GFR when renal perfusion drops.

**Countercurrent multiplier vs exchanger.** The **loop of Henle multiplies** — it actively builds the corticomedullary gradient using the TAL's pump plus the descending limb's water permeability. The **vasa recta exchanges** — it is passive, runs countercurrent to the loop, and merely *preserves* the gradient by not washing it out. **Urea recycling** in the inner medullary collecting duct supplies roughly half the medullary osmolarity, which is why protein-starved subjects cannot concentrate urine maximally.

**Glucose and the Tm.** Glucose reabsorption saturates. Below the transport maximum, urine glucose is zero; **glucosuria begins at a plasma glucose around 180–200 mg/dL** (threshold below Tm because of nephron heterogeneity, giving the "splay" in the curve). The osmotic diuresis of untreated diabetes follows directly.

**The calcium inversion — the highest-yield diuretic trap.** **Loop diuretics abolish the lumen-positive potential in the TAL → Ca2+ and Mg2+ are LOST → hypocalcemia** (used to treat hypercalcemia). **Thiazides act in the DCT and INCREASE Ca2+ reabsorption → hypercalcemia** (used to treat calcium kidney stones). Same organ, opposite calcium.

**Potassium.** Everything that delivers more Na+ to the collecting duct (loops, thiazides) **increases K+ secretion → hypokalemia**, because principal-cell Na+ entry through ENaC drives K+ out through ROMK. The K+-sparing agents block exactly that step. **Aldosterone secretes both K+ and H+**, so hyperaldosteronism gives hypokalemia **with metabolic alkalosis**.

**Clearance.** Clearance = (U × V) / P, in mL/min.
- **Inulin** — freely filtered, neither secreted nor reabsorbed → **clearance = GFR** exactly.
- **Creatinine** — filtered plus slightly secreted → **overestimates GFR** modestly.
- **PAH** — filtered *and* fully secreted, cleared in a single pass → **clearance = renal plasma flow**.
- **Filtration fraction = GFR / RPF ≈ 20%.**
- Clearance **> GFR** means net secretion; **< GFR** means net reabsorption; **= 0** means complete reabsorption (glucose in a normal person).

**Juxtaglomerular apparatus.** The **macula densa** sits in the TAL and senses **luminal NaCl**; the **JG cells** sit in the afferent arteriole and release **renin**. Three renin triggers: ↓ afferent arteriolar pressure, ↓ NaCl at the macula densa, **β1** sympathetic stimulation. Tubuloglomerular feedback: high distal NaCl → afferent constriction → ↓ GFR.

**ADH acts only on water; aldosterone acts only on solute.** Every free-water problem resolves through that sentence.

---

## 4. METABOLIC REGULATION POINTS ONLY

Every step listed here is **irreversible under cellular conditions** (large negative ΔG). That is not a coincidence — irreversible steps are the only ones worth regulating, because a near-equilibrium step's flux is set by substrate concentration no matter what you do to the enzyme. **Find the irreversible steps and you have found the control points.**

### 4.1 Glycolysis — 3 irreversible steps

| # | Enzyme | Reaction | Activators | Inhibitors |
|---|---|---|---|---|
| 1 | **Hexokinase** | glucose → G6P | — | **G6P** (product inhibition) |
| 1' | **Glucokinase** (liver, pancreatic β) | glucose → G6P | **insulin** (induces transcription) | **not** inhibited by G6P; sequestered by fructose-6-P via GKRP |
| 2 | **PFK-1** | F6P → **F1,6BP** | **AMP, ADP, fructose-2,6-bisphosphate** | **ATP, citrate, H+ (low pH)** |
| 3 | **Pyruvate kinase** | PEP → pyruvate (+ATP) | **F1,6BP (feed-forward)**, insulin | **ATP, alanine, acetyl-CoA**; glucagon → PKA phosphorylation (liver) |

**PFK-1 is the rate-limiting step and the committed step of glycolysis.** Hexokinase is not committed — G6P still has three fates (glycolysis, glycogen, pentose phosphate pathway).

**Hexokinase vs glucokinase — the discriminator:** hexokinase has a **low Km (high affinity, saturated at normal glucose) and low Vmax**, so it keeps working in every tissue at all times and shuts off on product. Glucokinase has a **high Km and high Vmax**, so it only engages when glucose is abundant — which makes the liver a glucose sink after a meal and lets the β cell use glucokinase as its **glucose sensor**.

### 4.2 The bifunctional enzyme — the single most tested regulatory node

**PFK-2 / FBPase-2** is one protein with two opposing active sites, and the phosphorylation state of one serine flips which one runs.

| Hormone | State | Which activity | F2,6BP | Net |
|---|---|---|---|---|
| **Insulin** (fed) | **de**phosphorylated | **PFK-2 kinase ON** | **↑ F2,6BP** | activates PFK-1, inhibits FBPase-1 → **glycolysis** |
| **Glucagon** (fasting) | phosphorylated by **PKA** | **FBPase-2 phosphatase ON** | **↓ F2,6BP** | de-activates PFK-1, releases FBPase-1 → **gluconeogenesis** |

F2,6BP is **not a glycolytic intermediate** — it is purely a signal molecule, and it is the **most potent allosteric activator of PFK-1**. It hits both directions at once, which is why a single second messenger can switch the liver's entire carbon flow.

### 4.3 The link reaction — pyruvate dehydrogenase

Irreversible. **The committed step to complete oxidation** — once carbon becomes acetyl-CoA, animals cannot get it back to glucose.

| Activators | Inhibitors |
|---|---|
| **NAD+, ADP, CoA, pyruvate, Ca2+** (muscle contraction signal), insulin (via PDH phosphatase) | **acetyl-CoA, NADH, ATP** (all products/energy-replete signals), PDH kinase |

Five cofactors, all vitamin-derived: **T**PP (B1) · **L**ipoic acid · **C**oA (B5) · **F**AD (B2) · **N**AD+ (B3). Mnemonic **"Tender Loving Care For Nancy."** α-ketoglutarate dehydrogenase and branched-chain ketoacid dehydrogenase are homologs and use the **identical five**.

### 4.4 TCA cycle — 3 regulated steps

| Enzyme | Reaction | Activators | Inhibitors |
|---|---|---|---|
| **Citrate synthase** | acetyl-CoA + OAA → citrate | substrate availability (OAA is the usual limiter) | **ATP, NADH, citrate, succinyl-CoA** |
| **Isocitrate dehydrogenase** | isocitrate → α-KG **(rate-limiting)** | **ADP, Ca2+, NAD+** | **ATP, NADH** |
| **α-Ketoglutarate DH** | α-KG → succinyl-CoA | **Ca2+** | **succinyl-CoA, NADH, ATP** |

The whole cycle reduces to one sentence: **ATP and NADH inhibit everything; ADP, NAD+, and Ca2+ activate everything.** Ca2+ appears three times (PDH, IDH, α-KGDH) because contraction and secretion are the events that spend ATP, so the calcium signal that triggers them also pre-orders the fuel.

### 4.5 Oxidative phosphorylation

**Regulation is almost entirely respiratory (acceptor) control: the rate is set by ADP availability.** No ADP → no flux through ATP synthase → protons accumulate → the gradient backs up → electron transport stalls → NADH accumulates → the TCA cycle stalls. The whole chain is one back-pressure system.

| Complex | Name | Pumps H+? |
|---|---|---|
| I | NADH dehydrogenase | yes (4) |
| II | Succinate dehydrogenase | **NO** — the only TCA enzyme embedded in the inner membrane, and it pumps nothing. This is why FADH2 yields less ATP |
| III | Cytochrome bc1 | yes (4) |
| IV | Cytochrome c oxidase (**O2 is the final acceptor**) | yes (2) |
| V | ATP synthase | uses the gradient |

| Poison | Site | Effect on O2 consumption |
|---|---|---|
| Rotenone, amytal | I | ↓ |
| Malonate | II (competitive with succinate) | ↓ |
| Antimycin A | III | ↓ |
| **Cyanide, CO, azide** | IV | ↓ |
| **Oligomycin** | V | ↓ (gradient builds, chain stalls) |
| **2,4-DNP, UCP1/thermogenin** (uncouplers) | membrane | **↑ — the counterintuitive one.** Gradient dissipates, electron transport runs faster, **ATP falls, heat rises, O2 consumption INCREASES** |

**P/O ratios: NADH → 2.5 ATP · FADH2 → 1.5 ATP.** Shuttles: **malate-aspartate** (liver, heart) delivers cytosolic NADH as NADH → 2.5; **glycerol-3-phosphate** (muscle, brain) delivers it as FADH2 → 1.5. That shuttle choice is the entire reason glucose yields **30 or 32 ATP** depending on the tissue.

### 4.6 Gluconeogenesis — the 4 bypass enzymes

The three irreversible glycolytic steps are the three that must be bypassed. **Seven of the ten glycolytic enzymes run backwards unchanged.**

| Bypass | Enzyme | Location | Cofactor / energy | Regulation |
|---|---|---|---|---|
| **1a** pyruvate → OAA | **Pyruvate carboxylase** | **mitochondrion** | **biotin**, CO2, **ATP** | **activated by acetyl-CoA** — the master fasting signal |
| **1b** OAA → PEP | **PEP carboxykinase (PEPCK)** | cytosol | **GTP** | **induced by glucagon and cortisol; repressed by insulin** (transcriptional, slow) |
| **2** F1,6BP → F6P | **Fructose-1,6-bisphosphatase** | cytosol | hydrolysis (no ATP made) | **rate-limiting.** Inhibited by **AMP and F2,6BP**; activated by **citrate** |
| **3** G6P → glucose | **Glucose-6-phosphatase** | **ER lumen — liver, kidney, intestine ONLY** | hydrolysis | present or absent, not allosterically tuned |

Three consequences that get tested directly:
- **Muscle lacks glucose-6-phosphatase**, so muscle glycogen serves only muscle. Muscle contributes to blood glucose only indirectly, by exporting **lactate (Cori cycle)** and **alanine (glucose-alanine cycle)**.
- **OAA cannot cross the inner mitochondrial membrane** — it exits as **malate** (or aspartate) and is reoxidized in the cytosol, which conveniently also supplies the cytosolic NADH gluconeogenesis needs.
- **Acetyl-CoA cannot become net glucose.** It activates pyruvate carboxylase (so fat oxidation *fuels* gluconeogenesis) but its own two carbons are lost as CO2 in the TCA turn. **Fatty acids cannot be converted to glucose** — except the glycerol backbone and odd-chain fatty acids' terminal propionyl-CoA → succinyl-CoA.

**Reciprocal regulation, one line:** every signal that turns glycolysis on turns gluconeogenesis off, through the same molecules — **F2,6BP** (activates PFK-1, inhibits FBPase-1), **AMP** (same), **ATP and citrate** (opposite), **acetyl-CoA** (inhibits PDH, activates pyruvate carboxylase).

### 4.7 The phosphate-transfer hierarchy

Standard free energy of phosphate-group hydrolysis, kJ/mol (memorize the **order**; the numbers are for calibration):

| Compound | ΔG°′ of hydrolysis | Class |
|---|---|---|
| **Phosphoenolpyruvate (PEP)** | **−61.9** | enol phosphate |
| **1,3-Bisphosphoglycerate** | **−49.3** | acyl phosphate (mixed anhydride) |
| **Creatine phosphate** | **−43.1** | phosphoguanidine |
| **ATP → ADP + Pi** | **−30.5** | phosphoanhydride |
| **Glucose-6-phosphate** | **−13.8** | phosphate ester |
| Glycerol-3-phosphate | −9.2 | phosphate ester |

**Why the order is what it is.** PEP is highest because hydrolysis releases an enol that immediately **tautomerizes to the far more stable keto form** — the tautomerization, not the phosphate bond itself, does the work. 1,3-BPG is a mixed anhydride whose hydrolysis produces a **resonance-stabilized carboxylate**. Ordinary phosphate **esters** (G6P, G3P) have no such escape and sit at the bottom.

**Why this explains substrate-level phosphorylation.** A phosphoryl group transfers spontaneously only **downhill** — from a higher-energy donor to a lower-energy acceptor. Because **PEP and 1,3-BPG sit above ATP**, they can hand a phosphate directly to ADP with no electron-transport chain, no membrane, no oxygen. That is exactly what happens at glycolysis steps **7 (phosphoglycerate kinase, from 1,3-BPG)** and **10 (pyruvate kinase, from PEP)**, and at **succinyl-CoA synthetase** in the TCA cycle. Those are the only substrate-level phosphorylations in central metabolism, and their existence is a direct consequence of this ranking.

Three more readings of the same table:
- **ATP sits in the middle on purpose.** It is a good enough donor to phosphorylate the low-energy compounds below it and a good enough acceptor to be charged by the high-energy compounds above it. A molecule at either extreme could not do both. ATP is a **carrier, not a store**.
- **Creatine phosphate sits just above ATP** — a small enough gap that the creatine kinase reaction runs **near equilibrium in both directions**. It reloads when ATP is plentiful and unloads within seconds when ATP falls, buffering muscle ATP for roughly the first 10 seconds of maximal effort. If it sat far above ATP it could not be recharged.
- **G6P sits well below ATP**, so ATP phosphorylates glucose readily and the reverse cannot happen. This is why **glucose-6-phosphatase must be a hydrolase** rather than hexokinase running backwards — and therefore why gluconeogenesis needs a separate enzyme in a separate compartment at all.

---

## 5. FORMULA SHEET

**Constants worth knowing cold:** g ≈ 10 m/s² (use 9.8 only if choices are tight) · k (Coulomb) = 9×10⁹ N·m²/C² · c = 3×10⁸ m/s · h = 6.6×10⁻³⁴ J·s · R = 8.314 J/mol·K = 0.0821 L·atm/mol·K · N_A = 6.02×10²³ · F = 96,485 C/mol · ρ_water = 1000 kg/m³ = 1 g/cm³ · 1 atm = 760 mmHg = 101 kPa · Kw = 10⁻¹⁴ · body temp 310 K.

### 5.1 Kinematics and mechanics

| Equation | Units | The thing people get wrong |
|---|---|---|
| v = v₀ + at | m/s | **Only valid for constant acceleration.** A graph with curvature in the v-t plot invalidates all four. |
| Δx = v₀t + ½at² | m | Sign of a. Down is negative only if you defined up as positive — then commit to it for the whole problem. |
| v² = v₀² + 2aΔx | — | The **time-free** equation. Reach for it whenever t is neither given nor asked. |
| Δx = ½(v₀ + v)t | m | Uses **average** velocity, which equals (v₀+v)/2 **only** at constant a. |
| **F = ma** | N = kg·m/s² | F is the **net** force. Every "find the acceleration" problem is a free-body diagram first. |
| F_f = μN | N | **N ≠ mg on an incline** — there N = mg cos θ. And **static friction is F ≤ μ_s N, an inequality**: it takes whatever value is needed up to the max. |
| F_c = mv²/r | N | Centripetal force is a **requirement, not a new force**. Something real (tension, gravity, friction, normal) supplies it. Also: it does **no work** — it is always perpendicular to velocity. |
| F = −kx | N | The minus sign is the whole content: **restoring**. x is displacement from equilibrium, not total length. |
| F_g = Gm₁m₂/r² | N | r is measured **center to center**, not surface to surface. |
| **τ = rF sin θ** | N·m | θ is between **r and F**; r sin θ is the **perpendicular lever arm**. AAMC excludes cross products, so torque is always a magnitude-plus-direction question, never a vector computation. |
| p = mv, J = FΔt = Δp | kg·m/s, N·s | Momentum is conserved in **all** collisions; kinetic energy only in **elastic** ones. Perfectly inelastic = they stick together. |

### 5.2 Energy, work, power

| Equation | Units | The thing people get wrong |
|---|---|---|
| KE = ½mv² | J | Scales with **v²** — double the speed, quadruple the energy. |
| PE = mgh | J | h is measured from **whatever zero you chose**; only ΔPE is physical. |
| PE_spring = ½kx² | J | x from equilibrium, and it is squared — so compression and extension store equally. |
| **W = Fd cos θ** | J = N·m | θ is between **force and displacement**. **W = 0 when they are perpendicular** — this is why the normal force, centripetal force, and magnetic force never do work. |
| W_net = ΔKE | J | The work-energy theorem. Faster than kinematics whenever speed, not time, is the target. |
| P = W/t = Fv | W = J/s | Power is a **rate**. "How much" is energy; "how fast" is power. |
| Mechanical advantage = F_out/F_in | — | A machine multiplies **force**, never **energy**. Trading force for distance is the whole idea. |

### 5.3 Fluids

| Equation | Units | The thing people get wrong |
|---|---|---|
| ρ = m/V | kg/m³ | Specific gravity = ρ/ρ_water and is **dimensionless**. SG > 1 sinks in water. |
| P = F/A | Pa = N/m² | Pressure is a **scalar** and acts in all directions. |
| **P = P₀ + ρgh** | Pa | Depends on **depth only** — the shape and volume of the container are irrelevant (hydrostatic paradox). Gauge pressure omits P₀; absolute includes it. |
| **F_b = ρ_fluid · V_displaced · g** | N | Uses the **fluid's** density and the **submerged** volume, not the object's. Floating fraction submerged = ρ_object/ρ_fluid. |
| **A₁v₁ = A₂v₂** | m³/s | Narrower → **faster**. Apply to the *total* cross-section: capillaries are individually tiny but enormous in aggregate, so blood is **slowest** there. |
| **P + ρgh + ½ρv² = constant** | Pa | **Faster fluid = LOWER pressure.** Valid only for ideal flow — nonviscous, incompressible, streamline. Not for a stenosed vessel with turbulence. |
| Q = πr⁴ΔP / 8ηL | m³/s | **r to the FOURTH power.** Halving a vessel radius cuts flow 16-fold. This one factor dominates every circulation passage. |
| Q = A·v | m³/s | Flow rate (volume/time) vs flow speed (distance/time) — the two are not the same quantity. |

### 5.4 Waves, sound, periodic motion

| Equation | Units | The thing people get wrong |
|---|---|---|
| v = fλ | m/s | **v is set by the medium; f is set by the source.** When a wave crosses into a new medium, **f stays fixed and λ changes.** |
| f = 1/T | Hz = s⁻¹ | — |
| T = 2π√(m/k) | s | Spring period is **independent of amplitude and of gravity**. |
| T = 2π√(L/g) | s | Pendulum period is **independent of mass** (small angles only). |
| Open pipe / string: fₙ = nv/2L, n = 1,2,3… | Hz | All harmonics present. |
| **Closed pipe: fₙ = nv/4L, n = 1,3,5… only** | Hz | **Odd harmonics only**, and the fundamental is **half** that of the equivalent open pipe. |
| β = 10 log(I/I₀), I₀ = 10⁻¹² W/m² | dB | **Logarithmic**: ×10 intensity = **+10 dB**, ×100 = +20 dB. Doubling intensity ≈ +3 dB. |
| I = P/A ∝ 1/r² | W/m² | Doubling the distance quarters intensity = **−6 dB**. |
| f′ = f (v ± v_o)/(v ∓ v_s) | Hz | Don't memorize the signs — ask **"is the gap closing?"** Closing → higher pitch. Opening → lower. Then pick the sign that produces that. |

### 5.5 Optics and light

| Equation | Units | The thing people get wrong |
|---|---|---|
| n = c/v | — | **n ≥ 1 always**; light slows in matter. |
| n₁ sin θ₁ = n₂ sin θ₂ | — | Angles from the **normal**, not the surface. Into a denser medium → bends **toward** the normal. |
| sin θ_c = n₂/n₁ | — | Total internal reflection requires **n₁ > n₂** — going from dense to less dense only. |
| **1/f = 1/o + 1/i** | m⁻¹ | Sign conventions are the entire question. **Converging lens and concave mirror: f > 0. Real image: i > 0** (and real images are on the far side for lenses, the same side for mirrors). |
| m = −i/o = h_i/h_o | — | **Negative m = inverted = real.** Positive m = upright = virtual. |
| f = R/2 (mirrors) | m | Mirrors only. |
| P = 1/f | **diopters, f in METERS** | Converting cm→m is where this is lost. Lenses in contact: **P_total = P₁ + P₂**. |
| E = hf = hc/λ | J | Energy ∝ f, **inversely** ∝ λ. Short wavelength = high energy. |
| KE_max = hf − W | J | Photoelectric: **below the threshold frequency, nothing happens no matter how intense the light.** Intensity sets the *number* of electrons, frequency sets their *energy*. |

### 5.6 Electricity, magnetism, circuits

| Equation | Units | The thing people get wrong |
|---|---|---|
| F = kq₁q₂/r² | N | Same 1/r² form as gravity, but charge comes in both signs → attraction or repulsion. |
| E = F/q = kQ/r² | N/C = V/m | **E is a VECTOR** — add components. Field lines run from + to −. |
| **V = kQ/r** | V = J/C | **V is a SCALAR** — just add the numbers. Note the **1/r**, not 1/r². This scalar/vector split is the most common electrostatics error. |
| U = qV, W = qΔV | J | A **positive** charge moves spontaneously from high V to low V; a **negative** charge does the opposite. |
| I = ΔQ/Δt | A = C/s | Conventional current is the direction **positive** charge would move — opposite to electron flow. |
| **V = IR** | V, A, Ω | — |
| R = ρL/A | Ω | **Longer = more resistance; thicker = less.** ρ is resistivity, a material property. |
| Series R: R_eq = ΣR; Parallel: 1/R_eq = Σ1/R | Ω | Parallel R_eq is **smaller than the smallest** resistor. Series shares **current**; parallel shares **voltage**. |
| **Capacitors are the mirror image** | F | **Series: 1/C_eq = Σ1/C. Parallel: C_eq = ΣC.** Backwards from resistors — this is the trap. |
| C = Q/V; C = κε₀A/d | F = C/V | Inserting a dielectric (κ > 1) **raises C**. At constant charge it **lowers V**. |
| U = ½CV² = ½QV = Q²/2C | J | Which form to use depends on what is held constant (a battery holds V; a disconnected capacitor holds Q). |
| P = IV = I²R = V²/R | W | — |
| **F = qvB sin θ** | N | Magnitude only — **direction by right-hand rule**, which is exactly why AAMC excludes cross products. **F = 0 when v ∥ B**, and the force is always ⊥ to v, so a magnetic field **does no work** and can only change direction, giving circular motion. |

### 5.7 Electrochemistry

| Equation | Units | The thing people get wrong |
|---|---|---|
| E°_cell = E°_cathode − E°_anode | V | Both taken as **reduction** potentials; do **not** multiply by stoichiometric coefficients — E° is intensive. |
| **ΔG° = −nFE°_cell** | J | The bridge between thermo and electrochem. **E° > 0 ⟺ ΔG° < 0 ⟺ K > 1 ⟺ spontaneous ⟺ galvanic.** |
| E = E° − (0.0592/n)·log Q (25 °C) | V | As the cell discharges, Q rises and E falls; **at equilibrium E = 0** — that is a dead battery, not E°. |
| mol deposited = It/(nF) | mol | Faraday's law. **F = 96,485 C per mole of electrons**; n is electrons per ion. |
| — | — | **Oxidation is at the ANODE in both cell types** ("an ox, red cat"). Only the **electrode sign flips**: galvanic anode is **negative**, electrolytic anode is **positive**. |

### 5.8 Thermodynamics and thermochemistry

| Equation | Units | The thing people get wrong |
|---|---|---|
| ΔU = Q − W | J | Sign convention: W is work **done by** the system. |
| **ΔG = ΔH − TΔS** | J/mol | **T must be in KELVIN**, and ΔS is usually tabulated in J while ΔH is in kJ. Unit mismatch is the #1 error on this equation. |
| **ΔG° = −RT ln K** | J/mol | Relates the **standard** state to K. K > 1 ⟺ ΔG° < 0. |
| ΔG = ΔG° + RT ln Q | J/mol | **ΔG°, not ΔG, is what's fixed.** Actual spontaneity depends on current concentrations. ΔG = 0 at equilibrium. |
| q = mcΔT | J | Only **within** a phase. |
| q = mL | J | Only **at** a phase change, where ΔT = 0. Mixing the two up is the classic heating-curve error. |
| ΔH°_rxn = ΣΔH°_f(products) − ΣΔH°_f(reactants) | kJ/mol | **ΔH°_f of any element in its standard state = 0.** Hess's law: reverse a reaction → flip the sign; scale it → scale ΔH. |
| — | — | ΔH < 0 and ΔS > 0 → spontaneous at **all** T. ΔH > 0 and ΔS < 0 → **never**. Mixed signs → temperature decides, and **T = ΔH/ΔS** is the crossover. |

### 5.9 Gases

| Equation | Units | The thing people get wrong |
|---|---|---|
| PV = nRT | — | **T in Kelvin, always.** Pick R to match your pressure unit (0.0821 for atm, 8.314 for Pa). |
| P₁V₁/T₁ = P₂V₂/T₂ | — | Drop out whatever is constant. |
| P_total = ΣP_i ; P_i = X_i·P_total | atm | Mole **fraction**, not mass fraction. |
| r₁/r₂ = √(M₂/M₁) | — | Graham: **lighter gas effuses FASTER** — the mass is in the denominator of the faster gas. |
| KE_avg = (3/2)kT ; v_rms = √(3RT/M) | J ; m/s | **Average KE depends only on temperature** — at the same T, all gases have equal KE but different speeds. |
| 22.4 L/mol at STP (0 °C, 1 atm) | L/mol | STP is **0 °C**, not 25 °C. Real gases deviate at **high P and low T** (where volume and attractions stop being negligible). |

### 5.10 Solutions, acids and bases

| Equation | Units | The thing people get wrong |
|---|---|---|
| M = mol solute / **L solution** | mol/L | Molarity uses liters of **solution**; molality uses kg of **solvent**. Molality is temperature-independent, molarity is not. |
| M₁V₁ = M₂V₂ | — | Dilution only — moles conserved. |
| pH = −log[H⁺]; pH + pOH = 14 | — | The 14 holds **only at 25 °C**. Each pH unit is a **10×** change. |
| K_a·K_b = K_w ; pK_a + pK_b = 14 | — | For a **conjugate pair only**. Stronger acid → weaker conjugate base. |
| **pH = pK_a + log([A⁻]/[HA])** | — | Henderson-Hasselbalch. **At half-equivalence, [A⁻] = [HA] so pH = pK_a** — that point is the buffer's center and its maximum capacity. Buffering range is **pK_a ± 1**. |
| — | — | At the **equivalence point** of a weak acid + strong base titration, pH > 7 (the conjugate base hydrolyzes). Equivalence ≠ neutral except for strong/strong. |
| K_sp | varies | Common-ion effect **decreases** solubility. Solubility of a salt of a **weak acid rises as pH falls**. |
| ΔT_b = i·K_b·m ; ΔT_f = i·K_f·m | °C | **i = van 't Hoff factor** — particles per formula unit (NaCl = 2, CaCl₂ = 3, glucose = 1). Forgetting i is the standard error. Freezing point goes **down**, boiling point **up**. |
| Π = iMRT | atm | Osmotic pressure. Same i problem; T in Kelvin. |

### 5.11 Kinetics and enzymes

| Equation | Units | The thing people get wrong |
|---|---|---|
| rate = k[A]^m[B]^n | M/s | **Orders come from experiment, NEVER from stoichiometry.** Overall order = m + n. |
| Zero order: [A] = [A]₀ − kt, t½ = [A]₀/2k | k in M/s | Linear on a plot of **[A] vs t**. |
| **1st order: ln[A] = ln[A]₀ − kt, t½ = 0.693/k** | k in s⁻¹ | **Half-life is independent of concentration** — the defining feature. Linear on **ln[A] vs t**. |
| 2nd order: 1/[A] = 1/[A]₀ + kt, t½ = 1/(k[A]₀) | k in M⁻¹s⁻¹ | Linear on **1/[A] vs t**. |
| k = Ae^(−Ea/RT) | — | **A catalyst lowers Ea and speeds both directions equally. It does NOT change ΔG, ΔH, or K** — only how fast equilibrium is reached. |
| **v = V_max[S]/(K_m + [S])** | M/s | **K_m = [S] at ½V_max.** Low K_m = **high** affinity. K_m is an intrinsic property; V_max scales with enzyme concentration. |
| 1/v = (K_m/V_max)(1/[S]) + 1/V_max | — | Lineweaver-Burk: **y-intercept = 1/V_max, x-intercept = −1/K_m, slope = K_m/V_max.** A **higher** y-intercept means a **lower** V_max — the reciprocal axes invert every intuition. |

**Enzyme inhibition — the four-row table that answers all of them:**

| Inhibitor | Binds | K_m | V_max | Lineweaver-Burk | Overcome by ↑[S]? |
|---|---|---|---|---|---|
| **Competitive** | active site, **free E only** | **↑** | **unchanged** | lines meet on the **y-axis** | **yes** |
| **Noncompetitive** | allosteric, **E and ES equally** | unchanged | **↓** | lines meet on the **x-axis** | no |
| **Uncompetitive** | allosteric, **ES only** | **↓** | **↓** | **parallel lines** | no |
| **Mixed** | allosteric, unequal affinity | ↑ or ↓ | **↓** | intersect off both axes | no |

Uncompetitive lowering K_m looks wrong until you see it: binding ES pulls the equilibrium toward ES (Le Châtelier), which makes the enzyme *appear* to bind substrate better while capping throughput.

### 5.12 Nuclear, and miscellaneous

| Equation | Units | The thing people get wrong |
|---|---|---|
| N = N₀(½)^(t/t½) | — | Exponential decay is **linear on a semilog plot** — and semilog reading is explicitly in AAMC's math scope. |
| E = mc² | J | Mass defect: the **binding energy** is the missing mass. |
| α decay: A−4, Z−2 · β⁻: Z+1 (n→p) · β⁺: Z−1 · γ: no change | — | β⁻ **increases** atomic number. γ changes neither A nor Z. |
| % yield = actual/theoretical × 100 | % | Theoretical yield comes from the **limiting** reactant. |
| Q = ΔP/R ; CO = HR × SV | — | The physiology analogue of V = IR. Resistances in the systemic circulation add in **series**; parallel organ beds **lower** total resistance. |

---

## 6. LAB TECHNIQUES

### 6.1 Electrophoresis and gels

| Technique | Separates on | Readout | The discriminating detail |
|---|---|---|---|
| **SDS-PAGE** | **Molecular weight only** | Lanes of horizontal **bands**; small proteins run **farther** (toward the **anode**, bottom of the gel). A MW ladder in one lane calibrates it | SDS is an **anionic detergent** that denatures the protein and coats it with a **uniform negative charge-to-mass ratio**, erasing native charge and shape so only mass matters. β-mercaptoethanol / DTT reduces disulfides. **A multimer therefore appears as its separate subunits** — a 200 kDa tetramer runs as one 50 kDa band. **log(MW) vs migration distance is linear** (a semilog read) |
| **Native PAGE** | **Mass, charge, AND shape together** | Bands, but **MW cannot be read off them** | The protein stays **folded and active** — so this is the gel you run when you need to recover function (in-gel activity stain) or preserve a complex. The cost is that you can no longer interpret migration distance |
| **Isoelectric focusing (IEF)** | **pI** | Sharp **focused bands**, positioned by pI along a pH gradient | The protein migrates through an immobilized pH gradient until it reaches **pH = pI**, where net charge is zero and it stops. Self-sharpening: drift in either direction gives it a charge that pushes it back |
| **2-D gel** | **pI, then MW** | **Spots** scattered on a plane — x-axis pI, y-axis MW | IEF first, then SDS-PAGE at right angles. Resolves thousands of proteins; the standard proteomics figure |
| **Agarose gel (DNA)** | **Size** (and, at fixed length, conformation) | Bands under UV with a DNA stain | DNA has a **uniform charge/mass ratio already** (the phosphate backbone) — no SDS needed. **Supercoiled DNA runs faster than linear of the same length** |

**Direction rule for every gel:** nucleic acids and SDS-coated proteins are negative, so they run **toward the positive electrode (anode)**. In IEF and native PAGE the direction depends on the molecule's own charge.

### 6.2 Chromatography

| Type | Separates on | What elutes first | Readout |
|---|---|---|---|
| **Size-exclusion (gel filtration)** | **Size / hydrodynamic radius** | **LARGE first.** Big molecules cannot enter the porous beads, so they take the short path around them; small molecules detour through the pores | Elution profile — A280 vs elution volume; large-species peak comes out at a **small** elution volume |
| **Ion-exchange** | **Net charge** | The species with **charge matching the resin** (i.e. that does not bind) comes off first; bound species elute in order of increasing charge as salt rises | Elution profile against a **salt or pH gradient**. **Cation exchange** = negatively charged resin, retains **positive** proteins. **Anion exchange** = positively charged resin, retains **negative** proteins |
| **Affinity** | **Specific biological binding** — antibody, substrate analog, His-tag/Ni-NTA | Everything **except** the target passes straight through | Nearly pure single band from one step. Elute by **competing with free ligand** (or imidazole for His-tags, or a pH shift) |
| **TLC / paper** | **Polarity** (partition between phases) | — | Spots on a plate; **R_f = distance spot travels / distance solvent front travels**, between 0 and 1. **Normal phase (polar silica): polar compounds stick → LOW R_f.** Reverse phase inverts this |
| **Gas chromatography (GLC)** | **Volatility (boiling point) + interaction with the column** | Most volatile first | Chromatogram — peaks vs **retention time**; **peak area ∝ amount** |
| **HPLC** | Same principles, driven at high pressure | — | Same chromatogram, much better resolution |

Two non-chromatographic separations AAMC lists alongside these: **distillation** separates on **boiling point**, and **extraction** separates on **partitioning between two immiscible solvents** — the acid-base trick being to deprotonate (or protonate) a compound into a charged salt so it moves into the **aqueous** layer.

**The size-exclusion trap:** large elutes first. This is backwards from SDS-PAGE, where large moves slowest. Both are "size," and they run in opposite directions.

### 6.3 The blots

**SNoW DRoP** — **S**outhern/**D**NA, **No**rthern/**R**NA, **W**estern/**P**rotein.

| Blot | Detects | Probe | Readout | What the experiment is actually asking |
|---|---|---|---|---|
| **Southern** | **DNA** | labeled complementary **DNA probe** (hybridization) | bands | Is the gene present? How many copies? Is a restriction site altered? |
| **Northern** | **RNA** | labeled complementary probe | bands | **Is the gene being transcribed, and at what level / what transcript size?** |
| **Western** | **Protein** | **primary antibody**, then labeled **secondary antibody** | bands | **Is the protein present, at what size, at what abundance?** |

All three follow the identical shape: **separate by electrophoresis → transfer to a membrane → probe → visualize.** The only variables are the analyte and the probe chemistry.

Reasoning use: **Northern positive but Western negative** means the message is made but the protein is not — a translational or protein-stability defect. **Southern positive, Northern negative** means the gene is there but silenced. That inference chain is the reason AAMC tests blots at all.

### 6.4 PCR and ELISA

**PCR — exponential amplification of one defined DNA sequence.**

| Step | Temp | What happens |
|---|---|---|
| **Denature** | ~95 °C | strands separate |
| **Anneal** | ~50–65 °C | **two primers** bind the flanking sequences |
| **Extend** | ~72 °C | **Taq polymerase** (thermostable, from a hot-spring organism) synthesizes 5′→3′ |

Requires: template, **two primers that define the product**, dNTPs, thermostable polymerase, Mg²⁺. **n cycles → 2ⁿ copies.** Readout: a **single band of predicted size** on an agarose gel.

- **qPCR (real-time)**: readout is **fluorescence vs cycle number**; the reported number is the **C_t** (threshold cycle). **Lower C_t = more starting template.** It is inverse and logarithmic — that inversion is the trap.
- **RT-PCR**: **reverse transcriptase** makes cDNA from mRNA first, so the assay measures **expression**, not genomic content. cDNA has **no introns** — which is why a cDNA-derived product is shorter than the genomic one, and why cDNA is what you clone for bacterial expression.

**ELISA — quantifies a specific antigen (or antibody) in solution.**

Sandwich format: plate-bound **capture antibody** → sample antigen → **detection antibody** → **enzyme-conjugated secondary** → substrate → **color**. Readout: **absorbance per well in a 96-well plate**, converted to concentration against a **standard curve**. It is quantitative.

**Western vs ELISA — the discriminator:** Western tells you **size and identity** (it runs a gel first) but is only semi-quantitative. ELISA tells you **concentration** precisely but gives you no size information and depends entirely on antibody specificity. Choose by whether the question is "which protein / what size" or "how much."

### 6.5 The rest of the toolkit

| Technique | Separates / measures | Readout |
|---|---|---|
| **Differential centrifugation** | **density and size** | Successive pellets at increasing speed: **nuclei → mitochondria/chloroplasts → membranes/microsomes → ribosomes → cytosol** stays in the supernatant |
| **Sanger (dideoxy) sequencing** | DNA sequence | **ddNTPs lack a 3′-OH → chain termination.** A nested ladder of fragments; modern version reads as **four-color fluorescence peaks** |
| **Mass spectrometry** | **mass-to-charge ratio (m/z)** | Peak spectrum; the tallest is the base peak, the highest-m/z the molecular ion |
| **X-ray crystallography** | atomic structure | Electron-density map → 3D model. **Requires a crystal**; captures a static, often non-physiological state |
| **NMR** | structure in solution; chemical environment of nuclei | Spectrum: **chemical shift** (environment), **integration** (how many H), **splitting n+1** (neighbors) |
| **Edman degradation** | N-terminal sequence, one residue at a time | Reads ~50 residues; **blocked N-terminus defeats it** |
| **UV-Vis / Beer's law: A = εlc** | concentration | Absorbance; linear in concentration only within range. **A280 for protein, A260 for nucleic acid** |
| **Flow cytometry / FACS** | cell size, granularity, surface markers | Scatter plots; sorts live cells |

### 6.6 Decision table — pick the technique from the question

| The question being asked | The technique |
|---|---|
| How big is this protein? | SDS-PAGE |
| Is this protein a multimer, and how many subunits? | SDS-PAGE **with and without** reducing agent, or native vs SDS |
| What is this protein's pI? | Isoelectric focusing |
| Purify one specific protein in one step | Affinity chromatography |
| Separate proteins of similar size but different charge | Ion-exchange |
| Separate a large complex from free subunits | Size-exclusion |
| Is the gene present in the genome? | Southern / PCR |
| Is the gene being transcribed? | Northern / RT-qPCR |
| Is the protein being made? | Western |
| How much of this protein is in the serum? | ELISA |
| Which cells express this surface marker? | Flow cytometry |
| Did I get the right clone? | PCR + restriction digest + sequencing |

---

## 7. GENETICS

### 7.1 The ratios

| Cross | Phenotypic ratio | Genotypic ratio | Note |
|---|---|---|---|
| Aa × Aa (monohybrid) | **3 : 1** | 1 : 2 : 1 | The default. Seeing 3:1 means one gene, complete dominance, both parents heterozygous |
| Aa × aa (**testcross**) | **1 : 1** | 1 : 1 | The cross that reveals an unknown dominant's genotype: any recessive offspring proves the parent was Aa |
| AA × aa | all dominant | all Aa | F₁ generation of a classic Mendel cross |
| AaBb × AaBb (dihybrid) | **9 : 3 : 3 : 1** | — | **Requires independent assortment.** Total 16 |
| AaBb × aabb (dihybrid testcross) | **1 : 1 : 1 : 1** | — | Deviation from 1:1:1:1 here is the **signature of linkage** |
| **Incomplete dominance** Aa × Aa | **1 : 2 : 1** | 1 : 2 : 1 | Heterozygote is an intermediate **blend** (pink flower). **Phenotypic ratio equals genotypic ratio** — that identity is the tell |
| **Codominance** Aa × Aa | **1 : 2 : 1** | 1 : 2 : 1 | Heterozygote expresses **both alleles fully and separately** (AB blood, sickle trait on electrophoresis) — not a blend |
| Homozygous-**lethal** dominant, Aa × Aa | **2 : 1** | 2 : 1 | A ratio of 2:1 is the fingerprint of a lethal allele: the AA class is missing |
| Epistasis (two genes, one masks the other) | **9:7, 9:3:4, 12:3:1, 15:1, 13:3** | — | Any ratio still summing to **16** but not 9:3:3:1 means **gene interaction**, not linkage |

**Do not draw a 16-box Punnett square.** Use the product rule: solve each gene separately as a 3:1 or 1:1, then multiply the probabilities. "Chance of A_bbCc" = P(A_) × P(bb) × P(Cc). **AND → multiply. OR → add.**

**Incomplete vs codominance in one line:** incomplete = the heterozygote is a **new intermediate**; codominant = **both parental phenotypes appear simultaneously**.

**ABO blood:** I^A and I^B are **codominant**; i is recessive. Type O (ii) is the universal **donor**; AB the universal **recipient**. Type O individuals carry **anti-A and anti-B antibodies**; AB individuals carry neither. The **Rh** locus is separate and simple dominant.

### 7.2 Pedigrees — the one-step identification

| Pattern | The single observation that identifies it | Corroborating features | Classic examples |
|---|---|---|---|
| **Autosomal dominant** | **No skipping — every affected person has an affected parent.** Vertical, generation after generation | ~50% of offspring affected; sexes equal; **male-to-male transmission occurs** | Huntington's, Marfan, achondroplasia, familial hypercholesterolemia, neurofibromatosis |
| **Autosomal recessive** | **Two unaffected parents produce an affected child.** That one fact proves recessive | Skips generations (horizontal — affected siblings); sexes equal; **consanguinity** raises incidence | Cystic fibrosis, sickle cell, Tay-Sachs, PKU, albinism |
| **X-linked recessive** | **Far more males than females affected, and NO male-to-male transmission** | An affected male's **daughters are all obligate carriers**; an affected mother's **sons are all affected**; transmitted silently through carrier mothers | Hemophilia A and B, Duchenne, red-green color blindness, G6PD deficiency |
| **X-linked dominant** | **An affected father has ALL daughters affected and NO sons affected** | Affected mother → ~50% of children of either sex; no male-to-male | Hypophosphatemic (vitamin-D-resistant) rickets |
| **Mitochondrial** | **Only mothers transmit it — an affected father transmits to no one** | An affected mother passes it to **all** children of both sexes; **heteroplasmy** produces highly variable severity | LHON, MELAS, MERRF |
| **Y-linked** | Father → **all** sons, **no** daughters | Vanishingly rare; very few genes on Y | — |

**The two moves that decide almost every pedigree question:**
1. **Look for two unaffected parents with an affected child.** If present → **recessive** (and if the child is female, it is almost certainly **autosomal** recessive). If absent and the trait runs in every generation → **dominant**.
2. **Then check for male-to-male transmission.** An affected father with an affected son **rules out anything X-linked** — a father hands his son a Y, never an X. If it's recessive with a strong male skew and no father-to-son transmission → **X-linked recessive**.

Two vocabulary items that explain otherwise-broken pedigrees: **incomplete penetrance** (a person carries the genotype but shows no phenotype — makes a dominant trait appear to skip) and **variable expressivity** (same genotype, different severity). **Pleiotropy** is one gene affecting many traits; **imprinting** is expression depending on parent of origin.

### 7.3 Hardy-Weinberg

**p + q = 1**  ·  **p² + 2pq + q² = 1**

| Term | Means |
|---|---|
| **p** | frequency of the dominant allele |
| **q** | frequency of the recessive allele |
| **p²** | frequency of **homozygous dominant** individuals |
| **2pq** | frequency of **heterozygotes (carriers)** |
| **q²** | frequency of **homozygous recessive** individuals |

**The five conditions** (violate any one and the population evolves): **no mutation · no migration/gene flow · no natural selection · random mating · infinitely large population (no genetic drift).**

**The traps:**
- **Start from q², not q.** With complete dominance the only phenotype you can count directly is the recessive one, and **that count is q²**. So **q = √(recessive phenotype frequency)**, then p = 1 − q. Nearly every missed HW problem is someone setting q equal to the observed frequency.
- **Carrier frequency is 2pq, not pq.** The factor of 2 is because Aa and aA are both heterozygotes.
- **Heterozygotes are maximized at p = q = 0.5**, where 2pq = 0.50. Carrier frequency can never exceed half the population.
- **The dominant allele is not necessarily the common one.** Dominance describes expression, not frequency. HW's central claim is that **allele frequencies do not drift on their own** — dominance alone changes nothing across generations.
- **X-linked loci: in males, allele frequency = phenotype frequency**, because males are hemizygous. So the frequency of color blindness in men *is* q, while in women it is q². This is why X-linked recessive conditions are so much more common in males.
- **A heterozygote advantage keeps a deleterious allele in the population** — sickle-cell (HbS) heterozygotes resist malaria, so q stays far above what selection against homozygotes alone would predict. This is balancing selection, and it is a *violation* of HW, not an application of it.

### 7.4 Linkage and mapping

- **Recombination frequency (RF) = recombinant offspring / total offspring × 100.**
- **1 map unit = 1 centimorgan = 1% recombination.**
- **RF = 50% means unlinked** — either on different chromosomes or so far apart on the same one that crossing over is guaranteed. **RF cannot exceed 50%.**
- Closer genes → **lower** RF → fewer recombinants. Map distances are additive over short intervals (A-B + B-C ≈ A-C).
- A dihybrid testcross that yields something other than **1:1:1:1** is showing linkage; the two **overrepresented** classes are the parental types, the two rare ones are the recombinants.

**Chi-square goodness of fit: χ² = Σ (O − E)² / E.** Large χ² → observed departs from expected → the model (independent assortment, or HW equilibrium) is rejected. df = (number of classes − 1).

---

## 8. VITAMINS AND COFACTORS

### 8.1 Vocabulary — sorted first, because AAMC tests the distinction

| Term | Means |
|---|---|
| **Cofactor** | any non-protein helper — the broad category, includes metal ions |
| **Coenzyme** | an **organic** cofactor, almost always **vitamin-derived** |
| **Prosthetic group** | a cofactor bound **tightly or covalently** and never released (FAD in succinate dehydrogenase, heme, biotin) |
| **Cosubstrate** | a cofactor that **binds, reacts, dissociates, and is recycled elsewhere** (NAD⁺, CoA) |
| **Apoenzyme / Holoenzyme** | protein **without** its cofactor (inactive) / **with** it (active) |

### 8.2 Water-soluble vitamins

| Vitamin | Coenzyme form | **Reaction type it enables** | Deficiency / anchor |
|---|---|---|---|
| **B1 Thiamine** | **TPP** (thiamine pyrophosphate) | **Oxidative decarboxylation of α-keto acids** — PDH, α-KGDH, branched-chain KDH. Also **transketolase** (PPP) | Beriberi; Wernicke-Korsakoff |
| **B2 Riboflavin** | **FAD / FMN** | **Redox** — flavins can carry **one or two** electrons, which is why they interface between 2e⁻ donors and 1e⁻ acceptors (Complex I/II). Handles the less favorable oxidations, e.g. creating C=C bonds in acyl-CoA dehydrogenase and succinate DH | Cheilosis, corneal vascularization |
| **B3 Niacin** | **NAD⁺ / NADP⁺** | **Redox — 2-electron hydride transfer.** Used for C=O ⟷ C–OH oxidations | **Pellagra: dermatitis, diarrhea, dementia.** Synthesized from **tryptophan** |
| **B5 Pantothenic acid** | **Coenzyme A** (and ACP) | **Acyl-group activation and transfer** — the thioester bond is high-energy | Rare |
| **B6 Pyridoxine** | **PLP** (pyridoxal phosphate) | **Amino-group chemistry** — **transamination, decarboxylation, deamination**; also glycogen phosphorylase. If nitrogen is moving, it is PLP | Sideroblastic anemia, neuropathy |
| **B7 Biotin** | **carboxybiotin** | **Carboxylation — CO₂ transfer.** Pyruvate carboxylase, acetyl-CoA carboxylase, propionyl-CoA carboxylase | Bound and blocked by **avidin** in raw egg white |
| **B9 Folate** | **THF** (tetrahydrofolate) | **One-carbon transfer** at the methyl/methylene/formyl level — **purine and thymidylate synthesis** | Megaloblastic anemia; **neural tube defects** |
| **B12 Cobalamin** | **methyl-** and **adenosyl-cobalamin** | **Methyl transfer** (homocysteine → methionine) and the **methylmalonyl-CoA mutase rearrangement** (odd-chain fatty acids) | Requires **intrinsic factor**. Megaloblastic anemia **plus neurological damage** |
| **C Ascorbate** | not a classic coenzyme — a **reducing agent** | Keeps **Fe²⁺ reduced** for **prolyl and lysyl hydroxylase** → **collagen crosslinking**; enhances dietary iron absorption; antioxidant | **Scurvy** — poor wound healing, bleeding gums |

### 8.3 Fat-soluble vitamins — **A D E K**

| Vitamin | Active form | Reaction / role | Deficiency |
|---|---|---|---|
| **A** | **retinal** (vision) / **retinoic acid** (transcription) | **11-cis-retinal** is the chromophore in **rhodopsin** — photon absorption isomerizes it to all-trans, triggering transduction. Retinoic acid acts as a **nuclear-receptor ligand** controlling differentiation | Night blindness, xerophthalmia |
| **D** | **calcitriol, 1,25-(OH)₂-D₃** | Not really a vitamin — a **steroid hormone**. Made in skin from **7-dehydrocholesterol + UV**, **25-hydroxylated in liver**, **1α-hydroxylated in kidney under PTH**. Raises intestinal absorption of **Ca²⁺ and phosphate** | Rickets (children), osteomalacia (adults) |
| **E** | tocopherol | **Lipid-phase antioxidant** — terminates radical chain reactions in **membranes** | Hemolytic anemia, neuropathy |
| **K** | phylloquinone / menaquinone | Cofactor for **γ-glutamyl carboxylase** → **γ-carboxylation of glutamate** in clotting factors **II, VII, IX, X and proteins C and S**, creating the Ca²⁺-binding sites | Bleeding. **Warfarin blocks vitamin K epoxide reductase**; newborns get a K shot because gut flora are absent |

**The absorption logic that generates half the questions:** fat-soluble vitamins require bile and are **stored in liver and adipose → deficiency is slow but toxicity is real (A and D especially)**. Water-soluble vitamins are **excreted in urine → deficiency develops fast, toxicity is rare.** The single exception is **B12, which is stored in the liver for years** — which is why B12 deficiency from a vegan diet or pernicious anemia takes so long to appear.

### 8.4 Non-vitamin cofactors

| Cofactor | Role |
|---|---|
| **Mg²⁺** | The **real substrate of every kinase is Mg-ATP** — Mg²⁺ shields the phosphate charge. Also required by DNA and RNA polymerases |
| **Zn²⁺** | **Carbonic anhydrase**, carboxypeptidase, alcohol dehydrogenase, and **zinc-finger transcription factors** — structural as well as catalytic |
| **Fe²⁺/Fe³⁺ (heme)** | O₂ binding (hemoglobin, myoglobin) and **one-electron transfer** in cytochromes. Heme iron is a **prosthetic group** |
| **Cu** | Cytochrome c oxidase (Complex IV), lysyl oxidase |
| **Se** | Glutathione peroxidase |
| **Coenzyme Q (ubiquinone)** | Not a vitamin. The **only lipid-soluble, freely mobile carrier in the inner membrane**; shuttles electrons from Complexes I **and II** to III. Can accept **one or two** electrons |
| **Lipoic acid** | Not a human vitamin. Swinging arm in the PDH / α-KGDH complexes |
| **SAM (S-adenosylmethionine)** | Not a vitamin. The **universal methyl donor** (from methionine + ATP) — DNA methylation, neurotransmitter synthesis. B12 and folate regenerate it |

### 8.5 The organizing table — reaction type → cofactor

This is the version to have loaded on test day. Given a reaction, name the cofactor.

| If the reaction is… | The cofactor is… |
|---|---|
| Oxidation/reduction with **hydride, C=O ⟷ C–OH** | **NAD⁺ / NADP⁺** (B3) |
| Oxidation creating a **C=C double bond**, or interfacing 1e⁻/2e⁻ | **FAD / FMN** (B2) |
| **Adding CO₂ (carboxylation)** | **Biotin** (B7) |
| **Removing CO₂ from an α-keto acid** | **TPP** (B1) |
| **Moving an amino group** — transamination, decarboxylation of an amino acid | **PLP** (B6) |
| **Carrying an acyl group** | **CoA** (B5) |
| **Moving a single carbon** (purine/thymidylate synthesis) | **THF** (B9) |
| **Moving a methyl group**, or a 1,2-carbon rearrangement | **B12**, or **SAM** |
| **Transferring a phosphoryl group** | **ATP** (with Mg²⁺) |
| **Transferring a sugar** | **UDP-glucose** |
| **Single-electron transfer** | **heme iron** in cytochromes, Fe-S clusters |

### 8.6 The three discriminators worth memorizing outright

**NAD⁺ vs NADPH.** Same chemistry, opposite jobs, and the cell keeps them in opposite redox states so both can be thermodynamically favorable at once. **NAD⁺ is kept oxidized and drives CATABOLISM** — it collects electrons from fuel. **NADPH is kept reduced and drives ANABOLISM** — fatty acid and cholesterol synthesis, glutathione reduction, the neutrophil respiratory burst, and steroid hydroxylation. **NADPH comes from the pentose phosphate pathway** (glucose-6-phosphate dehydrogenase). The single phosphate on the 2′-OH of the adenosine ribose is the tag enzymes read to tell them apart.

**Folate vs B12.** Both deficiencies produce **megaloblastic anemia** because both are needed for thymidylate synthesis. **Only B12 deficiency causes neurological damage** (subacute combined degeneration), because only B12 runs methylmalonyl-CoA mutase, and accumulating methylmalonyl-CoA damages myelin. Clinical consequence and standard passage twist: **folate supplementation corrects the anemia while the neurologic damage silently progresses.** Elevated **methylmalonic acid** distinguishes B12; homocysteine is elevated in both.

**Which vitamins are made, not eaten.** **Niacin (B3) from tryptophan · Vitamin D in skin from 7-dehydrocholesterol under UV · Vitamin K by gut flora.** These are the three that break the "vitamins must be ingested" rule, and each one is the basis of a deficiency scenario (pellagra in a corn diet with low tryptophan; rickets with low sun exposure; bleeding in a newborn or after prolonged antibiotics).

---

*End of pack. Everything here is arbitrary — it does not follow from anything else, so it has to be in memory. Anything you can derive was deliberately left out.*
