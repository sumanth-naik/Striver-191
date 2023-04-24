class Solution:
    def squareFreeSubsets(self, nums):

        primes, MOD = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 10**9+7

        # remove elements which wont be in any subsets
        @lru_cache(None)
        def hasSinglePrimeMultipleTimesAsFactors(num):
            for i in [2,3,5]:
                if num%i==0 and (num//i)%i==0: return True
            return False
        nums = [nums[i] for i in range(len(nums)) if not hasSinglePrimeMultipleTimesAsFactors(nums[i])]

        # remove duplicates and 1 from nums, as any other number can be added only once but 1 can be added any number of times
        # Its like combination counting, where given a subset that dp finds, say, [2,3,5], we know there will be count(2)*count(3)*count(5) [2,3,5] subsets that we will eventually see 
        # Need to handle 1 separately as [1] and [1,1] and [1,1,2] etc are all valid but [k,k] or [1,k,k] (any k>1) will never be valid
        counter = Counter(nums)
        nums = list(set(nums)-set([1]))

        # Create bitmasks wrt primes factors for each number in nums
        @lru_cache(None)
        def getBitMaskWithPrimeFactors(num):
            mask = 0
            for index, prime in enumerate(primes):
                if num%prime==0:
                    mask |= (1<<index)
            return mask
        bitMaskOfNumbers = [getBitMaskWithPrimeFactors(num) for num in nums]


        # recursion: if number can be added, take or not take to generate all possible subsets [this technique will have an empty subset as well so subtract it from final answer]
        # top down would be generally preferred as we wont need all combinations of maskOfPrimesUsedInTheProductSoFar for a given indexInNums
        @lru_cache(None)
        def recursion(indexInNums, maskOfPrimesUsedInTheProductSoFar):
            if indexInNums==len(nums):
                return 1
            if maskOfPrimesUsedInTheProductSoFar & bitMaskOfNumbers[nums[indexInNums]] != 0:
                return recursion(indexInNums+1, maskOfPrimesUsedInTheProductSoFar)
            else:
                return  (recursion(indexInNums+1, maskOfPrimesUsedInTheProductSoFar) + counter[nums[indexInNums]] * recursion(indexInNums+1, maskOfPrimesUsedInTheProductSoFar | getBitMaskWithPrimeFactors(nums[indexInNums])))%MOD
        
        squareFreeSubsetsDueToOtherNumbers = (recursion(0, 0)-1)%MOD 

        # any subset that we can generate with only 1s can be paired to any squareFreeSubset from @squareFreeSubsetsDueToOtherNumbers
        # like if original nums was [1,1,2,3], squareFreeSubsetsDueToOtherNumbers would be [(2), (3), (2,3)]
        # permutations due to ones would be [(1), (1,1), (1), ()] note that each 1 is distinct, hence permutation
        # final ans would be a combination of both with ones and without ones but empty subset removed like {[(1), (1,1), (1)] + cross product of subsets( i.e., [(1), (1,1), (1)] * [(2), (3), (2,3)])}
        permutationsDueToOnes = (pow(2, counter[1]))%MOD
        if permutationsDueToOnes:
            if squareFreeSubsetsDueToOtherNumbers: return (permutationsDueToOnes-1 + permutationsDueToOnes*squareFreeSubsetsDueToOtherNumbers)%MOD
            else: return permutationsDueToOnes-1
        else:
            return squareFreeSubsetsDueToOtherNumbers