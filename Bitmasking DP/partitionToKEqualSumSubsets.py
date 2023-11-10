# Key Idea 1: In this bucket, which all numbers should I put? -> Need sumLeftInCurrBucket, maskOfUsedNums, indexInNums as state
# Key Idea 2: Push looping on nums to dp impl -> Need sumLeftInCurrBucket, maskOfUsedNums

# Easy/useful to memoise - we take advantage of the fact that we only need to look at current bucket's status and what all nums are used
# Unlike in backtracking, here we dont need to know what other bucket's states are. 

# Optimisation 1: Sort to fill the big ones first which create less branches at the top
# Optimisation 2: Exit in case we know answer will be False. (1) Not divisible case (2) a num cant fit in bucket
# TC : min(2^n, sum(nums)//k) * 2^n * n 

class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        nums.sort(reverse=True) # Optimisation 1
        total, n = sum(nums), len(nums)
        sumInBucket, allUsedMask = total//k, (1<<n) - 1
        
        if total%k or nums[0]>sumInBucket: # Optimisation 2
            return False 

        @cache
        def bitMaskDp(sumLeft, maskOfUsedNums):
            if sumLeft==0: 
                sumLeft = sumInBucket
            if maskOfUsedNums==allUsedMask: 
                return sumLeft==sumInBucket
            for index in range(n):
                if not (maskOfUsedNums & (1<<index)) and sumLeft>=nums[index]:
                    if bitMaskDp(sumLeft-nums[index], maskOfUsedNums | (1<<index)):
                        return True
        
        return bitMaskDp(sumInBucket, 0)



# Key Idea 1: In which bucket should I put the current number?  -> Backtrack with index 

# hard/useless to memoise since we need to store EACH BUCKET's state.

# TC without Optimization3: k^n -> TLE
# Optimization 3: Stop creating permutations wrt buckets
#               if kBuckets[bucketNum] == sum(nums)//k, then every bucket on the right is also empty. 
#               We will be repeating same assignments again but starting with next bucket instead of this one.
#               [2] [] []
#               when kBuckets[bucketNum] == sum(nums)//k on first bucket
#               [] [] []
#               Not stopping will add 2 in second bucket
#               [] [2] [] <- useless for us, as this is same as above one
# TC with Optimization 3: (k^n) / (k!)     <- Better than bitmasking DP

class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        nums.sort(reverse=True) # Optimisation 1
        total, n = sum(nums), len(nums)
        sumInBucket = total//k

        if total%k or nums[0]>sumInBucket: # Optimisation 2
            return False 
        
        kBuckets = [sumInBucket] * k
        
        def backtrackingToFillBuckets(indexInNums):
            nonlocal kBuckets
            if indexInNums==n: return sum(kBuckets)==0
            for bucketNum in range(k):
                if kBuckets[bucketNum]>=nums[indexInNums]:
                    kBuckets[bucketNum] -= nums[indexInNums]
                    if backtrackingToFillBuckets(indexInNums+1): return True      
                    kBuckets[bucketNum] += nums[indexInNums]
                    if kBuckets[bucketNum] == sumInBucket: break # Optimization 3
            return False
        return backtrackingToFillBuckets(0)



