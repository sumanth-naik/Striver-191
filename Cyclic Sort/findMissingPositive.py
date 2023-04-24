class Solution:
    def firstMissingPositive(self, nums) -> int:
        index, n = 0, len(nums)
        while index<n:
            while (index+1)!=nums[index] and 0<=nums[index]-1<n and nums[nums[index]-1]!=(nums[index]):
                nums[nums[index]-1], nums[index] = nums[index], nums[nums[index]-1]
                # this wont swap correctly
                # nums[index], nums[nums[index]-1] = nums[nums[index]-1], nums[index]
            index += 1
        
        for index in range(n):
            if (index+1)!=nums[index]: return index+1
        return n+1