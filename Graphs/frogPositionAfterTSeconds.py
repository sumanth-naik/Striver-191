class Solution:
    def frogPosition(self, n: int, edges, t: int, target: int) -> float:

        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(node, parent):
            if node==target:
                return [node]
            for neigh in adjList[node]:
                if neigh!=parent:
                    pathFound = dfs(neigh, node)
                    if pathFound: return [node] + pathFound

        pathToTarget = dfs(1,-1)

        def getDegree(node):
            return len(adjList[node])-1 if node!=1 else len(adjList[node])
    
        def isLeaf(node):
            return True if getDegree(node)==0 else False
        
        reachedOnTime = len(pathToTarget)-1
        if (t<reachedOnTime) or (not isLeaf(target) and t!=reachedOnTime):
            return 0
        
        degreeDenominator = 1
        for index in range(len(pathToTarget)-1):
            degreeDenominator *= getDegree(pathToTarget[index])

        return 1/degreeDenominator

