# Key Idea: In order traversal can be done by recursion. What is recursion? A stack.

# Property: The values that BST Iterator gives are sorted

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
