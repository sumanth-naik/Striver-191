# Key Idea: There is a graph with nodes formed by two numbers 12, 13, 14, 15 etc and we need number of paths
    
# Note: dtype = np.uint64 is needed for multiplication of numpy as 
#        MOD -> 32 bits. max(MOD * MOD) -> 64 bits => uint64  [even int64 wont work]

import numpy as np
class Solution:

    def __init__(self):
        self.adjList = defaultdict(list)
        for i in range(1, 7):
            for j in range(1, 7):
                for k in range(1, 7):
                    if gcd(i,j)==1 and i!=j and gcd(j,k)==1 and j!=k and i!=k:
                        self.adjList[(i,j)].append((j,k))
        self.nodeAt = list(sorted(self.adjList.keys()))
    
    def distinctSequences(self, n: int) -> int:
        if n==1: return 6

        M = [[self.nodeAt[j] in self.adjList[self.nodeAt[i]] for j in range(22)] for i in range(22)]
        res, MOD = [1 for _ in range(22)], 10**9 + 7

        M = np.matrix(M, dtype = np.uint64) # Note
        res = np.matrix(res, dtype = np.uint64) # Note

        n -= 2
        while n:
            if n&1:
                res = res * M % MOD
            M = M * M % MOD
            n >>= 1
        return int(np.sum(res)%MOD) # Note: float to int
