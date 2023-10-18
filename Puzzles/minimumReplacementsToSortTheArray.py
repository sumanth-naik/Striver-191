class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        index, rightMin, totalSplits = len(nums)-2, nums[-1], 0
        while index>=0:
            numSplits = ceil(nums[index]/rightMin)
            totalSplits += (numSplits - 1)
            rightMin = floor(nums[index]/numSplits)
            index -= 1
        return totalSplits