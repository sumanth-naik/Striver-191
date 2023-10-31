# Key Idea: Implement the __lt__ magic method

class Solution:
    ListNode.__lt__ = lambda self, other: self.val<other.val    
    def mergeKLists(self, lists):
        minHeap = [head for head in lists if head]
        heapify(minHeap)
        head = prev = ListNode(0)
        while minHeap:
            node = heappop(minHeap)
            prev.next, prev = node, node
            if node.next: heappush(minHeap, node.next)
        return head.next



# If we cant write the __lt__ magic method, use listNumberToListNodeMap and populate (node.val, listNum) in heap
class Solution:
    def mergeKLists(self, lists):
        minHeap, listNumberToListNodeMap = [], {}

        for listNum, head in enumerate(lists):
            if head: 
                listNumberToListNodeMap[listNum] = head
                heapq.heappush(minHeap, (head.val, listNum))

        prevNode, headNode = None, None
        while minHeap:
            smallestElemVal, listNum = heapq.heappop(minHeap)
            node = ListNode(smallestElemVal)
            if not headNode: headNode = node
            if prevNode: prevNode.next = node
            if listNumberToListNodeMap[listNum].next:
                listNumberToListNodeMap[listNum] = listNumberToListNodeMap[listNum].next
                heapq.heappush(minHeap, (listNumberToListNodeMap[listNum].val, listNum))
            prevNode = node

        return headNode