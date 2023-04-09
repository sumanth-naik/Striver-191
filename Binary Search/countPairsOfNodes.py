class Solution:
    def countPairs(self, n: int, edges, queries):

        degreeArr = [0 for _ in range(n+1)]
        numEdgesMap = defaultdict(int)
        for u, v in edges:
            degreeArr[u] += 1
            degreeArr[v] += 1
            numEdgesMap[(min(u,v), max(u,v))] += 1

        
        sortedDegrees = sorted(degreeArr)
        
        for query in queries:
            count  = 0
            low, high = 1, n
            while low<high:
                if sortedDegrees[low] + sortedDegrees[high] > query:
                    count += (high - low)
                    high -= 1
                else:
                    low += 1
            for u, v in numEdgesMap.keys():
                if degreeArr[u] + degreeArr[v] - numEdgesMap[(min(u,v), max(u,v))]<=query<degreeArr[u] + degreeArr[v]:
                    count -= 1
            yield count