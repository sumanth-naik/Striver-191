# Key Idea: Creating partitions, each step will affect next steps -> Partition DP

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i, j):
            if i==j-1: return 0
            return min(values[i]*values[k]*values[j] + dp(i, k) + dp(k, j) for k in range(i+1, j))

        return dp(0, len(values)-1)