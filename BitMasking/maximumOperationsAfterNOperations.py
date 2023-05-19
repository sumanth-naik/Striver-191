from itertools import combinations
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @lru_cache(None)
        def bitmaskingDp(bitmask, i):
            maxSeen = 0
            for xIndex, yIndex in combinations([index for index in range(len(nums)) if bitmask&1<<index], 2):
                maxSeen = max(maxSeen, i*gcd(nums[xIndex], nums[yIndex]) + bitmaskingDp(bitmask&~(1<<xIndex)&~(1<<yIndex), i+1))
            return maxSeen

        return bitmaskingDp(2**(len(nums))-1, 1)

from itertools import combinations
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @lru_cache(None)
        def bitmaskingDp(bitmask, i):
            return max(i*gcd(nums[xIndex], nums[yIndex]) + bitmaskingDp(bitmask&~(1<<xIndex)&~(1<<yIndex), i+1) for xIndex, yIndex in combinations([index for index in range(len(nums)) if bitmask&1<<index], 2)) if bitmask else 0
        return bitmaskingDp(2**(len(nums))-1, 1)
