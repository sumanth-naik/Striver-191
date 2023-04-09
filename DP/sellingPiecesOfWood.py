class Solution:
    def sellingWood(self, m: int, n: int, prices):
        @lru_cache(None)
        def memoization(numRows, numCols):
            if numRows==0 or numCols==0: return 0
            maxProfit = 0
            for heightOfWood, widthOfWood, profitOfWood in prices:
                if heightOfWood<=numRows and widthOfWood<=numCols:
                    maxProfit = max(maxProfit, profitOfWood + max(memoization(heightOfWood, numCols-widthOfWood) + memoization(numRows-heightOfWood, numCols), 
                                                                  memoization(numRows-heightOfWood, widthOfWood) + memoization(numRows, numCols-widthOfWood)))            
            return maxProfit
        return memoization(m,n)
    

# sort prices and early exit
# DP idea: for each price, break the wood and call DP
class Solution:
    def sellingWood(self, m: int, n: int, prices):
        pricesSortedOnRows = sorted(prices)
        pricesSortedOnCols = sorted(prices, key=lambda x:x[1])
        @lru_cache(None)
        def memoization(numRows, numCols):
            if numRows==0 or numCols==0: return 0

            maxProfit = 0

            for heightOfWood, widthOfWood, profitOfWood in pricesSortedOnRows:
                if heightOfWood<=numRows and widthOfWood<=numCols:
                    maxProfit = max(maxProfit, profitOfWood + max(memoization(heightOfWood, numCols-widthOfWood) + memoization(numRows-heightOfWood, numCols), 
                                                                  memoization(numRows-heightOfWood, widthOfWood) + memoization(numRows, numCols-widthOfWood)))            
                if heightOfWood>numRows: break

                
            for heightOfWood, widthOfWood, profitOfWood in pricesSortedOnCols:
                if heightOfWood<=numRows and widthOfWood<=numCols:
                    maxProfit = max(maxProfit, profitOfWood + max(memoization(heightOfWood, numCols-widthOfWood) + memoization(numRows-heightOfWood, numCols), 
                                                                  memoization(numRows-heightOfWood, widthOfWood) + memoization(numRows, numCols-widthOfWood)))            
                if widthOfWood>numCols: break

            return maxProfit
        return memoization(m,n)
    


# DP idea: regardless of prices, just cut and see
# just cut till half height as we are calling for example (1,x) + (4,x), (2,x) + (3,x) then we dont need to call (3,x) + (2,x) and so on
# if current cut has a price, you could return it (or see if there is any better cuts possible)
class Solution:
    def sellingWood(self, m: int, n: int, prices):
        pricesMap = {(heightOfWood, widthOfWood):profitOfWood for heightOfWood, widthOfWood, profitOfWood in prices}

        @lru_cache(None)
        def memoization(numRows, numCols):
            if numRows==0 or numCols==0: return 0

            maxProfit = pricesMap[(numRows, numCols)] if (numRows, numCols) in pricesMap else 0

            for heightOfCut in range(1, numRows//2 + 1):
                maxProfit = max(maxProfit, memoization(heightOfCut, numCols) + memoization(numRows - heightOfCut, numCols))
            for widthOfCut in range(1, numCols//2 + 1):
                maxProfit = max(maxProfit, memoization(numRows, numCols-widthOfCut) + memoization(numRows, widthOfCut))
            
            return maxProfit
        return memoization(m,n)
    
class Solution:
    def sellingWood(self, m: int, n: int, prices):
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for heightOfWood, widthOfWood, profitOfWood in prices:
            dp[heightOfWood][widthOfWood] = profitOfWood

        for numRows in range(1, m+1):
            for numCols in range(1, n+1):
                for heightOfCut in range(1, numRows//2 + 1):
                    dp[numRows][numCols] = max(dp[numRows][numCols], dp[heightOfCut][numCols] + dp[numRows - heightOfCut][numCols])
                for widthOfCut in range(1, numCols//2 + 1):
                    dp[numRows][numCols] = max(dp[numRows][numCols], dp[numRows][numCols-widthOfCut] + dp[numRows][widthOfCut])
        return dp[m][n]