class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        prev1 = prev2 = None
        for right in range(len(nums)):
            if not (prev1==prev2==nums[right]):
                nums[left] = nums[right]
                left += 1
            if right>0: prev2 = prev1
            prev1 = nums[right]
        return left
                
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nextPlacingIndex, maxConsecutiveLength = 0, 2
        for num in nums:
            if nextPlacingIndex<maxConsecutiveLength or num!=nums[nextPlacingIndex-maxConsecutiveLength]:
                nums[nextPlacingIndex] = num
                nextPlacingIndex += 1
        return nextPlacingIndex