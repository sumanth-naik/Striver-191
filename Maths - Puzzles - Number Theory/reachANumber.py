# Key Idea 1: The crux of the problem is to put + and - signs on the numbers {1, 2, 3, ..., $moves} so that the sum is target
# Key Idea 2: If total(of nums till moves) is even, we can find delta/2 in {1,2,..moves} [delta = total-target]
# Key Idea 3: If odd, we cant. Add one/two more moves, based on moves' parity. Then we can.
#           delta = 1, moves = 3 => next num = 4... adding to delta is still odd
#                                => add 2 nums if moves is odd
#           delta = 1, moves = 6 => next num = 7... adding to delta is even
#                                => add 1 num if moves is even 

class Solution:
    def reachNumber(self, target: int) -> int:
        moves = ceil((sqrt(1 + 8*abs(target)) - 1)/2)
        total = (int)((moves * (moves+1))//2)
        return moves + 1 + (moves&1) if (total-abs(target))&1 else moves