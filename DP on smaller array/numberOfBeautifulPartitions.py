# Key Idea: do not have another param in recursion to calculate diff for checking minLength, just jump index+minLength in Take case

class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        primes = set(['2', '3', '5', '7'])
        if s[0] not in primes or s[-1] in primes: return 0
        n, MOD = len(s), 10**9+7

        @lru_cache(None)
        def isValidEnd(index):
            return s[index] not in primes and s[index+1] in primes
        
        @lru_cache(None)
        def recursion(index, kLeft):
            if index>=n: return 0
            if index==n-1: return 1 if kLeft==1 else 0
            take = recursion(index+minLength, kLeft-1) if isValidEnd(index) else 0
            notTake = recursion(index+1, kLeft)
            return (take + notTake)%MOD
        
        return recursion(minLength-1, k)

# Key Idea 1: Have an arr which tells the valid Start indices.
# Key Idea 2: Use two pointer to pre-populate, what is the minimum jump in Take case

# Note: its just that we are running DP on smaller arr. Nothing really changed from prev approach

class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        primes = set(['2', '3', '5', '7'])
        if s[0] not in primes or s[-1] in primes: return 0
        
        n, MOD, validStarts = len(s), 10**9+7, [0]
        for index in range(minLength, n-minLength+1): # NOTE: start and end 
            if s[index-1] not in primes and s[index] in primes:
                validStarts.append(index)

        m = len(validStarts)
        nextValidIndices, right = [m] * m, 1
        for left in range(m):
            while right<m and validStarts[right]-validStarts[left]<minLength:
                right += 1
            if right!=m:
                nextValidIndices[left] = right
            else: 
                break

        @lru_cache(None)
        def recursion(index, picked):
            if index==m: return 1 if picked==k else 0
            if picked>k or m-index<k-picked: return 0 #too many or too less picks -> early exit
            return (recursion(nextValidIndices[index], picked+1) + recursion(index+1, picked))%MOD
        return recursion(nextValidIndices[0], 1) # have to pick first one in any case

