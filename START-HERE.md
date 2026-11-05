# Drill Room

An MCAT practice app built to look and behave like the real AAMC exam interface,
plus a set of study docs. Everything runs on your own computer — no account,
no sign-up, and it never touches the internet.

## Running it

**Double-click `DrillRoom.html`.** That's it — it opens in your browser and runs.
The whole app is that one file.

Your progress saves automatically in the browser, so bookmark the tab and come
back to it. (Use the same browser each time — that's where the history lives.)

*Ignore the "days to exam" counter on the front page — it's still pointing at my
test date. Everything else is yours.*

---

## What's in it — 36 question sets

| | |
|---|---|
| **CARS** | 21 passages — **14 are real AAMC passages** (Thomas Hardy, free will, the ultimatum game, Puritan society, deconstructionism, censorship, Eurasian history, courthouse design, antenatal depression, energy and sustainability, tools for thought, what is life, maternal psychology, primordial complexity) plus 7 built from public-domain source texts |
| **Bio/Biochem** | 8 sets — enzymes (x2), renal, cardiovascular, endocrine, respiratory, neuro, genetics |
| **Chem/Phys** | 4 sets — acid/base, kinetics, physics, and a 20-question speed block |
| **Psych/Soc** | 3 sets — learning, social, disorders |

## The interface

The toolbar mirrors the real exam:

- **Highlight** — select text and hit it. There's a *sticky* checkbox so you can
  leave it on and highlight by dragging, which is how the real one feels.
- **Strikethrough** — cross out choices you've eliminated.
- **Navigator** — the review screen, with the same Unseen / Incomplete / Completed
  statuses the AAMC one uses.
- **Periodic Table**, **Noteboard**, **Pause**, **Review sheet**, **End Section**.

**Keyboard shortcuts**, same as the real exam: `Alt+H` highlight, `Alt+S`
strikethrough, `Alt+T` periodic table, `Alt+V` navigator, `Alt+N` next,
`Alt+P` previous. You can also just press `A` `B` `C` `D` to answer.

## The one thing the real exam doesn't have

After each question it asks how sure you were — **Sure / Down to two / Guess**.

It sounds minor and it's the most useful part. At the end it separates "right and
knew it" from "right but got lucky" from **"wrong and was sure."** That last group
is what's worth reviewing — those are the places where what you think you know is
wrong, and ordinary review never surfaces them.

---

## The study docs (`/study`) & Guides

All built off AAMC's published content outline.

| File | What it is |
|---|---|
| **MCAT-CURRICULUM-AND-TOPIC-TRACKER.md** | Complete blueprint audit of all created topics in DrillRoom vs uncreated topics across CARS, C/P, B/B, and P/S with interactive checkmarks to prevent repetition. |
| **PRACTICE-EXAM-GUIDE.md** | Specs for 90-min and 60-min sections, scaled scoring (118–132), AAMC distractor engineering, and Gemini AI diagnostic integration. |
| **PS-TERMS.md** | Every term in AAMC's Psych/Soc outline — about 1,200 — grouped by content category. Terms people confuse are placed next to each other on purpose, with a one-line `Split:` giving the exact difference. **If you read one thing, read this.** P/S is the most learnable section on the exam. |
| **CONCEPTS-ALL.md** | The full concept sheet. Also split by subject: `-BB`, `-CHEM`, `-PHYSICS`, `-PS`, `-CARS`. |
| **MEMORIZE.md** | The pure-memorization set — amino acids, hormones, equations, lab techniques. The stuff with no logic to derive. |
| **DISTINCTIONS.md** | Pairs that are easy to mix up, and the one feature that separates them. |
| **ORGO-TRIAGE.md** | Organic chem ranked by how often it's actually tested. |
| **CARS-AAMC-SETS.md** | How AAMC builds CARS passages and questions. |

Tip: `★` in PS-TERMS marks terms that carry a classic trap. Short on time — read
the ★ lines and the `Split:` lines and skip everything else.
