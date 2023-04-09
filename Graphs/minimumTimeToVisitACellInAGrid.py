import heapq
class Solution:
    def minimumTime(self, grid):
        if not (grid[0][1]<=1 or grid[1][0]<=1): return -1
        m, n = len(grid), len(grid[0])
        minTimeToReachMatrix = [[float('inf') for _ in range(n)] for _ in range(m)]
        minTimeToReachMatrix[0][0] = 0
        # time, i, j
        minHeap = [(0, 0, 0)]

        while minHeap:
            timeTaken, i, j = heapq.heappop(minHeap)
            if minTimeToReachMatrix[i][j]!=timeTaken: continue
            if i==m-1 and j==n-1: return timeTaken

            for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                neighI, neighJ = i+di, j+dj
                if 0<=neighI<m and 0<=neighJ<n:
                    minTimeOfNeigh = grid[neighI][neighJ]
                    if minTimeOfNeigh<=timeTaken+1:
                        timeProposedToNeigh = timeTaken + 1
                    elif ((minTimeOfNeigh&1) and (timeTaken&1)) or (not (minTimeOfNeigh&1) and not (timeTaken&1)):
                        timeProposedToNeigh = minTimeOfNeigh + 1
                    else:
                        timeProposedToNeigh = minTimeOfNeigh

                    if minTimeToReachMatrix[neighI][neighJ]>timeProposedToNeigh:
                        minTimeToReachMatrix[neighI][neighJ] = timeProposedToNeigh
                        heapq.heappush(minHeap, (minTimeToReachMatrix[neighI][neighJ], neighI, neighJ))
    
        