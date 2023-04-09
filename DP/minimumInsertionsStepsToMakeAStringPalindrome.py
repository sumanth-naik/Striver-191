class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dpPrev, dpPrev2 = [0]*n, [0]*n

        for delta in range(1, n):
            dpCurr = []
            for startIndex in range(n-delta):
                i, j = startIndex, startIndex+delta
                if s[i]==s[j]:
                    dpCurr.append(dpPrev2[startIndex+1])
                else:
                    dpCurr.append(1+min(dpPrev[startIndex], dpPrev[startIndex+1]))
            dpPrev2, dpPrev = dpPrev, dpCurr
        return dpPrev[-1]
    