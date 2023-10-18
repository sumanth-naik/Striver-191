# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(head):
            prev, node = None, head
            while node:
                prev, node.next, node = node, prev, node.next
            return prev

        def getLength(head):
            node, length = head, 0
            while node:
                node = node.next
                length += 1
            return length
        
        len1, len2 = getLength(l1), getLength(l2)
        if len1<len2: 
            len1, len2, l1, l2 = len2, len1, l2, l1
        
        addedListHead, addedListPrev, l1Node, l2Node = None, None, l1, l2
        while len1>0:
            node = ListNode()
            if len1>len2:
                len1 -= 1
                node.val = l1Node.val
                l1Node = l1Node.next
            else:
                len1 -= 1
                len2 -= 1
                node.val = l1Node.val + l2Node.val
                l1Node, l2Node = l1Node.next, l2Node.next
            if addedListHead is None:
                addedListHead = node
            else:
                addedListPrev.next = node
            addedListPrev = node

        reversedAddedListHead = reverse(addedListHead)
        node, lastNode, carry = reversedAddedListHead, None, 0
        while node:
            summation = node.val + carry
            carry, node.val = summation//10, summation%10 
            lastNode = node
            node = node.next

        if carry: lastNode.next = ListNode(carry)
        return reverse(reversedAddedListHead)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def addToStack(stack, node):
            while node:
                stack.append(node.val)
                node = node.next

        s1, s2 = [], []        
        addToStack(s1, l1)
        addToStack(s2, l2)

        addedListNext, carry = None, 0
        while s1 or s2 or carry:
            summation = carry + (0 if not s1 else s1.pop()) + (0 if not s2 else s2.pop())
            node, carry = ListNode(summation%10), summation//10
            node.next, addedListNext = addedListNext, node 

        return addedListNext
