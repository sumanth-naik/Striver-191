class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        dp = [[[0 for _ in range(k+1)] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dp[i][j][0] = 1

        @lru_cache(None)
        def getValidJumps(i, j):
            validIndices = []
            for di, dj in [[1,2], [1,-2], [-1,2], [-1,-2], [2,1], [-2,1], [2,-1], [-2,-1]]:
                if 0<=i+di<n and 0<=j+dj<n:
                    validIndices.append((i+di, j+dj))
            return validIndices

        for kIndex in range(1, k+1):
            for i in range(n):
                for j in range(n):
                    for iNext, jNext in getValidJumps(i, j):
                        dp[iNext][jNext][kIndex] += dp[i][j][kIndex-1]
        
        return dp[row][column][k]/8**k
    

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        @lru_cache(None)
        def getValidJumps(i, j):
            validIndices = []
            for di, dj in [[1,2], [1,-2], [-1,2], [-1,-2], [2,1], [-2,1], [2,-1], [-2,-1]]:
                if 0<=i+di<n and 0<=j+dj<n:
                    validIndices.append((i+di, j+dj))
            return validIndices

        @lru_cache(None)
        def recursion(i, j, currK):
            return sum(recursion(iNext, jNext, currK-1) for iNext, jNext in getValidJumps(i, j)) if currK!=0 else 1
        
        return recursion(row, column, k)/8**k