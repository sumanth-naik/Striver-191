class Solution:
    def longestCycle(self, edges):
        visitedSet, maxCycleLength = set(), -1

        def dfs(node):
            nonlocal visitedSet, maxCycleLength
            visitedSet.add(node)
            if edges[node] not in visitedSet and edges[node]!=-1:
                cycleFound = dfs(edges[node])
                if cycleFound:
                    cycleStartsAt, lengthSoFar = cycleFound
                    if cycleStartsAt!=node:
                        return cycleStartsAt, lengthSoFar+1
                    else:
                        maxCycleLength = max(maxCycleLength, lengthSoFar+1)
            elif edges[node] in visitedSet:
                return edges[node], 1

        for i in range(len(edges)):
            if i not in visitedSet:
                dfs(i)

        return maxCycleLength