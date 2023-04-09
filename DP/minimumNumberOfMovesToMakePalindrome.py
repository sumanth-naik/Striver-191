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