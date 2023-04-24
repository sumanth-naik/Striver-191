class Solution:
    def numOfWays(self, n: int) -> int:

        possibleLayouts = [permutation for permutation in itertools.product([1,2,3], repeat=3) if permutation[0]!=permutation[1] and permutation[1]!=permutation[2]]
        
        @lru_cache(None)
        def getNextPossibleCombinations(prevCombo):
            return [layout for layout in possibleLayouts if all(layout[i]!=prevCombo[i] for i in [0,1,2])]
        
        @lru_cache(None)
        def recursion(rowNum, prevCombo):
            if rowNum==n: return 1
            return sum(recursion(rowNum+1, combo) for combo in getNextPossibleCombinations(prevCombo))%(10**9+7)

        return recursion(0, (0,0,0))
    
class Solution:
    def numOfWays(self, n):
        a121, a123, mod = 6, 6, 10**9 + 7
        for i in range(n - 1):
            a121, a123 = a121 * 3 + a123 * 2, a121 * 2 + a123 * 2
        return (a121 + a123) % mod
    

import numpy    
class Solution:
    def numOfWays(self, n):
        # ans is same as [6, 6] * ([3, 2], [2, 2]]**(n-1))
        n, MOD = n-1, 10**9+7
        # adj matrix of directed graph
        M = numpy.matrix([[3, 2], [2, 2]])
        # intital number of paths
        res = [6, 6]
        # matrix exponentiation
        while n:
            if n&1:
                res = res * M % MOD
            M = M * M % MOD
            n //= 2
        return (numpy.sum(res)) % MOD