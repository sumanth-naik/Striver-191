
matrix = [[1]]
target = 1
m = len(matrix)
n = len(matrix[0])
def getMatrixIndex(num, m, n):
    i = num//n
    j = num%n
    return (i,j)
    
def binarySearchOnMatrix(matrix, target, m, n, low, high):
   
    while(low<high):
        mid = (low + high)//2
        
        midIndex = getMatrixIndex(mid, m, n)
        print(midIndex)
        midVal = matrix[midIndex[0]][midIndex[1]]
        if(midVal==target):
            return True
        elif(midVal>target):
            high = mid
        else:
            low = mid + 1
    
    if(low<=m*n-1 and matrix[low//n][low%n]==target):
        return True
    
    return False
    
print(binarySearchOnMatrix(matrix, target, m, n, 0, m*n-1))