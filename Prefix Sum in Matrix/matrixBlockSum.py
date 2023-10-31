#Key Idea: Use Prefix sum on matrix.

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        prefixSumMat = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                prefixSumMat[i][j] = mat[i-1][j-1] + prefixSumMat[i-1][j] + \
                                     prefixSumMat[i][j-1] - prefixSumMat[i-1][j-1]
        
        squareSumMat = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                squareSumMat[i][j] = prefixSumMat[min(i+k+1, m)][min(j+k+1, n)] - \
                                     prefixSumMat[max(i-k, 0)][min(j+k+1, n)] - \
                                     prefixSumMat[min(i+k+1, m)][max(j-k, 0)] + \
                                     prefixSumMat[max(i-k, 0)][max(j-k, 0)]
        
        return squareSumMat
        

        
# Key Idea: Use sliding window in each col first. Then on each row.

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        colsSumMat = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            currSum = sum(mat[i][j] for i in range(min(k+1, m)))
            colsSumMat[0][j] = currSum
            for i in range(1, m):
                currSum += (mat[i+k][j] if 0<=i+k<m else 0) - (mat[i-k-1][j] if 0<=i-k-1<m else 0)
                colsSumMat[i][j] = currSum

        colsAndRowsSumMat = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            currSum = sum(colsSumMat[i][j] for j in range(min(k+1, n)))
            colsAndRowsSumMat[i][0] = currSum
            for j in range(1, n):
                currSum += (colsSumMat[i][j+k] if 0<=j+k<n else 0) - (colsSumMat[i][j-k-1] if 0<=j-k-1<n else 0)
                colsAndRowsSumMat[i][j] = currSum
            
        return colsAndRowsSumMat
