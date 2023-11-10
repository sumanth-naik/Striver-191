# Key Idea 1: Interleave two orderings of length p1 and p2 -> (p1+p2)!/p1!p2! [denominator removes unnecessary repeats], which happens to be p1+p2 Choose p1
# Key Idea 2: Do that interleaving for each permutation combo of child subtrees to get total permutation from root
# Key Idea 3: create new arrays similar to BST structure as part of DFS instead of creating entire BST before hand

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9+7
        def dfs(nums):
            if len(nums)<=2: return 1
            left, right = [], []
            for num in nums:
                if num<nums[0]: left.append(num)
                if num>nums[0]: right.append(num)
            return (dfs(left) * dfs(right) * comb(len(left)+len(right), len(right)))%MOD
        return (dfs(nums)-1)%MOD


