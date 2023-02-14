class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
    if not root:
        return []
    levelNodesList = [root]
    fromLeft = False
    zigzagLevelOrderList = [[root.val]]
    while levelNodesList:
        nextLevelNodesList = []
        zigzagLevel = []
        for i in range(len(levelNodesList)-1, -1, -1):
            node = levelNodesList[i]
            if fromLeft:
                if node.left:
                    nextLevelNodesList.append(node.left)
                    zigzagLevel.append(node.left.val)
                if node.right:
                    nextLevelNodesList.append(node.right)
                    zigzagLevel.append(node.right.val)
            else:
                if node.right:
                    nextLevelNodesList.append(node.right)
                    zigzagLevel.append(node.right.val)
                if node.left:
                    nextLevelNodesList.append(node.left)
                    zigzagLevel.append(node.left.val)


        fromLeft = not fromLeft
        levelNodesList = nextLevelNodesList
        if zigzagLevel:
            zigzagLevelOrderList.append(zigzagLevel)
    
    return zigzagLevelOrderList


    
def zigzagLevelOrder(root):
    if not root:
        return []
    levelNodesList = [root]
    fromLeft = False
    zigzagLevelOrderList = [[root.val]]
    while levelNodesList:
        nextLevelNodesList = []
        zigzagLevel = []
        for node in levelNodesList:
            if node.left:
                nextLevelNodesList.append(node.left)
                zigzagLevel.append(node.left.val)
            if node.right:
                nextLevelNodesList.append(node.right)
                zigzagLevel.append(node.right.val)

        if not fromLeft:
            zigzagLevel.reverse()

        fromLeft = not fromLeft
        levelNodesList = nextLevelNodesList
        if zigzagLevel:
            zigzagLevelOrderList.append(zigzagLevel)
    
    return zigzagLevelOrderList