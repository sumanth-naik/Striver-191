class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:

        #       ((n-0) * n-1 * n-2 * n-3 ...... n-(k-1))
        # nCk = ----------------------------------------   <- loop populates numerator from left to right and denominator in reverse
        #           k * k-1 * k-2 * .... * 3 * 2 * 1
        @lru_cache(None)
        def nCk(n, k):
            res = 1
            for i in range(k):
                res *= (n-i)
                res //= (i + 1)
            return res
        
        # Idea: create arrays of distinct integers and ending in some number(lastElem) 
        # then use stars and bars to count combinations
        # Note: [1,2,4] is represented by recursion(4,2)
        # [1,2,6] and [1,3,6] both are recursion(6,2), hence memoise
        @lru_cache(None)
        def recursion(lastElem, size):
            # lastElem=4 size=3 like in [1,2,4] and n=4 -> [1,2,4,4], [1,2,2,4], [1,1,2,4] should contribute to count
            # Stars represent the actual numbers * _ * _ * _ *
            # In n-1 dashes put size-1 bars to create size number of buckets(we need to take each elem atleast once)
            # * | * | * _ * => [1,2,4,4]      * | * _ * | * => [1,2,2,4]      * _ * | * | * => [1,1,2,4] 
            count = nCk(n-1, size-1) 
            if size==n: return count
            for nextElem in range(lastElem*2, maxValue+1, lastElem):
                count += recursion(nextElem, size+1) # Adds new arrays only because lastElem for next iteration will be new like [1,2,4,8]
            return count
        
        return sum(recursion(lastElem, 1) for lastElem in range(1, maxValue+1))%(10**9+7)





'''
Idea 1: Count number of ways which end with num where 1<=num<=maxValue
Idea 2: All factors (ex: 2,2,3,3 of 36) needs to be placed and we are going to multiply a placed number from its index to right most index
Ex: if we decide to place first 2 at index 1; [_, _, _, _, _] => [_, 2, _, _, _] => [_,2,2,2,2] is the result
If we decide to place first 3 at index 3; [_, 2, _, 3, _] =>  [_,2,2,6,6] thus ensuring the problem constraints
Note that you HAVE to place all factors, if not product wont reach "num"
    - Here placing first two and second two are not independent and has to be done simultaneously to avoid overcounting
        - n = 5, k = 2(2 is factor twice) => n+k-1 slots => _ _ _ _ _ _ (6) => put 2 twos somewhere => _ 2 _ _ 2 _ => [,2,,2,] => [1,2,2,4,4] 
        - comb(n+k-1, k)
    - Placing twos and threes are independent and hence product rule must be used on their contibutions
        - count *= comb(n+k-1, k)
'''
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        primes = []
        def seiveTill(limit):
            flagsArr = [True]*(limit+1)
            for num in range(2, limit+1):
                if flagsArr[num]:
                    primes.append(num)
                    for multiple in range(num*num, limit+1, num): 
                        flagsArr[multiple] = False
        
        def nCk(n, k):
            res = 1
            for i in range(k):
                res *= (n-i)
                res //= (i+1)
            return res

        def getFactors(num):
            factorsMap = defaultdict(int)
            for prime in primes:
                while num%prime==0:
                    factorsMap[prime] += 1
                    num //= prime
            if num!=1:
                factorsMap[num] = 1
            return factorsMap

        def countTill(num):
            count = 1
            for prime, freq in getFactors(num).items():
                count *= nCk(n+freq-1, freq)
            return count

        '''
        We dont have to get primes till maxValue. 
        if num!=1: 
            factorsMap[num] = 1; 
        This step in getFactors will be sufficient as there can be atmost one prime factor bigger than sqrt(maxValue) in maxValue
        '''
        seiveTill(ceil(sqrt(maxValue))) 
        return sum(countTill(num) for num in range(1, maxValue+1))%(10**9+7)

# Same as above but concise, same as https://leetcode.com/problems/count-ways-to-make-array-with-product/
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
MOD = 10**9+7
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        def solver(buckets, num):
            ways = 1
            for prime in primes:
                count = 0
                while num%prime==0:
                    count += 1
                    num //= prime
                ways *= comb(buckets-1+count, count)
            if num!=1: #num has a factor which is a big prime
                ways *= buckets # there are 4 number of ways to put [num,1,1,1], [1,num,1,1], [1,1,num,1], [1,1,1,num]
            return ways%MOD
        return sum(solver(n, num) for num in range(1, maxValue+1))%MOD

# Not taking advantage of inbuilt functions and doing explicit MOD using factorials and factorialsInv
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9+7

        def seiveTill(limit):
            flagsArr, primes = [True]*(limit+1), []
            for num in range(2, limit+1):
                if flagsArr[num]:
                    primes.append(num)
                    for multiple in range(num*num, limit+1, num): 
                        flagsArr[multiple] = False
            return primes

        def powMod(n, m, MOD):
            res = 1
            while m:
                if m&1:
                    res = res * n % MOD
                n = n * n % MOD
                m //= 2
            return res

        def factAndFactInvMod(limit, MOD):
            factorials = [1] * (limit+1)
            for num in range(2, limit+1):
                factorials[num] = factorials[num-1] * num % MOD

            factorialsInv = [1] * (limit) + [powMod(factorials[-1], MOD-2, MOD)]
            for num in range(limit-1, 1, -1):
                factorialsInv[num] = factorialsInv[num+1] * (num+1) % MOD

            return factorials, factorialsInv

        def nCk(n, k, MOD):
            if k==1: return n
            return factorials[n] * factorialsInv[n-k] * factorialsInv[k] % MOD

        def getFactors(num):
            factorsMap = defaultdict(int)
            for prime in primes:
                while num%prime==0:
                    factorsMap[prime] += 1
                    num //= prime
            if num!=1: # needed as we limited primes to sqrt maxValue
                factorsMap[num] = 1
            return factorsMap

        def countTill(num, MOD):
            count = 1
            for prime, freq in getFactors(num).items():
                count = count * nCk(n+freq-1, freq, MOD) % MOD  # freq can be atmost log(maxValue, 2) 
            return count

        limit = ceil(sqrt(maxValue))
        primes = seiveTill(limit) 
        factorials, factorialsInv = factAndFactInvMod(n+14, MOD) # freq can be atmost log(maxValue, 2) 
        return sum(countTill(num, MOD) for num in range(1, maxValue+1))%MOD