import unittest

from DSA.stack_task.stack import Stack

class TestStack(unittest.TestCase):

    def test_that_stack_is_empty(self):
        stack = Stack()
        self.assertEqual(stack.is_empty(), True)

    def test_that_stack_is_not_empty(self):
        stack = Stack()
        stack.push('Samibyrone')
        stack.push('chibuzor')
        self.assertEqual(stack.is_empty(), False)

    def test_that_stack_can_push(self):
        stack = Stack()
        stack.push('Samibyrone')
        stack.push('chibuzor')
        stack.push(5000)
        self.assertEqual(stack.total_size() == 3, True)
        self.assertEqual(stack.is_empty(), False)

    def test_that_stack_can_pop(self):
        stack = Stack()
        stack.push('Samibyrone')
        stack.push('chibuzor')
        stack.push(5000)
        stack.push("Semicolon")
        stack.pop()
        self.assertEqual(stack.is_empty(), False)
        self.assertEqual(stack.total_size()== 3, True)

    def test_that_stack_can_push_and_peek(self):
        stack = Stack()
        stack.push('Samibyrone')
        stack.push('chibuzor')
        stack.push("semicolon")
        stack.push(5000)
        self.assertEqual(stack.is_empty(), False)
        self.assertEqual(stack.peek(), 5000)

    def test_that_stack_can_push_and_pop_and_peek_and_check_size(self):
        stack = Stack()
        stack.push('Samibyrone')
        stack.push('Chibuzor')
        stack.push("Semicolon")
        stack.push(5000)
        stack.pop()
        self.assertEqual(stack.is_empty(), False)
        self.assertEqual(stack.peek(), "Semicolon")
        self.assertEqual(stack.total_size(), 3)
