# MCAT Practice Exam — Content Generation Guide

Reference for creating 90-minute and 60-minute practice sections in DrillRoom.

> **Topic Coverage Tracker:** To see which topics are already built and select uncreated topics for new sections without repeating yourself, see [MCAT-CURRICULUM-AND-TOPIC-TRACKER.md](file:///home/cgslinde/DrillRoom/DrillRoom/MCAT-CURRICULUM-AND-TOPIC-TRACKER.md).

---

## Real MCAT Structure (for reference)

| Section | Code | Time | Passages | Qs per passage | Discrete Qs | Total Qs |
|---------|------|------|----------|---------------|-------------|----------|
| Chem/Phys | C/P | 95 min | 10 | 5–7 | 15 | 59 |
| CARS | CARS | 90 min | 9 | 5–7 | 0 | 53 |
| Bio/Biochem | B/B | 95 min | 10 | 5–7 | 15 | 59 |
| Psych/Soc | P/S | 95 min | 10 | 5–7 | 15 | 59 |

---

## Practice Section Specs

### 90-Minute Practice Section

| Section | Time | Passages | Qs per passage | Discrete Qs | Total Qs |
|---------|------|----------|---------------|-------------|----------|
| C/P | 90 min | 7 | 5–6 | 10 | ~50 |
| CARS | 90 min | 9 | 5–6 | 0 | ~50 |
| B/B | 90 min | 7 | 5–6 | 10 | ~50 |
| P/S | 90 min | 7 | 5–6 | 10 | ~50 |

### 60-Minute Practice Section

| Section | Time | Passages | Qs per passage | Discrete Qs | Total Qs |
|---------|------|----------|---------------|-------------|----------|
| C/P | 60 min | 5 | 5–6 | 5 | ~30 |
| CARS | 60 min | 6 | 5–6 | 0 | ~33 |
| B/B | 60 min | 5 | 5–6 | 5 | ~30 |
| P/S | 60 min | 5 | 5–6 | 5 | ~30 |

---

## MCAT Scoring System

Each section is scored on a scale of **118–132**, with **125** as the median.

### Raw-to-Scaled Score Conversion

The conversion uses a curved scale based on percentage correct:

| % Correct | Scaled Score | Percentile (approx) |
|-----------|-------------|---------------------|
| 95–100% | 132 | 100th |
| 90–94% | 131 | 99th |
| 85–89% | 130 | 98th |
| 80–84% | 129 | 95th |
| 75–79% | 128 | 90th |
| 70–74% | 127 | 82nd |
| 65–69% | 126 | 72nd |
| 60–64% | 125 | 60th |
| 55–59% | 124 | 47th |
| 50–54% | 123 | 35th |
| 45–49% | 122 | 25th |
| 40–44% | 121 | 16th |
| 35–39% | 120 | 9th |
| 30–34% | 119 | 4th |
| 0–29% | 118 | 1st |

**Total Score** = Sum of all 4 section scores (range: 472–528).
- Median: 500
- Competitive: 510+ (80th percentile)
- Top programs: 515+ (92nd percentile)
- Elite: 520+ (98th percentile)

---

## Content Generation Rules

### Passage Construction

1. **Length**: ~320–420 words for science passages (ensuring multi-variable experimental depth); ~550–650 words for CARS (with nuanced dialectical tension)
2. **Structure**: Always include experimental context with data (tables, figures described in text)
3. **Tone**: Scientific, clinical, experiment-based. Mimics journal article tone.
4. **Data tables**: Use HTML table markup with `<th>`, `<td>`, `<td class="n">` for numeric
5. **Title format**: `<div class="ttl">Passage N (Questions 1&ndash;K)</div>`

### Question Construction & AAMC Distractor Engineering

The MCAT does not test trivial trivia; it tests **Scientific Inquiry and Reasoning Skills (SIRS)** using psychometrically calibrated multiple-choice items. To write questions that match or exceed real AAMC difficulty, item writers must adhere to rigorous distractor construction standards.

#### 1. The Psychometric Principle of Distractors
In AAMC psychometrics, every question item is evaluated using the **Point-Biserial Correlation ($r_{pbi}$)**:
* **Correct Answer:** Must exhibit a strong **positive** point-biserial ($r_{pbi} > +0.25$), proving that high-scoring students select it while lower-scoring students miss it.
* **Distractors (Incorrect Options):** Must exhibit a **negative** point-biserial ($r_{pbi} < 0$). This ensures that each wrong answer functions as a plausible attractor for examinees with superficial knowledge, incomplete calculations, or cognitive heuristics, while high-scoring students systematically dismiss it through multi-step reasoning.
* **Non-Functioning Distractors (Prohibited):** A distractor that 0% of students choose is a "dead option." It reduces a 4-option item to a 3- or 2-option item, artificially inflating guessing accuracy. Distractors must **never** be absurd, comedic, or trivially dismissible without reading the passage.

---

#### 2. The 6 Archetypal AAMC Distractor Traps
When constructing incorrect choices, every distractor must be deliberately designed around one of the six classic AAMC trap architectures:

| Trap Archetype | Cognitive Mechanism | Writing Formula / Template | MCAT Example |
| :--- | :--- | :--- | :--- |
| **1. True Fact, Wrong Question** | Exploits recognition memory. The statement is 100% scientifically true, but fails to answer the specific prompt constraint. | `[Undisputed scientific truth]` that belongs to an adjacent pathway or ignores the stem's limiter. | Question asks why a competitive inhibitor changes $K_m$; trap choice states *"The inhibitor binds covalently to an allosteric site to lower $V_{max}$."* |
| **2. Directional / Reciprocal Inversion** | Exploits cognitive fatigue under time pressure. Inverts mathematical proportionality, thermodynamic signs, or feedback loops. | State the inverse parameter: $\uparrow$ instead of $\downarrow$, reciprocal relationship, or wrong regulatory sign. | In a stenosis problem, stating that internal hydrostatic pressure increases proportionally with fluid speed (confusing dynamic pressure $\frac{1}{2}\rho v^2$ with lateral static pressure). |
| **3. Intermediate Calculation (Partial Solve)** | Exploits premature closure during multi-step math. Captures examinees who stop after Step 1. | Insert the mathematical value obtained before completing the final conversion, stoichiometric ratio, or unit adjustment. | In a solution question requiring molarity of $OH^-$ from $Ca(OH)_2$, inserting the molarity of $Ca(OH)_2$ without multiplying by 2 (ignoring stoichiometry). |
| **4. Half-Right Mechanism** | Exploits rapid skimming. The first clause aligns with passage findings, but the explanatory clause cites the wrong driver. | `[Accurate passage observation]` because `[false physiological or chemical mechanism]`. | *"Decreases heart rate by directly inhibiting beta-1 adrenergic receptors in the SA node"* (when the drug is actually a muscarinic M2 agonist). |
| **5. Plausible Alternative Mechanism** | Exploits superficial conceptual categorization. Substitutes an adjacent textbook mechanism. | Swap a mechanism with its closest conceptual cousin in the same organ system or organic reaction class. | In an $S_NAr$ reaction, offering a Meisenheimer intermediate vs an Arenium carbocation intermediate (EAS) vs a Benzyne intermediate. |
| **6. Research Design & Control Fallacy** | Exploits confusion between correlation, causation, and experimental baselines. | Mischaracterize what the vehicle or negative control proves, or extrapolate findings beyond the sample tissue/species. | Claiming that an intervention *"cured glioblastoma"* when the data table only measured *in vitro* mitochondrial membrane potential in isolated cell lines. |

---

#### 3. Structural Parallelism & Anti-Cueing Standards
To prevent examinees from using "test-wiseness" to guess the key without knowing the science:
1. **Length Parity (Strict Symmetry, Ratio &le; 1.08x):**
   - The correct answer must **never** be noticeably longer, more nuanced, or more detailed than the distractors.
   - Keep all four options within $\pm 8\%$ character length (max-to-min character ratio $\le 1.08$). Perfect length symmetry eliminates subconscious length cueing.
2. **Homogeneity of Domain:**
   - All 4 choices must belong to the exact same grammatical and conceptual category (e.g., if Choice A is a hormone, B, C, and D must all be hormones).
3. **Prohibition of Extreme Qualifiers in Distractors:**
   - Avoid words like *always*, *never*, *completely eliminates*, or *solely* in distractors. Astute test-takers instantly eliminate them because biological systems rarely behave absolutely.
4. **Ascending / Descending Numerical Ordering:**
   - Whenever options are numbers, frequencies, or values, list them in strict numerical order (e.g., A: 12 mM, B: 24 mM, C: 48 mM, D: 96 mM).
5. **No "All of the Above" or "None of the Above":**
   - Never used on the real MCAT; allows examinees to arrive at the answer with only partial evaluation.

---

#### 4. CARS-Specific Distractor Engineering
CARS distractors are engineered around subtle rhetorical boundaries:
1. **The "Too Narrow" Trap:** A choice that is directly supported by a sentence in Paragraph 3, but is offered as the answer to a "Main Idea" or "Central Thesis" question.
2. **The "Scope Shift" Trap:** Extrapolates the author's argument beyond the textual evidence by introducing outside moral or sociological assumptions not made in the passage.
3. **The "Author Tone Inversion" Trap:** Subtly shifts the author's nuanced, skeptical critique into an endorsement or active hostility.
4. **The "Opposite Intent" Trap:** Incorporates verbatim vocabulary from the passage, but arranges the terms into an argument the author explicitly refuted.

---

### Explanation Construction

1. **Bold the key principle** at the start
2. **Name why each wrong answer fails** — explicitly identify the AAMC trap archetype for each distractor.
3. **Identify the trap explicitly** — state the exact misconception, calculation error, or cognitive bias that leads to each wrong choice.
4. **Keep it under 120 words** — dense, educational, and clinically precise.

### CARS-Specific Rules

1. **No discrete questions** — CARS is 100% passage-based
2. **Passage sources**: Humanities, social sciences, ethics, philosophy, arts criticism. NO natural science.
3. **Question types**:
   - Foundations of Comprehension: main idea, inference, vocabulary in context
   - Reasoning Within the Text: evaluate arguments, identify assumptions, assess evidence strength
   - Reasoning Beyond the Text: apply ideas to new scenarios, assess impact of new information
4. **Explanations**: Must reference specific paragraph numbers and quote key phrases

---

## The 5/5 Difficulty Standard: Multi-Step Item Review Protocol (The 5-Gate Pipeline)

To guarantee that future practice suites achieve authentic **5/5 AAMC Section Bank / 99th-Percentile Crucible** difficulty (where examinees cannot score 90%+ by skimming or basic intuition), every passage and question generated must pass through a strict **5-Gate Quality & Item Review Pipeline**.

If an item fails ANY gate, it is rejected and rewritten before inclusion.

```
       [ Gate 1: Passage Friction & Data Density Audit ]
                            │ PASS
                            ▼
       [ Gate 2: Cognitive Chain Audit (Min. 3-Step Solve) ]
                            │ PASS
                            ▼
       [ Gate 3: Distractor Trap & Seductiveness Audit ]
                            │ PASS
                            ▼
       [ Gate 4: Visual Symmetry & Heuristic Neutralization ]
                            │ PASS
                            ▼
       [ Gate 5: Pedagogical Autopsy & Explanatory Review ]
                            │ PASS
                            ▼
              [ APPROVED FOR EXAM SUITE ]
```

---

### Gate 1: Passage Friction & Experimental Density Audit
* **Word Count Threshold**:
  - **Science (C/P, B/B, P/S)**: 320–450 words of dense experimental narrative (no fluff, no simplified textbook summaries).
  - **CARS**: 550–650 words of dense, intellectual, humanities/social science prose with dialectical tension.
* **Experimental Perturbation Requirement (Science)**:
  - Every science passage MUST include an experimental intervention: wild-type vs mutant knockout, chemical inhibitor assay, physiological stress, or pharmacological titration.
  - MUST feature at least one quantitative data table or multi-condition assay (e.g., $K_m$, $V_{max}$, relative mRNA fold-change, Western blot densitometry, equilibrium constants).
* **Dialectical Friction Requirement (CARS)**:
  - The author's thesis must be nuanced, qualified, or counter-balanced against a competing school of thought (e.g., Frankfurt School vs Cultural Studies, Internalism vs Externalism, Aristotelian catharsis vs Brechtian epic theater).
  - Passages must NOT have clear "topic-summary" concluding sentences that give away the answers.
* **Gate 1 Pass Criteria**: Passage cannot be summarized in a single elementary sentence; contains multi-variable data requiring cross-referencing.

---

### Gate 2: Cognitive Chain Audit (Minimum 3-Step Solve Rule)
Single-step questions (direct text search, single formula substitution, or rote definitions) are **STRICTLY PROHIBITED**. Every question must require a minimum 3-step cognitive derivation chain:

* **Science 3-Step Solve Architecture**:
  1. **Step 1 (Data Interrogation)**: Extract a specific experimental constraint from the passage or data table (e.g., *Table 1 shows Compound X decreases $V_{max}$ by 50% without altering $K_m$*).
  2. **Step 2 (Biochemical / Physical Law Synthesis)**: Map that constraint to an outside foundational principle not stated in the passage (e.g., *A noncompetitive inhibitor binds with equal affinity to both free enzyme and enzyme-substrate complex*).
  3. **Step 3 (Downstream Deduction / Perturbed State Application)**: Apply the principle to predict the outcome of a novel scenario or solve a secondary physiological/mathematical problem (e.g., *Deduce whether increasing substrate concentration 10-fold will restore reaction velocity to baseline*).
* **CARS 3-Step Solve Architecture**:
  1. **Step 1 (Stated Text & Context)**: Identify the author's nuanced claim and the specific evidence marshaled in Paragraph X.
  2. **Step 2 (Unspoken Premise / Epistemological Core)**: Uncover the unstated assumption linking the author's premise to their conclusion.
  3. **Step 3 (Novel Extrapolation / Reasoning Beyond the Text)**: Evaluate how a novel hypothetical finding, historical counter-example, or philosophical critique strengthens, weakens, or forces revision of that core assumption.
* **Gate 2 Pass Criteria**: Item writer can document all 3 discrete logic nodes. If an examinee can jump directly from stem to answer in 1 step, the item is REJECTED.

---

### Gate 3: Distractor Trap & Seductiveness Audit (Zero Dead Options)
Every item must feature **exactly 3 active, functioning distractors**. Non-functioning distractors (throwaway options, comedic choices, or obviously false claims) artificially inflate the guessing rate to 50% or 100% and reduce difficulty to 1/5.

* **Mandatory Distractor Allocation**:
  1. **Distractor 1: The Primary Seducer (The 50/50 Trap)**
     - Target: 510+ scorers who read carefully but miss a subtle scope boundary.
     - Construction: 95% scientifically or textually accurate, but fails on a razor-thin qualifier: *confuses necessary with sufficient*, *swaps acute vs chronic physiological adaptation*, or *applies a true correlation as absolute causation*.
  2. **Distractor 2: The Directional / Reciprocal Inversion**
     - Target: Examinees operating under time pressure or mental fatigue.
     - Construction: Exactly mirrors the true mathematical derivation or regulatory cascade, but with the sign or direction flipped ($\uparrow$ instead of $\downarrow$, $\Delta G > 0$ instead of $< 0$, reciprocal slope $\frac{1}{V_{max}}$ vs $V_{max}$, or parasympathetic instead of sympathetic).
  3. **Distractor 3: True Fact, Wrong Stem OR Intermediate Step**
     - Target: Examinees relying on passive recognition memory or rushing through multi-step math.
     - Construction: States a 100% indisputable scientific truth that belongs to an adjacent biological pathway or answers an adjacent question, OR presents the numerical answer from Step 1 before the final conversion/stoichiometry is applied.
* **Gate 3 Pass Criteria**: A student scoring 500–505 would find all 4 answer choices highly plausible and defensible upon first reading.

---

### Gate 4: Visual Symmetry & Heuristic Neutralization Audit (Anti-Cueing)
Examinees must be prevented from using test-taking heuristics to bypass the science or reasoning:

1. **Answer Length Symmetry ($\le 1.08x$ Ratio)**:
   - Calculate: $\text{Length Ratio} = \frac{\text{Length of Longest Option (chars)}}{\text{Length of Shortest Option (chars)}}$.
   - **Threshold**: Must be $\le 1.08$ (strict length parity). Correct answers must NEVER be noticeably longer or more qualified than distractors.
2. **Grammatical & Syntactic Parallelism**:
   - All 4 choices must begin with the exact same grammatical structure (all infinitive verbs, all participial phrases, or all full declarative clauses).
3. **Neutralization of Extreme Qualifiers**:
   - Do NOT use *always*, *never*, or *solely* as easy discard flags in distractors. If extreme qualifiers appear, ensure they are balanced or tested deliberately.
4. **Ascending/Descending Numeric Sequencing**:
   - All quantitative choices must be arranged in strict ascending ($A < B < C < D$) or descending order.
5. **The Passage-Dependency Blind Test**:
   - Can an expert reliably answer this question correctly without reading the passage?
   - If YES $\rightarrow$ The question is an isolated discrete question in disguise. Rewrite to anchor it irreversibly to the passage's experimental conditions.
* **Gate 4 Pass Criteria**: Length ratio $\le 1.08$, flawless syntax parallelism, zero visual cues to the keyed answer.

---

### Gate 5: Pedagogical Autopsy & Explanatory Review
Every explanation in the `e` property must serve as a comprehensive post-exam diagnostic:

1. **Bolded Governing Principle**: First sentence states the foundational law, mechanism, or thesis in `<strong>` tags.
2. **Step-by-Step Derivation**: Concise, explicit demonstration of the 3-step cognitive pathway.
3. **Mandatory Distractor Autopsy**:
   - Must explicitly list all 3 wrong choices with bullet points (`&bull;`).
   - Must identify the specific AAMC Trap Archetype in parentheses (e.g., `&bull; B (Directional Inversion): ...`, `&bull; C (True Fact, Wrong Question): ...`, `&bull; D (Scope Creep): ...`).
   - Must explain the exact cognitive flaw or trap architecture that makes that distractor incorrect.
* **Gate 5 Pass Criteria**: Explanations diagnose WHY each wrong choice exists, turning mistakes into actionable cognitive calibration.

---

## Topic Coverage Checklist

### C/P (Chem/Phys)
- [ ] Atomic structure / periodic trends
- [ ] Bonding and intermolecular forces
- [ ] Stoichiometry and chemical reactions
- [ ] Thermochemistry / thermodynamics (ΔG, ΔH, ΔS)
- [ ] Chemical kinetics and rate laws
- [ ] Equilibrium (Ksp, Kp, Kc, Le Châtelier)
- [ ] Acids, bases, and buffers (Henderson-Hasselbalch)
- [ ] Electrochemistry (galvanic/electrolytic cells, Nernst equation)
- [ ] Organic structure and nomenclature
- [ ] Organic reactions (SN1/SN2, E1/E2, additions, substitutions)
- [ ] Stereochemistry (R/S, chirality, optical activity)
- [ ] Spectroscopy (NMR, IR, UV-Vis, mass spec)
- [ ] Kinematics and dynamics (Newton's laws, projectiles)
- [ ] Work, energy, momentum
- [ ] Fluids (Bernoulli, Pascal, buoyancy)
- [ ] Electrostatics and circuits (Ohm's law, Kirchhoff's, capacitors)
- [ ] Waves, sound, light, optics (refraction, diffraction, mirrors/lenses)
- [ ] Atomic/nuclear phenomena (radioactive decay, half-life)

### CARS
- [ ] Ethics and moral philosophy
- [ ] Political theory and governance
- [ ] Art criticism and aesthetics
- [ ] Literary analysis and criticism
- [ ] History of ideas / intellectual history
- [ ] Cultural studies and anthropology
- [ ] Economics and social policy
- [ ] Philosophy of science / epistemology
- [ ] Architecture and design

### B/B (Bio/Biochem)
- [ ] DNA replication, repair, recombination
- [ ] Transcription and RNA processing
- [ ] Translation and protein folding
- [ ] Gene regulation (prokaryotic and eukaryotic)
- [ ] Biotechnology (PCR, gel electrophoresis, cloning, CRISPR)
- [ ] Cell cycle and cancer
- [ ] Cellular respiration (glycolysis, TCA, ETC)
- [ ] Photosynthesis (light/dark reactions)
- [ ] Amino acids, protein structure, enzymes
- [ ] Lipid metabolism (β-oxidation, synthesis)
- [ ] Membrane transport (active, passive, vesicular)
- [ ] Cell signaling (G-protein, tyrosine kinase, second messengers)
- [ ] Nervous system (action potentials, synaptic transmission)
- [ ] Endocrine system (hormones, feedback loops)
- [ ] Cardiovascular system
- [ ] Respiratory system (gas exchange, ventilation control)
- [ ] Renal system (filtration, reabsorption, secretion)
- [ ] Immune system (innate, adaptive, antibodies)
- [ ] Digestive system
- [ ] Mendelian genetics (crosses, linkage, epistasis)
- [ ] Population genetics (Hardy-Weinberg)
- [ ] Evolution (natural selection, speciation, drift)

### P/S (Psych/Soc)
- [ ] Sensation and perception (signal detection, Weber's law, sensory adaptation)
- [ ] Vision, hearing, somatosensation
- [ ] Learning (classical conditioning, operant conditioning, observational)
- [ ] Memory (encoding, storage, retrieval, types of memory)
- [ ] Cognition (problem solving, decision making, heuristics, biases)
- [ ] Language development and processing
- [ ] Consciousness and sleep
- [ ] Motivation and emotion (theories, stress response)
- [ ] Personality theories (psychoanalytic, humanistic, trait, social-cognitive)
- [ ] Psychological disorders (anxiety, mood, schizophrenia, personality disorders)
- [ ] Treatment (biomedical, psychotherapy approaches)
- [ ] Social psychology (attribution, attitudes, conformity, obedience, group dynamics)
- [ ] Stereotypes, prejudice, discrimination
- [ ] Self-concept and identity (self-efficacy, locus of control)
- [ ] Socialization and social interaction (symbolic interactionism, dramaturgical analysis)
- [ ] Social institutions (education, family, religion, government, economy, healthcare)
- [ ] Culture and demographics
- [ ] Social stratification and inequality
- [ ] Health disparities and social determinants

---

## File Structure

Each practice exam section is stored in its own JavaScript file:

```
DrillRoom/
├── DrillRoom.html          (main app — loads everything)
├── exam_cp90.js            (C/P 90-min practice section)
├── exam_bb90.js            (B/B 90-min practice section)  
├── exam_cars90.js          (CARS 90-min practice section)
├── exam_ps90.js            (P/S 90-min practice section)
├── exam_cp60.js            (C/P 60-min — future)
├── exam_bb60.js            (B/B 60-min — future)
├── exam_cars60.js          (CARS 60-min — future)
├── exam_ps60.js            (P/S 60-min — future)
```

Each file exports a constant array: `const EXAM_CP90 = [...]`

The main HTML file loads these via `<script src="...">` tags and registers them with the practice exam system.

---

## How to Add a New Practice Section

1. **Select Uncovered Topics**: Consult `MCAT-CURRICULUM-AND-TOPIC-TRACKER.md` to select uncreated `[ ]` foundational topics to prevent duplication.
2. **Draft Passages & Questions**: Author passages adhering to 5/5 standards (320–450 words with experimental data tables for Science; 550–650 words with dialectical tension for CARS).
3. **Execute the 5-Gate Review Pipeline**: Audit every question against all 5 quality gates:
   - *Gate 1*: Passage Friction & multi-variable data density.
   - *Gate 2*: Cognitive Chain audit requiring a minimum 3-step logic pathway (no 1-step lookups).
   - *Gate 3*: 100% Distractor Trap engineering with a verified 50/50 Primary Seducer and zero dead choices.
   - *Gate 4*: Visual length symmetry ratio $\le 1.08$ with syntactic parallelism and no heuristic giveaways.
   - *Gate 5*: Pedagogical distractor autopsy in `e` classifying each wrong answer's trap archetype.
4. **Create the content file** (e.g., `exam_cp90_11.js`) following the format above
5. **Add a `<script>` tag** in DrillRoom.html to load it
6. **Register the exam** in the `PRACTICE_EXAMS` array in the app code (`practice_exam.js`):

```javascript
PRACTICE_EXAMS.push({
  id: "cp60",
  sec: "C/P",
  label: "Chemical and Physical Foundations of Biological Systems",
  duration: 60,       // minutes
  type: "60min",      // "90min" or "60min"
  sets: EXAM_CP60,    // reference to the loaded constant
  desc: "60-minute practice section — 30 questions"
});
```

4. **Test**: Open DrillRoom.html, go to the Practice Exams tab, verify it appears and runs

---

## Scoring Implementation

When a practice exam is completed:

1. Count raw correct answers
2. Calculate percentage: `pct = correct / total * 100`
3. Map to scaled score using the table above
4. Display section score (118–132) and equivalent percentile
5. If all 4 sections are done from the same exam, show composite (472–528)

The app stores results under `practiceExams` key in localStorage, keyed by exam ID.

---

## Subject-First Practice Workflow & History Features

DrillRoom organizes practice sections by **Subject** rather than by full-length exam suites:

### 1. Subject-First Practice Queue
* **Step 1 — Choose Subject**: Select from C/P, CARS, B/B, or P/S. Each card displays completion status and subject average score.
* **Step 2 — Choose Duration**: Toggle between **90 Minutes** (Standard Full Section: 52–53 Qs) and **60 Minutes** (Paced High-Yield Section: 33 Qs).
* **Step 3 — Start Next Available**: A dedicated CTA card automatically detects the next uncompleted section in the selected queue (e.g., Exam 1 &rarr; Exam 2). If all sections in that queue are completed, it enters a retake cycle.
* **Queue Overview**: Below the CTA, all sections in that subject and duration are listed with their question breakdown and status badges.
* **Exam Suite Switcher**: A mode toggle allows students to view the traditional 4-section suite view with 528 composite score cards when desired.

### 2. Exit & Reset Without Scoring
During any active practice section or base passage set:
* An **Exit (No Score)** button is available in the bottom exam toolbar (`#tExit`) and inside the Pause overlay (`#pExit`).
* Exiting prompts a confirmation: `"Exit and reset this exam without scoring? Your answers will be discarded. No score will be calculated and nothing will be added to your score history or averages."`
* When confirmed, the session terminates cleanly, the timer stops, and **zero score records** are saved to history or averages.

### 3. Comprehensive History & Rolling Averages
Located under the **History & Averages** tab:
* **Configurable Rolling Average Window**: Choose to calculate your average from the **most recent 3, 5, 10, or all** completed sections.
* **Subject & Duration Filters**: Isolate averages by subject (e.g. CARS only, C/P only) or length (90-min vs 60-min).
* **Metrics Displayed**:
  - Average Scaled Score (118–132)
  - Projected 4-Section Composite (472–528 = $4 \times \text{Avg Section}$)
  - Average Raw Accuracy (%) and questions answered
  - Included vs Excluded attempt counts
* **Selective Score Clearing / Exclusion**:
  - Each history row features an **In Avg / Exclude** toggle button.
  - Toggling an attempt to **Excluded** removes it from the rolling average immediately without deleting the review data (ideal for diagnostic baseline tests or interrupted sessions).
  - Individual attempts can also be permanently deleted using the **Delete** button.

---

## Gemini AI Post-Exam Diagnostic & Mistake Analysis

DrillRoom includes an AI diagnostic engine in `gemini_analysis.js` that integrates directly with Google Gemini.

### Features
1. **API Key Integration**: Stored locally in `localStorage` (`drillroom_gemini_api_key`) with connection verification.
2. **Model Selection**: Supports `gemini-3.8-flash` (Newest Flagship default), `gemini-3.8-pro`, `gemini-3.8`, `gemini-2.5-flash`, `gemini-2.0-flash`, `gemini-1.5-flash`, `gemini-1.5-pro`, plus auto-detection and custom model names.
3. **Comprehensive Mistake Audit**: Evaluates every missed question along with lucky guesses and 50/50 shaky choices.
4. **AAMC Trap Anatomy**: Classifies distractors by authentic AAMC patterns:
   - *True Fact, Wrong Question*
   - *Opposite Relationship / Inversion*
   - *Scope Creep & Extreme Language*
   - *Familiar Buzzword Attractor*
   - *Data / Experimental Control Misreading*
5. **Tactical Improvement**: Delivers the 3-Word Stem Rephrase rule, Process of Elimination (POOE) heuristics, and rapid table interrogation techniques.
6. **48-Hour Recovery Plan**: Concrete high-yield study topics tailored to the student's exact mistakes.
7. **Local Caching**: Saves generated reports in `localStorage` (`drillroom_ai_analysis_{examId}`) so returning to a completed exam preserves the AI report without re-querying the API.

