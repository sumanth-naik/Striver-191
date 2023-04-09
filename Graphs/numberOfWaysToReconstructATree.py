from collections import defaultdict
class Solution:
    def checkWays(self, pairs):
        adjSet = defaultdict(set)
        for pair in pairs:
            adjSet[pair[0]].add(pair[1])
            adjSet[pair[1]].add(pair[0])

        def canConstructTreeDfs(nodes):
            root, multipleRootsFound = None, False
            for node in nodes:
                if len(adjSet[node])==len(nodes)-1:
                    if root:
                        multipleRootsFound = True
                        break
                    root = node

            if not root: return 0

            for childNode in adjSet[root]: adjSet[childNode].remove(root)

            seen = set()
            def getComponentNodes(node, visited):
                visited.add(node)
                seen.add(node)
                for node in adjSet[node]:
                    if node not in visited:
                        getComponentNodes(node, visited)

            twoFound = False
            for childNode in adjSet[root]:
                if not childNode in seen:
                    childComponentSet = set()
                    getComponentNodes(childNode, childComponentSet)
                    childComponentDfsResult = canConstructTreeDfs(childComponentSet)
                    if childComponentDfsResult==0: return 0
                    if childComponentDfsResult==2: twoFound = True
            
            if twoFound: return 2
            return 2 if multipleRootsFound else 1
        return canConstructTreeDfs(adjSet.keys())
            


