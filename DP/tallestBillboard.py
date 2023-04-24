class Solution:
    def tallestBillboard(self, rods) -> int:
        @lru_cache(None)
        def memoization(i, s1, s2):
            if i==len(rods): return s1 if s1==s2 else 0, 
            return max(memoization(i+1, s1+rods[i], s2), memoization(i+1, s1, s2+rods[i]), memoization(i+1, s1, s2))
        return memoization(0, 0, 0)
    
class Solution:
    def tallestBillboard(self, rods) -> int:
        @lru_cache(None)
        def memoization(i, diff):
            if i==len(rods): return 0 if diff==0 else -1e9
            return max(rods[i] + memoization(i+1, abs(diff+rods[i])), rods[i]+memoization(i+1, abs(diff-rods[i])), memoization(i+1, diff))
        return max(0, memoization(0, 0)//2)
    
    
class Solution:
    def tallestBillboard(self, rods) -> int:
        n, maxSum = len(rods), sum(rods)
        dpIPlusOne = [0]+[-1e9 for _ in range(maxSum)]
        for i in range(n-1, -1, -1):
            dpI = [-1e9 for _ in range(maxSum+1)]
            for diff in range(maxSum-rods[i]+1):
                dpI[diff] = max(rods[i] + dpIPlusOne[abs(diff+rods[i])], rods[i]+dpIPlusOne[abs(diff-rods[i])], dpIPlusOne[diff])
            dpIPlusOne = dpI
        return max(0, dpIPlusOne[0]//2)