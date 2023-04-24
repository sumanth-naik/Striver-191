class Solution:
    def splitArray(self, nums, k: int) -> int:
        n = len(nums)
        def isPartitionPossible(maxSum):
            runningSum, index, partitionsLeft = 0, 0, k
            while index<n:
                if partitionsLeft==0: break
                if runningSum+nums[index]>maxSum:
                    runningSum = 0
                    partitionsLeft-=1
                runningSum+=nums[index]
                index+=1
            return partitionsLeft!=0
        
        low, high = max(nums), sum(nums)
        while low<high:
            mid = (low+high)//2
            if isPartitionPossible(mid): high = mid
            else: low = mid+1
        return low