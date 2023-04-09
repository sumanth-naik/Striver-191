# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq
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

