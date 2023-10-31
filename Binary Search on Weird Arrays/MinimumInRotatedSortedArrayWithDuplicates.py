# Key Idea 1: Compare nums[mid] and nums[high]
# Key Idea 2: If Equal, decrement high

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low<high:
            mid = (low+high)//2
            if nums[mid]<nums[high]:
                high = mid
            elif nums[mid]>nums[high]:
                low = mid + 1
            else:
                high -= 1
        return nums[low]