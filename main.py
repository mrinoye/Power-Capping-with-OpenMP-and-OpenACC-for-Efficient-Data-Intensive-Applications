from lexer import Lexer
from parser import Parser
from codegen import CodeGenerator

def main():
    code = """
    let x = 5;
    print(x);
    """
    
    # Tokenize the source code
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    # Parse the tokens into an AST
    parser = Parser(tokens)
    ast = parser.parse()

    # Generate LLVM IR
    code_gen = CodeGenerator()
    code_gen.generate_code(ast)

    # Print the generated LLVM IR
    print("Generated LLVM IR:")
    print(code_gen.module)

if __name__ == "__main__":
    main()
