class Solution:
    def partition(self, s):
        partitions, n = [], len(s)

        def backtracking(index, curr):
            if index==n: 
                partitions.append(deepcopy(curr))
            else:
                for next in range(index, n):
                    substr = s[index:next+1]
                    if substr==substr[::-1]:
                        curr.append(substr)
                        backtracking(next+1, curr)
                        curr.pop()
                        
        backtracking(0, [])
        return partitions

class Solution:
    def partition(self, s):
        @lru_cache(None)
        def getAllPalindromesLengthsStartingFromFirstElement(index):
            sPart = s[index:]
            kmpString = sPart+"#"+sPart[::-1]

            lpsArr, prevLpsLength = [0 for _ in range(len(kmpString))], 0
            for index in range(1, len(lpsArr)):
                while prevLpsLength!=0 and kmpString[index]!=kmpString[prevLpsLength]:
                    prevLpsLength = lpsArr[prevLpsLength-1]
                if kmpString[index]==kmpString[prevLpsLength]:
                    prevLpsLength+=1
                    lpsArr[index] = prevLpsLength

            palindromesLengths, lpsIndex = [lpsArr[-1]], lpsArr[-1]-1
            while lpsArr[lpsIndex]>0:
                palindromesLengths.append(lpsArr[lpsIndex])
                lpsIndex = lpsArr[lpsIndex-1]
            return palindromesLengths

        possiblePartitions, n = set(), len(s)
        def recursion(index, currPartition):
            if index==n:
                possiblePartitions.add(tuple(currPartition))
            else:
                palindromesLengthsStartingFromFirstElement = getAllPalindromesLengthsStartingFromFirstElement(index)
                for palindromeLengthStartingFromFirstElement in palindromesLengthsStartingFromFirstElement:
                    recursion(index+palindromeLengthStartingFromFirstElement, currPartition + [s[index:index+palindromeLengthStartingFromFirstElement]])

        recursion(0,[])
        return possiblePartitions
             