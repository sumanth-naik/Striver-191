# Key Idea: Compare nums[mid] and nums[mid+1]
# Code is same for if there is only one Peak

class Solution:
    def findPeakElement(self, nums) -> int:
        low, high = 0, len(nums)-1
        while low<high:
            mid = (low+high)//2
            if nums[mid]<nums[mid+1]: 
                low = mid + 1
            else: 
                high = mid
        return low