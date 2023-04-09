# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 2 pass DP
class Solution:
    def longestZigZag(self, root) -> int:

        @lru_cache(None)
        def memoization(node, isDirectionLeft):
            if not node: return 0
            if isDirectionLeft: return 1+memoization(node.left, False)
            else: return 1+memoization(node.right, True)

        nodesInMaxZigZagPath = 0
        def dfs(node):
            if not node: return
            nonlocal nodesInMaxZigZagPath
            nodesInMaxZigZagPath = max(nodesInMaxZigZagPath, memoization(node, True), memoization(node, False))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return nodesInMaxZigZagPath - 1
# 1 pass DP    
class Solution:
    def longestZigZag(self, root) -> int:
        maxZigZagPathLength = 0
        @lru_cache(None)
        def dfs(node):
            if not node: return (-1,-1)
            nonlocal maxZigZagPathLength

            _, r1 = dfs(node.left)
            l2, _ = dfs(node.right)

            maxZigZagPathLength = max(maxZigZagPathLength, 1+r1, 1+l2)
            return (1+r1, 1+l2)
        
        dfs(root)
        return maxZigZagPathLength
    
# stack based
class Solution:
    def longestZigZag(self, root) -> int:
        maxZigZagPathLength = 0
        # node, pathLenghtSoFar, prevDirectionWasLeft (initial direction doesnt matter as we check both ways anyway, just pass length differently)
        stack = [(root, 0, True)]

        while stack:
            node, pathLenghtSoFar, prevDirectionWasLeft = stack.pop()
            maxZigZagPathLength = max(maxZigZagPathLength, pathLenghtSoFar)        

            if prevDirectionWasLeft:
                if node.right: stack.append((node.right, pathLenghtSoFar+1, False))
                if node.left: stack.append((node.left, 1, True))
            else:
                if node.left: stack.append((node.left, pathLenghtSoFar+1, True))
                if node.right: stack.append((node.right, 1, False))
        return maxZigZagPathLength