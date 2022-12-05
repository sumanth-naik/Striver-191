nums = [1,2,2]
from copy import deepcopy
def subsets2(nums, index, ansArr, currAns):
    print(ansArr, currAns)
    if index == len(nums):
        ansArr.append(deepcopy(currAns))
        return 
    subsets2(nums, index+1, ansArr, currAns)
    subsets2(nums, index+1, ansArr, currAns + [nums[index]])

print(subsets2(nums, 0, [], []))