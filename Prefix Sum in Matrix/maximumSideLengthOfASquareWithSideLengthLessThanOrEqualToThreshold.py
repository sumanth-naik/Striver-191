# Key Idea: We only need to increment size of square by one each time.

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        maxSize, prefixSumMat = 0, [[0 for _ in range(n+1)] for _ in range(m+1)] 
        for i in range(1, m+1):
            for j in range(1, n+1):
                prefixSumMat[i][j] += mat[i-1][j-1] + prefixSumMat[i-1][j] + prefixSumMat[i][j-1] - prefixSumMat[i-1][j-1]
                if i-maxSize>0 and j-maxSize>0 and (prefixSumMat[i][j]-\
                                                    prefixSumMat[i-maxSize-1][j]-\
                                                    prefixSumMat[i][j-maxSize-1]+\
                                                    prefixSumMat[i-maxSize-1][j-maxSize-1])<=threshold:
                    maxSize+=1
        return maxSize