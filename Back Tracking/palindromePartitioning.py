class Solution:
    def partition(self, s):
        # possiblePartitions, n = set(), len(s)
        # def isPalindrome(i,j):
        #     while i<=j:
        #         if not s[i]==s[j]: return False
        #         i += 1
        #         j -= 1
        #     return True
        # def recursion(index, currPartition):
        #     if index==n:
        #         possiblePartitions.add(tuple(currPartition))
        #     else:
        #         i = index
        #         while i<n and isPalindrome(index, i):
        #             recursion(i+1, currPartition + [s[index:i+1]])
        #             i += 1

        # recursion(0,[])
        # #return possiblePartitions


        def kmpAlgoForPalindromeDetection(string):
            totalString = string + '#' + string[::-1]
            lpsLengthsArray, prevLpsLength = [0], 0
            for index in range(1,len(totalString)):
                while prevLpsLength!=0 and totalString[prevLpsLength]!=totalString[index]:
                    prevLpsLength = lpsLengthsArray[prevLpsLength-1]
                if totalString[prevLpsLength]==totalString[index]:
                    prevLpsLength += 1
                lpsLengthsArray.append(prevLpsLength)
            
        memo = {}
        def getAllPalindromesLengthsStartingFromFirstElement(string):
            if string in memo:
                return memo[string]
            totalString = string + '#' + string[::-1]
            lpsLengthsArray, prevLpsLength, lengthsMap = [0], 0, {}
            for index in range(1,len(totalString)):
                while prevLpsLength!=0 and totalString[prevLpsLength]!=totalString[index]:
                    prevLpsLength = lpsLengthsArray[prevLpsLength-1]
                if totalString[prevLpsLength]==totalString[index]:
                    prevLpsLength += 1
                lpsLengthsArray.append(prevLpsLength)
                if index>len(totalString)//2:
                    lengthsMap[prevLpsLength] = index
            palindromesLengthsStartingFromFirstElement = [1]
            for length in range(2, lpsLengthsArray[-1]):
                index = len(totalString) - lengthsMap[length] - 1 + length - 1
                while lpsLengthsArray[index]>length:
                    index = lpsLengthsArray[index] - 1
                if lpsLengthsArray[index]==length:
                    palindromesLengthsStartingFromFirstElement.append(length)
            memo[string] = set(palindromesLengthsStartingFromFirstElement + [lpsLengthsArray[-1]])
            return memo[string]

        possiblePartitions, n = set(), len(s)
        def recursion(index, currPartition):
            if index==n:
                possiblePartitions.add(tuple(currPartition))
            else:
                palindromesLengthsStartingFromFirstElement = getAllPalindromesLengthsStartingFromFirstElement(s[index:])
                for palindromeLengthStartingFromFirstElement in palindromesLengthsStartingFromFirstElement:
                    recursion(index+palindromeLengthStartingFromFirstElement, currPartition + [s[index:index+palindromeLengthStartingFromFirstElement]])

        recursion(0,[])
        return possiblePartitions
                