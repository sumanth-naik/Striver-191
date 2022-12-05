class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = 10e10

    def push(self, val: int) -> None:
        if self.minVal<val:
            self.stack.append(val)
        else:
            self.stack.append(2*val-self.minVal)
            self.minVal = val

    def pop(self) -> None:
        if self.minVal<self.stack[-1]:
            top = self.stack.pop()
            realTopVal = self.minVal
            self.minVal = 2*self.minVal - top
            return realTopVal
        else:
            return self.stack.pop()
            
    def top(self) -> int:
        if self.minVal<self.stack[-1]:
            return self.minVal
        else:
            return self.stack[-1]      

    def getMin(self) -> int:
        return self.minVal
