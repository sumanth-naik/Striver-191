class UnionFind:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
    def findParent(self, node):
        if self.parent[node] != node:
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
    def maxNumEdgesToRemove(self, n: int, edges):
        unionFindOfAlice, unionFindOfBob = UnionFind(n), UnionFind(n)
        aliceTraversableEdges, bobTraversableEdges, bothTraversableEdges = [], [], []
        for edge in edges:
            if edge[0]==1:
                aliceTraversableEdges.append((edge[1]-1, edge[2]-1))
            elif edge[0]==2:
                bobTraversableEdges.append((edge[1]-1, edge[2]-1))
            else:
                bothTraversableEdges.append((edge[1]-1, edge[2]-1))

        numEdgesAddedInBoth = 0
        for edge in bothTraversableEdges:
            if numEdgesAddedInBoth==n-1:
                break
            if not unionFindOfAlice.belongsToSameComponent(edge[0], edge[1]):
                unionFindOfAlice.union(edge[0],edge[1])
                unionFindOfBob.union(edge[0],edge[1])
                numEdgesAddedInBoth += 1


        numEdgesAddedInAliceOnly = 0
        for edge in aliceTraversableEdges:
            if numEdgesAddedInBoth + numEdgesAddedInAliceOnly==n-1:
                break
            if not unionFindOfAlice.belongsToSameComponent(edge[0], edge[1]):
                unionFindOfAlice.union(edge[0],edge[1])
                numEdgesAddedInAliceOnly += 1  

             
        numEdgesAddedInBobOnly = 0
        for edge in bobTraversableEdges:
            if numEdgesAddedInBoth + numEdgesAddedInBobOnly==n-1:
                break
            if not unionFindOfBob.belongsToSameComponent(edge[0], edge[1]):
                unionFindOfBob.union(edge[0],edge[1])
                numEdgesAddedInBobOnly += 1 

        if not (numEdgesAddedInAliceOnly + numEdgesAddedInBoth == n-1 == numEdgesAddedInBobOnly + numEdgesAddedInBoth):
            return -1
        else:
            return len(edges) - (numEdgesAddedInAliceOnly + numEdgesAddedInBoth + numEdgesAddedInBobOnly)
        

