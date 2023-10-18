class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return sum(1 for index, num in enumerate(sorted(citations, reverse=True)) if num>=index+1)

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        def isGood(target):
            return sum(1 for num in citations if num>=target)>=target

        low, high = 1, len(citations)
        while low<high:
            mid = (low+high+1)//2
            if isGood(mid):
                low = mid
            else:
                high = mid - 1
        return low


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        countsArr = [0 for _ in range(n+1)]
        for count in citations:
            if count>=n: countsArr[n] += 1
            else: countsArr[count] += 1

        cumulativeCount = 0
        for index in range(n, -1, -1):
            cumulativeCount += countsArr[index]
            if cumulativeCount>=index: return index
        

