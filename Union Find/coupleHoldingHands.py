class UnionFind:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
    def findParent(self, node):
        if self.parent[node]!=node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        parent1 = self.findParent(node1)
        parent2 = self.findParent(node2)
        if parent1!=parent2:
            if self.size[parent1]>self.size[parent2]:
                self.parent[parent2] = parent1
                self.size[parent1] += self.size[parent2]
            else:
                self.parent[parent1] = parent2
                self.size[parent2] += self.size[parent1] 
    

class Solution:
    def minSwapsCouples(self, row):
        unionFind = UnionFind(len(row))
        for i in range(0, len(row), 2):
            unionFind.union(row[i], row[i+1])
            unionFind.union(i, i+1)
        
        parentToSizeMap = {}
        for i in range(len(row)):
            parent = unionFind.findParent(i)
            if not parent in parentToSizeMap:
                parentToSizeMap[parent] = unionFind.size[parent]    
        
        return sum((num//2)-1 for num in parentToSizeMap.values())
