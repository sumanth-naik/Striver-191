from functools import lru_cache
class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        n = len(prices)

        @lru_cache(maxsize=2*n)
        def memoization(i, canSell):
            if i==n-1: return canSell*(prices[i]-fee)
            if canSell: return max((prices[i]-fee)+memoization(i+1, False), memoization(i+1, True))
            else: return max((-prices[i])+memoization(i+1, True), memoization(i+1, False))
        
        return memoization(0, False)
    
class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        n = len(prices)
        dp = [[1e9]*2 for _ in range(n)]
        # can not sell, can sell
        dp[n-1] = [0, prices[n-1]-fee]

        for i in range(n-2, -1, -1):
            dp[i][0] = max((-prices[i])+dp[i+1][1], dp[i+1][0])
            dp[i][1] = max((prices[i]-fee)+dp[i+1][0], dp[i+1][1])
        return dp[0][0]
    
class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        n = len(prices)
        # can not sell, can sell
        dpIPlusOne = [0, prices[n-1]-fee]

        for i in range(n-2, -1, -1):
            dpI = [0,0]
            dpI[0] = max((-prices[i])+dpIPlusOne[1], dpIPlusOne[0])
            dpI[1] = max((prices[i]-fee)+dpIPlusOne[0], dpIPlusOne[1])
            dpIPlusOne = dpI
        return dpIPlusOne[0]