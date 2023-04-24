matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5


def searchIn2DMatrix2(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    i = 0
    j = n-1
    while(i<m and i>=0 and j<n and j>= 0):
        currVal = matrix[i][j]
        if(currVal==target):
            return True
        elif (currVal>target):
            j -= 1
        else:
            i += 1
    
    return False

print(searchIn2DMatrix2(matrix, target))