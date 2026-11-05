import json

passages = []

# ==============================================================================
# PASSAGE 1: Polyprotic Amino Acid Titrations & Active Site Microenvironments
# Topics: Histidine titration, buffering zones, equivalence points, charge transitions, pKa shifts
# ==============================================================================
p1_html = """<div class="ttl">Passage 1 (Questions 1&ndash;6)</div>
<p>Enzyme active sites frequently exploit the ionizable functional groups of amino acid side chains to mediate acid-base catalysis. Histidine (His) is an especially versatile catalytic residue because its imidazole side chain possesses an intrinsic solution $pK_a$ near physiological pH ($pK_{a1} \\text{ [}\\alpha\\text{-COOH]} = 1.82$, $pK_{a2} \\text{ [imidazole]} = 6.00$, $pK_{a3} \\text{ [}\\alpha\\text{-NH}_3^+\\text{]} = 9.17$). In aqueous solution at 298 K, a 0.10 M sample of fully protonated histidine dihydrochloride ($\\text{His}\\cdot\\text{2HCl}$, fully protonated as $\\text{H}_3\\text{His}^{2+}$) was titrated with 0.10 M standard sodium hydroxide ($\\text{NaOH}$). The pH was recorded as a function of the volume equivalents of base added ($V_{base} / V_{initial}$), revealing three distinct buffering regions and three equivalence points.</p>
<p>To investigate how local electrostatic environments modulate ionization equilibria, researchers synthesized four peptide variants of an artificial zinc metalloprotease, each containing a target histidine residue located near charged amino acid residues. The effective side-chain $pK_a$ ($pK_R$) of the active-site histidine was measured using continuous-wave electron paramagnetic resonance (EPR) and NMR titration spectroscopy. The experimental findings and microenvironmental features are compiled in Table 1.</p>
<table class="tbl">
  <caption>Table 1 Active-site histidine ionization constants and local electrostatic residues in protease variants</caption>
  <thead>
    <tr><th>Variant</th><th>Adjacent Residue(s) within 4 &Aring;</th><th>Microenvironment Dielectric Constant (&epsilon;)</th><th>Measured His $pK_R$</th><th>Catalytic Activity at pH 7.0 (% of Wild-Type)</th></tr>
  </thead>
  <tbody>
    <tr><td>Wild-Type</td><td>None (Hydrated cleft)</td><td>~65</td><td>6.05</td><td>100%</td></tr>
    <tr><td>Variant 1</td><td>Asp102 (Carboxylate anion)</td><td>~40</td><td>7.40</td><td>185%</td></tr>
    <tr><td>Variant 2</td><td>Arg115 (Guanidinium cation)</td><td>~35</td><td>4.80</td><td>15%</td></tr>
    <tr><td>Variant 3</td><td>Leu88, Val92 (Hydrophobic core)</td><td>~10</td><td>5.10</td><td>25%</td></tr>
    <tr><td>Variant 4</td><td>Glu105, Lys108 (Salt bridge pair)</td><td>~45</td><td>6.10</td><td>98%</td></tr>
  </tbody>
</table>
<p>During the catalytic cycle, the target histidine alternates between a protonated, positively charged conjugate acid form ($\\text{His-H}^+$) and a neutral conjugate base form ($\\text{His}^0$), acting as a general base to deprotonate a nucleophilic water molecule coordinated to the active-site zinc ion ($\\text{Zn}^{2+}$).</p>"""

p1_qs = [
    {
        "q": "What is the net electrical charge of the predominant histidine species in an aqueous solution buffered at pH 7.58?",
        "ch": [
            "+1.00",
            "+0.50",
            "0.00",
            "-1.00"
        ],
        "a": 2,
        "e": "<strong>At pH 7.58:</strong> The pH is well above $pK_{a1}$ (1.82, so $\\alpha$-COOH is deprotonated to -1) and above $pK_{a2}$ (6.00, so the imidazole side chain is deprotonated to neutral 0), but below $pK_{a3}$ (9.17, so the $\\alpha$-amino group remains protonated to +1). Summing the partial charges yields: $-1 (\\alpha\\text{-COO}^-) + 0 (\\text{imidazole}) + 1 (\\alpha\\text{-NH}_3^+) = 0.00$. In fact, the isoelectric point of histidine is $pI = (pK_{a2} + pK_{a3})/2 = (6.00 + 9.17)/2 = 7.585$, where the net charge is exactly zero.<br><br><em>Distractor Traps:</em><br>&bull; A (+1.00) mistakenly calculates the net charge below the imidazole $pK_a$ (pH < 6.0).<br>&bull; B (+0.50) confuses the half-equivalence point buffering state with the isoelectric state.<br>&bull; D (-1.00) assumes all three ionizable groups are deprotonated (which only occurs at pH > 10)."
    },
    {
        "q": "According to the data in Table 1, the imidazole side chain in Variant 1 exhibits an elevated pK_R relative to the wild-type primarily because:",
        "ch": [
            "the nearby carboxylate group of Asp102 destabilizes the neutral imidazole conjugate base.",
            "the electrostatic attraction from Asp102 stabilizes the protonated cationic form of the histidine.",
            "the nonpolar hydrophobic microenvironment disfavors the formation of localized ionic species.",
            "the high dielectric constant of the surrounding solvent shields ionic electrostatic attraction."
        ],
        "a": 1,
        "e": "<strong>Electrostatic stabilization of conjugate acids:</strong> A higher $pK_a$ means the functional group holds onto its proton more tightly, shifting the equilibrium $\\text{His-H}^+ \\rightleftharpoons \\text{His}^0 + \\text{H}^+$ to the left. Asp102 bears a negatively charged carboxylate group ($\\text{COO}^-$). When histidine is protonated, it bears a formal positive charge ($\\text{ImH}^+$), creating a favorable electrostatic interaction (salt bridge/ion pair) with Asp102. This stabilizes the conjugate acid form, lowering its free energy and raising the $pK_R$ to 7.40.<br><br><em>Distractor Traps:</em><br>&bull; A reverses the thermodynamic effect: the primary driving factor is stabilizing the cation, not destabilizing the neutral base.<br>&bull; C describes Variant 3 (hydrophobic core), where nonpolar solvents decrease $pK_a$ by destabilizing charged species.<br>&bull; D contradicts the data: Variant 1 has a lower dielectric constant ($\epsilon = 40$) than wild-type ($\epsilon = 65$)."
    },
    {
        "q": "In the titration of 100 mL of 0.10 M fully protonated histidine dihydrochloride with 0.10 M NaOH, what total volume of titrant is required to reach the second equivalence point?",
        "ch": [
            "100 mL",
            "150 mL",
            "200 mL",
            "300 mL"
        ],
        "a": 2,
        "e": "<strong>Equivalence point stoichiometry:</strong> The initial moles of histidine are $n = M \\times V = 0.10\\text{ M} \\times 0.100\\text{ L} = 0.010\\text{ mol}$. Each equivalence point represents the quantitative neutralization of one mole of acidic protons per mole of histidine by 1 molar equivalent of $\\text{OH}^-$. At the first equivalence point, 0.010 mol of NaOH is consumed (neutralizing the $\\alpha$-COOH group), which requires $V_1 = 0.010\\text{ mol} / 0.10\\text{ M} = 0.100\\text{ L} = 100\\text{ mL}$. To reach the second equivalence point, the imidazole protons are neutralized as well, requiring an additional 0.010 mol of $\\text{OH}^-$, bringing the cumulative titrant volume to $100\\text{ mL} + 100\\text{ mL} = 200\\text{ mL}$.<br><br><em>Distractor Traps:</em><br>&bull; A (100 mL) is the volume to reach the first equivalence point.<br>&bull; B (150 mL) corresponds to the second half-equivalence point where $\\text{pH} = pK_{a2}$.<br>&bull; D (300 mL) is the volume required to reach the third equivalence point."
    },
    {
        "q": "At physiological pH 7.00, what is the approximate ratio of deprotonated conjugate base to protonated conjugate acid ([His^0] / [His-H^+]) for the catalytic histidine in Variant 2 (pK_R = 4.80)?",
        "ch": [
            "0.0063 : 1",
            "1 : 1",
            "158 : 1",
            "1600 : 1"
        ],
        "a": 2,
        "e": "<strong>Henderson-Hasselbalch calculation:</strong> The Henderson-Hasselbalch equation states $\\text{pH} = pK_a + \\log([\\text{A}^-]/[\\text{HA}])$. Rearranging: $\\log([\\text{His}^0]/[\\text{His-H}^+]) = \\text{pH} - pK_R = 7.00 - 4.80 = +2.20$. Converting from logarithm to linear scale: $[\\text{His}^0]/[\\text{His-H}^+] = 10^{2.20} = 10^2 \\times 10^{0.20} \\approx 100 \\times 1.58 = 158$. Thus, the ratio of deprotonated base to protonated acid is approximately 158 : 1.<br><br><em>Distractor Traps:</em><br>&bull; A ($0.0063 : 1 = 10^{-2.2}$) inverts the numerator and denominator, calculating $[\\text{His-H}^+]/[\\text{His}^0]$.<br>&bull; B ($1:1$) corresponds to $\\text{pH} = pK_a$.<br>&bull; D (1600 : 1) miscalculates $10^{2.20}$ as $10^{3.20}$."
    },
    {
        "q": "Based on the passage, why does Variant 2 exhibit a substantial reduction in catalytic activity at pH 7.00 compared to the wild-type enzyme?",
        "ch": [
            "The basic guanidinium group irreversibly binds and hydrolyzes the peptide backbone.",
            "The low pK_R shifts the equilibrium so that less than 1% remains in the protonated acid form.",
            "The elevated dielectric constant accelerates the spontaneous dissociation of active-site zinc ions.",
            "The mutation converts the active-site histidine into a nonpolar aromatic phenylalanine residue."
        ],
        "a": 1,
        "e": "<strong>Mechanistic equilibrium of general acid-base catalysis:</strong> Efficient general acid-base catalysis requires that both the proton donor and acceptor forms exist in sufficient quantities at physiological pH. For Variant 2 ($pK_R = 4.80$), at pH 7.0, the ratio of $[\\text{His}^0]/[\\text{His-H}^+]$ is ~158:1, meaning that >99.4% is deprotonated and less than 0.6% exists in the protonated form needed to complete the catalytic turnover, severely diminishing enzymatic velocity.<br><br><em>Distractor Traps:</em><br>&bull; A invents non-enzymatic backbone cleavage not described in the passage.<br>&bull; C contradicts Table 1, which shows $\\epsilon$ decreased from 65 to 35.<br>&bull; D fabricates an amino acid substitution in His itself rather than the adjacent residue Arg115."
    },
    {
        "q": "Which titration curve region corresponds to the highest buffering capacity for the imidazole side chain of free aqueous histidine?",
        "ch": [
            "pH 1.30 to 2.30",
            "pH 5.50 to 6.50",
            "pH 7.10 to 8.10",
            "pH 9.70 to 10.70"
        ],
        "a": 1,
        "e": "<strong>Maximum buffering capacity:</strong> Maximum buffering capacity for any weak acid occurs when $\\text{pH} = pK_a$, and extends within approximately $\\pm 1.0$ pH unit of the $pK_a$. For the imidazole side chain of free histidine, $pK_{a2} = 6.00$. Therefore, the region of highest imidazole buffering capacity is centered at pH 6.00, corresponding to pH 5.0 to 7.0 (and most strongly in pH 5.50 to 6.50).<br><br><em>Distractor Traps:</em><br>&bull; A (pH 1.30 to 2.30) is the buffering region for the $\\alpha$-carboxyl group ($pK_{a1} = 1.82$).<br>&bull; C (pH 7.10 to 8.10) is centered around the isoelectric point ($pI = 7.58$), which has minimal buffering capacity.<br>&bull; D (pH 9.70 to 10.70) is above the $\\alpha$-amino group buffering range ($pK_{a3} = 9.17$)."
    }
]

passages.append({
    "id": "exam_cp90_2_p1",
    "sec": "C/P",
    "topic": "Polyprotic Amino Acid Titrations & Active Site Microenvironments",
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_2",
    "passage": p1_html,
    "qs": p1_qs
})

print("Passage 1 defined.")

# ==============================================================================
# PASSAGE 2: Galvanic Concentration Cells & Transcellular Electrochemical Potentials
# Topics: Nernst equation, concentration cells, resting membrane potential, ion gradients
# ==============================================================================
p2_html = """<div class="ttl">Passage 2 (Questions 7&ndash;12)</div>
<p>Living cells maintain transcellular electrochemical gradients using membrane-bound ATPases, converting chemical potential energy into electrical energy analogous to a galvanic concentration cell. A concentration cell consists of two identical half-cells containing the same electroactive species at different concentrations ($C_1 < C_2$), separated by a semipermeable partition or salt bridge. The electromotive force ($E_{cell}$) generated by the spontaneous flow of charge is governed by the Nernst equation:</p>
<p>$$E_{cell} = E^\\circ_{cell} - \\frac{RT}{zF} \\ln Q$$</p>
<p>Because the chemical species in both compartments are identical, standard reduction potentials cancel, yielding $E^\\circ_{cell} = 0\\text{ V}$. At physiological temperature ($T = 310\\text{ K}$, $37^\\circ\\text{C}$), substituting universal constants ($R = 8.314\\text{ J}/(\\text{mol}\\cdot\\text{K})$, $F = 96,485\\text{ C/mol}$) and converting natural logarithms to base-10 yields the simplified expression:</p>
<p>$$E_{cell} = -\\frac{0.0615\\text{ V}}{z} \\log_{10} \\left( \\frac{C_{dilute}}{C_{concentrated}} \\right) = \\frac{0.0615\\text{ V}}{z} \\log_{10} \\left( \\frac{C_{concentrated}}{C_{dilute}} \\right)$$</p>
<p>Neurobiologists designed an in vitro bio-electrochemical apparatus to model the resting membrane potential generated by potassium ($\\text{K}^+$, $z = +1$) and calcium ($\\text{Ca}^{2+}$, $z = +2$) gradients across an artificial planar lipid bilayer containing selective ionophore channels. Table 1 summarizes the measured electromotive potentials across four experimental configurations at 310 K.</p>
<table class="tbl">
  <caption>Table 1 Measured electromotive force across planar lipid bilayers with varying ion concentrations</caption>
  <thead>
    <tr><th>Trial</th><th>Permeant Cation ($z$)</th><th>Compartment 1 [C1] (mM)</th><th>Compartment 2 [C2] (mM)</th><th>Measured $E_{cell}$ (mV)</th><th>Direction of Spontaneous Cation Flow</th></tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>$\\text{K}^+$ ($+1$)</td><td>14.0</td><td>140.0</td><td>+61.5</td><td>Compartment 2 &rarr; Compartment 1</td></tr>
    <tr><td>2</td><td>$\\text{K}^+$ ($+1$)</td><td>1.4</td><td>140.0</td><td>+123.0</td><td>Compartment 2 &rarr; Compartment 1</td></tr>
    <tr><td>3</td><td>$\\text{Ca}^{2+}$ ($+2$)</td><td>0.10</td><td>10.0</td><td>+61.5</td><td>Compartment 2 &rarr; Compartment 1</td></tr>
    <tr><td>4</td><td>$\\text{Ca}^{2+}$ ($+2$)</td><td>0.010</td><td>10.0</td><td>+92.3</td><td>Compartment 2 &rarr; Compartment 1</td></tr>
  </tbody>
</table>
<p>In Trial 5, researchers added the pore-forming ionophore gramicidin D, which permits nonselective monovalent cation flux, while adding 5.0 mM ATP to drive an active electrogenic sodium-potassium exchanger ($\\text{Na}^+/\\text{K}^+\\text{-ATPase}$).</p>"""

p2_qs = [
    {
        "q": "What is the theoretical standard cell potential (E_cell^o) for any galvanic concentration cell operating under standard conditions?",
        "ch": [
            "-0.615 V",
            "0.000 V",
            "+0.0615 V",
            "+1.100 V"
        ],
        "a": 1,
        "e": "<strong>Standard cell potential of concentration cells:</strong> Standard state conditions require all dissolved species to have a concentration of 1.0 M. In a concentration cell, both half-cells utilize the identical chemical species (e.g., $\\text{K}^+ + e^- \\rightleftharpoons \\text{K}$). Consequently, the standard reduction potential of the cathode ($E^\\circ_{red}$) is identical in magnitude and sign to the standard reduction potential of the anode ($E^\\circ_{red}$). Therefore, $E^\\circ_{cell} = E^\\circ_{cathode} - E^\\circ_{anode} = 0.000\\text{ V}$. The driving force ($E_{cell} > 0$) arises entirely from the entropy of mixing and concentration difference ($Q < 1$).<br><br><em>Distractor Traps:</em><br>&bull; A and C confuse the Nernst slope prefactor ($0.0615\\text{ V}$) with the standard cell potential.<br>&bull; D is the standard potential of a standard Daniell zinc-copper galvanic cell."
    },
    {
        "q": "In Trial 3, a tenfold increase in the calcium concentration ratio ([C2]/[C1] from 100 to 1,000 in Trial 4) increased the cell potential by approximately:",
        "ch": [
            "15.4 mV",
            "30.8 mV",
            "61.5 mV",
            "92.3 mV"
        ],
        "a": 1,
        "e": "<strong>Nernst sensitivity for divalent cations:</strong> For a divalent cation like $\\text{Ca}^{2+}$ ($z = +2$), the Nernst relationship yields $\\Delta E = (0.0615\\text{ V} / z) \\times \\Delta \\log_{10}(\\text{ratio}) = (61.5\\text{ mV} / 2) \\times \\log_{10}(10) = 30.75\\text{ mV} \\approx 30.8\\text{ mV}$. Trial 3 had $E = 61.5\\text{ mV}$ and Trial 4 had $E = 92.3\\text{ mV}$; the difference is $92.3 - 61.5 = 30.8\\text{ mV}$.<br><br><em>Distractor Traps:</em><br>&bull; A (15.4 mV) mistakenly divides by $z = 4$.<br>&bull; C (61.5 mV) calculates the shift for a monovalent cation ($z = 1$) across a 10-fold concentration change.<br>&bull; D (92.3 mV) is the absolute cell potential of Trial 4, not the change between trials."
    },
    {
        "q": "What is the standard Gibbs free energy change (Delta G^o) for the electrochemical cell reaction occurring in Trial 1?",
        "ch": [
            "-5.93 kJ/mol",
            "0.00 kJ/mol",
            "+5.93 kJ/mol",
            "+11.87 kJ/mol"
        ],
        "a": 1,
        "e": "<strong>Distinction between $\\Delta G^\\circ$ and $\\Delta G$:</strong> The standard Gibbs free energy change is defined by $\\Delta G^\\circ = -zFE^\\circ_{cell}$. As established in the passage and standard electrochemistry, the standard cell potential $E^\\circ_{cell}$ for any concentration cell is identically $0.00\\text{ V}$ because the chemical identities in both compartments are identical. Thus, $\\Delta G^\\circ = -zF(0) = 0.00\\text{ kJ/mol}$. Under actual operational conditions, $\\Delta G = -zFE_{cell} = -(1)(96,485)(0.0615\\text{ V}) = -5.93\\text{ kJ/mol}$, but $\\Delta G^\\circ$ is zero.<br><br><em>Distractor Traps:</em><br>&bull; A (-5.93 kJ/mol) calculates the non-standard free energy change $\\Delta G$, failing to heed the degree symbol ($^\\circ$).<br>&bull; C (+5.93 kJ/mol) has the wrong thermodynamic sign and refers to non-standard state.<br>&bull; D (+11.87 kJ/mol) calculates $2 \\times 5.93$ with the wrong sign."
    },
    {
        "q": "If the temperature of the apparatus in Trial 1 were increased from 310 K to 330 K while keeping all ion concentrations constant, the measured cell potential would:",
        "ch": [
            "decrease because elevated thermal motion accelerates spontaneous ion recombination.",
            "increase because the Nernst potential is directly proportional to absolute temperature.",
            "remain unchanged because the standard cell potential E^o is independent of temperature.",
            "drop immediately to zero because elevated thermal fluctuations rupture lipid bilayers."
        ],
        "a": 1,
        "e": "<strong>Temperature dependence of electrochemical potentials:</strong> In the Nernst equation, $E_{cell} = (RT / zF) \\ln([C_{conc}]/[C_{dil}])$. Because $R$, $z$, $F$, and the concentration ratio are constant, $E_{cell}$ is directly proportional to the absolute temperature $T$ in Kelvin ($E \\propto T$). Increasing temperature from 310 K to 330 K increases the thermal driving force (entropy of dispersion), increasing the measured electromotive force from $61.5\\text{ mV}$ to $61.5 \\times (330/310) = 65.5\\text{ mV}$.<br><br><em>Distractor Traps:</em><br>&bull; A asserts a decrease based on vague 'ion recombination'.<br>&bull; C confuses $E^\\circ$ with the operating potential $E_{cell}$.<br>&bull; D is an unjustified extreme scenario: biological membranes remain intact at 330 K (57 &deg;C)."
    },
    {
        "q": "As current flows spontaneously in Trial 1, which process occurs at the cathode compartment (Compartment 1, 14.0 mM K^+)?",
        "ch": [
            "Potassium ions are oxidized to elemental potassium metal.",
            "Electrons are consumed as potassium ions are reduced at the electrode.",
            "Potassium ions are actively pumped against their concentration gradient.",
            "Anions are generated by spontaneous catalytic water splitting."
        ],
        "a": 1,
        "e": "<strong>Reduction at the cathode:</strong> In all electrochemical cells (both galvanic and electrolytic), reduction occurs at the cathode ('RED CAT'). In a concentration cell, spontaneous reduction occurs in the more dilute compartment (Compartment 1) where cations accept electrons ($\\text{K}^+ + e^- \\rightarrow \\text{K}$) to deposit on or amalgamate at the electrode, while oxidation occurs in the concentrated compartment, moving both half-cells toward equilibrium ($Q \\rightarrow 1$).<br><br><em>Distractor Traps:</em><br>&bull; A reverses the electrodes: oxidation occurs at the anode ('AN OX').<br>&bull; C describes active transport requiring an ATPase, not spontaneous galvanic discharge.<br>&bull; D invents water electrolysis, which requires external overpotential exceeding 1.23 V."
    },
    {
        "q": "The biological Na^+/K^+-ATPase pump is classified as electrogenic primarily because each catalytic turnover:",
        "ch": [
            "exports 3 Na^+ ions and imports 2 K^+ ions, generating a net outward positive current.",
            "exports 2 Na^+ ions and imports 3 K^+ ions, producing an intracellular accumulation of cations.",
            "pumps equal equivalents of Na^+ and Cl^- across the membrane without net charge displacement.",
            "hydrolyzes two molecules of ATP to transport a single univalent sodium cation."
        ],
        "a": 0,
        "e": "<strong>Electrogenic stoichiometry:</strong> The $\\text{Na}^+/\\text{K}^+$-ATPase transports 3 $\\text{Na}^+$ ions outward toward the extracellular space and 2 $\\text{K}^+$ ions inward toward the cytosol per molecule of ATP hydrolyzed. Because there is a net transcellular translocation of one net positive charge ($+3 - 2 = +1$) out of the cell per cycle, it directly generates an electrical current and hyperpolarizes the membrane potential (making the interior more negative).<br><br><em>Distractor Traps:</em><br>&bull; B reverses the stoichiometry (would make interior positive).<br>&bull; C describes an electroneutral symporter like NKCC2 or NCC.<br>&bull; D states incorrect ATP stoichiometry (1 ATP is hydrolyzed per 3 $\\text{Na}^+$ / 2 $\\text{K}^+$)."
    }
]

passages.append({
    "id": "exam_cp90_2_p2",
    "sec": "C/P",
    "topic": "Galvanic Concentration Cells & Transcellular Electrochemical Potentials",
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_2",
    "passage": p2_html,
    "qs": p2_qs
})

print("Passage 2 defined.")

# ==============================================================================
# PASSAGE 3: Solubility Equilibria & Calcium Oxalate Nephrolithiasis
# Topics: Ksp, common-ion effect, selective precipitation, Qsp vs Ksp, urinary citrate chelation
# ==============================================================================
p3_html = """<div class="ttl">Passage 3 (Questions 13&ndash;18)</div>
<p>Nephrolithiasis (kidney stone formation) is a common urological disorder most frequently caused by the pathological precipitation of calcium oxalate monohydrate ($\\text{CaC}_2\\text{O}_4\\cdot\\text{H}_2\\text{O}$, abbreviated $\\text{CaOx}$) within renal tubules. In aqueous urine, the dissolution equilibrium of calcium oxalate is expressed as:</p>
<p>$$\\text{CaC}_2\\text{O}_4(s) \\rightleftharpoons \\text{Ca}^{2+}(aq) + \\text{C}_2\\text{O}_4^{2-}(aq) \\quad K_{sp} = 2.3 \\times 10^{-9} \\text{ at } 310\\text{ K}$$</p>
<p>Spontaneous nucleation and crystal growth occur whenever the ion product ($Q_{sp} = [\\text{Ca}^{2+}][\\text{C}_2\\text{O}_4^{2-}]$) exceeds the thermodynamic solubility product constant ($K_{sp}$). Urine supersaturation ($SS = Q_{sp} / K_{sp}$) is modulated by daily urinary fluid volume, dietary oxalate ingestion, hypercalciuria, and endogenous crystallization inhibitors such as citrate ($\\text{C}_6\\text{H}_5\\text{O}_7^{3-}$). Citrate forms a soluble, poorly dissociable coordination complex with calcium ions:</p>
<p>$$\\text{Ca}^{2+}(aq) + \\text{Citrate}^{3-}(aq) \\rightleftharpoons [\\text{Ca-Citrate}]^-(aq) \\quad K_f = 2.0 \\times 10^3$$</p>
<p>Clinical biochemists evaluated four urine samples from recurrent stone formers and healthy controls to determine free calcium, free oxalate, and citrate concentrations. The analytical findings and observed precipitation behaviors are compiled in Table 1.</p>
<table class="tbl">
  <caption>Table 1 Urinary electrolyte concentrations, citrate levels, and calcium oxalate saturation indices</caption>
  <thead>
    <tr><th>Patient Sample</th><th>Total $[\\text{Ca}^{2+}]$ (mM)</th><th>Total $[\\text{C}_2\\text{O}_4^{2-}]$ (mM)</th><th>Citrate (mM)</th><th>Calculated Free $[\\text{Ca}^{2+}]$ (mM)</th><th>Observed CaOx Precipitation</th></tr>
  </thead>
  <tbody>
    <tr><td>Control A</td><td>1.2</td><td>0.15</td><td>3.5</td><td>0.14</td><td>None</td></tr>
    <tr><td>Patient 1 (Hypocitraturia)</td><td>1.5</td><td>0.25</td><td>0.4</td><td>1.10</td><td>Rapid microcrystal nucleation</td></tr>
    <tr><td>Patient 2 (Hyperoxaluria)</td><td>1.2</td><td>1.20</td><td>3.2</td><td>0.15</td><td>Moderate macrolith growth</td></tr>
    <tr><td>Patient 3 (Hypercalciuria)</td><td>4.5</td><td>0.20</td><td>1.8</td><td>1.85</td><td>Extensive crystal agglomeration</td></tr>
  </tbody>
</table>
<p>To evaluate potential pharmacological interventions, the researchers supplemented Patient 1's urine in vitro with potassium citrate ($\\text{K}_3\\text{C}_6\\text{H}_5\\text{O}_7$) or sodium sulfate ($\\text{Na}_2\\text{SO}_4$). Sulfate forms a weakly soluble ion pair with calcium ($\\text{CaSO}_4$, $K_{sp} = 2.4 \\times 10^{-5}$).</p>"""

p3_qs = [
    {
        "q": "What is the molar solubility of pure calcium oxalate in distilled water at 310 K (K_sp = 2.3 x 10^-9)?",
        "ch": [
            "2.4 x 10^-5 M",
            "4.8 x 10^-5 M",
            "1.1 x 10^-4 M",
            "2.3 x 10^-9 M"
        ],
        "a": 1,
        "e": "<strong>Molar solubility from $K_{sp}$:</strong> Calcium oxalate dissolves via $\\text{CaC}_2\\text{O}_4(s) \\rightleftharpoons \\text{Ca}^{2+}(aq) + \\text{C}_2\\text{O}_4^{2-}(aq)$. If $x$ is the molar solubility, $[\\text{Ca}^{2+}] = x$ and $[\\text{C}_2\\text{O}_4^{2-}] = x$. Thus, $K_{sp} = x^2 = 2.3 \\times 10^{-9}$. Taking the square root: $x = \\sqrt{2.3 \\times 10^{-9}} = \\sqrt{23 \\times 10^{-10}} \\approx 4.8 \\times 10^{-5}\\text{ M}$.<br><br><em>Distractor Traps:</em><br>&bull; A ($2.4 \\times 10^{-5}\\text{ M}$) mistakenly divides $K_{sp}$ by 100 before square rooting.<br>&bull; C ($1.1 \\times 10^{-4}\\text{ M}$) calculates $\\sqrt{2.3} \\times 10^{-4} = 1.5 \\times 10^{-4}$ with arithmetic error.<br>&bull; D ($2.3 \\times 10^{-9}\\text{ M}$) equates molar solubility directly to the numerical value of $K_{sp}$."
    },
    {
        "q": "In Patient 1, the calculated free ion product Q_sp for calcium oxalate is approximately:",
        "ch": [
            "5.5 x 10^-11",
            "2.8 x 10^-7",
            "3.8 x 10^-4",
            "1.1 x 10^-3"
        ],
        "a": 1,
        "e": "<strong>Ion product calculation:</strong> In Patient 1, the free calcium concentration is $1.10\\text{ mM} = 1.10 \\times 10^{-3}\\text{ M}$, and the total oxalate concentration is $0.25\\text{ mM} = 2.5 \\times 10^{-4}\\text{ M}$. Calculating $Q_{sp}$: $Q_{sp} = [\\text{Ca}^{2+}][\\text{C}_2\\text{O}_4^{2-}] = (1.10 \\times 10^{-3}\\text{ M}) \\times (2.5 \\times 10^{-4}\\text{ M}) = 2.75 \\times 10^{-7} \\approx 2.8 \\times 10^{-7}$. Because $Q_{sp} (2.8 \\times 10^{-7}) > K_{sp} (2.3 \\times 10^{-9})$, the solution is heavily supersaturated ($SS \\approx 120$), explaining the observed rapid crystallization.<br><br><em>Distractor Traps:</em><br>&bull; A ($5.5 \\times 10^{-11}$) uses nanomolar exponents erroneously.<br>&bull; C ($3.8 \\times 10^{-4}$) uses total concentrations without converting millimolar to molar ($1.5 \\times 0.25$).<br>&bull; D ($1.1 \\times 10^{-3}$) simply reads the calcium molarity."
    },
    {
        "q": "Administration of potassium citrate suppresses calcium oxalate nephrolithiasis primarily because citrate:",
        "ch": [
            "increases urinary ionic strength, thereby accelerating the precipitation of sodium oxalate.",
            "acts as a Lewis acid to protonate oxalate into volatile carbon dioxide gas.",
            "chelates free Ca^2+ ions, reducing the ion product below the solubility product threshold.",
            "directly oxidizes oxalate into non-crystallizing carbonate and bicarbonate ions."
        ],
        "a": 2,
        "e": "<strong>Mechanism of citrate inhibition:</strong> As shown in the passage, citrate has a high formation constant ($K_f = 2.0 \\times 10^3$) with calcium, forming a highly soluble $[\\text{Ca-Citrate}]^-$ complex. By sequestering free calcium ions, citrate drastically decreases $[\\text{Ca}^{2+}]$, driving $Q_{sp} = [\\text{Ca}^{2+}][\\text{C}_2\\text{O}_4^{2-}]$ below $K_{sp}$, thereby inhibiting both spontaneous nucleation and aggregate crystal growth.<br><br><em>Distractor Traps:</em><br>&bull; A states the opposite of the clinical therapeutic goal.<br>&bull; B asserts that citrate is a Lewis acid that volatilizes oxalate, which is chemically false (citrate is a Lewis base).<br>&bull; D invents an oxidative degradation pathway that does not occur in urine."
    },
    {
        "q": "If sodium oxalate (Na_2C_2O_4) is added to a saturated aqueous solution of calcium oxalate at equilibrium, what immediate effect will be observed?",
        "ch": [
            "The solubility of calcium oxalate will increase due to the salting-in ionic effect.",
            "Additional calcium oxalate precipitate will form as calcium ion concentration decreases.",
            "The solubility product constant K_sp will decrease to compensate for added oxalate.",
            "The solution will become unsaturated due to the formation of soluble NaCa complexes."
        ],
        "a": 1,
        "e": "<strong>Common-ion effect:</strong> Adding $\\text{Na}_2\\text{C}_2\\text{O}_4$ introduces additional oxalate ions ($\\text{C}_2\\text{O}_4^{2-}$), a common ion in the equilibrium $\\text{CaC}_2\\text{O}_4(s) \\rightleftharpoons \\text{Ca}^{2+}(aq) + \\text{C}_2\\text{O}_4^{2-}(aq)$. According to Le Ch&acirc;telier's principle, increasing $[\\text{C}_2\\text{O}_4^{2-}]$ shifts the equilibrium to the left, inducing additional $\\text{CaC}_2\\text{O}_4(s)$ precipitation and reducing the concentration of dissolved $[\\text{Ca}^{2+}]$. The solubility product constant $K_{sp}$ is an equilibrium constant and depends only on temperature, so it remains unchanged.<br><br><em>Distractor Traps:</em><br>&bull; A misapplies the secondary ionic strength effect (the dominant effect is the common-ion precipitating effect).<br>&bull; C incorrectly claims that $K_{sp}$ changes (equilibrium constants are temperature-dependent, not concentration-dependent).<br>&bull; D falsely claims the solution becomes unsaturated."
    },
    {
        "q": "Comparing the solubility products of calcium oxalate (K_sp = 2.3 x 10^-9) and calcium sulfate (K_sp = 2.4 x 10^-5) in pure water at 310 K indicates that:",
        "ch": [
            "calcium sulfate requires a lower free calcium concentration to initiate precipitation.",
            "calcium oxalate is approximately 100 times less soluble on a molar basis than calcium sulfate.",
            "calcium oxalate and calcium sulfate possess identical molar solubilities at equilibrium.",
            "calcium sulfate forms an insoluble precipitate more readily than calcium oxalate."
        ],
        "a": 1,
        "e": "<strong>Comparing molar solubilities of 1:1 salts:</strong> Both $\\text{CaC}_2\\text{O}_4$ and $\\text{CaSO}_4$ are 1:1 electrolytes ($AB \\rightleftharpoons A + B$), so their molar solubilities are given by $s = \\sqrt{K_{sp}}$. For $\\text{CaOx}$, $s = \\sqrt{2.3 \\times 10^{-9}} \\approx 4.8 \\times 10^{-5}\\text{ M}$. For $\\text{CaSO}_4$, $s = \\sqrt{2.4 \\times 10^{-5}} \\approx 4.9 \\times 10^{-3}\\text{ M}$. The ratio of their solubilities is $(4.9 \\times 10^{-3}) / (4.8 \\times 10^{-5}) \\approx 102$. Thus, calcium oxalate is approximately 100 times less soluble on a molar basis than calcium sulfate.<br><br><em>Distractor Traps:</em><br>&bull; A and D assert the reverse: calcium oxalate has a much smaller $K_{sp}$, so it precipitates at far lower ion concentrations.<br>&bull; C ignores the four-order-of-magnitude difference in $K_{sp}$."
    },
    {
        "q": "Which molecular property of the oxalate dianion (C_2O_4^2-) makes it an effective bidentate chelating ligand for divalent transition metals and alkaline earth cations?",
        "ch": [
            "The presence of two lone pairs on a single central carbon atom forming a coordination bond.",
            "The availability of unshared electron pairs on two separate oxygen atoms forming a five-membered ring.",
            "The linear geometry of the central carbon-carbon single bond preventing ring closure.",
            "The complete absence of resonance delocalization across the four terminal oxygen atoms."
        ],
        "a": 1,
        "e": "<strong>Chelation chemistry of oxalate:</strong> The oxalate dianion ($^-\\text{O}-\\text{C}(=\\text{O})-\\text{C}(=\\text{O})-\\text{O}^-$) possesses lone pairs on two separate carboxylate oxygen atoms that can simultaneously donate electron pairs to a single central metal cation (such as $\\text{Ca}^{2+}$). This bidentate coordination forms a stable, low-strain five-membered chelate ring ($\\text{M-O-C-C-O}$), providing thermodynamic stability via the chelate effect.<br><br><em>Distractor Traps:</em><br>&bull; A describes carbene chemistry; carbons in oxalate have no lone pairs.<br>&bull; C is geometrically inaccurate; oxalate easily adopts a coplanar conformation to chelate.<br>&bull; D is chemically incorrect: oxalate has extensive resonance delocalization over all four oxygen atoms."
    }
]

passages.append({
    "id": "exam_cp90_2_p3",
    "sec": "C/P",
    "topic": "Solubility Equilibria & Calcium Oxalate Nephrolithiasis",
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_2",
    "passage": p3_html,
    "qs": p3_qs
})

print("Passage 3 defined.")

# ==============================================================================
# PASSAGE 4: Fluid Mechanics, Bernoulli Principle & Venturi Flow Dynamics
# Topics: Bernoulli equation, Venturi effect, dynamic vs static pressure, Poiseuille flow, oxygen masks
# ==============================================================================
p4_html = """<div class="ttl">Passage 4 (Questions 19&ndash;24)</div>
<p>The fluid dynamics of the human respiratory and circulatory systems can be modeled using the continuity equation and the Bernoulli principle for idealized, incompressible, laminar flow. According to the continuity equation, the volumetric flow rate ($Q = A \\cdot v$) must remain constant along a closed streamline conduit of varying cross-sectional area:</p>
<p>$$A_1 v_1 = A_2 v_2$$</p>
<p>Bernoulli's equation expresses the conservation of mechanical energy per unit volume for an inviscid fluid of density $\\rho$:</p>
<p>$$P_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g y_1 = P_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g y_2$$</p>
<p>where $P$ is the static pressure, $\\frac{1}{2}\\rho v^2$ is the dynamic pressure, and $\\rho g y$ is the gravitational potential energy density. In a horizontal tube ($y_1 = y_2$), a constriction in the conduit cross-section ($A_2 < A_1$) accelerates fluid velocity ($v_2 > v_1$), resulting in an increase in dynamic pressure and a concomitant reduction in static pressure ($P_2 < P_1$). This phenomenon, known as the <i>Venturi effect</i>, is operationalized in clinical entrainment devices (such as Venturi oxygen masks and medical nebulizers) where low static pressure at a constriction draws ambient air or liquid medication into a high-velocity oxygen jet.</p>
<p>Biomedical engineers tested an entrainment oxygen delivery mask across five constriction diameters ($d_2$) using pure medical oxygen ($\\rho_{O2} = 1.30\\text{ kg/m}^3$) fed through a main supply tube of diameter $d_1 = 12.0\\text{ mm}$ at a baseline supply flow rate of $Q = 6.0\\text{ L/min}$ ($1.0 \\times 10^{-4}\\text{ m}^3\\text{/s}$). The static pressure difference ($\\Delta P = P_1 - P_2$) between the main tube and the throat constriction was measured using a differential manometer filled with fluid ($\\rho_m = 1000\\text{ kg/m}^3$). The findings are summarized in Table 1.</p>
<table class="tbl">
  <caption>Table 1 Fluid dynamic parameters and manometer deflections across throat constrictions</caption>
  <thead>
    <tr><th>Design Variant</th><th>Throat Diameter $d_2$ (mm)</th><th>Area Ratio ($A_1 / A_2$)</th><th>Throat Velocity $v_2$ (m/s)</th><th>Measured $\\Delta P$ ($P_1 - P_2$) (Pa)</th><th>Air Entrainment Ratio ($Q_{air} / Q_{O2}$)</th></tr>
  </thead>
  <tbody>
    <tr><td>Device A</td><td>12.0 (No constriction)</td><td>1.0</td><td>0.88</td><td>0</td><td>0.0 : 1</td></tr>
    <tr><td>Device B</td><td>6.0</td><td>4.0</td><td>3.54</td><td>8.1</td><td>1.2 : 1</td></tr>
    <tr><td>Device C</td><td>4.0</td><td>9.0</td><td>7.96</td><td>41.2</td><td>3.1 : 1</td></tr>
    <tr><td>Device D</td><td>3.0</td><td>16.0</td><td>14.15</td><td>130.1</td><td>5.0 : 1</td></tr>
    <tr><td>Device E</td><td>2.0</td><td>36.0</td><td>31.83</td><td>658.8</td><td>9.4 : 1</td></tr>
  </tbody>
</table>
<p>In real clinical conduits, fluid viscosity ($\\eta$) introduces frictional dissipation. Poiseuille's law governs the viscous pressure drop ($\\Delta P_{visc} = \\frac{8\\eta L Q}{\\pi r^4}$) along uniform cylindrical vessels under laminar conditions.</p>"""

p4_qs = [
    {
        "q": "When oxygen flows from the main supply tube into the narrowed throat of Device D, how do the fluid velocity and static pressure change?",
        "ch": [
            "Velocity decreases, and static pressure increases.",
            "Velocity decreases, and static pressure decreases.",
            "Velocity increases, and static pressure increases.",
            "Velocity increases, and static pressure decreases."
        ],
        "a": 3,
        "e": "<strong>Continuity and Bernoulli dynamics:</strong> By the continuity equation ($A_1 v_1 = A_2 v_2$), when the cross-sectional area decreases in the throat ($A_2 < A_1$), fluid velocity must increase ($v_2 > v_1$). By Bernoulli's equation for horizontal flow ($P + \\frac{1}{2}\\rho v^2 = \\text{constant}$), an increase in fluid velocity elevates dynamic pressure ($\\frac{1}{2}\\rho v^2$), which strictly forces static pressure ($P$) to decrease to conserve total mechanical energy per unit volume.<br><br><em>Distractor Traps:</em><br>&bull; A claims velocity decreases (contradicting continuity).<br>&bull; B and C misunderstand the inverse trade-off between dynamic and static pressure."
    },
    {
        "q": "Device D has a throat diameter of 3.0 mm compared to the main supply tube diameter of 12.0 mm. By what factor is the cross-sectional area of the main tube larger than that of the throat?",
        "ch": [
            "4",
            "8",
            "16",
            "32"
        ],
        "a": 2,
        "e": "<strong>Cross-sectional area ratio:</strong> The cross-sectional area of a cylindrical tube is $A = \\pi r^2 = \\pi (d/2)^2$. The ratio of the areas is $(d_1 / d_2)^2 = (12.0\\text{ mm} / 3.0\\text{ mm})^2 = 4^2 = 16$. Thus, the main tube cross-sectional area is exactly 16 times larger than that of the constriction throat, as verified directly in Table 1.<br><br><em>Distractor Traps:</em><br>&bull; A (4) uses the linear diameter ratio $d_1/d_2 = 12/3 = 4$, forgetting to square the radius.<br>&bull; B (8) mistakenly cubes the radius or multiplies by 2.<br>&bull; D (32) doubles 16."
    },
    {
        "q": "Based on Poiseuille's law, if the internal radius of an airway is reduced by 50% due to acute bronchoconstriction while maintaining a constant volumetric flow rate, the viscous resistance to airflow will increase by a factor of:",
        "ch": [
            "2",
            "4",
            "8",
            "16"
        ],
        "a": 3,
        "e": "<strong>Poiseuille resistance and radius:</strong> According to Poiseuille's law, vascular and airway resistance is given by $R = \\frac{8\\eta L}{\\pi r^4}$. Therefore, resistance is inversely proportional to the fourth power of the radius ($R \\propto 1/r^4$). If the radius is halved ($r' = 0.5 r = r/2$), the new resistance is $R' \\propto 1/(r/2)^4 = 1/(r^4 / 16) = 16 / r^4 = 16 R$. Resistance increases by a factor of $2^4 = 16$.<br><br><em>Distractor Traps:</em><br>&bull; A (2) assumes an inverse linear relationship ($1/r$).<br>&bull; B (4) assumes an inverse square relationship ($1/r^2$).<br>&bull; C (8) assumes an inverse cube relationship ($1/r^3$)."
    },
    {
        "q": "In a Venturi mask using Device E, what is the primary physical driving force that entrains room air into the oxygen flow?",
        "ch": [
            "The ambient atmospheric pressure exceeds the reduced static pressure inside the throat constriction.",
            "The dynamic pressure of ambient air is greater than the total pressure inside the main supply tube.",
            "The high temperature of pure oxygen generates an upward thermal convection current.",
            "The electrostatic charge on oxygen molecules attracts neutral atmospheric nitrogen molecules."
        ],
        "a": 0,
        "e": "<strong>Physical mechanism of Venturi entrainment:</strong> In Device E, the rapid flow through the constriction lowers the static pressure inside the throat ($P_2$) well below ambient atmospheric pressure ($P_{atm}$). Entrainment ports are open to the room; because $P_{atm} > P_2$, a favorable pressure gradient ($\\Delta P = P_{atm} - P_2$) drives room air inward into the jet stream, mixing with pure oxygen to achieve a precise fraction of inspired oxygen ($\\text{FiO}_2$).<br><br><em>Distractor Traps:</em><br>&bull; B misapplies dynamic pressure to stationary room air (where $v = 0$, so dynamic pressure is zero).<br>&bull; C invents a thermal convection mechanism.<br>&bull; D invents electrostatic attraction."
    },
    {
        "q": "If the differential manometer fluid has density rho_m = 1000 kg/m^3 and g = 9.8 m/s^2, what manometer height difference (Delta h) corresponds to the pressure drop measured in Device E (Delta P = 658.8 Pa)?",
        "ch": [
            "0.67 cm",
            "6.72 cm",
            "67.2 cm",
            "672 cm"
        ],
        "a": 1,
        "e": "<strong>Hydrostatic pressure and manometer deflection:</strong> Hydrostatic pressure is given by $\\Delta P = \\rho_m g \\Delta h$. Solving for the height difference: $\\Delta h = \\frac{\\Delta P}{\\rho_m g} = \\frac{658.8\\text{ Pa}}{(1000\\text{ kg/m}^3)(9.8\\text{ m/s}^2)} = \\frac{658.8}{9800} = 0.0672\\text{ m} = 6.72\\text{ cm}$.<br><br><em>Distractor Traps:</em><br>&bull; A ($0.67\\text{ cm}$) is off by a factor of 10.<br>&bull; C ($67.2\\text{ cm}$) forgets to divide by the density of water.<br>&bull; D ($672\\text{ cm}$) miscalculates unit conversion by two orders of magnitude."
    },
    {
        "q": "Which assumption is NOT required when deriving Bernoulli's equation from the work-energy theorem?",
        "ch": [
            "The fluid must be incompressible with constant density throughout flow.",
            "The flow must be laminar and follow non-intersecting streamlines.",
            "The fluid must be completely free of viscous shear dissipation.",
            "The cross-sectional area of the conduit must remain strictly uniform."
        ],
        "a": 3,
        "e": "<strong>Assumptions of Bernoulli's principle:</strong> Bernoulli's equation applies to ideal fluids, requiring: (1) incompressible fluid (constant $\\rho$), (2) non-viscous/inviscid fluid (zero shear stress/internal friction), (3) laminar/streamline steady flow, and (4) irrotational flow. Crucially, the cross-sectional area of the conduit does NOT have to remain uniform; in fact, the entire utility of Bernoulli's equation (such as in Venturi tubes and flight airfoils) lies in analyzing flow through conduits of <i>varying</i> cross-sectional area and elevation.<br><br><em>Distractor Traps:</em><br>&bull; A, B, and C are all mandatory assumptions for the classical Bernoulli equation."
    }
]

passages.append({
    "id": "exam_cp90_2_p4",
    "sec": "C/P",
    "topic": "Fluid Mechanics, Bernoulli Principle & Venturi Flow Dynamics",
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_2",
    "passage": p4_html,
    "qs": p4_qs
})

print("Passage 4 defined.")

# ==============================================================================
# PASSAGE 5: Ultrasound Physics, Acoustic Impedance & Doppler Echocardiography
# Topics: Acoustic impedance Z = rho*v, reflection coefficient R, Doppler frequency shift, attenuation
# ==============================================================================
p5_html = """<div class="ttl">Passage 5 (Questions 25&ndash;30)</div>
<p>Medical ultrasound diagnostics utilize high-frequency acoustic waves ($f_0 = 2\\text{ to } 15\\text{ MHz}$) transmitted by piezoelectric ceramic crystals into biological tissues. As longitudinal pressure waves propagate through anatomical structures, acoustic energy is partially reflected at interfaces separating media of differing characteristic acoustic impedance ($Z$). Acoustic impedance quantifies a medium's resistance to acoustic particle displacement and is defined as the product of tissue density ($\\rho$) and acoustic propagation velocity ($v$):</p>
<p>$$Z = \\rho \\cdot v$$</p>
<p>For a wave striking a planar tissue boundary at normal incidence, the intensity reflection coefficient ($R$) defines the fraction of incident acoustic intensity ($I_0$) reflected back to the transducer:</p>
<p>$$R = \\frac{I_r}{I_0} = \\left( \\frac{Z_2 - Z_1}{Z_2 + Z_1} \\right)^2$$</p>
<p>The intensity transmission coefficient ($T$) satisfies conservation of energy: $T = 1 - R$. When imaging moving erythrocyte columns in cardiovascular echocardiography, the reflected acoustic wave exhibits a Doppler frequency shift ($\\Delta f = f_r - f_0$) proportional to the velocity of blood flow ($v_b$):</p>
<p>$$\\Delta f = \\frac{2 f_0 v_b \\cos\\theta}{c}$$</p>
<p>where $c$ is the speed of sound in soft tissue ($1540\\text{ m/s}$), and $\\theta$ is the Doppler angle of insonation between the ultrasound beam and the vector of erythrocyte motion. Table 1 lists physical properties of various anatomical media measured at 310 K.</p>
<table class="tbl">
  <caption>Table 1 Density, acoustic velocity, and impedance across biological media</caption>
  <thead>
    <tr><th>Medium</th><th>Density $\\rho$ (kg/m$^3$)</th><th>Speed of Sound $v$ (m/s)</th><th>Acoustic Impedance $Z$ ($\\times 10^6 \\text{ kg}/(\\text{m}^2\\cdot\\text{s})$)</th><th>Attenuation Coefficient at 5 MHz (dB/cm)</th></tr>
  </thead>
  <tbody>
    <tr><td>Air</td><td>1.2</td><td>343</td><td>0.00041</td><td>60.0</td></tr>
    <tr><td>Blood</td><td>1060</td><td>1570</td><td>1.66</td><td>0.9</td></tr>
    <tr><td>Soft Tissue (Muscle)</td><td>1070</td><td>1580</td><td>1.69</td><td>2.5</td></tr>
    <tr><td>Fat</td><td>920</td><td>1450</td><td>1.33</td><td>3.0</td></tr>
    <tr><td>Cortical Bone</td><td>1900</td><td>4080</td><td>7.75</td><td>25.0</td></tr>
    <tr><td>Ultrasound Acoustic Gel</td><td>1030</td><td>1540</td><td>1.59</td><td>0.8</td></tr>
  </tbody>
</table>
<p>In a clinical trial evaluating aortic valve stenosis, a sonographer aimed a 3.0 MHz ultrasound beam at a patient's ascending aorta at an insonation angle of $\\theta = 0^\\circ$ ($\\cos 0^\\circ = 1.0$), recording a Doppler shift of $\\Delta f = +7.80\\text{ kHz}$.</p>"""

p5_qs = [
    {
        "q": "Why is an acoustic coupling gel applied to a patient's skin prior to an ultrasound examination?",
        "ch": [
            "Gel lowers the frequency of transmitted acoustic waves into the audible human range.",
            "Gel eliminates air pockets that would otherwise reflect over 99% of acoustic wave energy.",
            "Gel ionizes skin surface lipids to conduct electromagnetic radio waves into tissues.",
            "Gel selectively absorbs bone reflections to prevent shadow artifact generation."
        ],
        "a": 1,
        "e": "<strong>Acoustic impedance matching at air-tissue interface:</strong> According to Table 1, the acoustic impedance of air is $Z_{air} = 0.00041 \\times 10^6$, whereas soft tissue is $Z_{tissue} \\approx 1.69 \\times 10^6$. The reflection coefficient at an air-tissue boundary is $R = ((1.69 - 0.00041)/(1.69 + 0.00041))^2 \\approx (1.0)^2 = 1.0$ (99.9% reflected). Acoustic coupling gel has an impedance ($1.59 \\times 10^6$) closely matching soft tissue, eliminating air pockets and allowing acoustic energy to transmit into the body.<br><br><em>Distractor Traps:</em><br>&bull; A is false: ultrasound relies on frequencies > 2 MHz; lowering to audible range (< 20 kHz) would destroy resolution.<br>&bull; C confuses mechanical sound waves with electromagnetic radiation.<br>&bull; D invents a selective absorption property that gel does not possess."
    },
    {
        "q": "Based on the equation in the passage, what blood flow velocity vb corresponds to the measured Doppler shift of Delta f = +7.80 kHz at f_0 = 3.0 MHz and theta = 0 degrees (c = 1540 m/s)?",
        "ch": [
            "0.50 m/s",
            "1.00 m/s",
            "2.00 m/s",
            "4.00 m/s"
        ],
        "a": 2,
        "e": "<strong>Doppler blood velocity calculation:</strong> The Doppler shift equation is $\\Delta f = \\frac{2 f_0 v_b \\cos\\theta}{c}$. Rearranging for $v_b$: $v_b = \\frac{\\Delta f \\cdot c}{2 f_0 \\cos\\theta}$. Substituting the given values: $v_b = \\frac{(7.80 \\times 10^3\\text{ Hz})(1540\\text{ m/s})}{2 (3.0 \\times 10^6\\text{ Hz})(1.0)} = \\frac{1.2012 \\times 10^7}{6.0 \\times 10^6} = 2.002\\text{ m/s} \\approx 2.00\\text{ m/s}$. Velocities above $2.0\\text{ m/s}$ in the aorta are characteristic of aortic valve stenosis.<br><br><em>Distractor Traps:</em><br>&bull; A (0.50 m/s) multiplies by 4 instead of dividing.<br>&bull; B (1.00 m/s) forgets the factor of 2 in the denominator (which accounts for round-trip Doppler shift).<br>&bull; D (4.00 m/s) forgets to divide by 2."
    },
    {
        "q": "What is the intensity reflection coefficient (R) at a perpendicular interface between fat (Z_1 = 1.33 x 10^6) and muscle tissue (Z_2 = 1.69 x 10^6)?",
        "ch": [
            "0.014",
            "0.119",
            "0.881",
            "0.986"
        ],
        "a": 0,
        "e": "<strong>Intensity reflection coefficient calculation:</strong> Using the formula $R = \\left( \\frac{Z_2 - Z_1}{Z_2 + Z_1} \\right)^2$: $\\frac{Z_2 - Z_1}{Z_2 + Z_1} = \\frac{1.69 - 1.33}{1.69 + 1.33} = \\frac{0.36}{3.02} \\approx 0.1192$. Squaring this value: $R = (0.1192)^2 \\approx 0.0142$ (or 1.4%). Thus, 1.4% of incident ultrasound energy is reflected at the fat-muscle interface, while the remaining 98.6% is transmitted ($T = 1 - R = 0.986$).<br><br><em>Distractor Traps:</em><br>&bull; B (0.119) forgets to square the amplitude reflection ratio $(Z_2 - Z_1)/(Z_2 + Z_1)$.<br>&bull; C (0.881) subtracts 0.119 from 1.<br>&bull; D (0.986) is the intensity transmission coefficient $T$, not the reflection coefficient $R$."
    },
    {
        "q": "If an echocardiographer increases the insonation angle theta from 0 degrees to 60 degrees while blood velocity remains constant, the measured Doppler frequency shift will:",
        "ch": [
            "decrease by 50% because the cosine of 60 degrees equals 0.50.",
            "increase by 73% because the tangent of 60 degrees exceeds unity.",
            "remain unchanged because Doppler shifts depend solely on blood velocity.",
            "drop to zero because ultrasound waves cannot penetrate at oblique angles."
        ],
        "a": 0,
        "e": "<strong>Angular dependence of Doppler shift:</strong> The Doppler equation explicitly incorporates $\\cos\\theta$: $\\Delta f \\propto \\cos\\theta$. At $\\theta = 0^\\circ$, $\\cos 0^\\circ = 1.00$. At $\\theta = 60^\\circ$, $\\cos 60^\\circ = 0.50$. Therefore, shifting the insonation angle from $0^\\circ$ to $60^\\circ$ reduces $\\Delta f$ by exactly $50\\%$. (This is why sonographers align the ultrasound beam as parallel to blood flow as possible; at $\\theta = 90^\\circ$, $\\cos 90^\\circ = 0$, detecting zero shift).<br><br><em>Distractor Traps:</em><br>&bull; B misapplies trigonometric tangent.<br>&bull; C ignores the angular vector projection in the Doppler equation.<br>&bull; D falsely claims sound cannot penetrate obliquely (sound penetrates, but Doppler shift drops to zero only at $90^\\circ$)."
    },
    {
        "q": "As an ultrasound beam travels through soft tissue, higher frequency waves (e.g., 12 MHz vs 3 MHz) provide:",
        "ch": [
            "deeper tissue penetration with reduced spatial image resolution.",
            "superior spatial resolution with greater attenuation and shallower depth.",
            "faster wave propagation speeds through identical soft tissue structures.",
            "decreased acoustic impedance at tissue boundaries due to shorter wavelengths."
        ],
        "a": 1,
        "e": "<strong>Trade-off between spatial resolution and depth:</strong> Spatial resolution improves with shorter wavelengths ($\\lambda = v / f$). High-frequency ultrasound (12 MHz) has shorter wavelengths, allowing finer discrimination of small structural details. However, acoustic attenuation in tissue increases proportionally with frequency (measured in dB/cm), meaning high-frequency sound waves are rapidly absorbed and scattered, limiting their practical penetration to superficial structures (e.g., thyroid, carotid artery). Low frequencies (3 MHz) penetrate deeper into abdominal organs.<br><br><em>Distractor Traps:</em><br>&bull; A states the opposite trade-off.<br>&bull; C is false: wave speed ($v$) in a medium is determined entirely by the bulk modulus and density of the medium ($v = \\sqrt{B/\\rho}$), NOT by wave frequency.<br>&bull; D is incorrect: acoustic impedance $Z = \\rho v$ is an intrinsic medium property independent of frequency."
    },
    {
        "q": "Piezoelectric ultrasound transducers convert electrical oscillations into mechanical sound waves via:",
        "ch": [
            "dimensional expansion and contraction of crystal lattices under alternating electric fields.",
            "photoelectric ejection of outer shell electrons from quartz crystal surfaces.",
            "thermodynamic boiling and rapid condensation of water molecules in the transducer head.",
            "spontaneous nuclear alpha decay generating local compression shockwaves."
        ],
        "a": 0,
        "e": "<strong>Piezoelectric effect:</strong> The piezoelectric effect is the coupling between electrical and mechanical states in non-centrosymmetric crystals (such as lead zirconate titanate, PZT). Applying an alternating electrical potential across the crystal forces dipoles to align, inducing rhythmic physical expansion and contraction (mechanical vibration) that launches longitudinal ultrasound pressure waves into adjacent media.<br><br><em>Distractor Traps:</em><br>&bull; B describes the photoelectric effect.<br>&bull; C describes thermal cavitational boiling.<br>&bull; D describes nuclear radioactive decay."
    }
]

passages.append({
    "id": "exam_cp90_2_p5",
    "sec": "C/P",
    "topic": "Ultrasound Physics, Acoustic Impedance & Doppler Echocardiography",
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_2",
    "passage": p5_html,
    "qs": p5_qs
})

print("Passage 5 defined.")

# ==============================================================================
# PASSAGE 6: Carbonyl Chemistry, Directed Aldol & Glycolytic Retro-Aldol Cleavage
# Topics: Aldol condensation, retro-aldol mechanism, enolate intermediates, aldolase, Schiff base
# ==============================================================================
p6_html = """<div class="ttl">Passage 6 (Questions 31&ndash;36)</div>
<p>The carbon-carbon bond forming and cleaving reactions of carbonyl compounds are central to organic synthesis and cellular metabolism. In a classical base-catalyzed aldol addition, a strong base deprotonates an $\\alpha$-carbon adjacent to a carbonyl group to generate a resonance-stabilized enolate nucleophile. This enolate attacks the electrophilic carbonyl carbon of an aldehyde or ketone to yield a $\\beta$-hydroxy carbonyl adduct. Subsequent acid- or base-catalyzed dehydration through an elimination pathway ($E1cB$) yields an $\\alpha,\\beta$-unsaturated carbonyl compound (aldol condensation).</p>
<p>In glycolysis, the fourth step is a biological <i>retro-aldol cleavage</i> catalyzed by the enzyme fructose-1,6-bisphosphate aldolase. Class I aldolases (found in mammals) utilize an active-site lysine residue ($\\text{Lys229}$) to form a covalent, protonated Schiff base (imine/iminium ion) intermediate with the C2 carbonyl of D-fructose-1,6-bisphosphate ($\\text{F-1,6-BP}$). The iminium ion acts as an electron sink, stabilizing the developing negative charge during the cleavage of the C3&ndash;C4 single bond. This reaction yields two triose phosphate isomers: dihydroxyacetone phosphate ($\\text{DHAP}$) and D-glyceraldehyde-3-phosphate ($\\text{G3P}$), as shown in Figure 1.</p>
<div style="text-align:center;margin:14px 0;padding:12px;background:#F9FAFB;border:1px solid #E5E7EB;font-family:monospace;font-size:13px;line-height:1.6">
  [F-1,6-BP] + Lys-NH<sub>2</sub> &rarr; [Protonated Schiff Base at C2] &rarr; C3&ndash;C4 Cleavage &rarr; Enamine-DHAP + G3P<br>
  Enamine-DHAP + H<sub>2</sub>O &rarr; Free DHAP + Regenerated Lys-NH<sub>2</sub>
</div>
<p>Synthetic chemists investigated the retro-aldol cleavage of four synthetic $\\beta$-hydroxy ketones (Compounds 1&ndash;4) using catalytic base or secondary amine catalysts that mimic the Class I aldolase mechanism. Table 1 lists the structural parameters and observed pseudo-first-order rate constants ($k_{obs}$) at 298 K.</p>
<table class="tbl">
  <caption>Table 1 Retro-aldol cleavage kinetics of synthetic &beta;-hydroxy ketones</caption>
  <thead>
    <tr><th>Substrate</th><th>Carbonyl Substituent (R1)</th><th>&beta;-Carbon Substituents (R2, R3)</th><th>Catalyst System</th><th>$k_{obs}$ ($\\times 10^{-3} \\text{ s}^{-1}$)</th><th>Major Cleavage Products</th></tr>
  </thead>
  <tbody>
    <tr><td>Compound 1</td><td>Methyl ($- \\text{CH}_3$)</td><td>$- \\text{H}$, $- \\text{H}$</td><td>0.1 M NaOH</td><td>1.2</td><td>Acetone + Formaldehyde</td></tr>
    <tr><td>Compound 2</td><td>Methyl ($- \\text{CH}_3$)</td><td>$- \\text{CH}_3$, $- \\text{CH}_3$</td><td>0.1 M NaOH</td><td>18.5</td><td>Acetone + Acetone</td></tr>
    <tr><td>Compound 3</td><td>Phenyl ($- \\text{C}_6\\text{H}_5$)</td><td>$- \\text{CH}_3$, $- \\text{CH}_3$</td><td>0.1 M NaOH</td><td>94.0</td><td>Acetophenone + Acetone</td></tr>
    <tr><td>Compound 4</td><td>Phenyl ($- \\text{C}_6\\text{H}_5$)</td><td>$- \\text{CH}_3$, $- \\text{CH}_3$</td><td>0.05 M Proline (Amine)</td><td>420.0</td><td>Acetophenone + Acetone</td></tr>
  </tbody>
</table>
<p>To confirm the formation of the Schiff base intermediate in Class I aldolase, researchers treated the enzyme-substrate complex with sodium borohydride ($\\text{NaBH}_4$), resulting in irreversible enzyme inactivation.</p>"""

p6_qs = [
    {
        "q": "Why does sodium borohydride (NaBH_4) treatment irreversibly inactivate Class I aldolase in the presence of its substrate F-1,6-BP?",
        "ch": [
            "It selectively reduces active-site disulfide bridges into free cysteine thiols.",
            "It reduces the covalent iminium intermediate into a stable secondary amine adduct.",
            "It oxidizes the catalytic lysine residue into an electrophilic alpha-amino aldehyde.",
            "It precipitates all quaternary protein subunits through non-specific ionic denaturation."
        ],
        "a": 1,
        "e": "<strong>Schiff base chemical trapping:</strong> In Class I aldolases, the active-site Lys forms a reversible protonated imine (Schiff base, $\\text{R}_2\\text{C}=\\text{N}^+\\text{HR}'$) with the substrate. Sodium borohydride ($\\text{NaBH}_4$) is a reducing agent that reduces imines/iminium ions to stable secondary amines ($\\text{R}_2\\text{CH}-\\text{NHR}'$). Unlike imines, secondary amines cannot undergo spontaneous hydrolysis back to free amine and carbonyl. This permanently covalently locks the substrate to Lys229, irreversibly inactivating the enzyme (a classic biochemical diagnostic for Class I aldolases).<br><br><em>Distractor Traps:</em><br>&bull; A confuses borohydride with dithiothreitol (DTT) or $\\beta$-mercaptoethanol.<br>&bull; C calls $\\text{NaBH}_4$ an oxidizing agent (it is a reducing agent).<br>&bull; D invents non-specific bulk precipitation."
    },
    {
        "q": "Comparing Compounds 2 and 3 in Table 1, why does substituting a phenyl ring for a methyl group at R1 increase the rate of retro-aldol cleavage by over five-fold?",
        "ch": [
            "The phenyl ring sterically hinders nucleophilic attack by incoming hydroxide ions.",
            "The phenyl ring stabilizes the enolate leaving group through extended pi-resonance delocalization.",
            "The phenyl ring increases the electrophilicity of the beta-carbon through hyperconjugation.",
            "The phenyl ring undergoes spontaneous electrophilic aromatic substitution with solvent."
        ],
        "a": 1,
        "e": "<strong>Enolate leaving group stabilization:</strong> In the base-catalyzed retro-aldol mechanism, hydroxide deprotonates the $\\beta$-hydroxyl group, forming an alkoxide. The alkoxide collapses to expel an enolate leaving group as the C&ndash;C bond cleaves. In Compound 2, the leaving group is the acetone enolate ($^-\\text{CH}_2-\\text{C}(=\\text{O})-\\text{CH}_3$). In Compound 3, the leaving group is the acetophenone enolate ($^-\\text{CH}_2-\\text{C}(=\\text{O})-\\text{C}_6\\text{H}_5$). The aromatic $\\pi$-system of the phenyl ring provides extensive resonance stabilization for the developing negative charge on the enolate, making it a substantially better leaving group and accelerating the rate ($k_{obs}$ increases from $18.5$ to $94.0$).<br><br><em>Distractor Traps:</em><br>&bull; A states steric hindrance (which would slow down, not accelerate, the reaction).<br>&bull; C describes $\\beta$-carbon changes, whereas the substitution was at $R1$ ($\\alpha$/carbonyl side).<br>&bull; D invents aromatic substitution irrelevant to retro-aldol cleavage."
    },
    {
        "q": "What type of reaction converts an aldol addition product (a beta-hydroxy ketone) into an aldol condensation product (an alpha,beta-unsaturated ketone)?",
        "ch": [
            "Hydrolysis",
            "Dehydration",
            "Transesterification",
            "Decarboxylation"
        ],
        "a": 1,
        "e": "<strong>Aldol addition vs condensation:</strong> The aldol addition product is a $\\beta$-hydroxy carbonyl compound. When heated in acid or base, it loses a molecule of water ($\\text{H}_2\\text{O}$)&mdash;a proton from the $\\alpha$-carbon and an $-\\text{OH}$ group from the $\\beta$-carbon&mdash;to form a conjugated $\\alpha,\\beta$-unsaturated carbonyl compound. This elimination of water is formally a <i>dehydration</i> reaction.<br><br><em>Distractor Traps:</em><br>&bull; A (Hydrolysis) adds water rather than removing it.<br>&bull; C (Transesterification) is the alcohol exchange of esters.<br>&bull; D (Decarboxylation) is the loss of carbon dioxide ($\\text{CO}_2$)."
    },
    {
        "q": "Why does proline (an amine catalyst) accelerate the retro-aldol cleavage of Compound 4 to 420.0 x 10^-3 s^-1 compared to NaOH catalysis (94.0 x 10^-3 s^-1)?",
        "ch": [
            "Proline acts as an organocatalyst by forming a positively charged iminium ion electron sink.",
            "Proline completely deprotonates the solvent to generate high local concentrations of oxide dianions.",
            "Proline irreversibly acylates the beta-carbon, locking the substrate into an open-chain enol.",
            "Proline functions as a non-nucleophilic phase-transfer catalyst that aggregates the reagents."
        ],
        "a": 0,
        "e": "<strong>Organocatalysis via iminium intermediates:</strong> Proline's secondary amine condenses with the carbonyl group to form a positively charged iminium ion ($\\text{C}=\\text{N}^+\\text{R}_2$). The positively charged nitrogen is substantially more electronegative and acts as a powerful electron sink compared to neutral oxygen ($=\\text{O}$). This dramatically lowers the activation energy for the cleavage of the C&ndash;C bond by stabilizing the enamine intermediate, mimicking the biological Class I aldolase mechanism.<br><br><em>Distractor Traps:</em><br>&bull; B claims proline (a weak base) generates oxide dianions ($\\text{O}^{2-}$), which is impossible in aqueous solution.<br>&bull; C claims irreversible acylation (the reaction is catalytic and reversible).<br>&bull; D misclassifies proline as a phase-transfer catalyst."
    },
    {
        "q": "In glycolysis, the retro-aldol cleavage of D-fructose-1,6-bisphosphate produces dihydroxyacetone phosphate (DHAP) and D-glyceraldehyde-3-phosphate (G3P). How are these two molecules related isomerically?",
        "ch": [
            "They are enantiomers with opposite absolute configurations at all chiral centers.",
            "They are diastereomers differing in configuration at a single stereocenter.",
            "They are constitutional aldose-ketose isomers possessing identical molecular formulas.",
            "They are geometric cis-trans isomers resulting from restricted double-bond rotation."
        ],
        "a": 2,
        "e": "<strong>Triose phosphate structural isomerism:</strong> Both DHAP and G3P share the identical molecular formula $\\text{C}_3\\text{H}_7\\text{O}_6\\text{P}$ (MW = 170.06 g/mol). DHAP is a ketose (ketone at C2: $\\text{CH}_2\\text{OH}-\\text{C}(=\\text{O})-\\text{CH}_2\\text{OPO}_3^{2-}$), whereas G3P is an aldose (aldehyde at C1: $\\text{H}-\\text{C}(=\\text{O})-\\text{CHOH}-\\text{CH}_2\\text{OPO}_3^{2-}$). Because they have the same atoms connected in a different order of bonding, they are constitutional (structural) aldose-ketose isomers, interconverted by triose phosphate isomerase (TPI).<br><br><em>Distractor Traps:</em><br>&bull; A and B are stereoisomers: DHAP has zero chiral centers, so it cannot be an enantiomer or diastereomer of G3P.<br>&bull; D refers to alkenes/rings with restricted rotation."
    },
    {
        "q": "Which proton in 4-hydroxy-4-methylpentan-2-one is the most acidic and therefore initially deprotonated during base-catalyzed retro-aldol cleavage?",
        "ch": [
            "The methyl protons adjacent to the carbonyl carbon (C1)",
            "The hydroxyl proton attached to the tertiary beta-oxygen",
            "The methylene protons situated between the carbonyl and beta-carbons (C3)",
            "The terminal methyl protons attached to the beta-carbon (C5)"
        ],
        "a": 1,
        "e": "<strong>Initial deprotonation in retro-aldol cleavage:</strong> In the retro-aldol reaction under basic conditions, base first removes the proton from the $\\beta$-hydroxyl group ($-\\text{OH}$, $pK_a \\approx 15-16$) to form the reactive alkoxide intermediate ($-\\text{O}^-$). The alkoxide lone pair then kicks down to form a carbonyl ($=\\text{O}$), driving the cleavage of the C&ndash;C bond and releasing the enolate leaving group. While $\\alpha$-protons ($pK_a \\approx 20$) are acidic, the hydroxyl proton is more acidic by ~4 pH units.<br><br><em>Distractor Traps:</em><br>&bull; A and C have $pK_a \\approx 20$ (less acidic than hydroxyl proton).<br>&bull; D has $pK_a \\approx 50$ (alkane methyl, completely unreactive)."
    }
]

passages.append({
    "id": "exam_cp90_2_p6",
    "sec": "C/P",
    "topic": "Carbonyl Chemistry, Directed Aldol & Glycolytic Retro-Aldol Cleavage",
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_2",
    "passage": p6_html,
    "qs": p6_qs
})

print("Passage 6 defined.")

# ==============================================================================
# PASSAGE 7: Strecker and Gabriel Amino Acid Syntheses & Stereochemical Outcomes
# Topics: Strecker synthesis, Gabriel synthesis, imine intermediates, alpha-aminonitriles, phthalimide
# ==============================================================================
p7_html = """<div class="ttl">Passage 7 (Questions 37&ndash;42)</div>
<p>Biochemists and pharmaceutical chemists employ classical organic methodologies to synthesize non-canonical $\\alpha$-amino acids for peptide drug design. Two premier synthetic routes are the <i>Strecker synthesis</i> and the <i>Gabriel synthesis</i>, each operating through distinct reaction mechanisms and stereochemical trajectories.</p>
<p>The Strecker synthesis begins with an aldehyde or ketone reacted with ammonium chloride ($\\text{NH}_4\\text{Cl}$) and potassium cyanide ($\\text{KCN}$). In the first step, condensation of the carbonyl substrate with ammonia yields an imine intermediate. Protonation generates an electrophilic iminium cation that undergoes nucleophilic attack by cyanide ion ($\\text{CN}^-$) to produce an $\\alpha$-aminonitrile. Subsequent acid-catalyzed aqueous hydrolysis of the nitrile functional group converts the cyano carbon into a carboxylic acid, yielding the target $\\alpha$-amino acid, as shown in Scheme 1.</p>
<div style="text-align:center;margin:14px 0;padding:12px;background:#F9FAFB;border:1px solid #E5E7EB;font-family:monospace;font-size:13px;line-height:1.6">
  R-CHO + NH<sub>4</sub>Cl + KCN &rarr; R-CH(NH<sub>2</sub>)CN (&alpha;-aminonitrile) + H<sub>3</sub>O<sup>+</sup>, &Delta; &rarr; R-CH(NH<sub>3</sub><sup>+</sup>)COOH (Racemic DL-Amino Acid)
</div>
<p>The Gabriel (phthalimide) synthesis generates primary amines and $\\alpha$-amino acids while circumventing polyalkylation. Potassium phthalimide acts as a protected, stabilized nitrogen nucleophile in an $S_N2$ alkylation with diethyl bromomalonate. The resulting intermediate is deprotonated by a base and alkylated with an alkyl halide ($\\text{R-X}$). Subsequent vigorous acid hydrolysis hydrolyzes the phthalimide protecting group, hydrolyzes the two ethyl esters into dicarboxylic acids, and induces thermal decarboxylation of the geminal dicarboxylic acid to yield the target $\\alpha$-amino acid.</p>
<p>Researchers synthesized four therapeutic phenylalanine analogues using either the Strecker or Gabriel route. The reaction pathways, starting materials, and optical rotations of the unpurified products are detailed in Table 1.</p>
<table class="tbl">
  <caption>Table 1 Synthetic precursors, reaction routes, and stereochemical outcomes of amino acid analogues</caption>
  <thead>
    <tr><th>Analogue</th><th>Starting Material</th><th>Synthetic Route</th><th>Isolated Yield (%)</th><th>Observed Optical Rotation $[\\alpha]_D^{20}$</th><th>Stereochemical Composition</th></tr>
  </thead>
  <tbody>
    <tr><td>Analogue 1</td><td>2-Phenylacetaldehyde</td><td>Strecker Route</td><td>78%</td><td>$0.0^\\circ$</td><td>Racemic mixture (50% D, 50% L)</td></tr>
    <tr><td>Analogue 2</td><td>4-Fluorobenzaldehyde</td><td>Strecker Route</td><td>82%</td><td>$0.0^\\circ$</td><td>Racemic mixture (50% D, 50% L)</td></tr>
    <tr><td>Analogue 3</td><td>Benzyl bromide + Phthalimide</td><td>Gabriel Route</td><td>71%</td><td>$0.0^\\circ$</td><td>Racemic mixture (50% D, 50% L)</td></tr>
    <tr><td>Analogue 4</td><td>4-Trifluoromethylbenzyl bromide</td><td>Gabriel Route</td><td>68%</td><td>$0.0^\\circ$</td><td>Racemic mixture (50% D, 50% L)</td></tr>
  </tbody>
</table>
<p>During the Strecker synthesis of Analogue 1, spectroscopic monitoring revealed the transient accumulation of an imine intermediate displaying a characteristic infrared stretching band at $1660\\text{ cm}^{-1}$ and a cyano stretching band at $2240\\text{ cm}^{-1}$.</p>"""

p7_qs = [
    {
        "q": "Why do both the Strecker and Gabriel synthetic routes yield optically inactive racemic mixtures (50% D, 50% L) of amino acids?",
        "ch": [
            "Both pathways employ chiral resolving agents that invert stereocenters at equilibrium.",
            "Nucleophilic attack occurs with equal probability from either face of a planar achiral intermediate.",
            "The high temperatures required for acidic hydrolysis racemize enantiopure products via free radicals.",
            "Cyanide and phthalimide ions exist as racemic mixtures of dextrorotatory and levorotatory enantiomers."
        ],
        "a": 1,
        "e": "<strong>Stereochemical origin of racemic mixtures:</strong> In the Strecker synthesis, the imine/iminium intermediate possesses an $sp^2$-hybridized, planar, achiral geometry. The cyanide nucleophile can attack the top face ($re$ face) or the bottom face ($si$ face) with equal thermodynamic probability (50% each), producing an equimolar enantiomeric mixture of $(R)$- and $(S)$-$\\alpha$-aminonitriles. Similarly, in the Gabriel synthesis, thermal decarboxylation of the geminal dicarboxylic acid proceeds through an enol intermediate whose planar $sp^2$ $\\alpha$-carbon is reprotonated equally from both faces. Thus, both syntheses yield racemic, optically inactive mixtures ($[\\alpha] = 0.0^\\circ$).<br><br><em>Distractor Traps:</em><br>&bull; A is false: resolving agents resolve enantiomers into pure optical isomers, not racemates.<br>&bull; C describes radical racemization, which is not the root mechanism.<br>&bull; D is nonsensical: monoatomic/small planar ions like $\\text{CN}^-$ have no chiral centers."
    },
    {
        "q": "During the Strecker synthesis of alanine from acetaldehyde, what is the structure of the intermediate formed immediately prior to nitrile hydrolysis?",
        "ch": [
            "2-hydroxypropanenitrile",
            "2-aminopropanenitrile",
            "prop-2-en-1-amine",
            "2-oxopropanamide"
        ],
        "a": 1,
        "e": "<strong>Strecker intermediates:</strong> Acetaldehyde ($\\text{CH}_3\\text{CHO}$) condenses with ammonia ($\\text{NH}_3$) to yield ethanimine ($\\text{CH}_3\\text{CH}=\\text{NH}$). Cyanide ($\\text{CN}^-$) then attacks the imine carbon to yield an $\\alpha$-aminonitrile: 2-aminopropanenitrile ($\\text{CH}_3-\\text{CH}(\\text{NH}_2)-\\text{C}\\equiv\\text{N}$). Subsequent aqueous acid hydrolysis of the cyano group yields 2-aminopropanoic acid (alanine).<br><br><em>Distractor Traps:</em><br>&bull; A (2-hydroxypropanenitrile / cyanohydrin) is formed if cyanide attacks the aldehyde without ammonia.<br>&bull; C (allylamine) lacks the nitrile carbon.<br>&bull; D (pyruvamide) is an oxidation/amide byproduct."
    },
    {
        "q": "In the Gabriel synthesis, why is phthalimide utilized as the amine precursor rather than simple aqueous ammonia (NH_3)?",
        "ch": [
            "Ammonia is too sterically hindered to participate in bimolecular nucleophilic substitution.",
            "Phthalimide prevents polyalkylation by acting as a mono-nucleophilic nitrogen source.",
            "Phthalimide directly oxidizes the alkyl halide into a carboxylic acid without base.",
            "Ammonia forms an insoluble explosive coordination complex with alkyl bromides."
        ],
        "a": 1,
        "e": "<strong>Preventing polyalkylation via Gabriel synthesis:</strong> When simple ammonia ($\\text{NH}_3$) reacts with an alkyl halide, the resulting primary amine product ($\\text{R-NH}_2$) is <i>more</i> nucleophilic than ammonia due to the electron-donating inductive effect of the alkyl group. Consequently, the primary amine outcompetes ammonia for remaining alkyl halide, undergoing sequential over-alkylation to yield secondary amines, tertiary amines, and quaternary ammonium salts. In contrast, phthalimide has only one acidic nitrogen proton flanked by two electron-withdrawing carbonyl groups. Once deprotonated and alkylated once, the resulting $N$-alkylphthalimide has no remaining acidic protons and its nitrogen lone pair is resonance-delocalized into both carbonyls, completely precluding polyalkylation.<br><br><em>Distractor Traps:</em><br>&bull; A is backwards: ammonia is tiny and unhindered.<br>&bull; C is chemically inaccurate; phthalimide does not oxidize alkyl halides.<br>&bull; D invents explosive complexes."
    },
    {
        "q": "Which step in the Gabriel synthesis involves the loss of carbon dioxide (CO_2)?",
        "ch": [
            "Deprotonation of potassium phthalimide with hydroxide",
            "Nucleophilic S_N2 displacement of bromide from diethyl bromomalonate",
            "Thermal decarboxylation of the 1,3-dicarboxylic acid upon heating",
            "Hydrazinolysis of the phthalhydrazide bicyclic ring"
        ],
        "a": 2,
        "e": "<strong>Decarboxylation of geminal dicarboxylic acids:</strong> After alkylation, acid hydrolysis cleaves the ethyl esters to produce a geminal malonic acid derivative containing two carboxylic acid groups attached to the same $\\alpha$-carbon ($\\beta$-dicarboxylic acid). When heated, $\\beta$-dicarboxylic acids readily undergo thermal decarboxylation through a cyclic six-membered transition state, releasing carbon dioxide gas ($\\text{CO}_2$) and yielding the mono-carboxylic $\\alpha$-amino acid.<br><br><em>Distractor Traps:</em><br>&bull; A, B, and D are acid-base, substitution, and hydrazinolysis reactions, none of which release $\\text{CO}_2$."
    },
    {
        "q": "In the infrared (IR) spectrum recorded during the Strecker synthesis, the diagnostic absorption bands at 1660 cm^-1 and 2240 cm^-1 correspond to which functional group stretching vibrations, respectively?",
        "ch": [
            "C=O stretch and O-H stretch",
            "C=N stretch and C(triple bond)N stretch",
            "C-O stretch and N-H stretch",
            "C=C stretch and C-H stretch"
        ],
        "a": 1,
        "e": "<strong>IR spectroscopy assignments:</strong> In infrared spectroscopy, the carbon-nitrogen double bond of an imine ($\\text{C}=\\text{N}$) appears as a sharp stretch near $1650-1680\\text{ cm}^{-1}$ (analogous to $\\text{C}=\\text{O}$ at $1700\\text{ cm}^{-1}$ and $\\text{C}=\\text{C}$ at $1640\\text{ cm}^{-1}$). The carbon-nitrogen triple bond of a nitrile ($\\text{C}\\equiv\\text{N}$) appears in the characteristic triple-bond region as a sharp, medium-intensity peak at $2220-2260\\text{ cm}^{-1}$.<br><br><em>Distractor Traps:</em><br>&bull; A ($\\text{O}-\\text{H}$ is broad at $3200-3600\\text{ cm}^{-1}$).<br>&bull; C ($\\text{C}-\\text{O}$ is in fingerprint region $1050-1250\\text{ cm}^{-1}$, $\\text{N}-\\text{H}$ is at $3300-3500\\text{ cm}^{-1}$).<br>&bull; D ($\\text{C}-\\text{H}$ is at $2850-3100\\text{ cm}^{-1}$)."
    },
    {
        "q": "What aldehyde starting material is required to synthesize valine ((CH_3)_2CH-CH(NH_2)COOH) via the Strecker synthesis?",
        "ch": [
            "Ethanal (acetaldehyde)",
            "Propanal (propionaldehyde)",
            "2-Methylpropanal (isobutyraldehyde)",
            "3-Methylbutanal (isovaleraldehyde)"
        ],
        "a": 2,
        "e": "<strong>Strecker starting materials:</strong> In the Strecker synthesis, the aldehyde provides all carbons of the amino acid except the carboxyl carbon (which is supplied by cyanide, $\\text{KCN}$). Valine has a five-carbon skeleton with an isopropyl side chain: $(\\text{CH}_3)_2\\text{CH}-\\text{CH}(\\text{NH}_2)-\\text{COOH}$. Removing the carboxyl carbon leaves an isopropyl group attached to the carbonyl: $(\\text{CH}_3)_2\\text{CH}-\\text{CHO}$, which is 2-methylpropanal (isobutyraldehyde).<br><br><em>Distractor Traps:</em><br>&bull; A (ethanal) yields alanine (3 carbons).<br>&bull; B (propanal) yields 2-aminobutanoic acid.<br>&bull; D (3-methylbutanal) yields leucine (6 carbons, containing an isobutyl side chain)."
    }
]

passages.append({
    "id": "exam_cp90_2_p7",
    "sec": "C/P",
    "topic": "Strecker and Gabriel Amino Acid Syntheses & Stereochemical Outcomes",
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_2",
    "passage": p7_html,
    "qs": p7_qs
})

print("Passage 7 defined.")

# ==============================================================================
# DISCRETE QUESTIONS (10 Standalone Questions: 43 to 52)
# Topics: Calorimetry & enthalpy of solution, osmotic pressure, capacitance & dielectrics,
# Beer-Lambert deviations, photoelectric effect & work function, acyl derivative reactivity,
# acetal hydrolysis, SN1 vs SN2 solvent effects, E1 vs E2 Hofmann/Zaitsev, Mass Spec fragmentation
# ==============================================================================
cp_discretes = [
    {
        "q": "When anhydrous lithium chloride (LiCl) is dissolved in water in an insulated constant-pressure calorimeter, the temperature of the solution increases from 22.0 &deg;C to 34.5 &deg;C. What thermodynamic deduction regarding the lattice energy and hydration enthalpy of LiCl is correct?",
        "ch": [
            "The lattice energy is positive, and the dissolution process is endothermic overall.",
            "The magnitude of the hydration enthalpy is greater than the lattice energy.",
            "The magnitude of the lattice energy is greater than the hydration enthalpy.",
            "The entropy change of the solvent is strictly zero throughout the dissolution process."
        ],
        "a": 1,
        "e": "<strong>Thermodynamics of solution:</strong> The enthalpy of solution is given by $\\Delta H_{soln} = \\Delta H_{lattice} + \\Delta H_{hydration}$ (where $\\Delta H_{lattice} > 0$ to separate ions in the crystal lattice, and $\\Delta H_{hydration} < 0$ as ions are hydrated by water dipoles). Because the calorimeter temperature increased, heat was released into the solution, indicating an exothermic dissolution ($\\Delta H_{soln} < 0$). For $\\Delta H_{soln}$ to be negative, the exothermic hydration enthalpy must exceed the endothermic lattice energy in magnitude: $|\\Delta H_{hydration}| > |\\Delta H_{lattice}|$.<br><br><em>Distractor Traps:</em><br>&bull; A and C state an endothermic dissolution, which would cause the temperature to decrease.<br>&bull; D is false: dissolving ions disrupts water hydrogen-bond networks, altering solvent entropy."
    },
    {
        "q": "What is the theoretical osmotic pressure (&Pi;) exerted by a 0.20 M aqueous solution of magnesium chloride (MgCl_2) at physiological temperature (310 K, R = 0.0821 L&middot;atm/(mol&middot;K)), assuming complete ionic dissociation?",
        "ch": [
            "5.09 atm",
            "10.18 atm",
            "15.27 atm",
            "20.36 atm"
        ],
        "a": 2,
        "e": "<strong>Van 't Hoff factor and osmotic pressure:</strong> Osmotic pressure is given by $\\Pi = iMRT$. Magnesium chloride ($\\text{MgCl}_2$) dissociates via $\\text{MgCl}_2(s) \\rightarrow \\text{Mg}^{2+}(aq) + 2\\text{Cl}^-(aq)$, giving a van 't Hoff factor of $i = 1 + 2 = 3$. Substituting: $\\Pi = (3)(0.20\\text{ mol/L})(0.0821\\text{ L}\\cdot\\text{atm}/(\\text{mol}\\cdot\\text{K}))(310\\text{ K}) = (0.60)(25.451) = 15.27\\text{ atm}$.<br><br><em>Distractor Traps:</em><br>&bull; A (5.09 atm) forgets the van 't Hoff factor entirely ($i = 1$).<br>&bull; B (10.18 atm) assumes $i = 2$ (like $\\text{NaCl}$).<br>&bull; D (20.36 atm) assumes $i = 4$."
    },
    {
        "q": "A parallel-plate capacitor with capacitance C_0 is charged to a voltage V_0 by a battery and then disconnected. A dielectric slab with dielectric constant kappa = 4.0 is then fully inserted between the plates. How do the stored electrical potential energy (U) and voltage (V) change?",
        "ch": [
            "Voltage increases by a factor of 4, and stored energy increases by a factor of 4.",
            "Voltage remains constant, and stored energy decreases by a factor of 4.",
            "Voltage decreases by a factor of 4, and stored energy decreases by a factor of 4.",
            "Voltage decreases by a factor of 4, and stored energy remains constant."
        ],
        "a": 2,
        "e": "<strong>Isolated capacitor with dielectric insertion:</strong> When the battery is disconnected, the charge on the plates remains trapped and constant ($Q = Q_0$). Inserting the dielectric increases capacitance by a factor of $\\kappa$: $C' = \\kappa C_0 = 4 C_0$. From $Q = C V$, the new voltage is $V' = Q / C' = Q_0 / (4 C_0) = V_0 / 4$ (voltage decreases by a factor of 4). The stored energy is $U = \\frac{Q^2}{2C}$. Because $C$ quadruples and $Q$ is constant: $U' = \\frac{Q_0^2}{2(4 C_0)} = \\frac{U_0}{4}$ (stored energy decreases by a factor of 4, as the dielectric is pulled inward by electrostatic attraction doing work).<br><br><em>Distractor Traps:</em><br>&bull; A confuses disconnected with battery connected ($V = \\text{constant}$).<br>&bull; B states voltage remains constant (only true if battery remains attached).<br>&bull; D claims energy remains constant."
    },
    {
        "q": "A biochemist using UV-Vis spectrophotometry to quantify protein concentration observes that the measured absorbance deviates from linearity at high protein concentrations (A > 2.5). What physical phenomenon is the primary cause of this deviation from the Beer-Lambert law?",
        "ch": [
            "Total destructive interference between incident photons and fluorophore emissions.",
            "Polychromatic stray light reaching the photodetector and molecular aggregation.",
            "Spontaneous beta decay of peptide bonds altering the molar absorptivity constant.",
            "The complete saturation of atomic nuclei preventing electron transitions."
        ],
        "a": 1,
        "e": "<strong>Deviations from Beer-Lambert law at high concentrations:</strong> The Beer-Lambert law ($A = \\epsilon b c$) assumes monochromatic radiation, independent absorbing species, and purely linear light attenuation. At high concentrations ($A > 2.0-2.5$), transmittance is $< 0.3-1\\%$. At these low light levels, instrumental stray light (light of other wavelengths reaching the detector) becomes a significant fraction of total detected light, causing the apparent absorbance to plateau. Furthermore, close molecular proximity leads to intermolecular electrostatic interactions, dimerization, and aggregation, altering the electronic ground state and molar absorptivity $\\epsilon$.<br><br><em>Distractor Traps:</em><br>&bull; A invents destructive interference.<br>&bull; C invents radioactive nuclear decay in standard proteins.<br>&bull; D misapplies electronic transitions to 'atomic nuclei saturation'."
    },
    {
        "q": "A metallic target has a work function of Phi = 3.20 eV. If ultraviolet light with photon energy E = 5.00 eV shines on the metal in a vacuum phototube, what is the maximum kinetic energy (KE_max) of the ejected photoelectrons?",
        "ch": [
            "1.80 eV",
            "3.20 eV",
            "5.00 eV",
            "8.20 eV"
        ],
        "a": 0,
        "e": "<strong>Photoelectric effect equation:</strong> According to Einstein's photoelectric equation, $KE_{max} = hf - \\Phi = E_{photon} - \\Phi$. Substituting the given values: $KE_{max} = 5.00\\text{ eV} - 3.20\\text{ eV} = 1.80\\text{ eV}$.<br><br><em>Distractor Traps:</em><br>&bull; B (3.20 eV) is the work function $\\Phi$.<br>&bull; C (5.00 eV) is the incident photon energy.<br>&bull; D (8.20 eV) adds the energies ($E + \\Phi$) rather than subtracting."
    },
    {
        "q": "Which carboxylic acid derivative exhibits the greatest reactivity toward nucleophilic acyl substitution, and why?",
        "ch": [
            "Amide, because nitrogen has the lowest electronegativity among second-row heteroatoms.",
            "Ester, because the alkoxy group stabilizes the tetrahedral intermediate by resonance.",
            "Acid anhydride, because the carboxylate leaving group is stabilized by two carbonyls.",
            "Acyl chloride, because chloride is a weak base and an exceptional leaving group."
        ],
        "a": 3,
        "e": "<strong>Reactivity hierarchy of carboxylic acid derivatives:</strong> The reactivity toward nucleophilic acyl substitution follows the order: Acyl chloride > Acid anhydride > Ester $\\approx$ Carboxylic acid > Amide > Carboxylate. Acyl chlorides are the most reactive because the strongly electron-withdrawing chlorine maximizes the partial positive charge ($\\delta^+$) on the carbonyl carbon, and chloride ($\\text{Cl}^-$) is the conjugate base of a strong acid ($\\text{HCl}$, $pK_a \\approx -7$), making it an exceptionally stable, weak base leaving group.<br><br><em>Distractor Traps:</em><br>&bull; A identifies the <i>least</i> reactive neutral derivative (amides are very unreactive due to strong $\\text{N}\\rightarrow\\text{C}=\\text{O}$ resonance).<br>&bull; B and C identify intermediates in the reactivity hierarchy."
    },
    {
        "q": "What reagents and conditions are required to hydrolyze a cyclic acetal protecting group back into the parent ketone and diol?",
        "ch": [
            "Aqueous acid (H_3O^+) and water",
            "Aqueous sodium hydroxide (NaOH) and heat",
            "Lithium aluminum hydride (LiAlH_4) in anhydrous ether",
            "Pyridinium chlorochromate (PCC) in dichloromethane"
        ],
        "a": 0,
        "e": "<strong>Acetal stability and hydrolysis conditions:</strong> Acetals and cyclic ketals are stable to basic reagents, nucleophiles, and reducing agents (which is why they serve as protecting groups). However, they are acid-labile. Exposure to aqueous acid ($\\text{H}_3\\text{O}^+$) protonates an acetal oxygen, forming a good leaving group that departs to yield a resonance-stabilized oxocarbenium ion. Subsequent addition of water and proton transfers fully hydrolyzes the acetal back to the carbonyl compound and diol.<br><br><em>Distractor Traps:</em><br>&bull; B is incorrect: acetals are completely resistant to base and nucleophilic attack.<br>&bull; C is a strong reducing agent that does not cleave acetals.<br>&bull; D is an oxidizing agent that converts secondary alcohols to ketones."
    },
    {
        "q": "A chemist performs a nucleophilic substitution reaction on (R)-2-bromobutane with sodium cyanide (NaCN) in dimethyl sulfoxide (DMSO). What is the kinetic order and stereochemical outcome of this reaction?",
        "ch": [
            "First-order kinetics yielding a racemic mixture of (R) and (S) enantiomers",
            "First-order kinetics yielding complete retention of configuration",
            "Second-order kinetics yielding stereochemical inversion to (S)-2-methylbutanenitrile",
            "Second-order kinetics yielding stereochemical retention to (R)-2-methylbutanenitrile"
        ],
        "a": 2,
        "e": "<strong>$S_N2$ mechanism in polar aprotic solvents:</strong> Cyanide ($\\text{CN}^-$) is a strong nucleophile, 2-bromobutane is a secondary substrate, and dimethyl sulfoxide (DMSO) is a polar aprotic solvent. Polar aprotic solvents do not hydrogen-bond with anions, leaving the cyanide nucleophile bare and highly reactive. This favors a concerted bimolecular nucleophilic substitution ($S_N2$), which follows second-order kinetics (Rate = $k[\\text{substrate}][\\text{nucleophile}]$) and proceeds with backside attack, resulting in 100% Walden inversion of configuration from $(R)$ to $(S)$.<br><br><em>Distractor Traps:</em><br>&bull; A describes an $S_N1$ mechanism (favored by polar protic solvents like water/ethanol).<br>&bull; B and D claim retention of configuration, which does not occur in simple single-step substitutions."
    },
    {
        "q": "Reaction of 2-bromo-2-methylbutane with potassium tert-butoxide (t-BuOK) in tert-butanol predominantly yields 2-methylbut-1-ene rather than 2-methylbut-2-ene. What explains this regiochemical preference?",
        "ch": [
            "Zaitsev's rule dictates formation of the thermodynamically most substituted alkene.",
            "The bulky sterically hindered base preferentially abstracts the more accessible primary proton.",
            "Bromide departs prior to deprotonation, forming an anti-aromatic bridgehead carbocation.",
            "Tert-butanol acts as a Lewis acid that coordinates exclusively to secondary carbons."
        ],
        "a": 1,
        "e": "<strong>Hofmann vs Zaitsev elimination:</strong> Small, unhindered bases (like $\\text{NaOCH}_3$ or $\\text{NaOH}$) abstract the most acidic proton to generate the most substituted, thermodynamically stable alkene (Zaitsev product: 2-methylbut-2-ene). However, potassium tert-butoxide ($t\\text{-BuOK}$) is a large, sterically hindered base. The steric bulk of the three methyl groups prevents it from accessing the more sterically congested secondary proton; instead, it rapidly deprotonates the more sterically exposed primary methyl group, yielding the less-substituted kinetic product (Hofmann product: 2-methylbut-1-ene).<br><br><em>Distractor Traps:</em><br>&bull; A describes Zaitsev's rule, which is superseded here by steric hindrance.<br>&bull; C describes an $E1$ carbocation, whereas $t\\text{-BuOK}$ enforces a concerted $E2$ mechanism.<br>&bull; D invents Lewis acid coordination."
    },
    {
        "q": "In the electron-ionization mass spectrum of 1-bromobutane, what characteristic feature confirms the presence of a single bromine atom in the molecular ion?",
        "ch": [
            "A base peak at m/z = 15 representing a stable methyl carbocation",
            "Two molecular ion peaks (M and M+2) of approximately equal intensity (1:1 ratio)",
            "A single sharp molecular ion peak at an odd m/z value consistent with the nitrogen rule",
            "An M and M+2 isotopic cluster with a 3:1 relative intensity ratio"
        ],
        "a": 1,
        "e": "<strong>Bromine isotopic signature in mass spectrometry:</strong> Bromine exists naturally as two major isotopes: $^{79}\\text{Br}$ (50.7% abundance) and $^{81}\\text{Br}$ (49.3% abundance), separated by 2 mass units. Consequently, any molecular ion or fragment containing a single bromine atom displays a distinctive doublet of peaks ($M$ and $M+2$) with virtually identical heights ($\\approx 1:1$ ratio).<br><br><em>Distractor Traps:</em><br>&bull; D describes chlorine ($^{35}\\text{Cl}$ and $^{37}\\text{Cl}$ with a $3:1$ intensity ratio).<br>&bull; C describes the nitrogen rule for odd numbers of nitrogen atoms.<br>&bull; A is an irrelevant low-mass fragment."
    }
]

passages.append({
    "id": "exam_cp90_2_disc",
    "sec": "C/P",
    "topic": "C/P Standalone Discrete Questions",
    "sheet": None,
    "label": "Chemical and Physical Foundations of Biological Systems",
    "examId": "cp90_2",
    "passage": "",
    "qs": cp_discretes
})

print("Discretes defined.")

total_qs = sum(len(p["qs"]) for p in passages)
print(f"Total C/P Exam 2 questions: {total_qs}")

# Write to exam_cp90_2.js
js_content = "/* ---- exam_cp90_2.js ---- */\n/* Full 90-minute Chem/Phys Practice Exam 2: 7 passages (42 Qs) + 10 discrete Qs = 52 Qs */\nconst EXAM_CP90_2 = " + json.dumps(passages, indent=2) + ";\n"
with open("/home/cgslinde/DrillRoom/DrillRoom/exam_cp90_2.js", "w") as f:
    f.write(js_content)

print("exam_cp90_2.js written successfully!")
