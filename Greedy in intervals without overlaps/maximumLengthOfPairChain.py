class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = list(map(tuple, pairs))
        pairs.sort(key = lambda x: (x[0], x[1]))
        print(pairs)
        n = len(pairs)
        maxLengthArr = [-1 for _ in range(n)]

        def recursion(index):
            if maxLengthArr[index]!=-1: return
            maxLengthArr[index] = 1
            left, right = pairs[index]
            searchStart = bisect_left(pairs, (right+1, -1e9), index, n)
            if searchStart==n:
                return
            iter, searchEndNum = searchStart, pairs[searchStart][1]
            while iter<n and pairs[iter][0]<searchEndNum:
                searchEndNum = min(searchEndNum, pairs[iter][1])
                recursion(iter)
                maxLengthArr[index] = max(maxLengthArr[index], maxLengthArr[iter]+1)
                iter += 1
        
        for index in range(n): 
            recursion(index)
        return max(maxLengthArr)

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        chainLength, chainTail = 0, -1e9
        for left, right in sorted(pairs, key=lambda x:x[1]):
            if chainTail<left:
                chainLength += 1
                chainTail = right
        return chainLength