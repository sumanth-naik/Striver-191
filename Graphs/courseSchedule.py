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
