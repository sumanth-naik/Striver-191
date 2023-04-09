# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root):
        preorderTraversalsSet, duplicatePreorderTraversalsSet, duplicateNodesSet = set(), set(), set()
        def preorderTraversal(node):
            if not node: return tuple("null")
            preorderTraversalFromNode = tuple([node.val]) + preorderTraversal(node.left) + preorderTraversal(node.right)
            if preorderTraversalFromNode in preorderTraversalsSet and preorderTraversalFromNode not in duplicatePreorderTraversalsSet:
                duplicateNodesSet.add(node)
                duplicatePreorderTraversalsSet.add(preorderTraversalFromNode)
            else:
                preorderTraversalsSet.add(preorderTraversalFromNode)
            return preorderTraversalFromNode
        preorderTraversal(root)
        return duplicateNodesSet

