
import heapq
class Solution:
    def findMinHeightTrees(self, n: int, edges):
        adjList = [[] for _ in range(n)]
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        visited, maxLengthPath = set(), []
        def dfs(node):
            nonlocal maxLengthPath
            visited.add(node)
            minHeap = []
            for neigh in adjList[node]:
                if neigh not in visited:
                    maxLengthPathFromThisNeigh = dfs(neigh)
                    heapq.heappush(minHeap, (-len(maxLengthPathFromThisNeigh), maxLengthPathFromThisNeigh))
            longestPath1, longestPath2 = [], []
            if minHeap:
                longestPath1 = heapq.heappop(minHeap)[1]
            if minHeap:
                longestPath2 = heapq.heappop(minHeap)[1]
            if len(longestPath1)+len(longestPath2)+1>len(maxLengthPath):
                maxLengthPath = longestPath1 + [node] + longestPath2[::-1]
            return longestPath1 + [node]

        dfs(0)
        if len(maxLengthPath)%2==0:
            return [maxLengthPath[len(maxLengthPath)//2 -1], maxLengthPath[len(maxLengthPath)//2]] 
        else:
            return [maxLengthPath[len(maxLengthPath)//2]] 


class Solution:
    def findMinHeightTrees(self, n: int, edges):
        adjList = [set() for _ in range(n)]
        for edge in edges:
            adjList[edge[0]].add(edge[1])
            adjList[edge[1]].add(edge[0])
        
        leaves = [i for i in range(n) if len(adjList[i])==1]
        numRemaining = n
        while numRemaining>2:
            numRemaining -= len(leaves)
            nextLeaves = []
            for num in leaves:
                for neigh in adjList[num]:
                    adjList[neigh].remove(num)
                    if len(adjList[neigh]) == 1:
                        nextLeaves.append(neigh)
            leaves = nextLeaves
        return leaves


             
        