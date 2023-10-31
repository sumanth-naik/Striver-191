# Key Idea: Figure out the update pattern

class Solution:
    def numOfWays(self, n):
        a121, a123, mod = 6, 6, 10**9 + 7
        for _ in range(n-1):
            a121, a123 = a121 * 3 + a123 * 2, a121 * 2 + a123 * 2
        return (a121 + a123) % mod


# Key Idea: Convert the problem to Graphs 

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


import numpy    
class Solution:
    def numOfWays(self, n):
        # ans is same as [6, 6] * ([3, 2], [2, 2]]**(n-1))
        n, MOD = n-1, 10**9+7
        # adj matrix of directed graph
        M = [[3, 2], [2, 2]]
        # intital number of paths
        res = [[6, 6]]

        def modMatMult(m1, m2, MOD):
            rows1, rows2, cols2 = len(m1), len(m2), len(m2[0])
            mult = [[0 for _ in range(cols2)] for _ in range(rows1)]
            for i in range(rows1):
                for j in range(cols2):
                    for k in range(rows2):
                        mult[i][j] = (mult[i][j] + m1[i][k]*m2[k][j]) % MOD
            return mult
        
        # matrix exponentiation
        while n:
            if n&1:
                res = modMatMult(res, M, MOD)
            M = modMatMult(M, M, MOD)
            n //= 2
        return sum(map(sum, res)) % MOD