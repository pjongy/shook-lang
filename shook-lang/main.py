import sys
from typing import List


class Flags:
    def __init__(self):
        self.variable_assigning = False


def _overflow_mask(op: int) -> int:
    return op & 0xff


class Interpreter:
    def __init__(self, stack_max_size=256, debug=False):
        self.stack_max_size = stack_max_size
        self.stack = [0 for _ in range(self.stack_max_size)]
        self.stack_pointer = 0

        self.flags = Flags()
        self._variable = 0
        self.debug = debug

    def print_memory(self):
        stack_memory = ','.join([str(i) for i in self.stack])
        print(f'stack:  {stack_memory}')
        print(f'variable: {self._variable}')
        print(f'stack pointer: {self.stack_pointer}')
        print(f'flag(variable_assigning): {self.flags.variable_assigning}')

    def run(self, code: str):
        if code == '슉':
            assert self.flags.variable_assigning is False
            self.flags.variable_assigning = True
            self._variable = 0
        if code == '슈':
            assert self.flags.variable_assigning is True
            self._variable += 1
            self._variable = _overflow_mask(self._variable)
        if code == '아':
            assert self.flags.variable_assigning is True
            self._variable -= 1
            self._variable = _overflow_mask(self._variable)
        if code == '.':
            assert self.flags.variable_assigning is True
            self._variable **= 2
            self._variable = _overflow_mask(self._variable)
        if code == ' ':
            self.stack_pointer += 1
        if code == ',':
            self.stack_pointer -= 1
        if code == '욱':
            # Add stack value to variable
            assert self.flags.variable_assigning is True
            self._variable += self.stack[self.stack_pointer]
            self._variable = _overflow_mask(self._variable)
        if code == '우욱':
            # Minus stack value to variable
            assert self.flags.variable_assigning is True
            self._variable -= self.stack[self.stack_pointer]
            self._variable = _overflow_mask(self._variable)
        if code == '우우욱':
            # Multiple stack value to variable
            assert self.flags.variable_assigning is True
            self._variable *= self.stack[self.stack_pointer]
            self._variable = _overflow_mask(self._variable)
        if code == '우우우욱':
            # Divide stack value to variable
            assert self.flags.variable_assigning is True
            self._variable /= self.stack[self.stack_pointer]
            self._variable = _overflow_mask(int(self._variable))
        if code == '시발럼아':
            # Assign variable to stack data
            assert self.flags.variable_assigning is True
            self.stack[self.stack_pointer] = self._variable
            self.flags.variable_assigning = False
        if code == '시발람아':
            # Assign stack data to variable
            assert self.flags.variable_assigning is False
            self._variable = self.stack[self.stack_pointer]
            self.flags.variable_assigning = True
        if code == '-':
            # Assign stack pointer to variable
            assert self.flags.variable_assigning is False
            self._variable = self.stack_pointer
            self.flags.variable_assigning = True
        if code == '_':
            # Assign variable to stack pointer
            assert self.flags.variable_assigning is True
            self.stack_pointer = min(self._variable, self.stack_max_size)
            self.flags.variable_assigning = False
        if code == '슥':
            # Change variable to str type and assign it to stack
            string_value = str(self._variable)
            for value in reversed(string_value):
                self.stack[self.stack_pointer] = int(value)
                self.stack_pointer += 1
        if code == '시발롬아':
            # Print current stack while null access
            printing_buffer_pointer = self.stack_pointer - 1
            while printing_buffer_pointer >= 0:
                element = self.stack[printing_buffer_pointer]
                if element == 0:
                    break
                sys.stdout.write(chr(element))
                printing_buffer_pointer -= 1
        if self.debug:
            print(code)
            self.print_memory()


def tokenize(code: str) -> List[str]:
    tokenized = []
    sibal_ing = False
    sibal_stack = []
    woo_stack = []
    for op in code:
        if op == '우':
            woo_stack.append(op)
        elif op == '욱':
            woo_stack.append(op)
            tokenized.append(''.join(woo_stack))
            woo_stack = []
        elif op == '시':
            assert sibal_ing is False
            sibal_ing = True
            sibal_stack.append(op)
        elif op == '발':
            assert sibal_stack[-1], '시'
            sibal_stack.append(op)
        elif op in ['럼', '롬', '람']:
            assert sibal_stack[-1], '발'
            sibal_stack.append(op)
        elif op == '아' and sibal_ing:
            if sibal_stack[-1] not in ['럼', '롬', '람']:
                raise AssertionError('럼,롬,람 should already be set')
            sibal_stack.append(op)
            tokenized.append(''.join(sibal_stack))
            sibal_stack = []
            sibal_ing = False
        else:
            tokenized.append(op)
    return tokenized


def main(input_file: str, debug: bool = False):
    with open(input_file, 'r') as shook:
        code = shook.read()
        thread = Interpreter(20, debug)
        for op in tokenize(code):
            thread.run(op)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Shook-lang runtime')
    parser.add_argument('--input', default='multiple3by4.shook', help='Pass input .shook file')
    parser.add_argument('--debug', default='False', help='Debug flag (True/False)')
    args = parser.parse_args()
    main(args.input, args.debug == 'True')
