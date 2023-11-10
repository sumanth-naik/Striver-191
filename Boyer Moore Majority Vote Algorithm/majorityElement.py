# Key Idea: If there is a majority elem, at some index it should break even
# https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
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
