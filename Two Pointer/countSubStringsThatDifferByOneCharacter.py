# two pointer
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        lenS, lenT, subStringsCount = len(s), len(t), 0
        for sIndex in range(lenS):
            for tIndex in range(lenT):
                if s[sIndex]!=t[tIndex]:
                    leftS, leftT, rightS, rightT = sIndex, tIndex, sIndex, tIndex
                    while leftS-1>=0 and leftT-1>=0 and s[leftS-1]==t[leftT-1]:
                        leftS -= 1
                        leftT -= 1
                    while rightS+1<lenS and rightT+1<lenT and s[rightS+1]==t[rightT+1]:
                        rightS += 1
                        rightT += 1
                    subStringsCount += ((sIndex-leftS+1)*(rightS-sIndex+1))
        return subStringsCount

# DP
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        lenS, lenT, subStringsCount = len(s), len(t), 0
        dp = [[[0,0] for _ in range(lenT+2)] for _ in range(lenS+2)]

        for sIndex in range(1, lenS+1):
            for tIndex in range(1, lenT+1):
                if s[sIndex-1]==t[tIndex-1]:
                    dp[sIndex][tIndex][0] = 1 + dp[sIndex-1][tIndex-1][0]

        for sIndex in range(lenS, 0, -1):
            for tIndex in range(lenT, 0, -1):
                if s[sIndex-1]==t[tIndex-1]:
                    dp[sIndex][tIndex][1] = 1 + dp[sIndex+1][tIndex+1][1]

        for sIndex in range(lenS, 0, -1):
            for tIndex in range(lenT, 0, -1):
                if s[sIndex-1]!=t[tIndex-1]:
                    subStringsCount += ((dp[sIndex-1][tIndex-1][0]+1) * (dp[sIndex+1][tIndex+1][1]+1))
        return subStringsCount

    