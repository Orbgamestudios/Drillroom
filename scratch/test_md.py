import re

def render_markdown(md):
    lines = md.split('\n')
    out = []
    in_list = False
    list_type = None
    in_table = False
    table_header_done = False
    in_code = False
    
    for line in lines:
        raw = line
        stripped = line.strip()
        
        # Code block
        if stripped.startswith('```'):
            if in_code:
                out.append('</code></pre>')
                in_code = False
            else:
                out.append('<pre style="background:#1e293b;color:#f8fafc;padding:12px;border-radius:4px;overflow-x:auto;font-family:monospace;font-size:13px"><code>')
                in_code = True
            continue
        
        if in_code:
            out.append(raw.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;'))
            continue
            
        # Tables
        if stripped.startswith('|') and stripped.endswith('|'):
            cells = [c.strip() for c in stripped[1:-1].split('|')]
            if all(re.match(r'^:?-+:?$', c) for c in cells):
                table_header_done = True
                continue
            if not in_table:
                if in_list:
                    out.append(f'</{list_type}>')
                    in_list = False
                out.append('<table style="width:100%;border-collapse:collapse;margin:14px 0;font-size:13px;border:1px solid var(--line)">')
                in_table = True
                table_header_done = False
            
            tag = 'th' if not table_header_done else 'td'
            bg = 'background:#EDEFF1;font-weight:700;' if not table_header_done else ''
            cells_html = ''.join(f'<{tag} style="border:1px solid var(--line);padding:7px 10px;text-align:left;{bg}">{c}</{tag}>' for c in cells)
            out.append(f'<tr>{cells_html}</tr>')
            continue
        elif in_table:
            out.append('</table>')
            in_table = False
            table_header_done = False

        # Blockquote / Alert
        if stripped.startswith('>'):
            content = stripped[1:].strip()
            alert_class = "info"
            if content.startswith('[!TIP]'):
                alert_class = "tip"; content = content[6:].strip()
            elif content.startswith('[!WARNING]'):
                alert_class = "warn"; content = content[10:].strip()
            elif content.startswith('[!IMPORTANT]'):
                alert_class = "alert"; content = content[12:].strip()
            out.append(f'<div style="margin:10px 0;padding:10px 14px;border-left:4px solid var(--selBd);background:#F0F4F8;font-size:13.5px;line-height:1.5">{content}</div>')
            continue

        # Lists
        m_ul = re.match(r'^[-*]\s+(.*)$', stripped)
        m_ol = re.match(r'^\d+\.\s+(.*)$', stripped)
        if m_ul:
            if not in_list or list_type != 'ul':
                if in_list: out.append(f'</{list_type}>')
                out.append('<ul style="margin:8px 0 12px 20px;line-height:1.6">')
                in_list = True
                list_type = 'ul'
            out.append(f'<li>{m_ul.group(1)}</li>')
            continue
        elif m_ol:
            if not in_list or list_type != 'ol':
                if in_list: out.append(f'</{list_type}>')
                out.append('<ol style="margin:8px 0 12px 20px;line-height:1.6">')
                in_list = True
                list_type = 'ol'
            out.append(f'<li>{m_ol.group(1)}</li>')
            continue
        else:
            if in_list:
                out.append(f'</{list_type}>')
                in_list = False

        # Headers
        if stripped.startswith('# '):
            out.append(f'<h1 style="font-size:20px;font-weight:700;margin:20px 0 10px;color:var(--nav);border-bottom:2px solid var(--line);padding-bottom:6px">{stripped[2:]}</h1>')
            continue
        elif stripped.startswith('## '):
            out.append(f'<h2 style="font-size:16px;font-weight:700;margin:16px 0 8px;color:var(--ink);border-bottom:1px solid var(--line);padding-bottom:4px">{stripped[3:]}</h2>')
            continue
        elif stripped.startswith('### '):
            out.append(f'<h3 style="font-size:14.5px;font-weight:700;margin:14px 0 6px;color:#2E6DA4">{stripped[4:]}</h3>')
            continue
        elif stripped.startswith('---'):
            out.append('<hr style="border:none;border-top:1px solid var(--line);margin:16px 0">')
            continue

        if not stripped:
            continue

        out.append(f'<p style="margin:8px 0;line-height:1.6;font-size:13.5px">{stripped}</p>')

    if in_list:
        out.append(f'</{list_type}>')
    if in_table:
        out.append('</table>')
    if in_code:
        out.append('</code></pre>')

    html = '\n'.join(out)
    # Inline formatting: **bold**, *italic*, `code`
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    html = re.sub(r'`(.*?)`', r'<code style="background:#EBF0F5;padding:2px 5px;border-radius:3px;font-family:monospace;font-size:12.5px">\1</code>', html)
    return html

sample = """# 1. Executive Score Diagnostic
- Scaled score of **126/132** is solid.
- You had 3 *lucky* guesses.

| Metric | Value |
| --- | --- |
| Raw | 68% |
| Scaled | 126 |

> High confidence misses indicate false models.

```python
print("Hello")
```
"""
res = render_markdown(sample)
print("Markdown rendered successfully! Length:", len(res))
print(res[:300])
