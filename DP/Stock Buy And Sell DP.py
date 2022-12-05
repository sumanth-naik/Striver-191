arr = [3,3,5,0,0,3,1,4]
rows = 2
cols = len(arr)+1

'''

0 -> Buy Mode
1 -> Sell Mode

'''

#Leet code 2
dp = [ [ 0 for i in range(cols) ] for j in range(rows)]
      
for i in range(len(arr)-1,-1,-1):
    dp[0][i] = max(dp[0][i+1], dp[1][i+1] - arr[i])
    dp[1][i] = max(dp[1][i+1], dp[0][i+1] + arr[i])

print(dp[0])
print(dp[1])
print(dp[0][0])


#LeetCode 2 space optimized

dp0 = 0
dp1 = 0

for i in range(len(arr)-1,-1,-1):
    temp = max(dp0, dp1 - arr[i])
    dp1 = max(dp1, dp0 + arr[i])
    dp0 = temp
    
print(dp0)

# max k transcations Leet code 3 and 4
max_transactions = 2
dp = [ [ [0 for k in range(max_transactions+1) ] for j in range(cols) ] for i in range(rows)]
      
for i in range(len(arr)-1,-1,-1):
    for k in range((max_transactions), -1, -1):
        dp[0][i][k] = max(dp[0][i+1][k], dp[1][i+1][k] - arr[i])
        if(k>0):
            dp[1][i][k] = max(dp[1][i+1][k], dp[0][i+1][k-1] + arr[i])
        else:
            dp[1][i][k] = dp[1][i+1][k]
        
print(dp[0])
print(dp[1])
print(dp[0][0][max_transactions])