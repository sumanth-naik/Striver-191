# back tracking
class Solution:
    def distributeCookies(self, cookies, k: int) -> int:
        minUnfairness = 1e9
        def backTracking(listOfSums, indexToAddNext):
            nonlocal minUnfairness
            if indexToAddNext==len(cookies): 
                minUnfairness = min(minUnfairness, max(listOfSums))
            else:
                for i in range(len(listOfSums)):
                    listOfSums[i]+=cookies[indexToAddNext]
                    backTracking(listOfSums, indexToAddNext+1)
                    listOfSums[i]-=cookies[indexToAddNext]
                if len(listOfSums)<k:
                    listOfSums.append(cookies[indexToAddNext])
                    backTracking(listOfSums, indexToAddNext+1)
                    listOfSums.pop()

        backTracking([], 0)
        return minUnfairness

# Bitmasking - Submask Enumeration with DP https://leetcode.com/problems/fair-distribution-of-cookies/solutions/2141573/dp-submask-enumeration-most-optimal-solution-100-faster-c/
#https://cp-algorithms.com/algebra/all-submasks.html#enumerating-all-submasks-of-a-given-mask
class Solution:
    def distributeCookies(self, cookies, k: int) -> int:

        sumOfSetBitMasks, n = [], len(cookies)
        for mask in range(1<<n):
            total = 0
            for i in range(n):
                if mask & 1<<i:
                    total+=cookies[i]
            sumOfSetBitMasks.append(total)

        dpPrev = [1e9 for _ in range(1<<n)]
        # setting it to 0 as in max(sumOfSetBitMasks[subsetMask], dpPrev[subsetMask^mask]) in the first iter subsetMask^mask is 0
        # we need to cover the case of all in one group, this is the shortest way to do, given the rest of the code
        dpPrev[0] = 0
        for _ in range(k):
            # copying prev since in subsetMask we are not going to check the case of none in last group i.e., dpPrev[mask] case
            dpCurr = deepcopy(dpPrev)
            for mask in range(1<<n):
                subsetMask = mask
                while subsetMask:
                    dpCurr[mask] = min(dpCurr[mask], max(sumOfSetBitMasks[subsetMask], dpPrev[subsetMask^mask]))
                    # submask enueration step, this removes the right most 1 and adds any 1 that right side to that removed 1 and is present in mask
                    # example: 10101 -> 10100 -> 10001 -> 10000 -> 00101 -> 00100 -> 00001 -> 00000(last case needs to be handled separately.. in this case we did that by copying dpPrev to dpCurr)
                    subsetMask = (subsetMask-1)&mask
            dpPrev = dpCurr
        return dpPrev[-1]
