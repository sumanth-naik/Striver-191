# Key Idea: Use bit encoding to traverse tree path

class Solution:
    def countNodes(self, root) -> int:
        if not root: return 0

        node, height = root, 0 # bottom layer is level 0
        while node.left:
            node, height = node.left, height + 1
        
        def nodeExists(path):
            node = root
            for char in path:
                if char=="0": node = node.left
                else: node = node.right
            return node

        low, high = 1<<height, (1<<(height+1)) - 1 
        while low<high:
            mid = (low+high+1)//2
            if nodeExists(bin(mid)[3:]):
                low = mid
            else:
                high = mid - 1
        return low
            

# Key Idea 1: See root and root's right child's height. If root's right's height is one less, missing nodes start on right. So add all the nodes on root's left side.
# Key Idea 2: If not, add all the nodes on root's right child and recurse on root's left subtree

# Note 1: Clever use of setting height as -1 when node is None instead of 0 when node.left is None. This avoids NPE when there is no root.right

class Solution:
    def countNodes(self, root) -> int:
        if not root: return 0

        def getHeight(node): # Note 1
            return -1 if node is None else 1 + getHeight(node.left)
        
        rootHeight, rightHeight = getHeight(root), getHeight(root.right)
        return (1<<rootHeight) + self.countNodes(root.right) if rootHeight==1+rightHeight \
                else (1<<(rootHeight-1)) + self.countNodes(root.left)
        