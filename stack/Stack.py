from typing import Any, Union


class Stack:
    # output_stack_empty = 'Stack is empty'

    def __init__(self):
        self.stack_list: list = []

    def is_empty(self) -> bool:
        return False if self.stack_list else True

    def push(self, element: Any):
        self.stack_list.append(element)

    def pop(self) -> Any:
        if not self.is_empty():
            self.stack_list.pop()
            return self.stack_list[-1] if self.stack_list else self.stack_list
        return self.stack_list

    def peek(self) -> Any:
        if not self.is_empty():
            return self.stack_list[-1]
        return self.stack_list

    def size(self) -> Union[list, int]:
        if not self.is_empty():
            return len(self.stack_list)
        return 0
