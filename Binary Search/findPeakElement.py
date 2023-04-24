class Solution:
    def findPeakElement(self, nums) -> int:
        low, high = 0, len(nums)-1
        while low<high:
            mid = (low+high)//2
            if nums[mid+1]<nums[mid]: high = mid
            else: low = mid+1
        return low