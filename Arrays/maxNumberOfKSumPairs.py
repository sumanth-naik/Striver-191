


nums = [1,2,3,4]
k = 5
from collections import Counter

numMap = Counter(nums)
print(numMap)

numPairs = 0
for num in numMap:
    if(k-num in numMap):
        numPairs += min(numMap[num], numMap[k-num])
print(numPairs//2)







nums.sort()

left = 0
right = len(nums) - 1
numPairs = 0
while(left<right):
    currSum = nums[left]+nums[right]
    if(currSum==k):
        numPairs += 1
        left += 1
        right -= 1
    elif currSum<k:
        left += 1
    else:
        right -= 1
print(numPairs)


