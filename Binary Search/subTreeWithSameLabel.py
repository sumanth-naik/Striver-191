from collections import Counter
class Solution:
    def countSubTrees(self, n, edges, labels):

        adjList = {}
        for edge in edges:
            if not edge[0] in adjList:
                adjList[edge[0]] = []
            if not edge[1] in adjList:
                adjList[edge[1]] = []
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        visited = set()
        countList = [0 for i in range(n)]

        def dfs(num):
            visited.add(num)
            counter = Counter()
            if num in adjList:
                for neigh in adjList[num]:
                    if neigh not in visited:
                        counter += (dfs(neigh))

            if labels[num] not in counter:
                counter[labels[num]] = 0
            counter[labels[num]] += 1
            countList[num] = counter[labels[num]]
            return counter

        dfs(0)
        return countList
        