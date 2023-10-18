# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        totalCount = 0

        def dfs(node, sumsArr):
            nonlocal totalCount
            if not node: return 
            
            for index in range(len(sumsArr)):
                sumsArr[index] += node.val
                if sumsArr[index]==targetSum:
                    totalCount += 1
            
            sumsArr.append(node.val)
            if node.val==targetSum:
                totalCount += 1

            dfs(node.left, sumsArr)
            dfs(node.right, sumsArr)

            sumsArr.pop()
            for index in range(len(sumsArr)):
                sumsArr[index] -= node.val

        dfs(root, [])
        return totalCount



# 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10 - 11
# <--firstPartSumNeeded--->   <--targetSum-->
# <------------------total------------------>
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(node, sumsFromRootMap, total):
            if not node: return 0

            total += node.val
            firstPartSumNeeded = total - targetSum
            
            count = sumsFromRootMap.get(firstPartSumNeeded, 0)
            sumsFromRootMap[total] = sumsFromRootMap.get(total, 0) + 1
            count += (dfs(node.left, sumsFromRootMap, total) + dfs(node.right, sumsFromRootMap, total))
            
            sumsFromRootMap[total] -= 1
            return count

        return dfs(root, {0:1}, 0)


            
