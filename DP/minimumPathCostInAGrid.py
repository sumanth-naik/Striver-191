class Solution:
    def minPathCost(self, grid, moveCost) -> int:
        m, n = len(grid), len(grid[0])
        dpArrOfNextLevel, dpCurrentLevel = grid[-1], [0]*n
        for i in range(m-2, -1, -1):
            for j in range(n):
                dpCurrentLevel[j] = grid[i][j] + min(dpArrOfNextLevel[k]+moveCost[grid[i][j]][k] for k in range(n))
            dpArrOfNextLevel = deepcopy(dpCurrentLevel)
        return min(dpArrOfNextLevel)