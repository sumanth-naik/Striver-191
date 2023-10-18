class Solution:
    def kConcatenationMaxSum(self, arr, k: int) -> int:
        MOD = 10**9+7
        def kadanesAlgo(arr):
            runningSum, maxSum = 0, 0
            for num in arr:
                runningSum = max(num + runningSum, num)
                maxSum = max(maxSum, runningSum)
            return maxSum
    
        maxSumFromLast, runningSum = 0, 0
        for num in reversed(arr):
            runningSum += num
            maxSumFromLast = max(maxSumFromLast, runningSum)

        maxSumFromFirst, runningSum = 0, 0
        for num in arr:
            runningSum += num
            maxSumFromFirst = max(maxSumFromFirst, runningSum)

        return max(maxSumFromLast+(k-2)*sum(arr)+maxSumFromFirst, kadanesAlgo(arr+arr))%MOD if k>=2 else kadanesAlgo(arr)%MOD