import heapq
class Solution:
    def reachableNodes(self, edges, maxMoves: int, n: int) -> int:

        adjList, edgeToDistMap = [[] for _ in range(n)], {}
        for u, v, count in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            edgeToDistMap[(u,v)] = count + 1
            edgeToDistMap[(v,u)] = count + 1

        # Djikstra's
        distArr = [1e9 for _ in range(n)]
        distArr[0] = 0
        # dist, node
        minHeap = [(0, 0)]
        while minHeap:
            dist, node = heapq.heappop(minHeap)
            if dist>distArr[node]: continue
            for neigh in adjList[node]:
                if distArr[neigh]>distArr[node] + edgeToDistMap[(node, neigh)]:
                    distArr[neigh] = distArr[node] + edgeToDistMap[(node, neigh)]
                    heapq.heappush(minHeap, (distArr[neigh], neigh))

        numOriginalNodesThatAreReachable = 0
        for dist in distArr:
            if dist<=maxMoves:
                numOriginalNodesThatAreReachable += 1

        numNewNodesThatAreReachable = 0
        for u, v, count in edges:
            numNewNodesThatAreReachable += min(count, max(0, maxMoves - distArr[u]) + max(0, maxMoves - distArr[v]))

        return numOriginalNodesThatAreReachable + numNewNodesThatAreReachable