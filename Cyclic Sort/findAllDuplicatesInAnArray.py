from typing import List

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