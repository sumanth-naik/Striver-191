class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m*n-1
        while low<=high:
            mid = (low+high)//2
            i, j = mid//n, mid%n
            if matrix[i][j]==target: return True
            elif matrix[i][j]>target: high = mid-1
            else: low = mid+1
        return False