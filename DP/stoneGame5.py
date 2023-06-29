class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:

        @lru_cache(None)
        def recursion(i, j):
            if i==j: return 0
            maxSeen = 0
            for k in range(i,j):
                sumLeft, sumRight = sum(stoneValue[i:k+1]), sum(stoneValue[k+1:j+1])
                if sumLeft<sumRight:
                    maxSeen = max(maxSeen, sumLeft + recursion(i, k))
                elif sumLeft>sumRight:
                    maxSeen = max(maxSeen, sumRight + recursion(k+1, j))
                else:
                    maxSeen = max(maxSeen, sumLeft + recursion(i, k), sumRight + recursion(k+1, j))
            return maxSeen
        
        return recursion(0, len(stoneValue)-1)
    
class BIT:
    def __init__(self, stoneValues) -> None:
        self.size = len(stoneValues)+1
        self.bit = [0 for _ in range(self.size)]
        for index, val in enumerate(stoneValues):
            self.add(index+1, val)

    def add(self, index, val):
        while index<self.size:
            self.bit[index] += val
            index += (index & -index)

    def sumTill(self, index):
        total = 0
        while index>0:
            total += self.bit[index]
            index -= (index & -index)
        return total
    
    @lru_cache(None)
    def rangeSum(self, left, right):
        return self.sumTill(right+1) - self.sumTill(left)



class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        bit = BIT(stoneValue)

        @lru_cache(None)
        def recursion(i, j):
            if i==j: return 0
            maxSeen = 0
            for k in range(i,j):
                sumLeft, sumRight = bit.rangeSum(i,k), bit.rangeSum(k+1,j)
                if sumLeft<sumRight:
                    maxSeen = max(maxSeen, sumLeft + recursion(i, k))
                elif sumLeft>sumRight:
                    maxSeen = max(maxSeen, sumRight + recursion(k+1, j))
                else:
                    maxSeen = max(maxSeen, sumLeft + recursion(i, k), sumRight + recursion(k+1, j))
            return maxSeen
        
        return recursion(0, len(stoneValue)-1)



class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefixSum = [0]
        for val in stoneValue:
            prefixSum.append(val+prefixSum[-1])

        @lru_cache(None)
        def recursion(i, j):
            if i==j: return 0
            maxSeen = 0
            for k in range(i,j):
                sumLeft, sumRight = prefixSum[k+1]-prefixSum[i], prefixSum[j+1]-prefixSum[k+1]
                if sumLeft<sumRight:
                    maxSeen = max(maxSeen, sumLeft + recursion(i, k))
                elif sumLeft>sumRight:
                    maxSeen = max(maxSeen, sumRight + recursion(k+1, j))
                else:
                    maxSeen = max(maxSeen, sumLeft + recursion(i, k), sumRight + recursion(k+1, j))
            return maxSeen
        
        return recursion(0, len(stoneValue)-1)




class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefixSum = [0]
        for val in stoneValue:
            prefixSum.append(val+prefixSum[-1])

        def getSumInRange(i, j):
            return prefixSum[j+1]-prefixSum[i]
        
        # can not get last index where left is smaller, as there might not be any
        # Do first index where left is greater or equal instead
        @lru_cache(None)
        def getTransitionIndex(i, j):
            low, high = i, j
            while low<high:
                mid = (low+high)//2
                if getSumInRange(i, mid)<getSumInRange(mid+1, j): 
                    low = mid + 1
                else:
                    high = mid
            return low
        
        def left(i, j):
            return 0 if i>j else max(getSumInRange(i, k) + recursion(i, k) for k in range(i, j+1))
        
        def right(i, j):
            return 0 if i>j else max(getSumInRange(k, j) + recursion(k, j) for k in range(i, j+1))

        @lru_cache(None)
        def recursion(i, j):
            if i==j: return 0
            k = getTransitionIndex(i, j)
            return max(left(i, k), right(k+1,j)) if getSumInRange(i,k)==getSumInRange(k+1,j) else max(left(i, k-1), right(k+1,j))
            
        return recursion(0, len(stoneValue)-1)





class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefixSum = [0]
        for val in stoneValue:
            prefixSum.append(val+prefixSum[-1])

        def getSumInRange(i, j):
            return prefixSum[j+1]-prefixSum[i]
        
        # can not get last index where left is smaller, as there might not be any
        # Do first index where left is greater or equal instead
        @lru_cache(None)
        def getTransitionIndex(i, j):
            low, high = i, j
            while low<high:
                mid = (low+high)//2
                if getSumInRange(i, mid)<getSumInRange(mid+1, j): 
                    low = mid + 1
                else:
                    high = mid
            return low
        
        @lru_cache(None)
        def left(i, j):
            return 0 if i>j else max(left(i, j-1), getSumInRange(i, j) + recursion(i, j))
        
        @lru_cache(None)
        def right(i, j):
            return 0 if i>j else max(right(i+1, j), getSumInRange(i, j) + recursion(i, j))

        @lru_cache(None)
        def recursion(i, j):
            if i==j: return 0
            k = getTransitionIndex(i, j)
            return max(left(i, k), right(k+1,j)) if getSumInRange(i,k)==getSumInRange(k+1,j) else max(left(i, k-1), right(k+1,j))
            
        return recursion(0, len(stoneValue)-1)

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefixSum = [0]
        for val in stoneValue:
            prefixSum.append(val+prefixSum[-1])

        def getSumInRange(i, j):
            return prefixSum[j+1]-prefixSum[i]
        
        # can not get last index where left is smaller, as there might not be any
        # Do first index where left is greater or equal instead
        @lru_cache(None)
        def getTransitionIndex(i, j):
            low, high = i, j
            while low<high:
                mid = (low+high)//2
                if getSumInRange(i, mid)<getSumInRange(mid+1, j): 
                    low = mid + 1
                else:
                    high = mid
            return low
        
        @lru_cache(None)
        def left(i, j):
            return 0 if i>j else max(left(i, j-1), getSumInRange(i, j) + recursion(i, j))
        
        @lru_cache(None)
        def right(i, j):
            return 0 if i>j else max(right(i+1, j), getSumInRange(i, j) + recursion(i, j))

        @lru_cache(None)
        def recursion(i, j):
            if i==j: return 0
            k = getTransitionIndex(i, j)
            return max(left(i, k), right(k+1,j)) if getSumInRange(i,k)==getSumInRange(k+1,j) else max(left(i, k-1), right(k+1,j))
            
        return recursion(0, len(stoneValue)-1)



class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefixSum = [0]
        for val in stoneValue:
            prefixSum.append(val+prefixSum[-1])

        def getSumInRange(i, j):
            return prefixSum[j+1]-prefixSum[i]
        
        def getTransitionIndex(i, j):
            low, high = i, j
            while low<high:
                mid = (low+high)//2
                if getSumInRange(i, mid)<getSumInRange(mid+1, j):
                    low = mid + 1
                else:
                    high = mid
            return low
        
        n = len(stoneValue)
        dpOfScores = [[0 for _ in range(n)] for _ in range(n)]
        dpOfLefts = [[0 for _ in range(n)] for _ in range(n)]
        dpOfRights = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dpOfLefts[i][i] = dpOfRights[i][i] = stoneValue[i]

        for delta in range(1, n):
            for startIndex in range(n-delta):
                i, j = startIndex, startIndex+delta
                k = getTransitionIndex(i, j)
                if getSumInRange(i, k)==getSumInRange(k+1,j):
                    dpOfScores[i][j] = max(dpOfLefts[i][k], dpOfRights[k+1][j] if k+1<n else 0)
                else:
                    dpOfScores[i][j] = max(dpOfLefts[i][k-1] if k-1>=0 else 0, dpOfRights[k+1][j] if k+1<n else 0)
                dpOfLefts[i][j] = max(dpOfLefts[i][j-1], getSumInRange(i, j)+dpOfScores[i][j])
                dpOfRights[i][j] = max(dpOfRights[i+1][j], getSumInRange(i, j)+dpOfScores[i][j])

        return dpOfScores[0][-1]
    


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefixSum = [0]
        for val in stoneValue:
            prefixSum.append(val+prefixSum[-1])

        def getSumInRange(i, j):
            return prefixSum[j+1]-prefixSum[i]
        
        n = len(stoneValue)
        dpOfScores = [[0 for _ in range(n)] for _ in range(n)]
        dpOfLefts = [[0 for _ in range(n)] for _ in range(n)]
        dpOfRights = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dpOfLefts[i][i] = dpOfRights[i][i] = stoneValue[i]
        
        for delta in range(1, n):
            k = 0
            for startIndex in range(n-delta):
                i, j = startIndex, startIndex+delta
                while getSumInRange(i, k)<getSumInRange(k+1, j): k += 1
                if getSumInRange(i, k)==getSumInRange(k+1,j):
                    dpOfScores[i][j] = max(dpOfLefts[i][k], dpOfRights[k+1][j] if k+1<n else 0)
                else:
                    dpOfScores[i][j] = max(dpOfLefts[i][k-1] if k-1>=0 else 0, dpOfRights[k+1][j] if k+1<n else 0)
                dpOfLefts[i][j] = max(dpOfLefts[i][j-1], getSumInRange(i, j)+dpOfScores[i][j])
                dpOfRights[i][j] = max(dpOfRights[i+1][j], getSumInRange(i, j)+dpOfScores[i][j])

        return dpOfScores[0][-1]