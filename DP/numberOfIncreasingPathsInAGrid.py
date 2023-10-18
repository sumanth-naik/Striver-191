class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        m, n, MOD = len(grid), len(grid[0]), 10**9+7
        dpArr = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            nonlocal dpArr
            dpArr[i][j] = 1
            for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                newI, newJ = i+di, j+dj
                if 0<=newI<m and 0<=newJ<n and grid[i][j]<grid[newI][newJ]:
                    if dpArr[newI][newJ]==0:
                        dfs(newI, newJ)
                    dpArr[i][j] = (dpArr[i][j]+dpArr[newI][newJ])%MOD

        for i in range(m):
            for j in range(n):
                if dpArr[i][j]==0:
                    dfs(i, j)
        
        return sum(map(sum, dpArr))%MOD
