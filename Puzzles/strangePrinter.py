class Solution:
    def strangePrinter(self, s: str) -> int:

        @lru_cache(None)
        def recursion(i, j):
            if i==j: return 1
            minPrints = min(recursion(i, k) + recursion(k+1, j) for k in range(i, j))
            return minPrints if s[i]!=s[j] else minPrints-1
            
        return recursion(0, len(s)-1)
    
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n): dp[i][i] = 1
        for delta in range(1, n):
            for startIndex in range(n-delta):
                i, j = startIndex, startIndex+delta
                minPrints = min(dp[i][k] + dp[k+1][j] for k in range(i, j))
                dp[i][j] = minPrints if s[i]!=s[j] else minPrints-1
        return dp[0][n-1]

                