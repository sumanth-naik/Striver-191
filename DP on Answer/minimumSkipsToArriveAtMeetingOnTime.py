'''
MLE:
        @lru_cache(None)
        def dp(i, skipsLeft):
            if i<0: return 0
            if skipsLeft<0: return 1e9
            return min(ceil(dp(i-1, skipsLeft)), dp(i-1, skipsLeft-1)) + dist[i]/speed
'''
# Initial thought was to figure out what is the wasted time if i skip today's break. This caused a chain, as if i skip next trip's break, its hard to calculate the wasted time.. skipping i'th ride started to depending on if skipping is done on i+1'th ride which depended on if skipped on i+2'th

# Idea switch -> Store un-rounded time in dp[i][skips], so that i+1'th ride doesn't have to know i'th ride's decision

# Key Idea 1: Do not try to eliminate wasted time, instead try to think if i+1'th ride can be sneaked into previous time left by i'th ride 
# Key Idea 2: Naturally, store 'time' in dp[i][skips] which is not a rounded number. So that i+1'th journey can 'fit in' with a skip if needed.

# Note 1: 1/3 + 2/3 = 1.00000001, ceil() will give 2. So have an error term to compensate. (1e-7 is random)
# if doing ceil -> subtract error
# if doing floor -> add error

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n, error = len(dist), 1e-7 
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for skips in range(n):
            dp[0][skips] = dist[0]/speed

        for i in range(1, n):
            for skips in range(n):               # Note 1
                dp[i][skips] = min(ceil(dp[i-1][skips]-error), dp[i-1][skips-1] if skips!=0 else 1e9) + dist[i]/speed

        skipsNeeded = bisect_left(dp[-1], -hoursBefore, key = lambda x:-x)
        return skipsNeeded if skipsNeeded!=n else -1


# Key Idea 3: Store dist in dp[i][skips] instead of time to avoid floating point errors

# Note 2: rounding up to speed multiple distance means adding (speed-dist)%speed to dist

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n, error = len(dist), 1e-7
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for skips in range(n):
            dp[0][skips] = dist[0]

        for i in range(1, n):
            for skips in range(n):                                 # Note 2
                dp[i][skips] = min(dp[i-1][skips] + ((speed-dp[i-1][skips])%speed), dp[i-1][skips-1] if skips!=0 else 1e9) + dist[i]

        skipsNeeded = bisect_left(dp[-1], -hoursBefore*speed, key = lambda x:-x)
        return skipsNeeded if skipsNeeded!=n else -1