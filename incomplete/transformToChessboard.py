# wrong answer
import copy

board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
board = [[0,1],[0,1]]
board = [[1,1,0],[0,0,1],[0,0,1]]
board = [[1,0,0],[0,1,1],[1,0,0]]



def calcNumZeroesAndOnes(arr):
    numOnes = 0
    numZeroes = 0
    for x in arr:
        if x == 1: numOnes += 1
        else: numZeroes += 1
        
    return (numZeroes, numOnes)


def transpose(arr):
    for i in range(1, len(arr)):
        for j in range(0, i):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    return arr
 
    
def calcNumR1AndR2(matrix, r1, r2):
    numR1 = 0
    numR2 = 0
    numOther = 0
    for arr in matrix:
        if arr == r1: numR1 += 1
        elif arr == r2: numR2 += 1
        else: numOther += 1
        
    return (numR1, numR2, numOther)


# decide R
def transformToChessboard(board):
    # even case
    if(len(board)%2==0):
      
        #check for validity
        
        #check all rows have equal zeroes and ones
        for b in board:
            (numZeroes, numOnes) = calcNumZeroesAndOnes(b)
            if(numZeroes != numOnes):
                return -1
        
        #check all columns have equal zeroes and ones
        for j in range(0, len(board)):
            (numZeroes, numOnes) = calcNumZeroesAndOnes([board[i][j] for i in range(0,len(board))])
            if(numZeroes != numOnes):
                return -1            
          
        #possible R, R' or R', R
        r1 = [i%2 for i in range(0, len(board))] 
        r2 = [(i+1)%2 for i in range(0, len(board))] 
        
        
        #check all rows have equal r1 and r2 
    
        (numR1, numR2, numOther) = calcNumR1AndR2(board, board[0], [board[0][i] ^ 1 for i in range(0, len(board))])
        if(numOther!=0 or numR1!=numR2):
            return -1
        
               
        tr = transpose(copy.deepcopy(board))
        #check all columns have equal r1 and r2 
        (numR1, numR2, numOther) = calcNumR1AndR2(tr, tr[0], [tr[0][i] ^ 1 for i in range(0, len(board))])
        if(numOther!=0 or numR1!=numR2):
            return -1
        
                
        #num different in board[0] wrt r1
        numDiffR1 = 0
        for j in range(0, len(board)):
            if(board[0][j] != r1[j]):
                numDiffR1 += 1
                
        #num different in board[0] wrt r1
        for i in range(0, len(board)):
            if(board[i][0] != r1[i]):
                numDiffR1 += 1        
                
        #num different in board[0] wrt r2
        numDiffR2 = 0
        for j in range(0, len(board)):
            if(board[0][j] != r2[j]):
                numDiffR2 += 1
                
        #num different in board[0] wrt r2
        for i in range(0, len(board)):
            if(board[i][0] != r2[i]):
                numDiffR2 += 1   
                
        return min(numDiffR1//2, numDiffR2//2)
    
        
    
    # odd case
    else:
        
        #check for validity
                
        #check all rows have diff 1 for zeroes and ones
        for b in board:
            (numZeroes, numOnes) = calcNumZeroesAndOnes(b)
            if(abs(numZeroes - numOnes) != 1):
                return -1
            
        numZeroesInRowAndCol, numOnesInRowAndCol = calcNumZeroesAndOnes(board[0])
        #check all columns have diff 1 for zeroes and ones
        for j in range(0, len(board)):
            (numZeroes, numOnes) = calcNumZeroesAndOnes([board[i][j] for i in range(0,len(board))])
            if(abs(numZeroes - numOnes) != 1):
                return -1      
            
        numZeroesInRowAndCol2, numOnesInRowAndCol2 = calcNumZeroesAndOnes([board[i][0] for i in range(0,len(board))])
        numZeroesInRowAndCol += numZeroesInRowAndCol2
        numOnesInRowAndCol += numOnesInRowAndCol2    
        
        # r1 is R , r2 is R'
        r1 = []
        r2 = []
        if(numZeroesInRowAndCol>numOnesInRowAndCol):
            r1 = [i%2 for i in range(0, len(board))] 
            r2 = [(i+1)%2 for i in range(0, len(board))] 
           
        else:
            r1 = [(i+1)%2 for i in range(0, len(board))] 
            r2 = [i%2 for i in range(0, len(board))] 

        #check all rows have r1 or r2 and numr1 = numr2 +1
    
        (numR1, numR2, numOther) = calcNumR1AndR2(board, board[0], [board[0][i] ^ 1 for i in range(0, len(board))])
        if(numOther!=0 or abs(numR1 - numR2)!=1):
            return -1

      
        
        tr = transpose(copy.deepcopy(board))
        #check all columns have  r1 or r2 and numr1 = numr2 +1
        (numR1, numR2, numOther) = calcNumR1AndR2(tr, tr[0], [tr[0][i] ^ 1 for i in range(0, len(board))])
        if(numOther!=0 or abs(numR1 - numR2)!=1):
            return -1
        
        
        #num different in board[0] wrt r1
        numDiff = 0
        for j in range(0, len(board)):
            if(board[0][j] != r1[j]):
                numDiff += 1
                
        index = 0
        #num different in board[0] wrt r1
        for j in range(0, len(board)):
            if(board[0][j]==r1[0]):
                index = j
                break 
        for i in range(0, len(board)):
            if(board[i][j] != r1[i]):
                numDiff += 1        
   
        return numDiff//2
    




print(transformToChessboard(board))








    