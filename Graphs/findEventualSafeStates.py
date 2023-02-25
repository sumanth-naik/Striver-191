class Solution:
    def eventualSafeNodes(self, graph):
        visited = [0 for _ in range(len(graph))]
        pathVisited = [0 for _ in range(len(graph))]

        def dfs(node):
            nonlocal visited, pathVisited
            visited[node] = 1
            pathVisited[node] = 1
            for neigh in graph[node]:
                if visited[neigh]==1 and pathVisited[neigh]==1:
                    return
                elif visited[neigh]==0:
                    dfs(neigh)
                    if pathVisited[neigh]==1:
                        return
            pathVisited[node] = 0

        for node in range(len(graph)):
            if visited[node]==0:
                dfs(node)
        
        return [i for i in range(len(graph)) if pathVisited[i]==0]
    


from collections import deque
class Solution:
    def eventualSafeNodes(self, graph):
        outdegreeArr = [0 for i in range(len(graph))]
        parentAdjList = [[] for _ in range(len(graph))]
        for node, neighList in enumerate(graph):
            outdegreeArr[node] += len(neighList)
            for neigh in neighList:
                parentAdjList[neigh].append(node)

        topoSortArr = []
        queue = deque([i for i in range(len(graph)) if outdegreeArr[i]==0])

        while queue:
            node = queue.popleft()
            topoSortArr.append(node)
            for parent in parentAdjList[node]:
                outdegreeArr[parent] -= 1
                if outdegreeArr[parent] == 0:
                    queue.append(parent)
                
        return sorted(topoSortArr)