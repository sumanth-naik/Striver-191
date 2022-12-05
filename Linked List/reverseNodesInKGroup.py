



def reverseKGroup(head, k):

    node  = head
    numNode = 1
    prevReversedTail = None
    overAllHead = None
    nodeToStartReversalFrom = head
    
    while node:
        nextNode = node.next

        if numNode%k==0:
            currReversedHead = None
            currReversedTail = None
            
            #reverse k nodes from nodeToStartReveralFrom
            currReversedTail = nodeToStartReversalFrom
            tempNodeForReversal = nodeToStartReversalFrom
            prevNode = None
            while tempNodeForReversal!=nextNode:
                nextNodeInReversal = tempNodeForReversal.next
                tempNodeForReversal.next = prevNode
                prevNode = tempNodeForReversal
                tempNodeForReversal = nextNodeInReversal
            currReversedHead = prevNode

            if prevReversedTail:
                prevReversedTail.next = currReversedHead
            if not overAllHead:
                overAllHead = currReversedHead
            prevReversedTail = currReversedTail
            nodeToStartReversalFrom = nextNode

        node = nextNode
        numNode += 1
             
    if prevReversedTail:
        prevReversedTail.next = nodeToStartReversalFrom

    return overAllHead