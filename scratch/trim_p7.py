with open("/home/cgslinde/DrillRoom/DrillRoom/scratch/p7.py", "r") as f:
    code = f.read()

old_p1 = """<p>The fidelity and efficiency of translation depend on two molecular checkpoints: the structural degeneracy of codon-anticodon pairing governed by the wobble hypothesis, and the enzymatic proofreading executed by aminoacyl-tRNA synthetases (aaRS). The standard genetic code contains 64 trinucleotide codons; 61 specify the 20 canonical amino acids, while 3 function as termination signals. However, human cells maintain only 48 distinct transfer RNA (tRNA) species, demonstrating that individual tRNAs must translate multiple synonymous codons.</p>"""

new_p1 = """<p>Ribosomal translation fidelity relies on two molecular mechanisms: the structural degeneracy of codon-anticodon pairing governed by the wobble hypothesis, and enzymatic proofreading by aminoacyl-tRNA synthetases (aaRS). While 61 sense codons specify the 20 canonical amino acids, human cells maintain only 48 distinct transfer RNA (tRNA) species, demonstrating that individual tRNAs decode multiple synonymous codons.</p>"""

code = code.replace(old_p1, new_p1)

with open("/home/cgslinde/DrillRoom/DrillRoom/scratch/p7.py", "w") as f:
    f.write(code)

print("Trimmed P7")
