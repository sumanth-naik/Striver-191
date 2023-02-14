class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bstFromPreorder(self, preorder):
    def bstSearch(node, searchVal):
        if node:
            if node.val<searchVal:
                if node.right:
                    bstSearch(node.right, searchVal)
                else:
                    node.right = TreeNode(searchVal)
            else:
                if node.left:
                    bstSearch(node.left, searchVal)
                else:
                    node.left = TreeNode(searchVal)

    root = TreeNode(preorder[0])
    for index in range(1, len(preorder)):
        bstSearch(root, preorder[index])

    return root



def bstFromPreorder(self, preorder):
   
    root = TreeNode(preorder[0])
    stack = [root]
    for index in range(1, len(preorder)):
        while len(stack)>1 and stack[-2].val<preorder[index]:
            stack.pop()
        nodeToAdd = TreeNode(preorder[index])
        if stack[-1].val>preorder[index]:
            stack[-1].left = nodeToAdd
        else:
            stack[-1].right = nodeToAdd
            stack.pop()
            stack.append(nodeToAdd)
            

    return root