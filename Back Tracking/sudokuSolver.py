board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]


def pprint(board):
    for x in board:
        print(x)   

def isValidMove(board, i, j, num):
    #check row
    for colIndex in range(0, 9):
        if(board[i][colIndex] == num):
            return False
    #check col
    for rowIndex in range(0, 9):
        if(board[rowIndex][j] == num):
            return False          
    
    #check box of nine
    boxStartRowIndex, boxStartColIndex = i//3, j //3
    boxStartRowIndex *= 3
    boxStartColIndex *= 3

    for rowIndex in [boxStartRowIndex, boxStartRowIndex+1, boxStartRowIndex + 2]:
        for colIndex in [boxStartColIndex, boxStartColIndex+1, boxStartColIndex + 2]:
            if(board[rowIndex][colIndex]==num):
                return False

    return True

def sudokuSolver(board, emptyPlaces, index):
    if index==len(emptyPlaces):
        return True
    
    i,j = emptyPlaces[index]  
    for num in range(1, 10):
        if isValidMove(board, i, j, str(num)):
            board[i][j] = str(num)
            if(sudokuSolver(board, emptyPlaces, index + 1)):
                return True
            board[i][j] = "."
            
        
    return False
    
    
  
emptyPlaces = []    
for i in range(0, 9):
    for j in range(0, 9):
        if board[i][j] == ".":
            emptyPlaces.append((i,j))
            
print(sudokuSolver(board, emptyPlaces, 0))
 
pprint(board)