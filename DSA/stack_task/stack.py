class Stack:

    def __init__(self):
        self.stack = []
        self.size = 10

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.size

    def push(self, element):
        if not self.is_full(): self.stack.append(element)
        else: print("Stack is full")

    def pop(self):
        if not self.is_empty(): return self.stack.pop()
        else: return "Stack is empty"

    def peek(self):
        if not self.is_empty(): return self.stack[-1]
        else: return "Stack is empty"

    def total_size(self):
        return len(self.stack)
