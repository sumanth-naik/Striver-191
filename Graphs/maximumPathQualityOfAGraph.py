class Solution:
    def maximalPathQuality(self, values, edges, maxTime):
        adjList = [[] for _ in range(len(values))]
        for edge in edges:
            adjList[edge[0]].append((edge[2], edge[1]))
            adjList[edge[1]].append((edge[2], edge[0]))

        maxPathQualitySeen = 0
        def dfs(node, visitedSet, timeLeft):
            nonlocal maxPathQualitySeen
            if node == 0:
                maxPathQualitySeen = max(maxPathQualitySeen, sum(values[i] for i in visitedSet))
            for timeToNeigh , neigh in adjList[node]:
                if timeToNeigh <= timeLeft:
                    # deepcopy is slow, use set(visitedSet) or directly or operator which creates a new one
                    dfs(neigh, visitedSet | set([neigh]), timeLeft - timeToNeigh)
        dfs(0,set([0]),maxTime)
        return maxPathQualitySeen    