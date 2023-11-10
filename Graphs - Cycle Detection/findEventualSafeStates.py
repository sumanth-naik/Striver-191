# Key Idea: DFS. Are all neighs safe?

class Solution:
    def eventualSafeNodes(self, graph):
        safe, visited = set(), set()
        
        def dfs(node):
            if node in visited: 
                return node in safe
            visited.add(node)
            if all(dfs(neigh) for neigh in graph[node]):
                safe.add(node)
                return True
        
        return list(filter(dfs, range(len(graph))))




# Key Idea: DFS. Use pathVisited and visited arrays. Visit unvisited neighs. 
#                pathVisited is 1 when neigh is unsafe

class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        visited, pathVisited = [0]*n, [0]*n

        def dfs(node):
            visited[node] = pathVisited[node] = 1
            for neigh in graph[node]:
                if not visited[neigh]: 
                    dfs(neigh)
                if pathVisited[neigh]==1: return
            pathVisited[node] = 0

        for node in range(len(graph)):
            if not visited[node]:
                dfs(node)
        
        return [node for node in range(len(graph)) if pathVisited[node]==0]
    


# Key Idea: TopoSort on reversed graph

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
