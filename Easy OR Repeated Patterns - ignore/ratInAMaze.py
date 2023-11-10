class Solution:
    def ratInAMaze(self, matrix, n):
        if not matrix[0][0]: return []

        path = ["D","L","R","U"]
        ansArr, visitedMatrix = [], [[0 for _ in range(n)] for _ in range(n)]
        visitedMatrix[0][0] = 1

        def ratInAMaze(i, j, matrix, n, ansArr, ansPath, visitedMatrix):
            if i==n-1 and j==n-1:
                ansArr.append(''.join(ansPath))
            else:    
                for index, di, dj in enumerate([[0,1], [1,0], [-1,0], [0,-1]]):
                    newI, newJ = i+di, j+dj
                    if 0<=newI<n and 0<=newJ<n and matrix[newI][newJ]==1 and visitedMatrix[newI][newJ]==0:
                        visitedMatrix[newI][newJ] = 1
                        ansPath.append(path[index])
                        ratInAMaze(newI, newJ, matrix, n, ansArr, ansPath, visitedMatrix)
                        ansPath.pop()
                        visitedMatrix[newI][newJ] = 0
                    
        ratInAMaze(0, 0, matrix, n, ansArr, [], visitedMatrix)
        return ansArr
    