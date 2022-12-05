
grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]


def findEdgeIslands(visited, i,j, grid, numOnesVisited):
    for pos in [(i+1,j), (i-1,j), (i, j+1), (i, j-1)]:
        if pos[0]>0 and pos[1]>0 and pos[0]<len(grid) and pos[1]<len(grid[0]) and grid[pos[0]][pos[1]] and pos not in visited:
            visited.add(pos)
            findEdgeIslands(visited, pos[0], pos[1], grid, numOnesVisited)
            if grid[pos[0]][pos[1]]==1:
                numOnesVisited[0] += 1

def callFindEdgeIslandsIfNecessary(visited,i,j,grid,numOnesVisited):
    if grid[i][j]==1 and (i,j) not in visited:
        numOnesVisited[0] += 1
        visited.add((i,j))
        findEdgeIslands(visited, i,j, grid, numOnesVisited)

def numEnclaves(grid):
    totalOnes = 0
    for row in grid:
        totalOnes += sum(row)

    m = len(grid)
    n = len(grid[0])
    visited = set()
    numOnesVisited = [0]
    for i in range(0,m):
        for j in [0, n-1]:
            callFindEdgeIslandsIfNecessary(visited,i,j,grid,numOnesVisited)
    for j in range(0,n):
        for i in [0, m-1]:
            callFindEdgeIslandsIfNecessary(visited,i,j,grid,numOnesVisited)

    return totalOnes-numOnesVisited[0]


print(numEnclaves(grid))