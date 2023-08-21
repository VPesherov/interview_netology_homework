from Stack import Stack
from typing import Any


def bracket_balance(input_string: str) -> str:
    i: int = 0
    stack: Stack = Stack()

    success_output: str = 'Сбалансированно'
    failure_output: str = 'Несбалансированно'

    analogue_dict: dict = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    while i < len(input_string):
        if input_string[i] in '({[':
            stack.push(input_string[i])
        if input_string[i] in ']})':
            if stack.is_empty():
                return failure_output
            top: Any = stack.peek()
            analogue: str = analogue_dict.get(top)
            if analogue == input_string[i]:
                stack.pop()
            else:
                return failure_output
        i += 1
    return success_output
