import bisect
class Solution:
    def minAbsDifference(self, nums, goal: int) -> int:

        n = len(nums)

        # dfs generation is simpler and faster as well than bitmask generation
        # this gave TLE
        # def getSumsSet(arr):
        #     sumsSet = []
        #     for mask in range(2**len(arr)):
        #         runningSum = index = 0
        #         while mask:
        #             if mask&1:
        #                 runningSum += arr[index]
        #             index += 1
        #             mask >>= 1
        #         sumsSet.append(runningSum)
        #     return sumsSet
        
        # sumsSet1, sumsSet2 = getSumsSet(nums[:n//2]), getSumsSet(nums[n//2:])

        def getSumsSet(arr, i, set, sum):
            if i==len(arr): set.add(sum)
            else:
                getSumsSet(arr, i+1, set, sum)
                getSumsSet(arr, i+1, set, sum+arr[i])
        
        sumsSet1, sumsSet2 = set(), set()
        getSumsSet(nums[:n//2], 0, sumsSet1, 0)
        getSumsSet(nums[n//2:], 0, sumsSet2, 0)

        minDiff, sumsList1 = float('inf'), sorted(list(sumsSet1))
        for sum2 in sumsSet2:
            toSearchIn1 = goal - sum2
            index = bisect.bisect_left(sumsList1, toSearchIn1)
            for i in [index-1, index]:
                if 0<=i<len(sumsList1): minDiff = min(minDiff, abs(goal - sumsList1[i] - sum2))

        return minDiff