# build_exam7.py
import json
import re
import sys

def word_count(html_str):
    # remove html tags and math formulas to count prose words
    # replace tags with spaces
    text = re.sub(r'<table[\s\S]*?</table>', ' ', html_str)
    text = re.sub(r'<div class="ttl">[\s\S]*?</div>', ' ', html)
    text = re.sub(r'<[^>]+>', ' ', text)
    # remove math expressions $...$ and $$...$$
    text = re.sub(r'\$\$[\s\S]*?\$\$', ' ', text)
    text = re.sub(r'\$[^\$]*\$', ' ', text)
    words = [w for w in re.split(r'\s+', text) if w.strip()]
    return len(words)
