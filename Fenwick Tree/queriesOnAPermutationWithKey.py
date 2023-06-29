class BIT:
    def __init__(self, m):
        self.bit = [0 for _ in range(2*m+1)]
        for num in range(1, m+1):
            self.update(m+num-1, 0, 1)

    def update(self, index, oldVal, newVal):
        val = newVal - oldVal
        index += 1
        while index<len(self.bit):
            self.bit[index] += val
            index += index & (-index)

    def getSumTill(self, index):
        index += 1
        total = 0
        while index>0:
            total += self.bit[index] 
            index -= index & (-index)
        return total

    def getSumInRange(self, left, right):
        return self.getSumTill(right) - self.getSumTill(left-1)


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        bit = BIT(m)
        numToPrevIndexMap = {}
        for num in range(1, m+1):
            numToPrevIndexMap[num] = m+num-1

        firstIndex = m
        for query in queries:
            yield bit.getSumInRange(firstIndex, numToPrevIndexMap[query]) - 1
            bit.update(numToPrevIndexMap[query], 1, 0)
            firstIndex -= 1
            numToPrevIndexMap[query] = firstIndex
            bit.update(firstIndex, 0, 1)


class SegmentTree:
    def __init__(self, m) -> None:
        self.size = 2*m
        self.tree = [0 for _ in range(4*self.size)]
        for num in range(1, m+1):
            self.update(m+num-1, 1)

    def _update(self, nodeIndex, nodeLeft, nodeRight, numsIndex, val):
        if numsIndex<nodeLeft or nodeRight<numsIndex:
            return
        if nodeLeft==nodeRight==numsIndex:
            self.tree[nodeIndex] = val
            return
        mid = (nodeLeft+nodeRight)//2
        if numsIndex<=mid:
            self._update(2*nodeIndex+1, nodeLeft, mid, numsIndex, val)
        else:
            self._update(2*nodeIndex+2, mid+1, nodeRight, numsIndex, val)
        self.tree[nodeIndex] = self.tree[2*nodeIndex+1] + self.tree[2*nodeIndex+2]
    
    def update(self, index, val):
        self._update(0, 0, self.size-1, index, val)

    def _getSumInRange(self, nodeIndex, nodeLeft, nodeRight, queryLeft, queryRight):
        if nodeRight<queryLeft or queryRight<nodeLeft:
            return 0
        if queryLeft<=nodeLeft and nodeRight<=queryRight:
            return self.tree[nodeIndex]
        mid = (nodeLeft+nodeRight)//2
        return self._getSumInRange(2*nodeIndex+1, nodeLeft, mid, queryLeft, queryRight) + self._getSumInRange(2*nodeIndex+2, mid+1, nodeRight, queryLeft, queryRight)

    def getSumInRange(self, queryLeft, queryRight):
        return self._getSumInRange(0, 0, self.size-1, queryLeft, queryRight)
    

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        segmentTree = SegmentTree(m)
        numToPrevIndexMap = {}
        for num in range(1, m+1):
            numToPrevIndexMap[num] = m+num-1
        
        firstIndex = m
        for query in queries:
            yield segmentTree.getSumInRange(firstIndex, numToPrevIndexMap[query]) - 1 
            segmentTree.update(numToPrevIndexMap[query], 0)
            firstIndex -= 1
            segmentTree.update(firstIndex, 1)
            numToPrevIndexMap[query] = firstIndex