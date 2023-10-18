class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        @lru_cache(None)
        def getNumFactors(num, div):
            count = 0
            while num and num%div==0:
                count += 1
                num //= div
            return count
        
        fives, twos = 0, 0
        for num in range(n+1):
            fives += getNumFactors(num, 5)
            twos += getNumFactors(num, 2)
        return min(fives, twos)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n:
            count += n//5
            n //= 5
        return count

# 2147483647!
# =2 * 3 * ...* 5 ... *10 ... 15* ... * 25 ... * 50 ... * 125 ... * 250...
# =2 * 3 * ...* 5 ... * (5^1*2)...(5^1*3)...*(5^2*1)...*(5^2*2)...*(5^3*1)...*(5^3*2)... (Equation 1)
# Note the duplication: multiple of 25 is also multiple of 5, so multiple of 25 only provides one extra 5.
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return n//5 + n//25 + n//125 + n//625 + n//3125