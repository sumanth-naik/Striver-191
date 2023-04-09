class Solution:
    def numTeams(self, rating):
        numTrios = 0
        @cache
        def memoization(index):
            nonlocal numTrios
            numIncreasingPairsTillIndex, numDecreasingPairsTillIndex = 0, 0
            for k in range(index):
                if rating[k]>rating[index]:
                    _, numDecreasingPairsTillK = memoization(k)
                    numTrios += numDecreasingPairsTillK
                    numDecreasingPairsTillIndex += 1
                elif rating[k]<rating[index]:
                    numIncreasingPairsTillK, _ = memoization(k)
                    numTrios += numIncreasingPairsTillK
                    numIncreasingPairsTillIndex += 1
            return numIncreasingPairsTillIndex, numDecreasingPairsTillIndex
        memoization(len(rating)-1)
        return numTrios

class Solution:
    def numTeams(self, rating):
        numTrios, n = 0, len(rating)
        # numIncreasingPairsTillIndex, numDecreasingPairsTillIndex
        dp = [[0, 0] for _ in range(n)]

        for i in range(n):
            incPairs, decPairs = 0, 0
            for k in range(i):
                if rating[k]<rating[i]:
                    numTrios += dp[k][0]
                    incPairs += 1
                else:
                    numTrios += dp[k][1]
                    decPairs += 1
            dp[i] = [incPairs, decPairs]
        return numTrios

from sortedcontainers import SortedList
from bisect import bisect_left
class Solution:
    def numTeams(self, rating):
        left = SortedList()
        right = SortedList(rating)
        numTrios = 0

        def getSplit(sortedList, num):
            i = bisect_left(sortedList, num)
            return i, len(sortedList) - i

        for num in rating:
            right.remove(num)
            smallerInLeft, largerInLeft = getSplit(left, num)
            smallerInRight, largerInRight = getSplit(right, num)
            numTrios += smallerInLeft*largerInRight + smallerInRight*largerInLeft
            left.add(num)
        return numTrios
    

