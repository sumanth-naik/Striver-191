#TLE
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:    
        aMultiple = a
        bMultiple = b
        cMultiple = c

        while(True):
            minVal = min(aMultiple, bMultiple, cMultiple)
            if(n==1):
                return minVal
            if aMultiple == minVal:
                aMultiple += a
            if bMultiple == minVal:
                bMultiple += b
            if cMultiple == minVal:
                cMultiple += c

            n = n-1

import math
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:    

        def getNumUglyNumbers(num, a, b, c):
            lcmAB = (a*b)//math.gcd(a,b)
            lcmBC = (b*c)//math.gcd(b,c)
            lcmCA = (c*a)//math.gcd(c,a)
            lcmABC = (lcmAB*lcmBC)//math.gcd(lcmAB, lcmBC)
            return num//a + num//b + num//c - num//lcmAB - num//lcmBC - num//lcmCA + num//lcmABC

        low, high = min(a,b,c), min(a,b,c)*n

        while low<high:
            mid = (low+high)//2
            numUglyNumbersTillMid = getNumUglyNumbers(mid, a, b, c)
            if numUglyNumbersTillMid==n: high = mid
            elif numUglyNumbersTillMid>n: high = mid-1
            else: low = mid+1
        return low