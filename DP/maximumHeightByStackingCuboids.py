class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        sortedCuboids = [[0, 0, 0]] + sorted(map(sorted, cuboids))
        dp = [0 for _ in range(len(sortedCuboids))]
        for j in range(1, len(sortedCuboids)):
            for i in range(j):
                if all(sortedCuboids[i][k]<=sortedCuboids[j][k] for k in [0,1,2]):
                    dp[j] = max(dp[j], dp[i]+sortedCuboids[j][2])
        return max(dp)
