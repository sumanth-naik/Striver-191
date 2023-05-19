from typing import List
from collections import deque
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        maxSum = -1e9
        queue = deque()
        for index, num in enumerate(nums):
            # remove out of window elements
            # 'if' is also fine as there will be atmost one to remove on each iteration
            while queue and queue[0][1]<index-k: queue.popleft()
            # remove all if all are negative
            if queue and queue[0][0]<=0: queue = deque()

            nextNum = num+queue[0][0] if queue else num
            # remove all smaller from the right to maintain monotonicity (decreasing from left to right => max on left corner)
            while queue and queue[-1][0]<nextNum: queue.pop()

            queue.append((nextNum, index))
            maxSum = max(maxSum, queue[0][0])

        return maxSum

import heapq      
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int: 
        maxHeap, maxSum = [], -1e9
        for index, num in enumerate(nums):
            # remove out of window elements
            while maxHeap and maxHeap[0][1]<index-k: heapq.heappop(maxHeap)
            
            nextNum = -(num - maxHeap[0][0]) if maxHeap else -num
            # instead of removing negative values from heap later, dont even add them
            if nextNum<0:
                heapq.heappush(maxHeap, (nextNum, index))
            if maxHeap:
                maxSum = max(maxSum, -maxHeap[0][0])

        return maxSum if maxSum!=-1e9 else max(nums)
