import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital):
        indexTillCapitalWhichAreAdded = -1
        capital, profits = zip(*sorted(zip(capital, profits)))
        # (-profit)
        profitsHeap = []
        def addTill(currentWeight):
            nonlocal indexTillCapitalWhichAreAdded, profitsHeap
            while indexTillCapitalWhichAreAdded + 1 < len(capital) and capital[indexTillCapitalWhichAreAdded+1]<=currentWeight:
                indexTillCapitalWhichAreAdded += 1 
                heapq.heappush(profitsHeap, -profits[indexTillCapitalWhichAreAdded])
        
        for _ in range(k):
            addTill(w)
            if profitsHeap:
                w -= heapq.heappop(profitsHeap)
        return w
