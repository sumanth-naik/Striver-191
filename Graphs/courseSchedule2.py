from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites):

        indegreeArr = [0 for _ in range(numCourses)]
        adjList = [[] for _ in range(numCourses)]

        for after, before in prerequisites:
            adjList[before].append(after)
            indegreeArr[after] += 1

        queue = deque()
        for i in range(numCourses):
            if indegreeArr[i]==0:
                queue.append(i)
        
        topologicalOrdering = []
        while queue:
            node = queue.popleft()
            topologicalOrdering.append(node)
            for neigh in adjList[node]:
                indegreeArr[neigh] -= 1
                if indegreeArr[neigh]==0:
                    queue.append(neigh)
        
        return [] if len(topologicalOrdering)!=numCourses else topologicalOrdering
                    
        
                        


