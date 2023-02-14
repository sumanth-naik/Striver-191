def oddEvenLinkedList(head):
    node, oddTail, isOddList = head,  None, True
    evenHead = head.next if head else None
    while node:
        nextNode = node.next
        if nextNode:
            node.next = nextNode.next
        if isOddList:
            oddTail = node
        isOddList = not isOddList
        node = nextNode
    if oddTail:
        oddTail.next = evenHead
    return head
    