import bisect
class Solution:
    def splitArraySameAverage(self, nums) -> bool:
        n, totalSum = len(nums), sum(nums)
        arr1, arr2 = nums[:n//2], nums[n//2:]


        def getSumsMap(arr):
            arrSumsMap = defaultdict(set)
            for mask in range(2**len(arr)):
                index, runningSum, numSelected = 0, 0, 0
                while mask:
                    if mask&1:
                        runningSum += arr[index]
                        numSelected += 1
                    index += 1
                    mask >>= 1
                arrSumsMap[numSelected].add(runningSum)
            return arrSumsMap

        arr1SumsMap, arr2SumsMap = getSumsMap(arr1), getSumsMap(arr2)

        # n/2 loops (say k)
        for numSelected1, sumsSet1 in arr1SumsMap.items(): 
            # n/2 loops
            for numSelected2, sumsSet2 in arr2SumsMap.items():
                if 0<numSelected1+numSelected2<n:
                    # asymptotic 2**(n/2) loops across this loop and prev loop => TC = O(k * 2**(n/2))
                    for sum2 in sumsSet2:
                        numberToSearchInSumsSet1 = ((numSelected1+numSelected2)*totalSum - n*sum2)/n
                        if numberToSearchInSumsSet1 in sumsSet1: return True

        return False


# DP
# s1/n1 = s2/n2 = s1+s2/n1+n2
# Thus, s1 = n1*avg
# All we need to do is to find a subset of length n1 such that their sum is n1*avg - N sum problem

class Solution:
    def splitArraySameAverage(self, nums) -> bool:
        n = len(nums)
        @lru_cache(None)
        def hasSum(sizeToChoose, index, sumLeft):
            if sizeToChoose==0: return sumLeft==0
            if sizeToChoose>n-index or sumLeft<0: return False
            return hasSum(sizeToChoose, index+1, sumLeft) or hasSum(sizeToChoose-1, index+1, sumLeft-nums[index])
        # search only if sizeToChoose*sum(nums)%len(nums)==0 as a findable sumLeft can only be an integer as it is sum of integers
        return any(hasSum(sizeToChoose, 0, sizeToChoose*sum(nums)//len(nums)) for sizeToChoose in range(1, n//2+1) if sizeToChoose*sum(nums)%len(nums)==0)




