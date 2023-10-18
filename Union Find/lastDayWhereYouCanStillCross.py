class UnionFind:
    def __init__(self, row, col):
        self.parent = defaultdict(int)
        self.size = defaultdict(int)
        self.row = row
        self.col = col

    def addNode(self, node):
        if not node in self.parent:
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

    def hasVerticalPath(self):
        return self.findParent((0,0))==self.findParent((self.row+1,0))

    def hasHorizontalPath(self):
        return self.findParent((1,0))==self.findParent((1, self.col+1))
    
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        unionFind = UnionFind(row, col) # land as components
        unionFind.addNode((0, 0))
        unionFind.addNode((row+1, 0))

        cellsSet = set(tuple([i,j]) for i,j in cells)


        def addCellToUnionFind(i,j):
            nonlocal unionFind
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                neighI, neighJ = i+di, j+dj
                if 1<=neighI<=row and 1<=neighJ<=col:
                    if (neighI, neighJ) not in cellsSet or (neighI, neighJ) in unionFind.parent:
                        unionFind.union((i,j), (neighI, neighJ))
                if neighI==0 and 1<=neighJ<=col:
                    unionFind.union((i,j), (0, 0))
                if neighI==row+1 and 1<=neighJ<=col:
                    unionFind.union((i,j), (row+1, 0))

        for i in range(1, row+1):
            for j in range(1, col+1):
                if (i, j) not in cellsSet:
                    addCellToUnionFind(i, j)

        index = len(cells)-1
        while True:
            if unionFind.hasVerticalPath(): return index+1
            unionFind.addNode((cells[index][0], cells[index][1]))
            addCellToUnionFind(cells[index][0], cells[index][1])
            index -= 1





class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        unionFind = UnionFind(row, col) # water as components

        for i in range(1, row): 
            unionFind.union((i,0),(i+1,0))
            unionFind.union((i,col+1),(i+1,col+1))

        for index, (i,j) in enumerate(cells):
            unionFind.addNode((i,j))
            for di, dj in [(0,1),(1,0),(-1,0),(0,-1),(1,-1),(-1,1),(-1,-1),(1,1)]:
                neighI, neighJ = i+di, j+dj
                if 0<=neighI<=row+1 and 0<=neighJ<=col+1:
                    if (neighI, neighJ) in unionFind.parent:
                        unionFind.union((i,j), (neighI, neighJ))
            if unionFind.hasHorizontalPath(): return index
            
        return len(cells)