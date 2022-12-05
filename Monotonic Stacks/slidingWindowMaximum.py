nums = [1,3,-1,-3,5,3,6,7]
k = 3


def slidingWindowMaximum(nums, k):
    leftMaxArray = []
    leftMax = -10e10
    n = len(nums)
    for i in range(0, n):
        if i%k==0:
            leftMax = -10e10
        leftMax = max(leftMax, nums[i])
        leftMaxArray.append(leftMax)

    rightMaxArray = []
    rightMax = -10e10
    for i in range(n-1, -1, -1):
        rightMax = max(rightMax, nums[i])
        rightMaxArray.append(rightMax)
        if i%k==0:
            rightMax = -10e10
    return [max(rightMaxArray[i],leftMaxArray[i+k-1]) for i in range(n-k+1)]

print(slidingWindowMaximum(nums, k))
    