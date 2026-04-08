class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minimum) > 0:
            if val <= self.minimum[-1]:
                self.minimum.append(val)
        else:
            self.minimum.append(val)

    def pop(self) -> None:
        temp = self.stack.pop()
        if temp == self.minimum[-1]:
            self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]
