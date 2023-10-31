# Key Idea: Qn has a graph which screamed Matrix Exponentiation
import numpy as np
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        adjMatrix = np.matrix( [[0, 1, 0, 0, 0],
                                [1, 0, 1, 0, 0],
                                [1, 1, 0, 1, 1],
                                [0, 0, 1, 0, 1],
                                [1, 0, 0, 0, 0]])
        n -= 1
        res, MOD = [1,1,1,1,1], 10**9+7

        while n:
            if n&1: 
                res = res * adjMatrix % MOD
            n //= 2
            adjMatrix = adjMatrix * adjMatrix % MOD
        
        return np.sum(res) % MOD
    
# Without numpy

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        M = [[0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0]]
        res, MOD = [[1, 1, 1, 1, 1]], 10**9 + 7

        def modMatMult(m1, m2, MOD):
            rows1, rows2, cols2 = len(m1), len(m2), len(m2[0])
            mult = [[0 for _ in range(cols2)] for _ in range(rows1)]
            for i in range(rows1):
                for j in range(cols2):
                    for k in range(rows2):
                        mult[i][j] = (mult[i][j] + m1[i][k]*m2[k][j]) % MOD
            return mult
        
        n -= 1 
        # matrix exponentiation
        while n:
            if n&1:
                res = modMatMult(res, M, MOD)
            M = modMatMult(M, M, MOD)
            n //= 2
        return sum(res[0]) % MOD