class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()
        n = len(rides)

        @lru_cache(None)
        def recursion(index):
            if index==n: return 0
            return max(rides[index][1]-rides[index][0]+rides[index][2]+recursion(bisect_left(rides, rides[index][1], index+1, n, key=lambda x:x[0])), recursion(index+1))

        return recursion(0)

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()
        minHeapWithEndTimeAndProfit, n, maxProfitBeforeThisRide = [], len(rides), 0
        for start, end, profit in rides:
            while minHeapWithEndTimeAndProfit and minHeapWithEndTimeAndProfit[0][0]<=start:
                maxProfitBeforeThisRide = max(maxProfitBeforeThisRide, heappop(minHeapWithEndTimeAndProfit)[1])
            heappush(minHeapWithEndTimeAndProfit, (end, end-start+profit+maxProfitBeforeThisRide))
        return max(profit for end, profit in minHeapWithEndTimeAndProfit)