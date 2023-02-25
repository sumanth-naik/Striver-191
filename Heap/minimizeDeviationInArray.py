import heapq
class Solution:
    def minimumDeviation(self, nums):
        nums, minInHeap, heapOfMaximums, minDeviation = set(nums), 1e10, [], 1e10
        for num in nums:
            if num & 1:
                num *= 2
            heapq.heappush(heapOfMaximums,-num)
            minInHeap = min(num, minInHeap)               

        while True:
            maxInHeap = -heapq.heappop(heapOfMaximums)
            minDeviation = min(minDeviation, maxInHeap - minInHeap)
            if maxInHeap & 1: 
                return minDeviation
            maxInHeapDiv2 = int(maxInHeap/2)
            heapq.heappush(heapOfMaximums, -maxInHeapDiv2)
            minInHeap = min(minInHeap, maxInHeapDiv2)


