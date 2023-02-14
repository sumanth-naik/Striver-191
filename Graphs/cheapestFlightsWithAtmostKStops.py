from collections import deque
import heapq
from copy import deepcopy
class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int):
        adjList = [[] for i in range(n)]
        for flight in flights:
            adjList[flight[0]].append(flight[1:])

        minSoFar = None
        visited = set([(src, 0, 0)])
        q = deque()
        q.append((src, 0, 0))
        minDict = {}
        while q:
            fromFlight, stepsTaken, costSoFar = q.popleft()
            if stepsTaken==k+2:
                break
            if (minSoFar is None or minSoFar>costSoFar) and fromFlight==dst:
                minSoFar = costSoFar
            for toFlightAndCost in sorted(adjList[fromFlight], key=lambda x:x[1]):
                next = (toFlightAndCost[0], stepsTaken+1, toFlightAndCost[1]+costSoFar)
                if next not in visited:
                    if ((toFlightAndCost[0], stepsTaken+1) in minDict and minDict[(toFlightAndCost[0], stepsTaken+1)]>toFlightAndCost[1]+costSoFar) or (toFlightAndCost[0], stepsTaken+1) not in minDict:
                        visited.add(next)
                        q.append(next)
                        minDict[(toFlightAndCost[0], stepsTaken+1)] = toFlightAndCost[1]+costSoFar
            
        return -1 if minSoFar is None else minSoFar

    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int):
        #Djikstra's
        minHeap = [(0, src)]
        distArr = [float('inf') for _ in range(n)]
        distArr[src] = 0

        adjList = [[] for _ in range(n)]
        for flight in flights:
            adjList[flight[0]].append(flight[1:])

        dropSet = set()
        while minHeap:
            costSoFar, node = heapq.heappop(minHeap)
            if (costSoFar, node) in dropSet:
                continue
            for nextNode, cost in adjList[node]:
                if distArr[nextNode]> distArr[node] + cost:
                    if distArr[nextNode] != float('inf'):
                        dropSet.add((distArr[nextNode], nextNode))
                    distArr[nextNode] = distArr[node] + cost
                    heapq.heappush(minHeap, (distArr[nextNode], nextNode))


    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int):
        #Djikstra's
        # cost, k, node
        minHeap = [(0, 0, src)]
        distArr = [float('inf') for _ in range(n)]
        distArr[src] = 0

        adjList = [[] for _ in range(n)]
        for flight in flights:
            adjList[flight[0]].append(flight[1:])

        minDist = 1e9
        minDistForNodeAndStepsCombinationMap = {}
        while minHeap:
            costSoFar, stopsSoFar, node = heapq.heappop(minHeap)
            if node==dst:
                minDist = min(minDist, costSoFar)
            if stopsSoFar==k+1:
                continue
            if (node, stopsSoFar) in minDistForNodeAndStepsCombinationMap:
                if minDistForNodeAndStepsCombinationMap[(node, stopsSoFar)]!=costSoFar:
                    continue
            for nextNode, cost in adjList[node]:
                if (nextNode, stopsSoFar+1) in minDistForNodeAndStepsCombinationMap and minDistForNodeAndStepsCombinationMap[(nextNode, stopsSoFar+1)]<=costSoFar+cost:
                    continue
                distArr[nextNode] = costSoFar + cost
                heapq.heappush(minHeap, (distArr[nextNode], stopsSoFar+1, nextNode))
                if (nextNode, stopsSoFar+1) not in minDistForNodeAndStepsCombinationMap:
                    minDistForNodeAndStepsCombinationMap[(nextNode, stopsSoFar+1)] = 1e9
                minDistForNodeAndStepsCombinationMap[(nextNode, stopsSoFar+1)] = min(minDistForNodeAndStepsCombinationMap[(nextNode, stopsSoFar+1)], distArr[nextNode])
                
        return -1 if minDist is 1e9 else minDist

    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int):
        costsArr = [float('inf') for _ in range(n)]
        costsArr[src] = 0
        for _ in range(k+1):
            costsArrCopy = deepcopy(costsArr)
            for fromFlight, toFlight, flightCost in flights:
                if costsArr[fromFlight] + flightCost < costsArrCopy[toFlight]:
                    costsArrCopy[toFlight] = costsArr[fromFlight] + flightCost
            costsArr = costsArrCopy
            del costsArrCopy
        return costsArr[dst] if costsArr[dst] != float('inf') else -1

        





