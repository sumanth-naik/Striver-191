class Solution:
    def largestPathValue(self, colors: str, edges):
        n = len(colors)
        adjList, indegreeArr = [[] for _ in range(n)], [0 for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            indegreeArr[v] += 1
        
        # node number -> color's number of occurences
        memo = [[0 for _ in range(26)] for _ in range(n)]
        topoSortArr, levelArr, maxVal = [], [i for i in range(n) if indegreeArr[i]==0], 0

        while levelArr:
            nextLevelArr = []
            for node in levelArr:
                topoSortArr.append(node)
                memo[node][ord(colors[node])-ord('a')] += 1
                if len(adjList[node])==0:
                    maxVal = max(maxVal, max(memo[node]))
                for neigh in adjList[node]:
                    for color in range(26):
                        memo[neigh][color] = max(memo[neigh][color], memo[node][color])
                    indegreeArr[neigh] -= 1
                    if indegreeArr[neigh]==0:
                        nextLevelArr.append(neigh)
            levelArr = nextLevelArr

        return maxVal if len(topoSortArr)==n else -1