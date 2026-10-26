class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = None
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)
            
    def pop(self) -> None:
        peek = self.stack[-1]
        self.stack.pop() 
        if peek == self.min_stack[-1]:
            self.min_stack.pop()       

    def top(self) -> int:
        return None if not self.stack else self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
