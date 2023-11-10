# Key Idea 1: Qn involves Greedy on each tire, but DP across tires
# Key Idea 2: For each tire, calc numLaps it can go greedily without changing tire.
# Key Idea 3: While at Key Idea 2, prepopulate dp, where dp[i] indicates the best way to do i laps
# Key Idea 4: Do dp with n^2 algo, where we start using multiple tires.

# Optimization 1: Go only till i//2 to avoid repeats like dp[1] + changeTime + dp[3]; dp[3] + changeTime + dp[1]

class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        dp = [1e20]*(numLaps+1)

        for f, r in tires:
            prevTotal = 0
            for x in range(1, numLaps+1):
                total = prevTotal + f*(r**(x-1))
                if total>=prevTotal+changeTime+f: 
                    break
                dp[x] = min(dp[x], total)
                prevTotal = total

        for i in range(1, numLaps+1):
            for k in range(1, i//2+1): # Optimization 1
                dp[i] = min(dp[i], dp[i-k] + changeTime + dp[k])
        
        return dp[-1]