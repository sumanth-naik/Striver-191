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


                