# Key Idea: maintain two majority elements instead of one. 

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maxElem1 = maxElem1Count = maxElem2 = maxElem2Count = 0
        
        for num in nums:
            if maxElem1==num:
                maxElem1Count += 1
            elif maxElem2 == num:
                maxElem2Count += 1
            elif maxElem1Count==0:
                maxElem1, maxElem1Count = num, 1
            elif maxElem2Count==0:
                maxElem2, maxElem2Count = num, 1
            else:
                maxElem1Count -= 1
                maxElem2Count -= 1

        return [num for num in (maxElem1, maxElem2)  if nums.count(num) > len(nums) // 3]