# Key Idea 1: What is the maxProfit I could have made until now? Use that to calc the next profit
# Key Idea 2: Use minHeap on (lastJob's EndTime, all Job's Profits) 
    
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        maxProfit, minHeapOfJobsCombinations = 0, []

        for start, end, profit in jobs:
            while minHeapOfJobsCombinations and minHeapOfJobsCombinations[0][0]<=start:
                maxProfit = max(maxProfit, heappop(minHeapOfJobsCombinations)[1])
            heappush(minHeapOfJobsCombinations, (end, profit + maxProfit))
            
        return max(minHeapOfJobsCombinations, key = lambda x: x[1])[1]
    



# Key Idea 1: Take/not Take DP
# Key Idea 2: sort by startTimes
# Key Idea 3: Use Binary Search to optimise finding next possible index

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        nums = sorted(zip(startTime, endTime, profit))

        @cache
        def dp(index):
            if index==len(nums): return 0
            return max(dp(index+1), \
            nums[index][2] + dp(bisect_left(nums, nums[index][1], index+1, len(nums), key=lambda x:x[0])))
        
        return dp(0)
    