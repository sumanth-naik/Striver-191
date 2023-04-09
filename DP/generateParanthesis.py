class Solution:
    def generateParenthesis(self, n: int):
        dp = [[] for _ in range(n+1)]
        dp[0] = [""]
        dp[1].append("()")
        for i in range(2, n+1):
            for k in range(0, i):
                for partOne in dp[k]:
                    for partTwo in dp[i-k-1]:
                        dp[i].append("(" + partOne + ")" +partTwo)
        return dp[n]
