class Solution:
    def numDecodings(self, s: str) -> int:

        @lru_cache(None)
        def recursion(i):
            if i==len(s): return 1
            numberOfDecodingsFromI = 0
            if 1<=int(s[i])<=9: numberOfDecodingsFromI += recursion(i+1) 
            if i+1<len(s) and 10<=int(s[i:i+2])<=26: numberOfDecodingsFromI += recursion(i+2)
            return numberOfDecodingsFromI
        
        return recursion(0)