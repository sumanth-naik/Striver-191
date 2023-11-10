# Key Idea 1: Find maxDiameter of each subset using DFS + MaxHeap(Storing Greedy max)-ish algo. Add iff subset is a connected graph.
# Key Idea 2: Can use Bitmasking to optimise space.

# Note: Finding root for DFS step just finds out the LSB Mask and gets bit number. log(001000) -> 3

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges):
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u-1].append(v-1)
            adjList[v-1].append(u-1)

        def getMaxDiameter(nodesSubsetMask):

            def dfs(node):
                nonlocal maxDiameterInSubTree, visitedNodesBitMask
                maxDepthInChildren = 0
                visitedNodesBitMask |= (1<<node)
                for neigh in adjList[node]:
                    if (1<<neigh) & nodesSubsetMask and not ((1<<neigh)&visitedNodesBitMask):
                        depthOfChild = dfs(neigh)
                        maxDiameterInSubTree = max(maxDiameterInSubTree, depthOfChild+maxDepthInChildren)
                        maxDepthInChildren = max(maxDepthInChildren, depthOfChild)
                return maxDepthInChildren+1
        
            maxDiameterInSubTree, visitedNodesBitMask = 0, 0
            dfs(int(log(nodesSubsetMask & -nodesSubsetMask, 2))) # Note
            return maxDiameterInSubTree if visitedNodesBitMask==nodesSubsetMask else 0

        ans = [0]*n
        for nodesSubsetMask in range(1, 1<<n):
            ans[getMaxDiameter(nodesSubsetMask)] += 1
        return ans[1:]

