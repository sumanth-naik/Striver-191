from collections import deque
class Solution:
    def isBipartite(self, graph):

        colorArr = [-1 for _ in range(len(graph))]
        
        def bfs(queue):
            while queue:
                node = queue.pop()
                for neigh in graph[node]:
                    if colorArr[neigh]==colorArr[node]:
                        return False
                    elif colorArr[neigh]==-1:
                        colorArr[neigh] = 1-colorArr[node]
                        queue.append(neigh)
            return True

        for i in range(len(graph)):
            if colorArr[i]==-1:
                colorArr[i]=1
                if not bfs(deque([i])): return False
        return True


        
class Solution:
    def isBipartite(self, graph):
        colorArr = [-1 for _ in range(len(graph))]
        def dfs(node):
            for neigh in graph[node]:
                if colorArr[neigh]==colorArr[node]: return False
                elif colorArr[neigh]==-1:
                    colorArr[neigh] = 1-colorArr[node]
                    if not dfs(neigh): return False
            return True
            
        for node in range(len(graph)):
            if colorArr[node]==-1:
                colorArr[node]=1
                if not dfs(node): return False
        return True 
