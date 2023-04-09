class Solution:
    def maximumInvitations(self, favorite):
        if len(favorite)==2: return 2
        adjList = [[] for _ in range(len(favorite))]
        nodePairsHavingTwoLengthCycles = set()
        for u, v in enumerate(favorite):
            adjList[v].append(u)
            # 2 len cycle
            if favorite[v]==u:
                nodePairsHavingTwoLengthCycles.add((min(u,v), max(u,v)))

        maxPeopleThatCanBeInvited = 0
        visited = set()
        def dfs(node):
            visited.add(node)
            if adjList[node]==[]: return 1
            maxSubtreeLength = 0
            for neigh in adjList[node]:
                maxSubtreeLength = max(maxSubtreeLength, dfs(neigh))
            return maxSubtreeLength + 1

        for node1, node2 in nodePairsHavingTwoLengthCycles:
            visited.add(node1)
            visited.add(node2)
            maxWithNode1, maxWithNode2 = 0, 0
            for neigh in adjList[node1]:
                if neigh!=node2:
                    maxWithNode1 = max(maxWithNode1, dfs(neigh))
            for neigh in adjList[node2]:
                if neigh!=node1:
                    maxWithNode2 = max(maxWithNode2, dfs(neigh))
            maxPeopleThatCanBeInvited += (maxWithNode1 + maxWithNode2 + 2)

        def dfsForLongestCycle(node):
            nonlocal visited, maxPeopleThatCanBeInvited
            visited.add(node)
            if favorite[node] not in visited and favorite[node]!=-1:
                cycleFound = dfsForLongestCycle(favorite[node])
                if cycleFound:
                    cycleStartsAt, lengthSoFar = cycleFound
                    if cycleStartsAt!=node:
                        return cycleStartsAt, lengthSoFar+1
                    else:
                        maxPeopleThatCanBeInvited = max(maxPeopleThatCanBeInvited, lengthSoFar+1)
            elif favorite[node] in visited:
                return favorite[node], 1
            
        for node in range(len(favorite)):
            if node not in visited:
                dfsForLongestCycle(node)

        return maxPeopleThatCanBeInvited

        


        