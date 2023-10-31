# Key Idea 1: Use parent param instead of visited set to avoid inf loop
# Key Idea 2: Use a single counter. Use 'before' children dfs call count and 'after' children dfs call count to get ans

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        counts, resultList = Counter(), [0]*n
        def dfs(num, parent):
            beforeCount = counts[labels[num]]
            for neigh in adjList[num]:
                if neigh!=parent:
                    dfs(neigh, num)
            counts[labels[num]] += 1
            resultList[num] = counts[labels[num]] - beforeCount

        dfs(0, -1)
        return resultList