class Solution:
    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums)

        while left<=right:
            mid = (left+right)//2
            if (mid-1>=0 and nums[mid-1]==nums[mid]):
                if (mid-1-left)%2==1:
                    right = mid - 2
                else:
                    left = mid + 1
            elif (mid+1<len(nums) and nums[mid+1]==nums[mid]):
                if (mid-left)%2==1:
                    right = mid - 1
                else:
                    left = mid + 2
            else:
                return nums[mid]              