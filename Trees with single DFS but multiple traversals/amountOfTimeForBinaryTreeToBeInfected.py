# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        maxBurnTime = 0
        def burn(node, burnTime):
            nonlocal maxBurnTime
            if not node: return None
            if node.val==start:
                burnTime = 0
            if burnTime is not None:
                burn(node.left, burnTime+1)
                burn(node.right, burnTime+1)
            else:
                burnTime = burn(node.left, None)
                if burnTime is not None:
                    burn(node.right, burnTime+1)
                else:
                    burnTime = burn(node.right, None)
                    if burnTime is not None:
                        burn(node.left, burnTime+1)
            if burnTime is not None:
                maxBurnTime = max(maxBurnTime, burnTime)
                return burnTime+1
            return None
        burn(root, None)
        return maxBurnTime
        