'''
m = [[1, 0, 0, 0],
    [1, 1, 0, 1], 
    [1, 1, 0, 0],
    [0, 1, 1, 1]]
n = 4

0 1 1 1 1 1 1 0 1 0 1 1 0 0 1 1
'''
m = [[0, 1, 1, 1],
    [1, 1, 1, 0], 
    [1, 0, 1, 1],
    [0, 0, 1, 1]]
n = 4

def ratInAMaze(i, j, matrix, n, ansArr, ansPath, visitedMatrix):
    
    if(i==n-1 and j==n-1):
        ansArr.append(ansPath)
        return
    
    #DLRU
    path = ["D","L","R","U"]
    changeI = [1, 0, 0, -1]
    changeJ = [0, -1, 1, 0]
    
    for changeIndex in range(0,4):
        newI = changeI[changeIndex] + i
        newJ = changeJ[changeIndex] + j
        
        if(newI<n and newJ< n and newI>=0 and newJ>=0 and matrix[newI][newJ]==1 and visitedMatrix[newI][newJ]==0):
            visitedMatrix[newI][newJ] = 1
            ratInAMaze(newI, newJ, matrix, n, ansArr, ansPath+path[changeIndex], visitedMatrix)
            visitedMatrix[newI][newJ] = 0
        
    
ansArr = []
if(not m[0][0]==0):
    visitedMatrix = [[0 for i in range(0, n)] for j in range(0, n)]
    visitedMatrix[0][0] = 1
    ratInAMaze(0, 0, m, n, ansArr, "", visitedMatrix)
    print(ansArr)
    
    
    
'''
corner cases:
    arr[0][0] is 0
    
    putting visitedMatrix[0][0] to 1 beforehand

'''
        
        