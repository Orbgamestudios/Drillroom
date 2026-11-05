#!/usr/bin/env python3
"""
Generator script for exam_cp90_3.js
Exam 3 Chem/Physical Foundations 90-minute Section
Topics 234 - 250
"""
import json
import re
import sys

def word_count(html_text):
    # strip html tags
    clean = re.sub(r'<[^>]+>', ' ', html_text)
    words = clean.split()
    return len(words)

def check_length_parity(ch_list):
    lens = [len(c) for c in ch_list]
    avg = sum(lens) / len(lens)
    if avg == 0:
        return True, 0
    max_dev = max(abs(l - avg) / avg for l in lens)
    return max_dev <= 0.25, max_dev

print("Initializing generation script...")
