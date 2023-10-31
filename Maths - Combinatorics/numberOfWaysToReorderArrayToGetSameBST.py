# Key Idea: create new arrays similar to BST structure as part of DFS instead of creating entire BST first

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9+7
        def dfs(nums):
            if len(nums)<=2: return 1
            left, right = [], []
            for num in nums:
                if num<nums[0]: left.append(num)
                if num>nums[0]: right.append(num)
            return (dfs(left) * dfs(right) * comb(len(left)+len(right), len(right)))%MOD
        return (dfs(nums)-1)%MOD



'''Basic Approach - Create BST and then do DFS'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(self.root, val)

    def _add(self, node, newVal):
        if node.val>newVal:
            if node.left is None: 
                node.left = Node(newVal)
            else:
                self._add(node.left, newVal)
        else:
            if node.right is None: 
                node.right = Node(newVal)
            else:
                self._add(node.right, newVal)

    def build(self, nums):
        for num in nums:
            self.add(num)


# Key Idea 1: Interleave two orderings of length p1 and p2 -> (p1+p2)!/p1!p2! [denominator removes unnecessary repeats], which happens to be p1+p2 Choose p1
# Key Idea 2: Do that interleaving for each permutation combo of child subtrees to get total permutation from root

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        bst = BST()
        bst.build(nums)
        MOD = 10**9+7

        def dfs(node):
            if not node: 
                return 0, 1 #number of nodes in subtree, number of permutations of subtree as arr
            leftNodesCount, leftPerms = dfs(node.left)
            rightNodesCount, rightPerms = dfs(node.right)
            return leftNodesCount+rightNodesCount+1, \
                (leftPerms * rightPerms * comb(leftNodesCount+rightNodesCount, rightNodesCount))%MOD

        return (dfs(bst.root)[1]-1)%MOD