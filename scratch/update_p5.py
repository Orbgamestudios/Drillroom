with open("/home/cgslinde/DrillRoom/DrillRoom/scratch/p5.py", "r") as f:
    code = f.read()

old_rows = """    <tr><td>Class 1: Dysplasia, Brachydactyly, Ataxia</td><td><em>N B S</em></td><td>412</td><td>290 (Plus 60 Non-Penetrant)</td><td>Non-Recombinant (Parental)</td><td>7.8 &plusmn; 0.6</td></tr>
    <tr><td>Class 2: Wild-Type Normal Controls</td><td><em>n b s</em></td><td>408</td><td>410</td><td>Non-Recombinant (Parental)</td><td>N/A (Normal Control)</td></tr>
    <tr><td>Class 3: Dysplasia Only</td><td><em>N b s</em></td><td>62</td><td>44 (Plus 9 Non-Penetrant)</td><td>Recombinant (Region I: <em>N</em>&ndash;<em>B</em>)</td><td>7.6 &plusmn; 0.5</td></tr>
    <tr><td>Class 4: Brachydactyly, Ataxia</td><td><em>n B S</em></td><td>58</td><td>57</td><td>Recombinant (Region I: <em>N</em>&ndash;<em>B</em>)</td><td>N/A (Normal Control)</td></tr>
    <tr><td>Class 5: Dysplasia, Brachydactyly</td><td><em>N B s</em></td><td>28</td><td>19 (Plus 4 Non-Penetrant)</td><td>Recombinant (Region II: <em>B</em>&ndash;<em>S</em>)</td><td>7.9 &plusmn; 0.7</td></tr>
    <tr><td>Class 6: Ataxia Only</td><td><em>n b S</em></td><td>24</td><td>25</td><td>Recombinant (Region II: <em>B</em>&ndash;<em>S</em>)</td><td>N/A (Normal Control)</td></tr>
    <tr><td>Class 7: Dysplasia, Ataxia</td><td><em>N b S</em></td><td>4</td><td>3 (Plus 1 Non-Penetrant)</td><td>Double Crossover (Regions I &amp; II)</td><td>7.7 &plusmn; 0.6</td></tr>
    <tr><td>Class 8: Brachydactyly Only</td><td><em>n B s</em></td><td>4</td><td>4</td><td>Double Crossover (Regions I &amp; II)</td><td>N/A (Normal Control)</td></tr>"""

new_rows = """    <tr><td>Class 1: Dysplasia, Brachydactyly, Ataxia</td><td><em>N B S</em></td><td>412</td><td>287 (Plus 123 Non-Penetrant)</td><td>Non-Recombinant (Parental)</td><td>7.8 &plusmn; 0.6</td></tr>
    <tr><td>Class 2: Wild-Type Normal Controls</td><td><em>n b s</em></td><td>408</td><td>410</td><td>Non-Recombinant (Parental)</td><td>N/A (Normal Control)</td></tr>
    <tr><td>Class 3: Dysplasia Only</td><td><em>N b s</em></td><td>62</td><td>42 (Plus 18 Non-Penetrant)</td><td>Recombinant (Region I: <em>N</em>&ndash;<em>B</em>)</td><td>7.6 &plusmn; 0.5</td></tr>
    <tr><td>Class 4: Brachydactyly, Ataxia</td><td><em>n B S</em></td><td>58</td><td>60</td><td>Recombinant (Region I: <em>N</em>&ndash;<em>B</em>)</td><td>N/A (Normal Control)</td></tr>
    <tr><td>Class 5: Dysplasia, Brachydactyly</td><td><em>N B s</em></td><td>28</td><td>18 (Plus 7 Non-Penetrant)</td><td>Recombinant (Region II: <em>B</em>&ndash;<em>S</em>)</td><td>7.9 &plusmn; 0.7</td></tr>
    <tr><td>Class 6: Ataxia Only</td><td><em>n b S</em></td><td>24</td><td>25</td><td>Recombinant (Region II: <em>B</em>&ndash;<em>S</em>)</td><td>N/A (Normal Control)</td></tr>
    <tr><td>Class 7: Dysplasia, Ataxia</td><td><em>N b S</em></td><td>4</td><td>3 (Plus 2 Non-Penetrant)</td><td>Double Crossover (Regions I &amp; II)</td><td>7.7 &plusmn; 0.6</td></tr>
    <tr><td>Class 8: Brachydactyly Only</td><td><em>n B s</em></td><td>4</td><td>5</td><td>Double Crossover (Regions I &amp; II)</td><td>N/A (Normal Control)</td></tr>"""

code = code.replace(old_rows, new_rows)

old_q28 = '"71%, because only 356 of the 500 offspring carrying the N allele manifested the neurocutaneous disease signs"'
new_q28 = '"70%, because exactly 350 of the 500 offspring carrying the N allele exhibited the neurocutaneous disease signs"'
code = code.replace(old_q28, new_q28)

# Also update the explanation of Q28
old_exp_part = """consisting of $290 + 60 = 350$ in Class 1; $44 + 9 = 53$ in Class 3; $19 + 4 = 23$ in Class 5; and $3 + 1 = 4$ in Class 7; total $= 350 + 53 + 23 + 4 = 430$ ... wait, let's sum: $290 + 44 + 19 + 3 = 356$ manifesting lesions, and $60 + 9 + 4 + 1 = 74$ non-penetrant carriers; total $N$ carriers $= 356 + 74 = 430$... wait, let's check: $430 + 410 + 57 + 25 + 4 = 926$). To calculate penetrance:<br>$$\\text{Penetrance} = \\frac{\\text{Number of Individuals with Genotype Exhibiting Phenotype}}{\\text{Total Number of Individuals Carrying Genotype}} \\times 100\\%$$<br>$$\\text{Penetrance} = \\frac{356}{356 + 74} = \\frac{356}{430} \\times 100\\% \\approx 82.8\\%$$\\nWait! Let's examine: $356 / 500 = 71.2\\% \\approx 71\\%$. If total carriers of N = 500, and $356$ manifest lesions, then $356 / 500 = 71.2\\% \\approx 71\\%$.<br><br><em>Distractor Traps:</em><br>&bull; A describes 100% penetrance, which was present at 22 &deg;C but lost at 30 &deg;C.<br>&bull; B and C are incorrect mathematical calculations that confuse total progeny with genotype carriers."""

new_exp_part = """comprising $287 + 123 = 410$ in Class 1; $42 + 18 = 60$ in Class 3; $18 + 7 = 25$ in Class 5; and $3 + 2 = 5$ in Class 7. Total $N$ carriers $= 410 + 60 + 25 + 5 = 500$. Of these 500 carriers, those manifesting neurocutaneous lesions are $287 + 42 + 18 + 3 = 350$, while $123 + 18 + 7 + 2 = 150$ are non-penetrant carriers. To calculate penetrance:<br>$$\\text{Penetrance} = \\frac{\\text{Number of Genotype Carriers Exhibiting Phenotype}}{\\text{Total Number of Individuals Carrying Genotype}} \\times 100\\%$$<br>$$\\text{Penetrance} = \\frac{350}{500} \\times 100\\% = 70.0\\%$$<br><em>Distractor Traps:</em><br>&bull; A describes 100% penetrance, which was present at 22 &deg;C but lost under thermal stress at 30 &deg;C.<br>&bull; B and C are mathematical distractor traps that confuse total progeny with genotype carriers or fail to account for non-penetrant classes."""

code = code.replace(old_exp_part, new_exp_part)

with open("/home/cgslinde/DrillRoom/DrillRoom/scratch/p5.py", "w") as f:
    f.write(code)

print("Updated p5.py successfully")
