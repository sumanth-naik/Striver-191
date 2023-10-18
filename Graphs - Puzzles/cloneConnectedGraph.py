# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if not node: return node
        realGraphVisitedSet = set()
        cloneGraphValToNodeMap = {}

        def dfs(realGraphNode):
            print(realGraphNode, realGraphNode.val)
            realGraphVisitedSet.add(realGraphNode)
            clonedNode = Node(realGraphNode.val)
            cloneGraphValToNodeMap[clonedNode.val] = clonedNode
            for neigh in realGraphNode.neighbors:
                if neigh not in realGraphVisitedSet:
                    clonedNode.neighbors.append(dfs(neigh))
                else:
                    clonedNode.neighbors.append(cloneGraphValToNodeMap[neigh.val])
            return clonedNode
        return dfs(node)