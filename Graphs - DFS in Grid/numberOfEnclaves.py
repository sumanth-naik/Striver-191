# Key Idea: DFS from edges

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n, visited = len(grid), len(grid[0]), set()

        def dfs(i, j):
            if not grid[i][j]: return
            visited.add((i,j))
            for di, dj in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                newI, newJ = i+di, j+dj
                if 0<=newI<m and 0<=newJ<n and grid[newI][newJ] and (newI, newJ) not in visited:
                    dfs(newI, newJ)
        
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)

        return sum(map(sum, grid)) - len(visited)