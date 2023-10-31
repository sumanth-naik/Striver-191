# Key Idea: Convert the problem to Graphs

import numpy as np
class Solution:
    def knightDialer(self, n: int) -> int:
        adjList = [[4,6], [6,8], [7,9], [4,8], [3,9,0], [], [1,7,0], [2,6], [1,3], [2,4]]
        adjMatrix = np.matrix([[1 if neigh in adjList[row] else 0 for neigh in range(10)] for row in range(10)])
        # res stores initial position
        # n stores number of moves/jumps
        n, res, MOD = n-1, [1 for _ in range(10)], 10**9+7
        while n:
            if n&1: 
                res = res * adjMatrix % MOD
            adjMatrix = adjMatrix * adjMatrix % MOD
            n //= 2
        return np.sum(res)%MOD

