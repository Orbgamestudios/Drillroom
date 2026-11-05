import re

def test_bullet_count(e):
    bullets = re.findall(r'&bull;\s*([A-D])\b', e)
    return bullets

print("Test harness ready")
