class Solution:

    def numberOfGoodSubsets(self, nums):
        counter, primes, MOD = Counter(nums), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 10**9+7
        nums = list(filter(lambda x: x!=1 and x%4 and x%9 and x%25, set(nums))) # Optimisation 1

        @cache
        def getPrimesMask(num):
            return reduce(lambda acc, index: acc|(1<<index) if num%primes[index]==0 else acc, range(len(primes)), 0)

        @cache
        def bitmaskDp(index, usedPrimesMask):
            if index==len(nums): return 1
            if usedPrimesMask & getPrimesMask(nums[index]):
                return bitmaskDp(index+1, usedPrimesMask)
            return (bitmaskDp(index+1, usedPrimesMask) + \
                    counter[nums[index]] * bitmaskDp(index+1, usedPrimesMask | getPrimesMask(nums[index])))%MOD
        
        return ((bitmaskDp(0, 0)-1)*pow(2, counter[1], MOD)) % MOD   # Note 1
