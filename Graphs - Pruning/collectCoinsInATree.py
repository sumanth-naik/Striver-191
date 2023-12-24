# Key Idea 1: Prune all coinless leaves recursively  
# Key Idea 2: Prune twice wrt leaves

# Note: We need to check if leaf has anything to pop in Key Idea 2 
# Only Case: Two leaves have an edge
# [0] - [1] (iteration 1)   or    [0] - 1 - 2 - [3] (iteration 2)
# [0] - [1] - 2 - 3 - 4 - [5]    is not problematic as both 0, 1 wont be in leaves arr at once.

class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        adjSet = [set() for _ in range(n)]
        for u, v in edges:
            adjSet[u].add(v)
            adjSet[v].add(u)

        for node in range(n):
            while len(adjSet[node])==1 and not coins[node]:
                parent = adjSet[node].pop()
                adjSet[parent].remove(node)
                node = parent
        
        for _ in range(2):
            leaves = [node for node in range(n) if len(adjSet[node])==1]
            for leaf in leaves:
                if not adjSet[leaf]: return 0 # Note
                parent = adjSet[leaf].pop()
                adjSet[parent].remove(leaf)

        return sum(len(adjSet[node]) for node in range(n))

