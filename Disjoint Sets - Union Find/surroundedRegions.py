class Solution:
    def solve(self, board) -> None:
        m = len(board)
        n = len(board[0])
        unionFind = UnionFind()
        for i in range(m):
            for j in range(n):
                unionFind.addNode((i,j))
                for neigh in [(i+1,j),(i,j+1)]:
                    if 0<=neigh[0]<m and 0<=neigh[1]<n:
                        unionFind.addNode(neigh)
                        if board[i][j]==board[neigh[0]][neigh[1]]:
                            unionFind.union((i,j),neigh)
        oParentSet = set()
        oParentSetToRemove = set()
        for i in range(m):
            for j in range(n):
                if unionFind.parent[(i,j)]==(i,j) and board[i][j]=="O":
                    oParentSet.add((i,j))
                if board[i][j]=="O" and (i==0 or i==m-1 or j==0 or j==n-1):
                    oParentSetToRemove.add(unionFind.find((i,j)))
        oParentSet -= oParentSetToRemove
        for i in range(m):
            for j in range(n): 
                if board[i][j]=="O" and unionFind.find((i,j)) in oParentSet:
                    board[i][j] = "X"

        
        
        
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}
    
    def addNode(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.size[node] = 1
    
    def find(self, node):
        if self.parent[node]!=node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def attachNode(self, node1, node2):
        self.parent[node1] = node2
        self.size[node2] += self.size[node1]            

    def union(self, node1, node2):
        if self.find(node1) != self.find(node2):
            parent1 = self.parent[node1]
            parent2 = self.parent[node2]
            if self.size[parent1]<self.size[parent2]:
                self.attachNode(parent1, parent2)
            else:
                self.attachNode(parent2, parent1)




board = [["X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X","X","O","O","O","X","X","X","X","X","X","X","X"],["X","X","X","X","X","O","O","O","X","O","X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","X","O","X","O","X","O","X","O","O","O","X","X","X","X","X","X"],["X","X","X","X","X","O","X","O","O","O","X","X","X","X","X","X","X","X","X","X"],["X","X","X","X","X","O","X","X","X","X","X","X","X","X","X","X","X","X","X","X"]]

sol = Solution()
sol.solve(board)
print(board)