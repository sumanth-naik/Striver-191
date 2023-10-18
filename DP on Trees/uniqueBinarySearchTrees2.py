# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        @lru_cache(None)
        def dp(numsTuple):
            if len(numsTuple)==0: return [None]
            bstList = []
            for index, num in enumerate(numsTuple):
                for leftTree in dp(numsTuple[:index]):
                    for rightTree in dp(numsTuple[index+1:]):
                        bstList.append(TreeNode(num, leftTree, rightTree))
            return bstList

        return dp(tuple(range(1, n+1)))
    
