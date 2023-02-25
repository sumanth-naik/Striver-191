class Solution:
    def sumOfDistancesInTree(self, n: int, edges):
        adjList = [[] for _ in range(n)]
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        subTreeSum = [0 for _ in range(n)]
        # does not include node itself
        numNodesInSubTree = [0 for _ in range(n)]

        def populateSubTreeSumAndNumNodesInSubtree(node, parent):
            for neigh in adjList[node]:
                if neigh!=parent:
                    populateSubTreeSumAndNumNodesInSubtree(neigh, node)
                    numNodesInSubTree[node] += (numNodesInSubTree[neigh] + 1)
                    subTreeSum[node] += (subTreeSum[neigh] + numNodesInSubTree[neigh] + 1)

        populateSubTreeSumAndNumNodesInSubtree(0, -1)

        sumOfDistancesArr = [0 for _ in range(n)]
        def populateSumOfDistances(node, parent, distanceContributedByParentSubTreeAndSiblingsSubTree):
            sumOfDistancesArr[node] = subTreeSum[node] + distanceContributedByParentSubTreeAndSiblingsSubTree
            for neigh in adjList[node]:
                if neigh!=parent:
                    subTreeSumContributedByNeigh = (subTreeSum[neigh] + numNodesInSubTree[neigh] + 1)
                    numNodesContributedByNeigh = (numNodesInSubTree[neigh] + 1)
                    distanceContributedBySibingsOfNeigh = (subTreeSum[node] - subTreeSumContributedByNeigh + numNodesInSubTree[node] - numNodesContributedByNeigh)
                    distanceContributedByNode = 1
                    distanceContributedByParentsOfNode = distanceContributedByParentSubTreeAndSiblingsSubTree + (n - numNodesInSubTree[node] - 1)
                    populateSumOfDistances(neigh, node, distanceContributedBySibingsOfNeigh + distanceContributedByNode + distanceContributedByParentsOfNode)
        
        populateSumOfDistances(0, -1, 0)
        return sumOfDistancesArr 
    

class Solution:
    def sumOfDistancesInTree(self, n: int, edges):
        adjList = [[] for _ in range(n)]
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        subTreeSum = [0 for _ in range(n)]
        # includes node itself
        numNodesInSubTree = [0 for _ in range(n)]

        def populateSubTreeSumAndNumNodesInSubtree(node, parent):
            for neigh in adjList[node]:
                if neigh!=parent:
                    populateSubTreeSumAndNumNodesInSubtree(neigh, node)
                    numNodesInSubTree[node] += (numNodesInSubTree[neigh])
                    subTreeSum[node] += (subTreeSum[neigh] + numNodesInSubTree[neigh])
            numNodesInSubTree[node] += 1

        populateSubTreeSumAndNumNodesInSubtree(0, -1)

        sumOfDistancesArr = [0 for _ in range(n)]
        sumOfDistancesArr[0] = subTreeSum[0]
        def populateSumOfDistances(node, parent):
            for neigh in adjList[node]:
                if neigh!=parent:
                    sumOfDistancesArr[neigh] = sumOfDistancesArr[node] - numNodesInSubTree[neigh] + (n - numNodesInSubTree[neigh]) 
                    populateSumOfDistances(neigh, node)
        
        populateSumOfDistances(0, -1)
        return sumOfDistancesArr 