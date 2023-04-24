class Solution:
    def canPartition(self, nums) -> bool:
        if sum(nums)%2!=0: return False
        sumNeeded = sum(nums)//2

        @lru_cache(None)
        def recursion(indexInNums, sumNeeded):
            if sumNeeded==0: return True
            if indexInNums==len(nums): return False
            if sumNeeded>=nums[indexInNums]:
                if recursion(indexInNums+1, sumNeeded-nums[indexInNums]):
                    return True
            return recursion(indexInNums+1, sumNeeded)
    
        return recursion(0, sumNeeded)