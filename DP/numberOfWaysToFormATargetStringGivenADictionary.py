class Solution:
    def numWays(self, words, target: str) -> int:
        n, m, MOD = len(words[0]), len(target), 10**9+7
        if m>n: return 0

        counterAtVariousIndices = [Counter([word[i] for word in words]) for i in range(n)]
        
        @lru_cache(None)
        def recursion(wordIndex, targetIndex):
            if targetIndex==m: return 1
            totalNumberOfWays = 0
            for nextPossibleWordIndex in range(wordIndex, n-(m-targetIndex)+1):
                count = counterAtVariousIndices[nextPossibleWordIndex][target[targetIndex]]
                if count>0: totalNumberOfWays = (totalNumberOfWays + count*recursion(nextPossibleWordIndex+1, targetIndex+1))%MOD
            return totalNumberOfWays%MOD
            
        return recursion(0, 0)
    




class Solution:
    def numWays(self, words, target: str) -> int:
        n, m, MOD = len(words[0]), len(target), 10**9+7
        if m>n: return 0

        counterAtVariousIndices = [Counter([word[i] for word in words]) for i in range(n)]
        
        @lru_cache(None)
        def recursion(wordIndex, targetIndex):
            if targetIndex==m: return 1
            if n-wordIndex<m-targetIndex: return 0
            return (recursion(wordIndex+1, targetIndex) + counterAtVariousIndices[wordIndex][target[targetIndex]]*recursion(wordIndex+1, targetIndex+1))%MOD
            
        return recursion(0, 0)
    
class Solution:
    def numWays(self, words, target: str) -> int:
        n, m, MOD = len(words[0]), len(target), 10**9+7
        if m>n: return 0

        counterAtVariousIndices = [Counter([word[i] for word in words]) for i in range(n)]

        dpMatrix = [[0 for _ in range(m+1)] for _ in range(n+1)]  
        for i in range(n+1): dpMatrix[i][m] = 1 

        for targetIndex in range(m-1, -1, -1):
            for wordIndex in range(n-1, -1, -1):
                dpMatrix[wordIndex][targetIndex] = (dpMatrix[wordIndex+1][targetIndex] + counterAtVariousIndices[wordIndex][target[targetIndex]]*dpMatrix[wordIndex+1][targetIndex+1])%MOD

        return dpMatrix[0][0]        
    
    
class Solution:
    def numWays(self, words, target: str) -> int:
        n, m, MOD = len(words[0]), len(target), 10**9+7
        if m>n: return 0

        counterAtVariousIndices = [Counter([word[i] for word in words]) for i in range(n)]

        dpIPlusOne = [0 for _ in range(m)] + [1]
        for wordIndex in range(n-1, -1, -1):
            dpI = [1 for _ in range(m+1)]
            for targetIndex in range(m-1, -1, -1):
                dpI[targetIndex] = (dpIPlusOne[targetIndex] + counterAtVariousIndices[wordIndex][target[targetIndex]]*dpIPlusOne[targetIndex+1])%MOD
            dpIPlusOne = dpI
        return dpIPlusOne[0]        
    
