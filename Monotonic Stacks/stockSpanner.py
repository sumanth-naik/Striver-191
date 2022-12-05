class StockSpanner:

    def __init__(self):
        self.stack = [(0,-1)]
        self.nextIndex = 0

    def next(self, price: int) -> int:
        
        while len(self.stack)>1 and price>=self.stack[len(self.stack)-1][0]:
            self.stack.pop()
        
        span = self.nextIndex - self.stack[len(self.stack)-1][1]
        self.stack.append((price,self.nextIndex))
        self.nextIndex += 1
        return span

