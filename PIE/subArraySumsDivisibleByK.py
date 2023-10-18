import bisect
class Solution:
    def subarraysDivByK(self, nums, k):
        mapOfRemaindersToIndices, cumulativeSum = {}, 0
        for index, num in enumerate(nums):
            cumulativeSum += num
            rem = cumulativeSum%k
            if not rem in mapOfRemaindersToIndices: 
                mapOfRemaindersToIndices[rem] = []
            mapOfRemaindersToIndices[rem].append(index)
        numSubArrays, cumulativeSum = 0, 0
        for index, num in enumerate(nums):
            rem = cumulativeSum%k
            if rem in mapOfRemaindersToIndices:
                numSubArrays += (len(mapOfRemaindersToIndices[rem]) - bisect.bisect_left(mapOfRemaindersToIndices[rem], index))
            cumulativeSum += num
        return numSubArrays

    def subarraysDivByK(self, nums, k):
        mapOfRemaindersToIndices, cumulativeSum, numSubArrays = {0:1}, 0, 0
        for num in nums:
            cumulativeSum += num
            cumulativeSum %= k
            if not cumulativeSum in mapOfRemaindersToIndices: 
                mapOfRemaindersToIndices[cumulativeSum] = 0
            else:
                numSubArrays += (mapOfRemaindersToIndices[cumulativeSum])
            mapOfRemaindersToIndices[cumulativeSum] += 1
        return numSubArrays