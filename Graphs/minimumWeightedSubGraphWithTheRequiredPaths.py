import heapq
class Solution:
    def minimumWeight(self, n: int, edges, src1: int, src2: int, dest: int) -> int:
        normalAdjList = [[] for _ in range(n)]
        reversedAdjList = [[] for _ in range(n)]

        for u, v, wt in edges:
            normalAdjList[u].append((v,wt))
            reversedAdjList[v].append((u,wt))

        def djikstras(src, adjList):
            minHeap = [(src,0)]
            distArr = [float('inf') for _ in range(n)]
            distArr[src] = 0
            while minHeap:
                node, dist = heapq.heappop(minHeap)
                if distArr[node]!=dist: continue
                for neigh, distToNeigh in adjList[node]:
                    if distArr[neigh] > distArr[node] + distToNeigh:
                        distArr[neigh] = distArr[node] + distToNeigh
                        heapq.heappush(minHeap, (neigh, distArr[neigh]))
            return distArr
        
        distArr1 = djikstras(src1, normalAdjList)
        distArr2 = djikstras(src2, normalAdjList)
        distArr3 = djikstras(dest, reversedAdjList)

        minDist = float('inf')
        for i in range(n):
            minDist = min(minDist, distArr1[i] + distArr2[i] + distArr3[i])
        return -1 if minDist==float('inf') else minDist