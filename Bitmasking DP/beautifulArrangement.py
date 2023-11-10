# Key Idea: Permutation -> Brute force -> Back tracking or Bitmasking. Overlapping subproblems -> Bitmasking DP

# Optimisation: Start from right to left as there will be less numbers that can fill higher indices

class Solution:
    def countArrangement(self, n: int) -> int:

        @lru_cache(None)
        def bitmaskingDP(bitmask, indexToSetNext):
            if indexToSetNext==0: return 1
            possibilities = 0
            for number in range(1, n+1):
                # number'th position is not set and number is div or mult of numberToSetNext
                if not (bitmask & 1<<number) and (number%indexToSetNext==0 or indexToSetNext%number==0):
                    possibilities += bitmaskingDP(bitmask | 1<<number, indexToSetNext-1)
            return possibilities

        return bitmaskingDP(0, n) # Optimisation