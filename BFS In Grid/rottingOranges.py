
from collections import deque
def rottingOranges(grid):
    queue = deque()
    visited = set()
    m, n = len(grid), len(grid[0])
    numOrangesLeftToRot = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]==2:
                visited.add((i,j))
                queue.append((i,j,0))
            elif grid[i][j]==1:
                numOrangesLeftToRot += 1
    maxNumDays = 0
    while queue:
        i,j,numDays = queue.popleft()
        maxNumDays = max(maxNumDays, numDays)
        for neigh in [(i,j+1), (i+1,j), (i-1,j), (i,j-1)]:
            if 0<=neigh[0]<m and 0<=neigh[1]<n and neigh not in visited and grid[neigh[0]][neigh[1]]==1:
                visited.add(neigh)
                queue.append((neigh[0], neigh[1], numDays+1))
                numOrangesLeftToRot -= 1
        
    return maxNumDays if numOrangesLeftToRot==0 else -1