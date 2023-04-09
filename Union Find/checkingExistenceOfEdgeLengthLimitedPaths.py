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
    def distanceLimitedPathsExist(self, n: int, edgeList, queries):
        sortedQueriesAndIndexTuples = sorted(zip(queries, list(range(len(queries)))), key=lambda x:x[0][2])
        ansArr = [True for _ in range(len(queries))]

        unionFind = UnionFind(n)
        edgeList.sort(key=lambda x: x[2])

        edgesIndex = 0
        for query, index in sortedQueriesAndIndexTuples:
            u,v,dist = query
            while edgesIndex<len(edgeList) and edgeList[edgesIndex][2]<dist:
                if not unionFind.belongsToSameComponent(edgeList[edgesIndex][0], edgeList[edgesIndex][1]):
                    unionFind.union(edgeList[edgesIndex][0], edgeList[edgesIndex][1])
                edgesIndex += 1
            if not unionFind.belongsToSameComponent(u,v):
                ansArr[index] = False

        return ansArr