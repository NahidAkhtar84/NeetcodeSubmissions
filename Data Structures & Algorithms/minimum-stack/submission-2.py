class MinStack:

    def __init__(self):
        self.stack = []
        self.ordered_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.ordered_stack:
            if val <= self.ordered_stack[-1]:
                self.ordered_stack.append(val)
        else:
            self.ordered_stack.append(val)
        
    def pop(self) -> None:
        if self.stack[-1] == self.ordered_stack[-1]:
            self.ordered_stack.pop()
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.ordered_stack[-1]
        
