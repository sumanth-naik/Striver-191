nums = [-2,1,-3,4,-1,2,1,-5,4]

maxSum, runningSum = -1e9, 0
for num in nums:
    runningSum += num
    maxSum = max(maxSum, runningSum)
    runningSum = max(0, runningSum)
print(maxSum)


class Solution:
    def maxSubarraySumCircular(self, nums):
        runningSumForMax, runningSumForMin, maxSum, minSum, totalSum = 0, 0,-1e10, 1e10, 0
        for num in nums:
            runningSumForMax += num
            runningSumForMin += num
            maxSum = max(maxSum, runningSumForMax)
            minSum = min(minSum, runningSumForMin)
            totalSum += num
            if runningSumForMax<0: runningSumForMax = 0
            if runningSumForMin>0: runningSumForMin = 0
        return max(maxSum, totalSum-minSum) if maxSum>0 else maxSum
