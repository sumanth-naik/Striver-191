class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root, k):
                   
        def kthSmallestElementInBST(node, smallerSeenSoFar):
            nonlocal k
            if not node:
                return 0, None
            
            numLeftSubTreeNodes, leftSubTreeAns = kthSmallestElementInBST(node.left, smallerSeenSoFar)
            if smallerSeenSoFar + numLeftSubTreeNodes + 1 == k or leftSubTreeAns:
                return (-1, leftSubTreeAns or node.val)
            
            numRightSubTreeNodes, rightSubTreeAns = kthSmallestElementInBST(node.right, smallerSeenSoFar + numLeftSubTreeNodes + 1)
            
            return (-1, rightSubTreeAns) if rightSubTreeAns else (numLeftSubTreeNodes + numRightSubTreeNodes + 1, None) 

        # return kthSmallestElementInBST(root, 0)[1]

        def kthSmallestinBSTUsingInorderTraversal(node):
            if node:
                nonlocal k
                leftSubTreeAns = kthSmallestinBSTUsingInorderTraversal(node.left)
                k -= 1
                if k==0:
                    return node
                rightSubTreeAns = kthSmallestinBSTUsingInorderTraversal(node.right)
                return leftSubTreeAns or rightSubTreeAns if leftSubTreeAns or rightSubTreeAns else None
        return kthSmallestinBSTUsingInorderTraversal(root).val