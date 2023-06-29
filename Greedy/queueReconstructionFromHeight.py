import heapq

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        unseenSet = set([tuple(p) for p in people])
        minHeap = []

        sortedHeights = sorted(list(set(h for h, k in people)))
        heightToCountMap = defaultdict(int)

        while unseenSet or minHeap:
            nextUnseenSet = set()
            for height, peopleInFront in unseenSet:
                if heightToCountMap[height]==peopleInFront:
                    heapq.heappush(minHeap, (height, peopleInFront))
                else:
                    nextUnseenSet.add((height, peopleInFront))

            heightToAdd, peopleInFrontToAdd = heapq.heappop(minHeap)
            for height in sortedHeights:
                if height<=heightToAdd: heightToCountMap[height] += 1
                else: break
            
            yield([heightToAdd, peopleInFrontToAdd])

            unseenSet = nextUnseenSet


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ansArr = []
        for height, peopleInFront in sorted(people, key=lambda x:(-x[0],x[1])):
            ansArr.insert(peopleInFront, [height, peopleInFront])
        return ansArr




class BIT:
    def __init__(self, arrSize) -> None:
        self.treeSize = arrSize + 1
        self.bit = [0 for _ in range(self.treeSize)]
        for index in range(arrSize):
            self.update(index, 0, 1)

    def update(self, arrIndex, oldVal, newVal):
        val = newVal - oldVal
        treeIndex = arrIndex+1
        while treeIndex<self.treeSize:
            self.bit[treeIndex] += val
            treeIndex += (treeIndex & -treeIndex)
    
    def getSumTill(self, arrIndex):
        treeIndex = arrIndex + 1
        total = 0
        while treeIndex>0:
            total += self.bit[treeIndex]
            treeIndex -= (treeIndex & -treeIndex)
        return total

import bisect
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        bit, rangeArr, outputArr = BIT(n), range(n), [None for _ in range(n)]

        for height, numPrevEmptyPositions in sorted(people, key=lambda x:(x[0], -x[1])):
            index = bisect.bisect_left(rangeArr, numPrevEmptyPositions+1, key=lambda i: bit.getSumTill(i))
            outputArr[index] = [height, numPrevEmptyPositions]
            bit.update(index, 1, 0)

        return outputArr
    

import bisect
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        bit, outputArr = BIT(n), [None for _ in range(n)]

        def getIndexToFill(numUnusedPositionsNeeded):
            low, high = 0, n-1
            while low<high:
                mid = (low+high)//2
                unusedPositions = bit.getSumTill(mid)
                if unusedPositions<numUnusedPositionsNeeded:
                    low = mid + 1
                else:
                    high = mid
            return low
            

        for height, numPrevEmptyPositions in sorted(people, key=lambda x:(x[0], -x[1])):
            index = getIndexToFill(numPrevEmptyPositions+1)
            outputArr[index] = [height, numPrevEmptyPositions]
            bit.update(index, 1, 0)

        return outputArr
    


import bisect
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        bit, rangeArr, outputArr = BIT(n), range(n), [None for _ in range(n)]

        def customBisectLeft(arr, need, key):
            low, high = 0, len(arr)
            while low<high:
                mid = (low+high)//2
                if key(mid)<need:
                    low = mid + 1
                else:
                    high = mid
            return low

        for height, numPrevEmptyPositions in sorted(people, key=lambda x:(x[0], -x[1])):
            index = customBisectLeft(rangeArr, numPrevEmptyPositions+1, key=lambda i: bit.getSumTill(i))
            outputArr[index] = [height, numPrevEmptyPositions]
            bit.update(index, 1, 0)

        return outputArr
    


import bisect
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        bit, rangeArr, outputArr = BIT(n), range(n), [None for _ in range(n)]
        # unnecessary space for rangeArr and arr is not exactly needed
        def customBisectRight(arr, need, key):
            low, high = 0, len(arr)
            while low<high:
                mid = (low+high)//2
                if key(mid)<=need:
                    low = mid + 1
                else:
                    high = mid
            return low

        for height, numPrevEmptyPositions in sorted(people, key=lambda x:(x[0], -x[1])):
            index = customBisectRight(rangeArr, numPrevEmptyPositions, key=lambda i: bit.getSumTill(i))
            outputArr[index] = [height, numPrevEmptyPositions]
            bit.update(index, 1, 0)

        return outputArr