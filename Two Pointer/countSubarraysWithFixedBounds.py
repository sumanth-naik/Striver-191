class Solution:
    def countSubarrays(self, nums, minK: int, maxK: int) -> int:
        iMin = iMax = iBad = -1
        res = 0
        for j, val in enumerate(nums):
            if not minK<=val<=maxK: iBad = j
            if val==minK: iMin = j
            if val==maxK: iMax = j
            #there are (iBad+1 to min(iMin,iMax) starting points to subarray ending at j)
            res += max(0, min(iMin, iMax) - iBad)
        return res