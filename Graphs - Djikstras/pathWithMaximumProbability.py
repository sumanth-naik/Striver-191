import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        adjList = defaultdict(list)
        for (u,v), edgeProb in zip(edges, succProb):
            adjList[u].append((v, edgeProb))
            adjList[v].append((u, edgeProb))

        minHeap, probArr = [(-1, start)], [0 for _ in range(n)]
        probArr[start] = 1

        while minHeap:
            probTillNode, node = heapq.heappop(minHeap)

            if node==end: return -probTillNode
            
            if -probTillNode!=probArr[node]: continue

            for neigh, edgeProb in adjList[node]:
                if probArr[neigh]<-probTillNode*edgeProb:
                    heapq.heappush(minHeap, (probTillNode*edgeProb, neigh))
                    probArr[neigh] = -probTillNode*edgeProb
   
        return 0