
from collections import Counter
class Solution:
    def numberOfGoodPaths(self, vals, edges):
        adjList = {}
        for edge in edges:
            if not edge[0] in adjList:
                adjList[edge[0]] = []
            if not edge[1] in adjList:
                adjList[edge[1]] = []
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        visited = set()
        numGoodPaths = 0
        def dfs(num):
            visited.add(num)
            nonlocal numGoodPaths
            counter = Counter()
            counter[vals[num]] = 1
            
            possiblePathEndingVertexToCountMapAcrossAllBranches = []
            for neighbor in adjList[num]:
                if neighbor not in visited:
                    possiblePathEndingVertexToCountMap = dfs(neighbor)
                    for endingVertex in list(possiblePathEndingVertexToCountMap.keys()):
                        if endingVertex<vals[num]:
                            del possiblePathEndingVertexToCountMap[endingVertex]
                        if endingVertex==vals[num]:
                            numGoodPaths += possiblePathEndingVertexToCountMap[endingVertex]
                    possiblePathEndingVertexToCountMapAcrossAllBranches.append(possiblePathEndingVertexToCountMap)
                    counter += possiblePathEndingVertexToCountMap
                    
            for i in range(len(possiblePathEndingVertexToCountMapAcrossAllBranches)):
                for j in range(i+1, len(possiblePathEndingVertexToCountMapAcrossAllBranches)):
                    for numKey in possiblePathEndingVertexToCountMapAcrossAllBranches[i]:
                        if numKey in possiblePathEndingVertexToCountMapAcrossAllBranches[j]:
                            numGoodPaths += (possiblePathEndingVertexToCountMapAcrossAllBranches[i][numKey] * possiblePathEndingVertexToCountMapAcrossAllBranches[j][numKey]) 
        
            return counter

        def dfs2(num):
            visited.add(num)
            nonlocal numGoodPaths
            counter = Counter()
            counter[vals[num]] = 1
            
            for neighbor in adjList[num]:
                if neighbor not in visited:
                    possiblePathEndingVertexToCountMap = dfs(neighbor)
                    for endingVertex in list(possiblePathEndingVertexToCountMap.keys()):
                        if endingVertex<vals[num]:
                            del possiblePathEndingVertexToCountMap[endingVertex]
                        elif endingVertex in counter:
                            numGoodPaths += possiblePathEndingVertexToCountMap[endingVertex]*counter[endingVertex]
                    counter += possiblePathEndingVertexToCountMap
                    
            return counter


        dfs(0)

        return numGoodPaths + len(visited)