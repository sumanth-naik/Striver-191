nums = [2,7,9,3,1]
from copy import deepcopy
def houseRobber(nums):
    if len(nums)==1:
        return nums[0]
    sum1, sum2 = nums[-2], nums[-1]
    for i in range(len(nums)-3, -1, -1):
        sum1, sum2 = max(sum1, nums[i]+sum2), max(sum1, sum2)
    return max(sum1,sum2)


def houseRobber2(nums):
    if len(nums)==1: return nums[0]
    return max(houseRobber(nums[:len(nums)-1]), houseRobber(nums[1:]))

print(houseRobber(nums))
print(houseRobber2(nums))
