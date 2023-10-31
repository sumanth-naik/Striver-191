class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n, MOD = len(grid), len(grid[0]), 10**9+7
        dp = [[defaultdict(int) for _ in range(n+1)] for _ in range(m+1)]
        dp[m-1][n][0] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                for key in dp[i][j+1]:
                    dp[i][j][(key+grid[i][j])%k] = dp[i][j+1][key]
                for key in dp[i+1][j]:
                    dp[i][j][(key+grid[i][j])%k] += dp[i+1][j][key]
                    dp[i][j][(key+grid[i][j])%k] %= MOD
        return dp[0][0][0]