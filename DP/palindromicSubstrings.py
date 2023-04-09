from functools import lru_cache
class Solution:
    def countSubstrings(self, s: str) -> int:

        @lru_cache(maxsize=len(s)*len(s))
        def memoization(i, j):
            if i==j: return True
            if i+1==j: return s[i]==s[j]
            return True if s[i]==s[j] and memoization(i+1,j-1) else False
        
        count = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if memoization(i,j): count +=1
        return count
    


class Solution:
    def countSubstrings(self, s: str) -> int:
        n, count = len(s), 0
        dp = [[True for _ in range(n)] for _ in range(n)]
        for i in range(n): dp[i][i] = True
        
        for j in range(1, n):
            for i in range(j-1, -1, -1):
                dp[i][j] = (s[i]==s[j] and dp[i+1][j-1])
                if dp[i][j]: count += 1
        return count + len(s)
    
    


class Solution:
    def countSubstrings(self, s: str) -> int:
        n, count = len(s), 0
        dp = [[True for _ in range(n)] for _ in range(n)]
        for i in range(n): dp[i][i] = True
        
        for j in range(1, n):
            for i in range(j-1, -1, -1):
                dp[i][j] = (s[i]==s[j] and dp[i+1][j-1])
                if dp[i][j]: count += 1
        return count + len(s)
    


class Solution:
    def countSubstrings(self, s: str) -> int:
        n, count = len(s), len(s)
        dpMinusOne, dpMinusTwo = [True for _ in range(n)], [True for _ in range(n-1)]

        for delta in range(1, n):
            dp = []
            for startIndex in range(0, n-delta):
                i, j = startIndex, startIndex+delta
                dp.append(s[i]==s[j] and dpMinusTwo[startIndex])
            count += sum(dp)
            dpMinusTwo = dpMinusOne[1:len(dpMinusOne)-1]
            dpMinusOne = dp
        return count