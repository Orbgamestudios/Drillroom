# Psychological, Social, and Biological Foundations of Behavior (P/S)
# Topics 741 to 1000 (260 topics)

import os, sys
sys.path.append(os.path.dirname(__file__))

from ps_topics_part1 import PS_TOPICS_PART1
from ps_topics_part2 import PS_TOPICS_PART2

PS_TOPICS = PS_TOPICS_PART1 + PS_TOPICS_PART2

if __name__ == "__main__":
    print(f"P/S topics defined: {len(PS_TOPICS)}")
    print(f"Start: {PS_TOPICS[0][0]} - {PS_TOPICS[0][1]}")
    print(f"End: {PS_TOPICS[-1][0]} - {PS_TOPICS[-1][1]}")
