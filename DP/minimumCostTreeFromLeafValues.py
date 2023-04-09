from functools import lru_cache
class Solution:
    def mctFromLeafValues(self, arr):    
        @lru_cache(maxsize=len(arr)*len(arr))
        def memoization(left, right):
            if left==right: return 0
            return min(memoization(left, i) + memoization(i+1, right) + max(arr[left:i+1])*max(arr[i+1:right+1]) for i in range(left, right))
                
        return memoization(0, len(arr)-1)
    
    def mctFromLeafValues(self, arr):  
        n = len(arr)  
        dp = [[1e9]*n for _ in range(n)]
        for i in range(n): dp[i][i] = 0

        for delta in range(1, n):
            for startIndex in range(n-delta):
                left, right = startIndex, startIndex+delta
                dp[left][right] = min(dp[left][i] + dp[i+1][right] + max(arr[left:i+1])*max(arr[i+1:right+1]) for i in range(left, right))
                
        return dp[0][n-1]
    
class Solution:
    def mctFromLeafValues(self, A):
        stack, minCost = [float('inf')], 0
        # we want stack to have left next greatest or equal element => we will pop smaller or equal elements till we see that element => stack will have (not strictly)increasing order of numbers => base case will be inf
        for num in A:
            while stack[-1]<=num:
                # num is the next greatest/equal elem on right side of stack[-1] because, stack[-1] is being popped out now and it happens only using a greater/equal number (stack[-1]<=num)
                # stack[-2] is the next greatest/equal elem on left of stack[-1] because any smaller/equal number between stack[-2] and stack[-1] would have been popped out by stack[-1]
                minCost += stack[-1]*min(stack[-2], num)
                stack.pop()
            stack.append(num)
        # now stack has increasing order (strictly) of numbers (as seen from top) meaning 
        # each element's next greatest elem on right is inf
        # so need to only check left next greatest element which are the elements in the stack itself
        while len(stack)>2:
            minCost += stack[-1]*stack[-2]
            stack.pop()
        return minCost