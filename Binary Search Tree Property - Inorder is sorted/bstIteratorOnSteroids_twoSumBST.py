# Key Idea: Classic two-pointer two-sum approach along with BST Iterator from left to right and right to left

# Property: BST is already sorted

class TreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None


def pairSumBST(root, k):

    def nextRight(leftToRightStack):
        if leftToRightStack:
            nextRightElem = leftToRightStack.pop()
            addAllLeft(nextRightElem.right, leftToRightStack)
            return nextRightElem

    def addAllLeft(node, leftToRightStack):
        while node:
            leftToRightStack.append(node)
            node = node.left

    def nextLeft(rightToLeftStack):
        if rightToLeftStack:
            nextLeftElem = rightToLeftStack.pop()
            addAllRight(nextLeftElem.left, rightToLeftStack)
            return nextLeftElem

    def addAllRight(node, rightToLeftStack):
        while node:
            rightToLeftStack.append(node)
            node = node.right

    leftToRightStack, rightToLeftStack = [], []
    addAllLeft(root, leftToRightStack)
    addAllRight(root, rightToLeftStack)
    
    leftToRightIteratorElem = nextRight(leftToRightStack)
    rightToLeftIteratorElem = nextLeft(rightToLeftStack)

    while leftToRightIteratorElem and rightToLeftIteratorElem and leftToRightIteratorElem.data<rightToLeftIteratorElem.data:
        currSum = leftToRightIteratorElem.data + rightToLeftIteratorElem.data
        if currSum<k:
            leftToRightIteratorElem = nextRight(leftToRightStack)
        elif currSum>k:
            rightToLeftIteratorElem = nextLeft(rightToLeftStack)
        else:
            return True 
    return False


