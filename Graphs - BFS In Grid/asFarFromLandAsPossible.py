class Solution:
    def maxDistance(self, grid):
        m, n = len(grid), len(grid[0])
        level = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    level.append((i,j))
        
        if len(level)==m*n or len(level)==0:
            return -1

        numLevels = -1
        visited = set()
        while level:
            nextLevel = []
            for node in level:
                for dx, dy in [(0,1), (0,-1), (-1,0), (1,0)]:
                    neighX, neighY = node[0] + dx, node[1] + dy
                    if 0<=neighX<m and 0<=neighY<n and grid[neighX][neighY]==0 and (neighX, neighY) not in visited:
                        visited.add((neighX, neighY))
                        nextLevel.append((neighX, neighY))
            numLevels += 1
            level = nextLevel
        return numLevels