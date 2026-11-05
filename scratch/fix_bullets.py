with open("/home/cgslinde/DrillRoom/DrillRoom/scratch/p5.py", "r") as f:
    p5_txt = f.read()

old_b_p5 = """&bull; A describes 100% penetrance, which was present at 22 &deg;C but lost under thermal stress at 30 &deg;C.<br>&bull; B and C are mathematical distractor traps that confuse total progeny with genotype carriers or fail to account for non-penetrant classes."""

new_b_p5 = """&bull; A describes 100% penetrance, which was present at 22 &deg;C but lost under thermal stress at 30 &deg;C.<br>&bull; B is a mathematical distractor trap that confuses total progeny with genotype carriers.<br>&bull; C is an incorrect calculation that fails to account for the non-penetrant carrier class."""

p5_txt = p5_txt.replace(old_b_p5, new_b_p5)

with open("/home/cgslinde/DrillRoom/DrillRoom/scratch/p5.py", "w") as f:
    f.write(p5_txt)

with open("/home/cgslinde/DrillRoom/DrillRoom/scratch/p7.py", "r") as f:
    p7_txt = f.read()

old_b_p7 = """&bull; B and C describe electrostatic interactions (salt bridges and positive charges), but isoleucine and valine both have completely nonpolar, hydrophobic, uncharged branched aliphatic hydrocarbon side chains.<br>&bull; D is a chemical error; amino acids are attached to tRNA via an **ester bond** at the 2'- or 3'-hydroxyl of the terminal adenosine ribose, not an amide bond."""

new_b_p7 = """&bull; B describes electrostatic salt bridges, but isoleucine and valine are both nonpolar aliphatic amino acids.<br>&bull; C describes charge repulsion, but both isoleucine and valine side chains are uncharged hydrocarbons.<br>&bull; D is a chemical error; amino acids are attached to tRNA via an **ester bond** at the 2'- or 3'-hydroxyl of the terminal adenosine ribose, not an amide bond."""

p7_txt = p7_txt.replace(old_b_p7, new_b_p7)

with open("/home/cgslinde/DrillRoom/DrillRoom/scratch/p7.py", "w") as f:
    f.write(p7_txt)

print("Fixed bullets successfully")
