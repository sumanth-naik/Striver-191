matrix = [[2,1,3],[6,5,4],[7,8,9]]
matrix = [[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]]

def minFallingPathSum2(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[10e10 for j in range(n+2)] for i in range(m)]
    for j in range(n):
        dp[m-1][j+1] = matrix[m-1][j] 
    for i in range(m-2, -1, -1):
        min1, min2 = None, None
        for j in range(0, n):
            if not min1 or min1[0]>dp[i+1][j+1]:
                min1 = (dp[i+1][j+1], j)
        for j in range(0, n):
            if (not min2 or min2[0]>dp[i+1][j+1]) and min1[1]!=j:
                min2 = (dp[i+1][j+1], j)
        # print(min1, min2, dp[i+1])
        for j in range(0, n):
            if min1[1]!=j:
                dp[i][j+1] = min1[0] + matrix[i][j]
            else:
                dp[i][j+1] = min2[0] + matrix[i][j]

    return min(dp[0])

print(minFallingPathSum2(matrix))
matrix = [[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]]
