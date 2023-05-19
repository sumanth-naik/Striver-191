# from typing import List
# # greedy wont work with subtracting, we need to check subtree minimum value
# class Trie:
#     def __init__(self):
#         self.children = defaultdict(Trie)

#     def insert(self, num):
#         node, mask = self, 1<<29
#         while mask:
#             bit = 1 if num&mask else 0
#             node = node.children[bit]
#             mask >>= 1

#     def search(self, num, limit):
#         node, mask = self, 1<<29
#         limitLeft, currXor = limit, 0
#         while mask:
#             numBit = 1 if num&mask else 0
#             # if numBit is 0, pick child as 1 greedily if possible else 0
#             if numBit==0:
#                 if 1 in node.children and limitLeft>=mask:
#                     currXor |= mask
#                     limitLeft &= ~(mask)
#                     node = node.children[1]
#                 elif 0 in node.children:
#                     node = node.children[0]
#                 else: return -1
#             # if numBit is 1, pick child as 0 greedily if possible else 1
#             else:
#                 if 0 in node.children:
#                     currXor |= mask
#                     node = node.children[0]
#                 elif 1 in node.children:
#                     node = node.children[1]
#                 else: return -1
#             mask >>= 1
#         return currXor


# class Solution:
#     def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
#         trie = Trie()
#         for num in nums:
#             trie.insert(num)
#         for num, limit in queries:
#             yield trie.search(num, limit)

from typing import List
# TLE
class Trie:
    def __init__(self):
        self.children = {}
        self.minVal = float('inf')

    def insert(self, num):
        node, mask = self, 1<<29
        while mask:
            bit = 1 if num&mask else 0
            if not bit in node.children:
                node.children[bit] = Trie()
            node = node.children[bit]
            node.minVal = min(node.minVal, num)
            mask >>= 1

    def search(self, num, limit):
        node, mask, currXor = self, 1<<29, 0
        while mask:
            numBit = 1 if num&mask else 0
            # if numBit is 0, pick child as 1 greedily if possible else 0 if possible
            if numBit==0:
                if 1 in node.children and node.children[1].minVal<=limit:
                    currXor |= mask
                    node = node.children[1]
                elif 0 in node.children and node.children[0].minVal<=limit:
                    node = node.children[0]
                else: return -1
            # if numBit is 1, pick child as 0 greedily if possible else 1 if possible
            else:
                if 0 in node.children and node.children[0].minVal<=limit:
                    currXor |= mask
                    node = node.children[0]
                elif 1 in node.children and node.children[1].minVal<=limit:
                    node = node.children[1]
                else: return -1
            mask >>= 1
        return currXor


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        trie = Trie()
        for num in nums:
            trie.insert(num)
        for num, limit in queries:
            yield trie.search(num, limit)



from typing import List
# TLE
class Trie:
    def __init__(self):
        self.children = {}

    def insert(self, num):
        node, mask = self, 1<<29
        while mask:
            bit = 1 if num&mask else 0
            if not bit in node.children:
                node.children[bit] = Trie()
            node = node.children[bit]
            mask >>= 1

    def search(self, num):
        node, mask, currXor = self, 1<<29, 0
        while mask:
            numBit = 1 if num&mask else 0
            if 1-numBit in node.children:
                currXor |= mask
                node = node.children[1-numBit]
            elif numBit in node.children:
                node = node.children[numBit]
            mask >>= 1
        return currXor


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        trie = Trie()
        nums.sort()
        lastInsertedIndex, ansArr = -1, [-1 for _ in range(len(queries))]
        queries = [(num, limit, index) for index, (num, limit) in enumerate(queries)]
        for num, limit, index in sorted(queries, key=lambda x:x[1]):
            while lastInsertedIndex+1<len(nums) and nums[lastInsertedIndex+1]<=limit:
                trie.insert(nums[lastInsertedIndex+1])
                lastInsertedIndex += 1
            if lastInsertedIndex!=-1: ansArr[index] = trie.search(num)
        return ansArr
    

import bisect
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()

        for num, limit in queries:
            start, stop, greedyRightBitsMask, greedyLeftBitsMask, nonGreedyRightBitsMask = 0, bisect.bisect_right(nums, limit), 0, 0, 0
            if stop==start: 
                yield -1
                continue
            for bitIndex in range(30)[::-1]:
                bitMask = 1<<bitIndex
                cut = bisect.bisect_left(nums, greedyRightBitsMask|bitMask|nonGreedyRightBitsMask, start, stop)
                # if bitIndex'th bit is set in num, try greedy left else forced right
                if num&bitMask:
                    # if cut==start: greedyRightBitsMask|bitMask = nums[cut] => nums[cut] has bitIndex'th bit set => it belongs to right half
                    # actual left half exists => there is atleast one number with bitIndex'th bit not set
                    if cut>start:
                        greedyLeftBitsMask |= bitMask
                        stop = cut # not cut+1 since cut itself has bitIndex'th bit set
                    else:
                        nonGreedyRightBitsMask |= bitMask
                        # start = cut
                        # start is already at cut, so not required
                # if bitIndex'th bit is not set in num, try greedy right else forced left
                else:
                    if cut<stop:
                        greedyRightBitsMask |= bitMask
                        start = cut
                    # else:
                    #     stop = cut
                    # stop is already at cut, so not required

            yield greedyRightBitsMask | greedyLeftBitsMask
                

import bisect
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()

        for num, limit in queries:
            start, stop, maxXoredNumbersBitsSoFar = 0, bisect.bisect_right(nums, limit), 0
            if stop==start: 
                yield -1
                continue
            for bitIndex in range(30)[::-1]:
                bitMask = 1<<bitIndex
                cut = bisect.bisect_left(nums, maxXoredNumbersBitsSoFar|bitMask, start, stop)
                # greedyRightBitsMask and nonGreedyRightBitsMask are stored in maxXoredNumbersBitsSoFar
                # we xor with num at the end to remove nonGreedyRightBitsMask and add greedyLeftBitsMask
                if num&bitMask and cut>start:
                    stop = cut 
                elif cut<stop:
                    maxXoredNumbersBitsSoFar |= bitMask
                    start = cut

            yield maxXoredNumbersBitsSoFar^num
                