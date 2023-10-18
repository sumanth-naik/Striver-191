# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallerNodesHead = largerOrEqualNodesHead = None
        smallerNode = largerOrEqualNode = None
        node = head
        while node:
            newNode = ListNode(node.val)
            if node.val<x: 
                if not smallerNodesHead: smallerNodesHead = newNode
                else: smallerNode.next = newNode
                smallerNode = newNode
            else:
                if not largerOrEqualNodesHead: largerOrEqualNodesHead = newNode
                else: largerOrEqualNode.next = newNode
                largerOrEqualNode = newNode
            node = node.next
        if smallerNode: smallerNode.next = largerOrEqualNodesHead
        return smallerNodesHead if smallerNodesHead else largerOrEqualNodesHead

 
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallerNodesHead = largerOrEqualNodesHead = None
        smallerNode = largerOrEqualNode = None
        node = head
        while node:
            if node.val<x: 
                if not smallerNodesHead: smallerNodesHead = node
                else: smallerNode.next = node
                smallerNode = node
            else:
                if not largerOrEqualNodesHead: largerOrEqualNodesHead = node
                else: largerOrEqualNode.next = node
                largerOrEqualNode = node
            node = node.next
        if largerOrEqualNode: largerOrEqualNode.next = None
        if smallerNode: smallerNode.next = largerOrEqualNodesHead
        return smallerNodesHead if smallerNodesHead else largerOrEqualNodesHead


 
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallerNodesDummyHead, largerOrEqualNodesDummyHead = ListNode(), ListNode()
        smallerNode, largerOrEqualNode = smallerNodesDummyHead, largerOrEqualNodesDummyHead
        while head: 
            if head.val<x: 
                smallerNode.next = head
                smallerNode = head
            else:
                largerOrEqualNode.next = head
                largerOrEqualNode = head
            head = head.next
        largerOrEqualNode.next = None
        smallerNode.next = largerOrEqualNodesDummyHead.next
        return smallerNodesDummyHead.next