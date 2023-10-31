# Key Idea: Creating partitions, each step will affect next steps -> Partition DP

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        @lru_cache(None)
        def dp(i, j):
            if i+1==j: return 0
            return max(nums[i]*nums[k]*nums[j] + dp(i, k) + dp(k, j) for k in range(i+1, j))
        
        return dp(0, len(nums)-1)