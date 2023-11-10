'''
Similar to Coin change but each coin pick at index i will be same in Coin Change problem. -> non-distinct picks
Here, if we picked the top of a pile, next pick has to be the one below it -> distinct picks
To distinguish those picks we needed to either (1) have a for loop or (2) have indexInCurrPile in dp state
'''

# Key Idea 1: Pick 1 or 2 or .. k from this pile(loop approach), rest from other.
# Key Idea 2: Use Prefix Sum to optimise

# Note: indexing is tricky. 0<=numCoinsTakenFromThisPile<length of that pile and 
#                              numCoinsTakenFromThisPile<=numCoinsTaken
class Solution:
    def maxValueOfCoins(self, piles, k: int) -> int:

        cumulativeSums = []
        for pile in piles:
            cumulativeSumArr = [0]
            for num in pile: cumulativeSumArr.append(cumulativeSumArr[-1]+num)
            cumulativeSums.append(cumulativeSumArr)

        @lru_cache(None)
        def recursion(pileNum, numCoinsTaken):
            if numCoinsTaken==0 or pileNum==-1: return 0
            return max(cumulativeSums[pileNum][numCoinsTakenFromThisPile] + recursion(pileNum-1, numCoinsTaken-numCoinsTakenFromThisPile)\
                        for numCoinsTakenFromThisPile in range(min(len(piles[pileNum]), numCoinsTaken)+1))

        return recursion(len(piles)-1, k)
    

class Solution:
    def maxValueOfCoins(self, piles, k: int) -> int:

        cumulativeSums = []
        for pile in piles:
            cumulativeSumArr = [0]
            for num in pile: cumulativeSumArr.append(cumulativeSumArr[-1]+num)
            cumulativeSums.append(cumulativeSumArr)

        dpIMinusOne = [0]*(k+1)

        for pileNumber in range(len(piles)):
            dpI = [0]*(k+1)
            for numCoinsToTake in range(1, k+1):
                for numCoinsToTakeFromCurrentPile in range(len(piles[pileNumber])+1):
                    if numCoinsToTake-numCoinsToTakeFromCurrentPile>=0:
                        dpI[numCoinsToTake] = max(dpI[numCoinsToTake], cumulativeSums[pileNumber][numCoinsToTakeFromCurrentPile]+dpIMinusOne[numCoinsToTake-numCoinsToTakeFromCurrentPile])
                    else: break
            dpIMinusOne = dpI
        return dpIMinusOne[-1]    