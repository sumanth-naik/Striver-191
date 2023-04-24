class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        @lru_cache(None)
        def recursion(i, j):
            if i==m or j==n: return i==m and (j==n or p[j:]=="*"*(n-j+1))
            if p[j]=="*":
                return recursion(i+1, j) or recursion(i+1, j+1) or recursion(i, j+1)
            elif p[j]=="?" or s[i]==p[j]:
                return recursion(i+1, j+1)
            return False
        
        return recursion(0, 0)