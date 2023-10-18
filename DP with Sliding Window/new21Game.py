class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp, probsSum = deque([1 if numCards<=n else 0 for numCards in range(k, k+maxPts)]), min(maxPts, n-k+1)
        for _ in range(k):
            dp.appendleft(probsSum/maxPts)
            probsSum +=  dp[0] - dp.pop()
        return dp[0]