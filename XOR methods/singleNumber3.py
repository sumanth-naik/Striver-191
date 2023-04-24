from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        num1XorNum2 = 0
        for num in nums: 
            num1XorNum2 ^= num
        
        numberWithRightMostDifferingBitSet = (~num1XorNum2+1)&num1XorNum2

        set1Xor, set2Xor = 0, 0
        for num in nums:
            if numberWithRightMostDifferingBitSet&num:
                set1Xor ^= num
            else:
                set2Xor ^= num

        return [set1Xor, set2Xor]
