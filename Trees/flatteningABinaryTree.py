
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root):
        
        def preorderTraversal(node):
            if node:
                leftFirst, leftLast = preorderTraversal(node.left)
                rightFirst, rightLast = preorderTraversal(node.right)
                if leftFirst:
                    node.right = leftFirst
                    node.left = None
                    if rightFirst:
                        leftLast.right = rightFirst
                        leftLast.left = None
                elif rightFirst:
                    node.right = rightFirst
                    node.left = None
                return node, rightLast if rightLast else leftLast if leftLast else node
            return None, None

        preorderTraversal(root)
        return root  


    def flatten2(root):
        def reversedPreorder(node):
            if node:
                nonlocal prevNode
                reversedPreorder(node.right)
                reversedPreorder(node.left)
                node.right = prevNode
                node.left = None
                prevNode = node

        prevNode = None
        reversedPreorder(root)
        return root

    def morrisTraversal(root):
        currNode = root
        while(currNode):
            if currNode.left:
                rightMostNode = currNode.left
                while rightMostNode.right:
                    rightMostNode = rightMostNode.right
                rightMostNode.right = currNode.right
                currNode.right = currNode.left
                currNode.left = None
            currNode = currNode.right
        return root