# Key Idea: Identify that multiplications form K sorted Lists

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        def countSmallerOrEqualTo(num):
            j, count = n, 0
            for i in range(1, m+1):
                while i*j>num: j -= 1
                count += j
            return count
        
        low, high = 1, m*n
        while low<high:
            mid = (low+high)//2
            count = countSmallerOrEqualTo(mid)
            if count==k: # mid may not be a valid value
                high = mid
            elif count>k: # count may never be k due to duplicates
                high = mid
            else:
                low = mid+1
        return low