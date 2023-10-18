# TLE
from copy import deepcopy
class Solution:
    def shortestPathLength(self, graph):
        if len(graph)==1: return 0
        edgeVisitedMap = {}
        degreeMap = {}
        numNodes = len(graph)
        for node, neighbors in enumerate(graph):
            for neigh in neighbors:
                edgeVisitedMap[(node, neigh)] = False
                if not node in degreeMap:
                    degreeMap[node] = 0
                degreeMap[node] += 1
        
        lengthOfShortestPath = 1e9

        def dfs(node, visitedMap, pathLengthSoFar, edgeVisitedMapCopy):
            nonlocal lengthOfShortestPath, numNodes
            if pathLengthSoFar>=lengthOfShortestPath: return
            if not node in visitedMap:
                visitedMap[node] = 0
            visitedMap[node] += 1
            # print(visitedMap, pathLengthSoFar)
            if len(visitedMap) == numNodes:
                lengthOfShortestPath = min(lengthOfShortestPath, pathLengthSoFar)
                # print("************************", lengthOfShortestPath)
            else:
                for neigh in graph[node]:
                    # print("---------",node, neigh, edgeVisitedMapCopy)
                    if not edgeVisitedMapCopy[(node, neigh)]:
                        edgeVisitedMapCopy[(node, neigh)] = True
                        dfs(neigh, visitedMap, pathLengthSoFar+1, edgeVisitedMapCopy)
                        edgeVisitedMapCopy[(node, neigh)] = False
            visitedMap[node] -= 1
            if visitedMap[node] == 0:
                del visitedMap[node]

        sortedDegreeMapKeys = sorted(degreeMap.keys(), key=lambda node:degreeMap[node])
        minDegree = degreeMap[sortedDegreeMapKeys[0]]
        for node in degreeMap:
            if degreeMap[node]==minDegree:
                edgeVisitedMapCopy = deepcopy(edgeVisitedMap)
                dfs(node, {}, 0, edgeVisitedMapCopy)

        return lengthOfShortestPath
    

class Solution:
    def shortestPathLength(self, graph):
        # lastVisitedNode, maskOfVisitedNodes
        masksOfCurrentLevel = [(i, 1<<i) for i in range(len(graph))]
        previouslySeenLastNodeAndVisitedMaskCombo = set()
        finalMask, steps = (1<<len(graph))-1, 0
        while masksOfCurrentLevel:
            masksOfNextLevel = []
            for lastVisitedNode, maskOfVisitedNodes in masksOfCurrentLevel:
                if maskOfVisitedNodes == finalMask:
                    return steps
                for neigh in graph[lastVisitedNode]:
                    if not (neigh, maskOfVisitedNodes | 1<<neigh) in previouslySeenLastNodeAndVisitedMaskCombo:
                        previouslySeenLastNodeAndVisitedMaskCombo.add((neigh, maskOfVisitedNodes | 1<<neigh))
                        masksOfNextLevel.append((neigh, maskOfVisitedNodes | 1<<neigh))
            masksOfCurrentLevel = masksOfNextLevel
            steps += 1
