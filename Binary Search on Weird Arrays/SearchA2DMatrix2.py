# Key Idea 1: Start from bottom left as it is kind of mid (top left and bottom right are like low and high)
# Key Idea 2: target>num[i][j] => eliminate col
#             target<num[i][j] => eliminate row

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = m-1, 0
        while i>=0 and j<n:
            if matrix[i][j]==target: return True
            if target>matrix[i][j]: j += 1
            else: i -= 1
        return False