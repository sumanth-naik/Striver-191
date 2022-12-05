


# out of memory error
def findPath(node, num1, num2, pathSoFar):
    
    if(node==None):
        return ("", -1)
    

    left = findPath(node.left, num1, num2, pathSoFar+"L")
    right = findPath(node.right, num1, num2, pathSoFar+"R")
    
   
    #LCA is one of source or destination nodes; at thaat type of LCA 
    if (left[1]!=-1 or right[1]!=-1) and (num1==node.val or num2==node.val):
        if(num1==node.val):
            if(left[1]!=-1):
                return left
            else:
                return right
        else:
            if(left[1]!=-1):
                return ("U" * len(left[0]), -1)
            else:
                return ("U" * len(right[0]), -1)

        
    #LCA is not in source or destination nodes; at that type of LCA
    if(left[1]!=-1 and right[1]!=-1):
        path = ""
        if(num1==left[1]):
            path = path + "U" * len(left[0]) + right[0]
        else:
            path = path + "U" * len(right[0]) + left[0]                        
        return (path, -1)
    
    #the current node is one of source or destintation
    if(num1 == node.val):
        return (pathSoFar, num1)
    if(num2 == node.val):
        return (pathSoFar, num2)
        
    #some node in the middle, returns whichever is not -1, if both are -1, returns -1
    if(right[1]==-1):
        return left
    
    return right


# too lengthy
def lowestCommonAncestorHelper(node, p, q):

    #base case of any tree recursion
    if(node == None):
        return (0, None)
    
    #case to handle p = q
    if(p.val==q.val):
        return (2, p)
    
    count = 0
    
    #dont return as this may be the LCA, so need to check if any child is p or q
    if(node.val==p.val or node.val==q.val):
        count += 1

    left = lowestCommonAncestorHelper(node.left, p, q)
    right = lowestCommonAncestorHelper(node.right, p, q)

    #if LCA already found, return that only                                       
    if(left[0] == 2):
        return left
    if(right[0] == 2):
        return right
                                       
    count = count + left[0]
    count = count + right[0]
    
    #this is LCA        
    if(count==2):
        return (2, node)
    
    #returns 0 or 1
    return (count, None)

'''
taken from leetcode https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/discuss/1612179/Python3-lca

def lca(node):
       if not node or node.val in [startValue, destValue]:
           return node
       left = lca(node.left)
       right = lca(node.right)
       return node if left and right else left or right
       
'''
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# LCA + DFS
def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        
    def lca(node):
       if not node or node.val in [startValue, destValue]:
           return node
       left = lca(node.left)
       right = lca(node.right)
       return node if left and right else left or right

    lca = lca(root)

    stack = [(lca,"")]
    pathToSource = ""
    numFound = 0
    pathToDest = ""
    while(len(stack)):
        if(numFound==2): break
        node = stack.pop()
        if(node[0].left): stack.append((node[0].left, node[1]+"L"))
        if(node[0].right): stack.append((node[0].right, node[1]+"R"))
        if(startValue==node[0].val): 
            pathToSource = node[1]
            numFound += 1
        if(destValue==node[0].val):
            pathToDest = node[1]
            numFound += 1

    return "U" * len(pathToSource) + pathToDest 



# DFS single pass with string cutting
def getDirections(self, root: [TreeNode], startValue: int, destValue: int) -> str:
        
    stack = [(root,"")]
    pathToSource = ""
    numFound = 0
    pathToDest = ""
    while(len(stack)):
        if(numFound==2): break
        node = stack.pop()
        if(node[0].left): stack.append((node[0].left, node[1]+"L"))
        if(node[0].right): stack.append((node[0].right, node[1]+"R"))
        if(startValue==node[0].val): 
            pathToSource = node[1]
            numFound += 1
        if(destValue==node[0].val):
            pathToDest = node[1]
            numFound += 1
  
    numSame = 0
    for i in range(0, min(len(pathToSource), len(pathToDest))):
        if(pathToSource[i]!=pathToDest[i]): break
        numSame += 1
   
    return "U" * (len(pathToSource) - numSame) + pathToDest[numSame:]
    




pathToSource = "ABCDF"
pathToDest = "ABCDE"
numSame = 0
for i in range(0, min(len(pathToSource), len(pathToDest))):
   if(pathToSource[i]!=pathToDest[i]): break
   numSame += 1
print(numSame)