# Key Idea: Maintain minVal, maxVal for each node. Assert minVal<node.val<maxVal

# Top down BST check

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, minVal, maxVal):
            if not node: return True
            if not minVal<node.val<maxVal: return False
            return dfs(node.left, minVal, node.val) and dfs(node.right, node.val, maxVal)

        return dfs(root, -2e32, 2e32)
    
# Other idea: check if inorder traversal is sorted