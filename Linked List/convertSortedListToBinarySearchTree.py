# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head):

        node = head
        # create Tree nodes and store head and tail(prevTreeNode will be the tail)
        headTreeNode, prevTreeNode = None, None
        while node:
            currTreeNode = TreeNode(node.val, prevTreeNode)
            if not headTreeNode:
                headTreeNode = currTreeNode
            if prevTreeNode:
                prevTreeNode.right = currTreeNode
            prevTreeNode = currTreeNode
            node = node.next

        # find mid using (head, tail)
        # remove links between mid-1 and mid; mid and mid+1
        # call recursion on (head, mid-1) and (mid+1, tail) each returning their mids
        # point current mid.left to left recursion answer and mid.right to right recursion answer

        def recursion(head, tail):
            if not head or not tail: return None 
            # finding mid (nodeMovingRight and nodeMovingLeft will point to mid in the end)
            nodeMovingRight, nodeMovingLeft, turn = head, tail, True
            while nodeMovingRight!=nodeMovingLeft:
                if turn: nodeMovingRight = nodeMovingRight.right
                else: nodeMovingLeft = nodeMovingLeft.left
                turn = not turn
            
            mid, midMinusOne, midPlusOne = nodeMovingLeft, None, None
            # removing links
            if mid.left:
                midMinusOne = mid.left
                midMinusOne.right = None
                mid.left = None
            if mid.right:
                midPlusOne = mid.right
                midPlusOne.left = None
                mid.right = None   

            # calling recursions
            mid.left = recursion(head, midMinusOne)
            mid.right = recursion(midPlusOne, tail)

            return mid
        
        return recursion(headTreeNode, prevTreeNode)
    