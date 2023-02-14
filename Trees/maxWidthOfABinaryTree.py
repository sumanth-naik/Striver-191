
def traversal(node, minMaxTupleArr, height, indexInLevel):
    if node:
        if not len(minMaxTupleArr)>height:
            minMaxTupleArr.append([float('inf'), -float('inf')])
        minMaxTupleArr[height][0] = min(minMaxTupleArr[height][0], indexInLevel)
        minMaxTupleArr[height][1] = max(minMaxTupleArr[height][1], indexInLevel)
        traversal(node.left, minMaxTupleArr, height+1, 2*indexInLevel)
        traversal(node.right, minMaxTupleArr, height+1, 2*indexInLevel+1)

def maxWidthOfABinaryTree(root):
    minMaxTupleArr = []
    traversal(root, minMaxTupleArr, 0, 0)
    maxDiff = 0
    print(minMaxTupleArr)
    for left, right in minMaxTupleArr:
        maxDiff = max(maxDiff, right-left+1)
        print(maxDiff)
    return maxDiff



def maxWidthBFS(root):
    levelList = [(1, root)]
    maxWidth = 1
    while levelList:
        maxWidth = max(maxWidth, levelList[-1][0] - levelList[0][0]+1)
        nextLevelList = []
        for nodeIndex, node in levelList:
            if node.left:
                nextLevelList.append((2*nodeIndex, node.left))
            if node.right:
                nextLevelList.append((2*nodeIndex+1, node.right))
        levelList = nextLevelList
    return maxWidth