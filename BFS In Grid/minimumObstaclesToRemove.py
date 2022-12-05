from collections import deque
grid = [[0,1,1],[1,1,0],[1,1,0]]
def minimumObstaclesToRemove(grid):
    
    m = len(grid)
    n = len(grid[0])
    minNumBreaks = [[1e9 for y in range(n)] for x in range(m)]
    visited = set()
    queue = deque()
    queue.append((0,0,grid[0][0]))
    minBreaks = 1e9
    while(len(queue)>0):
        popElem = queue.popleft()
        i, j, numBreaks = popElem[0], popElem[1], popElem[2]
        if(i==m-1 and j==n-1 and minBreaks>numBreaks):
            minBreaks = numBreaks
        for di, dj in [(1,0), (0,1), (0,-1), (-1,0)]:
            if(i+di<m and i+di>=0 and j+dj<n and j+dj>=0 and not(i==m-1 and j==n-1)):
                if(grid[i+di][j+dj]==0 and (i+di, j+dj, numBreaks) not in visited and numBreaks<minNumBreaks[i+di][j+dj]):
                    elem = (i+di, j+dj, numBreaks)
                    queue.appendleft(elem)
                    visited.add(elem)
                    minNumBreaks[i+di][j+dj] = numBreaks
                elif(grid[i+di][j+dj]==1 and (i+di, j+dj, numBreaks+1) not in visited and numBreaks+1<minNumBreaks[i+di][j+dj]):
                    elem = (i+di, j+dj, numBreaks+1)
                    queue.append(elem)
                    visited.add(elem)
                    minNumBreaks[i+di][j+dj] = numBreaks + 1

    return minBreaks
                        
print(minimumObstaclesToRemove(grid))

'''
Optimizations learnt:
    1. Dont use weak bound. 
        a.  numBreaks <= m*n-1
        b.  numBreaks <= i + di + j + dj + 1
        Both are correct but unnecessaryily increasing time complexity
    2. Use a matrix to store the minNumBreaks that we see so far on that index. Dont add anything bigger or equal
    3. DONT use DLRU everytime. When its a matrix moving from top left to bottom right, use DRLU
    4. Add elements with least numBreaks to front of queue and with more numBreaks to last of queue

'''



