class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traversal(node, minAncestorVal, maxAncestorVal, maxDiff):
    if node:
        maxDiff[0] = max(maxDiff[0], max(abs(node.val - minAncestorVal), abs(node.val - maxAncestorVal)))
        traversal(node.left, min(minAncestorVal, node.val), max(maxAncestorVal, node.val), maxDiff)
        traversal(node.right, min(minAncestorVal, node.val), max(maxAncestorVal, node.val), maxDiff)
        

def maxAncestorDiff(root):
    maxDiff = []
    traversal(root, root.val, root.val, maxDiff)
    return maxDiff[0]