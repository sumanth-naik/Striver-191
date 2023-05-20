from os import *
from sys import *
from collections import *
from math import *

def palindromesAtIndex(s, ind, length):
    s = s[ind-1:]

    def palindromesLengthsFromBeginning(s):
        kmpString = s+"#"+s[::-1]

        lpsArr, prevLpsLength = [0 for _ in range(len(kmpString))], 0
        lpsLengthToIndexMap, centerIndex = defaultdict(int), len(kmpString)//2
        for index in range(1, len(lpsArr)):
            while prevLpsLength!=0 and kmpString[index]!=kmpString[prevLpsLength]:
                prevLpsLength = lpsArr[prevLpsLength-1]
            if kmpString[index]==kmpString[prevLpsLength]:
                prevLpsLength+=1
                lpsArr[index] = prevLpsLength
            if index>centerIndex and prevLpsLength!=0:
                lpsLengthToIndexMap[prevLpsLength] = index

        palindromesLengths = [lpsArr[-1]]
        for length, index in lpsLengthToIndexMap.items():
            mirrorEndIndex = 2*centerIndex - index + (lpsArr[index]-1)
            while lpsArr[mirrorEndIndex]>length:
                mirrorEndIndex = lpsArr[mirrorEndIndex-1]
            if lpsArr[mirrorEndIndex]==length:
                palindromesLengths.append(length)

        return palindromesLengths

    return sum(1 for l in palindromesLengthsFromBeginning(s) if l>=length)