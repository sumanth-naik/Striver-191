class Solution:
    def maxSumAfterPartitioning(self, arr, k: int) -> int:
        
        dpArr = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]
        def memoization(i, j):
            nonlocal dpArr
            if dpArr[i][j]!=-1: return dpArr[i][j]

            if j-i+1<=k: dpArr[i][j] = max(arr[i:j+1]) * (j-i+1)
            else:
                for partition in range(i, j):
                    dpArr[i][j] = max(dpArr[i][j], memoization(i,partition) + memoization(partition+1,j))
            return dpArr[i][j]

        return memoization(0,len(arr)-1)
                    
class Solution:
    def maxSumAfterPartitioning(self, arr, k: int) -> int:
        memo = defaultdict(int)
        def memoization(i):
            nonlocal memo
            if i in memo: return memo[i]
            for j in range(i, min(len(arr), i+k)):
                memo[i] = max(memo[i], max(arr[i:j+1])*(j-i+1) + memoization(j+1))
            return memo[i]

        return memoization(0)
                    
                
class Solution:
    def maxSumAfterPartitioning(self, arr, k: int) -> int:
        dp = [0 for _ in range(len(arr)+1)]
        for i in range(len(arr)-1, -1, -1):
            currMax = 0
            for j in range(i, min(len(arr), i+k)):
                currMax = max(currMax, arr[j])
                dp[i] = max(dp[i], currMax*(j-i+1) + dp[j+1])
        return dp[0]
                         