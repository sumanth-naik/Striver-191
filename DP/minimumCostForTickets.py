from functools import lru_cache
class Solution:
    def mincostTickets(self, days, costs) -> int:
        n = len(days)

        @lru_cache(None)
        def memoization(i):
            if i==n: return 0

            indexCoveredBy1DayPass, indexCoveredBy7DayPass, indexCoveredBy30DayPass = i, i, i
            while indexCoveredBy7DayPass+1<n and days[indexCoveredBy7DayPass+1]-days[i]<=6: indexCoveredBy7DayPass += 1
            while indexCoveredBy30DayPass+1<n and days[indexCoveredBy30DayPass+1]-days[i]<=29: indexCoveredBy30DayPass += 1

            return min(costs[0]+memoization(indexCoveredBy1DayPass+1), costs[1]+memoization(indexCoveredBy7DayPass+1), costs[2]+memoization(indexCoveredBy30DayPass+1))
        
        return memoization(0)
    
# tabulation
class Solution:
    def mincostTickets(self, days, costs) -> int:
        n = len(days)
        dp = [0]*(n+1)
        for i in range(n-1, -1, -1):
            indexCoveredBy1DayPass, indexCoveredBy7DayPass, indexCoveredBy30DayPass = i, i, i
            while indexCoveredBy7DayPass+1<n and days[indexCoveredBy7DayPass+1]-days[i]<=6: indexCoveredBy7DayPass += 1
            while indexCoveredBy30DayPass+1<n and days[indexCoveredBy30DayPass+1]-days[i]<=29: indexCoveredBy30DayPass += 1
            dp[i] = min(costs[0]+dp[indexCoveredBy1DayPass+1], costs[1]+dp[indexCoveredBy7DayPass+1], costs[2]+dp[indexCoveredBy30DayPass+1])
        return dp[0]
        
# tabulation with constant space(30)
from collections import deque
class Solution:
    def mincostTickets(self, days, costs) -> int:
        n = len(days)
        dp = deque()
        dp.append(0)
        for i in range(n-1, -1, -1):
            indexCoveredBy1DayPass, indexCoveredBy7DayPass, indexCoveredBy30DayPass = i, i, i
            while indexCoveredBy7DayPass+1<n and days[indexCoveredBy7DayPass+1]-days[i]<=6: indexCoveredBy7DayPass += 1
            while indexCoveredBy30DayPass+1<n and days[indexCoveredBy30DayPass+1]-days[i]<=29: indexCoveredBy30DayPass += 1
            dp.appendleft(min(costs[0]+dp[indexCoveredBy1DayPass-i], costs[1]+dp[indexCoveredBy7DayPass-i], costs[2]+dp[indexCoveredBy30DayPass-i]))
            if len(dp)>30: dp.pop()
        return dp[0]
        
# bottom up O(days) sol ref:https://leetcode.com/problems/minimum-cost-for-tickets/solutions/810791/python-universal-true-o-days-solution-explained/
from collections import deque
class Solution:
    def mincostTickets(self, days, costs) -> int:
        n, k, passLength, cost = len(days), 3, [1,7,30], 0
        dp = [deque() for _ in range(k)]
        for i in range(n-1, -1, -1):
            for q in range(k):
                while dp[q] and dp[q][-1][0] - days[i]>=passLength[q]: dp[q].pop()[1]
                dp[q].appendleft([days[i], cost + costs[q]])
            cost = min(dp[q][-1][1] for q in range(k))
        return cost
        

# top down O(days) sol ref: https://leetcode.com/problems/minimum-cost-for-tickets/solutions/810791/python-universal-true-o-days-solution-explained/
from collections import deque
class Solution:
    def mincostTickets(self, days, costs) -> int:
        numPassTypes, numDaysForEachPassType, cost = 3, [1,7,30], 0
        queueForEachPassType = [deque() for _ in range(numPassTypes)]
        for day in days:
            for passType in range(numPassTypes):
                while queueForEachPassType[passType] and day-queueForEachPassType[passType][0][1]>=numDaysForEachPassType[passType]: queueForEachPassType[passType].popleft()
                queueForEachPassType[passType].append([cost+costs[passType], day])
            # cost stores the min cost till current day
            # each queue will just store all the reachable days with that pass and 
            # hence taking min of first elements ensure that the day(last added) is reachable
            # also each pair that is added to queue will be added such that, it will take the best cost till
            # the previous day and buy a particular pass with costs[passType] and gets added to the queues
            cost = min(queueForEachPassType[passType][0][0] for passType in range(numPassTypes))
        return cost
