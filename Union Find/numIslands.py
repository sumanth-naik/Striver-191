grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


class UnionFind:
    def __init__(self):
        self.size = {}
        self.parent = {}
    
    def findParent(self, node):
        if not node==self.parent[node]:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def addNode(self, node):
        if not node in self.parent:
            self.parent[node] = node
            self.size[node] = 1

    def attachNodes(self, node1, node2):
        self.parent[node2] = node1
        self.size[node1] += self.size[node2]

    def union(self, node1, node2):
        parent1 = self.findParent(node1)
        parent2 = self.findParent(node2)
        if parent1==parent2:
            return
        if self.size[parent1]>self.size[parent2]:
            self.attachNodes(parent1, parent2)
        else:
            self.attachNodes(parent2, parent1)

    def numDistinctComponents(self):
        count = 0
        for node in self.parent:
            if node==self.parent[node]:
                count += 1
        return count
    
    def numDistinctIslands(self, grid):
        count = 0
        for node in self.parent:
            if node==self.parent[node] and grid[node[0]][node[1]]=="1":
                count += 1    
        return count   

    def debug(self, m, n,grid):
        parentSet = set()
        for i in range(m):
            for j in range(n):
                parentSet.add(self.findParent((i,j)))
        for parent in parentSet:
            print("parent: ", parent)
            print("parent value in grid:",grid[parent[0]][parent[1]])
            print("parent size",self.size[parent])
        print("numDistinctComponents: ",self.numDistinctComponents())
        print("numDistinctIslands: ",self.numDistinctIslands(grid))
            
        
def numIslands(grid):
    m = len(grid)
    n = len(grid[0])
    unionFind = UnionFind()
    for i in range(m):
        for j in range(n):
            unionFind.addNode((i,j))
            for point in [(i+1,j), (i, j+1)]:
                if point[0]<m and point[1]<n and point[0]>=0 and point[1]>=0:
                    unionFind.addNode(point)
                    if grid[i][j]==grid[point[0]][point[1]]:
                        unionFind.union((i,j),point)
                

    unionFind.debug(m,n,grid)
    return unionFind.numDistinctIslands(grid)

print(numIslands(grid))
