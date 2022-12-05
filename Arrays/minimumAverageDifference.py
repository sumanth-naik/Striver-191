nums = [6,1]

def minimumAverageDifference(nums):
    totalSum, minAvgDiff, runningSum, minIndex = sum(nums), 10e9, 0, 0
    for i in range(0, len(nums)):
        runningSum += nums[i]
        currAvgDiff = abs(int(runningSum/(i+1))-int((totalSum-runningSum)/(max(len(nums)-i-1,1))))
        if minAvgDiff>currAvgDiff: 
            minAvgDiff = min(minAvgDiff, currAvgDiff)
            minIndex = i
    return minIndex

print(minimumAverageDifference(nums))
