class Solution:
    def criticalConnections(self, n: int, connections):
        adjList = [[] for _ in range(n)]
        for connection in connections:
            adjList[connection[0]].append(connection[1])
            adjList[connection[1]].append(connection[0])

        low, timeOfInsertion, time, bridges = [1e9 for _ in range(n)], [-1 for _ in range(n)], 1, set()
        def tarjansAlgo(node, parent):
            nonlocal low, timeOfInsertion, time, bridges
            timeOfInsertion[node] = time
            low[node] = time
            time += 1
            for neigh in adjList[node]:
                if neigh==parent:
                    continue
                if timeOfInsertion[neigh]==-1:
                    tarjansAlgo(neigh, node)
                    if low[neigh]>timeOfInsertion[node]:
                        bridges.add((min(node, neigh), max(node, neigh)))
                low[node] = min(low[node], low[neigh])

        for i in range(n):
            if timeOfInsertion[i]==-1:
                tarjansAlgo(i, -1)
        return bridges