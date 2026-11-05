# Passage 1: Topic 506 — Parathyroid Hormone (PTH), Calcitonin & Calcitriol Calcium Triad
# Answer keys: 1, 0, 2, 3, 0, 1

p1_data = {
    "id": "exam_bb90_3_p1",
    "sec": "B/B",
    "topic": "Parathyroid Hormone (PTH), Calcitonin & Calcitriol Calcium Triad",
    "sheet": 1,
    "label": "Biological and Biochemical Foundations of Living Systems",
    "examId": "bb90_3",
    "passage": """<div class=\"ttl\">Passage 1 (Questions 1&ndash;6)</div>
<p>Calcium ($\text{Ca}^{2+}$) and inorganic phosphate ($\text{P}_i$) balance is tightly regulated by parathyroid hormone (PTH), calcitriol ($1,25\text{-dihydroxyvitamin D}_3$), and calcitonin. Parathyroid gland chief cells express cell-surface calcium-sensing receptors (CaSR), which are G-protein coupled receptors ($G_{q/11}$ and $G_i$) that detect ionized extracellular calcium ($[\text{Ca}^{2+}]_e$). Hypocalcemia decreases CaSR activation, disinhibiting preformed PTH vesicle exocytosis into the circulation.</p>
<p>PTH acts directly on two principal target organs: bone and kidney. In renal proximal convoluted tubules, PTH binds its G-protein coupled receptor (PTHR1), stimulating adenylyl cyclase to generate cyclic AMP (cAMP). This initiates downstream protein kinase A (PKA) phosphorylation of the sodium-phosphate cotransporter NaPi-IIa, triggering its endocytosis and lysosomal degradation, resulting in phosphaturia. Concurrently, PTH upregulates 25-hydroxyvitamin D $1\alpha$-hydroxylase (CYP27B1) in proximal tubular mitochondria, converting 25-hydroxyvitamin D into active calcitriol. In distal convoluted tubules, PTH enhances $\text{Ca}^{2+}$ reabsorption via apical TRPV5 channels and basolateral $\text{Na}^+/\text{Ca}^{2+}$ exchangers (NCX1).</p>
<p>In skeletal tissue, mature osteoclasts lack PTH receptors. Instead, PTH binds osteoblasts and osteocytes, stimulating the expression of receptor activator of nuclear factor-$\kappa\text{B}$ ligand (RANKL) while suppressing osteoprotegerin (OPG), a soluble decoy receptor that neutralizes RANKL. Membrane-bound RANKL binds RANK on pre-osteoclast membranes, promoting osteoclast differentiation and ruffled border acid secretion, releasing $\text{Ca}^{2+}$ and $\text{HPO}_4^{2-}$ into the extracellular fluid.</p>
<p>To delineate the autonomous renal and skeletal contributions of PTH signaling, investigators infused recombinant continuous PTH(1-34) (10 nmol/kg/day for 72 hours) into wild-type mice, osteoblast-specific PTHR1 conditional knockout mice ($PTHR1^{\Delta\text{ob}}$), and wild-type mice co-treated with recombinant OPG-Fc. Baseline and post-infusion serum and urinary parameters are recorded in Table 1.</p>
<table class=\"tbl\">
  <caption>Table 1 Serum and urinary parameters following 72-hour continuous PTH(1-34) infusion</caption>
  <thead>
    <tr><th>Cohort</th><th>Treatment</th><th>Serum Ionized $\text{Ca}^{2+}$ (mM)</th><th>Serum Phosphate (mM)</th><th>Urinary cAMP ($\text{nmol}/\text{mg creatinine}$)</th><th>Osteoclast Surface per Bone Surface (%)</th></tr>
  </thead>
  <tbody>
    <tr><td>Wild-Type</td><td>Vehicle</td><td>1.24</td><td>2.10</td><td>18</td><td>4.2%</td></tr>
    <tr><td>Wild-Type</td><td>PTH(1-34)</td><td>1.68</td><td>1.15</td><td>86</td><td>16.8%</td></tr>
    <tr><td>$PTHR1^{\Delta\text{ob}}$</td><td>Vehicle</td><td>1.22</td><td>2.08</td><td>17</td><td>3.9%</td></tr>
    <tr><td>$PTHR1^{\Delta\text{ob}}$</td><td>PTH(1-34)</td><td>1.34</td><td>1.18</td><td>84</td><td>4.1%</td></tr>
    <tr><td>Wild-Type</td><td>PTH + OPG-Fc</td><td>1.32</td><td>1.14</td><td>85</td><td>3.8%</td></tr>
  </tbody>
</table>
<p>In response to acute hypercalcemia, thyroid parafollicular C-cells secrete calcitonin, which directly binds calcitonin receptors on mature osteoclasts to rapidly inhibit osteoclast motility and ruffled border bone resorption, antagonizing PTH action.</p>""",
    "qs": [
        {
            "q": "Why does osteoclast surface area remain unchanged following continuous PTH infusion in PTHR1-delta-ob mice compared to wild-type mice (Table 1)?",
            "ch": [
                "Osteoclasts require direct Gs-mediated activation by PTH receptors on their ruffled borders.",
                "Osteoclast differentiation requires osteoblast PTHR1 activation to stimulate RANKL expression.",
                "Absence of osteoblast PTHR1 prevents the renal hydroxylation of calcidiol into calcitriol.",
                "The knockout of osteoblast PTHR1 causes constitutive osteoprotegerin gene overexpression."
            ],
            "a": 1,
            "e": "<strong>Osteoclast differentiation via osteoblast RANKL signaling:</strong> As described in the passage, mature osteoclasts and pre-osteoclasts lack PTH receptors. PTH induces bone mineral resorption indirectly by binding PTHR1 on osteoblasts and osteocytes, which upregulates membrane-bound RANKL and downregulates osteoprotegerin (OPG). RANKL then binds RANK on pre-osteoclasts to drive osteoclastogenesis. In $PTHR1^{\\Delta\\text{ob}}$ mice, osteoblasts lack the receptor and cannot respond to PTH, so RANKL is not upregulated, and osteoclast surface area remains at baseline ($4.1\\%$ vs $16.8\\%$ in wild-type).<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because mature osteoclasts do not express functional PTH receptors; PTH acts indirectly through osteoblasts.<br>&bull; C is incorrect because renal $1\\alpha$-hydroxylase (CYP27B1) is expressed in renal proximal tubular cells, not osteoblasts, and Table 1 shows renal PTH signaling remains fully intact.<br>&bull; D is incorrect because osteoblast PTHR1 knockout does not constitutively overexpress OPG; rather, it abolishes the PTH-mediated suppression of OPG and induction of RANKL."
        },
        {
            "q": "PTH infusion markedly increased urinary cAMP excretion and lowered serum phosphate equally in both wild-type and PTHR1-delta-ob mice (Table 1). What explains this finding?",
            "ch": [
                "PTH acts directly on intact renal proximal tubule PTHR1 receptors coupled to adenylyl cyclase.",
                "Calcitonin released from thyroid C-cells stimulates renal cAMP generation and phosphate loss.",
                "Intestinal calcium transporters generate urinary cAMP via calcitriol-dependent exocytosis.",
                "Circulating OPG-Fc binds renal tubular apical membranes to trigger basolateral phosphate flux."
            ],
            "a": 0,
            "e": "<strong>Renal PTH signaling mechanism:</strong> The genetic knockout in $PTHR1^{\\Delta\\text{ob}}$ mice is osteoblast-specific, leaving renal tubular PTHR1 receptors entirely intact and fully functional. Circulating PTH binds basolateral PTHR1 on proximal tubule epithelial cells, activating $G_{\\alpha s}$ and stimulating adenylyl cyclase to generate intracellular cyclic AMP (cAMP). Intracellular cAMP is extruded into the tubular lumen, causing nephrogenous urinary cAMP to rise sharply ($86$ and $84\\;\\text{nmol/mg creatinine}$). Downstream PKA activation triggers endocytosis of apical NaPi-IIa cotransporters, causing identical phosphaturia and lowering serum phosphate to $\\sim 1.15\\text{--}1.18\\;\\text{mM}$.<br><br><em>Distractor Traps:</em><br>&bull; B reverses endocrine roles: calcitonin lowers serum calcium and does not mediate PTH's phosphaturic renal actions.<br>&bull; C invents intestinal generation of urinary cAMP.<br>&bull; D is incorrect because OPG-Fc was administered only to Group 5, not Group 4 ($PTHR1^{\\Delta\\text{ob}}$), and OPG is a decoy receptor for RANKL, not a renal transport ligand."
        },
        {
            "q": "How does active calcitriol (1,25-dihydroxyvitamin D3) participate in homeostatic negative feedback regulation within the parathyroid-calcium axis?",
            "ch": [
                "It activates basolateral calcium pumps in osteoclasts to directly inhibit bone demineralization.",
                "It competitively inhibits extracellular calcium-sensing receptors to promote parathyroid growth.",
                "It binds nuclear VDR in parathyroid chief cells to suppress transcription of the prepro-PTH gene.",
                "It allosterically activates proximal tubular CYP27B1 while suppressing 24-hydroxylase synthesis."
            ],
            "a": 2,
            "e": "<strong>Calcitriol negative feedback on parathyroid gland:</strong> Active calcitriol ($1,25(\\text{OH})_2\\text{D}_3$) binds the nuclear Vitamin D Receptor (VDR), which heterodimerizes with the retinoid X receptor (RXR). In parathyroid chief cells, the VDR-RXR complex binds vitamin D response elements (VDREs) in the promoter region of the prepro-PTH gene, directly suppressing PTH transcription and inhibiting parathyroid gland proliferation. Calcitriol also exerts negative feedback in the kidney by downregulating CYP27B1 ($1\\alpha$-hydroxylase) and upregulating CYP24A1 ($24$-hydroxylase) to promote its own catabolic clearance.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because calcitriol promotes bone resorption in conjunction with PTH rather than inhibiting osteoclasts.<br>&bull; B is incorrect because calcitriol sensitizes rather than competitively inhibits CaSR, and it suppresses rather than promotes parathyroid hyperplasia.<br>&bull; D states the exact opposite: calcitriol suppresses CYP27B1 and induces CYP24A1."
        },
        {
            "q": "Which molecular mechanism accounts for the profound reduction in serum phosphate concentration observed after continuous PTH administration (Table 1)?",
            "ch": [
                "Upregulation of basolateral phosphate antiporters in the medullary collecting duct epithelium",
                "Precipitation of insoluble calcium phosphate crystals within the hepatic parenchymal sinusoids",
                "Direct inhibition of brush-border alkaline phosphatase in the terminal ileal enterocyte villi",
                "Downregulation and lysosomal degradation of NaPi-IIa cotransporters in proximal renal tubules"
            ],
            "a": 3,
            "e": "<strong>Mechanism of PTH-induced phosphaturia:</strong> In the renal proximal convoluted tubule, inorganic phosphate reabsorption across the apical brush border membrane is mediated by sodium-phosphate cotransporters, predominantly NaPi-IIa (SLC34A1). PTH binding to PTHR1 activates PKA and PKC cascades that phosphorylate NaPi-IIa, stimulating its retrieval from the apical membrane via clathrin-coated vesicles and directing it to lysosomes for proteolytic degradation. The loss of apical NaPi-IIa decreases proximal tubular phosphate reabsorption, causing robust urinary phosphate excretion (phosphaturia) and decreasing serum phosphate from $2.10$ to $1.15\\;\\text{mM}$.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because phosphate handling occurs predominantly in the proximal convoluted tubule, not the medullary collecting duct.<br>&bull; B describes metastatic calcification, which occurs when the calcium-phosphate solubility product exceeds normal limits, not a regulated transport response.<br>&bull; C is incorrect because brush-border alkaline phosphatase cleaves organic phosphate esters, but its inhibition is not the mechanism of PTH-driven systemic phosphaturia."
        },
        {
            "q": "Under conditions of acute hypercalcemia, how does calcitonin rapidly lower circulating ionized calcium levels to antagonize the actions of PTH?",
            "ch": [
                "It binds receptors on mature osteoclasts to inhibit ruffled border motility and acid secretion.",
                "It binds parathyroid chief cell receptors to stimulate the rapid exocytosis of stored PTH pools.",
                "It upregulates the renal mitochondrial 1-alpha-hydroxylase enzyme to accelerate bone turnover.",
                "It promotes the nuclear translocation of osteoblast RANKL to sequester circulating calcium ions."
            ],
            "a": 0,
            "e": "<strong>Calcitonin physiology and osteoclast inhibition:</strong> Secreted by thyroid parafollicular C-cells in response to high ionized calcium ($[\\text{Ca}^{2+}]_e$), calcitonin binds G-protein coupled calcitonin receptors expressed directly on mature osteoclasts. Calcitonin signaling increases intracellular cAMP, causing rapid retraction of the osteoclast ruffled border, cessation of osteoclast pseudopodial motility, and inhibition of vacuolar $H^+$-ATPase proton extrusion and cathepsin K release. This shuts down bone mineral resorption within minutes, lowering circulating calcium.<br><br><em>Distractor Traps:</em><br>&bull; B describes stimulation of PTH release, which would worsen hypercalcemia and is the exact opposite of homeostatic feedback.<br>&bull; C is incorrect because calcitonin inhibits rather than stimulates renal $1\\alpha$-hydroxylase.<br>&bull; D is incorrect because RANKL is a membrane-bound ligand that stimulates osteoclasts, not an intracellular ion-sequestering protein."
        },
        {
            "q": "A patient experiencing acute hyperventilation develops respiratory alkalosis (arterial pH = 7.58). Why does this patient exhibit neuromuscular tetany despite normal total serum calcium?",
            "ch": [
                "Alkalemia causes renal proximal tubules to excrete ionized calcium while retaining serum albumin.",
                "Plasma proton loss causes albumin carboxyl groups to deprotonate, increasing ionized Ca2+ binding.",
                "Elevated extracellular pH activates parathyroid chief cells to degrade circulating PTH peptides.",
                "Systemic alkalosis prevents skeletal muscle voltage-gated sodium channels from inactivating."
            ],
            "a": 1,
            "e": "<strong>Serum calcium partitioning and pH-dependent albumin binding:</strong> Total serum calcium consists of three fractions: protein-bound ($\\sim 40\\%$, predominantly to albumin), anion-complexed ($\\sim 15\\%$, to phosphate and citrate), and free ionized $\\text{Ca}^{2+}$ ($\\sim 45\\%$, the biologically active form). Albumin possesses numerous carboxylate-containing side chains (Asp and Glu) that bind both protons ($H^+$) and $\\text{Ca}^{2+}$. In acute respiratory alkalosis, the extracellular proton concentration drops sharply. As protons dissociate from albumin carboxyl groups to buffer the alkalemia, more negatively charged binding sites become available, binding free ionized $\\text{Ca}^{2+}$. This precipitous drop in free ionized $[\\text{Ca}^{2+}]$ lowers the threshold for neuronal voltage-gated $\\text{Na}^+$ channel opening, causing neuromuscular hyperexcitability and carpopedal tetany (Trousseau's and Chvostek's signs) despite completely normal total serum calcium.<br><br><em>Distractor Traps:</em><br>&bull; A is incorrect because acute tetany is mediated by altered protein binding in plasma, not renal tubular calcium wasting.<br>&bull; C is incorrect because hypocalcemia stimulates parathyroid chief cells, and PTH is not degraded by plasma pH shifts.<br>&bull; D confuses the primary cause: hypocalcemia shifts the activation threshold of sodium channels toward resting potential, rather than preventing inactivation directly via alkalosis."
        }
    ]
}
