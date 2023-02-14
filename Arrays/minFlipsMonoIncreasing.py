class Solution:
    def minFlipsMonoIncr(self, s: str):
        onesToLeftCountList, zeroesToRightCountList = [0], [0]
        onesToLeftCountList = [s[i] + onesToLeftCountList[-1] for i in range(1, len(s)-1)]
        for i in range(len(s)-1):
            onesToLeftCountList.append(int(s[i])+onesToLeftCountList[-1])
        for i in range(len(s)-1,0,-1):
            zeroesToRightCountList.append(1-int(s[i])+zeroesToRightCountList[-1])
        return min([onesToLeftCountList[i]+zeroesToRightCountList[len(s)-i-1] for i in range(len(s))])