class UnionFind:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def findParent(self, node):
        if self.parent[node]!=node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        parent1 = self.findParent(node1)
        parent2 = self.findParent(node2)
        if parent1!=parent2:
            if self.size[parent1]>self.size[parent2]:
                self.parent[parent2] = parent1
                self.size[parent1] += self.size[parent2]
            else:
                self.parent[parent1] = parent2
                self.size[parent2] += self.size[parent1]
    
    def belongsToSameComponent(self, node1, node2):
        return self.findParent(node1) == self.findParent(node2)


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges):
        # stores (index of edge, u, v, wt)
        indexEdgeAndWeightArr = [[i]+edge for i, edge in enumerate(edges)]
        indexEdgeAndWeightArr.sort(key = lambda x : x[-1])

        criticalEdges, pseudoCriticalEdges = [], []

        def krushkalsMST(indexEdgeAndWeightArr, unionFind, excludedIndex = None, mstWeight = 0):
            for edgeIndex, u, v, edgeWeight in indexEdgeAndWeightArr:
                if edgeIndex!=excludedIndex:
                    if not unionFind.belongsToSameComponent(u, v):
                        unionFind.union(u, v)
                        mstWeight += edgeWeight
            return mstWeight
        
        mstWeight = krushkalsMST(indexEdgeAndWeightArr, UnionFind(n))
        
        for index, u, v, edgeWeight in indexEdgeAndWeightArr:
            if krushkalsMST(indexEdgeAndWeightArr, UnionFind(n), index) != mstWeight:
                criticalEdges.append(index)
            else:
                # check if must included
                unionFind = UnionFind(n)
                unionFind.union(u, v)
                if krushkalsMST(indexEdgeAndWeightArr, unionFind, None, edgeWeight) == mstWeight:
                    pseudoCriticalEdges.append(index)
       
        return [criticalEdges, pseudoCriticalEdges]
    

# incomplete
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges):

        adjList = [[] for _ in range(n)]

        # stores (index of edge, u, v, wt)
        indexEdgeAndWeightArr = [[i]+edge for i, edge in enumerate(edges)]
        indexEdgeAndWeightArr.sort(key = lambda x : x[-1])

        unionFind, index = UnionFind(n), 0
        criticalEdges, pseudoCriticalEdges = [], []
        while index<len(edges):
            # not inclusive
            weightIsSameTillIndex = index
            parentsToAddableEdgeMap = {}
            while weightIsSameTillIndex<len(edges) and indexEdgeAndWeightArr[weightIsSameTillIndex][-1] == indexEdgeAndWeightArr[index][-1]:
                edgeIndex, u, v, edgeWeight = indexEdgeAndWeightArr[weightIsSameTillIndex]
                if not unionFind.belongsToSameComponent(u, v):
                    parent1 = unionFind.findParent(u)
                    parent2 = unionFind.findParent(v)
                    parents = (min(parent1, parent2), max(parent1, parent2))
                    if not parents in parentsToAddableEdgeMap:
                        parentsToAddableEdgeMap[parents] = []
                    parentsToAddableEdgeMap[parents].append(indexEdgeAndWeightArr[weightIsSameTillIndex])
                weightIsSameTillIndex += 1
            
            possibleCriticalEdges = []
            for parents in parentsToAddableEdgeMap.keys():
                if len(parentsToAddableEdgeMap[parents])==1:
                    possibleCriticalEdges.append(parentsToAddableEdgeMap[parents][0])
                else:
                    pseudoCriticalEdges.extend(addableEdge[0] for addableEdge in parentsToAddableEdgeMap[parents])

            possibleCriticalEdgesAdjList = [[] for _ in range(n)]
            for _, u, v, _ in possibleCriticalEdges:
                possibleCriticalEdgesAdjList[u].append(v)
                possibleCriticalEdgesAdjList[v].append(u)
                
            low, timeOfInsertion, time, bridges = [1e9 for _ in range(n)], [-1 for _ in range(n)], 1, set()
            def tarjansAlgo(node, parent):
                nonlocal low, timeOfInsertion, time, bridges
                timeOfInsertion[node] = time
                low[node] = time
                time += 1
                for neigh in possibleCriticalEdgesAdjList[node] + adjList[node]:
                    if neigh==parent:
                        continue
                    if timeOfInsertion[neigh]==-1:
                        tarjansAlgo(neigh, node)
                        if low[neigh]>timeOfInsertion[node]:
                            bridges.add((min(node, neigh), max(node, neigh)))
                    low[node] = min(low[node], low[neigh])
           
            for _, u, v, _ in possibleCriticalEdges:
                if (min(u,v), max(u,v)) not in bridges:
                    tarjansAlgo(u, -1)

            for edgeIndex, u, v, _ in possibleCriticalEdges:
                if (min(u,v), max(u,v)) in bridges:
                    criticalEdges.append(edgeIndex)
                else:
                    pseudoCriticalEdges.append(edgeIndex)

            for parents in parentsToAddableEdgeMap.keys():
                for _, u, v, _ in parentsToAddableEdgeMap[parents]:
                    adjList[u].append(v)
                    adjList[v].append(u)
                unionFind.union(parents[0], parents[1])

            index = weightIsSameTillIndex

        return [criticalEdges, pseudoCriticalEdges]

            

            

for elem in [[5, 8, 1], [ 5, 9, 1], [ 8, 9, 1], [ 3, 12, 1], [ 7, 13, 2], [ 4, 11, 2], [ 1, 6, 2], [ 8, 13, 2], [ 8, 10, 2], [ 5, 11, 3], [ 2, 7, 3], [ 5, 12, 3], [ 4, 12, 3], [ 9, 11, 3], [ 0, 10, 3], [ 4, 13, 3], [ 4, 5, 3], [ 11, 12, 3], [ 8, 11, 3]]:
    print(elem[0], elem[1], elem[2])



            


[[28, 5, 8, 1], [32, 5, 9, 1], [39, 8, 9, 1], [58, 3, 12, 1], [13, 7, 13, 2], [45, 4, 11, 2], [55, 1, 6, 2], [61, 8, 13, 2], [89, 8, 10, 2], [10, 5, 11, 3], [16, 2, 7, 3], [37, 5, 12, 3], [51, 4, 12, 3], [54, 9, 11, 3], [57, 0, 10, 3], [70, 4, 13, 3], [75, 4, 5, 3], [76, 11, 12, 3], [85, 8, 11, 3], [3, 3, 4, 4], [9, 7, 10, 4], [15, 0, 6, 4], [23, 6, 10, 4], [25, 1, 13, 4], [34, 10, 11, 4], [41, 0, 3, 4], [43, 0, 11, 4], [49, 0, 13, 4], [24, 4, 8, 5], [73, 6, 9, 5], [1, 0, 2, 6], [7, 2, 8, 6], [8, 4, 9, 6], [22, 3, 10, 6], [29, 3, 7, 6], [42, 2, 9, 6], [47, 1, 11, 6], [60, 1, 8, 6], [81, 1, 10, 6], [11, 6, 12, 7], [20, 1, 2, 7], [68, 4, 10, 7], [86, 6, 13, 7], [6, 4, 7, 8], [17, 0, 7, 8], [26, 11, 13, 8], [40, 3, 6, 8], [77, 0, 4, 8], [78, 5, 7, 8], [88, 1, 4, 8], [12, 12, 13, 9], [18, 1, 12, 9], [31, 1, 7, 9], [50, 3, 9, 9], [65, 5, 10, 9], [67, 2, 6, 9], [71, 3, 11, 9], [82, 1, 9, 9], [83, 7, 8, 9], [14, 5, 13, 10], [21, 1, 3, 10], [27, 2, 12, 10], [33, 2, 13, 10], [35, 3, 5, 10], [52, 6, 7, 10], [66, 5, 6, 10], [69, 3, 13, 10], [87, 0, 12, 10], [4, 0, 5, 11], [19, 10, 12, 11], [46, 7, 11, 11], [63, 9, 13, 11], [30, 7, 12, 12], [48, 2, 10, 12], [56, 2, 4, 12], [59, 3, 8, 12], [62, 10, 13, 12], [74, 1, 5, 12], [80, 8, 12, 12], [0, 0, 1, 13], [2, 2, 3, 13], [38, 0, 8, 13], [53, 6, 8, 13], [79, 9, 12, 13], [84, 9, 10, 13], [5, 4, 6, 14], [36, 6, 11, 14], [44, 2, 5, 14], [64, 2, 11, 14], [72, 7, 9, 14]]