class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # assuming start time is sorted
        n = len(startTime)

        @lru_cache(None)
        def recursion(index):
            if index==n: return 0
            return max(profit[index]+recursion(bisect_left(startTime, endTime[index], index+1, n)), recursion(index+1))

        return recursion(0)


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        nums = sorted((startTime[index], endTime[index], profit[index]) for index in range(n))

        @lru_cache(None)
        def recursion(index):
            if index==n: return 0
            return max(nums[index][2]+recursion(bisect_left(nums, (nums[index][1], -1e9, -1e9), index+1, n)), recursion(index+1))

        return recursion(0)
    
class Solution: #not mine
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        ends, best = [], 0
        for s, e, p in sorted(zip(startTime, endTime, profit)):
            while ends and ends[0][0] <= s:
                best = max(best, heappop(ends)[1])
            heappush(ends, (e, best+p))
        return max(x[1] for x in ends)