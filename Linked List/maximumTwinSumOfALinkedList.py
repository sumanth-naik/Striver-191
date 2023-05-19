# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # find middle (given even number of nodes)
        slowPointer, fastPointer = head, head.next
        while fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

        def reverseLinkedList(node):
            prev, curr = None, node
            while curr:
                next = curr.next
                curr.next = prev
                prev, curr = curr, next
            return prev

        secondHalfStartingNode = slowPointer.next
        lastNode = reverseLinkedList(secondHalfStartingNode)

        maxTwinSum, firstHalfNode, reversedSecondHalfNode = 0, head, lastNode
        while reversedSecondHalfNode:
            maxTwinSum = max(maxTwinSum, firstHalfNode.val + reversedSecondHalfNode.val)
            firstHalfNode = firstHalfNode.next
            reversedSecondHalfNode = reversedSecondHalfNode.next

        # back to normal
        reverseLinkedList(lastNode)

        return maxTwinSum

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        left, right, maxTwinSum = head, prev, 0
        while right:
            maxTwinSum = max(maxTwinSum, left.val + right.val)
            left = left.next
            right = right.next

        prev, curr = None, prev
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        return maxTwinSum