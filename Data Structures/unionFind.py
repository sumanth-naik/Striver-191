# init with n nodes
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
    
    def belongsToSameComponent(self, node1, node2):
        return self.findParent(node1) == self.findParent(node2)




# have addNode function which is called on union
class UnionFind:
    def __init__(self) -> None:
        self.parent = {}
        self.size = {}
    
    def findParent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def addNode(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.size[node] = 1

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

    def belongsToSameComponent(self, node1, node2):
        return self.findParent(node1) == self.findParent(node2)

    def getParentToNodesInComponentMap(self):
        map = defaultdict(list)
        for node in self.parent:
            map[self.findParent(node)].append(node)
        return map
