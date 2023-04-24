class Solution:
    def countPyramids(self, grid):
        
        def getPyramidsCount(grid):
            m, n = len(grid), len(grid[0])
            dpMatrix = [[0 for _ in range(n)] for _ in range(m)]

            for i in range(m-2, -1, -1):
                for j in range(1, n-1):
                    if grid[i][j]:
                        minInDPMatrix = min(dpMatrix[i+1][j-1], dpMatrix[i+1][j], dpMatrix[i+1][j+1])
                        if minInDPMatrix==0:
                            if min(grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1])==1:
                                dpMatrix[i][j] = 1
                        else:
                            dpMatrix[i][j] = minInDPMatrix + 1

            return sum(map(sum, dpMatrix))

        return getPyramidsCount(grid) + getPyramidsCount(grid[::-1])
        


class Solution:
    def countPyramids(self, grid):
        
        def getPyramidsCount(grid):
            m, n, numPyramids = len(grid), len(grid[0]), 0
            dpIPlusOne = [0 for _ in range(n)]

            for i in range(m-2, -1, -1):
                dpI = [0 for _ in range(n)]
                for j in range(1, n-1):
                    if grid[i][j]:
                        minInDPMatrix = min(dpIPlusOne[j-1:j+2])
                        if minInDPMatrix==0:
                            if min(grid[i+1][j-1:j+2])==1:
                                dpI[j] = 1
                        else:
                            dpI[j] = minInDPMatrix + 1
                dpIPlusOne = dpI
                numPyramids += sum(dpIPlusOne)
            return numPyramids
        return getPyramidsCount(grid) + getPyramidsCount(grid[::-1])
        
                    