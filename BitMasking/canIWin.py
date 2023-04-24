class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (maxChoosableInteger*(maxChoosableInteger+1))//2 < desiredTotal: return False

        @lru_cache(None)
        def getMaxNum(mask):
            num = 0
            while mask:
                num += 1
                mask >>= 1
            return num

        @lru_cache(None)
        def bitMaskingDP(mask, remSum, player):
            if getMaxNum(mask)>= remSum: return player
            for num in range(1, maxChoosableInteger+1):
                if 1<<(num-1) & mask:
                    if bitMaskingDP(mask & ~(1<<(num-1)), remSum - num, not player) == player:
                        return player
            return not player

        return bitMaskingDP((1<<(maxChoosableInteger))-1, desiredTotal, True)