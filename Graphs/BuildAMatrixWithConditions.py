from collections import deque
class Solution:
    def buildMatrix(self, k: int, rowConditions, colConditions):

        # 1 indexed
        def kahnsAlgo(numNodes, edges):
            indegreeArr, adjList = [0 for _ in range(numNodes+1)], [[] for _ in range(numNodes+1)]
            for edge in edges:
                adjList[edge[0]].append(edge[1])
                indegreeArr[edge[1]] += 1
            queue = deque()
            for node in range(1, numNodes+1):
                if indegreeArr[node] == 0:
                    queue.append(node)
            topoSortArr = []
            while queue:
                node = queue.pop()
                topoSortArr.append(node)
                for neigh in adjList[node]:
                    indegreeArr[neigh] -= 1
                    if indegreeArr[neigh] == 0:
                        queue.append(neigh)
            return topoSortArr if len(topoSortArr)==k else None
        
        rowConditionsTopoSortArr = kahnsAlgo(k, rowConditions)
        if rowConditionsTopoSortArr is None: return
        colConditionsTopoSortArr = kahnsAlgo(k, colConditions)
        if colConditionsTopoSortArr is None: return

        colConditionsTopoSortToIndex = {}
        for j, colConditionsTopoSortElem in enumerate(colConditionsTopoSortArr):
            colConditionsTopoSortToIndex[colConditionsTopoSortElem] = j

        outputMatrix = [[0 for _ in range(k)] for _ in range(k)]
        for i, rowConditionsTopoSortElem in enumerate(rowConditionsTopoSortArr):
            outputMatrix[i][colConditionsTopoSortToIndex[rowConditionsTopoSortElem]] = rowConditionsTopoSortElem
        return outputMatrix