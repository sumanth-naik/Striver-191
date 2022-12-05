nums = [-1,0,1,2,-1,-4]


def twoPointerSum(i, j, nums, sum, tripletSet):
    while i<j:
        currSum = nums[i] + nums[j]
        if currSum<sum:
            i += 1
        elif currSum>sum:
            j -= 1
        else:
            tripletSet.add((-sum, nums[i], nums[j]))
            i += 1

def threeSum(nums):
    nums.sort()
    tripletSet, n = set(), len(nums)
    for index in range(n):
        twoPointerSum(index+1, n-1, nums, -nums[index], tripletSet)
    return tripletSet

print(threeSum(nums))