import heapq
class Solution:
    def minCost(self, maxTime: int, edges, passingFees):
        n = len(passingFees)
        edges.sort()
        adjList = [[] for _ in range(n)]
        seenEdges = set()
        for u,v, time in edges:
            if (u,v) in seenEdges: continue
            adjList[u].append((v, time))
            adjList[v].append((u, time))
            seenEdges.add((u, v))

        minCostMinTimeAndNodeHeap = [(passingFees[0], 0, 0)]
        minTimeWithMinCostArr = [float('inf') for _ in range(n)]

        while minCostMinTimeAndNodeHeap:
            cost, time, node = heapq.heappop(minCostMinTimeAndNodeHeap)

            if time>maxTime: continue
            if node==n-1: return cost  

            if time<minTimeWithMinCostArr[node]:
                minTimeWithMinCostArr[node] = time
                for neigh, timeToNeigh in adjList[node]:
                    if time+timeToNeigh<minTimeWithMinCostArr[neigh]:
                        heapq.heappush(minCostMinTimeAndNodeHeap, (cost+passingFees[neigh], time+timeToNeigh, neigh))

        return -1