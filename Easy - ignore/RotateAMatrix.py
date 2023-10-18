
matrix = [[1,2,3],[4,5,6],[7,8,9]]

def transpose(matrix, m, n):
    for i in range(1, m):
        for j in range(0, i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
            

def reverseEachRow(matrix, n):
    for row in matrix:
        for i in range(0, (n-1)//2 +1):
            row[i], row[n-1-i] = row[n-1-i], row[i]
            

m = len(matrix)
n = len(matrix[0])
transpose(matrix, m, n)
reverseEachRow(matrix, n)
print(matrix)