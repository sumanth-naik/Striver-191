class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        

class Codec:

    def serialize(self, root):
        serializedString = ""
        if not root:
            return serializedString

        levelNodesList = [root]
        while levelNodesList:
            nextLevelNodesList = []
            for node in levelNodesList:
                if not node:
                    serializedString +='#,'
                else:
                    nextLevelNodesList.append(node.left)
                    nextLevelNodesList.append(node.right)
                    serializedString += (str(node.val)+',')
            levelNodesList = nextLevelNodesList
        return serializedString[0:-1]

   

    def deserialize(self, data):

        if data=='':
            return None

        nodesValuesList = data.split(',')
        
        root = TreeNode(nodesValuesList[0])
        prevLevelNodes = [root]
        numCurrentLevelNodes, indexInNodesValuesList = 2, 1
        while indexInNodesValuesList<len(nodesValuesList):
            numNextLevelNodes = 0
            parentIndex = 0
            currentLevelNodes = []
            while numCurrentLevelNodes:
                for child in ['left', 'right']:
                    nodeVal = nodesValuesList[indexInNodesValuesList]
                    
                    if nodeVal !='#':
                        node = TreeNode(nodeVal)
                        numNextLevelNodes += 2
                        if child=='left':
                            prevLevelNodes[parentIndex].left = node
                        else:
                            prevLevelNodes[parentIndex].right = node
                        currentLevelNodes.append(node)
                    indexInNodesValuesList += 1                    
                    
                parentIndex += 1            
                numCurrentLevelNodes -= 2
            prevLevelNodes = currentLevelNodes
            numCurrentLevelNodes = numNextLevelNodes
        return root



        
class Codec:

    def serialize(self, root):
        serializeArr = []
        def preOrder(node):
            if not node:
                serializeArr.append('#')
                return
            serializeArr.append(str(node.val))
            preOrder(node.left)
            preOrder(node.right)
        preOrder(root)
        return ' '.join(serializeArr)

   

    def deserialize(self, data):
        nodeValsIter = iter(data.split())
        def preOrder():
            nodeVal = next(nodeValsIter)
            if nodeVal=='#':
                return None
            node = TreeNode(nodeVal)
            node.left = preOrder()
            node.right = preOrder()
            return node
        return preOrder()
            
