
class DoublyLinkedList:
    def __init__(self, key, val, counterValue = 0, left=None, right=None):
        self.key = key
        self.val = val
        self.counterValue = counterValue
        self.left = left
        self.right = right


class LFUCache:

    def __init__(self, capacity: int):
        self.keyToNodeMap = {}
        self.counterToLinkedListHeadMap = {}
        self.counterToLinkedListTailMap = {}
        self.capacity = capacity
        self.capacityUsedSoFar = 0
        self.minCounterValue = 1


    def removeNodeFromPreviousCounterValue(self, node, prevCounterValue):
        if node.left:
            node.left.right = node.right
        else:
            self.counterToLinkedListHeadMap[prevCounterValue] = node.right
        if node.right:
            node.right.left = node.left
        else:
            self.counterToLinkedListTailMap[prevCounterValue] = node.left

        if self.counterToLinkedListHeadMap[prevCounterValue] is None:
            del self.counterToLinkedListHeadMap[prevCounterValue]
            if self.minCounterValue==prevCounterValue:
                self.minCounterValue += 1

    def addNodetoNewCounterValue(self, node, newCounterValue):
        node.counterValue = newCounterValue
        node.left = None
        if not newCounterValue in self.counterToLinkedListHeadMap:
            node.right = None
            self.counterToLinkedListHeadMap[newCounterValue] = node
            self.counterToLinkedListTailMap[newCounterValue] = node
        else:
            node.right = self.counterToLinkedListHeadMap[newCounterValue]
            self.counterToLinkedListHeadMap[newCounterValue].left = node
            self.counterToLinkedListHeadMap[newCounterValue] = node


    def updateLinkedLists(self, node):
        self.removeNodeFromPreviousCounterValue(node, node.counterValue)
        self.addNodetoNewCounterValue(node, node.counterValue+1)
        

    def get(self, key: int) -> int:
        if not key in self.keyToNodeMap:
            return -1
        node = self.keyToNodeMap[key]
        self.updateLinkedLists(node)
        return node.val

        

    def put(self, key: int, value: int):
        # update
        if key in self.keyToNodeMap:
            node = self.keyToNodeMap[key]
            node.val = value
            self.updateLinkedLists(node)
        # new
        else:
            # not full
            if self.capacityUsedSoFar!=self.capacity:
                self.capacityUsedSoFar += 1
            # full
            else:
                evictedNode = self.counterToLinkedListTailMap[self.minCounterValue]
                self.removeNodeFromPreviousCounterValue(evictedNode, evictedNode.counterValue)
                del self.keyToNodeMap[evictedNode.key]
            # not full or full
            node = DoublyLinkedList(key, value)
            self.keyToNodeMap[key] = node
            self.addNodetoNewCounterValue(node, 1)            
            self.minCounterValue = 1
