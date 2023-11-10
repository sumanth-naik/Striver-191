class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        def dfs(node):
            visited.add(node)
            for neigh in filter(lambda neigh: isConnected[node][neigh], range(n)):
                if neigh not in visited:
                    dfs(neigh)

        count, visited = 0, set()
        for node in range(n):   
            if node not in visited:
                count += 1
                dfs(node)
        return count
        