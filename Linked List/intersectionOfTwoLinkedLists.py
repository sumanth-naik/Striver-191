
def findIntersection(firstHead, secondHead):

    len1 = 0
    len2 = 0
    
    node1, node2 = firstHead, secondHead
    while(node1 or node2):
        if node1:
            len1 += 1
            node1 = node1.next
        if node2:
            len2 += 1
            node2 = node2.next

    diff = abs(len1-len2)

    if len1>len2:
        node1, node2 = firstHead, secondHead
    else:
        node2, node1 = firstHead, secondHead
    
    for _ in range(diff):
        node1 = node1.next

    for _ in range(min(len1,len2)):
        if node1==node2:
            return node1.val
        node1 = node1.next
        node2 = node2.next
    
    return -1
