class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adjList = defaultdict(list)

        for (u, v), val in zip(equations, values):
            adjList[u].append((v, 1/val))
            adjList[v].append((u, val))

        def findDiv(currNode, finalNode, currDiv, visited):
            visited.add(currNode)
            if currNode==finalNode: return currDiv
            for neigh, val in adjList[currNode]:
                if neigh not in visited:
                    possibleDiv = findDiv(neigh, finalNode, currDiv/val, visited)
                    if possibleDiv!=-1: return possibleDiv
            return -1

        ansArr = []
        for u, v in queries:
            if u not in adjList or v not in adjList: ansArr.append(-1)
            else: ansArr.append(round(findDiv(u, v, 1, set()), 5))
        return ansArr


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adjList = defaultdict(list)

        for (u, v), val in zip(equations, values):
            adjList[u].append((v, val))
            adjList[v].append((u, 1/val))

        def bfs(u, v):
            queue = deque([(u, 1)])
            visited = set([u])

            while queue:
                node, nodeMultVal = queue.popleft()
                if node==v: return nodeMultVal
                for neigh, neighMultVal in adjList[node]:
                    if neigh not in visited:
                        queue.append((neigh, nodeMultVal*neighMultVal))
                        visited.add(neigh)
            return -1


        ansArr = []
        for u, v in queries:
            if u not in adjList or v not in adjList: ansArr.append(-1)
            else: ansArr.append(round(bfs(u, v), 5))
        return ansArr



# classic Floyd Warshall
# adjMatrix = [[1e15 for _ in range(n)] for _ in range(n)]

# for i in range(n):
#      for j in range(n):
#         if i==j:
#             adjMatrix[i][j] = 0

# for road in roads:
#     adjMatrix[road[0]][road[1]] = road[2]
#     adjMatrix[road[1]][road[0]] = road[2]

# for middle in range(n):
#     for i in range(n):
#         for j in range(n):
#             if i!=j and i!=middle and j!=middle:
#                 adjMatrix[i][j] = min(adjMatrix[i][j], adjMatrix[i][middle] + adjMatrix[middle][j])
        
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adjMatrixWithMap = defaultdict(lambda : defaultdict(int)) # map of map instead of traditional matrix (array of arrays)

        for (u, v), val in zip(equations, values):
            adjMatrixWithMap[u][u] = adjMatrixWithMap[v][v] = 1
            adjMatrixWithMap[u][v] = val
            adjMatrixWithMap[v][u] = 1/val

        for mid in adjMatrixWithMap.keys():
            for src in adjMatrixWithMap[mid].keys(): # checking [mid] because we ony need those connections where there is a path. Also, if u -> v exists, v -> u also exists
                for dest in adjMatrixWithMap[mid]: # .keys() is not necessary
                    if src!=dest: # needed to avoid unnecessary float rounding errors, if not u/u will not be 1
                        adjMatrixWithMap[src][dest] = adjMatrixWithMap[src][mid]*adjMatrixWithMap[mid][dest] # update even if it is already present as the value will be same as per qn constraints
                    elif src==mid:
                        print("src is mid", adjMatrixWithMap[src][dest], adjMatrixWithMap[src][mid], adjMatrixWithMap[mid][dest], adjMatrixWithMap[src][mid]*adjMatrixWithMap[mid][dest])
                    elif dest==mid:
                        print("dest is mid", adjMatrixWithMap[src][dest], adjMatrixWithMap[src][mid], adjMatrixWithMap[mid][dest], adjMatrixWithMap[src][mid]*adjMatrixWithMap[mid][dest])
        
        return [round(adjMatrixWithMap[src].get(dest, -1), 5) for src, dest in queries] # use get(,) to return -1 if any of src or dest is not present
            
 
# https://alexgolec.medium.com/google-interview-problems-ratio-finder-d7aa8bf201e3
# one node is like master node(bfs starting node) that allows for constant time conversion
# start/end = 1/(master/start) * (master/end)

# Use this technique whenever you have all paths leading to the same answer, in this case the product of edgeVals.
# It is essentially caching
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
                
        adjList = defaultdict(list)

        for (u, v), val in zip(equations, values):
            adjList[u].append((v, val))
            adjList[v].append((u, 1/val))

        conversions = defaultdict(tuple)

        def bfs(start):
            nonlocal conversions
            queue = deque([(start, 1.0)])
            while queue:
                node, startToNodeVal = queue.popleft()
                conversions[node] = (start, startToNodeVal)
                for neigh, val in adjList[node]:
                    if neigh not in conversions:
                        queue.append((neigh, startToNodeVal*val))
                        conversions[neigh] = 1e9 # random number to mark as visited
            
        for node in adjList:
            if node not in conversions:
                bfs(node)
        
        def getDiv(start, end):
            if start not in conversions or end not in conversions: return -1.0
            return round((1/conversions[start][1])*conversions[end][1], 5) if conversions[start][0]==conversions[end][0] else -1.0
        
        return [getDiv(start, end) for start, end in queries]
