# Key Idea 1: minimax style algo: need to know what is already picked, how much left to pick, game on.
# Key Idea 2: Optimise with bitmasking. Can DP.

# Note 1: If sum of numbers can't reach desired total -> Cant force win -> False
# Note 2: If desired total==0 -> Already won -> True

# Note 3: Clever check to see if a number greater than remSum exists in mask

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (maxChoosableInteger*(maxChoosableInteger+1))//2 < desiredTotal: return False # Note 1
        if desiredTotal==0: return True # Note 2
        
        @lru_cache(None)
        def bitMaskingDP(availableMask, remSum):
            if availableMask >= (1 << (remSum - 1)): return True # Note 3
            for num in range(maxChoosableInteger, 0, -1):
                if 1<<(num-1) & availableMask:
                    if not bitMaskingDP(availableMask & ~(1<<(num-1)), remSum - num):
                        return True
            return False

        return bitMaskingDP((1<<(maxChoosableInteger))-1, desiredTotal)

        
        