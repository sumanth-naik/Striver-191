
class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        if sum(nums)%k!=0: return False 
        kBuckets = [sum(nums)//k] * k

        def backtrackingToFillBuckets(indexInNums):
            nonlocal kBuckets
            if indexInNums==len(nums): return sum(kBuckets)==0
            for bucketNum in range(k):
                if kBuckets[bucketNum]>=nums[indexInNums]:
                    kBuckets[bucketNum] -= nums[indexInNums]
                    if backtrackingToFillBuckets(indexInNums+1): return True      
                    kBuckets[bucketNum] += nums[indexInNums]
            return False
        return backtrackingToFillBuckets(0)


class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        if sum(nums)%k!=0: return False 
        sumNeeded, n = sum(nums)//k, len(nums)
        allUsedMask = (2**n) - 1

        @lru_cache(None)
        def backtracking(sumLeft, maskOfUsedNums, indexInNums):
            if maskOfUsedNums==allUsedMask: return sumLeft==sumNeeded
            if indexInNums==n: return False
            if maskOfUsedNums & (1<<indexInNums): 
                return backtracking(sumLeft, maskOfUsedNums, indexInNums+1)
            if sumLeft>nums[indexInNums]:
                if backtracking(sumLeft-nums[indexInNums], maskOfUsedNums | (1<<indexInNums), indexInNums+1):
                    return True
            if sumLeft==nums[indexInNums]:
                if backtracking(sumNeeded, maskOfUsedNums | (1<<indexInNums), 0):
                    return True
            return backtracking(sumLeft, maskOfUsedNums, indexInNums+1)
        
        return backtracking(sumNeeded, 0, 0)
            
