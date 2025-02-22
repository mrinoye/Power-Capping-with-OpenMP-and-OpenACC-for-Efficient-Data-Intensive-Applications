import re

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.current_pos = 0

    def next_token(self):
        if self.current_pos >= len(self.code):
            return None
        match = re.match(r'\s*(\d+|let|print|[a-zA-Z_][a-zA-Z0-9_]*|=|;|\+|\-|\*|/|\(|\))', self.code[self.current_pos:])
        if match:
            token = match.group(0).strip()
            self.current_pos += len(token)
            return token
        return None

    def tokenize(self):
        while token := self.next_token():
            self.tokens.append(token)
        return self.tokens
