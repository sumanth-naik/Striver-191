class Solution:
    def eventualSafeNodes(self, graph):
        visited = [0 for _ in range(len(graph))]
        # pathVisited will contain 1 if they are part of cycle or they lead to a cycle
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
        indegreeArr, adjList = [0 for _ in range(len(graph))], defaultdict(list)
        for node, neighList in enumerate(graph):
            indegreeArr[node] += len(neighList)
            for neigh in neighList:
                adjList[neigh].append(node)
        
        queue, topoSort = deque([node for node in range(len(graph)) if indegreeArr[node]==0]), []
        while queue:
            node = queue.popleft()
            topoSort.append(node)
            for neigh in adjList[node]:
                indegreeArr[neigh] -= 1
                if indegreeArr[neigh]==0:
                    queue.append(neigh)
        return sorted(topoSort)
