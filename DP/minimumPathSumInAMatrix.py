

grid = [[1,2,3],[4,5,6]]

def minPathSum(i,j,m,n,grid,dp):
    if(i==m or j==n):
        return 1e9
    if(i==m-1 and j==n-1):
        return grid[i][j]

    if(dp[i][j]==-1):
        dp[i][j] = grid[i][j] + min(minPathSum(i+1, j, m, n, grid, dp), minPathSum(i, j+1, m, n, grid, dp))
    return dp[i][j]

m = len(grid)
n = len(grid[0])
dp = [[-1 for j in range(n)] for i in range(m)]
print(minPathSum(0,0,m,n,grid,dp))


dp = [[1e9 for j in range(n+1)] for i in range(m+1)]
dp[m][n-1] = 0
for i in range(m-1,-1,-1):
    for j in range(n-1,-1,-1):
        dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
print(dp[0][0])



dp1 = [1e9 for j in range(n+1)]
dp2 = [1e9 for j in range(n+1)]

dp2[n-1] = 0
for i in range(m-1,-1,-1):
    for j in range(n-1,-1,-1):
        dp1[j] = grid[i][j] + min(dp2[j], dp1[j+1])
    dp2 = dp1
    dp1 = [1e9 for j in range(n+1)]

print(dp2[0])
