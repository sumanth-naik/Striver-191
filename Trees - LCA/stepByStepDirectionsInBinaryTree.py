# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
            
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

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
            
            def lca(node):
                if not node or node.val in [startValue, destValue]: return node
                left, right = lca(node.left), lca(node.right)
                return node if left and right else left or right
            
            root = lca(root)

            def getPath(node, pathArr, targetVal):
                if node.val==targetVal: return pathArr
                if node.left:
                    pathArr.append("L")
                    path = getPath(node.left, pathArr, targetVal)
                    if path: return path
                    pathArr.pop()
                if node.right:
                    pathArr.append("R")
                    path = getPath(node.right, pathArr, targetVal)
                    if path: return path
                    pathArr.pop()

            def getDepth(node, depth, targetVal):
                if not node: return
                if node.val==targetVal: return depth
                left = getDepth(node.left, depth+1, targetVal)
                if left: return left
                right = getDepth(node.right, depth+1, targetVal)
                if right: return right


            return "U"*getDepth(root, 0, startValue) + ''.join(getPath(root, [], destValue))

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
            
            def lca(node):
                if not node or node.val in [startValue, destValue]: return node
                left, right = lca(node.left), lca(node.right)
                return node if left and right else left or right
            
            root = lca(root)

            def getPath(node, pathArr, targetVal):
                if node.val==targetVal: 
                    return True
                if node.left and getPath(node.left, pathArr, targetVal):
                    pathArr.append("L")
                    return True
                if node.right and getPath(node.right, pathArr, targetVal):
                    pathArr.append("R")
                    return True

            def getDepth(node, depth, targetVal):
                if not node: return
                if node.val==targetVal: return depth
                left = getDepth(node.left, depth+1, targetVal)
                if left: return left
                right = getDepth(node.right, depth+1, targetVal)
                if right: return right

            pathToDest = []
            getPath(root, pathToDest, destValue)
            return "U"*getDepth(root, 0, startValue) + ''.join(pathToDest)[::-1]

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def getPath(node, path, targetVal):
            if node.val==targetVal:
                return True
            if node.left and getPath(node.left, path, targetVal):
                path.append("L")
            elif node.right and getPath(node.right, path, targetVal):
                path.append("R")
            return path
        
        sourcePath, destPath = [], []
        getPath(root, sourcePath, startValue)
        getPath(root, destPath, destValue)
        while sourcePath and destPath and sourcePath[-1]==destPath[-1]:
            sourcePath.pop()
            destPath.pop()
        
        return "U"*len(sourcePath) + ''.join(destPath)[::-1]



class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        NONE, SRC, DST, BOTH = 0, 2, 3, 4
        srcPath, dstPath = [], []

        def dfs(node):
            nonlocal srcPath, dstPath
            if not node: return NONE
            leftHas = dfs(node.left)
            rightHas = dfs(node.right)

            if leftHas==SRC or rightHas==SRC: srcPath.append("U")
           
            if leftHas==DST: dstPath.append("L")
            elif rightHas==DST: dstPath.append("R")

            if leftHas==BOTH or rightHas==BOTH or (leftHas==SRC and rightHas==DST) or (leftHas==DST and rightHas==SRC):
                return BOTH
            
            if node.val==startValue: 
                if leftHas==DST or rightHas==DST: return BOTH
                return SRC

            if node.val==destValue: 
                if leftHas==SRC or rightHas==SRC: return BOTH
                return DST

            return leftHas or rightHas
        
        dfs(root)
        return ''.join(srcPath) + ''.join(dstPath[::-1])




class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        NONE, SRC, DST, BOTH = 0, 2, 3, 4 # Just NONE is False
        srcPath, dstPath = [], []

        def dfs(node):
            nonlocal srcPath, dstPath
            if not node: return NONE
            left, right = dfs(node.left), dfs(node.right)

            if SRC in [left, right]: srcPath.append("U")
            if DST in [left]: dstPath.append("L")
            elif DST in [right]: dstPath.append("R")

            if BOTH in [left, right] or (left and right): return BOTH
            if node.val==startValue: return BOTH if left or right else SRC
            if node.val==destValue: return BOTH if left or right else DST

            return left or right
        
        dfs(root)
        return ''.join(srcPath) + ''.join(dstPath[::-1])




class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        NONE, SRC, DST, BOTH = 0, 1, 2, 3
        srcPath, dstPath = [], []

        def dfs(node):
            if not node: return NONE
            left, right = dfs(node.left), dfs(node.right)

            if SRC in [left, right]: srcPath.append("U")
            if DST in [left]: dstPath.append("L")
            elif DST in [right]: dstPath.append("R")

            # return left | right | (2 - [destValue, startValue, node.val].index(node.val))
            return left | right | (SRC if node.val==startValue else DST if node.val==destValue else NONE)
        
        dfs(root)
        return ''.join(srcPath + dstPath[::-1])