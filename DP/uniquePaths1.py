
m = 6
n = 4
#m+n-2 C m-1

num = 1
den = 1
for k in range(n-1,0,-1):
    num = num*(m-1+k)
    den = den * k

print(int(num/den))
        
        
        
def uniquePaths(i,j,m,n):
    if(i==m or j==n):
        return 0
    if(i==m-1 and j==n-1):
        return 1
    return uniquePaths(i+1,j,m,n) + uniquePaths(i,j+1,m,n)

print(uniquePaths(0, 0, m, n))




def uniquePaths(i,j,m,n,dp):
    if(i==m or j==n):
        return 0
    if(i==m-1 and j==n-1):
        return 1
    if(dp[i][j]==-1):
        dp[i][j] =  uniquePaths(i+1,j,m,n,dp) + uniquePaths(i,j+1,m,n,dp)
    return dp[i][j]

dp = [[-1 for j in range(n)] for i in range(m)] 
print(uniquePaths(0, 0, m, n, dp))




dp = [[0 for j in range(n+1)] for i in range(m+1)]
dp[m-1][n] = 1
for i in range(m-1, -1, -1):
    for j in range(n-1,-1,-1):
        dp[i][j] = dp[i+1][j] + dp[i][j+1]
print(dp[0][0])



dp1 = [0 for j in range(n+1)]
dp2 = [0 for j in range(n+1)]
dp2[n-1] = 1
for i in range(m-1, -1, -1):
    for j in range(n-1,-1,-1):
        dp1[j] = dp2[j] + dp1[j+1]
    dp2 = dp1
        
print(dp1[0])



        































