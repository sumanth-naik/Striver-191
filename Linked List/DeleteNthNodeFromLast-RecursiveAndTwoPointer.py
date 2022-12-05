def removeNthFromEnd(head, n: int):
    
    if recursiveDeleteNthNode(head,n)!=0:
        head = head.next
    return head
    
    
    
    
def recursiveDeleteNthNode(node, n):
    if not node:
        return 1
    numIndexFromReverse = recursiveDeleteNthNode(node.next,n)
    if numIndexFromReverse==n+1:
        node.next = node.next.next
        return 0
    return 0 if numIndexFromReverse==0 else numIndexFromReverse+1
    





def removeNthFromEnd2(head, n: int):
    return recursiveDeleteNthNode2(None, head, n)[0]
    
      
    
def recursiveDeleteNthNode2(prevNode, currNode, n):
    if not currNode:
        return None,1
    
    _,numIndexFromReverse = recursiveDeleteNthNode2(currNode,currNode.next,n)
    if numIndexFromReverse==n:
        if prevNode:
            prevNode.next = currNode.next
        else:
            return currNode.next,0
    return currNode,numIndexFromReverse+1


def removeNthFromEndTwoPointer(head, n: int):
    
    right = head
    for _ in range(n):
        right = right.next
    if not right:
        return head.next
    left = head
    while right:
        right = right.next
        left = left.next
    left.next = left.next.next
    return head
    
    