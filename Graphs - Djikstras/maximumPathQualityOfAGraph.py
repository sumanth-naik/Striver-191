# Key Idea: Use dfs without cycle check. When at node 0, update best
# Note 1: visited is used just to compute best efficiently. 
# Note 2: This is not exactly backtracking as visited is never popped, its simple brute-force
class Solution:
    def maximalPathQuality(self, values, edges, maxTime):
        adjList = defaultdict(list)
        for u, v, t in edges:
            adjList[u].append((v, t))
            adjList[v].append((u, t))

        best = 0
        def dfs(node, visited, timeLeft):
            nonlocal best
            if node==0:
                best = max(best, sum(values[seen] for seen in visited))
            for neigh, timeToMove in adjList[node]:
                if timeLeft>=timeToMove:
                    dfs(neigh, visited | {neigh}, timeLeft-timeToMove)
        
        dfs(0, {0}, maxTime)
        return best


# Key Idea: Instead of creating new set everytime, use visitedCount and only add its val once
# This is proper backtracking wrt dfs visits
class Solution:
    def maximalPathQuality(self, values, edges, maxTime):
        adjList = defaultdict(list)
        for u, v, t in edges:
            adjList[u].append((v, t))
            adjList[v].append((u, t))

        visitedCount = [0]*len(values)
        def dfs(node, timeLeft, valTillNow, best):
            visitedCount[node] += 1
            valTillNow += values[node] if visitedCount[node]==1 else 0 #only add once
            if node==0:
                best = max(best, valTillNow)
            for neigh, timeToMove in adjList[node]:
                if timeLeft>=timeToMove:
                    best = max(best, dfs(neigh, timeLeft-timeToMove, valTillNow, best))
            visitedCount[node] -= 1 #backtracking
            return best
        return dfs(0, maxTime, 0, 0)

# Key Idea 1: Use frozen set, which is immutable, to cache
# Key Idea 2: Use djikstra's to compute distances. Only visit a node if we can reach back to 0
class Solution:
    def maximalPathQuality(self, values, edges, maxTime):
        adjList = defaultdict(list)
        for u, v, t in edges:
            adjList[u].append((v, t))
            adjList[v].append((u, t))

        minHeap, distArr = [(0, 0)], [1e9]*len(values)
        distArr[0] = 0
        while minHeap:
            distToNode, node = heappop(minHeap)
            if distArr[node]!=distToNode: continue
            for neigh, distToNeigh in adjList[node]:
                if distToNode + distToNeigh < distArr[neigh]:
                    distArr[neigh] = distToNode + distToNeigh
                    heappush(minHeap, (distArr[neigh], neigh))

        best = 0
        @lru_cache(None)
        def dfs(node, visited, timeLeft):
            nonlocal best
            if node==0:
                best = max(best, sum(values[seen] for seen in visited))
            for neigh, timeToMove in adjList[node]:
                if timeLeft>=timeToMove and timeLeft-timeToMove>=distArr[neigh]:
                    dfs(neigh, visited | {neigh}, timeLeft-timeToMove)
        
        dfs(0, frozenset([0]), maxTime)
        return best
