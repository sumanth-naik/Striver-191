class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreeMaxPathSum(node):
    if not node:
        return -float('inf'),-float('inf')
    leftSubTreeMaxBranchSum, leftSubTreeMaxPathSum = binaryTreeMaxPathSum(node.left)
    rightSubTreeMaxBranchSum, rightSubTreeMaxPathSum = binaryTreeMaxPathSum(node.right)
    subTreeMax = max(max(max(leftSubTreeMaxBranchSum + rightSubTreeMaxBranchSum + node.val, node.val), leftSubTreeMaxBranchSum + node.val), rightSubTreeMaxBranchSum + node.val)
    return max(max(leftSubTreeMaxBranchSum + node.val, rightSubTreeMaxBranchSum + node.val), node.val), max(subTreeMax, max(leftSubTreeMaxPathSum, rightSubTreeMaxPathSum))
 

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSumSeen = -1e9

        def dfs(node):
            nonlocal maxSumSeen
            if not node: return -1e9
            leftSubtreeMax = dfs(node.left)
            rightSubtreeMax = dfs(node.right)
            onlyNode = node.val
            nodeAndLeft = node.val + leftSubtreeMax
            nodeAndRight = node.val + rightSubtreeMax
            nodeAndBoth = node.val + leftSubtreeMax + rightSubtreeMax
            maxSumSeen = max(maxSumSeen, onlyNode, nodeAndLeft, nodeAndRight, nodeAndBoth)
            return max(onlyNode, nodeAndLeft, nodeAndRight)
        dfs(root)
        return maxSumSeen

