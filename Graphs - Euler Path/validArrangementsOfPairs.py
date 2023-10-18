# wrong idea. DFS with atmost two visits. can check if there is a Hamiltonian path getting path is difficult
# class Solution:
#     def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
#         pairs = [tuple(pair) for pair in pairs]
#         adjList = defaultdict(list)
#         for pair in pairs:
#             adjList[pair[0]].append(pair)

#         visited = set()
#         def dfs(pair, pathVisitedToCountMap):
#             nonlocal visited
#             if not pair in pathVisitedToCountMap:
#                 pathVisitedToCountMap[pair] = 0
#             pathVisitedToCountMap[pair] += 1
#             visited.add(pair)

#             if len(pathVisitedToCountMap)==len(pairs):
#                 pathVisitedToCountMap[pair]-=1
#                 return [pair]

#             for neighPair in adjList[pair[1]]:
#                 if neighPair not in pathVisitedToCountMap or pathVisitedToCountMap[neighPair]<2:
#                     print(pair, neighPair)
#                     path = dfs(neighPair, pathVisitedToCountMap)
#                     if path:
#                         if pathVisitedToCountMap[pair]==1: 
#                             path.append(pair)
#                         pathVisitedToCountMap[pair]-=1
#                         return path

#             pathVisitedToCountMap[pair] -= 1
#             if pathVisitedToCountMap[pair]==0:
#                 del pathVisitedToCountMap[pair]

#         for pair in pairs:
#             if pair not in visited:
#                 path = dfs(pair, {})
#                 if path: return reversed(path)


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        inDegreeMap, outDegreeMap, adjList = defaultdict(int), defaultdict(int), defaultdict(list)
        for u, v in pairs:
            inDegreeMap[v] += 1
            outDegreeMap[u] += 1
            adjList[u].append(v)

        # if Euler circuit, we can start anywhere
        eulerPathRoot = pairs[0][0]
        for num in outDegreeMap.keys():
            if outDegreeMap[num] > inDegreeMap[num]:
                # it has to be an Eulerian Path and not circuit
                eulerPathRoot = num
                break

        # Hierholzer's Algorithm
        nodesVisited = []
        def dfs(num):
            while adjList[num]:
                neigh = adjList[num].pop()
                dfs(neigh)
            nodesVisited.append(num)

        dfs(eulerPathRoot)

        return [[nodesVisited[i], nodesVisited[i-1]] for i in range(len(nodesVisited)-1, 0, -1)]