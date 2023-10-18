class Solution:
    def majorityElement(self, nums):
        major, count = nums[0], 1
        for i in range(1, len(nums)):
            if count == 0:
                count += 1
                major = nums[i]
            elif major == nums[i]:
                count += 1
            else:
                count -= 1
        return major


arr = [2,3,4,2,2]
n = len(arr)

minElem = 0
minElemCount = 0
for num in arr:
    if minElemCount == 0:
        minElem = num
        minELemCOunt = 1
    if(minElem==num):
        minElemCount += 1
    else:
        minElemCount -= 1

count = 0
for num in arr:
    if minElem==num: count+=1
    
if count> n//2:
    print(minElem)
else:
    print(-1)