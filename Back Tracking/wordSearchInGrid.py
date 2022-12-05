def exist( board, word):
    charSet = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            charSet.add(board[i][j])

    for char in word:
        if char not in charSet:
             return False        
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] == word[0] and findWord(word, (i,j), 0, set(), board)):
                return True
    return False
        
        
def findWord(word, currMatrixIndex, wordIndex, visited, board):
    print(currMatrixIndex)
    i = currMatrixIndex[0]
    j = currMatrixIndex[1]
    m,n  = len(board), len(board[0])
    if(wordIndex == len(word)):
        return True
    if(i<0 or i>m-1 or j<0 or j>n-1 or board[i][j]!=word[wordIndex] or currMatrixIndex in visited):
        return False
    
    
    for neigh in [[1,0],[0,1],[0,-1],[-1,0]]:
        visited.add(currMatrixIndex)
        if(findWord(word, (i + neigh[0], j + neigh[1]), wordIndex+1, visited, board)):
            return True
        visited.remove(currMatrixIndex)
    return False

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "SEE"

board = [["A","A","A","A","A","A"],
 ["A","A","A","A","A","A"],
 ["A","A","A","A","A","A"],
 ["A","A","A","A","A","A"],
 ["A","A","A","A","A","A"],
 ["A","A","A","A","A","A"]]
word = "AAAAAAAAAAAAAAB"
print(exist(board, word))