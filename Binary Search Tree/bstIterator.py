class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.addToStack(root)

    def next(self) -> int:
        nextElem = self.stack.pop()
        self.addToStack(nextElem.right)
        return nextElem.val
        
    def addToStack(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self) -> bool:
        return len(self.stack)
