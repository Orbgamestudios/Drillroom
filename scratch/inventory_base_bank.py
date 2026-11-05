import re

with open('/home/cgslinde/DrillRoom/DrillRoom/DrillRoom.html') as f:
    t = f.read()

# Find all sets in DrillRoom.html
sets = re.findall(r'id:\s*\"([^\"]+)\",\s*sec:\s*\"([^\"]+)\",\s*topic:\s*\"([^\"]+)\"', t)
print(f"Total base sets in DrillRoom.html: {len(sets)}")
by_sec = {}
for sid, sec, top in sets:
    by_sec.setdefault(sec, []).append((sid, top))

for sec, sl in by_sec.items():
    print(f"\n{sec} ({len(sl)} sets):")
    for sid, top in sl:
        print(f"  {sid:28} | {top}")

