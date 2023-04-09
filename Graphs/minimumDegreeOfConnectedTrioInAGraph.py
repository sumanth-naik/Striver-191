    
class Solution:
    def minTrioDegree(self, n: int, edges):
        adjSet = [set() for _ in range(n+1)]
        for u, v in edges:
            adjSet[u].add(v) 
            adjSet[v].add(u) 
        nodesSortedByDegrees = sorted((len(adjSet[i]), i) for i in range(n+1))
        minTrioDegreeSum = 1e9
        for u, v in edges:
            if minTrioDegreeSum<len(adjSet[u]) + len(adjSet[v]):
                continue
            for degree, node in nodesSortedByDegrees:
                if node in adjSet[u] and node in adjSet[v]:
                    minTrioDegreeSum = min(minTrioDegreeSum, len(adjSet[u]) + len(adjSet[v]) + degree)
                    break
            
        return -1 if minTrioDegreeSum==1e9 else minTrioDegreeSum-6 