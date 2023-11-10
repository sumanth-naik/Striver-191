# Key Idea 1: Create valid subsets and use product rule. (2, 3, 5) contributes counter[2] * dp([3, 5]) times
#             Use take/not-take DP with bitmasking
# Key Idea 2: Handle ones separately. Multiply each non-oned subset with all permutations of ones (2**counter[1])

# Optimisation 1: Remove elements which wont be in any subsets, also remove 1.
# Note 1: Subtract one as empty subset is counted. It implicitly takes care of ones present and not present cases.

class Solution:
    def squareFreeSubsets(self, nums):
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
        
        return (bitmaskDp(0, 0)*pow(2, counter[1], MOD) - 1) % MOD   # Note 1
