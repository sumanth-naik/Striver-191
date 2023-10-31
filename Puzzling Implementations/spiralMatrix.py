# Key Idea: mark visited as *
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        arr, m, n = [], len(matrix), len(matrix[0])
        i, j, di, dj = 0, 0, 0, 1
        while len(arr)<(m*n):
            arr.append(matrix[i][j])
            matrix[i][j]="*"
            newI, newJ = i + di, j + dj
            if not (0<=newI<m and 0<=newJ<n) or matrix[newI][newJ]!="*":
                di, dj = dj, -di
            i, j = i + di, j + dj
        return arr


# Key Idea: use packing, unpacking with zip
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # unpacking and packing for matrix.pop(0) is needed for converting tuple(zip gave tuples) to list. Its same as list(matrix.pop(0))
        # *matrix unpacks rows, zip combines column wise.
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
        # return matrix and list(matrix.pop(0)) + self.spiralOrder(list(zip(*matrix))[::-1])  <- same as above


# Key Idea: Think of onion peels. Figure out number of steps in each direction and starting i,j for each peel
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n, arr = len(matrix), len(matrix[0]), []
        for onionPeel in range((min(m,n)+1)//2): 
            i, j, di, dj = onionPeel, onionPeel, 0, 1
            right, down = n-2*i, m-2*i-1
            left, up =  (right-1, down-1) if right-1 and down else (0, 0) # matrix is a col or row case
            for steps in range(1, right+down+left+up+1):
                arr.append(matrix[i][j])
                if steps in [right, right+down, right+down+left]: 
                    di, dj = dj, -di
                i, j = i+di, j+dj
        return arr


# Key Idea: Think of snake motion. Update rows, cols, direction after traversing side.
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols, arr = len(matrix), len(matrix[0]), []
        i, j, direction = 0, -1, 1 # Note that j = -1, which is incremented first, then used
        while rows*cols>0:
            for _ in range(cols):
                j += direction
                arr.append(matrix[i][j])
            rows -= 1
            for _ in range(rows):
                i += direction
                arr.append(matrix[i][j])
            cols -= 1
            direction *= -1
        return arr