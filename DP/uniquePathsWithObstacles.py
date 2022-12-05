obstacleGrid = [[0,1],[0,0]]


def uniquePaths2(i,j,m,n,obstacleGrid):
    if(i==m or j==n or obstacleGrid[i][j]==1):
        return 0
    if(i==m-1 and j==n-1):
        return 1
    return uniquePaths2(i+1, j, m, n, obstacleGrid) + uniquePaths2(i, j+1, m, n, obstacleGrid)
print(uniquePaths2(0, 0, len(obstacleGrid), len(obstacleGrid[0]), obstacleGrid))




def uniquePaths2(i,j,m,n,obstacleGrid, dp):
    if(i==m or j==n or obstacleGrid[i][j]==1):
        return 0
    if(i==m-1 and j==n-1):
        return 1
    if(dp[i][j]==-1):
        dp[i][j] = uniquePaths2(i+1, j, m, n, obstacleGrid,dp) + uniquePaths2(i, j+1, m, n, obstacleGrid,dp)
    return dp[i][j]
    
m = len(obstacleGrid)
n = len(obstacleGrid[0])
dp = [[-1 for j in range(n)] for i in range(m)]
print(uniquePaths2(0, 0, m,n, obstacleGrid, dp))





dp = [[0 for j in range(n+1)] for i in range(m+1)]

dp[m][n-1] = 1

for i in range(m-1,-1,-1):
    for j in range(n-1,-1,-1):
        if(obstacleGrid[i][j]!=1):
            dp[i][j] = dp[i+1][j] + dp[i][j+1]
print(dp[0][0])







dp1 = [0 for j in range(n+1)]
dp2 = [0 for j in range(n+1)]
dp2[n-1] = 1

for i in range(m-1,-1,-1):
    for j in range(n-1,-1,-1):
        if(obstacleGrid[i][j]!=1):
            dp1[j] = dp2[j] + dp1[j+1]
    dp2 = dp1
    dp1 = [0 for j in range(n+1)]
print(dp2[0])






obstacleGrid = [[0,1],[0,0]]
dp1 = [0 for j in range(n+1)]
dp2 = [0 for j in range(n+1)]
dp2[n-1] = 1

for i in range(m-1,-1,-1):
    print(dp1,dp2)
    for j in range(n-1,-1,-1):
        if(obstacleGrid[i][j]!=1):
            dp1[j] = dp2[j] + dp1[j+1]
        else:
            dp1[j] = 0
    dp2,dp1 = dp1,dp2
print(dp2[0])













