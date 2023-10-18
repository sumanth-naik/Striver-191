class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        currentSum, smallestSubArrayLength = 0, 1e9
        while right<len(nums):
            currentSum += nums[right]
            while currentSum>=target:
                smallestSubArrayLength = min(smallestSubArrayLength, right-left+1)
                currentSum -= nums[left]
                left += 1
            right += 1
        return 0 if smallestSubArrayLength==1e9 else smallestSubArrayLength