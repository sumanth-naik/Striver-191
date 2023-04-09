class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def getPower(num):
            if num==1: return 0
            if num&1: return getPower(num*3+1)
            return getPower(num//2)

        tuplesOfPowerAndNums = []
        for num in range(lo, hi+1):
            tuplesOfPowerAndNums.append((getPower(num), num))
        return sorted(tuplesOfPowerAndNums)[k-1]