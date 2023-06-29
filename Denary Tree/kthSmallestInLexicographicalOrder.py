class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def getSubtreeCount(curr):
            count = 0
            n1, n2 = curr, curr+1
            while n1<=n:
                count += min(n2, n+1) - n1
                n1 *= 10
                n2 *= 10
            return count
        
        curr = 1
        while k!=1:
            subtreeCount = getSubtreeCount(curr)
            if subtreeCount<k:
                # go right
                curr += 1
                k -= subtreeCount
            else:
                # go down
                curr *= 10
                k -= 1
        
        return curr