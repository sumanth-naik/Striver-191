class Solution:
    def longestIncreasingPath(self, matrix):
        m, n = len(matrix), len(matrix[0])
        memo = {}
        def recursiveDfsWithMemo(i, j):
            nonlocal memo
            if not (i, j) in memo: 
                memo[(i,j)] = 0
                for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                    if 0<=i+di<m and 0<=j+dj<n and matrix[i][j]<matrix[i+di][j+dj]:
                        memo[(i,j)] = max(memo[(i,j)], recursiveDfsWithMemo(i+di, j+dj)+1)
            return memo[(i,j)]
        
        maxPathLengthInEntireMatrix = 0
        for i in range(m):
            for j in range(n):
                maxPathLengthInEntireMatrix = max(maxPathLengthInEntireMatrix, recursiveDfsWithMemo(i, j))
        return maxPathLengthInEntireMatrix + 1