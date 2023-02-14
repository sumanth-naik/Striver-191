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
 