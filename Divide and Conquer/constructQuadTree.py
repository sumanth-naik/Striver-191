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
       

# Key Idea 1: Given the size of square, if all elems are equal, return a Leaf. Else, recurse on size/2
# Note: use size instead of passing i1, j1 and i2, j2

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def build(i, j, size):
            if all(grid[x][y]==grid[i][j] for x in range(i, i+size) for y in range(j, j+size)): return Node(grid[i][j], True)
            mid = size//2
            return Node(1, False, build(i, j, mid), build(i, j+mid, mid), build(i+mid, j, mid), build(i+mid, j+mid, mid))

        return build(0, 0, len(grid))


# Key Idea 2: Optimise checking if all have same value by using Prefix Sum in Matrix approach

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        n = len(grid)
        prefixSumMat = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                prefixSumMat[i][j] = prefixSumMat[i][j-1] + prefixSumMat[i-1][j] - prefixSumMat[i-1][j-1] + grid[i-1][j-1]

        def isLeaf(i, j, size):
            sumInMatrix = prefixSumMat[i+size][j+size] - prefixSumMat[i+size][j] - prefixSumMat[i][j+size] + prefixSumMat[i][j] 
            return sumInMatrix in [0, size*size]
 
        def build(i, j, size):
            if isLeaf(i, j, size): return Node(grid[i][j], True)
            mid = size//2
            return Node(1, False, build(i, j, mid), build(i, j+mid, mid), build(i+mid, j, mid), build(i+mid, j+mid, mid))
            
        return build(0, 0, n)




# Key Idea: Divide till size=1. Post recursion, decide if children can be merged
# Note: Use the unpacking operator
 
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def build(i, j, size):
            if size==1: return Node(grid[i][j], True)
            mid = size//2
            children = build(i, j, mid), build(i, j+mid, mid), build(i+mid, j, mid), build(i+mid, j+mid, mid)
            if all(child.isLeaf and child.val==children[0].val for child in children):
                return Node(grid[i][j], True)
            return Node(1, False, *children) # Note
            
        return build(0, 0, len(grid))
        

# Follow up - write a set() function which interally updates the quad tree

'''
Key Idea: Stucture changes iff leaf changes. Leaves may SPLIT. Ancestors may MERGE.

How to TRAVERSE till leaf?
-> based on i, j and size. 
    -> Example: topLeft iff 0<=i<mid and 0<=j<mid 
-> Transpose to keep i, j as 0 indexed wrt currNode
    -> Example: i-mid, j-mid in case of currNode.bottomRight 

Cases:
Its a Leaf
    -> Its of size 1 
        -> No change in value
            => Nothing to do
        -> Change in value
            => set val and return; parent may need to MERGE
    -> not size 1
        -> No change in value
            => Nothing to do
        -> Change in value
            => SPLIT curr node(add children) and continue TRAVERSAL
Its not a leaf
    => TRAVERSAL to find leaf

'''
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        # 0<=i<size and 0<=j<size always
        def set(i, j, size, currNode, setVal):

            if currNode.isLeaf:
                if currNode.val==setVal: # Nothing to do
                    return currNode
                
                if size==1: # set val and parent may need to MERGE
                    currNode.val = setVal
                    return currNode

                # SPLIT curr node(add children) and continue TRAVERSAL
                currNode.topLeft, currNode.topRight, currNode.bottomLeft, currNode.bottomRight = [Node(currNode.val, True) for _ in range(4)]
                currNode.isLeaf = False 
            
            # TRAVERSAL
            mid = size//2
            if 0<=i<mid:
                if 0<=j<mid: set(i, j, mid, currNode.topLeft, setVal) # topLeft has the change
                else: set(i, j-mid, mid, currNode.topRight, setVal) # topRight has the change
            else:
                if 0<=j<mid: set(i-mid, j, mid, currNode.bottomLeft, setVal) # bottomLeft has the change
                else: set(i-mid, j-mid, mid, currNode.bottomRight, setVal) # bottomRight has the change

            # MERGE: iff all children are leaves with same value
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
         