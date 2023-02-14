class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxSumBST(self, root) -> int:
    maxSum = 0
    def maxSumBSTHelper(node):
        nonlocal maxSum
        if node:
            left1, right1, sum1 = node.val, -float('inf'), 0
            if node.left:
                left1, right1, sum1 = maxSumBSTHelper(node.left)
            left2, right2, sum2 = float('inf'), node.val, 0
            if node.right:
                left2, right2, sum2 = maxSumBSTHelper(node.right)

            if sum1!=-float('inf') and sum2!=-float('inf') and right1<node.val<left2:
                maxSum = max(maxSum, sum1+sum2+node.val)
                return (left1, right2, sum1+sum2+node.val)
            else:
                return (-1,-1,-float('inf'))
    maxSumBSTHelper(root)
    return maxSum            

def maxSumBST(self, root) -> int:
    maxSum = 0
    def maxSumBSTHelper(node):
        if not node:
            return (float('inf'), -float('inf'),0)
        nonlocal maxSum
        if node:
            left1, right1, sum1 = maxSumBSTHelper(node.left)
            left2, right2, sum2 = maxSumBSTHelper(node.right)

            if sum1!=-float('inf') and sum2!=-float('inf') and right1<node.val<left2:
                maxSum = max(maxSum, sum1+sum2+node.val)
                return (min(left1, node.val), max(right2, node.val), sum1+sum2+node.val)
            else:
                return (-1,-1,-float('inf'))
    maxSumBSTHelper(root)
    return maxSum            