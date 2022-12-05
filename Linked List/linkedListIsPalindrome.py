           
            
def isPalindrome(head):
    if not head: return True
    
    # find mid
    slowPointer = head
    fastPointer = head.next
    while fastPointer and fastPointer.next:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next
        if fastPointer.next:
            fastPointer = fastPointer.next
    
    #reverse
    curr = slowPointer.next
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next


    reversedListNode = prev
    node = head
    
    #check palindrome
    isNotPalindrome = False
    while reversedListNode:
        if node.data != reversedListNode.data:
            isNotPalindrome = True
            break
        reversedListNode = reversedListNode.next
        node = node.next

    
    #undo reversing
    curr = prev
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    slowPointer.next = prev

    return not isNotPalindrome



    
    
    
  