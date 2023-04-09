
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]


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
        if not self.findParent(node1)==self.findParent(node2):
            self.islands -= 1
            print(node1, ~node2)
            self.parent[self.parent[node1]] = self.parent[self.parent[node2]]
    
def removeStones(stones):
    unionFind = UnionFind()
    for stone in stones:
        unionFind.addNode(stone[0])
        unionFind.addNode(~stone[1])
        unionFind.union(stone[0],~stone[1])
    print(unionFind.parent)
    return len(stones) - unionFind.islands

print(removeStones(stones))