class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @lru_cache(None)
        def recursion(amountLeft, lastUsableIndex):
            if amountLeft==0: return 1
            if amountLeft<0: return 0
            return sum(recursion(amountLeft-coins[index], index) for index in range(lastUsableIndex+1))
        
        return recursion(amount, len(coins)-1)