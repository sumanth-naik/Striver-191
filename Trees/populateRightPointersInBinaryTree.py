class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def populateRightPointersInBinaryTree(root):
    levelNodesList = [root]
    while levelNodesList:
        nextLevelNodesList = []
        for index in range(len(levelNodesList)-1):
            levelNodesList[index].right = levelNodesList[index+1]
            if levelNodesList[index].left:
                nextLevelNodesList.append(levelNodesList[index].left)
                nextLevelNodesList.append(levelNodesList[index].right)
        levelNodesList = nextLevelNodesList


def populateRightPointersInBinaryTreeOptimale(root):
    levelStart = root
    while levelStart:
        node = levelStart
        while node:
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
            node = node.next 
        levelStart = levelStart.left
