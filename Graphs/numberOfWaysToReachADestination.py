
import heapq
class Solution:
    def countPaths(self, n: int, roads):
        adjList = [[] for _ in range(n)]
        for road in roads:
            adjList[road[0]].append((road[1], road[2]))
            adjList[road[1]].append((road[0], road[2]))

        distanceArr = [1e15 for _ in range(n)]
        distanceArr[0] = 0

        # (dist, node)
        minHeap = [(0,0)]
        nodeToMinDistFoundMap = {}
        nodeToMinDistFoundMap[0] = 0

        nodeToNumberOfShortestPathsModuloedMap = {}
        nodeToNumberOfShortestPathsModuloedMap[0] = 1

        while minHeap:
            distanceSoFar, node = heapq.heappop(minHeap)
            if distanceSoFar!=nodeToMinDistFoundMap[node]:
                continue
            for neigh, costFromNodeToGoToNeigh in adjList[node]:
                if distanceArr[neigh] > distanceArr[node] + costFromNodeToGoToNeigh:
                    nodeToNumberOfShortestPathsModuloedMap[neigh] = nodeToNumberOfShortestPathsModuloedMap[node]
                    distanceArr[neigh] = distanceArr[node] + costFromNodeToGoToNeigh
                    nodeToMinDistFoundMap[neigh] = distanceArr[neigh]
                    heapq.heappush(minHeap, (distanceArr[neigh], neigh))
                elif distanceArr[neigh] == distanceArr[node] + costFromNodeToGoToNeigh:
                    nodeToNumberOfShortestPathsModuloedMap[neigh] = (nodeToNumberOfShortestPathsModuloedMap[neigh] + nodeToNumberOfShortestPathsModuloedMap[node])%(10**9+7)

        return nodeToNumberOfShortestPathsModuloedMap[n-1]


        # Floyd Warshall
        # adjMatrix = [[1e15 for _ in range(n)] for _ in range(n)]
        
        # for i in range(n):
        #      for j in range(n):
        #         if i==j:
        #             adjMatrix[i][j] = 0

        # for road in roads:
        #     adjMatrix[road[0]][road[1]] = road[2]
        #     adjMatrix[road[1]][road[0]] = road[2]

        # for middle in range(n):
        #     for i in range(n):
        #         for j in range(n):
        #             if i!=j and i!=middle and j!=middle:
        #                 adjMatrix[i][j] = min(adjMatrix[i][j], adjMatrix[i][middle] + adjMatrix[middle][j])
        

class Solution:
    def countPaths(self, n: int, roads):
        adjMatrix = [[(1e15,0) for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
             for j in range(n):
                if i==j:
                    adjMatrix[i][j] = (0,1)

        for road in roads:
            adjMatrix[road[0]][road[1]] = (road[2],1)
            adjMatrix[road[1]][road[0]] = (road[2],1)

        for middle in range(n):
            for i in range(n):
                for j in range(n):
                    if i!=j and i!=middle and j!=middle:
                        if adjMatrix[i][middle][0] + adjMatrix[middle][j][0] < adjMatrix[i][j][0]:
                            adjMatrix[i][j] = (adjMatrix[i][middle][0] + adjMatrix[middle][j][0], (adjMatrix[i][middle][1] * adjMatrix[middle][j][1])%(10**9+7))
                        elif adjMatrix[i][middle][0] + adjMatrix[middle][j][0] == adjMatrix[i][j][0]:
                            adjMatrix[i][j] = (adjMatrix[i][j][0], (adjMatrix[i][j][1] + adjMatrix[i][middle][1] * adjMatrix[middle][j][1])%(10**9+7))
        
        return adjMatrix[0][n-1][1]
