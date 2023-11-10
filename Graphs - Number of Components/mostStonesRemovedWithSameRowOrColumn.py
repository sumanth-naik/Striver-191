# Key Idea 1: In each component, we can always remove the peripheral nodes till we have only one left
# Key Idea 2: Create two nodes for each point x, ~y to ease components union 

class UnionFind:
    def __init__(self):
        self.islands = 0
        self.parent = {}
    
    def findParent(self, node):
        if not self.parent[node]==node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def addNode(self, node):
        if not node in self.parent:
            self.parent[node] = node
            self.islands += 1
    
    def union(self, node1, node2):
        self.addNode(node1)
        self.addNode(node2)
        if not self.findParent(node1)==self.findParent(node2):
            self.islands -= 1
            self.parent[self.parent[node1]] = self.parent[self.parent[node2]]
    
   
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        unionFind = UnionFind()
        for stone in stones:
            unionFind.union(stone[0], ~stone[1])
        return len(stones) - unionFind.islands
        
        
        
        