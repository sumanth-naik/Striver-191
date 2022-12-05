def addTwoNumbers(l1, l2):

    head = None
    prevNode = None
    overflow = 0
    node1 = l1
    node2 = l2
    num1, num2 = 0,0
    while node1 or node2:

        if not node1:
            num1 = 0
        else:
            num1 = node1.val

        if not node2:
            num2 = 0
        else:
            num2 = node2.val

        currSum = num1 + num2 + overflow

        if currSum>9:
            overflow = 1
            currSum = currSum - 10
        else:
            overflow = 0

        currNode = ListNode(currSum)
        if not head:
            head = currNode
        else:
            prevNode.next = currNode
        prevNode = currNode

        if node1:
            node1 = node1.next
        if node2:
            node2 = node2.next
    if overflow:
        prevNode.next = ListNode(1)
    return head



def addTwoNumbers(l1, l2):

    currNode = dummy = ListNode(-1)
    carry = 0
    node1 = l1
    node2 = l2
    while node1 or node2 or carry:

        if node1:
            carry += node1.val
            node1 = node1.next

        if node2:
            carry += node2.val
            node2 = node2.next
            
        currNode.next = ListNode(carry%10)
        currNode = currNode.next
        carry =carry//10

    return dummy.next