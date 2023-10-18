class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        emptyPlaces = [(i,j) for i in range(9) for j in range(9) if board[i][j]=="."]    
             
        def isValidMove(i, j, num):
            if any(board[i][col]==num for col in range(9)): return False #check row
            if any(board[row][j]==num for row in range(9)): return False #check col
            blockRow, blockCol = (i//3)*3, (j//3)*3 #check block of num
            if any(board[row][col]==num for row in range(blockRow, blockRow+3) for col in range(blockCol, blockCol+3)): return False
            return True

        def sudokuSolver(index):
            if index==len(emptyPlaces): return True
            i, j = emptyPlaces[index]  
            for num in range(1, 10):
                if isValidMove(i, j, str(num)):
                    board[i][j] = str(num)
                    if sudokuSolver(index + 1): return True
                    board[i][j] = "."
            return False

        sudokuSolver(0)
   