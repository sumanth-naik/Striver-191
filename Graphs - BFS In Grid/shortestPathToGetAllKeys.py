import heapq
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        m, n = len(grid), len(grid[0])
        start, numKeys = (None, None), 0
        locksStr, keysStr = "ABCDEF", "abcdef"

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="@":
                    start = i, j
                if grid[i][j] in keysStr: numKeys += 1
        
        exitKeysState = (1<<numKeys)-1


        # node = steps, -keys, i, j => least steps most keys first 
        minHeap = [(0, 0, start[0], start[1])]
        # (i, j, keys) -> steps
        visitedMap = {(start[0], start[1], 0):0}

        while minHeap:
            steps, keys, i, j = heapq.heappop(minHeap)
            keys = -keys

            if visitedMap[(i, j, keys)]!=steps: continue
            if grid[i][j] in keysStr: keys |= (1<<keysStr.index(grid[i][j]))
            if keys==exitKeysState: return steps

            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newI, newJ = i+di, j+dj
                if 0<=newI<m and 0<=newJ<n:
                    char = grid[newI][newJ]
                    if char!="#" and not(char in locksStr and not keys&(1<<locksStr.index(char))) \
                        and not((newI, newJ, keys) in visitedMap and visitedMap[(newI, newJ, keys)]<=steps+1):
                        visitedMap[(newI, newJ, keys)] = steps + 1
                        heapq.heappush(minHeap, (steps+1, -keys, newI, newJ))
        return -1
    

# BFS
from collections import deque
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        m, n = len(grid), len(grid[0])
        start, numKeys = (None, None), 0
        locksStr, keysStr = "ABCDEF", "abcdef"

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="@":
                    start = i, j
                if grid[i][j] in keysStr: numKeys += 1
        
        exitKeysState = (1<<numKeys)-1


        # node = steps, -keys, i, j => least steps most keys first 
        level = deque([(0, 0, start[0], start[1])])
        # (i, j, keys)
        visited = {(start[0], start[1], 0)}

        while level:
            nextLevel = deque()
            for steps, keys, i, j in level:
                keys = -keys

                if grid[i][j] in keysStr: keys |= (1<<keysStr.index(grid[i][j]))
                if keys==exitKeysState: return steps

                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    newI, newJ = i+di, j+dj
                    if 0<=newI<m and 0<=newJ<n:
                        char = grid[newI][newJ]
                        if char!="#" and not(char in locksStr and not keys&(1<<locksStr.index(char))) and (newI, newJ, keys) not in visited:
                            visited.add((newI, newJ, keys))
                            nextLevel.append((steps+1, -keys, newI, newJ))
            level = nextLevel
        return -1