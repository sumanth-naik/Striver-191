# Key Idea: Subsets. no greedy -> DP possible? -> Yes -> brute force backtracking not needed

# Note: There is no need to maintain indexOfNums in state. we can actually figure it out from mask.

class Solution:
    def maxScore(self, nums: List[int]) -> int:

        @cache
        def gcd(x, y): return math.gcd(x, y)

        @cache
        def bitmaskingDp(unusedBitMask, indexInNums):
            maxSeen = 0
            for xIndex in range(len(nums)):
                if not (unusedBitMask & (1<<xIndex)): continue
                for yIndex in range(xIndex+1, len(nums)):
                    if not (unusedBitMask & (1<<yIndex)): continue
                    maxSeen = max(maxSeen, (indexInNums+1)*gcd(nums[xIndex], nums[yIndex]) + \
                                           bitmaskingDp(unusedBitMask&~(1<<xIndex)&~(1<<yIndex), indexInNums+1))
            return maxSeen

        return bitmaskingDp((1<<len(nums))-1, 0)
