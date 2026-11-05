# scratch/sync_cars60_p6.py
import json, re

with open('exam_cars90.js', 'r', encoding='utf-8') as f:
    cars90 = json.loads(f.read().split('const EXAM_CARS90 = ')[1].rstrip().rstrip(';'))

p2_qs = cars90[1]['qs']

with open('exam_60min.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const EXAM_CARS60\s*=\s*(\[[\s\S]*?\]);\s*(?:const|var|let|\/\*|$)', text)
cars60 = json.loads(m.group(1))

assert cars60[5]['topic'] == 'AAMC · Puritan society'
cars60[5]['qs'] = p2_qs

new_cars60_json = json.dumps(cars60, indent=2, ensure_ascii=False)
text = text[:m.start(1)] + new_cars60_json + text[m.end(1):]

with open('exam_60min.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully synchronized EXAM_CARS60 P6 with 5/5 questions from EXAM_CARS90 P2!")
