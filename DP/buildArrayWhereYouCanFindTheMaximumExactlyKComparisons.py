class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9+7
        @lru_cache(None)
        def recursion(indexInArr, maxNumInArr, newMaximumsSeenSoFar):
            if newMaximumsSeenSoFar>k: return 0
            if indexInArr==n: return 1 if newMaximumsSeenSoFar==k else 0
            return (maxNumInArr*recursion(indexInArr+1, maxNumInArr, newMaximumsSeenSoFar) + sum(recursion(indexInArr+1, num, newMaximumsSeenSoFar+1) for num in range(maxNumInArr+1, m+1)))%MOD
        
        return recursion(0, 0, 0)
    
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9+7
        dpIPlusOneMatrix = [[0 for _ in range(k+1)] for _ in range(m+1)]
        for maxNumInArr in range(m+1):
            dpIPlusOneMatrix[maxNumInArr][k] = 1
            
        for _ in range(n-1, -1, -1):
            dpIMatrix = [[0 for _ in range(k+1)] for _ in range(m+1)]
            for maxNumInArr in range(m+1):
                for newMaximumsSeenSoFar in range(k+1):
                    dpIMatrix[maxNumInArr][newMaximumsSeenSoFar] = maxNumInArr*dpIPlusOneMatrix[maxNumInArr][newMaximumsSeenSoFar]
                    if newMaximumsSeenSoFar!=k:
                        for num in range(maxNumInArr+1, m+1):
                            dpIMatrix[maxNumInArr][newMaximumsSeenSoFar] += dpIPlusOneMatrix[num][newMaximumsSeenSoFar+1] 
                    dpIMatrix[maxNumInArr][newMaximumsSeenSoFar] = (dpIMatrix[maxNumInArr][newMaximumsSeenSoFar])%MOD
            dpIPlusOneMatrix = dpIMatrix
        return dpIPlusOneMatrix[0][0]