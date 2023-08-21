import pytest
from Stack import Stack
from tools.bracket_balance import bracket_balance

class TestStack:

    def test_is_empty(self):
        test_object = Stack()
        res = test_object.is_empty()
        expected = True
        assert res == expected

    def test_push(self):
        test_object = Stack()
        test_object.push(1)
        res = test_object.stack_list[-1]
        expected = 1
        assert res == expected

    def test_is_not_empty(self):
        test_object = Stack()
        test_object.push(1)
        res = test_object.is_empty()
        expected = False
        assert res == expected

    def test_pop(self):
        test_object = Stack()
        test_object.stack_list = [1, 2, 3]
        test_object.pop()
        res = test_object.stack_list
        expected = [1, 2]
        assert res == expected

    def test_peek(self):
        test_object = Stack()
        test_object.stack_list = [1, 2, 3]
        res = test_object.peek()
        expected = 3
        assert res == expected

    def test_size(self):
        test_object = Stack()
        test_object.stack_list = [1, 2, 3]
        res = test_object.size()
        expected = 3
        assert res == expected

'''
Пример сбалансированных последовательностей скобок:

(((([{}]))))
[([])((([[[]]])))]{()}
{{[()]}}
Несбалансированные последовательности:

}{}
{{[(])]}}
[[{())}]
'''

class TestBracketBalance:
    @pytest.mark.parametrize(
        'input_string,expected',
        [
            ('([])', 'Сбалансированно'),
            ('(((([{}]))))', 'Сбалансированно'),
            ('[([])((([[[]]])))]{()}', 'Сбалансированно'),
            ('{{[()]}}', 'Сбалансированно'),
            ('}{}', 'Несбалансированно'),
            ('{{[(])]}}', 'Несбалансированно'),
            ('[[{())}]', 'Несбалансированно')
        ]
    )
    def test_with_params(self, input_string, expected):
        res = bracket_balance(input_string)
        assert res == expected
