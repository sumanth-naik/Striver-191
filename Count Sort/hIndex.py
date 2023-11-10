# Key Idea: Since the problem can be solved if the arr is sorted and 0<=num<n, we can use count sort

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        countsArr = [0]*(n+1)
        for count in citations:
            countsArr[min(n, count)] += 1

        cumulativeCount = 0
        for index in range(n, -1, -1):
            cumulativeCount += countsArr[index]
            if cumulativeCount>=index: return index



'''Other Ideas'''

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return sum(num>=index+1 for index, num in enumerate(sorted(citations, reverse=True)))

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
        