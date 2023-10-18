# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = right = curr = head
        count = 1
        while curr:
            if count<k:
                left = left.next
            elif count>k:
                right = right.next
            curr = curr.next
            count += 1
        left.val, right.val = right.val, left.val
        return head

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = right = head
        for _ in range(k-1): 
            left = left.next
        temp = left.next
        while temp: 
            right = right.next
            temp = temp.next
        left.val, right.val = right.val, left.val
        return head


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(-1, head)
        pre_left = pre_right = dummy
        left = right = head
        
        for _ in range(k-1):
            pre_left, left = left, left.next
        
        null_checker = left.next
        while null_checker:
            pre_right, right, null_checker = right, right.next, null_checker.next

        pre_left.next, pre_right.next = right, left
        left.next, right.next = right.next, left.next
        return dummy.next
