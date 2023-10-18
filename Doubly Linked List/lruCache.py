class DoublyLinkedListNode:
    def __init__(self, key = -1, val = -1, prev = None, next = None) -> None:
        self.prev = prev
        self.next = next
        self.val = val
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyToNodeMap = {}

        self.head = DoublyLinkedListNode()
        self.tail = DoublyLinkedListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def __addToList__(self, key, val):
        node = DoublyLinkedListNode(key, val, self.head, self.head.next)
        self.head.next.prev, self.head.next= node, node
        return node

    def __removeFromList__(self, node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode
        return node

    def __evictFromList__(self):
        return self.__removeFromList__(self.tail.prev)

    def get(self, key: int) -> int:
        if key not in self.keyToNodeMap: return -1
        self.keyToNodeMap[key] = self.__addToList__(key, self.__removeFromList__(self.keyToNodeMap[key]).val)
        return self.keyToNodeMap[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNodeMap:
            self.__removeFromList__(self.keyToNodeMap[key])    
        self.keyToNodeMap[key] = self.__addToList__(key, value)
        if len(self.keyToNodeMap)>self.capacity:
            del self.keyToNodeMap[self.__evictFromList__().key]
            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)