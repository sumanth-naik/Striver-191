

grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]

m = len(grid)
n = len(grid[0])

outputArr = [-1 for x in range(n)]

for ballIndex in range(n):
    i = 0
    j = ballIndex
    
    while(i<m):
        if(0<=j+grid[i][j]<n and grid[i][j] == grid[i][j+grid[i][j]]):
            j = j + grid[i][j]
            i += 1
        else:
            break
        
    if(i==m):
        outputArr[ballIndex] = j
        
print(outputArr)