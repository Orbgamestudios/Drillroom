# Passage 6: Topic 779 — Depth Perception Cues: Monocular vs Binocular Mechanisms
# Keys: 2, 3, 0, 1, 2, 3

p6_data = {
    "id": "exam_ps90_3_p6",
    "sec": "P/S",
    "topic": "Depth Perception Cues: Monocular vs Binocular Mechanisms",
    "sheet": 6,
    "label": "Psychological, Social, and Biological Foundations of Behavior",
    "examId": "ps90_3",
    "passage": """<div class="ttl">Passage 6 (Questions 31&ndash;36)</div>
<p>The human visual system reconstructs a three-dimensional (3D) representation of the external physical world from two-dimensional (2D) planar retinal projections by integrating binocular and monocular depth cues. Binocular cues require coordinated sensory input from both eyes. The primary binocular cue is <i>retinal disparity</i> (binocular disparity or stereopsis), arising from the horizontal separation of the eyes (interpupillary distance $\\sim 6\\text{ cm}$). Because each eye views a visual target from a slightly different vantage point, objects located closer or farther than the fixation plane (the <i>horopter</i>) cast images onto non-corresponding retinal loci. Striate cortical neurons (V1 and V2) express disparity tuning curves that quantify this angular geometric difference, generating vivid stereoscopic depth perception. A secondary binocular cue is <i>convergence</i>, a neuromuscular feedback signal mediated by kinesthetic stretch receptors and motor efference copy as the medial rectus muscles rotate the globes inward to fixate nearby targets ($< 2\\text{ to }3\\text{ m}$).</p>
<p>Monocular depth cues operate effectively with only one eye and provide essential spatial information across intermediate and distant environments. These include dynamic cues, primarily <i>motion parallax</i>&mdash;wherein an observer's self-movement causes stationary objects closer than the fixation plane to sweep rapidly across the retina in the direction opposite to observer travel, while distant objects beyond fixation drift slowly in the same direction. Monocular cues also encompass static pictorial cues: linear perspective (converging parallel lines), relative size, familiar size, interposition (occlusion of distant contours by closer objects), texture gradient (progressive densification of surface elements), relative height, and aerial/atmospheric perspective (haziness and contrast reduction caused by photon scattering in air).</p>
<p>Cognitive psychophysicists tested depth discrimination thresholds (just noticeable difference, JND, in mm; lower values indicate superior depth discrimination) in adult human observers in a high-fidelity virtual reality stereoscopic rig. Observers judged the relative depth offset between two vertical rods positioned across four viewing distances ($0.5\\text{ m}$, $2.0\\text{ m}$, $8.0\\text{ m}$, and $30.0\\text{ m}$) under four viewing conditions, as shown in Table 1.</p>
<table class="tbl">
  <caption>Table 1 Depth discrimination thresholds (JND, mm) across viewing distances and sensory viewing conditions</caption>
  <thead>
    <tr><th>Viewing Distance (m)</th><th>Condition 1: Full Binocular (Disparity + Motion)</th><th>Condition 2: Binocular Static (Disparity Only)</th><th>Condition 3: Monocular Dynamic (Motion Parallax)</th><th>Condition 4: Monocular Static (Pictorial Cues Only)</th></tr>
  </thead>
  <tbody>
    <tr><td>0.5 m (Near peripersonal)</td><td>0.8 mm</td><td>1.1 mm</td><td>4.2 mm</td><td>14.5 mm</td></tr>
    <tr><td>2.0 m (Intermediate peripersonal)</td><td>4.2 mm</td><td>5.6 mm</td><td>12.8 mm</td><td>28.4 mm</td></tr>
    <tr><td>8.0 m (Extrapersonal action space)</td><td>38.6 mm</td><td>41.2 mm</td><td>44.1 mm</td><td>62.0 mm</td></tr>
    <tr><td>30.0 m (Distant vista space)</td><td>185.0 mm</td><td>188.0 mm</td><td>192.0 mm</td><td>204.0 mm</td></tr>
  </tbody>
</table>""",
    "qs": [
      {
        "q": "Based on the psychophysical data in Table 1, why does the depth discrimination advantage of binocular viewing over monocular static viewing (Condition 2 vs Condition 4) decline dramatically as viewing distance increases from 0.5 m to 30.0 m?",
        "ch": [
          "Ciliary muscle accommodation contracts more vigorously at 30 m than at 0.5 m, overriding cortical disparity computations.",
          "Atmospheric air density selectively filters out the binocular disparity signals before electromagnetic light reaches the cornea.",
          "Retinal disparity diminishes as an inverse square function of distance, rendering binocular disparity negligible at far distances.",
          "Axons originating from nasal retinal ganglion cells fail to decussate across the optic chiasm when viewing distant landscape targets."
        ],
        "a": 2,
        "e": "<strong>Physical limits and geometric scaling of retinal disparity:</strong> The angular retinal disparity ($\\eta$) produced by a fixed depth separation ($\\Delta d$) between two objects viewed at distance $d$ is governed by the geometric relation $\\eta \\approx (I \\cdot \\Delta d) / d^2$, where $I$ is the interpupillary distance ($\sim 6\\text{ cm}$). Because disparity decreases with the square of viewing distance ($1/d^2$), binocular disparity is extraordinarily fine and dominant at near peripersonal distances ($0.5\\text{ m}$, where JND is $1.1\\text{ mm}$ for binocular vs $14.5\\text{ mm}$ for monocular static, a $>13\\text{-fold}$ advantage). At $30.0\\text{ m}$, the angular disparity subtended by small depth differences becomes smaller than the photoreceptor inter-cone spacing and optical resolving limit of the eye. Consequently, binocular disparity ceases to provide useful depth information at large distances, causing the binocular threshold ($188.0\\text{ mm}$) to converge with the monocular static threshold ($204.0\\text{ mm}$), where pictorial cues (e.g., relative size, aerial perspective) dominate.<br><br><em>Distractor Traps:</em><br>&bull; A is false: ciliary accommodation relaxes at far distances ($30\\text{ m}$) and only functions within $\sim 2\\text{ m}$.<br>&bull; B is absurd: atmospheric density does not 'filter out' angular disparities.<br>&bull; D falsely claims chiasmatic decussation depends on viewing distance."
      },
      {
        "q": "In Condition 3 (monocular dynamic), an observer traveling laterally to the right fixates their gaze steadily on a road sign located 20 m away. How do near trees (5 m) and distant mountain peaks (500 m) appear to move across the observer's visual field?",
        "ch": [
          "Both near trees and distant mountains appear stationary, as fixating on the road sign suppresses all peripheral motion perception.",
          "Both near trees and distant mountains appear to move rapidly to the right in the identical direction of the observer's travel.",
          "Near trees appear to move to the right in the direction of travel, while distant mountains move rapidly to the left in the opposite direction.",
          "Near trees appear to move rapidly to the left in the opposite direction, while distant mountains move slowly to the right with the observer."
        ],
        "a": 3,
        "e": "<strong>Optic geometry of motion parallax:</strong> Motion parallax is a powerful dynamic monocular depth cue generated by relative movement between the observer and the environment. When an observer moves laterally while maintaining fixation on an intermediate target (here, the road sign at $20\\text{ m}$), the fixation point serves as the pivot axis on the retina (zero relative motion):<br>&bull; <strong>Objects closer than the fixation point</strong> (near trees at $5\\text{ m}$): Undergo rapid retinal motion in the <i>opposite direction</i> of the observer's movement. As the observer moves right, the near trees appear to rush rapidly to the left.<br>&bull; <strong>Objects farther than the fixation point</strong> (distant mountains at $500\\text{ m}$): Undergo slow retinal motion in the <i>same direction</i> as the observer's movement. As the observer moves right, the distant mountains appear to drift slowly to the right with the observer.<br><br><em>Distractor Traps:</em><br>&bull; A incorrectly asserts that fixation suppresses peripheral motion perception.<br>&bull; B falsely claims all objects move in the same direction.<br>&bull; C inverts the relative motion directions."
      },
      {
        "q": "A child with untreated congenital strabismus (ocular misalignment) develops amblyopia. Which neurological consequence in the primary visual cortex accounts for this child's permanent loss of stereoscopic depth perception?",
        "ch": [
          "Failure of binocular disparity-tuned neurons to develop in striate cortex due to lack of correlated inputs during the critical period.",
          "Complete bilateral atrophy of the magnocellular layers of the lateral geniculate nucleus due to lack of high-frequency temporal flicker.",
          "Massive overproliferation of ocular dominance columns that completely engulf and destroy the surrounding cytochrome oxidase blobs.",
          "Irreversible mechanical degeneration of the medial and lateral rectus extraocular muscle tendons preventing all ocular motility."
        ],
        "a": 0,
        "e": "<strong>Neurobiology of strabismic amblyopia and stereoblindness:</strong> Stereoscopic depth perception requires cortical neurons in V1 and V2 that receive converging, temporally and spatially matched inputs from both eyes to compute binocular disparity. During early postnatal development (the critical period), the brain requires binocular alignment so that both retinas receive congruent, correlated visual images of the environment. In congenital strabismus (e.g., esotropia/cross-eyed or exotropia/wall-eyed), the visual axes are chronically misaligned, projecting conflicting images to the two retinas. To prevent diplopia (double vision) and visual confusion, the infant's brain actively suppresses the cortical representation of the deviating eye. Without correlated synchronous activity, binocular connections in V1 fail to mature; binocular disparity-tuned neurons are permanently lost. Even if the physical eye muscles are surgically realigned in adulthood, the cortical circuitry cannot be rewired outside the critical period, leaving the individual permanently stereoblind.<br><br><em>Distractor Traps:</em><br>&bull; B is false: the LGN maintains normal lamination, and strabismus does not cause magnocellular atrophy.<br>&bull; C invents destructive column proliferation.<br>&bull; D describes mechanical extraocular tendon damage, whereas the primary defect in amblyopia is cortical."
      },
      {
        "q": "In the classic Ponzo illusion, two identical horizontal yellow lines superimposed across converging railroad tracks appear markedly different in length. Which monocular depth cue is primarily responsible for inducing this misperception?",
        "ch": [
          "Retinal disparity, which signals that the upper line projects to non-corresponding points across the two foveas.",
          "Linear perspective, which provides converging geometric depth cues that lead the brain to scale up the perceived size of the upper line.",
          "Motion parallax, which simulates rapid translational movement across the railroad tracks to trigger false velocity calculations.",
          "Binocular convergence, which generates extraocular muscle proprioceptive strain signaling that the lower line is closer to the face."
        ],
        "a": 1,
        "e": "<strong>Linear perspective and the Ponzo illusion:</strong> The Ponzo illusion is a classic geometric optical illusion that illustrates the size-distance invariance hypothesis. In the drawing, two converging lines depict parallel railroad tracks receding into the distance—a pictorial monocular cue known as <strong>linear perspective</strong>. The visual system's perceptual constancies interpret the converging lines as indicating that the top of the image is physically farther away in depth than the bottom. Two identical horizontal bars are drawn across the tracks: one near the top (converged tracks) and one near the bottom (separated tracks). Because both bars cast identical retinal image sizes ($S_{\\text{retina}}$), the visual cortex applies the size-distance equation ($S_{\\text{perceived}} \\propto S_{\\text{retina}} \\times D_{\\text{perceived}}$). Because the top bar is judged to be at a greater distance ($D$), the visual system automatically scales up its perceived physical size, making the upper bar appear significantly longer than the lower bar.<br><br><em>Distractor Traps:</em><br>&bull; A and D refer to binocular cues (disparity and convergence), but the Ponzo illusion works perfectly in 2D drawings viewed with a single eye.<br>&bull; C refers to motion parallax, which requires physical movement and is absent in static illustrations."
      },
      {
        "q": "Based on Table 1, comparing Condition 3 (monocular dynamic) to Condition 4 (monocular static) at a viewing distance of 0.5 m reveals a decrease in JND from 14.5 mm to 4.2 mm. What conclusion does this experimental comparison support?",
        "ch": [
          "Monocular dynamic viewing completely restores depth discrimination to the exact physiological precision of full binocular stereopsis.",
          "Lateral head translation degrades depth accuracy by introducing excessive retinal motion blur and activating vestibular nystagmus.",
          "Motion parallax provides an exceptionally powerful dynamic monocular depth cue that substantially enhances spatial precision.",
          "Head movement shifts visual processing entirely from the dorsal stream to the ventral stream to activate facial recognition circuits."
        ],
        "a": 2,
        "e": "<strong>Depth enhancement via motion parallax:</strong> In Table 1, Condition 4 represents monocular static viewing (one eye patched, head stationary), which relies solely on static pictorial depth cues (JND = $14.5\\text{ mm}$ at $0.5\\text{ m}$). Condition 3 represents monocular dynamic viewing, where the observer still views with one eye but translates their head laterally, engaging motion parallax. The JND drops from $14.5\\text{ mm}$ down to $4.2\\text{ mm}$ (a $>3.4\\text{-fold}$ improvement in depth discrimination precision). This directly proves that motion parallax is a highly effective, independent depth cue that substantially enhances spatial resolution and depth accuracy even in the complete absence of binocular stereopsis.<br><br><em>Distractor Traps:</em><br>&bull; A is refuted by the data: binocular stereopsis in Condition 1 ($0.8\\text{ mm}$) remains significantly superior to monocular motion parallax ($4.2\\text{ mm}$).<br>&bull; B contradicts the empirical findings: head motion improved accuracy (lowered JND) rather than degrading it.<br>&bull; D falsely claims motion shifts processing to ventral facial recognition areas."
      },
      {
        "q": "Which of the following correctly pairs a visual depth cue with its physiological and anatomical classification?",
        "ch": [
          "Linear perspective &mdash; Binocular neuromuscular depth cue mediated by extraocular motor neurons.",
          "Retinal disparity &mdash; Monocular pictorial depth cue processed exclusively by the inferior temporal cortex.",
          "Binocular convergence &mdash; Dynamic monocular cue requiring active lateral head translation across space.",
          "Interposition (occlusion) &mdash; Monocular pictorial cue wherein a closer object partially conceals a farther object."
        ],
        "a": 3,
        "e": "<strong>Taxonomy of visual depth cues:</strong> Depth cues are fundamentally classified into binocular versus monocular mechanisms:<br>&bull; <strong>Interposition (occlusion):</strong> A classic static <i>monocular pictorial cue</i> occurring when the boundary of one opaque object partially conceals or overlaps another object, signaling that the overlapping object is closer to the viewer.<br>&bull; <strong>Linear perspective:</strong> A <i>monocular pictorial cue</i>, not a binocular neuromuscular cue.<br>&bull; <strong>Retinal disparity:</strong> A <i>binocular cue</i> (requires two eyes), computed in V1/V2 striate cortex, not a monocular cue.<br>&bull; <strong>Convergence:</strong> A <i>binocular neuromuscular cue</i> driven by medial rectus vergence, not a monocular motion cue.<br><br><em>Distractor Traps:</em><br>&bull; A, B, and C all misclassify the respective depth cues."
      }
    ]
}
