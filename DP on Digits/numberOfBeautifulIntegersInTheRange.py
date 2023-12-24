# Key Idea 1: Digit DP with hasNonZeroDigit and isDigitRestricted
# Key Idea 2: maintain oddEvenDiff instead of oddCount and evenCount
# Key Idea 3: 123%4 = (100%4 + 20%4 + 3%4)%4  
#           => (modSoFar + digit*pow(10, len(num)-index-1))%k
#           => or simply (modSoFar*10 + digit)%k


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:

        def dpHelper(num):
            @cache
            def dp(index, hasNonZeroDigit, isDigitRestricted, oddEvenDiff, modSoFar):
                if index==len(num):
                    return (modSoFar%k)==0 and oddEvenDiff==0 and hasNonZeroDigit
                
                count, limit = 0, int(num[index]) if isDigitRestricted else 9
                for digit in range(limit+1):
                    hasNonZeroDigit |= (digit>0)
                    count += dp(index+1, \
                                hasNonZeroDigit, \
                                isDigitRestricted and digit==limit, \
                                oddEvenDiff + (hasNonZeroDigit)*((-1)**(digit&1)), \
                                (modSoFar*10 + digit)%k)
                return count
            return dp(0, 0, 1, 0, 0)
        
        return dpHelper(str(high)) - dpHelper(str(low-1))

