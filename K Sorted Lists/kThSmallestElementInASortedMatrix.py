# Key Idea: Same as Merge K sorted lists

class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        n = len(matrix)
        minHeap = [(matrix[i][0], i, 0) for i in range(n)] # val, i, j
        heapify(minHeap)
        for _ in range(k-1):
            _, i, j = heappop(minHeap)
            if j+1<n: heappush(minHeap, (matrix[i][j+1], i, j+1))
        return minHeap[0][0]



# Key Idea 1: Similar to Search in a 2D Matrix. Use it to write getSmallerThanOrEqualNumbersCount(num)
# Key Idea 2: Use binary search on answer. 

# Note 1: Find the smaller number that satisfies the condition because mid might not even be in the matrix
# Note 2: In case of duplicates, count can never be k. Ex [10, 20, 20]; count will never be 2, its only 1 or 3

'''
[1,5,9],       [1, 5, 9]    num = 11
[10,11,13],    [10,11]
[12,13,15]     []
'''
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
            if count==k: # Note 1 
                high = mid
            elif count>k: # Note 2
                high = mid
            else:
                low = mid+1
        return low

