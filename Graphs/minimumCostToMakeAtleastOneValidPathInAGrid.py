# Bellman Fords
class Solution:
    def minCost(self, grid):
        numRows, numColumns = len(grid), len(grid[0])
        costsMatrix = [[1e10 for _ in range(numColumns)] for _ in range(numRows)]
        costsMatrix[numRows-1][numColumns-1] = 0
        changedInPreviousIteration = True
        for _ in range(numRows*numColumns):
            if changedInPreviousIteration:
                changedInPreviousIteration = False
                for i in range(numRows):
                    for j in range(numColumns):
                        for dx, dy, direction in [(0,1,1),(0,-1,2),(1,0,3),(-1,0,4)]:
                            prev = costsMatrix[i][j]
                            if 0<=i+dx<numRows and 0<=j+dy<numColumns:
                                costsMatrix[i][j] = min(costsMatrix[i][j], costsMatrix[i+dx][j+dy]+min(1,abs(direction-grid[i][j])))
                            if prev!=costsMatrix[i][j]:
                                changedInPreviousIteration = True
        return costsMatrix[0][0]
    

# Djisktra's
import heapq
class Solution:
    def minCost(self, grid):
        numRows, numColumns = len(grid), len(grid[0])
        distMatrix = [[1e10 for _ in range(numColumns)] for _ in range(numRows)]
        distMatrix[0][0] = 0

        # (i,j, dist)
        minHeap = [(0,0,0)]

        matrixIndexToMinDistFoundMap = {}
        matrixIndexToMinDistFoundMap[(0,0)] = 0

        while minHeap:
            i, j, dist = heapq.heappop(minHeap)
            if (i,j) in matrixIndexToMinDistFoundMap and matrixIndexToMinDistFoundMap[(i,j)] > dist:
                continue

            for dx, dy, direction in [(0,1,1),(0,-1,2),(1,0,3),(-1,0,4)]:
                if 0<=i+dx<numRows and 0<=j+dy<numColumns:
                    if distMatrix[i+dx][j+dy] > distMatrix[i][j] + min(1, abs(direction-grid[i][j])):
                        distMatrix[i+dx][j+dy] = distMatrix[i][j] + min(1, abs(direction-grid[i][j]))
                        heapq.heappush(minHeap, (i+dx, j+dy, distMatrix[i+dx][j+dy]))
                        matrixIndexToMinDistFoundMap[(i+dx, j+dy)] = distMatrix[i+dx][j+dy]

        return distMatrix[numRows-1][numColumns-1]



# 0-1 BFS with map
from collections import deque
class Solution:
    def minCost(self, grid):
        numRows, numColumns = len(grid), len(grid[0])
        queue = deque()
        queue.append((0,0,0))
        
        matrixIndexToMinDistFoundMap = {}
        matrixIndexToMinDistFoundMap[(0,0)] = 0

        while queue:
            i, j, dist = queue.popleft()
            if (i,j) in matrixIndexToMinDistFoundMap and matrixIndexToMinDistFoundMap[(i,j)] < dist:
                continue
            
            for dx, dy, direction in [(0,1,1),(0,-1,2),(1,0,3),(-1,0,4)]:
                if 0<=i+dx<numRows and 0<=j+dy<numColumns:
                    if ((i+dx, j+dy) not in matrixIndexToMinDistFoundMap) or ((i+dx, j+dy) in matrixIndexToMinDistFoundMap and matrixIndexToMinDistFoundMap[(i+dx, j+dy)]>dist + min(1, abs(direction-grid[i][j]))):
                        if direction == grid[i][j]:
                            queue.appendleft((i+dx, j+dy, dist))
                            matrixIndexToMinDistFoundMap[(i+dx, j+dy)] = dist
                        else:
                            queue.append((i+dx, j+dy, dist+1))
                            matrixIndexToMinDistFoundMap[(i+dx, j+dy)] = dist + 1
        return matrixIndexToMinDistFoundMap[(numRows-1, numColumns-1)]
    


    
# 0-1 BFS with matrix
from collections import deque
class Solution:
    def minCost(self, grid):
        numRows, numColumns = len(grid), len(grid[0])
        queue = deque()
        queue.append((0,0,0))
        
        distMatrix = [[1e10 for _ in range(numColumns)] for _ in range(numRows)]
        distMatrix[0][0] = 0

        while queue:
            i, j, dist = queue.popleft()
            if distMatrix[i][j] < dist:
                continue
            
            for dx, dy, direction in [(0,1,1),(0,-1,2),(1,0,3),(-1,0,4)]:
                if 0<=i+dx<numRows and 0<=j+dy<numColumns:
                    if distMatrix[i+dx][j+dy] > dist + min(1, abs(direction-grid[i][j])):
                        if direction == grid[i][j]:
                            queue.appendleft((i+dx, j+dy, dist))
                            distMatrix[i+dx][j+dy] = dist
                        else:
                            queue.append((i+dx, j+dy, dist+1))
                            distMatrix[i+dx][j+dy] = dist + 1

        return distMatrix[numRows-1][numColumns-1]