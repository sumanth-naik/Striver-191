# from functools import cache

# class Solution:
#     def twoEggDrop(self, n: int) -> int:
#         numDrops, i = 0, 1
#         while n>0:
#             n -= i
#             numDrops += 1
#             i+=1
#         return numDrops

# class Solution:
#     def twoEggDrop(self, n: int) -> int:
#         @cache
#         def dp(num):
#             if num==0: return 0
#             return min([max(k, 1+dp(num-k)) for k in range(1,num)], default=1)
#         return dp(n)
    


class Solution:
    @cache
    def superEggDrop(self, k: int, n: int) -> int:
        if n==0: return 0
        return min(1+max(self.superEggDrop(k-1, n-f), self.superEggDrop(k, f-1)) for f in range(1, n+1))
    
    
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[1e9 for _ in range(n+1)] for _ in range(k+1)]
        for i in range(k+1): dp[i][0]=0
        for numEggs in range(1, k+1):
            prevBestIntermediateFloor = 1
            for numFloors in range(1, n+1):
                for intermediateFloor in range(prevBestIntermediateFloor, numFloors+1):
                    # dp[numEggs][numFloors] = min(1+max(dp[numEggs][intermediateFloor-1], dp[numEggs-1][numFloors-intermediateFloor]) for intermediateFloor in range(1, numFloors+1))

                    # dp[numEggs][intermediateFloor-1] is independent of numFloors and is an increasing function
                    # dp[numEggs-1][numFloors-intermediateFloor] is dependant on numFloors and decreases with intermediateFloor and increases with numFloors
                    # for a constant numFloors, wrt intermediateFloor, first is increasing and second is decreasing
                    # when first crosses/intersects second, we have minima for the function max(first, second)
                    # for next numFloors, first is constant wrt intermediateFloor and second is increasing
                    # Thus max(first, second) will be increasing function with increasing numFloors
                    # and thus no need to check any previous intermediateFloor from next iteration
                    if dp[numEggs][intermediateFloor-1] >= dp[numEggs-1][numFloors-intermediateFloor]:
                        prevBestIntermediateFloor = intermediateFloor
                        dp[numEggs][numFloors] = 1+dp[numEggs][intermediateFloor-1]
                        break
        return dp[k][n]

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # solving how many floors can you reach given m moves and n eggs
        dp = [[0]*(k+1) for _ in range(n+1)]
        for moves in range(1, n+1):
            for eggs in range(1, k+1):
                # egg can break or not break
                # egg breaks -> we still have moves-1 moves and eggs-1 eggs
                # what is the best floor to drop if we know that with moves-1 moves and eggs-1 eggs we can check dp[moves-1][eggs-1] number of floors
                # it will be dp[moves-1][eggs-1]+1'th floor as we know we can surely check the bottom floor even if it breaks
                # Now, if we are at that dp[moves-1][eggs-1]+1'th floor and it breaks we are fine, given any number of floors, the threshold floor
                # will be below and we are going to find it.
                # But if the egg does not break, we need to check upper floors and we can only check dp[moves-1][eggs] number of floors
                # So, the best strategy of starting at dp[moves-1][eggs-1]+1'th floor can successfully/definetley check only dp[moves-1][eggs-1] + 1 + dp[moves-1][eggs] floors
                # difference between previous approach and this approach is, we are feeding in the best strategy here, previoulsy with min(1+max(.., ..)) we are finding the best strategy
                dp[moves][eggs] = dp[moves-1][eggs-1] + 1 + dp[moves-1][eggs]
                if dp[moves][eggs]>=n: return moves

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dpMovesMinusOne = [0]*(k+1)
        for moves in range(1, n+1):
            dpMoves = [0]*(k+1)
            for eggs in range(1, k+1):
                dpMoves[eggs] = dpMovesMinusOne[eggs-1] + 1 + dpMovesMinusOne[eggs]
                if dpMoves[eggs]>=n: return moves
            dpMovesMinusOne = dpMoves


# class Solution:
#     def superEggDrop(self, k: int, n: int) -> int:
#         dpOfMoves = [[0 for _ in range(n+1)] for _ in range(k+1)]
#         for j in range(n+1): dpOfMoves[1][j] = j

#         for numEggs in range(2, k+1):
#             for numFloors in range(1, n+1):
#                 dpOfMoves[numEggs][numFloors] = min([1+max(dpOfMoves[numEggs-1][intermediateFloor-1], dpOfMoves[numEggs][numFloors-intermediateFloor]) for intermediateFloor in range(1, numFloors+1)])
        
#         return dpOfMoves[k][n]

# TLE bottom up
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dpOfMoves = [[0 for _ in range(n+1)] for _ in range(k+1)]
        for j in range(n+1): dpOfMoves[1][j] = j

        for numEggs in range(2, k+1):
            prevBestFloor = 1
            for numFloors in range(1, n+1):
                low, high, bestFloor, bestDiff = prevBestFloor, numFloors, 1, 1e9
                while low<=high:
                    mid = (low+high)//2
                    if bestDiff>abs(dpOfMoves[numEggs-1][mid-1]-dpOfMoves[numEggs][numFloors-mid]):
                        bestDiff = abs(dpOfMoves[numEggs-1][mid-1]-dpOfMoves[numEggs][numFloors-mid])
                        bestFloor = mid
                    if dpOfMoves[numEggs-1][mid-1]<dpOfMoves[numEggs][numFloors-mid]:
                        low = mid + 1
                    else:
                        high = mid - 1
                prevBestFloor = bestFloor
                dpOfMoves[numEggs][numFloors] = 1 + max(dpOfMoves[numEggs-1][bestFloor-1], dpOfMoves[numEggs][numFloors-bestFloor])
        return dpOfMoves[k][n]
    
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        @lru_cache(None)
        def dpOfMoves(numEggs, numFloors):
            if numEggs==1: return numFloors
            if numFloors==0: return 0
            low, high, bestFloor, bestDiff = 1, numFloors, 1, 1e9
            while low<=high:
                mid = (low+high)//2
                breakCase = dpOfMoves(numEggs-1, mid-1)
                notBreakCase = dpOfMoves(numEggs, numFloors-mid)
                if bestDiff>abs(breakCase-notBreakCase):
                    bestDiff = abs(breakCase-notBreakCase)
                    bestFloor = mid
                if breakCase<notBreakCase:
                    low = mid + 1
                else:
                    high = mid - 1
            return 1 + max(dpOfMoves(numEggs-1, bestFloor-1), dpOfMoves(numEggs, numFloors-bestFloor))
        return dpOfMoves(k, n)

# Bottom up Better Binary Search + reduced search space using prevBestFloor is TLE as binary search will need more steps!
# Bottom up Better Binary Search is also TLE :(
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dpOfMoves = [[0 for _ in range(n+1)] for _ in range(k+1)]
        for j in range(n+1): dpOfMoves[1][j] = j

        for numEggs in range(2, k+1):
            prevBestFloor = 1
            for numFloors in range(1, n+1):
                low, high = prevBestFloor, numFloors
                # Idea is to keep two values as there are two cases
                # 1. There exists a intersection point (dpOfMoves[numEggs-1][mid-1]==dpOfMoves[numEggs][numFloors-mid])
                # 2. No intersection point => We need two values to see which is smaller
                while low+1<high: 
                    mid = (low+high)//2
                    if dpOfMoves[numEggs-1][mid-1]<dpOfMoves[numEggs][numFloors-mid]:
                        low = mid
                    elif dpOfMoves[numEggs-1][mid-1]>dpOfMoves[numEggs][numFloors-mid]:
                        high = mid
                    else:
                        low = high = mid
                        break
                dpOfMoves[numEggs][numFloors] = 1 + min(max(dpOfMoves[numEggs-1][mid-1], dpOfMoves[numEggs][numFloors-mid]) for mid in [low,high])
                # prevBestFloor = low 
        return dpOfMoves[k][n]
    
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        @lru_cache(None)
        def dpOfMoves(numEggs, numFloors):
            if numEggs==1: return numFloors
            if numFloors==0: return 0
            low, high = 1, numFloors
            while low+1<high:
                mid = (low+high)//2
                breakCase = dpOfMoves(numEggs-1, mid-1)
                notBreakCase = dpOfMoves(numEggs, numFloors-mid)
                if breakCase<notBreakCase:
                    low = mid
                elif breakCase>notBreakCase:
                    high = mid
                else:
                    low = high = mid
                    break
                
            return 1 + min(max(dpOfMoves(numEggs-1,mid-1), dpOfMoves(numEggs,numFloors-mid)) for mid in [low,high])
               
        return dpOfMoves(k, n)
    

# Sigma {numBrokenEggs = [1, min(k, numMoves)+1)} (numMoves choose numBrokenEggs)
# each sequence generates a unique floor as the logic is, if breaks, move up, else down which are mutually exculsive
# Binary Search on answer with PnC
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:

        def numFloors(numMoves):
            floorsCount, combinations = 0, 1
            for numBrokenEggs in range(1, min(k, numMoves)+1):
                combinations *= (numMoves-numBrokenEggs+1)
                combinations //= numBrokenEggs
                floorsCount += combinations
                if floorsCount>=n: break # early exit
            return floorsCount
        
        low, high = 1, n
        while low<high:
            mid = (low+high)//2
            if numFloors(mid)<n:
                low = mid + 1
            else:
                high = mid
        return low
        

