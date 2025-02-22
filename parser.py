class ASTNode:
    pass

class VariableAssignment(ASTNode):
    def __init__(self, var_name, value):
        self.var_name = var_name
        self.value = value

class PrintStatement(ASTNode):
    def __init__(self, var_name):
        self.var_name = var_name

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_pos = 0

    def parse(self):
        ast = []
        while self.current_pos < len(self.tokens):
            token = self.tokens[self.current_pos]
            if token == "let":
                ast.append(self.parse_variable_assignment())
            elif token == "print":
                ast.append(self.parse_print_statement())
            else:
                self.current_pos += 1
        return ast

    def parse_variable_assignment(self):
        self.current_pos += 1  # Skip 'let'
        var_name = self.tokens[self.current_pos]
        self.current_pos += 1  # Skip variable name
        self.current_pos += 1  # Skip '='
        
        # Expect the next token after '=' to be a number (value to assign to the variable)
        value_token = self.tokens[self.current_pos]
        if value_token.isdigit():
            value = int(value_token)  # Convert value to integer
            self.current_pos += 1  # Skip value
            self.current_pos += 1  # Skip ';'
            return VariableAssignment(var_name, value)
        else:
            raise ValueError(f"Expected integer value after '=' but got {value_token}")

    def parse_print_statement(self):
        self.current_pos += 1  # Skip 'print'
        var_name = self.tokens[self.current_pos]
        self.current_pos += 1  # Skip variable name
        self.current_pos += 1  # Skip ';'
        return PrintStatement(var_name)
