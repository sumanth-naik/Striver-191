class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        wordDict, n = set(wordDict), len(s)

        @lru_cache(None)
        def recursion(i, j):
            if j==n: return i==j
            if s[i:j+1] in wordDict and recursion(j+1, j+1): return True
            if recursion(i, j+1): return True
            return False
        
        return recursion(0, 0)