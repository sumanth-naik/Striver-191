

class UnionFind:
    def __init__(self) -> None:
        self.parent = {}
        self.size = {}

    def addNode(self, node):
        if not node in self.parent:
            self.parent[node] = node
            self.size[node] = 1

    def findParent(self, node):
        if not self.parent[node]==node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        parent1 = self.findParent(node1)
        parent2 = self.findParent(node2)
        if not parent1==parent2:
            if self.size[parent1]>self.size[parent2]:
                self.parent[parent2] = parent1
                self.size[parent1] += self.size[parent2]
            else:
                self.parent[parent1] = parent2
                self.size[parent2] += self.size[parent1]

    def belongToSameComponent(self, node1, node2):
        return self.findParent(node1)==self.findParent(node2)

class Solution:
    def findRedundantDirectedConnection(self, edges):
        indegreeArr = [0 for _ in range(len(edges)+1)]
        indegreeArr[0] = -1

        for edge in edges:
            indegreeArr[edge[1]] += 1

        indegreeZeroNode, indegreeTwoNode = None, None
        for index, indegree in enumerate(indegreeArr):
            if indegree==0:
                indegreeZeroNode = index
            elif indegree==2:
                indegreeTwoNode = index

        if indegreeZeroNode is None and indegreeTwoNode is None:
            unionFind = UnionFind()
            for edge in edges:
                unionFind.addNode(edge[0])
                unionFind.addNode(edge[1])
                if unionFind.belongToSameComponent(edge[0], edge[1]):
                    return edge
                else:
                    unionFind.union(edge[0], edge[1])

        # if indegreeZeroNode is None and indegreeTwoNode is not None:
        #     for edge in reversed(edges):
        #         if edge[1] == indegreeTwoNode:
        #             return edge
        
        if indegreeZeroNode is not None and indegreeTwoNode is not None:

            adjList = [[] for _ in range(len(edges)+1)]
            for edge in edges:
                adjList[edge[0]].append(edge[1])

            visited, found = set(), None
            def dfs(node):
                visited.add(node)
                for neigh in adjList[node]:
                    if neigh not in visited:
                        dfs(neigh)
                    else:
                        nonlocal found
                        found = [node, neigh]

            dfs(indegreeTwoNode)
            if found:
                return found

        for edge in reversed(edges):
            if edge[1] == indegreeTwoNode:
                return edge



class Solution:
    def findRedundantDirectedConnection(self, edges):
        indegreeArr = [0 for _ in range(len(edges)+1)]
        indegreeArr[0] = -1
        adjList = [[] for _ in range(len(edges)+1)]
        indegreeTwoNode = None

        for edge in edges:
            indegreeArr[edge[1]] += 1
            adjList[edge[0]].append(edge[1])
            if indegreeArr[edge[1]]==2:
                indegreeTwoNode = edge[1]
      
        visitedInDfs, found = set(), None
        def dfs(node):
            visitedInDfs.add(node)
            for neigh in adjList[node]:
                if neigh not in visitedInDfs:
                    dfs(neigh)
                else:
                    nonlocal found
                    found = [node, neigh]

        if indegreeTwoNode is not None:
            dfs(indegreeTwoNode)
            if found:
                return found
            for edge in reversed(edges):
                if edge[1] == indegreeTwoNode:
                    return edge
        else:
            visitedNodes = set()
            for edge in reversed(edges):    
                if edge[1] not in visitedNodes:
                    dfs(edge[1])
                    if found:
                        return edge
                    visitedInDfs = set()
                    visitedNodes = visitedNodes.union(visitedInDfs)
                    
                    
