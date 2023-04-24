class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        
        def getSmallerThanOrEqualNumbersCount(num):
            count, j = 0, n-1
            for i in range(m):
                while j>=0 and matrix[i][j]>num: j-=1
                count += (j+1)
            return count
    
        low, high = matrix[0][0], matrix[-1][-1]
        while low<high:
            mid = (low+high)//2
            count = getSmallerThanOrEqualNumbersCount(mid)
            # because mid might not even be in the matrix, we need to find the 
            # smallest number with count=k to ensure that its in matrix
            if count==k:
                high = mid
            # because if there are duplicates, and the ans is one of those, count will never equal k
            elif count>k:
                high = mid
            else:
                low = mid+1
        return low