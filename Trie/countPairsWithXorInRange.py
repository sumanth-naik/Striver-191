
from typing import List
# TLE
# class Trie:
#     def __init__(self) -> None:
#         self.children = defaultdict(Trie)
#         self.count = 0
        
#     def insert(self, bitsArr):
#         node = self
#         for bit in bitsArr:
#             node = node.children[bit]
#         node.count += 1

#     def numXorWithinLowAndHigh(self, node, bitsArr, indexInBitsArr, low, high, currNum):
#         if currNum>high: return 0
#         if indexInBitsArr==len(bitsArr): return node.count if low<=currNum<=high else 0

#         count, mask = 0, 1<<(len(bitsArr)-indexInBitsArr-1)
#         for bit in node.children:
#             if (bitsArr[indexInBitsArr] ^ bit):
#                 count += self.numXorWithinLowAndHigh(node.children[bit], bitsArr, indexInBitsArr+1, low, high, currNum|mask)
#             else:
#                 count += self.numXorWithinLowAndHigh(node.children[bit], bitsArr, indexInBitsArr+1, low, high, currNum)
#         return count



# class Solution:
#     def countPairs(self, nums: List[int], low: int, high: int) -> int:

#         maxInNums = max(nums)
#         numBitsInMax = 0
#         while maxInNums:
#             numBitsInMax += 1
#             maxInNums >>= 1

#         def getArrOfBits(num):
#             arr, size = [], numBitsInMax
#             while num or size:
#                 arr.append(num&1)
#                 num >>= 1
#                 size -= 1
#             return arr[::-1]
        
#         trie, count = Trie(), 0
#         for num in nums:
#             bitsArr = getArrOfBits(num)
#             count += trie.numXorWithinLowAndHigh(trie, bitsArr, 0, low, high, 0)
#             trie.insert(bitsArr)
#         return count
    




class Trie:
    def __init__(self) -> None:
        self.children = defaultdict(Trie)
        self.countInSubtree = 0
        
    def insert(self, num):
        node, mask = self, 1<<14
        while mask:
            bit = 1 if mask&num else 0
            node = node.children[bit]
            node.countInSubtree += 1
            mask >>= 1

    def numXorLesserThan(self, limit, num, indexInNum):
        if not self.children: return 0
        mask, count = 1<<indexInNum, 0
        numBit, limitBitMask = 1 if num&mask else 0, limit&mask
        # if limit bit is 0, go to a side which gives xor as 0
        if not limitBitMask:
            if numBit in self.children:
                count += self.children[numBit].numXorLesserThan(limit, num, indexInNum-1)
        # if limit bit is 1, add all 0 xor side and call 1 xor side
        else:
            # 0 xor side
            if numBit in self.children:
                count += self.children[numBit].countInSubtree
            # 1 xor side
            if 1-numBit in self.children:
                count += self.children[1-numBit].numXorLesserThan(limit, num, indexInNum-1)

        return count
    
    def numXorWithinLowAndHigh(self, num, low, high):
        return self.numXorLesserThan(high+1, num, 14) - self.numXorLesserThan(low, num, 14)


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trie, count = Trie(), 0
        for num in nums:
            count += trie.numXorWithinLowAndHigh(num, low, high)
            trie.insert(num)
        return count
    