# Key Idea 1: Compare nums[low] and nums[mid] to find out if low to mid is sorted or mid to high
# Key Idea 2: Compare once more on the sorted part to eliminate

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
            
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target: return mid
            if nums[low]<=nums[mid]:
                if nums[low]<=target<nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid]<target<=nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            
        return -1