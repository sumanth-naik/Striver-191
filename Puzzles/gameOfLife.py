class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # (old -> new)
        # (0 -> 0) -> -2
        # (0 -> 1) -> -3
        # (1 -> 0) -> 2
        # (1 -> 1) -> 3
        m, n = len(board), len(board[0])

        def getUpdatedCount(i, j):
            totalLiveNeighs = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if not di==dj==0:
                        neighI, neighJ = i+di, j+dj
                        if 0<=neighI<m and 0<=neighJ<n and board[neighI][neighJ]>0:
                            totalLiveNeighs += 1
            if board[i][j]==1:
                if totalLiveNeighs<2: return 2
                if totalLiveNeighs==2 or totalLiveNeighs==3: return 3
                if totalLiveNeighs>3: return 2
            else:
                if totalLiveNeighs==3: return -3
                return -2
    
        for i in range(m):
            for j in range(n):
                board[i][j] = getUpdatedCount(i, j)
    
        for i in range(m):
            for j in range(n):
                board[i][j] %= 2

                

