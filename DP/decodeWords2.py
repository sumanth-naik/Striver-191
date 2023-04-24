class Solution:
    def numDecodings(self, s: str) -> int:

        @lru_cache(None)
        def recursion(i):
            if i==len(s): return 1
            numberOfDecodingsFromI = 0
            
            if s[i].isdigit() and 1<=int(s[i])<=9: numberOfDecodingsFromI += recursion(i+1) 
            if i+1<len(s) and s[i:i+2].isdigit() and 10<=int(s[i:i+2])<=26: numberOfDecodingsFromI += recursion(i+2)
            
            if s[i]=="*": numberOfDecodingsFromI += (9*recursion(i+1))
            if i+1<len(s):
                if s[i:i+2]=="**": numberOfDecodingsFromI += (15*recursion(i+2))
                elif s[i:i+2]=="1*": numberOfDecodingsFromI += (9*recursion(i+2))
                elif s[i:i+2]=="2*": numberOfDecodingsFromI += (6*recursion(i+2))
                elif s[i]=="*":
                    if s[i+1].isdigit():
                        if 0<=int(s[i+1])<=6: numberOfDecodingsFromI += (2*recursion(i+2))
                        else: numberOfDecodingsFromI += (recursion(i+2))

            
            return numberOfDecodingsFromI%(10**9+7)
        
        return recursion(0)