nums = [1,2,3,5,6,7,8]


def arithmeticSlices(nums):
    runningDifference = 0
    i,j, totalSlices = 0, 0, 0

    while j+1<len(nums):
        j += 1
        lastDifference = nums[j] - nums[j-1]
        if not lastDifference==runningDifference:
            i = j-1
            runningDifference = lastDifference
        elif j-i>=2:
            totalSlices += (j-i-1)
    return totalSlices
print(arithmeticSlices(nums))

