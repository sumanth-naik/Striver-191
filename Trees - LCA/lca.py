class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lca(node, p, q):
    if not node:
         return None
    if node is p or node is q:
        return node
    else:
        left = lca(node.left, p, q)
        right = lca(node.right, p, q)
        if left and right:
            return node
        return left if left else right if right else None


def lca(node, p, q):
    if not node or node in [p,q]:
        return node
    left = lca(node.left, p, q)
    right = lca(node.right, p, q)
    return node if left and right else left or right
