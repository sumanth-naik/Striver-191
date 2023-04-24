class Solution:
    def nthUglyNumber(self, n: int) -> int:
        twoIndex, threeIndex, fiveIndex = 0, 0, 0
        uglyNumbers = [1]
        for _ in range(n-1):
            nextUglyNumber = min(2*uglyNumbers[twoIndex], 3*uglyNumbers[threeIndex], 5*uglyNumbers[fiveIndex])
            if nextUglyNumber==2*uglyNumbers[twoIndex]: twoIndex+=1
            if nextUglyNumber==3*uglyNumbers[threeIndex]: threeIndex+=1
            if nextUglyNumber==5*uglyNumbers[fiveIndex]: fiveIndex+=1
            uglyNumbers.append(nextUglyNumber)
        return uglyNumbers[-1]
    
