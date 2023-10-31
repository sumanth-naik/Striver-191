# Key Idea: Use maxIndexSeen to avoid repetitive search in BFS

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue, maxIndexSeen, n = deque([0]), 0, len(s)
        while queue:
            index = queue.popleft()
            for nextIndex in range(max(maxIndexSeen+1, index + minJump), min(index+maxJump+1, n)):
                if s[nextIndex]=='0':
                    if nextIndex==n-1: return True
                    queue.append(nextIndex)
            maxIndexSeen = index+maxJump
        return False
    



# ref: https://leetcode.com/problems/jump-game-vii/solutions/1226593/two-pointers-and-sliding-window/
# Key Idea 1: Naive way would take O(n*k). Need to optimize that k
# Key Idea 2: Create an auxillary array(isReachableArr) on which we can perform sliding window
# Key Idea 3: count variable will store number of different ways to reach index, which can be updated by sliding window. This avoids checking entire window.
# similar to: https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/solutions/238609/java-c-python-one-pass-and-o-1-space/comments/239423

# Note: there is no space optimisation by changing s[i] to store s[i]+2 as Python strings are immutable, however we can use deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        count, isReachableArr, n = 0, [False]*len(s), len(s)
        isReachableArr[0] = True
        for index in range(minJump, n):
            count += isReachableArr[index-minJump]
            if index-maxJump>0:
                count -= isReachableArr[index-maxJump-1]
            isReachableArr[index] = count>0 and s[index]=='0'
        return isReachableArr[-1]
    

