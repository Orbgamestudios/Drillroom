import re, json

with open("/home/cgslinde/DrillRoom/DrillRoom/DrillRoom.html") as f:
    html = f.read()

scripts = re.findall(r"<script>(.*?)</script>", html, re.DOTALL)
s5 = scripts[5]
s6 = scripts[6]

class JSObjectParser:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.n = len(text)

    def skip_whitespace(self):
        while self.pos < self.n:
            c = self.text[self.pos]
            if c.isspace():
                self.pos += 1
            elif c == '/' and self.pos + 1 < self.n:
                if self.text[self.pos+1] == '/':
                    # line comment
                    self.pos = self.text.find('\n', self.pos)
                    if self.pos == -1: self.pos = self.n
                elif self.text[self.pos+1] == '*':
                    # block comment
                    self.pos = self.text.find('*/', self.pos + 2)
                    if self.pos == -1: self.pos = self.n
                    else: self.pos += 2
                else:
                    break
            else:
                break

    def parse_value(self):
        self.skip_whitespace()
        if self.pos >= self.n:
            return None
        c = self.text[self.pos]
        if c == '{':
            return self.parse_object()
        elif c == '[':
            return self.parse_array()
        elif c == '"':
            return self.parse_string('"')
        elif c == "'":
            return self.parse_string("'")
        elif c == '`':
            return self.parse_template_string()
        elif c.isdigit() or (c == '-' and self.pos + 1 < self.n and self.text[self.pos+1].isdigit()):
            return self.parse_number()
        elif self.text[self.pos:self.pos+4] == 'true':
            self.pos += 4
            return True
        elif self.text[self.pos:self.pos+5] == 'false':
            self.pos += 5
            return False
        elif self.text[self.pos:self.pos+4] == 'null':
            self.pos += 4
            return None
        else:
            raise ValueError(f"Unexpected character '{c}' at position {self.pos}: {self.text[self.pos:self.pos+40]}")

    def parse_string(self, quote_char):
        self.pos += 1  # skip opening quote
        start = self.pos
        result = []
        while self.pos < self.n:
            c = self.text[self.pos]
            if c == '\\':
                result.append(self.text[start:self.pos])
                self.pos += 1
                esc = self.text[self.pos]
                if esc == 'n': result.append('\n')
                elif esc == 'r': result.append('\r')
                elif esc == 't': result.append('\t')
                elif esc == '"': result.append('"')
                elif esc == "'": result.append("'")
                elif esc == '\\': result.append('\\')
                elif esc == '/': result.append('/')
                elif esc == 'u':
                    # unicode \uXXXX
                    u_code = self.text[self.pos+1:self.pos+5]
                    result.append(chr(int(u_code, 16)))
                    self.pos += 4
                else:
                    result.append(esc)
                self.pos += 1
                start = self.pos
            elif c == quote_char:
                result.append(self.text[start:self.pos])
                self.pos += 1  # skip closing quote
                return "".join(result)
            else:
                self.pos += 1
        raise ValueError(f"Unterminated string starting near {self.text[start-1:start+30]}")

    def parse_template_string(self):
        self.pos += 1  # skip opening `
        start = self.pos
        result = []
        while self.pos < self.n:
            c = self.text[self.pos]
            if c == '\\':
                result.append(self.text[start:self.pos])
                self.pos += 1
                esc = self.text[self.pos]
                if esc == '`': result.append('`')
                elif esc == '\\': result.append('\\')
                else: result.append('\\' + esc)
                self.pos += 1
                start = self.pos
            elif c == '`':
                result.append(self.text[start:self.pos])
                self.pos += 1  # skip closing `
                return "".join(result)
            else:
                self.pos += 1
        raise ValueError(f"Unterminated template string starting near {self.text[start-1:start+30]}")

    def parse_number(self):
        start = self.pos
        if self.text[self.pos] == '-': self.pos += 1
        while self.pos < self.n and (self.text[self.pos].isdigit() or self.text[self.pos] == '.'):
            self.pos += 1
        num_str = self.text[start:self.pos]
        return float(num_str) if '.' in num_str else int(num_str)

    def parse_identifier(self):
        self.skip_whitespace()
        start = self.pos
        while self.pos < self.n and (self.text[self.pos].isalnum() or self.text[self.pos] in '_$'):
            self.pos += 1
        return self.text[start:self.pos]

    def parse_object(self):
        self.pos += 1  # skip {
        obj = {}
        while True:
            self.skip_whitespace()
            if self.pos >= self.n:
                raise ValueError("Unterminated object")
            if self.text[self.pos] == '}':
                self.pos += 1
                return obj
            # parse key
            if self.text[self.pos] in ('"', "'"):
                key = self.parse_string(self.text[self.pos])
            else:
                key = self.parse_identifier()
            if not key:
                raise ValueError(f"Expected key at {self.pos}: {self.text[self.pos:self.pos+30]}")
            self.skip_whitespace()
            if self.pos >= self.n or self.text[self.pos] != ':':
                raise ValueError(f"Expected ':' after key '{key}' at {self.pos}")
            self.pos += 1  # skip :
            val = self.parse_value()
            obj[key] = val
            self.skip_whitespace()
            if self.pos < self.n and self.text[self.pos] == ',':
                self.pos += 1
            elif self.pos < self.n and self.text[self.pos] == '}':
                self.pos += 1
                return obj
            else:
                # in case comma is omitted or next is closing brace
                if self.pos < self.n and self.text[self.pos] == '}':
                    self.pos += 1
                    return obj

    def parse_array(self):
        self.pos += 1  # skip [
        arr = []
        while True:
            self.skip_whitespace()
            if self.pos >= self.n:
                raise ValueError("Unterminated array")
            if self.text[self.pos] == ']':
                self.pos += 1
                return arr
            val = self.parse_value()
            arr.append(val)
            self.skip_whitespace()
            if self.pos < self.n and self.text[self.pos] == ',':
                self.pos += 1
            elif self.pos < self.n and self.text[self.pos] == ']':
                self.pos += 1
                return arr

def parse_set_at(text, search_id):
    pos = text.find(f'"{search_id}"')
    if pos == -1:
        pos = text.find(f"'{search_id}'")
    if pos == -1:
        raise ValueError(f"Could not find {search_id}")
    # find the preceding '{'
    brace_pos = text.rfind('{', 0, pos)
    parser = JSObjectParser(text)
    parser.pos = brace_pos
    return parser.parse_object()

# Test on cars_veblen
veblen = parse_set_at(s5, "cars_veblen")
print("Parsed cars_veblen successfully!")
print("ID:", veblen["id"])
print("Topic:", veblen["topic"])
print("Passage snippet:", veblen["passage"][:100])
print("Num questions:", len(veblen["qs"]))
for i, q in enumerate(veblen["qs"]):
    print(f"  Q{i+1}: {q['q'][:50]} | a={q['a']} | ch_len={len(q['ch'])}")
