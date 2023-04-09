class Solution:
    def cherryPickup(self, grid) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def memoization(i1, j1, i2, j2):
            if not(0<=i1<m) or not(0<=i2<m) or not(0<=j1<n) or not(0<=j2<n): return 0
            numCherries = 0
            if i1==i2 and j1==j2: numCherries += grid[i1][j1]
            else: numCherries += (grid[i1][j1] + grid[i2][j2])
            maxInNextStep = 0
            for dj1 in [-1,0,1]:
                for dj2 in [-1,0,1]:
                    maxInNextStep = max(maxInNextStep, memoization(i1+1, j1+dj1, i2+1, j2+dj2))
            return maxInNextStep + numCherries
        return memoization(0,0,0,n-1)
    
class Solution:
    def cherryPickup(self, grid) -> int:
        m, n = len(grid), len(grid[0])

        dpIPlusOneCherries = None
        for i in range(m-1, -1, -1):
            dpCurrentCherries = [[0]*n for _ in range(n)]
            for j1 in range(n):
                for j2 in range(n):
                    if j1==j2: dpCurrentCherries[j1][j2] += grid[i][j1]
                    else: dpCurrentCherries[j1][j2] += (grid[i][j1] + grid[i][j2])
                    maxCherries = 0
                    if (0<=i+1<m):
                        for dj1 in [-1,0,1]:
                            for dj2 in [-1,0,1]:
                                if (0<=j1+dj1<n) and (0<=j2+dj2<n):
                                    maxCherries = max(maxCherries, dpIPlusOneCherries[j1+dj1][j2+dj2])
                    dpCurrentCherries[j1][j2] += maxCherries
            dpIPlusOneCherries = dpCurrentCherries
        return dpIPlusOneCherries[0][n-1]