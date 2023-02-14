
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        inorderValToIndexMap = {}
        for index, val in enumerate(inorder):
            inorderValToIndexMap[val] = index
        return createTree(inorder, 0, len(preorder)-1, inorderValToIndexMap, preorder, 0)[0]

def createTree(inorder, inorderLeft, inorderRight, inorderValToIndexMap, preorder, preorderIndex):
    if inorderLeft>inorderRight:
        return None, preorderIndex
    currentNodePreorderIndex = inorderValToIndexMap[preorder[preorderIndex]]
    node = TreeNode(preorder[preorderIndex])
    preorderIndex += 1
    if preorderIndex!=len(preorder):
        node.left, preorderIndex = createTree(inorder, inorderLeft, currentNodePreorderIndex-1, inorderValToIndexMap, preorder, preorderIndex)
    if preorderIndex!=len(preorder):
        node.right, preorderIndex = createTree(inorder, currentNodePreorderIndex+1, inorderRight, inorderValToIndexMap, preorder, preorderIndex)
    return node, preorderIndex




class Solution2:
    def buildTree(self, preorder, inorder):
       
        def createTree(inorderLeft, inorderRight):
            nonlocal preorderIndex
            if inorderLeft>inorderRight:
                return None
            currentNodePreorderIndex = inorderValToIndexMap[preorder[preorderIndex]]
            node = TreeNode(preorder[preorderIndex])
            preorderIndex += 1
            node.left = createTree(inorderLeft, currentNodePreorderIndex-1)
            node.right = createTree(currentNodePreorderIndex+1, inorderRight)
            return node

        preorderIndex = 0
        inorderValToIndexMap = {}
        for index, val in enumerate(inorder):
            inorderValToIndexMap[val] = index
        return createTree(0, len(preorder)-1)




class SolutionPostOrder:
    def buildTree(self, inorder, postorder):

        def buildTreeFromArr(inorderLeft, inorderRight):
            nonlocal postorderIndex
            if inorderLeft>inorderRight:
                return None
            nodeVal = postorder[postorderIndex]
            node = TreeNode(nodeVal)
            postorderIndex -= 1
            node.right = buildTreeFromArr(inorderValToIndexMap[nodeVal]+1,inorderRight)
            node.left = buildTreeFromArr(inorderLeft, inorderValToIndexMap[nodeVal]-1)
            return node

        postorderIndex = len(postorder)-1
        inorderValToIndexMap = {}
        for index, val in enumerate(inorder):
            inorderValToIndexMap[val] = index
        return buildTreeFromArr(0, len(inorder)-1)

        

 