class Solution:
    def countArrangement(self, n: int) -> int:

        @lru_cache(None)
        def bitmaskingDP(bitmask, numberToSetNext):
            if numberToSetNext==0: return 1
            possibilities = 0
            for number in range(1, n+1):
                # number'th position is not set and number is div or mult of numberToSetNext
                if not (bitmask & 1<<number) and (number%numberToSetNext==0 or numberToSetNext%number==0):
                    possibilities += bitmaskingDP(bitmask | 1<<number, numberToSetNext-1)
            return possibilities

        return bitmaskingDP(0, n)