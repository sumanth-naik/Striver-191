class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        queue, visited, end = deque([(1, 0)]), set([1]), n*n

        def getNextMoveBasedOnSnakeOrLadder(pos):
            row, col = (pos-1)//n, (pos-1)%n
            if row&1: col = ~col
            row = ~row
            return board[row][col] if board[row][col]!=-1 else pos

        while queue:
            pos, numMoves = queue.popleft()
            if pos==end:
                return numMoves
            for nextMove in range(pos+1, min(pos+6, end)+1):
                nextMove = getNextMoveBasedOnSnakeOrLadder(nextMove)
                if nextMove not in visited:
                    visited.add(nextMove)
                    queue.append((nextMove, numMoves+1))
        return -1

