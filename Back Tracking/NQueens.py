# Key Idea - Use col and diagonal invariants to check queen position

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        allBoards, currBoard = [], [['.' for _ in range(n)] for _ in range(n)]
        cols, posDiags, negDiags = set(), set(), set()

        def backtracking(i):
            if i==n:
                allBoards.append([''.join(row) for row in currBoard])
            else:
                for j in range(n):
                    if not (j in cols or i-j in posDiags or i+j in negDiags):
                        currBoard[i][j]="Q"
                        cols.add(j)
                        posDiags.add(i-j)
                        negDiags.add(i+j)
                        backtracking(i+1)
                        currBoard[i][j]="."
                        cols.remove(j)
                        posDiags.remove(i-j)
                        negDiags.remove(i+j)
                
        backtracking(0)
        return allBoards

