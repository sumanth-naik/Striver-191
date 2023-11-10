'''
Key Idea 1: MSB should be same
011001   <- left
...
100000   <- this will be in between => AND will be 0
...
111111   <- right


Key Idea 2:
11011-0-01
...
...       
11011-1-00

=> AND will be
11011-000

given left < right
left := common bits + 0 + remaining bits of left
right := common bits + 1 + remaining bits of right
thus repeatedly clear last bit of right and left, until right <= left
'''

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shifts = 0
        while left<right:
            left >>= 1
            right >>= 1
            shifts += 1
        return right<<shifts