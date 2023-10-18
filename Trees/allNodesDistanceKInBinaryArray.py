# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        distMap = defaultdict(int)

        def dfs(node, dist):
            if not node: return

            if node==target:
                dist = 0

            nonlocal distMap
            if dist!=None:
                distMap[node.val] = dist
                dfs(node.left, dist+1)
                dfs(node.right, dist+1)
            else:
                dfs(node.left, None)
                dfs(node.right, None)
                if node.left is not None and node.left.val in distMap:
                    distMap[node.val] = distMap[node.left.val] + 1
                    dfs(node.right, distMap[node.val]+1)
                elif node.right is not None and node.right.val in distMap:
                    distMap[node.val] = distMap[node.right.val] + 1
                    dfs(node.left, distMap[node.val]+1)

        dfs(root, None)
        return [node for node in distMap.keys() if distMap[node]==k]
    

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        adjList = defaultdict(set)

        def dfsToPopulateGraph(node, parent):
            if not node: return
            nonlocal adjList
            if parent is not None:
                adjList[node.val].add(parent.val)
                adjList[parent.val].add(node.val)
            
            dfsToPopulateGraph(node.left, node)
            dfsToPopulateGraph(node.right, node)
        
        dfsToPopulateGraph(root, None)
        
        levelArr = [target.val]
        while levelArr:
            if k==0: return levelArr
            nextLevelArr = []
            for nodeInLevel in levelArr:
                for neigh in adjList[nodeInLevel]:
                    nextLevelArr.append(neigh)
                    adjList[neigh].discard(nodeInLevel)
            levelArr = nextLevelArr
            k-=1
        return []
    

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        adjList = defaultdict(set)

        def dfsToPopulateGraph(node, parent):
            if not node: return
            nonlocal adjList
            if parent is not None:
                adjList[node.val].add(parent.val)
                adjList[parent.val].add(node.val)
            
            dfsToPopulateGraph(node.left, node)
            dfsToPopulateGraph(node.right, node)
        
        dfsToPopulateGraph(root, None)
        
        kDistNodes, visited = [], set()
        def dfs(node, dist):
            nonlocal kDistNodes, visited 
            visited.add(node)
            if dist==k: kDistNodes.append(node)
            for neigh in adjList[node]:
                if neigh not in visited:
                    dfs(neigh, dist+1)
        
        dfs(target.val, 0)
        return kDistNodes