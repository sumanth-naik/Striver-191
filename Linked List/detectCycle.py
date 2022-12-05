
def detectCycle(head) :
    slowPointer = head
    fastPointer = head.next  
    while(slowPointer!=fastPointer and fastPointer):
        slowPointer = slowPointer.next
        if fastPointer.next:
            fastPointer = fastPointer.next.next
        else:
            return False
    if fastPointer:
        return True
    return False