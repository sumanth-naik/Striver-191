class TreeNode:
    def __init__(self, val=0, left=None, right=None, leftSubtreeCount=0,currNumCount=1,rightSubtreeCount=0):
        self.val = val
        self.left = left
        self.right = right
        self.leftSubtreeCount = leftSubtreeCount
        self.currNumCount = currNumCount
        self.rightSubtreeCount = rightSubtreeCount


class MedianFinder:

    def __init__(self):
        self.root = None
        self.totalCount = 0
        
    def addNode(self, newNodeNum, currNode):
        if newNodeNum>currNode.val:
            currNode.rightSubtreeCount += 1
            if not currNode.right:
                currNode.right = TreeNode(newNodeNum)
            else:
                self.addNode(newNodeNum, currNode.right)
        elif newNodeNum<currNode.val:
            currNode.leftSubtreeCount += 1
            if not currNode.left:
                currNode.left = TreeNode(newNodeNum)
            else:
                self.addNode(newNodeNum, currNode.left)
        else:
            currNode.currNumCount += 1


    def addNum(self, num: int) -> None:
        self.totalCount += 1
        if not self.root:
            self.root = TreeNode(num)
        else:
            self.addNode(num, self.root)
    
    # 1 indexed search
    def findKthNum(self, k, node, numOfNumsSmallerThanNodeValWhichAreNotPresentInNodesSubtree = 0):
        totalSmallerNums = node.leftSubtreeCount + numOfNumsSmallerThanNodeValWhichAreNotPresentInNodesSubtree
        if totalSmallerNums<k<=totalSmallerNums+node.currNumCount:
            return node.val
        if totalSmallerNums>=k:
            return self.findKthNum(k, node.left, numOfNumsSmallerThanNodeValWhichAreNotPresentInNodesSubtree)
        else:
            return self.findKthNum(k, node.right, totalSmallerNums + node.currNumCount)

    def findMedian(self) -> float:
        mid = (int) (self.totalCount)//2
        if self.totalCount%2==0:
            return (self.findKthNum(mid, self.root) + self.findKthNum(mid+1, self.root))//2
        else:
            return self.findKthNum(mid+1, self.root)

    def preOrder(self, node):
        if not node:
            print("null")
        else:
            print(node.val, node.leftSubtreeCount, node.currNumCount, node.rightSubtreeCount)
            self.preOrder(node.left)
            self.preOrder(node.right)

            