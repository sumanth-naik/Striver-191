# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def joinBySorting(node1, node2):
            if not node1: return node2
            if not node2: return node1

            head = prev = None
            temp1, temp2 = node1, node2

            while temp1 and temp2:
                if temp1.val<temp2.val:
                    if prev: 
                        prev.next, prev = temp1, temp1
                    else: 
                        head = prev = temp1
                    temp1.next, temp1 = None, temp1.next
                else:
                    if prev: 
                        prev.next, prev = temp2, temp2
                    else: 
                        head = prev = temp2
                    temp2.next, temp2 = None, temp2.next

            if temp1:
                prev.next = temp1
            if temp2:
                prev.next = temp2
            
            return head


        def merge(node, length):
            if not node: return None
            if length==1: return node
            
            temp = node
            for _ in range(max((length//2) -1, 0)):
                temp = temp.next
            
            node1 = merge(temp.next, length-(length//2))
            temp.next = None
            node2 = merge(node, length//2)

            return joinBySorting(node1, node2)

        node, length = head, 0
        while node:
            length += 1
            node = node.next
            
        return merge(head, length)


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def mergeHelper(head1, head2):
            if not head1 or not head2: return head1 or head2

            dummy = prev = ListNode()
            temp1, temp2 = head1, head2
            while temp1 and temp2:
                if temp1.val<temp2.val:
                    prev.next, prev = temp1, temp1
                    temp1 = temp1.next
                else:
                    prev.next, prev = temp2, temp2
                    temp2 = temp2.next
                
            prev.next = temp1 or temp2
            return dummy.next

        def merge(head):
            if not head or not head.next: return head

            fast, slow = head.next, head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            mid, slow.next = slow.next, None
            
            return mergeHelper(merge(head), merge(mid))

        return merge(head)