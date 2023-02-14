from itertools import chain
class Solution:
    def convert(self, s: str, numRows: int):
        if numRows==1: return s
        zigZagArrays, zigZagArrayIndex, increment = [[] for i in range(numRows)], 0, 1
        for ch in s:
            if zigZagArrayIndex==-1:
                zigZagArrayIndex += 2
                increment = -increment
            elif zigZagArrayIndex==numRows:
                zigZagArrayIndex -= 2
                increment = -increment
            zigZagArrays[zigZagArrayIndex].append(ch)
            zigZagArrayIndex += increment
        return "".join(chain.from_iterable(zigZagArrays))