# Key Idea: BST's inorder traversal is sorted. Just do Inorder with nonlocal variable keeping index

class Solution:
    def kthSmallest(self, root, k):                   

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
    