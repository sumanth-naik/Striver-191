class Solution:
    def countSquares(self, matrix):
        m, n = len(matrix), len(matrix[0])

        def isValid(i, j, lastSquareSize):
            if 0<=i<m and 0<=j<n and matrix[i][j]==lastSquareSize:
                return True
            return False
        
        for squareSize in range(2, min(m, n)+1):
            changed = False
            for i in range(m):
                for j in range(n):
                    if isValid(i,j, squareSize-1) and isValid(i+1, j, squareSize-1) and isValid(i, j+1, squareSize-1) and isValid(i+1, j+1, squareSize-1):
                        matrix[i][j] += 1
                        changed = True
            if not changed: break
        numSquares = 0
        for row in matrix:
            numSquares += sum(row)
        return numSquares
    
    
class Solution:
    def countSquares(self, matrix):
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j]:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
        return sum(map(sum, matrix))