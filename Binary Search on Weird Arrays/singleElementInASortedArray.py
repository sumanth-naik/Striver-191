# Key Idea 1: Check if number is equal to its left or right
# Key Idea 2: Eliminate even length part

# Note: return statement is not return nums[low]. Its inside the loop

class Solution:
    def singleNonDuplicate(self, nums):
        low, high = 0, len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if mid-1>=0 and nums[mid-1]==nums[mid]:
                if (mid-1-low)&1:
                    high = mid - 2
                else:
                    low = mid + 1
            elif mid+1<len(nums) and nums[mid+1]==nums[mid]:
                if (mid-low)&1:
                    high = mid - 1
                else:
                    low = mid + 2
            else:
                return nums[mid]