# -*- coding: utf-8 -*-
"""
Suite 1 Bio/Biochem 90 Overhaul: Passages 5 to 8 (Questions 25 to 52)
5-Gate Review Protocol calibration
"""
import re

def validate_questions(qs_list, start_idx=25):
    for i, q in enumerate(qs_list):
        num = start_idx + i
        ans = q["a"]
        ch = q["ch"]
        lens = [len(c) for c in ch]
        
        is_num = all(re.match(r'^[+-]?\d+(?:\.\d+)?(?:/[+-]?\d+(?:\.\d+)?)?(?:\s*(?:×|x)\s*10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹\d+-]+)?(?:\s*[\w%/°℃Ω\^]+)?(?:\s*\([^\)]+\))?$', c.strip()) for c in ch)
        if is_num:
            def extract_val(s):
                m = re.search(r'([+-]?\d+(?:\.\d+)?)', s)
                return float(m.group(1)) if m else 0.0
            vals = [extract_val(c) for c in ch]
            asc = all(vals[j] <= vals[j+1] for j in range(len(vals)-1))
            desc = all(vals[j] >= vals[j+1] for j in range(len(vals)-1))
            assert asc or desc, f"Q{num} numeric choices not sorted: {vals}"
        else:
            ratio = max(lens) / min(lens) if min(lens) > 0 else 999
            assert ratio <= 1.0801, f"Q{num} length ratio violated: {ratio:.3f} (lens: {lens})"
            assert ans != lens.index(max(lens)), f"Q{num} correct choice is strictly longest! ans={ans}, lens={lens}"

        e = q["e"]
        assert "<strong>[Governing Principle:" in e, f"Q{num} missing Governing Principle tag"
        assert "<em>Distractor Traps:</em><br>&bull;" in e, f"Q{num} missing Distractor Traps tag"
        other_letters = [chr(65+j) for j in range(4) if j != ans]
        for ol in other_letters:
            assert f"&bull; {ol} (" in e, f"Q{num} missing autopsy for {ol}"
    print(f"Validated {len(qs_list)} questions starting at Q{start_idx} successfully!")

p5_qs = [
    {
        "q": "Based on the patch-clamp electrophysiology in Table 1, LQT2 (KCNH2 dominant negative) and LQT3 (SCN5A gain-of-function) prolong action potential duration (APD90) through which respective biophysical mechanisms?",
        "ch": [
            "LQT2 accelerates inward Phase 0 depolarization, whereas LQT3 suppresses transient Phase 1 efflux",
            "LQT2 destroys resting potassium conductance IK1, whereas LQT3 blocks inward L-type calcium channels",
            "LQT2 blocks voltage-gated chloride channels in cells, whereas LQT3 accelerates delayed rectifier K+",
            "LQT2 impairs repolarizing outward IKr, whereas LQT3 promotes sustained late INa,L influx in cells"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Ion Channel Biophysics and Cardiac Action Potential Kinetics]</strong><br><br>1. <em>Extract Biophysical Parameters from Table 1:</em> Control APD90 is 340 ms. In LQT2, peak repolarizing outward potassium current (IKr) crashes from 4.2 to 0.8 pA/pF, prolonging APD90 to 590 ms while sodium current remains normal. In LQT3, peak IKr is normal (4.2 pA/pF), but sustained non-inactivating late sodium current (late INa,L) surges from 0.2% to 2.8% of peak, prolonging APD90 to 560 ms.<br>2. <em>Synthesize Biophysical Mechanisms:</em> Ventricular repolarization requires net outward positive current (K+ efflux) exceeding inward positive current. LQT2 reduces outward positive charge removal by crippling hERG/IKr potassium channels during Phase 3. Conversely, LQT3 introduces abnormal persistent inward positive charge entry via mutant NaV1.5 channels that fail to completely inactivate during Phase 2/3.<br>3. <em>Derive Net Phenotype:</em> Both distinct channel defects disrupt the delicate balance of transmembrane charge transfer, delaying membrane repolarization back to the -85 mV resting potential and substantially prolonging APD90.<br><br><em>Distractor Traps:</em><br>&bull; A (Phase Conflation): LQT2/3 channelopathies affect Phase 2/3 repolarization and plateau duration, not initial Phase 0 upstroke velocity or Phase 1 Ito.<br>&bull; B (Wrong Current Assignment): Neither mutation impacts inward rectifier IK1 (which governs Phase 4 resting potential), and LQT3 does not block L-type calcium channels.<br>&bull; C (Directional & Conductance Inversion): Cardiac repolarization is driven by K+ efflux, not Cl- channels; LQT3 causes persistent inward Na+, not accelerated K+ conductance."
    },
    {
        "q": "Early afterdepolarizations (EADs) that trigger fatal polymorphic ventricular arrhythmias (Torsades de Pointes) in LQT patients are initiated primarily by:",
        "ch": [
            "sudden opening of nuclear pore complexes allowing calcium leakage into the sarcoplasm of myocytes",
            "re-activation of voltage-gated L-type Ca2+ channels (Cav1.2) during prolonged Phase 2/3 plateaus",
            "spontaneous ATP depletion within the matrix causing rapid potassium channel opening in myocytes",
            "abrupt efflux of divalent magnesium ions through sarcolemmal calcium-activated pump complexes"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Arrhythmogenesis and Window Currents in Delayed Cardiac Repolarization]</strong><br><br>1. <em>Voltage-Dependent Gating of Cav1.2:</em> L-type calcium channels (Cav1.2) open upon depolarization, inactivate slowly during Phase 2, and recover from inactivation as the membrane potential repolarizes between -40 mV and -10 mV (the 'window current' voltage range).<br>2. <em>Pathophysiology of Prolonged Plateaus:</em> When repolarization is delayed (due to crippled IKr or late INa,L), the myocyte membrane remains stalled within this critical -40 to -10 mV window for an extended duration.<br>3. <em>Triggered Trigger Activity:</em> Stalling in this voltage window permits Cav1.2 channels to recover from inactivation and re-open. Inward Ca2+ influx through re-opened Cav1.2 channels (amplified by forward-mode Na+/Ca2+ exchanger NCX current) depolarizes the membrane, producing an oscillatory depolarization known as an early afterdepolarization (EAD). If the EAD reaches threshold, it fires a triggered action potential that initiates Torsades de Pointes.<br><br><em>Distractor Traps:</em><br>&bull; A (Subcellular Anomaly): EADs are sarcolemmal electrical events governed by plasma membrane ion channels, not nuclear pore complexes.<br>&bull; C (Ischemia Confusion): ATP depletion opens K_ATP channels during acute myocardial ischemia (which shortens APD, causing re-entry), rather than producing delayed repolarization EADs.<br>&bull; D (Magnesium Misapplication): While intravenous magnesium sulfate is administered clinically to stabilize membranes and suppress EADs, EAD generation is driven by Ca2+ influx, not sarcolemmal Mg2+ efflux."
    },
    {
        "q": "Why does mexiletine (Row 6) abolish arrhythmic events and normalize APD90 in LQT3 cardiomyocytes while leaving peak Phase 0 depolarization unimpaired?",
        "ch": [
            "Mexiletine activates inward rectifier IK1 channels to accelerate terminal Phase 4 resting recovery",
            "Mexiletine upregulates transcription of KCNH2 mRNA to double outward repolarizing IKr density",
            "Mexiletine selectively blocks the pathological late INa,L current without suppressing peak INa",
            "Mexiletine irreversibly chelates extracellular calcium ions to terminate the Phase 2 plateau"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: State-Dependent Sodium Channel Blockade and Targeted Pharmacotherapy]</strong><br><br>1. <em>Electrophysiological Defect in LQT3:</em> Gain-of-function mutations in SCN5A disrupt the fast inactivation gate (III-IV linker or IFM motif) of NaV1.5, allowing a small, sustained non-inactivating late sodium current (late INa,L = 2.8%) to leak during Phase 2/3, which prolongs APD90 to 560 ms.<br>2. <em>Pharmacological Profile of Mexiletine:</em> Mexiletine is a Class IB antiarrhythmic agent that exhibits state-dependent binding with fast unbinding kinetics, showing exceptional selectivity for inactivated/bursting open conformations of NaV1.5 over closed/resting states.<br>3. <em>Empirical Verification:</em> Table 1 shows that mexiletine reduces late INa,L from 2.8% to 0.3% (a ~90% inhibition), while peak INa is preserved (-210 vs -220 pA/pF, >95% retained). By selectively eliminating the abnormal plateau-phase sodium leak, mexiletine rescues APD90 back to 355 ms and completely abolishes EADs without blunting Phase 0 conduction velocity.<br><br><em>Distractor Traps:</em><br>&bull; A (Potassium Channel Conflation): Mexiletine is a sodium channel blocker; it does not activate inward rectifier IK1 channels.<br>&bull; B (Wrong Gene & Mechanism): Mexiletine does not alter hERG expression or enhance IKr; its action is targeted directly at NaV1.5 channels.<br>&bull; D (Chelation Distractor): Mexiletine does not chelate extracellular calcium; extracellular chelation would cause profound hypocalcemic neuromuscular excitability and circulatory collapse."
    },
    {
        "q": "During Phase 4 of the cardiac ventricular action potential, the stable resting membrane potential (-85 mV) is predominantly established and maintained by:",
        "ch": [
            "high baseline resting permeability to K+ via IK1 channels coupled with the Na+/K+-ATPase pump",
            "continuous active efflux of calcium ions through sarcolemmal SERCA pumps into the interstitium",
            "sustained inward conductance of chloride ions through resting CFTR channels in the sarcolemma",
            "passive electrochemical equilibration of extracellular sodium ions through open leak channels"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Goldman-Hodgkin-Katz Equilibrium and Resting Membrane Conductance]</strong><br><br>1. <em>Goldman-Hodgkin-Katz Voltage Relationship:</em> The resting membrane potential (Vm) is determined by the relative permeabilities (P) of the cell membrane to major physiological ions and their respective equilibrium potentials (E_ion).<br>2. <em>Dominant Permeability in Phase 4:</em> In ventricular myocytes at rest, inward rectifier potassium channels (IK1) are constitutively open, rendering potassium permeability (P_K) overwhelmingly larger than sodium (P_Na) or calcium (P_Ca) permeabilities (P_K >> P_Na, P_Ca). Consequently, Vm (-85 mV) sits extremely close to the potassium Nernst equilibrium potential (E_K ~ -90 mV).<br>3. <em>Active Maintenance of Gradients:</em> The electrogenic Na+/K+-ATPase continuously pumps 3 Na+ out and 2 K+ in per ATP hydrolyzed, replenishing the trans-sarcolemmal chemical concentration gradients that permit IK1-mediated K+ efflux to maintain resting potential stability.<br><br><em>Distractor Traps:</em><br>&bull; B (SERCA Localization Error): SERCA is an intracellular pump localized on the sarcoplasmic reticulum membrane that sequesters cytosolic Ca2+ into the SR lumen, not across the sarcolemma into interstitial space.<br>&bull; C (Chloride Equilibrium Error): Resting ventricular potential is not governed by CFTR chloride channels; E_Cl (~ -65 mV) is significantly less negative than Phase 4 Vm (-85 mV).<br>&bull; D (Depolarizing Gradient Inversion): High sodium permeability would drive Vm toward E_Na (+60 mV), causing resting depolarization, not a stable -85 mV potential."
    },
    {
        "q": "On a standard 12-lead electrocardiogram (ECG), the QT interval reflects the total duration of which physiological event across the ventricular myocardium?",
        "ch": [
            "The time required for electrical conduction to traverse the atrioventricular AV node alone in heart",
            "The isolated period of ventricular mechanical contraction occurring strictly during systole phase",
            "The duration of atrial depolarization and subsequent repolarization prior to the QRS wave in rhythm",
            "The total time required for ventricular depolarization and subsequent complete repolarization"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Electrocardiographic Vector Correlation with Cellular Action Potentials]</strong><br><br>1. <em>ECG Waveform Anatomy:</em> The QRS complex marks the onset of ventricular myocardial depolarization (corresponding to cellular Phase 0). The T wave marks the completion of ventricular myocardial repolarization (corresponding to Phase 3).<br>2. <em>Interval Definition:</em> The QT interval is measured from the very beginning of the QRS complex to the point where the T wave returns to the isoelectric baseline.<br>3. <em>Cellular Integration:</em> Because it spans from initial depolarization through final repolarization, the QT interval directly represents the aggregate duration of ventricular action potentials (APD) across the ventricular syncytium. Prolongation of cellular APD90 (as seen in LQT syndromes) manifests directly as QT prolongation on surface ECGs.<br><br><em>Distractor Traps:</em><br>&bull; A (PR Interval Conflation): AV nodal conduction delay is represented by the PR interval (specifically the PR segment), not the QT interval.<br>&bull; B (Mechanical vs Electrical Scope Error): The ECG records electrical potential differences across cardiac tissue, not mechanical muscle tension; although mechanical systole coincides temporally, the QT interval is fundamentally an electrical measure.<br>&bull; C (Atrial Activity Error): Atrial depolarization produces the P wave; atrial repolarization (Ta wave) is buried within the QRS complex."
    },
    {
        "q": "The absolute refractory period (ARP) of cardiac ventricular myocytes is extraordinarily long (~250 ms) compared to skeletal muscle fibers (~2 ms). What vital physiological adaptation does this prevent?",
        "ch": [
            "It prevents premature activation of the sympathetic nervous system during vigorous exercise",
            "It prevents tetanic sustained contraction, ensuring intermittent filling and pumping phases",
            "It prevents excess calcium entry to protect the sarcolemma from lethal proteolytic lysis",
            "It prevents outward potassium flux from dissipating intracellular glycogen energy stores"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Electromechanical Coupling and Cardiac Hemodynamic Protection]</strong><br><br>1. <em>Biophysical Basis of Refractoriness:</em> During Phase 0, NaV1.5 channels open and then rapidly enter a non-conducting inactivated state. They cannot transition back to the closed-activatable resting state until the membrane repolarizes to negative potentials (below -50 mV). Because the Phase 2 plateau maintains prolonged depolarization, myocytes remain in the absolute refractory period (ARP) for ~200-250 ms.<br>2. <em>Mechanical Contraction Duration:</em> A cardiac ventricular twitch contraction lasts approximately 250-300 ms. Thus, electrical refractoriness outlasts the peak developed mechanical tension.<br>3. <em>Hemodynamic Necessity:</em> Because the myocyte cannot fire a second action potential while still contracting, cardiac muscle cannot undergo wave summation or tetany (sustained involuntary spastic contraction). This ensures the heart relaxes during diastole, allowing ventricular chambers to fill with blood before the subsequent systolic stroke.<br><br><em>Distractor Traps:</em><br>&bull; A (Autonomic Mismatch): Sympathetic adrenergic stimulation actively modulates heart rate and contractility; refractory periods protect cardiac muscle tissue locally, not sympathetic tone.<br>&bull; C (Excitotoxicity Distractor): While prolonged Ca2+ overload is detrimental, the primary evolutionary and physiological design of the long ARP is hemodynamic (preventing tetany).<br>&bull; D (Metabolic Confabulation): Potassium conductance does not directly consume or dissipate glycogen stores."
    }
]
p6_qs = [
    {
        "q": "In isolated mitochondria challenged with rotenone (Condition 4), why does adding succinate completely restore oxygen consumption and coupled ATP synthesis?",
        "ch": [
            "Succinate hydrolyzes mitochondrial GTP to pump protons across Complex I directly in matrix",
            "Succinate donates electrons to Complex II (FAD), bypassing the rotenone block at Complex I",
            "Succinate allosterically displaces rotenone from the NADH-ubiquinone binding active pocket",
            "Succinate acts as a synthetic uncoupler that dissipates the inner membrane proton gradient"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Convergent Electron Entry Points into the Mitochondrial Respiratory Chain]</strong><br><br>1. <em>Electron Entry Architecture:</em> The electron transport chain features two parallel initial electron entry portals: Complex I (NADH:ubiquinone oxidoreductase), which extracts electrons from NADH, and Complex II (succinate dehydrogenase), which extracts electrons from succinate via its covalently bound FAD prosthetic group.<br>2. <em>Locus of Rotenone Blockade:</em> Rotenone specifically binds the ubiquinone reduction site of Complex I, halting electron transfer from NADH to ubiquinone (Q).<br>3. <em>Functional Bypass via Complex II:</em> Complex II operates independently of Complex I. Succinate dehydrogenase oxidizes succinate to fumarate, reducing FAD to FADH2, which immediately transfers 2 electrons into the inner membrane ubiquinone pool (reducing Q to QH2). Reduced QH2 shuttles electrons directly to Complex III &rarr; cytochrome c &rarr; Complex IV &rarr; O2, pumping protons at Complexes III and IV to regenerate the proton motive force and drive ATP synthesis.<br><br><em>Distractor Traps:</em><br>&bull; A (Substrate-Level Energy Fabrication): Succinate is a TCA cycle substrate; it does not hydrolyze GTP to pump protons, nor does it interact with Complex I.<br>&bull; C (Competitive Displacement Error): Succinate binds Complex II, not Complex I; it does not displace rotenone from Complex I.<br>&bull; D (Uncoupler Confabulation): An uncoupler dissipates the proton gradient and STOPS ATP synthesis; succinate drives coupled respiration that actively SYNTHESIZES ATP."
    },
    {
        "q": "In Condition 6, adding oligomycin directly inhibits the F0 subunit of ATP synthase, causing oxygen consumption to crash to near zero. Why does inhibiting ATP synthesis arrest electron transport in well-coupled mitochondria?",
        "ch": [
            "Oligomycin oxidizes all intramitochondrial NADH molecules into NAD+ to deplete electron pools",
            "Oligomycin covalently cleaves cytochrome c, severing electron transfer between III and IV cristae",
            "Oligomycin opens giant outer membrane channels, dissipating all mitochondrial substrate gradients",
            "Proton pumping against a hyperpolarized electrochemical gradient is thermodynamically arrested"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Respiratory Control and Chemiosmotic Back-Pressure]</strong><br><br>1. <em>Chemiosmotic Coupling:</em> Electron transport through Complexes I, III, and IV pumps protons from matrix into the intermembrane space, generating the proton motive force (&Delta;p = &Delta;&Psi; - 60&Delta;pH). In basal State 3 respiration, protons re-enter the matrix through the F0 channel of ATP synthase, driving ATP production and relieving the proton gradient.<br>2. <em>Effect of Oligomycin:</em> Oligomycin binds the c-ring of the F0 subunit, physically occluding the proton translocation path and arresting proton flux into the matrix.<br>3. <em>Thermodynamic Back-Pressure:</em> Because protons can no longer re-enter the matrix, continued electron transport pumps protons until the proton electrochemical gradient (&Delta;p) reaches a maximal thermodynamic ceiling (~220 mV). At this point, the free energy required to pump an additional proton (&Delta;G_pump = F&Delta;p) exceeds the free energy liberated by electron transfer (&Delta;G_redox). Electron flow stalls, halting O2 consumption (respiratory control).<br><br><em>Distractor Traps:</em><br>&bull; A (Redox State Inversion): Inhibiting the ETC causes NADH to accumulate in its reduced form; it does not oxidize NADH.<br>&bull; B (Structural Damage Distractor): Oligomycin is a specific inhibitor of ATP synthase; it does not cleave cytochrome c.<br>&bull; C (Membrane Rupture Confabulation): Intact inner membrane impermeability is preserved; if channels opened, uncoupling would occur and oxygen consumption would soar."
    },
    {
        "q": "Based on the proton pumping stoichiometry of the respiratory complexes described in the passage, how many total protons are translocated from the matrix into the intermembrane space per pair of electrons originating from NADH versus FADH2?",
        "ch": [
            "NADH translocates 10 H+ (4 at I, 4 at III, 2 at IV); FADH2 translocates 6 H+ (4 at III, 2 at IV)",
            "NADH translocates 12 H+ (4 at I, 4 at III, 4 at IV); FADH2 translocates 8 H+ (4 at III, 4 at IV) net",
            "NADH translocates 8 H+ (4 at I, 2 at III, 2 at IV); FADH2 translocates 4 H+ (2 at III, 2 at IV) net",
            "NADH translocates 6 H+ (2 at I, 2 at III, 2 at IV); FADH2 translocates 3 H+ (2 at III, 1 at IV) net"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Stoichiometric Proton Translocation in Chemiosmotic Theory]</strong><br><br>1. <em>Complex Proton Stoichiometries:</em> Complex I (NADH:ubiquinone oxidoreductase) pumps 4 H+ per 2e- transferred from NADH to ubiquinone. Complex II (succinate dehydrogenase) pumps 0 H+ across the membrane. Complex III (cytochrome bc1 complex, via Q cycle) pumps 4 H+ per 2e- transferred to cytochrome c. Complex IV (cytochrome c oxidase) pumps 2 H+ per 2e- transferred to terminal 1/2 O2.<br>2. <em>Proton Summation for NADH:</em> Electrons from NADH traverse Complex I (4 H+), Complex III (4 H+), and Complex IV (2 H+). Total protons translocated = 4 + 4 + 2 = 10 H+.<br>3. <em>Proton Summation for FADH2:</em> Electrons from FADH2 enter at Complex II (0 H+), then traverse Complex III (4 H+) and Complex IV (2 H+). Total protons translocated = 0 + 4 + 2 = 6 H+. This 10:6 ratio explains why NADH yields ~2.5 ATP whereas FADH2 yields ~1.5 ATP (given ~4 H+ required per ATP synthesized and imported).<br><br><em>Distractor Traps:</em><br>&bull; B (Complex IV Overestimate): Complex IV translocates 2 protons per electron pair, not 4 (4 H+ are pumped per full O2 reduced by 4 electrons).<br>&bull; C (Complex III Underestimate): Complex III pumps 4 H+ via the Q cycle mechanism, not 2.<br>&bull; D (Gross Underestimate): Classical older textbooks occasionally misattributed ratios, but the established structural consensus is 10 H+ for NADH and 6 H+ for FADH2."
    },
    {
        "q": "Cyanide (CN-) and carbon monoxide (CO) act as lethal cellular poisons by selectively binding the heme a3-CuB binuclear center of which electron transport chain component?",
        "ch": [
            "Complex I, preventing electron transfer from flavin mononucleotide to iron-sulfur centers in core",
            "Complex II, preventing oxidation of succinate into fumarate during the citric acid cycle in cells",
            "Complex IV (cytochrome c oxidase), blocking terminal electron transfer to molecular oxygen gas",
            "Complex III (cytochrome bc1), preventing ubiquinol oxidation via the Q cycle mechanism in cristae"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Targeted Inhibitors of Terminal Electron Transfer and Heme Coordination]</strong><br><br>1. <em>Molecular Target:</em> Cyanide (CN-) and carbon monoxide (CO) possess high affinity for the transition metal centers of heme proteins. In the ETC, their primary lethal target is the heme a3-CuB binuclear center of Complex IV (cytochrome c oxidase).<br>2. <em>Mechanism of Inhibition:</em> CN- and CO coordinate tightly to the iron in heme a3, sterically and electronically preventing molecular oxygen (O2) from binding.<br>3. <em>Downstream Consequences:</em> Because oxygen cannot be reduced to water, Complex IV cannot reoxidize cytochrome c. Cytochrome c remains reduced, which backs up Complex III, ubiquinone, and Complexes I and II. All electron transport ceases, the proton motive force collapses as existing protons leak, ATP synthesis arrests, and cells undergo rapid hypoxic death.<br><br><em>Distractor Traps:</em><br>&bull; A (Complex I Inhibitor): Rotenone and piericidin A inhibit Complex I; cyanide targets Complex IV.<br>&bull; B (Complex II Inhibitor): Malonate competitively inhibits Complex II (succinate dehydrogenase).<br>&bull; D (Complex III Inhibitor): Antimycin A inhibits Complex III at the Qi site; myxothiazol inhibits at the Qo site."
    },
    {
        "q": "During active State 3 mitochondrial respiration in intact, well-coupled hepatocytes, the mitochondrial matrix exhibits which pH and electrical polarity relative to the intermembrane space?",
        "ch": [
            "The matrix is more acidic (lower pH) and electrically positive relative to space in organelle",
            "The matrix is more alkaline (higher pH) and electrically negative relative to space in organelle",
            "The matrix is more alkaline (higher pH) and electrically positive relative to the outer organelle",
            "The matrix is iso-osmolar with identical pH and zero potential relative to space in organelle"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Electrochemical Components of the Proton Motive Force]</strong><br><br>1. <em>Direction of Proton Translocation:</em> Active respiratory complexes (Complexes I, III, and IV) pump positively charged protons (H+) outward from the mitochondrial matrix into the intermembrane space (IMS).<br>2. <em>Chemical Gradient (&Delta;pH):</em> Removing H+ ions from the matrix reduces [H+] inside the matrix, rendering the matrix more alkaline (pH ~7.8 to 8.0) than the intermembrane space (pH ~7.0 to 7.2, which equilibrates with the cytosol via outer membrane porins).<br>3. <em>Electrical Membrane Potential (&Delta;&Psi;):</em> Translocating positive charge (H+) outward leaves an excess of unneutralized negative charges (e.g., from polyanionic proteins and phosphates) inside the matrix. Consequently, the matrix interior becomes electrically negative (-150 to -180 mV) relative to the intermembrane space.<br><br><em>Distractor Traps:</em><br>&bull; A (Complete Inversion): Reversing both vectors assumes protons are pumped INTO the matrix, which is the exact opposite of ETC function.<br>&bull; C (Charge Inversion): Correctly recognizes matrix alkalinity but errs on electrical charge; outward positive charge pumping makes the matrix electrically negative, not positive.<br>&bull; D (Equilibrium Fallacy): In active State 3 respiration, the inner mitochondrial membrane maintains a steep non-equilibrium electrochemical proton gradient (&Delta;p ~180-220 mV)."
    },
    {
        "q": "Brown adipose tissue (BAT) produces non-shivering thermogenesis in neonates using uncoupling protein 1 (UCP1 / thermogenin). How does UCP1 alter the bioenergetics of oxidative phosphorylation?",
        "ch": [
            "It selectively blocks oxygen consumption at Complex IV, releasing latent chemical enthalpy in cristae",
            "It accelerates ATP synthase rotation to hydrolyze newly formed ATP into heat energy directly in BAT",
            "It acts as a competitive substrate for Complex II, driving futile redox cycling in inner cristae",
            "It allows protons to re-enter matrix without passing through ATP synthase, dissipating PMF as heat"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Physiological Uncoupling and Chemiosmotic Thermogenesis]</strong><br><br>1. <em>Structure and Function of UCP1:</em> Thermogenin (UCP1) is an integral inner mitochondrial membrane carrier protein abundant in brown adipose tissue that acts as a regulated proton channel.<br>2. <em>Short-Circuiting the Circuit:</em> Activated by fatty acids (released via &beta;3-adrenergic signaling during cold exposure), UCP1 provides an alternative, low-resistance pathway for protons to flow down their electrochemical gradient from the intermembrane space back into the matrix, bypassing the F0F1 ATP synthase.<br>3. <em>Thermodynamic Outcome:</em> Because the proton electrochemical gradient (&Delta;p) is dissipated without performing mechanical work (ATP synthesis), the immense potential energy of substrate oxidation is released entirely as thermal energy (heat). Respiration runs at maximal rates (high O2 consumption) uninhibited by ATP feedback, generating essential warmth for neonates and hibernating mammals.<br><br><em>Distractor Traps:</em><br>&bull; A (Respiratory Inhibition Error): UCP1 increases oxygen consumption rather than blocking it; respiration accelerates because proton back-pressure is relieved.<br>&bull; B (ATP Hydrolysis Distractor): UCP1 uncouples respiration from ATP synthesis; it does not drive ATP synthase in reverse or consume cellular ATP stores.<br>&bull; C (Redox Cycling Confabulation): UCP1 is a proton transporter, not a redox substrate or electron transport complex component."
    }
]
p7_qs = [
    {
        "q": "Why does Patient 1, who carries homozygous null mutations in the RAG1 gene, present with severe combined immunodeficiency (SCID) marked by a complete absence of mature B and T lymphocytes?",
        "ch": [
            "RAG1/2 endonucleases are indispensable for initiating DNA cleavage at conserved RSSs in lymphocytes",
            "RAG1 is a transcriptional master regulator required for interleukin-7 receptor surface expression",
            "RAG1 catalyzes non-homologous end joining ligation of broken chromosomal DNA strands in the marrow",
            "RAG1 phosphorylates Bruton tyrosine kinase to activate pre-B cell receptor signaling cascades in cells"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Enzymatic Initiation of V(D)J Recombination and Lymphocyte Ontogeny]</strong><br><br>1. <em>Physiological Role of RAG1/2:</em> The RAG1/RAG2 endonuclease complex is exclusively expressed in immature lymphocytes during the early stages of B-cell and T-cell development. It specifically recognizes recombination signal sequences (RSSs) flanking variable (V), diversity (D), and joining (J) gene segments.<br>2. <em>Enzymatic Mechanism:</em> RAG1 introduces a single-strand nick adjacent to the RSS, and the liberated 3'-OH attacks the opposite strand, forming a covalently closed DNA hairpin intermediate at the coding ends and blunt 5'-phosphorylated signal ends.<br>3. <em>Genetic Consequence of RAG1 Loss:</em> Without functional RAG1, neither B-cell receptors (immunoglobulins) nor T-cell receptors (TCRs) can undergo somatic gene rearrangement. Developing pro-B and pro-T cells arrest irreversibly at early developmental checkpoints and undergo apoptosis, resulting in a total absence of mature peripheral B and T cells (T-B- SCID).<br><br><em>Distractor Traps:</em><br>&bull; B (Transcription Factor Conflation): RAG1 is a DNA recombinase/endonuclease, not a transcription factor; IL-7R signaling requires cytokines and STAT transcription factors.<br>&bull; C (NHEJ Enzyme Mismatch): Ligation of cleaved ends is catalyzed by ubiquitous NHEJ machinery (Ku70/80, DNA-PKcs, Artemis, XRCC4, DNA ligase IV), not RAG1.<br>&bull; D (Signaling Kinase Confusion): BTK is an intracellular tyrosine kinase involved in pre-BCR signaling, not a downstream substrate of RAG1."
    },
    {
        "q": "Patient 2 carries a catalytic loss-of-function mutation in activation-induced cytidine deaminase (AID). Which molecular immunologic process will be completely abolished in this patient?",
        "ch": [
            "Initial V(D)J recombination of immunoglobulin heavy and light chain variable loci in bone marrow",
            "Junctional diversity generated by terminal deoxynucleotidyl transferase (TdT) nucleotide insertion",
            "Somatic hypermutation (SHM) for affinity maturation and class-switch recombination (CSR) in nodes",
            "Alternative RNA splicing of primary transcripts yielding membrane-bound versus secreted IgM forms"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Cytidine Deamination in Somatic Hypermutation and Class-Switch Recombination]</strong><br><br>1. <em>Function and Expression of AID:</em> Activation-induced cytidine deaminase (AID) is expressed selectively in mature germinal center B cells upon antigen activation and CD40 co-stimulation.<br>2. <em>Biochemical Action:</em> AID deaminates cytosine (C) bases to uracil (U) within single-stranded DNA during active immunoglobulin gene transcription.<br>3. <em>Dual Immunologic Roles:</em> In variable regions, processing of these U:G mismatches by base excision repair (uracil-DNA glycosylase) or mismatch repair (MSH2/6) introduces point mutations, driving somatic hypermutation (SHM) and affinity maturation. In switch (S) regions upstream of constant heavy (CH) genes, clustered U:G lesions are converted to double-strand breaks that mediate class-switch recombination (CSR) from IgM to IgG, IgA, or IgE. Thus, defective AID abolishes both SHM and CSR (Hyper-IgM Syndrome Type 2).<br><br><em>Distractor Traps:</em><br>&bull; A (Primary Recombination Error): V(D)J recombination occurs in the bone marrow prior to antigen exposure and depends on RAG1/2, not AID.<br>&bull; B (Junctional Diversity Mismatch): N-nucleotide addition during V(D)J recombination is catalyzed by TdT (terminal deoxynucleotidyl transferase) in immature cells.<br>&bull; D (Post-Transcriptional Misconception): Alternative RNA splicing mediates the choice between membrane-bound (hydrophobic C-terminus) and secreted (hydrophilic C-terminus) IgM; AID acts strictly on DNA."
    },
    {
        "q": "Why does Patient 2 (AID deficiency) exhibit elevated serum IgM (380 mg/dL) alongside virtually undetectable levels of serum IgG, IgA, and IgE?",
        "ch": [
            "AID normally acts as a transcriptional repressor that suppresses baseline IgM synthesis in B lymphocytes",
            "IgM expression requires RAG1-mediated inversion, whereas other isotypes require RNA degradation in cells",
            "T-helper cells selectively destroy B cells that attempt to secrete IgG or IgA in secondary lymph nodes",
            "B cells can transcribe the default C\u03bc constant region, but cannot undergo CSR to other isotypes in body"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Genomic Architecture of Immunoglobulin Heavy Chain Constant Regions]</strong><br><br>1. <em>Organization of the IgH Locus:</em> In naive mature B cells, the rearranged VDJ variable exon is positioned immediately upstream of the constant &mu; (C&mu;) and constant &delta; (C&delta;) genes. Primary transcripts encompassing VDJ-C&mu; produce IgM without requiring DNA excision.<br>2. <em>Requirement for Class-Switch Recombination (CSR):</em> To express downstream isotypes (C&gamma; for IgG, C&alpha; for IgA, C&epsilon; for IgE), B cells must undergo AID-mediated DNA double-strand breaks at repetitive switch (S) regions flanking the intervening constant genes, followed by non-homologous excision of C&mu; and ligation of VDJ to the target CH gene.<br>3. <em>Pathophysiological Consequence:</em> In the absence of AID, CSR cannot take place. B cells proliferate and respond to antigen by secreting massive amounts of default pentameric IgM, but cannot switch to IgG, IgA, or IgE. Serum IgM is elevated or normal, while all downstream isotypes are absent.<br><br><em>Distractor Traps:</em><br>&bull; A (Repressor Fallacy): AID does not act as a transcriptional repressor; it is an enzymatic DNA deaminase.<br>&bull; B (Recombination Mismatch): RAG1 operates during initial VDJ assembly in the bone marrow; isotype switching is a distinct AID-dependent DNA deletion process, not RNA degradation.<br>&bull; C (Autoimmune Distractor): Helper T cells do not kill switched B cells; CD4+ T follicular helper cells provide CD40L and cytokines to promote switching."
    },
    {
        "q": "Patient 4 carries a hemizygous mutation in the CD40L (CD154) gene on the X chromosome. Why does this defect impair antibody class switching despite normal intrinsic AID gene integrity in B cells?",
        "ch": [
            "CD40L is an essential co-factor that directly cleaves single-stranded DNA hairpins in switch regions",
            "CD40L on activated CD4+ T cells must bind CD40 on B cells to induce AID expression and CSR signaling",
            "CD40L functions as the antigen-binding variable fragment of the B-cell receptor complex in follicles",
            "CD40L is a coreceptor on cytotoxic CD8+ T cells required to eliminate autoreactive B cell clones"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: T-Cell Dependent B-Cell Activation and Costimulatory Signaling]</strong><br><br>1. <em>Cellular Interactions in Humoral Immunity:</em> For protein antigens, B cells require two signals to form germinal centers, undergo class-switching, and generate memory: Signal 1 via BCR antigen binding, and Signal 2 via T-cell help.<br>2. <em>CD40-CD40L Costimulation:</em> Following antigen presentation by B cells on MHC Class II, activated antigen-specific CD4+ T follicular helper (Tfh) cells express CD40 Ligand (CD40L / CD154) on their surface. CD40L binds CD40 on the B cell surface.<br>3. <em>Signal Transduction and AID Induction:</em> CD40 trimerization recruits TRAF proteins, activating NF-&kappa;B and MAPK signaling pathways that directly induce transcription of the <i>AICDA</i> gene (encoding AID). In Patient 4 (X-linked Hyper-IgM Syndrome Type 1), mutant CD40L prevents this essential T-cell helper signal, leaving AID unexpressed and completely stalling class-switch recombination and somatic hypermutation.<br><br><em>Distractor Traps:</em><br>&bull; A (Catalytic Fabrication): CD40L is a transmembrane cell-surface signaling ligand of the TNF family, not a DNA endonuclease.<br>&bull; C (BCR Component Mismatch): CD40L is expressed on activated T cells, not B cells; BCR comprises membrane immunoglobulin associated with Ig&alpha; (CD79a) and Ig&beta; (CD79b).<br>&bull; D (Cytotoxic T-Cell Error): CD40L is primarily expressed on CD4+ helper T cells, not CD8+ cytotoxic T cells; its role is helper activation, not cytotoxic elimination."
    },
    {
        "q": "Which molecular mechanism is primarily responsible for introducing non-templated (N-nucleotide) additions at the junctions between D and J gene segments during heavy-chain V(D)J rearrangement?",
        "ch": [
            "Template-independent polymerase activity of terminal deoxynucleotidyl transferase (TdT)",
            "Endonucleolytic hairpin cleavage and asymmetric resolution catalyzed by Artemis protein",
            "Proofreading 3'-to-5' exonuclease activity of replicative DNA polymerases delta and epsilon",
            "Targeted cytidine deamination followed by error-prone base excision repair by UNG enzyme"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Junctional Diversity Mechanisms in Antigen Receptor Assembly]</strong><br><br>1. <em>Generation of Coding Ends:</em> RAG1/2 introduces double-strand breaks at RSS borders, generating covalently closed hairpin loops at the coding ends of gene segments.<br>2. <em>Hairpin Opening and P-Nucleotides:</em> Artemis, complexed with DNA-PKcs, cleaves the hairpin asymmetrically. If cleavage occurs off-center, it yields short single-stranded palindromic overhangs known as P-nucleotides.<br>3. <em>N-Nucleotide Addition by TdT:</em> Terminal deoxynucleotidyl transferase (TdT) is a unique template-independent DNA polymerase expressed exclusively in lymphoid progenitors during early development. Before broken ends are ligated, TdT randomly adds up to ~20 non-templated nucleotides (N-nucleotides) to the free 3'-OH ends of the cleaved heavy-chain coding junctions, vastly expanding the hypervariable CDR3 region diversity beyond the germline sequence.<br><br><em>Distractor Traps:</em><br>&bull; B (Artemis Function): Artemis opens the hairpins and generates palindromic (P) nucleotides; it is an endonuclease, not a polymerase that adds non-templated (N) nucleotides.<br>&bull; C (Proofreading Mismatch): Replicative polymerases (&delta;/&epsilon;) perform high-fidelity genome duplication during S phase; their exonuclease activity removes mismatched bases, it does not add random N-nucleotides.<br>&bull; D (AID/UNG Conflation): Cytidine deamination by AID and base excision by UNG operate during somatic hypermutation in mature germinal center B cells, not junctional diversification during initial bone marrow V(D)J rearrangement."
    },
    {
        "q": "Patient 3 has X-linked agammaglobulinemia (XLA) caused by a loss-of-function mutation in Bruton tyrosine kinase (BTK). At which developmental stage are B cells arrested in this patient?",
        "ch": [
            "During terminal differentiation of memory B lymphocytes into antibody-secreting plasma cells in organs",
            "During common lymphoid progenitor commitment to the B-cell lineage before heavy chain assembly stage",
            "At the pre-B cell stage (transition from pro-B to mature pre-B) in the fetal liver and bone marrow",
            "In peripheral germinal centers following CD40 co-stimulation and antigen challenge in the spleen"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: B-Cell Ontogeny and Pre-BCR Checkpoint Signaling]</strong><br><br>1. <em>Pre-BCR Assembly:</em> In developing pro-B cells in the bone marrow, successful V-to-DJ rearrangement produces a functional immunoglobulin &mu; heavy chain (&mu;HC). The &mu;HC pairs with surrogate light chains (VpreB and &lambda;5) and signaling dimers (Ig&alpha;/Ig&beta;) to form the pre-B cell receptor (pre-BCR) complex on the cell surface.<br>2. <em>Role of Bruton Tyrosine Kinase:</em> Pre-BCR aggregation stimulates downstream signal transduction via Bruton tyrosine kinase (BTK). BTK phosphorylation activates PLC&gamma;2, inducing calcium mobilization and transcription factors (NF-&kappa;B) that license light chain rearrangement (V-J at &kappa; or &lambda; loci) and drive clonal expansion.<br>3. <em>Pathology of XLA:</em> Without functional BTK, pre-BCR signaling fails. Developing B cells arrest irreversibly at the pre-B cell stage and undergo apoptosis. Consequently, mature B cells (CD19+/CD20+) are virtually absent in peripheral blood (<0.1%), lymphoid tissues lack germinal centers, and all serum immunoglobulin isotypes are profoundly deficient.<br><br><em>Distractor Traps:</em><br>&bull; A (Terminal Differentiation Error): Plasma cell differentiation occurs in peripheral lymphoid organs upon antigen activation; in XLA, mature B cells never develop or reach the periphery.<br>&bull; B (Early Lineage Commitment): Common lymphoid progenitors successfully commit to the B lineage and express CD19 and perform heavy-chain VDJ recombination; the developmental arrest occurs specifically at the pre-BCR transition.<br>&bull; D (Germinal Center Confusion): Germinal center arrest is characteristic of Hyper-IgM syndromes (AID or CD40L deficiency), where mature B cells exist but cannot switch or hypermutate."
    }
]
discrete_qs = [
    {
        "q": "What is the approximate isoelectric point (pI) of the tripeptide Glu-His-Ala? (Relevant pKa values: Glu alpha-COOH = 2.19, side chain = 4.25, alpha-NH3+ = 9.67; His alpha-COOH = 1.82, side chain = 6.00, alpha-NH3+ = 9.17; Ala alpha-COOH = 2.34, alpha-NH3+ = 9.69).",
        "ch": [
            "5.13",
            "6.84",
            "7.59",
            "9.43"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Isoelectric Point Determination of Oligopeptides]</strong><br><br>1. <em>Identify Ionizable Groups in the Tripeptide:</em> The tripeptide Glu-His-Ala contains four titratable functional groups:<br>- Terminal &alpha;-amino group (on Glu): pKa ~9.67<br>- Side chain &gamma;-carboxyl group (on Glu): pKa ~4.25<br>- Side chain imidazole group (on His): pKa ~6.00<br>- Terminal &alpha;-carboxyl group (on Ala): pKa ~2.34<br>(The internal peptide bonds and Ala side chain are non-titratable).<br>2. <em>Track Net Charge Across pH Transitions:</em><br>- At pH < 2.34: Net charge = +2 (terminal amino +1, imidazole +1, both carboxyls 0).<br>- At 2.34 < pH < 4.25: Terminal carboxyl deprotonates (-1); Net charge = +1.<br>- At 4.25 < pH < 6.00: Glu side chain deprotonates (-1); Net charge = 0 (neutral zwitterion).<br>- At 6.00 < pH < 9.67: His imidazole deprotonates (0); Net charge = -1.<br>- At pH > 9.67: Terminal amino deprotonates (0); Net charge = -2.<br>3. <em>Calculate pI:</em> The neutral species exists between pH 4.25 and 6.00. The isoelectric point is the arithmetic mean of the two pKa values flanking the net zero charge state: pI = (4.25 + 6.00) / 2 = 10.25 / 2 = 5.125 &asymp; 5.13.<br><br><em>Distractor Traps:</em><br>&bull; B (His-Ala Mean Trap): Averages His imidazole (6.00) and terminal amino (~9.67) erroneously, reflecting the pI of a basic peptide.<br>&bull; C (Histidine Mean Trap): Averages His side chain (6.00) and His alpha-amino (9.17), failing to recognize that internal amino groups form covalent peptide bonds.<br>&bull; D (Terminal Amino Trap): Reflects the pKa of the terminal amino group without accounting for acidic carboxylate neutralization."
    },
    {
        "q": "A native 200-kDa homotetrameric cytosolic enzyme is stabilized exclusively by intermolecular disulfide bonds between four identical 50-kDa monomers. When analyzed by SDS-PAGE under reducing versus non-reducing conditions, what band pattern will appear?",
        "ch": [
            "Reducing: four separate bands at 50, 100, 150, 200 kDa; Non-reducing: a single band",
            "Reducing: a single sharp 50 kDa band; Non-reducing: a single intact 200 kDa band",
            "Reducing: a single intact 200 kDa band; Non-reducing: a single sharp 50 kDa band",
            "Reducing: two distinct bands at 100 kDa; Non-reducing: a single intact 200 kDa band"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Principles of SDS-PAGE Under Reducing vs Non-Reducing Conditions]</strong><br><br>1. <em>Protein Architecture:</em> The protein is a homotetramer (four identical subunits, each 200 kDa / 4 = 50 kDa). Crucially, the subunits are covalently cross-linked to one another by intermolecular disulfide bonds.<br>2. <em>Non-Reducing SDS-PAGE:</em> SDS denatures the protein and coats it with a uniform negative charge-to-mass ratio, but SDS alone cannot cleave covalent disulfide bonds. Because the four subunits remain covalently joined by disulfides, the intact complex migrates as a single, intact 200-kDa multimer.<br>3. <em>Reducing SDS-PAGE:</em> Adding a reducing agent such as &beta;-mercaptoethanol (&beta;-ME) or dithiothreitol (DTT) reduces all covalent disulfide bridges (-S-S-) to free sulfhydryl groups (-SH). This dissociates the homotetramer into its four individual, identical 50-kDa monomeric subunits. Because all four monomers possess identical molecular weight (50 kDa), they migrate together to form a single sharp band at 50 kDa.<br><br><em>Distractor Traps:</em><br>&bull; A (Degradation Artifact Fallacy): Homotetramers dissociate into identical monomers; reducing conditions do not generate an anomalous ladder of partial assembly intermediates.<br>&bull; C (Reversal Error): Reverses reducing and non-reducing conditions, forgetting that reducing agents cleave disulfides to liberate smaller subunits.<br>&bull; D (Heterodimer Misclassification): Assumes the tetramer consists of disulfide-linked dimers that resist reduction, which contradicts complete disulfide reduction."
    },
    {
        "q": "In a human population in Hardy-Weinberg equilibrium, an autosomal recessive inborn error of metabolism affects 1 in 10,000 live births (q\u00b2 = 0.0001). What fraction of the population are asymptomatic heterozygous carriers (2pq) of the mutant allele?",
        "ch": [
            "0.0001 (1 in 10,000)",
            "0.0002 (1 in 5,000)",
            "0.0198 (1 in 50)",
            "0.0400 (1 in 25)"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Hardy-Weinberg Equilibrium and Population Genetics]</strong><br><br>1. <em>Determine Recessive Allele Frequency (q):</em> The frequency of affected homozygous recessive individuals is q2 = 1 / 10,000 = 0.0001. Taking the square root: q = &radic;0.0001 = 0.01.<br>2. <em>Determine Dominant Allele Frequency (p):</em> Because p + q = 1, p = 1 - 0.01 = 0.99.<br>3. <em>Calculate Carrier Frequency (2pq):</em> Heterozygous carriers are represented by 2pq = 2 &times; (0.99) &times; (0.01) = 0.0198 (approximately 2%, or 1 in 50 individuals). In rare recessive diseases, asymptomatic heterozygous carriers vastly outnumber affected homozygotes (here, 198 carriers for every 1 affected individual).<br><br><em>Distractor Traps:</em><br>&bull; A (Affected Frequency Trap): Confuses carrier frequency (2pq) with the homozygous recessive disease incidence (q2 = 0.0001).<br>&bull; B (Allele Frequency Doubling Trap): Multiplies q by 2 without including the dominant allele term (2q instead of 2pq), or assumes 2 &times; q2.<br>&bull; D (Squaring Inversion Trap): Erroneously calculates 4pq or doubles 2pq."
    },
    {
        "q": "Which tissue pair is correctly matched to its embryonic germ layer of origin during vertebrate gastrulation and organogenesis?",
        "ch": [
            "Adrenal medulla derived from endoderm; Adrenal cortex derived from ectoderm",
            "Thyroid follicular cells from mesoderm; Adrenal medulla from endoderm layer",
            "Pancreatic beta-islets from ectoderm; Spleen derived from endoderm tissues",
            "Adrenal medulla from ectoderm (neural crest); Adrenal cortex from mesoderm"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Embryonic Germ Layer Derivation and Organogenesis]</strong><br><br>1. <em>Germ Layer Lineages:</em> During gastrulation, the inner cell mass differentiates into three primary germ layers: ectoderm, mesoderm, and endoderm.<br>2. <em>Adrenal Gland Dual Derivation:</em> The adrenal gland possesses a dual embryonic origin that mirrors its neuroendocrine function:<br>- <em>Adrenal Medulla:</em> Arises from neural crest cells (specialized multipotent cells derived from the embryonic ectoderm). Chromaffin cells are modified postganglionic sympathetic neurons that secrete catecholamines.<br>- <em>Adrenal Cortex:</em> Arises from intermediate/coelomic mesoderm. Cortical cells produce steroid hormones (cortisol, aldosterone, androgens).<br>3. <em>Eliminate Other Errors:</em> Thyroid follicular cells and pancreatic islet cells are endodermal; the spleen is mesodermal.<br><br><em>Distractor Traps:</em><br>&bull; A (Complete Inversion): Reverses the germ layers and misassigns the cortex to ectoderm and medulla to endoderm.<br>&bull; B (Thyroid Mismatch): Thyroid follicular cells originate from the primitive endodermal pharyngeal floor, not mesoderm.<br>&bull; C (Endocrine Visceral Inversion): Pancreatic islets are endodermal (foregut budding), while the spleen is of mesenchymal (mesodermal) origin."
    },
    {
        "q": "A woman diagnosed with mitochondrial encephalomyopathy (MERRF syndrome, caused by a point mutation in mitochondrial tRNALys) has children with an unaffected, genotypically normal male. What is the expected inheritance outcome among their four offspring (two sons, two daughters)?",
        "ch": [
            "All four children inherit the maternal mitochondrial mutation and risk developing clinical symptoms",
            "Only the two daughters will inherit the mutation, whereas both sons will remain completely unaffected here",
            "Only the two sons will inherit the mutation via non-recombining holandric Y-chromosome transmission line",
            "Fifty percent of the children will inherit the mutation following typical Mendelian dominant genetics"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Non-Mendelian Maternal Extranuclear Inheritance and Mitochondrial Heteroplasmy]</strong><br><br>1. <em>Maternal Inheritance of mtDNA:</em> In human fertilization, the ovum contributes virtually all cytoplasm, organelles, and mitochondrial DNA (mtDNA, ~100,000 copies) to the zygote. Sperm mitochondria localized in the midpiece are targeted for ubiquitin-mediated proteolysis and autophagy upon entering the egg.<br>2. <em>Transmission to Offspring:</em> An affected homoplasmic or heteroplasmic female transmits mutant mtDNA to 100% of her progeny, regardless of the biological sex of the offspring.<br>3. <em>Phenotypic Manifestation:</em> Both sons and daughters inherit the disease allele. Although phenotypic severity may vary among offspring due to mitochondrial heteroplasmy (the proportion of mutant vs wild-type mitochondria partitioned into each blastomere during cleavage), all four children inherit the maternal mitochondrial mutation.<br><br><em>Distractor Traps:</em><br>&bull; B (Sex-Linked Misapplication): Mitochondrial inheritance is maternal, but it affects BOTH male and female offspring equally; daughters pass it to the next generation, while sons do not.<br>&bull; C (Y-Linked Distractor): Extranuclear mitochondrial DNA is located in the cytoplasm, not on the paternal Y chromosome.<br>&bull; D (Mendelian Assumption): Mitochondrial inheritance does not follow Mendelian ratios (e.g., 50% segregation) because mitochondria are distributed stochastically via cytoplasmic partitioning during cytokinesis."
    },
    {
        "q": "Which physiological feature correctly distinguishes the mechanism of action of peptide hormones (e.g., insulin, glucagon) from that of steroid hormones (e.g., cortisol, aldosterone)?",
        "ch": [
            "Peptide hormones are lipophilic and cross the plasma membrane to bind nuclear transcription factors in cell",
            "Peptide hormones act via cell-surface receptors and second messengers, while steroids alter expression",
            "Steroid hormones circulate freely dissolved in plasma, whereas peptide hormones require carrier globulins",
            "Peptide hormones are synthesized directly from cholesterol, whereas steroid hormones translate from mRNA"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Endocrine Signaling Mechanisms and Chemical Classes of Hormones]</strong><br><br>1. <em>Biophysical Nature:</em> Peptide hormones are hydrophilic and lipophobic; they cannot cross the hydrophobic lipid bilayer of target cells. Steroid hormones are lipophilic derivatives of cholesterol; they readily diffuse through plasma membranes.<br>2. <em>Peptide Hormone Signaling:</em> Peptide hormones bind extracellular ligand-binding domains of cell-surface transmembrane receptors (GPCRs, RTKs). This triggers rapid second-messenger cascades (cAMP, IP3/DAG, kinase phosphorylation cascades) that modify existing protein activity within seconds to minutes.<br>3. <em>Steroid Hormone Signaling:</em> Steroid hormones bind intracellular or nuclear receptors (zinc-finger transcription factors). The hormone-receptor complex dimerizes, translocates to the nucleus, and binds hormone response elements (HREs) on genomic DNA to modulate transcription and de novo protein synthesis, exerting biological effects over a prolonged timescale (hours to days).<br><br><em>Distractor Traps:</em><br>&bull; A (Complete Mechanism Inversion): Reverses the mechanisms of peptide and steroid hormones.<br>&bull; C (Plasma Transport Inversion): Hydrophilic peptide hormones dissolve freely in aqueous plasma; lipophilic steroids require carrier proteins (e.g., albumin, cortisol-binding globulin).<br>&bull; D (Biosynthetic Inversion): Steroids derive from cholesterol; peptide hormones are encoded by genes and translated from mRNA on ribosomes."
    },
    {
        "q": "Hemoglobin exhibits an oxygen-binding Hill coefficient (nH) of approximately 2.8 to 3.0, whereas myoglobin exhibits a Hill coefficient of nH = 1.0. What biophysical property does this disparity demonstrate?",
        "ch": [
            "Hemoglobin has a significantly higher overall affinity for oxygen across all physiological tissue pO2 values",
            "Hemoglobin exhibits negative cooperativity, meaning oxygen binding promotes rapid subunit disassembly in cells",
            "Hemoglobin displays positive cooperativity, where O2 binding at one subunit increases affinity elsewhere",
            "Myoglobin contains four cooperative heme groups, whereas hemoglobin binds O2 through a single porphyrin ring"
        ],
        "a": 2,
        "e": "<strong>[Governing Principle: Cooperativity and Allosteric Transitions in Oxygen-Binding Globins]</strong><br><br>1. <em>Definition of Hill Coefficient:</em> The Hill coefficient (nH) quantifies cooperative ligand binding: nH = 1 indicates non-cooperative, independent binding; nH > 1 indicates positive cooperativity; nH < 1 indicates negative cooperativity.<br>2. <em>Hemoglobin vs Myoglobin Architecture:</em> Myoglobin is a monomer containing a single heme group; binding of O2 to one molecule cannot influence another (nH = 1.0, generating a hyperbolic binding curve). Hemoglobin is a tetramer (&alpha;2&beta;2) containing four distinct heme binding sites.<br>3. <em>Mechanism of Positive Cooperativity:</em> Hemoglobin exists in an equilibrium between a low-affinity T (tense) state and a high-affinity R (relaxed) state. Binding of O2 to the Fe2+ of one heme pulls the iron into the porphyrin plane, which tugs the proximal histidine (F8) and shifts the &alpha;&beta; subunit interface. This conformational change relaxes the remaining subunits into the R-state, dramatically increasing their oxygen affinity. This positive cooperativity yields nH &asymp; 2.8 to 3.0 and produces the classic sigmoidal oxygen-binding curve essential for oxygen loading in lungs and offloading in tissues.<br><br><em>Distractor Traps:</em><br>&bull; A (Affinity Comparison Error): Myoglobin has a far HIGHER affinity for oxygen (P50 ~2-3 mmHg) than hemoglobin (P50 ~26 mmHg), ensuring myoglobin can extract O2 from hemoglobin in capillaries.<br>&bull; B (Negative Cooperativity Fallacy): nH > 1 indicates positive cooperativity, not negative; oxygen binding stabilizes the tetramer, it does not cause disassembly.<br>&bull; D (Structural Reversal): Myoglobin is a monomer with ONE heme; hemoglobin is a tetramer with FOUR hemes."
    },
    {
        "q": "A clinical pharmacologist measures the renal clearances of three markers: Inulin (125 mL/min), Glucose (0 mL/min), and Para-aminohippurate (PAH, 650 mL/min). Based on these values, how is PAH processed by the nephron?",
        "ch": [
            "PAH undergoes freely filtered glomerular loading followed by extensive passive tubular reabsorption",
            "PAH undergoes glomerular filtration alone, making its clearance equal to the glomerular filtration rate",
            "PAH is completely excluded from the glomerular ultrafiltrate and cleared via hepatic cytochrome P450",
            "PAH undergoes filtration and active tubular secretion, making clearance equal to renal plasma flow"
        ],
        "a": 3,
        "e": "<strong>[Governing Principle: Renal Clearance Mechanics and Quantification of Nephron Handling]</strong><br><br>1. <em>Reference Clearances:</em> Renal clearance is defined as C = (U &times; V) / P.<br>- <em>Inulin (C = 125 mL/min):</em> Freely filtered and neither reabsorbed nor secreted; its clearance equals the Glomerular Filtration Rate (GFR).<br>- <em>Glucose (C = 0 mL/min):</em> Freely filtered but completely reabsorbed along the proximal tubule; clearance < GFR indicates net reabsorption.<br>2. <em>Handling of PAH (C = 650 mL/min):</em> Clearance of PAH (650 mL/min) is over 5-fold greater than GFR (125 mL/min). This massive clearance disparity proves that PAH is filtered at the glomerulus AND actively secreted from peritubular capillaries into the tubular lumen by organic anion transporters (OAT1/3).<br>3. <em>Physiological Signification:</em> Because nearly 100% of PAH entering the renal circulation is cleared in a single pass through the kidneys (filtration + secretion), PAH clearance serves as the clinical gold standard for measuring Effective Renal Plasma Flow (ERPF).<br><br><em>Distractor Traps:</em><br>&bull; A (Reabsorption Trap): Net tubular reabsorption results in clearance LOWER than GFR (as seen with glucose, urea, and sodium); PAH clearance is 5 times higher than GFR.<br>&bull; B (Inulin Conflation): Filtration alone with zero net transport defines inulin (GFR ~125 mL/min), not PAH.<br>&bull; C (Hepatic Misconception): PAH is cleared almost exclusively by the kidneys; its high renal clearance reflects rapid renal excretion, not hepatic metabolism."
    },
    {
        "q": "On a Lineweaver-Burk double-reciprocal plot (1/v versus 1/[S]), an uncompetitive enzyme inhibitor will produce a line that:",
        "ch": [
            "is parallel to the uninhibited line, exhibiting an identical slope but elevated y- and x-intercepts",
            "intersects the uninhibited line directly on the y-axis, exhibiting identical 1/Vmax with steeper slope",
            "intersects the uninhibited line directly on the negative x-axis, exhibiting identical apparent Km values",
            "pivots around a common point in the fourth quadrant, altering both slope and intercepts inversely"
        ],
        "a": 0,
        "e": "<strong>[Governing Principle: Double-Reciprocal Lineweaver-Burk Analysis of Enzyme Inhibition]</strong><br><br>1. <em>Lineweaver-Burk Equation:</em> 1/v = (Km / Vmax) &times; (1/[S]) + (1/Vmax). The slope is Km / Vmax, the y-intercept is 1/Vmax, and the x-intercept is -1/Km.<br>2. <em>Uncompetitive Inhibition Mechanism:</em> An uncompetitive inhibitor binds exclusively to the enzyme-substrate (ES) complex (not the free enzyme). By sequestering ES into inactive ESI, Le Chatelier's principle drives more free E to bind S, which increases apparent substrate affinity (decreasing apparent Km). Concurrently, catalytically active ES is depleted, which proportionally decreases Vmax.<br>3. <em>Mathematical Consequences:</em> Because both Vmax and Km are reduced by the identical factor &alpha;' (Vmax,app = Vmax / &alpha;' and Km,app = Km / &alpha;'), the slope of the line (Km,app / Vmax,app = Km / Vmax) remains completely unchanged. Both 1/Vmax (y-intercept) and -1/Km (x-intercept) increase by &alpha;', generating a series of strictly parallel lines shifted upward and leftward on the plot.<br><br><em>Distractor Traps:</em><br>&bull; B (Competitive Signature): Intersecting on the y-axis (same 1/Vmax) with an increased slope is the hallmark of competitive inhibition.<br>&bull; C (Noncompetitive Signature): Intersecting on the negative x-axis (same -1/Km) with a higher y-intercept defines pure noncompetitive inhibition.<br>&bull; D (Mixed Inhibition Confusion): Lines that intersect in the second or third quadrant represent mixed inhibition; lines do not intersect in the fourth quadrant in standard enzyme kinetics."
    },
    {
        "q": "Which structural feature is essential for initiating cap-dependent translation of eukaryotic mRNAs, but is completely ABSENT in prokaryotic mRNAs?",
        "ch": [
            "A purine-rich Shine-Dalgarno consensus motif located upstream of the translation initiation codon in mRNA",
            "A 5' 7-methylguanosine (m7G) triphosphate cap recognized by the eIF4E eukaryotic initiation factor",
            "A polycistronic operon organization that translates multiple distinct open reading frames simultaneously",
            "A formylmethionine (fMet) moiety loaded onto initiator tRNA that pairs with the AUG start codon in cells"
        ],
        "a": 1,
        "e": "<strong>[Governing Principle: Comparative Molecular Biology of Translation Initiation]</strong><br><br>1. <em>Eukaryotic Translation Initiation Architecture:</em> During post-transcriptional processing in the eukaryotic nucleus, RNA guanylyltransferase and (guanine-N7)-methyltransferase add an inverted 7-methylguanosine cap linked via an unusual 5'-to-5' triphosphate bridge (m7GpppN) to the 5' end of the pre-mRNA.<br>2. <em>Recognition Mechanism:</em> In the cytoplasm, the eukaryotic initiation factor 4F complex (eIF4F), specifically the cap-binding subunit eIF4E, recognizes this m7G cap. This recruits the 43S pre-initiation complex (including the 40S ribosomal subunit) to scan the 5' UTR linearly until encountering the optimal start codon in a Kozak consensus sequence.<br>3. <em>Prokaryotic Architecture:</em> Prokaryotes do not possess an m7G cap. Instead, the 16S rRNA within the 30S ribosomal subunit directly base-pairs with a purine-rich Shine-Dalgarno consensus sequence (5'-AGGAGG-3') located 8-10 nucleotides upstream of the start codon. In addition, prokaryotes use N-formylmethionine (fMet) and frequent polycistronic transcripts.<br><br><em>Distractor Traps:</em><br>&bull; A (Prokaryotic Inversion): The Shine-Dalgarno sequence is the hallmark of prokaryotic translation initiation, not eukaryotic.<br>&bull; C (Prokaryotic Gene Organization): Polycistronic operons are characteristic of bacteria (prokaryotes); eukaryotic nuclear mRNAs are almost exclusively monocistronic.<br>&bull; D (Prokaryotic Initiator Residue): N-formylmethionine (fMet) is used exclusively by prokaryotes, mitochondria, and chloroplasts; eukaryotic cytosolic translation utilizes unformylated methionine (Met)."
    }
]

if __name__ == "__main__":
    validate_questions(p5_qs, 25)
    validate_questions(p6_qs, 31)
    validate_questions(p7_qs, 37)
    validate_questions(discrete_qs, 43)
    print("ALL PASSAGES 5 TO 8 QUESTIONS VALIDATED 100% PERFECTLY!")
