# Key Idea 1: Pick or not pick this coin. Don't try to figure out how many to pick, let dp do its thing.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = list(set(coins))
        coins.sort(reverse=True)
        n = len(coins)

        @lru_cache(None)
        def dp(index, amountLeft):
            if amountLeft==0: return 0
            if index==n: return 1e9 
            if amountLeft<coins[index]: return dp(index+1, amountLeft)
            return min(dp(index+1, amountLeft), 1 + dp(index, amountLeft-coins[index]))

        count = dp(0, amount)
        return count if count!=1e9 else -1 




# Key Idea 2: Push indexing into the dp as a loop
    
# Note 1: Dont use 1e9, as count can be 1e9+numCoinsPicked. Use float("inf").

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = list(set(coins))
        coins.sort(reverse=True)

        @cache
        def dp(amountLeft):
            if amountLeft==0: return 0
            if amountLeft<0: return float("inf") # Note 1
            return min(1 + dp(amountLeft-coinVal) for coinVal in coins)

        count = dp(amount)
        return count if count!=float("inf") else -1 