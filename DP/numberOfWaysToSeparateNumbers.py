# TLE
class Solution:
    def numberOfCombinations(self, num: str) -> int:
        n = len(num)

        @lru_cache(None)
        def getNum(i, j):
            if i<0: return -1
            if i==j: return int(num[i])
            return int(num[j]) + 10*getNum(i, j-1)
        
        @lru_cache(None)
        def recursion(prevNumberStartIndex, prevNumberEndIndex, currIndex):
            if currIndex==n: return 1 if prevNumberEndIndex==n-1 else 0
            if currIndex==prevNumberEndIndex+1 and num[currIndex]=="0": return 0
            totalCombinations = 0
            if prevNumberEndIndex-prevNumberStartIndex+1<=currIndex-prevNumberEndIndex and getNum(prevNumberEndIndex+1, currIndex) >= getNum(prevNumberStartIndex, prevNumberEndIndex):
                totalCombinations += recursion(prevNumberEndIndex+1, currIndex, currIndex+1)
            totalCombinations += recursion(prevNumberStartIndex, prevNumberEndIndex, currIndex+1)
            return totalCombinations % (10**9+7)
        
        return recursion(-1, -1, 0)
    
# TLE
class Solution:
    def numberOfCombinations(self, num: str) -> int:
        n = len(num)

        @lru_cache(None)
        def getNum(i, j):
            if i<0: return -1
            if i==j: return int(num[i])
            return int(num[j]) + 10*getNum(i, j-1)
        
        @lru_cache(None)
        def recursion(prevNumberStartIndex, prevNumberEndIndex):
            if prevNumberEndIndex==n-1: return 1
            if num[prevNumberEndIndex+1]=="0": return 0
            minLengthOfNextNum = prevNumberEndIndex-prevNumberStartIndex+1
            startIndex = prevNumberEndIndex+1
            totalCombinations = 0

            for endIndex in range(startIndex+minLengthOfNextNum-1, n):
                if getNum(startIndex, endIndex)>=getNum(prevNumberStartIndex, prevNumberEndIndex): 
                    totalCombinations+= recursion(startIndex, endIndex)
            return totalCombinations % (10**9+7)
        
        return recursion(-1, -1)
    

# TLE  
class Solution:
    def numberOfCombinations(self, num: str) -> int:
        n = len(num)

        @lru_cache(None)
        def getNum(i, j):
            if i<0: return -1
            if i==j: return int(num[i])
            return int(num[j]) + 10*getNum(i, j-1)
        
        @lru_cache(None)
        def recursion(prevNumberStartIndex, prevNumberEndIndex):
            if prevNumberEndIndex==n-1: return 1
            if num[prevNumberEndIndex+1]=="0": return 0
            minLengthOfNextNum = prevNumberEndIndex-prevNumberStartIndex+1
            startIndex = prevNumberEndIndex+1
            totalCombinations = 0
            endIndex = startIndex+minLengthOfNextNum-1
            if endIndex<n and getNum(startIndex, endIndex)>=getNum(prevNumberStartIndex, prevNumberEndIndex): 
                totalCombinations+= recursion(startIndex, endIndex)
            # length is greater, no need to check numbers
            for endIndex in range(startIndex+minLengthOfNextNum, n):
                totalCombinations+= recursion(startIndex, endIndex)
            return totalCombinations % (10**9+7)
        
        return recursion(-1, -1)
    


# TLE
class Solution:
    def numberOfCombinations(self, num: str) -> int:
        n = len(num)

        @lru_cache(None)
        def getNum(i, j):
            if i<0: return -1
            if i==j: return int(num[i])
            return int(num[j]) + 10*getNum(i, j-1)
        
        @lru_cache(None)
        def getCombinationsSum(startIndex, minLengthOfNextNum):
            # length is greater, no need to check numbers
            totalCombinations = 0
            for endIndex in range(startIndex+minLengthOfNextNum, n):
                totalCombinations+= recursion(startIndex, endIndex)
            return totalCombinations
        
        @lru_cache(None)
        def recursion(prevNumberStartIndex, prevNumberEndIndex):
            if prevNumberEndIndex==n-1: return 1
            if num[prevNumberEndIndex+1]=="0": return 0
            minLengthOfNextNum = prevNumberEndIndex-prevNumberStartIndex+1
            startIndex = prevNumberEndIndex+1
            totalCombinations = 0
            endIndex = startIndex+minLengthOfNextNum-1
            if endIndex<n and getNum(startIndex, endIndex)>=getNum(prevNumberStartIndex, prevNumberEndIndex): 
                totalCombinations+= recursion(startIndex, endIndex)
            totalCombinations += getCombinationsSum(startIndex, minLengthOfNextNum)
            return totalCombinations % (10**9+7)
        
        return recursion(-1, -1)
    
# MLE
class Solution:
    def numberOfCombinations(self, num: str) -> int:
        n = len(num)

        @lru_cache(None)
        def getNum(i, j):
            if i<0: return -1
            if i==j: return int(num[i])
            return int(num[j]) + 10*getNum(i, j-1)
        
        @lru_cache(None)
        def getCombinationsSum(startIndex, minLengthOfNextNum):
            if startIndex+minLengthOfNextNum<n:
                return recursion(startIndex, startIndex+minLengthOfNextNum) + getCombinationsSum(startIndex, minLengthOfNextNum+1)
            return 0
        
        @lru_cache(None)
        def recursion(prevNumberStartIndex, prevNumberEndIndex):
            if prevNumberEndIndex==n-1: return 1
            if num[prevNumberEndIndex+1]=="0": return 0
            minLengthOfNextNum = prevNumberEndIndex-prevNumberStartIndex+1
            startIndex = prevNumberEndIndex+1
            totalCombinations = 0
            endIndex = startIndex+minLengthOfNextNum-1
            if endIndex<n and getNum(startIndex, endIndex)>=getNum(prevNumberStartIndex, prevNumberEndIndex): 
                totalCombinations+= recursion(startIndex, endIndex)
            totalCombinations += getCombinationsSum(startIndex, minLengthOfNextNum)
            return totalCombinations % (10**9+7)
        
        return recursion(-1, -1)
    

class Solution:
    def numberOfCombinations(self, num: str) -> int:
        n = len(num)
        if num[0]=="0": return 0

        dpOfDiff = [[0 for _ in range(n+1)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if num[i]>num[j]: dpOfDiff[i][j] = -1
                elif num[i]<num[j]: dpOfDiff[i][j] = 1
                else: 
                    if dpOfDiff[i+1][j+1]<0: dpOfDiff[i][j] = dpOfDiff[i+1][j+1]-1                    
                    elif dpOfDiff[i+1][j+1]>0: dpOfDiff[i][j] = dpOfDiff[i+1][j+1]+1
    
        def isSecondGreaterThanOrEqual(i, j, length):
            return False if dpOfDiff[i][j]<0 and length>=abs(dpOfDiff[i][j]) else True
        

        dpOfCombinations = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n): dpOfCombinations[i][n-1] = 1

        dpOfCumulativeCombinations = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n): dpOfCumulativeCombinations[i][n-1] = 1

        for prevNumberStartIndex in range(n-2, -1, -1):
            for prevNumberEndIndex in range(prevNumberStartIndex, n-1):
                # print("iter", prevNumberStartIndex, prevNumberEndIndex)
                startIndex = prevNumberEndIndex+1
                if num[startIndex]=="0": continue
                minLengthOfNextNum = prevNumberEndIndex-prevNumberStartIndex+1
                endIndex = startIndex+minLengthOfNextNum-1
                if endIndex<n and isSecondGreaterThanOrEqual(prevNumberStartIndex, startIndex, minLengthOfNextNum): 

                    # print("found", prevNumberStartIndex, prevNumberEndIndex)
                    dpOfCombinations[prevNumberStartIndex][prevNumberEndIndex] = dpOfCumulativeCombinations[startIndex][endIndex]% (10**9+7)
                elif endIndex+1<n:
                    # print(prevNumberStartIndex, prevNumberEndIndex)

                    dpOfCombinations[prevNumberStartIndex][prevNumberEndIndex] = dpOfCumulativeCombinations[startIndex][endIndex+1]% (10**9+7)
            for prevNumberEndIndex in range(n-2, prevNumberStartIndex-1, -1):
                # print(prevNumberStartIndex, prevNumberEndIndex)
                dpOfCumulativeCombinations[prevNumberStartIndex][prevNumberEndIndex] = dpOfCombinations[prevNumberStartIndex][prevNumberEndIndex] + dpOfCumulativeCombinations[prevNumberStartIndex][prevNumberEndIndex+1] 
        # print(dpOfCombinations)
        # print(dpOfCumulativeCombinations)
        return dpOfCumulativeCombinations[0][0]% (10**9+7)
    
    

class Solution:
    def numberOfCombinations(self, num: str) -> int:
        n = len(num)
        if num[0]=="0": return 0

        dpOfDiff = [[0 for _ in range(n+1)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if num[i]>num[j]: dpOfDiff[i][j] = -1
                elif num[i]<num[j]: dpOfDiff[i][j] = 1
                else: 
                    if dpOfDiff[i+1][j+1]<0: dpOfDiff[i][j] = dpOfDiff[i+1][j+1]-1                    
                    elif dpOfDiff[i+1][j+1]>0: dpOfDiff[i][j] = dpOfDiff[i+1][j+1]+1
    
        def isSecondGreaterThanOrEqual(i, j, length):
            return False if dpOfDiff[i][j]<0 and length>=abs(dpOfDiff[i][j]) else True
        
        dpOfCumulativeCombinations = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n): dpOfCumulativeCombinations[i][n-1] = 1

        for prevNumberStartIndex in range(n-2, -1, -1):
            dpOfCombinations = [0 for _ in range(n)]
            dpOfCombinations[n-1] = 1
            for prevNumberEndIndex in range(n-2, prevNumberStartIndex-1, -1):
                startIndex = prevNumberEndIndex+1
                if num[startIndex]!="0": 
                    minLengthOfNextNum = prevNumberEndIndex-prevNumberStartIndex+1
                    endIndex = startIndex+minLengthOfNextNum-1
                    if endIndex<n and isSecondGreaterThanOrEqual(prevNumberStartIndex, startIndex, minLengthOfNextNum): 
                        dpOfCombinations[prevNumberEndIndex] = dpOfCumulativeCombinations[startIndex][endIndex]% (10**9+7)
                    elif endIndex+1<n:
                        dpOfCombinations[prevNumberEndIndex] = dpOfCumulativeCombinations[startIndex][endIndex+1]% (10**9+7)
            
                dpOfCumulativeCombinations[prevNumberStartIndex][prevNumberEndIndex] = dpOfCombinations[prevNumberEndIndex] + dpOfCumulativeCombinations[prevNumberStartIndex][prevNumberEndIndex+1] 
        return dpOfCumulativeCombinations[0][0]% (10**9+7)
    
