
# WA - does not generate all combinations
# class Solution:
#     def minimumDifference(self, nums) -> int:
#         n, totalSum, minDiff = len(nums)//2, sum(nums), float('inf')
#         for state in range(2**n):
#             currentSum, index = 0, 0
#             for _ in range(n):
#                 if state&1: index+=1
#                 currentSum+=nums[index]
#                 state>>=1
#                 index+=1
#             minDiff = min(minDiff, abs(totalSum-2*currentSum))
#         return minDiff
import bisect
class Solution:
    def minimumDifference(self, nums) -> int:
        # Meet in the middle technique
        n, totalSum = len(nums)//2, sum(nums)
        
        # divide arr into two parts
        arr1, arr2 = nums[:n], nums[n:]

        # on all subsets, calculate sum and add to a map of numSelected -> sumOfSelected
        # Can be done in same loop
        arr1SumsMap, arr2SumsMap = defaultdict(list), defaultdict(list)
        for mask in range(2**n):
            arr1Sum, arr2Sum, numSelected, index = 0, 0, 0, 0
            while mask:
                if mask&1:
                    arr1Sum += arr1[index]
                    arr2Sum += arr2[index]
                    numSelected += 1
                index += 1
                mask >>= 1
            arr1SumsMap[numSelected].append(arr1Sum)
            arr2SumsMap[numSelected].append(arr2Sum)
        
        # for all k all combinations(x in arr1SumsMap[k], y in arr2SumsMap[n-k])  abs(sum - 2*(x+y)) should be minimized
        # we can optimize by sorting one of them and using bisect_left to findout nearest number
        # assume sum - 2x -2y = 0
        # y = (sum - 2x)/2
        # lets find a number closest to y in arr2SumsMap[n-k]. It might not be an exact match. We just need closest one
        # suppose y is 5 and arr2SumsMap[n-k] is {-1,3,6,7}, bisect_left will give 2(index). Check 1 and 2 indices values only.

        # sort 
        for k, v in arr1SumsMap.items():
            v.sort()

        # since other set choosing 0 elements adds 0
        minDiff = min(abs(totalSum - 2*sum(arr1)), abs(totalSum - 2*sum(arr2)))
        for numSelected, sums in arr2SumsMap.items():
            for sum2 in sums:
                index = bisect.bisect_left(arr1SumsMap[n-numSelected], (totalSum-2*sum2)/2)
                for ind in [index, index-1]:
                    if 0<=ind<len(arr1SumsMap[n-numSelected]): minDiff = min(minDiff, abs(totalSum - 2*(arr1SumsMap[n-numSelected][ind]+sum2)))

        return minDiff
        

