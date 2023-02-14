class Solution:
    def minReorder(self, n: int, connections):
        adjList, connectionsSet = [[] for _ in range(n)], set()
        for connection in connections:
            adjList[connection[0]].append(connection[1])
            adjList[connection[1]].append(connection[0])
            connectionsSet.add(tuple(connection))

        numChangesOfConnections = 0
        def dfs(node, parent):
            nonlocal numChangesOfConnections
            for neigh in adjList[node]:
                if neigh != parent:
                    if (node, neigh) in connectionsSet: 
                        numChangesOfConnections += 1
                    dfs(neigh, node)

        dfs(0, -1)
        return numChangesOfConnections