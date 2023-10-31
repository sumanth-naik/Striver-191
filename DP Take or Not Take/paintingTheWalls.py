# Key Idea 1: Just think from the perspective of paid painter
# Key Idea 2: If paid painter picks a wall, free painter can finish time[index] walls

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        @lru_cache(None)
        def recursion(index, wallsLeft):
            if wallsLeft<=0: return 0 
            if index==n: return 10**10
            # If paid painter does the job, his painting decreases wallsLeft by 1 and free painter paints time[index] walls meanwhile
            return min(cost[index]+recursion(index+1, wallsLeft-1-time[index]), recursion(index+1, wallsLeft))
        
        return recursion(0, n)