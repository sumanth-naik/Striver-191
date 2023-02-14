class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges, blueEdges):
        distArrWhosePathsEndWithRedEdge, distArrWhosePathsEndWithBlueEdge = [1e10 for _ in range(n)], [1e10 for _ in range(n)]
        distArrWhosePathsEndWithRedEdge[0], distArrWhosePathsEndWithBlueEdge[0] = 0, 0

        for _ in range(n-1):
            for redEdgeStart, redEdgeEnd in redEdges:
                distArrWhosePathsEndWithRedEdge[redEdgeEnd] = min(distArrWhosePathsEndWithRedEdge[redEdgeEnd], distArrWhosePathsEndWithBlueEdge[redEdgeStart]+1)
            for blueEdgeStart, blueEdgeEnd in blueEdges:
                distArrWhosePathsEndWithBlueEdge[blueEdgeEnd] = min(distArrWhosePathsEndWithBlueEdge[blueEdgeEnd], distArrWhosePathsEndWithRedEdge[blueEdgeStart]+1)
                    
        return [min(len1, len2) if min(len1, len2)!=1e10 else -1 for len1, len2 in zip(distArrWhosePathsEndWithRedEdge, distArrWhosePathsEndWithBlueEdge)]


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges, blueEdges):
        blueAdjList, redAdjList = [[] for _ in range(n)], [[] for _ in range(n)]
        for start, end in redEdges:
            redAdjList[start].append(end)
        for start, end in blueEdges:
            blueAdjList[start].append(end)
        levelArr, nodeAndEndsWithVisitedSet = [(0,0,0), (0,0,1)], set([(0,0),(0,1)])
        distArr = [1e10 for _ in range(n)]
        distArr[0], red, blue = 0, 0, 1
        while levelArr:
            nextLevelArr = []
            for node, dist, colorOfLastEdge in levelArr:
                distArr[node] = min(distArr[node], dist)
                if colorOfLastEdge==red:
                    for blueNeigh in blueAdjList[node]:
                        if (blueNeigh, blue) not in nodeAndEndsWithVisitedSet:
                            nodeAndEndsWithVisitedSet.add((blueNeigh, blue))
                            nextLevelArr.append((blueNeigh, dist+1, blue))
                else:
                    for redNeigh in redAdjList[node]:
                        if (redNeigh, red) not in nodeAndEndsWithVisitedSet:
                            nodeAndEndsWithVisitedSet.add((redNeigh, red))
                            nextLevelArr.append((redNeigh, dist+1, red))

            levelArr = nextLevelArr
        return [dist if dist!=1e10 else -1 for dist in distArr]
