class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        numMoves, s = 0, list(s)
        while s:
            i = s.index(s[-1])
            # if only element, then make it to centre
            if i==len(s)-1: numMoves += len(s)//2
            # consider a..b....a.....b
            # even if we move a or b we will end up with ab side to side
            # ab......ba or ba......ab (doesnt matter which we swap, left or right)
            else:
                numMoves += i
                s.pop(i)
            s.pop()
        return numMoves


class BIT:
    def __init__(self, size):
        self.size = size + 1
        self.bit = [0 for _ in range(self.size)]

    def add(self, index, val):
        index += 1
        while index<self.size:
            self.bit[index] += val
            index += (index & -index)
        
    def sumTill(self, index):
        index += 1
        total = 0
        while index>0:
            total += self.bit[index]
            index -= (index & -index)
        return total
    
from collections import deque
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        totalMoves, s, n = 0, list(s), len(s)
        bit = BIT(n)

        charToIndicesMap = defaultdict(deque)
        for index, char in enumerate(s):
            charToIndicesMap[char].append(index)

        for index in range(n)[::-1]:
            char = s[index]
            if len(charToIndicesMap[char]):
                firstIndex = charToIndicesMap[char][0]
                moves = firstIndex - bit.sumTill(firstIndex)
                # if only single element, moves will simply be index - numused => len of unused chars
                if len(charToIndicesMap[s[index]])==1:
                    moves //= 2
                else:
                    charToIndicesMap[char].popleft()
                totalMoves += moves
                charToIndicesMap[char].pop()
                bit.add(firstIndex, 1) #no need to add for index, as we wont be querying anyway
        return totalMoves

        
