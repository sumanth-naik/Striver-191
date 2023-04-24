from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        residual = 0
        for bitNum in range(32):
            count = 0
            for num in nums:
                if num & (1<<bitNum):
                    count += 1
            if count%3!=0:
                residual |= (1<<bitNum)
        return residual if residual<(1<<31) else residual - (1<<32)
    

# ref https://leetcode.com/problems/single-number-ii/solutions/43295/detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter1, counter2 = 0, 0
        for num in nums:
            counter2 ^= (counter1 & num)
            counter1 ^= num
            mask = ~(counter2 & counter1)
            counter2 &= mask
            counter1 &= mask
        singleNum = counter1 | counter2
        return singleNum if singleNum<(1<<31) else singleNum - (1<<32)
    
# simulating buffer overflow/rounding
''' 
considering int4 instead of int32,
7+1 would give -8 in C and 8 in python which we can get by 8-(1<<4)
7+2 would give -7 in C and 9 in python which we can get by 9-(1<<4) and so on
0111 <= 7
0110 <= 6
0101 <= 5
0100 <= 4
0011 <= 3
0010 <= 2
0001 <= 1
0000 <= 0
1111 <= -1
1110 <= -2
1101 <= -3
1100 <= -4
1011 <= -5
1010 <= -6
1001 <= -7
1000 <= -8
''' 