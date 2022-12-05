matrix =[[1,1,1],[0,0,1],[1,1,1]]

m = len(matrix)
n = len(matrix[0])
rowZeroVal = 1

for row in range(0, m):
    for col in range(0, n):
        if(matrix[row][col]==0):
            if(row==0):
                rowZeroVal = 0
            else:
                matrix[row][0] = 0
            matrix[0][col] = 0
            
for row in range(m-1, -1, -1):
    for col in range(n-1, -1, -1):
        if(row==0):
            if(rowZeroVal==0):
                matrix[row][col] = 0
        elif(matrix[row][0]==0 or matrix[0][col]==0):
            matrix[row][col] = 0

print(matrix)   



## very very tricky