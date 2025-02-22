from llvmlite import binding
from parser import VariableAssignment,PrintStatement


class CodeGenerator:
    def __init__(self):
        self.module = binding.Module(name="my_program")
        self.builder = binding.IRBuilder()
        self.int32_type = binding.IntType(32)
        self.context = binding.get_global_context()

    def generate_code(self, ast):
        for node in ast:
            if isinstance(node, VariableAssignment):
                self.generate_variable_assignment(node)
            elif isinstance(node, PrintStatement):
                self.generate_print_statement(node)

    def generate_variable_assignment(self, node):
        func = self.create_main_function()
        var = func.append_basic_block('entry')
        self.builder.position_at_end(var)

        # Create the variable in the LLVM IR
        alloca = self.builder.alloca(self.int32_type, name=node.var_name)
        self.builder.store(binding.ConstantInt(self.int32_type, node.value), alloca)

    def generate_print_statement(self, node):
        print_func = self.module.get_or_insert_function("printf", 
            binding.FunctionType(self.int32_type, [binding.PointerType(self.int32_type)]))
        
        print_str = self.builder.global_string_ptr("%d\n")
        self.builder.call(print_func, [print_str])

    def create_main_function(self):
        func_type = binding.FunctionType(self.int32_type, [])
        func = binding.Function(self.module, func_type, name="main")
        return func
