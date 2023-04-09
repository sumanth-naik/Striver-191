# sorting wont work as if there are multiple same numbers, we dont know which to pick first
# to decide, we will have to do a BFS starting from index with max(max(lastRankInRowArr[i], lastRankInColArr[j]))
# which is basically topo sort, we could do it from beginning itself
# class Solution:
#     def matrixRankTransform(self, matrix):
#         m, n = len(matrix), len(matrix[0])

#         sortedList = sorted([(matrix[i][j], i, j) for i in range(m) for j in range(n)])

#         lastSeenRowArr, lastSeenColArr, lastRankInRowArr, lastRankInColArr = [float('inf')] * m, [float('inf')] * n, [0] * m, [0] * n
#         rankMatrix = [[0 for _ in range(n)] for _ in range(m)]

#         prevVal, sameValElements = float('inf')
#         for val, i, j in sortedList:
#             if val==prevVal:
#                 sameValElements.append(( lastRankInRowArr[i] + lastRankInColArr[j], i, j))

#             if lastSeenRowArr[i]!=val:
#                 lastSeenRowArr[i] = val
#                 lastRankInRowArr[i] += 1
#             if lastSeenColArr[j]!=val:
#                 lastSeenColArr[j] = val
#                 lastRankInColArr[j] += 1

#             rankMatrix[i][j] = lastRankInRowArr[i] = lastRankInColArr[j] = max(lastRankInRowArr[i], lastRankInColArr[j])
        
#         return rankMatrix
    

# [-37,-50,-3,44],
# [-37,46,13,-32],
# [47,-42,-3,-40],
# [-17,-22,-39,24]

# [2,1,3,6],
# [2,6,5,4],
# [5,2,4,3],
# [4,3,1,5]

# [2,1,4,6],
# [2,6,5,4],
# [5,2,4,3],
# [4,3,1,5]


# topo sort with a twist O(mn(m+n)) 
# sameValIndegreeZeroNodesMap, sameValNonIndegreeZeroNodesMap help to decide if we want to add or not to arr used in Kahn's algo
# class Solution:
#     def matrixRankTransform(self, matrix):
#         m, n = len(matrix), len(matrix[0])
#         indegreeArr = [[0 for _ in range(n)] for _ in range(m)]

#         rankMatrix, rank = [[0 for _ in range(n)] for _ in range(m)], 1

#         adjList, sameValAdjList = defaultdict(list), defaultdict(list)
#         for i in range(m):
#             for j in range(n):
#                 for sameRowElemJIndex in range(j+1, n):
#                     if matrix[i][j]>matrix[i][sameRowElemJIndex]:
#                         indegreeArr[i][j] += 1
#                         adjList[(i, sameRowElemJIndex)].append((i,j))
#                     elif matrix[i][j]<matrix[i][sameRowElemJIndex]:
#                         indegreeArr[i][sameRowElemJIndex] += 1
#                         adjList[(i,j)].append((i, sameRowElemJIndex))
#                     else:
#                         sameValAdjList[(i,j)].append((i,sameRowElemJIndex))
#                         sameValAdjList[(i,sameRowElemJIndex)].append((i,j))
#                 for sameColElemIIndex in range(i+1, m):
#                     if matrix[i][j]>matrix[sameColElemIIndex][j]:
#                         indegreeArr[i][j] += 1
#                         adjList[(sameColElemIIndex,j)].append((i, j))
#                     elif matrix[i][j]<matrix[sameColElemIIndex][j]:
#                         indegreeArr[sameColElemIIndex][j] += 1
#                         adjList[(i,j)].append((sameColElemIIndex, j))
#                     else:
#                         sameValAdjList[(i,j)].append((sameColElemIIndex,j))
#                         sameValAdjList[(sameColElemIIndex,j)].append((i,j))



#         # map of node to set of nodes in that component where node is present
#         sameValIndegreeZeroNodesMap, sameValNonIndegreeZeroNodesMap = {}, {}
#         visited = set()
#         def dfs(node, indegreeZeroSet, nonIndegreeZeroSet):
#             visited.add(node)
#             if indegreeArr[node[0]][node[1]]==0:
#                 indegreeZeroSet.add(node)
#             else:
#                 nonIndegreeZeroSet.add(node)
#             for neigh in sameValAdjList[node]:
#                 if neigh not in indegreeZeroSet and neigh not in nonIndegreeZeroSet:
#                     dfs(neigh, indegreeZeroSet, nonIndegreeZeroSet)
#             return indegreeZeroSet, nonIndegreeZeroSet

#         componentParentMap = {}
#         for node in sameValAdjList:
#             if node not in visited:
#                 indegreeZeroSet, nonIndegreeZeroSet = dfs(node, set(), set())
#                 sameValIndegreeZeroNodesMap[node] = indegreeZeroSet
#                 sameValNonIndegreeZeroNodesMap[node] = nonIndegreeZeroSet
#                 for componentNode in indegreeZeroSet | nonIndegreeZeroSet:
#                     componentParentMap[componentNode] = node


#         zeroIndegreeIndicesList = [(i,j) for i in range(m) for j in range(n) if indegreeArr[i][j]==0 and (i,j) not in visited]
#         for parent in sameValNonIndegreeZeroNodesMap.keys():
#             if len(sameValNonIndegreeZeroNodesMap[parent])==0:
#                 zeroIndegreeIndicesList.extend(sameValIndegreeZeroNodesMap[parent])


#         while zeroIndegreeIndicesList:
#             nextIterationZeroIndegreeIndicesList = []
#             for i, j in zeroIndegreeIndicesList:
#                 rankMatrix[i][j] = rank
#                 for neighI, neighJ in adjList[(i,j)]:
#                     indegreeArr[neighI][neighJ] -= 1
#                     if indegreeArr[neighI][neighJ]==0:
#                         if (neighI, neighJ) in componentParentMap:
#                             parent = componentParentMap[(neighI, neighJ)]
#                             sameValNonIndegreeZeroNodesMap[parent].remove((neighI, neighJ))
#                             sameValIndegreeZeroNodesMap[parent].add((neighI, neighJ))
#                             if len(sameValNonIndegreeZeroNodesMap[parent])==0:
#                                 nextIterationZeroIndegreeIndicesList.extend(sameValIndegreeZeroNodesMap[parent])
#                         else:
#                             nextIterationZeroIndegreeIndicesList.append((neighI, neighJ))
#             rank += 1
#             zeroIndegreeIndicesList = nextIterationZeroIndegreeIndicesList

#         return rankMatrix




class UnionFind:
    def __init__(self) -> None:
        self.parent = {}
        self.size = {}

    def addNode(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.size[node] = 0
    
    def findParent(self, node):
        if self.parent[node]!=node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        self.addNode(node1)
        self.addNode(node2)
        parent1 = self.findParent(node1)
        parent2 = self.findParent(node2)
        if parent1!=parent2:
            if self.size[parent1]>self.size[parent2]:
                self.parent[parent2] = parent1
                self.size[parent1] += self.size[parent2]
            else:
                self.parent[parent1] = parent2
                self.size[parent2] += self.size[parent1]

class Solution:
    def matrixRankTransform(self, matrix):
        m, n = len(matrix), len(matrix[0])
        rankMatrix = [[0 for _ in range(n)] for _ in range(m)]
        rowRanksArr, colRanksArr = [0 for _ in range(m)], [0 for _ in range(n)]
        valToIndicesMap = defaultdict(list)
        for i in range(m):
            for j in range(n):
                valToIndicesMap[matrix[i][j]].append((i,j))

        for val in sorted(valToIndicesMap.keys()):
            unionFind = UnionFind()
            for i, j in valToIndicesMap[val]:
                unionFind.union(i,~j)

            parentToMaxRankFoundMap = defaultdict(int)
            for i, j in valToIndicesMap[val]:
                parentToMaxRankFoundMap[unionFind.findParent(i)] = max(parentToMaxRankFoundMap[unionFind.findParent(i)], max(rowRanksArr[i], colRanksArr[j]))

            for i, j in valToIndicesMap[val]:
                rankMatrix[i][j] = rowRanksArr[i] = colRanksArr[j] = parentToMaxRankFoundMap[unionFind.findParent(i)] + 1

        return rankMatrix
            

