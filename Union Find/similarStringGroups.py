from typing import List
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def addNode(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.size[node] = 1
    
    def findParent(self, node):
        if self.parent[node]!=node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        self.addNode(node1)
        self.addNode(node2)
        parent1 = self.findParent(node1)
        parent2 = self.findParent(node2)
        if parent1!=parent2:
            if self.size[parent1]>self.size[parent2]:
                self.parent[parent2] = parent1
                self.size[parent1] += self.size[parent2]
            else:
                self.parent[parent1] = parent2
                self.size[parent2] += self.size[parent1]
            
    def getNumComponents(self):
        parentsSet = set()
        for node in self.parent:
            parentsSet.add(self.findParent(node))
        return len(parentsSet)


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        def isSimilar(str1, str2):
            numDiffs = 0
            for char1, char2 in zip(str1, str2):
                if char1!=char2: numDiffs+=1
                if numDiffs>2: return False
            return numDiffs<=2
        
        unionFind = UnionFind()
        for str1 in strs:
            for str2 in strs:
                if isSimilar(str1, str2): unionFind.union(str1, str2)

        return unionFind.getNumComponents()