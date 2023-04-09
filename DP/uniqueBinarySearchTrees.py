class Solution:
    def numTrees(self, n: int) -> int:
        dpArr = [1]*(n+1)
        for i in range(2,n+1):
            dpArr[i] = sum(dpArr[k]*dpArr[i-k-1] for k in range(i))
        return dpArr[n]