# WA
# class Solution:
#     def cherryPickup(self, grid) -> int:
#         m, n = len(grid), len(grid[0])

#         @lru_cache(None)
#         def memoization(i, j):
#             isLastReachable = False
#             cherriesUsedSet = set()
#             if grid[i][j]==1: 
#                 cherriesUsedSet.add((i,j))
#             if i==m-1 and j==n-1: 
#                 isLastReachable = True
#             else:
#                 maxInNextStep, cherriesUsedInNextStep = 0, set()
#                 for di in [0,1]:
#                     newI, newJ = i+di, j+(1-di)
#                     if (0<=newI<m) and (0<=newJ<n):
#                         if grid[newI][newJ]!=-1:
#                             nextStepCherriesCollected, nextStepCherriesUsed, isLastReachableFromNextStep =  memoization(newI, newJ)
#                             if (not isLastReachable and isLastReachableFromNextStep) or (isLastReachableFromNextStep and nextStepCherriesCollected>maxInNextStep):
#                                 maxInNextStep, cherriesUsedInNextStep = nextStepCherriesCollected, nextStepCherriesUsed
#                                 isLastReachable = True
#                 cherriesUsedSet.update(cherriesUsedInNextStep)
#             return (len(cherriesUsedSet), cherriesUsedSet, isLastReachable)

#         _, cherriesUsedSet, isLastReachable = memoization(0,0)        
#         if not isLastReachable: return 0

#         for i, j in cherriesUsedSet:
#             grid[i][j] = 0

#         @lru_cache(None)
#         def memoization2(i, j):
#             isFirstReachable = False
#             numCherries = grid[i][j]
#             maxInNextStep = 0
#             if i==0 and j==0: 
#                 isFirstReachable = True
#             else:
#                 for di in [0,-1]:
#                     newI, newJ = i+di, j-(1+di)
#                     if (0<=newI<m) and (0<=newJ<n):
#                         if grid[newI][newJ]!=-1:
#                             nextStepCherriesUsed, isFirstReachableFromNextStep = memoization2(newI, newJ)
#                             if (not isFirstReachable and isFirstReachableFromNextStep) or (isFirstReachableFromNextStep and nextStepCherriesUsed>maxInNextStep):
#                                 isFirstReachable = True
#                                 maxInNextStep = nextStepCherriesUsed

#             return (numCherries + maxInNextStep, isFirstReachable)      

#         return memoization2(m-1,n-1)[0] + len(cherriesUsedSet)
        





class Solution:
    def cherryPickup(self, grid) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def memoization(i1, j1, i2):
            j2 = i1+j1-i2
            isLastReachable, maxInNextStep = False, 0
            numCherries = grid[i1][j1] + grid[i2][j2] if not(i1==i2 and j1==j2) else grid[i1][j1]
            if i1+j1==m-1+n-1:
                isLastReachable = True
            else:
                for di1 in [0,1]:
                    for di2 in [0,1]:
                        newI1, newJ1, newI2, newJ2 = i1+di1, j1+(1-di1), i2+di2, j2+(1-di2)
                        if (0<=newI1<m) and (0<=newI2<m) and (0<=newJ1<n) and (0<=newJ2<n):
                            if grid[newI1][newJ1]!=-1 and grid[newI2][newJ2]!=-1:
                                nextStepCherriesCollected, isLastReachableFromNextStep =  memoization(newI1, newJ1, newI2)
                                if (not isLastReachable and isLastReachableFromNextStep) or (isLastReachableFromNextStep and nextStepCherriesCollected>maxInNextStep):
                                    maxInNextStep = nextStepCherriesCollected
                                    isLastReachable = True

            return (numCherries+maxInNextStep, isLastReachable) if isLastReachable else (0, False)
        
        return memoization(0,0,0)[0]
    

class Solution:
    def cherryPickup(self, grid) -> int:
        n = len(grid)
        dpArrI2PlusOne = [[0]*(n+1) for _ in range(n+1)]
        for i2 in range(n-1, -1, -1):
            dpArrI2 = [[0]*(n+1) for _ in range(n+1)]
            for i1 in range(n-1, -1, -1):
                for j1 in range(n-1, -1, -1):
                    j2 = i1+j1-i2
                    if not 0<=j2<n: continue
                    if grid[i1][j1]==-1 or grid[i2][j2]==-1: continue
                    maxInNextStep = -1e9
                    numCherries = grid[i1][j1] + grid[i2][j2] if not(i1==i2 and j1==j2) else grid[i1][j1]
                    if i1==j1==n-1:
                        maxInNextStep = 0
                    else:
                        for di1 in [0,1]:
                            for di2 in [0,1]:
                                newI1, newJ1, newI2, newJ2 = i1+di1, j1+(1-di1), i2+di2, j2+(1-di2)
                                if (0<=newI1<n) and (0<=newI2<n) and (0<=newJ1<n) and (0<=newJ2<n):
                                    if grid[newI1][newJ1]!=-1 and grid[newI2][newJ2]!=-1:
                                        if di2==1: 
                                            nextStepCherriesCollected = dpArrI2PlusOne[newI1][newJ1]
                                        else:
                                            nextStepCherriesCollected = dpArrI2[newI1][newJ1]
                                        maxInNextStep = max(maxInNextStep, nextStepCherriesCollected)

                    dpArrI2[i1][j1] = numCherries+maxInNextStep
            dpArrI2PlusOne = dpArrI2
        return max(0, dpArrI2PlusOne[0][0])
    


class Solution:
    def cherryPickup(self, grid) -> int:
        n = len(grid)
        dpArrI2PlusOne = [[-1e9]*(n+1) for _ in range(n+1)]
        for i2 in range(n-1, -1, -1):
            dpArrI2 = [[-1e9]*(n+1) for _ in range(n+1)]
            for i1 in range(n-1, -1, -1):
                for j1 in range(n-1, -1, -1):
                    j2 = i1+j1-i2
                    if (0<=j2<n) and grid[i1][j1]!=-1 and grid[i2][j2]!=-1:
                        dpArrI2[i1][j1] = grid[i1][j1] + grid[i2][j2] if not(i1==i2 and j1==j2) else grid[i1][j1]
                        maxInNextStep = -1e9
                        if i1==j1==n-1:
                            maxInNextStep = 0
                        else:
                            for di1 in [0,1]:
                                newI1, newJ1 = i1+di1, j1+(1-di1)
                                maxInNextStep = max(maxInNextStep, dpArrI2PlusOne[newI1][newJ1], dpArrI2[newI1][newJ1])
                        dpArrI2[i1][j1] += maxInNextStep
            dpArrI2PlusOne = dpArrI2
        return max(0, dpArrI2PlusOne[0][0])