with open("/home/cgslinde/DrillRoom/DrillRoom/scratch/p5.py", "r") as f:
    text = f.read()

# Let's replace the whole "e" for Q28
old_e_target = text[text.find('"<strong>Calculation of incomplete penetrance'):]
old_e_target = old_e_target[:old_e_target.find('"\n    }')]

new_e = """<strong>Calculation of incomplete penetrance under environmental modification (Topic 621):</strong> In a testcross between a heterozygous female ($N / n$) and a homozygous recessive male ($n / n$), Mendelian segregation dictates that exactly half (50%) of all gametes receive the dominant $N$ allele. Across the 1,000 total testcross progeny scored at 30 &deg;C, exactly 500 individuals inherited the $N$ allele from the mother, comprising 287 + 123 = 410 in Class 1; 42 + 18 = 60 in Class 3; 18 + 7 = 25 in Class 5; and 3 + 2 = 5 in Class 7. Total $N$ carriers = 410 + 60 + 25 + 5 = 500. Of these 500 carriers, those manifesting neurocutaneous lesions are 287 + 42 + 18 + 3 = 350, while 123 + 18 + 7 + 2 = 150 are non-penetrant carriers. To calculate penetrance:<br>$$\\text{Penetrance} = \\frac{\\text{Number of Genotype Carriers Exhibiting Phenotype}}{\\text{Total Number of Individuals Carrying Genotype}} \\times 100\\%$$<br>$$\\text{Penetrance} = \\frac{350}{500} \\times 100\\% = 70.0\\%$$<br><em>Distractor Traps:</em><br>&bull; A describes 100% penetrance, which was present at 22 &deg;C but lost under thermal stress at 30 &deg;C.<br>&bull; B is a mathematical distractor trap that confuses total progeny with genotype carriers.<br>&bull; C is an incorrect calculation that fails to account for the non-penetrant carrier class."""

text = text.replace(old_e_target, new_e)

with open("/home/cgslinde/DrillRoom/DrillRoom/scratch/p5.py", "w") as f:
    f.write(text)

print("Directly updated p5.py")
