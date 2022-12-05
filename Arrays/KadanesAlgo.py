nums = [-2,1,-3,4,-1,2,1,-5,4]

maxSum = -1e9
runningSum = 0
for num in nums:
    runningSum += num
    maxSum = max(maxSum, runningSum)
    if(runningSum<0):
        runningSum = 0
print(maxSum)
