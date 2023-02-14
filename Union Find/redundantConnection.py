# Krushkals

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
    def findRedundantConnection(self, edges):
        unionFind = UnionFind()
        for edge in edges:
            unionFind.addNode(edge[0])
            unionFind.addNode(edge[1])
            if unionFind.belongToSameComponent(edge[0], edge[1]):
                return edge
            else:
                unionFind.union(edge[0], edge[1])
