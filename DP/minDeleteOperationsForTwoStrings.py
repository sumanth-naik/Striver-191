
def minDeleteOperationsForTwoStrings(word1, word2, i, j, dp):
    if i==len(word1):
        return len(word2) - j
    if j==len(word2):
        return len(word1) - i

    if dp[i][j]!=-1:
        return dp[i][j]

    if word1[i]==word2[j]:
        dp[i][j] = minDeleteOperationsForTwoStrings(word1, word2, i+1, j+1)
    else:
        dp[i][j] =  1 + min(minDeleteOperationsForTwoStrings(word1, word2, i+1, j), minDeleteOperationsForTwoStrings(word1, word2, i, j+1))
    return dp[i][j]

word1, word2 = "",""
dp = [[-1 for j in range(len(word2))] for i in range(len(word1))]
minDeleteOperationsForTwoStrings(word1, word2, 0, 0, dp)