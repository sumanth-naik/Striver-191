# Combinations -> Brute force only -> Backtracking with exit(for combinations) or Bitmasking DP



# Key Idea 1: Which bag should I add this current cookie? (try all)
# Note: Exit to get combinations and not permutations
# TC - (k^n / k!) * n

class Solution:
    def distributeCookies(self, cookies, k: int) -> int:
        minUnfairness, bags = 1e9, [0]*k

        def backTracking(indexToAddNext):
            nonlocal minUnfairness
            if indexToAddNext==len(cookies): 
                minUnfairness = min(minUnfairness, max(bags))
            else:
                for bagsIndex in range(len(bags)):
                    bags[bagsIndex] += cookies[indexToAddNext]
                    backTracking(indexToAddNext+1)
                    bags[bagsIndex] -= cookies[indexToAddNext]
                    if not bags[bagsIndex]: break  # Note

        backTracking(0)
        return minUnfairness
    



# Key Idea 1: Loop on bags instead of cookies. In current bag, which all cookies should I add?
#             Recursion: f(mask, bagNum) = min(max(sum(subset), f(subset^mask, bagNum - 1)) for subset in getAllSubsets(mask)) 

# Optimisation 1: Use subset enumeration to optimise        - getAllSubsets(mask)  - 3^n 
# Optimisation 2: Prepopulate sumOfSetBitMasks to optimise  - sum(subset)          - n * 2^n

# Bottom up with space optimization version
# TC - n * 2^n + k * 3^n 

class Solution:
    def distributeCookies(self, cookies, k: int) -> int:

        n = len(cookies)
        sumOfSetBitMasks = list(map(lambda mask: sum(cookies[i] for i in range(n) if mask&(1<<i)), range(1<<n)))

        dpPrev = [1e9] * (1<<n)
        dpPrev[0] = 0
        for _ in range(k):
            dpCurr = [1e9] * (1<<n)
            for mask in range(1<<n):
                subsetMask = mask
                while subsetMask:
                    dpCurr[mask] = min(dpCurr[mask], max(sumOfSetBitMasks[subsetMask], dpPrev[subsetMask^mask]))
                    subsetMask = (subsetMask-1) & mask
            dpPrev = dpCurr
        return dpPrev[-1]
