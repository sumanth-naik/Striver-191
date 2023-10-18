class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        def getLen(num):
            length = 0
            while num:
                length += 1
                num >>= 1
            return length

        leftLen, rightLen = getLen(left), getLen(right)
        if leftLen!=rightLen: return 0

        ans = 0
        for index in range(leftLen-1, -1, -1):
            mask = 1<<index
            if right&mask:
                if left&mask: 
                    ans |= mask
                else:
                    break
        return ans


# // given m < n
# m := common bits + 0 + remaining bits of m
# n := common bits + 1 + remaining bits of n.
# // thus repeatedly clear last bit of n, until n <= m

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shifts = 0
        while left<right:
            left >>= 1
            right >>= 1
            shifts += 1
        return right<<shifts