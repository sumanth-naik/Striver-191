class Solution:
    def minimumOneBitOperations(self, n: int) -> int:

        '''
        Observation: same as
        https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/submissions/931635916/
        
        e.g. turning 1010100 to 0
        - 1010(100) -> 1010(000), we will need 2**3 - 1 operations
        - 10(10000) -> 10(00000), we will need (2**5 - 1) - (2**3 - 1) operations
        - (1000000) -> 0, we will need (2**7 - 1) - ((2**5 - 1) - (2**3 - 1)) operations
        '''


        ans, power = 0, 1
        while n:
            if n&1: ans = (pow(2, power) - 1 - ans)
            power += 1
            n >>= 1
        return abs(ans)