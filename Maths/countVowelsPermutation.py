
n = 4

def matrixMultModK(matrix1, matrix2, mod):
    square = [[0 for j in range(5)] for i in range(5)]
    for i in range(5):
        for j in range(5):
            for k in range(5):
                square[i][j] += (matrix1[i][k] * matrix2[k][j])%mod
    return square

def matrixPowModK(matrix, n, k):
    if n==1:
        return matrix
    if n&1:
        return matrixMultModK(matrix, matrixPowModK(matrix, n-1, k), k)
    else:
        return matrixPowModK(matrixMultModK(matrix, matrix, k), n//2, k)

def countVowelPermutationWithGraphs(n):
    if n==1: return 5
    adjMatrix = [[0, 1, 0, 0, 0],
                [1, 0, 1, 0, 0],
                [1, 1, 0, 1, 1],
                [0, 0, 1, 0, 1],
                [1, 0, 0, 0, 0]]
    k = 10**9 + 7
    powAdjMatrix =  matrixPowModK(adjMatrix, n-1, k)
    count = 0
    for row in powAdjMatrix:
        for num in row:
            count = (count+num)%k
    return int(count%k)
    
print(countVowelPermutationWithGraphs(n))





'''
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

# print(countVowelsPermutation(n)) 


# for i in range(1,2000):
#     if countVowelPermutationWithGraphs(i)!=countVowelsPermutation(i):
#         print("F", i, countVowelPermutationWithGraphs(i), countVowelsPermutation(i))
#         break

import timeit
start = timeit.default_timer()
for i in range(1,10000):
    countVowelPermutationWithGraphs(i)
print(timeit.default_timer() - start)

    
# start = timeit.default_timer()
# for i in range(1,10000):
#     countVowelsPermutation(i)
# print(timeit.default_timer() - start)


8.8606408 sec O(logN)
115.7640767 sec O(N)
'''