n = 3

def countVowelsPermutation(n):
    dp = [[1 for i in range(5)]]
    a, e, i, o, u, k = 0, 1, 2, 3, 4, 10**9+7
    for index in range(1, n):
        dp.append([1 for i in range(5)])
        dp[index][a] = (dp[index-1][e] + dp[index-1][i] + dp[index-1][u])%k
        dp[index][e] = (dp[index-1][a] + dp[index-1][i])%k
        dp[index][i] = (dp[index-1][e] + dp[index-1][o])%k
        dp[index][o] = dp[index-1][i]
        dp[index][u] = (dp[index-1][i] + dp[index-1][o])%k
    return sum(dp[n-1])%k

print(countVowelsPermutation(n)) 