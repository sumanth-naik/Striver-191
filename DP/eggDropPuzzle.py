'''

[0, 0, 0, 0, 0]
[0, 1, 1, 1, 1]
[0, 2, -, -, -]
[0, 3, -, -, -]
[0, 4, -, -, -]
[0, 5, -, -, -]




[0, 0, 0, 0, 0]
[0, 1, 1, 1, 1]
[0, 2, 2, 2, 2]
[0, 3, 2, 2, 2]
[0, 4, 3, 3, 3]
[0, 5, 3, 3, 3]

'''

n = 5
e = 4
dp = [[0 for j in range(0,e+1)] for i in range(0,n+1)]

for x in range(1,e+1):
    dp[1][x] = 1

for x in range(1,n+1):
    dp[x][1] = x

for floors in range(2,n+1):
    for eggs in range(2,e+1):
        minimumDrops = 1e9
        for currFloor in range(1,floors+1):
            temp = max(dp[currFloor - 1][eggs - 1], dp[floors - currFloor][eggs])
            minimumDrops = min(minimumDrops, temp)
        dp[floors][eggs] = 1 + minimumDrops

for x in dp:
    print(x)
    
print(dp[n][e])