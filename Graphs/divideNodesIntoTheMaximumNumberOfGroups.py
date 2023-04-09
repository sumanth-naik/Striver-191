class Solution:
    def magnificentSets(self, n: int, edges):

        adjList = [[] for _ in range(n)]
        for u,v in edges:
            adjList[u-1].append(v-1)
            adjList[v-1].append(u-1)

        overallVisited = set()
        def dfs(node, componentVisited):
            nonlocal overallVisited
            overallVisited.add(node)
            componentVisited.add(node)
            for neigh in adjList[node]:
                if neigh not in componentVisited:
                    dfs(neigh, componentVisited)
            return componentVisited
        
        components = []
        for node in range(n):
            if node not in overallVisited:
                components.append(dfs(node, set()))


        def getBFSDepth(node):
            level, numLevels = [node], 0
            visited = set([node])
            while level:
                numLevels += 1
                levelSet, nextLevel = set(level), []
                for levelNode in level:
                    for neigh in adjList[levelNode]:
                        if neigh in visited and neigh in levelSet:
                            return -1
                        if neigh not in visited:
                            visited.add(neigh)
                            nextLevel.append(neigh)
                level = nextLevel
            return numLevels

        maxDepthAcrossComponent = 0
        for component in components:
            maxDepthOfComponent = 1
            for node in component:
                depth = getBFSDepth(node)
                if depth==-1: return -1
                maxDepthOfComponent = max(maxDepthOfComponent, depth)
            maxDepthAcrossComponent += maxDepthOfComponent
        
        return maxDepthAcrossComponent

        