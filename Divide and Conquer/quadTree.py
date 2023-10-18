"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
# not so good way of doing it
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        summationMatrix = deepcopy(grid)
        n = len(grid)
        for i in range(n):
            for j in range(1, n):
                summationMatrix[i][j] += summationMatrix[i][j-1]
        for i in range(1, n):
            for j in range(n):
                summationMatrix[i][j] += summationMatrix[i-1][j]

        def getSum(topleftI, topLeftJ, bottomRightI, bottomRightJ):
            return summationMatrix[bottomRightI][bottomRightJ] - \
                    (summationMatrix[bottomRightI][topLeftJ-1] if topLeftJ-1>=0 else 0)- \
                    (summationMatrix[topleftI-1][bottomRightJ] if topleftI-1>=0 else 0)+ \
                    (summationMatrix[topleftI-1][topLeftJ-1] if topleftI-1>=0 and topLeftJ-1>=0 else 0)

        def getVal(topleftI, topLeftJ, bottomRightI, bottomRightJ):
            sumInMatrix = getSum(topleftI, topLeftJ, bottomRightI, bottomRightJ)
            if sumInMatrix == 0: return 0
            if sumInMatrix == (bottomRightI-topleftI+1)*(bottomRightJ-topLeftJ+1): return 1
            return -1

        def buildQuadTree(topleftI, topLeftJ, bottomRightI, bottomRightJ):
            val = getVal(topleftI, topLeftJ, bottomRightI, bottomRightJ)
            if val==-1:
                return Node(1, 0, \
                            buildQuadTree(topleftI, topLeftJ, (bottomRightI+topleftI)//2, (bottomRightJ+topLeftJ)//2),\
                            buildQuadTree(topleftI, (bottomRightJ+topLeftJ)//2+1, (bottomRightI+topleftI)//2, bottomRightJ),\
                            buildQuadTree((bottomRightI+topleftI)//2+1, topLeftJ, bottomRightI, (bottomRightJ+topLeftJ)//2),\
                            buildQuadTree((bottomRightI+topleftI)//2+1, (bottomRightJ+topLeftJ)//2+1, bottomRightI, bottomRightJ))
            elif val==1:
                return Node(1, 1, None, None, None, None)
            else:
                return Node(0, 1, None, None, None, None)

        return buildQuadTree(0, 0, n-1, n-1)


# Simple way
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def build(i, j, size):
            if all(grid[x][y]==grid[i][j] for x in range(i, i+size) for y in range(j, j+size)): return Node(grid[i][j], True)
            mid = size//2
            return Node(1, False, build(i, j, mid), build(i, j+mid, mid), build(i+mid, j, mid), build(i+mid, j+mid, mid))

        return build(0,0,len(grid))


# Another Simple way
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def build(i, j, size):
            if size==1: return Node(grid[i][j], True)
            mid = halfSize = size//2
            children = build(i, j, halfSize), build(i, j+mid, halfSize), build(i+mid, j, halfSize), build(i+mid, j+mid, halfSize)
            return Node(grid[i][j], True) if all(child.isLeaf and child.val==children[0].val for child in children) else Node(1, False, *children)
            
        return build(0, 0, len(grid))
        

# The hard way - follow up - write a set() function which interally updates the quad tree
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        # 0<=i<size and 0<=j<size always
        def set(i, j, size, currNode, setVal):

            if currNode.isLeaf and currNode.val==setVal: # leaf has same value -> no change
                return currNode
                
            if size==1: # a unit square -> no splitting, just change val
                currNode.val = setVal
                return currNode

            if currNode.isLeaf: # leaf and value changed and is not a unit square -> split
                currNode.topLeft, currNode.topRight, currNode.bottomLeft, currNode.bottomRight = [Node(currNode.val, True) for _ in range(4)] # fancy one liner to create children
                currNode.isLeaf = False # currNode.val does not matter anymore to currNode
            
            # currNode is not leaf in any case -> move to correct quadrant with index transposition to maintain "0<=i<size and 0<=j<size always"
            mid = size//2
            if 0<=i<mid:
                if 0<=j<mid: set(i, j, mid, currNode.topLeft, setVal) # topLeft has the change
                else: set(i, j-mid, mid, currNode.topRight, setVal) # topRight has the change
            else:
                if 0<=j<mid: set(i-mid, j, mid, currNode.bottomLeft, setVal) # bottomLeft has the change
                else: set(i-mid, j-mid, mid, currNode.bottomRight, setVal) # bottomRight has the change

            # cleanup post recursion step -> merge if all children are leaves with same value
            if all(child.isLeaf and child.val==setVal for child in [currNode.topLeft, currNode.topRight, currNode.bottomLeft, currNode.bottomRight]):
                currNode.isLeaf, currNode.val = True, setVal
                currNode.topLeft = currNode.topRight = currNode.bottomLeft = currNode.bottomRight = None    

            return currNode

        # Setting one by one to test the code     
        root, size = Node(1, True), len(grid)
        for i in range(size):
            for j in range(size):
                root = set(i, j, size, root, grid[i][j])
        return root
                
