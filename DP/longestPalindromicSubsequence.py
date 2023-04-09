class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def longestCommonSubsequence(text1, text2, i=0, j=0):
            if i==len(text1):
                return 0
            if j==len(text2):
                return 0
            maxVal = 0
            if text1[i]==text2[j]:
                maxVal = 1 + longestCommonSubsequence(text1, text2, i+1, j+1)
            maxVal = max([maxVal, longestCommonSubsequence(text1, text2, i+1, j), longestCommonSubsequence(text1, text2, i, j+1)])
            return maxVal

        return longestCommonSubsequence(s,s[::-1])
    
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        def longestCommonSubsequence(text1, text2):
            m, n = len(text1), len(text2)
            dpNextRow = [0]*(n+1)

            for i in range(m-1, -1, -1):
                dpCurrRow = [0]*(n+1)
                for j in range(n-1, -1, -1):
                    if text1[i]==text2[j]: dpCurrRow[j] = 1 + dpNextRow[j+1]
                    dpCurrRow[j] = max(dpCurrRow[j], dpCurrRow[j+1], dpNextRow[j])
                dpNextRow = dpCurrRow
            return dpNextRow[0]

        return longestCommonSubsequence(s,s[::-1])

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @lru_cache(None)
        def memoization(left, right):
            if left==right: return 1
            if left>right: return 0
            return max((2+memoization(left+1, right-1)) if s[left]==s[right] else 0, memoization(left+1, right), memoization(left, right-1))

        return memoization(0, len(s)-1)
    
from collections import deque    
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dpNextRow = deque([0,1])

        for left in range(n-2, -1, -1):
            dpCurrRow = deque([1])
            for right in range(left+1, n):
                dpCurrRow.append(max((2+dpNextRow[right-1-left]) if s[left]==s[right] else 0, dpNextRow[right-left], dpCurrRow[-1]))
            dpCurrRow.appendleft(0)
            dpNextRow = dpCurrRow
        return dpNextRow[-1]            
    
    
from collections import deque    
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dpNextRow = deque([0,1])

        for left in range(n-2, -1, -1):
            dpCurrRow = deque([1])
            for right in range(left+1, n):
                dpCurrRow.append(max((2+dpNextRow[len(dpCurrRow)-1]) if s[left]==s[right] else 0, dpNextRow[len(dpCurrRow)], dpCurrRow[-1]))
            dpCurrRow.appendleft(0)
            dpNextRow = dpCurrRow
        return dpNextRow[-1]            