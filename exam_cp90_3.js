/* ---- exam_cp90_3.js ---- */
/* Full 90-minute Chem/Phys Practice Exam 3: 7 passages (42 Qs) + 10 discrete Qs = 52 Qs */
const EXAM_CP90_3 = [
  {
    "id": "exam_cp90_3_p1",
    "sec": "C/P",
    "topic": "One-Dimensional Kinematics & Freefall Acceleration in Pulmonary Drug Delivery",
    "sheet": 1,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_3",
    "passage": "<div class=\"ttl\">Passage 1 (Questions 1&ndash;6)</div>\n<p>Targeted pulmonary drug delivery requires precise control over the aerodynamic deposition of nebulized aerosol droplets in deep alveolar tissue. To avoid premature upper-airway impaction, pharmacologists synthesize polymeric microparticles and evaluate their sedimentation behavior. In an analytical testing facility, microparticles are introduced into an instrumented drop tower consisting of two parallel vertical columns: an evacuated vacuum column ($P < 10^{-4}\\text{ Torr}$) and a fluid-filled settling column maintained at atmospheric pressure ($1.00\\text{ atm}$, $T = 293\\text{ K}$) containing standard dry air (density $\\rho_{air} = 1.20\\text{ kg/m}^3$, dynamic viscosity $\\eta = 1.81 \\times 10^{-5}\\text{ Pa}\\cdot\\text{s}$).</p>\n<p>In the vacuum column, particles accelerate solely under the influence of gravity ($g = 9.80\\text{ m/s}^2$). Kinematic sensors track downward position $y(t)$, instantaneous velocity $v(t)$, and elapsed fall time $t$ over a standardized vertical drop distance of $h = 4.90\\text{ m}$ from rest ($v_0 = 0\\text{ m/s}$). In the atmospheric column, particles encounter a velocity-dependent linear aerodynamic drag force, $F_d = -b v$, where $b$ represents the Stokes drag coefficient governed by sphere diameter $d$ ($b = 3\\pi\\eta d$). As downward velocity increases, aerodynamic drag opposes the gravitational force ($F_g = mg$), causing net acceleration to diminish until reaching terminal velocity ($v_t$), at which point net force is zero. Physical dimensions, mass, fall times, and measured terminal velocities for four therapeutic microsphere formulations are summarized in Table 1.</p>\n<table class=\"tbl\">\n  <caption>Table 1 Physical parameters and sedimentation kinematics of therapeutic microspheres</caption>\n  <thead>\n    <tr><th>Formulation</th><th>Diameter $d$ (&mu;m)</th><th>Mass $m$ ($10^{-11}$ kg)</th><th>Vacuum Fall Time from 4.90 m (s)</th><th>Measured Terminal Velocity $v_t$ (m/s)</th><th>Linear Drag Coeff. $b$ ($10^{-8}$ N&middot;s/m)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Formulation 1</td><td>10.0</td><td>0.52</td><td>1.00</td><td>0.30</td><td>1.70</td></tr>\n    <tr><td>Formulation 2</td><td>20.0</td><td>4.16</td><td>1.00</td><td>1.20</td><td>3.40</td></tr>\n    <tr><td>Formulation 3</td><td>30.0</td><td>14.04</td><td>1.00</td><td>2.70</td><td>5.10</td></tr>\n    <tr><td>Formulation 4</td><td>40.0</td><td>33.28</td><td>1.00</td><td>4.80</td><td>6.80</td></tr>\n  </tbody>\n</table>\n<p>Following sedimentation trials, researchers conduct high-speed landing deceleration tests on viscoelastic collection plates to ensure encapsulated peptide drugs do not rupture upon alveolar impact.</p>",
    "qs": [
      {
        "q": "In the evacuated drop column ($g = 9.80\\text{ m/s}^2$), what is the downward impact velocity of Formulation 2 when dropped from rest through a total height of 19.6 m?",
        "ch": [
          "9.80 m/s",
          "14.0 m/s",
          "39.2 m/s",
          "19.6 m/s"
        ],
        "a": 3,
        "e": "<strong>Torricelli kinematic equation in vacuum:</strong> In the absence of air resistance, motion under constant gravitational acceleration is governed by $v^2 = v_0^2 + 2gh$. With an initial velocity of $v_0 = 0\\text{ m/s}$, this simplifies to $v = \\sqrt{2gh} = \\sqrt{2 \\times 9.80\\text{ m/s}^2 \\times 19.6\\text{ m}} = \\sqrt{384.16} = 19.6\\text{ m/s}$.<br><br><em>Distractor Traps:</em><br>&bull; A (9.80 m/s) is the velocity after falling for only 1.0 s or from a height of 4.90 m.<br>&bull; B (14.0 m/s) is the velocity after falling 10.0 m.<br>&bull; C (39.2 m/s) results from forgetting to take the square root ($2gh / 9.8$ or doubling the correct velocity)."
      },
      {
        "q": "Which differential expression describes the instantaneous downward acceleration $a(t)$ of a microsphere of mass $m$ falling through the atmospheric column with linear drag $F_d = -bv$?",
        "ch": [
          "a(t) = g - (b/m)v",
          "a(t) = g + (b/m)v",
          "a(t) = g - (m/b)v",
          "a(t) = (b/m)v - g"
        ],
        "a": 0,
        "e": "<strong>Newton's Second Law with aerodynamic drag:</strong> Defining downward as the positive direction, two forces act on the falling microsphere: downward gravity ($F_g = mg$) and upward resistive drag ($F_d = -bv$). Summing forces gives $F_{net} = mg - bv = ma(t)$. Dividing both sides by mass $m$ yields the instantaneous acceleration: $a(t) = g - \\frac{b}{m}v$. At terminal velocity, $a(t) = 0$, giving $v_t = \\frac{mg}{b}$.<br><br><em>Distractor Traps:</em><br>&bull; B adds drag to gravity instead of subtracting it, which would imply air resistance accelerates the sphere downward.<br>&bull; C inverts the mass-to-drag ratio ($m/b$ instead of $b/m$), which has incorrect physical dimensions.<br>&bull; D reverses the signs of gravity and drag, indicating upward acceleration."
      },
      {
        "q": "A specialized nebulizer nozzle ejects a Formulation 1 droplet vertically upward into the evacuated column with an initial speed of $14.0\\text{ m/s}$. Neglecting air resistance, what maximum height above the nozzle does the droplet reach?",
        "ch": [
          "5.00 m",
          "7.14 m",
          "10.0 m",
          "20.0 m"
        ],
        "a": 2,
        "e": "<strong>Maximum height in free fall:</strong> At the apex of vertical flight, instantaneous velocity is zero ($v = 0\\text{ m/s}$). Applying $v^2 = v_0^2 - 2gh_{max} \\implies 0 = (14.0\\text{ m/s})^2 - 2(9.80\\text{ m/s}^2)h_{max}$. Solving for height: $h_{max} = \\frac{v_0^2}{2g} = \\frac{196}{19.6} = 10.0\\text{ m}$.<br><br><em>Distractor Traps:</em><br>&bull; A (5.00 m) mistakenly divides by $4g$ or divides the correct height by 2.<br>&bull; B (7.14 m) calculates $v_0 / 1.96$ or confuses displacement with apex time multiplied by velocity.<br>&bull; D (20.0 m) forgets the factor of 2 in the denominator, computing $v_0^2 / g$."
      },
      {
        "q": "During a landing impact test, a Formulation 4 capsule strikes a viscoelastic test plate at $12.0\\text{ m/s}$ and decelerates uniformly to rest over a displacement of $0.060\\text{ m}$. What is the magnitude of the deceleration?",
        "ch": [
          "100 m/s^2",
          "600 m/s^2",
          "2400 m/s^2",
          "1200 m/s^2"
        ],
        "a": 3,
        "e": "<strong>Kinematic deceleration derivation:</strong> Using the kinematic equation $v_f^2 = v_i^2 + 2ad$, where $v_f = 0\\text{ m/s}$, $v_i = 12.0\\text{ m/s}$, and $d = 0.060\\text{ m}$: $0 = (12.0)^2 + 2a(0.060) \\implies 0 = 144 + 0.120a$. Solving for the deceleration magnitude: $|a| = \\frac{144}{0.120} = 1200\\text{ m/s}^2$.<br><br><em>Distractor Traps:</em><br>&bull; A (100 m/s^2) divides velocity by distance ($12.0 / 0.060 = 200$) and halves it.<br>&bull; B (600 m/s^2) forgets the factor of 2 in the denominator, computing $v^2 / (4d)$ or $v^2 / (2 \\times 0.120)$.<br>&bull; C (2400 m/s^2) forgets the factor of 2 in $2ad$, calculating $v^2 / d = 144 / 0.060 = 2400\\text{ m/s}^2$."
      },
      {
        "q": "When Formulation 3 falls through air and reaches exactly half of its terminal velocity ($v = 0.50\\,v_t$), what percentage of the gravitational force is balanced by aerodynamic drag?",
        "ch": [
          "25% of gravitational force",
          "50% of gravitational force",
          "71% of gravitational force",
          "100% of gravitational force"
        ],
        "a": 1,
        "e": "<strong>Linear drag relationship:</strong> For Stokes flow, the drag force is strictly linear with respect to velocity: $F_d = bv$. At terminal velocity $v_t$, aerodynamic drag exactly balances gravity: $F_d(v_t) = b v_t = mg = 100\\%\\text{ of } F_g$. When falling at $v = 0.50\\,v_t$, the drag force is $F_d = b(0.50\\,v_t) = 0.50(b v_t) = 0.50 mg$, which is exactly $50\\%$ of the gravitational force.<br><br><em>Distractor Traps:</em><br>&bull; A (25%) erroneously assumes quadratic drag ($F_d \\propto v^2$), where $(0.5)^2 = 0.25$.<br>&bull; C (71%) invokes $\\sqrt{0.5} \\approx 0.707$, confusing velocity scaling with kinetic energy or RMS values.<br>&bull; D (100%) is only true when the particle reaches terminal velocity ($v = v_t$)."
      },
      {
        "q": "Which statement correctly describes the mathematical relationship between elapsed fall time $t$ and release height $h$ for particles dropped from rest in a vacuum?",
        "ch": [
          "Fall time is directly proportional to the square root of release height.",
          "Fall time is directly proportional to the second power of release height.",
          "Fall time is linearly proportional to the release height divided by mass.",
          "Fall time is inversely proportional to the square root of release height."
        ],
        "a": 0,
        "e": "<strong>Kinematic scaling of fall time:</strong> For free fall from rest in a vacuum, displacement is given by $h = \\frac{1}{2}gt^2$. Rearranging to solve for elapsed time yields $t = \\sqrt{\\frac{2h}{g}} = \\sqrt{\\frac{2}{g}} \\cdot \\sqrt{h}$. Because $g$ is constant, fall time $t$ is directly proportional to the square root of the release height ($t \\propto \\sqrt{h}$). Note that mass does not appear in this equation, confirming Galilean equivalence.<br><br><em>Distractor Traps:</em><br>&bull; B states $t \\propto h^2$, inverting the power relationship ($h \\propto t^2$, not $t \\propto h^2$).<br>&bull; C incorrectly introduces mass and assumes a linear relationship.<br>&bull; D claims an inverse relationship ($t \\propto 1/\\sqrt{h}$), which would absurdly imply taller falls take less time."
      }
    ]
  },
  {
    "id": "exam_cp90_3_p2",
    "sec": "C/P",
    "topic": "Two-Dimensional Projectile Motion & Vector Independence in Paralympic Biomechanics",
    "sheet": 2,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_3",
    "passage": "<div class=\"ttl\">Passage 2 (Questions 7&ndash;12)</div>\n<p>In Paralympic throwing sports, seated athletes launch competitive implements (e.g., shot put, javelin) from specialized throwing frames anchored to a concrete circle. Because trunk stability, shoulder positioning, and release heights differ substantially from standing throws, sports biomechanists use high-speed optical motion capture (500 frames/s) to optimize release parameters. The projectile's flight path through the air is modeled by decoupling its continuous trajectory into two independent, mutually perpendicular kinematic components: a horizontal axis ($x$) with zero net acceleration ($a_x = 0$), and a vertical axis ($y$) dominated by constant gravitational downward acceleration ($a_y = -g = -9.80\\text{ m/s}^2$).</p>\n<p>An elite seated athlete launched a standardized 4.00 kg shot put at varying release angles ($\\theta$) relative to the horizontal, with a constant initial launch speed of $v_0 = 10.0\\text{ m/s}$ from a fixed seated release height of $y_0 = 1.60\\text{ m}$. Kinematic equations for horizontal and vertical positions as functions of elapsed flight time $t$ are given by $x(t) = (v_0\\cos\\theta)t$ and $y(t) = y_0 + (v_0\\sin\\theta)t - \\frac{1}{2}gt^2$. The vertical velocity at any instant is $v_y(t) = v_0\\sin\\theta - gt$. Table 1 displays the launch parameters, velocity components, time to apogee, maximum vertical height ($y_{max}$), and measured horizontal range ($R$) at ground landing ($y = 0\\text{ m}$) across four experimental trials.</p>\n<table class=\"tbl\">\n  <caption>Table 1 Kinematic trajectory parameters of a 4.00 kg shot launched at 10.0 m/s from 1.60 m height</caption>\n  <thead>\n    <tr><th>Trial</th><th>Launch Angle &theta; (&deg;)</th><th>Initial $v_x$ (m/s)</th><th>Initial $v_y$ (m/s)</th><th>Time to Apogee (s)</th><th>Max Height $y_{max}$ (m)</th><th>Horizontal Range $R$ (m)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Trial 1</td><td>0.0</td><td>10.00</td><td>0.00</td><td>0.00</td><td>1.60</td><td>5.71</td></tr>\n    <tr><td>Trial 2</td><td>30.0</td><td>8.66</td><td>5.00</td><td>0.51</td><td>2.88</td><td>11.08</td></tr>\n    <tr><td>Trial 3</td><td>45.0</td><td>7.07</td><td>7.07</td><td>0.72</td><td>4.15</td><td>11.60</td></tr>\n    <tr><td>Trial 4</td><td>60.0</td><td>5.00</td><td>8.66</td><td>0.88</td><td>5.43</td><td>9.65</td></tr>\n  </tbody>\n</table>\n<p>Aerodynamic drag is determined to contribute less than 1.5% variance over the short flight duration, allowing pure ballistic equations to accurately predict implement trajectories.</p>",
    "qs": [
      {
        "q": "At the apogee (peak height) of the trajectory in Trial 3, what are the magnitude of velocity and the acceleration of the projectile?",
        "ch": [
          "Velocity is 0.00 m/s; acceleration is 9.80 m/s^2 directed downward.",
          "Velocity is 7.07 m/s; acceleration is 9.80 m/s^2 directed downward.",
          "Velocity is 7.07 m/s; acceleration is 0.00 m/s^2 along the trajectory.",
          "Velocity is 10.0 m/s; acceleration is 9.80 m/s^2 directed downward."
        ],
        "a": 1,
        "e": "<strong>Vector independence at apogee:</strong> At the highest point of a parabolic trajectory, the vertical component of velocity momentarily vanishes ($v_y = 0\\text{ m/s}$). However, because horizontal acceleration is zero, the horizontal velocity component remains constant throughout the flight: $v_x = v_0\\cos(45.0^\\circ) = 7.07\\text{ m/s}$. Thus, the overall velocity magnitude at apogee is $\\sqrt{v_x^2 + v_y^2} = \\sqrt{(7.07)^2 + 0^2} = 7.07\\text{ m/s}$. Gravity acts downward continuously throughout the entire flight, so acceleration is strictly $g = 9.80\\text{ m/s}^2$ downward.<br><br><em>Distractor Traps:</em><br>&bull; A confuses the total velocity with the vertical component, incorrectly assuming total velocity is zero at the peak.<br>&bull; C incorrectly assumes acceleration ceases at the peak where vertical velocity is zero.<br>&bull; D uses the initial launch speed ($v_0 = 10.0\\text{ m/s}$), neglecting the loss of vertical kinetic energy."
      },
      {
        "q": "In Trial 2, how much time elapses between implement release and the moment the shot reaches its maximum vertical elevation?",
        "ch": [
          "0.26 s",
          "1.02 s",
          "0.88 s",
          "0.51 s"
        ],
        "a": 3,
        "e": "<strong>Time to apogee derivation:</strong> The vertical velocity equation is $v_y(t) = v_{0y} - gt$. At maximum height, vertical velocity is zero: $0 = v_{0y} - gt_{apex} \\implies t_{apex} = \\frac{v_{0y}}{g}$. In Trial 2, $v_{0y} = v_0\\sin(30.0^\\circ) = 10.0 \\times 0.500 = 5.00\\text{ m/s}$. Therefore, $t_{apex} = \\frac{5.00\\text{ m/s}}{9.80\\text{ m/s}^2} \\approx 0.510\\text{ s}$.<br><br><em>Distractor Traps:</em><br>&bull; A (0.26 s) incorrectly divides by $2g$ instead of $g$.<br>&bull; B (1.02 s) represents the total round-trip flight time to return to the original release height ($2 \\times t_{apex}$).<br>&bull; C (0.88 s) uses the vertical velocity component from Trial 4 ($8.66 / 9.80$)."
      },
      {
        "q": "If the athlete increases launch velocity from 10.0 m/s to 14.0 m/s at a 45.0&deg; launch angle from ground level ($y_0 = 0$), by what percentage does the horizontal range increase?",
        "ch": [
          "40% increase",
          "70% increase",
          "96% increase",
          "140% increase"
        ],
        "a": 2,
        "e": "<strong>Range proportionality with launch speed:</strong> For a projectile launched from and returning to ground level ($y_0 = 0$), the horizontal range is given by $R = \\frac{v_0^2\\sin(2\\theta)}{g}$. For a fixed launch angle, range is directly proportional to the square of initial velocity: $R \\propto v_0^2$. Taking the ratio of new to old range: $\\frac{R_{new}}{R_{old}} = \\left(\\frac{14.0}{10.0}\\right)^2 = (1.40)^2 = 1.96$. A ratio of 1.96 corresponds to a $96\\%$ increase in range ($1.96 - 1.00 = 0.96$).<br><br><em>Distractor Traps:</em><br>&bull; A (40%) reflects a linear scaling error ($14.0 / 10.0 = 1.40$, a 40% increase), forgetting that velocity is squared.<br>&bull; B (70%) assumes range scales with $v_0 \\sqrt{2}$.<br>&bull; D (140%) is the new range expressed as a percentage of the original plus 40%."
      },
      {
        "q": "Which fundamental physical principle explains why the horizontal velocity component remains constant throughout the implement's flight?",
        "ch": [
          "Zero net horizontal force results in zero horizontal acceleration.",
          "Gravitational field lines exert equal and opposite torque vectors.",
          "Conservation of momentum strictly requires orthogonal decoupling.",
          "Centripetal forces exactly counterbalance gravitational pull vectors."
        ],
        "a": 0,
        "e": "<strong>Newton's First Law and vector independence:</strong> According to Newton's First Law of Motion, an object continues in its state of uniform motion unless acted upon by an external net force. Because gravity acts strictly in the vertical direction (downward toward Earth's center) and aerodynamic drag is neglected, the net horizontal force is zero ($F_{net,x} = 0$). By Newton's Second Law ($F_{net,x} = ma_x$), horizontal acceleration is zero ($a_x = 0$), meaning horizontal velocity $v_x$ remains constant throughout the trajectory.<br><br><em>Distractor Traps:</em><br>&bull; B invents a pseudo-scientific explanation involving gravitational torques.<br>&bull; C misapplies momentum conservation, which applies to closed multi-body systems rather than external gravitational trajectories.<br>&bull; D incorrectly introduces centripetal force into linear free-fall motion."
      },
      {
        "q": "In Trial 1 ($\theta = 0.0^\\circ$, $y_0 = 1.60\text{ m}$), what is the magnitude of the vertical component of velocity $v_y$ immediately prior to ground landing?",
        "ch": [
          "2.80 m/s",
          "5.60 m/s",
          "8.66 m/s",
          "10.0 m/s"
        ],
        "a": 1,
        "e": "<strong>Vertical velocity upon ground impact:</strong> In Trial 1, the implement is launched horizontally, so its initial vertical velocity is zero ($v_{0y} = 0\\text{ m/s}$). The vertical motion is pure free fall from rest over a vertical displacement of $\\Delta y = -1.60\\text{ m}$. Applying Torricelli's equation for the vertical axis: $v_y^2 = v_{0y}^2 + 2g|\\Delta y| = 0 + 2(9.80\\text{ m/s}^2)(1.60\\text{ m}) = 31.36\\text{ m}^2/\\text{s}^2$. Taking the square root: $|v_y| = \\sqrt{31.36} = 5.60\\text{ m/s}$.<br><br><em>Distractor Traps:</em><br>&bull; A (2.80 m/s) forgets the factor of 2 inside the square root: $\\sqrt{g \\Delta y} = \\sqrt{15.68} \\approx 3.96$, or halves 5.60.<br>&bull; C (8.66 m/s) confuses the velocity with horizontal velocity components from other trials.<br>&bull; D (10.0 m/s) is the horizontal velocity component $v_x$."
      },
      {
        "q": "Why does the optimal launch angle for achieving maximum horizontal range shift to less than 45.0&deg; when projectiles are released from an elevated platform ($y_0 > 0$)?",
        "ch": [
          "Shallower angles maximize horizontal speed without sacrificing extra flight time.",
          "Elevated launch heights increase the effective local gravitational acceleration.",
          "Horizontal drag forces decrease significantly when projectiles stay close to ground.",
          "Higher release angles cause implement rotation that disrupts laminar air streams."
        ],
        "a": 0,
        "e": "<strong>Elevated launch angle optimization:</strong> When launching from ground level ($y = 0$), $45.0^\\circ$ provides the perfect symmetry between horizontal velocity ($v_x = v_0\\cos\\theta$) and flight time ($t = 2v_0\\sin\\theta / g$). However, when launching from an elevation ($y_0 > 0$), the projectile has extra fall distance below the release point, providing extra flight time even with a smaller initial vertical velocity. Athletes can therefore trade away some vertical velocity in favor of a larger horizontal velocity ($v_x = v_0\\cos\\theta$) by using a shallower angle (typically $38^\\circ$--$42^\\circ$), maximizing horizontal distance traveled.<br><br><em>Distractor Traps:</em><br>&bull; B falsely claims that gravitational acceleration varies with small elevation changes.<br>&bull; C is incorrect because drag does not decrease near the ground.<br>&bull; D focuses on rotational aerodynamic effects, whereas the angle shift is a purely kinematic effect present even in a total vacuum."
      }
    ]
  },
  {
    "id": "exam_cp90_3_p3",
    "sec": "C/P",
    "topic": "Newton's Laws of Motion & Inertial Reference Frames in Clinical Transport and Traction",
    "sheet": 3,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_3",
    "passage": "<div class=\"ttl\">Passage 3 (Questions 13&ndash;18)</div>\n<p>Transporting critically injured trauma patients between hospital floors requires rigorous management of dynamic inertial forces. Rapid acceleration or deceleration of hospital elevators alters the apparent weight ($W_{app}$) experienced by patients, potentially exacerbating unstable cervical spine fractures or displacing orthopedic skeletal traction pins. The biomechanical interaction between a supine patient of mass $m_p = 70.0\\text{ kg}$ and an instrumented transport bed of mass $m_b = 50.0\\text{ kg}$ (total system mass $M_{sys} = 120.0\\text{ kg}$) is analyzed in an elevator cab suspended by high-tensile steel cables.</p>\n<p>According to Newton's Second Law, the motion of the patient within an inertial reference frame fixed to the elevator shaft is governed by $\\sum F_y = F_N - m_p g = m_p a$, where $F_N$ represents the upward contact normal force exerted by the mattress on the patient, $g = 9.80\\text{ m/s}^2$ is the acceleration due to gravity, and $a$ is the vertical acceleration of the elevator cab (with upward taken as positive). The apparent weight recorded by piezoresistive pressure sensors embedded beneath the mattress reflects this normal force: $W_{app} = F_N = m_p(g + a)$. Simultaneously, load cells measure the total tensile force ($T$) supported by the overhead hoist cables: $T = M_{sys}(g + a)$. Table 1 details the kinematic states, normal force readings, cable tensions, and perceived g-force ratios across five operational phases of inter-floor transit.</p>\n<table class=\"tbl\">\n  <caption>Table 1 Dynamic sensor measurements for a 70.0 kg patient on a 50.0 kg bed during elevator transit</caption>\n  <thead>\n    <tr><th>Phase</th><th>Kinematic Description</th><th>Acceleration $a$ (m/s<sup>2</sup>)</th><th>Patient Normal Force $F_N$ (N)</th><th>Cable Tension $T$ (N)</th><th>Apparent Weight Ratio ($F_N / m_p g$)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Phase 1</td><td>Stationary on ground floor</td><td>0.00</td><td>686</td><td>1176</td><td>1.00</td></tr>\n    <tr><td>Phase 2</td><td>Upward acceleration</td><td>+2.00</td><td>826</td><td>1416</td><td>1.20</td></tr>\n    <tr><td>Phase 3</td><td>Upward constant velocity (3.0 m/s)</td><td>0.00</td><td>686</td><td>1176</td><td>1.00</td></tr>\n    <tr><td>Phase 4</td><td>Upward deceleration (slowing down)</td><td>-1.80</td><td>560</td><td>960</td><td>0.82</td></tr>\n    <tr><td>Phase 5</td><td>Downward acceleration</td><td>-2.00</td><td>546</td><td>936</td><td>0.80</td></tr>\n  </tbody>\n</table>\n<p>Additionally, clinical engineers evaluate orthopedic traction setups, wherein a suspended counterweight provides continuous axial tension along fractured long bones via a low-friction pulley system.</p>",
    "qs": [
      {
        "q": "During Phase 2, what is the magnitude of the apparent weight experienced by the 70.0 kg patient as measured by the bed sensors?",
        "ch": [
          "546 N",
          "686 N",
          "966 N",
          "826 N"
        ],
        "a": 3,
        "e": "<strong>Apparent weight during upward acceleration:</strong> The apparent weight of a body is defined as the magnitude of the normal force ($F_N$) supporting it. Setting up Newton's Second Law for the patient: $\\sum F_y = F_N - m_p g = m_p a \\implies F_N = m_p(g + a)$. In Phase 2, upward acceleration is $a = +2.00\\text{ m/s}^2$. Substituting the parameters: $F_N = (70.0\\text{ kg})(9.80\\text{ m/s}^2 + 2.00\\text{ m/s}^2) = (70.0\\text{ kg})(11.80\\text{ m/s}^2) = 826\\text{ N}$.<br><br><em>Distractor Traps:</em><br>&bull; A (546 N) calculates the apparent weight during downward acceleration ($g - a = 7.80\\text{ m/s}^2$).<br>&bull; B (686 N) is the true gravitational weight ($m_p g$) when stationary or moving at constant velocity.<br>&bull; C (966 N) adds twice the acceleration or miscalculates $70 \\times 13.8$."
      },
      {
        "q": "In Phase 4, the elevator cab decelerates at $1.80\\text{ m/s}^2$ while ascending. What is the magnitude of the net force acting on the total system (patient plus bed, mass = 120.0 kg)?",
        "ch": [
          "126 N",
          "216 N",
          "960 N",
          "1176 N"
        ],
        "a": 1,
        "e": "<strong>Newton's Second Law net force calculation:</strong> According to Newton's Second Law, the net external force acting on any physical system is strictly equal to the product of total mass and acceleration: $F_{net} = M_{sys} \\cdot |a|$. For the combined patient-bed system ($M_{sys} = 70.0\\text{ kg} + 50.0\\text{ kg} = 120.0\\text{ kg}$) undergoing a deceleration magnitude of $|a| = 1.80\\text{ m/s}^2$: $F_{net} = (120.0\\text{ kg})(1.80\\text{ m/s}^2) = 216\\text{ N}$ directed downward.<br><br><em>Distractor Traps:</em><br>&bull; A (126 N) calculates the net force on the patient alone ($70.0 \\times 1.80 = 126\\text{ N}$), ignoring the bed.<br>&bull; C (960 N) is the upward cable tension $T$, not the net force.<br>&bull; D (1176 N) is the static gravitational force acting on the combined system ($M_{sys} g$)."
      },
      {
        "q": "Which pair of forces constitutes an authentic Newton's Third Law action-reaction pair in the elevator scenario?",
        "ch": [
          "Upward normal force on the patient and downward gravitational pull on patient",
          "Upward normal force on the patient and downward contact force on the mattress",
          "Upward hoist tension on elevator cab and downward gravitational pull on cab",
          "Upward normal force on the patient and downward cable tension on elevator cab"
        ],
        "a": 1,
        "e": "<strong>Newton's Third Law force pairs:</strong> Newton's Third Law states that every action force is accompanied by an equal and opposite reaction force acting on the <i>other</i> interacting body ($F_{A\\rightarrow B} = -F_{B\\rightarrow A}$). The contact normal force exerted upward by the mattress on the patient ($F_{\\text{bed}\\rightarrow\\text{patient}}$) is paired with the contact force exerted downward by the patient on the mattress ($F_{\\text{patient}\\rightarrow\\text{bed}}$). These forces are identical in magnitude, opposite in direction, and act on two distinct objects.<br><br><em>Distractor Traps:</em><br>&bull; A pairs normal force and gravity; although they may balance when stationary, both act on the patient (gravity is exerted by Earth, normal force by the bed), so they are not an action-reaction pair.<br>&bull; C pairs cable tension and gravity on the cab, which also act on the same object from different sources.<br>&bull; D connects two entirely separate contact/tension interfaces."
      },
      {
        "q": "While the elevator ascends at a constant vertical velocity of 3.0 m/s in Phase 3, how does the patient's scale reading compare to the stationary reading in Phase 1?",
        "ch": [
          "Lower, because upward motion continually reduces contact pressure against bed.",
          "Higher, because upward kinetic energy generates supplementary dynamic thrust.",
          "Identical, because zero vertical acceleration implies zero net dynamic force.",
          "Oscillating, because uniform linear velocity induces cyclic inertial waves."
        ],
        "a": 2,
        "e": "<strong>Inertial reference frames and zero acceleration:</strong> An elevator ascending at constant velocity constitutes an inertial reference frame. By Newton's First and Second Laws, if velocity is constant, acceleration is strictly zero ($a = 0$). Consequently, $\\sum F_y = F_N - m_p g = m_p(0) = 0 \\implies F_N = m_p g$. The scale reading in Phase 3 ($686\\text{ N}$) is identical to the scale reading when stationary in Phase 1 ($686\\text{ N}$). Velocity alone does not generate force; only acceleration alters apparent weight.<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly asserts that upward motion relieves weight.<br>&bull; B falsely claims kinetic energy generates an upward contact thrust.<br>&bull; D invents fictitious inertial oscillations during uniform motion."
      },
      {
        "q": "If the elevator hoist cables were to completely sever during descent, causing unrestricted free fall ($a = -9.80\\text{ m/s}^2$), what normal force would the mattress exert on the patient?",
        "ch": [
          "0.00 N",
          "343 N",
          "686 N",
          "1372 N"
        ],
        "a": 0,
        "e": "<strong>Apparent weightlessness in free fall:</strong> In unrestricted free fall, both the elevator cab and the patient accelerate downward at identical rates equal to gravitational acceleration ($a = -g$). Evaluating the normal force equation: $F_N = m_p(g + a) = m_p(g - g) = 0.00\\text{ N}$. Because both the mattress and the patient accelerate downward together at $g$, there is no mutual compressive contact force between them, resulting in complete apparent weightlessness ($F_N = 0$).<br><br><em>Distractor Traps:</em><br>&bull; B (343 N) is half the patient's stationary weight.<br>&bull; C (686 N) is the stationary gravitational weight, ignoring free fall acceleration.<br>&bull; D (1372 N) adds gravity instead of subtracting it, doubling the weight ($m_p \\times 2g$)."
      },
      {
        "q": "An orthopedic traction cable runs over a low-friction pulley and supports a suspended mass of $5.00\\text{ kg}$. During Phase 2, when the elevator accelerates upward at $2.00\\text{ m/s}^2$, what is the tension in the traction cable?",
        "ch": [
          "39.0 N",
          "49.0 N",
          "59.0 N",
          "69.0 N"
        ],
        "a": 2,
        "e": "<strong>Tension under vertical acceleration:</strong> Applying Newton's Second Law to the suspended counterweight ($m_w = 5.00\\text{ kg}$), the upward cable tension $T$ and downward gravity $m_w g$ yield a net upward acceleration $a$: $\\sum F_y = T - m_w g = m_w a \\implies T = m_w(g + a)$. Substituting $g = 9.80\\text{ m/s}^2$ and $a = +2.00\\text{ m/s}^2$: $T = (5.00\\text{ kg})(9.80 + 2.00) = (5.00\\text{ kg})(11.80\\text{ m/s}^2) = 59.0\\text{ N}$.<br><br><em>Distractor Traps:</em><br>&bull; A (39.0 N) subtracts acceleration: $5.00 \\times (9.80 - 2.00) = 39.0\\text{ N}$, which corresponds to downward acceleration.<br>&bull; B (49.0 N) is the static tension when stationary: $5.00 \\times 9.80 = 49.0\\text{ N}$.<br>&bull; D (69.0 N) adds an extra $10\\text{ N}$ or assumes $a = 4.0\\text{ m/s}^2$."
      }
    ]
  },
  {
    "id": "exam_cp90_3_p4",
    "sec": "C/P",
    "topic": "Static vs Kinetic Friction on Inclined Planes in Orthopedic Biomechanics",
    "sheet": 4,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_3",
    "passage": "<div class=\"ttl\">Passage 4 (Questions 19&ndash;24)</div>\n<p>Friction plays a dual role in orthopedic rehabilitation: high static friction is vital to prevent slips on wheelchair access ramps, whereas minimal kinetic friction is essential to prevent wear and aseptic loosening in total hip and knee arthroplasty. To evaluate joint bearing longevity and hospital surface safety, tribologists utilize an instrumented inclined plane apparatus. An articulated test sled of mass $m = 10.0\\text{ kg}$ is mounted with interchangeable material specimens and placed onto a motorized ramp whose inclination angle $\\theta$ can be continuously varied from $0.0^\\circ$ to $50.0^\\circ$.</p>\n<p>Resolving the gravitational force vector ($F_g = mg$, with $g = 9.80\\text{ m/s}^2$) into orthogonal components yields a perpendicular contact force balanced by the normal force, $F_N = mg\\cos\\theta$, and a parallel downhill driving force, $F_\\parallel = mg\\sin\\theta$. At low tilt angles, static friction opposes sliding: $f_s = mg\\sin\\theta \\le f_{s,max} = \\mu_s F_N = \\mu_s mg\\cos\\theta$. As the incline angle is incrementally increased, the sled begins to slip at a characteristic critical sliding angle $\\theta_c$, where $mg\\sin\\theta_c = \\mu_s mg\\cos\\theta_c$, establishing the mathematical relation $\\tan\\theta_c = \\mu_s$. Once motion commences, kinetic friction acts up the plane: $f_k = \\mu_k F_N = \\mu_k mg\\cos\\theta$. Applying Newton's Second Law along the incline gives the downward acceleration: $a = g(\\sin\\theta - \\mu_k\\cos\\theta)$. Table 1 displays the friction coefficients, critical slip angles, and downhill accelerations at $\\theta = 30.0^\\circ$ across four bearing and flooring interfaces.</p>\n<table class=\"tbl\">\n  <caption>Table 1 Tribological parameters and downhill kinematics of a 10.0 kg sled across test interfaces</caption>\n  <thead>\n    <tr><th>Interface</th><th>Material Pairing</th><th>Static Coeff. &mu;<sub>s</sub></th><th>Kinetic Coeff. &mu;<sub>k</sub></th><th>Critical Slip Angle &theta;<sub>c</sub> (&deg;)</th><th>Acceleration at 30.0&deg; (m/s<sup>2</sup>)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Interface 1</td><td>CoCr Alloy on Dry UHMWPE</td><td>0.25</td><td>0.18</td><td>14.0</td><td>3.37</td></tr>\n    <tr><td>Interface 2</td><td>Ceramic on Lubricated UHMWPE</td><td>0.08</td><td>0.05</td><td>4.6</td><td>4.48</td></tr>\n    <tr><td>Interface 3</td><td>Rubber Sole on Wet Aluminum Ramp</td><td>0.60</td><td>0.45</td><td>31.0</td><td>0.00</td></tr>\n    <tr><td>Interface 4</td><td>Rubber Sole on High-Traction Grit</td><td>0.90</td><td>0.70</td><td>42.0</td><td>0.00</td></tr>\n  </tbody>\n</table>\n<p>Researchers confirm that for all tested interfaces, the static friction coefficient strictly exceeds the kinetic friction coefficient ($\\mu_s > \\mu_k$), characteristic of macroscopic Coulomb friction.</p>",
    "qs": [
      {
        "q": "At the critical tilt angle $\\theta_c$ where the sled spontaneously begins to slip from rest, which formula directly expresses the static coefficient of friction $\\mu_s$?",
        "ch": [
          "&mu;<sub>s</sub> = sin &theta;<sub>c</sub>",
          "&mu;<sub>s</sub> = cos &theta;<sub>c</sub>",
          "&mu;<sub>s</sub> = cot &theta;<sub>c</sub>",
          "&mu;<sub>s</sub> = tan &theta;<sub>c</sub>"
        ],
        "a": 3,
        "e": "<strong>Critical slip angle derivation:</strong> At the verge of slipping, the parallel downhill component of gravity is precisely balanced by the maximum static friction force: $mg\\sin\\theta_c = f_{s,max} = \\mu_s F_N$. Because the normal force on an incline is $F_N = mg\\cos\\theta_c$, substituting yields $mg\\sin\\theta_c = \\mu_s mg\\cos\\theta_c$. Dividing both sides by $mg\\cos\\theta_c$ cancels the mass and gravitational constant: $\\mu_s = \\frac{\\sin\\theta_c}{\\cos\\theta_c} = \\tan\\theta_c$.<br><br><em>Distractor Traps:</em><br>&bull; A confuses tangent with sine, valid only if normal force equaled total weight.<br>&bull; B confuses tangent with cosine.<br>&bull; C inverts the trigonometric ratio (cotangent instead of tangent)."
      },
      {
        "q": "For Interface 1 sliding on an incline tilted at $30.0^\\circ$ ($\\sin 30.0^\\circ = 0.500$, $\\cos 30.0^\\circ = 0.866$), what is the magnitude of the kinetic friction force acting on the 10.0 kg sled?",
        "ch": [
          "8.82 N",
          "15.3 N",
          "24.5 N",
          "49.0 N"
        ],
        "a": 1,
        "e": "<strong>Kinetic friction on an incline:</strong> The kinetic friction force is given by $f_k = \\mu_k F_N = \\mu_k mg\\cos\\theta$. For Interface 1, $\\mu_k = 0.18$, $m = 10.0\\text{ kg}$, $g = 9.80\\text{ m/s}^2$, and $\\cos(30.0^\\circ) = 0.866$. Substituting: $f_k = (0.18)(10.0\\text{ kg})(9.80\\text{ m/s}^2)(0.866) = (0.18)(98.0\\text{ N})(0.866) = 15.28\\text{ N} \\approx 15.3\\text{ N}$.<br><br><em>Distractor Traps:</em><br>&bull; A (8.82 N) mistakenly uses $\\sin(30.0^\\circ)$ instead of $\\cos(30.0^\\circ)$: $0.18 \\times 98 \\times 0.50 = 8.82\\text{ N}$.<br>&bull; C (24.5 N) uses static friction coefficient: $0.25 \\times 98 = 24.5\\text{ N}$.<br>&bull; D (49.0 N) is the parallel gravitational force component: $mg\\sin(30.0^\\circ) = 10 \\times 9.8 \\times 0.50 = 49.0\\text{ N}$."
      },
      {
        "q": "If the mass of the sled on Interface 1 is doubled from 10.0 kg to 20.0 kg, how will the critical slip angle $\\theta_c$ be affected?",
        "ch": [
          "The critical slip angle decreases because normal force increases contact cohesion.",
          "The critical slip angle doubles because static friction force scales with mass.",
          "The critical slip angle remains unchanged because mass cancels from the force balance.",
          "The critical slip angle halves because gravitational shear forces overwhelm friction."
        ],
        "a": 2,
        "e": "<strong>Mass independence of critical slip angle:</strong> The equilibrium condition at the slip threshold is $mg\\sin\\theta_c = \\mu_s mg\\cos\\theta_c$. Because mass $m$ appears as a linear factor on both sides of the equation, it cancels entirely: $\\tan\\theta_c = \\mu_s \\implies \\theta_c = \\arctan(\\mu_s)$. Consequently, the critical slip angle depends solely on the coefficient of static friction between the contact materials, completely independent of the sled's mass.<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly asserts that increased normal force alters the friction coefficient.<br>&bull; B confuses the static friction <i>force</i> (which doubles) with the critical <i>angle</i> (which is unchanged).<br>&bull; D erroneously claims greater weight promotes easier slipping on an incline."
      },
      {
        "q": "Why does the test sled on Interface 3 remain completely stationary when the ramp is set to an inclination of $30.0^\\circ$?",
        "ch": [
          "The normal force cancels the entire magnitude of the gravitational vector.",
          "The maximum available static friction exceeds the downhill gravitational force.",
          "Kinetic friction dynamically adjusts to match downhill gravitational acceleration.",
          "Atmospheric pressure generates a downward clamping force exceeding gravity."
        ],
        "a": 1,
        "e": "<strong>Static equilibrium on an incline:</strong> For Interface 3, $\\mu_s = 0.60$. The critical slip angle is $\\theta_c = \\arctan(0.60) \\approx 31.0^\\circ$. At $\\theta = 30.0^\\circ$, the downhill gravitational driving force is $F_\\parallel = mg\\sin(30.0^\\circ) = (10)(9.8)(0.500) = 49.0\\text{ N}$. The maximum possible static friction force that the surface can provide is $f_{s,max} = \\mu_s mg\\cos(30.0^\\circ) = (0.60)(10)(9.8)(0.866) = 50.9\\text{ N}$. Because $f_{s,max} > F_\\parallel$ (50.9 N > 49.0 N), static friction easily prevents motion, providing exactly $49.0\\text{ N}$ of opposing force to keep acceleration at $0.00\\text{ m/s}^2$.<br><br><em>Distractor Traps:</em><br>&bull; A is false: normal force only cancels the perpendicular component of gravity ($mg\\cos\\theta$), not the whole vector.<br>&bull; C is false: kinetic friction only acts when an object is sliding; stationary objects experience static friction.<br>&bull; D invents atmospheric clamping."
      },
      {
        "q": "The sled with Interface 1 slides a distance of $4.00\\text{ m}$ down a $30.0^\\circ$ incline. What is the total work performed by the kinetic friction force on the sled?",
        "ch": [
          "-122 J",
          "-61.2 J",
          "+61.2 J",
          "+122 J"
        ],
        "a": 1,
        "e": "<strong>Work done by friction:</strong> Work is defined as $W = \\vec{F} \\cdot \\vec{d} = F d \\cos\\phi$. Because kinetic friction acts directly opposite to the direction of sliding motion along the ramp, the angle between the friction force and displacement is $\\phi = 180^\\circ$, giving $\\cos(180^\\circ) = -1$. Using the kinetic friction force calculated previously ($f_k = 15.3\\text{ N}$) and displacement $d = 4.00\\text{ m}$: $W_f = -f_k \\cdot d = -(15.28\\text{ N})(4.00\\text{ m}) = -61.12\\text{ J} \\approx -61.2\\text{ J}$. Friction does negative work, dissipating mechanical energy as heat.<br><br><em>Distractor Traps:</em><br>&bull; A (-122 J) multiplies by 8.0 m or uses a static coefficient.<br>&bull; C (+61.2 J) has the wrong algebraic sign: kinetic friction removes mechanical energy and thus performs negative work.<br>&bull; D (+122 J) combines a sign error with a magnitude error."
      },
      {
        "q": "As an external pulling force parallel to the surface is gradually increased on a stationary sled until it accelerates, which pattern best describes the friction force?",
        "ch": [
          "Increases linearly with applied force to a peak, then drops to a constant plateau.",
          "Remains at a fixed constant value regardless of the applied external pulling force.",
          "Grows exponentially until slipping occurs, then asymptotically approaches infinity.",
          "Follows a symmetrical parabolic arc that peaks at slip and smoothly drops to zero."
        ],
        "a": 0,
        "e": "<strong>Static vs kinetic friction force profile:</strong> While the object remains stationary, static friction exactly matches the applied external force ($f_s = F_{pull}$) to maintain zero net force. This produces a linear graph of friction versus applied force with a slope of +1. Once the applied force exceeds the maximum static friction threshold ($f_{s,max} = \\mu_s F_N$), the object breaks free and begins to slide. At that precise transition, friction drops abruptly to the kinetic friction value ($f_k = \\mu_k F_N$), which remains constant as a horizontal plateau independent of speed or applied force (for Coulomb friction).<br><br><em>Distractor Traps:</em><br>&bull; B describes kinetic friction behavior or incorrectly assumes static friction is always at its maximum.<br>&bull; C falsely describes exponential growth and asymptotic infinity.<br>&bull; D invents a parabolic decline, which contradicts the discrete step-down to constant kinetic friction."
      }
    ]
  },
  {
    "id": "exam_cp90_3_p5",
    "sec": "C/P",
    "topic": "Uniform Circular Motion & Centripetal Acceleration in Analytical Ultracentrifugation",
    "sheet": 5,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_3",
    "passage": "<div class=\"ttl\">Passage 5 (Questions 25&ndash;30)</div>\n<p>Analytical ultracentrifugation (AUC) is a cornerstone biophysical technique used to determine the molecular weight, oligomeric stoichiometry, and hydrodynamic conformation of macromolecules in native solution. When a sample solution containing proteins, lipoproteins, or viral capsids is loaded into an AUC titanium rotor and spun at high angular frequency, the particles execute uniform circular motion in a horizontal plane. Although the rotational frequency remains constant, the direction of each particle's tangential velocity vector ($\\vec{v}$) continuously changes, producing a continuous centripetal acceleration ($\\vec{a}_c$) directed radially inward toward the central axis of rotation.</p>\n<p>The magnitude of the centripetal acceleration is defined by $a_c = \\frac{v^2}{r} = \\omega^2 r$, where $r$ is the radial distance from the center of rotation to the sample cell, $v = \\omega r$ is the linear tangential speed, and $\\omega$ is the angular velocity in radians per second ($\\omega = 2\\pi \\times \\text{RPM} / 60$). By Newton's Second Law, this inward acceleration requires a net inward centripetal force, $F_c = m a_c = m \\omega^2 r$, provided by the rigid mechanical structure of the rotor holding the sample cell. In the non-inertial rotating frame of reference, particles experience an apparent outward centrifugal force that drives sedimentation against solvent buoyancy and viscous drag. Centrifugal performance is reported as the Relative Centrifugal Field (RCF), expressed in multiples of Earth's standard gravity ($g = 9.80\\text{ m/s}^2$): $\\text{RCF} = a_c / g$. Table 1 compiles rotor radii, operational speeds, centripetal accelerations, and RCF values across four analytical configurations.</p>\n<table class=\"tbl\">\n  <caption>Table 1 Ultracentrifugation kinematic and acceleration parameters for macromolecular separation</caption>\n  <thead>\n    <tr><th>Rotor Config</th><th>Radius $r$ (m)</th><th>Speed (RPM)</th><th>Angular Velocity &omega; (rad/s)</th><th>Centripetal Accel. $a_c$ (m/s<sup>2</sup>)</th><th>Relative Centrifugal Field (g)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Config A</td><td>0.050</td><td>10,000</td><td>1047</td><td>5.48 &times; 10<sup>4</sup></td><td>5,590</td></tr>\n    <tr><td>Config B</td><td>0.100</td><td>10,000</td><td>1047</td><td>1.10 &times; 10<sup>5</sup></td><td>11,200</td></tr>\n    <tr><td>Config C</td><td>0.050</td><td>40,000</td><td>4189</td><td>8.77 &times; 10<sup>5</sup></td><td>89,500</td></tr>\n    <tr><td>Config D</td><td>0.100</td><td>60,000</td><td>6283</td><td>3.95 &times; 10<sup>6</sup></td><td>403,000</td></tr>\n  </tbody>\n</table>\n<p>Optical absorbance scanners record particle boundary movement over time to calculate sedimentation coefficients without disturbing the hydrodynamic equilibrium.</p>",
    "qs": [
      {
        "q": "What is the angular velocity $\\omega$ in radians per second of an ultracentrifuge rotor operating at 10,000 RPM in Config B?",
        "ch": [
          "167 rad/s",
          "524 rad/s",
          "1047 rad/s",
          "2094 rad/s"
        ],
        "a": 2,
        "e": "<strong>Angular velocity conversion:</strong> Rotational speed in revolutions per minute (RPM) is converted to radians per second by multiplying by $2\\pi\\text{ radians}$ per revolution and dividing by $60\\text{ seconds}$ per minute: $\\omega = \\frac{2\\pi \\times 10,000\\text{ rev/min}}{60\\text{ s/min}} = \\frac{20,000\\pi}{60} = \\frac{1000\\pi}{3} \\approx \\frac{3141.59}{3} \\approx 1047\\text{ rad/s}$.<br><br><em>Distractor Traps:</em><br>&bull; A (167 rad/s) divides by 60 but omits the $2\\pi$ factor ($10,000 / 60 = 167$).<br>&bull; B (524 rad/s) multiplies by $\\pi$ instead of $2\\pi$ ($1000\\pi / 6 = 524$).<br>&bull; D (2094 rad/s) doubles the correct value ($4\\pi$ per revolution)."
      },
      {
        "q": "Comparing Config A and Config B at the same rotational speed (10,000 RPM), why is the centripetal acceleration in Config B exactly twice that in Config A?",
        "ch": [
          "Centripetal acceleration is directly proportional to radius at constant angular velocity.",
          "Tangential speed is inversely proportional to radius at constant angular velocity.",
          "Rotational kinetic energy quadruples whenever radial distance from the spindle doubles.",
          "Buoyant forces acting on the solution decrease linearly with increasing rotor radius."
        ],
        "a": 0,
        "e": "<strong>Centripetal acceleration scaling at constant angular velocity:</strong> Centripetal acceleration can be expressed either as $a_c = v^2 / r$ or as $a_c = \\omega^2 r$. When comparing two rotors operating at the same angular velocity ($\\\\omega = 1047\\text{ rad/s}$), $\\omega$ is held constant. Therefore, centripetal acceleration is strictly proportional to the first power of radius: $a_c \\propto r$. Because Config B has twice the radius of Config A ($0.100\\text{ m}$ vs $0.050\\text{ m}$), its centripetal acceleration is exactly double: $\\frac{a_{c,B}}{a_{c,A}} = \\frac{0.100}{0.050} = 2.0$.<br><br><em>Distractor Traps:</em><br>&bull; B is false: tangential speed is directly proportional to radius ($v = \\omega r$), not inversely.<br>&bull; C describes kinetic energy scaling, not acceleration.<br>&bull; D introduces buoyant forces, which do not dictate rotor centripetal acceleration."
      },
      {
        "q": "In uniform circular motion at constant angular speed, what is the net mechanical work performed by the inward centripetal force on a particle during one full revolution?",
        "ch": [
          "0.00 J, because centripetal force acts perpendicular to instantaneous displacement.",
          "2&pi; F_c r, because work equals the total inward force multiplied by circumference.",
          "0.50 m v^2, because kinetic energy is periodically replenished along orbital paths.",
          "m &omega;^2 r^2, because gravitational potential energy is converted into work."
        ],
        "a": 0,
        "e": "<strong>Work in uniform circular motion:</strong> Work is defined as the line integral of force along the path of motion: $W = \\int \\vec{F} \\cdot d\\vec{r} = \\int F \\cos\\phi \\, ds$. In uniform circular motion, the centripetal force vector $\\vec{F}_c$ is always directed radially inward toward the center of rotation, whereas the instantaneous displacement vector $d\\vec{r}$ is directed tangentially along the circumference. Because the force and displacement vectors are strictly orthogonal at every instant ($\\phi = 90^\\circ$), $\\cos(90^\\circ) = 0$. Consequently, the centripetal force does zero mechanical work ($W = 0.00\\text{ J}$). Tangential speed and kinetic energy remain constant.<br><br><em>Distractor Traps:</em><br>&bull; B computes force multiplied by circumference ($F \\times 2\\pi r$), ignoring the perpendicular vector angle.<br>&bull; C is the kinetic energy, not work.<br>&bull; D combines rotational parameters into an arbitrary energy term."
      },
      {
        "q": "If the rotational speed in Config A ($r = 0.050\\text{ m}$) is increased from 10,000 RPM to 40,000 RPM, by what factor does the centripetal acceleration increase?",
        "ch": [
          "2-fold",
          "4-fold",
          "8-fold",
          "16-fold"
        ],
        "a": 3,
        "e": "<strong>Quadratic dependence on angular velocity:</strong> Centripetal acceleration is given by $a_c = \\omega^2 r$. For a fixed radius $r$, centripetal acceleration is proportional to the square of angular velocity (or RPM): $a_c \\propto \\omega^2$. Increasing rotational speed from 10,000 RPM to 40,000 RPM represents a 4-fold increase in $\\omega$ ($\\omega_{new} = 4\\,\\omega_{old}$). Squaring this factor yields: $\\frac{a_{c,new}}{a_{c,old}} = \\left(\\frac{4\\,\\omega_{old}}{\\omega_{old}}\\right)^2 = 4^2 = 16$. Thus, the centripetal acceleration increases by a factor of 16.<br><br><em>Distractor Traps:</em><br>&bull; A (2-fold) takes the square root ($\\sqrt{4} = 2$).<br>&bull; B (4-fold) assumes a linear relationship ($a_c \\propto \\omega$).<br>&bull; C (8-fold) computes $4 \\times 2$ or $2^3$."
      },
      {
        "q": "What is the linear tangential speed $v$ of a sample cell positioned at $r = 0.100\\text{ m}$ in Config D spinning at $\\omega = 6283\\text{ rad/s}$?",
        "ch": [
          "62.8 m/s",
          "314 m/s",
          "628 m/s",
          "1256 m/s"
        ],
        "a": 2,
        "e": "<strong>Linear tangential velocity from angular velocity:</strong> Tangential speed is the product of angular velocity and radial distance: $v = \\omega r$. In Config D, $\\omega = 6283\\text{ rad/s}$ and $r = 0.100\\text{ m}$. Multiplying these values yields: $v = (6283\\text{ rad/s})(0.100\\text{ m}) = 628.3\\text{ m/s} \\approx 628\\text{ m/s}$. (This supersonic speed underscores why ultracentrifuge chambers operate under a high vacuum to eliminate aerodynamic heating).<br><br><em>Distractor Traps:</em><br>&bull; A (62.8 m/s) multiplies by 0.010 m instead of 0.100 m.<br>&bull; B (314 m/s) halves the tangential velocity ($100\\pi$).<br>&bull; D (1256 m/s) doubles the tangential velocity."
      },
      {
        "q": "Which statement accurately describes the geometric orientation of the velocity and acceleration vectors for a particle undergoing uniform circular motion?",
        "ch": [
          "Velocity is tangent to orbital path; acceleration points radially toward the center.",
          "Velocity points radially toward the center; acceleration is tangent to orbital path.",
          "Velocity and acceleration vectors both point radially outward from rotation center.",
          "Velocity and acceleration vectors both point tangentially in direction of motion."
        ],
        "a": 0,
        "e": "<strong>Vector kinematics of circular motion:</strong> In uniform circular motion, an object travels along a curved circular trajectory at constant speed. The instantaneous velocity vector $\\vec{v}$ is always tangent to the circular path in the instantaneous direction of motion. Because the velocity vector is constantly turning toward the center of curvature without changing magnitude, the instantaneous acceleration vector $\\vec{a}_c$ (centripetal acceleration) points strictly radially inward toward the center of rotation, perpendicular to the velocity vector at all times.<br><br><em>Distractor Traps:</em><br>&bull; B inverts the two vectors, assigning radial direction to velocity and tangential to acceleration.<br>&bull; C claims both vectors point outward (centrifugal misconception).<br>&bull; D claims both vectors are tangential, which would describe tangential linear acceleration (changing speed), not circular curvature."
      }
    ]
  },
  {
    "id": "exam_cp90_3_p6",
    "sec": "C/P",
    "topic": "Work-Energy Theorem & Kinetic Energy in Cardiac Hemodynamics",
    "sheet": 6,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_3",
    "passage": "<div class=\"ttl\">Passage 6 (Questions 31&ndash;6)</div>\n<p>During each cardiac cycle, the muscular wall of the human left ventricle (LV) performs mechanical work to eject oxygenated blood into the aorta against the resistive impedance of the systemic arterial tree. In clinical physiology, ventricular performance is evaluated using pressure-volume ($P$-$V$) loops obtained via conductance catheterization. The external mechanical work performed by the myocardium during a single contraction, termed stroke work ($W_{stroke}$), corresponds to the integration of ventricular pressure over the change in cavity volume: $W_{stroke} = \\oint P \\, dV$. For a simplified rectangular approximation, stroke work is calculated as the product of mean aortic ejection pressure ($P_{mean}$) and stroke volume ($\\Delta V = SV = \\text{EDV} - \\text{ESV}$), where EDV is end-diastolic volume and ESV is end-systolic volume ($1.00\\text{ mmHg} = 133.3\\text{ Pa}$, $1.00\\text{ mL} = 1.00 \\times 10^{-6}\\text{ m}^3$).</p>\n<p>According to the Work-Energy Theorem, the net mechanical work performed on a parcel of blood accelerates its mass ($m$) from rest in the ventricular cavity ($v_i = 0\\text{ m/s}$) to a peak ejection velocity ($v_f$) in the aortic root: $W_{net} = \\Delta KE = \\frac{1}{2}m v_f^2 - \\frac{1}{2}m v_i^2 = \\frac{1}{2}m v_f^2$. Assuming a physiological blood density of $\\rho = 1050\\text{ kg/m}^3$, the mass of blood ejected per stroke is $m = \\rho \\cdot SV$. Beyond accelerating blood mass, cardiac work also overcomes viscous dissipation in peripheral microvascular beds, where mechanical flow energy is irreversibly degraded into thermal energy. Table 1 lists hemodynamic parameters, ventricular stroke work, and peak aortic blood velocities across four clinical cardiovascular conditions in a 70 kg patient.</p>\n<table class=\"tbl\">\n  <caption>Table 1 Hemodynamic parameters and mechanical stroke work across physiological conditions</caption>\n  <thead>\n    <tr><th>Cardiovascular State</th><th>EDV (mL)</th><th>ESV (mL)</th><th>Stroke Vol. (mL)</th><th>Mean Pressure (mmHg)</th><th>Stroke Work (J)</th><th>Peak Velocity (m/s)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Baseline Rest</td><td>120</td><td>50</td><td>70</td><td>95</td><td>0.89</td><td>1.00</td></tr>\n    <tr><td>Strenuous Exercise</td><td>150</td><td>40</td><td>110</td><td>120</td><td>1.76</td><td>2.00</td></tr>\n    <tr><td>Severe Aortic Stenosis</td><td>130</td><td>60</td><td>70</td><td>180</td><td>1.68</td><td>4.00</td></tr>\n    <tr><td>Dilated Cardiomyopathy</td><td>200</td><td>150</td><td>50</td><td>75</td><td>0.50</td><td>0.70</td></tr>\n  </tbody>\n</table>\n<p>Continuous Doppler echocardiography confirms that blood flow profiles remain predominantly laminar in healthy aortic roots but transition to turbulent jets across stenotic valves.</p>",
    "qs": [
      {
        "q": "For the Baseline Rest state, what is the calculated external mechanical stroke work performed by the left ventricle if mean pressure is 95 mmHg ($1.27 \\times 10^4\\text{ Pa}$) and stroke volume is 70 mL ($7.0 \\times 10^{-5}\\text{ m}^3$)?",
        "ch": [
          "0.089 J",
          "0.89 J",
          "8.90 J",
          "89.0 J"
        ],
        "a": 1,
        "e": "<strong>Pressure-volume work calculation:</strong> Mechanical work is the product of pressure and volume change: $W = P \\Delta V$. Pressure must be expressed in Pascals ($\\text{N/m}^2$) and volume in cubic meters ($\\text{m}^3$): $P = 95\\text{ mmHg} \\times 133.3\\text{ Pa/mmHg} \\approx 1.266 \\times 10^4\\text{ Pa}$, and $\\Delta V = 70\\text{ mL} \\times 10^{-6}\\text{ m}^3/\\text{mL} = 7.0 \\times 10^{-5}\\text{ m}^3$. Multiplying: $W = (1.266 \\times 10^4\\text{ N/m}^2)(7.0 \\times 10^{-5}\\text{ m}^3) = 0.886\\text{ J} \\approx 0.89\\text{ J}$.<br><br><em>Distractor Traps:</em><br>&bull; A (0.089 J) divides by an extra factor of 10 or misconverts milliliters ($10^{-7}$).<br>&bull; C (8.90 J) multiplies by 10 or forgets a power of 10.<br>&bull; D (89.0 J) forgets the $10^{-6}$ volumetric conversion factor or uses Liters directly without converting to cubic meters."
      },
      {
        "q": "According to the Work-Energy Theorem, what net work must be done on an ejected blood mass of $0.070\\text{ kg}$ to accelerate it from rest to a peak velocity of $1.00\\text{ m/s}$?",
        "ch": [
          "0.018 J",
          "0.140 J",
          "0.070 J",
          "0.035 J"
        ],
        "a": 3,
        "e": "<strong>Work-Energy Theorem kinetic energy derivation:</strong> The Work-Energy Theorem establishes that the net work performed on an object equals its change in kinetic energy: $W_{net} = \\Delta KE = \\frac{1}{2}m v_f^2 - \\frac{1}{2}m v_i^2$. Because blood starts from rest within the ventricle ($v_i = 0$), the equation simplifies to $W_{net} = \\frac{1}{2}m v_f^2$. Substituting $m = 0.070\\text{ kg}$ and $v_f = 1.00\\text{ m/s}$: $W_{net} = \\frac{1}{2}(0.070\\text{ kg})(1.00\\text{ m/s})^2 = 0.035\\text{ J}$. Note that this kinetic work is a small fraction (~4%) of the total stroke work (0.89 J), the vast majority of which is expended establishing potential pressure energy.<br><br><em>Distractor Traps:</em><br>&bull; A (0.018 J) halves the result again ($0.25 \\times m v^2$).<br>&bull; B (0.140 J) doubles the kinetic energy ($2 m v^2$).<br>&bull; C (0.070 J) forgets the factor of 1/2 in kinetic energy ($m v^2$)."
      },
      {
        "q": "During Strenuous Exercise, peak aortic blood velocity increases from 1.00 m/s to 2.00 m/s. By what factor does the kinetic energy per unit volume of ejected blood increase?",
        "ch": [
          "1.4-fold",
          "2.0-fold",
          "4.0-fold",
          "8.0-fold"
        ],
        "a": 2,
        "e": "<strong>Quadratic velocity scaling of kinetic energy:</strong> Kinetic energy per unit volume is given by $\\frac{KE}{V} = \\frac{1}{2}\\rho v^2$. Because fluid density $\\rho$ remains constant, kinetic energy density scales with the square of velocity: $KE \\propto v^2$. Doubling the velocity from $1.00\\text{ m/s}$ to $2.00\\text{ m/s}$ scales the kinetic energy by a factor of: $\\frac{KE_{exercise}}{KE_{rest}} = \\left(\\frac{2.00}{1.00}\\right)^2 = 2^2 = 4.0$. Thus, kinetic energy increases 4-fold.<br><br><em>Distractor Traps:</em><br>&bull; A (1.4-fold) takes the square root ($\\sqrt{2} \\approx 1.41$).<br>&bull; B (2.0-fold) assumes a linear relationship with velocity ($KE \\propto v$).<br>&bull; D (8.0-fold) assumes a cubic power ($2^3 = 8$)."
      },
      {
        "q": "If the heart beats at a frequency of 72 beats per minute at Baseline Rest with a stroke work of 0.89 J per beat, what is the average mechanical power output of the left ventricle?",
        "ch": [
          "0.53 W",
          "1.07 W",
          "64.1 W",
          "107 W"
        ],
        "a": 1,
        "e": "<strong>Cardiac mechanical power output:</strong> Power is the rate at which work is performed: $P = \\frac{W}{\\Delta t} = W_{stroke} \\times f$, where $f$ is the heart rate in beats per second (Hertz). Converting 72 beats/min to seconds: $f = \\frac{72\\text{ beats}}{60\\text{ s}} = 1.20\\text{ beats/s}$. Multiplying by the stroke work per beat: $P = (0.89\\text{ J/beat}) \\times (1.20\\text{ beats/s}) = 1.068\\text{ W} \\approx 1.07\\text{ W}$.<br><br><em>Distractor Traps:</em><br>&bull; A (0.53 W) divides the power by 2.<br>&bull; C (64.1 W) forgets to convert minutes to seconds, multiplying $0.89 \\times 72 = 64.08\\text{ W}$.<br>&bull; D (107 W) multiplies by an erroneous factor of 100."
      },
      {
        "q": "On a diagnostic ventricular pressure-volume (P-V) loop, which geometric characteristic directly represents the net external mechanical stroke work performed during one cardiac cycle?",
        "ch": [
          "The area enclosed within the perimeter of the four phases of the loop",
          "The linear slope of the end-systolic elastance relationship boundary",
          "The horizontal width of the loop between the end-systolic and diastolic volumes",
          "The vertical height of the isovolumetric contraction segment on pressure axis"
        ],
        "a": 0,
        "e": "<strong>Geometric interpretation of P-V loops:</strong> Work is mathematically defined as the integral $\\oint P \\, dV$. On a Cartesian plot where pressure ($P$) is the vertical axis and volume ($V$) is the horizontal axis, the integral of $P$ with respect to $V$ around a closed operating trajectory corresponds exactly to the two-dimensional area enclosed within the loop boundaries. Counter-clockwise traversal of the four phases (filling, isovolumetric contraction, ejection, isovolumetric relaxation) yields net positive external mechanical work done on the vasculature.<br><br><em>Distractor Traps:</em><br>&bull; B represents myocardial contractility (end-systolic elastance $E_{es}$), not work.<br>&bull; C represents stroke volume ($SV = \\text{EDV} - \\text{ESV}$), which is only one component of work.<br>&bull; D represents the pressure developed during isovolumetric contraction without volume change ($W = 0$ during that phase)."
      },
      {
        "q": "Why does the systemic circulation require continuous ventricular mechanical work to maintain blood flow, rather than operating as a self-sustaining conservative system?",
        "ch": [
          "Non-conservative viscous drag dissipates fluid mechanical energy into heat.",
          "Negative gravitational potential energy continually destroys circulating kinetic energy.",
          "Capillary expansion breaks hydrostatic fluid columns to create energy sinks.",
          "Erythrocyte membranes absorb fluid mechanical work to drive active ion pumps."
        ],
        "a": 0,
        "e": "<strong>Non-conservative viscous dissipation in hemodynamics:</strong> A conservative mechanical system conserves the sum of kinetic and potential energy indefinitely ($\\Delta E_{mech} = 0$). In the vascular system, however, blood is a viscous fluid flowing through narrow microvessels (arterioles and capillaries). Internal fluid friction (viscosity) and shear stresses along vessel walls are non-conservative forces. As blood circulates, viscous shear performs negative work ($W_{nc} < 0$), continually degrading fluid pressure and kinetic energy into non-recoverable thermal energy (heat). The heart must continuously pump to replenish this dissipated energy and sustain circulation.<br><br><em>Distractor Traps:</em><br>&bull; B is false: the cardiovascular system is a closed hydrodynamic loop where gravity cancels out over any complete circuit.<br>&bull; C falsely claims cross-sectional expansion destroys energy.<br>&bull; D invents active transport powered directly by hydrodynamic flow work."
      }
    ]
  },
  {
    "id": "exam_cp90_3_p7",
    "sec": "C/P",
    "topic": "Conservative vs Non-Conservative Forces in Energy-Storing Prosthetics",
    "sheet": 7,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_3",
    "passage": "<div class=\"ttl\">Passage 7 (Questions 37&ndash;42)</div>\n<p>Modern running prostheses for lower-limb amputees incorporate curved, carbon-fiber composite springs (commonly termed running blades) designed to mimic the biological energy-storing function of the human Achilles tendon and gastrocnemius complex. During the initial ground-contact stance phase, downward gravitational and inertial forces compress the prosthetic leaf spring by a maximum displacement ($\\Delta x$), storing mechanical work as elastic potential energy: $U_e = \\frac{1}{2} k (\\Delta x)^2$, where $k$ is the effective spring constant. During the late stance and toe-off phases, the blade recoils elastically, returning this potential energy as forward kinetic energy to propel the runner into flight phase.</p>\n<p>In a purely conservative physical system, the mechanical energy is perfectly preserved ($\\Delta E_{mech} = \\Delta KE + \\Delta U = 0$). In physical carbon-fiber laminates and polymeric matrix resins, however, non-conservative internal frictional forces cause viscoelastic hysteresis. When plotted on a force-displacement ($F$-$x$) diagram across a complete compression-recoil cycle, the unloading recoil curve falls below the compression curve. The area bounded between these two curves represents non-conservative work ($W_{nc} = \\oint \\vec{F} \\cdot d\\vec{x} = \\Delta E_{diss}$), which is irreversibly dissipated into internal thermal energy (heat) and acoustic vibrations. Conversely, in specialized prosthetic knee orthoses, clinical engineers deliberately introduce non-conservative viscous fluid dampers ($F_d = -c v$) to dissipate excess kinetic energy during late swing phase, preventing knee hyperextension with an instantaneous rate of energy dissipation given by $P = c v^2$. Table 1 details mechanical metrics, stored energies, returned energies, and thermal dissipation measured across four prosthetic devices under standardized cyclic testing.</p>\n<table class=\"tbl\">\n  <caption>Table 1 Mechanical work, elastic energy storage, and dissipation in prosthetic springs and dampers</caption>\n  <thead>\n    <tr><th>Device</th><th>Mechanism</th><th>Stiffness $k$ (kN/m)</th><th>Peak Deflection (m)</th><th>Input Work $E_{in}$ (J)</th><th>Returned Energy $E_{out}$ (J)</th><th>Thermal Loss &Delta;E (J)</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Blade Model A</td><td>Carbon-Fiber Spring</td><td>40.0</td><td>0.050</td><td>50.0</td><td>46.0</td><td>4.0</td></tr>\n    <tr><td>Blade Model B</td><td>Stiff Sprint Blade</td><td>60.0</td><td>0.040</td><td>48.0</td><td>44.2</td><td>3.8</td></tr>\n    <tr><td>Damper Model C</td><td>Viscous Knee Orthosis</td><td>N/A</td><td>0.050</td><td>50.0</td><td>10.0</td><td>40.0</td></tr>\n    <tr><td>Ideal Spring</td><td>Theoretical Reference</td><td>40.0</td><td>0.050</td><td>50.0</td><td>50.0</td><td>0.0</td></tr>\n  </tbody>\n</table>\n<p>Materials scientists record infrared thermography during high-cadence treadmill sprints to verify that steady-state blade temperature rises match predicted cumulative hysteresis dissipation.</p>",
    "qs": [
      {
        "q": "What is the theoretical elastic potential energy stored in Blade Model A at its maximum stance deflection of $0.050\\text{ m}$ ($k = 40.0\\text{ kN/m}$)?",
        "ch": [
          "25.0 J",
          "1000 J",
          "100 J",
          "50.0 J"
        ],
        "a": 3,
        "e": "<strong>Hookean elastic potential energy:</strong> Elastic potential energy stored in an ideal spring compressed by displacement $x$ is given by $U_e = \\frac{1}{2} k x^2$. Converting the stiffness of Blade Model A to standard SI units: $k = 40.0\\text{ kN/m} = 4.00 \\times 10^4\\text{ N/m}$. The deflection is $x = 0.050\\text{ m}$. Substituting these values: $U_e = \\frac{1}{2}(4.00 \\times 10^4\\text{ N/m})(0.050\\text{ m})^2 = (2.00 \\times 10^4)(0.0025\\text{ m}^2) = 50.0\\text{ J}$.<br><br><em>Distractor Traps:</em><br>&bull; A (25.0 J) divides by 4 or mistakenly halves the correct energy.<br>&bull; B (1000 J) fails to square the deflection: $0.5 \\times 40,000 \\times 0.050 = 1000\\text{ J}$.<br>&bull; C (100 J) forgets the factor of 1/2, calculating $k x^2 = 40,000 \\times 0.0025 = 100\\text{ J}$."
      },
      {
        "q": "For Blade Model A, why is the returned mechanical energy ($46.0\\text{ J}$) during recoil strictly less than the mechanical work invested during compression ($50.0\\text{ J}$)?",
        "ch": [
          "Non-conservative internal polymeric friction dissipates mechanical energy as heat.",
          "Gravitational potential energy permanently converts mechanical energy into mass.",
          "The spring constant decreases exponentially during tensile unloading cycles.",
          "Normal force exerted by the running track does negative work on the prosthetic."
        ],
        "a": 0,
        "e": "<strong>Non-conservative dissipation via viscoelastic hysteresis:</strong> Conservative forces (such as gravity or ideal elastic springs) conserve total mechanical energy over a complete cycle ($\\Delta E_{mech} = 0$). However, real materials experience internal friction between polymer chains and carbon fiber layers as they deform. This non-conservative internal friction performs negative work on the system ($W_{nc} = -4.0\\text{ J}$), transforming ordered mechanical strain energy into disordered thermal vibration (heat) and acoustic energy. Consequently, $E_{out} = E_{in} + W_{nc} = 50.0\\text{ J} - 4.0\\text{ J} = 46.0\\text{ J}$.<br><br><em>Distractor Traps:</em><br>&bull; B invokes mass-energy equivalence, which is completely irrelevant to classical biomechanics.<br>&bull; C is incorrect: the spring constant does not exponentially decay; rather, hysteresis causes path-dependent stress-strain loops.<br>&bull; D is false: track reaction force provides boundary support, but does not absorb net energy over stance."
      },
      {
        "q": "On a force versus displacement ($F$-$x$) diagram depicting the full compression and recoil cycle of Blade Model A, what does the area enclosed between the two curves represent?",
        "ch": [
          "The net mechanical kinetic energy transferred to the runner at toe-off",
          "The quantity of thermal energy dissipated through viscoelastic hysteresis",
          "The maximum instantaneous mechanical power produced during peak stance",
          "The total gravitational potential energy gained during the airborne phase"
        ],
        "a": 1,
        "e": "<strong>Physical significance of hysteresis loops:</strong> On a force-displacement graph, the area under the compression (loading) curve represents the total mechanical work done on the spring during compression: $W_{in} = \\int F_{load} \\, dx = 50.0\\text{ J}$. The area under the recoil (unloading) curve represents the mechanical work returned by the spring to the runner: $W_{out} = \\int F_{unload} \\, dx = 46.0\\text{ J}$. The closed area enclosed between the two curves is the difference: $\\oint F \\, dx = W_{in} - W_{out} = 4.0\\text{ J}$, which corresponds precisely to the thermal energy dissipated by non-conservative hysteresis forces.<br><br><em>Distractor Traps:</em><br>&bull; A describes the area under the unloading curve ($W_{out} = 46.0\\text{ J}$), not the enclosed loop area.<br>&bull; C confuses work (area under $F$-$x$ curve) with power (rate of work over time).<br>&bull; D confuses spring hysteresis with flight gravitational potential energy."
      },
      {
        "q": "If the $46.0\\text{ J}$ of returned elastic energy from Blade Model A is converted completely into kinetic energy of a runner's leg of effective mass $5.75\\text{ kg}$ at toe-off, what is the toe-off speed?",
        "ch": [
          "2.00 m/s",
          "4.00 m/s",
          "8.00 m/s",
          "16.0 m/s"
        ],
        "a": 1,
        "e": "<strong>Kinetic energy to velocity derivation:</strong> Kinetic energy is given by $KE = \\frac{1}{2}m v^2$. Rearranging to solve for velocity: $v = \\sqrt{\\frac{2 KE}{m}}$. Substituting $KE = 46.0\\text{ J}$ and $m = 5.75\\text{ kg}$: $v = \\sqrt{\\frac{2(46.0\\text{ J})}{5.75\\text{ kg}}} = \\sqrt{\\frac{92.0}{5.75}} = \\sqrt{16.0} = 4.00\\text{ m/s}$.<br><br><em>Distractor Traps:</em><br>&bull; A (2.00 m/s) forgets the factor of 2 in the numerator: $\\sqrt{46.0 / 5.75} = \\sqrt{8.0} \\approx 2.83$, or halves the correct velocity.<br>&bull; C (8.00 m/s) multiplies by 2 outside the square root or computes $92 / 5.75 = 16$ and forgets to take the square root.<br>&bull; D (16.0 m/s) forgets to take the square root entirely ($v^2 = 16.0$)."
      },
      {
        "q": "Which mathematical criterion rigorously defines a conservative force field $\\vec{F}$ acting on an object traveling along any arbitrary closed loop path $C$?",
        "ch": [
          "&oint;<sub>C</sub> F&middot;dr = 0",
          "&oint;<sub>C</sub> F&middot;dr > 0",
          "&oint;<sub>C</sub> F&middot;dr < 0",
          "&oint;<sub>C</sub> F&times;dr = 0"
        ],
        "a": 0,
        "e": "<strong>Mathematical definition of conservative forces:</strong> A force is defined as conservative if and only if the total work done by the force around any arbitrary closed loop path is strictly zero: $\\oint_C \\vec{F} \\cdot d\\vec{r} = 0$. Equivalently, the work done between any two points is completely path-independent. Non-conservative forces (like friction or viscous drag) do negative net work over a closed path ($\\oint_C \\vec{F}_{nc} \\cdot d\\vec{r} < 0$), continually removing mechanical energy from the system.<br><br><em>Distractor Traps:</em><br>&bull; B and C describe non-conservative work over a closed trajectory where net energy is added or removed.<br>&bull; D uses a cross product instead of a scalar dot product; work is fundamentally a scalar defined by the dot product."
      },
      {
        "q": "In Damper Model C, the viscous damping force is $F_d = -c v$, where $c = 200\\text{ N}\\cdot\\text{s/m}$. At an instantaneous speed of $v = 1.50\\text{ m/s}$, what is the instantaneous rate of energy dissipation?",
        "ch": [
          "150 W",
          "300 W",
          "450 W",
          "600 W"
        ],
        "a": 2,
        "e": "<strong>Instantaneous mechanical power dissipation:</strong> Power is defined as the scalar dot product of force and velocity: $P = \\vec{F} \\cdot \\vec{v} = F v$. For a linear viscous damper where resistive force magnitude is $F_d = c v$, the rate of mechanical energy dissipation (power) is $P = (c v) v = c v^2$. Substituting $c = 200\\text{ N}\\cdot\\text{s/m}$ and $v = 1.50\\text{ m/s}$: $P = (200\\text{ N}\\cdot\\text{s/m})(1.50\\text{ m/s})^2 = (200)(2.25) = 450\\text{ W}$.<br><br><em>Distractor Traps:</em><br>&bull; A (150 W) computes $P = c v / 2$ or forgets the square and divides by 2.<br>&bull; B (300 W) computes the damping force itself ($F_d = c v = 200 \\times 1.50 = 300\\text{ N}$), confusing force with power.<br>&bull; D (600 W) doubles the force or computes $200 \\times 3.0 = 600\\text{ W}$."
      }
    ]
  },
  {
    "id": "exam_cp90_3_disc",
    "sec": "C/P",
    "topic": "C/P Standalone Discrete Questions",
    "sheet": null,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_3",
    "passage": "",
    "qs": [
      {
        "q": "During locomotion, the human Achilles tendon undergoes tensile elongation, storing elastic potential energy that is recovered during push-off. If a tendon with an effective stiffness of $k = 2.00 \\times 10^5\\text{ N/m}$ stretches elastically by $6.00\\text{ mm}$ ($6.00 \\times 10^{-3}\\text{ m}$), what is the total elastic strain energy stored within the tendon?",
        "ch": [
          "1.80 J",
          "7.20 J",
          "3.60 J",
          "12.0 J"
        ],
        "a": 2,
        "d": true,
        "e": "<strong>Hookean elastic potential energy in biological tissues:</strong> The elastic strain energy stored in a stretched tendon behaving as an ideal Hookean spring is given by $U_e = \\frac{1}{2} k x^2$. Substituting the tendon stiffness $k = 2.00 \\times 10^5\\text{ N/m}$ and displacement $x = 6.00 \\times 10^{-3}\\text{ m}$: $U_e = \\frac{1}{2}(2.00 \\times 10^5\\text{ N/m})(6.00 \\times 10^{-3}\\text{ m})^2 = (1.00 \\times 10^5)(3.60 \\times 10^{-5}\\text{ m}^2) = 3.60\\text{ J}$.<br><br><em>Distractor Traps:</em><br>&bull; A (1.80 J) divides by 4 or halves the correct energy ($0.25 \\times k x^2$).<br>&bull; B (7.20 J) forgets the factor of 1/2, calculating $k x^2 = 7.20\\text{ J}$.<br>&bull; D (12.0 J) forgets to square the displacement: $0.5 \\times (2.00 \\times 10^5) \\times (6.00 \\times 10^{-3}) = 600\\text{ J}$, or miscalculates $2 \\times 6$."
      },
      {
        "q": "A 70.0 kg athlete sprints up a stadium stairwell with a total vertical elevation gain of 6.00 m in an elapsed time of 4.00 s. Assuming acceleration due to gravity is $g = 9.80\\text{ m/s}^2$, what is the athlete's average mechanical power output against gravity?",
        "ch": [
          "257 W",
          "515 W",
          "4116 W",
          "1029 W"
        ],
        "a": 3,
        "d": true,
        "e": "<strong>Mechanical power against gravity:</strong> Power is defined as work done divided by elapsed time: $P = \\frac{W}{\\Delta t}$. The work required to elevate mass $m$ to height $h$ against gravity is equal to the change in gravitational potential energy: $W = mgh$. Calculating work: $W = (70.0\\text{ kg})(9.80\\text{ m/s}^2)(6.00\\text{ m}) = 4116\\text{ J}$. Dividing by time $\\Delta t = 4.00\\text{ s}$: $P = \\frac{4116\\text{ J}}{4.00\\text{ s}} = 1029\\text{ W}$. (Over short sprints, elite athletes can generate explosive power exceeding 1000 W).<br><br><em>Distractor Traps:</em><br>&bull; A (257 W) divides power by 4.<br>&bull; B (515 W) divides power by 2 or uses an incorrect time interval ($8.0\\text{ s}$).<br>&bull; C (4116 W) reports the total mechanical work in Joules ($W$), failing to divide by time."
      },
      {
        "q": "During a collision in ice hockey, a puck of mass 0.160 kg traveling horizontally at $35.0\\text{ m/s}$ strikes a goalkeeper's padded glove and is brought completely to rest in an impact duration of $\\Delta t = 0.0200\\text{ s}$. What is the magnitude of the average impact force exerted on the glove?",
        "ch": [
          "70.0 N",
          "140 N",
          "280 N",
          "560 N"
        ],
        "a": 2,
        "d": true,
        "e": "<strong>Impulse-momentum theorem derivation:</strong> The impulse-momentum theorem states that impulse equals change in linear momentum: $J = \\Delta p = m(v_f - v_i) = F_{avg} \\Delta t$. Here, the puck is brought to rest ($v_f = 0$), so the magnitude of momentum change is $|\\Delta p| = m |v_i| = (0.160\\text{ kg})(35.0\\text{ m/s}) = 5.60\\text{ N}\\cdot\\text{s}$. Solving for the average impact force: $F_{avg} = \\frac{|\\Delta p|}{\\Delta t} = \\frac{5.60\\text{ N}\\cdot\\text{s}}{0.0200\\text{ s}} = 280\\text{ N}$.<br><br><em>Distractor Traps:</em><br>&bull; A (70.0 N) divides by 4 or misplaces a factor of 4.<br>&bull; B (140 N) doubles the impact time or halves the force.<br>&bull; D (560 N) doubles the force or assumes an elastic rebound where $\\Delta v = 70.0\\text{ m/s}$."
      },
      {
        "q": "In an automated cell sorter, an erythrocyte of mass $m_1 = 2.00\\,\\mu\\text{g}$ moving at $v_1 = 6.00\\text{ mm/s}$ collides head-on and coalesces completely with an identical stationary cell of mass $m_2 = 2.00\\,\\mu\\text{g}$. What percentage of initial kinetic energy is lost as thermal dissipation during this collision?",
        "ch": [
          "0.0% loss",
          "25.0% loss",
          "75.0% loss",
          "50.0% loss"
        ],
        "a": 3,
        "d": true,
        "e": "<strong>Kinetic energy loss in perfectly inelastic collisions:</strong> When two bodies coalesce and stick together, the collision is perfectly inelastic. Momentum is strictly conserved: $m_1 v_1 + m_2 v_2 = (m_1 + m_2)v_f$. Substituting $v_2 = 0$: $(2.00)(6.00) + 0 = (2.00 + 2.00)v_f \\implies 12.0 = 4.00 v_f \\implies v_f = 3.00\\text{ mm/s}$. The initial kinetic energy is $KE_i = \\frac{1}{2}m_1 v_1^2 = \\frac{1}{2}(2.00)(6.00)^2 = 36.0\\text{ pJ}$. The final kinetic energy is $KE_f = \\frac{1}{2}(m_1 + m_2)v_f^2 = \\frac{1}{2}(4.00)(3.00)^2 = 18.0\\text{ pJ}$. The kinetic energy lost is $\\Delta KE = 36.0 - 18.0 = 18.0\\text{ pJ}$, which represents $\\frac{18.0}{36.0} = 50.0\\%$ of the initial kinetic energy.<br><br><em>Distractor Traps:</em><br>&bull; A (0.0% loss) assumes a perfectly elastic collision where mechanical energy is conserved.<br>&bull; B (25.0% loss) calculates $KE$ proportional to final velocity ($3/6 = 0.5$ squared is $0.25$).<br>&bull; C (75.0% loss) calculates $(1 - v_f^2 / v_i^2)$ with mismatched mass."
      },
      {
        "q": "A modular prosthetic leg is modeled as three collinear point masses along the vertical axis: foot ($m_1 = 1.00\\text{ kg}$ at $y_1 = 10.0\\text{ cm}$), lower leg ($m_2 = 3.00\\text{ kg}$ at $y_2 = 30.0\\text{ cm}$), and thigh ($m_3 = 6.00\\text{ kg}$ at $y_3 = 60.0\\text{ cm}$). What is the vertical center of mass coordinate ($y_{cm}$) of the prosthetic system?",
        "ch": [
          "46.0 cm",
          "33.3 cm",
          "40.0 cm",
          "50.0 cm"
        ],
        "a": 0,
        "d": true,
        "e": "<strong>Center of mass for discrete multi-body systems:</strong> The center of mass coordinate along a single coordinate axis is given by the mass-weighted average of position: $y_{cm} = \\frac{\\sum m_i y_i}{\\sum m_i}$. Evaluating the numerator: $\\sum m_i y_i = (1.00\\text{ kg})(10.0\\text{ cm}) + (3.00\\text{ kg})(30.0\\text{ cm}) + (6.00\\text{ kg})(60.0\\text{ cm}) = 10.0 + 90.0 + 360.0 = 460.0\\text{ kg}\\cdot\\text{cm}$. The total mass is $M_{tot} = 1.00 + 3.00 + 6.00 = 10.00\\text{ kg}$. Dividing gives: $y_{cm} = \\frac{460.0\\text{ kg}\\cdot\\text{cm}}{10.00\\text{ kg}} = 46.0\\text{ cm}$.<br><br><em>Distractor Traps:</em><br>&bull; B (33.3 cm) is the unweighted arithmetic mean of positions: $(10.0 + 30.0 + 60.0) / 3 = 33.3\\text{ cm}$.<br>&bull; C (40.0 cm) assigns equal 1/3 weighting to each position.<br>&bull; D (50.0 cm) inverts the weights or assumes the thigh dominates completely."
      },
      {
        "q": "A clinical urinometer (hydrometer) floats in pure water ($\\rho_w = 1.000\\text{ g/cm}^3$) with $82.0\\%$ of its total volume submerged. When transferred to a patient's urine specimen, the urinometer floats with $80.0\\%$ of its volume submerged. What is the specific gravity (SG) of the urine sample?",
        "ch": [
          "0.976",
          "1.000",
          "1.025",
          "1.050"
        ],
        "a": 2,
        "d": true,
        "e": "<strong>Hydrometer principle and specific gravity:</strong> A floating object displaces a weight of fluid equal to its own weight ($W = \\rho_{fluid} V_{sub} g = m_{obj} g$). Because the hydrometer's total mass $m_{obj}$ is constant: $\\rho_w V_{sub,w} = \\rho_{urine} V_{sub,urine}$. Specific gravity is the ratio of fluid density to water density: $\\text{SG} = \\frac{\\rho_{urine}}{\\rho_w} = \\frac{V_{sub,w}}{V_{sub,urine}}$. Substituting the submerged volume percentages: $\\text{SG} = \\frac{0.820\\,V_{tot}}{0.800\\,V_{tot}} = \\frac{82.0}{80.0} = 1.025$. (Normal physiological urine specific gravity ranges from 1.005 to 1.030).<br><br><em>Distractor Traps:</em><br>&bull; A (0.976) inverts the volume ratio ($80.0 / 82.0 = 0.976$), which would incorrectly indicate a fluid less dense than water.<br>&bull; B (1.000) is the specific gravity of pure water.<br>&bull; D (1.050) doubles the density increment ($1 + 2 \\times 0.025$)."
      },
      {
        "q": "In an adult patient standing erect, the vertical distance from the aortic valve to the foot is $1.35\\text{ m}$. Assuming blood density is $\\rho = 1060\\text{ kg/m}^3$, $g = 9.80\\text{ m/s}^2$, and $1.00\\text{ mmHg} = 133.3\\text{ Pa}$, what is the hydrostatic pressure difference between the heart and foot?",
        "ch": [
          "52.6 mmHg",
          "85.0 mmHg",
          "140 mmHg",
          "105 mmHg"
        ],
        "a": 3,
        "d": true,
        "e": "<strong>Hydrostatic fluid column pressure:</strong> The hydrostatic pressure difference between two points separated by vertical height $h$ in a stationary fluid column is given by $\\Delta P = \\rho g h$. Substituting $\\rho = 1060\\text{ kg/m}^3$, $g = 9.80\\text{ m/s}^2$, and $h = 1.35\\text{ m}$: $\\Delta P = (1060\\text{ kg/m}^3)(9.80\\text{ m/s}^2)(1.35\\text{ m}) = 14,023.8\\text{ Pa}$. Converting to mmHg using $1.00\\text{ mmHg} = 133.3\\text{ Pa}$: $\\Delta P = \\frac{14,023.8\\text{ Pa}}{133.3\\text{ Pa/mmHg}} = 105.2\\text{ mmHg} \\approx 105\\text{ mmHg}$. This explains why arterial blood pressure in the feet of a standing person is ~105 mmHg higher than at heart level.<br><br><em>Distractor Traps:</em><br>&bull; A (52.6 mmHg) halves the column height ($0.675\\text{ m}$).<br>&bull; B (85.0 mmHg) uses water density ($\\rho = 1000\\text{ kg/m}^3$) and misdivides by 160.<br>&bull; C (140 mmHg) forgets to divide by 133.3 or confuses column height with total height."
      },
      {
        "q": "A hydraulic hospital bed lift operates via Pascal's principle. The small circular input piston has a radius of $r_1 = 2.00\\text{ cm}$, while the load-bearing output piston has a radius of $r_2 = 12.0\\text{ cm}$. If an operator applies a downward force of $100\\text{ N}$ to the input piston, what is the maximum weight the lift can support?",
        "ch": [
          "600 N",
          "1200 N",
          "2400 N",
          "3600 N"
        ],
        "a": 3,
        "d": true,
        "e": "<strong>Pascal's principle and hydraulic force multiplication:</strong> Pascal's principle states that pressure applied to an enclosed incompressible fluid is transmitted undiminished to every portion of the fluid: $P_1 = P_2 \\implies \\frac{F_1}{A_1} = \\frac{F_2}{A_2} \\implies F_2 = F_1 \\left(\\frac{A_2}{A_1}\\right)$. The cross-sectional areas of circular pistons are proportional to the square of their radii: $\\frac{A_2}{A_1} = \\frac{\\pi r_2^2}{\\pi r_1^2} = \\left(\\frac{r_2}{r_1}\\right)^2$. Substituting $r_2 = 12.0\\text{ cm}$ and $r_1 = 2.00\\text{ cm}$: $\\frac{A_2}{A_1} = \\left(\\frac{12.0}{2.00}\\right)^2 = (6.00)^2 = 36.0$. Multiplying by input force $F_1 = 100\\text{ N}$: $F_2 = (100\\text{ N})(36.0) = 3600\\text{ N}$.<br><br><em>Distractor Traps:</em><br>&bull; A (600 N) uses the linear radius ratio ($r_2 / r_1 = 6$) rather than area ratio: $100 \\times 6 = 600\\text{ N}$.<br>&bull; B (1200 N) doubles the linear ratio ($100 \\times 12 = 1200\\text{ N}$).<br>&bull; C (2400 N) incorrectly computes $(12 / 2) \\times 400$ or miscalculates area."
      },
      {
        "q": "A researcher determines the density of a cortical bone biopsy specimen via hydrostatic weighing. The specimen registers a dry weight of $0.450\\text{ N}$ in air, but registers an apparent weight of $0.250\\text{ N}$ when completely submerged in pure water (density $\\rho_w = 1.00 \\times 10^3\\text{ kg/m}^3$). What is the specific gravity of the bone specimen?",
        "ch": [
          "0.56",
          "1.80",
          "2.25",
          "4.50"
        ],
        "a": 2,
        "d": true,
        "e": "<strong>Archimedes' principle and specific gravity:</strong> Archimedes' principle states that the buoyant force ($F_b$) on a submerged object equals the weight of displaced fluid: $F_b = W_{air} - W_{sub}$. For this specimen: $F_b = 0.450\\text{ N} - 0.250\\text{ N} = 0.200\\text{ N}$. The volume of the submerged object equals the volume of displaced water ($V = F_b / (\\rho_w g)$). The density of the object is $\\rho_{obj} = \\frac{m}{V} = \\frac{W_{air}/g}{F_b / (\\rho_w g)} = \\left(\\frac{W_{air}}{F_b}\\right)\\rho_w$. Therefore, the specific gravity is simply the ratio of weight in air to buoyant force: $\\text{SG} = \\frac{W_{air}}{F_b} = \\frac{0.450\\text{ N}}{0.200\\text{ N}} = 2.25$.<br><br><em>Distractor Traps:</em><br>&bull; A (0.56) computes $W_{sub} / W_{air} = 0.250 / 0.450 = 0.556$.<br>&bull; B (1.80) divides weight in air by submerged apparent weight ($0.450 / 0.250 = 1.80$).<br>&bull; D (4.50) divides $0.450 / 0.100$ or doubles 2.25."
      },
      {
        "q": "Jurin's law dictates that the equilibrium height $h$ to which a wetting liquid ascends in a narrow vertical tube is given by $h = \\frac{2\\gamma\\cos\\theta}{\\rho g r}$. If blood serum with contact angle $\\theta \\approx 0^\\circ$ rises to a height of $4.00\\text{ cm}$ in a glass capillary tube of inner radius $r$, what height will the serum reach in a narrower capillary tube of radius $r/2$ under identical conditions?",
        "ch": [
          "1.00 cm",
          "2.00 cm",
          "4.00 cm",
          "8.00 cm"
        ],
        "a": 3,
        "d": true,
        "e": "<strong>Capillary action and Jurin's law scaling:</strong> Jurin's law establishes that the capillary rise height is inversely proportional to the tube's inner radius: $h = \\frac{2\\gamma\\cos\\theta}{\\rho g r} \\implies h \\propto \\frac{1}{r}$. When surface tension $\\gamma$, contact angle $\\theta$, density $\\rho$, and gravity $g$ remain constant, halving the tube radius ($r_{new} = r/2$) yields: $h_{new} = \\frac{2\\gamma\\cos\\theta}{\\rho g (r/2)} = 2 \\left(\\frac{2\\gamma\\cos\\theta}{\\rho g r}\\right) = 2 h$. Therefore, the fluid will rise to twice its original height: $h_{new} = 2 \\times 4.00\\text{ cm} = 8.00\\text{ cm}$.<br><br><em>Distractor Traps:</em><br>&bull; A (1.00 cm) assumes an inverse-square relationship ($(1/2)^2 = 1/4$).<br>&bull; B (2.00 cm) assumes a direct relationship where halving radius halves height.<br>&bull; C (4.00 cm) assumes capillary height is independent of radius."
      }
    ]
  }
];
