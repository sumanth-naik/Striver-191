class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        # force sorted picking for duplicate prevention
        types.sort(key = lambda x:x[1])
        MOD = 10**9+7
        @lru_cache(None)
        def recursion(targetLeft, index):
            if targetLeft==0: return 1
            if targetLeft<0 or index==-1: return 0
            return sum(recursion(targetLeft-count*types[index][1], index-1) for count in range(types[index][0]+1))%MOD

        return recursion(target, len(types)-1)



class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int: 
        types.sort(key = lambda x:x[1])
        MOD, n = 10**9+7, len(types)
        dp = [[0 for _ in range(n)] for _ in range(target+1)]
        for j in range(n):
            dp[0][j] = 1
        for num in range(types[0][1], min(target, types[0][1]*types[0][0])+1, types[0][1]):
            dp[num][0] = 1
        for index in range(1, n):
            for targetLeft in range(1, target+1):
                dp[targetLeft][index] = sum(dp[targetLeft-count*types[index][1]][index-1] for count in range(types[index][0]+1) if targetLeft-count*types[index][1]>=0)%MOD
        return dp[target][n-1]




class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int: 
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        # keep considering each type from left to right
        for count, val in types:
            for targetToFill in range(target, -1, -1):
                # add values dp[targetToFill-val*countChosen] which indicates the number of ways when current type is not included in them previously. First, use them then update them. Thats why range(target, -1, -1)
                for countChosen in range(1, min(count, targetToFill//val)+1):
                    dp[targetToFill] = (dp[targetToFill] + dp[targetToFill-val*countChosen])%(10**9+7)
        return dp[target]
    

class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int: 

        dp = [1] + [0 for _ in range(target)]
        for count, val in types:
            # use val once -> add dp[index-val] to dp[index]
            # dp[index-val] inturn would have used val multiple times
            for index in range(val, target+1):
                dp[index] += dp[index-val]

            # remove more than count usages of val
            # Its first use will happen at (count+1)*val index
            # over used values at index have 1-1 mapping with dp value at index-(count+1)*val 
            # because those are the values which contribute to more than count usages
            for index in range(target, (count+1)*val-1, -1):
                dp[index] -= dp[index-(count+1)*val]
        
        return dp[-1]%(10**9+7)