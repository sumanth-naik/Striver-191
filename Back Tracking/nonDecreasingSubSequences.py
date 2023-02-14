from copy import deepcopy
class Solution:
    def findSubsequences(self, nums):
        allSubsequences, currentSubsequence, n = set(), [], len(nums)
        def recursion(index):
            for i in range(index, n):
                if len(currentSubsequence)==0 or nums[i]>=currentSubsequence[-1]:
                    currentSubsequence.append(nums[i])
                    recursion(i+1)
                    currentSubsequence.pop()
            if len(currentSubsequence)>=2:
                allSubsequences.add(deepcopy(tuple(currentSubsequence)))
        recursion(0)
        return allSubsequences