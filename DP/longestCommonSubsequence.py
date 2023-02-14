
def longestCommonSubsequence(text1, text2, i=0, j=0):
    if i==len(text1):
        return 0
    if j==len(text2):
        return 0
    maxVal = 0
    if text1[i]==text2[j]:
        maxVal = 1 + longestCommonSubsequence(text1, text2, i+1, j+1)
    maxVal = max([maxVal, longestCommonSubsequence(text1, text2, i+1, j), longestCommonSubsequence(text1, text2, i, j+1)])
    return maxVal


def longestCommonSubsequenceMemo(text1, text2, dp, i=0, j=0):
    if i==len(text1):
        return 0
    if j==len(text2):
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    maxVal = 0
    if text1[i]==text2[j]:
        maxVal = 1 + longestCommonSubsequenceMemo(text1, text2, dp, i+1, j+1)
    maxVal = max([maxVal, longestCommonSubsequenceMemo(text1, text2, dp, i+1, j), longestCommonSubsequenceMemo(text1, text2, dp, i, j+1)])
    dp[i][j] = maxVal
    return dp[i][j]

text1, text2 = "", ""
dp = [[0 for j in range(len(text2))] for i in range(len(text1))]
longestCommonSubsequenceMemo(text1, text2, dp, i=0, j=0)
