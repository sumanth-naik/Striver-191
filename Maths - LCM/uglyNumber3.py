# Key Idea 1: Use PIE with LCM to getNumUglyNumbers till some number
# Key Idea 2: a * b = LCM(a,b) * GCD(a*b)
# Key Idea 3: Use Binary Search on Answer

# def gcd(a, b):
#   if b == 0:
#     return a
#   else:
#     return gcd(b, (a % b))
  
import math
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:    

        def getNumUglyNumbers(num):
            lcmAB = (a*b)//math.gcd(a,b)
            lcmBC = (b*c)//math.gcd(b,c)
            lcmCA = (c*a)//math.gcd(c,a)
            lcmABC = (lcmAB*lcmBC)//math.gcd(lcmAB, lcmBC)
            return num//a + num//b + num//c - num//lcmAB - num//lcmBC - num//lcmCA + num//lcmABC

        low, high = min(a,b,c), min(a,b,c)*n

        while low<high:
            mid = (low+high)//2
            numUglyNumbersTillMid = getNumUglyNumbers(mid)
            if numUglyNumbersTillMid==n: high = mid
            elif numUglyNumbersTillMid>n: high = mid-1
            else: low = mid+1
        return low