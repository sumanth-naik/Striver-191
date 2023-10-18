class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right, n = 0, 0, len(nums)
        hasZero, bestWindowLength = False, 0
        while right<n:                
            if nums[right]==0:
                if hasZero:
                    while nums[left]==1: left += 1 # skip all ones
                    left += 1 # skip that left zero
                else:
                    hasZero = True
            right += 1
            bestWindowLength = max(bestWindowLength, right-left-1 if hasZero else right-left)
        return bestWindowLength if bestWindowLength!=n else n-1

        
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right, n = 0, 0, len(nums)
        numZeroes, bestWindowLength = 0, 0
        while right<n:
            numZeroes += (nums[right]==0)
            while numZeroes>1: 
                numZeroes -= (nums[left]==0)
                left += 1
            bestWindowLength = max(bestWindowLength, right-left)
            right += 1
        return bestWindowLength
            
