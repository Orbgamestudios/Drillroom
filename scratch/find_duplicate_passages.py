# scratch/find_duplicate_passages.py
import glob, json, re
from collections import defaultdict

files = sorted(glob.glob('exam_*.js'))
all_items = []

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = re.finditer(r'(?:const|var|let)\s+([A-Za-z0-9_]+)\s*=\s*(\[[\s\S]*?\]);', content)
    for m in matches:
        var_name = m.group(1)
        json_str = m.group(2)
        try:
            arr = json.loads(json_str)
            for idx, item in enumerate(arr):
                passage_text = item.get('passage', '')
                topic = item.get('topic', '')
                pid = item.get('id', f'{var_name}_{idx}')
                sec = item.get('sec', '')
                qs = item.get('qs', [])
                
                # Clean passage text: strip HTML, lowercase, normalize whitespace
                clean_passage = re.sub(r'<[^>]+>', ' ', passage_text)
                # Remove common header like "Passage 1 (Questions 1-6)"
                clean_passage = re.sub(r'Passage\s+\d+\s*\([^)]+\)', '', clean_passage)
                clean_passage = ' '.join(clean_passage.lower().split())
                
                all_items.append({
                    'file': fname,
                    'var': var_name,
                    'index': idx,
                    'id': pid,
                    'sec': sec,
                    'topic': topic.strip(),
                    'raw_passage': passage_text,
                    'clean_passage': clean_passage,
                    'num_qs': len(qs),
                    'questions': [q.get('q', '') for q in qs],
                    'clean_qs': [' '.join(re.sub(r'<[^>]+>', '', q.get('q', '')).lower().split()) for q in qs]
                })
        except Exception as e:
            print(f"Error parsing {var_name} in {fname}: {e}")

print(f"Total items extracted: {len(all_items)} across {len(files)} files.\n")

# ==============================================================================
# 1. EXACT ID DUPLICATES
# ==============================================================================
print("=== 1. ID COLLISIONS ===")
id_map = defaultdict(list)
for item in all_items:
    id_map[item['id']].append(item)

id_dups = {k: v for k, v in id_map.items() if len(v) > 1}
if not id_dups:
    print("✓ No passage ID collisions found.")
else:
    print(f"Found {len(id_dups)} ID collisions:")
    for pid, instances in id_dups.items():
        print(f"  ID '{pid}' appears in {len(instances)} places:")
        for inst in instances:
            print(f"    - {inst['file']} ({inst['var']}[{inst['index']}]): topic='{inst['topic']}'")

# ==============================================================================
# 2. EXACT OR NEAR-IDENTICAL PASSAGE TEXT DUPLICATES
# ==============================================================================
print("\n=== 2. PASSAGE TEXT DUPLICATES (Cleaned text >= 100 chars) ===")
# Only consider actual passages (skip discretes with empty passage)
passage_items = [it for it in all_items if len(it['clean_passage']) >= 100]
print(f"Total non-discrete passages to compare: {len(passage_items)}")

# Map by first 120 characters of cleaned text
prefix_map = defaultdict(list)
for item in passage_items:
    prefix = item['clean_passage'][:120]
    prefix_map[prefix].append(item)

exact_passage_dups = {k: v for k, v in prefix_map.items() if len(v) > 1}
if not exact_passage_dups:
    print("✓ No identical passage text prefixes found.")
else:
    print(f"Found {len(exact_passage_dups)} passage text matches:")
    for prefix, instances in exact_passage_dups.items():
        print(f"\n  Match on prefix: '{prefix[:70]}...'")
        for inst in instances:
            print(f"    - {inst['file']} ({inst['var']}[{inst['index']}]): id='{inst['id']}', topic='{inst['topic']}', qs={inst['num_qs']}")

# Also check pairwise high word Jaccard similarity (> 0.70)
print("\n=== 3. FUZZY PASSAGE TEXT OVERLAP (Jaccard word similarity > 0.70) ===")
fuzzy_dups = []
seen_pairs = set()
for i in range(len(passage_items)):
    words_i = set(passage_items[i]['clean_passage'].split())
    if len(words_i) < 20: continue
    for j in range(i + 1, len(passage_items)):
        # If they already matched in exact prefix, skip
        if passage_items[i]['clean_passage'][:120] == passage_items[j]['clean_passage'][:120]:
            continue
        words_j = set(passage_items[j]['clean_passage'].split())
        if len(words_j) < 20: continue
        sim = len(words_i & words_j) / len(words_i | words_j)
        if sim > 0.70:
            fuzzy_dups.append((passage_items[i], passage_items[j], sim))

if not fuzzy_dups:
    print("✓ No additional fuzzy passage duplicates found.")
else:
    print(f"Found {len(fuzzy_dups)} fuzzy passage matches:")
    for p1, p2, sim in fuzzy_dups:
        print(f"  Similarity {sim:.2f}:")
        print(f"    A: {p1['file']} ({p1['var']}[{p1['index']}]): '{p1['topic']}'")
        print(f"    B: {p2['file']} ({p2['var']}[{p2['index']}]): '{p2['topic']}'")

# ==============================================================================
# 4. DUPLICATE TOPICS / TITLES
# ==============================================================================
print("\n=== 4. TOPIC / TITLE MATCHES ===")
topic_map = defaultdict(list)
for item in all_items:
    norm_topic = re.sub(r'[^a-z0-9]', '', item['topic'].lower())
    if len(norm_topic) > 5 and 'standalone' not in norm_topic and 'discrete' not in norm_topic:
        topic_map[norm_topic].append(item)

topic_dups = {k: v for k, v in topic_map.items() if len(v) > 1}
if not topic_dups:
    print("✓ No duplicate topics found.")
else:
    print(f"Found {len(topic_dups)} topic matches across different files:")
    for ntopic, instances in topic_dups.items():
        print(f"\n  Topic: '{instances[0]['topic']}' ({len(instances)} occurrences):")
        for inst in instances:
            print(f"    - {inst['file']} ({inst['var']}[{inst['index']}]): id='{inst['id']}', qs={inst['num_qs']}")

# ==============================================================================
# 5. DUPLICATE QUESTIONS (Identical question stems)
# ==============================================================================
print("\n=== 5. DUPLICATE QUESTION STEMS ===")
q_map = defaultdict(list)
for item in all_items:
    for q_idx, q_text in enumerate(item['clean_qs']):
        if len(q_text) > 25:
            q_map[q_text].append((item, q_idx))

q_dups = {k: v for k, v in q_map.items() if len(v) > 1}
if not q_dups:
    print("✓ No duplicate question stems found.")
else:
    print(f"Found {len(q_dups)} duplicate question stems:")
    # Group by passage pairs
    dup_pairs = defaultdict(list)
    for q_text, instances in q_dups.items():
        pair_key = tuple(sorted(set((inst[0]['file'], inst[0]['var'], inst[0]['id']) for inst in instances)))
        dup_pairs[pair_key].append(q_text)
    
    for pair, q_list in dup_pairs.items():
        print(f"\n  Between {pair}:")
        print(f"    Shared {len(q_list)} question stems, e.g.: '{q_list[0][:80]}...'")
