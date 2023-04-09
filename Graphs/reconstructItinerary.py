class Solution:
    def findItinerary(self, tickets):
        adjList = defaultdict(list)
        for u, v in tickets:
            adjList[u].append(v)
        for key in adjList.keys():
            adjList[key].sort(reverse=True)
        
        path = []
        def dfs(node):
            while adjList[node]:
                dfs(adjList[node].pop())
            path.append(node)

        dfs("JFK")
        return reversed(path)