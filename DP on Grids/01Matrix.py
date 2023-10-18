class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        outputMatrix = [[1e9 for _ in range(n)] for _ in range(m)]
        queue = deque((i, j, 0) for i in range(m) for j in range(n) if mat[i][j]==0)
        visited = set((i, j) for i in range(m) for j in range(n) if mat[i][j]==0)

        while queue:
            i, j, dist = queue.popleft()
            outputMatrix[i][j] = dist
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newI, newJ = i+di, j+dj
                if 0<=newI<m and 0<=newJ<n and (newI, newJ) not in visited:
                    visited.add((newI,newJ))
                    queue.append((newI, newJ, dist+1))
        return outputMatrix

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        outputMatrix = [[1e9 for _ in range(n)] for _ in range(m)]
        queue = deque((i, j, 0) for i in range(m) for j in range(n) if mat[i][j]==0) 
        while queue:
            i, j, dist = queue.popleft()
            outputMatrix[i][j] = dist
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newI, newJ = i+di, j+dj
                if 0<=newI<m and 0<=newJ<n and (newI, newJ) and mat[newI][newJ]!=0 and outputMatrix[newI][newJ]==1e9:
                    outputMatrix[newI][newJ] = -1
                    queue.append((newI, newJ, dist+1))
        return outputMatrix


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j]!=0: mat[i][j] = min(mat[i-1][j] if 0<=i-1<m else 1e9, mat[i][j-1] if 0<=j-1<n else 1e9)+1
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                if mat[i][j]!=0: mat[i][j] = min(mat[i][j], mat[i+1][j]+1 if 0<=i+1<m else 1e9, mat[i][j+1]+1 if 0<=j+1<n else 1e9)
        return mat
        