# TLE O(nlogn) TC O(n) SC
import bisect
from sortedcontainers import SortedList
class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        sortedList = SortedList()

        ansArr = [-1 for _ in range(len(queries))]
        queryNumToIndexMap = defaultdict(list)
        for index, query in enumerate(queries):
            queryNumToIndexMap[query[0]].append(index)

        adjList = defaultdict(list)
        for node, parent in enumerate(parents):
            adjList[parent].append(node)


        def getMaxXorWithBinarySearch(num):
            start, stop = 0, len(sortedList)
            greedyLeftsBitsMask = greedyRightsBitsMask = forcedRightsBitsMask = 0
            for bitIndex in range(18)[::-1]:
                bitMask = (1 << bitIndex)
                cutIndex = bisect.bisect_left(sortedList, bitMask | greedyRightsBitsMask | forcedRightsBitsMask, start, stop)
                if bitMask & num:
                    # greedy left exists
                    if cutIndex!=start:
                        greedyLeftsBitsMask |= bitMask
                        stop = cutIndex
                    else:
                        forcedRightsBitsMask |= bitMask
                else:
                    # greedy right exists
                    if cutIndex!=stop:
                        greedyRightsBitsMask |= bitMask
                        start = cutIndex
                    #else:
                        # do nothing
            return greedyRightsBitsMask | greedyLeftsBitsMask


        def dfs(node):
            nonlocal sortedList, ansArr
            sortedList.add(node)

            for index in queryNumToIndexMap[node]:
                ansArr[index] = getMaxXorWithBinarySearch(queries[index][1])

            for neigh in adjList[node]:
                dfs(neigh)

            sortedList.discard(node)

        dfs(adjList[-1][0])
        return ansArr

# O(n) TC and SC
from collections import defaultdict
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)

    def insert(self, num):
        node = self
        for bitIndex in range(18)[::-1]:
            bit = 1 if (1<<bitIndex) & num else 0
            node = node.children[bit]
    def delete(self, num, bitIndex=17):
        if bitIndex<0: return True
        bit = 1 if (1 << bitIndex) & num else 0
        if self.children[bit].delete(num, bitIndex-1):
            del self.children[bit]
        return not self.children

    def getMaxXor(self, num):
        node, xorValue = self, 0
        for bitIndex in range(18)[::-1]:
            bit = 1 if (1<<bitIndex) & num else 0
            # greedy opposite
            if 1-bit in node.children:
                xorValue |= (1<<bitIndex)
                node = node.children[1-bit]
            else:
                node = node.children[bit]
        return xorValue


class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        trie = Trie()
        ansArr = [-1 for _ in range(len(queries))]
        queryNumToIndexMap = defaultdict(list)
        for index, query in enumerate(queries):
            queryNumToIndexMap[query[0]].append(index)

        adjList = defaultdict(list)
        for node, parent in enumerate(parents):
            adjList[parent].append(node)

        def dfs(node):
            nonlocal trie, ansArr
            trie.insert(node)

            for index in queryNumToIndexMap[node]:
                ansArr[index] = trie.getMaxXor(queries[index][1])

            for neigh in adjList[node]:
                dfs(neigh)
            trie.delete(node)

        dfs(adjList[-1][0])
        return ansArr




class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:

        ansArr = [-1 for _ in range(len(queries))]
        queryNumToIndexMap = defaultdict(list)
        for index, query in enumerate(queries):
            queryNumToIndexMap[query[0]].append(index)

        adjList = defaultdict(list)
        for node, parent in enumerate(parents):
            adjList[parent].append(node)

        prefixLengthsToPrefixesCounter = defaultdict(lambda : defaultdict(int))
        def getMaxXorWithPrefixSearch(num):
            prefixOfAnsSoFar = 0
            for bitShifts in range(17, -1, -1):
                numBit = 1 if num & (1<<bitShifts) else 0
                choice1, choice2 = (prefixOfAnsSoFar<<1) | (1-numBit), (prefixOfAnsSoFar<<1) | numBit
                prefixOfAnsSoFar = choice1 if prefixLengthsToPrefixesCounter[18-bitShifts][choice1]>0 else choice2
            return num^prefixOfAnsSoFar

        def dfs(node):
            nonlocal prefixLengthsToPrefixesCounter, ansArr
            num = node
            for prefixLength in range(18, 0, -1):
                prefixLengthsToPrefixesCounter[prefixLength][num] += 1
                num >>= 1

            for index in queryNumToIndexMap[node]:
                ansArr[index] = getMaxXorWithPrefixSearch(queries[index][1])

            for neigh in adjList[node]:
                dfs(neigh)

            num = node
            for prefixLength in range(18, 0, -1):
                prefixLengthsToPrefixesCounter[prefixLength][num] -= 1
                num >>= 1

        dfs(adjList[-1][0])
        return ansArr