# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, n: int):
        if not n&1: return []
        
        def recursion(n):
            if n==1: return [TreeNode()]
            ansArr = []
            for i in range(1, n, 2):
                leftSubTreePossibilities = recursion(i)
                rightSubTreePossibilities = recursion(n-i-1)
                for left in leftSubTreePossibilities:
                    for right in rightSubTreePossibilities:
                        root = TreeNode()
                        root.left = left
                        root.right = right
                        ansArr.append(root)
            return ansArr

        return recursion(n)
    
class Solution:
    def allPossibleFBT(self, n: int):
        if not n&1: return []
        
        memo = {1:[TreeNode(0)]}
        def memoization(n):
            nonlocal memo
            if n in memo: return memo[n]
            ansArr = []
            for i in range(1, n, 2):
                leftSubTreePossibilities = memoization(i)
                rightSubTreePossibilities = memoization(n-i-1)
                for left in leftSubTreePossibilities:
                    for right in rightSubTreePossibilities:
                        root = TreeNode()
                        root.left = left
                        root.right = right
                        ansArr.append(root)
            memo[n] = ansArr
            return memo[n]

        return memoization(n)
    
    
class Solution:
    def allPossibleFBT(self, n: int):
        if not n&1: return []
        
        dp = [[] for _ in range(n+1)]
        dp[1] = [TreeNode()]
        # tabulation
        for numNodes in range(1, n+1, 2):
            for i in range(1, numNodes, 2):
                leftSubTreePossibilities = dp[i]
                rightSubTreePossibilities = dp[numNodes-i-1]
                for left in leftSubTreePossibilities:
                    for right in rightSubTreePossibilities:
                        root = TreeNode()
                        root.left = left
                        root.right = right
                        dp[numNodes].append(root)

        return dp[n]