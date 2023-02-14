# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getTotalSum(node):
    if not node:
        return 0
    return (getTotalSum(node.left) + getTotalSum(node.right) + node.val)

def getMaxProductSplit(node, totalSum):
    if not node:
        return 0
    if node:
        leftSubtreeSum, leftMax = getMaxProductSplit(node.left, totalSum)
        rightSubtreeSum, rightMax = getMaxProductSplit(node.right, totalSum)
        maxVal = max(leftMax,max(rightMax,max(leftSubtreeSum*(totalSum-leftSubtreeSum), rightSubtreeSum*(totalSum-leftSubtreeSum))))
        return (leftSubtreeSum+rightSubtreeSum+node.val, maxVal)


def maxProductOfSplittedBinaryTree(root):
    totalSum = getTotalSum(root)
    return getMaxProductSplit(root, totalSum)[1]%(10**9+7)