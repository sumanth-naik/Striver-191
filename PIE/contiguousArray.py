class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mapOfCountToIndex, count, maxLen = {0:-1}, 0, 0
        for index, num in enumerate(nums):
            count += (1 if num==1 else -1)
            if count not in mapOfCountToIndex:
                mapOfCountToIndex[count] = index
            else:
                maxLen = max(maxLen, index-mapOfCountToIndex[count])
        return maxLen