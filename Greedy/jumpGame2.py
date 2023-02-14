# BFS, DP, Optimized DP/Greedy 
from collections import deque
class Solution:
    def jump(self, nums):
        queue, visited, n = deque([(0,0)]), set([0]), len(nums)
        if n==1: return 0
        while queue:
            index, stepsSoFar = queue.popleft()
            for neigh in range(index+1, index+nums[index]+1):
                if neigh==n-1:
                    return stepsSoFar+1
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append((neigh, stepsSoFar+1))

class Solution:
    def jump(self, nums):
        dp = [0 for _ in range(len(nums))]
        for index in range(len(nums)-2, -1, -1):
            dp[index] = min([1e9]+dp[index+1:index+nums[index]+1]) + 1
        return dp[0]

class Solution:
    def jump(self, nums):
        lastIndexOfPreviousJumpSet, largestJumpableIndexFromPreviousJumpSet, jumps = -1, 0, 0
        while largestJumpableIndexFromPreviousJumpSet<len(nums)-1:
            largestJumpableIndexFromPreviousJumpSet, lastIndexOfPreviousJumpSet = max([nums[index]+index for index in range(lastIndexOfPreviousJumpSet+1, largestJumpableIndexFromPreviousJumpSet+1)]), largestJumpableIndexFromPreviousJumpSet
            jumps+=1
        return jumps