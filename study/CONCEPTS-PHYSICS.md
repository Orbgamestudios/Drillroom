# CONCEPTS — C/P PHYSICS

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

# CLUSTER 1 — OPTICS
**FL1: Q15, Q45 · CC4D (4/6, 67%)**

**Shared scenario: one eye looking at a candle.** A 6 cm flame across the room. Light leaves it in
air, crosses the cornea, the aqueous humor, the lens, and the **vitreous humor**, and lands on the
retina as a real, inverted, tiny image. Each concept is one step further along that trip.

---

### Index of refraction
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

### Snell's law
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

### Total internal reflection
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

### Thin lens and mirror equation, with sign conventions
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

### Magnification
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

# CLUSTER 2 — FLUIDS AND CIRCULATION
**FL1: Q18, Q21, Q26 · CC4B (2/4, 50%)**

**Shared scenario: one heartbeat's worth of blood.** The left ventricle squeezes, 70 mL leaves
through the aortic valve, and that bolus runs aorta → arteries → arterioles → capillary bed →
venules → veins → right heart → pulmonary artery → lung capillaries. Each concept is something
that happens to that same bolus at a different point.

---

### Continuity equation — and why capillary flow is slow
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

### Poiseuille flow and vascular resistance
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

### Bernoulli's equation
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

### Hydrostatic pressure
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

### Systolic, diastolic, pulse, and mean pressure
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

### Work done by the heart
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

# CLUSTER 3 — CIRCUITS
**FL1: Q56 · CC4C (2/5, 40% — worst C/P content category)**

**Shared scenario: one bench circuit.** A battery, wires, and one or two identical 60 Ω bulbs. Put
them in a line or side by side, insert a resistor, swap the battery. Every concept below is a
rearrangement of these same parts.

---

### Ohm's law and resistance
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

### Series and parallel
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

### Current division
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

### Power
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

### Capacitors
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

# CLUSTER 4 — ELECTROCHEMISTRY
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

### Reduction potentials and cell potential
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

### Spontaneity
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

### Galvanic vs electrolytic
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

### Galvanic (voltaic) cell
FL1: — · CC4C · supports Q54, Q55

**Structure.** A **spontaneous** redox reaction split into two half-cells so its electrons must travel through a wire: `E°_cell > 0`, `ΔG < 0`, chemical energy → electrical. Electrons leave the anode (oxidation; the **negative** terminal, because that is where electrons are produced), cross the wire, and arrive at the cathode (reduction; **positive**). The salt bridge passes ions — anions toward the anode, cations toward the cathode — so neither beaker builds up charge and stalls the reaction.

**Concrete.** Zinc in zinc sulfate, copper in copper sulfate, a wire and a salt bridge between them. The bulb lights. Over the afternoon the zinc strip thins and roughens, the copper strip thickens, and the blue on the copper side pales as Cu²⁺ plates out. The meter reads 1.10 V at the start and drifts down as Zn²⁺ builds and Cu²⁺ is spent; pull the salt bridge and the bulb goes out at once.

**Claims.** Asserts the cell produces a voltage because the reaction *wants* to go — the voltage is the reaction's spontaneity expressed in volts. Denies that the terminal signs are a convention: the anode is negative *because* oxidation pumps electrons into it. Denies that the salt bridge carries electrons; it carries ions, and without it the anode beaker goes positive and the cathode beaker negative until nothing more can move. Every battery is one of these.

**Predicts.** Given two `E°_red` values, the more positive is the cathode; the meter reads `E°_cathode − E°_anode`. Anode loses mass if its metal is the species oxidized; cathode gains mass if the cation plates. Running the cell moves concentrations in the direction that lowers `E`, until `E = 0` — a dead battery is a cell at equilibrium. "Which electrode is negative" → the anode, in this cell type only.

---

### Electrolytic cell
FL1: — · CC4C · supports Q54, Q55

**Structure.** A **non-spontaneous** redox reaction driven by an external source whose voltage exceeds `|E°_cell|`: `E°_cell < 0`, `ΔG > 0`, electrical energy → chemical. The supply's positive terminal *pulls* electrons out of one electrode — that one is oxidized, so it is the anode, and it is **positive**; its negative terminal *pushes* electrons into the other — reduction, cathode, **negative**. Same definitions as the galvanic cell, opposite signs.

**Concrete.** The same beakers, with a power supply set above 1.10 V clipped across them backwards. Now the zinc strip *grows* — Zn²⁺ is forced back onto it (cathode, on the supply's negative clip) — and the copper strip dissolves into blue (anode, on the positive clip). Recharging the lead-storage battery in a car is this exact operation: the alternator drives the discharge reaction in reverse.

**Claims.** Asserts oxidation is still at the anode and reduction still at the cathode — the labels follow the reaction, and the reaction at each physical electrode has been reversed. Denies "the anode is negative" as a rule; it is negative in a galvanic cell and positive here. Denies that the supply changes what is favorable: it does not make `ΔG` negative, it pays the positive `ΔG` in electrical work, and must supply at least `|E°_cell|` to do so. Denies that electrons travel through the solution — ions do, anions to the anode as always.

**Predicts.** `E°_cell` negative, or a stem with "a current is passed through," "electrolysis," "plating," "recharging" → electrolytic. The electrode clipped to the supply's positive terminal is the anode: write the oxidation there. On recharge, the electrode that was the cathode on discharge is now the anode — its *sign* has not changed, its *role* has. Minimum applied voltage = `|E°_cell|`; how much is deposited is Faraday's law, below.

---

### Anode
FL1: — · CC4C · supports Q53, Q54

**Structure.** The electrode where **oxidation** happens: a species gives up electrons, and those electrons enter the external circuit from here. Anions migrate toward it — that is what "anion" means. Its *sign* depends on the cell: **negative** in a galvanic cell (electron source), **positive** in an electrolytic cell (the supply is pulling electrons out).

**Concrete.** In the battery, the zinc strip: it thins because `Zn → Zn²⁺ + 2e⁻` is eating it, and it is the negative post. Under the power supply, the copper strip: it thins because `Cu → Cu²⁺ + 2e⁻` is eating *it*, and it is on the positive clip. Two different pieces of metal, one name, because the same thing — metal dissolving, electrons leaving — happens at each.

**Claims.** Asserts the anode is defined by its chemistry and nothing else. Denies that it is the negative electrode by definition — the most-tested false belief in the container. Denies that it attracts cations; it attracts anions, in both cell types, because oxidation is making the electrolyte around it positive and negative ions move in to balance. Denies that the anode always loses mass: if the species oxidized is an ion or water (`2H₂O → O₂ + 4H⁺ + 4e⁻`), the electrode is inert and a gas comes off instead.

**Predicts.** "At the anode" → write the oxidation half-reaction. "Which electrode loses mass" → the anode, if its own metal is what oxidizes. "Which way do anions move" → toward the anode, in any cell. Sign: ask first which cell type you are in — galvanic, negative; electrolytic, positive. Electrons in the wire leave the anode; conventional current in the wire arrives at it.

---

### Cathode
FL1: — · CC4C · supports Q53, Q54

**Structure.** The electrode where **reduction** happens: electrons arrive from the external circuit and are consumed by a species that gains them. Cations migrate toward it. Its sign: **positive** in a galvanic cell (electrons are being drawn in), **negative** in an electrolytic cell (the supply is pushing electrons in).

**Concrete.** In the battery, the copper strip: it thickens as `Cu²⁺ + 2e⁻ → Cu` plates on, the blue fades around it, and it is the positive post. Under the power supply, the zinc strip: it regrows as `Zn²⁺ + 2e⁻ → Zn`, on the negative clip. In acid, hydrogen bubbles off the cathode — `2H⁺ + 2e⁻ → H₂` — which is the fizz in the metal-plus-acid block.

**Claims.** Asserts the cathode is defined by reduction, so metal plating and hydrogen evolution are cathode events in every cell. Denies that it is the positive electrode by definition. Denies that a cation is reduced at the anode under any wiring. Denies that the electrode metal itself must react: a platinum or graphite cathode just hands electrons to whatever in the solution is most reducible.

**Predicts.** "At the cathode" → write the reduction half-reaction. "Metal deposited," "gas evolved at the negative electrode during electrolysis," "mass gained" → cathode, and the amount is Faraday's law. "Which way do cations move" → toward the cathode, in any cell. **Anode vs cathode is one question: are electrons leaving the species, or arriving?** Sign is a second question, answered by cell type.

---

### Faraday's law
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

### Concentration cell
FL1: — · CC4C · supports Q55 · **added — not a table row; an outline bullet ("Concentration cell") that appears in this cluster only as a clause inside Spontaneity's Predicts**

**Structure.** Two half-cells with the **same** metal and the **same** ion at **different concentrations**: `E° = 0` because the half-reactions are identical, yet `E > 0` because equalizing the concentrations is downhill. The dilute side is the **anode** — its metal dissolves to raise its ion concentration; the concentrated side is the **cathode** — its ions plate out to lower theirs. Electrons flow dilute → concentrated, and `E` falls to zero as the two sides meet.

**Concrete.** Two copper strips, two copper sulfate beakers, one at 0.01 M and one at 1.0 M, wire and bridge. The meter reads a few hundredths of a volt — real, small — and all of it comes from the difference in blue. The pale beaker's strip thins; the dark beaker's strip thickens; the pale one darkens and the dark one pales until they match, and then the meter reads zero.

**Claims.** Asserts a voltage can exist with no difference in chemistry at all — only a difference in concentration — which is the Nernst equation's concentration term doing all the work with `E° = 0`. Denies that the concentrated side is the anode: the system moves to *equalize*, so the dilute side must gain ions (oxidation) and the concentrated side lose them (reduction). Denies that `E°_cell = 0` means nothing happens; it means the standard-state cell does nothing, and this cell is not at standard state.

**Predicts.** Identical electrodes, different concentrations → concentration cell; `E° = 0`; electrons flow **from the dilute half-cell to the concentrated one**; the cathode is in the concentrated beaker. A larger concentration ratio raises `E`; a tenfold ratio gives about 30 mV for a 2+ ion. A neuron's membrane potential is the same physics — one ion, two concentrations, a voltage — which is why the same equation appears on both sides of the exam.

---

### Metal plus acid — the activity series
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

# CLUSTER 5A — NUCLEAR DECAY
**FL1: Q42 · CC4E (4/6, 67%)**

**Shared scenario: one atom of uranium-238 in a granite countertop.** Over four and a half billion
years it steps down a chain of fourteen decays to lead-206, changing identity every time something
leaves the nucleus. Each concept tracks one step.

---

### Conservation of A and Z
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

### The decay modes
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

### Alpha decay
FL1: **Q42** · CC4E · supports

**Structure.** The nucleus ejects two protons and two neutrons bound as one particle, `⁴₂He`: `ΔA = −4, ΔZ = −2`, a new element two places down the table. The mode of nuclei that are simply **too heavy** — every nuclide past bismuth (`Z > 83`) is unstable, and alpha is how the heavy ones shed mass.

**Concrete.** The uranium-238 atom in the countertop, step one of fourteen: `²³⁸₉₂U → ²³⁴₉₀Th + ⁴₂He`. The helium nucleus leaves at about 5% of light speed; the thorium recoils the other way, slowly, because momentum balances and it is sixty times heavier. The alpha crosses a few centimeters of air and is stopped by the dead outer layer of your skin — or by a sheet of paper.

**Claims.** Asserts the emitted particle is a helium *nucleus* — no electrons — so the atom left behind carries two surplus electrons and the alpha steals two from whatever it hits. Denies that alpha is the "weak" radiation because it is easily stopped: it is the most ionizing per centimeter, dumping all its energy in a few cells, which is why the alpha that matters is the one emitted **inside** you (radon-222, a gas in this same chain, in a lung). Denies that alpha alone can carry a heavy nucleus to stability: removing two protons and two neutrons from a nucleus with `N/Z ≈ 1.6` leaves the daughter *more* neutron-rich (`146/92 → 144/90`), so a heavy chain must interleave alphas with beta-minus steps.

**Predicts.** `ΔA = 4` between parent and product → alpha, the only common mode that moves `A`. Parent heavier than bismuth with no other cue → alpha first. After an alpha, expect a beta-minus soon — the U-238 chain runs eight alphas and six beta-minuses to reach lead-206. Shielding stem: paper or skin.

---

### Beta-minus decay
FL1: **Q42** · CC4E · supports

**Structure.** A neutron becomes a proton inside the nucleus, `n → p + e⁻ + ν̄`; the electron is **manufactured there and ejected**: `ΔA = 0, ΔZ = +1`, one element *up*. The mode of a nucleus with **too many neutrons** for its protons.

**Concrete.** Step two on the countertop: `²³⁴₉₀Th → ²³⁴₉₁Pa + ⁰₋₁e`. Thorium-234 has 144 neutrons to 90 protons — more neutron-heavy than the uranium that made it. One neutron converts; the electron leaves at a good fraction of light speed with a spread of energies, the antineutrino carrying the rest; a few millimeters of aluminum stops it. Same 234 nucleons. Protactinium.

**Claims.** Asserts the electron came from the nucleus, not from the electron cloud — which is why `Z` climbs and the mass number holds. Denies the model where beta decay ejects an orbital electron; that would leave `Z` unchanged and make an ion, not a new element. Denies that ejecting a negative particle lowers the nucleus's charge: the nucleus *gained* a positive unit, and the atom as a whole is briefly a positive ion until it picks up an electron from its surroundings.

**Predicts.** `ΔA = 0, ΔZ = +1` → beta-minus, and the balancing move is subtracting `−1`: `Z_daughter = Z_parent + 1`. Carbon-14 → nitrogen-14; every neutron-rich fission product; every "became the next element with the same mass number" stem. **Beta-minus vs beta-plus is one question: did `Z` go up or down?** Up is this one.

---

### Beta-plus decay
FL1: **Q42** · CC4E · supports

**Structure.** A proton becomes a neutron, `p → n + e⁺ + ν`, and the **positron** — the electron's antiparticle, `⁰₊₁e` — is ejected: `ΔA = 0, ΔZ = −1`, one element *down*. The mode of a nucleus with **too many protons**, and only available when the parent atom outweighs the daughter atom by at least **1.022 MeV** — two electron masses — because the products carry two particles the parent did not have to pay for before: the positron, and the orbital electron the daughter no longer needs.

**Concrete.** The countertop has none of these; the hospital next door makes thousands a second. Fluorine-18 in a PET tracer: `¹⁸₉F → ¹⁸₈O + ⁰₊₁e`. The positron travels about a millimeter through tissue, meets an electron, and both vanish into **two 511 keV photons flying in exactly opposite directions**. The detector ring catches both and draws the line between them. Fluorine became oxygen; the picture is made of annihilations.

**Claims.** Asserts something leaves the nucleus and is detectable at a distance — the positron, then its two photons. Denies that beta-plus is beta-minus run backwards at the same price: beta-minus needs only a positive mass difference, beta-plus needs it to exceed two electron masses, so a proton-rich nucleus with a small mass surplus **cannot** do this and must capture instead. Denies that the 511 keV photons are gamma decay — they come from annihilation outside the nucleus, after the decay is over.

**Predicts.** `ΔZ = −1` with a positron named, or **two back-to-back 511 keV photons**, or a PET stem → beta-plus. The daughter sits one element to the left. **Beta-plus vs electron capture is one question: did anything leave the nucleus?** Here, yes — a positron.

---

### Electron capture
FL1: **Q42** · CC4E · supports

**Structure.** The nucleus pulls in one of the atom's own **inner-shell electrons** and a proton becomes a neutron, `p + e⁻ → n + ν`: `ΔA = 0, ΔZ = −1`, the same bookkeeping as beta-plus. Nothing charged leaves the nucleus; the neutrino carries the energy away unseen, and the only signal is atomic — the hole left in the inner shell is filled from above, emitting the **daughter element's characteristic X-ray**.

**Concrete.** An iodine-125 seed implanted in a prostate: `¹²⁵₅₃I + ⁰₋₁e → ¹²⁵₅₂Te`. The nucleus swallows a K-shell electron and is tellurium. An outer electron drops into the empty shell and a tellurium X-ray leaves the atom — those low-energy photons are the radiation doing the treating. Iodine-125's mass surplus over tellurium-125 is 0.19 MeV, nowhere near the 1.022 MeV a positron costs, so this nucleus **can decay no other way**. Back on the countertop: potassium-40 in the feldspar does this one time in nine, becoming argon that stays trapped in the crystal — the clock used to date the rock.

**Claims.** Asserts a capture is possible whenever the parent atom outweighs the daughter atom at all, because nothing new is created — the electron was already there. Denies that beta-plus and electron capture are one process with one condition: capture is available wherever beta-plus is, and also across the whole window from 0 to 1.022 MeV where beta-plus is forbidden. Denies that the X-ray is a gamma: it comes from the electron shell, not the nucleus, and it is the *daughter's* X-ray, because by the time the shell refills the atom is already the new element.

**Predicts.** `ΔZ = −1` with **no emitted particle**, or "characteristic X-rays of the daughter," or a stem describing an orbital electron entering the nucleus → electron capture. A proton-rich nuclide with a small mass difference → capture only; with a large one → both are open and beta-plus usually dominates. **Beta-plus vs electron capture is one question: did anything leave the nucleus?** Here, no — an electron went *in*.

---

### Gamma decay
FL1: **Q42** · CC4E · supports

**Structure.** An **excited nucleus** drops to a lower energy state and emits the difference as a photon: `ΔA = 0, ΔZ = 0`. No new element. Usually the second half of another decay — the daughter of an alpha or beta step is often left excited and sheds the surplus within picoseconds — or, in a **metastable** nuclide, a delayed step of its own.

**Concrete.** The bone-scan isotope from the half-life block: the "m" in technetium-99m means the nucleus is holding 140 keV it has not yet released. It releases it as one photon, which passes out of the patient and into the gamma camera. Technetium before, technetium after. On the countertop, the gamma a counter hears is the same thing one step behind a beta: bismuth-214 beta-decays to polonium-214, and the newborn polonium nucleus, arriving excited, drops to its ground state by emitting a 609 keV photon.

**Claims.** Asserts a gamma-only step changes energy and nothing else — not `A`, not `Z`, not the element. Denies that gamma can ever answer "which two atoms form": it forms none. Denies that gamma is a particle in the alpha/beta sense; it is light, uncharged, undeflected by a magnetic field, and stopped only by centimeters of lead or thick concrete because it ionizes sparsely along a long path. Denies that every photon from a decaying atom is a gamma — an X-ray comes from the electron shell, a gamma from the nucleus.

**Predicts.** "Element unchanged, energy released," an asterisk or "m" on the parent, or a shielding stem answered by lead → gamma. Given `ΔA = 0, ΔZ = 0` between parent and product, the product is the same nuclide and the mode is gamma. **Gamma vs everything else is one question: did the element change?** Only gamma leaves it alone.

---

### Half-life
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

# CLUSTER 5B — ELECTRONIC STRUCTURE
**FL1: — · CC4E**

**Shared scenario: a pinch of table salt thrown into the candle flame from Cluster 1.** The flame
turns brilliant yellow. Sodium's outer electron absorbs heat, jumps to a higher orbital, falls back,
and emits a photon at exactly 589 nm — the yellow of a streetlight. Each concept is one part of why
that color and no other came out.

---

### Electron configuration and the filling rules
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

### Photons, line spectra, and the photoelectric effect
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

# THE 60-SECOND TRIGGER TABLE

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
