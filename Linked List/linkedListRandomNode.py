# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head):
        self.head = head    
        self.k = 1   

    def getRandom(self) -> int:
        nodeValues = []
        currNode = self.head
        for _ in range(self.k):
            nodeValues.append(currNode.val)
            currNode = currNode.next
            if not currNode: break

        runningIndex = self.k
        while currNode:
            # replace with decreasing probability
            indexToReplace = random.randint(0, runningIndex)
            if indexToReplace<self.k:
                nodeValues[indexToReplace] = currNode.val
            runningIndex += 1
            currNode = currNode.next

        if self.k==1: return nodeValues[0]
        return nodeValues

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()