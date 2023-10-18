
class BIT2D:
    def __init__(self, m, n) -> None:
        self.m = m+1
        self.n = n+1
        self.bit = defaultdict(lambda:defaultdict(int))

    def insert(self, x, y, val):
        x += 1
        y += 1
        while x<=self.m: # points on line also needs to be updated
            yTemp = y
            while yTemp<=self.n:
                self.bit[x][yTemp] += val
                yTemp += (yTemp & -yTemp)
            x += (x & -x)
        
    # 1 indexed
    @lru_cache(None)
    def pointsTill(self, x, y):
        total = 0
        while x>0:
            yTemp = y
            while yTemp>0:
                total += self.bit[x][yTemp]
                yTemp -= (yTemp & -yTemp)
            x -= (x & -x)
        return total
    
    def pointsGreaterThan(self, x, y):
        return self.pointsTill(self.m, self.n) - self.pointsTill(x, self.n) - self.pointsTill(self.m, y) + self.pointsTill(x, y)


class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        m, n = max(x for x,y in rectangles), max(y for x,y in rectangles)
        bit = BIT2D(m, n)

        for x,y in rectangles:
            bit.insert(x,y,1)

        ansArr = []
        for x,y in points:
            if x>m or y>n: ansArr.append(0)
            else: ansArr.append(bit.pointsGreaterThan(x,y))
        return ansArr

from sortedcontainers import SortedDict
from sortedcontainers import SortedList
from bisect import bisect_left
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        sortedDictOfYToX = SortedDict()
        for x, y in rectangles:
            sortedDictOfYToX.setdefault(y,SortedList()).add(x)
        
        sortedDictKeys, ansArr = sortedDictOfYToX.keys(), []

        for x, y in points:
            index, count = bisect_left(sortedDictKeys, y), 0
            for sortedKeysIndex in range(index, len(sortedDictKeys)):
                xList = sortedDictOfYToX[sortedDictKeys[sortedKeysIndex]]
                count += (len(xList)-bisect_left(xList, x))
            ansArr.append(count)
        
        return ansArr

        