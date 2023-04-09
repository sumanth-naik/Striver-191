
# Djikstra's way
class Solution:
    def secondMinimum(self, n: int, edges, time: int, change: int) -> int:
        adjList = [[] for _ in range(n+1)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        minTimeSeen = None
        minHeap = [(0, 1)]
        distArr = [[] for _ in range(n+1)]
        distArr[1] = [0]
        while minHeap:
            timeTaken, node = heapq.heappop(minHeap)

            if node==n and len(distArr[node])==2: return max(distArr[node])

            for neigh in adjList[node]:
                # red signal -> wait and move to neigh if possible
                if timeTaken//change & 1:
                    newMove = (((timeTaken//change)+1)*change + time, neigh)
                else:
                    newMove = (timeTaken + time, neigh)

                if distArr[neigh]==[] or (len(distArr[neigh])==1 and distArr[neigh][0]!=newMove[0]):
                    distArr[neigh] += [newMove[0]]
                    heapq.heappush(minHeap, newMove)

from collections import deque
# BFS way
class Solution:
    def secondMinimum(self, n: int, edges, time: int, change: int) -> int:
        adjList = [[] for _ in range(n+1)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        queue = deque()
        queue.append((0, 1))
        visitedDistancesSet = defaultdict(set)
        visitedDistancesSet[1] = {0}
        while queue:
            timeTaken, node = queue.pop()
            if node==n and len(visitedDistancesSet[node])==2:
                return max(visitedDistancesSet[node])
            
            for neigh in adjList[node]:
                # red signal
                if timeTaken//change & 1:
                    newMove = (((timeTaken//change)+1)*change + time, neigh)
                else:
                    newMove = (timeTaken + time, neigh)

                if not visitedDistancesSet[neigh] or (len(visitedDistancesSet[neigh])==1 and newMove[0] not in visitedDistancesSet[neigh]):
                    visitedDistancesSet[neigh].add(newMove[0])
                    queue.appendleft(newMove)
