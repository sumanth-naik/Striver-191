import heapq
class Solution:
    def maxStarSum(self, vals, edges, k):
        adjList = [[] for _ in range(len(vals))]
        for edge in edges:
            if vals[edge[0]]>0:
                adjList[edge[1]].append(vals[edge[0]])
            if vals[edge[1]]>0:
                adjList[edge[0]].append(vals[edge[1]])

        maxSum = -1e15
        for node in range(len(vals)):
            nodeStarSum = vals[node]
            if adjList[node]:
                nodeStarSum += sum(heapq.nlargest(k, adjList[node]))
            maxSum = max(maxSum, nodeStarSum)
        return maxSum