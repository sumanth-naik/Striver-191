import bisect
from typing import List
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        totalCount, right, MOD = 0, 0, 10**9+7
        nums.sort()
        nums = nums[:bisect.bisect_right(nums, target)]
        n = len(nums)
        for left in range(n):
            right = bisect.bisect_right(nums, target - nums[left], left, n) - 1
            if right>=left: totalCount += pow(2, right-left)%MOD
        return totalCount%MOD

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        totalCount, left, right, MOD = 0, 0, len(nums)-1, 10**9+7
        nums.sort()
        while left<=right:
            if nums[left]+nums[right]<=target:
                totalCount += pow(2, right-left, MOD)
                left += 1
            else: 
                right -= 1  
        return totalCount