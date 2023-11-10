# Key Idea: DFS should return min, max in subtree along with sum

# Note 1: Base case is tricky
# Note 2: Use "is not None", since sumLeft=0 gives False

# Bottom up BST check

class Solution:
    def maxSumBST(self, root) -> int:
        maxSum = 0

        def dfs(node):
            if not node: return (1e9, -1e9, 0) # Note 1
            minLeft, maxLeft, sumLeft = dfs(node.left)
            minRight, maxRight, sumRight = dfs(node.right)
            if sumLeft is not None and sumRight is not None and maxLeft<node.val<minRight: # Note 2
                nonlocal maxSum
                maxSum = max(maxSum, sumLeft+sumRight+node.val)
                return (min(minLeft, node.val), max(maxRight, node.val), sumLeft+sumRight+node.val)
            return (None, None, None)
        
        dfs(root)
        return maxSum            