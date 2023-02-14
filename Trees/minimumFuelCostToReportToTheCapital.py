import math
class Solution:
    def minimumFuelCost(self, roads, seats):
        adjList = [[] for _ in range(len(roads)+1)]
        for road in roads:
            adjList[road[0]].append(road[1])
            adjList[road[1]].append(road[0])

        fuelCost = 0
        def dfs(node, parent):
            nonlocal fuelCost
            numChildren = 1
            for neigh in adjList[node]:
                if neigh != parent:
                    numChildren += dfs(neigh, node)
            if parent!=-1:
                fuelCost += math.ceil(numChildren/seats)
            return numChildren
        dfs(0,-1)
        return fuelCost