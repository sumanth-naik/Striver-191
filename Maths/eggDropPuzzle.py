'''

[0, 0, 0, 0, 0]
[0, 1, 1, 1, 1]
[0, 2, -, -, -]
[0, 3, -, -, -]
[0, 4, -, -, -]
[0, 5, -, -, -]




[0, 0, 0, 0, 0]
[0, 1, 1, 1, 1]
[0, 2, 2, 2, 2]
[0, 3, 2, 2, 2]
[0, 4, 3, 3, 3]
[0, 5, 3, 3, 3]

'''

n = 5
e = 4
dp = [[0 for j in range(0,e+1)] for i in range(0,n+1)]

for x in range(1,e+1):
    dp[1][x] = 1

for x in range(1,n+1):
    dp[x][1] = x

for floors in range(2,n+1):
    for eggs in range(2,e+1):
        minimumDrops = 1e9
        for currFloor in range(1,floors+1):
            temp = max(dp[currFloor - 1][eggs - 1], dp[floors - currFloor][eggs])
            minimumDrops = min(minimumDrops, temp)
        dp[floors][eggs] = 1 + minimumDrops

for x in dp:
    print(x)
    
print(dp[n][e])

from functools import cache

class Solution:
    def twoEggDrop(self, n: int) -> int:
        numDrops, i = 0, 1
        while n>0:
            n -= i
            numDrops += 1
            i+=1
        return numDrops

class Solution:
    def twoEggDrop(self, n: int) -> int:
        @cache
        def dp(num):
            if num==0: return 0
            return min([max(k, 1+dp(num-k)) for k in range(1,num)], default=1)
        return dp(n)
    


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

