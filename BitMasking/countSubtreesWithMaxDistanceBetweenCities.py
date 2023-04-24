# Wrong idea
# class Solution:
#     def countSubgraphsForEachDiameter(self, n: int, edges):
#         adjList = [[] for _ in range(n)]
#         for u, v in edges:
#             adjList[u-1].append(v-1)
#             adjList[v-1].append(u-1)

#         # root = None
#         # for node in range(n):
#         #     if len(adjList[node])==1:
#         #         root = node 
#         #         break
#         root = next(node for node in range(n) if len(adjList[node])==1)


#         setOfSubtreeBitmasks = set()

#         # def subsetEnumeration(bitmask):
#         #     subsetMask = bitmask
#         #     while subsetMask:
#         #         setOfSubtreeBitmasks.add(subsetMask)
#         #         subsetMask = (subsetMask-1) & bitmask

#         def getMSB(bitmask):
#             msb = 0
#             while bitmask:
#                 msb += 1
#                 bitmask >>= 1
#             return 1<<(msb-1)

#         def subArrayEnumeration(bitmask):
#             while bitmask:
#                 subArrayMask = bitmask
#                 while subArrayMask:
#                     setOfSubtreeBitmasks.add(subArrayMask)
#                     subArrayMask = (subArrayMask-1) & subArrayMask

#                 bitmask &= ~(1<<getMSB(bitmask))


#         def dfs(bitmaskOfVisitedNodes, node):
#             bitmaskOfVisitedNodes |= (1<<node)
#             neighFound = False
#             for neigh in adjList[node]:
#                 if not ((1<<neigh) & bitmaskOfVisitedNodes):
#                     neighFound = True
#                     dfs(bitmaskOfVisitedNodes, neigh)
            
#             if not neighFound:
#                 # subsetEnumeration(bitmaskOfVisitedNodes)
#                 subArrayEnumeration(bitmaskOfVisitedNodes)

#             bitmaskOfVisitedNodes &= ~(1<<node)

#         dfs(0, root)

#         distanceArr = [0]*(n+1)

#         for bitmask in setOfSubtreeBitmasks:
#             count = 0
#             while bitmask:
#                 if bitmask&1: count+=1
#                 bitmask >>= 1
#             distanceArr[count] += 1

#             # distanceArr[bin(bitmask).bit_count()] += 1

#         return distanceArr[2:]



class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges):
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u-1].append(v-1)
            adjList[v-1].append(u-1)


        def dfs(bitmask, node, maxDiameterInSubTree, visitedNodesBitMask):
            maxDiameterOfChild = 0
            visitedNodesBitMask[0] |= (1<<node)
            for neigh in adjList[node]:
                if (1<<neigh) & bitmask:
                    diameterOfChild = dfs(bitmask & ~(1<<node), neigh, maxDiameterInSubTree, visitedNodesBitMask)
                    maxDiameterInSubTree[0] = max(maxDiameterInSubTree[0], diameterOfChild+maxDiameterOfChild)
                    maxDiameterOfChild = max(maxDiameterOfChild, diameterOfChild)
            return maxDiameterOfChild+1

        def getAnySetNodeNum(i):
            node = 0
            while i and not(i&1):
                node += 1
                i >>= 1
            return node

        ans = [0] * (n - 1)
        for i in range(1, 2**n):
            maxDiameterInSubTree, visitedNodesBitMask = [0], [0]
            dfs(i, getAnySetNodeNum(i), maxDiameterInSubTree, visitedNodesBitMask)
            if visitedNodesBitMask[0]==i and maxDiameterInSubTree[0]>0:
                ans[maxDiameterInSubTree[0]-1] += 1
        return ans