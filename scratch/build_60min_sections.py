import re, json
from parse_cars import JSObjectParser, parse_set_at

with open("DrillRoom.html") as f:
    html = f.read()

scripts = re.findall(r"<script>(.*?)</script>", html, re.DOTALL)

# Helper to renumber passage title
def update_title(passage_html, passage_num, q_start, q_end):
    new_ttl = f'<div class="ttl">Passage {passage_num} (Questions {q_start}&ndash;{q_end})</div>'
    return re.sub(r'<div class="ttl">.*?</div>', new_ttl, passage_html, count=1)

print("Helper defined.")
