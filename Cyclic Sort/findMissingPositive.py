# Key Idea 1: Sorting will make the question trivial. Cyclic sort is just another fancy way to sort
# Key Idea 2: (1) If this number is not in the right place, 
#             (2) the number is swappable,
#             (3) the number's right place is not occupied, SWAP

class Solution:
    def firstMissingPositive(self, nums) -> int:
        index, n = 0, len(nums)
        while index<n:
            while (index+1)!=nums[index] and 0<=nums[index]-1<n and nums[nums[index]-1]!=(nums[index]):
                nums[nums[index]-1], nums[index] = nums[index], nums[nums[index]-1]
            index += 1
        
        for index in range(n):
            if (index+1)!=nums[index]: return index+1
        return n+1