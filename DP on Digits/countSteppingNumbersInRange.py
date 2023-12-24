# Key Idea 1: Digit DP with another boolean to tell whether number started or not
# Key Idea 2: prevDigit is needed to determine the possibilities

class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        
        def dpHelper(num):
            
            @cache
            def dp(index, hasNonZeroDigit, isDigitRestricted, prevDigit):
                if index==len(num):
                    return 1 and prevDigit!=-1
                
                count, limit = 0, int(num[index]) if isDigitRestricted else 9
                for digit in range(limit+1):
                    if not hasNonZeroDigit:
                        count += dp(index+1, digit>0, isDigitRestricted and digit==limit, digit)
                    elif digit in [prevDigit+1, prevDigit-1]:
                        count += dp(index+1, True, isDigitRestricted and digit==limit, digit)
                return count

            return dp(0, 0, 1, -1)

        return (dpHelper(str(high)) - dpHelper(str(int(low)-1)))%(10**9+7)