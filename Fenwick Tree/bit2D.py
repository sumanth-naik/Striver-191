# 1 indexed 2D BIT
class BIT2D:
    def __init__(self, m, n) -> None:
        self.treeSize = (m, n)
        self.bit = [[0 for _ in range(n)] for _ in range(m)]

    def add(self, x, y, val):
        while x<self.treeSize[0]:
            yTemp = y
            while yTemp<self.treeSize[1]:
                self.bit[x][yTemp] += val
                yTemp += (yTemp & -yTemp)
            x += (x & -x)
        
    def numPointsInside(self, x, y):
        total = 0
        while x>0:
            yTemp = y
            while yTemp>0:
                total += self.bit[x][yTemp]
                yTemp -= (yTemp & -yTemp)
            x -= (x & -x)
        return total
    

# 1 indexed 2D BIT
class BIT2D:
    def __init__(self, m, n) -> None:
        self.treeSize = (m, n)
        self.bit = [[-1 for _ in range(n)] for _ in range(m)]

    def add(self, x, y):
        while x<self.treeSize[0]:
            yTemp = y
            while yTemp<self.treeSize[1]:
                self.bit[x][yTemp] = max(self.bit[x][yTemp], y)
                yTemp += (yTemp & -yTemp)
            x += (x & -x)
        
    def numPointsInside(self, x, y):
        total = 0
        while x>0:
            yTemp = y
            while yTemp>0:
                total += self.bit[x][yTemp]
                yTemp -= (yTemp & -yTemp)
            x -= (x & -x)
        return total
    