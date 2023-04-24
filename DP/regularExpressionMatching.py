class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        @lru_cache(None)
        def recursion(i, j):
            if i==m or j==n: return i==m and (j==n or (all(p[jIndex]=="*" for jIndex in range(j+1, n, 2)) and (n-j)%2==0))
            if j+1<n and p[j+1]=="*":
                if p[j]=="." or s[i]==p[j]:
                    return recursion(i+1, j) or recursion(i+1, j+2) or recursion(i, j+2)
                return recursion(i, j+2)
            elif s[i]==p[j] or p[j]==".":
                return recursion(i+1, j+1)
            return False
        
        return recursion(0, 0)



class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        @lru_cache(None)
        def recursion(i, j):
            if i >= len(s) and j >= len(p):
                return True 
            if j >= len(p):
                return False
            if j+1<n and p[j+1]=="*":
                if i<m and (p[j]=="." or s[i]==p[j]):
                    return recursion(i+1, j) or recursion(i+1, j+2) or recursion(i, j+2)
                return recursion(i, j+2)
            elif i<m and (p[j]=="." or s[i]==p[j]):
                return recursion(i+1, j+1)
            return False
        
        return recursion(0, 0)



