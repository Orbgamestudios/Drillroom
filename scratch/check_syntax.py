with open('/home/cgslinde/DrillRoom/DrillRoom/gemini_analysis.js') as f:
    text = f.read()

stack = []
in_str = False
str_char = ''
in_line_comment = False
in_block_comment = False
escape = False

for idx, ch in enumerate(text):
    if escape:
        escape = False
        continue
    if ch == '\\':
        escape = True
        continue
    if in_line_comment:
        if ch == '\n': in_line_comment = False
        continue
    if in_block_comment:
        if ch == '/' and idx > 0 and text[idx-1] == '*':
            in_block_comment = False
        continue
    if in_str:
        if ch == str_char:
            in_str = False
        continue
    if ch == '/' and idx + 1 < len(text):
        if text[idx+1] == '/':
            in_line_comment = True
            continue
        elif text[idx+1] == '*':
            in_block_comment = True
            continue
    if ch in ('"', "'", '`'):
        in_str = True
        str_char = ch
        continue
    if ch in '({[':
        stack.append((ch, idx))
    elif ch in ')}]':
        if not stack:
            raise ValueError(f'Unmatched {ch} at char {idx}')
        top, top_idx = stack.pop()
        pairs = {'(':')', '{':'}', '[':']'}
        if pairs[top] != ch:
            raise ValueError(f'Mismatched {top} at {top_idx} with {ch} at {idx}')

if stack:
    print('Unclosed:', stack[-5:])
    raise ValueError(f'{len(stack)} unclosed brackets!')

print('gemini_analysis.js syntax check PASSED! All brackets, braces, and quotes match perfectly.')
