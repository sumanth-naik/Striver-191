import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        minHeap, n = [], len(costs)
        left, right = -1, n

        while left+1<right and left+1<candidates:
            heapq.heappush(minHeap, (costs[left+1], left+1, "L"))
            left += 1
        while right-1>left and n-right<candidates:
            heapq.heappush(minHeap, (costs[right-1], right-1, "R"))
            right -= 1
        
        totalCost = 0
        while k:
            if not minHeap: return totalCost
            cost, index, direction = heapq.heappop(minHeap)
            totalCost += cost
            
            if direction=="L" and left+1<right:
                heapq.heappush(minHeap, (costs[left+1], left+1, "L"))
                left += 1
            elif direction=="R" and right-1>left:
                heapq.heappush(minHeap, (costs[right-1], right-1, "R"))
                right -= 1
            k -= 1

        return totalCost
    

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n, totalCost = len(costs), 0
        left, right, minHeap = candidates, n-candidates-1, []
        for index in set(range(0, candidates)) | set(range(n-candidates, n)):
            heapq.heappush(minHeap, (costs[index], index))
    
        while k:
            cost, index = heapq.heappop(minHeap)
            totalCost += cost
            if index<left and left<=right:
                heapq.heappush(minHeap, (costs[left], left))
                left += 1
            elif index>right and right>=left:
                heapq.heappush(minHeap, (costs[right], right))
                right -= 1
            k -= 1
            
        return totalCost
        
    

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n, totalCost = len(costs), 0
        left, right, minHeap = candidates, n-candidates-1, []
        
        for index in list(range(0, candidates)) + list(range(max(n-candidates, left), n)):
            heapq.heappush(minHeap, (costs[index], index))
    
        while k:
            cost, index = heapq.heappop(minHeap)
            totalCost += cost
            if index<left and left<=right:
                heapq.heappush(minHeap, (costs[left], left))
                left += 1
            elif index>right and right>=left:
                heapq.heappush(minHeap, (costs[right], right))
                right -= 1
            k -= 1
            
        return totalCost
        

