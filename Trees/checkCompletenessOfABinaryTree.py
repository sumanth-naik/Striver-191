# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root):

        depthOfLastSeenLeafNode, leafNodeHeightDecreased = None, False
        def traversal(node, height):
            nonlocal depthOfLastSeenLeafNode, leafNodeHeightDecreased
            if not node:
                if not depthOfLastSeenLeafNode:
                    depthOfLastSeenLeafNode = height
                elif height!=depthOfLastSeenLeafNode:
                    if height>depthOfLastSeenLeafNode or height<depthOfLastSeenLeafNode-1 or leafNodeHeightDecreased:
                        return False
                    depthOfLastSeenLeafNode = height
                    leafNodeHeightDecreased = True
            else:
                if not traversal(node.left, height + 1): return False
                if not traversal(node.right, height + 1): return False
            return True
        
        return traversal(root, 0)
        

                
