# Key Idea 1: Sorting will make the question trivial. Cyclic sort is just another fancy way to sort
# Key Idea 2: (1) If this number is not in the right place, 
#             (2) the number's right place is not occupied, SWAP

# ref https://emre.me/coding-patterns/cyclic-sort/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums = [0]+nums
        index = 0
        while index<len(nums):
            while nums[index]!=index and nums[nums[index]]!=nums[index]:
                nums[nums[index]], nums[index] = nums[index], nums[nums[index]]
            index += 1
        return [num for index, num in enumerate(nums) if num!=index]