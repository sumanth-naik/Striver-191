
class UnionFind:
    def __init__(self) -> None:
        self.parent = {}
        self.size = {}

    def addNode(self, node):
        if not node in self.parent:
            self.parent[node] = node
            self.size[node] = 1

    def union(self, node1, node2):
        self.addNode(node1)
        self.addNode(node2)
        parent1 = self.findParent(node1)
        parent2 = self.findParent(node2)
        if not parent1==parent2:
            if self.size[parent1]>self.size[parent2]:
                self.parent[parent2] = parent1
                self.size[parent1] += self.size[parent2]
            else:
                self.parent[parent1] = parent2
                self.size[parent2] += self.size[parent1]

    def findParent(self, node):
        if not self.parent[node]==node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    

class Solution:
    def numberOfGoodPaths(self, vals, edges):
        unionFind = UnionFind()
        numGoodPaths, numNodes = 0, len(vals)

        adjList = [[] for i in range(numNodes)]
        for edge in edges:
            if vals[edge[0]]>=vals[edge[1]]:
                adjList[edge[0]].append(edge[1])
            else:
                adjList[edge[1]].append(edge[0])

        valToNodesMap = {}
        for index, val in enumerate(vals):
            if not val in valToNodesMap:
                valToNodesMap[val] = []
            valToNodesMap[val].append(index)
        sortedMapTuples = sorted(valToNodesMap.items())

        for valAndNodesTuple in sortedMapTuples:
            for node in valAndNodesTuple[1]:
                for neigh in adjList[node]:
                    unionFind.union(node, neigh)

            numNodesInEachComponentMap = {}
            for node in valAndNodesTuple[1]:
                componentParent = unionFind.findParent(node)
                if not componentParent in numNodesInEachComponentMap:
                    numNodesInEachComponentMap[componentParent] = 0
                numNodesInEachComponentMap[componentParent] += 1
            
            for count in numNodesInEachComponentMap.values():
                numGoodPaths += ((count)*(count-1))//2

        return numGoodPaths + numNodes











# vals = [1,3,2,1,3]
# edges = [[0,1],[0,2],[2,3],[2,4]]
# sol = Solution()
# sol.numberOfGoodPaths(vals, edges)