class Solution:
    def canFinish(self, numCourses, prerequisites):
        adjList = {}
        for after, before in prerequisites:
            if not before in adjList:
                adjList[before] = []
            adjList[before].append(after)
        
        visitedInAllComponents = set()
        def dfs(course, visitedInThePath):
            visitedInThePath.add(course)
            visitedInAllComponents.add(course)
            if course in adjList:
                for nextCourse in adjList[course]:
                    if nextCourse in visitedInThePath: return False
                    if nextCourse in visitedInAllComponents: continue
                    if not dfs(nextCourse, visitedInThePath): return False
            visitedInThePath.remove(course)
            return True
        
        for course in adjList.keys():
            if not course in visitedInAllComponents:
                if not dfs(course, set()): return False

        return True

class Solution:
    def canFinish(self, numCourses, prerequisites):

        adjList = [[] for _ in range(numCourses)]
        reversedAdjList = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            if course==prereq: return False
            adjList[prereq].append(course)
            reversedAdjList[course].append(prereq)

        visited, stronglyConnectedComponentsOrderStack = set(), []
        def dfs(node):
            nonlocal visited, stronglyConnectedComponentsOrderStack
            visited.add(node)
            for neigh in adjList[node]:
                if neigh not in visited:
                    dfs(neigh)
            stronglyConnectedComponentsOrderStack.append(node)

        for course in range(numCourses):
            if not course in visited:
                dfs(course)

        kosarajusAlgoVisited = set()
        def kosarajusAlgo(node):
            nonlocal kosarajusAlgoVisited
            kosarajusAlgoVisited.add(node)
            for neigh in reversedAdjList[node]:
                if neigh not in kosarajusAlgoVisited:
                    kosarajusAlgo(neigh)

        numStronglyConnectedComponents = 0
        for course in reversed(stronglyConnectedComponentsOrderStack):
            if course not in kosarajusAlgoVisited:
                numStronglyConnectedComponents += 1
                kosarajusAlgo(course)

        return numStronglyConnectedComponents==numCourses
    
class Solution:
    def canFinish(self, numCourses, prerequisites):
        indegreeArr, adjList, topoSortArr = [0]*numCourses, [[] for _ in range(numCourses)], []

        for after, before in prerequisites:
            indegreeArr[after] += 1
            adjList[before].append(after)

        def dfs(node, indegreeArr, topoSortArr):
            topoSortArr.append(node)
            indegreeArr[node] = -1
            for neigh in adjList[node]:
                indegreeArr[neigh] -= 1
                if indegreeArr[neigh]==0:
                    dfs(neigh, indegreeArr, topoSortArr)
        
        for node in range(numCourses):
            if indegreeArr[node]==0:
                dfs(node, indegreeArr, topoSortArr)
        return True if len(topoSortArr)==numCourses else False
