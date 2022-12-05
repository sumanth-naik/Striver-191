class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def createListWithoutRandom(node, nodesMap):
    newNode = None
    if not node.next:
        newNode = Node(node.val)
    else:
        newNode = Node(node.val, createListWithoutRandom(node.next, nodesMap))
    nodesMap[node] = newNode
    return newNode

def addRandomtoCopiedList(head, nodesMap):
    node = head
    while node:
        if node.random:
            nodesMap[node].random = nodesMap[node.random]
        node = node.next



def copyRandomList(head):
    nodesMap = {}
    newHead = createListWithoutRandom(head, nodesMap)
    addRandomtoCopiedList(head, nodesMap)
    return newHead







def copyRandomListWithoutMap(head):
    # create copy of each node and point original node's next as copied node and 
    # that copied node's next as original node's next
    node = head
    while node:
        newNode = Node(node.val, node.next)
        node.next = newNode
        node = node.next.next
    
    # add random pointers for each
    node = head
    while node:
        if node.random:
            node.next.random = node.random.next
        node = node.next.next

    # update next pointers for both newList and oldList. Update copyNode's next only if realNext exists
    # find newHead
    node = head
    newHead = None
    while node:
        if not newHead:
            newHead = node.next
        realNext = node.next.next
        if realNext:
            node.next.next = realNext.next
        node.next = realNext
        node = node.next

    return newHead







