
def rotateRight(head, k):
    n = 0
    tail = head
    while tail.next:
        tail = tail.next
        n += 1
    k = k%n
    if k==0: return head
    k = n-k
    node = head
    while k!=1:
        k -= 1
        node = node.next    
        
    node.next, head, tail.next = None, node.next, head

    return head