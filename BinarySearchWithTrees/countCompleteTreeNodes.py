class Solution:
    def countNodes(self, root) -> int:
        if root==None: return 0
        height = getHeight(root)
        numLeafNodes = pow(2, height)
        left = 1
        right = numLeafNodes
        while(left<right):
            mid = (left+right+1)//2
            if nThNodeExists(root, numLeafNodes, mid):
                left = mid
            else:
                right = mid-1
        return pow(2,height)-1 + left
        
        
def nThNodeExists(node, numLeafNodes, n):
    if n==1 and numLeafNodes==2:
        return node.left!=None
    if n==2 and numLeafNodes==2:
        return node.right!=None
    if n<=numLeafNodes//2:
        return nThNodeExists(node.left, numLeafNodes//2, n)
    else:
        return nThNodeExists(node.right, numLeafNodes//2, n-numLeafNodes//2)

def getHeight(node):
    if node.left==None:
        return 0
    return 1+getHeight(node.left)

