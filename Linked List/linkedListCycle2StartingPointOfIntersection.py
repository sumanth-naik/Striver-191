def detectCycle(head):
    if not head: return None
    slowPointer = head
    fastPointer = head.next
    while fastPointer and fastPointer.next and fastPointer!=slowPointer:
        fastPointer = fastPointer.next.next
        slowPointer = slowPointer.next

    if not fastPointer or not fastPointer.next:
        return None
    slowPointer = head
    fastPointer = fastPointer.next
    while fastPointer!=slowPointer:
        fastPointer = fastPointer.next
        slowPointer = slowPointer.next
    return fastPointer