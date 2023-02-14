matrix = [[2,1,3],[6,5,4],[7,8,9]]
matrix = [[-19,57],[-40,-5]]
def minFallingPathSum(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[10e10 for j in range(n+2)] for i in range(m)]
    for j in range(n):
        dp[m-1][j+1] = matrix[m-1][j] 
    for i in range(m-2, -1, -1):
        for j in range(0, n):
            dp[i][j+1] = matrix[i][j] + min([dp[i+1][j], dp[i+1][j+1], dp[i+1][j+2]])
    return min(dp[0])

print(minFallingPathSum(matrix))


