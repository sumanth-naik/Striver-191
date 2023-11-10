# Key Idea 1: You need average out if the current number is too big.
# Key Idea 2: If the number is very small, you cant make it till avg, since we take max(), it will have no effect 

class Solution:
    def minimizeArrayValue(self, nums):
        total, maxAvgSeen = 0, 0
        for i, num in enumerate(nums):
            total += num
            maxAvgSeen = max(maxAvgSeen, ceil(total/(i+1)))
        return maxAvgSeen